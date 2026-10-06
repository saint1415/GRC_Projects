# Scenario facts: Cris Santos Company | Arts, Entertainment, and Recreation | Enterprise

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a law, regulation, standard, or card brand rule, the citation is given. Facts about the acquirer, the processors, the merchant agreement, clients, and vendors are fictional.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (publicly traded SEC registrant; live entertainment company that operates venues, promotes events, and runs its own ticketing platform) |
| Business | Promoter of live events with its own facilities (NAICS 711310). Operates **36 venues**: 6 arenas, 10 amphitheaters, 14 theaters and music halls, and 6 clubs. 28 are owned or leased; 8 are operated for public owners (cities, counties, and a state university) under venue management agreements. Also produces 3 annual multi-day festivals on leased grounds. Runs an **in-house ticketing platform** used for its own events and licensed to about 340 client venues and promoters (white-label ticketing) |
| Location | Headquartered in Florida. Venues in Florida (9) and 7 other states (Georgia, Alabama, South Carolina, North Carolina, Tennessee, Louisiana, and Arizona). Ticket buyers live in all 50 states. **State law is handled generically:** apply the law of each state where affected individuals reside, with Florida as the worked example |
| Activity | About 5,400 ticketed events a year at its own venues and festivals, with about 19 million attendees. The platform issues about 52 million tickets a year: about 21 million for the company's own events and about 31 million for client venues |
| Workforce | 12,000 employees: about 4,100 full-time (corporate, ticketing technology, venue management) and about 7,900 part-time and seasonal event staff (box office, ushers, food and beverage, guest services). Contracted security and crowd management staff are not employees |
| Revenue | About $4.8 billion a year (fictional): event promotion and own-event ticket sales $2.4 billion; ticketing service fees $0.9 billion; food, beverage, and merchandise $0.8 billion; sponsorship and premium seating $0.5 billion; venue management fees and other $0.2 billion. Not small under the SBA standard for NAICS 711310 ($40.0 million; 13 CFR 121.201) |
| Patrons | About 41 million patron accounts on the platform, about 16 million active in the last 24 months, and about 11 million active mobile app installs. Accounts require age 18 or older |
| Card acceptance and PCI DSS | **Merchant:** about 49 million card transactions a year for the company's own events and venues (about 18 million ticket orders and about 31 million food, beverage, and merchandise sales); Visa is about 52% (about 25 million). **Service provider:** the platform's payment service transmits card data for about 15 million client ticket orders a year (Visa about 7.8 million), for which client venues are the merchants of record. Visa defines a Level 1 merchant as one with more than 6 million Visa transactions a year and a Level 1 service provider as one that stores, processes, or transmits more than 300,000 Visa transactions a year (Visa Account Information Security program page and *What To Do If Compromised* v10.0, effective 2026-06-25). The company is therefore a **Level 1 merchant** (annual Report on Compliance by a QSA and an attestation of compliance) and a **Level 1 service provider** (annual on-site assessment and an AOC signed by the company and the QSA, submitted to Visa). PCI DSS v4.0.1 applies by contract; it is not law |
| Payment design | Online and app checkouts (own brand and client white-label sites) collect card data in payment fields served by the company's **payment service** from a dedicated payment domain. The payment service sends card data to a third-party tokenization and vault provider and to two processors, and keeps only tokens and truncated card numbers. Box office and stand sales use a PCI-listed validated P2PE solution at 30 venues; the 6 acquired venues still use legacy card readers on Windows POS terminals. Phone sales are keyed by contact center agents into an agent payment page |
| SEC status | Publicly traded; files Form 10-K (fiscal year ends December 31). Form 8-K Item 1.05 and Regulation S-K Item 106 apply. SOX IT general controls are tested annually |
| Not in scope | **Gaming** (Nevada Reg. 5.260, NIGC MICS, casino BSA/AML): the company runs no casino, gaming, or wagering. **COPPA:** websites and the app are general audience and accounts require age 18 or older. **HIPAA:** first aid is provided by contracted ambulance services. **Federal contracts:** none |
| Added at this size | Level 1 merchant and Level 1 service provider PCI DSS validation; SEC cybersecurity disclosure; SOX IT general controls; two service lines offered to business clients (P09); growth by acquisition (a 6-venue regional operator acquired on 2026-02-02) |

## 2. People (role titles only)
| Role | Duties |
|---|---|
| Board (audit committee and risk committee) | Cyber oversight (Item 106 disclosure); the risk committee approves risk appetite |
| Chief Executive Officer; Chief Financial Officer | Accept Very High risk; materiality determinations with the disclosure committee |
| Chief Information Security Officer (CISO) | Security program owner; reports to the CEO and quarterly to the board risk committee |
| Chief Privacy Officer | Privacy program, patron data, breach determinations |
| Chief Risk Officer | Enterprise risk management (ERM); owns the enterprise risk register |
| Chief Technology Officer (CTO) | Owns ticketing platform engineering and the payment service |
| President, Ticketing | Business owner of the ticketing platform and the white-label ticketing service line (SL-1) |
| Director of Payments and PCI Compliance | PCI DSS program owner (in the GRC team); QSA, acquirer, and card brand liaison |
| GRC team (11), Security Operations Center (24x7, in-house plus MSSP overflow), Internal Audit (in-house) | Three lines model |
| Disclosure committee | Form 8-K materiality decisions (General Counsel chairs) |

## 3. Systems
| ID | System | Notes |
|---|---|---|
| SYS-01 | Ticketing platform (built in-house, cloud-native, on Cloud provider A) | Event and seat-map setup, inventory, web and white-label checkout, patron accounts, mobile app back end, digital tickets and access control scanning, transfer and resale, **dynamic pricing service**, **bot defense and virtual queue**. About 9,400 client user accounts at about 340 clients |
| SYS-02 | Payment service (in-house, separate cardholder data environment accounts on Cloud provider A) | Payment fields, agent payment page, tokenization and vault provider, two processors. Stores tokens and truncated card numbers only |
| SYS-03 | Venue point of sale | Box office devices and food, beverage, and merchandise POS. Validated P2PE at 30 venues; legacy non-P2PE readers on Windows POS terminals at the 6 acquired venues |
| SYS-04 | Identity platform (SSO, MFA, privileged access management, identity governance) | Workforce identities; the 6 acquired venues are still on a legacy directory |
| SYS-05 | Multi-cloud estate (two public cloud providers, vendor-agnostic) plus 2 colocation data centers | Cloud A: ticketing and payments. Cloud B: data warehouse, marketing customer data platform, analytics and AI services. DC-1 (Florida) and DC-2 (Georgia): network core, legacy venue systems, offline backup copies |
| SYS-06 | Venue networks and operational technology | SD-WAN to 36 venues; temporary festival networks; public Wi-Fi; building management, turnstile and access control, and CCTV (about 8,600 cameras) |
| SYS-07 | Endpoints | About 13,000 workstations and laptops, about 7,500 handheld scanners and POS handhelds, about 2,000 managed phones and tablets |
| SYS-08 | ERP, payroll, and human capital management (SaaS) | SOX-relevant |
| SYS-09 | Contact centers | In-house center in Florida (about 380 seats) and an outsourced overflow center (about 220 seats) on a cloud contact center platform with call recording |
| SYS-10 | Marketing technology | Email and SMS services, tag manager, advertising pixels, customer data platform (Cloud B) |
| SYS-11 | Third parties | About 1,450 vendors; 230 handle patron, card, or employee data |
| SYS-12 | AI portfolio (13 use cases) | Governed by an AI governance committee formed in 2025 |

**SSP system (P02):** the *Ticketing and Venue Operations Platform (TVOP)*: the ticketing platform (SYS-01) and the payment service (SYS-02) on Cloud provider A, the box office and access control channel at all 36 venues (box office devices in SYS-03 and scanners in SYS-07), and the contact center agent payment page (SYS-09), inheriting common controls from the enterprise identity, cloud, security operations, network, endpoint, facilities, human resources, third-party risk, and GRC programs.

## 4. Current security posture: mostly compliant, with targeted gaps
**In place today:**
- A security program aligned to CSF 2.0 and integrated with ERM (NIST IR 8286)
- A policy hierarchy of policies, standards, procedures, and exceptions
- 24x7 SOC with an MSSP for overflow
- Privileged access management and phishing-resistant MFA for administrators
- Quarterly access certification for the cardholder data environment
- Immutable backups and annual disaster recovery tests for tier-1 systems
- 2025 PCI DSS Reports on Compliance (merchant and service provider) with a Compliant result; passing quarterly ASV scans
- Tokenization by design: no stored card numbers in platform databases
- Validated P2PE at 30 of 36 venues
- Edge bot management and a virtual queue for high-demand on-sales
- SOC 2 Type 2 report for the white-label ticketing service line (SL-1) since 2025
- Tiered third-party risk program
- Item 106 disclosure in the Form 10-K and a standing disclosure committee

**Targeted gaps:**
1. **Acquired venues.** The 6 venues acquired on 2026-02-02 (AV-01 to AV-06) run legacy non-P2PE card readers and Windows POS terminals on flat networks with local administrator accounts and a legacy directory. They entered the merchant cardholder data environment on day one. Migration is due 2027-03-31.
2. **Payment page scripts on client templates.** Script authorization and change detection (PCI DSS 6.4.3 and 11.6.1) cover the company's own-brand checkout, but white-label client templates let clients load their own tag containers on the checkout page shell.
3. **Card numbers in unexpected places.** Full card numbers sit in contact center case notes and in call recordings at the outsourced overflow contact center, which has no keypad (DTMF) masking.
4. **Client and service accounts.** MFA is optional for client users of the platform, client integration API keys are long-lived, and data warehouse service accounts use passwords without network restrictions.
5. **Third parties.** 58 of 230 data-handling vendors are overdue for reassessment; marketing tag vendors are outside the third-party risk program; the outsourced contact center's PCI DSS AOC has expired.
6. **Venue operational technology.** Building management, turnstile controllers, and CCTV share network segments with venue corporate networks at 14 venues, and the venue OT inventory is about 70% complete.
7. **AI.** 13 AI use cases, but only 8 have completed AI governance committee review. Dynamic pricing has not been tested for accessible seating price parity at every venue, and the bot challenge has not been tested with assistive technology.
8. **Materiality for service-provider incidents.** The materiality playbook does not cover incidents where the company is a service provider to client venues, and the disclosure committee has not exercised a payment card breach scenario.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 | PCI DSS v4.0.1 as a Level 1 merchant and a Level 1 service provider (primary), plus SEC Item 1.05 and Item 106, FTC Act Section 5, the FTC Rule on Unfair or Deceptive Fees (16 CFR Part 464), ADA ticketing rules (28 CFR 36.302(f)), the BOTS Act (15 U.S.C. 45c), and state breach and privacy laws; gaming and COPPA rules documented as not applicable |
| P08 | Ticketing platform breach exposing customer and card data: an e-skimming script loaded through a compromised third-party tag on client checkout templates, combined with a patron data export from the data warehouse using a stolen service account credential. Includes an **SEC materiality assessment and Form 8-K Item 1.05** step, card brand duties as merchant and as service provider, client notifications, and multi-state breach notification |
| P09 | SOC 2 Type 2 readiness across two service lines offered to business clients: SL-1 white-label ticketing and SL-2 venue management services for public owners |
| P10 | Enterprise AI portfolio (13 use cases) under the AI governance committee, with a full assessment of AI-001 dynamic ticket pricing and AI-002 bot detection and virtual queue (the registry default use case, split into two inventory rows) |
| Cloud | Multi-cloud (vendor-agnostic) with common controls; AWS, Azure, and Google Cloud names appear only in an equivalents table |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-06-01 to 2026-07-31 | Enterprise risk analysis and regulatory gap analysis (including the PCI DSS pre-assessment) |
| 2026-07-13 to 2026-08-28 | Control assessment (Internal Audit, third line) |
| 2026-08-17 to 2026-08-28 | SOC 2 readiness review and AI governance committee review |
| 2026-09-10 | Results to the audit committee and the risk committee of the board |
| 2026-10-19 to 2026-11-25 | QSA fieldwork for the 2026 merchant and service provider Reports on Compliance (planned) |
| 2026-12-31 | 2026 Reports on Compliance and AOCs due to the acquirer and Visa (fictional dates) |
