# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (with Cris Santos Bank, N.A. and Cris Santos Investment Services, LLC) |
| Policy ID | POL-04 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Chief Privacy Officer |
| Approved by | Executive risk committee |
| Approval date | 2026-09-18 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | RA-2, SC-8, SC-28, SI-7, AU-10, AC-3, AC-6, MP-6, CP-9, SI-12, SA-9 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-11 |
| Regulatory basis | 12 CFR 30 App. B II.B, III.C.1.c, III.C.4; 12 CFR 21.11(k); 17 CFR 248.30(b) |

## 1. Purpose
Classify the group's information and set how each class is protected, used, kept, and destroyed, with special care for customer information, account integrity, and SAR information.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary staff) of the parent, Cris Santos Bank, N.A., and Cris Santos Investment Services, LLC, at all sites in the six footprint states and remote locations, including the acquired bank's staff and systems from the merger date. Covers all systems and data, including the data centers, both clouds, SaaS, branches, ATMs, and systems that third parties operate for the group, and the services the group offers to institutional clients (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Privacy Officer | Owns classification and handling rules |
| Data owners | Approve access to Restricted data sets |
| Chief Data and Analytics Officer | Masking and minimization on the data platform |
| Director of Data Center and Mainframe Operations | Backups and media handling in the data centers |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Information must be classified as Restricted (customer NPI, account numbers with access codes, credentials, Social Security numbers, card data, consumer reports, SAR information), Confidential (material nonpublic information, security information), Internal, or Public, and labeled where systems allow. (RA-2; ID.AM-07)
4.2 Restricted data must be encrypted at rest and in transit under STD-04.1. (SC-28; SC-8; PR.DS-01)
4.3 Every change to a balance, posting, beneficiary, or payment instruction must be attributable to a person, a customer session, or an approved automated process, and balances must be reconciled daily between the core, the payments hub, and the card processor. (SI-7; AU-10; PR.DS-01)
4.4 SAR information must be accessible only to the financial crimes team and must never be disclosed except as 12 CFR 21.11(k) allows. (AC-3; PR.DS-01)
4.5 Restricted data on the enterprise data platform must be masked by default; raw access needs data owner approval and quarterly certification. (AC-6; PR.DS-01)
4.6 Media holding Restricted or Confidential data must be sanitized before reuse and destroyed by a certified vendor with a serial-number certificate before disposal. (MP-6; PR.DS-01)
4.7 Backups of Restricted data must be encrypted, immutable, and held in a separate account or location; tier-1 restores must be tested at least quarterly; core banking data must have a logically isolated immutable copy. (CP-9; PR.DS-11)
4.8 Restricted data must not be entered into any AI tool unless the AI governance committee has approved the use case and the contract bars training on or secondary use of the data. (SA-9; PL-4; GV.SC-05)
4.9 Records must be kept per the records schedule, including 5 years for SAR supporting documents and 7 years for security documentation. (SI-12; PR.DS-11)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-04.1 Encryption Standard
- STD-04.2 Media Protection and Disposal Standard
- STD-04.3 Backup Standard
- STD-04.4 Payment and Ledger Integrity Standard
- PRC-04.1 Data Extract Registration Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, second-line reviews by independent risk management, the annual Internal Audit assessment (P07), and quarterly access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 CBDC SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
