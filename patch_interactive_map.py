import re

with open('storefront.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Inject Leaflet CDN into head
leaflet_cdn = """    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
</head>"""
content = content.replace('</head>', leaflet_cdn)

# 2. Update the button to say "Choose on Map" and call openMapModal
old_btn = """<button type="button" onclick="getLocation()" class="btn" style="width:auto; margin:0; background:#f1f5f9; color:#475569; border:1px solid #cbd5e1;" title="Get GPS Pin">📍 Use GPS</button>"""
new_btn = """<button type="button" onclick="openMapModal()" class="btn" style="width:auto; margin:0; background:#f1f5f9; color:#475569; border:1px solid #cbd5e1;" title="Pick on Map">📍 Map Pin</button>"""
content = content.replace(old_btn, new_btn)

# 3. Add the Map Modal HTML before the closing </body> or before <script>
map_modal = """
    <!-- MAP MODAL -->
    <div class="modal-overlay" id="mapModal" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.5); align-items:center; justify-content:center; z-index:200;">
        <div style="background:white; padding:20px; border-radius:8px; width:90%; max-width:500px;">
            <h3 style="margin-bottom:10px;">Pin Delivery Location</h3>
            <p style="font-size:12px; color:#64748b; margin-bottom:10px;">Drag the marker or click on the map to pin the exact delivery drop-off point.</p>
            <div id="map" style="width:100%; height:300px; background:#e2e8f0; margin-bottom:15px; border-radius:4px; z-index: 10;"></div>
            <div style="display:flex; justify-content:space-between; gap:10px;">
                <button class="btn" style="background:#e2e8f0; color:#475569; flex:1;" onclick="document.getElementById('mapModal').style.display='none'">Cancel</button>
                <button class="btn btn-blue" style="flex:2;" onclick="confirmMapPin()">Confirm Pin</button>
            </div>
        </div>
    </div>
"""
content = content.replace('<script>', map_modal + '\n  <script>')

# 4. Add the Map JS logic (replacing the old getLocation function)
map_js = """
   let map, marker, selectedLatLng;
   
   function openMapModal() {
       document.getElementById('mapModal').style.display = 'flex';
       
       if (!map) {
           // Center on Nairobi by default
           map = L.map('map').setView([-1.2921, 36.8219], 12);
           L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { maxZoom: 19 }).addTo(map);
           marker = L.marker([-1.2921, 36.8219], {draggable: true}).addTo(map);
           
           // If they allow GPS, jump to their current location
           if (navigator.geolocation) {
               navigator.geolocation.getCurrentPosition((pos) => {
                   const lat = pos.coords.latitude;
                   const lng = pos.coords.longitude;
                   map.setView([lat, lng], 15);
                   marker.setLatLng([lat, lng]);
                   selectedLatLng = marker.getLatLng();
               }, () => { console.log("GPS denied, defaulting to Nairobi."); });
           }
           
           marker.on('dragend', function(e) { selectedLatLng = marker.getLatLng(); });
           map.on('click', function(e) {
               marker.setLatLng(e.latlng);
               selectedLatLng = e.latlng;
           });
       }
       
       selectedLatLng = marker.getLatLng();
       
       // Force Leaflet to recalculate size since it was initially hidden in a display:none div
       setTimeout(() => { map.invalidateSize(); }, 200);
   }

   function confirmMapPin() {
       const addrInput = document.getElementById('delAddress');
       const originalValue = addrInput.value;
       const mapsLink = `https://maps.google.com/?q=${selectedLatLng.lat},${selectedLatLng.lng}`;
       
       if (originalValue.trim().length > 0 && originalValue.indexOf('maps.google') === -1) {
           addrInput.value = originalValue.trim() + " - " + mapsLink;
       } else {
           addrInput.value = mapsLink;
       }
       document.getElementById('mapModal').style.display = 'none';
   }
"""
content = re.sub(r'function getLocation\(\) \{.*?(?=function proceedToPayment)', map_js, content, flags=re.DOTALL)

with open('storefront.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Interactive Map Pinning injected!")
