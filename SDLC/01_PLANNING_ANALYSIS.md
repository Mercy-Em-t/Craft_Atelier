# 01 Planning & Analysis: Supabase Migration

## 1. Scope
- **Objective:** Transition the current mocked DIY Kit fulfillment pipeline to a live Supabase environment (Phase 2).
- **Core Components:**
  - Setup core PostgreSQL tables (`kits`, `orders`, `fulfillment_logs`).
  - Implement a PostgreSQL Finite State Machine (FSM) for order statuses (`QUEUED_FOR_PACKING`, `PACKING_IN_PROGRESS`, `STAGED_FOR_DISPATCH`, `IN_TRANSIT`, `DELIVERED`, `CANCELLED`).
  - Develop Role-Based Access Control (RBAC) with specific RPC actions for Operations Staff and full capabilities for Business Admins.
  - Implement Database Webhooks and Edge Functions for automated WhatsApp notifications.
- **Out of Scope (for now):** Complementary systems like ERP Lite, CRM, Automated Label Printing, and Interactive Video Platform.

## 2. Security Requirements
- **Role-Based Access Control (RBAC):**
  - **Operations Staff:** Restricted access. Can only view fulfillment details (no financials) and execute specific state-advancing RPCs (`verify_and_stage_order`, `dispatch_order`).
  - **Business Admin:** Full access to financials, inventory, overrides, and catalog updates.
- **Data Integrity:** Strict PostgreSQL RLS (Row Level Security) policies to enforce the above access controls.
- **Audit Logging:** Every state transition and verification must record securely in the `fulfillment_logs` table (Zero-Mistake check log).
- **API Security:** Edge functions must validate webhook payloads to prevent unauthorized execution. WhatsApp API tokens must be securely stored in Supabase Vault/Secrets.

## 3. Milestones
- **Milestone 1: Database Setup & Migration (Week 1)**
  - Provision Supabase project.
  - Create schemas, tables, and relationships.
  - Migrate mocked data into the live PostgreSQL database.
- **Milestone 2: Security & State Machine (Week 2)**
  - Define RLS policies for Operations and Admin roles.
  - Implement FSM constraints for order status transitions.
  - Create secure RPC functions for fulfillment actions.
- **Milestone 3: Automations & Edge Functions (Week 3)**
  - Implement Supabase Webhooks for state changes.
  - Deploy Edge Functions for WhatsApp Cloud API integration (send alerts & receive notes).
- **Milestone 4: Dashboard Integration & Testing (Week 4)**
  - Connect the mobile PWA (Operations) and Admin dashboards to live Supabase REST/GraphQL endpoints.
  - Perform end-to-end user acceptance testing (UAT).
  - Go-live!
