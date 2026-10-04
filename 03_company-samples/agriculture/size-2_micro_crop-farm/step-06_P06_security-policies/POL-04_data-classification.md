# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Office Manager (Security Coordinator) |
| Approved by | Owner and General Manager, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes |
| Implements (SP 800-53 Rev. 5) | RA-2, CM-8, MP-6, SC-8, SC-28, CP-9, CP-4, SA-9, SI-12, PL-4 |
| CSF 2.0 | ID.AM-01, ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11, GV.SC-05 |
| Binding rules served | Fla. Stat. 501.171(2) and (8) (security and disposal); 21 CFR 112.164(a)(1) and 112.166(a) (Produce Safety record retention and access); 20 CFR 655.122(j)(2) and (j)(4) (H-2A record safekeeping and retention) |

## 1. Purpose
Sort farm information by how much harm its loss, change, or disclosure would cause, and set simple handling, backup, retention, and disposal rules for each level.

## 2. Scope
All workforce members of Cris Santos Company and all farm information in any form: in SYS-01, email, the Office folder, the telematics portal, the payroll and accounting services, on devices, on paper, in drone images, and in any supplier's system.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Office Manager (Security Coordinator) | Owns this policy; keeps the inventory of devices, OT, services, and Restricted data; approves new tools |
| Irrigation and Equipment Technician | Keeps the OT part of the inventory and the controller program copy; follows the drone imagery rule |
| MSP | Encryption, backup, restore tests, and device wiping, as directed by the Security Coordinator |
| All workforce | Handle information according to its level |

## 4. Policy statements
4.1 Farm information has three levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Social Security, passport, visa, and bank account numbers; H-2A files; payroll exports; operator location history; passwords, PINs, and MFA codes; the pump station controller program and gateway settings | Only in approved locations (4.3); encrypted at rest and in transit; limited to people who need it; never in personal accounts or public AI tools |
| **Internal** | Produce Safety records, daily hours, field and application records, yields, load commitments, drone imagery, contracts, security documents | Workforce and approved suppliers only; encrypted in transit; changed only by named users |
| **Public** | Farm name, address, crops grown | No restriction |

When unsure, treat information as Restricted. (RA-2; ID.AM-07)

4.2 Restricted information must be encrypted wherever it is stored, including on every laptop, desktop, tablet, and phone that holds it, and whenever it is sent outside farm systems. Payroll and H-2A documents are sent to the payroll service and the H-2A filing agent only through their portals, never as email attachments. (SC-28; SC-8; PR.DS-01; PR.DS-02; Fla. Stat. 501.171(2))

4.3 Restricted information may be kept only in: the restricted Office folder in the productivity suite (Office Manager and Owner and General Manager only, not synced to any desktop), the payroll service and accounting SaaS, the H-2A filing agent's portal, the telematics portal (operator location history), and, for the controller program, the encrypted offline drive in the farm office. The inventory (4.4) records every place Restricted information lives. (AC-3; ID.AM-07; 20 CFR 655.122(j)(2))

4.4 The Security Coordinator must keep a one-page inventory of every IT device, OT and IoT device (with firmware version and location), SaaS service, and place Restricted information is stored, and update it when anything is added or removed. (CM-8; ID.AM-01; ID.AM-02)

4.5 Before any new supplier, app, or device receives Restricted or Internal information or connects to irrigation equipment, the Security Coordinator must approve it under POL-02 A.5 and add it to the inventory. (SA-9; GV.SC-05)

4.6 **AI tools.** Farm information may be entered only into AI tools on the approved list kept by the Security Coordinator. Restricted information must never be entered into any AI tool. Internal information (drone imagery, yields) may go only to an approved AI tool whose terms bar use of farm data to train or improve models for others without the farm's opt-in. Public or personal AI chatbots must never receive Restricted or Internal information. (SA-9; PL-4)

4.7 **Disposal.** Devices and media that held Restricted information must be wiped before reuse or given away, or destroyed by a vendor that provides a certificate of destruction. Paper with Restricted information is shredded. The Security Coordinator keeps each wipe or destruction record. (MP-6; ID.AM-08; Fla. Stat. 501.171(8))

4.8 **Retention schedule.** Produce Safety records are kept at least 2 years after creation (21 CFR 112.164(a)(1)). H-2A earnings records, including daily hours, are kept at least 3 years after the date of the certification (20 CFR 655.122(j)(4)). Security records follow POL-02 A.7. Records past their retention period and no longer needed are disposed of under 4.7. (SI-12; ID.AM-08)

4.9 **Backups.** The productivity suite must be backed up nightly, with versions kept at least 90 days in storage that cannot be changed or deleted within that period, and the backup console protected with MFA. SYS-01 records must be exported monthly to an encrypted drive kept in the farm office. The farm must hold a current copy of the pump station controller program after every change. The MSP must restore a sample every quarter and give the Security Coordinator a written result. (CP-9; CP-4; PR.DS-11; 21 CFR 112.166(a))

4.10 **Drone imagery.** Drone images are used for crops only. They must not be used to watch, identify, or evaluate workers or neighbors. Images that show identifiable people and are not needed for crop work are deleted within 30 days. (PL-4; PR.DS-01)

## 5. Compliance and enforcement
Breaking this policy leads to action under POL-02 A.4. Compliance is checked through the monthly MSP report (encryption and backup status), quarterly restore results, the monthly export record, and the annual assessment (P07).

## 6. Exceptions
Exceptions follow POL-02 A.9.

## 7. Related documents
POL-02; POL-03; inventory; supplier checklist; P04 cloud control map; P10 AI risk assessment
