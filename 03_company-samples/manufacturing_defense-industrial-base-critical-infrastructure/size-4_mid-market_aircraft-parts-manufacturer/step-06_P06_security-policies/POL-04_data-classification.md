# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Owner | Director of Engineering (CUI data owner) |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes, incidents, or assessment findings |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-1, MP-2, MP-3, MP-4, MP-5, MP-6, MP-7, SC-8, SC-13, SC-28, CP-2, CP-4, CP-9, CP-10, CM-12, AC-22 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11, RC.RP-01 |
| SP 800-171 Rev. 2 and other rules | 3.1.3, 3.1.22, 3.8.1 to 3.8.9, 3.13.8, 3.13.11, 3.13.16; 32 CFR 2002.14; ITAR 22 CFR 120.54(a)(5); EAR 15 CFR 734.18(a)(5) |
| Supporting standards | STD-07 Contingency and recovery; STD-08 Cryptography and key management; STD-11 CUI marking and media handling |

## 1. Purpose
Classify company information by sensitivity and set handling rules so protection matches the harm a disclosure or loss would cause. Most of the company's CUI is controlled technical information, much of it export-controlled, and some of the most sensitive data belongs to services customers.

## 2. Scope
All information the company creates, receives, or holds, in any form, at both plants, in the cloud, at suppliers, and in transit.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Engineering | CUI data owner; decides what is CUI when a customer's marking is unclear |
| Director of Trade Compliance and Contracts | Export classification (ITAR or EAR); public release review |
| Director of Quality | Printed drawings, travelers, and test reports: distribution, storage, and destruction at both plants |
| Director of Additive and Engineering Services | Services customer data handling |
| IT Director | Encryption, backups, recovery, media sanitization |
| All workforce | Mark, handle, and dispose of information according to this policy |

## 4. Policy statements
4.1 Information must be classified in one of four levels:

| Level | Examples | Handling |
|---|---|---|
| **CUI** | Controlled drawings, models, specifications, NC programs, build files, test procedures, and travelers or inspection data that show controlled features; ITAR and EAR technical data | Enclave or controlled paper only; U.S. persons with need-to-know (unless an export authorization covers the data); FIPS-validated encryption |
| **Confidential** | Services customer files (when not CUI), DoD purchase orders (FCI), pricing, payroll, security documents | Company systems only; need-to-know; encrypted in transit and at rest |
| **Internal** | Schedules, procedures | Workforce only |
| **Public** | Website content released under 4.9 | No restriction |

(RA-2; ID.AM-07)

4.2 CUI received from a customer keeps the customer's marking. CUI created by the company (NC programs, build files, travelers, test reports built from controlled data) must carry a CUI banner and the customer's distribution statement. MES print templates at both plants must add the banner automatically. (MP-3; 3.8.4)
4.3 CUI may be stored only in the enclave: PLM, enclave file storage, the MFT gateway, MES, DNC, and the build preparation and test data systems. It must never be kept on corporate systems, personal devices, uncontrolled removable media, vendor clouds, or any AI service outside the enclave. Every approved CUI location is recorded in the data flow register. (MP-2; CM-12; 3.1.3; 3.8.2)
4.4 CUI must be encrypted at rest and in transit with FIPS-validated cryptography, on every path including the tunnel between the plants. This also keeps the ITAR and EAR carve-outs for end-to-end encrypted data available. (SC-8; SC-13; SC-28; 3.13.8; 3.13.11; 3.13.16)
4.5 **Printed CUI.** At both plants, printed drawings, travelers, and test reports must be kept in lockable cell cabinets when not in use, covered on visitor routes, and returned to quality when a job closes. Printed CUI may leave a plant only in a sealed opaque envelope, logged by quality, for a supplier with DFARS flowdown or an employee approved to carry it. (MP-4; MP-5; PE-5; 3.8.1; 3.8.5; 32 CFR 2002.14)
4.6 **Destruction.** Paper CUI must go only into locked shred bins and be destroyed by a vendor that provides certificates of destruction. Digital media, including controller and test stand storage sent out for repair, must be sanitized or removed before it leaves company control. (MP-6; 3.8.3)
4.7 **Removable media.** Only company-owned, labeled, inventoried, encrypted USB drives may be used, and only to load the 8 legacy CNC machines at Plant 2 until the DNC serial gateway replaces them. Drives must be scanned before each use. Drives with no identifiable owner must be removed and destroyed. (MP-7; 3.8.7; 3.8.8)
4.8 **Backups and recovery.** Backups of CUI must be encrypted, stored in the isolated backup account with write-once retention, and restore-tested quarterly for each High-criticality process in the BIA. Recovery objectives come from the BIA (P05) and are maintained in the contingency plan. (CP-2; CP-4; CP-9; CP-10; PR.DS-11; 3.8.9)
4.9 Content may be posted on the public website or shown at trade shows only after the Director of Trade Compliance and Contracts confirms it contains no CUI or export-controlled data. (AC-22; 3.1.22)
4.10 **Services customer data.** Each services customer's files must be kept in a separate folder on the MFT gateway and build preparation server, accessed only by the engineers assigned to that customer, reviewed quarterly, and deleted or returned at the end of the engagement as the agreement requires. (AC-3; AC-4)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement in POL-01 section 4.8. A suspected unauthorized release of ITAR or EAR technical data is referred to the Director of Trade Compliance and Contracts for a voluntary disclosure decision. Compliance is checked through quality walkthroughs, the annual self-assessment, and the co-sourced internal audit (P07).

## 6. Exceptions
Exceptions follow POL-01 section 4.7. An exception never permits CUI outside the enclave or an unauthorized export.

## 7. Related documents
POL-01; POL-02; POL-05; STD-07; STD-08; STD-11; data flow register; customer marking instructions; 32 CFR Part 2002
