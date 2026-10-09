import re

with open('admin-hub.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Tracking Board HTML to show resolution buttons for ON_HOLD
old_action = """${order.status === 'IN_TRANSIT' ? `<br><button class="btn-verify" style="margin-top:6px; background:#10b981; font-size:10px; padding:2px 6px;" onclick="markDelivered('${order.id}', '${order.delivery_pin}')">Complete Delivery</button>` : ''}"""

new_action = """${order.status === 'IN_TRANSIT' ? `<br><button class="btn-verify" style="margin-top:6px; background:#10b981; font-size:10px; padding:2px 6px;" onclick="markDelivered('${order.id}', '${order.delivery_pin}')">Complete Delivery</button>` : ''}
                        ${order.status === 'ON_HOLD' ? `<br>
                            <button class="btn-verify" style="margin-top:6px; background:#3b82f6; font-size:10px; padding:2px 6px;" onclick="resolveIssue('${order.id}')">Resolve & Re-Queue</button>
                            <button class="btn-verify" style="margin-top:4px; background:#ef4444; font-size:10px; padding:2px 6px;" onclick="cancelOrder('${order.id}')">Cancel Order</button>
                        ` : ''}"""

content = content.replace(old_action, new_action)

# 2. Inject the JS functions to handle the resolution
js_inject = """
    window.resolveIssue = async (id) => {
        const confirmResolve = confirm("Have you secured the missing items? This will send the order back to the warehouse floor for packing.");
        if(!confirmResolve) return;
        
        const staffEmail = (await client.auth.getUser()).data.user.email;
        await client.from('orders').update({status: 'QUEUED_FOR_PACKING', delivery_notes: 'ISSUE RESOLVED'}).eq('id', id);
        
        await client.from('order_audit_logs').insert([{
            order_id: id, old_status: 'ON_HOLD', new_status: 'QUEUED_FOR_PACKING',
            changed_by: 'Admin: ' + staffEmail, notes: 'Admin resolved stock issue'
        }]);
        
        alert("Order successfully re-queued for packing!");
        loadTracking('ALL');
        loadAnalytics();
    };

    window.cancelOrder = async (id) => {
        const reason = prompt("Enter reason for cancellation / refund:");
        if(!reason) return;
        
        const staffEmail = (await client.auth.getUser()).data.user.email;
        await client.from('orders').update({status: 'CANCELLED', delivery_notes: 'CANCELLED: ' + reason}).eq('id', id);
        
        await client.from('order_audit_logs').insert([{
            order_id: id, old_status: 'ON_HOLD', new_status: 'CANCELLED',
            changed_by: 'Admin: ' + staffEmail, notes: 'Order Cancelled: ' + reason
        }]);
        
        alert("Order Cancelled.");
        loadTracking('ALL');
        loadAnalytics();
    };
"""

content = content.replace('window.markDelivered = async (id, correctPin) => {', js_inject + '\n    window.markDelivered = async (id, correctPin) => {')

with open('admin-hub.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Admin Hub updated with ON_HOLD resolution buttons")
