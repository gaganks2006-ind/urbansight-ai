// ==========================================================================
// RescuAgent AI — Dashboard Controller JavaScript
// ==========================================================================

document.addEventListener('DOMContentLoaded', () => {
    // 1. Initialize Map centered on Guwahati, Assam
    const defaultCenter = [26.1700, 91.7500];
    const map = L.map('gis-map').setView(defaultCenter, 12);

    // Dark Tile Layer (CartoDB Dark Matter)
    L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
        attribution: '&copy; OpenStreetMap &copy; CARTO',
        maxZoom: 18
    }).addTo(map);

    let incidentMarkers = {};
    let assetMarkers = {};

    // Initial Social Feed Posts
    const socialFeedPosts = [
        {
            id: 'POST-801',
            user: '@guwahati_reporter',
            time: '2 mins ago',
            content: 'URGENT! Water level reached 1st floor near North Guwahati Bank. 12 people trapped on roof! #AssamFloods #SOS',
            location: 'North Guwahati Ferry Ghat',
            lat: 26.1985,
            lng: 91.7320
        },
        {
            id: 'POST-802',
            user: '@disaster_alert_in',
            time: '5 mins ago',
            content: 'Landslide blocked Jalukbari bypass flyover. 2 cars trapped under debris, 4 people injured!',
            location: 'Jalukbari Flyover Bypass',
            lat: 26.1550,
            lng: 91.6850
        },
        {
            id: 'POST-803',
            user: '@fancy_bazaar_volunteers',
            time: '12 mins ago',
            content: '45 women & children without clean drinking water or baby food at sector 3 community hall.',
            location: 'Fancy Bazaar Sector 3',
            lat: 26.1820,
            lng: 91.7420
        },
        {
            id: 'POST-804',
            user: '@cwc_river_bot',
            time: '18 mins ago',
            content: 'CRITICAL: Brahmaputra river level cross 49.8m (0.8m above danger line) at Chandrapur gauge station.',
            location: 'Chandrapur Riverside Village',
            lat: 26.2350,
            lng: 91.9120
        },
        {
            id: 'POST-805',
            user: '@zoo_road_resident',
            time: '25 mins ago',
            content: 'Submerged electric pole sparking near Zoo Road Tiniali! High risk of electrocution!',
            location: 'Zoo Road Tiniali',
            lat: 26.1680,
            lng: 91.7810
        }
    ];

    // Clock update
    setInterval(() => {
        const now = new Date();
        document.getElementById('clock-timer').innerText = now.toTimeString().split(' ')[0] + ' IST';
    }, 1000);

    // Render Social Feed
    function renderSocialFeed() {
        const container = document.getElementById('social-media-feed-container');
        container.innerHTML = '';

        socialFeedPosts.forEach(post => {
            const item = document.createElement('div');
            item.className = 'feed-item';
            item.innerHTML = `
                <div class="feed-header">
                    <span class="feed-author"><i class="fa-brands fa-x-twitter"></i> ${post.user}</span>
                    <span class="feed-time">${post.time}</span>
                </div>
                <div class="feed-content">${post.content}</div>
                <div class="feed-actions">
                    <span class="feed-location"><i class="fa-solid fa-location-dot"></i> ${post.location}</span>
                    <button class="btn-process-feed" data-id="${post.id}">
                        <i class="fa-solid fa-microchip"></i> Run Social Sentinel
                    </button>
                </div>
            `;
            
            item.querySelector('.btn-process-feed').addEventListener('click', async () => {
                await processSocialPost(post);
            });

            container.appendChild(item);
        });
    }

    async function processSocialPost(post) {
        try {
            const resp = await fetch('/api/distress', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    source: 'TWITTER',
                    content: post.content,
                    raw_location: post.location,
                    lat: post.lat,
                    lng: post.lng
                })
            });
            if (resp.ok) {
                fetchDashboardData();
            }
        } catch (e) {
            console.error('Error processing post:', e);
        }
    }

    // Main Data Refresh Polling
    async function fetchDashboardData() {
        try {
            const [incidentsRes, assetsRes, logsRes, statsRes, advisoriesRes] = await Promise.all([
                fetch('/api/incidents'),
                fetch('/api/assets'),
                fetch('/api/logs'),
                fetch('/api/stats'),
                fetch('/api/advisories')
            ]);

            const incidents = await incidentsRes.json();
            const assets = await assetsRes.json();
            const logs = await logsRes.json();
            const stats = await statsRes.json();
            const advisories = await advisoriesRes.json();

            updateMetrics(stats);
            updateMapMarkers(incidents, assets);
            updateTerminalLogs(logs);
            updateTriageTable(incidents, assets);
            updateAdvisories(advisories);
        } catch (err) {
            console.error('Failed fetching telemetry:', err);
        }
    }

    // Update Top Metrics
    function updateMetrics(stats) {
        document.getElementById('val-critical').innerText = stats.critical_count;
        document.getElementById('val-total-incidents').innerText = stats.total_incidents;
        document.getElementById('val-deployed-assets').innerText = `${stats.total_assets - stats.available_assets} / ${stats.total_assets}`;
        document.getElementById('val-people-rescued').innerText = stats.people_rescued;
    }

    // Update GIS Map Markers
    function updateMapMarkers(incidents, assets) {
        // Clear existing incident markers
        Object.values(incidentMarkers).forEach(m => map.removeLayer(m));
        incidentMarkers = {};

        incidents.forEach(inc => {
            let color = '#ef4444'; // CRITICAL
            if (inc.priority === 'HIGH') color = '#f97316';
            if (inc.priority === 'MEDIUM') color = '#eab308';
            if (inc.status === 'RESCUED') color = '#10b981';

            const circle = L.circleMarker([inc.lat, inc.lng], {
                radius: inc.priority === 'CRITICAL' ? 12 : 8,
                fillColor: color,
                color: '#ffffff',
                weight: 1.5,
                opacity: 0.9,
                fillOpacity: 0.75
            }).addTo(map);

            circle.bindPopup(`
                <div style="font-family: sans-serif; font-size: 12px; color: #1e293b;">
                    <b style="color: ${color};">[${inc.priority}] ${inc.hazard_type}</b><br/>
                    <b>Location:</b> ${inc.location_name}<br/>
                    <b>Victims:</b> ${inc.victim_count} citizens<br/>
                    <b>Status:</b> ${inc.status}<br/>
                    <small><i>${inc.verification_notes}</i></small>
                </div>
            `);

            incidentMarkers[inc.id] = circle;
        });

        // Update Asset Markers
        Object.values(assetMarkers).forEach(m => map.removeLayer(m));
        assetMarkers = {};

        assets.forEach(asset => {
            let iconClass = 'fa-ship';
            if (asset.asset_type === 'AMBULANCE') iconClass = 'fa-truck-medical';
            if (asset.asset_type === 'CHOPPER_AIRLIFT') iconClass = 'fa-helicopter';
            if (asset.asset_type === 'RELIEF_CAMP') iconClass = 'fa-campground';

            const customHtml = `<div style="background:#1e293b; color:#38bdf8; border:1px solid #38bdf8; border-radius:50%; width:28px; height:28px; display:flex; align-items:center; justify-content:center; box-shadow:0 0 8px #38bdf8;">
                <i class="fa-solid ${iconClass}" style="font-size:12px;"></i>
            </div>`;

            const icon = L.divIcon({
                html: customHtml,
                className: 'custom-map-icon',
                iconSize: [28, 28]
            });

            const marker = L.marker([asset.lat, asset.lng], { icon: icon }).addTo(map);
            marker.bindPopup(`
                <div style="font-family: sans-serif; font-size: 12px; color: #1e293b;">
                    <b>${asset.name}</b><br/>
                    <b>Type:</b> ${asset.asset_type}<br/>
                    <b>Status:</b> ${asset.status}<br/>
                    <b>Capacity:</b> ${asset.capacity} people<br/>
                    <b>Contact:</b> ${asset.contact_phone}
                </div>
            `);
            assetMarkers[asset.id] = marker;
        });
    }

    // Terminal log view
    function updateTerminalLogs(logs) {
        const container = document.getElementById('agent-terminal-logs');
        container.innerHTML = '';
        logs.forEach(log => {
            const div = document.createElement('div');
            let levelClass = log.level.toLowerCase();
            div.className = `log-line ${levelClass}`;
            div.innerText = `[${log.timestamp}] [${log.agent_name}] ${log.message}`;
            container.appendChild(div);
        });
    }

    // Update Triage Table
    function updateTriageTable(incidents, assets) {
        const tbody = document.getElementById('triage-table-body');
        tbody.innerHTML = '';

        document.getElementById('queue-count-badge').innerText = `${incidents.length} Active Incidents`;

        incidents.forEach(inc => {
            const tr = document.createElement('tr');
            
            let actionBtn = '';
            if (inc.status === 'RESCUED') {
                actionBtn = `<span class="badge-status status-RESCUED"><i class="fa-solid fa-check"></i> RESCUED</span>`;
            } else if (inc.status === 'DISPATCHED') {
                actionBtn = `<button class="btn-process-feed btn-rescue" data-id="${inc.id}"><i class="fa-solid fa-person-shelter"></i> Mark Rescued</button>`;
            } else {
                actionBtn = `<button class="btn-process-feed btn-auto-dispatch" data-id="${inc.id}"><i class="fa-solid fa-paper-plane"></i> Dispatch Unit</button>`;
            }

            tr.innerHTML = `
                <td><code>${inc.id}</code></td>
                <td><b>${inc.location_name}</b></td>
                <td>${inc.hazard_type}</td>
                <td><b>${inc.victim_count}</b></td>
                <td><span class="badge-priority ${inc.priority}">${inc.priority}</span></td>
                <td><b>${intScore(inc.confidence_score)}%</b></td>
                <td><span class="badge-status status-${inc.status}">${inc.status}</span></td>
                <td>${actionBtn}</td>
            `;

            const rescueBtn = tr.querySelector('.btn-rescue');
            if (rescueBtn) {
                rescueBtn.addEventListener('click', async () => {
                    await fetch('/api/rescue', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify({ incident_id: inc.id })
                    });
                    fetchDashboardData();
                });
            }

            const autoDispatchBtn = tr.querySelector('.btn-auto-dispatch');
            if (autoDispatchBtn) {
                autoDispatchBtn.addEventListener('click', async () => {
                    // Trigger dispatch simulation
                    fetchDashboardData();
                });
            }

            tbody.appendChild(tr);
        });
    }

    function intScore(score) {
        return Math.round(score * 100);
    }

    // Update Public Advisories
    function updateAdvisories(advisories) {
        const container = document.getElementById('advisory-feed');
        container.innerHTML = '';

        if (advisories.length === 0) {
            container.innerHTML = '<div style="font-size:0.75rem; color:#64748b;">No active emergency advisories published yet.</div>';
            return;
        }

        advisories.forEach(adv => {
            const card = document.createElement('div');
            card.className = 'advisory-card-item';
            card.innerHTML = `
                <div class="advisory-title"><i class="fa-solid fa-triangle-exclamation"></i> ${adv.title}</div>
                <div class="advisory-text"><b>English:</b> ${adv.message_en}</div>
                <div class="advisory-text" style="color: #cbd5e1; font-family: sans-serif;"><b>हिन्दी:</b> ${adv.message_hi}</div>
            `;
            container.appendChild(card);
        });
    }

    // Button event listeners
    document.getElementById('btn-simulate-event').addEventListener('click', async () => {
        await fetch('/api/simulate-stream', { method: 'POST' });
        fetchDashboardData();
    });

    document.getElementById('btn-reset-system').addEventListener('click', async () => {
        await fetch('/api/reset', { method: 'POST' });
        fetchDashboardData();
    });

    // Custom Modal Controls
    const modal = document.getElementById('custom-incident-modal');
    document.getElementById('btn-open-custom-modal').addEventListener('click', () => modal.classList.add('active'));
    document.getElementById('btn-close-modal').addEventListener('click', () => modal.classList.remove('active'));
    document.getElementById('btn-cancel-modal').addEventListener('click', () => modal.classList.remove('active'));

    document.getElementById('form-custom-incident').addEventListener('submit', async (e) => {
        e.preventDefault();
        const source = document.getElementById('input-source').value;
        const location = document.getElementById('input-location').value;
        const content = document.getElementById('input-content').value;

        await fetch('/api/distress', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                source: source,
                raw_location: location,
                content: content
            })
        });

        modal.classList.remove('active');
        fetchDashboardData();
    });

    // Initial render & 3s polling loop
    renderSocialFeed();
    fetchDashboardData();
    setInterval(fetchDashboardData, 3000);
});
