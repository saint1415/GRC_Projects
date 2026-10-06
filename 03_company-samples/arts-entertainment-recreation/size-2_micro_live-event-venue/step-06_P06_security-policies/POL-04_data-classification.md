# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Venue Manager (Security and Privacy Lead) |
| Approved by | Owner and General Manager, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes |
| Implements (SP 800-53 Rev. 5) | RA-2, CM-8, SI-12, MP-6, SC-8, SC-28, CP-9, CP-4, PE-3, SA-9, PL-4 |
| CSF 2.0 | ID.AM-01, ID.AM-02, ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| PCI DSS v4.0.1 (N71-R04) | 3.1, 3.2, 3.3, 4.2, 9.4, 9.5, 12.5 |
| Law (N71-R05) | FTC Act Section 5, 15 U.S.C. 45(n) |

## 1. Purpose
Sort company information by how much harm its loss or disclosure would cause, and set simple handling rules for each level, starting with the most important rule of all: the company does not keep card data.

## 2. Scope
All employees, owners, and contractors, and all company information in any form: in the ticketing platform, email, shared files, the website, on devices, on paper, and in any vendor's system.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Venue Manager | Owns this policy; keeps the inventory; approves new tools and data uses with the Owner |
| Box Office and Ticketing Manager, Marketing Coordinator, Bar Manager | Apply these rules in the ticketing platform, website and email marketing, and bar POS |
| MSP | Encryption, backup, restore tests, and device wiping, as directed by the Venue Manager |
| All workforce and contractors | Handle information according to its level |

## 4. Policy statements
4.1 Company information has three levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Card data of any kind (never kept, see 4.2); patron records and exports; corporate client attendee lists; passwords, MFA codes, and API tokens; bank details for artist payments | Only in approved systems (4.3); encrypted at rest and in transit; minimum necessary; never in personal accounts or public AI tools |
| **Internal** | Artist offers and contracts, settlement sheets, payroll, vendor contracts, security documents | Employees and approved vendors only; encrypted in transit |
| **Public** | Event calendar, posted prices, press releases | No restriction |

When unsure, treat information as Restricted. (RA-2; ID.AM-07)

4.2 **Card data.** The company accepts card payments only through the ticketing vendor's checkout widget or vendor-hosted pages, a payment link from the ticketing platform, and PCI-listed validated P2PE readers. No one may write down, type into a company computer, email, photograph, or store a card number, expiration date, or security code. Card data that arrives anyway must be deleted from the mailbox and deleted items, or cross-cut shredded, the same day, and reported to the Venue Manager. (SI-12; MP-6; PR.DS-01; PCI 3.1; 3.2; 3.3; 9.4)

4.3 **Patron records** may be kept only in the ticketing platform, the email marketing service, and the restricted patron folder in the suite. Exports must go to that folder, not to a laptop's downloads, and must be deleted within 30 days of their use. Corporate client attendee lists are kept in the client's restricted folder and deleted 30 days after the event. (AC-3; SI-12; ID.AM-07)

4.4 **Encryption.** Every laptop and desktop must have full-disk encryption, and Restricted information sent outside company systems must be encrypted in transit. (SC-28; SC-8; PR.DS-01; PR.DS-02; PCI 4.2)

4.5 **Inventory.** The Venue Manager keeps a one-page inventory of every computer, tablet, and scanner; every P2PE card reader with its serial number and location; every SaaS service; every API token and connected app; every script on the website pages that host the checkout widget; and every place Restricted information is stored. It is updated when anything is added or removed and checked in the monthly account check. (CM-8; ID.AM-01; ID.AM-02; PCI 9.5.1; 12.5.1)

4.6 **Card readers.** Before each show the door and bar leads inspect each reader against the inventory (serial number, seals, no extra parts) and initial the checklist. Spare readers stay locked in the back office safe. Anything odd is reported at once (POL-03 4.2) and the reader is not used. (CM-8; PE-3; PCI 9.5.1)

4.7 **AI tools.** Restricted information may be used only by AI tools on the approved list. Today the list has one entry: the ticketing platform's demand tools module, under the conditions in P10. Public or personal AI tools may be used only with Public information. Any new AI feature, or any new use of patron data, needs a P10 review before it goes live. (SA-9; PL-4)

4.8 **Backups.** The suite backup must cover every mailbox, including shared mailboxes, and shared files, with versions kept at least 30 days and the backup console protected by MFA. The MSP must restore a sample every quarter and give the Venue Manager a written result. (CP-9; CP-4; PR.DS-11)

4.9 **Retention and disposal.** Patron exports: 30 days after use. Email marketing lists: while the subscriber stays opted in. Security records: at least 5 years (POL-02 A.9). Devices and media that held Restricted information must be wiped before reuse or destroyed by a vendor that provides a certificate, and paper is cross-cut shredded. (SI-12; MP-6; ID.AM-08)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Compliance is checked through the monthly account check, the monthly MSP report (encryption and backup status), quarterly restore results, the pre-show reader checklists, and the annual assessment (P07).

## 6. Exceptions
Exceptions follow POL-02 A.12. No exception is allowed to rule 4.2.

## 7. Related documents
POL-02; POL-03; inventory; pre-show reader checklist; P04 cloud control map; P03 PCI DSS scope decision; P10 AI risk assessment
