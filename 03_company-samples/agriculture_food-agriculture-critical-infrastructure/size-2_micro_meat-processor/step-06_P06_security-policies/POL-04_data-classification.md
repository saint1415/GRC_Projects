# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Office Manager (security and compliance lead) |
| Approved by | Owner and General Manager, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes |
| Implements (SP 800-53 Rev. 5) | RA-2, CM-8, CM-2, MP-6, SC-8, CP-9, CP-4, AU-9, AU-11, SA-9, PL-4 |
| CSF 2.0 | ID.AM-01, ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11 |
| FSIS rules supported | 9 CFR 416.16(b)-(c); 417.5(d)-(f); 418.3 |

## 1. Purpose
Sort company information by how much harm its loss, change, or disclosure would cause, and set simple handling rules for each level. In a meat plant, **integrity** matters as much as secrecy: a changed cook cycle or label can hurt consumers.

## 2. Scope
Everyone working for the company and all company information in any form: in SaaS services, on PCs and tablets, in machine controllers, on paper, and in any vendor's system.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Office Manager | Owns this policy; keeps the inventory; approves new tools and vendors |
| Production Supervisor | Owns food safety settings and records; keeps approved copies of cycles, formulations, and label templates |
| MSP | Encryption, backup, restore tests, and device wiping on the PCs, as directed by the Office Manager |
| Everyone | Handle information according to its level |

## 4. Policy statements
4.1 Company information has three levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Food safety settings (cook cycles, formulations, label templates and allergen statements); CCP and SSOP records; HACCP plans; employee personal information (Social Security numbers, bank details); passwords, PINs, and MFA codes | Only in approved systems (4.3); changes only under POL-02 B.10; integrity protected (4.5); never in personal accounts or public AI tools |
| **Internal** | Customer and price lists, orders and invoices, supplier contracts, security documents, the recall procedure | Employees and approved vendors only; encrypted in transit |
| **Public** | Product list, retail hours, brochures | No restriction |

When unsure, treat information as Restricted. (RA-2; ID.AM-07)

4.2 Restricted and Internal information must be encrypted in transit whenever it leaves the plant (all approved SaaS services use encrypted connections). Laptops and phones that hold company email must be encrypted and locked. (SC-8; PR.DS-02)

4.3 Restricted information may be kept only in: the records app, the productivity suite folders restricted to the owner, Office Manager, and Production Supervisor, the accounting and payroll services, the labeling PC, the machine controllers that use it, the cloud backup, and the locked office binder. HACCP plans and formulations must not sit in folders open to all accounts. (AC-3; PR.DS-01)

4.4 The Office Manager must keep a one-page inventory of every device, machine controller, SaaS service, remote access path, and place where Restricted information is stored, and update it whenever anything is added or removed. (CM-8; ID.AM-01; ID.AM-07)

4.5 **Integrity of food safety records and settings.** Electronic CCP and SSOP records must be made under named accounts, corrected only by a new entry that keeps the original visible, and never deleted. Cook logs leave the smokehouse controller only as read-only exports (PDF with a file hash) attached to the batch record. The Production Supervisor keeps an offline copy of every approved cook cycle, formulation, line setting, and label template, and compares the machines with it every month. (AU-9; SI-7; CM-2; PR.DS-10; 9 CFR 417.5(d); 416.16(b))

4.6 **AI tools.** Restricted information may be entered only into AI tools on the approved list. Today the approved list has one entry: the AI label and seal camera on Line 2, under the P10 conditions. Public or personal AI chatbots must never receive Restricted information. (SA-9; PL-4)

4.7 **Backups.** The office desktop, labeling PC, and productivity suite must be backed up nightly, with versions kept at least 90 days in storage that cannot be changed or deleted within that period. The MSP must restore a sample every quarter, including cook-log exports, and give the Office Manager a written result. Machine settings are copied after every approved change (4.5). (CP-9; CP-4; PR.DS-11)

4.8 **Retention.** Cook-log exports and other CCP records for shelf-stable product (jerky, snack sticks) are kept at least 3 years, which covers the 2-year FSIS minimum (9 CFR 417.5(e)(1)) with margin; records for refrigerated product at least 1 year; SSOP records at least 6 months (416.16(c)). Lot and customer data needed for the recall procedure are exported monthly to the restricted folder. (AU-11; SI-12; 9 CFR 418.3)

4.9 **New tools and vendors.** Before any new vendor, app, or device receives Restricted information or connects to a plant machine, the Office Manager must approve it and add it to the inventory and vendor list (POL-02 A.5). (SA-9; GV.SC-05)

4.10 **Disposal.** Devices, machine controllers, and media that held Restricted information must be wiped or destroyed before they leave the company, with a record kept. This includes controllers and HMIs removed during machine upgrades. (MP-6; ID.AM-08)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Compliance is checked through the monthly comparison of machine settings, the monthly MSP report, quarterly restore results, and the annual assessment (P07).

## 6. Exceptions
Exceptions follow POL-02 A.9.

## 7. Related documents
POL-02; POL-03; inventory; change log; HACCP plans and recall procedure; P04 cloud control map; P10 AI risk assessment
