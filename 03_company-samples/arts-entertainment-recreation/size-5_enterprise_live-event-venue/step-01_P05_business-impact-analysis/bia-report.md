# Business Impact Analysis: Cris Santos Company | Arts, Entertainment, and Recreation | Enterprise

**Organization:** Cris Santos Company, Inc. (publicly traded live entertainment company: 36 venues, 3 festivals, and an in-house ticketing platform) | **Tier:** Enterprise (12,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, informed by NIST IR 8286D
**Prepared by:** GRC team with process owners, 2026-06-01 to 2026-07-15 | **Approved:** President, Venue Operations; President, Ticketing; and Chief Risk Officer, 2026-08-14 | **Reported to:** risk committee of the board, 2026-09-10
**Sources:** process owner interviews 2026-06-01 to 2026-07-10 (EV-075, EV-076), dependency and contract review (EV-078), venue drill records (EV-079), venue and entity register (EV-052), FY2025 revenue report (EV-049), platform sales and volume report (EV-050), card transaction and routing report (EV-051), contact center volumes (EV-033), Integration Management Office status report (EV-053), DR and failover test reports (EV-022, EV-018), and the Cloud provider B recovery test (EV-077). The `source_evidence` column in `bia.csv` names the source of each process's values. Downtime limits are the owners' statements, reviewed and approved by the President, Venue Operations, the President, Ticketing, and the Chief Risk Officer.

## 1. Overview and purpose
This enterprise-wide BIA identifies the business processes the company depends on, how long each can be down, how much data each can lose, and what each depends on, including third parties and the six venues acquired in February 2026. It feeds:
- the enterprise contingency and disaster recovery plans, and the incident response plan that PCI DSS Requirement 12.10.1 expects to include business recovery and continuity procedures;
- the availability rating and recovery objectives in the Ticketing and Venue Operations Platform (TVOP) System Security Plan (P02);
- impact ratings in the enterprise risk register (P01), per NIST IR 8286D;
- the recovery order in the ticketing platform breach runbook (P08);
- the Availability criteria for the two SOC 2 service lines (P09).

**Results in one line:** 18 processes were analyzed; 7 are High criticality, 9 Moderate, and 2 Low. 9 processes need recovery within 4 hours, and two (gate entry and venue safety) within 1 hour. The dependency map (`dependency-map.csv`) lists 26 dependencies, 9 of them single points of failure (2 more are partial) and 4 never tested.

## 2. System and business description
Cris Santos Company operates 36 venues in Florida and 7 other states (6 arenas, 10 amphitheaters, 14 theaters and music halls, 6 clubs) and produces 3 annual festivals. It holds about 5,400 ticketed events a year with about 19 million attendees, has 12,000 employees (about 7,900 of them part-time and seasonal event staff), and earns about $4.8 billion a year. Its in-house ticketing platform issues about 52 million tickets a year, 21 million for its own events and 31 million for about 340 client venues and promoters (SL-1). It also manages 8 publicly owned venues (SL-2).

The technology estate is listed in the intake [asset inventory](../step-00_P00_intake/asset-inventory.csv) and [vendor register](../step-00_P00_intake/vendor-register.csv): the ticketing platform (SYS-01) and payment service (SYS-02) on Cloud provider A; venue point of sale (SYS-03); the identity platform (SYS-04); Cloud provider B for data, marketing, and AI, plus two colocation data centers (SYS-05); venue networks and operational technology (SYS-06); about 22,500 endpoints, scanners, and POS handhelds (SYS-07); ERP and payroll (SYS-08); two contact centers (SYS-09); marketing technology (SYS-10); and about 1,450 vendors (SYS-11). The six acquired venues (AV-01 to AV-06) still run legacy POS and a legacy directory.

## 3. Impact categories and values
Dollar thresholds are scaled to about $13.2 million of revenue per calendar day ($4.8 billion in FY2025 revenue, EV-049) and about $12.6 million of gross ticket sales through the platform on an average day (3 to 4 times that on peak on-sale days; EV-050), and to the company's materiality framework (P08 section 6). Values are per 24 hours of outage unless stated.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $1 million per day, or more than $10 million cumulative | $100,000 to $1 million per day | Less than $100,000 per day |
| Operations | Online ticketing, payments, or gate entry stops company-wide, a major on-sale fails, or events at more than 5 venues are cancelled or delayed | One venue, one festival, one service line, or a client segment stops | Staff slowed but working |
| Regulatory and contractual | Card data compromise reportable to card brands; breach notice in multiple states; missed SEC filing; failed PCI DSS validation | Missed contractual deadline or client service credit; single-state notice | Internal policy deviation |
| Safety | Plausible injury from crowding at gates, loss of screening or evacuation capability, or unsafe building conditions | Degraded but safe operations with extra staff | None |
| Reputation | National media, artist or client loss, analyst or ratings action | Regional media; client or artist complaints | Internal only |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO | Quantified impact per 24 h |
|---|---|---|---|---|---|
| BP-04 Event-day entry and access control scanning | High | 1 h | 30 min | 15 min | $1.20M (per 1-hour failure at doors on a busy night) |
| BP-10 Venue safety and security operations | High | 1 h | 1 h | 24 h | $1.00M |
| BP-02 Payment authorization and tokenization | High | 4 h | 2 h | 15 min | $4.90M |
| BP-01 Online and app ticket sales (own events) | High | 4 h | 2 h | 15 min | $2.40M |
| BP-03 High-demand on-sales and virtual queue | High | 4 h | 2 h | 15 min | $6.00M (peak on-sale day) |
| BP-07 White-label ticketing for client venues (SL-1) | High | 4 h | 2 h | 15 min | $2.00M |
| BP-06 Food, beverage, and merchandise sales | High | 4 h | 2 h | 15 min | $2.20M |
| BP-05 Box office sales at venues | Moderate | 8 h | 4 h | 15 min | $0.30M |
| BP-11 Venue building systems | Moderate | 6 h | 4 h | 24 h | $0.90M |
| BP-18 Ticketing and POS at the acquired venues (AV-01 to AV-06) | Moderate | 12 h | 8 h | 24 h | $0.35M |
| BP-08 Contact center sales and patron support | Moderate | 24 h | 8 h | 24 h | $0.40M |
| BP-12 Event production systems | Low | 8 h | 8 h | 24 h | $0.30M |
| BP-14 Marketing and patron communications | Moderate | 24 h | 12 h | 4 h | $0.50M |
| BP-09 Event settlement | Moderate | 72 h | 24 h | 4 h | $0.20M |
| BP-13 Venue management services for public owners (SL-2) | Moderate | 72 h | 24 h | 4 h | $0.15M |
| BP-15 Payroll and timekeeping | Moderate | 72 h | 48 h | 24 h | $0.30M |
| BP-16 Financial close and SEC reporting | Moderate | 120 h | 72 h | 24 h | $0.10M |
| BP-17 Event booking and promotion planning | Low | 168 h | 72 h | 24 h | $0.05M |

**What drives the values:**
- **Crowd safety** sets the shortest MTDs. Gates must admit thousands of people in 60 to 90 minutes, and an event cannot continue without screening, video coverage, and the ability to announce an evacuation (BP-04, BP-10). The offline scanning mode is the main workaround for BP-04, and it has been tested at only 21 of 36 venues.
- **Event time cannot be bought back.** Stand sales and on-sales that miss their window are mostly lost, not deferred (BP-03, BP-06). This is the opposite of claims-style processes, where cash is only delayed.
- **The payment service is the hub.** One payment service and one tokenization provider sit under every online, app, and phone sale for own and client events. A payment outage stops BP-01, BP-07, and BP-08 at once (about $4.9 million a day).
- **Contracts** set the SL-1 and SL-2 objectives: 99.9% monthly availability with service credits for client venues, and monthly reporting and settlement statements for public owners (P09).
- **Regulation** tightens financial close (BP-16) during the quarter-end window, when the MTD drops to 48 hours because of SEC filing deadlines.

## 5. Dependency mapping and third parties
The full map is in `dependency-map.csv`. Key findings:

1. **Tokenization concentration (DEP-02).** All card-not-present tokens and card-on-file credentials sit with one tokenization and vault provider. The tokens cannot be used with any other provider, there is no exit or token migration clause (EV-038), and the provider's recovery has never been observed (EV-078). An outage stops refunds and chargeback handling as well as sales. This is P01 risk R-011 and POA&M item POAM-015.
2. **Edge and bot management concentration (DEP-05).** All web and app traffic passes through one edge, WAF, and bot management provider. The fallback (DNS cut-over to the cloud provider's WAF with reduced bot protection) has never been tested, and reopening an on-sale without bot protection would hand inventory to resellers. P01 R-008; POAM-014.
3. **Regional failover (DEP-01).** The ticketing platform and payment service failed over to the second region in 3.2 hours against a 2-hour RTO in the 2026-04-25 test, because database promotion and payment endpoint certificates were manual steps (EV-022). P01 R-010; P02 CP-10; POAM-010.
4. **Acquired venues (DEP-07, DEP-10, DEP-26).** AV-01 to AV-06 run legacy POS servers that back up nightly to local disks (actual RPO 24 hours) with no tested restore, use single internet carriers, and depend on a local IT support firm and a legacy directory (EV-053). P01 R-004; POAM-001; POAM-011.
5. **Gate entry offline mode (DEP-08).** Offline scanning was tested at 21 of 36 venues in May 2026 (EV-079). The 15 untested venues include all 6 AV venues and 3 amphitheaters. P01 R-015; POAM-013.
6. **Outsourced overflow contact center (DEP-15).** It handles about 35% of contacts, records spoken card numbers, and its PCI DSS AOC expired on 2026-05-31 (EV-033, EV-032, EV-036). P01 R-007 and R-021; POAM-003; POAM-009.
7. **Industry-wide dependencies (DEP-22).** Mobile app stores and push notification services cannot be replaced; the workaround is web checkout and email or SMS.

## 6. Resource requirements
| Resource / component | Description | Supports process |
|---|---|---|
| SYS-01 Ticketing platform (Cloud A) | Event setup, inventory, checkout, accounts, access control, queue and bot defense, pricing | BP-01, BP-03, BP-04, BP-05, BP-07 |
| SYS-02 Payment service (Cloud A CDE accounts) | Payment fields, agent payment page, tokenization, authorization routing | BP-01, BP-02, BP-07, BP-08 |
| SYS-03 Venue point of sale | Box office and stand devices (P2PE at 30 venues; legacy at AV venues) | BP-05, BP-06, BP-18 |
| SYS-04 Identity platform | SSO, MFA, privileged access, identity governance | All |
| SYS-05 Cloud B workloads | Data warehouse, customer data platform, settlement application, AI services | BP-09, BP-13, BP-14, BP-16 |
| SYS-05 Colocation DC-1 and DC-2 | Network core, legacy venue systems, offline backup copies | Recovery of all |
| SYS-06 Venue networks and OT | SD-WAN, venue LANs, CCTV, access control, building management, screening | BP-04, BP-10, BP-11, BP-12 |
| SYS-07 Endpoints and handhelds | Workstations, about 7,500 scanners and POS handhelds | BP-04, BP-05, BP-06 |
| SYS-08 ERP and payroll | Finance, payroll, human capital management | BP-09, BP-15, BP-16 |
| SYS-09 Contact centers | Cloud contact center platform; in-house and outsourced centers | BP-08 |
| Immutable backups | Separate backup accounts with write-once retention; weekly copy to DC-2 | RPO for all Cloud A and B workloads |
| People | Platform and payments engineering, ticketing operations, venue operations and security, SOC | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Scanner offline mode and venue network connectivity for events in progress | 30 min | Cached ticket lists; printed manifests; cellular failover |
| 2 | Venue safety systems (CCTV, screening, access control, public address) | 1 h | Manual screening posts; extra staff; stop entry |
| 3 | SYS-04 identity platform and break-glass accounts | 1 h | Sealed break-glass accounts; secondary region |
| 4 | Network core, SD-WAN, DNS, and edge provider connectivity | 2 h | Cellular failover at venues; cloud WAF fallback (untested) |
| 5 | Security tooling (EDR console, SIEM) for clean-room validation | 2 h | MSSP tooling |
| 6 | SYS-02 payment service and tokenization connectivity | 2 h | Second region; processor failover |
| 7 | SYS-01 ticketing platform (own events, client venues, on-sale queue) | 2 h | Second region; pause on-sales and hold inventory |
| 8 | Food, beverage, and merchandise POS | 2 h | Offline mode for up to 4 hours |
| 9 | Box office devices and building management systems | 4 h | App sales and will-call; manual plant control |
| 10 | AV-01 to AV-06 legacy POS | 8 h target (24 h actual RPO; restore untested) | App sales; cash where allowed |
| 11 | Contact center platform and agent payment page | 8 h | Web help center; callbacks |
| 12 | Marketing and patron messaging | 12 h | Website, app banner, social channels |
| 13 | Settlement application, owner portal, and data warehouse | 24 h | Spreadsheet settlement with dual review |
| 14 | ERP and payroll | 48 h | Repeat prior payroll |
| 15 | Booking and promotion planning tools | 72 h | Email and spreadsheets |

## 8. Gaps carried to other deliverables
| Gap | Carried to |
|---|---|
| Payment service and platform failover 3.2 h against a 2 h RTO | P01 R-010; P02 CP-10; POAM-010 |
| Single tokenization provider without exit plan or token portability | P01 R-011; POAM-015 |
| Edge and bot management provider concentration; fallback untested | P01 R-008; POAM-014 |
| Offline scanning not tested at 15 venues | P01 R-015; POAM-013 |
| AV-01 to AV-06 legacy POS with 24 h RPO and no tested restore | P01 R-004; POAM-001 |
| Outsourced overflow contact center records card numbers; AOC expired | P01 R-007, R-021; POAM-003; POAM-009 |
| Building management and OT integrators reach shared venue segments | P01 R-013; POAM-006 |
