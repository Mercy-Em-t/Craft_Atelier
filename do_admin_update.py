with open('admin-hub.html', 'r', encoding='utf-8') as f:
    content = f.read()

html_inject = """
    <!-- CATALOG MANAGEMENT -->
    <div class="dashboard-header" style="margin-top: 60px;">
        <h2>Catalog & Inventory</h2>
        <p>Manage product listings, pricing, and stock levels.</p>
    </div>
    <div class="card">
        <div class="card-header" style="display: flex; justify-content: space-between; align-items: center;">
            <span>Product Catalog</span>
            <button class="btn-verify" style="background: #2563eb;" onclick="addKit()">+ Add New Kit</button>
        </div>
        <div class="table-wrapper">
            <table>
                <thead><tr><th>Kit Title</th><th>Price (KES)</th><th>Inventory</th><th>Status</th><th>Action</th></tr></thead>
                <tbody id="catalogList"><tr><td colspan="5" class="empty-state">Loading...</td></tr></tbody>
            </table>
        </div>
    </div>

    <!-- BUSINESS SETTINGS -->
    <div class="dashboard-header" style="margin-top: 60px;">
        <h2>Business Settings</h2>
        <p>Global configurations for the storefront and operations.</p>
    </div>
    <div class="card" style="padding: 20px;">
        <div style="margin-bottom: 16px;">
            <label style="display:block; font-size:12px; font-weight:600; color:#64748b; margin-bottom:6px;">M-PESA TILL / PAYBILL NUMBER</label>
            <div style="display:flex; gap:10px;">
                <input type="text" id="settingMpesa" style="padding:10px; border:1px solid #e2e8f0; border-radius:6px; flex:1;" placeholder="e.g. 123456">
                <button class="btn-verify" style="background: #16a34a;" onclick="saveSetting('mpesa_till', document.getElementById('settingMpesa').value)">Save</button>
            </div>
            <p style="font-size:12px; color:#94a3b8; margin-top:6px;">This number is displayed to customers during the checkout process.</p>
        </div>
    </div>
</div> <!-- End of container -->
"""

js_inject = """
    // --- CATALOG & SETTINGS ---
    async function loadAdminExtras() {
        // Load Settings
        const { data: settings } = await client.from('business_settings').select('*');
        if(settings) {
            const till = settings.find(s => s.setting_key === 'mpesa_till');
            if(till) document.getElementById('settingMpesa').value = till.setting_value;
        }

        // Load Catalog
        const { data: kits } = await client.from('kits').select('*').order('title');
        const cTbody = document.getElementById('catalogList');
        cTbody.innerHTML = '';
        (kits || []).forEach(k => {
            const stockBadge = k.inventory_count > 0 
                ? `<span class="badge" style="background:#dcfce7;color:#166534">IN STOCK</span>` 
                : `<span class="badge" style="background:#fee2e2;color:#991b1b">OUT OF STOCK</span>`;
            
            cTbody.innerHTML += `
                <tr>
                    <td><strong>${k.title}</strong><br><small style="color:#64748b;">/${k.slug}</small></td>
                    <td>KES ${(k.price_cents / 100).toLocaleString()}</td>
                    <td>${k.inventory_count} units</td>
                    <td>${stockBadge}</td>
                    <td>
                        <button class="btn-verify" style="background:#64748b; padding:4px 8px; font-size:12px;" onclick="editKit('${k.id}', '${k.title}', ${k.price_cents}, ${k.inventory_count})">Edit</button>
                    </td>
                </tr>
            `;
        });
    }

    window.addKit = async () => {
        const title = prompt("Enter new kit title:");
        if(!title) return;
        const slug = title.toLowerCase().replace(/[^a-z0-9]+/g, '-');
        const price = prompt("Enter price in KES (e.g. 2500):", "2500");
        if(!price) return;
        const stock = prompt("Enter initial inventory count:", "10");
        
        await client.from('kits').insert([{
            title, slug, price_cents: parseInt(price)*100, inventory_count: parseInt(stock),
            description: 'New craft kit', category: 'DIY Kit', image_urls: ['https://via.placeholder.com/400'], bom_items: []
        }]);
        loadAdminExtras();
    };

    window.editKit = async (id, oldTitle, oldPrice, oldStock) => {
        const stock = prompt(`Update inventory for ${oldTitle}:`, oldStock);
        if(stock === null) return;
        const price = prompt(`Update price (KES) for ${oldTitle}:`, oldPrice / 100);
        if(price === null) return;

        await client.from('kits').update({
            inventory_count: parseInt(stock),
            price_cents: parseInt(price)*100
        }).eq('id', id);
        loadAdminExtras();
    };

    window.saveSetting = async (key, val) => {
        if(!val) return;
        await client.from('business_settings').upsert({setting_key: key, setting_value: val});
        alert("Setting saved successfully!");
    };
"""

# Inject HTML right before the final </div> closing the container
content = content.replace('</div>\n\n<script>', html_inject + '\n<script>')

# Inject JS
content = content.replace('loadCommissioning();', 'loadCommissioning();\n        loadAdminExtras();')
content = content.replace('window.addRider = async () => {', js_inject + '\n    window.addRider = async () => {')

with open('admin-hub.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Admin updated with Catalog and Settings")
