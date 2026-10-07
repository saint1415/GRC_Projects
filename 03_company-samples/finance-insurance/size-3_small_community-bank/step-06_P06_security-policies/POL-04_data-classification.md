# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Bank, N.A. |
| Policy ID | POL-04 |
| Owner | Compliance Officer (Privacy Officer) |
| Approved by | Audit and Risk Committee of the Board of Directors, 2026-08-27 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-1, MP-6, SC-8, SC-28, SI-12, CP-9, CM-8 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| Interagency Guidelines (12 CFR 30 App. B) | II.B.1; II.B.4; III.C.1.c; III.C.1.h; III.C.4 |

## 1. Purpose
Classify bank information by sensitivity and set handling rules, so protection matches the harm a disclosure or loss would cause. The rules put into practice the encryption, disposal, and backup measures of the Guidelines (III.C.1.c, III.C.1.h, III.C.4).

## 2. Scope
All Cris Santos Bank workforce members (directors, officers, employees, contractors, and temporary staff) at the six branches and the operations center. Covers all systems and data, including systems that service providers operate for the bank. It applies to customer information and all other bank information, in any form.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Compliance Officer | Owns classification; approves new uses of Restricted data |
| BSA/AML Officer | Controls access to SAR information |
| IT Manager (ISO) | Implements encryption, backup, and disposal controls; keeps the data inventory |
| All workforce | Label and handle information according to this policy |

## 4. Policy statements
4.1 Information must be classified in one of four levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Customer nonpublic personal information, account and card numbers, Social Security numbers, online banking credentials, credit reports and loan files, SAR information, wire instructions | Encrypted at rest and in transit; need-to-know; approved systems only |
| **Confidential** | Board materials, loan pipeline, security assessments, vendor contracts | Encrypted in transit; need-to-know |
| **Internal** | Procedures, schedules, training | Workforce only |
| **Public** | Rates, website, branch brochures | No restriction |

(RA-2; ID.AM-07)
4.2 Restricted data must be encrypted at rest on every device and service, and encrypted in transit. Loan documents and statements containing Restricted data must be exchanged with customers through the secure document portal, not as ordinary email attachments (from 2027-03-31; until then, by encrypted email). (SC-28; SC-8; PR.DS-01; PR.DS-02; III.C.1.c)
4.3 Restricted data may be stored only in approved systems: the core, online banking, the wire platform, the loan origination system, the reporting data warehouse, the bank file share, and the backup vault. It must never be kept on personal devices or in personal email or cloud accounts.
4.4 SAR information, and any information that would reveal whether a SAR exists, is available only to the BSA staff and those they authorize, and must not be disclosed except as 12 CFR 21.11(k) permits.
4.5 The ISO must keep an inventory of where Restricted data is stored and which service providers receive it. (ID.AM-07; CM-8)
4.6 Paper and media holding Restricted data must be shredded, wiped (for reuse), or destroyed by a certified vendor that provides a certificate listing each drive's serial number (for disposal), including drives from workstations and ATMs. (MP-6; ID.AM-08; II.B.4; III.C.4)
4.7 Backups of bank-managed Restricted data must be encrypted, stored in a separate account from production with immutable retention, and restore-tested quarterly. Recovery objectives come from the BIA (P05). (CP-9; PR.DS-11; III.C.1.h)
4.8 Restricted data must not be entered into AI tools or other third-party services unless the tool is on the approved list and the provider is under a contract that meets POL-01 section 4.8 (see P10 and POL-05).
4.9 Records are kept according to the bank's records retention schedule. SAR copies and supporting documents are kept for five years from filing (12 CFR 21.11(g)). (SI-12)

## 5. Compliance and enforcement
Violations are handled under the sanctions procedure (POL-01 section 4.7). Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07) and the annual independent IT audit.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved at the level in POL-01 section 4.4, and expire within 12 months.

## 7. Related documents
POL-01; POL-05; records retention schedule; data inventory; BIA (P05); P10 approved-tools list
