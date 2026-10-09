import re

modal_js = """
// CUSTOM MODAL SYSTEM
window.customPrompt = function(title, message, placeholder = '') {
    return new Promise((resolve) => {
        const overlay = document.createElement('div');
        overlay.style.cssText = 'position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.5); z-index:10000; display:flex; align-items:center; justify-content:center;';
        const modal = document.createElement('div');
        modal.style.cssText = 'background:white; padding:20px; border-radius:8px; width:90%; max-width:400px; box-shadow:0 10px 25px rgba(0,0,0,0.2);';
        
        modal.innerHTML = `
            <h3 style="margin-bottom:10px;">${title}</h3>
            <p style="font-size:14px; color:#64748b; margin-bottom:15px;">${message}</p>
            <input type="text" id="cpInput" placeholder="${placeholder}" style="width:100%; padding:10px; border:1px solid #cbd5e1; border-radius:4px; margin-bottom:20px; font-size:14px;">
            <div style="display:flex; justify-content:flex-end; gap:10px;">
                <button id="cpCancel" class="btn" style="background:#e2e8f0; color:#475569; width:auto; border:none; padding:8px 15px; cursor:pointer; border-radius:4px; font-weight:bold;">Cancel</button>
                <button id="cpConfirm" class="btn btn-blue" style="width:auto; border:none; background:#3b82f6; color:white; padding:8px 15px; cursor:pointer; border-radius:4px; font-weight:bold;">Confirm</button>
            </div>
        `;
        overlay.appendChild(modal);
        document.body.appendChild(overlay);
        
        const input = modal.querySelector('#cpInput');
        input.focus();
        
        modal.querySelector('#cpCancel').onclick = () => { overlay.remove(); resolve(null); };
        modal.querySelector('#cpConfirm').onclick = () => { overlay.remove(); resolve(input.value.trim()); };
        input.onkeyup = (e) => { if(e.key === 'Enter') modal.querySelector('#cpConfirm').click(); };
    });
};

window.customConfirm = function(title, message) {
    return new Promise((resolve) => {
        const overlay = document.createElement('div');
        overlay.style.cssText = 'position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.5); z-index:10000; display:flex; align-items:center; justify-content:center;';
        const modal = document.createElement('div');
        modal.style.cssText = 'background:white; padding:20px; border-radius:8px; width:90%; max-width:400px; box-shadow:0 10px 25px rgba(0,0,0,0.2);';
        
        modal.innerHTML = `
            <h3 style="margin-bottom:10px;">${title}</h3>
            <p style="font-size:14px; color:#64748b; margin-bottom:20px;">${message}</p>
            <div style="display:flex; justify-content:flex-end; gap:10px;">
                <button id="ccCancel" class="btn" style="background:#e2e8f0; color:#475569; width:auto; border:none; padding:8px 15px; cursor:pointer; border-radius:4px; font-weight:bold;">Cancel</button>
                <button id="ccConfirm" class="btn btn-blue" style="width:auto; border:none; background:#3b82f6; color:white; padding:8px 15px; cursor:pointer; border-radius:4px; font-weight:bold;">Confirm</button>
            </div>
        `;
        overlay.appendChild(modal);
        document.body.appendChild(overlay);
        
        modal.querySelector('#ccCancel').onclick = () => { overlay.remove(); resolve(false); };
        modal.querySelector('#ccConfirm').onclick = () => { overlay.remove(); resolve(true); };
    });
};
"""

def replace_modals(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if "CUSTOM MODAL SYSTEM" not in content:
        content = content.replace('<script>', '<script>\n' + modal_js)

    # We safely replace prompt(msg) with await customPrompt('Input Required', msg)
    # We replace confirm(msg) with await customConfirm('Please Confirm', msg)
    # Because some prompts might already have a placeholder, we use a regex careful replacement or just blind replace.
    # Fortunately, JS allows extra args to be passed. `customPrompt('Input', 'msg')` works.
    
    # Replace simple prompt("...") -> await customPrompt("Action Required", "...")
    content = re.sub(r'prompt\((.*?)\)', r'await customPrompt("Action Required", \1)', content)
    
    # Replace simple confirm("...") -> await customConfirm("Please Confirm", "...")
    content = re.sub(r'confirm\((.*?)\)', r'await customConfirm("Please Confirm", \1)', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

replace_modals('admin-hub.html')
replace_modals('ops-packing.html')
print("Prompts replaced with custom modals!")
