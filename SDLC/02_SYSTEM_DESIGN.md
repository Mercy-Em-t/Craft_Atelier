# 02. System Design: Production Deployment & Security

## 1. Production Hosting Strategy
The DIY Kit system heavily utilizes a decentralized and managed approach for maximum scalability and zero-maintenance operations.
* **Frontend Dashboards (Operations & Business Admin):** 
  - **Hosting:** Vercel or Netlify. Since the operations dashboard is a mobile-optimized standalone HTML/PWA and the admin dashboard consists of static assets talking directly to the Supabase REST API, hosting on Vercel/Netlify provides global edge CDN delivery. GitHub Pages is also a viable fallback.
  - **CI/CD:** Automated deployments connected to the main GitHub repository. Every merge to `main` triggers a production build.

## 2. Supabase Edge Function Deployment
* **Workflow:** Edge Functions (e.g., WhatsApp Cloud API integration, webhook listeners) will be deployed to Supabase edge.
* **Tooling:** Using the Supabase CLI (`supabase functions deploy <function_name>`).
* **Environment Variables:** Securely managed within the Supabase Dashboard, housing secrets like WhatsApp API tokens and database service keys.

## 3. Database Security Rules (Row Level Security - RLS)
Supabase (PostgreSQL) relies heavily on RLS to enforce the strict RBAC defined in the architecture.
* **Operations Staff (Role: `ops_staff`):**
  - **Read:** Allowed to read specific columns in `orders` (recipient, delivery landmark, phone, BOM checklists). Explicitly denied read access to `price_cents` or revenue margins.
  - **Write:** Allowed to insert into `fulfillment_logs`. Allowed to invoke specific RPCs (`verify_and_stage_order`, `dispatch_order`) to transition states.
* **Business Admin (Role: `admin`):**
  - **Read/Write:** Full access to all tables (`kits`, `orders`, `fulfillment_logs`), including margins, analytics, overrides, and catalog updates.
* **Public/Customers:**
  - **Read:** Read-only access to active catalog (`kits`).
  - **Write:** Secure webhook ingestion for WhatsApp replies.
