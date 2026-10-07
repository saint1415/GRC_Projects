# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Office Manager (security and compliance lead) |
| Approved by | Broker-owner, 2026-09-14 |
| Effective date | 2026-09-15 |
| Review cycle | Annually (next review 2027-08-31), and after major changes |
| Implements (SP 800-53 Rev. 5) | RA-2, CM-8, MP-6, SC-8, SC-28, CP-9, CP-4, SA-9, SI-12, PL-4 |
| CSF 2.0 | ID.AM-01, ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11, GV.SC-05 |
| Rules served | Fla. Stat. 501.171(2) and (8); Fla. Stat. 475.5015; 16 CFR 682.3; benchmark 16 CFR 314.4(c)(2), (c)(3), (c)(6) |

## 1. Purpose
Sort brokerage information by the harm its loss, change, or disclosure would cause, and set simple handling, backup, retention, and disposal rules for each level.

## 2. Scope
All employees and contractor sales associates, and all brokerage information in any form: in the transaction platform, email and files, the property management platform, online banking, accounting, on company and personal devices, on paper, and in any vendor's system.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Office Manager | Owns this policy; keeps the system and data inventory; approves new tools; runs the January purge |
| Property Manager | Applies the screening report rules in 4.8 |
| MSP | Encryption, backup, restore tests, and device wiping, as directed by the Office Manager |
| Employees and contractor agents | Handle information according to its level |

## 4. Policy statements
4.1 Brokerage information has three levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Social Security, driver license, and passport numbers or images; bank statements and account numbers; wire and payout instructions; tenant screening reports; passwords and MFA codes | Only in approved systems (4.3); encrypted at rest and in transit; shared with clients only through client document sharing, never as an email attachment; never in personal accounts or AI tools |
| **Internal** | Contracts, listing agreements, escrow ledgers and reconciliations, commission records, agent agreements, security documents | Employees, assigned agents, and approved vendors only; encrypted in transit |
| **Public** | Active listings, marketing, office hours | No restriction |

When unsure, treat information as Restricted. (RA-2; ID.AM-07)

4.2 Restricted information must be encrypted wherever it is stored, including on every laptop, desktop, and phone that holds it, and whenever it leaves brokerage systems. Wire instructions and ID or bank documents go to clients only through the transaction platform's client document sharing. (SC-28; SC-8; PR.DS-01; PR.DS-02; benchmark 314.4(c)(3))

4.3 Restricted information may be kept only in: the transaction platform, the productivity suite (mail and shared files), the property management platform, online banking, the backup service, and for one business day the scanning workstation before files move to the shared files. (AC-3; benchmark 314.4(c)(2))

4.4 The Office Manager must keep a one-page inventory of every company device, every SaaS service, the vendors that hold brokerage data, and where Restricted information is stored, and update it when anything changes. (CM-8; ID.AM-01; ID.AM-07)

4.5 Before any new app, vendor, or device receives Restricted or Internal information, the Office Manager must approve it under POL-02 A.5 and add it to the inventory. (SA-9; GV.SC-05; benchmark 314.4(c)(4), (f))

4.6 **AI tools.** Restricted information must never be entered into an AI tool. Internal information may be entered only into an AI tool on the approved list, which today is empty; a business plan with no-training terms is under review (P10 AI-002). Listing descriptions written with AI help must be checked by the agent for accuracy and for discriminatory wording before publication. (SA-9; PL-4)

4.7 **Backups.** Every mailbox (employees and agents) and the shared files must be backed up nightly with at least 30 days of versions, in a service whose administrator login requires MFA. Active transaction files are exported monthly from the transaction platform. The MSP restores a sample every quarter, including the sales escrow ledger, and gives the Office Manager a written result. (CP-9; CP-4; PR.DS-11)

4.8 **Retention.** Brokerage books, accounts, and records are kept for 5 years from the receipt of funds or the signing of the agreement, longer if they relate to litigation (Fla. Stat. 475.5015). Tenant screening reports and rejected or withdrawn rental applications are kept 2 years after the decision and then deleted, unless a dispute or complaint is open. Copies of IDs and bank statements in email are deleted once the transaction file is complete in the transaction platform. Each January the Office Manager runs a purge of records past their period and records what was removed. (SI-12; ID.AM-08; benchmark 314.4(c)(6))

4.9 **Disposal.** Paper with Restricted information goes in the locked shred bin. Devices and media are wiped or destroyed by a vendor that issues a certificate before they leave the brokerage. The Office Manager keeps each certificate. (MP-6; ID.AM-08; Fla. Stat. 501.171(8); 16 CFR 682.3)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Compliance is checked through the monthly MSP report (encryption and backup status), quarterly restore results, the January purge record, and the annual assessment (P07).

## 6. Exceptions
Exceptions follow POL-02 A.9.

## 7. Related documents
POL-02; POL-03; system and data inventory; P04 cloud control map; P10 AI risk assessment
