# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent community pharmacy) |
| Policy ID | POL-04 |
| Owner | Store Manager (Privacy Officer and Security Officer) |
| Approved by | Pharmacist-owner, 2026-08-28 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes |
| Implements (SP 800-53 Rev. 5) | RA-2, CM-8, MP-6, SC-8, SC-28, CP-9, CP-4, SA-9, SI-12, PL-4 |
| CSF 2.0 | ID.AM-01, ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11, GV.SC-05 |
| HIPAA Security Rule | 164.308(a)(7)(ii)(A), (D); 164.310(d); 164.312(a)(2)(iv), (e) |

## 1. Purpose
Sort pharmacy information by how much harm its loss, change, or disclosure would cause, and set simple handling rules for each level.

## 2. Scope
All workforce members of Cris Santos Company and all pharmacy information in any form: in the PMS, email, the shared drive, the fax portal, the packaging workstation, the delivery app, on devices, on paper (labels, bag receipts, delivery slips, downtime logs), and in any vendor's system.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Store Manager | Owns this policy; keeps the device and ePHI inventory; approves new tools |
| Pharmacist-owner | Approves AI tools and any change to where controlled substance records are kept |
| MSP | Encryption, backup, restore tests, and device wiping, as directed by the Store Manager |
| All workforce | Handle information according to its level |

## 4. Policy statements
4.1 Pharmacy information has three levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Anything about a patient (ePHI and paper PHI): profiles, prescriptions, allergies, ALF medication lists and order sheets, packaging schedules, delivery routes and signatures, insurance and PBM identifiers; controlled substance records and inventory spreadsheets; the CSOS certificate; passwords and MFA codes | Only in approved systems (4.3); encrypted at rest and in transit; minimum necessary; never in personal accounts, unapproved apps, or public AI tools |
| **Internal** | Payroll and HR files, contracts, BAAs, wholesaler invoices, PBM contracts, security documents, schedules without patient details | Workforce and approved vendors only; encrypted in transit |
| **Public** | Store hours, delivery area, front-store prices, website | No restriction |

When unsure, treat information as Restricted. (RA-2; ID.AM-07)

4.2 Restricted information must be encrypted wherever it is stored, on every laptop, desktop, and phone that holds it, and whenever it is sent outside the pharmacy's systems. Email to anyone outside the pharmacy that contains Restricted information, including the ALFs, must be encrypted end to end; the suite's automatic encryption rule does this once enabled. (SC-28; SC-8; PR.DS-01; PR.DS-02; 164.312(a)(2)(iv); 164.312(e)(2)(ii))

4.3 Restricted information may be kept only in: the PMS, the productivity suite (email and the shared drive, under its BAA), the cloud fax portal, the backup service, the packaging workstation (current pack orders only), and the delivery app (once under a BAA, and for no more than 90 days). Downloaded faxes and reports must be deleted from computer download folders each week. Monthly delivery log exports are not kept in the shared drive beyond the current year. (AC-3; 164.310(d))

4.4 The Store Manager must keep a one-page inventory of every device, every SaaS service, and every place Restricted information is stored, and update it when anything is added or removed. (CM-8; ID.AM-01; ID.AM-07; 164.310(d)(2)(iii))

4.5 Before any new vendor, app, or device receives Restricted information, the Store Manager must approve it, a BAA must be in place (POL-02 A.5), and it must be added to the inventory. (SA-9; GV.SC-05)

4.6 **AI tools.** Restricted information may be entered only into AI tools on the approved list, which the pharmacist-owner approves after a P10 assessment. Today the approved list has one entry: the PMS controlled substance risk score (SYS-09), for pharmacist use only, under the conditions in P10 section 6. Any new AI or decision support feature the PMS vendor switches on must be reported to the Store Manager and reviewed before staff rely on it. Public or personal AI chatbots must never receive Restricted information. (SA-9; PL-4; GV.SC-05)

4.7 **Backups.** The shared drive, the back-office desktop, and the packaging workstation must be backed up nightly, with versions kept at least 90 days in storage that cannot be changed or deleted within that period. The MSP must restore a sample every quarter and give the Store Manager a written result. (CP-9; CP-4; PR.DS-11; 164.308(a)(7)(ii)(A), (D))

4.8 **Disposal.** Devices and media that held Restricted information must be wiped before reuse, or destroyed by a vendor that provides a certificate of destruction. Paper with Restricted information (labels, bag receipts, delivery slips, downtime logs after back-entry) goes in the locked shred bin. The Store Manager keeps each wipe or destruction record. (MP-6; ID.AM-08; 164.310(d)(2)(i)-(ii))

4.9 **Retention.** Prescription and controlled substance records follow the federal and Florida retention rules (at least 2 years for controlled substance records, 21 CFR 1311.305(b) and Fla. Stat. 893.07(4)); the PMS keeps all records for the life of the contract. Security documentation is kept for 6 years (POL-02 A.7). (SI-12)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Compliance is checked through the monthly MSP report (encryption and backup status), quarterly restore results, and the annual assessment (P07).

## 6. Exceptions
Exceptions follow POL-02 A.9.

## 7. Related documents
POL-02; POL-03; device and ePHI inventory; P04 cloud control map; P10 AI risk assessment
