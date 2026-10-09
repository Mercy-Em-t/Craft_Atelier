import re
import json

with open('admin-hub.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update loadAdminExtras to filter out archived kits, and pass the entire kit object to editKit
old_catalog_load = "const { data: kits } = await client.from('kits').select('*').order('title');"
new_catalog_load = "const { data: kits } = await client.from('kits').select('*').eq('is_archived', false).order('title');"
content = content.replace(old_catalog_load, new_catalog_load)

# Fix editKit call to pass full JSON object (escaped)
old_btn = """<button class="btn-verify" style="background:#64748b; padding:4px 8px; font-size:12px;" onclick="editKit('${k.id}', '${k.title}', ${k.price_cents}, ${k.inventory_count})">Edit</button>"""
new_btn = """<button class="btn-verify" style="background:#64748b; padding:4px 8px; font-size:12px;" onclick='editKit(${JSON.stringify(k)})'>Edit</button>"""
content = content.replace(old_btn, new_btn)

# 2. Update addKit and editKit
old_js = """    window.addKit = async () => {
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
    };"""

new_js = """    window.addKit = async () => {
        const choice = prompt("Enter '1' to add a Single Kit manually.\\nEnter '2' to Bulk Import kits via JSON array.");
        
        if (choice === '1') {
            const title = prompt("Enter new kit title:");
            if(!title) return;
            const slug = title.toLowerCase().replace(/[^a-z0-9]+/g, '-');
            const price = prompt("Enter price in KES (e.g. 2500):", "2500");
            if(!price) return;
            const stock = prompt("Enter initial inventory count:", "10");
            
            await client.from('kits').insert([{
                title, slug, price_cents: parseInt(price)*100, inventory_count: parseInt(stock),
                description: 'New craft kit', category: 'DIY Kit', image_urls: ['https://via.placeholder.com/400'], bom_items: [], is_archived: false
            }]);
            loadAdminExtras();
        } else if (choice === '2') {
            const jsonStr = prompt("Paste your JSON array of kits here:\\nExample: [{title: 'A', price_cents: 1000}, ...]");
            if(!jsonStr) return;
            try {
                let parsed = JSON.parse(jsonStr);
                if(!Array.isArray(parsed)) parsed = [parsed];
                
                const toInsert = parsed.map(k => ({
                    title: k.title || 'Untitled',
                    slug: (k.title || 'Untitled').toLowerCase().replace(/[^a-z0-9]+/g, '-'),
                    price_cents: k.price_cents || 0,
                    inventory_count: k.inventory_count || 0,
                    description: k.description || '',
                    category: k.category || 'DIY Kit',
                    image_urls: k.image_urls || [],
                    bom_items: k.bom_items || [],
                    is_archived: false
                }));
                
                const { error } = await client.from('kits').insert(toInsert);
                if(error) alert("Import Error: " + error.message);
                else alert("Successfully imported " + toInsert.length + " kits!");
                
                loadAdminExtras();
            } catch (err) {
                alert("Invalid JSON format. Please try again.");
            }
        }
    };

    window.editKit = async (k) => {
        const stock = prompt(`Update inventory for ${k.title}:`, k.inventory_count);
        if(stock === null) return;
        const price = prompt(`Update price (KES) for ${k.title}:`, k.price_cents / 100);
        if(price === null) return;

        // 1. Archive the old record
        await client.from('kits').update({ is_archived: true }).eq('id', k.id);
        
        // 2. Insert the new record pointing to the old one as parent
        await client.from('kits').insert([{
            title: k.title, slug: k.slug,
            price_cents: parseInt(price)*100, inventory_count: parseInt(stock),
            description: k.description, category: k.category, 
            image_urls: k.image_urls, bom_items: k.bom_items,
            parent_id: k.id, is_archived: false
        }]);
        
        loadAdminExtras();
    };"""

content = content.replace(old_js, new_js)

with open('admin-hub.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Admin Hub updated with versioning and bulk import")
