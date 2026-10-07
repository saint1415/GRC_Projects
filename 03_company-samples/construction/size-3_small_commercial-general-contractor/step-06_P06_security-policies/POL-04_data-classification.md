# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Contracts Administrator |
| Approved by | CFO |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-20, MP-1, MP-3, MP-6, SC-8, SC-28, SI-12, CP-9, SA-9 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| Federal contract requirements | FAR 52.204-21(b)(1)(iii), (vii), (b)(2) (N23-R01); DFARS 252.204-7021(d)(2) (N23-R04) |

## 1. Purpose
Classify company information by sensitivity and set handling rules, so that Federal Contract Information stays inside the systems that are assessed for it and sensitive data gets protection that matches the harm a disclosure would cause.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, temporary staff, and interns) at the main office, the equipment yard, and every jobsite. Covers all company systems and data, including systems that vendors operate for the company, and company-issued devices wherever they are used.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Contracts Administrator | Owns classification; identifies FCI and checks incoming documents for CUI markings |
| IT Manager | Implements encryption, backup, and disposal controls; keeps the approved external systems list |
| Systems Integration Manager | Custodian of client facility security details |
| All workforce | Handle information according to this policy |

## 4. Policy statements
4.1 Information must be classified in one of five levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Client facility security details (camera layouts, access control and building automation credentials); bank details for vendors, owners, and employees; Social Security numbers and payroll; passwords | Approved system only (password vault, ERP, payroll system); encrypted; named need-to-know |
| **Federal (FCI)** | Drawings, submittals, schedules, daily logs, pay apps, and certified payrolls for federal contracts | Only inside the Project Delivery and Payment Platform; never in personal accounts or unapproved tools |
| **Confidential** | Bid and pricing data; private owners' drawings; contracts | Need-to-know; never shared with competitors |
| **Internal** | Procedures, schedules, safety plans | Workforce and project team only |
| **Public** | Approved website content, marketing | No restriction |

(RA-2; ID.AM-07)
4.2 **Controlled unclassified information (CUI) is not accepted** until the President approves a CUI program. Anyone who receives a document marked CUI must stop, must not forward it, and must notify the Contracts Administrator. The Contracts Administrator must quarantine it and contact the Contracting Officer. (MP-3; FAR 52.204-21(b)(2))
4.3 FCI may be processed, stored, or transmitted only on systems inside the assessed boundary (P02 section 7). Personal email, personal cloud storage, and personal devices are prohibited for FCI. Automatic forwarding of company email to external addresses is blocked. (AC-20; FAR 52.204-21(b)(1)(iii); DFARS 252.204-7021(d)(2))
4.4 Restricted and FCI data must be encrypted at rest on every device, including tablets and commissioning laptops, and encrypted in transit. Drawings and models must be exchanged through the project management platform or the file-transfer portal, not email attachments. (SC-28; SC-8; PR.DS-01; PR.DS-02)
4.5 Media and devices that held FCI or Restricted data must be sanitized before disposal, return to a lessor, or reuse. Wiping is required for reuse; disposal requires a certified vendor that provides a certificate of destruction. Every sanitization must be recorded. (MP-6; ID.AM-08; FAR 52.204-21(b)(1)(vii))
4.6 Backups must be encrypted, stored apart from production (a separate account and region), protected from alteration, and restore-tested quarterly. (CP-9; PR.DS-11)
4.7 FCI, Restricted, and Confidential data must not be entered into any AI tool or other external service unless it is on the approved external systems list under terms that bar training on company data (see P10 and POL-01 4.8). (AC-20; SA-9)
4.8 Client facility security details must be kept in the password vault under the client's project. They must be handed to the client at the end of warranty and then deleted from company systems. (AC-3)
4.9 Records must be retained under the retention schedule, including 6 years for CMMC evidence and security records and 3 years after completion for certified payroll records (POL-01 4.12). (SI-12)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.14. Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07), the CMMC self-assessment, and the access reviews in this policy set.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the policy owner (or by the President for High risk), and expire within 12 months.

## 7. Related documents
POL-01; POL-05; P02 boundary (section 7); P10 approved AI tools; records retention schedule
