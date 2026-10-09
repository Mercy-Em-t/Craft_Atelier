import re

with open('storefront.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Locate submitOrder and add the financial columns
old_insert = """const { error } = await client.from('orders').insert([{
 customer_name: name, customer_phone: phone, delivery_type: type, delivery_address: addr,
 kit_name: orderSummary, payment_ref: mpesa, cart_items: cart, status: 'PENDING_PAYMENT'
 }]);"""

new_insert = """const subtotal = cart.reduce((sum, item) => sum + item.price, 0);
 const sel = document.getElementById('delType');
 const delCostCents = parseInt(sel.options[sel.selectedIndex].getAttribute('data-cost')) * 100;
 const total = subtotal + delCostCents;

 const { error } = await client.from('orders').insert([{
 customer_name: name, customer_phone: phone, delivery_type: type, delivery_address: addr,
 kit_name: orderSummary, payment_ref: mpesa, cart_items: cart, status: 'PENDING_PAYMENT',
 subtotal_cents: subtotal, delivery_fee_cents: delCostCents, total_cents: total
 }]);"""

content = content.replace(old_insert, new_insert)

with open('storefront.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Storefront updated with financial snapshots")
