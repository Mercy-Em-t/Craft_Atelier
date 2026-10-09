import re

toast_css = """
/* TOAST NOTIFICATIONS */
#toast-container { position: fixed; top: 20px; right: 20px; z-index: 9999; display: flex; flex-direction: column; gap: 10px; }
.toast { background: white; color: #0f172a; padding: 15px 20px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15); border-left: 4px solid #3b82f6; font-weight: 600; font-size: 14px; animation: slideIn 0.3s ease-out; max-width: 350px; transition: opacity 0.3s; }
.toast.error { border-left-color: #ef4444; }
.toast.success { border-left-color: #10b981; }
@keyframes slideIn { from { transform: translateX(100%); opacity: 0; } to { transform: translateX(0); opacity: 1; } }
"""

toast_js = """
// TOAST NOTIFICATION SYSTEM
function showToast(message, type = 'info') {
    let container = document.getElementById('toast-container');
    if (!container) {
        container = document.createElement('div');
        container.id = 'toast-container';
        document.body.appendChild(container);
    }
    const toast = document.createElement('div');
    
    // Auto-detect error/success based on text if type is info
    if (type === 'info') {
        const lowerMsg = message.toLowerCase();
        if (lowerMsg.includes('error') || lowerMsg.includes('invalid') || lowerMsg.includes('denied') || lowerMsg.includes('unable') || lowerMsg.includes('please enter') || lowerMsg.includes('please provide') || lowerMsg.includes('alert')) type = 'error';
        if (lowerMsg.includes('success') || lowerMsg.includes('closed') || lowerMsg.includes('received')) type = 'success';
    }
    
    toast.className = `toast ${type}`;
    toast.innerText = message;
    container.appendChild(toast);
    setTimeout(() => { toast.style.opacity = '0'; setTimeout(() => toast.remove(), 300); }, 3500);
}
"""

def inject_toast(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "TOAST NOTIFICATION SYSTEM" in content:
        return # Already injected

    # Inject CSS
    content = content.replace('</style>', toast_css + '\n</style>')
    
    # Inject JS
    content = content.replace('<script>', '<script>\n' + toast_js)
    
    # Replace alert() with showToast()
    # We use a regex to safely replace alert(...) without breaking string quotes.
    content = re.sub(r'\balert\s*\(', 'showToast(', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

inject_toast('storefront.html')
inject_toast('admin-hub.html')
inject_toast('ops-packing.html')

print("Replaced all alerts with modern Toast notifications!")
