import uuid
from datetime import datetime
from typing import List, Dict, Any, Optional
from backend.models import (
    BusTelemetry, HazardDetection, PWDWorkOrder, DriverAdvisory,
    AgentEventLog, HazardType, SeverityLevel, TicketStatus
)
from backend.simulated_data import INITIAL_BUSES, INITIAL_HAZARDS, INITIAL_WORK_ORDERS

class UrbanSightOrchestrator:
    def __init__(self):
        self.buses: List[BusTelemetry] = [BusTelemetry(**b) for b in INITIAL_BUSES]
        self.hazards: List[HazardDetection] = [HazardDetection(**h) for h in INITIAL_HAZARDS]
        self.work_orders: List[PWDWorkOrder] = [PWDWorkOrder(**w) for w in INITIAL_WORK_ORDERS]
        self.advisories: List[DriverAdvisory] = []
        self.event_logs: List[AgentEventLog] = []

        # Initial seed logs
        self._log_event(
            "Agent 1: Vision Perception",
            "ON_CHIP_INFERENCE",
            "YOLOv8-Nano initialized @ 30 FPS. DPDP Gaussian privacy blur active."
        )
        self._log_event(
            "Agent 2: Geo-Spatial Clustering",
            "DBSCAN_OPTIMIZED",
            "Spatial epsilon set to 15m; 5 active clusters indexed in PostGIS."
        )
        self._log_event(
            "Agent 3: Municipal Dispatch",
            "PORTAL_LINKED",
            "REST Gateway to BBMP Sahaya & PWD active. Auto-ticket SLA <180s."
        )
        self._log_event(
            "Agent 4: Fleet Advisory",
            "WEBSOCKET_READY",
            "In-cab driver console advisory stream broadcasting live."
        )

    def _log_event(self, agent_name: str, action: str, detail: str):
        log = AgentEventLog(
            id=str(uuid.uuid4())[:8],
            agent_name=agent_name,
            action=action,
            detail=detail
        )
        self.event_logs.insert(0, log)
        if len(self.event_logs) > 50:
            self.event_logs.pop()

    def get_system_metrics(self) -> Dict[str, Any]:
        return {
            "total_buses_online": len(self.buses),
            "km_scanned_today": 4820,
            "total_hazards_tracked": len(self.hazards),
            "critical_p1_count": sum(1 for h in self.hazards if h.severity == SeverityLevel.CRITICAL_P1),
            "pwd_work_orders_filed": len(self.work_orders),
            "average_dispatch_sla_min": 2.4,
            "bandwidth_saved_pct": 99.4,
            "privacy_compliance": "100% DPDP Compliant (Zero PII)"
        }

    def process_edge_detection(
        self,
        bus_id: str,
        hazard_type: HazardType,
        lat: float,
        lng: float,
        location_name: str,
        confidence: float = 0.95,
        damage_depth_cm: Optional[float] = None
    ) -> HazardDetection:
        """
        Agent 1 receives detection -> Agent 2 clusters -> Agent 3 auto-files ticket -> Agent 4 alerts fleet.
        """
        # 1. Agent 1: Vision Ingestion
        self._log_event(
            "Agent 1: Vision Perception",
            "DEFECT_DETECTED",
            f"Bus {bus_id} spotted {hazard_type.value} (conf: {confidence:.2f}) at {location_name}"
        )

        # 2. Agent 2: DBSCAN Spatial Deduplication
        # Check if hazard exists within ~30 meters (rough 0.0003 lat/lng delta)
        matching_cluster = None
        for existing in self.hazards:
            dist_sq = (existing.lat - lat)**2 + (existing.lng - lng)**2
            if dist_sq < 0.0000001:  # within ~30m
                matching_cluster = existing
                break

        if matching_cluster:
            matching_cluster.pass_count += 1
            matching_cluster.confidence = min(0.99, matching_cluster.confidence + 0.02)
            self._log_event(
                "Agent 2: Geo-Spatial Clustering",
                "CLUSTER_INCREMENTED",
                f"Merged repeat bus pass into Cluster {matching_cluster.cluster_id} (Pass count: {matching_cluster.pass_count})"
            )
            detection = matching_cluster
        else:
            cluster_id = f"DBSCAN-CL-{len(self.hazards) + 1:03d}"
            severity = SeverityLevel.CRITICAL_P1 if hazard_type in [HazardType.POTHOLE, HazardType.ACCIDENT] else SeverityLevel.HIGH_P2
            detection = HazardDetection(
                id=f"HAZ-2026-{len(self.hazards) + 1:03d}",
                bus_id=bus_id,
                hazard_type=hazard_type,
                severity=severity,
                confidence=confidence,
                lat=lat,
                lng=lng,
                location_name=location_name,
                damage_depth_cm=damage_depth_cm,
                pass_count=1,
                cluster_id=cluster_id,
                image_url="image1.jpg",
                status=TicketStatus.DETECTED
            )
            self.hazards.append(detection)
            self._log_event(
                "Agent 2: Geo-Spatial Clustering",
                "NEW_CANONICAL_CLUSTER",
                f"Formed new canonical cluster {cluster_id} at {location_name}"
            )

        # 3. Agent 3: Autonomous Municipal Dispatch if passes >= 3 or Critical P1
        if detection.status != TicketStatus.AUTO_DISPATCHED and (detection.pass_count >= 2 or detection.severity == SeverityLevel.CRITICAL_P1):
            ticket_id = f"PWD-2026-OCT-{random_number():04d}"
            work_order = PWDWorkOrder(
                ticket_id=ticket_id,
                hazard_id=detection.id,
                hazard_type=detection.hazard_type,
                severity=detection.severity,
                location_name=detection.location_name,
                lat=detection.lat,
                lng=detection.lng,
                cluster_count=detection.pass_count,
                sla_hours=48 if detection.severity == SeverityLevel.CRITICAL_P1 else 24,
                dispatched_to="BBMP Central Ward Dispatch / PWD Zone 1",
                status=TicketStatus.AUTO_DISPATCHED
            )
            self.work_orders.insert(0, work_order)
            detection.status = TicketStatus.AUTO_DISPATCHED
            detection.pwd_ticket_id = ticket_id
            self._log_event(
                "Agent 3: Municipal Dispatch",
                "WORK_ORDER_AUTO_FILED",
                f"Auto-filed PWD Work Order #{ticket_id} for {detection.location_name} (SLA: <48h)"
            )

        # 4. Agent 4: Fleet Driver Advisory broadcast
        advisory = DriverAdvisory(
            id=str(uuid.uuid4())[:8],
            bus_id=bus_id,
            hazard_type=detection.hazard_type,
            distance_meters=180,
            recommendation=f"Caution: {detection.hazard_type.value} ahead at {location_name}. Lane merge recommended.",
            alert_level="WARNING"
        )
        self.advisories.insert(0, advisory)
        self._log_event(
            "Agent 4: Fleet Advisory",
            "WEBSOCKET_ALERT_PUSHED",
            f"Pushed warning alert to driver consoles on route: {location_name}"
        )

        return detection

def random_number():
    import random
    return random.randint(1000, 9999)
