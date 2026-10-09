import re

with open('storefront.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's replace the entire submitOrder top section using a robust regex.
pattern = re.compile(r'async function submitOrder\(\) \{.*?const type = document\.getElementById\(\'delType\'\)\.value;', re.DOTALL)

new_code = """async function submitOrder() {
   const btn = document.getElementById('submitOrderBtn');
   
   const mpesa = document.getElementById('mpesaCode').value.trim().toUpperCase();
   const mpesaRegex = /^[A-Z0-9]{10}$/;
   if (!mpesaRegex.test(mpesa)) {
       alert("Invalid M-Pesa Code. It must be exactly 10 alphanumeric characters.");
       if (btn) { btn.disabled = false; btn.textContent = "Complete Order"; }
       return;
   }
   
   const name = document.getElementById('custName').value.replace(/</g, "").replace(/>/g, "").trim();
   const phone = document.getElementById('custPhone').value.trim();
   const phoneRegex = /^(?:254|\\+254|0)?(7[0-9]{8}|1[0-9]{8})$/;
   if (!phoneRegex.test(phone)) {
       alert("Please enter a valid Kenyan phone number (e.g., 0712345678).");
       if (btn) { btn.disabled = false; btn.textContent = "Complete Order"; }
       return;
   }

   const type = document.getElementById('delType').value;"""

content = re.sub(pattern, new_code, content)

with open('storefront.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Storefront regex patch applied!")
