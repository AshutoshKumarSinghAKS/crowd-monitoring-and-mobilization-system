# 🚨 CrowdFlow — Crowd Monitoring and Mobilization System

A real-time **AI-powered crowd monitoring and mobilization system** designed to monitor crowd density across multiple rooms or areas, detect overcrowding using computer vision, and recommend less-crowded routes for safer movement.

The system uses **Python, Flask, OpenCV, YOLO, and NetworkX** to combine real-time camera monitoring with crowd analysis and route recommendation.

---

## 📌 Table of Contents

* [Overview](#-overview)
* [Problem Statement](#-problem-statement)
* [Objectives](#-objectives)
* [Key Features](#-key-features)
* [How the System Works](#-how-the-system-works)
* [Technology Stack](#-technology-stack)
* [Project Structure](#-project-structure)
* [Requirements](#-requirements)
* [Installation](#-installation)
* [Running the Project](#-running-the-project)
* [Configuration](#-configuration)
* [How to Use](#-how-to-use)
* [Crowd Density Calculation](#-crowd-density-calculation)
* [Route Recommendation](#-route-recommendation)
* [Camera Configuration](#-camera-configuration)
* [YOLO Model](#-yolo-model)
* [Troubleshooting](#-troubleshooting)
* [Future Enhancements](#-future-enhancements)
* [Use Cases](#-use-cases)
* [Limitations](#-limitations)
* [Contributing](#-contributing)
* [License](#-license)
* [Author](#-author)

---

# 📖 Overview

**CrowdFlow** is a computer-vision-based crowd monitoring system that helps monitor the number of people present in different areas in real time.

The application provides a web-based dashboard where users can configure multiple rooms/areas and associate each area with a camera. The system processes the camera feeds using **YOLO-based object detection** and displays the detected crowd information.

The system also represents rooms and their connections as a graph and uses **NetworkX** to determine a recommended route through less-crowded areas.

This type of system can be useful in environments where crowd congestion needs to be monitored and managed, such as:

* 🏫 Educational institutions
* 🏟️ Stadiums
* 🎪 Events and exhibitions
* 🛍️ Shopping centers
* 🏢 Large buildings
* 🚉 Transportation facilities
* 🛕 Religious places
* 🎭 Public gatherings

---

# 🎯 Problem Statement

Managing crowds manually can become difficult when multiple areas need to be monitored simultaneously.

Traditional monitoring generally depends on security personnel continuously watching multiple CCTV feeds. This can make it difficult to quickly identify overcrowded areas and determine where people should be redirected.

CrowdFlow attempts to address this problem by combining:

1. Real-time camera feeds
2. AI-based person detection
3. Crowd counting
4. Area capacity monitoring
5. Visual density indicators
6. Graph-based route recommendation

The goal is to provide a centralized dashboard that helps users understand the current crowd situation and make better movement decisions.

---

# 🎯 Objectives

The major objectives of this project are:

* Detect people from camera feeds using computer vision.
* Monitor multiple rooms/areas simultaneously.
* Estimate the current crowd level of each area.
* Compare crowd count against the configured capacity.
* Identify areas approaching or reaching capacity.
* Represent connected areas as a graph.
* Recommend a less-crowded route.
* Provide a simple web-based monitoring dashboard.
* Make the system configurable for different building layouts.

---

# 🚀 Key Features

## 1. 👥 Real-Time Crowd Monitoring

The system processes camera feeds and detects people using a YOLO-based object detection model.

The detected people are counted to estimate the current occupancy of an area.

---

## 2. 📹 Multiple Camera Support

Different rooms or areas can be associated with different camera indexes.

For example:

```text
Camera 0 → Room 1
Camera 1 → Room 2
Camera 2 → Room 3
```

The dashboard can display multiple camera feeds in a grid.

---

## 3. 🏢 Room/Area Configuration

Users can configure the number of rooms using the dashboard.

Each room can have information such as:

* Area
* Camera Index
* X coordinate
* Y coordinate

The area value is used as the capacity ceiling in the current implementation.

---

## 4. 📊 Crowd Density Monitoring

The system compares the detected crowd count with the configured capacity.

The dashboard provides a visual indication of crowd density.

Current density states are:

```text
Green   → Below 70%
Orange  → 70%–100%
Red     → Full
```

---

## 5. 🧠 AI-Based Person Detection

The system uses the **YOLO object detection model** through the Ultralytics library.

The model analyzes camera frames and identifies people present in the monitored area.

---

## 6. 🗺️ Graph-Based Route Recommendation

Rooms/areas can be represented as nodes in a graph.

Connections between areas represent possible movement paths.

NetworkX is used to work with the graph and determine a recommended route based on crowd conditions.

The dashboard displays a **Recommended Route** based on the least-crowded available path.

---

## 7. 🌐 Web-Based Dashboard

The application uses Flask to provide a web interface.

The dashboard allows users to:

* Configure rooms
* Configure camera indexes
* Enter room information
* Start monitoring
* View camera feeds
* Monitor crowd levels
* View recommended routes

---

## 8. 🧪 UI Testing Without the YOLO Model

If the YOLO model is not available, the application can still run with a zero-count/mock detection behavior for testing the user interface.

This allows developers to test the dashboard without immediately configuring the complete AI model.

---

# ⚙️ How the System Works

The overall workflow is:

```text
Camera Feed
     ↓
OpenCV
     ↓
Frame Processing
     ↓
YOLO Object Detection
     ↓
Person Detection
     ↓
Crowd Count
     ↓
Capacity Comparison
     ↓
Density Calculation
     ↓
Crowd Status
     ↓
Graph / Route Analysis
     ↓
Recommended Route
     ↓
Flask Web Dashboard
```

---

# 🛠️ Technology Stack

| Technology       | Purpose                     |
| ---------------- | --------------------------- |
| Python           | Core programming language   |
| Flask            | Web application/backend     |
| OpenCV           | Camera and video processing |
| Ultralytics YOLO | Person/object detection     |
| NetworkX         | Graph and route processing  |
| HTML             | Dashboard structure         |
| CSS              | Dashboard styling           |
| JavaScript       | Frontend interactions       |

---

# 📁 Project Structure

The current repository follows a simple Flask project structure:

```text
crowd-monitoring-and-mobilization-system/
│
├── app.py
│
├── templates/
│   └── index.html
│
├── requirements.txt
│
└── README.md
```

### `app.py`

Main Flask application.

It handles the application logic, camera processing, crowd monitoring, and route-related functionality.

### `templates/index.html`

Contains the web dashboard/interface used to configure and monitor the system.

### `requirements.txt`

Contains the Python dependencies required to run the project.

### `README.md`

Project documentation and setup instructions.

---

# 💻 Requirements

Before running the project, make sure you have:

* Python 3.9 or later
* pip
* Webcam or compatible camera
* Internet connection for installing dependencies
* Modern web browser

For AI-based detection, you also need the YOLO model file used by the application.

---

# 📥 Installation

## Step 1 — Clone the Repository

Open Command Prompt, PowerShell, or a terminal:

```bash
git clone https://github.com/tripthiprashant/crowd-monitoring-and-mobilization-system.git
```

Move into the project directory:

```bash
cd crowd-monitoring-and-mobilization-system
```

---

# 🐍 Step 2 — Create a Virtual Environment

Creating a virtual environment is recommended so that project dependencies remain isolated.

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

If PowerShell blocks the activation script, you can use:

```powershell
.\venv\Scripts\Activate.ps1
```

### macOS/Linux

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

After activation, you should see something similar to:

```text
(venv)
```

at the beginning of your terminal prompt.

---

# 📦 Step 3 — Install Dependencies

Install the dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

If you want to install the main dependencies manually:

```bash
pip install flask opencv-python ultralytics networkx
```

---

# 🧠 Step 4 — Add the YOLO Model

Place the required YOLO model file in the same directory as `app.py`.

For example:

```text
crowd-monitoring-and-mobilization-system/
│
├── app.py
├── yolo11x.pt
├── requirements.txt
│
└── templates/
    └── index.html
```

The current project documentation expects:

```text
yolo11x.pt
```

to be placed next to `app.py`.

---

# ▶️ Running the Project

After installing the dependencies and configuring the model, run:

```bash
python app.py
```

If the application starts successfully, Flask will provide a local address.

Open your browser and visit:

```text
http://localhost:5000
```

You can also typically use:

```text
http://127.0.0.1:5000
```

---

# 🖥️ How to Use the Application

After opening the dashboard:

### Step 1 — Configure Number of Rooms

Use the `+` and `−` controls to configure the number of rooms/areas.

---

### Step 2 — Configure Each Room

Provide information for each room.

Example:

```text
Room: Room 1
Area: 100
Camera Index: 0
X Coordinate: 100
Y Coordinate: 150
```

---

### Step 3 — Configure Camera

Set the camera index.

Common examples:

```text
0 → Built-in/default webcam
1 → Second camera
2 → Third camera
```

The exact camera index depends on the cameras connected to your computer.

---

### Step 4 — Start Monitoring

Click:

```text
▶ Start Monitoring
```

The system will begin processing the configured camera feeds.

---

### Step 5 — Monitor Crowd Levels

The dashboard displays the camera feeds and crowd information.

The system calculates the crowd level relative to the configured capacity.

---

### Step 6 — Follow the Recommended Route

The system updates the recommended route according to the crowd conditions of the monitored areas.

The objective is to direct movement toward a less-crowded path.

---

# 📊 Crowd Density Calculation

The system uses the detected number of people and configured capacity to determine crowd utilization.

Conceptually:

```text
Density (%) = (Detected People / Capacity) × 100
```

For example:

```text
Capacity = 100
Detected People = 60

Density = (60 / 100) × 100
        = 60%
```

The dashboard can therefore classify the area as:

```text
< 70%       → Low/Normal
70–100%     → High
100%        → Full
```

---

# 🗺️ Route Recommendation

One of the important components of CrowdFlow is its graph-based movement recommendation.

Each room/area can be treated as a node:

```text
Room A
  |
Room B
  |
Room C
```

Connections between rooms represent possible movement paths.

NetworkX can then be used to analyze the graph and determine a route.

The crowd level can influence route selection so that a less-crowded path can be recommended.

Example:

```text
Entrance
   |
   +------ Room A ------+
   |                    |
   |                    |
   +------ Room B ------+---- Exit
            ↑
       Less crowded
```

The system can therefore recommend movement through areas with lower crowd levels.

---

# 📹 Camera Configuration

OpenCV uses camera indexes to access connected cameras.

A typical configuration is:

```text
Camera 0 → Laptop webcam
Camera 1 → External USB camera
Camera 2 → Another connected camera
```

If your webcam does not work with:

```text
0
```

try:

```text
1
```

or:

```text
2
```

depending on your hardware.

---

# 🧠 YOLO Model

The project uses a YOLO model through the **Ultralytics** library for object detection.

The model analyzes frames from the camera and identifies detected objects.

For crowd monitoring, the important detection category is:

```text
person
```

The detected people are then counted to estimate the current crowd level.

> **Note:** The exact model file must match the model expected by the current application configuration. The repository's current README specifies `yolo11x.pt`.

---

# 🧪 Testing Without the Model

For interface testing, the current implementation can still run when the YOLO model is unavailable by using a zero-count/mock behavior.

This is useful when you want to:

* Test the dashboard
* Check room configuration
* Test frontend interactions
* Verify Flask application startup
* Develop the UI before configuring AI detection

However, actual person detection requires the appropriate YOLO model.

---

# 🐛 Troubleshooting

## Problem 1 — `ModuleNotFoundError`

Example:

```text
ModuleNotFoundError: No module named 'flask'
```

Solution:

Make sure your virtual environment is activated and run:

```bash
pip install -r requirements.txt
```

---

## Problem 2 — Camera Not Opening

Try another camera index:

```text
0
1
2
```

Also make sure:

* Your camera is connected.
* Another application is not exclusively using the camera.
* Camera permissions are enabled in Windows.
* The selected camera index is correct.

---

## Problem 3 — YOLO Model Not Found

If you receive a model-related error, check that the required model file exists in the project directory.

Example:

```text
app.py
yolo11x.pt
```

The model filename should match the filename expected by the application.

---

## Problem 4 — Port Already in Use

If port `5000` is already being used, stop the other Flask application/process or configure the application to use another port.

For example:

```text
http://localhost:5001
```

depending on the application's configuration.

---

## Problem 5 — Slow Detection

YOLO inference can require significant computational resources.

If detection is slow:

* Use a smaller YOLO model.
* Reduce camera resolution.
* Process fewer frames.
* Use GPU acceleration if available.
* Reduce the number of simultaneous camera feeds.

---

# 🔮 Future Enhancements

The current project can be significantly improved in future versions.

## 1. 📈 Advanced Crowd Analytics

Add historical crowd data and analytics such as:

* Crowd count over time
* Peak crowd hours
* Average occupancy
* Room utilization
* Daily/weekly reports
* Crowd trends

Example:

```text
Time       People
10:00      35
10:30      48
11:00      72
11:30      91
12:00      105
```

---

## 2. 🚨 Automatic Overcrowding Alerts

Introduce real-time alerts when crowd density exceeds a configured threshold.

Possible alert mechanisms:

* Dashboard notification
* Sound alert
* Email notification
* SMS notification
* Push notification

Example:

```text
⚠️ ALERT

Room 3 has exceeded its safe capacity.
Current Crowd: 105
Capacity: 100
```

---

## 3. 🔥 Crowd Heatmaps

Generate visual heatmaps showing areas with high crowd density.

Example:

```text
Low Density       ███
Medium Density    ██████
High Density      ██████████
```

This would make it easier for administrators to identify congestion zones.

---

## 4. 👤 Person Tracking

Instead of only detecting people in individual frames, integrate object tracking.

Possible technologies include:

* YOLO tracking
* ByteTrack
* DeepSORT

This can help analyze:

* Movement patterns
* Entry/exit flow
* Direction of movement
* Approximate dwell time

---

## 5. 🚪 Entry and Exit Counting

Add virtual lines at entrances and exits.

The system could calculate:

```text
People Entered
People Exited
Current Occupancy
```

This would provide more accurate occupancy information.

---

## 6. 🗺️ Interactive Building Map

Replace manually configured coordinates with an interactive map.

Administrators could visually create:

```text
Entrance → Room A → Room B → Exit
```

and define connections using the dashboard.

---

## 7. 📱 Mobile-Friendly Dashboard

Improve the frontend so that administrators can monitor the system from:

* Smartphones
* Tablets
* Laptops
* Desktop computers

---

## 8. ☁️ Cloud Deployment

Deploy the application to a cloud platform so that authorized users can monitor the system remotely.

Possible future architecture:

```text
CCTV Cameras
      ↓
AI Processing Server
      ↓
Backend API
      ↓
Cloud Database
      ↓
Web Dashboard
      ↓
Administrator
```

---

## 9. 🗄️ Database Integration

Add a database to store:

* Crowd counts
* Room information
* Camera configurations
* Alerts
* Historical analytics
* Monitoring sessions

Potential database options include:

* PostgreSQL
* MySQL
* MongoDB

---

## 10. 🔐 Authentication and Authorization

Add secure login functionality for administrators and monitoring staff.

Possible roles:

```text
Admin
  ↓
Full system control

Security Staff
  ↓
Monitoring + alerts

Viewer
  ↓
Read-only dashboard
```

---

## 11. 🤖 Improved Crowd Prediction

Instead of only detecting the current crowd, future versions could predict crowd levels.

For example:

```text
Current Crowd: 75

Predicted after 10 min: 92
Predicted after 20 min: 110

⚠️ Possible overcrowding
```

Machine learning models could be trained using historical crowd data.

---

## 12. 📡 IP Camera / CCTV Integration

Currently, the system can work with camera indexes.

A future version could support:

* IP cameras
* RTSP streams
* CCTV systems
* Network cameras

This would make the project more suitable for real-world deployment.

---

## 13. 📊 Admin Analytics Dashboard

A more advanced dashboard could include:

* Live crowd count
* Total monitored areas
* Most crowded room
* Least crowded room
* Active alerts
* Historical graphs
* Camera status
* Recommended routes

---

# 🏢 Potential Use Cases

CrowdFlow can potentially be adapted for:

### 🏫 Colleges and Universities

Monitor:

* Corridors
* Classrooms
* Cafeterias
* Entrances
* Auditoriums

---

### 🏟️ Stadiums

Monitor:

* Entry gates
* Exit gates
* Seating areas
* Corridors
* Emergency routes

---

### 🛕 Religious Places

Monitor:

* Entry points
* Waiting areas
* Main halls
* Exit routes

---

### 🎪 Events

Monitor:

* Event halls
* Entry gates
* Food areas
* Exhibition areas
* Emergency exits

---

### 🚉 Transportation Facilities

Monitor:

* Platforms
* Waiting areas
* Ticket counters
* Entry/exit points

---

# ⚠️ Limitations

The current project is a prototype and has several limitations.

* Detection accuracy depends on the selected YOLO model.
* Camera quality can affect detection.
* Poor lighting may reduce detection accuracy.
* Heavy crowd occlusion can make person detection difficult.
* Multiple high-resolution camera feeds may require significant computational resources.
* Camera indexes depend on the local machine.
* The current capacity model uses the configured area value as the capacity ceiling.
* The current project does not yet provide persistent historical analytics or a production database.
* Route recommendation depends on the configured room/graph information.

These limitations can be addressed through the future enhancements described above.

---

# 🔒 Privacy and Responsible Use

Because the project processes camera footage, real-world deployments should consider privacy and security requirements.

When deploying such a system:

* Use cameras only where legally permitted.
* Avoid unnecessary storage of raw video.
* Protect collected data.
* Restrict dashboard access to authorized users.
* Follow applicable privacy and data-protection regulations.
* Clearly communicate surveillance practices where required.

---

# 🤝 Contributing

Contributions and improvements are welcome.

### 1. Fork the repository

```bash
git fork https://github.com/tripthiprashant/crowd-monitoring-and-mobilization-system.git
```

### 2. Clone your fork

```bash
git clone <your-fork-url>
```

### 3. Create a new branch

```bash
git checkout -b feature/new-feature
```

### 4. Make your changes

Implement and test your changes locally.

### 5. Commit your changes

```bash
git add .
git commit -m "Add new crowd monitoring feature"
```

### 6. Push your branch

```bash
git push origin feature/new-feature
```

### 7. Create a Pull Request

Open a Pull Request on GitHub with a description of your changes.

---

# 📄 License

If you have not yet added a license to the repository, you should add one before publishing the project for broader open-source use.

For example, you can use the **MIT License** if it matches your intended project usage.

---

# 👨‍💻 Author

**Prashant Pratap Tripathi**

B.Tech. Computer Science and Engineering

GitHub:
https://github.com/tripthiprashant

---

# ⭐ Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.

**Repository:**

https://github.com/tripthiprashant/crowd-monitoring-and-mobilization-system

---

## 🚀 Future Vision

CrowdFlow can evolve from a simple crowd-monitoring prototype into a complete **AI-powered crowd safety and management platform**.

The long-term architecture could combine:

```text
             CCTV / IP Cameras
                     ↓
             Computer Vision
                     ↓
          YOLO Person Detection
                     ↓
             Crowd Analytics
                     ↓
        ┌────────────┴────────────┐
        ↓                         ↓
   Alert System             Route Engine
        ↓                         ↓
        └────────────┬────────────┘
                     ↓
             Backend / Database
                     ↓
             Admin Dashboard
                     ↓
              Decision Making
```

The ultimate goal is to help administrators **detect congestion early, understand crowd movement, and guide people toward safer and less-crowded routes.**

```

This version is based on what is actually visible in your current repository—`app.py`, `templates/index.html`, `requirements.txt`, Flask setup, YOLO model configuration, camera indexes, density thresholds, and NetworkX route recommendation.

You can also open your [Crowd Monitoring GitHub repository](https://github.com/tripthiprashant/crowd-monitoring-and-mobilization-system?utm_source=chatgpt.com) and replace the existing `README.md` with the above.
```
