import re

with open('ops-packing.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_btns = """<button id="verifyBtn" class="btn btn-primary" disabled onclick="submitVerification()">Verify All Items & Seal Box</button>"""
new_btns = """<div style="display:flex; gap:10px;">
    <button id="verifyBtn" class="btn btn-primary" style="flex:2;" disabled onclick="submitVerification()">Verify All Items & Seal Box</button>
    <button class="btn btn-secondary" style="flex:1; background:#ef4444; color:white; border:none;" onclick="reportIssue()">Report Stock Issue</button>
</div>"""
content = content.replace(old_btns, new_btns)

js_inject = """
    window.reportIssue = async () => {
        const reason = prompt("What item is missing or unavailable?");
        if (!reason) return;
        
        const { error } = await client.from('orders').update({status: 'ON_HOLD', delivery_notes: 'ISSUE: ' + reason}).eq('id', activeOrder.id);
        
        // Log audit
        await client.from('order_audit_logs').insert([{
            order_id: activeOrder.id,
            old_status: activeOrder.status,
            new_status: 'ON_HOLD',
            changed_by: document.getElementById('staffLabel').innerText,
            notes: 'Stock issue reported: ' + reason
        }]);

        if(!error) {
            alert("Issue reported to Admin. Order placed ON HOLD.");
            fetchNextOrder();
        }
    };
"""

content = content.replace('window.submitVerification = async () => {', js_inject + '\n    window.submitVerification = async () => {')

with open('ops-packing.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Ops Hub updated with Issue Reporting")
