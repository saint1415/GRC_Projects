# Scenario facts: Cris Santos Company | Arts, Entertainment, and Recreation | Enterprise

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a law, regulation, standard, or card brand rule, the citation is given. Facts about the acquirer, the processors, the merchant agreement, clients, and vendors are fictional.

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
| Card acceptance and PCI DSS | **Merchant:** about 49 million card transactions a year for the company's own events and venues (about 18 million ticket orders and about 31 million food, beverage, and merchandise sales); Visa is about 52% (about 25 million). **Service provider:** the platform's payment service transmits card data for about 15 million client ticket orders a year (Visa about 7.8 million), for which client venues are the merchants of record. Visa defines a Level 1 merchant as one with more than 6 million Visa transactions a year and a Level 1 service provider as one that stores, processes, or transmits more than 300,000 Visa transactions a year (Visa Account Information Security program page and *What To Do If Compromised* v10.0, effective 2026-06-25). The company is therefore a **Level 1 merchant** (annual Report on Compliance by a QSA and an attestation of compliance) and a **Level 1 service provider** (annual on-site assessment and an AOC signed by the company and the QSA, submitted to Visa), determined in the intake obligations register (N71-R04) from the card volume report (EV-051). PCI DSS v4.0.1 applies by contract; it is not law |
| Payment design | Online and app checkouts (own brand and client white-label sites) collect card data in payment fields served by the company's **payment service** from a dedicated payment domain. The payment service sends card data to a third-party tokenization and vault provider and to two processors, and keeps only tokens and truncated card numbers. Box office and stand sales use a PCI-listed validated P2PE solution at 30 venues; the 6 acquired venues still use legacy card readers on Windows POS terminals (EV-053). Phone sales are keyed by contact center agents into an agent payment page |
| SEC status | Publicly traded; files Form 10-K (fiscal year ends December 31). Form 8-K Item 1.05 and Regulation S-K Item 106 apply. SOX IT general controls are tested annually |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): **Gaming** (Nevada Reg. 5.260, NIGC MICS, casino BSA/AML): the company runs no casino, gaming, or wagering. **COPPA:** websites and the app are general audience and accounts require age 18 or older. **HIPAA:** first aid is provided by contracted ambulance services. **Federal contracts:** none (EV-059) |
| Added at this size | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): Level 1 merchant and Level 1 service provider PCI DSS validation; SEC cybersecurity disclosure; SOX IT general controls; two service lines offered to business clients (P09); growth by acquisition (a 6-venue regional operator acquired on 2026-02-02) |

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
The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv).

| ID | System | Notes |
|---|---|---|
| SYS-01 | Ticketing platform (built in-house, cloud-native, on Cloud provider A) | Event and seat-map setup, inventory, web and white-label checkout, patron accounts, mobile app back end, digital tickets and access control scanning, transfer and resale, **dynamic pricing service**, **bot defense and virtual queue**. About 9,400 client user accounts at about 340 clients |
| SYS-02 | Payment service (in-house, separate cardholder data environment accounts on Cloud provider A) | Payment fields, agent payment page, tokenization and vault provider, two processors. Stores tokens and truncated card numbers only |
| SYS-03 | Venue point of sale | Box office devices and food, beverage, and merchandise POS. Validated P2PE at 30 venues; legacy non-P2PE readers on Windows POS terminals at the 6 acquired venues (EV-011, EV-053) |
| SYS-04 | Identity platform (SSO, MFA, privileged access management, identity governance) | Workforce identities; the 6 acquired venues are still on a legacy directory (EV-001, EV-006) |
| SYS-05 | Multi-cloud estate (two public cloud providers, vendor-agnostic) plus 2 colocation data centers | Cloud A: ticketing and payments. Cloud B: data warehouse, marketing customer data platform, analytics and AI services. DC-1 (Florida) and DC-2 (Georgia): network core, legacy venue systems, offline backup copies |
| SYS-06 | Venue networks and operational technology | SD-WAN to 36 venues; temporary festival networks; public Wi-Fi; building management, turnstile and access control, and CCTV (about 8,600 cameras) |
| SYS-07 | Endpoints | About 13,000 workstations and laptops, about 7,500 handheld scanners and POS handhelds, about 2,000 managed phones and tablets |
| SYS-08 | ERP, payroll, and human capital management (SaaS) | SOX-relevant |
| SYS-09 | Contact centers | In-house center in Florida (about 380 seats) and an outsourced overflow center (about 220 seats) on a cloud contact center platform with call recording |
| SYS-10 | Marketing technology | Email and SMS services, tag manager, advertising pixels, customer data platform (Cloud B) |
| SYS-11 | Third parties | About 1,450 vendors; 230 handle patron, card, or employee data (EV-036) |
| SYS-12 | AI portfolio (13 use cases) | Governed by an AI governance committee formed in 2025 (EV-055) |

**SSP system (P02):** the *Ticketing and Venue Operations Platform (TVOP)*: the ticketing platform (SYS-01) and the payment service (SYS-02) on Cloud provider A, the box office and access control channel at all 36 venues (box office devices in SYS-03 and scanners in SYS-07), and the contact center agent payment page (SYS-09), inheriting common controls from the enterprise identity, cloud, security operations, network, endpoint, facilities, human resources, third-party risk, and GRC programs.

## 4. Where the evidence is
This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Every item has a source system, an owner, and as-of and collected dates. At this size the sources are enterprise systems of record across the business units, the 2025 PCI DSS Reports on Compliance and QSA files, SOX and Internal Audit records, contracts with service providers, clients and public owners, and board and committee records.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv), reviewed by the General Counsel's office.
- **Gaps against PCI DSS v4.0.1 and the other applicable rules** are judged in the gap analysis (P03), and **whether controls work** is tested by Internal Audit in the control assessment (P07). Both cite evidence IDs.

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
| 2026-05-04 to 2026-05-29 | Intake: evidence requests, exports from systems of record, inventories, obligations register (reviewed by counsel) |
| 2026-06-01 to 2026-07-15 | BIA interviews and dependency review |
| 2026-06-01 to 2026-07-31 | Enterprise risk analysis and regulatory gap analysis (including the PCI DSS pre-assessment; gap analysis evidence sampling completed 2026-08-14) |
| 2026-06-22 to 2026-07-10 | 2026 revision of POL-01 to POL-05 drafted from the intake evidence and early risk and gap results |
| 2026-07-13 to 2026-08-28 | Control assessment (Internal Audit, third line): operating tests of controls in force under the current policy set; design review of the draft 2026 policy revisions |
| 2026-08-17 to 2026-08-28 | SOC 2 readiness review and AI governance committee review |
| 2026-09-10 | Results to the audit committee and the risk committee of the board; 2026 policy revisions approved (effective 2026-10-01) |
| 2026-10-19 to 2026-11-25 | QSA fieldwork for the 2026 merchant and service provider Reports on Compliance (planned) |
| 2026-12-31 | 2026 Reports on Compliance and AOCs due to the acquirer and Visa (fictional dates) |
| 2027-03 (planned) | Internal Audit follow-up: operating effectiveness of the controls the 2026 policy revisions and POA&M items introduced, after at least one quarter of operation |

## 7. Facts added for the deliverables
These facts were added while building the deliverables. They do not change sections 1-6.

**Registry defaults.** The registry's primary system (ticketing and venue operations platform), P08 incident (ticketing platform breach exposing customer and card data), and P10 use case (dynamic ticket pricing and bot detection) fit this company and were kept. At this size the P10 use case is split into two inventory rows (AI-001 pricing and AI-002 bot detection) because they have different owners, data, and failure modes, and both sit inside a 13-use-case portfolio. The P08 incident combines e-skimming on client checkout templates with a data warehouse export because those are the two Very High and High card and patron data risks in P01 (R-001, R-003).

**Volumes and money.** Gross ticket sales through the platform are about $4.6 billion a year ($2.0 billion own events, $2.6 billion client events), about $12.6 million on an average day ($5.5 million own, $7.1 million client) and 3 to 4 times that on peak on-sale days. Revenue of about $4.8 billion a year is about $13.2 million per calendar day. About 140 high-demand on-sales, about 3,500 event days, and about 5,400 show settlements a year. A major tour on-sale grosses about $18 million in its first 4 hours. Client agreements commit 99.9% monthly availability with service credits.

**Additional roles (titles only).**
| Role | Duties in the deliverables |
|---|---|
| Chief Operating Officer | Authorizing official for the TVOP (P02); chairs the crisis management team |
| Chief Information Officer | Corporate IT and general IT controls |
| Chief Audit Executive | Heads Internal Audit; reports to the audit committee; leads P07 |
| Chief Compliance Officer | Second-line compliance; approves P03 with the CISO |
| General Counsel; Deputy General Counsel | Disclosure committee chair and alternate; outside counsel engagement |
| Controller | SOX program; disclosure committee member |
| Chief Marketing Officer | Marketing technology, tags, fee display in campaigns |
| Chief Human Resources Officer | Workforce lifecycle, training, acceptable use |
| President, Venue Operations | Venues, box offices, stands, gate entry |
| President, Concerts | Booking and promotion planning (delegate of the CEO for BP-17) |
| Senior Vice President, Venue Management Services | SL-2 owner |
| Vice President, Integration Management Office | Integration of AV-01 to AV-06 |
| Vice President, Ticketing Operations | Checkout templates, contact centers, support assistant |
| Vice President, Client Success | Client communications backup during incidents |
| Vice President, Pricing and Revenue Management | AI-001 owner |
| Vice President, Data and AI | Chairs the AI governance committee |
| Vice President, Venue Security and Safety | Physical security, venue OT, crowd safety |
| Vice President, Corporate Communications; Vice President, Investor Relations | Incident communications; investor messages |
| Director of Fraud and Bot Defense | AI-002 owner |
| Director of Accessibility Compliance | ADA ticketing compliance; AI committee member |
| Directors of Platform Engineering, Payments Engineering, Data Engineering, Security Operations, Identity and Access Management, Cloud Platform Engineering, Network Engineering, Endpoint Engineering, and Third-Party Risk Management | System administration and common control providers (P02 section 10.3) |

**Disclosure committee (P08).** General Counsel (chair), CFO, Controller, CISO, Chief Privacy Officer, Chief Risk Officer, and Vice President, Investor Relations, advised by outside securities counsel. Last tabletop 2025-10-21 (ransomware).

**Acquired venues.** AV-01 to AV-06 are 4 theaters and 2 clubs in Georgia, Tennessee, and North Carolina, acquired 2026-02-02 (about 640 employees). They sell online through the platform since 2026-04 but keep about 150 legacy POS terminals and card readers (31 readers were missing from any inventory), local POS servers backed up nightly to local disks, single internet carriers, legacy site VPNs, and a legacy directory managed by a local IT support firm (EV-053, EV-006; missing readers EV-087, EV-CM-8). AV employees move to enterprise payroll on 2026-12-31 (EV-005). A reachability test at AV-03 reached POS terminals from an office PC (EV-SC-7). 7 of 10 AV terminations in a 60-item sample were disabled late; 23 stale AV accounts were found (EV-AC-2).

**Platform and payments.** About 140 microservices; about 3,900 open-source dependencies; about 1,100 engineers (EV-066); about 2,900 workforce TVOP accounts (EV-001); 312 privileged and CDE accounts (EV-003); about 2,900 P2PE devices (about 430 at box offices); about 7,500 scanners; about 900 turnstile controllers and access control devices (EV-011). About 340 client templates, 212 with sales in the last 30 days; 61 scripts on client checkout templates, 14 unauthorized on 37 templates (EV-084); 41 templates show face value before the total price (EV-090). Client users: about 9,400, 38% with MFA (EV-007), 1,130 inactive over 90 days (EV-AC-2(3)), 14 client organizations sharing logins (EV-IA-8); 127 client API keys older than 12 months (EV-008, EV-085). The tokenization provider's AOC is dated 2026-03 (EV-040). The acquirer letter of 2026-02-15 confirms the company is not a designated entity (EV-058). The 2025 ROCs (merchant and service provider) were Compliant (EV-027). Service provider scope was last confirmed in 2025-10 (EV-029).

**Contact centers.** About 6.5 million contacts a year; the outsourced overflow center handles about 35% with about 220 agents (EV-033; 40 without training records, EV-086). Data discovery on 2026-07-08 found about 41,000 full card numbers in about 6.5 million case notes (EV-082); 22 of 60 sampled overflow recordings (from about 1.1 million in 12 months) captured spoken card numbers and security codes (EV-083). The overflow center's PCI DSS AOC expired on 2026-05-31 (EV-036, EV-086).

**Data warehouse.** Holds about 41 million patron records with 10 years of order history against a 7-year schedule (EV-034, EV-035; about 6.3 million records past retention, EV-091) and approximate app check-in locations for about 2.3 million patrons. 14 service accounts use passwords without key-pair authentication or network policies (EV-034).

**Tests and operations (2025-2026).** Regional failover test 2026-04-25 (3.2 hours against a 2-hour RTO); processor routing failover 2026-03-11; tier-1 DR test 2026-05-16 (EV-022); Cloud B test 2026-06-20 (EV-077); offline scanning drills at 21 of 36 venues (2026-05; EV-079); penetration test 2026-03; segmentation tests 2025-11 and 2026-05 (EV-016). In 2026 H1 (P07 and P03 populations): 241 security incidents (9 at AV venues and festivals; EV-IR-4), 1,940 PAM elevations to CDE accounts (EV-AC-6), 212 payment service changes (31 emergency; EV-CM-3), 1,904 critical and high findings (EV-RA-5), 248 security patches (EV-SI-2), 1,236 terminations with TVOP access (88 at AV venues; EV-AC-2), and 1,240 privacy rights requests (EV-086). 58 of 230 data-handling vendors are overdue for reassessment; 31 service providers have PCI DSS impact (EV-036); 9 marketing tag vendors run scripts on checkout templates (EV-084).

**Venue OT.** OT shares segments with corporate networks at 14 venues (3 of them SL-2 managed venues; EV-012); 4 building management integrators have remote access outside PAM at 9 venues (EV-013). P07 testing (reported 2026-08-12; EV-IA-5) found vendor default credentials on 14 turnstile controllers at 2 venues and a building management interface at a third venue.

**Contract terms (fictional).** Acquirer notice within 24 hours of a suspected card compromise (EV-058); notice to SL-1 clients within 72 hours of suspicion; clients notify the company within 24 hours; notice to SL-2 owners within 72 hours (EV-039).

**Risk program.** Board risk appetite approved 2026-02; 8 enterprise risks (ER-01 to ER-08) with tolerance thresholds (EV-025, EV-026; P01 section 1); about $7.2 million of treatment funded for 2026 Q4 to 2027 Q2. Policy exceptions EXC-2026-011, -017, -020, and -023 (P06).

**AI portfolio.** 13 use cases; AI governance committee formed 2025 and chaired by the Vice President, Data and AI (EV-055). AI-001 prices reserved-seat events at 11 own venues (about 1,900 events in 2026 H1) and for 52 SL-1 clients that opted in (EV-055, EV-089). AI-002 protected 12 on-sales in the 2026 H1 sample (about 2.4 million queue entrants, about 610,000 sessions blocked and 380,000 challenged; EV-089). AI-005 (facial recognition entry pilot at 2 venues) paused 2026-07-31; AI-006 crowd analytics pilot at 3 arenas; AI-010 applicant ranking disabled 2026-06-30. The support assistant (AI-007) gave 3 incorrect answers in a 200-answer sample (EV-093).

**SOC 2.** SL-1 reports for 2025 (no exceptions; EV-041) and 2026; the 2027 period adds Processing Integrity and Privacy. SL-2's first Type 2 period is 2027-04-01 to 2027-09-30, with the report expected 2027-11. The 8 managed venues have an owner portal and a settlement application on Cloud provider B.

**Worked incident example (P08, fictional future dates).** Tamper alert on 37 client templates on 2027-03-02; warehouse export of 9.2 million patron records on 2027-02-20 found on 2027-03-03; materiality determined 2027-03-04.
