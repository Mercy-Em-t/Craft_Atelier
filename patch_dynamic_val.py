import re

with open('storefront.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update proceedToPayment to do the full validation
old_proceed = """function proceedToPayment() {
   const name = document.getElementById('custName').value;
   const phone = document.getElementById('custPhone').value;
   if (!name || !phone) return alert("Please fill name and phone.");
   closeModals();"""

new_proceed = """function proceedToPayment() {
   const name = document.getElementById('custName').value.replace(/</g, "").replace(/>/g, "").trim();
   const phone = document.getElementById('custPhone').value.trim();
   const type = document.getElementById('delType').value;
   const addr = type === 'pickup' ? document.getElementById('pickupPoint').value : document.getElementById('delAddress').value;

   const phoneRegex = /^(?:254|\\+254|0)?(7[0-9]{8}|1[0-9]{8})$/;
   if (!phoneRegex.test(phone)) {
       return alert("Please enter a valid Kenyan phone number (e.g., 0712345678).");
   }
   if (name.length < 2) return alert("Please provide a valid name.");
   if (type !== 'pickup' && addr.length < 5) return alert("Please provide a detailed delivery address.");

   // Re-write back sanitized values
   document.getElementById('custName').value = name;
   
   closeModals();"""

content = content.replace(old_proceed, new_proceed)


# 2. Add real-time M-Pesa validation to the input HTML
old_input = """<input type="text" id="mpesaCode" placeholder="e.g. QKZ9A1B2C3" style="text-transform: uppercase;">"""
new_input = """<input type="text" id="mpesaCode" placeholder="e.g. QKZ9A1B2C3" style="text-transform: uppercase;" oninput="validateMpesa()">
<div id="mpesaError" style="color:#ef4444; font-size:12px; margin-top:5px; display:none;">Must be exactly 10 alphanumeric characters.</div>"""
content = content.replace(old_input, new_input)


# 3. Add validateMpesa function
val_func = """
   function validateMpesa() {
       const mpesa = document.getElementById('mpesaCode').value.trim().toUpperCase();
       const btn = document.getElementById('submitOrderBtn');
       const err = document.getElementById('mpesaError');
       const mpesaRegex = /^[A-Z0-9]{10}$/;
       
       if (mpesa.length === 0) {
           err.style.display = 'none';
           btn.disabled = false;
       } else if (!mpesaRegex.test(mpesa)) {
           err.style.display = 'block';
           btn.disabled = true;
       } else {
           err.style.display = 'none';
           btn.disabled = false;
       }
   }
"""
content = content.replace('function closeModals() {', val_func + '\n   function closeModals() {')

# 4. Remove the redundant Phone validation from submitOrder
content = re.sub(r'const phoneRegex = \/\^.*?\n.*?return;\n   }', '', content, flags=re.DOTALL)
# Also remove the name logic since we did it above
content = re.sub(r'const name = document\.getElementById\(\'custName\'\)\.value\.replace.*?;', "const name = document.getElementById('custName').value;", content)

with open('storefront.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Storefront UX dynamically updated!")
