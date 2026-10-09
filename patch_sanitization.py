import re

with open('storefront.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Validation & Sanitization to submitOrder
old_submit = """const name = document.getElementById('custName').value;
            const phone = document.getElementById('custPhone').value;
            const addr = document.getElementById('custAddress').value;
            const mpesa = document.getElementById('mpesaCode').value;"""

new_submit = """let name = document.getElementById('custName').value.trim();
            let phone = document.getElementById('custPhone').value.trim();
            let addr = document.getElementById('custAddress').value.trim();
            let mpesa = document.getElementById('mpesaCode').value.trim().toUpperCase();

            // XSS Sanitization (remove angle brackets)
            name = name.replace(/</g, "").replace(/>/g, "");
            addr = addr.replace(/</g, "").replace(/>/g, "");

            // Validation Rules
            const phoneRegex = /^(?:254|\+254|0)?(7[0-9]{8}|1[0-9]{8})$/;
            if (!phoneRegex.test(phone)) {
                alert("Please enter a valid Kenyan phone number (e.g., 0712345678).");
                if (btn) { btn.disabled = false; btn.innerText = "Complete Order"; }
                return;
            }

            const mpesaRegex = /^[A-Z0-9]{10}$/;
            if (!mpesaRegex.test(mpesa)) {
                alert("Invalid M-Pesa Code. It must be exactly 10 alphanumeric characters (e.g., SJL2K39F8D).");
                if (btn) { btn.disabled = false; btn.innerText = "Complete Order"; }
                return;
            }
            
            if (name.length < 2 || addr.length < 5) {
                alert("Please provide a valid name and detailed delivery address.");
                if (btn) { btn.disabled = false; btn.innerText = "Complete Order"; }
                return;
            }"""

content = content.replace(old_submit, new_submit)

# 2. Add UX text to the M-Pesa modal to reassure the user
old_modal_text = """<p style="font-size:14px; margin-bottom:15px;">Please send <b id="mpesaTotalAmount"></b> to our Till Number:</p>"""
new_modal_text = """<p style="font-size:14px; margin-bottom:15px;">Please send <b id="mpesaTotalAmount"></b> to our Till Number:</p>
            <div style="background:#f0fdf4; border-left:4px solid #22c55e; padding:10px; margin-bottom:15px; font-size:12px; color:#166534;">
                💡 <b>Take your time!</b> This screen will not time out. Switch to your M-Pesa menu, make the payment, and return here to paste the receipt code.
            </div>"""

content = content.replace(old_modal_text, new_modal_text)

with open('storefront.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Storefront updated with Sanitization and Modal UX")
