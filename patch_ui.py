import re

with open('ops-packing.html', 'r', encoding='utf-8') as f:
    content = f.read()

correct_js = """
    function renderOrderView() {
        const container = document.getElementById('appContainer');
        const badge = document.getElementById('statusBadge');
        
        badge.textContent = activeOrder.status.replace(/_/g, ' ');
        badge.style.background = activeOrder.status === 'STAGED_FOR_DISPATCH' ? 'rgba(16, 185, 129, 0.15)' : 'rgba(245, 158, 11, 0.15)';
        badge.style.color = activeOrder.status === 'STAGED_FOR_DISPATCH' ? 'var(--accent)' : 'var(--warn)';

        const isStaged = activeOrder.status === 'STAGED_FOR_DISPATCH';

        // Base Customer Card (Always shown)
        let html = `
            <div class="card">
                <div class="order-title">Order #${activeOrder.order_number} • ${activeOrder.kit_name}</div>
                <div class="meta-row"><span>Recipient:</span> <strong style="color: var(--text);">${activeOrder.customer_name}</strong></div>
                <div class="meta-row"><span>Phone:</span> <span>${activeOrder.customer_phone}</span></div>
                <div class="meta-row"><span>Channel:</span> <span>${activeOrder.delivery_type.toUpperCase()}</span></div>
                <div class="meta-row"><span>Address:</span> <span>${activeOrder.delivery_address}</span></div>
                ${activeOrder.delivery_notes ? `<div class="meta-row" style="margin-top:6px; color: var(--warn);"><span>Notes: ${activeOrder.delivery_notes}</span></div>` : ''}
            </div>
        `;

        if (!isStaged) {
            // PACKING VIEW
            html += `
            <div class="card">
                <div class="checklist-title">BOM Packing Verification</div>
                <label class="check-item"><input type="checkbox" class="bom-check"><span>Curated Yarn Bundles (Weight & Color Verified)</span></label>
                <label class="check-item"><input type="checkbox" class="bom-check"><span>Ergonomic Hook (Calibrated Gauge)</span></label>
                <label class="check-item"><input type="checkbox" class="bom-check"><span>Notions Pack (Darning Needle + 5 Markers)</span></label>
                <label class="check-item"><input type="checkbox" class="bom-check"><span>Pre-Started Foundation Piece (Zero-Frustration Starter)</span></label>
                <label class="check-item"><input type="checkbox" class="bom-check"><span>Accordion Print Guide + Video QR Card</span></label>
                
                <div style="margin-top: 14px; border-top: 1px dashed var(--border); padding-top: 12px;"></div>
                <label class="check-item bonus"><input type="checkbox" id="bonusCheck" checked><span>✨ Surprise Maker's Charm Included</span></label>
                
                <button id="verifyBtn" class="btn btn-primary" disabled onclick="submitVerification()">Verify All Items & Seal Box</button>
            </div>
            `;
        } else {
            // HANDOVER VIEW (Clean, no checklist)
            html += `
            <div class="card" style="text-align: center; border-color: var(--accent); background: rgba(16, 185, 129, 0.05);">
                <div style="font-size: 48px; margin-bottom: 16px;">📦</div>
                <h2 style="margin-bottom: 8px; color: var(--accent);">Sealed & Ready for Dispatch</h2>
                <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 24px;">This order has been verified and securely packed. It is currently waiting at the dispatch bay.</p>
                
                <button id="dispatchBtn" class="btn btn-blue" onclick="openModal()">Assign Carrier / Hand Off</button>
            </div>
            `;
        }

        container.innerHTML = html;

        if (!isStaged) {
            attachChecklistListeners();
        }
    }
"""

content = re.sub(r"function renderOrderView\(\) \{.*?(?=function attachChecklistListeners)", correct_js, content, flags=re.DOTALL)

with open('ops-packing.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("ops-packing view updated")
