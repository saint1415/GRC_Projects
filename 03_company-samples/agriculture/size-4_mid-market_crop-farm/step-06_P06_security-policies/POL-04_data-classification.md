# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Owner | Security Manager (records retention with the Director of Food Safety and Quality and the HR Director) |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-6, SC-8, SC-12, SC-28, CP-9, CM-8, AC-3, SA-9, SI-12 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| Other requirements | Fla. Stat. 501.171(1)(g), (2), and (8); 21 CFR 112.164 and 112.166; 21 CFR 1.1455(c)-(d) (FTR, readiness); 20 CFR 655.122(j)(2) and (j)(4); 40 CFR 170.311(b)(6); 7 CFR 46.32(b) |
| Languages | Issued in English; a Spanish summary is given to crew leads and Food Safety Coordinators |
| Supporting standards | STD-08 Encryption and key management standard; STD-07 Contingency and recovery standard; STD-04 OT security standard |

## 1. Purpose
Classify company information by sensitivity and legal weight, and set handling, retention, backup, and disposal rules so protection matches the harm a disclosure, loss, or change would cause.

## 2. Scope
All information the company creates, receives, maintains, or transmits, in any form, at every site and in every system: SaaS, the cloud landing zone, OT controllers and historians, time clocks, tablets, drones, and data held by vendors and agricultural data services.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Security Manager | Owns this policy; keeps the data inventory; approves new locations of Restricted data |
| Director of Food Safety and Quality | Owns Produce Safety, pesticide application, and traceability records and their exports |
| HR Director | Owns personnel, payroll, H-2A, and biometric time clock data |
| Vice President of Grower Services | Owns grower business, pack-out, and settlement data |
| IT Director | Implements encryption, backup, and disposal controls |
| All workforce | Handle information according to its level |

## 4. Policy statements
4.1 Information must be classified in one of five levels. (RA-2; ID.AM-07)

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Personal information under Fla. Stat. 501.171(1)(g): Social Security, passport, visa, and bank account numbers; biometric templates; operator geolocation history; health information in workers' compensation files; credentials | Encrypted at rest and in transit; named people only; approved systems only |
| **Regulated records** | Produce Safety records; pesticide application and hazard information; H-2A earnings records including field tally; Food Traceability Rule key data elements; grower settlement and pack-out records | Kept accurate and unaltered with an edit history; named users only; retained and exportable as 4.7 requires |
| **Confidential** | Grower prices and yields, customer pricing, PLC programs, fertigation recipes, ripening programs, network diagrams, the food defense plan, security documents | Need-to-know; not shared outside the company without the owner's approval |
| **Internal** | Crop plans, schedules, procedures | Workforce only |
| **Public** | Website, product lists, market hours | No restriction |

4.2 Restricted data must be encrypted at rest on every device, service, and backup (including the local SCADA backup device and packinghouse line PCs if they hold it) and encrypted in transit. (SC-28; SC-8; PR.DS-01; PR.DS-02; Fla. Stat. 501.171(2))
4.3 Encryption keys for cloud workloads and backups must be managed in the company's key service, with separate keys for the backup account. (SC-12)
4.4 The Security Manager must keep a **data inventory** of where Restricted data and Regulated records are stored and which vendors receive them, including the 14 biometric time clocks, the personnel share, mailboxes, the telematics portal, and agricultural data services. It must be reconciled each quarter. (CM-8; ID.AM-07)
4.5 Restricted data may be stored only in the HR and payroll service, the ERP, the grower portal settlement database, the restricted HR share, and the backup account. Payroll and HR exports must be deleted from mailboxes and file shares within 90 days. Restricted data must never be kept on personal devices, in personal cloud accounts, or in unapproved AI tools. (AC-3)
4.6 **Biometric and location data.** Time clock templates must be deleted within 30 days after a worker separates or at season end, whichever comes first. Operator location history in the telematics portal must be deleted or de-identified after 13 months unless it is needed for a warranty or legal claim. (SI-12)
4.7 **Retention schedule for regulated records.** A company-held copy must be exported monthly from SYS-01 to the backup account, and a full record set must be retrievable within 24 hours (quarterly drill). (SI-12; CP-9; PR.DS-11)

| Record | Minimum retention | Basis |
|---|---|---|
| Produce Safety records | 2 years after creation (2 years after use ends for equipment, process, and analysis records) | 21 CFR 112.164(a)(1), (b) |
| Pesticide application and hazard information | 2 years after the restricted-entry interval expires | 40 CFR 170.311(b)(6) |
| H-2A earnings records, including field tally | 3 years after the date of each labor certification | 20 CFR 655.122(j)(4) |
| Food Traceability Rule records (tomatoes, peppers, watermelons) | 2 years from creation (readiness; not enforced before 2028-07-20) | 21 CFR 1.1455(d) |
| Grower receiving, grading, pack-out, and settlement records | 7 years (company rule, matching finance records) | Company rule; 7 CFR 46.32(b) requires complete, auditable records |
| Security logs | 1 year searchable; 3 years archived | POL-01 4.12; STD-02 |

4.8 **Backups** of Restricted data and Regulated records must be encrypted, stored in the separate backup account in a second region, protected by write-once retention, and restore-tested every quarter. PLC and HMI programs, SCADA images, fertigation recipes, and ripening programs must be copied to offline, versioned storage after every change and verified each quarter. (CP-9; PR.DS-11)
4.9 **Disposal.** Devices and media holding Restricted data or Regulated records, including HMIs, line PCs, time clocks, tablets, and drives returned to vendors, must be wiped or destroyed with a certificate kept. Customer and worker records must be shredded or erased when no longer to be retained, as Fla. Stat. 501.171(8) requires. (MP-6; ID.AM-08)
4.10 **Agricultural data shared with vendors.** Company and grower imagery, yield, and field data may be shared only with services on the approved list whose terms bar secondary use without opt-in and require deletion on exit (STD-03; P10). (SA-9)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.8. Compliance is checked through the annual independent assessment (P07), the quarterly data inventory reconciliation, and the quarterly retrieval drill.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. No exception may shorten a retention period set by law.

## 7. Related documents
POL-01; POL-05; STD-03; STD-04; STD-07; STD-08; data inventory; P04 cloud architecture; P10 approved-tools list
