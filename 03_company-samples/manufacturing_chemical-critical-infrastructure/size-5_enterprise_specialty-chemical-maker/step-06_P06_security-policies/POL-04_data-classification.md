# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Chief Data and Analytics Officer (with the PLT-01 Facility Security Officer for SSI) |
| Approved by | Executive risk committee |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-1, MP-3, MP-4, MP-6, SC-8, SC-28, CP-9, AC-21 |
| CSF 2.0 | ID.AM-05, PR.DS-01, PR.DS-02, PR.DS-11 |
| Regulatory drivers | SSI 49 CFR Part 1520 (101.630(b)); MTSA 33 CFR 101.650(c); state breach laws; toll agreements; EAR (export compliance program); legacy CVI (6 CFR 27.400) |

## 1. Purpose
Classify company information so that the people who handle it know how to protect it, with the strongest protection for Sensitive Security Information, formulations and toll customer recipes, and process control and safety logic.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, integrators, and temporary staff) at all 14 plants, 9 distribution centers, 2 R&D centers, and offices, including acquired plants from their acquisition date. Covers all information technology (IT) and operational technology (OT): process control systems, safety instrumented systems, PLCs, terminal and loading rack automation, cloud, colocation, SaaS, and systems that vendors and integrators operate for the company, and the services the company offers to external customers (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Data and Analytics Officer | Owns the classification scheme and data catalog |
| PLT-01 Facility Security Officer | SSI designation and handling at PLT-01 |
| Data owners | Classify their data and approve access |
| Chief Compliance Officer | EAR-controlled technology tagging with the export compliance program |
| All workforce | Label and handle information by its class |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 All information must be classified as Restricted, Confidential, Internal, or Public. Restricted includes SSI, legacy CVI, formulations, toll customer recipes, control and safety logic, network maps of OT, and EAR-controlled technology. (RA-2; ID.AM-05)
4.2 SSI, including MTSA Facility Security Plans, Cybersecurity Plans, and assessments, must be stored only in the SSI repository, marked, and shared only with covered persons with a need to know. (MP-3; AC-3; PR.DS-01)
4.3 Restricted and Confidential data must be encrypted in transit and at rest where technically feasible. Where OT protocols cannot be encrypted, segmentation and monitoring must compensate under an approved exception. (SC-8; SC-28; PR.DS-02)
4.4 Toll customer recipes and batch records must be accessible only to the customer and the staff assigned to that customer, and must never be used for another customer's products. (AC-3; AC-21; PR.DS-01)
4.5 Control logic, SIS programs, recipes, and OT configurations must be backed up to the offline OT vault after every approved change, with integrity checks. (CP-9; SI-7; PR.DS-11)
4.6 Removable media must be company-issued, scanned at a media kiosk before use on OT, and stored securely; unused ports on OT devices must be disabled. (MP-7; MP-4; PR.PS-01)
4.7 Media and devices that held Restricted or Confidential data must be sanitized before reuse or disposal following NIST SP 800-88. (MP-6; PR.DS-01)
4.8 Personal information of employees and customers must be kept only as long as needed and protected under the law of each state where the individuals reside. (SI-12; PM-5(1); PR.DS-01)
4.9 EAR-controlled technology must be tagged and kept out of shared workspaces open to foreign persons unless the export compliance program has approved access. (AC-3; AC-21; PR.DS-01)
4.10 Legacy CVI must remain in the restricted repository and be handled as Restricted while CFATS is lapsed. (MP-4; AC-3; PR.DS-01)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-04.1 Encryption Standard
- STD-04.2 Media Protection and Disposal Standard
- STD-04.3 Backup Standard (IT and OT vault)
- STD-04.4 SSI and CVI Handling Standard
- PRC-04.1 SSI Handling Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring (including OT metrics), the annual Internal Audit assessment (P07), access certifications, and MTSA Cybersecurity Plan audits at PLT-01. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 GC-PCBMS SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
