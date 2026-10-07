# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Store Manager (Security and PCI Lead) |
| Approved by | Owner, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Yearly (next review 2027-08-31), and after major changes |
| Implements (SP 800-53 Rev. 5) | RA-2, CM-8, PE-3, MP-6, SC-8, SC-28, CP-9, SA-9, SI-12, PT-5 |
| CSF 2.0 | ID.AM-01, ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11, PR.PS-01 |
| PCI DSS v4.0.1 (N44-45-R01) | 3.1-3.3, 4.1-4.2, 9.1, 9.4, 9.5 |
| Other | FTC Act Section 5 (N44-45-R02); Fla. Stat. 501.171(8) disposal |

## 1. Purpose
Sort store information by how much harm its loss or disclosure would cause, and set simple handling rules for each level, including the rules for card data and card terminals.

## 2. Scope
All workforce members and outside users, and all store information in any form: in the platform, the online store, email, the office PC, the store phone, on paper, and in any vendor's system.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Store Manager | Owns this policy; keeps the inventory and the terminal list; approves new tools and data sharing |
| Cashiers | Inspect terminals at opening; follow the card data rules |
| MSP | Encryption, backups, restore tests, and wiping of the computers it manages, as directed by the Store Manager |
| All workforce | Handle information according to its level |

## 4. Policy statements
4.1 Store information has three levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Card numbers and security codes (never kept); loyalty and customer lists; online customer accounts and delivery addresses; payout and bank details; passwords, POS codes, and MFA codes; employee pay and ID documents | Only in approved systems (4.4); encrypted at rest and in transit; never in personal accounts or public AI tools; full exports only with the Owner's approval |
| **Internal** | Supplier prices and contracts, sales reports, schedules, security documents | Staff and approved vendors only |
| **Public** | Store hours, weekly ad, website content | No restriction |

When unsure, treat information as Restricted. (RA-2; ID.AM-07)

4.2 **Card data is never kept.** Card numbers are entered only on the P2PE terminals in the store or in the provider's card fields online. No one may write down, type into any other system, photograph, email, or text a full card number or security code, and the dashboard virtual terminal stays turned off. Merchant copies and reports with truncated numbers are kept in the locked back office and shredded after 90 days. (SI-12; PCI DSS 3.1, 3.2, 3.3, 9.4)

4.3 **Card numbers received by email or chat.** If a customer sends a card number, staff must not reply with it or forward it. Delete it from the mailbox and deleted items, and reply with the standard message asking the customer to pay through the online store or in person. The shared orders mailbox carries an auto-reply that says never to send card numbers. (SC-8; PCI DSS 4.1, 4.2)

4.4 Restricted information may be kept only in: the commerce platform and online store, the productivity suite (personal and delegated mailboxes and the store's file area), the accounting SaaS and payroll service, and the office PC backup. Loyalty and customer lists may not be exported in full; use the platform's own email and offer tools instead. (AC-3; SI-12)

4.5 **Inventory.** The Store Manager must keep a one-page inventory of every device, every SaaS service, every script and app on the online store, and every place Restricted information is stored, and update it whenever anything is added or removed. (CM-8; ID.AM-01; PCI DSS 12.5)

4.6 **Card terminals.** The Store Manager must keep a list of every card terminal with make, model, serial number, and location, reconciled with the provider's records. Cashiers must inspect each countertop terminal at opening for added parts, broken seals, wires, or a changed serial number, and sign the inspection sheet. No one may let a person service, swap, or remove a terminal without verifying their identity with the provider first. Only devices in the provider's P2PE solution may take card payments. (CM-8; PE-3; ID.AM-01; PCI DSS 9.1, 9.5)

4.7 **Encryption.** Restricted information must be encrypted wherever it is stored, including the office PC and laptop, and whenever it is sent outside the store's systems. (SC-28; SC-8; PR.DS-01; PR.DS-02)

4.8 **AI tools.** Restricted information may be used only by AI tools on the approved list kept in this policy. Today the list has one entry: the commerce platform's offers and markdown feature (SYS-10), under the P10 conditions. Public or personal AI chatbots may be used only for product descriptions and social posts with no customer, employee, or supplier pricing data (P10 AI-002). (SA-9; PL-4)

4.9 **New tools and sharing.** Before any new vendor, app, script, or AI feature receives Restricted information, the Store Manager must approve it, a written agreement must be in place (POL-02 A.5), it must be added to the inventory, and the privacy notice must still be accurate. (SA-9; PT-5; GV.SC-05)

4.10 **Backups.** The MSP must back up the office PC nightly and restore a sample at least twice a year, with a written result. The Store Manager must export the item file and customer directory from the platform monthly and keep the export in the store's file area. (CP-9; PR.DS-11)

4.11 **Disposal.** Devices that held Restricted information must be wiped or factory reset (tablets and phones) before reuse or disposal, and the Store Manager keeps a record. Paper with customer or card information is shredded. Records are disposed of in a way that makes the personal information unreadable (Fla. Stat. 501.171(8)). (MP-6; ID.AM-08)

## 5. Compliance and enforcement
Breaking this policy is handled under POL-02 section 5. Compliance is checked through the inspection sheets, the monthly MSP report, the inventory, and the yearly assessment (P07).

## 6. Exceptions
Exceptions follow POL-02 A.9. No exception may allow card numbers to be kept.

## 7. Related documents
POL-02; POL-03; terminal list and inspection sheet; inventory; P2PE Instruction Manual; P04 cloud control map; P10 AI risk assessment
