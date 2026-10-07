# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Operations Manager (Qualified Individual and security lead) |
| Approved by | Owner, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after a significant change |
| Implements (SP 800-53 Rev. 5) | RA-2, CM-3, CM-8, MP-6, SC-8, SC-28, CP-9, SA-9, SI-7, SI-12, PE-3 |
| CSF 2.0 | ID.AM-01, ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11, PR.PS-01 |
| Drivers | PCI DSS v4.0.1 3.2, 3.3, 4.2, 6.4.3, 9.4, 9.5, 12.5.1, 12.10.7; 16 CFR 314.4(c)(2), (c)(3), (c)(6) |

## 1. Purpose
Sort company information by the harm its loss or disclosure would cause, keep card data out of company systems wherever possible, and set simple rules for the information the company must hold.

## 2. Scope
All employees and outside agents and all company information in any form: in the console, portal, CRM, suite, phone system, website, laptops, paper, and any vendor's system. It also covers the content the company adds to merchants' hosted payment pages and the spare terminals the company holds.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Operations Manager | Owns this policy; keeps the inventory; approves new tools and vendors |
| Terminal and Integration Technician | Payment page content inventory; terminal inventory and inspections |
| Onboarding and Risk Specialist | Merchant file retention and purges |
| MSP | Encryption, backup, restore tests, and laptop wiping, as directed by the Operations Manager |
| All employees and agents | Handle information according to its level |

## 4. Policy statements
4.1 Company information has three levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Card numbers, expiry dates, card security codes; merchant owner Social Security numbers, dates of birth, ID images, bank account numbers; passwords and MFA codes | Card data: never stored (4.2). Merchant owner data: only in approved systems (4.3), encrypted, minimum necessary |
| **Confidential** | Merchant names with pricing or volumes; residual reports; agent commissions; contracts; SAQs and security documents | Employees, approved agents, and approved vendors only; encrypted in transit |
| **Public** | Website content, brochures | No restriction |

When unsure, treat information as Restricted. (RA-2; ID.AM-07)

4.2 **Card data.** The company must not store card data in any form. Card security codes must never be recorded or written down, before or after authorization. Call recording must stay off for any queue or call where a card number might be spoken. If card details must be taken by phone while the keyed-entry service runs (until 2026-10-15), they are keyed directly into the gateway on a support laptop in the office and never written down. (SC-28; SI-12; PCI DSS 3.2.1, 3.3.1)

4.3 **Where Restricted merchant data may live.** Merchant owner information may be kept only in the CRM and the processor partner portal, and must reach the company only through the CRM's secure upload link. It must not be kept in email, the shared drive, the website, or laptops. (AC-3; 16 CFR 314.4(c)(3))

4.4 **Inventory.** The Operations Manager must keep a one-page inventory of every system, data store, and service that holds Restricted or Confidential information, and of every laptop and spare terminal, and update it when anything is added or removed. This inventory is the PCI DSS scope list. (CM-8; ID.AM-01; PCI DSS 12.5.1; 16 CFR 314.4(c)(2))

4.5 **Encryption.** Restricted information must be encrypted at rest on every device and service that holds it and whenever it travels over the internet. Email that must carry Confidential information outside the company must use the suite's encrypted mail feature. (SC-28; SC-8; PR.DS-01; PR.DS-02; PCI DSS 4.2.1)

4.6 **AI tools.** Only AI tools on the approved list may be used for company work. Today the list has one entry: the business AI assistant licensed by the company, with terms that bar training on company data, for Confidential and Public information only. Restricted information must never be entered into any AI tool. Changes to the gateway's AI fraud-scoring settings follow P10 and the change rule in 4.9. (SA-9; PL-4)

4.7 **Retention and disposal.** Declined and withdrawn merchant applications must be deleted within 24 months of the decision. Closed merchant files must be deleted 24 months after closing unless the ISO agreement or law requires longer. Support call recordings, where allowed, are kept for 90 days. The Onboarding and Risk Specialist runs a purge every quarter and records it. Laptops are wiped by the MSP before reuse or disposal, with a record. Paper goes in the locked shred bin. (SI-12; MP-6; ID.AM-08; 16 CFR 314.4(c)(6))

4.8 **Card data found where it should not be.** Anyone who finds card data in email, tickets, recordings, files, or paper must tell the Operations Manager at once. The Operations Manager logs it as an incident under POL-03, finds out how it got there, deletes it securely, fixes the cause, and records whether any notice is owed. Every quarter the Merchant Support Lead searches mailboxes and tickets for card numbers. (SI-12; PCI DSS 12.10.7; PCI DSS 3.2.1)

4.9 **Payment page content and gateway settings.** No script or other content may be added to a merchant's hosted payment page unless it is in the payment page inventory with a written business justification and the Operations Manager has approved it. Every change to payment page content or fraud filter settings must be recorded in the change log. The Technician must compare each page against the inventory every month until the processor partner confirms in writing that its change-detection covers company-added content. (SI-7; CM-3; PR.PS-01; PCI DSS 6.4.3, 6.5.1)

4.10 **Spare terminals.** Spare terminals must be kept in the locked cabinet and listed by serial number. The Technician must reconcile the list every month and inspect every returned terminal for signs of tampering before it goes back into stock; damaged or doubtful units go back to the processor partner. (PE-3; CM-8; PCI DSS 9.5.1)

4.11 **New tools and vendors.** Before any new vendor, app, or device receives Restricted or Confidential information, the Operations Manager must approve it, the vendor must be added to the service provider list (POL-02 A.7), and it must be added to the inventory. (SA-9; GV.SC-05)

4.12 **Backups.** Suite data must be backed up daily with at least 1 year of retention. The MSP must restore a sample every quarter and give the Operations Manager a written result. (CP-9; PR.DS-11)

## 5. Compliance and enforcement
Breaking this policy leads to action under POL-02 A.12. Compliance is checked through the quarterly PCI review (POL-02 A.5), the quarterly card data search and purge, and the annual assessment (P07).

## 6. Exceptions
Exceptions follow POL-02 A.11. No exception may allow card security codes to be stored.

## 7. Related documents
POL-02; POL-03; inventory; payment page inventory and change log; terminal inspection checklist; P04 cloud control map; P10 AI risk assessment

## 8. Procedures to be written under this policy
These short procedures sit under this policy and are tracked in P03:
- network and firewall procedure, with the MSP's roles (PCI DSS 1.1)
- laptop and firewall configuration standard from the MSP (PCI DSS 2.2)
- change and patch roles, including critical patches within 30 days (PCI DSS 6.1, 6.3.3)
- physical security and visitor log (PCI DSS 9.1, 9.3)
