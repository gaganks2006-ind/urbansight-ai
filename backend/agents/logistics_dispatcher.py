import math
from typing import List, Optional, Tuple
from backend.models import ParsedIncident, EmergencyAsset, AssetType, AssetStatus, IncidentStatus

def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calculates distance in kilometers between two geo points."""
    R = 6371.0  # Earth radius in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) ** 2 +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

class LogisticsDispatcherAgent:
    """
    Agent 3: Logistics & Dispatcher Agent
    Calculates spatial distances, matches asset capabilities to hazard requirements,
    estimates response ETA, and auto-issues dispatch orders.
    """
    
    def dispatch_incident(
        self,
        incident: ParsedIncident,
        assets: List[EmergencyAsset]
    ) -> Tuple[ParsedIncident, List[EmergencyAsset], str]:
        
        # Filter available assets
        available_assets = [a for a in assets if a.status == AssetStatus.AVAILABLE]
        
        if not available_assets:
            return incident, assets, "DISPATCH_FAILED: No available emergency units in operational area."
            
        # 1. Determine suitable asset types for the hazard
        preferred_types = []
        if incident.hazard_type in ["FLASH_FLOOD", "WATER_TRAPPED"]:
            preferred_types = [AssetType.BOAT_RESCUE, AssetType.CHOPPER_AIRLIFT, AssetType.FIRE_RESCUE]
        elif incident.hazard_type in ["MEDICAL_EMERGENCY", "LANDSLIDE"]:
            preferred_types = [AssetType.AMBULANCE, AssetType.CHOPPER_AIRLIFT]
        elif incident.hazard_type == "ELECTRICAL_HAZARD":
            preferred_types = [AssetType.FIRE_RESCUE, AssetType.AMBULANCE]
        else:
            preferred_types = [AssetType.BOAT_RESCUE, AssetType.AMBULANCE, AssetType.FIRE_RESCUE]
            
        # If high victim count (>15), prioritize CHOPPER_AIRLIFT or large BOAT_RESCUE
        if incident.victim_count > 15:
            preferred_types.insert(0, AssetType.CHOPPER_AIRLIFT)
            
        # 2. Find best asset matching type and nearest distance
        candidate_assets = [a for a in available_assets if a.asset_type in preferred_types]
        if not candidate_assets:
            candidate_assets = available_assets  # Fallback to any available asset
            
        # Calculate distance to each asset
        best_asset = None
        best_distance = float('inf')
        
        for asset in candidate_assets:
            dist = haversine_distance(incident.lat, incident.lng, asset.lat, asset.lng)
            if dist < best_distance:
                best_distance = dist
                best_asset = asset
                
        if best_asset:
            # 3. Calculate estimated ETA
            # Speed assumptions: Chopper = 150 km/h, Boat/Ambulance = 30 km/h (due to floods)
            speed_kmh = 120.0 if best_asset.asset_type == AssetType.CHOPPER_AIRLIFT else 25.0
            travel_time_hours = best_distance / speed_kmh
            eta_mins = max(5, int(travel_time_hours * 60) + 5)  # 5 min prep time
            
            # Update Asset status
            best_asset.status = AssetStatus.DISPATCHED
            best_asset.current_incident_id = incident.id
            
            # Update Incident status
            incident.status = IncidentStatus.DISPATCHED
            incident.assigned_asset_ids.append(best_asset.id)
            incident.eta_minutes = eta_mins
            
            dispatch_msg = (
                f"DISPATCH SUCCESS: {best_asset.name} ({best_asset.id}) assigned to "
                f"{incident.id} at {incident.location_name}. Distance: {best_distance:.1f} km, Estimated ETA: {eta_mins} mins."
            )
            return incident, assets, dispatch_msg
            
        return incident, assets, "DISPATCH_PENDING: Matching asset evaluation complete."
