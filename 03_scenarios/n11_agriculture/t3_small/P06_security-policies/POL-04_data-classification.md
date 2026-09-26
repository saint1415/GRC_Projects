# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Operations and Technology Manager |
| Approved by | Majority owner and General Manager, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-6, SC-8, SC-28, SI-12, CP-9, CM-8, AC-3 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| Other requirements | Fla. Stat. 501.171(1)(g), (2), and (8); 21 CFR 112.161-112.166; 20 CFR 655.122(j) |
| Languages | Issued in English; a Spanish summary is given to all field staff |

## 1. Purpose
Classify farm information by sensitivity and legal weight, and set handling, retention, and disposal rules so protection matches the harm a loss or change would cause.

## 2. Scope
All Cris Santos Company workforce members (owners, year-round and seasonal employees including H-2A workers, and contractors such as the MSP and the irrigation integrator when they work on farm systems) at the Home Block and the North Block. Covers all farm systems and data, including the irrigation, pump, fertigation, and cooler operational technology (OT) and the systems vendors operate for the farm.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Operations and Technology Manager | Owns this policy; keeps the data inventory; runs encryption, backup, and disposal |
| Office and HR Manager | Handles personnel, payroll, and H-2A records |
| Food Safety and Packing Lead | Handles Produce Safety records |
| All workforce | Handle information according to its level |

## 4. Policy statements
4.1 Information must be classified in one of five levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Personal information under Fla. Stat. 501.171(1)(g): Social Security, passport, visa, and bank account numbers; operator location history linked to a name; account passwords | Encrypted at rest and in transit; named people only; approved systems only |
| **Regulated records** | Produce Safety records; H-2A earnings records including field tally | Kept accurate and unaltered; named users only; retained and exportable as 4.6 requires |
| **Confidential** | Yields, buyer prices, PLC programs, network diagrams, security documents | Need-to-know; not shared outside the farm without the owner's approval |
| **Internal** | Crop plans, schedules, procedures | Workforce only |
| **Public** | Farm stand hours, website, product list | No restriction |

(RA-2; ID.AM-07)
4.2 Restricted data must be encrypted at rest on every device and service, including desktops and tablets, and encrypted in transit. (SC-28; SC-8; PR.DS-01; PR.DS-02; Fla. Stat. 501.171(2))
4.3 Restricted data may be kept only in the payroll provider, the accounting SaaS, the restricted personnel library, and the backup vault. It must never be kept on personal phones or in personal cloud accounts. (AC-3)
4.4 The security lead must keep an inventory of where Restricted data and Regulated records are stored and which vendors receive them, including the equipment telematics portal. (CM-8; ID.AM-07)
4.5 Operator location history in the telematics portal must be deleted or de-identified after 2 seasons unless needed for a warranty or legal claim. (SI-12)
4.6 **Retention.** Produce Safety records must be kept for at least 2 years after creation (21 CFR 112.164(a)(1)) in a form FDA can read (112.166(b)). H-2A earnings records must be kept for at least 3 years after the certification date (20 CFR 655.122(j)(4)). A farm-held export of both must be taken from the farm management platform every month. (SI-12; CP-9)
4.7 **Backups** must be encrypted, stored in a separate account and region from production, protected from deletion or change (immutable), and restore-tested every quarter. PLC and HMI programs must be backed up after every change and kept with a version number. (CP-9; PR.DS-11)
4.8 **Disposal.** Devices and media holding Restricted data or Regulated records must be wiped or destroyed with a record kept. Customer records must be shredded or erased when no longer needed, as Fla. Stat. 501.171(8) requires. (MP-6; ID.AM-08)
4.9 Restricted data must not be entered into AI tools. Farm imagery and yield data may be shared only with AI tools on the approved list whose terms bar secondary use (see POL-05 and P10). (SA-9)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.9. Consequences range from retraining to termination, depending on intent and harm, and are applied the same way to every worker regardless of visa status. Compliance is checked through the annual control assessment (P07) and the access reviews in this policy set.

## 6. Exceptions
Exceptions follow POL-01 section 4.8. They must be written, risk-rated, approved by the policy owner (or by the majority owner and General Manager for High risk), and expire within 12 months.

## 7. Related documents
POL-01; POL-05; data inventory; retention schedule; P10 AI approved-tools list
