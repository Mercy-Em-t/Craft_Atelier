import re

with open('storefront.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_block = """   const mpesa = document.getElementById('mpesaCode').value.trim();
   if (!mpesa) return alert("Please enter M-Pesa code.");
   
   const name = document.getElementById('custName').value;
   const phone = document.getElementById('custPhone').value;"""

new_block = """   const mpesa = document.getElementById('mpesaCode').value.trim().toUpperCase();
   const mpesaRegex = /^[A-Z0-9]{10}$/;
   if (!mpesaRegex.test(mpesa)) {
       alert("Invalid M-Pesa Code. It must be exactly 10 alphanumeric characters.");
       return;
   }
   
   const name = document.getElementById('custName').value.replace(/</g, "").replace(/>/g, "").trim();
   const phone = document.getElementById('custPhone').value.trim();
   const phoneRegex = /^(?:254|\+254|0)?(7[0-9]{8}|1[0-9]{8})$/;
   if (!phoneRegex.test(phone)) {
       alert("Please enter a valid Kenyan phone number (e.g., 0712345678).");
       return;
   }"""

if old_block in content:
    content = content.replace(old_block, new_block)
else:
    print("WARNING: Anchor not found!")

# Also fix the button reset in case of error
old_err = """if (error) {
       alert('Error: ' + error.message);
   } else {"""

new_err = """if (error) {
       alert('Error: ' + error.message);
       btn.disabled = false;
       btn.textContent = "Complete Order";
   } else {"""

if old_err in content:
    content = content.replace(old_err, new_err)

with open('storefront.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Storefront validation fully applied!")
