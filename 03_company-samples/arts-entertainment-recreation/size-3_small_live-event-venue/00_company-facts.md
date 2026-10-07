# Scenario facts: Cris Santos Company | Arts, Entertainment, and Recreation | Small

All 10 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a law, regulation, standard, or card brand rule, the citation is given. Facts about the acquirer, the merchant agreement, and vendors are fictional.

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
| Card acceptance | About 610,000 card transactions a year across all brands, through **two merchant accounts** with the same acquiring bank. **Ticketing account (MID-T):** about 150,000 online orders, about 16,000 box office window sales (card present), and about 5,000 phone orders a year. **Food, beverage, and merchandise account (MID-F):** about 440,000 card-present sales a year. The venue has been cashless since 2023. Visa is about 55% of transactions (about 335,000 a year) |
| Merchant of record | The company is the merchant of record for ticket sales. Ticket revenue settles daily to the company's bank through the ticketing vendor's payment partner. The ticketing vendor is not the merchant of record |
| PCI DSS status | **Merchant.** PCI DSS v4.0.1 (PCI SSC) applies through the merchant agreement. It is a contractual standard, not law. In a letter dated 2026-05-18 (fictional), the **acquirer classified the company as a Visa Level 3 merchant**. That matches Visa's current table in *What To Do If Compromised* v10.0 (effective 2026-06-25): Level 3 merchants have 1 to 1,000,000 Visa transactions a year, because Visa merged its former Levels 3 and 4 into one Level 3 on 2024-04-25. Other brands' levels were not verified. The acquirer set the 2026 validation: an annual SAQ and attestation of compliance (AOC) for each merchant account, plus passing quarterly external vulnerability scans by an Approved Scanning Vendor (ASV) for MID-T. Both are due **2026-12-15** |
| SAQ decision (acquirer letter, 2026-05-18) | **MID-F: SAQ P2PE.** All stand and bar card readers belong to a PCI-listed validated point-to-point encryption (P2PE) solution. **MID-T: SAQ D for Merchants.** The company filed SAQ A for MID-T in 2025. The acquirer rejected that for 2026 because MID-T also carries card-present box office sales and phone orders typed into box office PCs, and SAQ A covers only card-not-present channels that are completely outsourced. The letter says the acquirer will consider **SAQ A (online) plus SAQ P2PE (box office)** for MID-T once box office sales and phone orders move to a validated P2PE solution and the online checkout meets the SAQ A eligibility criteria. The SAQs used are the v4.0.1 versions published by PCI SSC (bulletin of 2024-10-15; SAQ A revised in January 2025) |
| Not in scope | **Gaming** (Nevada Reg. 5.260, NIGC MICS, BSA/AML for casinos): the venue has no casino, gaming, or wagering. **COPPA:** the website and ticketing pages are general audience, not directed to children, and accounts require age 18 or older (family-show tickets are bought by adults). **HIPAA:** no health care services; first aid is provided by a contracted ambulance service. **SEC disclosure:** privately held. **Federal contracts:** none. **Facial recognition:** the CCTV system does not use it |
| Other applicable law | FTC Act Section 5 (15 U.S.C. 45(a), (n)) for patron data security, privacy statements, and pricing claims; the FTC Rule on Unfair or Deceptive Fees (16 CFR Part 464, effective 2025-05-12), which covers live-event tickets; the BOTS Act (15 U.S.C. 45c), which protects the company as a ticket issuer; Florida breach notification (Fla. Stat. 501.171); Florida ticket resale law (Fla. Stat. 817.36) only as noted in P10; ADA Title III ticketing rules for accessible seating (28 CFR 36.302(f)), as they affect dynamic pricing and bot challenges (P10) |
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

| ID | System | Hosting | Personal or card data? | Notes |
|---|---|---|---|---|
| SYS-01 | Ticketing platform: event and seat-map setup, online sales on vendor-hosted event and checkout pages under a venue-branded web address, box office web app, patron accounts, access control (barcode scanning), reporting and exports, **dynamic pricing module**, **bot mitigation and virtual queue** | Vendor SaaS | About 260,000 patron accounts (name, email, phone, billing address, order history). Card data only inside the vendor's and payment partner's PCI environments; the company sees tokens and truncated card numbers | 34 venue user accounts with local passwords. MFA is available but not enforced (see gaps). The "marketing settings" permission lets users add scripts to checkout pages. Vendor provides a PCI DSS AOC as a service provider (dated 2026-02-20) and a SOC 2 Type 2 report (Security, Availability, Confidentiality; 12 months to 2026-03-31) |
| SYS-02 | Payment partner services for MID-T: gateway, tokenization, chargeback portal, and 4 USB card readers at the box office windows | Service provider, plus readers on premises | Card data | The box office readers encrypt card data but are **not part of a PCI-listed validated P2PE solution**, so the PCs they attach to are in PCI DSS scope. The partner offers a validated P2PE option with standalone devices that also allow key entry of phone orders |
| SYS-03 | Food, beverage, and merchandise POS: 38 P2PE card readers (26 fixed at bars and stands, 12 handheld) and a vendor cloud back office | Vendor SaaS with devices on a vendor-managed network segment | Encrypted card data only (P2PE) | Manual card entry disabled on the POS. Event-day bartenders use shared clerk logins per bar |
| SYS-04 | Box office workstations: 6 Windows PCs (4 ticket windows, 2 phone sales desk) | On premises | **Card data typed by staff** for phone orders; card data from the attached readers | On the corporate network segment with office PCs. Also used for email and web browsing (see gaps) |
| SYS-05 | Cloud tenant (IaaS/PaaS) | Public cloud provider (vendor-agnostic) | Patron marketing data; settlement data | Patron marketing database (nightly copy of about 260,000 patron records through the ticketing API; no card data), show settlement web app (built by a contractor in 2023), serverless function for the nightly API pull, object storage for exports and settlement files, backup vault |
| SYS-06 | Identity provider (single sign-on and MFA) | SaaS | No (identities only) | Protects email, the productivity suite, the cloud console, the accounting system, and the email marketing service. **Not connected to SYS-01 or SYS-03** |
| SYS-07 | Productivity suite (email, files, chat) | SaaS | Yes (patron emails and exports as attachments) | Box office and guest services mailboxes |
| SYS-08 | Venue network | On premises | Card data in transit from SYS-04 | Firewall, switches, and Wi-Fi. Segments: corporate (office PCs **and** box office PCs), production, POS (vendor managed), CCTV and door access, and public guest Wi-Fi (internet only). Primary fiber and backup cable internet |
| SYS-09 | Endpoints | On premises | Yes (cached exports) | 48 Windows PCs and laptops (including the 6 box office PCs), 24 handheld ticket scanners managed through SYS-01, 10 tablets for operations and production |
| SYS-10 | Physical security systems | On premises | Video; badge records | 96 CCTV cameras with an on-premises recorder (30-day retention) and a door access control system for staff doors, the box office, and the cash office |
| SYS-11 | Website and email marketing | Vendor SaaS | Subscriber emails and preferences | Event calendar with "Buy tickets" links that send patrons to SYS-01 hosted pages. The email service receives a weekly subscriber list from SYS-05 |
| SYS-12 | Finance and HR | Vendor SaaS | Employee and vendor data | Accounting and payroll services |
| SYS-13 | Production systems | On premises | No | Lighting and audio consoles and video wall controllers on the production segment. Touring crews connect their own equipment there |

**SSP system (P02):** the *Ticketing and Venue Operations Platform (TVOP)*: the company's configuration and accounts in SYS-01, the box office channel (SYS-02 readers and SYS-04), SYS-05, SYS-06, SYS-08, and the administrator endpoints in SYS-09, with interfaces to SYS-03, SYS-07, SYS-10, and SYS-11.

## 4. Current security posture: partially compliant

**In place today:**
- Online card payments are entered only on the ticketing vendor's hosted checkout pages. The company's website only links to them
- Stand and bar card payments use a PCI-listed validated P2PE solution, with manual card entry disabled
- The ticketing vendor's service provider AOC (2026) and SOC 2 Type 2 report are on file
- MFA through the identity provider for email, the productivity suite, the cloud console, and accounting
- Public guest Wi-Fi is separated from all business segments (internet only)
- Signature anti-malware and automatic operating system updates on office and box office PCs
- Daily backups of the patron marketing database and settlement app, in the same cloud account
- Background checks for box office, cash office, and finance staff
- Bot mitigation, a virtual queue, and a posted limit of 6 tickets per account for high-demand on-sales
- Card receipts show only the last 4 digits of the card number
- CCTV covers the box office, the cash office, and all bars
- A cyber insurance policy with a breach hotline (fictional terms)

**Missing or weak, found in the 2026 assessments:**
1. MID-T was validated in 2025 with SAQ A even though it includes box office and phone order channels. There is no documented PCI DSS scope (Requirement 12.5.2). The acquirer requires SAQ D for MID-T in 2026 unless the scope is reduced.
2. The 6 box office PCs, where staff type phone order card numbers and where non-P2PE card readers are attached, sit on the corporate network segment with office PCs and are also used for email and web browsing. There is no segmentation between them and the rest of the network.
3. Phone order staff write card numbers, expiration dates, and security codes on paper slips for callbacks. P03 fieldwork found a binder with 41 slips dating back to March 2026.
4. The 34 venue user accounts on the ticketing platform use local passwords, and MFA is not enforced. One shared "boxoffice" login is used by seasonal sellers. P07 testing found 5 accounts of departed employees and agency staff still active.
5. The marketing agency can add tracking pixels and custom scripts to the vendor-hosted event and checkout pages. On 2026-07-21, 9 third-party scripts were active on the checkout page, none inventoried or approved, 2 with no known owner (relevant to Requirements 6.4.3 and 11.6.1 and to SAQ A eligibility).
6. No written incident response plan. Staff do not know the merchant agreement's 24-hour notice term (fictional) or the card brand compromise procedures.
7. No review of ticketing platform administrator activity, identity provider sign-ins, or cloud logs. The ticketing platform keeps venue audit logs for 90 days by default.
8. The nightly export function in the cloud tenant uses a ticketing API key with full administrator scope that has never been rotated. Patron database backups are in the same account as production and have never been restore-tested.
9. No security policies beyond a 2022 one-page acceptable use form.
10. No security awareness training beyond card reader tamper awareness for bar leads. Box office staff have no training on phone order card handling or phishing.
11. No internal vulnerability scanning and no external ASV scans. Two box office PCs run an operating system version that reaches end of vendor support in 2026-10.
12. The dynamic pricing module was switched on in March 2026 without a review of total-price display under the FTC fee rule, of price-change disclosures, or of fairness across patron groups. Bot mitigation blocks are not reviewed for false positives (P10).
13. No list of third-party service providers with their PCI DSS responsibilities and no annual check of their compliance status (Requirement 12.8). The payment partner's AOC on file is from 2024.
14. The P2PE card reader inventory has not been reconciled with the POS vendor's list, and device inspections are not recorded (Requirement 9.5.1). P03 fieldwork located 36 of the 38 listed readers.
15. The CCTV recorder and the door access controller still use the integrator's default administrator passwords and are reachable from the corporate segment (found during P07 testing).

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
| 2026-07-13 to 2026-07-24 | Risk assessment and gap analysis fieldwork (box office observed during an on-sale on 2026-07-17 and a show night on 2026-07-18) |
| 2026-08-03 to 2026-08-07 | Control assessment fieldwork |
| 2026-08-17 to 2026-08-21 | SOC 2 readiness benchmark, vendor report review, and AI assessment |
| 2026-08-31 | Deliverables approved by the General Manager (High risks by the majority owner) |
| 2026-12-15 | 2026 SAQs, AOCs, and ASV scan reports due to the acquirer |
