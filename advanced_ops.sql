-- 1. Create Order Audit Logs
CREATE TABLE IF NOT EXISTS order_audit_logs (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    order_id UUID REFERENCES orders(id),
    old_status TEXT,
    new_status TEXT,
    changed_by TEXT, -- Email or 'SYSTEM_AUTO'
    notes TEXT,
    created_at TIMESTAMPTZ DEFAULT now()
);

ALTER TABLE order_audit_logs ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Staff read audit logs" ON order_audit_logs FOR SELECT TO authenticated USING (true);
CREATE POLICY "Staff insert audit logs" ON order_audit_logs FOR INSERT TO authenticated USING (true);

-- 2. Add ON_HOLD status to the enum if possible, or just use TEXT for status. 
-- Since we used an ENUM 'order_lifecycle_state', we need to alter it:
ALTER TYPE order_lifecycle_state ADD VALUE IF NOT EXISTS 'ON_HOLD';

-- 3. RPC for Automated SMS Webhook (System Auto-Verify)
CREATE OR REPLACE FUNCTION auto_verify_mpesa_payment(p_mpesa_code TEXT, p_raw_sms TEXT)
RETURNS BOOLEAN
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
DECLARE
    v_order_id UUID;
    v_current_status TEXT;
BEGIN
    -- Find the order with this exact M-Pesa code that is pending payment
    SELECT id, status INTO v_order_id, v_current_status
    FROM orders
    WHERE payment_ref = UPPER(p_mpesa_code) AND status = 'PENDING_PAYMENT'
    LIMIT 1;

    IF v_order_id IS NOT NULL THEN
        -- Update Order
        UPDATE orders SET status = 'QUEUED_FOR_PACKING' WHERE id = v_order_id;
        
        -- Log to Audit Trail
        INSERT INTO order_audit_logs (order_id, old_status, new_status, changed_by, notes)
        VALUES (v_order_id, 'PENDING_PAYMENT', 'QUEUED_FOR_PACKING', 'SYSTEM_AUTO_SMS', 'Auto-verified from SMS: ' || p_raw_sms);
        
        RETURN TRUE;
    END IF;
    
    RETURN FALSE;
END;
$$;
