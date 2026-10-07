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
| Review cycle | Annually (next review by 2027-09-30), and after material changes, incidents, or new service lines |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-1, MP-6, SC-8, SC-28, AC-4, AC-21, PT-3, CM-8, SI-12, CP-9 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-11, GV.PO-01 |
| Key regulatory requirements | 16 CFR 314.4(c)(2), (c)(3), (c)(6); HEA section 483; 34 CFR 99.30, 99.32 |

## 1. Purpose
Classify the company's information by the harm its disclosure, alteration, or loss would cause, and set handling rules that match, including the purpose limits on FAFSA data and the disposal rules for customer information.

## 2. Scope
All Cris Santos Company workforce members (employees, including full-time and adjunct faculty, contractors, student workers, and volunteers) at headquarters, the 23 campuses, and the 4 student support centers, and all remote workers in any state. Covers all systems and data, including cloud, colocation, SaaS, and systems that vendors and the Title IV third-party servicer operate for the company, and the services the company offers to other organizations (SL-1 Workforce Education Services and SL-2 Online Program Services).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Privacy Officer | Owns classification and the data use register; approves new uses of Restricted data |
| University Registrar | Education records data owner; FERPA disclosures and records |
| Vice President, Financial Aid | Owner of FAFSA, ISIR, and federal tax information data |
| Data owners (system owners) | Classify their data; approve access |
| CISO | Encryption, backup, and disposal standards |
| All workforce | Handle information according to its class |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Information must be classified as Restricted (customer information such as SSNs, ISIR and other FAFSA-derived data, federal tax information, and refund bank details; education records; credentials; disability accommodation and health records), Confidential (financial, legal, security, material nonpublic information), Internal, or Public, and labeled where systems allow. (RA-2; ID.AM-07)
4.2 Restricted data must be encrypted at rest and in transit over external networks using STD-04.1. Any alternative requires compensating controls reviewed and approved by the Qualified Individual. (SC-28; SC-8; PR.DS-01; PR.DS-02)
4.3 FAFSA data and federal tax information, including ISIR-derived fields, must be used only for the application, award, and administration of student aid, and must not be copied to analytics, marketing, or AI systems. (PT-3; AC-4; PR.DS-01; GV.PO-01)
4.4 Data owners must keep a data map of where Restricted data is stored and processed, including vendors and analytics copies, and update it at least quarterly. (CM-8; ID.AM-07)
4.5 Any new use of student data for analytics or AI must be approved by the Chief Privacy Officer and recorded in the data use register before data is copied. (PT-3; GV.PO-01)
4.6 Customer information must be securely disposed of no later than 2 years after the last date it was used to provide a product or service to the student, unless it is needed for business operations or required by law (for example, Title IV record retention under 34 CFR 668.24(e)), through an annual disposal run under STD-04.4. (SI-12; MP-6; PR.DS-01)
4.7 Media holding Restricted or Confidential data must be sanitized before reuse and destroyed by a certified vendor with a certificate before disposal, so that personal information is unreadable. (MP-6; PR.DS-01)
4.8 Backups of Restricted data must be encrypted, immutable, stored in a separate account or location, and restore-tested at least quarterly for tier-1 systems. (CP-9; PR.DS-11)
4.9 The records retention schedule (STD-04.4) must be reviewed at least annually to minimize unnecessary retention. (SI-12; GV.PO-02)
4.10 Restricted data must not be entered into any AI tool unless the AI governance committee has approved the use case and the vendor contract prohibits training on company data. (SA-9; PL-4; GV.SC-05)
4.11 Personally identifiable information from education records must be disclosed only with written consent or under a FERPA exception, and each disclosure must be recorded in the SIS disclosure record. (AC-21; PT-4; GV.OC-03)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-04.1 Encryption Standard
- STD-04.2 Media Protection and Disposal Standard
- STD-04.3 Backup Standard
- STD-04.4 Records Retention Schedule
- STD-04.5 FAFSA and Federal Tax Information Use Standard
- PRC-04.1 Data Use Register Procedure
- PRC-04.2 FERPA Disclosure Recording Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), access certifications, and the Qualified Individual's annual report to the board. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 SRLP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
