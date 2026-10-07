# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | VP Engineering |
| Approved by | VP Operations, 2026-09-04 |
| Effective date | 2026-09-08 |
| Review cycle | Annually (next review by 2027-09-08), and after major changes or incidents |
| Replaces | IT handbook (2021), for the topics covered here |
| Implements (SP 800-53 Rev. 5) | RA-2, CM-12, MP-6, SC-8, SC-28, SI-7, SI-12, CP-9, SR-11 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-11, ID.AM-08, ID.RA-09 |
| Contract and regulatory drivers | FAR 52.204-21(b)(1)(i), (iii), (iv), (vii); 15 CFR 762.6 (C-CRITICAL-MFG-R03); Utility addendum sec. 5 (CIP-013-2 R1.2.5 flow-down); customer NDAs |

## 1. Purpose
Classify company and customer information by sensitivity and set handling rules, so that protection matches the harm a disclosure or alteration would cause.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, temporary workers, and contractors) on the Florida campus and in the field. Covers office IT, plant control systems (OT), the high-voltage test bay, cloud and SaaS services, and systems that service providers operate for the company. It applies to all company information, customer information shared under NDA, and federal contract information (FCI).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| VP Engineering | Owns classification; approves new uses of Restricted data |
| Contracts and Compliance Manager | Identifies FCI and export records; keeps the FCI part of the data inventory |
| IT Manager | Implements encryption, backup, and disposal controls |
| Controls Engineer | Backs up controller programs and recipes |
| Quality Manager | Protects test data and certified test reports |
| All workforce | Label and handle information according to this policy |

## 4. Policy statements
4.1 Information must be classified in one of four levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Transformer designs, electromagnetic calculations, winding specifications; customer substation drawings under NDA; TMU firmware images and configuration files; credentials; employee Social Security and bank data | Encrypted at rest and in transit; named groups only; approved systems only |
| **Confidential** | Supplier pricing and bills of materials; contracts; certified test reports; export classification and screening records; security documents; payroll | Encrypted in transit; need-to-know |
| **Internal** | Production schedules, work instructions, procedures | Workforce only |
| **Public** | Website, catalog, published ratings | No restriction |

Federal contract information (FCI) also carries an **FCI** label on top of its level, and follows 4.5. (RA-2; ID.AM-07)

4.2 Restricted data must be encrypted at rest on every device and service, including the PLM vault and file server, and encrypted in transit outside the plant network. (SC-28; SC-8; PR.DS-01; PR.DS-02)

4.3 Restricted data may be stored only in approved systems: the PLM vault, the engineering file share, the ERP, the TMU firmware library, and company backups. It must never be kept on personal devices, personal cloud accounts, or unapproved AI tools. (AC-3)

4.4 The IT Manager and the Contracts and Compliance Manager must keep a data inventory showing where Restricted data and FCI are stored and which suppliers receive them. (CM-12; ID.AM-07)

4.5 **FCI handling.** FCI must be kept only in the labeled federal project folder and project records, available to the named project team. It must not be posted on public websites, and must not be entered into any AI tool or external service that is not approved. (AC-3; AC-22; FAR 52.204-21(b)(1)(i), (iii), (iv))

4.6 Export classification and screening records must be kept for at least 5 years, as 15 CFR 762.6 requires. The ERP keeps them for 7. (SI-12; C-CRITICAL-MFG-R03)

4.7 **Firmware integrity.** TMU firmware images and configuration files must be kept in the controlled firmware library. Only staff approved by the VP Engineering may change them, and each image's hash or signature must be verified on receipt and again before loading at final test. (SI-7; SR-11; ID.RA-09; Utility addendum sec. 5)

4.8 Raw test data must be kept unaltered with the certified test report that relies on it. (SI-7)

4.9 **Backups.** ERP, PLM, MES, and file server backups must be encrypted, stored apart from production (a separate account or offline store), protected from alteration or deletion, and restore-tested quarterly. PLC, HMI, and CNC programs and winding recipes must be backed up after every approved change and monthly to the offline OT backup store. (CP-9; PR.DS-11)

4.10 Media and devices that held Restricted data or FCI must be wiped (for reuse) or destroyed by a vendor that issues certificates of destruction (for disposal). (MP-6; ID.AM-08; FAR 52.204-21(b)(1)(vii))

4.11 Restricted data and FCI must not be entered into any AI tool that is not on the approved list (POL-05 4.8; P10). (SA-9)

## 5. Compliance and enforcement
Violations are handled under POL-01 statement 4.12. Consequences range from retraining to termination of employment or contract, depending on intent and harm. Compliance is checked through the annual control assessment (P07), access reviews, and the quarterly obligations register review.

## 6. Exceptions
Exceptions follow POL-01 statement 4.11. They must be written, risk-rated, approved by the policy owner (or by the President for High risk), and expire within 12 months. Exceptions for plant equipment that cannot technically meet a statement (for example, an HMI without individual accounts) must name the compensating controls.

## 7. Related documents
POL-01; POL-02; POL-05; data inventory; firmware library procedure; P10 approved AI tools list; customer NDAs; FAR 52.204-21; 15 CFR 762.6
