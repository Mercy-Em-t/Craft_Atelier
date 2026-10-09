import re

with open('admin-hub.html', 'r', encoding='utf-8') as f:
    content = f.read()

correct_js = """    window.loadTracking = async (statusFilter = 'ALL') => {
        let query = client.from('orders').select('*').order('created_at', {ascending: false}).limit(50);
        
        if (statusFilter !== 'ALL') {
            query = query.eq('status', statusFilter);
        }

        const { data, error } = await query;
        const tbody = document.getElementById('trackingList');
        tbody.innerHTML = '';
        
        if (error) {
            tbody.innerHTML = `<tr><td colspan="5" class="empty-state">Error: ${error.message}</td></tr>`;
            return;
        }
        
        if (!data || data.length === 0) {
            tbody.innerHTML = '<tr><td colspan="5" class="empty-state">No orders found for this filter.</td></tr>';
            return;
        }

        data.forEach(order => {
            const date = new Date(order.created_at).toLocaleDateString();
            
            let badgeStyle = "background: #f1f5f9; color: #475569;";
            if(order.status === 'PENDING_PAYMENT') badgeStyle = "background: #fef08a; color: #854d0e;";
            if(order.status === 'QUEUED_FOR_PACKING') badgeStyle = "background: #e2e8f0; color: #334155;";
            if(order.status === 'PACKING_IN_PROGRESS') badgeStyle = "background: #fef08a; color: #854d0e;";
            if(order.status === 'STAGED_FOR_DISPATCH') badgeStyle = "background: #ede9fe; color: #5b21b6;";
            if(order.status === 'IN_TRANSIT') badgeStyle = "background: #dbeafe; color: #1e40af;";
            if(order.status === 'DELIVERED') badgeStyle = "background: #dcfce7; color: #166534;";
            
            const badge = `<span class="badge" style="${badgeStyle}">${order.status.replace(/_/g, ' ')}</span>`;

            tbody.innerHTML += `
                <tr>
                    <td><strong>#${order.order_number}</strong></td>
                    <td>${order.customer_name}<br><span style="font-size:12px;color:#64748b">${order.customer_phone}</span></td>
                    <td>${order.kit_name}</td>
                    <td>${date}</td>
                    <td>${badge}</td>
                </tr>
            `;
        });
    };
"""

content = re.sub(r"window\.loadTracking = async \(statusFilter = 'ALL'\) => \{.*?(?=window\.addRider = async)", correct_js, content, flags=re.DOTALL)

with open('admin-hub.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Tracking fixed")
