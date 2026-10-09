# 03 Implementation Plan: Supabase Migration

## Objective
Migrate the mocked DIY Kit fulfillment system to the live Supabase environment as described in the End-to-End System Architecture.

## Execution Steps

### 1. Remove Mock Wrappers
* **Audit HTML Files**: Locate all operations and admin dashboard HTML files.
* **Strip Hardcoded Data**: Remove static JSON/arrays representing `kits`, `orders`, and `fulfillment_logs`.
* **Remove Mock Functions**: Delete any client-side JavaScript simulating database latency or state transitions.

### 2. Inject Supabase Credentials Securely
* **Client Library Integration**: Include the Supabase JS client via CDN or build pipeline.
* **Environment Variables**: Configure the build process or hosting provider to inject `SUPABASE_URL` and `SUPABASE_ANON_KEY` as environment variables.
* **Security Check**: Ensure the `service_role` key is strictly kept out of client-facing HTML and is only used in secure backend edge functions.

### 3. Implement Live Database Queries
* **Catalog & Orders**: Bind the UI lists to `supabase.from('kits').select()` and `supabase.from('orders').select()`.
* **State Machine RPCs**: Map the verification and dispatch buttons on the Operations Dashboard to the Supabase RPCs `verify_and_stage_order` and `dispatch_order`.
* **Audit Logging**: Ensure packing check-offs write directly to the `fulfillment_logs` table.

### 4. Deploy and Push Live
* **Environment Setup**: Set production database credentials in the deployment hosting environment (e.g., Vercel, Netlify).
* **Push Code**: Commit all live integration changes and push to the production branch.
* **Smoke Testing**: Run a test order from `QUEUED_FOR_PACKING` through to `IN_TRANSIT` to ensure edge functions and WhatsApp API webhooks fire correctly.
