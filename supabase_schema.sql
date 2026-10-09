-- 1. Create Enums
CREATE TYPE order_lifecycle_state AS ENUM (
 'PENDING_PAYMENT',
 'QUEUED_FOR_PACKING',
 'PACKING_IN_PROGRESS',
 'STAGED_FOR_DISPATCH',
 'IN_TRANSIT',
 'DELIVERED',
 'CANCELLED'
);

CREATE TYPE delivery_channel AS ENUM ('rider', 'pickup', 'courier');

-- Kits Catalog
CREATE TABLE kits (
 id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
 title TEXT NOT NULL,
 slug TEXT UNIQUE NOT NULL,
 description TEXT,
 price_cents INT NOT NULL,
 inventory_count INT DEFAULT 0,
 bom_items JSONB NOT NULL DEFAULT '[]'::jsonb
);

-- 2. Orders Table
CREATE TABLE orders (
 id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
 order_number SERIAL UNIQUE,
 customer_name TEXT NOT NULL,
 customer_phone TEXT NOT NULL,
 delivery_type delivery_channel NOT NULL,
 delivery_address TEXT NOT NULL,
 delivery_notes TEXT,
 kit_name TEXT NOT NULL,
 status order_lifecycle_state DEFAULT 'QUEUED_FOR_PACKING',
 created_at TIMESTAMPTZ DEFAULT now(),
 updated_at TIMESTAMPTZ DEFAULT now()
);

-- 3. Fulfillment & Audit Log
CREATE TABLE fulfillment_logs (
 id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
 order_id UUID NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
 packed_by TEXT NOT NULL,
 all_bom_checked BOOLEAN DEFAULT false,
 bonus_item_included BOOLEAN DEFAULT false,
 bom_checklist_state JSONB NOT NULL,
 carrier_name TEXT,
 carrier_phone TEXT,
 staged_at TIMESTAMPTZ,
 dispatched_at TIMESTAMPTZ
);

-- Security Policies
CREATE POLICY "Ops staff read-only access" ON orders
 FOR SELECT TO authenticated
 USING (
 auth.jwt() ->> 'role' IN ('admin', 'ops_staff')
 );

CREATE POLICY "Admin update orders" ON orders
 FOR UPDATE TO authenticated
 USING (auth.jwt() ->> 'role' = 'admin')
 WITH CHECK (auth.jwt() ->> 'role' = 'admin');

-- 4. Secure RPC: Complete Packing Verification
CREATE OR REPLACE FUNCTION verify_and_stage_order(
 p_order_id UUID,
 p_packed_by TEXT,
 p_checklist JSONB,
 p_bonus_included BOOLEAN
) RETURNS VOID LANGUAGE plpgsql AS $$
DECLARE
 v_status order_lifecycle_state;
BEGIN
 SELECT status INTO v_status FROM orders WHERE id = p_order_id;
 IF v_status != 'PACKING_IN_PROGRESS' THEN
 RAISE EXCEPTION 'Order must be in PACKING_IN_PROGRESS to stage for dispatch.';
 END IF;
 -- Upsert fulfillment audit
 INSERT INTO fulfillment_logs (order_id, packed_by, all_bom_checked, bonus_item_included, bom_checklist_state, staged_at)
 VALUES (p_order_id, p_packed_by, true, p_bonus_included, p_checklist, now());
 -- Event transition
 UPDATE orders 
 SET status = 'STAGED_FOR_DISPATCH', updated_at = now() 
 WHERE id = p_order_id;
END;
$$;

-- 5. Secure RPC: Dispatch to Carrier
CREATE OR REPLACE FUNCTION dispatch_order(
 p_order_id UUID,
 p_carrier_name TEXT,
 p_carrier_phone TEXT
) RETURNS VOID LANGUAGE plpgsql AS $$
DECLARE
 v_status order_lifecycle_state;
BEGIN
 SELECT status INTO v_status FROM orders WHERE id = p_order_id;
 IF v_status != 'STAGED_FOR_DISPATCH' THEN
 RAISE EXCEPTION 'Order must be STAGED_FOR_DISPATCH before assigning to a rider.';
 END IF;
 UPDATE fulfillment_logs
 SET carrier_name = p_carrier_name,
 carrier_phone = p_carrier_phone,
 dispatched_at = now()
 WHERE order_id = p_order_id;
 UPDATE orders 
 SET status = 'IN_TRANSIT', updated_at = now() 
 WHERE id = p_order_id;
END;
$$;

-- Seed Kit Catalog
INSERT INTO kits (id, title, slug, description, price_cents, inventory_count, bom_items)
VALUES
(
 'a1b2c3d4-0001-4000-8000-000000000001',
 'Everyday Ribbed Shoulder Bag Kit',
 'everyday-ribbed-shoulder-bag',
 'Structured baguette-style shoulder bag made with seamless ribbing. Complete with pre-started base rows, snag-free',
 345000,
 35,
 '[
 {"item_id": "YRN-TUB-CRM", "name": "Cotton Tube Yarn - Cream Oat (150g)", "qty": 2, "unit": "skein"},
 {"item_id": "HK-ERG-50", "name": "5.0mm Ergonomic Soft-Grip Hook", "qty": 1, "unit": "piece"},
 {"item_id": "PRE-BASE-RIB", "name": "Pre-Started Foundation Strip (Rows 1-2)", "qty": 1, "unit": "piece"},
 {"item_id": "NOT-SET-01", "name": "Notions Pouch (1 Large Eye Needle + 5 Locking Markers)", "qty": 1, "unit": "piece"},
 {"item_id": "HDW-MAG-BRS", "name": "Sew-in Antique Brass Magnetic Clasp", "qty": 1, "unit": "set"},
 {"item_id": "DOC-ACC-RIB", "name": "Accordion Visual Guide & QR Link Card", "qty": 1, "unit": "card"}
 ]'::jsonb
),
(
 'a1b2c3d4-0002-4000-8000-000000000002',
 'Checkerboard Mini Bucket Hat Kit',
 'checkerboard-bucket-hat',
 'Y2K-inspired streetwear bucket hat in two-tone checkerboard blocks. Features calibrated contrast yarn and pre-cut',
 285000,
 40,
 '[
 {"item_id": "YRN-TUB-MAT", "name": "Cotton Tube Yarn - Matcha Green (100g)", "qty": 1, "unit": "skein"},
 {"item_id": "YRN-TUB-IVR", "name": "Cotton Tube Yarn - Ivory Cloud (100g)", "qty": 1, "unit": "skein"},
 {"item_id": "HK-ERG-45", "name": "4.5mm Ergonomic Soft-Grip Hook", "qty": 1, "unit": "piece"},
 {"item_id": "PRE-CROWN-01", "name": "Pre-Started Flat Magic Ring Crown (Rounds 1-3)", "qty": 1, "unit": "piece"},
 {"item_id": "NOT-SET-01", "name": "Notions Pouch (1 Large Eye Needle + 5 Locking Markers)", "qty": 1, "unit": "piece"},
 {"item_id": "DOC-ACC-HAT", "name": "Accordion Visual Guide & QR Link Card", "qty": 1, "unit": "card"}
 ]'::jsonb
),
(
 'a1b2c3d4-0003-4000-8000-000000000003',
 'Artisan Envelope Clutch & Card Sleeve',
 'artisan-envelope-clutch',
 'Compact handheld pouch with a textured moss stitch body. Ideal 2-hour beginner project requiring zero pattern shaping',
 225000,
 50,
 '[
 {"item_id": "YRN-TUB-TER", "name": "Cotton Tube Yarn - Terracotta (120g)", "qty": 1, "unit": "skein"},
 {"item_id": "HK-ERG-50", "name": "5.0mm Ergonomic Soft-Grip Hook", "qty": 1, "unit": "piece"},
 {"item_id": "PRE-BASE-ENV", "name": "Pre-Started Envelope Base Chain (24 Stitches)", "qty": 1, "unit": "piece"},
 {"item_id": "NOT-SET-01", "name": "Notions Pouch (1 Large Eye Needle + 5 Locking Markers)", "qty": 1, "unit": "piece"},
 {"item_id": "HDW-BTN-WOD", "name": "Engraved Olivewood Toggle Button", "qty": 1, "unit": "piece"},
 {"item_id": "DOC-ACC-CLT", "name": "Accordion Visual Guide & QR Link Card", "qty": 1, "unit": "card"}
 ]'::jsonb
)
ON CONFLICT (id) DO UPDATE SET
 title = EXCLUDED.title,
 price_cents = EXCLUDED.price_cents,
 bom_items = EXCLUDED.bom_items;
