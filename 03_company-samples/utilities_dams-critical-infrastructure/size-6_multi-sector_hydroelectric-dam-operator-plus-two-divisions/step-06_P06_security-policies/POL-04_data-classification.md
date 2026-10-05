# Data Classification and Handling Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-04 |
| Owner | General Counsel, with the Group CISO |
| Approved by | Group CISO and General Counsel under authority of POL-01, 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-3, AC-4, AC-21, CM-8, MP-3, SC-8, SC-28, CP-9, MP-6, SI-12, SA-9 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11, ID.AM-08 |
| Regulatory drivers | C-DAMS-R03 (CIP-011-3 R1 and R2; CIP-004-7 R6); C-DAMS-R01 (Rev. 3A 3.2 OPSEC, 7.2 document control, 8.0 marking; Form 1 Q22); N23-R03 and N23-R04 (252.204-7012(b); SP 800-171 Rev. 2 3.1.3, 3.8, 3.13.11); 18 CFR 388.113 (CEII); state breach laws |
| Division supplements | Hydro: BCSI and security-sensitive documents. Constructors: CUI and FCI. Engineering: client CEII and DSMS client data |

## 1. Purpose
Classify group information by sensitivity and by whose information it is, and set handling rules so that CEII, BCSI, CUI, and client information stay where they belong.

## 2. Scope
All information the group creates, receives, maintains, or transmits, in any form, including on shared platforms and in affiliate project folders.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| General Counsel | Owns classes and handling rules; intercompany and client NDAs |
| Information owners | Classify and label information; approve access and sharing |
| Director, Hydro Security | Owns the BCSI and security-sensitive document library |
| Federal Programs Compliance Director | Owns CUI handling and the FPE |
| All workforce | Handle information according to its class |

## 4. Policy statements
4.1 Information must be classified as **Restricted** (BCSI, CEII, security-sensitive documents, CUI, client CEII, personal information, credentials, and keys), **Confidential**, **Internal**, or **Public**. (RA-2; ID.AM-07)

4.2 **Marking.** Security Assessments, Vulnerability Assessments, Security Plans, and certification letters must be marked "Privileged - Security Sensitive Material." CUI must carry the markings the contracting agency applied. BCSI must be identified under the CIP-011 program. (MP-3; CIP-011-3 R1 Part 1.1; Rev. 3A 8.0)

4.3 **Where Restricted information may live.** BCSI and security-sensitive documents only in the Hydro restricted library; CUI only in the Federal Projects Enclave; client CEII only in restricted project libraries. General file shares, the commercial project platform, and personal storage are prohibited for these classes. (AC-3; AC-4; PR.DS-10; SP 800-171 Rev. 2 3.1.3; CIP-011-3 R1 Part 1.2)

4.4 **Between divisions.** Sharing Restricted information with another division requires the owner's approval, an NDA or intercompany agreement, and, for BCSI, an authorization record (CIP-004-7 R6 Part 6.1). (AC-21; PR.DS-10)

4.5 Restricted information must be encrypted at rest and in transit with approved algorithms; CUI with FIPS-validated cryptography. (SC-28; SC-8; SC-13; PR.DS-01; PR.DS-02; SP 800-171 Rev. 2 3.13.11)

4.6 Backups of Restricted information must be immutable, held in a different provider or account from production, and restore-tested at least twice a year for High-criticality systems. (CP-9; PR.DS-11)

4.7 Media holding Restricted information must be sanitized or destroyed with a certificate before reuse or disposal, including OT devices and commissioning laptops. (MP-6; ID.AM-08; CIP-011-3 R2)

4.8 Information must be retained per the group retention schedule, and personal information that is no longer needed (for example crew badging lists after a project ends) must be deleted. (SI-12)

4.9 Restricted information must not be entered into any AI tool unless the tool is on the Group AI approved-tools list for that class. CUI, BCSI, and client CEII may not be entered into any external AI service. (SA-9; PL-4)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment (AC-3, AC-4), DLP reports, BCSI access reviews, and share scans.

## 6. Exceptions
Exceptions follow POL-01 section 4.11. No exception may move CUI outside the FPE or BCSI outside the restricted library.

## 7. Related documents
POL-01; POL-02; `division-supplements.md`; CIP-011 information protection program; FPE SSP; client NDAs.
