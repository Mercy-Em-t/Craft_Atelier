import re

with open('ops-packing.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Header HTML
old_header = '''<span class="badge" id="statusBadge">CONNECTING...</span>
 </div>'''
new_header = '''<div style="display: flex; gap: 8px; flex-direction: column; align-items: flex-end;">
 <span class="badge" id="statusBadge">CONNECTING...</span>
 <span class="badge" id="queueCountBadge" style="background: rgba(59, 130, 246, 0.15); color: var(--blue);">0 IN QUEUE</span>
 </div>
 </div>'''
content = content.replace(old_header, new_header)

# 2. Update fetchNextOrder
old_fetch = """const { data, error } = await client
 .from('orders')
 .select('*')
 .in('status', currentUserRole === 'packer' ? ['QUEUED_FOR_PACKING', 'PACKING_IN_PROGRESS'] : 
               currentUserRole === 'dispatcher' ? ['STAGED_FOR_DISPATCH'] : 
               ['QUEUED_FOR_PACKING', 'PACKING_IN_PROGRESS', 'STAGED_FOR_DISPATCH'])
 .order('created_at', { ascending: true })
 .limit(1)
 .maybeSingle();"""

new_fetch = """
    const statuses = currentUserRole === 'packer' ? ['QUEUED_FOR_PACKING', 'PACKING_IN_PROGRESS'] : 
                     currentUserRole === 'dispatcher' ? ['STAGED_FOR_DISPATCH'] : 
                     ['QUEUED_FOR_PACKING', 'PACKING_IN_PROGRESS', 'STAGED_FOR_DISPATCH'];

    // Update Queue Count
    const { count } = await client.from('orders').select('*', { count: 'exact', head: true }).in('status', statuses);
    const queueBadge = document.getElementById('queueCountBadge');
    if (count !== null) {
        queueBadge.textContent = `${count} IN QUEUE`;
        queueBadge.style.background = count > 0 ? 'rgba(59, 130, 246, 0.15)' : 'rgba(148, 163, 184, 0.15)';
        queueBadge.style.color = count > 0 ? 'var(--blue)' : '#94a3b8';
    }

    const { data, error } = await client
 .from('orders')
 .select('*')
 .in('status', statuses)
 .order('created_at', { ascending: true })
 .limit(1)
 .maybeSingle();
"""

content = content.replace(old_fetch, new_fetch.strip())

with open('ops-packing.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Added queue counter")
