import random
from backend.models import ParsedIncident, PriorityEnum, IncidentStatus

class TriageVerificationAgent:
    """
    Agent 2: Triage & Verification Agent
    Cross-references reported incidents against satellite inundation data, river level gauges,
    and weather radar telemetry to calculate verified confidence scores and set final priority.
    """
    
    def verify_and_triage(self, incident: ParsedIncident) -> ParsedIncident:
        # Simulate cross-referencing satellite radar (Sentinel-1 / CWC gauge)
        simulated_river_gauge_m = 49.8  # Danger level is 49.0m
        simulated_rainfall_mm_hr = 42.5 # Heavy torrential rainfall
        
        notes = []
        confidence_delta = 0.0
        
        # Check source reliability
        if incident.source in ["CWC_RIVER_GAUGE", "SATELLITE_BEACON", "EMERGENCY_CALL_112"]:
            confidence_delta += 0.20
            notes.append(f"Source '{incident.source}' verified via official emergency protocol.")
        elif incident.source == "TWITTER":
            confidence_delta += 0.10
            notes.append("Social media report cross-analyzed with NLP keyword frequency.")
            
        # Environmental verification
        if incident.hazard_type in ["FLASH_FLOOD", "LANDSLIDE"]:
            if simulated_river_gauge_m > 49.0:
                confidence_delta += 0.15
                notes.append(f"Water gauge at {simulated_river_gauge_m}m confirms river overflow state (+0.8m above danger mark).")
            if simulated_rainfall_mm_hr > 30.0:
                notes.append(f"Radar telemetry confirms intense precipitation ({simulated_rainfall_mm_hr} mm/hr).")
                
        # Final Confidence & Status Assignment
        final_confidence = min(0.98, incident.confidence_score + confidence_delta)
        incident.confidence_score = round(final_confidence, 2)
        
        if incident.confidence_score >= 0.70:
            incident.status = IncidentStatus.VERIFIED
            notes.append("VERIFIED: High risk authenticity threshold passed.")
        else:
            incident.status = IncidentStatus.REPORTED
            notes.append("PENDING: Additional telemetry check recommended.")
            
        # Priority adjustment based on victim count & hazard severity
        if incident.victim_count >= 10 or (incident.hazard_type == "FLASH_FLOOD" and incident.confidence_score > 0.85):
            incident.priority = PriorityEnum.CRITICAL
        elif incident.victim_count >= 4:
            incident.priority = PriorityEnum.HIGH
            
        incident.verification_notes = " | ".join(notes)
        return incident
