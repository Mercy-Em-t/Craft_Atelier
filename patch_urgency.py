import re

with open('storefront.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_banner = """💡 <b>Take your time!</b> This screen will not time out. Switch to your M-Pesa menu, make the payment, and return here to paste the receipt code."""
new_banner = """💡 <b>Waiting for payment...</b> Switch to your M-Pesa menu to complete the transaction, then return here to paste the receipt code."""

content = content.replace(old_banner, new_banner)

with open('storefront.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Storefront updated to remove 'take your time'")
