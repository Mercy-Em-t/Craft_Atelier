CREATE TABLE IF NOT EXISTS business_settings (
  setting_key TEXT PRIMARY KEY,
  setting_value TEXT NOT NULL,
  updated_at TIMESTAMPTZ DEFAULT now()
);

ALTER TABLE business_settings ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Public read settings" ON business_settings FOR SELECT TO public USING (true);
CREATE POLICY "Admin manage settings" ON business_settings FOR ALL TO authenticated 
  USING (EXISTS (SELECT 1 FROM staff_directory WHERE email = auth.jwt()->>'email' AND role = 'admin' AND status = 'active'));

INSERT INTO business_settings (setting_key, setting_value) VALUES ('mpesa_till', '888999') ON CONFLICT (setting_key) DO NOTHING;

-- Ensure Admin can manage kits
ALTER TABLE kits ENABLE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS "Public read kits" ON kits;
CREATE POLICY "Public read kits" ON kits FOR SELECT TO public USING (true);

DROP POLICY IF EXISTS "Admin manage kits" ON kits;
CREATE POLICY "Admin manage kits" ON kits FOR ALL TO authenticated 
  USING (EXISTS (SELECT 1 FROM staff_directory WHERE email = auth.jwt()->>'email' AND role = 'admin' AND status = 'active'));
