import re

with open('ops-packing.html', 'r', encoding='utf-8') as f:
    content = f.read()

correct_js = """    async function submitDispatch() {
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
        
        alert("Order handed off successfully! Opening WhatsApp to notify customer...");
        closeModal();
        
        // --- WhatsApp Click-to-Chat Logic ---
        let cleanPhone = activeOrder.customer_phone.replace(/\D/g, '');
        if (cleanPhone.startsWith('0')) cleanPhone = '254' + cleanPhone.substring(1);
        
        const msg = encodeURIComponent(`Hi ${activeOrder.customer_name}! 🧶 Your Craft Atelier kit has just been handed over to our rider, ${rider.name} (${rider.phone}). They are on their way to ${activeOrder.delivery_address} and will call you shortly!`);
        
        const waUrl = `https://wa.me/${cleanPhone}?text=${msg}`;
        window.open(waUrl, '_blank');
        // ------------------------------------

        loadRiders();
        fetchNextOrder();
    }"""

content = re.sub(r"async function submitDispatch\(\) \{.*?(?=</script>)", correct_js + '\n', content, flags=re.DOTALL)

with open('ops-packing.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("WhatsApp integration added")
