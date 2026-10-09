import re

with open('storefront.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace hardcoded till with an ID
content = content.replace('<h3>123 456</h3>', '<h3 id="dynamicTill">Loading...</h3>')

# Add JS to load it
js_load = """
    async function fetchBusinessSettings() {
        const { data } = await client.from('business_settings').select('*');
        if(data) {
            const till = data.find(s => s.setting_key === 'mpesa_till');
            if(till && document.getElementById('dynamicTill')) {
                document.getElementById('dynamicTill').innerText = till.setting_value;
            }
        }
    }
"""

content = content.replace('let cart = [];', js_load + '\nlet cart = [];')
content = content.replace('loadCatalog();', 'loadCatalog();\n fetchBusinessSettings();')

with open('storefront.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Storefront updated")
