import re

with open('admin-hub.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_tracking = """<td>${date}</td>
                    <td>${badge}</td>"""
new_tracking = """<td>${date}</td>
                    <td>
                        ${badge}
                        ${order.status === 'IN_TRANSIT' ? `<br><button class="btn-verify" style="margin-top:6px; background:#10b981; font-size:10px; padding:2px 6px;" onclick="markDelivered('${order.id}', '${order.delivery_pin}')">Complete Delivery</button>` : ''}
                    </td>"""
content = content.replace(old_tracking, new_tracking)

js_inject = """
    window.markDelivered = async (id, correctPin) => {
        const pin = prompt("Enter the 4-digit Delivery PIN provided by the customer:");
        if (!pin) return;
        
        if (pin === correctPin) {
            const { error } = await client.from('orders').update({status: 'DELIVERED'}).eq('id', id);
            
            await client.from('order_audit_logs').insert([{
                order_id: id, old_status: 'IN_TRANSIT', new_status: 'DELIVERED',
                changed_by: 'Admin / Rider App', notes: 'Delivery confirmed with valid PIN.'
            }]);
            
            if(!error) {
                alert("Order successfully marked as DELIVERED!");
                loadTracking('ALL');
            }
        } else {
            alert("❌ Invalid PIN. Please confirm the PIN with the customer.");
        }
    };
"""

content = content.replace('window.loadTracking = async (statusFilter = \'ALL\') => {', js_inject + '\n    window.loadTracking = async (statusFilter = \'ALL\') => {')

with open('admin-hub.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Admin Tracking updated with Delivery PIN logic")
