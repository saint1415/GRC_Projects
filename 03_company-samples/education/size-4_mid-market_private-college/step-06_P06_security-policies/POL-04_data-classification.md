# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Owner | Chief Compliance Officer |
| Approved by | Chief Information Officer |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2023 policy) |
| Review cycle | Annually (next review 2027-09-30), and after material changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-1, MP-6, SC-8, SC-12, SC-28, CP-9, CM-8, SI-12, SA-9, PT-3, AC-21 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| Safeguards Rule and other rules | 16 CFR 314.4(c)(2), (c)(3), (c)(6); 34 CFR 99.30, 99.32, 99.33; 34 CFR 668.24(e); HEA section 483 |
| Supporting standards | STD-08 Encryption and key management standard; STD-07 Contingency and recovery standard; STD-11 Data retention and disposal standard |

## 1. Purpose
Classify college information by sensitivity and set handling rules, so protection matches the harm a disclosure, misuse, or loss would cause.

## 2. Scope
All information the college creates, receives, maintains, or transmits, in any form, at every campus and in every system, including data held by vendors, the third-party servicer, and employer partner systems.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Compliance Officer | Owns classification; approves new uses and new locations of Restricted data |
| Data owners (Registrar, Director of Financial Aid, Bursar, Director of Institutional Research) | Classify their data; approve access and sharing; confirm permitted uses |
| Chief Information Officer | Implements encryption, backup, and disposal controls; keeps the Restricted data inventory |
| All employees | Label and handle information according to this policy |

## 4. Policy statements
4.1 Information must be classified in one of four levels. (RA-2; ID.AM-07)

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Customer information (aid records, ISIRs, tax and verification documents, SSNs, bank details, payment plan data); education records (grades, transcripts, disciplinary and accommodation records); counseling treatment records; credentials | Encrypted at rest and in transit; need-to-know or legitimate educational interest; approved systems only |
| **Confidential** | Employee HR and payroll data, contracts, security documents, board materials, employer partner agreements | Encrypted in transit; need-to-know |
| **Internal** | Course materials, schedules, procedures, internal announcements | Employees and enrolled students |
| **Public** | Website, catalog, directory information for students who have not opted out | No restriction |

4.2 Restricted data must be encrypted at rest on every device, service, and backup, and in transit over external networks. Email or file transfers containing customer information must use the enforced encryption option or the approved secure transfer service. Any exception requires compensating controls approved by the Qualified Individual. (SC-28; SC-8; PR.DS-01; PR.DS-02; 314.4(c)(3))
4.3 Encryption keys for cloud workloads and backups must be managed in the college's key management service, with separate keys for the backup account and annual rotation. (SC-12)
4.4 Restricted data may be stored only in approved systems: the SIS, LMS, FAMS, the SAIG workstations, the data warehouse (education records only), approved file shares, the backup account, and approved vendor systems under contract (POL-01 4.9). It must never be kept on personal devices, in personal cloud accounts, or in unapproved AI tools. (AC-3; SA-9)
4.5 **FAFSA and ISIR data** may be used only for aid administration (POL-01 4.12). They must not be copied into the data warehouse, marketing systems, or AI models. Reports that combine aid and academic data need the Director of Financial Aid's written confirmation that the use is permitted. (PT-3; HEA section 483)
4.6 Education records may be disclosed outside the college only with written student consent or under a FERPA exception, and the disclosure must be recorded under 34 CFR 99.32. Recipients must be told they may not redisclose. Data feeds to vendors are recorded in the integration register with their school-official basis. (AC-21; 34 CFR 99.30; 99.32; 99.33)
4.7 The Chief Information Officer must keep an inventory of where Restricted data is stored and which vendors receive it, reconciled quarterly against the SaaS register and card spend. (ID.AM-07; CM-8; 314.4(c)(2))
4.8 Media and devices holding Restricted data must be sanitized (for reuse) or destroyed by a certified vendor that provides a certificate (for disposal). **Leased copiers and multifunction printers must come back from the vendor with a certificate of sanitization.** (MP-6; ID.AM-08; 314.4(c)(6)(i))
4.9 Backups of Restricted data must be encrypted, stored in the separate backup account in a second region, protected by write-once retention, and restore-tested at least quarterly for each college-managed workload. (CP-9; PR.DS-11)
4.10 Restricted data must not be entered into AI tools unless the tool is approved under STD-05 and its contract prohibits training on college data and requires deletion at the end of the contract (P10). (SA-9)
4.11 Records are kept and disposed of under STD-11: Title IV records at least as long as 34 CFR 668.24(e) requires, and other customer information disposed of no later than 2 years after its last use unless a documented reason requires longer (314.4(c)(6)). (SI-12)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.8. Compliance is checked through the annual independent assessment (P07), quarterly inventory reconciliation, and the annual disposal report.

## 6. Exceptions
Exceptions follow POL-01 section 4.7.

## 7. Related documents
POL-01; POL-05; STD-05; STD-07; STD-08; STD-11; P04 cloud architecture; P10 approved-tools list; FERPA annual notice
