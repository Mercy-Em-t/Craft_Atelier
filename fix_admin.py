import re

with open('admin-hub.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I will just write a regex to replace the entire script block that was injected.
# Or better, just rewrite the JS functions correctly.

correct_js = """
    async function loadCommissioning() {
        // Load Riders
        const { data: riders } = await client.from('riders').select('*').order('created_at', {ascending: false});
        const rTbody = document.getElementById('ridersList');
        rTbody.innerHTML = '';
        (riders || []).forEach(r => {
            const btn = r.status === 'active' 
                ? `<button class="btn-verify" style="background: #dc2626;" onclick="toggleRider('${r.id}', 'inactive')">Suspend</button>`
                : `<button class="btn-verify" style="background: #16a34a;" onclick="toggleRider('${r.id}', 'active')">Activate</button>`;
            const badge = r.status === 'active' ? `<span class="badge" style="background:#dcfce7;color:#166534">ACTIVE</span>` : `<span class="badge" style="background:#fee2e2;color:#991b1b">INACTIVE</span>`;
            rTbody.innerHTML += `<tr><td>${r.name}</td><td>${r.phone}</td><td>${badge}</td><td>${btn}</td></tr>`;
        });

        // Load Staff
        const { data: staff } = await client.from('staff_directory').select('*').order('created_at', {ascending: false});
        const sTbody = document.getElementById('staffList');
        sTbody.innerHTML = '';
        if(!staff || staff.length === 0) sTbody.innerHTML = '<tr><td colspan="4" class="empty-state">No staff listed yet.</td></tr>';
        (staff || []).forEach(s => {
            const btn = s.status === 'active' 
                ? `<button class="btn-verify" style="background: #dc2626;" onclick="toggleStaff('${s.id}', 'revoked')">Revoke</button>`
                : `<button class="btn-verify" style="background: #16a34a;" onclick="toggleStaff('${s.id}', 'active')">Restore</button>`;
            const badge = s.status === 'active' ? `<span class="badge" style="background:#dcfce7;color:#166534">ACTIVE</span>` : `<span class="badge" style="background:#fee2e2;color:#991b1b">REVOKED</span>`;
            sTbody.innerHTML += `<tr><td>${s.email}</td><td>${s.name}</td><td>${badge}</td><td>${btn}</td></tr>`;
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
"""

# Find everything from "async function loadCommissioning()" to the end of the script block.
pattern = r"async function loadCommissioning\(\) \{.*"
# Use dotall to match across newlines up to </script>
content = re.sub(r"async function loadCommissioning\(\) \{.*?(?=</script>)", correct_js, content, flags=re.DOTALL)

with open('admin-hub.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("admin-hub repaired")
