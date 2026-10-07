# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (holding company, GBS, and all subsidiaries) |
| Policy ID | POL-04 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Chief Privacy Officer |
| Approved by | Executive risk committee |
| Approval date | 2026-09-14 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-3, AC-16, MP-1, MP-6, SC-8, SC-28, SI-7, SI-12, CP-9 |
| CSF 2.0 | ID.AM-05, ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11 |
| Regulatory drivers | 16 CFR 314.4(c)(1)(ii), (c)(2), (c)(3), (c)(6) for Finance; 45 CFR 164.504(f)(2)(iii) and 164.314(b) (N55-R06); Fla. Stat. 501.171(2), (8) (worked example); Rule 13a-15 (MNPI) |

## 1. Purpose
Classify the group's information by the harm its disclosure, alteration, or loss would cause, and set handling rules that match, including the rules that keep each subsidiary's restricted data within that subsidiary and out of AI tools that do not need it.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary staff) of the holding company, Global Business Services (GBS), and every subsidiary (Building Products, Home Services, Manufacturing, and Finance), at all sites in the six operating states, including acquired businesses from their closing date. Covers all systems and data, including cloud, data centers, SaaS, plant OT, systems that vendors operate for the group, and the services offered to outside customers (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Privacy Officer | Owns classification; approves new uses of Restricted data |
| Data owners (system owners and subsidiary Presidents) | Classify their data; approve access; approve sharing of their Restricted data with other entities |
| CISO | Encryption, labeling, backup, and disposal standards |
| Finance Information Security Officer | Agrees to any handling exception for Finance customer information |
| Treasurer | Payment file integrity |
| All workforce | Handle information according to its class |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested a mapped control in 2026 (P07).

4.1 All information must be classified as Public, Internal, Confidential, or Restricted. Restricted includes MNPI, Finance customer information, SSNs and bank account data, plan PHI, and bank and treasury credentials. (RA-2; ID.AM-05)
4.2 Confidential and Restricted data must be encrypted in transit over external networks and at rest. (SC-8; SC-28; PR.DS-01; PR.DS-02)
4.3 Any collaboration site or library holding Restricted data must carry a Restricted sensitivity label. Labeled locations must not be shared with all employees and are excluded from AI assistant retrieval unless the data owner approves. (AC-16; AC-3; PR.DS-01)
4.4 An inventory of Restricted data locations, including copies in the data warehouse and file shares, must be maintained. (CM-12; ID.AM-07)
4.5 Data must be retained and destroyed per the retention schedule and legal holds. Finance customer information must be disposed of no later than two years after its last use for the customer unless an exception in the Safeguards Rule applies. (SI-12; MP-6; PR.DS-01)
4.6 Group health plan PHI may be kept only in the restricted benefits site and used only by the staff named in the plan documents, never for employment decisions. (AC-3; PR.AA-05)
4.7 Payment files must be created, approved, and sent only through the payment hub, which hashes and verifies them. Manually prepared payment files require a Treasurer-approved exception. (SI-7; PR.DS-01)
4.8 Backups of tier-1 data must be immutable and stored in a separate account, with an offline copy. (CP-9; PR.DS-11)
4.9 MNPI must be handled under PRC-04.1: deal rooms and earnings drafts in access-listed locations, insiders listed, and trading blackouts applied. (AC-3; PR.DS-01)
4.10 Restricted data may be entered only into AI tools on the approved list (STD-05.3) and only for approved purposes. (AC-20; PR.DS-10)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-04.1 Encryption Standard
- STD-04.2 Media Protection and Disposal Standard
- STD-04.3 Backup Standard
- STD-04.4 Records Retention Standard
- STD-04.5 Sensitivity Labeling Standard
- PRC-04.1 MNPI and Deal Room Handling Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, quarterly sub-certifications, access certifications, and the annual Internal Audit assessment (P07). Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 SCSP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance; Finance WISP annex (SUP-FIN); Manufacturing OT annex (SUP-MFG).
