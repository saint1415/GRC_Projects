# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Office Manager (security and compliance lead) |
| Approved by | Owner and President, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-20, CM-8, MP-3, MP-6, SC-8, SC-28, CP-9, CP-4, SA-9, SI-12 |
| CSF 2.0 | ID.AM-01, ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| Federal contract requirements | FAR 52.204-21(b)(1)(iii), (vii), (b)(2) (N23-R01); DFARS 252.204-7021(d)(2) and 32 CFR 170.15(c)(2) (N23-R04) |

## 1. Purpose
Sort company information by the harm its loss or disclosure would cause, keep Federal Contract Information inside the systems that are assessed for it, and set simple handling rules for each level.

## 2. Scope
All Cris Santos Company workforce members and all company information in any form: in SaaS services, email, the shared drive, on laptops, phones, and tablets, on paper plan sets, and in any vendor's system.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Office Manager | Owns this policy; keeps the inventory and the approved-systems list; approves new tools |
| Project Manager and Estimator | Identifies FCI on federal jobs; checks incoming documents for CUI markings |
| MSP | Encryption, backup, restore tests, and device wiping, as directed by the Office Manager |
| All workforce | Handle information according to its level |

## 4. Policy statements
4.1 Company information has five levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Bank details of the company, owners, vendors, and employees; Social Security numbers and payroll; passwords and MFA codes; owners' security system layouts (camera, access control, alarm) | Only in SYS-02, SYS-03, the password manager, or the restricted shared-drive folder; never in an email body or on a pay app cover page; encrypted; named need-to-know |
| **Federal (FCI)** | Drawings, submittals, schedules, daily logs, pay apps, and certified payrolls for federal contracts | Only on the approved systems in 4.3; never in personal accounts or unapproved tools |
| **Confidential** | Bids and pricing; subcontractor quotes; private owners' drawings; contracts | Need-to-know; never shared with competitors |
| **Internal** | Schedules, safety plans, procedures | Workforce and project team only |
| **Public** | Approved website content and marketing | No restriction once approved (POL-02 B.10) |

When unsure, treat information as Restricted. (RA-2; ID.AM-07)

4.2 **Controlled unclassified information (CUI) is not accepted.** Anyone who receives a document marked CUI must stop, must not forward or upload it, and must tell the Project Manager, who quarantines it and contacts the Contracting Officer. (MP-3; FAR 52.204-21(b)(2))

4.3 **Approved systems for FCI.** FCI may be processed, stored, or transmitted only on: SYS-01, SYS-02, SYS-03, the productivity suite (SYS-04), the backup service (SYS-07), company laptops and the desktop, and company phones and tablets enrolled in device management. Personal email, personal cloud storage, and personal devices are prohibited for FCI. Automatic forwarding of company email to outside addresses is blocked. The Office Manager keeps this list and the inventory (CM-8) current. (AC-20; CM-8; FAR 52.204-21(b)(1)(iii); DFARS 252.204-7021(d)(2))

4.4 Restricted and FCI information must be encrypted at rest on every laptop, desktop, phone, and tablet, and encrypted in transit. Drawings go to subcontractors and print shops through SYS-01 or a shared-drive link, not as email attachments from personal accounts. (SC-28; SC-8; PR.DS-01; PR.DS-02)

4.5 Before any new vendor, app, or device receives Restricted, FCI, or Confidential information, the Office Manager must approve it under POL-02 A.5 and add it to the inventory. (SA-9; GV.SC-05)

4.6 **AI tools.** Restricted, FCI, and Confidential information may be entered only into AI tools on the approved list. Today the list has one entry: the AI estimating and bid assistant, for the Project Manager only, under the conditions in P10. FCI may not be uploaded to it until enterprise terms that bar training on company data are signed. Public or personal AI chatbots must never receive Restricted, FCI, or Confidential information. (AC-20; SA-9; PL-4)

4.7 **Backups.** Email and files must be backed up daily, with versions kept at least 90 days in storage that cannot be changed or deleted within that period, under an administrator login protected by MFA. The MSP must restore a sample every quarter and give the Office Manager a written result. Current drawings and pay app packages are exported from SYS-01 to the shared drive monthly. (CP-9; CP-4; PR.DS-11)

4.8 **Disposal.** Devices and media that held FCI or Restricted information must be wiped before reuse or given away, or destroyed by a vendor that provides a certificate of destruction. The storage in leased printers and plotters must be wiped before return. The Office Manager keeps each wipe or destruction record. Paper plan sets for federal jobs are shredded at closeout. (MP-6; ID.AM-08; FAR 52.204-21(b)(1)(vii))

4.9 **Retention.** Security policies, risk assessments, assessments, incident records, and CMMC self-assessment evidence are kept for 6 years (for CMMC evidence, counted from the CMMC status date; 32 CFR 170.15(c)(2)). Certified payroll records are kept 3 years after the work is completed (FAR 52.222-8(a)). A written Florida no-harm determination is kept at least 5 years (Fla. Stat. 501.171(4)(c)). (SI-12; GV.PO-02)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Compliance is checked through the monthly MSP report (encryption and backup status), quarterly restore results, and the annual assessment (P07).

## 6. Exceptions
Exceptions follow POL-02 A.10.

## 7. Related documents
POL-02; POL-03; inventory and approved-systems list; P02 boundary (section 7); P04 cloud control map; P10 AI risk assessment
