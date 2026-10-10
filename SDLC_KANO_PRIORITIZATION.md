# SDLC Kano Prioritization Analysis

## 1. Methodology & Scale
We interviewed 4 key stakeholders: Customer (CUST), System Admin (ADM), Warehouse/Support Ops (OPS), and Independent Creator (CRE).

**Functional Assessment (Presence):** How do you feel if this feature is present?
`1=Dislike | 2=Live With | 3=Neutral | 4=Expect | 5=Like`

**Dysfunctional Assessment (Absence):** How do you feel if this feature is absent?
`1=Like | 2=Expect | 3=Neutral | 4=Live With | 5=Dislike (Hate that it's missing)`

## 2. Tabular Data (Scores & Statistics)
| Use Case | Description | Func Scores (C,A,O,Cr) | Dys Scores (C,A,O,Cr) | Avg Func (Y) | StdDev Func | Avg Dys (X) | StdDev Dys | Category |
|---|---|---|---|---|---|---|---|---|
| **UC-04 Interactive Tutorial** | Navigate video and text pattern UI. | [5,3,3,4] | [5,4,3,4] | **3.75** | *0.96* | **4.00** | *0.82* | **Must-Be** |
| **UC-12 Manage Global Inventory** | Reconcile physical counts vs database. | [3,5,4,3] | [3,5,5,3] | **3.75** | *0.96* | **4.00** | *1.15* | **Must-Be** |
| **UC-01 Checkout & Pay** | Process order via M-Pesa. | [5,5,4,5] | [5,5,4,5] | **4.75** | *0.50* | **4.75** | *0.50* | **One-Dimensional** |
| **UC-10 Input Delivery PIN** | Customer provides PIN to rider for handoff. | [4,5,5,4] | [5,5,5,4] | **4.50** | *0.58* | **4.75** | *0.50* | **One-Dimensional** |
| **UC-18 Process Customer Refund** | Issue partial/full refunds via M-Pesa. | [5,5,4,4] | [5,5,4,5] | **4.50** | *0.58* | **4.75** | *0.50* | **One-Dimensional** |
| **UC-17 Review Support Escalations** | Support views user history to solve tickets. | [4,5,5,3] | [4,5,5,3] | **4.25** | *0.96* | **4.25** | *0.96* | **One-Dimensional** |
| **UC-09 Batch Dispatch Orders** | Group orders and assign to Boda rider. | [4,5,5,3] | [4,4,5,3] | **4.25** | *0.96* | **4.00** | *0.82* | **One-Dimensional** |
| **UC-07 Scan & Verify BOM** | Packers verify physical items using tablet. | [3,5,5,3] | [3,5,5,3] | **4.00** | *1.15* | **4.00** | *1.15* | **One-Dimensional** |
| **UC-08 Flag Stock Exception** | Mark order On-Hold if yarn is damaged. | [3,5,5,3] | [3,5,5,3] | **4.00** | *1.15* | **4.00** | *1.15* | **One-Dimensional** |
| **UC-16 Disburse Creator Royalties** | Admin triggers M-Pesa B2C payouts. | [3,5,3,5] | [3,5,3,5] | **4.00** | *1.15* | **4.00** | *1.15* | **One-Dimensional** |
| **UC-02 Bulk Address CSV** | Upload multiple addresses at once. | [4,5,4,3] | [3,4,3,3] | **4.00** | *0.82* | **3.25** | *0.50* | **Attractive** |
| **UC-05 Trigger Panic Button** | SOS video call for immediate help. | [5,4,4,3] | [2,3,3,3] | **4.00** | *0.82* | **2.75** | *0.50* | **Attractive** |
| **UC-15 View Royalty Dashboard** | Creators track their cleared sales volume. | [3,4,3,5] | [3,3,3,5] | **3.75** | *0.96* | **3.50** | *1.00* | **Indifferent** |
| **UC-11 Update Business Settings** | Admin updates dynamic Till numbers. | [3,5,3,3] | [3,5,3,3] | **3.50** | *1.00* | **3.50** | *1.00* | **Indifferent** |
| **UC-13 View Financial/Audit Logs** | View unchangeable historical order data. | [3,5,3,3] | [3,5,3,3] | **3.50** | *1.00* | **3.50** | *1.00* | **Indifferent** |
| **UC-14 Generate Tax CSV** | Format sales data for KRA e-TIMS. | [3,5,3,3] | [3,5,3,3] | **3.50** | *1.00* | **3.50** | *1.00* | **Indifferent** |
| **UC-03 Create Modular SKU** | Creators drag-and-drop materials to launch kits. | [3,4,3,5] | [3,3,3,4] | **3.75** | *0.96* | **3.25** | *0.50* | **Indifferent** |
| **UC-06 Left-Handed Mirror** | CSS toggle to reverse tutorial visuals. | [5,3,3,4] | [2,3,3,3] | **3.75** | *0.96* | **2.75** | *0.50* | **Indifferent** |

## 3. Kano Categorization Plane
```text
        High Satisfaction (Func -> 5)
             ^ 
             |     ATTRACTIVE (Delighters)      | ONE-DIMENSIONAL (Performance)
             |     (High F, Low D)              | (High F, High D)
             |                                  |
Functional   |     * UC-05 Panic Button         | * UC-01 Checkout
Average (Y)  |     * UC-06 Mirror Mode          | * UC-10 Delivery PIN
             |     * UC-03 Modular SKU          | * UC-09 Batch Dispatch
             |                                  | * UC-18 Process Refund
        -----+----------------------------------+------------------------------> High Frustration if missing (Dys -> 5)
             |     INDIFFERENT (Low ROI)        | MUST-BE (Basic Expectations)
             |     (Low F, Low D)               | (Low F, High D)
             |                                  |
             |     * UC-11 Business Settings    | * UC-07 Scan BOM
             |     * UC-14 Tax CSV              | * UC-12 Manage Inventory
             |     * UC-13 Audit Logs           | * UC-16 Disburse Royalties
        Low  |                                  |
```

## 4. Priority Assessment & Total Ordering
Based on the mathematical averages and categorizations, we have derived a strict implementation priority. **Must-Be** features form the uncompromisable foundation (without them, the business cannot operate or is illegal). **One-Dimensional** features form the core performance tier where more execution equals more satisfaction. **Attractive** features are delayed to Phase 2/3 as they are strictly 'Delighters', and **Indifferent** features are pushed to the backlog.

### Total Ordering of Priority:
**1. UC-04 Interactive Tutorial** (Must-Be)  
**2. UC-12 Manage Global Inventory** (Must-Be)  
**3. UC-01 Checkout & Pay** (One-Dimensional)  
**4. UC-10 Input Delivery PIN** (One-Dimensional)  
**5. UC-18 Process Customer Refund** (One-Dimensional)  
**6. UC-17 Review Support Escalations** (One-Dimensional)  
**7. UC-09 Batch Dispatch Orders** (One-Dimensional)  
**8. UC-07 Scan & Verify BOM** (One-Dimensional)  
**9. UC-08 Flag Stock Exception** (One-Dimensional)  
**10. UC-16 Disburse Creator Royalties** (One-Dimensional)  
**11. UC-02 Bulk Address CSV** (Attractive)  
**12. UC-05 Trigger Panic Button** (Attractive)  
**13. UC-15 View Royalty Dashboard** (Indifferent)  
**14. UC-11 Update Business Settings** (Indifferent)  
**15. UC-13 View Financial/Audit Logs** (Indifferent)  
**16. UC-14 Generate Tax CSV** (Indifferent)  
**17. UC-03 Create Modular SKU** (Indifferent)  
**18. UC-06 Left-Handed Mirror** (Indifferent)  
