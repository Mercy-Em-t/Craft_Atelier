import re

files = ['storefront.html', 'ops-packing.html', 'admin-hub.html']

url = '"https://yjgskbdtnyzsmuzvnrsz.supabase.co"'
key = '"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlqZ3NrYmR0bnl6c211enZucnN6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTA5NDQ5NzEsImV4cCI6MjEwNjUyMDk3MX0.elz2qyCCXBRFTCdbzqYqoiltkkmBALKrQhAv-I4SC7Q"'

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Revert to standard script tags (python server doesn't need modules if we aren't using import.meta)
    content = content.replace('<script type="module">', '<script>')

    content = content.replace('import.meta.env.VITE_SUPABASE_URL', url)
    content = content.replace('import.meta.env.VITE_SUPABASE_ANON_KEY', key)
    content = content.replace('import.meta.env.VITE_SUPABASE_SERVICE_ROLE_KEY', key)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Hardcoded credentials for Python server execution.")
