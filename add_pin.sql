-- Add delivery_pin to orders
ALTER TABLE orders ADD COLUMN IF NOT EXISTS delivery_pin TEXT;
