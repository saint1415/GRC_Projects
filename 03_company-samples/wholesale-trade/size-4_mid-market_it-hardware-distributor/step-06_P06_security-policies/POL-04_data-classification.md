# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Owner | Security Manager |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and when a new prime program or data type is added |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-4, MP-2, MP-4, MP-6, MP-7, SC-8, SC-13, SC-28, CP-9, SA-9 |
| CSF 2.0 | ID.AM-05, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11 |
| Contract and regulatory basis | 32 CFR 2002.14(g); SP 800-171 Rev. 2 3.1.3, 3.8, 3.13.11, 3.13.16; FAR 52.204-21(b)(1)(vii) |
| Supporting standards | STD-08 Encryption and key management standard; STD-07 Contingency and recovery standard |

## 1. Purpose
Define how company, customer, and federal information is classified and handled so that each type gets protection that matches its sensitivity and its contract rules.

## 2. Scope
All information the company creates, receives, or holds, in any form (electronic, paper, removable media), and all systems and providers that handle it.

## 3. Classification levels
| Level | Examples | Where it may be stored |
|---|---|---|
| **CUI** | Prime network drawings, IP addressing plans, configuration templates, hardened image baselines, installation drawings | Only the Federal Integration Enclave and the FIL |
| **Restricted** | FCI in federal channel orders, employee personal information, supplier bank details, security configurations and logs | Approved company systems and providers bound by FAR 52.204-21 terms for FCI |
| **Confidential** | Contract pricing, reseller and supplier commercial data, margins | Approved company systems and approved AI tools |
| **Internal** | Procedures, general business information | Company systems |
| **Public** | Catalog, marketing material, published content | Anywhere after approval |

## 4. Policy statements
4.1 Every information owner must classify their information using the levels above. Information arriving from a prime marked CUI is CUI. (RA-2; ID.AM-05)
4.2 **CUI location.** CUI must be stored, processed, and transmitted only in the enclave and the FIL. It must never be attached to ERP records, sent to or from corporate email, saved on corporate file services, printed outside the FIL, or entered into any AI tool. (AC-4; PR.DS-10; DFARS 252.204-7012(b)(2))
4.3 Prime CUI must arrive only through the prime's secure file exchange into the enclave. Sales staff who receive CUI by corporate email must report it under POL-03 4.2 and not forward it. (AC-4; PR.DS-10)
4.4 CUI must be encrypted with FIPS 140-validated cryptography in transit and at rest. (SC-13; SC-8; SC-28; PR.DS-01; PR.DS-02)
4.5 Printed CUI and CUI media must carry CUI markings, be kept in locked FIL cabinets, and be shredded in the FIL when no longer needed. (MP-2; MP-4; PR.DS-01)
4.6 Removable storage is blocked on all endpoints except company-issued encrypted drives registered to named FIL technicians. (MP-7; PR.DS-01)
4.7 FCI may be shared only with providers whose contracts include FAR 52.204-21 safeguards, and federal channel orders must be filtered out of data feeds to vendors without them. (SA-9; GV.SC-05)
4.8 Restricted and Confidential data may be placed only in approved systems and approved AI tools (P10 approved-tools list). (AC-4; PR.DS-10)
4.9 Media must be sanitized or destroyed before disposal or reuse, with a certificate. (MP-6; PR.DS-01; FAR 52.204-21(b)(1)(vii))
4.10 Backups of Restricted and CUI data must be encrypted, isolated from production administrators, write-once, and restore-tested at least quarterly. (CP-9; PR.DS-11)

## 5. Compliance and enforcement
Compliance is checked by quarterly CUI content searches of corporate systems, clean-desk sweeps in the Integration Center, device control reports, and the annual assessment (P07). Violations are handled under POL-05 section 4.12.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. No exception may permit CUI outside the enclave and the FIL.

## 7. Related documents
POL-01; POL-03; STD-08; STD-07; System Security Plan (P02); P03 rows G-001, G-003, G-064, G-065, G-148
