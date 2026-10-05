# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (community water system, 2,850 population served) |
| Policy ID | POL-04 |
| Owner | Office Manager (security and compliance coordinator), with the Chief Operator for OT information and backups |
| Approved by | Owner and General Manager, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Every August (next review 2027-08-31), and after major changes |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-3, CM-8, SC-8, SC-28, CP-9, CP-4, SA-9, PL-4, MP-6, SI-12 |
| CSF 2.0 | ID.AM-01, ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11, GV.SC-05, GV.PO-02 |
| Regulatory basis | Drinking water record retention, 40 CFR 141.33; customer personal information and disposal, Fla. Stat. 501.171. Readiness for SDWA section 1433 information protection, 42 U.S.C. 300i-2 |

## 1. Purpose
Sort company information by the harm its loss, change, or disclosure could cause, and set simple handling rules for each level. For a water system the most sensitive information is not customer data but the information that would help someone attack the plant, and the PLC program the company needs to recover it.

## 2. Scope
All employees and contractors, and all company information in any form: in the SaaS systems, on the HMI computer, in the PLC, on backup drives, in the plant binder, on paper, and in any vendor's system.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Office Manager | Owns this policy; keeps the SaaS and device list; approves new tools; manages the restricted folder |
| Chief Operator | Owns OT information: the PLC program, HMI project, drawings, device credentials, and the OT inventory; runs the OT backups |
| MSP | Office backup, restore tests, encryption, and device wiping, as the Office Manager directs |
| All staff | Handle information according to its level |

## 4. Policy statements
4.1 Company information has three levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | SCADA drawings and network information; HMI, PLC, modem, gateway, and remote access credentials; the PLC program and HMI project; the OT inventory; the emergency plan's cyber annex and this assessment set; customer bank draft details and portal credentials; payroll bank details | Only in the locations in 4.2; named-role access; encrypted at rest and in transit; never in personal accounts or public AI tools |
| **Internal** | Customer names, addresses, phone numbers, and usage; the printed contact list for notices; compliance records and lab reports; HR files; contracts | Staff and approved vendors only; encrypted in transit; paper kept in locked rooms |
| **Public** | Rates, the annual water quality report, issued public notices, the website | No restriction |

When unsure, treat information as Restricted. (RA-2; ID.AM-07)

4.2 **Where Restricted information may be kept.** The restricted OT folder in the productivity suite (Owner, Office Manager, and Chief Operator only), the company password manager, the 2 encrypted offline backup drives (4.5), the HMI computer, the billing system, and the accounting and payroll system. The SCADA drawings and the password spreadsheet must be moved out of the shared folder by 2026-09-30. Restricted OT files may be sent to the integrator only through the restricted folder's share link with an expiry date, never as an email attachment. (AC-3; PR.DS-01)

4.3 **Encryption.** Restricted information must be encrypted when stored on laptops, phones, and backup drives, and whenever it is sent outside company systems. (SC-28; SC-8; PR.DS-01; PR.DS-02)

4.4 **Inventory.** The Chief Operator keeps the OT inventory (every PLC, RTU, modem, gateway, network device, and the HMI computer, with model, firmware, network address, location, and owner), due 2026-10-31 and reviewed every quarter. The Office Manager keeps the list of SaaS services, computers, and phones. Both are updated when anything is added or removed. (CM-8; ID.AM-01)

4.5 **OT backups.** The Chief Operator, with the integrator, must export the PLC program and HMI project monthly and after every change, and keep encrypted copies on 2 offline drives: one in the plant safe and one in the Owner's office. The HMI computer must be imaged after each approved change. Each quarter the running PLC logic is compared with the offline copy. The first export is due 2026-09-15. (CP-9; PR.DS-11)

4.6 **Office backups.** The productivity suite and office desktops are backed up nightly with at least 90 days of versions. The MSP must restore a sample every quarter and give the Office Manager a written result. The first restore test is due 2026-09-30. (CP-9; CP-4; PR.DS-11)

4.7 **Drinking water records.** Compliance records are kept at the plant or the office for at least the periods in 40 CFR 141.33: microbiological and turbidity analyses 5 years; chemical analyses 10 years; records of action to correct a violation 3 years after the last action; sanitary survey reports 10 years; public notices and certifications 3 years. The daily lowest chlorine residual from the HMI historian must be printed or exported each month to the compliance file, so the record does not depend on the HMI computer. (SI-12; GV.PO-02)

4.8 **New tools and AI.** Before any new vendor, app, device, or feature receives Restricted information or connects to the WTSS, the Office Manager and Chief Operator must approve it and it must be added to the inventory. AI features follow the approved list: today it has one entry, the anomaly detection feature of the remote monitoring service, approved only as advisory under the P10 conditions. Public AI chatbots may be used only for Public information. (SA-9; PL-4; GV.SC-05)

4.9 **Printed binder.** The plant binder (runbook, contacts, customer contact list, hand-operation steps) contains Internal and Restricted pages. It stays in the locked control room, the 3 copies are numbered, and the old customer contact list is shredded when the monthly copy is printed. (AC-3; MP-6)

4.10 **Disposal.** Devices and media that held Restricted or Internal information must be wiped before reuse or destroyed by a vendor that provides a certificate. Paper customer records must be shredded so they cannot be read, as Fla. Stat. 501.171(8) requires for customer records. The Office Manager keeps each disposal record. (MP-6; ID.AM-08)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Compliance is checked through the monthly MSP report, the quarterly OT backup and restore records, and the independent assessment (P07).

## 6. Exceptions
Exceptions follow POL-02 A.9.

## 7. Related documents
POL-02; POL-03; OT inventory (due 2026-10-31); P04 cloud control map; P10 AI risk assessment; 40 CFR 141.33; Fla. Stat. 501.171
