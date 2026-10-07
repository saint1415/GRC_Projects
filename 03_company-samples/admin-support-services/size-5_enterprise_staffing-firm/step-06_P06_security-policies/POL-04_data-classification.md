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
| Implements (SP 800-53 Rev. 5) | RA-2, SC-28, SC-8, AC-4, SI-12, MP-6, AU-12, AC-3, CP-9, SI-7, SI-10, AC-20 |
| CSF 2.0 | ID.AM-05, PR.DS-01, ID.AM-07, ID.AM-08, PR.PS-04, PR.DS-11, PR.DS-02, PR.DS-10 |
| Binding rules served | Fla. Stat. 501.171(2); N56-R03 (8 CFR 274a.2(b)(2)(i)(A)); N56-R01 (16 CFR 682.3); N56-R01 (16 CFR 682.3(b)); Fla. Stat. 501.171(8); FAR 52.204-21(b)(1)(vii); N56-R03 (8 CFR 274a.2(b)(4); (g)(1)(iv)); N56-R03 (8 CFR 274a.2(g)(1)(ii)); N56-R07 (48 CFR 52.204-21(b)(1)(iii)) |

## 1. Purpose
Classify the firm's information by harm if disclosed or altered, and set handling, retention, and disposal rules, so that the most sensitive records (SSNs, bank accounts, Form I-9 documents, E-Verify data, consumer reports) are protected wherever they are copied and destroyed when they are no longer needed.

## 2. Scope
All Cris Santos Company internal employees, contractors, and temporary associates while they use company systems (the associate app, time clocks, kiosks), at all of its about 520 sites in 38 states and the District of Columbia, including acquired firms from their acquisition date. Covers all systems and data, including cloud, colocation, SaaS, and systems that vendors operate for the firm, and the services the firm offers to clients (SL-1 Workforce Management Platform and SL-2 payrolling).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Privacy Officer | Policy owner; data inventory; extract registration |
| Vice President, Employment Compliance | Form I-9, E-Verify, and consumer report retention and disposal (PRC-09.1 to PRC-09.4) |
| Chief Data Officer | Enterprise data platform; tokenization and masking of Restricted data |
| Data owners (system owners) | Classify data and approve access |
| Treasurer | Integrity of pay files |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Information must be classified as Restricted (SSNs, bank accounts, Form I-9 documents, E-Verify data, consumer reports, clinician health records), Confidential, Internal, or Public, and labeled in the data inventory. (RA-2; ID.AM-05)
4.2 Restricted data must be encrypted at rest and in transit; outside the payroll engine, SSNs and bank account numbers must be tokenized or masked, and clear-text Restricted data must not be available for analytics. (SC-28; SC-8; PR.DS-01)
4.3 Every recurring extract of Restricted data must be registered (PRC-04.1) with its purpose, owner, recipients, and retention, and approved by the Chief Privacy Officer. (AC-4; ID.AM-07)
4.4 Records must be kept and then destroyed under the retention schedule in STD-04.2; each Form I-9 must be kept until 3 years after hire or 1 year after employment ends, whichever is later, and destroyed within 90 days after that date unless a legal hold applies. (SI-12; ID.AM-08)
4.5 Paper must be shredded and media destroyed or wiped by a certified vendor with certificates of destruction; electronic records past retention must be purged. (MP-6; ID.AM-08)
4.6 Form I-9 information must be used only for employment eligibility purposes, and every creation, change, or access of an electronic Form I-9 record must leave a permanent audit trail. (AU-12; AC-3; PR.PS-04)
4.7 Backups of tier-1 data, including Form I-9 records, must be immutable, kept in a separate account, and restore-tested monthly. (CP-9; PR.DS-11)
4.8 Bank, paycard, and tax files must be hashed when generated and verified before transmission; a mismatch must stop the file. (SI-7; PR.DS-02)
4.9 Client data received for SL-1 and SL-2 must be used only for that client's service and validated on intake. (SI-10; AC-3; PR.DS-10)
4.10 Federal contract information must be handled only in approved systems and must not be received or sent through personal or non-company email. (AC-20; PR.DS-01)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-04.1 Encryption and Tokenization Standard
- STD-04.2 Records Retention and Disposal Standard (retention schedule)
- STD-04.3 Media Protection Standard
- STD-04.4 Backup Standard
- PRC-04.1 Data Extract Registration Procedure
- PRC-09.1 Associate Onboarding and Form I-9 Procedure
- PRC-09.2 Form I-9 Correction and Reverification Procedure
- PRC-09.3 E-Verify Case and Outage Procedure
- PRC-09.4 Form I-9 Retention and Purge Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), quarterly access certifications, and the fraud and KRI dashboards. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 ALPP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
