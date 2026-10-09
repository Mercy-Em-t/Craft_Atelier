import re

with open('admin-hub.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_html = '''
    <div class="dashboard-header" style="margin-top: 60px;">
        <h2>Commissioning & Fleet</h2>
        <p>Manage your delivery riders and warehouse staff directory.</p>
    </div>

    <div class="card">
        <div class="card-header" style="display: flex; justify-content: space-between; align-items: center;">
            <span>Riders Fleet</span>
            <button class="btn-verify" style="background: #2563eb;" onclick="addRider()">+ Add Rider</button>
        </div>
        <div class="table-wrapper">
            <table>
                <thead><tr><th>Name</th><th>Phone</th><th>Status</th><th>Action</th></tr></thead>
                <tbody id="ridersList"><tr><td colspan="4" class="empty-state">Loading...</td></tr></tbody>
            </table>
        </div>
    </div>

    <div class="card">
        <div class="card-header" style="display: flex; justify-content: space-between; align-items: center;">
            <span>Staff Directory</span>
            <button class="btn-verify" style="background: #2563eb;" onclick="addStaff()">+ Add Staff</button>
        </div>
        <div class="table-wrapper">
            <table>
                <thead><tr><th>Email</th><th>Name</th><th>Status</th><th>Action</th></tr></thead>
                <tbody id="staffList"><tr><td colspan="4" class="empty-state">Loading...</td></tr></tbody>
            </table>
        </div>
    </div>
</div>
'''

content = content.replace('</div>\n\n<script>', new_html + '\n<script>')

js_inject = '''
    async function loadCommissioning() {
        // Load Riders
        const { data: riders } = await client.from('riders').select('*').order('created_at', {ascending: false});
        const rTbody = document.getElementById('ridersList');
        rTbody.innerHTML = '';
        (riders || []).forEach(r => {
            const btn = r.status === 'active' 
                ? <button class="btn-verify" style="background: #dc2626;" onclick="toggleRider('', 'inactive')">Suspend</button>
                : <button class="btn-verify" style="background: #16a34a;" onclick="toggleRider('', 'active')">Activate</button>;
            const badge = r.status === 'active' ? <span class="badge" style="background:#dcfce7;color:#166534">ACTIVE</span> : <span class="badge" style="background:#fee2e2;color:#991b1b">INACTIVE</span>;
            rTbody.innerHTML += <tr><td></td><td></td><td></td><td></td></tr>;
        });

        // Load Staff
        const { data: staff } = await client.from('staff_directory').select('*').order('created_at', {ascending: false});
        const sTbody = document.getElementById('staffList');
        sTbody.innerHTML = '';
        if(!staff || staff.length === 0) sTbody.innerHTML = '<tr><td colspan="4" class="empty-state">No staff listed yet.</td></tr>';
        (staff || []).forEach(s => {
            const btn = s.status === 'active' 
                ? <button class="btn-verify" style="background: #dc2626;" onclick="toggleStaff('', 'revoked')">Revoke</button>
                : <button class="btn-verify" style="background: #16a34a;" onclick="toggleStaff('', 'active')">Restore</button>;
            const badge = s.status === 'active' ? <span class="badge" style="background:#dcfce7;color:#166534">ACTIVE</span> : <span class="badge" style="background:#fee2e2;color:#991b1b">REVOKED</span>;
            sTbody.innerHTML += <tr><td></td><td></td><td></td><td></td></tr>;
        });
    }

    window.addRider = async () => {
        const name = prompt("Enter rider name:");
        if(!name) return;
        const phone = prompt("Enter phone number:");
        if(!phone) return;
        await client.from('riders').insert([{name, phone}]);
        loadCommissioning();
    };

    window.toggleRider = async (id, newStatus) => {
        await client.from('riders').update({status: newStatus}).eq('id', id);
        loadCommissioning();
    };

    window.addStaff = async () => {
        const email = prompt("Enter staff email:");
        if(!email) return;
        const name = prompt("Enter staff name:");
        if(!name) return;
        await client.from('staff_directory').insert([{email, name}]);
        loadCommissioning();
    };

    window.toggleStaff = async (id, newStatus) => {
        await client.from('staff_directory').update({status: newStatus}).eq('id', id);
        loadCommissioning();
    };
'''

content = content.replace('loadVerificationQueue();', 'loadVerificationQueue();\n        loadCommissioning();')
content = content.replace('</script>', js_inject + '\n</script>')

with open('admin-hub.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("admin-hub patched")
