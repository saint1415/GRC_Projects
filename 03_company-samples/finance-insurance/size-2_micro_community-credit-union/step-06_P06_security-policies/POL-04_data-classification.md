# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Community Federal Credit Union |
| Policy ID | POL-04 |
| Owner | Operations Manager (Information Security Officer and Privacy Officer) |
| Approved by | Board of Directors, 2026-08-25 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes |
| Implements (SP 800-53 Rev. 5) | RA-2, CM-3, CM-8, MP-6, SC-8, SC-28, CP-9, CP-4, SA-9, SI-12 |
| CSF 2.0 | ID.AM-01, ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11, PR.PS-01, GV.SC-06 |
| NCUA Part 748 | 748.0(b)(2), (b)(5), 748.0(c); 717.83; Appendix A II.B, III.C.1.c, III.C.1.d, III.C.1.h, III.C.4; Part 749 |

## 1. Purpose
Sort credit union information by how much harm its loss or disclosure would cause, and set simple handling rules for each level.

## 2. Scope
All workforce members and all credit union information in any form: in the core, online banking, the wire portal, the LOS, email, the imaging server, on devices, on paper, and in any vendor's system.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Operations Manager (ISO) | Owns this policy; keeps the inventory; approves new tools, vendors, and changes |
| Accounting and Compliance Officer | Owns SAR records and the vital records log |
| MSP | Encryption, backups, restore tests, and device wiping, as directed by the ISO |
| All workforce | Handle information according to its level |

## 4. Policy statements
4.1 Credit union information has three levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Member information (names with account numbers, Social Security numbers, ID copies, balances, loan files, credit reports); online banking credentials; wire instructions; the nightly offline-teller balance file; passwords, MFA codes, and wire tokens; SAR information | Only in approved systems (4.3); encrypted at rest and in transit; need-to-know only; never in personal accounts or public AI tools. SAR information is limited to the BSA Officer and the President and CEO (748.1(d)(5)) |
| **Internal** | Policies, vendor contracts, board materials, security reports, staff schedules | Workforce, board, and approved vendors only; encrypted in transit |
| **Public** | Rates, hours, website, brochures | No restriction |

When unsure, treat information as Restricted. (RA-2; ID.AM-07)

4.2 Restricted information must be encrypted wherever it is stored, on every laptop, desktop, and phone that holds it, and whenever it is sent outside credit union systems. Members must send and receive documents through the secure upload link or encrypted email, not plain email. (SC-28; SC-8; PR.DS-01; PR.DS-02; App. A III.C.1.c)

4.3 Restricted information may be kept only in: the core, online banking, the wire portal, the LOS, the imaging server, encrypted laptops, and the suite. Member documents that arrive by email must be moved to the imaging server and deleted from the mailbox within 30 days. The balance file may be kept only on the one encrypted desktop designated for offline teller mode. (AC-3; PR.DS-01)

4.4 The ISO must keep a one-page inventory of every device, every vendor service, and every place Restricted information is stored, and update it when anything is added or removed. (CM-8; ID.AM-01; ID.AM-07; App. A III.B.1)

4.5 Before any new vendor, feature, app, or device receives Restricted information, and before any change to a member information system that affects security (including vendor features switched on at the credit union's request), the ISO must approve it under POL-02 A.5 and record the approval in the MSP ticket or vendor file. (CM-3; SA-9; PR.PS-01; GV.SC-06; App. A III.C.1.d)

4.6 **AI tools.** Restricted information may be entered only into AI tools on the approved list. Today the list has one entry: the LOS vendor's AI credit scoring add-on, used only under the P10 conditions. Public or personal AI chatbots must never receive Restricted information. (SA-9; PL-4)

4.7 **Backups and vital records.** The imaging server must be backed up daily, with a copy kept at least 30 days in a separate account where it cannot be changed or deleted during that period. The MSP must restore a sample every quarter and give the ISO a written result. The Accounting and Compliance Officer keeps the vital records preservation log required by Part 749 and confirms each year that the core processor's agreement protects against losing production and backup data at the same time (749.2(b)). (CP-9; CP-4; PR.DS-11; 748.0(b)(5); App. A III.C.1.h)

4.8 **Disposal.** Devices and media that held Restricted information must be wiped before reuse, or destroyed by a vendor that provides a certificate listing serial numbers. Paper with Restricted information goes in the locked shred bin. The ISO keeps each wipe or destruction record. (MP-6; ID.AM-08; 748.0(c); 717.83; App. A III.C.4)

4.9 **Retention.** Member records follow the credit union's record retention schedule. SAR copies and supporting documents are kept 5 years from the date of the report (748.1(d)(3)). Security documentation is kept at least 5 years (POL-02 A.9). (SI-12)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Compliance is checked through the monthly MSP report (encryption and backup status), quarterly restore results, the monthly mailbox clean-up check, and the annual assessment (P07).

## 6. Exceptions
Exceptions follow POL-02 A.10.

## 7. Related documents
POL-02; POL-03; inventory of systems and member information locations; vital records preservation log; record retention schedule; P04 cloud control map; P10 AI risk assessment
