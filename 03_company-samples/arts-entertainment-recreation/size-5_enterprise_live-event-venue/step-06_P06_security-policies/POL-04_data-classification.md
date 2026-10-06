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
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | RA-2, SC-8, SC-28, SI-12, MP-6, AC-6, PT-5, AC-20 |
| CSF 2.0 | ID.AM-05, PR.DS-01, PR.DS-02 |
| Regulatory basis | PCI DSS v4.0.1 Requirements 3, 4, and 9.4 (N71-R04); FTC Act Section 5 (N71-R05); state privacy and breach laws (Fla. Stat. 501.171(8) worked example) |

## 1. Purpose
Classify company, patron, client, and card data, and set handling rules for each class so the most sensitive data gets the strongest protection and is kept no longer than needed.

## 2. Scope
All Cris Santos Company workforce members (employees, part-time and seasonal event staff, contractors, and interns) at headquarters, all 36 venues in 8 states, the 3 festivals, and the two contact centers, including acquired venues from their acquisition date. Covers all systems and data, including cloud, colocation, SaaS, venue operational technology, and systems that service providers and other vendors operate for the company, and the services the company offers to business clients (SL-1 white-label ticketing and SL-2 venue management).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Privacy Officer | Policy owner; retention schedule; privacy reviews |
| Director of Payments and PCI Compliance | Card data handling rules; card data discovery |
| Data owners | Classify their data and approve access |
| Director of Data Engineering | Warehouse retention, minimization, and masking |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 All data must be classified as Restricted (card data, sensitive authentication data, credentials, keys, biometric data), Confidential (patron, client, and employee personal data; client business data), Internal, or Public, and labeled or tagged where systems allow. (RA-2; ID.AM-05)
4.2 Restricted and Confidential data must be encrypted in transit with TLS 1.2 or higher and at rest with approved algorithms and customer-managed keys. (SC-8; SC-28; PR.DS-01; PR.DS-02)
4.3 Sensitive authentication data must never be stored after authorization, and full card numbers must exist only inside the payment service and the tokenization provider: never in email, chat, case notes, recordings, spreadsheets, or tickets. (SI-12; MP-6; PR.DS-01)
4.4 Phone payments must be taken only through the agent payment page with keypad entry or with call recording paused or masked while card data is spoken. (MP-6; PR.DS-01)
4.5 Data must be kept only as long as the retention schedule allows and then disposed of so it cannot be read or reconstructed. (SI-12; MP-6; PR.DS-01)
4.6 Analysts must use minimized and masked views of patron data; raw patron tables are limited to the data engineering role. (AC-6; PR.AA-05)
4.7 Any new use of patron data, including a new AI feature or a new tag on a company or client site, requires a privacy review and, for AI, an AI governance review (P10) before go-live. (RA-3; PT-5; GV.OC-03)
4.8 The privacy notice must describe actual practices, and opt-out preference signals must be honored on every site the company operates, including client templates. (PT-5; GV.OC-03)
4.9 Restricted data must never be entered into AI tools, and Confidential data only into tools on the approved AI tools list (STD-05.3). (AC-20; PR.DS-01)
4.10 Biometric data, including face templates, may be collected only with AI governance committee approval, counsel's review of the laws of each state where it is collected, and opt-in consent. (PT-5; RA-3; GV.OC-03)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-04.1 Encryption Standard
- STD-04.2 Media Protection, Retention, and Disposal Standard
- STD-04.3 Backup Standard
- STD-04.4 Phone Payment Handling Standard
- PRC-04.1 Data Extract Registration Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), the QSA's Reports on Compliance, and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 TVOP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
