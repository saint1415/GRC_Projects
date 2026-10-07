# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Owner | Security Manager with the General Counsel |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, or significant incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, CM-12, AC-3, AC-22, SC-8, SC-12, SC-28, SI-7, SI-12, MP-6, CP-9 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11, ID.RA-09 |
| Drivers | FAR 52.204-21(b)(1)(i), (iii), (iv), (vii); 15 CFR 762.6 (C-CRITICAL-MFG-R03); utility addendum sec. 5; FMS subscription agreements |
| Supporting standards | STD-07 Contingency and recovery standard; STD-08 Encryption and key management standard |

## 1. Purpose
Make sure every kind of company and customer information is protected according to its sensitivity, wherever it is stored or sent.

## 2. Scope
All information in any form, including designs, customer drawings, FMS data, firmware and software, test data, FCI, and personal information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Security Manager | Owns this policy with the General Counsel; data inventory |
| Data owners (VP Engineering, Director of Digital Services, Director of Quality, CFO, HR Director) | Classify their data and approve access |
| Contracts and Trade Compliance Manager | FCI labeling and export records |
| IT Director | Encryption, backups, media sanitization |

## 4. Policy statements
4.1 Information must be classified in one of four levels: **Restricted** (transformer designs, calculations, winding specifications; customer substation drawings under NDA; utility asset data in the FMS; firmware images, configuration software source, and signing keys; credentials; employee identity and bank data), **Confidential** (supplier pricing, bills of materials, contracts, certified test reports, export records, security documents, payroll), **Internal** (schedules, work instructions), and **Public**. FCI also carries an FCI label on top of its level. (RA-2; ID.AM-07)

4.2 Restricted data must be encrypted at rest on every device and service and encrypted in transit outside a plant network. (SC-28; SC-8; PR.DS-01; PR.DS-02)

4.3 Restricted data may be stored only in approved systems (PLM vault, labeled project sites, ERP, FMS, firmware library, company backups) and never on personal devices, personal cloud accounts, or unapproved AI tools. (AC-3; PR.DS-10)

4.4 The Security Manager and the Contracts and Trade Compliance Manager must keep a data inventory showing where Restricted data and FCI are stored and which suppliers receive them. (CM-12; ID.AM-07)

4.5 **FCI handling.** FCI must be kept only in the labeled federal project sites and the systems listed in the SSP, available to the named project team. It must not be posted publicly or entered into any unapproved AI tool or external service. (AC-3; AC-22; PR.DS-10)

4.6 **FMS data.** Each utility's data must be kept separate from every other utility's, used only to deliver the service, and returned or deleted at the end of the subscription as the agreement states. (AC-3; PR.DS-10)

4.7 Export classification and screening records must be kept at least 5 years, as 15 CFR 762.6 requires. The ERP keeps them 7. (SI-12; ID.AM-07)

4.8 **Firmware and software integrity.** Firmware images, configuration software releases, and signing keys must be kept in controlled systems; only staff approved by the VP Engineering may change them; signing keys must be held in the hardware-backed key service. (SI-7; SC-12; ID.RA-09)

4.9 Raw test data must be kept unaltered with the certified test report that relies on it, and test data imports into the MES must be integrity-checked. (SI-7; PR.DS-01)

4.10 **Backups.** ERP, FMS, PLM, MES, and file server backups must be encrypted, stored apart from production in the backup account or offline, protected from alteration or deletion, and restore-tested quarterly. PLC, HMI, and CNC programs and winding recipes must be backed up after every approved change and at least weekly to the OT backup store at each plant. (CP-9; PR.DS-11)

4.11 Media that held Restricted data or FCI must be wiped for reuse or destroyed by a vendor that issues certificates of destruction. (MP-6; PR.DS-01)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.13. Compliance is verified through the data inventory review, backup and restore test records, and the annual control assessment (P07: CP-9, CP-4).

## 6. Exceptions
Exceptions follow POL-01 section 4.12.

## 7. Related documents
POL-01; POL-05; STD-07; STD-08; STD-10; FAR 52.204-21; 15 CFR 762.6; FMS subscription agreements; utility addendum sec. 5
