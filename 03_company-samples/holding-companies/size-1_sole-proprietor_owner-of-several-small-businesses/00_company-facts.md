# Scenario facts: Cris Santos Company | Management of Companies and Enterprises | Sole Proprietorship

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship; the owner files Schedule C) |
| Business | The owner's management business for three small companies the owner wholly owns (NAICS 551112, Offices of Other Holding Companies). Through the sole proprietorship the owner personally runs the back office for all three: bookkeeping, banking and payments, payroll, vendor contracts, IT accounts, and tenant and customer records. Each company pays a monthly management fee under a written management agreement (EV-015) |
| Portfolio companies | Each is a single-member Florida LLC wholly owned by the owner, with its own bank account, books, insurance, and contracts. **CSC Self Storage, LLC** ("Storage"): one 180-unit self-storage facility (NAICS 531130), about 150 units rented, keypad gate, online rentals and autopay. **CSC Rentals, LLC** ("Rentals"): six duplexes with 12 residential units (NAICS 531110); applicants are screened through the property management platform. **CSC Laundry, LLC** ("Laundry"): one laundromat with wash-and-fold pickup and delivery (NAICS 812310); machines take coins, cards, and a payment app (EV-007, EV-008, EV-009, EV-024) |
| Location | Florida. Three places: the owner's **home office** (the sole proprietorship's only office), the **Storage office** at the storage facility (about 8 miles away), and the **laundromat** (about 5 miles away). The duplexes are on two streets near the laundromat |
| Workforce | The owner only at the sole proprietorship (0 employees). The LLCs employ 3 part-time workers in total (Storage 1, Laundry 2), paid through the payroll service. Rentals has no employees (EV-006, EV-023) |
| Receipts | About $180,000 a year (fictional), all management fees: Storage $72,000, Rentals $48,000, Laundry $60,000. The LLCs' own revenue (fictional): Storage about $310,000, Rentals about $200,000, Laundry about $240,000. SBA counts the receipts of a concern and its affiliates (13 CFR 121.103(a)(6); 121.104(d)(1)); even combined, about $750,000 is far below the $45.5 million standard for NAICS 551112 (EV-022, EV-023) |
| Personal information held | **Storage:** about 610 current and former tenant records in the storage management system (name, address, phone, email, driver license number, gate code); about 230 scanned driver license copies from 2021 to 2024 in the shared file storage. **Rentals:** 12 current households; 47 rental application files (2023 to 2026) with Social Security numbers, driver license copies, pay stubs, bank statements, and tenant screening reports, downloaded as PDFs into the shared file storage. **Laundry:** about 140 wash-and-fold customers (name, phone, address) in the POS system; about 900 payment app accounts are held by the payment vendor. **Employees:** 3 current and 5 former LLC employees (SSNs, bank accounts) in the payroll service, plus scanned new-hire forms in the file storage (EV-006, EV-007, EV-008, EV-009, EV-031) |
| Card payments | Storage takes cards through the storage system's integrated processor (hosted payment fields). Laundry's machine readers and app are run by the laundry payment vendor. The owner stores no card numbers. PCI DSS duties are contractual (merchant agreements) and are noted, not assessed (EV-017) |
| Florida breach law status | Determined in the intake obligations register (FL-501.171). Each LLC is a **covered entity** under Fla. Stat. 501.171(1)(b) for its own tenants, customers, and employees. The sole proprietorship maintains and processes that information for the LLCs under the management agreements, so it is also their **third-party agent** (501.171(1)(h)). The definition of covered entity names a sole proprietorship expressly |
| Federal rules that reach an LLC | Determined in the intake obligations register (FCRA-1681b, FCRA-1681m, FTC-682.3, FHA-3604). **Rentals** uses consumer reports to screen applicants: the Fair Credit Reporting Act user duties (permissible purpose, 15 U.S.C. 1681b(a)(3)(F)(i) and 1681b(f); adverse action notices, 1681m(a)) and the FTC Disposal Rule (16 CFR 682.3) apply. The Fair Housing Act (42 U.S.C. 3604) applies to Rentals' tenant selection: the units are in duplexes, not single-family houses, and the owner lives in none of them, so neither exemption in 42 U.S.C. 3603(b) fits |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): SEC Regulation S-K Item 106, Form 8-K Item 1.05, and SOX section 404 (no securities registered; not an issuer). Federal Reserve Regulation Y Subpart N and 12 CFR Part 225 Appendix F (no bank). HIPAA (no group health plan; no LLC is a health care provider). FTC Safeguards Rule (no LLC is a financial institution under 16 CFR 314.2(h): none extends consumer credit, brokers loans, or gives financial advice, and Rentals maintains and repairs its units, so its leases are not the nonoperating leases in 12 CFR 225.28(b)(3)). Florida Digital Bill of Rights (a controller must exceed $1 billion in global gross annual revenue) |
| Contrast worth noting | The test is the activity, not the size. If Rentals began owner-financing sales of its duplexes, or Laundry opened its own customer credit accounts, that LLC could become a financial institution under 16 CFR 314.2(h) if it were significantly engaged in that activity, and the Safeguards Rule would follow |
| State law approach | Florida law is cited only where unavoidable (breach notice, data security, and disposal, Fla. Stat. 501.171) |

## 2. People and contracted services (role titles only)
| Role | Duties |
|---|---|
| Owner-manager | Every role for the sole proprietorship and, as sole member and manager, for each LLC: risk acceptor, security lead, incident lead, policy approver, and administrator of every system |
| Designated successor manager | Named in each LLC operating agreement to manage the LLCs if the owner is incapacitated. Has no system access and no written instructions today (EV-003, EV-014, EV-015) |
| Storage facility manager (part-time employee of Storage) | Runs the Storage office: move-ins, payments, gate codes. Manager role in the storage system; a mailbox in the productivity suite (EV-001, EV-007) |
| Laundry attendants (2 part-time employees of Laundry) | Wash-and-fold orders on the POS tablet; use one shared POS PIN and the shared Laundry mailbox (EV-001, EV-009) |
| Outside bookkeeper (contractor) | Monthly reconciliations and payroll entry for all four entities. Accountant user in the accounting service with full access to all four company files; payroll entry role. No written confidentiality or security terms (EV-004, EV-006, EV-016) |
| Outside CPA firm | Annual tax returns. Receives year-end files through its own client portal |
| On-call IT technician (hourly contractor) | Help with the laptop, Storage desktop, routers, and the gate controller on request. No standing access; uses a remote-support tool the owner starts (EV-016) |
| Business attorney | Prepares the LLC agreements and management agreements; refers a privacy attorney for breach questions |
| Rentals maintenance contractor | Repairs at the duplexes. Receives tenant names and phone numbers by text. No system access |

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv).

| ID | System | Hosting | Personal information? | Notes |
|---|---|---|---|---|
| SYS-01 | Productivity suite (email, files, calendar, and identity for the suite), business plan | SaaS | Yes: rental applications, driver license scans, new-hire forms, tenant and vendor correspondence | One tenant with four email domains (one per entity). Mailboxes: owner (administrator), Storage manager, shared Laundry mailbox. Owner uses text-message MFA; the other two have no MFA. Deleted items kept 30 days; no independent backup (EV-001, EV-002) |
| SYS-02 | Accounting service with four company files | SaaS | Vendor bank details; employee pay data | The back-office system of record for all four entities (it plays the ERP role at this size). Bank feeds. Vendor enforces authenticator-app MFA. Vendor has a SOC 2 Type 2 report (EV-004, EV-020) |
| SYS-03 | Online banking: four business accounts at one bank | Bank-hosted | Account credentials | One online profile; the owner sees and pays from all four accounts. The bank requires a one-time code for wires and new payees. The owner is the only user, so dual approval is not possible (EV-005) |
| SYS-04 | Payroll service: two employer accounts (Storage, Laundry) | SaaS | Employee SSNs, bank accounts, tax forms | Vendor enforces MFA. Bookkeeper enters hours (EV-006) |
| SYS-05 | Storage management system with online rentals, autopay, and gate access integration | SaaS | Tenant records with driver license numbers; gate codes | Users: owner (administrator), Storage manager, and a former storage assistant's account still active. MFA available, not turned on (EV-007, EV-AC-2) |
| SYS-06 | Property management platform (Rentals) | SaaS | Applications, screening reports, leases, rent payments | Listings, applications, tenant screening ordered through the platform's consumer reporting agency partner, leases, rent by ACH, tenant portal. Owner is the only user; text-message MFA (EV-008, EV-026) |
| SYS-07 | Laundry POS and machine payment platform | SaaS | Wash-and-fold customer contacts | POS app on one tablet; card and app readers on the machines; customer app accounts held by the vendor. Owner is administrator; attendants share one PIN (EV-009) |
| SYS-08 | Owner laptop and phone | Owner devices | Yes (downloads, cached mail and files) | Laptop full-disk encryption on; built-in antivirus; automatic updates. Phone receives MFA codes. Passwords saved in the browser; no password manager (EV-010) |
| SYS-09 | Site devices and networks | On premises | Yes (Storage desktop) | Storage office desktop (one shared local account with no password; no disk encryption); Laundry POS tablet; internet routers at the Storage office and the laundromat (laundromat customer Wi-Fi on the same network as the POS tablet and payment hub); gate controller at Storage (installer default administrator password, EV-IA-5); home office Wi-Fi (EV-011, EV-012, EV-032) |
| SYS-10 | Generative AI assistant (add-on to SYS-01) | SaaS | Yes (whatever the owner's account can open) | Turned on by the owner on 2026-06-01 for the owner's account only. Can read the owner's mail and files for all four entities (EV-027). See P10 |

**SSP system (P02):** the *Shared Back-Office Platform*: SYS-01 to SYS-04, SYS-08, and SYS-10, plus the owner's administrator access to the LLC systems SYS-05 to SYS-07 and the site devices in SYS-09.

## 4. Where the evidence is
This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Every item has a source system, an owner, and as-of and collected dates. For a one-person holding business the sources are the SaaS vendors' admin consoles and reports, online banking and its statements, the inbox, the signed agreements folder, the device settings screens, the owner's walk-through of the two sites, and the insurance agent's portal.
- **Which rules apply** to each entity is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps against the CSF 2.0 portfolio profile and the binding rules** are judged in the gap analysis (P03), and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

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
| 2026-07-20 to 2026-07-24 | Intake: the owner collects SaaS and banking settings and reports, statements, agreements, insurance records, device settings, the AI assistant's settings and history, and a walk-through of both sites; inventories; obligations register. The IT technician's confidentiality and security agreement was signed 2026-07-24 |
| 2026-07-27 to 2026-07-31 | Self-assessment by the owner with the on-call IT technician (tests on 2026-07-30): BIA worksheet (2026-07-27 to 2026-07-28), site walk-through (2026-07-28), settings review (2026-07-29), gap analysis self-review (2026-07-29 to 2026-07-30), AI use assessment (2026-07-30), risk register completed (2026-07-31) |
| 2026-08-03 to 2026-08-28 | POL-01 drafted from the gaps and the test results |
| 2026-08-31 | Deliverables and POL-01 adopted by the owner-manager (POL-01 effective 2026-09-01) |
| 2027-02 (planned) | Follow-up check: operating effectiveness of the controls POL-01 introduced, after at least one quarter of operation |

## 7. Facts added while building the deliverables
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| IT technician terms | The on-call IT technician signed a written confidentiality and security agreement on 2026-07-24, before the self-assessment began (EV-016) | P01, P02, P03, P07, P08 |
| Former storage assistant | The former storage assistant left on 2026-01-16. The account stayed enabled in the storage system until the owner disabled it during the P07 test on 2026-07-30 (EV-006, EV-007, EV-AC-2) | P01, P02, P04, P07 |
| Bookkeeper access | Since 2025 the owner releases every payment; the bookkeeper prepares a payables list and enters payroll hours. The bookkeeper's accountant user also held the company administrator role in all four company files (found 2026-07-29, removed 2026-08-12); reducing the accountant role is still open (EV-004, EV-005, EV-SA-9) | P05, P07, P09 |
| Accounting service assurance | The accounting service's SOC 2 Type 2 report (Security, Availability, Confidentiality; period ending 2026-03-31; unqualified; one deprovisioning exception at the vendor) was reviewed on 2026-07-29. Stated RTO 12 hours, RPO 1 hour (EV-020) | P02, P04, P09 |
| Operating figures | Storage rent about $850 a day, with autopay on the 1st. Laundry revenue about $660 a day, about 60% by card or app; coin acceptors keep machines running. Rentals rent about $16,700 a month, due on the 1st. LLC payroll every second Friday. The gate controller keeps existing codes working when the storage system is down (EV-006, EV-008, EV-012, EV-024, EV-025) | P05, P08 |
| People with Florida personal information | About 670: Storage about 610 tenant records (the about 230 license scans are of tenants in that group), Rentals 47 applicants, LLC employees 8 (3 current, 5 former) (EV-006, EV-007, EV-008, EV-031) | P02, P03, P08 |
| Former payroll provider | The LLCs used a different payroll provider until 2024. That account was never closed and still holds former employees' records (EV-030) | P03, P07 |
| Missed alert | An unfamiliar sign-in alert for the owner's email in May 2026 was deleted unread (EV-034) | P03, P07, P09 |
| Site details | The Storage desktop is 7 years old. The gate logs each code entry in the storage system. According to the installer, the gate controller is reachable only from the Storage office network. Site equipment at the Storage office sits on the floor (EV-007, EV-011, EV-012, EV-029) | P01, P03 |
| Device disposal | One laptop was traded in during 2025 with no wipe record (EV-013) | P03, P09 |
| Unit 4B decision | The owner chose the unit 4B applicant on 2026-07-16; the two declined applicants each failed the screening criterion and received the platform's adverse action notice that day. The owner wrote tenant selection criteria (income, rental history, screening result) on 2026-07-30 and re-checked the decision against them (EV-026, EV-035) | P01, P03, P10 |
| AI assistant use | Before the assessment the owner used the assistant to draft Storage delinquency reminders, laundromat signs, and rental listings and to summarize leases and contracts. The vendor's business terms exclude training on customer prompts and files (EV-019, EV-027) | P10 |
| Screening recommendation (AI-002) | The screening partner shows an accept, decline, or conditional recommendation with each report; its basis has not been disclosed to the owner (EV-026) | P10 |
| Retention rules | Set by the owner in POL-01 8.7: declined and withdrawn applications 2 years after the decision; signed tenants' applications for the lease term plus 2 years; former Storage tenant records 3 years after move-out; license scans not kept once the number is in the storage system; new-hire forms only in the payroll service | P06, P10 |
| Costs | Password manager about $40 a year; backup service about $150 a year; two hardware keys about $100 once; two extra suite licenses about $150 a year; encrypted drive about $80 once; gate installer visit about $120; business attorney about $300 for the bookkeeper terms | P01, P07 |
| Staff interviews | On 2026-07-30 the Storage manager and the Laundry attendants were each asked whom they would call about a suspicious email and whether they share a PIN (EV-IR-6) | P07, P09 |
| Cyber insurance | None today (EV-018, EV-021). The owner will get quotes for one policy covering all four entities by 2026-12-31 | P01, P08, P09 |
