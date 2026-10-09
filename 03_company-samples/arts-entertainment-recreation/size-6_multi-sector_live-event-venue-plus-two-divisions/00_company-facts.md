# Scenario facts: Cris Santos Company | Arts, Entertainment, and Recreation | Multi-Sector

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a law, regulation, standard, or card brand rule, the citation is given. Facts about acquirers, merchant agreements, clients, and vendors are fictional.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company Holdings, Inc. (publicly traded SEC registrant; live entertainment, hospitality, and ticketing group) |
| Structure | A holding company with three divisions and corporate shared services |
| Division 1: Live Venues (NAICS 711310), **focus of this scenario** | Owns or operates 38 venues in 9 states (5 arenas, 11 amphitheaters, 16 theaters, 6 clubs) and promotes about 8,600 events a year for about 26 million attendees. Merchant of record for its tickets, food and beverage, parking, and merchandise. About 14,000 employees (about 4,500 full-time and 9,500 part-time event staff); about 22,000 event-day workers come from staffing contractors and are not employees |
| Division 2: Hotels and Restaurants (NAICS 721110 and 722511, sector 72 Accommodation and Food Services) | Owns and operates 16 hotels (about 7,800 rooms) in 5 states, 9 of them next to group venues, plus 58 full-service restaurants. Manages 6 more hotels for third-party owners under management agreements. Merchant of record for rooms and dining. About 19,000 employees |
| Division 3: Ticketing and Streaming Technology (NAICS 513210, sector 51 Information) | Builds and runs the group ticketing platform (SYS-D3), sold as a service to about 1,150 third-party venue clients in 44 states and used by the group's own venues and hotels. Also runs a live-concert streaming service (SYS-D4) for about 3.1 million subscribers. A **PCI DSS service provider** to its clients and a SOC 2 service organization. About 4,500 employees |
| Corporate shared services | Identity, security operations, cloud and network, the patron data platform, finance, HR, legal. About 7,500 employees |
| Location | Headquartered in Florida. Venues in 9 states and hotels in 5 states (Florida and California are among them); ticketing clients and streaming subscribers nationwide. **State law is handled generically** ("each state where affected individuals reside"), with Florida as the worked example |
| Workforce / revenue | 45,000 employees; about $18.0 billion revenue (fictional) |
| SBA size status | Not small: the SBA standard for NAICS 711310 is $40.0 million in average annual receipts (13 CFR 121.201) |
| Not in scope by fact | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv). **Gaming** (Nevada Reg. 5.260, NIGC MICS, casino BSA/AML; N71-R01 to R03): no division holds a gaming license or operates games or wagering. **COPPA** (N71-R06, N51-R02): ticketing, venue, hotel, and streaming services are general audience; accounts require age 18 or older. **HIPAA:** no division is a covered entity or business associate. **Federal contracts:** none. **FedRAMP** (N51-R07): no federal agency customers. **FCC CPNI** (N51-R06): no division is a telecommunications carrier |

## 2. People (role titles only)
| Role | Duties |
|---|---|
| Board risk committee | Group cyber oversight; accepts Very High risks; approves group policy POL-01 and POL-03 |
| Board audit committee | Oversees group internal audit |
| Group CISO; Group Chief Risk Officer; Group Chief Privacy Officer; Group General Counsel | Group standards, the group risk register, the patron data platform's purposes, and the notification matrix |
| Group PCI program director (reports to the Group CISO) | One PCI DSS program for three merchant and service provider roles; owns scope documents and QSA relationships |
| Division presidents (3) | Accept Moderate risks for their divisions |
| Division security and compliance leads (3) | Division registers, division supplements, division-specific regulators and contracts |
| Live Venues: VP Ticketing and Box Office; VP Venue Operations; VP Food and Beverage | Ticket pricing rules and on-sales (P10 business owner for group venues); venue networks, access control, CCTV; venue POS and P2PE devices |
| Hotels and Restaurants: VP Revenue Management; Director of Hotel Technology; hotel general managers | Room pricing; PMS, front desk terminals, central reservations; property operations |
| Ticketing and Streaming: Chief Technology Officer; General Manager Ticketing; General Manager Streaming; VP Product, Pricing and Access; Director of Payments Engineering | Platform engineering; client contracts and client notices; streaming; the pricing and bot modules; payment orchestration and the token vault |
| Group internal audit | Independent of control operation; assesses common controls once and samples division controls (P07) |
| Disclosure committee | SEC materiality decisions |
| Group AI council | Approves High-tier AI use cases (P10) |
| External assessors (fictional firms, unnamed) | A QSA firm (ROCs for Live Venues and the ticketing platform); a SOC 2 service auditor; a PCI forensic investigator (PFI) on the insurer panel |

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv). Suppliers are in the [vendor register](step-00_P00_intake/vendor-register.csv).

| ID | System | Owner |
|---|---|---|
| SYS-G1 | Group identity platform (workforce SSO, MFA, PAM, identity governance) | Corporate |
| SYS-G2 | Group SOC, SIEM, and EDR | Corporate |
| SYS-G3 | Group cloud platform (two providers, called provider A and provider B; vendor-agnostic) and the wide-area network to venues and hotels | Corporate |
| SYS-G4 | Patron data platform: unified patron profiles from ticketing, hotels, dining, and streaming, used for marketing and analytics | Corporate (marketing data office) |
| SYS-D1 | Venue operations estate: venue networks, box office stations, food, beverage, and merchandise POS, access control scanners, CCTV, venue Wi-Fi, production networks | Live Venues |
| SYS-D2 | Hotel systems: property management system (vendor SaaS), central reservations and call center, front desk payment terminals, restaurant POS, door locks, guest Wi-Fi | Hotels and Restaurants |
| SYS-D3 | Ticketing platform (multi-tenant SaaS): event setup, hosted checkout, payment orchestration and token vault, patron accounts, mobile tickets, access control service, dynamic pricing module, bot detection and virtual queue | Ticketing and Streaming |
| SYS-D4 | Streaming service: subscriber accounts, pay-per-view and subscription billing (through SYS-D3 payment orchestration), video delivery | Ticketing and Streaming |

**SSP system (P02):** the *Ticketing and Venue Operations Platform (TVOP)*: SYS-D3 in provider A (with disaster recovery in provider B) plus the venue edge components that connect to it at the 30 integrated group venues (box office stations with P2PE devices, access control scanners, and venue operations consoles); it inherits common controls from SYS-G1 to SYS-G3.

## 4. Where the evidence is
This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Rows are grouped by division (Group, Live Venues, Hotels and Restaurants, Ticketing and Streaming). Every item has a source system, an owner, and as-of and collected dates.
- **Which rules apply** to each division and to the group is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps** against PCI DSS, the FTC fee rule, ADA ticketing rules, client and SOC 2 commitments, and state law are judged in the gap analyses (P03), which also number the seven group gaps cited across this sample, and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P02 | One shared system used by all three divisions: the Ticketing and Venue Operations Platform (TVOP), with a common control catalog for inheritance |
| P03 | Live Venues: PCI DSS v4.0.1 as a merchant (primary), plus the FTC fee rule (16 CFR Part 464), FTC Act Section 5, ADA ticketing rules, and the BOTS Act. Hotels and Restaurants: PCI DSS as a merchant, Part 464 for lodging, Florida guest register. Ticketing and Streaming: PCI DSS as a service provider, SOC 2 commitments, FTC Act Section 5, and data rules for a technology company |
| P08 | Ticketing platform breach: a skimming script injected through a tenant tag on the hosted checkout, exposing card and customer data for group venues, hotel packages, streaming purchases, and 41 third-party clients |
| P09 | SOC 2 scoped per division: the ticketing platform is in scope (true service organization); streaming, Live Venues, and Hotels are out of scope, with reasons |
| P10 | Group AI governance program: group standard, division use cases, and the rules that apply (FTC fee rule, ADA ticketing, BOTS Act, FTC Act, state privacy and biometric questions) |
| Cloud | Shared corporate platform (providers A and B, vendor-agnostic) plus division workloads |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-03-30 to 2026-04-24 | Intake: evidence requests, exports, inventories, obligations register |
| 2026-04-15 | Acquirer letters (received during intake): Live Venues validated by QSA ROC; Hotels and Restaurants by SAQ D for Merchants with quarterly ASV scans |
| 2026-05-01 to 2026-07-31 | BIA interviews (May), group and division risk analyses, and regulatory gap analyses |
| 2026-06-01 to 2026-06-19 | Group policies v2026 drafted from the gaps found so far (P06); the Live Venues supplement was aligned to the drafts on 2026-06-20 |
| 2026-07-01 to 2026-08-31 | Common control assessment (group internal audit) plus division samples: operating tests of controls already in place; design review of the draft v2026 policies and the notification matrix |
| 2026-08-17 to 2026-08-28 | AI use case assessments (group AI council) |
| 2026-09-15 | Results to the board risk committee; deliverables and group policies v2026 approved (policies effective 2026-10-01) |
| 2026-11-30 | Live Venues 2026 ROC and AOC due to its acquirer |
| 2026-12-31 | Hotels and Restaurants 2026 SAQ D and AOC due |
| 2027-03-31 | Ticketing platform service provider ROC renewal |
| 2027-04 (planned) | Follow-up assessment: operating effectiveness of the controls the v2026 policies introduced, after at least one quarter of operation |

## 7. Facts added while building the deliverables
These facts were added so the deliverables could be completed. They do not change sections 1 to 6.

| Topic | Added fact |
|---|---|
| Registry defaults | The registry defaults (primary system "Ticketing and venue operations platform", incident "Ticketing platform breach exposing customer and card data", AI use case "Dynamic ticket pricing and bot detection") fit this group and are kept. At this size the ticketing platform is a multi-tenant service run by Division 3, so the SSP covers the platform plus its venue edge, and the incident spans all three divisions and outside clients |
| Revenue split (fictional) | Live Venues about $9.4 billion (about $25.8 million per day on average); Hotels and Restaurants about $6.1 billion (about $16.7 million per day); Ticketing and Streaming about $2.5 billion (about $6.8 million per day). Total about $18.0 billion, as in section 1 (EV-003) |
| Risk acceptance | Low: division security and compliance lead. Moderate: division president. High: Group Chief Risk Officer with the Group CISO, reported to the board risk committee. Very High: board risk committee only. Crowd-safety and guest-safety risks rated High must be treated (EV-028) |
| PCI DSS roles and levels | Visa merchant levels from Visa *What To Do If Compromised* v10.0 (effective 2026-06-25): Level 1 more than 6,000,000 Visa transactions a year; Level 2 1,000,001 to 6,000,000; Level 3 1 to 1,000,000. **Live Venues:** about 61 million card transactions a year (about 14 million ticket orders, 47 million food, beverage, merchandise, and parking), about 33 million Visa, so Visa Level 1; its acquirer (letter 2026-04-15) requires an annual QSA ROC and quarterly ASV scans; 2026 ROC due 2026-11-30. The 2025 ROC was Compliant, but its scope date preceded the theater acquisition (closed 2025-10). **Hotels and Restaurants:** about 24 million transactions, about 5.4 million Visa, so Visa Level 2; its acquirer requires SAQ D for Merchants with quarterly ASV scans, due 2026-12-31. **Ticketing and Streaming:** service provider ROC (AOC 2026-03-31, renewal 2027-03-31); streaming is about 4.6 million transactions a year, and the streaming acquirer accepts the service provider ROC for that channel. Other brands' levels not verified (evidence: EV-004, EV-005, EV-044, EV-061) |
| Live Venues details | 7 of the 38 venues are operated for public owners under management agreements. About 22 million tickets a year sold on the TVOP for 30 integrated venues; about 5,900 validated P2PE devices; about 3,200 seasonal box office users (180 found stale at 9 venues). Dynamic pricing at 27 venues; posted limit 8 tickets per customer. Live Venues marketing added 23 tags to its checkout pages. Venue privacy notice dated 2023. Facility fee described as "set by the ticketing company" on 6 venue FAQs. Offline scanner mode tested at 4 of 30 venues in 12 months (one 2025 failure at an amphitheater). Integrators hold persistent tunnels to CCTV and door access at 6 venues; 11 venues have a single CCTV recorder; 3 group venues still use static barcodes. Live Venues supplement last aligned 2026-06-20 (evidence: EV-043, EV-045, EV-007, EV-C-AC2, EV-072, EV-049, EV-039, EV-092, EV-048, EV-047, EV-046, EV-086) |
| Acquired theaters (8) | About 1.1 million tickets a year on the seller's ticketing SaaS; about 410 non-P2PE terminals on flat networks; the legacy POS keeps full card numbers in a local database for 18 months; 3 theaters used consumer-grade routers with open management ports (closed 2026-07-16 as an interim fix). Option B interim fix (P2PE devices, firewalls, EDR, purge) costs about $1.4 million (fictional) (evidence: EV-050, EV-098, EV-L-SC7) |
| Hotels and Restaurants details | Hotels: about 7,800 rooms in 16 owned hotels; the 6 managed hotels use the same PMS. About 180,000 event-and-stay packages a year sold on the TVOP hotels tenant (4 tags on its checkout). About 180 semi-integrated front desk terminals (not P2PE) on flat staff networks; about 1,400 validated P2PE devices in restaurants. PMS: about 2,600 local accounts outside SYS-G1, 340 stale, 410 with permission to display full virtual card numbers, shared front desk logins at 4 hotels; PMS logs kept 90 days by the vendor; guest register kept 7 years. Central reservations: 140 agents key card numbers into the PMS. 214 emailed card authorization forms with security codes found in group sales mailboxes (purged 2026-08-20). Mandatory $32 resort fee at the 9 venue hotels; a metasearch feed and 2 partner channels show rates without it; 3 hotels describe it as covering a shuttle discontinued in 2025. Door lock servers at 5 hotels run an unsupported operating system. About 1.9 million identity document numbers in the PMS, copied nightly to SYS-G4. Paper background check reports at 4 hotel HR offices. Channel manager AOC not on file. Hotels standards v2024 (aligned 2024-04) (evidence: EV-053, EV-056, EV-054, EV-055, EV-057, EV-096, EV-099, EV-059, EV-091, EV-014, EV-060, EV-034, EV-058) |
| Ticketing and Streaming details | About 96 million tickets a year on the TVOP (about 22 million group venues, about 74 million clients); about 68 million patron accounts; about 41 million card-on-file tokens; 3 acquirers and gateways; 14 inventoried platform scripts; tags found on the checkout pages of 641 client tenants (scan 2026-07-21). 310 clients opted into dynamic pricing (22 with accessible levels in auto-apply); about 1,900 protected on-sales a year. About 2,300 workforce console users and about 41,000 client tenant users; 38% of client administrators do not use MFA; 412 support engineers hold a standing tenant impersonation role; 37 integration keys older than 1 year. 2024 client agreement: incident notice within 72 hours (186 clients negotiated 24 hours), 99.95% monthly availability, aggregated analytics allowed; 212 clients remain on pre-2024 agreements without that clause, a PCI DSS acknowledgment, or CCPA service provider terms. SOC 2 Type 2 (Security, Availability, Confidentiality) for 12 months ending 2026-06-30, issued 2026-08-21, unqualified with no exceptions. PCI scope confirmed 2026-06-30; segmentation tests 2026-01 and 2026-07; disaster recovery failover tests 2026-02-11 and 2026-06-09. A software testing contractor has staff in the United States and India, with no access from countries of concern and synthetic test data only (evidence: EV-064, EV-065, EV-097, EV-072, EV-101, EV-067, EV-068, EV-069, EV-063, EV-105, EV-090, EV-015, EV-095, EV-071, EV-079, EV-041) |
| Cloud placement | Provider A: corporate hub, the TVOP (two regions, with a separate CDE account and managed HSMs), the patron data platform (SYS-G4), and hotel cloud workloads. Provider B: TVOP disaster recovery, the streaming service with a CDN, and the immutable backup vault. The hotel PMS is vendor-hosted; the SD-WAN connects 30 integrated venues, 16 hotels, and 58 restaurants (evidence: EV-018, EV-020, EV-055) |
| California and CCPA | The group does business in California and exceeds the CCPA revenue threshold; it processes personal information of more than 250,000 consumers, so a cybersecurity audit applies, with the first report due 2028-04-01 (2026 revenue above $100 million, N51-R03) (evidence: EV-003, EV-040) |
| AI program | Group AI Standard adopted 2026-06 and a group AI council chaired by the Group Chief Risk Officer. The face-based express entry pilot runs at 2 Florida amphitheaters since 2026-05 with about 38,000 enrolled patrons; the vendor keeps templates 12 months. The generative support assistant uses a hosted model service under no-training, zero-retention terms. The enterprise generative AI pilot has 3,000 users (evidence: EV-100, EV-084, EV-103, EV-035) |
| P08 exercise counts (illustrative) | 11-day window; about 412,000 checkouts (Live Venues about 236,000, hotel packages about 9,800, streaming about 61,000, 41 clients about 105,000); about 382,000 unique cards; about 52,000 new accounts with email and password captured; about 104,000 affected Florida residents |
| Fictional costs in the POA&M | SIEM ingestion increase about $180,000 a year; tamper detection licence increase about $90,000 a year; tabletop facilitator about $40,000; PMS single sign-on services about $60,000; front desk P2PE devices about $450,000 |
