# Scenario facts: Cris Santos Company | Management of Companies and Enterprises | Sole Proprietorship

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship; the owner files Schedule C) |
| Business | The owner's management business for three small companies the owner wholly owns (NAICS 551112, Offices of Other Holding Companies). Through the sole proprietorship the owner personally runs the back office for all three: bookkeeping, banking and payments, payroll, vendor contracts, IT accounts, and tenant and customer records. Each company pays a monthly management fee under a written management agreement |
| Portfolio companies | Each is a single-member Florida LLC wholly owned by the owner, with its own bank account, books, insurance, and contracts. **CSC Self Storage, LLC** ("Storage"): one 180-unit self-storage facility (NAICS 531130), about 150 units rented, keypad gate, online rentals and autopay. **CSC Rentals, LLC** ("Rentals"): six duplexes with 12 residential units (NAICS 531110); applicants are screened through the property management platform. **CSC Laundry, LLC** ("Laundry"): one laundromat with wash-and-fold pickup and delivery (NAICS 812310); machines take coins, cards, and a payment app |
| Location | Florida. Three places: the owner's **home office** (the sole proprietorship's only office), the **Storage office** at the storage facility (about 8 miles away), and the **laundromat** (about 5 miles away). The duplexes are on two streets near the laundromat |
| Workforce | The owner only at the sole proprietorship (0 employees). The LLCs employ 3 part-time workers in total (Storage 1, Laundry 2), paid through the payroll service. Rentals has no employees |
| Receipts | About $180,000 a year (fictional), all management fees: Storage $72,000, Rentals $48,000, Laundry $60,000. The LLCs' own revenue (fictional): Storage about $310,000, Rentals about $200,000, Laundry about $240,000. SBA counts the receipts of a concern and its affiliates (13 CFR 121.103(a)(6); 121.104(d)(1)); even combined, about $750,000 is far below the $45.5 million standard for NAICS 551112 |
| Personal information held | **Storage:** about 610 current and former tenant records in the storage management system (name, address, phone, email, driver license number, gate code); about 230 scanned driver license copies from 2021 to 2024 in the shared file storage. **Rentals:** 12 current households; 47 rental application files (2023 to 2026) with Social Security numbers, driver license copies, pay stubs, bank statements, and tenant screening reports, downloaded as PDFs into the shared file storage. **Laundry:** about 140 wash-and-fold customers (name, phone, address) in the POS system; about 900 payment app accounts are held by the payment vendor. **Employees:** 3 current and 5 former LLC employees (SSNs, bank accounts) in the payroll service, plus scanned new-hire forms in the file storage |
| Card payments | Storage takes cards through the storage system's integrated processor (hosted payment fields). Laundry's machine readers and app are run by the laundry payment vendor. The owner stores no card numbers. PCI DSS duties are contractual (merchant agreements) and are noted, not assessed |
| Florida breach law status | Each LLC is a **covered entity** under Fla. Stat. 501.171(1)(b) for its own tenants, customers, and employees. The sole proprietorship maintains and processes that information for the LLCs under the management agreements, so it is also their **third-party agent** (501.171(1)(h)). The definition of covered entity names a sole proprietorship expressly |
| Federal rules that reach an LLC | **Rentals** uses consumer reports to screen applicants: the Fair Credit Reporting Act user duties (permissible purpose, 15 U.S.C. 1681b(a)(3)(F)(i) and 1681b(f); adverse action notices, 1681m(a)) and the FTC Disposal Rule (16 CFR 682.3) apply. The Fair Housing Act (42 U.S.C. 3604) applies to Rentals' tenant selection: the units are in duplexes, not single-family houses, and the owner lives in none of them, so neither exemption in 42 U.S.C. 3603(b) fits |
| Not in scope | SEC Regulation S-K Item 106, Form 8-K Item 1.05, and SOX section 404 (no securities registered; not an issuer). Federal Reserve Regulation Y Subpart N and 12 CFR Part 225 Appendix F (no bank). HIPAA (no group health plan; no LLC is a health care provider). FTC Safeguards Rule (no LLC is a financial institution under 16 CFR 314.2(h): none extends consumer credit, brokers loans, or gives financial advice, and Rentals maintains and repairs its units, so its leases are not the nonoperating leases in 12 CFR 225.28(b)(3)). Florida Digital Bill of Rights (a controller must exceed $1 billion in global gross annual revenue) |
| Contrast worth noting | The test is the activity, not the size. If Rentals began owner-financing sales of its duplexes, or Laundry opened its own customer credit accounts, that LLC could become a financial institution under 16 CFR 314.2(h) if it were significantly engaged in that activity, and the Safeguards Rule would follow |
| State law approach | Florida law is cited only where unavoidable (breach notice, data security, and disposal, Fla. Stat. 501.171) |

## 2. People and contracted services (role titles only)
| Role | Duties |
|---|---|
| Owner-manager | Every role for the sole proprietorship and, as sole member and manager, for each LLC: risk acceptor, security lead, incident lead, policy approver, and administrator of every system |
| Designated successor manager | Named in each LLC operating agreement to manage the LLCs if the owner is incapacitated. Has no system access and no written instructions today |
| Storage facility manager (part-time employee of Storage) | Runs the Storage office: move-ins, payments, gate codes. Manager role in the storage system; a mailbox in the productivity suite |
| Laundry attendants (2 part-time employees of Laundry) | Wash-and-fold orders on the POS tablet; use one shared POS PIN and the shared Laundry mailbox |
| Outside bookkeeper (contractor) | Monthly reconciliations and payroll entry for all four entities. Accountant user in the accounting service with full access to all four company files; payroll entry role. No written confidentiality or security terms |
| Outside CPA firm | Annual tax returns. Receives year-end files through its own client portal |
| On-call IT technician (hourly contractor) | Help with the laptop, Storage desktop, routers, and the gate controller on request. No standing access; uses a remote-support tool the owner starts |
| Business attorney | Prepares the LLC agreements and management agreements; refers a privacy attorney for breach questions |
| Rentals maintenance contractor | Repairs at the duplexes. Receives tenant names and phone numbers by text. No system access |

## 3. Systems
| ID | System | Hosting | Personal information? | Notes |
|---|---|---|---|---|
| SYS-01 | Productivity suite (email, files, calendar, and identity for the suite), business plan | SaaS | Yes: rental applications, driver license scans, new-hire forms, tenant and vendor correspondence | One tenant with four email domains (one per entity). Mailboxes: owner (administrator), Storage manager, shared Laundry mailbox. Owner uses text-message MFA; the other two have no MFA. Deleted items kept 30 days; no independent backup |
| SYS-02 | Accounting service with four company files | SaaS | Vendor bank details; employee pay data | The back-office system of record for all four entities (it plays the ERP role at this size). Bank feeds. Vendor enforces authenticator-app MFA. Vendor has a SOC 2 Type 2 report |
| SYS-03 | Online banking: four business accounts at one bank | Bank-hosted | Account credentials | One online profile; the owner sees and pays from all four accounts. The bank requires a one-time code for wires and new payees. The owner is the only user, so dual approval is not possible |
| SYS-04 | Payroll service: two employer accounts (Storage, Laundry) | SaaS | Employee SSNs, bank accounts, tax forms | Vendor enforces MFA. Bookkeeper enters hours |
| SYS-05 | Storage management system with online rentals, autopay, and gate access integration | SaaS | Tenant records with driver license numbers; gate codes | Users: owner (administrator), Storage manager, and a former storage assistant's account still active. MFA available, not turned on |
| SYS-06 | Property management platform (Rentals) | SaaS | Applications, screening reports, leases, rent payments | Listings, applications, tenant screening ordered through the platform's consumer reporting agency partner, leases, rent by ACH, tenant portal. Owner is the only user; text-message MFA |
| SYS-07 | Laundry POS and machine payment platform | SaaS | Wash-and-fold customer contacts | POS app on one tablet; card and app readers on the machines; customer app accounts held by the vendor. Owner is administrator; attendants share one PIN |
| SYS-08 | Owner laptop and phone | Owner devices | Yes (downloads, cached mail and files) | Laptop full-disk encryption on; built-in antivirus; automatic updates. Phone receives MFA codes. Passwords saved in the browser; no password manager |
| SYS-09 | Site devices and networks | On premises | Yes (Storage desktop) | Storage office desktop (one shared local account with no password; no disk encryption); Laundry POS tablet; internet routers at the Storage office and the laundromat (laundromat customer Wi-Fi on the same network as the POS tablet and payment hub); gate controller at Storage (installer default administrator password); home office Wi-Fi |
| SYS-10 | Generative AI assistant (add-on to SYS-01) | SaaS | Yes (whatever the owner's account can open) | Turned on by the owner on 2026-06-01 for the owner's account only. Can read the owner's mail and files for all four entities. See P10 |

**SSP system (P02):** the *Shared Back-Office Platform*: SYS-01 to SYS-04, SYS-08, and SYS-10, plus the owner's administrator access to the LLC systems SYS-05 to SYS-07 and the site devices in SYS-09.

## 4. Current security posture: early (few formal controls)
**In place today:**
- Authenticator-app MFA enforced by the vendors of the accounting service (SYS-02) and payroll service (SYS-04)
- Text-message MFA on the owner's email (SYS-01) and property management (SYS-06) accounts
- The bank's one-time code for wires and new payees, and email alerts for every outgoing payment
- Separate bank accounts, books, insurance, and contracts for each LLC
- Laptop full-disk encryption, built-in antivirus, and automatic updates; phone passcode and automatic updates
- Card data handled only by processors (hosted payment fields; vendor-run machine readers)
- Screening reports delivered inside the property management platform
- A cross-cut shredder at the Storage office for paper move-in forms

**Missing:**
1. No risk assessment, no inventory of accounts and data, and no written security policy for any of the four entities.
2. One identity is the key to all four entities. The owner's email account is the administrator and recovery address for every system, uses text-message MFA, and has no stored recovery codes.
3. No password manager. Passwords are saved in the browser, and the owner reused one password on the storage system and the laundry platform.
4. The Storage manager's mailbox and the storage system have no MFA. The Storage office desktop has one shared local account with no password and no disk encryption.
5. Access is not removed when people leave. A former storage assistant's account (left 2026-01-16) is still active, and the shared Laundry POS PIN and mailbox password were not changed after an attendant left on 2026-03-27.
6. Rental application files (47, with SSNs and screening reports) and about 230 driver license scans are kept with no retention or disposal rule (16 CFR 682.3; Fla. Stat. 501.171(8)).
7. No backup of email and files beyond the vendor's 30-day deleted-item retention, and no exports from the accounting, storage, or property management systems.
8. Payment changes are accepted by email. There is no callback before paying a new or changed bank account.
9. The laundromat's customer Wi-Fi shares a network with the POS tablet and payment hub, and the storage gate controller still uses the installer's default administrator password.
10. No incident plan, no contact list, and no cyber insurance (each LLC carries general liability coverage only).
11. No vendor list and no review of vendor terms or SOC 2 reports. The bookkeeper has full access to all four company files with no written confidentiality or security terms.
12. The generative AI assistant was turned on 2026-06-01 with no rules. On 2026-07-14 the owner used it to summarize six rental applications for unit 4B, including their screening reports, and asked it which applicant to choose.
13. No security training for the owner or the LLC staff.
14. The owner is a single point of failure for all four entities. The successor manager has no access path or instructions.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 benchmark | NIST CSF 2.0 portfolio profile (voluntary), all 106 subcategories, rated for the Shared Back-Office Platform with notes where an LLC differs. Binding rows: Fla. Stat. 501.171, the FCRA user duties and FTC Disposal Rule for Rentals, and the card processor terms (contract). N55-R01 to N55-R07 recorded as not applicable |
| P05 functions | Five: Storage rentals and gate access; Rentals leasing and rent; Laundry operations; payments, payroll, and bookkeeping for all four entities; owner email, files, and records |
| P08 incident | Compromise of the shared back office affecting all three LLCs: takeover of the owner's email account (SYS-01) through a fake document-share page that relays the text-message code, followed by a payment redirection attempt and download of the Rentals application folder |
| P09 SOC 2 | Security criteria only, as the owner's self-check, plus a review of the accounting service's SOC 2 Type 2 report (the system that holds all four entities' books) |
| P10 AI | The generative AI assistant add-on (SYS-10) the owner uses across all three LLCs |
| Cloud | SaaS only. No IaaS |
| Registry defaults adapted | Primary system: a one-person holding business has no ERP or separate identity provider, so the "shared corporate services platform (ERP and identity)" is the productivity suite tenant (identity, email, files) plus the multi-company accounting service. Incident: "compromise of shared services affecting subsidiaries" becomes the takeover of the owner's one email account, which administers every LLC system. AI: the "enterprise generative AI assistant across subsidiaries" is the business-plan add-on used by one person whose account reaches all four entities' data |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-07-27 to 2026-07-31 | Self-assessment by the owner with the on-call IT technician (tests on 2026-07-30) |
| 2026-08-31 | Deliverables adopted by the owner-manager |

## 7. Facts added while building the deliverables
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
