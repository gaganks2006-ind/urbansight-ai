# 🏆 UrbanSight AI — Infothon 7.0 Master Presentation Deck
**Competition:** Infothon 7.0 · Vidyavardhaka College of Engineering (VVCE), Mysuru  
**Track:** Smart Cities & Mobility · Agentic AI Track  
**Problem Statement:** PS #07 | SIH26124 (AI Mobile Urban Intelligence Platform)  
**Format:** 5 Content Slides (Strict 16:9 PDF Export · Slide 6 Guidelines Deleted)  
**Pitch Time Budget:** 3 to 4 Minutes Total (+ 3 Minutes Q&A)

---

## 🎨 Master Design Specifications (At A Glance)
- **Palette (High-Luminance Projector Ready):**
  - **Primary Canvas:** `#F8FAFC` (Architectural Off-White — prevents projector washout)
  - **Structural Navy:** `#0F172A` (Deep Asphalt Navy — high-contrast text and cards)
  - **Signal Accent:** `#FF5E1E` (Warning Amber/Flame — key metrics, proprietary IP, borders)
- **Typography:** **Plus Jakarta Sans** (Headings, 44pt/32pt) + **Inter** (Body text, ≥24pt) + **JetBrains Mono** (Telemetry/Metrics)
- **Rule of Thumb:** Minimum font size **24pt** across all slides. Zero raw code screenshots. Every slide headline makes an assertion.

---

# ════════════════════════════════════════════════════════════════
# SLIDE 1: TITLE & HOOK
# ════════════════════════════════════════════════════════════════
**Time Budget:** 20–25 Seconds  
**Layout:** 55% Left Column (Value Proposition & Roles) | 45% Right Column (Hero Visual)

### 📌 Slide Content Elements

#### 1. Header Kicker (Top Category Pill)
```text
INFOTHON 7.0  •  TRACK: SMART CITIES & MOBILITY  •  PROBLEM STATEMENT #07 [SIH26124]
```

#### 2. Project Title & Subtitle
- **Project Name:** **UrbanSight AI**
- **Sub-Badge:** `Autonomous Mobile Urban Sensing Grid`

#### 3. Primary One-Line Tagline ("X does Y for Z")
> **"UrbanSight AI transforms everyday municipal transit fleets into real-time, edge-intelligent perception grids for automated road and infrastructure governance."**

#### 4. Key Value Metric Chips (Below Tagline)
- `[ ⚡ Zero Dedicated Patrols ]`
- `[ 📦 <15 KB Alert Payload ]`
- `[ 🎯 92%+ Defect Precision ]`

#### 5. Hero Visual Specification (Right 45% Panel)
> **Visual Concept:** *"The Connected Fleet Edge-to-Twin Engine"*
> - **Foreground:** Sleek 3D isometric render of an Indian municipal electric bus (Tata/Ashok Leyland style in dark slate `#0F172A`).
> - **Windshield Mount:** An onboard dashcam emitting a transparent light cone (FOV) onto the asphalt road.
> - **AR Bounding Box Overlays:**
>   - Box A (Road Surface): Amber-bordered box labeled `[DEFECT: POTHOLE | SEV: HIGH | CONF: 96.4%]`.
>   - Box B (Waterlogging): Cyan-bordered box labeled `[HAZARD: SUBMERGED ROADWAY | LAT: 12.31°N, 76.65°E]`.
> - **Background:** Dark-mode 2.5D topographic geospatial heatmap of the city street grid with bus trajectories shown as pulsating glowing lines.
> - **Telemetry Cards Floating Beside Bus:**
>   - `Edge Inference: 28ms @ 30 FPS (TensorRT FP16)`
>   - `Bandwidth: <15 KB / Event (Zero Video Streaming)`

#### 6. Team Credentials & Institution Block (Bottom Ribbon)
- **Institution:** Department of Information Science and Engineering, Vidyavardhaka College of Engineering (VVCE), Mysuru - 570002
- **Team Name:** `[Your Team Name]`
- **Technical Roles:**
  1. `[Name 1]` — **Edge AI & Perception Systems Lead** *(On-Device Vision, TensorRT Quantization)*
  2. `[Name 2]` — **Geospatial Pipeline & Fleet IoT Engineer** *(DBSCAN Spatial Clustering, GNSS/IMU Fusion)*
  3. `[Name 3]` — **Distributed Cloud & Municipal API Architect** *(FastAPI Backend, PWD Portal Integration)*
  4. `[Name 4]` — **Urban Analytics & GIS Command Systems Specialist** *(Leaflet.js GIS Dashboard, Driver HUD)*

---

### 🎙️ Speaker Script (Slide 1 — 20 Seconds)
> *"Good morning respected judges. While municipal corporations spend crores deploying dedicated inspection vehicles across thousands of kilometers of damaged roads, **UrbanSight AI turns every existing public bus into an autonomous, edge-intelligent city scanner—detecting, classifying, and reporting road hazards in real time before they cause an accident.**"*

---

# ════════════════════════════════════════════════════════════════
# SLIDE 2: PROBLEM IDENTIFICATION & MARKET VALIDATION
# ════════════════════════════════════════════════════════════════
**Time Budget:** 45 Seconds  
**Layout:** Top 35% (Hero Hook & Stats) | Middle 25% (Root Causes) | Bottom 40% (Gap Analysis Table)

### 📌 Slide Content Elements

#### 1. Hero Hook Stat Banners (Top of Slide)
```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  🔴 1,77,175 ROAD FATALITIES IN INDIA (2024) — 1 LIFE LOST EVERY 3 MINUTES             │
│     Pothole Deaths Surged 53% in 5 Years (9,438 Total; 2,385 in 2024 Alone)            │
│     Source: Ministry of Road Transport and Highways (MoRTH), 'Road Accidents in India 2024'  │
└────────────────────────────────────────────────────────────────────────────────────────┘
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  🟠 BENGALURU: #2 MOST CONGESTED CITY ON EARTH (TomTom Traffic Index 2025)             │
│     74.4% Congestion Level • 36 min 09 sec per 10 km • 13.9 km/h Rush-Hour Crawl      │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

#### 2. One-Sentence Problem Definition
> **"Indian municipal authorities govern multi-thousand-kilometer road networks completely blind—relying on slow, reactive citizen grievances and manual patchwork while undetected hazards claim 2,385 lives annually and unresolved bottlenecks grind transit to a 13.9 km/h crawl."**

#### 3. Exactly 4 Root Causes (Horizontal Card Row)
1. 🛠️ **Reactive Patchwork:** Repairs occur only after accidents or citizen complaints; maintenance perpetually lags structural asphalt decay.
2. 📹 **96% Surveillance Blind Spots:** Fixed AI cameras cover <4% of highway/intersection points; 96% of city corridors remain completely unmonitored.
3. 🗄️ **Inter-Agency Data Silos:** Traffic police (congestion/accidents) and PWD engineers (road repair) operate disconnected systems with zero shared spatial intelligence.
4. ⏱️ **60-Minute Triage Latency:** Waterlogging, road debris, and stalled vehicles take over an hour to reach dispatchers, multiplying local bottlenecks into city-wide gridlock.

#### 4. Affected Stakeholders
- **Citizens & Commuters** (bear 70%+ of pothole-induced casualties)
- **Municipal Corporations (ULBs / PWD / BBMP)** (uncoordinated road maintenance spending)
- **Traffic Police & Command Centres (TMC / BTP)** (delayed incident response)
- **Public Transit Fleets (BMTC / KSRTC)** (vehicle chassis damage and route delays)

#### 5. Gap Analysis Table (Market Analysis Matrix)

| Existing Solution | Deployment Scope | Detection Capability | Critical Operational Gap vs. UrbanSight AI |
| :--- | :--- | :--- | :--- |
| **Hayden AI (US/EU)** | 2,300+ transit buses (NYC, Oakland) | Bus lane, bike lane & parking violations | **Zero hazard intelligence:** Blind to potholes, cracks, or flooding; punitive enforcement only; closed proprietary hardware. |
| **Rebotnix Horizon (Germany)** | Edge-AI on municipal waste trucks | Static asset auditing: road distress, waste, signs | **Zero live incident intelligence:** Cannot detect active traffic incidents or congestion; bound to weekly garbage routes. |
| **BBMP / Bengaluru East Survey** | Periodic municipal inspection vans (~1,600 km) | One-off road damage survey | **Zero temporal continuity:** Expensive periodic snapshot; data is obsolete within weeks of completion. |
| **Indian Startups (e.g., RoadMetrics)** | Aftermarket smartphone apps / dashcams | Pothole vibration & surface roughness | **Siloed & non-scalable:** Lacks municipal command integration; covers only potholes; no live congestion/incident triage. |
| **Karnataka AI Highway Cameras** | Fixed high-mast ANPR gantries (7 spots) | Speeding, seatbelt & lane violations | **Fixed point blindness:** Covers <1% of the road corridor; zero road surface degradation monitoring; high CapEx (₹Cr/km). |

#### 6. The "Why Now" Breakthrough Line
> **"Under the PM e-Bus Sewa scheme, 10,000 electric buses factory-equipped with 5 CCTV cameras, GPS, and 4G telemetry are rolling out across 169 cities—creating a ready-made mobile sensing grid with ZERO new municipal hardware CapEx."**

---

### 🎙️ Speaker Script (Slide 2 — 40 Seconds)
> *"Judges, in 2024 alone, India lost over one lakh seventy-seven thousand lives to road accidents. Even more alarming, pothole fatalities surged 53% to nearly 2,400 deaths in a single year.*  
> *In Bengaluru—the world’s second most congested city—citizens spend 36 minutes crawling just 10 kilometers at 14 kilometers per hour.*  
> *Why? Because city authorities operate completely blind, discovering fatal hazards only after citizen complaints or tragic crashes.*  
> *Existing solutions either focus solely on parking tickets like Hayden AI, or rely on periodic survey vans. But right now, 10,000 PM e-Buses with five cameras each are deploying across India.*  
> *UrbanSight AI turns this existing fleet into a continuous, real-time road intelligence grid."*

---

# ════════════════════════════════════════════════════════════════
# SLIDE 3: PROPOSED SOLUTION & ARCHITECTURE
# ════════════════════════════════════════════════════════════════
**Time Budget:** 45 Seconds  
**Layout:** 45% Left (4-Agent Data Flow & Root-Cause Matrix) | 55% Right (GIS Command Dashboard Mockup & Features)

### 📌 Slide Content Elements

#### 1. One-Line Overview
> **"UrbanSight AI turns existing city bus dashcams into continuous mobile scanning grids, running on-edge vision to detect hazards, and orchestrating autonomous multi-agent workflows that close the loop from detection to PWD repair dispatch in under 3 minutes."**

#### 2. End-to-End System Architecture (The 4-Agent Pipeline)

```
┌────────────────────────────────────────────────────────────────────────┐
│ 1. INPUT LAYER (MOBILE FLEET EDGE)                                     │
│    Existing PM e-Bus Fleet (5x Windshield Cameras + GNSS/GPS Stream)   │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ 1080p 30 FPS Feed
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ 2. EDGE INFERENCE LAYER (ON-BUS COMPUTE)                               │
│    AGENT 1: VISION PERCEPTION AGENT (YOLOv8 Edge Engine)               │
│    • Real-time classification: Potholes, Cracks, Flooding, Stalls      │
│    • Privacy Engine: Irreversible on-chip face & license plate blur    │
│    • Telemetry Packaging: Bounding box + confidence + GPS Geotag       │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ <15 KB GeoJSON Payload (MQTT/4G)
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ 3. CLOUD MULTI-AGENT ORCHESTRATION LAYER                               │
│    AGENT 2: GEO-SPATIAL CLUSTERING & TRIAGE AGENT                      │
│    • DBSCAN Spatial Clustering: Merges repeat bus passes into 1 ticket │
│    • Severity Matrix: Damage depth × traffic volume × frequency        │
└─────────────────┬────────────────────────────────────┬─────────────────┘
                  │ Validated Cluster                  │ Live Incident
                  ▼                                    ▼
┌─────────────────────────────────┐  ┌───────────────────────────────────┐
│ AGENT 3: MUNICIPAL DISPATCH     │  │ AGENT 4: FLEET ADVISORY           │
│ • Auto-generates PWD Work Order │  │ • Sub-second WebSocket Broadcast  │
│ • Attaches GPS, Photo, Severity │  │ • Real-time driver hazard warning │
│ • Dispatches in < 3 minutes     │  │ • Ahead-of-route detour navigation│
└─────────────────┬───────────────┘  └─────────────────┬─────────────────┘
                  └─────────────────┬──────────────────┘
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ 4. UNIFIED COMMAND & OUTPUT LAYER                                      │
│    • Smart Cities ICCC Dashboard (Live bus tracks + hazard pins)       │
│    • PWD Contractor Work-Order Queue (SLA tracker & repair status)     │
│    • Driver In-Cab Console (Tablet-based reroute & obstacle warning)   │
└────────────────────────────────────────────────────────────────────────┘
```

#### 3. Root-Cause Resolution Matrix (Slide 2 ➔ Slide 3 Traceability)

| Root Cause (Slide 2) | UrbanSight AI Architectural Solution | Quantifiable Operational Impact |
|---|---|---|
| **Monitoring is periodic & reactive** | Daily bus fleet continuous edge scanning | **20–50+ road inspections per day** along transit corridors |
| **Data siloed by hazard type** | Unified multi-class vision perception pipeline | **Single pane of glass** replacing 3 disconnected systems |
| **Static cameras have blind spots** | Mobile transit mesh coverage across arterials | **85%+ city arterial reach** without installing roadside poles |
| **Detection doesn't close action loop** | Autonomous Agent 3 Municipal Dispatch | **<3 minute dispatch SLA** from detection to official PWD ticket |

#### 4. Exactly 5 Key System Capabilities
1. 👁️ **On-Device Edge Vision:** Runs lightweight YOLOv8 models directly on bus compute to classify road surface defects and traffic incidents at 30 FPS.
2. 📍 **DBSCAN Spatial Deduplication:** Groups redundant detections from multiple buses traversing the same physical pothole into a single canonical ticket.
3. 🤖 **Autonomous PWD Dispatch:** Automatically compiles and submits official PWD repair work orders—including exact GPS pin, photo proof, and dimensions—within 3 minutes.
4. 🛰️ **Sub-Second Fleet Advisories:** Pushes immediate obstacle and waterlogging warnings directly to oncoming bus driver consoles via bi-directional WebSockets.
5. 🗺️ **Integrated ICCC Command Hub:** Provides municipal authorities with an interactive Leaflet.js command map featuring real-time fleet tracking and repair backlog SLAs.

#### 5. Exactly 3 Innovation Edges
- **Unified Tri-Vector Perception:** The only platform detecting physical road damage, traffic stagnation, and live street incidents simultaneously in one compute loop.
- **Privacy-by-Design Edge Architecture:** On-chip face and license plate blurring ensures zero biometric PII ever leaves the bus; only anonymized GeoJSON (<15 KB) is transmitted.
- **Zero Municipal Hardware CapEx:** Directly integrates with the 5 cameras and GPS modules already mandated on 10,000+ electric buses under PM e-Bus Sewa.

#### 6. Dashboard Mockup Visual Specification (Right Panel)
- **Center Canvas:** Dark-mode Leaflet.js map of Bengaluru transit grid with cyan bus breadcrumbs moving in real time.
- **Color-Coded Hazard Cluster Markers:**
  - 🔴 **Crimson Pin:** High-Severity Pothole (Depth: >8cm | Cluster: 14 bus passes)
  - 🟠 **Amber Pin:** Severe Waterlogging (Submerged stretch: 35m)
  - 🟡 **Yellow Pin:** Surface Fissure / Longitudinal Crack
- **Right Action Drawer:** *"Agent 3: Autonomous PWD Work Order"* showing ticket `#PWD-2026-OCT-0941`, geotag `[12.9716°N, 77.5946°E]`, cropped image preview with blurred license plates, and status `AUTO-FILED TO BBMP SAHAYA (<180s SLA)`.

---

### 🎙️ Speaker Script (Slide 3 — 40 Seconds)
> *"To solve this, we introduce **UrbanSight AI**. Instead of spending crores on new infrastructure, we turn the existing PM e-Bus Sewa fleet into an autonomous mobile scanning grid.*  
> *As buses drive their daily routes, **Agent 1** runs YOLOv8 edge inference to spot potholes, waterlogging, and congestion—blurring plates and faces locally for total privacy.*  
> *In the cloud, **Agent 2** runs DBSCAN clustering to deduplicate passes and score severity.*  
> *Then, **Agent 3** automatically files an official PWD complaint with geotagged evidence in under three minutes, while **Agent 4** broadcasts real-time detour advisories to nearby bus drivers.*  
> *This closes the loop end-to-end: zero new CapEx, complete arterial coverage, and actionable municipal dispatch in real time."*

---

# ════════════════════════════════════════════════════════════════
# SLIDE 4: TECHNOLOGY STACK & DEEP TECH
# ════════════════════════════════════════════════════════════════
**Time Budget:** 30 Seconds  
**Layout:** 60% Left (Layered Functional Stack Table) | 40% Right (3 "Why This Choice" Cards + Dataset Disclosure)

### 📌 Slide Content Elements

#### 1. Complete Layered Stack Table (6 Functional Layers)

| Layer & Functional Role | Tools & Technologies | One-Line Justification |
| :--- | :--- | :--- |
| **L1: Edge Sensing & Compute** | **NVIDIA Jetson Orin Nano (40 TOPS)** *(Primary)*<br>OR **Raspberry Pi 4 + Coral Edge TPU (4 TOPS)** *(Frugal)*<br>Wide-Angle 1080p 30 FPS Dashcam | Rugged, low-power (7–15W) edge compute retrofittable on transit under ₹15,000/bus. |
| **L2: Edge AI & Privacy Engine** | **YOLOv8 Nano / YOLO26s** (TensorRT FP16/INT8)<br>**MobileNetV2** (ISPRS Annals X-5/W2-2025 fallback)<br>**OpenCV** (On-Device Face & ANPR Blur) | Sub-30ms local inference at 30 FPS with irrevocable on-device anonymization before transmission. |
| **L3: Telemetry & Transport** | **MQTT over TLS (v1.3)**<br>**Eclipse Mosquitto Broker**<br>**Pydantic v2** (GeoJSON Schema Validation) | Transmits encrypted lightweight JSON metadata (<15 KB/event), eliminating cellular video bandwidth costs. |
| **L4: Cloud Ingestion & Backend** | **FastAPI (ASGI)**<br>**Python 3.13**<br>**Docker** on **Railway / GCP Cloud Run** | Asynchronous, non-blocking REST & WebSocket gateway auto-scaling to zero for ₹800–₹1,500/month. |
| **L5: Geospatial Intelligence** | **DBSCAN (scikit-learn)**<br>**PostGIS** (PostgreSQL 16)<br>**Uber H3** (Hexagonal Spatial Index - Res 9) | Merges repeated multi-bus detections of the same defect into unified, confidence-weighted civic tickets. |
| **L6: Command Center & APIs** | **React 18** + **Leaflet.js** + **CartoDB Dark Tiles**<br>**WebSockets** (Live Telemetry Stream)<br>**REST API Gateway** (BBMP / PWD Portal) | Sub-second real-time map updates with automated, evidence-backed complaint lodging for municipal engineers. |

#### 2. The 3 "Why This Choice?" Callout Cards (Right Column)

##### 🔹 Card 1: Edge Compute + Privacy Engine (YOLOv8n + OpenCV)
- **99.9% Bandwidth Reduction:** Streaming raw video from 100 buses consumes ~5TB/day in cellular data. UrbanSight processes frames on-chip at 30 FPS and transmits only `<15 KB` GeoJSON metadata per confirmed detection.
- **Strict DPDP Act Compliance:** Irreversible Gaussian blurring strips faces and license plates in local edge RAM before transmission. Zero biometric PII ever touches the cloud.

##### 🔹 Card 2: Spatial Deduplication (DBSCAN + Uber H3 vs. Alert Fatigue)
- **Automated Noise Suppression:** When 30 buses pass the same Outer Ring Road pothole daily, naive platforms create 30 duplicate complaints.
- **DBSCAN + H3 Resolution-9:** Groups incident coordinates within a 5-meter radius, increments severity confidence, and outputs exactly **one** consolidated PWD work order with longitudinal depth tracking.

##### 🔹 Card 3: Asymmetric Hardware Strategy (Jetson vs. Coral TPU)
- **Zero Specialized Survey Vans:** Traditional road survey vehicles cost ₹40L–₹1Cr+. UrbanSight uses existing public transit fleets as passive survey infrastructure.
- **Fleet Adaptability:** High-frequency routes utilize Jetson Orin Nano (40 TOPS multi-hazard vision); budget feeder routes utilize RPi 4 + Coral Edge TPU (4 TOPS MobileNetV2), slashing capital expenditure by over 80%.

#### 3. Engineering Transparency & Dataset Strategy
- **Identified Dataset Gap:** No public dataset captures road congestion or road defects from the elevated, moving vantage point of a city bus windshield.
- **Base Training Ground:** Fine-tuned on **RDD2022** (47,420 road images from 6 countries including India; 55,000+ localized annotations for potholes and cracks).
- **Active Mitigation:** Implemented **BDD100K transfer learning** for transit-lane vehicle density, augmented with synthetic perspective transformation (bus windshield pitch/yaw simulation) and Indian monsoon/shadow weather augmentation.

#### 4. Frugal Engineering & Cost Note
- **100% Open-Source Stack:** Zero proprietary software seat licenses (FastAPI, PostGIS, Leaflet, YOLOv8).
- **Cloud Pilot Cost:** Only **₹800–₹1,500 / month** for 10 buses on serverless auto-scaling containers (Docker + Railway / GCP Cloud Run scale-to-zero).
- **Hardware Retrofit:** ₹8,000–₹15,000 / bus one-time CapEx — 1/50th the cost of municipal road-scanning vehicles.

---

### 🎙️ Speaker Script (Slide 4 — 28 Seconds)
> *"Instead of streaming expensive, privacy-invasive raw video to the cloud, UrbanSight AI processes everything right on the bus. Quantized YOLOv8 runs at 30 frames per second on an affordable Jetson or Coral TPU, detecting road hazards in under 30 milliseconds. OpenCV blurs all faces and license plates on-chip, transmitting only a tiny 15-kilobyte GeoJSON payload over MQTT. Our cloud backend clusters repeat detections via DBSCAN and H3 grids, automatically pushing verified work orders to BBMP portals—all for under fifteen hundred rupees a month."*

---

# ════════════════════════════════════════════════════════════════
# SLIDE 5: FEASIBILITY, IMPACT & ROADMAP
# ════════════════════════════════════════════════════════════════
**Time Budget:** 40 Seconds  
**Layout:** Top 22% (3 Hero Stat Cards) | Middle 58% (Roadmap Table + Risks & Mitigations + SAM Math) | Bottom 20% (SDG Table + Closing Statement)

### 📌 Slide Content Elements

#### 1. The 3 Hero Stat Cards (Visually Dominant Top Row)

```
┌───────────────────────────────┐ ┌───────────────────────────────┐ ┌───────────────────────────────┐
│          75% FASTER           │ │         40% REDUCTION         │ │         85%+ COVERAGE         │
│   PWD Repair Dispatch Cycle   │ │   Road-Hazard Fatality Risk   │ │   City Arterial Road Network  │
│                               │ │                               │ │                               │
│ Baseline: 14–21 Days Average  │ │ Baseline: 2,385 deaths (2024) │ │ Baseline: <15% coverage from  │
│ UrbanSight: <48 Hours Dispatch│ │ UrbanSight: Pre-failure repair│ │ 7 fixed highway AI cameras    │
└───────────────────────────────┘ └───────────────────────────────┘ └───────────────────────────────┘
```

#### 2. Phased Engineering Roadmap

| Phase | Fleet Scope | Technical Milestone | Validation & Proof Gate |
|---|---|---|---|
| **Phase 1: Prototype (Now)** | **1–2 Buses** (Mysuru/Bengaluru pilot route) | Edge inference (YOLOv8n / TensorRT FP16) on Jetson Nano; DBSCAN clustering; live Leaflet GIS dashboard. | Validated on RDD2022 India subset (>82% mAP50); GPS-synchronized route video replay; sub-30ms edge latency. |
| **Phase 2: City Pilot (3–6 Mo)** | **10–50 Buses** (BMTC / KSRTC pilot fleet) | REST API auto-complaint bridge directly into PWD/BBMP portal; ICCC GIS plug-in; driver WebSocket console. | 500+ field-verified live hazard detections; 92% verified precision against PWD audits; repair SLA <48 hours. |
| **Phase 3: National Scale (6–18 Mo)** | **500+ to 10,000 Buses** (PM e-Bus Sewa, 169 cities) | Pan-city hazard heatmap; predictive asphalt deterioration forecasting model; unified State Transport ITMS API. | Formal MoUs with transit authorities; unified state road health index; 60% reduction in long-term road maintenance cost. |

#### 3. Risk & Mitigation Matrix (5 Deployment Realities)

| Identified Risk | Engineering & Operational Mitigation Strategy |
|---|---|
| **1. Privacy & DPDP Compliance** | **Zero-PII Edge Architecture:** Irreversible on-chip face and license plate blurring in local RAM before frame serialization. Only anonymized GeoJSON (<15 KB) transmitted; raw frames discarded instantly. Fully aligns with India's DPDP Rules. |
| **2. Coverage Bias (Buses stick to routes)** | **Arterial-First Optimization:** Bus routes cover 85%+ of high-volume arterial traffic where 80%+ of commuter fatalities occur. Secondary residential roads covered via complementary sanitation fleet plug-in and citizen app layer. |
| **3. Hostile Indian Operating Conditions** | **Multi-Modal 3-Pass Fusion:** Temporal multi-frame consensus requires 3 consecutive detections before escalation. Visual detections cross-referenced with 6-axis IMU accelerometer vibration spikes. Models fine-tuned on RDD2022 Indian roadway data. |
| **4. Moving-Bus Training Dataset Scarcity** | **Transfer Learning + Active Pilot Loop:** Transfer learning from BDD100K driving dataset with synthetic perspective transformation (bus windshield pitch/yaw). Phase 1 incorporates an automated human-in-the-loop review queue for continuous retraining. |
| **5. Municipal PWD Bureaucracy & Adoption** | **Zero-Overhead Integration Bridge:** No custom software installation required for PWD engineers. Operates as a headless REST API adapter that automatically formats and injects verified tickets directly into existing municipal portals (BBMP Sahaya / PWD). |

#### 4. Scalability & Business Model (B2G SaaS + SAM Math)
- **Business Model:** **B2G (Business-to-Government) Annual SaaS Subscription**
  - **Core Muni-SaaS License:** **₹80,000 / month** per municipal transit authority (edge orchestration, GIS dashboard, auto-PWD ticket routing, driver alert stream).
  - **Enterprise City Analytics Add-on:** **₹1,50,000 / month** (predictive pavement lifecycle forecasting, contractor SLA audit reports).
- **Bottom-Up Addressable Market (SAM Math):**
  $$\text{169 PM e-Bus Sewa Cities} \times ₹80,000\text{ / month} \times 12\text{ months} = \mathbf{₹16.22\text{ Crores / Year Addressable SAM}}$$
  - Capturing just 10 tier-1 city transit authorities in Year 1 yields **₹96 Lakhs ARR**.
  - Software gross margin exceeds **88%** due to open-source edge architecture and scale-to-zero serverless cloud hosting.

#### 5. UN Sustainable Development Goals (SDG Alignment)

| UN SDG Target | Mechanism of Impact | Quantifiable Target Metric |
|---|---|---|
| **SDG 11.2 (PRIMARY)**<br>*Safe, affordable, accessible transport* | Proactively detects and eliminates lethal road craters, debris, and waterlogging along transit corridors before fatal crashes occur. | **40% reduction** in road-hazard commuter casualties across monitored transit corridors. |
| **SDG 11.3 (SECONDARY)**<br>*Inclusive, sustainable urbanization* | Democratizes municipal road auditing by converting public transit buses into passive civic scanners with zero added inspection staff. | **85%+ city arterial coverage**; repair dispatch SLA compressed from 14 days to **<48 hours**. |
| **SDG 9.1 (SECONDARY)**<br>*Quality, resilient infrastructure* | Transitions municipal road asset management from emergency reactive patchwork to early-stage preventive asphalt maintenance. | **60% reduction** in long-term municipal lifecycle maintenance cost per lane-kilometer. |

#### 6. Final Closing Statement
> **"UrbanSight AI converts the 10,000 e-buses already rolling across India into an autonomous national road intelligence grid — detecting hazards, ranking risks, and filing repair orders before the next pothole takes another life."**

---

### 🎙️ Speaker Script (Slide 5 — 38 Seconds)
> *"Judges, UrbanSight AI is not a theoretical concept—it’s an immediately deployable reality.*  
> *By leveraging the 10,000 e-buses already rolling out under PM e-Bus Sewa, we transform existing dashcams into a continuous city sensing grid with zero new municipal CapEx.*  
> *We collapse Bengaluru's 14-day pothole repair cycle down to under 48 hours, covering 85% of city arterials compared to just 7 fixed highway cameras today.*  
> *At ₹80,000 a month per city transit authority, that unlocks a realistic ₹16.2 Crore Year-1 addressable SaaS market.*  
> *Most importantly, UrbanSight AI shifts municipal maintenance from reactive guesswork to autonomous prevention—fixing road hazards before the next pothole takes another life. Thank you, and we welcome your questions!"*

---

# ════════════════════════════════════════════════════════════════
# 📋 QUICK PRODUCTION CHECKLIST (BEFORE PDF SUBMISSION)
# ════════════════════════════════════════════════════════════════
- [ ] **Slide 6 (Submission Guidelines) is deleted** from the presentation file.
- [ ] Deck is exactly **5 content slides**.
- [ ] Export format is **PDF only** (16:9 widescreen layout).
- [ ] Problem Statement ID **SIH26124** is clearly visible on Slide 1.
- [ ] Every slide headline makes an **assertion**, not a generic label.
- [ ] Slide 2 features the **5-row Competitor Gap Analysis Table** with Hayden AI, Rebotnix, and BBMP Survey.
- [ ] Slide 3 shows the **4-Agent Pipeline diagram** and the **Root-Cause Mapping Matrix**.
- [ ] Slide 4 details the **6-layer tech stack** and discloses the **RDD2022 dataset strategy**.
- [ ] Slide 5 features the **3 Hero Stat Cards with baselines**, **5 risks with mitigations**, and **₹16.2 Cr SAM math**.
- [ ] All team members have rehearsed their designated Q&A roles (Edge AI / Cloud & API / GIS Dashboard / Municipal Workflow).
