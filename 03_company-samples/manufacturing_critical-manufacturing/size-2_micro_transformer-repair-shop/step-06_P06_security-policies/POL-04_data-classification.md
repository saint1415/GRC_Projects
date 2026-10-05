# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Office Manager (Security Coordinator) |
| Approved by | Owner, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes |
| Implements (SP 800-53 Rev. 5) | RA-2, CM-8, CM-12, MP-6, MP-7, SC-8, SC-28, CP-9, CP-4, SA-9, AC-22, SI-3, SI-12 |
| CSF 2.0 | ID.AM-01, ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11, RC.RP-03 |
| Binding duties carried | FAR 52.204-21(b)(1)(iv), (vii), (xv); Fla. Stat. 501.171(2), (8); confidentiality terms in customer agreements |

## 1. Purpose
Sort company and customer information by how much harm its loss or disclosure would cause, set simple handling rules for each level, and make sure the information the shop needs to keep working can be restored.

## 2. Scope
All employees and all company and customer information in any form: in the ERP, email, the shared drive, the AI portal, on computers, tablets, USB sticks, the test PC, the shop equipment, and paper.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Office Manager | Owns this policy; keeps the inventory; approves new tools and vendors |
| Shop Manager | Keeps copies of shop equipment programs and recipes; owns test data |
| MSP | Encryption, backups, restore tests, and device wiping, as directed by the Office Manager |
| All employees | Handle information according to its level |

## 4. Policy statements
4.1 Company information has three levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | The rewind data sheet library; federal contract information (FCI); customer substation and site details and anything a customer marks confidential; employee personal information (HR and payroll); bank details; passwords and MFA codes | Only in approved locations (4.3); encrypted at rest and in transit; only people who need it; never in personal accounts or public AI tools |
| **Internal** | Test reports, quotes and pricing, job records, supplier lists, security documents | Employees and approved vendors only; shared outside the shop only for a business need |
| **Public** | Website, brochures, published price sheets | No restriction |

When unsure, treat information as Restricted. (RA-2; ID.AM-07)

4.2 Restricted information must be encrypted on every laptop, desktop, tablet, and test PC that stores it, and whenever it is sent outside the shop's systems. (SC-28; SC-8; PR.DS-01; PR.DS-02; Fla. Stat. 501.171(2))

4.3 Restricted information may be kept only in: the ERP, the suite (email and the shared drive), the suite backup, and the AI portal (customer transformer data only, and only under the conditions in 4.7). (CM-12; ID.AM-07)

4.4 The Office Manager must keep a one-page inventory of every device (including the test PC, oven controls, winding machine, camera recorder, and network equipment), every SaaS service and vendor with access, and every place Restricted information is stored, and update it when anything is added or removed. (CM-8; ID.AM-01)

4.5 Before any new vendor, app, or device receives Restricted information or connects to a shop network, the Office Manager must approve it, check it for covered telecommunications or video surveillance equipment (FAR 52.204-25), put written terms in place (POL-02 A.5), and add it to the inventory. (SA-9; GV.SC-05)

4.6 **Federal contract information.** FCI is kept only in the federal order folder in the shared drive and in the ERP job record, labeled "FCI," and shared only with named staff and the agency. Anyone-with-the-link sharing is turned off for the whole shared drive. Nothing about the federal order may be posted publicly without the Owner's approval. (AC-3; AC-22; FAR 52.204-21(b)(1)(iv))

4.7 **AI tools.** Restricted information may be entered only into AI tools on the approved list. Today the list has one entry: the oil laboratory's AI health-scoring portal (AI-001), for DGA results and nameplate data of customers that have consented in writing, without site coordinates, and only once its data processing addendum bars use of the data for model training (P10). FCI, the rewind library, and employee data must never be entered into any AI tool. Public AI chatbots must never receive Restricted information. (SA-9; PL-4; FAR 52.204-21(b)(1)(iii))

4.8 **Backups.** The following must be backed up and restorable:
- the suite (mail and shared drive): daily, kept at least 1 year, with deletion protected by a separate MFA-protected login;
- the ERP: the vendor's scheduled full export to the shared drive at least weekly;
- the test PC database: nightly copy to the shared drive;
- oven PLC program, recipes, and HMI project, and winding machine programs: copied to the shared drive after every change and checked at least every 6 months.

The MSP must restore a sample every quarter and give the Office Manager a written result. (CP-9; CP-4; PR.DS-11; RC.RP-03)

4.9 **Removable media.** USB sticks used with the test PC, the oven HMI, or the winding machine must be shop-owned, labeled, and scanned on an MSP-managed computer before each use on shop equipment. Personal USB sticks must not be used. (MP-7; SI-3; FAR 52.204-21(b)(1)(xv))

4.10 **Disposal.** Computers, drives, tablets, phones, and USB sticks that held Restricted information must be wiped before reuse, or destroyed by a vendor that provides a certificate of destruction. Paper with Restricted information is shredded. The Office Manager keeps each wipe or destruction record. (MP-6; ID.AM-08; FAR 52.204-21(b)(1)(vii); Fla. Stat. 501.171(8))

4.11 **Retention.** Test reports and job records are kept as long as customer contracts require and at least 5 years. Security documentation follows POL-02 A.7. (SI-12)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Compliance is checked through the monthly MSP report (encryption and backup status), quarterly restore results, and the annual assessment (P07).

## 6. Exceptions
Exceptions follow POL-02 A.9.

## 7. Related documents
POL-02; POL-03; inventory; P04 cloud control map; P10 AI risk assessment; federal purchase order; cooperative master service agreement
