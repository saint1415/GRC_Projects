# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (and Cris Santos Payouts, LLC, under 23 NYCRR 500.2(d)) |
| Policy ID | POL-04 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Chief Data and Analytics Officer |
| Approved by | Executive risk committee |
| Approval date | 2026-09-08 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, new sponsor banks, or acquisitions |
| Implements (SP 800-53 Rev. 5) | RA-2, SC-28, SC-8, SI-12, CM-12(1), MP-6, SC-12, SC-13, AC-4, AC-20, SA-9, CP-9, SI-7, SI-7(5) |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-11 |
| Regulatory drivers | See `policy-control-map.csv` (one driver per statement) |

## 1. Purpose
Classify the company's information and set handling rules so that account data, customer information, and nonpublic information are protected wherever they are stored, processed, or transmitted, and are kept only as long as needed.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary staff) in every location, and Cris Santos Payouts, LLC, which adopted this program under 23 NYCRR 500.2(d). Covers all systems and data, including Cloud A, Cloud B, DC-1, DC-2, SaaS, and systems that service providers operate for the company, and the services the company provides to merchants, ISV partners, and sponsor Banks A, B, and C.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Data and Analytics Officer | Owns the classification scheme, data inventory, and PAN discovery |
| Data owners (business executives) | Classify their data; approve extracts and retention exceptions |
| Director of Cryptographic Services | Key management and the cryptographic architecture |
| All workforce | Handle data by its class |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

**Classification scheme:**

| Class | Examples | Minimum handling |
|---|---|---|
| Restricted | PAN, sensitive authentication data, cryptographic keys, merchant owner SSNs and bank accounts, funding files, payout destinations | Encrypted at rest and in transit; CDE or approved stores only; no AI tools; access by named role |
| Confidential | Tokens, transaction data without PAN, merchant business data, customer information under 16 CFR 314, nonpublic information under 23 NYCRR 500.1(k), workforce data | Encrypted at rest and in transit over external networks; need-to-know access; approved AI tools only |
| Internal | Policies, procedures, internal communications | Company systems only |
| Public | Published material | No restriction |

4.1 All data must be classified as Restricted, Confidential, Internal, or Public, and each data set must have a named owner. (RA-2; ID.AM-07)
4.2 Restricted and Confidential data must be encrypted at rest and in transit over external networks, and stored PAN must be rendered unreadable by tokenization or strong cryptography. (SC-28; SC-8; PR.DS-01; PR.DS-02)
4.3 Sensitive authentication data must never be stored after authorization, including in call recordings, tickets, email, or chat. (SI-12; PR.DS-01)
4.4 PAN may be stored only in approved CDE stores. Automated PAN discovery must scan all data stores and recordings at least monthly, and any PAN found elsewhere must be handled under PRC-04.2. (CM-12(1); SI-12; PR.DS-01)
4.5 Data must be kept only as long as STD-04.4 allows: PAN in the settlement archive for 18 months; customer information disposed of no later than two years after last use unless a business or legal need applies; disposal must make data unreadable (NIST SP 800-88). (SI-12; MP-6; PR.DS-01)
4.6 Cryptographic keys must be generated and stored in HSMs or the key management service, managed under dual control and split knowledge, and described in the documented cryptographic architecture. (SC-12; SC-13; PR.DS-01)
4.7 Extracts from the CDE to analytics or AI platforms must be registered (PRC-04.1) and tokenized; ingestion must block PAN patterns. (AC-4; SI-12; PR.DS-01)
4.8 Restricted data must not be entered into AI tools; Confidential data only into tools on the approved list (STD-05.3) with no-training and deletion terms, and training data must be minimized. (AC-20; SA-9; PR.DS-01)
4.9 Backups of tier-1 data must be encrypted, immutable, and restore-tested. (CP-9; PR.DS-11)
4.10 Funding and clearing files must carry control totals and hashes that are verified before transmission, and transmission must halt on a mismatch. (SI-7; SI-7(5); PR.DS-02)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-04.1 Encryption and Key Management Standard
- STD-04.2 Media Protection and Disposal Standard
- STD-04.3 Backup Standard
- STD-04.4 Data Retention Standard
- PRC-04.1 Data Extract Registration Procedure
- PRC-04.2 PAN Discovery and Unexpected PAN Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the PCI DSS quarterly reviews (PCI DSS 12.4.2), access certifications, and the annual Internal Audit assessment (P07). Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 Core Payment Processing Platform SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
