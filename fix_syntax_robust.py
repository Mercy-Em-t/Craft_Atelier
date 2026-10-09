import re

with open('storefront.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the second 'const btn = ...' with just 'btn = ...' or remove the 'const'
# A robust way is to just do re.sub but only for the second occurrence.
# Actually, the simplest is to replace `const btn = ` with `btn = ` globally, but wait! The first one needs a `const` or `let`.
# Let's change the first one to `let btn = ` and the second to `btn = `.

# Find all indices
lines = content.split('\n')
btn_count = 0
for i, line in enumerate(lines):
    if "btn = document.getElementById('submitOrderBtn')" in line:
        btn_count += 1
        if btn_count == 1:
            lines[i] = line.replace("const btn", "let btn")
        elif btn_count == 2:
            lines[i] = line.replace("const btn", "btn")

content = '\n'.join(lines)

with open('storefront.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Syntax fixed robustly!")
