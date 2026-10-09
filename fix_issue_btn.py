import re

with open('ops-packing.html', 'r', encoding='utf-8') as f:
    content = f.read()

js_inject = """
    window.reportIssue = async () => {
        if (!activeOrder) return;
        const reason = prompt("What item is missing or unavailable?");
        if (!reason) return;
        
        const staffName = document.getElementById('staffLabel').innerText;
        
        const { error } = await client.from('orders').update({status: 'ON_HOLD', delivery_notes: 'ISSUE: ' + reason}).eq('id', activeOrder.id);
        
        // Log audit
        await client.from('order_audit_logs').insert([{
            order_id: activeOrder.id,
            old_status: activeOrder.status,
            new_status: 'ON_HOLD',
            changed_by: staffName,
            notes: 'Stock issue reported: ' + reason
        }]);

        if(!error) {
            alert("Issue reported to Admin. Order placed ON HOLD.");
            fetchNextOrder();
        } else {
            alert("Error reporting issue: " + error.message);
        }
    };
"""

if "window.reportIssue = async ()" not in content:
    content = content.replace('async function submitVerification() {', js_inject + '\n    async function submitVerification() {')

with open('ops-packing.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Injected reportIssue JS successfully")
