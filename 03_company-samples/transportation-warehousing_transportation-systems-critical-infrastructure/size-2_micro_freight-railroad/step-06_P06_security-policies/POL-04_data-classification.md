# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Office Manager (Security Lead); SSI rules owned by the Owner and General Manager (Security Coordinator) |
| Approved by | Owner and General Manager, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-3, MP-3, MP-4, MP-6, CM-8, SC-8, SC-28, CP-9, CP-4, SA-9, SI-12 |
| CSF 2.0 | ID.AM-01, ID.AM-02, ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| Regulatory drivers | C-TRANSPORTATION-S03 (49 CFR 1520.9); C-TRANSPORTATION-S06 (172.802(c)); C-TRANSPORTATION-S07 (Fla. Stat. 501.171); C-TRANSPORTATION-BM |

## 1. Purpose
Sort company information by how much harm its loss, change, or disclosure would cause, and set simple handling rules for each level, including the federal rules for Sensitive Security Information (SSI).

## 2. Scope
All employees and all company information in any form: in the operations system, email, the shared drive, the telematics and payroll systems, on devices, on paper, and in any vendor's system.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Office Manager | Owns this policy; keeps the inventory; approves new tools |
| Owner and General Manager | Owns the SSI rules and the hazmat security plan; decides who has a need to know |
| MSP | Encryption, backup, restore tests, and device wiping, as directed by the Office Manager |
| All employees | Handle information according to its level |

## 4. Policy statements
4.1 Company information has three levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | SSI; the hazmat security plan; employee personal information, certification, and drug and alcohol testing records; passwords and MFA codes; network diagrams and system configurations | Only in approved locations (4.4); need to know; encrypted at rest and in transit; never in personal accounts or public AI tools |
| **Internal** | Train sheets and authority records, car inventory, waybills, customer contracts and rates, the timetable and special instructions, track charts, inspection records, track imagery | Employees, the connecting Class I where needed, and approved vendors only; encrypted in transit |
| **Public** | Published service information, the company's public contact details | No restriction |

When unsure, treat information as Restricted. (RA-2; ID.AM-07)

4.2 **SSI.** SSI is any record TSA marks as SSI, and any company record that repeats its content.
- Only the Security Coordinators and people they authorize with a need to know may access SSI. Requests from anyone else go to TSA. (49 CFR 1520.9(a)(2)-(3))
- Electronic SSI is kept only in the restricted SSI folder. Paper SSI is kept in the locked cabinet in the General Manager's office when not in use. (1520.9(a)(1))
- Unmarked SSI is marked on receipt and the sender is told. Company records that repeat SSI content carry the same marking. (1520.9(a)(4), (b))
- SSI paper is shredded; electronic SSI is deleted from the folder and from any device it was synced to. (1520.9(a)(5))
- SSI is never emailed outside the company except to TSA or another covered person with a need to know.
- Any release of SSI to someone without a need to know is reported under POL-03 4.5. (1520.9(c))
(AC-3; MP-3; MP-4; MP-6)

4.3 Restricted information must be encrypted wherever it is stored, on every laptop, desktop, tablet, and phone that holds it, and whenever it is sent outside company systems. (SC-28; SC-8; PR.DS-01; PR.DS-02)

4.4 Restricted information may be kept only in: the restricted folders of the productivity suite (SSI and security plan; employee files), the payroll system, the operations system administrator settings, the backup service, and the General Manager's locked cabinet. The hazmat security plan is available to the employees who carry it out, limited to the parts they need (49 CFR 172.802(c)). (AC-3)

4.5 The Office Manager must keep a one-page inventory of every device, radio component, telematics unit, SaaS service and account, and every place Restricted information is stored, and update it when anything changes. (CM-8; ID.AM-01; ID.AM-02)

4.6 Before any new vendor, app, or device receives Restricted or Internal information, the Office Manager must approve it under POL-02 A.5 and add it to the inventory. (SA-9; GV.SC-05)

4.7 **AI tools.** Company information may be entered only into AI tools on the approved list kept by the Office Manager. Today the list has one entry: the track defect detection service (AI-001), for the hi-rail truck camera only, under the conditions in P10. Public or personal AI chatbots must never receive Restricted information. (SA-9; PL-4)

4.8 **Backups.** The productivity suite must be backed up nightly, with versions kept at least 90 days in storage that cannot be changed or deleted within that period. The Office Manager exports car inventory and authority history from the operations system every week to the suite. The MSP must restore a sample every quarter and give the Office Manager a written result. (CP-9; CP-4; PR.DS-11)

4.9 **Disposal.** Devices and media that held Restricted information must be wiped before reuse, or destroyed by a vendor that provides a certificate of destruction. The Office Manager keeps each record. (MP-6; ID.AM-08)

4.10 **Retention.** Authority records and train sheets follow the operations system's retention settings; hazmat records and security documents follow POL-02 A.7. (SI-12)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Compliance is checked through the monthly MSP report (encryption and backup status), quarterly restore results, the quarterly access review of the restricted folders, and the annual assessment (P07).

## 6. Exceptions
Exceptions follow POL-02 A.9. No exception may widen access to SSI.

## 7. Related documents
POL-02; POL-03; inventory; hazmat security plan; P04 cloud control map; P10 AI risk assessment
