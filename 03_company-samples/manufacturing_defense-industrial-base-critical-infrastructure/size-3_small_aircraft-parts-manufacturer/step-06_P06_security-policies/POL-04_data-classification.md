# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Director of Engineering |
| Approved by | Vice President of Operations (2026-08-31) |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes, incidents, or assessment findings |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-1, MP-2, MP-3, MP-4, MP-5, MP-6, MP-7, SC-8, SC-13, SC-28, CP-9, PE-17 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| SP 800-171 Rev. 2 and contract clauses | 3.1.3, 3.1.22, 3.8.1 to 3.8.9, 3.13.8, 3.13.11, 3.13.16; 32 CFR 2002.14; ITAR 22 CFR 120.54(a)(5); EAR 15 CFR 734.18(a)(5) |

## 1. Purpose
Classify company information by sensitivity and set handling rules so protection matches the harm a disclosure would cause. Most of the company's CUI is controlled technical information, and much of it is also export-controlled.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, temporary workers, and contractors) at the Florida plant and working remotely. Covers all company systems and data, with added rules for the CUI Engineering Enclave (CEE) defined in the SSP (P02), printed CUI on the shop floor, and systems that service providers operate for the company. It applies to controlled unclassified information (CUI), including controlled technical information and export-controlled technical data, federal contract information (FCI), and all other company information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Engineering | CUI data owner; decides what is CUI when a customer's marking is unclear |
| Contracts Manager | Export classification (ITAR or EAR) of technical data; public release review |
| Quality Manager | Printed drawings and travelers: distribution, storage, and destruction |
| IT Manager | Encryption, backup, and media sanitization |
| All workforce | Mark, handle, and dispose of information according to this policy |

## 4. Policy statements
4.1 Information must be classified in one of four levels:

| Level | Examples | Handling |
|---|---|---|
| **CUI** | Controlled drawings, 3D models, specifications, NC programs, travelers and inspection data that show controlled features; ITAR and EAR technical data | Enclave or controlled paper only; U.S. persons with need-to-know; FIPS-validated encryption |
| **FCI and Confidential** | DoD purchase orders, pricing, payroll, security documents | Company systems only; need-to-know; encrypted in transit |
| **Internal** | Schedules, procedures | Workforce only |
| **Public** | Website content released by the Contracts Manager | No restriction |

(RA-2; ID.AM-07)

4.2 CUI received from a customer keeps the customer's marking. CUI created by the company (for example, NC programs and travelers built from controlled drawings) must carry a CUI banner and the customer's distribution statement. MES print templates must add the banner automatically. (MP-3; 3.8.4)
4.3 CUI may be stored only in the enclave: PLM, enclave file storage, MES, and DNC. It must never be kept on corporate systems, personal devices, removable media outside the controlled USB set, or unapproved AI or file-sharing services. (MP-2; 3.1.3; 3.8.2)
4.4 CUI must be encrypted at rest and in transit with FIPS-validated cryptography. Encryption on every external path (SFTP gateway, site-to-site VPN, collaboration suite) must use modules with a current FIPS 140 validation. This also keeps the ITAR and EAR carve-outs for end-to-end encrypted data available. (SC-8; SC-13; SC-28; 3.13.8; 3.13.11; 3.13.16)
4.5 **Printed CUI.** Printed drawings and travelers must be kept in cell drawing cabinets when not in use, covered on visitor routes, and returned to the Quality Manager when a job closes. Printed CUI may leave the plant only in a sealed opaque envelope, logged by the Quality Manager, for an outside processor with DFARS flowdown or with an employee approved to carry it. (MP-4; MP-5; PE-17; 3.8.1; 3.8.5; 3.10.6; 32 CFR 2002.14(c)(3))
4.6 **Destruction.** Paper CUI must go only into locked shred bins and be destroyed by cross-cut shredding or a vendor that provides certificates of destruction. Digital media, including CNC controller storage sent out for repair, must be sanitized or removed before it leaves company control. (MP-6; ID.AM-08; 3.8.3)
4.7 **Removable media.** Only company-owned, labeled, inventoried USB drives may be used, and only to load the 6 legacy CNC machines until the DNC serial gateway replaces them. Drives must be scanned at the kiosk before each use. Drives with no identifiable owner are prohibited. (MP-7; 3.8.7; 3.8.8)
4.8 Backups of CUI must be encrypted, access-limited, stored apart from production administration, and restore-tested at least annually. (CP-9; PR.DS-11; 3.8.9)
4.9 Content may be posted on the public website or shared at trade shows only after the Contracts Manager confirms it contains no CUI or export-controlled data. (AC-22; 3.1.22)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement in POL-01 section 4.8. Sanctions range from retraining to termination, depending on intent and harm. A suspected unauthorized release of ITAR or EAR technical data is also referred to the Contracts Manager (Empowered Official) for a voluntary disclosure decision. Compliance is checked through the annual self-assessment against SP 800-171A objectives, the control assessment (P07), and the reviews in this policy set.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. They must be written, risk-rated, approved by the policy owner (or by the President for High risk), recorded in the risk register, and expire within 12 months. An exception never removes a DFARS 252.204-7012 duty or permits an unauthorized export.

## 7. Related documents
POL-01; POL-02; POL-05; P10 approved-tools list; customer marking instructions; 32 CFR Part 2002; DoD Instruction 5230.24 distribution statements
