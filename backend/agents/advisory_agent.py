import uuid
from backend.models import ParsedIncident, PublicAdvisory, PriorityEnum

class AdvisoryAgent:
    """
    Agent 4: Public Advisory & Warning Broadcast Agent
    Generates localized multilingual public warnings and evacuation instructions
    tailored to affected communities based on verified critical incident alerts.
    """
    
    def generate_advisory(self, incident: ParsedIncident) -> PublicAdvisory:
        location = incident.location_name
        hazard = incident.hazard_type.replace("_", " ").title()
        
        title = f"EMERGENCY WARNING: {incident.priority.value} {hazard} Alert for {location}"
        
        # English Broadcast Text
        message_en = (
            f"CIVIL DEFENSE ALERT: A severe {hazard.lower()} has been reported near {location}. "
            f"Water levels and high-risk hazards are currently active. "
            f"Emergency rescue teams are en route. Residents in low-lying areas are advised to move to higher ground immediately. "
            f"Avoid electricity poles and flooded roads. Emergency Helpline: 112 / 1070."
        )
        
        # Hindi Broadcast Text
        message_hi = (
            f"आपातकालीन चेतावनी: {location} के पास {hazard} की गंभीर सूचना मिली है। "
            f"जल स्तर और बाढ़ का खतरा बढ़ा हुआ है। राष्ट्रीय आपदा मोचन बल (NDRF) की टीमें रवाना कर दी गई हैं। "
            f"निचले इलाकों के निवासी तुरंत सुरक्षित और ऊंचे स्थानों पर जाएं। "
            f"बिजली के खंभों और जलमग्न सड़कों से दूर रहें। आपातकालीन हेल्पलाइन: 112 / 1070."
        )
        
        actions = [
            "Evacuate ground floors and move to reinforced rooftops or elevated structures.",
            "Keep emergency flashlight, drinking water, and essential medicines ready.",
            "Do not attempt to wade or drive through flowing floodwaters.",
            "Follow instructions from NDRF rescue boats and local disaster officers."
        ]
        
        advisory = PublicAdvisory(
            id=f"ADV-{uuid.uuid4().hex[:6].upper()}",
            title=title,
            affected_region=location,
            severity=incident.priority,
            message_en=message_en,
            message_hi=message_hi,
            recommended_actions=actions
        )
        
        return advisory
