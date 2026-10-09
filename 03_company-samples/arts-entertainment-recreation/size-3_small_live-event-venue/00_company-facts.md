# Scenario facts: Cris Santos Company | Arts, Entertainment, and Recreation | Small

All 11 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a law, regulation, standard, or card brand rule, the citation is given. Facts about the acquirer, the merchant agreement, and vendors are fictional.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (live event venue operator with ticketing) |
| Business | Promoter of live events with its own facility (NAICS 711310). Owns and operates **one venue building** with two rooms: **the Hall** (3,200 standing or 2,400 seated) and **the Lounge** (350 standing). Promotes and co-promotes concerts, comedy, and family shows, and rents the rooms for private and corporate events |
| Location | Florida. One building holds both rooms, the box office, the administrative offices, and the cash and settlement office |
| Activity | About 260 shows a year (about 150 in the Hall and 110 in the Lounge) on about 200 event days. About 400,000 attendees and about 330,000 tickets sold a year |
| Workforce | 60 employees: 10 management and administration (including the IT Manager and one IT technician), 7 booking and marketing, 9 ticketing and box office, 20 operations, production, and facilities, 8 food and beverage, 6 guest services. About 220 event-day workers (ushers, bartenders, stand cashiers, security guards) are supplied by two staffing contractors and are not employees |
| Revenue | $24.0 million a year (fictional): ticket sales and ticket fees about $13.9 million, food and beverage about $6.5 million, sponsorship, room rentals, and merchandise commissions about $3.6 million. Under the SBA standard of $40.0 million for NAICS 711310 (13 CFR 121.201), so SBA-small |
| Patrons | About 260,000 patron accounts on the ticketing platform (anyone who bought a ticket in the last 5 years) and about 140,000 email marketing subscribers. About 78% of ticket buyers have a Florida billing address; the rest live in other states (touring fans and visitors) |
| Card acceptance | About 610,000 card transactions a year across all brands (EV-024), through **two merchant accounts** with the same acquiring bank. **Ticketing account (MID-T):** about 150,000 online orders, about 16,000 box office window sales (card present), and about 5,000 phone orders a year. **Food, beverage, and merchandise account (MID-F):** about 440,000 card-present sales a year. The venue has been cashless since 2023. Visa is about 55% of transactions (about 335,000 a year) |
| Merchant of record | The company is the merchant of record for ticket sales. Ticket revenue settles daily to the company's bank through the ticketing vendor's payment partner. The ticketing vendor is not the merchant of record |
| PCI DSS status | **Merchant**, determined in the intake obligations register (N71-R04) from the merchant agreement and the acquirer's letter (EV-023, EV-021). PCI DSS v4.0.1 (PCI SSC) applies through the merchant agreement. It is a contractual standard, not law. In a letter dated 2026-05-18 (fictional), the **acquirer classified the company as a Visa Level 3 merchant**. That matches Visa's current table in *What To Do If Compromised* v10.0 (effective 2026-06-25): Level 3 merchants have 1 to 1,000,000 Visa transactions a year, because Visa merged its former Levels 3 and 4 into one Level 3 on 2024-04-25. Other brands' levels were not verified. The acquirer set the 2026 validation: an annual SAQ and attestation of compliance (AOC) for each merchant account, plus passing quarterly external vulnerability scans by an Approved Scanning Vendor (ASV) for MID-T. Both are due **2026-12-15** |
| SAQ decision (acquirer letter, 2026-05-18; EV-021) | **MID-F: SAQ P2PE.** All stand and bar card readers belong to a PCI-listed validated point-to-point encryption (P2PE) solution. **MID-T: SAQ D for Merchants.** The company filed SAQ A for MID-T in 2025 (EV-022). The acquirer rejected that for 2026 because MID-T also carries card-present box office sales and phone orders typed into box office PCs, and SAQ A covers only card-not-present channels that are completely outsourced. The letter says the acquirer will consider **SAQ A (online) plus SAQ P2PE (box office)** for MID-T once box office sales and phone orders move to a validated P2PE solution and the online checkout meets the SAQ A eligibility criteria. The SAQs used are the v4.0.1 versions published by PCI SSC (bulletin of 2024-10-15; SAQ A revised in January 2025) |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): the **gaming** rules (Nevada Reg. 5.260, NIGC MICS, BSA/AML for casinos), **COPPA**, **HIPAA**, **SEC disclosure**, and **federal contract** clauses do not apply. **Facial recognition:** the CCTV system does not use it (EV-042) |
| Other applicable law | Recorded in the intake obligations register: FTC Act Section 5 (15 U.S.C. 45(a), (n)) for patron data security, privacy statements, and pricing claims; the FTC Rule on Unfair or Deceptive Fees (16 CFR Part 464, effective 2025-05-12), which covers live-event tickets; the BOTS Act (15 U.S.C. 45c), which protects the company as a ticket issuer; Florida breach notification (Fla. Stat. 501.171); Florida ticket resale law (Fla. Stat. 817.36) only as noted in P10; ADA Title III ticketing rules for accessible seating (28 CFR 36.302(f)), as they affect dynamic pricing and bot challenges (P10) |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notification, and the Florida ticket statute in P10). Other states are treated generically ("each state where affected individuals reside") |

## 2. People (role titles only)

| Role | Security and privacy duties |
|---|---|
| Majority owner (Cris Santos) | Accepts High and Very High risks; signed the 2025 SAQs and will sign the 2026 AOCs |
| General Manager | Executive owner of the security program; approves policies; accepts Moderate risks |
| IT Manager | Part-time **Information Security Lead** and PCI DSS contact. Runs IT with one IT technician and a network and security integrator |
| Controller | Owns the merchant agreement, the acquirer relationship, SAQ submissions, show settlements, and the cyber insurance policy |
| Director of Ticketing | Owns the ticketing platform configuration, the box office, ticket pricing rules, per-account ticket limits, and the bot mitigation settings. **P10 business owner** |
| Marketing Director | Owns the website, email marketing, the patron marketing database, and the marketing agency relationship |
| Operations Director | Facilities, event-day operations, crowd safety, CCTV, door access control, and production systems |
| Food and Beverage Manager | Stand and bar operations; owns the POS and the P2PE card readers |
| HR and Payroll Specialist | Onboarding, terminations, training records, staffing contractor rosters |
| Ticketing platform vendor (external) | White-label ticketing SaaS. A PCI DSS validated service provider with a SOC 2 Type 2 report |
| Payment partner (external) | The ticketing vendor's payment gateway and tokenization partner for MID-T; supplies the box office card readers. A PCI DSS validated service provider |
| POS vendor (external) | Cloud POS for food, beverage, and merchandise, with a PCI-listed validated P2PE solution for MID-F |
| Marketing agency (external) | Three-person agency. Holds two accounts on the ticketing platform with the "marketing settings" permission, which can add tracking pixels and custom scripts to event and checkout pages |
| Network and security integrator (external) | Firewall, switches, Wi-Fi, CCTV, and door access control installation and support; has remote access |
| Staffing contractors (external, 2) | Supply event-day workers |

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv).

| ID | System | Hosting | Personal or card data? | Notes |
|---|---|---|---|---|
| SYS-01 | Ticketing platform: event and seat-map setup, online sales on vendor-hosted event and checkout pages under a venue-branded web address, box office web app, patron accounts, access control (barcode scanning), reporting and exports, **dynamic pricing module**, **bot mitigation and virtual queue** | Vendor SaaS | About 260,000 patron accounts (name, email, phone, billing address, order history). Card data only inside the vendor's and payment partner's PCI environments; the company sees tokens and truncated card numbers | 34 venue user accounts with local passwords. MFA is available but not enforced (EV-001, EV-002). The "marketing settings" permission lets users add scripts to checkout pages (EV-025). Vendor provides a PCI DSS AOC as a service provider (dated 2026-02-20) and a SOC 2 Type 2 report (Security, Availability, Confidentiality; 12 months to 2026-03-31) (EV-025, EV-026) |
| SYS-02 | Payment partner services for MID-T: gateway, tokenization, chargeback portal, and 4 USB card readers at the box office windows | Service provider, plus readers on premises | Card data | The box office readers encrypt card data but are **not part of a PCI-listed validated P2PE solution**, so the PCs they attach to are in PCI DSS scope. The partner offers a validated P2PE option with standalone devices that also allow key entry of phone orders (EV-027) |
| SYS-03 | Food, beverage, and merchandise POS: 38 P2PE card readers (26 fixed at bars and stands, 12 handheld) and a vendor cloud back office | Vendor SaaS with devices on a vendor-managed network segment | Encrypted card data only (P2PE) | Manual card entry disabled on the POS. Event-day bartenders use shared clerk logins per bar (EV-028) |
| SYS-04 | Box office workstations: 6 Windows PCs (4 ticket windows, 2 phone sales desk) | On premises | **Card data typed by staff** for phone orders; card data from the attached readers | On the corporate network segment with office PCs. Also used for email and web browsing (EV-011, EV-014) |
| SYS-05 | Cloud tenant (IaaS/PaaS) | Public cloud provider (vendor-agnostic) | Patron marketing data; settlement data | Patron marketing database (nightly copy of about 260,000 patron records through the ticketing API; no card data), show settlement web app (built by a contractor in 2023), serverless function for the nightly API pull, object storage for exports and settlement files, backup vault (EV-018) |
| SYS-06 | Identity provider (single sign-on and MFA) | SaaS | No (identities only) | Protects email, the productivity suite, the cloud console, the accounting system, and the email marketing service. **Not connected to SYS-01 or SYS-03** (EV-004) |
| SYS-07 | Productivity suite (email, files, chat) | SaaS | Yes (patron emails and exports as attachments) | Box office and guest services mailboxes |
| SYS-08 | Venue network | On premises | Card data in transit from SYS-04 | Firewall, switches, and Wi-Fi. Segments: corporate (office PCs **and** box office PCs), production, POS (vendor managed), CCTV and door access, and public guest Wi-Fi (internet only). Primary fiber and backup cable internet (EV-014) |
| SYS-09 | Endpoints | On premises | Yes (cached exports) | 48 Windows PCs and laptops (including the 6 box office PCs), 24 handheld ticket scanners managed through SYS-01, 10 tablets for operations and production (EV-011, EV-013) |
| SYS-10 | Physical security systems | On premises | Video; badge records | 96 CCTV cameras with an on-premises recorder (30-day retention) and a door access control system for staff doors, the box office, and the cash office (EV-042, EV-043) |
| SYS-11 | Website and email marketing | Vendor SaaS | Subscriber emails and preferences | Event calendar with "Buy tickets" links that send patrons to SYS-01 hosted pages. The email service receives a weekly subscriber list from SYS-05 |
| SYS-12 | Finance and HR | Vendor SaaS | Employee and vendor data | Accounting and payroll services |
| SYS-13 | Production systems | On premises | No | Lighting and audio consoles and video wall controllers on the production segment. Touring crews connect their own equipment there |

**SSP system (P02):** the *Ticketing and Venue Operations Platform (TVOP)*: the company's configuration and accounts in SYS-01, the box office channel (SYS-02 readers and SYS-04), SYS-05, SYS-06, SYS-08, and the administrator endpoints in SYS-09, with interfaces to SYS-03, SYS-07, SYS-10, and SYS-11.

## 4. Where the evidence is

This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Every item has a source system, an owner, and as-of and collected dates.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps against PCI DSS v4.0.1 and the FTC rules** are judged in the gap analysis (P03), and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 primary standard | PCI DSS v4.0.1 (contractual), with FTC Act Section 5 and the Rule on Unfair or Deceptive Fees (16 CFR Part 464) as the secondary regulation, and a one-row BOTS Act applicability check |
| P08 incident | Ticketing platform breach: takeover of a venue administrator account on the ticketing platform, followed by an export of patron records and a card-skimming script placed on the checkout page through the marketing settings |
| P09 SOC 2 | SOC 2 is **not** the company's assurance mechanism (PCI DSS validation is). (a) Security-only readiness check as an internal benchmark; (b) review of the ticketing vendor's SOC 2 Type 2 report and PCI DSS AOC |
| P10 AI | AI-001 dynamic ticket pricing and AI-002 bot detection and virtual queue, both modules of SYS-01. AI-001 runs in "auto-apply" mode on reserved-seat Hall shows only (46 shows since March 2026) and uses no patron-level data. AI-002 protects on-sales marked high demand (14 in the last 12 months) and keeps session records for 30 days |
| Cloud | Vendor-agnostic. Services are described by category, with AWS, Azure, and Google Cloud equivalents noted only for shared responsibility |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-05-18 | Acquirer letter: Visa Level 3; SAQ D for MID-T and SAQ P2PE for MID-F; due 2026-12-15 |
| 2026-06-29 to 2026-07-10 | Intake: evidence requests, exports, walk-throughs, inventories, obligations register |
| 2026-07-13 to 2026-07-24 | BIA interviews, risk assessment and gap analysis fieldwork (box office observed during an on-sale on 2026-07-17 and a show night on 2026-07-18) |
| 2026-07-27 to 2026-07-31 | Policies drafted from the gaps |
| 2026-08-03 to 2026-08-07 | Control assessment fieldwork: operating tests of controls already in place; design review of the draft policies |
| 2026-08-17 to 2026-08-21 | SOC 2 readiness benchmark, vendor report review, and AI assessment |
| 2026-08-31 | Deliverables and policies approved by the General Manager (High risks by the majority owner) |
| 2026-12-15 | 2026 SAQs, AOCs, and ASV scan reports due to the acquirer |
| 2027-02 (planned) | Follow-up assessment: operating effectiveness of the controls the new policies introduced, after at least one quarter of operation |
