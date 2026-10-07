# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Bank, N.A. |
| Policy ID | POL-04 |
| Owner | Chief Compliance Officer (Privacy Officer) |
| Approved by | Board Risk Committee, 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-6, SC-8, SC-12, SC-28, SI-12, CP-9, CP-9(1), CM-8 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| Interagency Guidelines (12 CFR 30 App. B) | II.B.1; II.B.4; III.C.1.c; III.C.1.h; III.C.4 |
| Supporting standards | STD-06 Cryptography and key management; STD-08 Contingency and recovery |

## 1. Purpose
Classify bank information by sensitivity and set handling rules, so protection matches the harm a disclosure, alteration, or loss would cause. The rules put into practice the encryption, disposal, and backup measures of the Guidelines (III.C.1.c, III.C.1.h, III.C.4).

## 2. Scope
All workforce members; all information the bank creates, receives, or holds in any form, including information held for respondent institutions and information processed by service providers.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Compliance Officer | Owns classification; approves new uses of Restricted data |
| BSA/AML Officer | Controls access to SAR information |
| Information Security Officer | Keeps the inventory of where Restricted data is stored and which providers receive it |
| Chief Information Officer | Implements encryption, backup, and disposal controls |
| All workforce | Label and handle information according to this policy |

## 4. Policy statements
4.1 Information must be classified in one of four levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Customer nonpublic personal information, account and card numbers, Social Security numbers, online banking credentials, credit reports and loan files, SAR information, wire instructions, respondent institutions' customer payment data | Encrypted at rest and in transit; need-to-know; approved systems only |
| **Confidential** | Board materials, loan pipeline, security assessments, vendor contracts, model documentation | Encrypted in transit; need-to-know |
| **Internal** | Procedures, schedules, training | Workforce only |
| **Public** | Rates, website, branch brochures | No restriction |

(RA-2; ID.AM-07)
4.2 Restricted data must be encrypted at rest on every device and service, and in transit with TLS 1.2 or higher or IPsec (STD-06). Loan documents and statements containing Restricted data must be exchanged with customers through the secure document portal, not as ordinary email attachments (from 2027-06-30; until then, by encrypted email). (SC-28; SC-8; PR.DS-01; PR.DS-02; III.C.1.c)
4.3 The bank must use customer-managed keys for Restricted data in its cloud accounts, with backup keys separate from production keys. (SC-12; PR.DS-01)
4.4 Restricted data may be stored only in approved systems: the core, online banking, the payments hub and correspondent portal, the LOS, the AML monitoring system, the data warehouse (masked for non-analyst roles), the bank file shares, and the backup vault. It must never be kept on personal devices or in personal email or cloud accounts. Production Restricted data must not be copied to the non-production account.
4.5 SAR information, and any information that would reveal whether a SAR exists, is available only to the BSA staff and those they authorize, and must not be disclosed except as 12 CFR 21.11(k) permits.
4.6 The ISO must keep an inventory of where Restricted data is stored and which service providers receive it, reconciled each quarter. (ID.AM-07; CM-8)
4.7 Paper and media holding Restricted data must be shredded, wiped for reuse, or destroyed by a certified vendor that provides a certificate listing each drive's serial number, including drives from workstations, servers, and ATMs. (MP-6; ID.AM-08; II.B.4; III.C.4)
4.8 Backups of bank-managed Restricted data must be encrypted, stored in the separate backup account with write-once retention, and restore-tested: file-level monthly, and a full restore of each critical workload (payments database, item processing servers) at least twice a year. Recovery objectives come from the BIA (P05). (CP-9; CP-9(1); PR.DS-11; III.C.1.h)
4.9 Restricted data must not be entered into AI tools or other third-party services unless the tool is on the approved list and the provider is under a contract that meets POL-01 section 4.9 (STD-05; P10).
4.10 Records are kept according to the bank's records retention schedule. SAR copies and supporting documents are kept for five years from filing (12 CFR 21.11(g)). (SI-12)

## 5. Compliance and enforcement
Violations are handled under the sanctions procedure (POL-01 section 4.8). Compliance is checked through the annual independent assessment (P07) and the quarterly data inventory reconciliation.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. They must be written, risk-rated, approved at the level in POL-01 section 4.4, and expire within 12 months.

## 7. Related documents
POL-01; POL-05; STD-05; STD-06; STD-08; records retention schedule; data inventory; BIA (P05); P10 approved-tools list
