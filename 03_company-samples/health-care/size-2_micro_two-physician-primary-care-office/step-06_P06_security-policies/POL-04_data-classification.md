# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Office Manager (Privacy Officer and Security Officer) |
| Approved by | Owner physician, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes |
| Implements (SP 800-53 Rev. 5) | RA-2, CM-8, MP-6, SC-8, SC-28, CP-9, CP-4, SA-9, SI-12 |
| CSF 2.0 | ID.AM-01, ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| HIPAA Security Rule | 164.308(a)(7)(ii)(A), (D); 164.310(d); 164.312(a)(2)(iv), (e) |

## 1. Purpose
Sort practice information by how much harm its loss or disclosure would cause, and set simple handling rules for each level.

## 2. Scope
All workforce members of Cris Santos Company and all practice information in any form: in the EHR, email, the shared drive, the fax portal, on devices, on paper, and in any vendor's system.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Office Manager | Owns this policy; keeps the device and ePHI inventory; approves new tools |
| MSP | Encryption, backup, restore tests, and device wiping, as directed by the Office Manager |
| All workforce | Handle information according to its level |

## 4. Policy statements
4.1 Practice information has three levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Anything about a patient (ePHI and paper PHI), ECG and spirometry results, insurance numbers, Social Security numbers, passwords and MFA codes | Only in approved systems (4.3); encrypted at rest and in transit; minimum necessary; never in personal accounts or public AI tools |
| **Internal** | Payroll and HR files, contracts, BAAs, security documents, schedules without patient details | Workforce and approved vendors only; encrypted in transit |
| **Public** | Office hours, website, brochures | No restriction |

When unsure, treat information as Restricted. (RA-2; ID.AM-07)

4.2 Restricted information must be encrypted wherever it is stored, on every laptop, desktop, tablet, and phone that holds it, and whenever it is sent outside the practice's systems. Email to anyone outside the practice that contains Restricted information must be encrypted end to end. (SC-28; SC-8; PR.DS-01; PR.DS-02; 164.312(a)(2)(iv); 164.312(e)(2)(ii))

4.3 Restricted information may be kept only in: the EHR, the productivity suite (email and the shared drive, under its BAA), the cloud fax portal, the backup service, and, for no longer than one week, the procedure-room workstation before results are imported into the EHR. (AC-3; 164.310(d))

4.4 The Office Manager must keep a one-page inventory of every device, every SaaS service, and every place Restricted information is stored, and update it when anything is added or removed. (CM-8; ID.AM-01; ID.AM-07; 164.310(d)(2)(iii))

4.5 Before any new vendor, app, or device receives Restricted information, the Office Manager must approve it, a BAA must be in place (POL-02 A.5), and it must be added to the inventory. (SA-9; GV.SC-05)

4.6 **AI tools.** Restricted information may be entered only into AI tools on the approved list. Today the approved list has one entry: the AI scribe, for the enrolled pilot physician only, and only after its BAA is signed and the P10 conditions are met. Public or personal AI chatbots must never receive Restricted information. (SA-9; PL-4)

4.7 **Backups.** The shared drive must be backed up nightly, with versions kept at least 90 days in storage that cannot be changed or deleted within that period. The MSP must restore a sample every quarter and give the Office Manager a written result. (CP-9; CP-4; PR.DS-11; 164.308(a)(7)(ii)(A), (D))

4.8 **Disposal.** Devices and media that held Restricted information must be wiped before reuse, or destroyed by a vendor that provides a certificate of destruction. Paper with Restricted information goes in the locked shred bin. The Office Manager keeps each wipe or destruction record. (MP-6; ID.AM-08; 164.310(d)(2)(i)-(ii))

4.9 **Retention.** Medical records follow the practice's medical records retention schedule. Security documentation is kept for 6 years (POL-02 A.7). (SI-12)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Compliance is checked through the monthly MSP report (encryption and backup status), quarterly restore results, and the annual assessment (P07).

## 6. Exceptions
Exceptions follow POL-02 A.9.

## 7. Related documents
POL-02; POL-03; device and ePHI inventory; P04 cloud control map; P10 AI risk assessment; medical records retention schedule
