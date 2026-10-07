import os
import random
from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List

from backend.models import (
    BusTelemetry, HazardDetection, PWDWorkOrder, DriverAdvisory,
    AgentEventLog, HazardType, SeverityLevel
)
from backend.agents.orchestrator import UrbanSightOrchestrator

app = FastAPI(
    title="UrbanSight AI — Mobile Urban Intelligence Platform",
    description="Multi-Agent AI framework for continuous transit-fleet road sensing, DBSCAN spatial clustering, automated PWD dispatch, and driver advisories (SIH26124).",
    version="2.0.0"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Setup paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, "static")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
templates = Jinja2Templates(directory=TEMPLATES_DIR)

# Initialize Orchestrator Singleton
orchestrator = UrbanSightOrchestrator()

class DetectSimulationRequest(BaseModel):
    bus_id: Optional[str] = "BMTC-KA01-E542"
    hazard_type: Optional[HazardType] = HazardType.POTHOLE
    lat: Optional[float] = 12.9350
    lng: Optional[float] = 77.6820
    location_name: Optional[str] = "Sarjapur-ORR Junction (Near EcoWorld)"
    confidence: Optional[float] = 0.965
    damage_depth_cm: Optional[float] = 9.8

@app.get("/")
def read_root(request: Request):
    """Renders the main UrbanSight AI Command Dashboard."""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/metrics")
def get_metrics():
    return orchestrator.get_system_metrics()

@app.get("/api/buses")
def get_buses():
    return orchestrator.buses

@app.get("/api/hazards")
def get_hazards():
    return orchestrator.hazards

@app.get("/api/work-orders")
def get_work_orders():
    return orchestrator.work_orders

@app.get("/api/advisories")
def get_advisories():
    return orchestrator.advisories

@app.get("/api/events")
def get_event_logs():
    return orchestrator.event_logs

@app.post("/api/simulate-detection")
def simulate_detection(req: DetectSimulationRequest):
    detection = orchestrator.process_edge_detection(
        bus_id=req.bus_id,
        hazard_type=req.hazard_type,
        lat=req.lat,
        lng=req.lng,
        location_name=req.location_name,
        confidence=req.confidence,
        damage_depth_cm=req.damage_depth_cm
    )
    return {
        "status": "SUCCESS",
        "detection": detection,
        "metrics": orchestrator.get_system_metrics()
    }

@app.post("/api/reset")
def reset_system():
    global orchestrator
    orchestrator = UrbanSightOrchestrator()
    return {"status": "RESET_SUCCESSFUL"}
