with open('admin-hub.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Scaffold Analytics at the top
analytics_html = """
    <!-- ANALYTICS SCAFFOLD -->
    <div class="dashboard-header">
        <h2>Analytics & Reports</h2>
        <p>High-level overview of fulfillment performance.</p>
    </div>
    <div style="display:flex; gap:15px; margin-bottom:40px;">
        <div class="card" style="flex:1; padding:20px; text-align:center;">
            <h3 style="color:#64748b; font-size:12px;">TODAY'S ORDERS</h3>
            <div style="font-size:32px; font-weight:800; color:#0f172a; margin-top:10px;">--</div>
        </div>
        <div class="card" style="flex:1; padding:20px; text-align:center;">
            <h3 style="color:#64748b; font-size:12px;">PENDING REVENUE</h3>
            <div style="font-size:32px; font-weight:800; color:#0f172a; margin-top:10px;">KES --</div>
        </div>
        <div class="card" style="flex:1; padding:20px; text-align:center;">
            <h3 style="color:#64748b; font-size:12px;">ON HOLD (ISSUES)</h3>
            <div style="font-size:32px; font-weight:800; color:#ef4444; margin-top:10px;">--</div>
        </div>
    </div>
"""

content = content.replace('<div class="dashboard-header">', analytics_html + '\n    <div class="dashboard-header">', 1)

# 2. Add Realtime Notifications script and verify logic logging
js_realtime = """
    // --- REALTIME NOTIFICATIONS ---
    client.channel('custom-insert-channel')
      .on('postgres_changes', { event: 'INSERT', schema: 'public', table: 'orders' }, payload => {
          alert(`🚨 NEW ORDER RECEIVED! Order #${payload.new.order_number} from ${payload.new.customer_name}.`);
          loadQueue();
          loadTracking('ALL');
      })
      .subscribe();
      
    // Modify verifyOrder to log audit trail
"""

content = content.replace('window.verifyOrder = async (id) => {', js_realtime + '\n    window.verifyOrder = async (id) => {')

# Inject audit log into verifyOrder
old_verify = """await client.from('orders').update({status: 'QUEUED_FOR_PACKING'}).eq('id', id);"""
new_verify = """await client.from('orders').update({status: 'QUEUED_FOR_PACKING'}).eq('id', id);
        
        // Audit log
        await client.from('order_audit_logs').insert([{
            order_id: id, old_status: 'PENDING_PAYMENT', new_status: 'QUEUED_FOR_PACKING',
            changed_by: 'Admin: ' + (await client.auth.getUser()).data.user.email,
            notes: 'Manually verified in Admin Hub'
        }]);"""
content = content.replace(old_verify, new_verify)

with open('admin-hub.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Admin Hub updated with Realtime and Analytics")
