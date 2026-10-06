import os
import random
from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List

from backend.models import DistressSignal, ParsedIncident, EmergencyAsset, AgentActionLog, PublicAdvisory, SystemStats
from backend.agents.orchestrator import AgentOrchestrator
from backend.simulated_data import SIMULATED_DISTRESS_FEEDS

app = FastAPI(
    title="RescuAgent AI — Autonomous Disaster Command Platform",
    description="Multi-Agent AI framework for real-time disaster information aggregation, verification, dispatch, and public advisory.",
    version="1.0.0"
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
orchestrator = AgentOrchestrator()

# Request schemas for API endpoints
class DistressRequest(BaseModel):
    source: str
    content: str
    channel: Optional[str] = "CUSTOM_SIMULATION"
    raw_location: Optional[str] = None
    lat: Optional[float] = None
    lng: Optional[float] = None

class DispatchRequest(BaseModel):
    incident_id: str
    asset_id: str

class RescueRequest(BaseModel):
    incident_id: str

@app.get("/")
def read_root(request: Request):
    """Renders the main Disaster Command Dashboard."""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/incidents", response_model=List[ParsedIncident])
def get_incidents():
    return list(orchestrator.incidents.values())

@app.get("/api/assets", response_model=List[EmergencyAsset])
def get_assets():
    return orchestrator.assets

@app.get("/api/logs", response_model=List[AgentActionLog])
def get_logs():
    return orchestrator.logs

@app.get("/api/advisories", response_model=List[PublicAdvisory])
def get_advisories():
    return orchestrator.advisories

@app.get("/api/stats", response_model=SystemStats)
def get_stats():
    return orchestrator.get_stats()

@app.post("/api/distress", response_model=ParsedIncident)
def ingest_distress_signal(req: DistressRequest):
    signal = DistressSignal(
        source=req.source,
        content=req.content,
        channel=req.channel or "API",
        raw_location=req.raw_location,
        lat=req.lat,
        lng=req.lng
    )
    processed = orchestrator.process_incoming_distress(signal)
    return processed

@app.post("/api/simulate-stream")
def simulate_random_distress():
    """Injects a random pre-seeded or procedural distress signal into the system."""
    random_signal = random.choice(SIMULATED_DISTRESS_FEEDS)
    # Clone with new ID so it creates a distinct incident
    new_signal = random_signal.model_copy(update={"id": None})
    processed = orchestrator.process_incoming_distress(new_signal)
    return {"status": "SUCCESS", "incident": processed}

@app.post("/api/dispatch")
def manual_dispatch(req: DispatchRequest):
    success = orchestrator.manual_dispatch(req.incident_id, req.asset_id)
    if not success:
        raise HTTPException(status_code=400, detail="Dispatch failed. Verify incident ID and asset availability.")
    return {"status": "SUCCESS", "message": f"Asset {req.asset_id} dispatched to {req.incident_id}"}

@app.post("/api/rescue")
def mark_rescued(req: RescueRequest):
    success = orchestrator.mark_rescued(req.incident_id)
    if not success:
        raise HTTPException(status_code=404, detail="Incident not found.")
    return {"status": "SUCCESS", "message": f"Incident {req.incident_id} marked rescued."}

@app.post("/api/reset")
def reset_system():
    orchestrator.reset_state()
    return {"status": "SUCCESS", "message": "System state reset to baseline."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)
