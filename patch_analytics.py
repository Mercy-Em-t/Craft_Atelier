import re

with open('admin-hub.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the HTML Scaffold to include IDs
old_html = """<div class="card" style="flex:1; padding:20px; text-align:center;">
            <h3 style="color:#64748b; font-size:12px;">TODAY'S ORDERS</h3>
            <div style="font-size:32px; font-weight:800; color:#0f172a; margin-top:10px;">--</div>
        </div>
        <div class="card" style="flex:1; padding:20px; text-align:center;">
            <h3 style="color:#64748b; font-size:12px;">PENDING REVENUE</h3>
            <div style="font-size:32px; font-weight:800; color:#0f172a; margin-top:10px;">KES --</div>
        </div>
        <div class="card" style="flex:1; padding:20px; text-align:center;">
            <h3 style="color:#64748b; font-size:12px;">ON HOLD (ISSUES)</h3>
            <div style="font-size:32px; font-weight:800; color:#ef4444; margin-top:10px;">--</div>
        </div>"""

new_html = """<div class="card" style="flex:1; padding:20px; text-align:center;">
            <h3 style="color:#64748b; font-size:12px;">TODAY'S ORDERS</h3>
            <div id="statTodayOrders" style="font-size:32px; font-weight:800; color:#0f172a; margin-top:10px;">--</div>
        </div>
        <div class="card" style="flex:1; padding:20px; text-align:center;">
            <h3 style="color:#64748b; font-size:12px;">PENDING REVENUE</h3>
            <div id="statPendingRev" style="font-size:32px; font-weight:800; color:#0f172a; margin-top:10px;">KES --</div>
        </div>
        <div class="card" style="flex:1; padding:20px; text-align:center;">
            <h3 style="color:#64748b; font-size:12px;">ON HOLD (ISSUES)</h3>
            <div id="statOnHold" style="font-size:32px; font-weight:800; color:#ef4444; margin-top:10px;">--</div>
        </div>"""

content = content.replace(old_html, new_html)

# 2. Inject the JavaScript function to fetch real data
js_inject = """
    window.loadAnalytics = async () => {
        try {
            // Get today's date start (midnight)
            const today = new Date();
            today.setHours(0,0,0,0);
            
            // Fetch Today's Orders count
            const { count: todayCount } = await client.from('orders').select('*', { count: 'exact', head: true }).gte('created_at', today.toISOString());
            document.getElementById('statTodayOrders').innerText = todayCount || 0;
            
            // Fetch Pending Revenue
            const { data: pending } = await client.from('orders').select('total_cents').eq('status', 'PENDING_PAYMENT');
            const pendingRev = pending ? pending.reduce((sum, o) => sum + (o.total_cents || 0), 0) : 0;
            document.getElementById('statPendingRev').innerText = 'KES ' + (pendingRev / 100).toLocaleString();
            
            // Fetch On Hold count
            const { count: onHoldCount } = await client.from('orders').select('*', { count: 'exact', head: true }).eq('status', 'ON_HOLD');
            document.getElementById('statOnHold').innerText = onHoldCount || 0;
        } catch (err) {
            console.error("Analytics Error", err);
        }
    };
"""

content = content.replace('window.loadQueue = async () => {', js_inject + '\n    window.loadQueue = async () => {')

# 3. Call loadAnalytics when the page loads
content = content.replace('loadQueue();\n        loadTracking();', 'loadQueue();\n        loadTracking();\n        loadAnalytics();')

# 4. Also refresh analytics when real-time insert happens
content = content.replace('loadTracking(\'ALL\');\n      })', 'loadTracking(\'ALL\');\n          loadAnalytics();\n      })')

with open('admin-hub.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Admin Hub updated with Live Analytics")
