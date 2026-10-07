# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | IT Manager (Configuration Lab Lead is the CUI custodian) |
| Approved by | Chief Operating Officer |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-4, MP-2, MP-3, MP-4, MP-6, MP-7, PE-17, SC-8, SC-13, SC-28, CP-9, SI-12, SA-9 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11, ID.AM-08 |
| Contract and regulatory basis | DFARS 252.204-7012(b); 32 CFR 2002.14(g); FAR 52.204-21; SP 800-171 3.1.3, 3.8.1 to 3.8.9, 3.10.6, 3.13.11, 3.13.16 |

## 1. Purpose
Classify company information by sensitivity and set handling rules so that protection matches the harm a disclosure would cause, with specific rules for CUI and FCI.

## 2. Scope
All Cris Santos Company workforce members, the MSP, and all company information in any form (electronic, paper, removable media, configured devices), including information that customers, primes, and suppliers give the company.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Configuration Lab Lead | CUI custodian; checks markings; keeps CUI in the lab and CUI share |
| Government Contracts Manager | Identifies which contracts involve CUI or FCI; confirms markings with the prime when unclear |
| IT Manager | Implements encryption, backup, media, and disposal controls |
| All workforce | Label and handle information according to this policy |

## 4. Policy statements
4.1 Information must be classified in one of five levels:

| Level | Examples | Handling |
|---|---|---|
| **CUI** | Prime B network drawings, IP addressing plans, device configuration templates, and anything marked CUI | Only in the CUI share, on the 6 lab workstations, or on the prime's secure file share; FIPS-validated encryption; CUI access list only |
| **FCI** | DoD purchase orders, ship-to data, kitting and labeling instructions | Approved systems only (ERP, WMS, EDI, label service); FAR 52.204-21 safeguards |
| **Confidential** | Customer pricing, supplier bank details, employee personal information, security documents | Encrypted in transit; need-to-know |
| **Internal** | Procedures, schedules, catalogs before release | Workforce only |
| **Public** | Website, published catalog | No restriction |

(RA-2; ID.AM-07)
4.2 **Where CUI may live.** CUI must never be stored in or sent through the ERP, the WMS, email, chat, the productivity suite's file storage, personal devices, or AI tools. DoD order types in the ERP must not carry attachments. (AC-4; SP 800-171 3.1.3; DFARS 252.204-7012(b)(2)(ii)(D))
4.3 CUI must carry its CUI marking. Printouts and media derived from CUI must be marked, kept in the locked cabinet in the lab cage, and printed only on the lab printer. (MP-3; MP-4; MP-2; SP 800-171 3.8.1, 3.8.2, 3.8.4)
4.4 CUI must be protected by FIPS-validated cryptography at rest and in transit. (SC-13; SC-28; SC-8; SP 800-171 3.13.11, 3.13.16)
4.5 USB storage is blocked on all endpoints. Lab technicians may use only company-issued, labeled, encrypted drives, recorded against their names. (MP-7; SP 800-171 3.8.7, 3.8.8)
4.6 CUI may not be worked on at home or any alternate site. Laptops used for CUI stay in the lab. (PE-17; SP 800-171 3.10.6)
4.7 **FCI with vendors.** A vendor may receive FCI only if its contract requires the FAR 52.204-21 safeguards. DoD orders must be excluded from data feeds to vendors that lack those terms, including the forecasting add-on. (SA-9; FAR 52.204-21)
4.8 Media and devices holding CUI, FCI, or Confidential data must be wiped (for reuse) or destroyed by a certified vendor that provides a certificate of destruction (for disposal). Configured DoD devices returned by customers are wiped before restocking or disposal. (MP-6; ID.AM-08; SP 800-171 3.8.3)
4.9 Backups of CUI and business data must be encrypted, stored apart from production (a separate account), protected from alteration, and restore-tested quarterly. (CP-9; PR.DS-11; SP 800-171 3.8.9)
4.10 CUI, FCI, and Confidential data must not be entered into AI tools unless the tool is on the approved list for that level (P10 and POL-05). No AI tool is approved for CUI. (SA-9)
4.11 Records are kept according to the records retention schedule. Security documentation is kept for 6 years (POL-01 4.15). (SI-12)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.7). Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07) and quarterly CUI location checks by the Configuration Lab Lead.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the policy owner (or by the Chief Executive Officer for High risk), and expire within 12 months. No exception may allow CUI outside the locations in 4.1.

## 7. Related documents
POL-01; POL-02; POL-05; CUI handling procedure for the lab (due 2026-11-30); P10 approved AI tools list; records retention schedule
