import re

with open('storefront.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the HTML for the address input
old_address = """<div class="form-group" id="addressGroup"><label>Delivery Address</label><input type="text" id="delAddress" placeholder="e.g. TRM Mall, Thika Road"></div>"""

new_address = """<div class="form-group" id="addressGroup">
       <label>Delivery Address</label>
       <div style="display:flex; gap:10px;">
           <input type="text" id="delAddress" placeholder="e.g. TRM Mall, Thika Road" style="flex:1;">
           <button type="button" onclick="getLocation()" class="btn" style="width:auto; margin:0; background:#f1f5f9; color:#475569; border:1px solid #cbd5e1;" title="Get GPS Pin">📍 Use GPS</button>
       </div>
   </div>"""

content = content.replace(old_address, new_address)

# 2. Add the Geolocation JavaScript function
geo_js = """
   function getLocation() {
       const addrInput = document.getElementById('delAddress');
       const originalValue = addrInput.value;
       addrInput.value = "📍 Fetching GPS location...";
       
       if (navigator.geolocation) {
           navigator.geolocation.getCurrentPosition((position) => {
               const lat = position.coords.latitude;
               const lng = position.coords.longitude;
               const mapsLink = `https://maps.google.com/?q=${lat},${lng}`;
               // If they already typed something, append the link
               if (originalValue.trim().length > 0 && originalValue.indexOf('maps.google') === -1) {
                   addrInput.value = originalValue.trim() + " - " + mapsLink;
               } else {
                   addrInput.value = mapsLink;
               }
           }, (error) => {
               alert("Unable to retrieve location. Please ensure location permissions are granted.");
               addrInput.value = originalValue;
           });
       } else {
           alert("Geolocation is not supported by your browser.");
           addrInput.value = originalValue;
       }
   }
"""

content = content.replace('function proceedToPayment() {', geo_js + '\n   function proceedToPayment() {')

with open('storefront.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Storefront updated with GPS Location Pinning")
