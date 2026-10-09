import re

# --- 1. PATCH ADMIN HUB ---
with open('admin-hub.html', 'r', encoding='utf-8') as f:
    admin = f.read()

# Add Role to table header
admin = admin.replace('<th>Email</th><th>Name</th><th>Status</th>', '<th>Email</th><th>Name</th><th>Role</th><th>Status</th>')

# Update JS loadCommissioning
old_staff_render = '''sTbody.innerHTML += `<tr><td>${s.email}</td><td>${s.name}</td><td>${badge}</td><td>${btn}</td></tr>`;'''
new_staff_render = '''sTbody.innerHTML += `<tr><td>${s.email}</td><td>${s.name}</td><td><strong style="text-transform:uppercase;font-size:11px;color:#64748b;">${s.role}</strong></td><td>${badge}</td><td>${btn}</td></tr>`;'''
admin = admin.replace(old_staff_render, new_staff_render)

# Update addStaff prompt
old_add_staff = '''const name = prompt("Enter staff name:");
        if(!name) return;
        await client.from('staff_directory').insert([{email, name}]);'''
new_add_staff = '''const name = prompt("Enter staff name:");
        if(!name) return;
        let role = prompt("Enter role (packer, dispatcher, or admin):", "packer");
        if (!['packer', 'dispatcher', 'admin'].includes(role)) role = 'packer';
        await client.from('staff_directory').insert([{email, name, role}]);'''
admin = admin.replace(old_add_staff, new_add_staff)

with open('admin-hub.html', 'w', encoding='utf-8') as f:
    f.write(admin)

# --- 2. PATCH OPS PACKING ---
with open('ops-packing.html', 'r', encoding='utf-8') as f:
    ops = f.read()

# Add logic for initializeStation
init_js = """
    let currentUserRole = 'packer';
    let currentUserName = 'Staff';

    async function initializeStation() {
        const { data: { session } } = await client.auth.getSession();
        if (session && session.user) {
            const { data } = await client.from('staff_directory').select('name, role').eq('email', session.user.email).maybeSingle();
            if (data) {
                currentUserRole = data.role;
                currentUserName = data.name;
                document.getElementById('staffLabel').textContent = `${currentUserName} (${currentUserRole.toUpperCase()})`;
            }
        }
        loadRiders();
        fetchNextOrder();
    }
"""

ops = ops.replace('let activeOrder = null;', init_js + '\n let activeOrder = null;')

# Update fetchNextOrder query
old_fetch = """.in('status', ['QUEUED_FOR_PACKING', 'PACKING_IN_PROGRESS', 'STAGED_FOR_DISPATCH'])"""
new_fetch = """
 .in('status', currentUserRole === 'packer' ? ['QUEUED_FOR_PACKING', 'PACKING_IN_PROGRESS'] : 
               currentUserRole === 'dispatcher' ? ['STAGED_FOR_DISPATCH'] : 
               ['QUEUED_FOR_PACKING', 'PACKING_IN_PROGRESS', 'STAGED_FOR_DISPATCH'])
"""
ops = ops.replace(old_fetch, new_fetch.strip())

# Update DOMContentLoaded
old_dom = '''window.addEventListener('DOMContentLoaded', () => {
 loadRiders();
 fetchNextOrder();
 });'''
new_dom = '''window.addEventListener('DOMContentLoaded', initializeStation);'''
ops = ops.replace(old_dom, new_dom)

with open('ops-packing.html', 'w', encoding='utf-8') as f:
    f.write(ops)

print("Patch successful")
