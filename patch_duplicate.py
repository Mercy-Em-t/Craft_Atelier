import re

with open('storefront.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Locate the submitOrder function and add button disabling
old_submit = """async function submitOrder() {
            const name = document.getElementById('custName').value;"""
new_submit = """async function submitOrder() {
            const btn = document.querySelector('.btn-primary[onclick="submitOrder()"]');
            if (btn) {
                btn.disabled = true;
                btn.innerText = "Processing...";
            }
            const name = document.getElementById('custName').value;"""

old_reset = """alert('Order Placed Successfully! We will verify your payment.');
            closeCheckout();"""
new_reset = """alert('Order Placed Successfully! We will verify your payment.');
            if (btn) {
                btn.disabled = false;
                btn.innerText = "Complete Order";
            }
            closeCheckout();"""

# Also need to handle error cases so the button reenables if it fails
old_error = """if (error) {
                alert('Error placing order: ' + error.message);
            }"""
new_error = """if (error) {
                alert('Error placing order: ' + error.message);
                if (btn) {
                    btn.disabled = false;
                    btn.innerText = "Complete Order";
                }
            }"""

content = content.replace(old_submit, new_submit)
content = content.replace(old_reset, new_reset)
content = content.replace(old_error, new_error)

with open('storefront.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Storefront updated to prevent UI double-clicks.")
