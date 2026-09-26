# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Owner | Compliance and Privacy Officer |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2023 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-1, MP-6, SC-8, SC-12, SC-28, CP-9, CM-8, SI-12, SA-9 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| HIPAA Security Rule | 164.310(d); 164.312(a)(2)(iv), (e); 164.308(a)(7)(ii)(A) |
| Supporting standards | STD-08 Encryption and key management standard; STD-07 Contingency and recovery standard; STD-04 Medical device security standard |

## 1. Purpose
Classify company information by sensitivity and set handling rules, so protection matches the harm a disclosure or loss would cause.

## 2. Scope
All information the company creates, receives, maintains, or transmits, in any form, at every site and in every system, including data held by vendors and data stored on medical devices and modalities.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Compliance and Privacy Officer | Owns classification; approves new uses and new locations of Restricted data |
| Data owners (business unit leaders) | Classify their data; approve access and sharing |
| IT Director | Implements encryption, backup, and disposal controls; keeps the Restricted data inventory |
| All workforce | Label and handle information according to this policy |

## 4. Policy statements
4.1 Information must be classified in one of four levels. (RA-2; ID.AM-07)

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | ePHI, images, patient financial and insurance data, Social Security numbers, credentials, visit audio | Encrypted at rest and in transit; minimum necessary; approved systems only |
| **Confidential** | Payroll, contracts, security documents, joint venture data, board materials | Encrypted in transit; need-to-know |
| **Internal** | Schedules, procedures, internal announcements | Workforce only |
| **Public** | Website, brochures | No restriction |

4.2 Restricted data must be encrypted at rest on every device, service, and backup, and in transit on every network. External email containing PHI must use the enforced encryption option. (SC-28; SC-8; PR.DS-01; PR.DS-02; 164.312(a)(2)(iv); 164.312(e)(2)(ii))
4.3 Encryption keys for cloud workloads and backups must be managed in the company's key management service, with separate keys for the backup account and annual rotation. (SC-12)
4.4 Restricted data may be stored only in approved systems: the EHR, PACS, the data warehouse, approved file shares, the backup account, and approved vendor systems under a BAA. It must never be kept on personal devices, in personal cloud accounts, or in unapproved AI tools. (AC-3; SA-9)
4.5 The IT Director must keep an inventory of where Restricted data is stored, including medical devices and modalities that store PHI, and which vendors receive it. The inventory must be reconciled quarterly. (ID.AM-07; CM-8; 164.310(d)(2)(iii))
4.6 Media and devices holding Restricted data must be sanitized (for reuse) or destroyed by a certified vendor that provides a certificate (for disposal). **Leased modalities, copiers, and devices returned to vendors must come back with a certificate of sanitization.** (MP-6; ID.AM-08; 164.310(d)(2)(i)-(ii))
4.7 Backups of Restricted data must be encrypted, stored in the separate backup account in a second region, protected by write-once retention, and restore-tested at least quarterly for each practice-managed workload. (CP-9; PR.DS-11; 164.308(a)(7)(ii)(A))
4.8 Restricted data must not be entered into AI tools unless the tool is approved under STD-05 and the vendor has a BAA that prohibits training on company data (P10). (SA-9)
4.9 Records are retained according to the medical records retention schedule. Security documentation is retained for 6 years (POL-01 4.12). (SI-12)

## 5. Compliance and enforcement
Violations are handled under the HIPAA sanctions procedure (POL-01 section 4.8). Compliance is checked through the annual independent assessment (P07) and quarterly inventory reconciliation.

## 6. Exceptions
Exceptions follow POL-01 section 4.7.

## 7. Related documents
POL-01; POL-05; STD-04; STD-05; STD-07; STD-08; P04 cloud architecture; P10 AI approved-tools list; medical records retention schedule
