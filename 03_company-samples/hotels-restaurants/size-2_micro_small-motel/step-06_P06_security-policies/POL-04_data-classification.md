# Data Classification and Card Data Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Assistant Manager (Security and Privacy Lead) |
| Approved by | Owner-Manager, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Yearly (next review 2027-08-31), and after any change to how payments are taken |
| Implements (SP 800-53 Rev. 5) | RA-2, CM-8, MP-4, MP-6, SC-8, SC-28, CP-9, CP-4, SA-9, SI-12, AU-6 |
| CSF 2.0 | ID.AM-01, ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11, DE.AE-02 |
| Requirements | PCI DSS v4.0.1 requirement groups 3.1 to 3.5, 4.2, 9.4, 9.5, 10.4, 12.5 (N72-R01); 16 CFR 682.3 (N72-R03); Fla. Stat. 501.171(8) and 509.101(2) (N72-R04) |

## 1. Purpose
Sort motel information by how much harm its loss or disclosure would cause, set simple handling rules for each level, and set the card data rules that keep the front desk PC out of card data scope.

## 2. Scope
All workforce members and all motel information in any form: in the PMS, email, files, the gateway portal, on devices, on paper, and in any vendor's system.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Assistant Manager | Owns this policy; keeps the inventory; approves new tools; runs the weekly log review |
| Night Auditor | Weekly terminal inspection |
| MSP | Encryption, backup, restore tests, and device wiping, as directed by the Assistant Manager |
| All workforce | Handle information according to its level |

## 4. Policy statements
4.1 Motel information has three levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Card numbers and security codes; ID card, driver license, and passport numbers and scans; passwords and MFA codes; background-check reports | Only in approved systems (4.3); encrypted at rest and in transit; never on paper except as 4.2 allows; never in personal accounts or AI tools |
| **Internal** | Guest names, contact details, and stay history; the guest register; crew rosters and crew client contracts; payroll; security documents | Workforce and approved vendors only; encrypted in transit |
| **Public** | Rates as published (total price), amenities, policies, website content | No restriction, but must be accurate (16 CFR 464) |

When unsure, treat information as Restricted. (RA-2; ID.AM-07)

4.2 **Card data rules.** (a) Card numbers are entered only on the P2PE terminals or by the guest on the gateway's pay-by-link or the booking engine. (b) Staff never type card numbers into a PC, and never write them on paper. (c) Card numbers are never accepted by email, text, chat, or fax; a guest or crew company that sends one gets a pay-by-link, and the message is deleted the same day. (d) Card security codes are never stored after authorization, on any medium. (e) Full card numbers are never displayed; virtual cards are charged through the PMS without display. Until the redesign is complete (2026-11-30), the Assistant Manager may approve keyed entry only on the P2PE terminal keypad where the P2PE Instruction Manual allows. (SI-12; AC-6; PR.DS-01; PCI DSS 3.2, 3.3.1, 3.4, 4.2)

4.3 Restricted information may be kept only in: the PMS (profiles, ID data, card vault), the payment gateway, the suite (named mailboxes and files, never card data), the accounting and payroll services, and the backup service. Paper crew card forms remaining from before 2026-11-30 are kept in a locked drawer in the back office until shredded. (AC-3; MP-4; PCI DSS 9.4)

4.4 The Assistant Manager must keep a one-page inventory of every device (including both terminals with their serial numbers), every SaaS service, and every place Restricted information is stored, and update it when anything changes. The PCI DSS scope is confirmed from it every year (POL-02 A.6). (CM-8; ID.AM-01; PCI DSS 12.5, 9.5)

4.5 **Terminals.** The Night Auditor inspects both terminals every week for tampering or substitution (serial number, seals, cables, overlays) as the P2PE Instruction Manual describes, and records the result. Staff never let anyone service or replace a terminal without the Assistant Manager confirming the visit with the gateway. (CM-8; PCI DSS 9.5)

4.6 Before any new vendor, app, or device receives Restricted or Internal information, the Assistant Manager must approve it, POL-02 A.5 must be met, and it must be added to the inventory. (SA-9; GV.SC-05)

4.7 **AI tools.** Only AI tools on the approved list may be used for motel work. Today the list has one entry: the dynamic pricing tool, which receives no guest identities or card data (P10). The PMS vendor's AI guest messaging add-on must not be switched on until it has been assessed. Public or personal AI chatbots must never receive Restricted or Internal information. (SA-9; PL-4)

4.8 **Retention.** Register data (guest names, dates of occupancy, rates) is kept 2 years and then purged (Fla. Stat. 509.101(2) sets the 2-year availability floor). ID scans and ID numbers are deleted 30 days after checkout. Crew rosters (beyond the register entries) are deleted 30 days after the crew's last checkout. Card data is not kept. Background-check reports are kept in a locked drawer and shredded once they are no longer needed for the hiring decision and any record period counsel confirms. Security records follow POL-02 A.7. The PMS purge settings are used to enforce these periods. (SI-12; ID.AM-08; Fla. Stat. 501.171(8))

4.9 **Disposal.** Paper with Restricted information is cross-cut shredded. Devices and media are wiped before reuse or destroyed by a vendor that provides a certificate of destruction. The Assistant Manager keeps each wipe or destruction record. (MP-6; ID.AM-08; 16 CFR 682.3; Fla. Stat. 501.171(8); PCI DSS 9.4)

4.10 **Log review.** Each week the Assistant Manager reviews the PMS activity report for full card number displays, profile exports, and sign-ins at unusual hours, and the suite's sign-in alerts, and records the review on a checklist. (AU-6; DE.AE-02; PCI DSS 10.4)

4.11 **Encryption and backups.** Restricted information must be encrypted wherever it is stored and whenever it is sent outside motel systems; the front desk and back office PCs use full-disk encryption. The back office PC, including the lock database, and the suite are backed up nightly, with versions kept at least 30 days in storage that cannot be changed or deleted in that period. The MSP restores a sample, including the lock database, every quarter and gives the Assistant Manager a written result. (SC-28; SC-8; CP-9; CP-4; PR.DS-11)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Compliance is checked through the weekly terminal and log checklists, the monthly MSP report (encryption and backup status), quarterly restore results, and the yearly assessment (P07).

## 6. Exceptions
Exceptions follow POL-02 A.9. No exception may allow storage of card security codes.

## 7. Related documents
POL-02; POL-03; inventory; P2PE Instruction Manual; P04 cloud control map; P10 AI risk assessment
