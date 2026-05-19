from flask import Flask, render_template, Response, request, jsonify
import cv2
import threading
import networkx as nx
import math
import os
import time

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))

rooms = {}
camera_caps = {}
G = nx.Graph()
model = None
monitoring_active = False
lock = threading.Lock()
latest_path_info = {"target": None, "path": [], "length": 0}

FIXED_POSITIONS = {
    "My Location": (60, 230),
    "Hallway_A": (240, 230),
    "Hallway_B": (460, 230),
}

ROOM_SLOT_POSITIONS = [
    (650, 80), (780, 80),
    (650, 180), (780, 180),
    (650, 280), (780, 280),
    (650, 380), (780, 380),
]

def load_model():
    global model
    from ultralytics import YOLO
    model = YOLO("yolo11x.pt")
    print("[INFO] YOLO model loaded.")

def count_people(frame):
    if model is None:
        return 0
    results = model(frame)
    count = 0
    for r in results:
        for box in r.boxes:
            if int(box.cls[0]) == 0:
                count += 1
    return count

def get_all_positions():
    pos = dict(FIXED_POSITIONS)
    for i, name in enumerate(sorted(rooms.keys())):
        if i < len(ROOM_SLOT_POSITIONS):
            pos[name] = ROOM_SLOT_POSITIONS[i]
    return pos

def rebuild_graph():
    global G
    G = nx.Graph()
    G.add_edge("My Location", "Hallway_A", weight=5)
    G.add_edge("Hallway_A", "Hallway_B", weight=15)
    for room in rooms:
        G.add_edge("Hallway_B", room, weight=10)

def euclidean(a, b):
    p = get_all_positions()
    c1, c2 = p.get(a, (0, 0)), p.get(b, (0, 0))
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def monitor_loop():
    global monitoring_active, latest_path_info
    while monitoring_active:
        with lock:
            rnames = list(rooms.keys())
        for room in rnames:
            cap = camera_caps.get(room)
            if cap and cap.isOpened():
                ret, frame = cap.read()
                if ret:
                    cnt = count_people(frame)
                    with lock:
                        if room in rooms:
                            rooms[room]["yolo_count"] = cnt
        with lock:
            available = [n for n, d in rooms.items() if d["yolo_count"] < int(d["area"])]
            if available:
                target = min(available, key=lambda r: euclidean("My Location", r))
                try:
                    path = nx.dijkstra_path(G, "My Location", target, weight="weight")
                    length = nx.dijkstra_path_length(G, "My Location", target, weight="weight")
                    latest_path_info = {"target": target, "path": path, "length": length}
                except Exception:
                    latest_path_info = {"target": None, "path": [], "length": 0}
            else:
                latest_path_info = {"target": None, "path": [], "length": 0}
        time.sleep(1)

def gen_frames(room_name):
    while True:
        cap = camera_caps.get(room_name)
        if not cap or not cap.isOpened():
            time.sleep(0.1)
            continue
        ret, frame = cap.read()
        if not ret:
            time.sleep(0.05)
            continue
        with lock:
            d = rooms.get(room_name, {})
            people = d.get("yolo_count", 0)
            capacity = int(d.get("area", 1))
            density = people / capacity if capacity > 0 else 0
        color = (0, 200, 0) if density < 0.7 else (0, 165, 255) if density < 1.0 else (0, 0, 255)
        cv2.rectangle(frame, (0, 0), (frame.shape[1], 60), (0, 0, 0), -1)
        cv2.putText(frame, f"{room_name}  {people}/{capacity}  ({density:.0%})",
                    (10, 40), cv2.FONT_HERSHEY_DUPLEX, 1, color, 2)
        _, buf = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 70])
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + buf.tobytes() + b'\r\n')
        time.sleep(0.033)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/setup", methods=["POST"])
def setup():
    global monitoring_active
    data = request.json
    monitoring_active = False
    time.sleep(0.5)
    with lock:
        for cap in camera_caps.values():
            cap.release()
        camera_caps.clear()
        rooms.clear()
    with lock:
        for i, r in enumerate(data.get("rooms", [])):
            name = f"Room_{i+1}"
            rooms[name] = {
                "coords": (float(r["x"]), float(r["y"])),
                "area": float(r["area"]),
                "yolo_count": 0,
                "camera_index": int(r.get("camera_index", i))
            }
            camera_caps[name] = cv2.VideoCapture(int(r.get("camera_index", i)))
    rebuild_graph()
    monitoring_active = True
    threading.Thread(target=monitor_loop, daemon=True).start()
    return jsonify({"status": "ok", "rooms": list(rooms.keys())})

@app.route("/status")
def status():
    with lock:
        room_data = {}
        for name, d in rooms.items():
            cap = int(d["area"])
            ppl = d["yolo_count"]
            dens = ppl / cap if cap > 0 else 0
            room_data[name] = {
                "people": ppl,
                "capacity": cap,
                "density": round(dens, 2),
                "status": "available" if ppl < cap else "full"
            }
        path_info = dict(latest_path_info)
    return jsonify({"rooms": room_data, "path": path_info})

@app.route("/graph")
def graph_data():
    with lock:
        positions = get_all_positions()
        nodes = []
        for node in G.nodes():
            is_room = node in rooms
            ppl = cap = dens = 0
            if is_room:
                d = rooms[node]
                cap = int(d["area"])
                ppl = d["yolo_count"]
                dens = ppl / cap if cap > 0 else 0
            x, y = positions.get(node, (0, 0))
            nodes.append({
                "id": node, "x": x, "y": y,
                "type": "room" if is_room else "hallway",
                "density": round(dens, 2), "people": ppl, "capacity": cap
            })
        edges = []
        for u, v, edata in G.edges(data=True):
            pu = positions.get(u, (0, 0))
            pv = positions.get(v, (0, 0))
            edges.append({
                "from": u, "to": v,
                "x1": pu[0], "y1": pu[1],
                "x2": pv[0], "y2": pv[1],
                "weight": edata.get("weight", 1)
            })
        path_info = dict(latest_path_info)
    return jsonify({"nodes": nodes, "edges": edges, "path": path_info})

@app.route("/video/<room_name>")
def video_feed(room_name):
    return Response(gen_frames(room_name), mimetype="multipart/x-mixed-replace; boundary=frame")

@app.route("/stop", methods=["POST"])
def stop():
    global monitoring_active
    monitoring_active = False
    with lock:
        for cap in camera_caps.values():
            cap.release()
    return jsonify({"status": "stopped"})

if __name__ == "__main__":
    load_model()
    app.run(debug=True, threaded=True, port=5000)