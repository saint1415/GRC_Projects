# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Chief Privacy Officer |
| Approved by | Executive risk committee |
| Approval date | 2026-08-24 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | AC-1, AU-1, CM-1, MP-1, RA-1, SA-1, SC-1, SI-1, RA-2, SC-8, SC-28, SC-13, AC-6, AC-3, AC-21, MP-6, MP-4, AU-10, SI-7, SI-10, CM-3, SA-9, AC-20, SI-12, CM-12 |
| CSF 2.0 | ID.AM-05, ID.RA-04, PR.DS-02, PR.DS-01, PR.AA-05, PR.DS-10, ID.RA-09, GV.OC-05, GV.SC-04, ID.AM-02, ID.AM-07, ID.AM-08 |
| HIPAA Security Rule and other drivers | 164.306(d)(3); 164.308(a)(1)(ii)(A); 164.308(b)(1); 164.310(d)(2)(i); 164.312(a)(2)(iv); 164.312(c)(1); 164.312(e)(2)(ii); 164.316(b)(2)(i); 164.502(b); see `policy-control-map.csv` for each statement's driver |

## 1. Purpose
Classify the system's information and set handling rules so that patient information, including Part 2 records and paper downtime records, is protected, kept accurate, and kept only as long as needed.

## 2. Scope
All Cris Santos Company workforce members (employees, medical staff, agency and contracted staff, students, and volunteers) at the 8 hospitals, 3 freestanding emergency departments, 46 clinics, 4 imaging centers, the data centers, and corporate offices in Florida, Georgia, and Alabama, including H-08 and any future acquisition from its closing date. Covers all systems and data, including the data centers, both clouds, SaaS, medical devices, building OT, systems that vendors operate for the system, and the services sold to other organizations (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Privacy Officer | Owns the classification scheme; approves identified-data use |
| Data owners (vice presidents) | Classify data in their systems |
| Director of Health Information Management | Medical record retention and downtime record back-entry |
| Vice President, Behavioral Health | Part 2 program records at H-03 |
| Chief Data and Analytics Officer | Analytics platform data sets |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategories. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 All information must be classified as Restricted (PHI, Part 2 records, Social Security numbers, payment card data, credentials), Confidential, Internal, or Public, and labeled where the system supports it. (RA-2; ID.AM-05; ID.RA-04)
4.2 Restricted data must be encrypted at rest and in transit. Any exception must document why encryption is not reasonable and appropriate and what equivalent measure is used. (SC-8; SC-28; SC-13; PR.DS-02; PR.DS-01)
4.3 Use and disclosure of PHI must be limited to the minimum necessary; identified data may be used in the analytics platform only with data governance approval. (AC-6; PR.AA-05)
4.4 Part 2 records must be flagged at registration and disclosed only with written consent or under a Part 2 exception, with the required notice. (AC-3; AC-21; PR.AA-05; PR.DS-10)
4.5 Media and equipment holding Restricted data must be sanitized under NIST SP 800-88 before reuse or disposal, with certificates kept. (MP-6; )
4.6 Printed downtime reports and paper records must be kept in staff-only areas, shredded when superseded, and back-entered into the EHR within 24 hours of recovery with the author's authentication. (MP-4; AU-10; )
4.7 Clinical results and orders must be reconciled across interfaces, and changes to clinical content must go only through change control. (SI-7; SI-10; CM-3; ID.RA-09; PR.DS-01; PR.DS-10)
4.8 Restricted data must not be entered into AI tools unless the AI governance committee has approved the use and a BAA with no-training terms is in place. (SA-9; AC-20; GV.OC-05; GV.SC-04; ID.AM-02)
4.9 Medical records must be retained for at least 5 years, or longer where state law requires; security documentation for at least 6 years. (SI-12; ID.AM-07; ID.AM-08)
4.10 Every recurring extract of Restricted data must be registered with its purpose, recipient, and retention. (CM-12; ID.AM-07)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-04.1 Encryption Standard
- STD-04.2 Media Protection and Disposal Standard
- STD-04.3 Backup Standard
- STD-04.4 Clinical Data Integrity Standard
- STD-04.5 Part 2 Records Standard
- PRC-04.1 Data Extract Registration Procedure
- PRC-04.2 Downtime Record Back-Entry Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), access certifications, and the emergency preparedness program's exercises. Violations are handled under the HIPAA sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment, contract, or privileges, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 ECIS SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance; the unified emergency preparedness plan.
