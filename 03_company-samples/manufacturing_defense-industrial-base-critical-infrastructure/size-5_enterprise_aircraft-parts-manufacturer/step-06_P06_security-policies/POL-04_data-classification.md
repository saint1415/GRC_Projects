# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Vice President, Engineering (CUI data owner), with the Vice President, Trade Compliance |
| Approved by | Executive risk committee |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, acquisitions, or CMMC scope changes |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-1, MP-2, MP-3, MP-4, MP-5, MP-6, MP-7, SC-8, SC-13, SC-28, CP-9, SI-12, AC-22 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| SP 800-171, CMMC, and other drivers | SP 800-171 Rev. 2 3.1.22, 3.8.1 to 3.8.9, 3.13.8, 3.13.11, 3.13.16; 32 CFR 2002.14; 22 CFR 120.54(a)(5); 15 CFR 734.18(a)(5) |

## 1. Purpose
Classify company information by the harm its disclosure, alteration, or loss would cause, and set handling rules that match. Most of the company's CUI is controlled technical information, and much of it is also export-controlled.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, temporary workers, and interns) at all 8 sites in Florida, Georgia, Alabama, Texas, Kansas, and Arizona and at the 2 data centers, including acquired operations from their acquisition date. Covers all company systems and data, including the government-community and commercial clouds, SaaS, plant OT, and systems that suppliers and service providers operate for the company, with added rules for the CUI Engineering Enclave (CEE) and the Manufacturing Operations Zone (MOZ). The classified information system at FL-1 also follows NISPOM and DCSA requirements, which prevail where stricter.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Vice President, Engineering | CUI data owner; decides what is CUI when a customer marking is unclear |
| Vice President, Trade Compliance | Export classification (ITAR or EAR) and public release review |
| Vice President, Quality | Printed drawings and travelers on the shop floor |
| Director of Endpoint Engineering | Encryption, removable media, and sanitization |
| All workforce | Mark, handle, and dispose of information according to its class |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Information must be classified as Classified (handled only under NISPOM), CUI (including ITAR and EAR technical data), FCI and Confidential, Internal, or Public. (RA-2; ID.AM-07)
4.2 CUI may be stored and processed only in the CEE, the MOZ, and approved government-community cloud services. It must never be placed in the commercial cloud, corporate systems, personal devices, or unapproved AI or file-sharing services. (MP-2; AC-20; PR.DS-01)
4.3 CUI must carry the CUI banner and the customer distribution statement; PLM and print templates must add them automatically. (MP-3; PR.DS-01)
4.4 CUI must be encrypted at rest and in transit with FIPS-validated cryptography, recorded in the cryptography register for every CUI path. (SC-8; SC-13; SC-28; PR.DS-01; PR.DS-02)
4.5 Printed CUI must be kept in controlled cabinets when not in use, released only from badge-release printers, and shipped only by approved couriers with tracking. (MP-4; MP-5; PR.DS-01)
4.6 Media and equipment that held CUI, including machine controller drives sent for repair, must be sanitized per NIST SP 800-88 or destroyed, with a record kept before the item leaves company control. (MP-6; PR.DS-01)
4.7 Removable media are blocked on CEE and MOZ components except labeled, inventoried company drives approved by exception and scanned at a kiosk before every use. (MP-7; PR.DS-01)
4.8 Backups of CUI must be encrypted, immutable, held in separate accounts, and restore-tested at least quarterly for tier-1 systems. (CP-9; PR.DS-11)
4.9 Content may be posted publicly or presented at trade shows only after Trade Compliance confirms it contains no CUI or export-controlled data. (AC-22; PR.DS-01)
4.10 Generative AI tools may be used with CUI only if they are on the approved AI tools list (STD-05.3) and inside the government-community authorization boundary. (AC-20; SA-9; GV.SC-05)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-04.1 Encryption Standard
- STD-04.2 Media Protection and Disposal Standard
- STD-04.3 Backup Standard
- STD-04.4 CUI Marking Standard
- PRC-04.1 Public Release Review Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), access certifications, and the CMMC readiness checks before each affirmation. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm. A suspected unauthorized release of ITAR or EAR technical data is also referred to the Vice President, Trade Compliance for a voluntary disclosure decision.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 CEE SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
