import re

with open('storefront.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the second declaration.
old_str = "   const btn = document.getElementById('submitOrderBtn');\n   btn.disabled = true;"
new_str = "   btn.disabled = true;"

if old_str in content:
    content = content.replace(old_str, new_str)
    
with open('storefront.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("SyntaxError fixed!")
