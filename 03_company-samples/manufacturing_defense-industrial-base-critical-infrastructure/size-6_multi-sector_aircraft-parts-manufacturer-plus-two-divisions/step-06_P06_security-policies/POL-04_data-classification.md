# Data Classification and Handling Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-04 |
| Owner | Group CISO, with the Group export compliance director for export tags |
| Approved by | Group CISO and Group export compliance director, under authority of POL-01 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-4, AC-21, CM-8, CM-12, MP-2, MP-3, MP-4, MP-5, MP-6, MP-7, SC-8, SC-13, SC-28, CP-9, SI-12 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11 |
| SP 800-171 Rev. 2 | 3.1.3, 3.1.22, 3.8.1 to 3.8.9, 3.13.8, 3.13.11, 3.13.16 |
| Division supplements | Aircraft Parts: printed drawings, travelers, NC programs, and USB transfer at plants. Engineering Services: test data media and CUI at customer sites. Defense Software: Government data, Government-related data, and tenant data |

## 1. Purpose
Classify group information by sensitivity and by who controls it, and set handling rules so that CUI, export-controlled data, and Government data stay only in approved systems and reach only authorized people.

## 2. Scope
All information the group creates, receives, maintains, or transmits, in any form, including paper on shop floors and in engineering centers, removable media, and data in sister-division services.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Data owners | Decide what is CUI; set export tags with the Empowered Officials |
| Group export compliance office | Owns export tag definitions and audits |
| GCEE platform engineering lead and platform owners | Enforce tags, locations, and encryption |
| All workforce | Handle information according to its class and tag |

## 4. Policy statements
4.1 Information must be classified as **CUI** (including CDI and controlled technical information), **Government data** (data created or obtained for DoD under the DoD edition contracts), **Confidential**, **Internal**, or **Public**. Export-controlled data also carries an export tag (ITAR, EAR, or no foreign access). (RA-2; ID.AM-07)

4.2 CUI must be marked as the contract and the DoD CUI program require. PLM must apply markings automatically to released documents. (MP-3; ID.AM-07; 3.8.4)

4.3 **Approved locations.** CUI may be stored and processed only in the GCEE, the plant enclave systems, the CUI collaboration suite, and other systems listed in the CUI location register. CUI must not be stored in a sister-division service until that service is in the register (POL-01 4.9). (CM-12; AC-4; PR.DS-10; 3.1.3)

4.4 CUI and Government data must be encrypted at rest and in transit with FIPS-validated cryptography and group-managed keys. (SC-8; SC-13; SC-28; PR.DS-01; PR.DS-02; 3.13.8; 3.13.11; 3.13.16)

4.5 **Government-related data** (data a Defense Software platform creates or obtains through processing Government data) may be used only to manage the operating environment of that platform, unless the Contracting Officer approves another use in writing. (AC-21; PR.DS-10; 252.239-7010(c)(2))

4.6 **Removable media.** Only registered, encrypted drives with a named owner may hold CUI. Drives without an identifiable owner must be blocked and collected. Transfer workstations that load machines by USB must enforce device control. CUI moved on media must be encrypted or physically protected and tracked. (MP-5; MP-7; PR.DS-01; 3.8.5 to 3.8.8)

4.7 **Paper.** Printed CUI must be stored in locked containers when not in use, covered during visits, and destroyed in locked shred bins. (MP-4; MP-6; 3.8.1; 3.8.3)

4.8 Backups of CUI must be encrypted, immutable, held in a separate account or region inside the government-community offering, and restore-tested at least twice a year for High-criticality systems. (CP-9; PR.DS-11; 3.8.9)

4.9 Media holding CUI must be sanitized to NIST SP 800-88 or destroyed with a certificate before disposal or reuse. (MP-6; ID.AM-08; 3.8.3)

4.10 CUI, export-controlled data, and Government data must not be entered into any AI tool unless the tool is approved under the Group AI Standard, sits inside an approved boundary for that data, and does not use the data to train models for other customers. (AC-4; PL-4)

4.11 Information must be retained per the group retention schedule and each contract's terms; Government data must be returned or disposed of as the contract specifies. (SI-12; 252.239-7010(i))

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment (AC-4, MP-7, CM-8, SC-13), quarterly export tag audits, and plant walkthroughs.

## 6. Exceptions
Exceptions follow POL-01 section 4.12.

## 7. Related documents
POL-01; POL-02; `division-supplements.md`; GCEE SSP (P02); Group AI Standard (P10).
