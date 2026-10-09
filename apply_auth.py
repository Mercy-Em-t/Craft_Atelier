import re

login_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Staff Portal - Login</title>
    <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
    <style>
        :root { --bg: #0f172a; --surface: #1e293b; --text: #f8fafc; --accent: #3b82f6; }
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, sans-serif; }
        body { background: var(--bg); color: var(--text); display: flex; align-items: center; justify-content: center; height: 100vh; }
        .login-box { background: var(--surface); padding: 40px; border-radius: 16px; width: 100%; max-width: 400px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); text-align: center; }
        h1 { margin-bottom: 8px; font-size: 24px; }
        p { color: #94a3b8; margin-bottom: 24px; font-size: 14px; }
        input { width: 100%; padding: 12px; margin-bottom: 16px; background: #0f172a; border: 1px solid #334155; color: #fff; border-radius: 8px; }
        button { width: 100%; padding: 12px; background: var(--accent); color: #fff; border: none; border-radius: 8px; font-weight: bold; cursor: pointer; margin-bottom: 12px; }
        button.secondary { background: transparent; border: 1px solid #334155; }
        .error { color: #ef4444; font-size: 13px; margin-bottom: 16px; display: none; }
    </style>
</head>
<body>

<div class="login-box">
    <h1>Craft Atelier</h1>
    <p>Secure Staff & Admin Portal</p>
    
    <div id="errorMsg" class="error"></div>
    
    <input type="email" id="email" placeholder="Staff Email Address">
    <input type="password" id="password" placeholder="Password">
    
    <button onclick="handleLogin()">Secure Login</button>
    <button class="secondary" onclick="handleSignup()">Create Account</button>
    
    <div style="margin-top: 20px; text-align: left; font-size: 12px; color: #64748b;">
        * New staff must create an account first. An administrator must then assign your role in the database before you can access the dashboard.
    </div>
</div>

<script>
    const SUPABASE_URL = "https://yjgskbdtnyzsmuzvnrsz.supabase.co";
    const SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlqZ3NrYmR0bnl6c211enZucnN6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTA5NDQ5NzEsImV4cCI6MjEwNjUyMDk3MX0.elz2qyCCXBRFTCdbzqYqoiltkkmBALKrQhAv-I4SC7Q";
    const client = supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

    async function handleLogin() {
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        const { data, error } = await client.auth.signInWithPassword({ email, password });
        
        if (error) {
            showError(error.message);
        } else {
            // Redirect to launchpad upon success
            window.location.href = 'dev-launchpad.html';
        }
    }

    async function handleSignup() {
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        const { data, error } = await client.auth.signUp({ email, password });
        
        if (error) {
            showError(error.message);
        } else {
            alert("Account created! You are logged in, but you need your role assigned in Supabase before accessing dashboards.");
            window.location.href = 'dev-launchpad.html';
        }
    }
    
    function showError(msg) {
        const el = document.getElementById('errorMsg');
        el.innerText = msg;
        el.style.display = 'block';
    }
</script>
</body>
</html>'''

with open('login.html', 'w', encoding='utf-8') as f:
    f.write(login_html)

def add_auth_guard(filepath, init_func):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    guard_code = f"""window.addEventListener('DOMContentLoaded', async () => {{
    const {{ data: {{ session }} }} = await client.auth.getSession();
    if (!session) {{
        window.location.href = 'login.html';
        return;
    }}
    
    // Inject Logout button
    const header = document.querySelector('header');
    if (header) {{
        const btn = document.createElement('button');
        btn.innerText = 'Logout';
        btn.style.cssText = 'position:absolute; right:20px; top:20px; background:transparent; color:#fff; border:1px solid #334155; padding:6px 12px; border-radius:6px; cursor:pointer; font-size:12px;';
        btn.onclick = async () => {{ await client.auth.signOut(); window.location.href = 'login.html'; }};
        header.appendChild(btn);
    }}
    
    {init_func}();
}});"""

    # Replace the existing initialization hook
    content = re.sub(rf"window\.addEventListener\('DOMContentLoaded',\s*{init_func}\);", guard_code, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

add_auth_guard('ops-packing.html', 'loadQueue')
add_auth_guard('admin-hub.html', 'initDashboard')

# Update dev-launchpad to point to login.html if they click Ops or Admin
with open('dev-launchpad.html', 'r', encoding='utf-8') as f:
    lp = f.read()
    lp = lp.replace('ops-packing.html', 'login.html')
    lp = lp.replace('admin-hub.html', 'login.html')
with open('dev-launchpad.html', 'w', encoding='utf-8') as f:
    f.write(lp)

print("Auth integrated.")
