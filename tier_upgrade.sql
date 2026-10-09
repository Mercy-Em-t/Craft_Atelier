ALTER TABLE staff_directory ADD COLUMN IF NOT EXISTS role TEXT DEFAULT 'packer' CHECK (role IN ('packer', 'dispatcher', 'admin'));
UPDATE staff_directory SET role = 'admin' WHERE email = 'memurugat@gmail.com';
