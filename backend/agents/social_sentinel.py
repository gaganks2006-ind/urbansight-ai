import re
import uuid
from typing import Dict, Any, Tuple
from backend.models import DistressSignal, ParsedIncident, PriorityEnum, IncidentStatus

# Known location lookup table for demo geocoding resolution
DEMO_GEOCODING_DB = {
    "north guwahati": (26.1985, 91.7320),
    "jalukbari": (26.1550, 91.6850),
    "fancy bazaar": (26.1820, 91.7420),
    "chandrapur": (26.2350, 91.9120),
    "zoo road": (26.1680, 91.7810),
    "dispur": (26.1300, 91.7900),
    "panbazar": (26.1870, 91.7490),
    "khanapara": (26.1150, 91.8200),
    "kamakhya": (26.1660, 91.7050),
}

class SocialSentinelAgent:
    """
    Agent 1: Social Sentinel
    Monitors, parses, and extracts structured hazard entity information from raw text feeds.
    """
    
    def process_signal(self, signal: DistressSignal) -> ParsedIncident:
        text = signal.content.lower()
        
        # 1. Hazard Type Classification
        if any(w in text for w in ["landslide", "mudslide", "rockfall"]):
            hazard = "LANDSLIDE"
        elif any(w in text for w in ["sparking", "electro", "fire", "short circuit", "pole"]):
            hazard = "ELECTRICAL_HAZARD"
        elif any(w in text for w in ["hospital", "injured", "bleeding", "trauma", "medical"]):
            hazard = "MEDICAL_EMERGENCY"
        elif any(w in text for w in ["water", "flood", "submerged", "roof", "trapped", "inundation"]):
            hazard = "FLASH_FLOOD"
        else:
            hazard = "GENERAL_DISTRESS"
            
        # 2. Extract Victim Count heuristic
        victim_count = 1
        numbers = re.findall(r'\b(\d{1,3})\b', text)
        if numbers:
            # Filter reasonable human victim counts (e.g. 1 to 200)
            valid_counts = [int(n) for n in numbers if 1 <= int(n) <= 200]
            if valid_counts:
                victim_count = max(valid_counts)
                
        # 3. Geocode Location
        lat, lng = signal.lat, signal.lng
        location_name = signal.raw_location or "Unknown Sector"
        
        if lat is None or lng is None:
            # Match location against known geocoding database
            found_loc = False
            for loc_key, coords in DEMO_GEOCODING_DB.items():
                if loc_key in text or (signal.raw_location and loc_key in signal.raw_location.lower()):
                    lat, lng = coords
                    location_name = loc_key.title()
                    found_loc = True
                    break
            if not found_loc:
                # Default fallback coordinates around central Guwahati
                lat, lng = 26.1600, 91.7500
                location_name = "Central Command Zone"
                
        # 4. Initial Priority Assessment
        if victim_count >= 10 or hazard in ["LANDSLIDE", "FLASH_FLOOD"] and "trapped" in text:
            priority = PriorityEnum.CRITICAL
        elif victim_count >= 4 or hazard in ["MEDICAL_EMERGENCY", "ELECTRICAL_HAZARD"]:
            priority = PriorityEnum.HIGH
        else:
            priority = PriorityEnum.MEDIUM
            
        incident = ParsedIncident(
            id=f"INC-{uuid.uuid4().hex[:6].upper()}",
            source=signal.source,
            content=signal.content,
            location_name=location_name,
            lat=lat,
            lng=lng,
            hazard_type=hazard,
            victim_count=victim_count,
            priority=priority,
            confidence_score=0.75,  # Baseline confidence before verification
            status=IncidentStatus.REPORTED,
            verification_notes="Initial extraction by SocialSentinel Agent."
        )
        
        return incident
