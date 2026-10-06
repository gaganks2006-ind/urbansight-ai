import uuid
from typing import List, Dict, Tuple, Optional
from datetime import datetime

from backend.models import (
    DistressSignal, ParsedIncident, EmergencyAsset, AgentActionLog,
    PublicAdvisory, SystemStats, PriorityEnum, IncidentStatus, AssetStatus
)
from backend.simulated_data import INITIAL_ASSETS, SIMULATED_DISTRESS_FEEDS
from backend.agents.social_sentinel import SocialSentinelAgent
from backend.agents.triage_verification import TriageVerificationAgent
from backend.agents.logistics_dispatcher import LogisticsDispatcherAgent
from backend.agents.advisory_agent import AdvisoryAgent

class AgentOrchestrator:
    """
    Master Multi-Agent Orchestrator
    Manages state, runs multi-agent pipelines sequentially or asynchronously,
    and logs step-by-step reasoning for real-time telemetry.
    """
    
    def __init__(self):
        self.sentinel_agent = SocialSentinelAgent()
        self.triage_agent = TriageVerificationAgent()
        self.dispatcher_agent = LogisticsDispatcherAgent()
        self.advisory_agent = AdvisoryAgent()
        
        self.incidents: Dict[str, ParsedIncident] = {}
        self.assets: List[EmergencyAsset] = list(INITIAL_ASSETS)
        self.logs: List[AgentActionLog] = []
        self.advisories: List[PublicAdvisory] = []
        self.people_rescued_counter: int = 42  # Seeded initial rescue count
        
        # Initialize default log entry
        self.add_log(
            "SystemCore", "INFO",
            "RescuAgent Multi-Agent Orchestrator initialized. Deployed 4 autonomous agents."
        )
        
        # Pre-seed initial simulated incidents through the pipeline
        self._seed_initial_state()
        
    def _seed_initial_state(self):
        """Processes initial distress feeds to populate dashboard with active state."""
        for signal in SIMULATED_DISTRESS_FEEDS[:3]:
            self.process_incoming_distress(signal)
            
    def add_log(self, agent_name: str, level: str, message: str, details: Optional[Dict] = None):
        log_entry = AgentActionLog(
            id=f"LOG-{uuid.uuid4().hex[:6].upper()}",
            agent_name=agent_name,
            level=level,
            message=message,
            details=details
        )
        self.logs.insert(0, log_entry)  # Newest logs first
        if len(self.logs) > 100:
            self.logs = self.logs[:100]  # Cap at 100 logs
            
    def process_incoming_distress(self, signal: DistressSignal) -> ParsedIncident:
        """
        Executes the full 4-Agent Pipeline for an incoming distress signal.
        """
        # Step 1: Social Sentinel Extraction
        self.add_log(
            "SocialSentinel", "INFO",
            f"Ingested raw distress signal from [{signal.source}] ({signal.channel}). Extracting hazard & location."
        )
        incident = self.sentinel_agent.process_signal(signal)
        self.incidents[incident.id] = incident
        
        self.add_log(
            "SocialSentinel", "SUCCESS",
            f"Extracted Incident [{incident.id}]: {incident.hazard_type} at {incident.location_name} (Est. Victims: {incident.victim_count})."
        )
        
        # Step 2: Triage & Verification Agent
        self.add_log(
            "TriageVerifier", "INFO",
            f"Cross-referencing Incident [{incident.id}] with satellite radar & CWC gauge telemetry..."
        )
        verified_incident = self.triage_agent.verify_and_triage(incident)
        self.incidents[verified_incident.id] = verified_incident
        
        self.add_log(
            "TriageVerifier", "WARN" if verified_incident.priority == PriorityEnum.CRITICAL else "INFO",
            f"Verified Incident [{incident.id}]: Priority set to [{verified_incident.priority.value}] with {int(verified_incident.confidence_score * 100)}% confidence."
        )
        
        # Step 3: Logistics & Dispatch Agent
        self.add_log(
            "LogisticsDispatcher", "INFO",
            f"Evaluating spatial proximity & asset capabilities for Incident [{incident.id}]..."
        )
        dispatched_incident, updated_assets, dispatch_msg = self.dispatcher_agent.dispatch_incident(
            verified_incident, self.assets
        )
        self.incidents[dispatched_incident.id] = dispatched_incident
        self.assets = updated_assets
        
        level = "SUCCESS" if "SUCCESS" in dispatch_msg else "WARN"
        self.add_log("LogisticsDispatcher", level, dispatch_msg)
        
        # Step 4: Advisory Agent (Triggered if Critical or High Priority)
        if dispatched_incident.priority in [PriorityEnum.CRITICAL, PriorityEnum.HIGH]:
            self.add_log(
                "AdvisoryAgent", "ALERT",
                f"Generating emergency public advisory broadcast for [{dispatched_incident.location_name}]..."
            )
            advisory = self.advisory_agent.generate_advisory(dispatched_incident)
            self.advisories.insert(0, advisory)
            self.add_log(
                "AdvisoryAgent", "SUCCESS",
                f"Published bilingual Advisory [{advisory.id}] for region: {advisory.affected_region}."
            )
            
        return dispatched_incident

    def manual_dispatch(self, incident_id: str, asset_id: str) -> bool:
        """Manually dispatches a specific asset to an incident."""
        incident = self.incidents.get(incident_id)
        asset = next((a for a in self.assets if a.id == asset_id), None)
        
        if incident and asset and asset.status == AssetStatus.AVAILABLE:
            asset.status = AssetStatus.DISPATCHED
            asset.current_incident_id = incident.id
            incident.status = IncidentStatus.DISPATCHED
            if asset.id not in incident.assigned_asset_ids:
                incident.assigned_asset_ids.append(asset.id)
            incident.eta_minutes = 15
            
            self.add_log(
                "CommandCenter", "SUCCESS",
                f"Manual Dispatch Executed: {asset.name} assigned to Incident [{incident.id}]."
            )
            return True
        return False

    def mark_rescued(self, incident_id: str) -> bool:
        """Marks an incident as RESCUED and frees up assigned assets."""
        incident = self.incidents.get(incident_id)
        if incident:
            incident.status = IncidentStatus.RESCUED
            self.people_rescued_counter += incident.victim_count
            
            # Free up assigned assets
            for asset_id in incident.assigned_asset_ids:
                for asset in self.assets:
                    if asset.id == asset_id:
                        asset.status = AssetStatus.AVAILABLE
                        asset.current_incident_id = None
                        
            self.add_log(
                "CommandCenter", "SUCCESS",
                f"RESCUE COMPLETE: Incident [{incident.id}] marked rescued! {incident.victim_count} citizens evacuated to safety."
            )
            return True
        return False

    def get_stats(self) -> SystemStats:
        total_incidents = len(self.incidents)
        critical_count = sum(1 for i in self.incidents.values() if i.priority == PriorityEnum.CRITICAL)
        high_count = sum(1 for i in self.incidents.values() if i.priority == PriorityEnum.HIGH)
        dispatched_count = sum(1 for i in self.incidents.values() if i.status == IncidentStatus.DISPATCHED)
        rescued_count = sum(1 for i in self.incidents.values() if i.status == IncidentStatus.RESCUED)
        
        available_assets = sum(1 for a in self.assets if a.status == AssetStatus.AVAILABLE)
        
        return SystemStats(
            total_incidents=total_incidents,
            critical_count=critical_count,
            high_count=high_count,
            dispatched_count=dispatched_count,
            rescued_count=rescued_count,
            total_assets=len(self.assets),
            available_assets=available_assets,
            people_rescued=self.people_rescued_counter,
            avg_response_time_min=12.4
        )
        
    def reset_state(self):
        """Resets the state back to clean baseline."""
        self.incidents.clear()
        self.assets = [a.model_copy(update={"status": AssetStatus.AVAILABLE, "current_incident_id": None}) for a in INITIAL_ASSETS]
        self.logs.clear()
        self.advisories.clear()
        self.people_rescued_counter = 42
        self.add_log("SystemCore", "INFO", "System state reset. Multi-agent framework ready.")
        self._seed_initial_state()
