# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Chief Privacy Officer (with the Director of Payments and PCI Compliance for cardholder data) |
| Approved by | Executive risk committee |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | RA-2, SC-8, SC-28, SI-12, MP-4, MP-6, CP-9, CM-12, AC-21 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-11 |
| Regulatory basis | PCI DSS 3, 4, 9.4; Fla. Stat. 501.171(8) and 509.101(2); FTC Disposal Rule |

## 1. Purpose
Make sure guest, card, employee, and company information is classified, stored only where it should be, protected in proportion to its sensitivity, and kept no longer than needed.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary staff) at headquarters, the regional offices, the contact center, and the 110 company-operated hotels in 33 states and DC, including acquired hotels from their acquisition date. Covers all systems and data, including cloud, colocation, SaaS, payment devices, and hotel building and guest-room technology, and the systems and services the company provides to franchisees and distribution clients (SL-1 and SL-2). Franchisees are bound through the brand technology standards and the franchise agreement, not directly by this policy.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Privacy Officer | Owns the classification scheme and retention schedule |
| Director of Payments and PCI Compliance | Owns cardholder data rules and the card vault |
| Data owners | Classify data and approve access and sharing |
| Hotel general managers | Apply handling rules at company-operated hotels |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Information must be classified as Restricted (card data, sensitive authentication data, identity document numbers, biometric data, credentials, bank data), Confidential (guest profiles, loyalty data, folios, financial data, non-public rates and occupancy, material nonpublic information), Internal, or Public, and labeled where systems allow. (RA-2; ID.AM-07)
4.2 Card numbers must be stored only in the card vault; every other system must hold tokens. Sensitive authentication data must never be kept after authorization. (SC-28; SI-12; PR.DS-01)
4.3 Card numbers must not be accepted or sent by email, chat, messaging, or paper forms. Staff must use secure payment links, P2PE terminals, or tone-masking capture. (SC-8; PR.DS-02)
4.4 Restricted data must be encrypted at rest and in transit using STD-04.1, including inside hotel networks. (SC-28; SC-8; PR.DS-01)
4.5 Non-public rate, occupancy, and revenue data must not be shared with competitors or pooled into vendor benchmarks without General Counsel approval. (AC-21; GV.OC-03)
4.6 Paper records with card or identity data must be kept in locked storage and cross-cut shredded when no longer needed; media must be sanitized or destroyed with a certificate. (MP-4; MP-6; PR.DS-01)
4.7 Backups of Restricted data must be encrypted, immutable, stored in a separate account or location, and restore-tested at least quarterly for tier-1 systems. (CP-9; PR.DS-11)
4.8 Records must be kept per STD-04.4: Florida guest register data at least 2 years (Fla. Stat. 509.101(2)); identity document numbers deleted 30 days after checkout; card data in the vault purged 13 months after checkout; guest profiles deleted after 5 years without a stay unless the guest keeps a loyalty account. (SI-12; PR.DS-11)
4.9 Restricted or Confidential data must not be entered into any AI tool unless the AI governance committee has approved the use case and the contract prohibits training on company data. (SA-9; PL-4; GV.SC-05)
4.10 Data discovery scans for card numbers must run at least quarterly on mailboxes, file shares, chat transcripts, and the data warehouse, and before each PCI DSS scope confirmation. (CM-12; ID.AM-07)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-04.1 Encryption and Tokenization Standard
- STD-04.2 Media Protection and Disposal Standard
- STD-04.3 Backup Standard
- STD-04.4 Records Retention Schedule
- PRC-04.1 Card Data Discovery and Purge Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), the QSA's PCI DSS assessments, and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm. Franchisee violations of brand technology standards are handled under the franchise agreement.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 PPP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance; brand technology standards BS-TECH-01 to BS-TECH-06.
