import re

files = ['storefront.html', 'ops-packing.html', 'admin-hub.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove mock blocks
    content = re.sub(r"if \(SUPABASE_URL\.includes\('YOUR_PROJECT_REF'\)\) \{.*?return; \}\n\s*", "", content, flags=re.DOTALL)
    
    # 2. Convert to ES Module for Vite env variables
    content = content.replace('<script>', '<script type="module">')
    
    # 3. Replace hardcoded keys with Vite env variables
    content = re.sub(r'const SUPABASE_URL = ".*?";', 'const SUPABASE_URL = import.meta.env.VITE_SUPABASE_URL;', content)
    content = re.sub(r'const SUPABASE_ANON_KEY = ".*?";', 'const SUPABASE_ANON_KEY = import.meta.env.VITE_SUPABASE_ANON_KEY;', content)
    content = re.sub(r'const SUPABASE_SERVICE_OR_ADMIN_KEY = ".*?";', 'const SUPABASE_SERVICE_OR_ADMIN_KEY = import.meta.env.VITE_SUPABASE_ANON_KEY; // Requires Supabase Auth login for Admin JWT in production', content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Mocks stripped and environment variables injected.")
