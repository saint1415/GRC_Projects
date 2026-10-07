# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Deputy General Counsel, Privacy (with the SVP FSQA for food safety records) |
| Approved by | Executive risk committee |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-3, AU-9, AU-10, SC-8, SC-28, SI-12, AU-11, CP-9, MP-6, SA-9 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11 |
| Regulatory drivers | 9 CFR 416.16, 417.5; 21 CFR 117.305, 117.315, 121.305, 121.315; Fla. Stat. 501.171(8) |

## 1. Purpose
Make sure every kind of company and customer information is classified, handled, kept, and destroyed according to its sensitivity, and that food safety records stay trustworthy enough for FSIS and FDA review.

## 2. Scope
All Cris Santos Company workforce members (employees, agency temporary workers, contractors, and interns) at the 8 plants, 4 distribution centers, headquarters, and regional offices in Florida, Georgia, Alabama, North Carolina, Tennessee, and Texas, including acquired operations from their acquisition date. Covers all IT and OT systems and data, including plant control systems, refrigeration controls, cloud, colocation, SaaS, and systems vendors operate for the company, and the services the company offers to external customers (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Deputy General Counsel, Privacy | Owns the classification scheme and personal information handling |
| Senior Vice President, Food Safety and Quality Assurance | Owns food safety record integrity and retention |
| Data owners | Classify their data and approve access |
| Director of Cloud Platform Engineering | Encryption and backup services |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Information must be classified in one of four levels. **Restricted:** the PLT-07 food defense plan and vulnerability assessment; formulations and cure specifications; SL-2 customer specifications; PLC programs and OT network diagrams; employee Social Security numbers and bank data; credentials. **Confidential:** HACCP, SSOP, food defense, and preventive controls records; SL-1 customer inventory and temperature data; pricing and contracts; consumer accounts. **Internal:** production schedules, procedures, training materials. **Public:** website, labels, published reports. (RA-2; ID.AM-07)
4.2 The PLT-07 food defense plan and vulnerability assessment must be kept in a restricted library limited to named roles, with a controlled printed copy at PLT-07 so the plan stays available onsite during outages. (AC-3; PR.DS-01)
4.3 Record integrity. CCP, SSOP, food defense, and preventive controls records must be created under named accounts at the time of the activity, keep an audit trail of every change, and be locked after sign-off. Plant historians must keep audit trails enabled. Corrections must be made by a new entry that keeps the original. (AU-9; AU-10; PR.DS-10)
4.4 Restricted and Confidential data must be encrypted in transit. Restricted data must also be encrypted at rest on every device and service. (SC-8; SC-28; PR.DS-02)
4.5 Retention. HACCP records follow 9 CFR 417.5(e) (at least 1 year for refrigerated products and 2 years for frozen, preserved, or shelf-stable products); SSOP records at least 6 months (9 CFR 416.16(c)); Part 121 and Part 117 records at least 2 years (21 CFR 121.315; 117.315). For simplicity the company keeps every such record for 3 years after preparation. (SI-12; AU-11; PR.DS-11)
4.6 Backups of Restricted and Confidential data, including PLC programs, MES databases, and records, must be encrypted, stored apart from production (a separate account or offline), protected from alteration, and restore-tested at least annually for each plant and quarterly for the MES. (CP-9; PR.DS-11)
4.7 Media and devices holding Restricted or Confidential data, including replaced HMIs and engineering workstations, must be wiped or destroyed by a certified vendor that provides a certificate of destruction. (MP-6; PR.DS-01)
4.8 Restricted data must not be entered into AI tools or other third-party services unless the AI council has approved the tool and its contract bars training on company data (POL-05 4.8). (SA-9; GV.SC-05)
4.9 SL-2 customer specifications may be used only for that customer's production and only by named SL-2 and FSQA staff. (AC-3; AC-6; PR.AA-05)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-04.1 Encryption Standard
- STD-04.2 Media Protection and Disposal Standard
- STD-04.3 Backup Standard (IT and OT)
- STD-04.4 Food Safety Record Integrity Standard
- PRC-04.1 Formulation and Food Defense Document Handling Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, OT monitoring, the annual Internal Audit assessment (P07), and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.9), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 PPCM SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance; the PLT-07 food defense plan and the plant HACCP plans.
