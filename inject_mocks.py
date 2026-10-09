import re

def update_storefront():
    with open('storefront.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Add mock mode logic
    if 'if (SUPABASE_URL.includes("YOUR_PROJECT_REF"))' not in content:
        # loadCatalog replacement
        content = content.replace(
            "const { data: kits, error } = await client.from('kits').select('*').order('price_cents', { ascending: true });",
            "if (SUPABASE_URL.includes('YOUR_PROJECT_REF')) { renderKitCard({ id: '1', title: 'Everyday Ribbed Shoulder Bag Kit', description: 'Zero-frustration starter project.', price_cents: 345000 }); renderKitCard({ id: '2', title: 'Checkerboard Mini Bucket Hat Kit', description: 'Y2K-inspired streetwear bucket hat in two-tone checkerboard blocks.', price_cents: 285000 }); return; }\n const { data: kits, error } = await client.from('kits').select('*').order('price_cents', { ascending: true });"
        )
        # submitOrder replacement
        content = content.replace(
            "const { data, error } = await client.from('orders').insert([{",
            "if (SUPABASE_URL.includes('YOUR_PROJECT_REF')) { alert('Mock Mode: Order placed successfully! (No DB connection)'); closeModal(); btn.disabled = false; btn.textContent = 'Place Order'; return; }\n const { data, error } = await client.from('orders').insert([{"
        )
        with open('storefront.html', 'w', encoding='utf-8') as f:
            f.write(content)

def update_ops():
    with open('ops-packing.html', 'r', encoding='utf-8') as f:
        content = f.read()

    if 'if (SUPABASE_URL.includes("YOUR_PROJECT_REF"))' not in content:
        content = content.replace(
            "const { data, error } = await client",
            "if (SUPABASE_URL.includes('YOUR_PROJECT_REF')) { activeOrder = { id: 'mock', order_number: 1042, kit_name: 'Everyday Ribbed Bag', customer_name: 'Jasmine Wambui', customer_phone: '+254 712 345 678', delivery_type: 'rider', delivery_address: 'Kilimani, Wood Ave', delivery_notes: 'Leave at security', status: 'QUEUED_FOR_PACKING' }; activeOrder.status = 'PACKING_IN_PROGRESS'; renderOrderView(); return; }\n const { data, error } = await client"
        )
        content = content.replace(
            "const { error } = await client.rpc('verify_and_stage_order', {",
            "if (SUPABASE_URL.includes('YOUR_PROJECT_REF')) { setTimeout(() => { activeOrder.status = 'STAGED_FOR_DISPATCH'; renderOrderView(); }, 500); return; }\n const { error } = await client.rpc('verify_and_stage_order', {"
        )
        content = content.replace(
            "const { error } = await client.rpc('dispatch_order', {",
            "if (SUPABASE_URL.includes('YOUR_PROJECT_REF')) { setTimeout(() => { alert('Mock Mode: Dispatched!'); closeModal(); fetchNextOrder(); }, 500); return; }\n const { error } = await client.rpc('dispatch_order', {"
        )
        with open('ops-packing.html', 'w', encoding='utf-8') as f:
            f.write(content)

def update_admin():
    with open('admin-hub.html', 'r', encoding='utf-8') as f:
        content = f.read()

    if 'if (SUPABASE_URL.includes("YOUR_PROJECT_REF"))' not in content:
        content = content.replace(
            "const { data: orders } = await client.from('orders').select('*').order('created_at', { ascending: false });",
            "if (SUPABASE_URL.includes('YOUR_PROJECT_REF')) { document.getElementById('kpiActive').textContent = '12'; document.getElementById('kpiPacked').textContent = '4'; document.getElementById('kpiRevenue').textContent = 'KES 41,400'; document.getElementById('ordersTableBody').innerHTML = '<tr><td>#1042</td><td>Jasmine Wambui<br><span style=\"color:var(--muted); font-size:11px;\">+254 712 345 678</span></td><td>Everyday Ribbed Bag</td><td><span class=\"status-pill\" style=\"background: rgba(255,255,255,0.1);\">PACKING_IN_PROGRESS</span></td><td>RIDER</td><td><button class=\"btn-sm btn-override\" onclick=\"alert(\\'Mock Override\\')\">Admin Intervene</button></td></tr>'; return; }\n const { data: orders } = await client.from('orders').select('*').order('created_at', { ascending: false });"
        )
        with open('admin-hub.html', 'w', encoding='utf-8') as f:
            f.write(content)

update_storefront()
update_ops()
update_admin()
print("Mocks injected successfully.")
