# 🚌 UrbanSight AI — Autonomous Mobile Urban Intelligence Platform
> **Infothon 7.0 · Vidyavardhaka College of Engineering (VVCE), Mysuru**  
> **Problem Statement:** PS #07 | **Ref:** SIH26124 | **Track:** Smart Cities & Mobility (Agentic AI)

[![Infothon 7.0](https://img.shields.io/badge/Hackathon-Infothon%207.0-003580.svg)](https://vvce.ac.in)
[![Track](https://img.shields.io/badge/Track-Smart%20Cities%20%26%20Mobility-138808.svg)](#)
[![Python](https://img.shields.io/badge/Python-3.13-3776AB.svg?logo=python)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688.svg?logo=fastapi)](https://fastapi.tiangolo.com)
[![YOLOv8](https://img.shields.io/badge/AI%20Vision-YOLOv8%20Nano-FF9933.svg)](#)
[![Tests Passing](https://img.shields.io/badge/Tests-289%20%2F%20289%20Passing-brightgreen.svg)](#)
[![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)](#)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-0284C7.svg)](https://gaganks2006-ind.github.io/urbansight-ai/)

---

## 🌐 Live Interactive Portals & Demos

All 5 core civic stakeholder portals run seamlessly in any modern browser without requiring app store installation:

| Component | Live Portal Link | Description |
| :--- | :--- | :--- |
| 🏙️ **Smart City ICCC Command Center** | [**Live Command Dashboard**](https://gaganks2006-ind.github.io/urbansight-ai/) | Real-time Leaflet GIS tracking across Mysuru (VVCE Ring Road, Gokulam, Hunsur Road) and Bengaluru ORR. Real-time video inspection player with YOLOv8 optical inference, bounding boxes, depth estimation, and instant work-order dispatch. |
| 🚌 **In-Cab Driver HUD Console** | [**Live Driver HUD**](https://gaganks2006-ind.github.io/urbansight-ai/driver_console.html) | Tablet HUD for transit bus drivers featuring an animated CAN-BUS speedometer, dynamic hazard advisory card, audio chime alerts, lane merge recommendations, and road smoothness index. |
| 📱 **Mobile Navigation Proximity Overlay** | [**Live Navigation Overlay**](https://gaganks2006-ind.github.io/urbansight-ai/nav_overlay.html) | Mobile floating overlay designed for commuter and driver phones. Features an interactive **"Simulate Driving Along Mysuru Ring Road"** mode with turn-by-turn proximity voice advisories. |
| 👥 **Citizen Road Repair Tracker** | [**Live Citizen Portal**](https://gaganks2006-ind.github.io/urbansight-ai/citizen_portal.html) | Transparent public portal tracking repair milestones from initial camera sighting to field crew patch. Includes the **Adopt-a-Road Citizen Rewards Club** with anti-spam zero-trust verification. |
| 🛠️ **Mobile Field Crew PWA** | [**Live Field Crew PWA**](https://gaganks2006-ind.github.io/urbansight-ai/field_crew.html) | Fast mobile web app for PWD rapid repair vans. Displays prioritized work orders, Google Maps turn-by-turn navigation, before/after audit photos, and one-click completion sign-off. |
| 📄 **CPWD Statutory Tender Voucher & AI Cost Audit** | [**Live CPWD Voucher**](https://gaganks2006-ind.github.io/urbansight-ai/voucher.html?ticket=PWD-OCT-0941) | Official civil engineering tender voucher with itemized **CPWD Schedule of Rates (SOR 2023)** breakdown, non-hallucinated volumetric rate math, Gemini cost auditing, and e-RUPI payment barcode. |

---

## 📌 Executive Summary

**UrbanSight AI** transforms everyday municipal public transit fleets (city buses) into real-time, edge-intelligent road perception grids. By processing windshield dashcam video feeds on-device, UrbanSight autonomously detects road surface distress (potholes, cracks, waterlogging) in real time, clusters recurring passes, and auto-dispatches geotagged PWD repair orders with CPWD engineering cost estimates—with **zero new municipal hardware CapEx**.

```
┌────────────────────────────────────────────────────────────────────────┐
│ 1. TRANSIT EDGE SENSING (KSRTC & BMTC e-Bus Fleets)                    │
│    Windshield Optical Dashcam (1080p 30 FPS) + Phone/IMU Sensor Fusion │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ In-Memory Video Frames
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ 2. ON-DEVICE EDGE PERCEPTION (YOLOv8 Nano Engine)                      │
│    • Real-time classification: Potholes (D40), Cracks (D00), Flooding  │
│    • DPDP Act 2023 §2(t) Privacy: On-chip in-memory face/plate masking │
│    • Depth & Severity Estimation: Volumetric math + IRI roughness      │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Lightweight Geohash Payload (<12 KB)
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ 3. MULTI-AGENT CLOUD ORCHESTRATION & TRIAGE                            │
│    • Spatial Clustering (DBSCAN): Merges duplicate sightings into 1 ID │
│    • Packet Header De-duplication: Drops redundant bursts on high-freq │
│    • Gemini / CPWD Civil Rate Engine: Itemized volume-based SOR audit  │
└─────────────────┬────────────────────────────────────┬─────────────────┘
                  │ Validated Work Order               │ High-Priority Hazard
                  ▼                                    ▼
┌─────────────────────────────────┐  ┌───────────────────────────────────┐
│ PWD FIELD CREW & CITIZEN PORTAL │  │ DRIVER HUD & NAVIGATION OVERLAY   │
│ • Geotagged Van Dispatch Queue  │  │ • 300m Forward Radar Warning      │
│ • Before / After Photo Audit    │  │ • Lane Merge Recommendation       │
│ • CPWD Statutory Tender Voucher │  │ • Proximity Speech Audio Alert    │
└─────────────────────────────────┘  └───────────────────────────────────┘
```

---

## 🧠 Key Technical Innovations

### 1. Gemini-Powered CPWD Civil Engineering Cost Audit
To eliminate arbitrary hallucinations in repair costing, UrbanSight incorporates an exact civil engineering rate formula verified against the **CPWD Schedule of Rates (SOR 2023)**:
$$\text{Compacted Asphalt Volume } (V) = \text{Length} \times \text{Width} \times \text{Depth} \times 1.25 \text{ (Compaction Factor)}$$
$$\text{Base Material Cost} = V \times \text{CPWD SOR Rate (Item 16.14.2: ₹7,850/m³ for Dense Bituminous Macadam)}$$
$$\text{Total Sanctioned Cost} = \text{Base Cost} + \text{Tack Coat (16.2.1)} + \text{Labour \& Roller Equipment} + 18\% \text{ GST}$$
Available via REST endpoint: `GET /api/work-orders/{ticket_id}/ai-cost-audit`.

### 2. High-Density Network Packet Header Optimization
When 100+ public transit vehicles travel the same busy corridor, naive cloud reporting would flood central servers with duplicate telemetry. UrbanSight solves this via **Smart Packet Header De-duplication**:
- **Spatial Geohash-7 Header:** Each edge packet carries an 8-character spatial geohash in its HTTP/MQTT header (`X-Distress-Geohash: tdrt3u8q`).
- **Cloud Gateway Cache Filter:** The API gateway evaluates the header in $O(1)$ memory without unmarshaling the JSON body. If that geohash was acknowledged within the last 15 minutes, the payload is counted as a frequency confidence increment without invoking downstream clustering pipelines.

### 3. DPDP Act 2023 §2(t) In-Memory Privacy Redaction
To strictly comply with the **Digital Personal Data Protection (DPDP) Act 2023**, optical frames are processed strictly in RAM buffers. Pedestrian faces and vehicle license plates are irreversibly Gaussian-blurred before any telemetry is dispatched. Zero raw video frames are persisted to disk.

### 4. Dual-Mode Mobile Navigation Proximity Engine
Provides a REST endpoint (`POST /api/nav/proximity-check`) that calculates distance to known road hazards along the driver's heading vector and returns immediate lane recommendations (*"Merge to Left Lane — Critical Pothole in 280m"*). Includes an interactive simulated driving mode along the **Mysuru Outer Ring Road Corridor** with automated Web Speech synthesis.

---

## 📂 Repository Organization

```
Infothon 7.0/
├── backend/                  # FastAPI Core Backend Services
│   ├── main.py               # REST API, Work Orders, AI Cost Audit & Nav Proximity
│   ├── models.py             # Pydantic v2 Telemetry & Work Order Schemas
│   └── simulated_data.py     # Grounded Mysuru & Bengaluru Transit Corridors
├── templates/                # Jinja2 Templates for FastAPI Server
│   ├── index.html            # ICCC Command Center Dashboard
│   ├── driver_console.html   # Driver In-Cab HUD
│   ├── nav_overlay.html      # Mobile Navigation Proximity Overlay
│   ├── citizen_portal.html   # Citizen Grievance Resolution & Rewards Tracker
│   ├── field_crew.html       # PWD Field Crew Resolution PWA
│   └── voucher.html          # CPWD Statutory Tender Voucher
├── static/                   # Static Assets & Styling
│   ├── css/style.css         # Unified Design System (Noto Sans, NIC Blue)
│   ├── js/app.js             # Client SPA State Management & GIS Map Logic
│   └── videos/               # Real Mysuru Road Inspection Footage (.mp4)
├── distributed/              # Edge Bus Telemetry & Streaming Benchmarks
│   ├── edge_bus_node.py      # Edge Bus Node Emulator
│   └── video_edge_streamer.py# Video Frame Perception Pipe
├── tests/                    # Comprehensive Test Suite (289 Passing Tests)
│   ├── test_pipeline.py      # Work Orders, Clustering, Cost Audit & API Tests
│   ├── test_vision_cv.py     # YOLOv8 Optical Inference & DPDP Redaction Tests
│   ├── test_adversarial_cv.py# Edge Lighting, Blur & Weather Robustness Tests
│   ├── test_fleet_stress.py  # Fleet Scale & Network Packet Header Tests
│   └── test_e2e_suite.py     # Full End-to-End Civic Handoff Workflow Tests
├── index.html                # GitHub Pages Standalone Entry Point
├── driver_console.html       # GitHub Pages Standalone Driver HUD
├── nav_overlay.html          # GitHub Pages Standalone Navigation Overlay
├── citizen_portal.html       # GitHub Pages Standalone Citizen Portal
├── field_crew.html           # GitHub Pages Standalone Field Crew PWA
├── voucher.html              # GitHub Pages Standalone CPWD Voucher
├── requirements.txt          # Python Package Dependencies
└── README.md                 # Project Master Documentation
```

---

## 🛠️ Technology Stack

| Layer | Tools & Technologies | Role in Platform |
| :--- | :--- | :--- |
| **Edge Perception** | YOLOv8-Nano / OpenCV | Real-time road distress inference at 30 FPS with in-memory DPDP privacy blur |
| **Backend API** | FastAPI (ASGI), Python 3.13, Pydantic v2 | High-throughput asynchronous REST & telemetry orchestration |
| **Civil Cost Engine** | Google Gemini API + CPWD SOR 2023 | Non-hallucinated volumetric asphalt repair costing & engineering audits |
| **Spatial GIS** | Leaflet.js, Turf.js, Haversine Geodesic | Sub-second GIS map rendering, hazard pin clustering, and proximity checks |
| **Navigation** | HTML5 Geolocation, Web Speech API | Floating HUD overlay with turn-by-turn driving alerts |
| **Testing** | pytest, pytest-asyncio, HTTPX | **289 rigorous automated unit, performance, and integration tests** |
| **Cloud Deployment** | GitHub Pages (SPA) / Docker / ASGI | Instant evaluation without local installation requirements |

---

## ⚡ Quickstart & Local Setup

### 1. Clone & Set Up Environment
```bash
# Clone the repository
git clone https://github.com/gaganks2006-ind/urbansight-ai.git
cd urbansight-ai

# Create virtual environment
python -m venv venv
venv\Scripts\activate       # On Windows
# source venv/bin/activate  # On Linux / macOS

# Install dependencies
pip install -r requirements.txt
```

### 2. Launch Backend Server
```bash
uvicorn backend.main:app --reload --port 8000
```
Open **`http://127.0.0.1:8000`** in your browser.

### 3. Run Test Suite
```bash
python -m pytest "Infothon 7.0/tests" -v
```
All **289 tests** should pass in ~11 seconds.

---

## 📡 REST API Reference

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/api/health` | `GET` | Health check endpoint returning backend status and operational mode. |
| `/api/work-orders` | `GET` | Returns all active PWD repair work orders with severity, GPS coordinates, and SLA status. |
| `/api/work-orders/{ticket_id}` | `GET` | Returns full engineering details for a specific municipal repair work order. |
| `/api/work-orders/{ticket_id}/ai-cost-audit` | `GET` | Executes Gemini/CPWD volumetric cost audit and returns non-hallucinated SOR rate analysis. |
| `/api/work-orders/{ticket_id}/status` | `PATCH` | Updates work-order status (`IN_PROGRESS`, `RESOLVED`) with field crew telemetry. |
| `/api/nav/proximity-check` | `POST` | Calculates proximity to hazards along a coordinate vector and returns lane guidance. |
| `/api/simulate-detection` | `POST` | Triggers a simulated multi-agent transit bus detection pipeline event for evaluation. |

---

## 👥 Hackathon Credentials
- **Event:** **Infothon 7.0 (2026)**
- **Venue:** Department of Information Science and Engineering, **Vidyavardhaka College of Engineering (VVCE)**, Mysuru – 570002
- **Lead Developer & Architect:** Gagan K S
- **Repository Remotes:**
  - `origin`: `https://github.com/gaganks2006-ind/urbansight-ai.git`
  - `infothon`: `https://github.com/Infothon-7-0/AGENTIC-AI-05-EcoLogic.git`

---

## 📜 License
Distributed under the **MIT License**. Developed exclusively for **Infothon 7.0**.
Special acknowledgment to the **Mysuru City Corporation (MCC)**, **BBMP**, and the **Ministry of Housing and Urban Affairs (MoHUA)** open transit initiatives.
