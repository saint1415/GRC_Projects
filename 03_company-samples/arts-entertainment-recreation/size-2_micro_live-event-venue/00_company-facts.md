# Scenario facts: Cris Santos Company | Arts, Entertainment, and Recreation | Micro

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a law, regulation, standard, or card brand rule, the citation is given. Facts about the acquirer, the merchant agreements, the MSP, and other vendors are fictional.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (live event venue operator with ticketing; one music club) |
| Business | Promoter of live events with its own facility (NAICS 711310). Operates **one leased music club** with one room: 650 standing, or 300 seated for about 20 seated shows a year. Books and promotes its own concerts and comedy nights, co-promotes with outside promoters, and rents the room for private and corporate events |
| Location | Florida. One building holds the room, the bar, the door box office, the green room, and a back office |
| Activity | About 150 shows a year on about 140 event nights. About 42,000 attendees and about 30,000 tickets sold a year. Doors usually open 1 hour before the first act |
| Workforce | 7 employees: the Owner and General Manager, the Venue Manager, the Box Office and Ticketing Manager, the Marketing Coordinator, the Bar Manager, the Production Manager, and a part-time Bookkeeper. About 20 event-night workers per show (bartenders, barbacks, door staff, and licensed security guards) come from two staffing contractors and are not employees |
| Revenue | About $1.1 million a year (fictional): tickets and ticket fees about $610,000, bar about $410,000, room rentals and merchandise commission about $80,000. Under the SBA standard of $40.0 million for NAICS 711310 (13 CFR 121.201), so SBA-small |
| Patrons | About 47,000 patron accounts on the ticketing platform (anyone who bought a ticket in the last 5 years) and about 18,000 email marketing subscribers. About 84% of ticket buyers have a Florida billing address; the rest live in other states |
| Ticket fees | Each ticket carries a $3.50 service fee and a $1.50 facility fee (fictional amounts). Both are mandatory |
| Card acceptance | About 57,000 card transactions a year through **two merchant accounts** with the same acquiring bank. **Ticketing account (MID-T):** about 13,500 online orders, about 2,600 door sales on show nights (card present), and about 300 phone orders a year. **Bar and merchandise account (MID-F):** about 40,600 card-present sales a year. Visa is about 55% of transactions (about 31,000 a year) |
| Merchant of record | The company is the merchant of record for ticket sales. Ticket revenue settles daily to the company's bank through the ticketing vendor's payment partner |
| PCI DSS status | **Merchant.** PCI DSS v4.0.1 (PCI SSC) applies through the merchant agreements. It is a contractual standard, not law. In a letter dated **2026-06-08** (fictional), the acquirer classified the company as a **Visa Level 3 merchant**. That matches Visa's table in *What To Do If Compromised* v10.0 (effective 2026-06-25): Level 3 merchants have 1 to 1,000,000 Visa transactions a year (Visa merged its former Levels 3 and 4 on 2024-04-25). Other brands' levels were not verified. **No SAQ has ever been filed for either account** since the accounts opened in 2023, and the acquirer has charged a monthly non-validation fee on each account since March 2024. The letter requires an SAQ and attestation of compliance (AOC) for each account by **2026-12-15**, and passing quarterly external vulnerability scans by an Approved Scanning Vendor (ASV) of the company website for MID-T (an acquirer requirement) |
| SAQ pre-selection | The acquirer's compliance portal pre-selected **SAQ A for MID-T** from the 2023 enrollment answers, which described the ticket account as "online only", and **SAQ P2PE for MID-F**. MID-T also carries door sales and phone orders. Whether SAQ A fits is the main question in P03 |
| Not in scope | **Gaming** (Nevada Reg. 5.260, NIGC MICS, BSA/AML for casinos): the club has no casino, gaming, or wagering. **COPPA:** the website and ticket pages are general audience, not directed to children, and accounts require age 18 or older. **HIPAA:** no health care services. **SEC disclosure:** privately held. **Federal contracts:** none. **Facial recognition:** the CCTV system does not use it |
| Other applicable law | FTC Act Section 5 (15 U.S.C. 45(a), (n)) for patron data security, privacy statements, and pricing claims; the FTC Rule on Unfair or Deceptive Fees (16 CFR Part 464, effective 2025-05-12), which covers live-event tickets; the BOTS Act (15 U.S.C. 45c), which protects the company as a ticket issuer; Florida breach notification (Fla. Stat. 501.171); Florida ticket statute (Fla. Stat. 817.36) only as noted in P10; ADA Title III ticketing rules (28 CFR 36.302(f)) as they affect pricing tools and sales channels |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notification, and the Florida ticket statute in P10). Other states are treated generically ("each state where affected individuals reside") |

## 2. People (role titles only)

| Role | Security and privacy duties |
|---|---|
| Owner and General Manager | Sole member of the LLC and talent buyer. Accepts Moderate risks and approves dated plans for High risks; approves policies and spending; will sign the 2026 SAQs and AOCs. Decision authority for P10 |
| Venue Manager | Part-time **Security and Privacy Lead** and PCI DSS contact (designated in writing on 2026-07-13). Runs event-night operations, the staffing contractors, CCTV, and the MSP relationship. Incident lead |
| Box Office and Ticketing Manager | Ticketing platform administrator: events, price tiers, the door box office, phone orders, the shared box office mailbox, and the demand tools settings. **P10 business owner** |
| Marketing Coordinator | Website content (with the freelance web designer), email marketing, social media, and advertising pixels |
| Bar Manager | Bar operations; owns the POS and the bar card readers |
| Production Manager | Sound and lighting; touring crew liaison |
| Bookkeeper (part-time) | Show settlements, artist payments, payroll, merchant statements, and the acquirer compliance portal |
| Managed service provider (MSP, external) | Help desk, the 5 office computers (patching, anti-malware, encryption), firewall and Wi-Fi, productivity suite administration, and the suite backup. Has remote access through its management tool |
| Ticketing platform vendor (external) | White-label ticketing SaaS. A PCI DSS validated service provider with a SOC 2 Type 2 report |
| Payment partner (external) | The ticketing vendor's payment gateway and tokenization partner for MID-T. Supplies the door card readers, which belong to its PCI-listed validated point-to-point encryption (P2PE) solution |
| POS vendor (external) | Cloud bar POS with a PCI-listed validated P2PE solution for MID-F |
| Freelance web designer (external) | Built the website in 2023 on a website builder SaaS; makes changes on request; shares the website administrator login |
| Staffing contractors (external, 2) | A hospitality staffing agency (bartenders, barbacks, door staff) and a licensed security contractor (guards) |

## 3. Systems

| ID | System | Hosting | Personal or card data? | Notes |
|---|---|---|---|---|
| SYS-01 | Ticketing platform: events, price tiers, seat maps for seated shows, online sales through a **checkout widget embedded in the company website** and on vendor-hosted event pages, box office app, scanning app, patron accounts, reports and exports, and a **"demand tools" module** (price recommendations and bot screening with an on-sale queue) | Vendor SaaS | About 47,000 patron accounts (name, email, phone, billing address, order history). Card data only inside the vendor's and payment partner's PCI environments; the company sees tokens and the last 4 digits | 9 venue user accounts with local passwords. MFA is available but not enforced. Vendor provides a PCI DSS AOC as a service provider and a SOC 2 Type 2 report (see section 7) |
| SYS-02 | Payment partner services for MID-T: gateway, tokenization, chargeback portal, and **2 Bluetooth card readers** paired with the door tablets | Service provider, plus readers on premises | Card data (encrypted in the reader) | The readers are part of the payment partner's PCI-listed validated P2PE solution (checked on the PCI SSC list on 2026-07-15) |
| SYS-03 | Bar POS: 2 fixed terminals and 2 handhelds with **4 P2PE card readers** and a vendor cloud back office | Vendor SaaS with devices on premises | Encrypted card data only (P2PE) | Manual card entry disabled. Bartenders share one clerk login per terminal |
| SYS-04 | Endpoints: 2 desktops (the **back-office PC**, shared by the Box Office and Ticketing Manager and the Bookkeeper, and the bar office PC), 3 laptops (Owner, Venue Manager, Marketing Coordinator), 2 door tablets running the box office app, and 3 handheld ticket scanners | On premises | **Card data typed by staff** on the back-office PC for phone orders; cached patron exports on 2 laptops | The 5 computers are MSP-managed. The tablets and scanners are not MSP-managed |
| SYS-05 | Productivity suite (email, files, chat) | SaaS | Yes (patron emails, artist contracts, settlement workbooks, patron exports) | 7 named users and **2 shared mailboxes** (box office and general info) |
| SYS-06 | Venue network | On premises | Card data in transit from the back-office PC | Small-business firewall and router with **one staff Wi-Fi** used by the office computers, door tablets, scanners, bar POS, and touring crews, plus a separate patron guest Wi-Fi (internet only). One business internet line |
| SYS-07 | Website | Website builder SaaS | Indirectly: event pages host the ticketing checkout widget | Built and maintained by the Marketing Coordinator and the freelance web designer. Event pages load **6 third-party scripts** (see gaps) |
| SYS-08 | Email marketing service | SaaS | Subscriber emails and preferences | About 18,000 subscribers; lists uploaded by hand from ticketing exports |
| SYS-09 | Finance and payroll | SaaS | Employee and vendor data | Accounting service and payroll service, used by the Bookkeeper |
| SYS-10 | CCTV | On premises | Video | 16 cameras and an on-premises recorder (21-day retention), viewable in a phone app by the Owner and Venue Manager |
| SYS-11 | Suite backup (the one cloud workload) | SaaS-to-SaaS backup service, resold and operated by the MSP | Yes (copies of SYS-05) | Daily backup of the named mailboxes and shared files with 30 days of versions |
| SYS-12 | Production consoles | On premises | No | Lighting and audio consoles, standalone (not networked). Show files on the consoles and on USB copies |

**SSP system (P02):** the *Ticketing and Venue Operations Platform (TVOP)*: the company's configuration and accounts in SYS-01, the door sales channel (SYS-02 readers and the door tablets), the back-office PC and other endpoints in SYS-04, SYS-05, SYS-06, SYS-07, and SYS-11, with interfaces to SYS-03, SYS-08, SYS-09, and SYS-10.

## 4. Current security posture: informal, basic hygiene, big gaps

**In place today:**
- Online card payments are entered only in the ticketing vendor's checkout widget or on vendor-hosted event pages. The company never sees full card numbers from online sales
- Door and bar card payments use PCI-listed validated P2PE readers. Manual card entry is disabled on the bar POS
- MSP patching, anti-malware, and firewall management for the 5 office computers
- MFA on the 7 named productivity suite accounts (enabled by the MSP in 2025)
- Patron guest Wi-Fi is separated from the staff network (internet only)
- Bot screening and an on-sale queue are switched on for on-sales, with a posted limit of 4 tickets per account
- Card receipts show only the last 4 digits of the card number
- CCTV covers the door box office, the bar, and the back office
- A cyber insurance policy with a breach hotline (bought in 2025; fictional terms)

**Missing or weak, found in the 2026 assessments:**
1. PCI DSS has never been validated for either merchant account. There is no documented PCI DSS scope (Requirement 12.5). The acquirer's portal pre-selected SAQ A for MID-T although the account also carries door sales and phone orders.
2. Phone orders: the Box Office and Ticketing Manager types callers' card numbers into the box office web app on the back-office PC, which is also used for email, web browsing, and bookkeeping, and sits on the staff Wi-Fi with touring crews.
3. Card numbers arrive by email. Patrons and corporate renters send card details to the shared box office mailbox for phone-style orders and rental deposits. P03 fieldwork found 23 emails with full card numbers since 2023, 9 of them with security codes.
4. The 9 ticketing platform accounts use local passwords with no MFA. One shared "door" login, used by contractor door staff on the tablets and scanners, can sell and refund tickets. The former Marketing Coordinator's account (left in March 2026) is still active.
5. The website administrator login is shared by the Owner, the Marketing Coordinator, and the freelance web designer, with no MFA. Event pages that host the checkout widget load 6 third-party scripts with no inventory or owner; one plugin has not been updated since 2024. SAQ A eligibility cannot be confirmed.
6. The two shared mailboxes allow direct sign-in with a shared password and no MFA.
7. One staff Wi-Fi carries the back-office PC, the door tablets, the scanners, the bar POS, and touring crews. Its password is posted in the green room and has not changed since 2023.
8. No written incident response plan. Nobody knows the merchant agreement's 24-hour compromise notice term (fictional) or the card brand procedures. The MSP contract has no incident notice term.
9. No security policies beyond one page on computer use in the 2021 employee handbook.
10. No security awareness training. Contractor door staff and bartenders get no card reader tamper training.
11. No inventory or inspection records for the 6 P2PE card readers, as the P2PE instruction manuals and PCI DSS 9.5 expect. P03 fieldwork found a third door reader, a spare, in an unlocked drawer and on no list.
12. No review of ticketing audit logs, mailbox sign-ins, or website changes. The ticketing platform keeps venue audit logs for 90 days.
13. The suite backup excludes the 2 shared mailboxes and has never been restore-tested. Patron exports are downloaded as files to the Owner's and the Marketing Coordinator's laptops; the Owner's laptop is not encrypted.
14. No list of service providers with their PCI DSS responsibilities. The payment partner's AOC has never been requested, the ticketing vendor's AOC and SOC 2 report have never been reviewed, and the web designer has no written security terms.
15. The demand tools' price recommendations have been used on 9 shows since April 2026 with no review of total-price display, price-change disclosure, artist price caps, or accessible ticket prices. Bot screening blocks are not reviewed and blocked patrons have no appeal route (P10).
16. Website event listings, emails, and social posts advertise the ticket price without the two mandatory fees (16 CFR 464.2(a)).

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 primary standard | PCI DSS v4.0.1 (contractual), with FTC Act Section 5 and the Rule on Unfair or Deceptive Fees (16 CFR Part 464) as the secondary regulation, and a one-row BOTS Act applicability check |
| P08 incident | Ticketing channel breach exposing customer and card data: a reused password opens the shared website administrator login and the Marketing Coordinator's ticketing account; the attacker places a fake payment form over the checkout widget on event pages and exports patron records. The MSP and the cyber insurer are in the notification chain |
| P09 SOC 2 | SOC 2 is **not** the company's assurance mechanism (PCI DSS validation is). (a) Security plus Confidentiality readiness self-assessment, used to answer a corporate rental client's security questionnaire; (b) review of the ticketing vendor's SOC 2 Type 2 report and PCI DSS AOC |
| P10 AI | One use case: AI-001, the ticketing platform's demand tools module (price recommendations and bot screening). **Adapted from the registry default** ("dynamic ticket pricing and bot detection"): at this size the company does not let software set prices on its own. The module recommends price tier changes and the Box Office and Ticketing Manager accepts or rejects each one. Bot screening runs automatically on on-sales. Both are one vendor module with one settings page and one owner, so they are assessed as one use case |
| Cloud | SaaS plus one cloud workload: the SaaS-to-SaaS suite backup (SYS-11), operated by the MSP. Vendor-agnostic |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-06-08 | Acquirer letter: Visa Level 3; an SAQ and AOC for each account and ASV scans for MID-T, due 2026-12-15 |
| 2026-07-13 to 2026-07-24 | BIA, risk assessment, and gap analysis with the MSP (show nights observed on 2026-07-17 and 2026-07-18; an on-sale observed on 2026-07-21) |
| 2026-08-10 to 2026-08-12 | Control assessment by an independent consultant (on site 2026-08-11, a dark night) |
| 2026-08-17 to 2026-08-21 | SOC 2 readiness self-assessment, vendor report review, and AI assessment |
| 2026-08-31 | Deliverables approved by the Owner and General Manager |
| 2026-12-15 | 2026 SAQs, AOCs, and ASV scan reports due to the acquirer |

## 7. Facts added while building the deliverables
These facts were added because the deliverables needed them. They do not change sections 1-6.

| Topic | Added fact | Used in |
|---|---|---|
| Ticketing accounts | The 9 venue accounts are: the Owner, the Venue Manager, and the Box Office and Ticketing Manager (all 3 administrators); the Marketing Coordinator (marketing role, which can export patron lists); the Bookkeeper (reports); the Production Manager (guest lists); the freelance web designer (marketing role, given for widget setup); the former Marketing Coordinator; and the shared "door" login (box office sales, refunds, scanning) | P01, P02, P07 |
| Former Marketing Coordinator | Left in March 2026. The ticketing account was found active on 2026-07-21 during the risk assessment and disabled that day; the audit log showed no sign-ins after the departure date | P01, P03, P07 |
| Web designer rights | The web designer's marketing role with patron export rights was found in P07 testing and the rights were removed on 2026-08-12. The designer will run weekly page checks for about $150 a month (fictional) | P07 |
| Vendor assurance | Ticketing vendor: PCI DSS service provider AOC dated 2026-03-12 (Compliant, QSA-assessed) and a SOC 2 Type 2 report for the 12 months ending 2026-03-31 (Security, Availability, Confidentiality; unqualified; 1 exception: 3 of 40 vendor access removals late). The system description states 99.9% monthly uptime, RTO 4 hours, RPO 15 minutes, and customer notice within 72 hours of confirming an incident. Both were downloaded from the vendor portal and reviewed on 2026-08-19. The payment partner's AOC was requested on 2026-08-14 and not received by the end of fieldwork | P02, P05, P09 |
| MSP contract | Covers help desk, the 5 office computers (patching, anti-malware, encryption), firewall and Wi-Fi, suite administration, and the suite backup, with a 4-business-hour response time. No recovery time commitment and no incident notice term. The backup console and firewall each use one MSP administrator login with a password only. The technician list and MFA on the remote management tool were requested and not received | P02, P04, P05, P07 |
| Non-validation fee | $39.95 per merchant account per month (fictional), about $960 a year for both accounts | P01 |
| Card data found | 23 emails with full card numbers (9 with security codes) in the box office mailbox since 2023, 4 of them forwarded to the Bookkeeper; 2 printed rental deposit forms with card numbers in an unlocked rentals binder. The MSP purged the emails and the forms were shredded on 2026-08-03. A repeat search on 2026-08-11 found none | P01, P03, P07 |
| Spare door reader | Found on 2026-07-22 in an unlocked back office drawer and locked in the back office safe the same day | P01, P03, P07 |
| Website scripts and privacy notice | The 6 scripts are an analytics tag, 2 advertising pixels, a chat widget, a newsletter pop-up, and a countdown timer plugin with no updates since 2024. A seventh script, a sponsor's tracking tag added by the web designer at the sponsor's request, was found on 2026-08-11. The 2023 privacy notice says patron information is never shared with third parties | P03, P04, P07, P08 |
| Forgotten API token | A 2024 API token for a former email marketing service, with patron read access, was still sending patron records every night to the company's lapsed account at that service. Found in P07 testing on 2026-08-11; revoked on 2026-08-12; written deletion requested from the former service | P01, P02, P04, P07, P09 |
| Shared passwords | The door login password was written on a card taped inside the door box office (removed 2026-08-12). Suite MFA uses push approval without number matching | P03, P07 |
| Network test | A laptop on the staff Wi-Fi reached the back-office PC's shared folder and both door tablets; a phone on the guest Wi-Fi reached no staff device (P07, 2026-08-11). The CCTV recorder's default password had been changed by the installer | P07 |
| Accessible tickets | Wheelchair spaces and companion seats for seated shows, and the 6 spaces on the accessible viewing platform for standing shows, are sold only by phone today. For pricing, the company treats the platform as part of the general admission section | P03, P10 |
| Demand tools use | Switched on 2026-04-06. Price recommendations used on 9 shows: 31 recommendations, 27 accepted, 4 rejected; 2 shows went above the artist-agreed cap (by up to 15%); on one show the platform tier rose $6 above general admission for 2 days (3 buyers; refund approved). Bot screening on 6 high-demand on-sales in the last 12 months, about 9,000 queue entrants across the last 2; 7 groups of linked accounts bought 61 tickets above the posted "limit 4 per customer"; challenge failure 4.1% on mobile carrier networks vs 1.3% on home broadband, 19% on VPN or privacy relays; audio challenge alternative switched off; the block page gives no contact route | P01, P03, P10 |
| Facility fee wording | The website FAQ describes the facility fee as a charge from the ticketing company, but the club keeps it for building upkeep | P03 |
| Corporate rental client | A regional employer booked the room for a November 2026 employee event and product reveal and will send an attendee list of about 550 names, work emails, and dietary and accessibility notes. Its TSC-based security questionnaire (Security and Confidentiality) arrived 2026-07-28 and is due 2026-09-30. Client attendee lists arrive in the shared info mailbox, where 2025 client lists are still kept | P09 |
| Assessor | The P07 assessor is an independent security consultant with payment card experience (not a QSA) on a fixed fee, not involved in P01 or P03, operating no control, and not the company's future ASV | P07 |
| Cyber insurance | The 2025 policy has a 24x7 breach hotline and panel breach counsel and forensics, and requires prompt notice before outside firms are hired. Whether it covers card brand assessments is not confirmed | P01, P08 |
| Q4 2026 budget | About $5,700 one-time and $2,160 a year (fictional): EDR $900 a year, training $500 a year, ASV scans $400 a year, failover router $400 plus $360 a year, MSP project time $1,800, assessment and policy work $3,500 | P01 |
| Show economics | About $7,300 of revenue per show, about $2,700 of it from the bar; about 85% of bar sales by card. The door and bar accept cash as a fallback. Settlements are done on show night in a workbook in the suite, and artists are paid by bank transfer the next business day after the Owner approves. A cash reserve covers about 45 days of expenses | P05 |
| Payment link | The ticketing platform has a payment link feature that opens a vendor-hosted payment page; it will be used for rental deposits and callers instead of taking card numbers | P03, P06 |
| Screening | Background checks at hire for the Box Office and Ticketing Manager and the Bookkeeper; the security contractor screens its guards under its license; hospitality agency door staff are not screened | P02, P03 |
| Owner's laptop | Holds patron exports going back to 2024 and is the one office computer without encryption | P01, P07 |
| PCI DSS copy | The Venue Manager downloaded PCI DSS v4.0.1 from the PCI SSC document library under its license terms | P03 |
