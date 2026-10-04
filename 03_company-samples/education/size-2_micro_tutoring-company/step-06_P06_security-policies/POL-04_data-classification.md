# Data Classification, Handling, and Retention Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Center Director (Information Security Coordinator) |
| Approved by | Owner, 2026-08-28 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after material changes |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-3, CM-8, SC-8, SC-28, SA-9, PL-4, CP-9, CP-4, MP-6, SI-12, AC-3(14), SI-18(4), PT-4, PT-5 |
| CSF 2.0 | ID.AM-01, ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11, GV.SC-05, GV.OC-03 |
| COPPA Rule | 16 CFR 312.4, 312.5, 312.6, 312.8(b)(3), 312.8(c), 312.10 |
| Other | Fla. Stat. 501.171(8) (disposal); district data privacy agreement (deletion) |

## 1. Purpose
Sort company information by how much harm its loss or disclosure would cause, set simple handling rules for each level, and set how long each kind of student information is kept. Section 4.9 is the company's **written data retention policy** under 16 CFR 312.10.

## 2. Scope
All workforce members of Cris Santos Company, including contractor tutors, and all company information in any form: in the tutoring platform, the scheduling platform, the suite, the backup, on devices, on paper, and in any vendor's system.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Center Director | Owns this policy; keeps the inventory; approves new tools; handles parent requests; runs the yearly purge |
| Director of Tutoring | Platform retention settings, exports, and the AI module settings |
| MSP | Encryption, backup, restore tests, and device wiping, as directed |
| All workforce | Handle information according to its level |

## 4. Policy statements
4.1 Company information has three levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Anything about a student: names with grades or schools, work samples, session notes and recordings, assessment results, messages, evaluation reports, IEP or 504 plan excerpts, district roster data; parents' contact and payment details; passwords and MFA codes | Only in approved systems (4.3); encrypted at rest and in transit; only for students you work with; never in personal accounts or public AI tools |
| **Internal** | Staff and contractor files, contracts, vendor terms, security documents, schedules without student details | Workforce and approved vendors only; encrypted in transit |
| **Public** | Website, brochures, opening hours | No restriction |

When unsure, treat information as Restricted. (RA-2; ID.AM-07)

4.2 Restricted information must be encrypted wherever it is stored, on every company laptop, desktop, and phone that holds it, and whenever it is sent outside the company's systems. Progress reports and documents go to parents through the parent portal, not as email attachments. (SC-28; SC-8; PR.DS-01; PR.DS-02)

4.3 Restricted information may be kept only in: the tutoring platform; the scheduling platform; the suite (email and the "Student files" folder, which is limited under POL-02 B.2); and the backup service. Contractor tutors may view student information only in the platform (POL-02 B.9). District roster data is loaded into the platform and not kept elsewhere. (AC-3; PR.DS-01; district DPA)

4.4 The Center Director must keep a one-page inventory of every device, every SaaS service, and every place Restricted information is stored, and update it when anything is added or removed. (CM-8; ID.AM-01; ID.AM-07; 312.8(b)(2))

4.5 Before any new vendor, app, feature, or device receives Restricted information, the Center Director must approve it, the vendor's written security commitment must be on file (POL-02 A.6), and it must be added to the inventory. Disclosures that are not needed to provide tutoring (for example, to advertise or to train a vendor's AI models) need separate parental consent and are not made today. (SA-9; GV.SC-05; 312.5(a)(2); 312.8(c))

4.6 **AI tools.** Restricted information may be entered only into AI tools on the approved list. Today the list is empty: the tutoring platform's AI progress insights module is turned off until the P10 conditions are met. Public or personal AI chatbots must never receive Restricted information; tutors may use them to make generic worksheets with no student details. (SA-9; PL-4)

4.7 **Backups and exports.** Suite email and the shared drive must be backed up nightly, with versions kept at least 90 days in storage that cannot be changed or deleted within that period. The MSP must restore a sample every quarter and give the Center Director a written result. The Director of Tutoring exports students' progress data from the platform monthly, and the Enrollment and Billing Coordinator prints the next week's schedule every Friday. (CP-9; CP-4; PR.DS-11)

4.8 **Disposal.** Devices and media that held Restricted information must be wiped before reuse or destroyed by a vendor that provides a certificate. Paper with Restricted information goes in the locked shred bin. The Center Director keeps each wipe, destruction, and purge record. (MP-6; ID.AM-08; Fla. Stat. 501.171(8))

4.9 **Retention schedule (written data retention policy, 16 CFR 312.10).** Children's information is collected only to provide tutoring, report progress to parents (and, for program students, to the district), bill for services, and keep students safe. It is kept only as long as those purposes need it, then deleted in a way that protects it during deletion:

| Information | Business need | Deleted |
|---|---|---|
| Online session recordings | Review a session after a parent question or a safety concern | 90 days after the session |
| Tutor-student messages | Continuity and safety review | 1 year after the message |
| Student record in the platform (profile, work samples, notes, assessments, progress reports) | Continuity if the student returns; answering parents' questions | 2 years after the student's last session |
| Trial or prospective student data without parental consent | None | Not created (POL-04 4.11); any found is deleted at once |
| District program data | District contract | Within 60 days after the contract ends, with a deletion certificate to the district |
| Intake forms, evaluation reports, IEP or 504 excerpts in the "Student files" folder | Accommodations during tutoring | 90 days after the student's last session |
| Family account and invoices in the scheduling platform | Billing, tax, and dispute records | 5 years after the last invoice; the child's details are removed 2 years after the last session |
| Backup copies | Recovery | Expire with the 90-day versioning cycle |

The Center Director runs a purge every November and records what was deleted. This schedule is published in the online privacy notice. (SI-12; SI-12(3); ID.AM-08; 312.10)

4.10 **Parent requests.** A parent may ask to see what the company holds about their child, to stop further collection, or to have it deleted. Before acting, the Center Director must confirm the requester is the child's parent through the parent portal sign-in or a call-back to the phone number on file. Deletion covers the platform, the scheduling platform, and the suite; backup copies expire under 4.9. Every request and its outcome are logged. (AC-3(14); SI-18(4); 312.6)

4.11 **Notice and consent before collection.** No platform account may be created for a child, and no child's information may be collected, until the parent has received the direct notice and given verifiable consent (or, for district program students, the district's written authorization covers the student). Any material change to what is collected or shared needs a new notice and, where required, new consent. (PT-4; PT-5; 312.4; 312.5)

## 5. Compliance and enforcement
Breaking this policy leads to consequences under POL-02 A.5. Compliance is checked through the monthly MSP report (encryption and backup status), quarterly restore results, the November purge record, the parent request log, and the annual assessment (P07).

## 6. Exceptions
Exceptions follow POL-02 A.9. No exception may extend retention of children's information beyond 4.9 without the Owner's written approval and a stated business need.

## 7. Related documents
POL-02; POL-03; inventory; online privacy notice and direct notice; P04 cloud control map; P10 AI risk assessment; district data privacy agreement
