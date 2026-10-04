# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Office Manager (Security Coordinator) |
| Approved by | Owner, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes |
| Implements (SP 800-53 Rev. 5) | RA-2, CM-12, AC-3, SC-8, SC-28, CP-9, CP-4, SA-9, PL-4, MP-6, SI-12, SI-7 |
| CSF 2.0 | ID.AM-05, ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11, GV.SC-05 |
| Benchmark and law | SP 800-82 Rev. 3 section 6.2.3 (data security) and 6.2.4 (backups); Fla. Stat. 501.171(2) |

## 1. Purpose
Sort company information by how much harm its loss, change, or disclosure would cause, and set simple handling rules for each level.

## 2. Scope
All workforce members and all company information in any form: in production accounting, email, the shared drive, the SCADA host and controllers, the SCADA vendor's cloud, on computers and phones, on paper, and in any vendor's system.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Office Manager | Owns this policy; keeps the list of where Restricted data is kept; approves new tools with the Owner |
| Production Accountant | Data owner for royalty owner and production data |
| Owner | Data owner for licensed seismic data and reservoir interpretations |
| Field Superintendent | Data owner for controller programs, SCADA configuration, and field network drawings |
| MSP | Encryption, backup, restore tests, and device wiping, as directed |
| All workforce | Handle information according to its level |

## 4. Policy statements
4.1 Company information has three levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Royalty owner and employee Social Security, taxpayer, driver license, and bank account numbers; licensed seismic data and reservoir interpretations; controller programs, SCADA configuration, and field network drawings; passwords and MFA codes | Approved systems only (4.3); encrypted at rest and in transit where technically feasible; named people only; never in personal accounts or public AI tools |
| **Internal** | Production volumes, run tickets, contracts, partner statements, security documents, schedules | Workforce, partners, and approved vendors only; encrypted in transit |
| **Public** | Published permits, company contact details | No restriction |

When unsure, treat information as Restricted. (RA-2; ID.AM-05)

4.2 Restricted information must be encrypted wherever it is stored on a computer, laptop, or phone, and whenever it leaves the company's systems. Email containing Restricted information must use the suite's encrypted send. Where an OT device or protocol cannot encrypt (radio polling), the exception is recorded with its compensating controls under POL-02 A.9. (SC-28; SC-8; PR.DS-01; PR.DS-02; Fla. Stat. 501.171(2))

4.3 Restricted information may be kept only in: production accounting, the payroll service, the suite (restricted folders only), the cloud backup, the SCADA host and the rotated backup drives, and the Owner's encrypted laptop. Royalty owner exports must not be saved to laptops for longer than the task needs, and are deleted at the monthly close. The Geology folder is limited to the Owner and the named users in the seismic license. (AC-3; PR.DS-01)

4.4 The Office Manager must keep a one-page list of every place Restricted information is kept and every vendor that receives it, and update it when anything changes. (CM-12; ID.AM-07)

4.5 Before any new vendor, app, or cloud feature receives Restricted information or connects to the SCADA host, the Office Manager and the Owner must approve it under POL-02 A.5 and add it to the list. (SA-9; GV.SC-05)

4.6 **AI tools.** Restricted information may be entered only into AI tools on the approved list. Today the list has one entry: the SCADA vendor's predictive maintenance add-on, for pump-off controller data only, in advisory mode, under the P10 conditions. Public or personal AI chatbots must never receive Restricted information. (SA-9; PL-4)

4.7 **Bank detail changes.** No royalty owner, partner, employee, or vendor bank account may be added or changed from an email, text, or phone request alone. The Production Accountant (or the Office Manager for vendors and payroll) must call the person back on the number already on file, record the call, and have the Owner review a monthly report of changed bank details before the next ACH batch. (SI-7; PR.DS-10)

4.8 **Disposal.** Computers, phones, drives, and controllers that held Restricted information must be wiped before reuse or destroyed with a certificate of destruction. Paper with Restricted information is shredded. The Office Manager keeps each wipe or destruction record. (MP-6; ID.AM-08)

4.9 **Backups.** Office computers and the shared drive are backed up nightly with versions kept at least 90 days in storage that cannot be changed or deleted within that period. The SCADA host is backed up weekly to two encrypted drives used in rotation, one always kept at the main office, and to the immutable cloud backup once added. Current controller programs are copied to the restricted Field folder after every change. The MSP and the Field Technician each restore a sample every quarter and give the Office Manager a written result. (CP-9; CP-4; PR.DS-11)

4.10 **Retention.** Royalty, production, and tax records follow the company's records retention schedule. Security records are kept as POL-02 A.7 requires. (SI-12)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Compliance is checked through the monthly MSP report, quarterly restore results, the monthly bank detail change report, and the annual assessment (P07).

## 6. Exceptions
Exceptions follow POL-02 A.9.

## 7. Related documents
POL-02; POL-03; list of Restricted data locations; seismic data license; P04 cloud control map; P10 AI risk assessment; records retention schedule
