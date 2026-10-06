from backend.models import EmergencyAsset, AssetType, AssetStatus, DistressSignal
from typing import List

# Initial baseline emergency assets deployed across the region
INITIAL_ASSETS: List[EmergencyAsset] = [
    EmergencyAsset(
        id="AST-NDRF-01",
        name="NDRF Battalion 01 (Motorized Rescue Boats)",
        asset_type=AssetType.BOAT_RESCUE,
        lat=26.1850,
        lng=91.7480,
        status=AssetStatus.AVAILABLE,
        capacity=25,
        contact_phone="+91-98765-00101"
    ),
    EmergencyAsset(
        id="AST-NDRF-02",
        name="NDRF Rapid Response Boat Team 02",
        asset_type=AssetType.BOAT_RESCUE,
        lat=26.2100,
        lng=91.8000,
        status=AssetStatus.AVAILABLE,
        capacity=20,
        contact_phone="+91-98765-00102"
    ),
    EmergencyAsset(
        id="AST-AMB-01",
        name="Guwahati Medical Center ALS Ambulance #1",
        asset_type=AssetType.AMBULANCE,
        lat=26.1445,
        lng=91.7362,
        status=AssetStatus.AVAILABLE,
        capacity=4,
        contact_phone="+91-98765-00103"
    ),
    EmergencyAsset(
        id="AST-AMB-02",
        name="Dispur Trauma Care Mobile Unit #2",
        asset_type=AssetType.AMBULANCE,
        lat=26.1300,
        lng=91.7900,
        status=AssetStatus.AVAILABLE,
        capacity=4,
        contact_phone="+91-98765-00104"
    ),
    EmergencyAsset(
        id="AST-AIR-01",
        name="IAF Mi-17 Airlift Helicopter Squad (Borjhar Air Base)",
        asset_type=AssetType.CHOPPER_AIRLIFT,
        lat=26.1061,
        lng=91.5859,
        status=AssetStatus.AVAILABLE,
        capacity=35,
        contact_phone="+91-98765-00105"
    ),
    EmergencyAsset(
        id="AST-CAMP-01",
        name="Sarusajai Stadium Emergency Relief Center",
        asset_type=AssetType.RELIEF_CAMP,
        lat=26.1150,
        lng=91.7550,
        status=AssetStatus.AVAILABLE,
        capacity=500,
        contact_phone="+91-98765-00106"
    ),
    EmergencyAsset(
        id="AST-FIRE-01",
        name="State Fire & Emergency Heavy Rescue Squad",
        asset_type=AssetType.FIRE_RESCUE,
        lat=26.1780,
        lng=91.7720,
        status=AssetStatus.AVAILABLE,
        capacity=15,
        contact_phone="+91-98765-00107"
    )
]

# Preset distress signals ready to trigger/simulate
SIMULATED_DISTRESS_FEEDS: List[DistressSignal] = [
    DistressSignal(
        id="DS-1001",
        source="TWITTER",
        content="URGENT! Water level reached 1st floor near North Guwahati Bank. 12 people trapped on roof including 3 elderly citizens. Send boats immediately! #AssamFloods #SOS",
        channel="PUBLIC_SOCIAL",
        raw_location="North Guwahati Ferry Ghat",
        lat=26.1985,
        lng=91.7320
    ),
    DistressSignal(
        id="DS-1002",
        source="SOS_HOTLINE",
        content="Emergency call from Jalukbari: Landslide near bypass road! 2 vehicles submerged, 4 injured, medical care needed immediately!",
        channel="EMERGENCY_CALL_112",
        raw_location="Jalukbari Flyover Bypass",
        lat=26.1550,
        lng=91.6850
    ),
    DistressSignal(
        id="DS-1003",
        source="SMS_GATEWAY",
        content="Relief needed at Fancy Bazaar community hall. 45 displaced women and children without drinking water and baby food for 18 hours.",
        channel="SMS_RELIEF",
        raw_location="Fancy Bazaar Sector 3",
        lat=26.1820,
        lng=91.7420
    ),
    DistressSignal(
        id="DS-1004",
        source="SATELLITE_BEACON",
        content="AUTOMATED BEACON: Flash flood inundation surge detected in Chandrapur revenue circle. Depth 2.4m, rapid current.",
        channel="CWC_RIVER_GAUGE",
        raw_location="Chandrapur Riverside Village",
        lat=26.2350,
        lng=91.9120
    ),
    DistressSignal(
        id="DS-1005",
        source="TWITTER",
        content="Submerged electric pole sparking near Zoo Road Tiniali! High risk of electrocution! Need fire & safety response crew.",
        channel="PUBLIC_SOCIAL",
        raw_location="Zoo Road Tiniali",
        lat=26.1680,
        lng=91.7810
    )
]
