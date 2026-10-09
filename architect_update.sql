-- 1. Financial Snapshots for Invoices
ALTER TABLE orders ADD COLUMN IF NOT EXISTS subtotal_cents INT DEFAULT 0;
ALTER TABLE orders ADD COLUMN IF NOT EXISTS delivery_fee_cents INT DEFAULT 0;
ALTER TABLE orders ADD COLUMN IF NOT EXISTS total_cents INT DEFAULT 0;

-- 2. Kit Attributes
ALTER TABLE kits ADD COLUMN IF NOT EXISTS category TEXT;
ALTER TABLE kits ADD COLUMN IF NOT EXISTS skill_level TEXT;

-- 3. Unhappy Path End States (Enums)
-- Note: 'CANCELLED' is usually already in your enum from earlier, 
-- but we add REFUNDED and DISPUTED.
ALTER TYPE order_lifecycle_state ADD VALUE IF NOT EXISTS 'REFUNDED';
ALTER TYPE order_lifecycle_state ADD VALUE IF NOT EXISTS 'DISPUTED';
