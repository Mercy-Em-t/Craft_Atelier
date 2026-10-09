with open('ops-packing.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_str = "async function submitDispatch() {"
end_str = "}\n </script>"

start_idx = content.find(start_str)
end_idx = content.find(end_str) + 1

if start_idx != -1 and end_idx != -1:
    correct_js = """async function submitDispatch() {
 const rId = document.getElementById('riderSelect').value;
 const rider = activeRiders.find(r => r.id === rId);
 const btn = document.getElementById('confirmDispatchBtn');
 
 if (!rider) {
 alert("Please select a rider from the dropdown.");
 return;
 }
 
 btn.disabled = true;
 btn.textContent = "Dispatching...";
 
 const { error } = await client.rpc('dispatch_order', {
 p_order_id: activeOrder.id,
 p_carrier_name: rider.name,
 p_carrier_phone: rider.phone
 });
 if (error) {
 alert("Dispatch error: " + error.message);
 btn.disabled = false;
 btn.textContent = "Assign Carrier / Hand Off";
 return;
 }
 
 alert("Order handed off! Opening WhatsApp to notify the customer...");
 closeModal();
 
 // --- WhatsApp Click-to-Chat Logic ---
 let cleanPhone = activeOrder.customer_phone.replace(/\\D/g, '');
 if (cleanPhone.startsWith('0')) cleanPhone = '254' + cleanPhone.substring(1);
 
 const msg = encodeURIComponent(`Hi ${activeOrder.customer_name}! 📦 Your Craft Atelier kit has just been handed over to our rider, ${rider.name} (${rider.phone}). They are on their way to ${activeOrder.delivery_address} and will call you shortly!`);
 
 const waUrl = `https://wa.me/${cleanPhone}?text=${msg}`;
 window.open(waUrl, '_blank');
 // ------------------------------------
 
 loadRiders();
 fetchNextOrder();
}"""
    
    new_content = content[:start_idx] + correct_js + content[end_idx:]
    with open('ops-packing.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("WhatsApp feature integrated successfully.")
else:
    print("Could not find function.")
