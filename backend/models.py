from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum

class PriorityEnum(str, Enum):
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

class IncidentStatus(str, Enum):
    REPORTED = "REPORTED"
    VERIFIED = "VERIFIED"
    DISPATCHED = "DISPATCHED"
    RESCUED = "RESCUED"
    FALSE_ALARM = "FALSE_ALARM"

class AssetType(str, Enum):
    BOAT_RESCUE = "BOAT_RESCUE"
    AMBULANCE = "AMBULANCE"
    CHOPPER_AIRLIFT = "CHOPPER_AIRLIFT"
    RELIEF_CAMP = "RELIEF_CAMP"
    FIRE_RESCUE = "FIRE_RESCUE"

class AssetStatus(str, Enum):
    AVAILABLE = "AVAILABLE"
    DISPATCHED = "DISPATCHED"
    MAINTENANCE = "MAINTENANCE"

class DistressSignal(BaseModel):
    id: Optional[str] = None
    source: str  # e.g. "TWITTER", "SOS_HOTLINE", "SMS_GATEWAY", "SATELLITE_BEACON"
    content: str
    channel: str = "PUBLIC"
    raw_location: Optional[str] = None
    lat: Optional[float] = None
    lng: Optional[float] = None
    timestamp: str = Field(default_factory=lambda: datetime.now().isoformat())

class ParsedIncident(BaseModel):
    id: str
    source: str
    content: str
    location_name: str
    lat: float
    lng: float
    hazard_type: str  # e.g., "FLASH_FLOOD", "BUILDING_COLLAPSE", "LANDSLIDE", "MEDICAL_EMERGENCY"
    victim_count: int
    priority: PriorityEnum
    confidence_score: float  # 0.0 to 1.0
    status: IncidentStatus
    assigned_asset_ids: List[str] = []
    eta_minutes: Optional[int] = None
    verification_notes: str = ""
    timestamp: str = Field(default_factory=lambda: datetime.now().isoformat())

class EmergencyAsset(BaseModel):
    id: str
    name: str
    asset_type: AssetType
    lat: float
    lng: float
    status: AssetStatus
    capacity: int
    contact_phone: str
    current_incident_id: Optional[str] = None

class AgentActionLog(BaseModel):
    id: str
    timestamp: str = Field(default_factory=lambda: datetime.now().strftime("%H:%M:%S"))
    agent_name: str  # "SocialSentinel", "TriageVerifier", "LogisticsDispatcher", "AdvisoryAgent"
    level: str       # "INFO", "WARN", "ALERT", "SUCCESS"
    message: str
    details: Optional[Dict[str, Any]] = None

class PublicAdvisory(BaseModel):
    id: str
    title: str
    affected_region: str
    severity: PriorityEnum
    message_en: str
    message_hi: str
    recommended_actions: List[str]
    issued_at: str = Field(default_factory=lambda: datetime.now().isoformat())

class SystemStats(BaseModel):
    total_incidents: int
    critical_count: int
    high_count: int
    dispatched_count: int
    rescued_count: int
    total_assets: int
    available_assets: int
    people_rescued: int
    avg_response_time_min: float
