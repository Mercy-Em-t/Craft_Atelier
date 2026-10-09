import re

with open('admin-hub.html', 'r', encoding='utf-8') as f:
    content = f.read()

tracking_html = '''
    <div class="dashboard-header" style="margin-top: 60px;">
        <h2>Order Tracking Board</h2>
        <p>Monitor the real-time status of all orders across the fulfillment pipeline.</p>
    </div>

    <div class="card">
        <div class="card-header" style="display: flex; gap: 10px; flex-wrap: wrap; background: #f8fafc; padding: 12px 20px;">
            <button class="btn-verify filter-btn" style="background: #0f172a;" onclick="loadTracking('ALL')">All</button>
            <button class="btn-verify filter-btn" style="background: #64748b;" onclick="loadTracking('QUEUED_FOR_PACKING')">Queued</button>
            <button class="btn-verify filter-btn" style="background: #eab308; color: #422006;" onclick="loadTracking('PACKING_IN_PROGRESS')">Packing</button>
            <button class="btn-verify filter-btn" style="background: #8b5cf6;" onclick="loadTracking('STAGED_FOR_DISPATCH')">Ready for Delivery</button>
            <button class="btn-verify filter-btn" style="background: #3b82f6;" onclick="loadTracking('IN_TRANSIT')">In Transit</button>
            <button class="btn-verify filter-btn" style="background: #10b981;" onclick="loadTracking('DELIVERED')">Delivered</button>
        </div>
        <div class="table-wrapper">
            <table>
                <thead>
                    <tr>
                        <th>Order #</th>
                        <th>Customer</th>
                        <th>Kit Summary</th>
                        <th>Date</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody id="trackingList">
                    <tr><td colspan="5" class="empty-state">Loading...</td></tr>
                </tbody>
            </table>
        </div>
    </div>
'''

# Insert the new HTML before the Commissioning header
content = content.replace('<div class="dashboard-header" style="margin-top: 60px;">\n        <h2>Commissioning & Fleet</h2>', tracking_html + '\n    <div class="dashboard-header" style="margin-top: 60px;">\n        <h2>Commissioning & Fleet</h2>')

tracking_js = '''
    window.loadTracking = async (statusFilter = 'ALL') => {
        let query = client.from('orders').select('*').order('created_at', {ascending: false}).limit(50);
        
        if (statusFilter !== 'ALL') {
            query = query.eq('status', statusFilter);
        }

        const { data, error } = await query;
        const tbody = document.getElementById('trackingList');
        tbody.innerHTML = '';
        
        if (error) {
            tbody.innerHTML = <tr><td colspan="5" class="empty-state">Error: </td></tr>;
            return;
        }
        
        if (!data || data.length === 0) {
            tbody.innerHTML = '<tr><td colspan="5" class="empty-state">No orders found for this filter.</td></tr>';
            return;
        }

        data.forEach(order => {
            const date = new Date(order.created_at).toLocaleDateString();
            
            // Generate a nice badge for the status
            let badgeStyle = "background: #f1f5f9; color: #475569;"; // Default
            if(order.status === 'PENDING_PAYMENT') badgeStyle = "background: #fef08a; color: #854d0e;";
            if(order.status === 'QUEUED_FOR_PACKING') badgeStyle = "background: #e2e8f0; color: #334155;";
            if(order.status === 'PACKING_IN_PROGRESS') badgeStyle = "background: #fef08a; color: #854d0e;";
            if(order.status === 'STAGED_FOR_DISPATCH') badgeStyle = "background: #ede9fe; color: #5b21b6;";
            if(order.status === 'IN_TRANSIT') badgeStyle = "background: #dbeafe; color: #1e40af;";
            if(order.status === 'DELIVERED') badgeStyle = "background: #dcfce7; color: #166534;";
            
            const badge = <span class="badge" style=""></span>;

            tbody.innerHTML += 
                <tr>
                    <td><strong>#</strong></td>
                    <td><br><span style="font-size:12px;color:#64748b"></span></td>
                    <td></td>
                    <td></td>
                    <td></td>
                </tr>
            ;
        });
    };
'''

content = content.replace('loadCommissioning();', 'loadCommissioning();\n        loadTracking();')
content = content.replace('window.addRider = async () => {', tracking_js + '\n    window.addRider = async () => {')

with open('admin-hub.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("admin-hub tracking added")
