# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Chief Privacy Officer |
| Approved by | Executive risk committee |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, acquisitions, or new contract types |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-3, AC-21, MP-3, MP-5, MP-6, SC-8, SC-28, SI-12, CP-9, SA-9 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11 |
| Contract and legal basis | State exhibits (MP, SC, SI families); 32 CFR Part 2002 (CUI); FERPA 34 CFR 99.33(a); FAR 52.204-21(b)(1)(vii) |

## 1. Purpose
Classify company and customer information by sensitivity and set handling rules so protection matches the risk and the obligations attached to each type, including CUI, student records, biometric data, and security system records.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and subcontractor personnel working under company accounts) in all segments and acquired businesses from their acquisition date, in Florida, Georgia, Alabama, South Carolina, North Carolina, Tennessee, Virginia, Maryland, and the District of Columbia. Covers all company systems and data (cloud, colocation, SaaS, ROCs, endpoints, and the OT edge), the company's administration of customer building systems through the IBOP, customer data the company holds, and systems that vendors and subcontractors operate for the company. GSA systems that company staff use under GSA's authorization are governed by GSA policy; this policy governs the company staff who use them.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Privacy Officer | Owns classification, retention, and breach determinations |
| Vice President, Government Contracts Compliance | CUI program; CUI Program Manager reports here |
| Data owners (segment presidents and system owners) | Classify their data and approve access |
| Customer custodians | Decide public records requests for customer records |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its contract or regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Information must be classified as Restricted (CUI, cardholder records with access history, face templates, student records, security system layouts and door schedules, employee SSNs and background checks, credentials), Confidential (financial, legal, material nonpublic information, non-CUI drawings), Internal, or Public, and labeled where systems allow. (RA-2; ID.AM-07)
4.2 Restricted data must be encrypted at rest and in transit under STD-04.1. Where an OT protocol cannot be encrypted, the traffic must stay inside a segmented OT network. (SC-28; SC-8; PR.DS-01)
4.3 CUI must be kept only in the CUI enclave, marked before it is shared, and shared only with recipients who are authorized and trained; any mishandling must be reported to the GSA contracting officer. (AC-3; MP-3; PR.DS-01)
4.4 Student cardholder records must be used only for the contracted purpose and must not be redisclosed without the university's direction. (AC-21; PR.DS-10)
4.5 Customer data must be kept only as long as STD-04.5 and the customer's schedule allow: cardholder records of departed people and face templates must be deleted within 30 days after the customer's retention date, withdrawal, or departure. (SI-12; PR.DS-01)
4.6 Media holding Restricted or Confidential data must be sanitized before reuse and destroyed by a certified vendor with a certificate before disposal. (MP-6; PR.DS-01)
4.7 Backups of Restricted data and of controller programs and door schedules must be encrypted, immutable, stored in a separate account, and restore-tested at least quarterly for tier-1 systems. (CP-9; PR.DS-11)
4.8 Restricted data must not be entered into any AI tool unless the AI governance committee has approved the use case and the tool's terms prohibit training on company or customer data. (SA-9; PL-4; GV.SC-05)
4.9 Public records requests for customer records must be routed to the customer's custodian within 1 business day, and security system records must be labeled exempt when created. (AC-21; MP-3; PR.DS-10)
4.10 Video exports must follow the chain-of-custody procedure (PRC-04.1), with a hash recorded for each export. (MP-5; AU-10; PR.DS-01)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-04.1 Encryption Standard
- STD-04.2 Media Protection and Disposal Standard
- STD-04.3 Backup Standard
- STD-04.4 CUI and Security Records Handling Standard
- STD-04.5 Customer Data Retention Standard
- PRC-04.1 Video Evidence Export Procedure
- PRC-04.2 Public Records Request Routing Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), quarterly access certifications, and customer audits. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm. Subcontractor violations are handled under the subcontract and may end the subcontractor's access.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. An exception never waives a customer contract term or a law.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 IBOP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance; the contract obligations register.
