# SDLC Domain Specification Model Directory

Because the Craft Atelier platform is too large and complex to be legible on a single Domain Model Diagram, we have decomposed the system into three mutually consistent sub-models. 

These models adhere to strict Domain-Driven Design (DDD) and Jackson's Problem Frames conventions, explicitly separating **Environmental Phenomena** (the real world) from **Interface Phenomena** (the machine/software).

## Domain Sub-Models

| Sub-Domain | Description | Use Cases Covered |
|---|---|---|
| [1. E-Commerce & Intake](./01_ECommerce_Intake_Domain.md) | Customer interactions, STK Push APIs, and Interactive Tutorials. | UC-01, 04, 05, 06 |
| [2. Warehouse Operations & Dispatch](./02_Warehouse_Operations_Domain.md) | Tablet Packing UI, Inventory tracking, WhatsApp APIs, and Boda Logistics. | UC-07, 08, 09, 10, 12 |
| [3. Admin, Creator SKUs & Finance](./03_Admin_Finance_Domain.md) | Royalty Ledgers, M-Pesa B2C, Tax Compliance, and Modular SKU building. | UC-02, 03, 11, 13, 14, 15, 16, 17, 18 |
