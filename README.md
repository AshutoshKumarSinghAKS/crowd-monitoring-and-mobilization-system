# CrowdFlow — Crowd Mobilising System

## Project Structure
```
crowd_system/
├── app.py                  ← Flask backend (run this)
├── templates/
│   └── index.html          ← Frontend dashboard
└── requirements.txt
```

## Setup & Run

### 1. Install dependencies
```bash
pip install flask opencv-python ultralytics networkx
```

### 2. Place your YOLO model
Put `yolo11x.pt` in the same folder as `app.py`.

### 3. Run Flask
```bash
python app.py
```

### 4. Open browser
Visit → http://localhost:5000

---

## How to Use

1. **Set number of rooms** using the +/− buttons in the sidebar
2. **Fill in each room's details:**
   - **Area (m²)** — used as the capacity ceiling
   - **Camera Index** — 0 = first webcam, 1 = second, etc.
   - **X / Y Coords** — position on your building map
3. Click **▶ Start Monitoring**
4. Live camera feeds appear in the dashboard grid
5. The **Recommended Route** banner auto-updates with the least-crowded room path

---

## Notes
- If YOLO model is missing, the system still runs with 0-count mock (for UI testing)
- Camera Index 0 is usually your built-in webcam; USB cameras are 1, 2, …
- Density bar: Green < 70% · Orange 70–100% · Red = Full
