# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Owner | Director of Compliance and Privacy |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-22 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-6, SC-8, SC-28, SI-12, SI-12(1), CP-9, CM-12, PT-5, AC-3 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| Legal drivers | 8 CFR 274a.2(b)(2)-(4), (e), (g); Fla. Stat. 448.095(2)(d); 16 CFR 682.3; 29 CFR 1630.14(b)(1), (c)(1); Fla. Stat. 501.171(1)(g), (2), (8); 501.702(4); 400.980(5); 934.03(2)(d) |
| Supporting standards | STD-04 Records retention and disposal; STD-08 Encryption and key management |

## 1. Purpose
Classify firm information by sensitivity and legal duty, and set handling, retention, and disposal rules so protection matches the harm a disclosure would cause.

## 2. Scope
All workforce members and all firm information in any form, including information held by vendors and call recordings.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Compliance and Privacy | Owns classification, the retention schedule, and the data inventory; approves new uses of Restricted data |
| Credentialing Manager | Applies the medical information rules to credential files |
| IT Director | Implements encryption, backup, and disposal controls |
| Security Manager | Monitors Restricted data locations and access |
| All workforce | Handle information according to this policy |

## 4. Policy statements
4.1 Information must be classified in one of four levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | SSNs; Form I-9 records and document images; E-Verify results; consumer reports and drug test results; clinician medical information; finger templates; bank account numbers; clock-in geolocation; call recordings that contain SSNs; credentials and API keys | Encrypted at rest and in transit; access per POL-02 4.2; approved systems only; access logged |
| **Confidential** | Pay and bill rates; client and MSP contracts; supplier rates; resumes; security documents | Encrypted in transit; need-to-know |
| **Internal** | Job orders, schedules, procedures | Workforce only |
| **Public** | Job postings, website | No restriction |

(RA-2; ID.AM-07)
4.2 Restricted data must be encrypted at rest and in transit. (SC-28; SC-8; PR.DS-01; PR.DS-02)
4.3 Restricted data may be stored only in approved systems: the ATS (including the I-9 module), the payroll platform, the timekeeping platform, the credentialing platform, the screening provider portal, the document archive, and the backup account. It must never be kept in email, chat, file shares, personal devices, or personal cloud accounts. I-9 documents are collected through the ATS upload link only; copies received by email must be uploaded and the email deleted. Credential files go to clients only through the client compliance portal. (AC-3; 8 CFR 274a.2(b)(3))
4.4 **Minimization.** Reports, exports, and the data warehouse may not contain full SSNs or bank account numbers; use the last 4 digits. SSNs are taken by keypad in the IVR, not spoken on recorded calls. (SI-12(1))
4.5 The Director of Compliance and Privacy keeps an inventory of where Restricted data is stored and which vendors receive it, reviewed quarterly. (CM-12; ID.AM-07)
4.6 **Retention schedule (STD-04).**

| Record | Keep | Then |
|---|---|---|
| Form I-9, attached document copies, and E-Verify case results | 3 years after hire or 1 year after employment ends, whichever is later (8 CFR 274a.2(b)(2)(i)(A)); never less than 3 years for E-Verify documentation (Fla. Stat. 448.095(2)(d)) | Purge quarterly |
| Consumer reports, drug test results, and FCRA notices | 2 years after the hiring decision (firm choice; counsel to confirm against claims periods) | Purge quarterly |
| Clinician credential and screening documentation | While the clinician is active and 3 years after the last assignment (firm choice, supports 400.980(5) inquiries); medical documents in the separate medical category | Purge quarterly |
| Candidate records (not hired) | 2 years after last activity (firm choice) | Purge quarterly |
| Finger templates | Deleted within 30 days after the associate's last assignment at an on-site program (firm choice) | Vendor deletion report monthly |
| Clock-in geolocation | 13 months (firm choice) | Vendor setting |
| Call recordings | 18 months (firm choice) | Platform setting |
| Payroll and tax records | Per the Controller's tax schedule | Purge per schedule |

A legal hold stops any purge. Purges of records past retention begin 2027-01-31. (SI-12; ID.AM-08)
4.7 **Disposal.** Paper with Restricted data goes in locked shred bins; the shredding vendor must provide certificates. Devices and media, including kiosks, clocks, and multifunction devices, are wiped to a documented standard for reuse or destroyed by a certified vendor with a certificate for disposal. (MP-6; 16 CFR 682.3(b)(1)-(3); Fla. Stat. 501.171(8))
4.8 Backups of Restricted data, including the document archive, must be encrypted, stored in the separate backup account, protected by write-once retention, and restore-tested quarterly. (CP-9; PR.DS-11; 8 CFR 274a.2(g)(1)(ii))
4.9 **Medical information** about applicants and employees (including clinicians' immunizations, TB tests, physicals, fit tests, and medical notes) must be kept on separate forms and in a separate medical file category, treated as confidential, and disclosed only as 29 CFR 1630.14 allows or with the individual's written authorization scoped to what the client needs. (AC-3; 29 CFR 1630.14(b)(1), (c)(1))
4.10 **Biometric data.** No associate may be enrolled on a fingerprint clock without written notice of what is collected, why, how long it is kept, and who holds it, and the associate's written consent. An alternative clock-in method must be offered to anyone who declines. (PT-5; Fla. Stat. 501.171(1)(g)1.a.(VI); 501.702(4))
4.11 Restricted data must not be entered into AI tools unless the tool is on the approved list for that data (P10; POL-05 4.10). (SA-9)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 4.8). Compliance is checked through the annual control assessment (P07), the quarterly purge and I-9 quality checks, and the data inventory review.

## 6. Exceptions
Exceptions follow POL-01 4.7. They must be written, risk-rated, approved at the risk acceptance level in POL-01 4.4, and expire within 12 months.

## 7. Related documents
POL-01; POL-02; POL-05; STD-04; STD-08; electronic Form I-9 procedure (due 2026-12-31); P10 approved AI tools list
