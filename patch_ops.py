import re

with open('ops-packing.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace inputs with select
old_html = '''<div class="input-group">
 <label>Rider / Courier Name</label>
 <input type="text" id="riderName" placeholder="e.g. Dennis Mwangi (Boda Express)">
 </div>
 <div class="input-group">
 <label>Rider Phone Number</label>
 <input type="tel" id="riderPhone" placeholder="+254 7XX XXX XXX">
 </div>'''

new_html = '''<div class="input-group">
 <label>Assign Active Rider</label>
 <select id="riderSelect" style="width: 100%; padding: 12px; background: #0b1120; border: 1px solid var(--border); border-radius: 8px; color: var(--text);">
    <option value="">Select a rider...</option>
 </select>
 </div>'''

content = content.replace(old_html, new_html)

# Add loadRiders to JS
js_inject = '''let activeRiders = [];
 async function loadRiders() {
     const { data, error } = await client.from('riders').select('*').eq('status', 'active');
     if (data) {
         activeRiders = data;
         const sel = document.getElementById('riderSelect');
         sel.innerHTML = '<option value="">Select a rider...</option>';
         data.forEach(r => sel.innerHTML += <option value=""> ()</option>);
     }
 }'''

content = content.replace('let activeOrder = null;', js_inject + '\n let activeOrder = null;')

# Update submitDispatch
old_dispatch = '''const rName = document.getElementById('riderName').value.trim();
 const rPhone = document.getElementById('riderPhone').value.trim();
 if (!rName || !rPhone) return alert("Please provide rider details.");'''

new_dispatch = '''const rId = document.getElementById('riderSelect').value;
 const rider = activeRiders.find(r => r.id === rId);
 if (!rider) return alert("Please select a rider.");
 const rName = rider.name;
 const rPhone = rider.phone;'''

content = content.replace("const rName = document.getElementById('riderName').value.trim();", new_dispatch).replace("const rPhone = document.getElementById('riderPhone').value.trim();", "").replace("if (!rName || !rPhone) return alert(\"Please provide rider details.\");", "")


# Make sure loadQueue calls loadRiders
content = content.replace('fetchNextOrder();', 'loadRiders();\n fetchNextOrder();')

with open('ops-packing.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("ops-packing patched")
