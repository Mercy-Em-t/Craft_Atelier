import re

with open('ops-packing.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_dispatch = """const waUrl = `https://wa.me/${cleanPhone}?text=${msg}`;"""

new_dispatch = """// Generate Delivery PIN
 const deliveryPin = Math.floor(1000 + Math.random() * 9000).toString();
 await client.from('orders').update({ delivery_pin: deliveryPin }).eq('id', activeOrder.id);
 
 const msg = encodeURIComponent(`Hi ${activeOrder.customer_name}! 📦 Your Craft Atelier kit has just been handed over to our rider, ${rider.name} (${rider.phone}). They are on their way to ${activeOrder.delivery_address} and will call you shortly!\n\n🔐 *Your Delivery PIN is: ${deliveryPin}*\nPlease provide this PIN to the rider to confirm you have received your package.`);
 
 const waUrl = `https://wa.me/${cleanPhone}?text=${msg}`;"""

# Replace the msg generation logic safely
# I will use string replace targeting the specific msg line
old_msg_line = "const msg = encodeURIComponent(`Hi ${activeOrder.customer_name}! 📦 Your Craft Atelier kit has just been handed over to our rider, ${rider.name} (${rider.phone}). They are on their way to ${activeOrder.delivery_address} and will call you shortly!`);"

content = content.replace(old_msg_line, new_dispatch)

with open('ops-packing.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Ops Hub updated with Delivery PIN")
