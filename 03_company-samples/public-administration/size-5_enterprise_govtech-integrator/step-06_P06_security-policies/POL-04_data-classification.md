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
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, acquisitions, or new CJISSECPOL versions |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-3, MP-6, SA-3, SC-8, SC-13, SC-28, SI-12, CP-9, CM-12, AC-21 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| Key requirements | Pub. 1075 sec. 2.C.5, 2.E.6.4, 3.3.1, Exhibit 7 I(5); CJISSECPOL v6.1 SC-13, SC-28; 18 U.S.C. 2721; 42 CFR 431.305-431.306; 45 CFR 164.312 (AG-04) |

## 1. Purpose
Classify information by sensitivity and legal restriction, and set handling rules so protection matches the harm and the law.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and subcontractor staff) in every state and delivery center, including AQ-1 staff from the acquisition date. Covers all company systems, the hosted agency environments (ACMC, IES, legacy hosting, AQ-1), the CUI enclave, and all agency data the company receives, wherever it is stored or processed.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Privacy Officer | Owns classification; approves any new use or location of Regulated data |
| Director of Regulated Data Compliance | Keeps the data location inventory for FTI, CJI, ePHI, and DPPA data |
| System owners | Implement encryption, backup, retention, and deletion |
| Chief Technology Officer | Keeps production data out of non-production |
| All workforce | Handle information according to its level |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Information must be classified as Regulated (FTI, CJI, ePHI, DPPA highly restricted personal information, CUI), Restricted (other agency personal information such as benefits applicant data and Social Security numbers), Confidential, Internal, or Public, with the handling rules in STD-04.1 to STD-04.4. (RA-2; ID.AM-07)
4.2 Regulated data must be encrypted in transit and at rest with FIPS-validated modules (FIPS 140-3 certified modules for CJI in transit), with keys controlled by the company or the agency, and must stay in U.S. systems. (SC-8; SC-13; SC-28; PR.DS-01; PR.DS-02)
4.3 FTI may be stored only in the approved FTI tenants and their backups. It must never enter IES environments, support tickets, email, chat, or non-production. Commingled data must be treated and labeled as FTI. (CM-12; MP-3; AC-21; ID.AM-07)
4.4 Non-production environments must use synthetic or masked data. Real agency data outside production needs written agency approval and, for FTI, an IRS Data Testing Request obtained by the agency, before it is copied. (SA-3; PR.DS-01)
4.5 The Director of Regulated Data Compliance must keep an inventory of where Regulated and Restricted data are stored, including vendors, backups, and logs. (CM-12; ID.AM-07)
4.6 When a contract ends, the agency's data must be returned or deleted within the contract deadline and a deletion certificate issued; for FTI this is the Exhibit 7 purge certification. (MP-6; SI-12; ID.AM-08)
4.7 Backups of Regulated and Restricted data must be encrypted, immutable, stored in a separate account and a second U.S. location, and restore-tested quarterly. (CP-9; PR.DS-11)
4.8 Regulated or Restricted data may be sent to an AI service only if the AI governance committee approved the use case and the service has written no-training and retention terms and a confirmed FedRAMP scope. (SA-9; GV.SC-05)
4.9 DPPA personal information may be used or disclosed only for permitted uses recorded with a use code; exports over 500 records need written AG-05 approval. (AC-21; PR.DS-01)
4.10 Retention must follow each agency contract; security records are kept 7 years (POL-01 4.11). (SI-12; ID.AM-08)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-04.1 Encryption Standard
- STD-04.2 Media Protection and Disposal Standard
- STD-04.3 Backup Standard
- STD-04.4 Non-Production Data Standard
- PRC-04.1 Contract-End Data Return and Deletion Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), access certifications, and agency audits (CJIS audits, IRS safeguard reviews). Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. No exception may be granted against a CJIS Security Addendum, Pub. 1075 Exhibit 7, or business associate agreement term, or a statute.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 ACMC SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance; agency contracts; CJIS Security Policy v6.1; IRS Publication 1075.
