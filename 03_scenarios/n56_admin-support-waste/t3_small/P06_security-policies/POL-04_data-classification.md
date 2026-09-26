# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | HR and Compliance Manager |
| Approved by | COO |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-1, MP-6, SC-8, SC-28, SI-12, SI-12(1), CP-9, CM-12 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| Legal drivers | 8 CFR 274a.2(b)(2)-(4), (e), (g); Fla. Stat. 448.095(2)(d); 16 CFR 682.3; Fla. Stat. 501.171(2), (8) |

## 1. Purpose
Classify firm information by sensitivity and legal duty, and set handling, retention, and disposal rules so protection matches the harm a disclosure would cause.

## 2. Scope
All workforce members and all firm information in any form, including information held by vendors.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| HR and Compliance Manager | Owns classification and the retention schedule; approves new uses of Restricted data |
| IT Manager | Implements encryption, backup, logging, and disposal controls; keeps the data inventory |
| All workforce | Handle information according to this policy |

## 4. Policy statements
4.1 Information must be classified in one of four levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | SSNs, Form I-9 records and document images, E-Verify results, consumer reports, bank account numbers, clock-in geolocation, credentials | Encrypted at rest and in transit; access per POL-02 4.2; approved systems only; access logged |
| **Confidential** | Pay rates, client contracts and bill rates, resumes, security documents | Encrypted in transit; need-to-know |
| **Internal** | Job orders, schedules, procedures | Workforce only |
| **Public** | Job postings, website | No restriction |

(RA-2; ID.AM-07)
4.2 Restricted data must be encrypted at rest and in transit. (SC-28; SC-8; PR.DS-01; PR.DS-02)
4.3 Restricted data may be stored only in approved systems: the ATS (including the I-9 module), the payroll platform, the timekeeping app, the screening provider portal, the document archive, and the backup vault. It must never be kept in email, chat, personal devices, or personal cloud accounts. I-9 documents are collected through the ATS upload link only; copies received by email must be uploaded and the email deleted. (AC-3; 8 CFR 274a.2(b)(3))
4.4 **Minimization.** Reporting copies and exports may not contain full SSNs or bank account numbers; use the last 4 digits. (SI-12(1))
4.5 The IT Manager must keep an inventory of where Restricted data is stored and which vendors receive it. (ID.AM-07; CM-12)
4.6 **Retention schedule.**

| Record | Keep | Then |
|---|---|---|
| Form I-9, attached document copies, and E-Verify case results | 3 years after hire or 1 year after employment ends, whichever is later (8 CFR 274a.2(b)(2)(i)(A)); never less than 3 years for E-Verify documentation (Fla. Stat. 448.095(2)(d)) | Purge quarterly |
| Consumer reports and FCRA notices | 2 years after the hiring decision (firm choice; counsel to confirm against claims periods) | Purge quarterly |
| Candidate records (not hired) | 2 years after last activity (firm choice) | Purge quarterly |
| Clock-in geolocation | 13 months (firm choice) | Purge by vendor setting |
| Payroll and tax records | Per the Controller's tax schedule | Purge per schedule |

A legal hold stops any purge. (SI-12; ID.AM-08)
4.7 **Disposal.** Paper with Restricted data goes in locked shred bins; the shredding vendor must provide certificates. Devices and media are wiped to a documented standard (for reuse) or destroyed by a certified vendor with a certificate (for disposal), including kiosks and scanners. (MP-6; 16 CFR 682.3(b)(1)-(3); Fla. Stat. 501.171(8))
4.8 Backups of Restricted data must be encrypted, stored apart from production (a separate account), protected from alteration, and restore-tested quarterly, including the I-9 archive. (CP-9; PR.DS-11; 8 CFR 274a.2(g)(1)(ii))
4.9 Restricted data must not be entered into AI tools unless the tool is on the approved list (see P10 and POL-05). (SA-9)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.7). Compliance is checked through the annual control assessment (P07) and the quarterly purge and I-9 quality check.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the policy owner (or by the President for High risk), and expire within 12 months.

## 7. Related documents
POL-01; POL-02; POL-05; electronic Form I-9 procedure (due 2026-12-31); P10 AI approved-tools list
