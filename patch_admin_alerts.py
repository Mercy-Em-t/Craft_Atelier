import re

with open('admin-hub.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add the UPDATE listener to the existing real-time channel
old_channel = """client.channel('custom-insert-channel')
      .on('postgres_changes', { event: 'INSERT', schema: 'public', table: 'orders' }, payload => {
          alert(`🚨 NEW ORDER RECEIVED! Order #${payload.new.order_number} from ${payload.new.customer_name}.`);
          loadQueue();
          loadTracking('ALL');
          loadAnalytics();
      })
      .subscribe();"""

new_channel = """client.channel('custom-insert-channel')
      .on('postgres_changes', { event: 'INSERT', schema: 'public', table: 'orders' }, payload => {
          alert(`🚨 NEW ORDER RECEIVED! Order #${payload.new.order_number} from ${payload.new.customer_name}.`);
          loadQueue();
          loadTracking('ALL');
          loadAnalytics();
      })
      .on('postgres_changes', { event: 'UPDATE', schema: 'public', table: 'orders' }, payload => {
          if (payload.new.status === 'ON_HOLD' && payload.old.status !== 'ON_HOLD') {
              alert(`⚠️ WAREHOUSE ALERT: Order #${payload.new.order_number} was placed ON HOLD due to a stock issue!`);
              loadTracking('ALL');
              loadAnalytics();
          }
      })
      .subscribe();"""

content = content.replace(old_channel, new_channel)

with open('admin-hub.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Admin Hub updated with ON_HOLD alerts")
