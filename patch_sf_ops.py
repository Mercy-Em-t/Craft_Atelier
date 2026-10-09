import re

with open('storefront.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update delivery options in HTML
old_del = """<select id="delType" onchange="toggleDeliveryOptions()">
 <option value="rider">Motorbike Rider (Doorstep)</option>
 <option value="pickup">Self-Pickup (HQ)</option>
 <option value="courier">National Courier (Fargo/G4S)</option>
 </select>"""
new_del = """<select id="delType" onchange="toggleDeliveryOptions()">
 <option value="rider" data-cost="300">Motorbike Rider (Doorstep) - KES 300</option>
 <option value="pickup" data-cost="0">Self-Pickup (HQ) - FREE</option>
 <option value="courier" data-cost="500">National Courier (Fargo/G4S) - KES 500</option>
 </select>"""
content = content.replace(old_del, new_del)

# 2. Update payment logic in JS
old_pay = """const total = cart.reduce((sum, item) => sum + item.price, 0);
 document.getElementById('mpesaTotalAmount').innerText = 'KES ' + (total / 100).toLocaleString();"""
new_pay = """const subtotal = cart.reduce((sum, item) => sum + item.price, 0);
 const sel = document.getElementById('delType');
 const delCostCents = parseInt(sel.options[sel.selectedIndex].getAttribute('data-cost')) * 100;
 const total = subtotal + delCostCents;
 document.getElementById('mpesaTotalAmount').innerText = 'KES ' + (total / 100).toLocaleString();"""
content = content.replace(old_pay, new_pay)

with open('storefront.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Storefront updated with Delivery Costs")
