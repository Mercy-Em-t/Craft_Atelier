with open('storefront.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_load = "const { data, error } = await client.from('kits').select('*');"
new_load = "const { data, error } = await client.from('kits').select('*').eq('is_archived', false);"
content = content.replace(old_load, new_load)

with open('storefront.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Storefront updated")
