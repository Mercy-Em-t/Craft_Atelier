with open('ops-packing.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add Realtime listener to ops-packing
js_realtime = """
    // --- REALTIME NOTIFICATIONS ---
    client.channel('ops-orders-channel')
      .on('postgres_changes', { event: 'UPDATE', schema: 'public', table: 'orders' }, payload => {
          if (currentUserRole === 'packer' && payload.new.status === 'QUEUED_FOR_PACKING') {
              // Only alert if we don't have an active order or we just got a new one in the queue
              fetchNextOrder();
          } else if (currentUserRole === 'dispatcher' && payload.new.status === 'STAGED_FOR_DISPATCH') {
              fetchNextOrder();
          }
      })
      .subscribe();
"""

content = content.replace('fetchNextOrder();\n    }', 'fetchNextOrder();\n    }\n' + js_realtime)

with open('ops-packing.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Ops Hub updated with Realtime")
