# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Office Manager (Privacy Officer and Security Officer) |
| Approved by | Owner, 2026-09-04 |
| Effective date | 2026-09-08 |
| Review cycle | Annually (next review 2027-08-31), and after major changes |
| Implements (SP 800-53 Rev. 5) | RA-2, CM-8, MP-6, SC-8, SC-28, CP-9, CP-4, SA-9, SI-12 |
| CSF 2.0 | ID.AM-01, ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11, GV.PO-02 |
| HIPAA Security Rule (C-EMERGENCY-R04) | 164.308(a)(7)(ii)(A), (D); 164.310(d); 164.312(a)(2)(iv), (e) |
| Other records rules | 42 CFR 410.40(e) and 424.516(f) (Medicare documentation); Fla. Stat. 401.30; Rule 64J-1.014, F.A.C. (EMS records) |

## 1. Purpose
Sort company information by how much harm its loss or disclosure would cause, and set simple handling and retention rules for each level.

## 2. Scope
All workforce members of Cris Santos Company and all company information in any form: in the operations platform, email, the shared drive, the phone system (recordings and faxes), on devices in the office and the ambulances, on paper, and in any vendor's system.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Office Manager | Owns this policy; keeps the device and ePHI inventory; approves new tools; keeps the retention schedule |
| MSP | Encryption, backup, restore tests, and device wiping, as directed by the Office Manager |
| All workforce | Handle information according to its level |

## 4. Policy statements
4.1 Company information has three levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Anything about a patient: trip requests, face sheets, certification statements, patient care reports, call recordings and transcripts, insurance numbers; Social Security numbers; passwords and MFA codes | Only in approved systems (4.3); encrypted at rest and in transit; minimum necessary; never in personal accounts, personal phones, or public AI tools |
| **Internal** | Payroll and HR files, certifications, contracts, BAAs, security documents, crew schedules, vehicle records | Workforce and approved vendors only; encrypted in transit |
| **Public** | Service area, phone number, website, brochures | No restriction |

When unsure, treat information as Restricted. (RA-2; ID.AM-07)

4.2 Restricted information must be encrypted wherever it is stored, on every computer, tablet, and phone that holds it, and whenever it is sent outside the company's systems. Email with Restricted information to anyone outside the company, including facilities, must use the suite's encryption option. (SC-28; SC-8; PR.DS-01; PR.DS-02; 164.312(a)(2)(iv); 164.312(e)(2)(ii))

4.3 Restricted information may be kept only in: the operations platform, the productivity suite (email, shared drive, shared fax mailbox), the phone system (recordings and faxes, under its BAA), the billing company's systems, the backup service, the company's tablets and phones, and the locked paper file in the office. (AC-3; 164.310(d))

4.4 The Office Manager must keep a one-page inventory of every device (including the vehicle hotspots and trackers), every SaaS service, and every place Restricted information is stored, and update it when anything is added or removed. (CM-8; ID.AM-01; ID.AM-07; 164.310(d)(2)(iii))

4.5 Before any new vendor, app, device, or feature of an existing service receives Restricted information, the Office Manager must approve it, a BAA covering it must be in place (POL-02 A.5), and it must be added to the inventory. (SA-9; GV.SC-05)

4.6 **AI tools.** Restricted information may be entered only into AI tools on the approved list. Today the approved list has one entry: the AI intake assistant in the operations platform, for the Scheduler-Dispatcher only, and only while the P10 conditions are met. Public or personal AI chatbots must never receive Restricted information. (SA-9; PL-4)

4.7 **Backups.** Suite mailboxes and the shared drive must be backed up nightly, with versions kept at least 90 days in storage that cannot be changed or deleted within that period, and the backup console must require MFA. The MSP must restore a sample every quarter and give the Office Manager a written result. (CP-9; CP-4; PR.DS-11; 164.308(a)(7)(ii)(A), (D))

4.8 **Disposal.** Devices and media that held Restricted information must be wiped before reuse, or destroyed by a vendor that provides a certificate of destruction. Paper with Restricted information, including run sheets and paper patient care reports once entered, goes in the locked shred bin. The Office Manager keeps each wipe or destruction record. (MP-6; ID.AM-08; 164.310(d)(2)(i)-(ii))

4.9 **Retention schedule.** (SI-12; GV.PO-02)

| Record | Where | Keep for | Basis |
|---|---|---|---|
| Patient care reports and records of each call | Operations platform | At least 7 years from the date of service | Rule 64J-1.014, F.A.C. (at least 5 years); 42 CFR 424.516(f) (7 years for documentation supporting Medicare claims) |
| Certification statements (PCS) and supporting trip documentation | Attached to the trip in the platform before release to billing; paper originals scanned, then shredded | 7 years from the date of service | 42 CFR 410.40(e); 424.516(f) |
| Call recordings | Phone system | 2 years, unless held for an incident, complaint, or legal hold | Company decision |
| Security documentation | Security folder in the shared drive | 6 years | POL-02 A.7; 164.316(b)(2)(i) |

4.10 **Records to hospitals.** A copy of the patient care report must be available to the receiving hospital through the platform's hospital portal, or on paper during an outage, and on request within 48 hours of dispatch (Fla. Stat. 401.30(2); Rule 64J-1.014, F.A.C.). Patient care records may be disclosed without consent only as Fla. Stat. 401.30(4) and the HIPAA Privacy Rule allow; requests from anyone else go to the Office Manager.

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Compliance is checked through the monthly MSP report (encryption and backup status), quarterly restore results, a quarterly sample of 10 trips for an attached PCS, and the annual assessment (P07).

## 6. Exceptions
Exceptions follow POL-02 A.9.

## 7. Related documents
POL-02; POL-03; device and ePHI inventory; retention schedule; P04 cloud control map; P10 AI risk assessment
