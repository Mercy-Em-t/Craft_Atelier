import re

with open('ops-packing.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_alert = """alert("Issue reported to Admin. Order placed ON HOLD.");
            fetchNextOrder();"""

new_alert = """document.getElementById('appContainer').innerHTML = `<div class="empty-state" style="color:#ef4444;"><h3>⚠️ Order Placed On Hold</h3><p>Sent to Admin for review.</p></div>`;
            setTimeout(() => { fetchNextOrder(); }, 1500);"""

content = content.replace(old_alert, new_alert)

old_empty = """<h3 style="margin-bottom: 8px;">All orders packed!</h3>
 <p>Queue is empty. New orders will appear here automatically.</p>"""

new_empty = """<h3 style="margin-bottom: 8px;">Queue is clear!</h3>
 <p>Waiting for new orders from Admin.</p>"""

content = content.replace(old_empty, new_empty)

with open('ops-packing.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Ops Packing UI updated for better visual feedback")
