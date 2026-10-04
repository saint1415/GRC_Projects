# Business Impact Analysis: Cris Santos Company | Retail Trade | Enterprise

**Organization:** Cris Santos Company, Inc. (publicly traded regional supermarket chain: 112 stores, online ordering, 2 distribution centers) | **Tier:** Enterprise (12,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, informed by NIST IR 8286D
**Prepared by:** GRC team with process owners, 2026-06-01 to 2026-07-15 | **Approved:** Chief Operating Officer and Chief Risk Officer, 2026-08-14 | **Reported to:** risk and technology committee of the board, 2026-09-10

## 1. Overview and purpose
This enterprise-wide BIA identifies the business processes the company depends on, how long each can be down, how much data each can lose, and what each depends on, including third parties and the acquired banner. It feeds:
- the availability rating and recovery objectives in the Omnichannel Commerce and Payments Platform (OCPP) System Security Plan (P02);
- impact ratings in the enterprise risk register (P01), per NIST IR 8286D;
- the business continuity plan, store downtime procedures, and the SNAP EBT manual voucher procedures required by each state retailer agreement (7 CFR 274.3(c)(4));
- the PCI DSS incident response plan's business recovery and continuity procedures (PCI DSS v4.0.1 Requirement 12.10; N44-45-R01);
- the recovery order in the e-commerce skimming runbook (P08);
- the Availability criteria for the two SOC 2 service lines (P09).

**Results in one line:** 17 processes were analyzed; 8 are High criticality, 7 Moderate, and 2 Low. 5 processes need recovery within 4 hours. The dependency map (`dependency-map.csv`) lists 26 dependencies, 14 of them single points of failure and 5 never tested.

## 2. System and business description
Cris Santos Company runs 112 supermarkets in Florida (66), Georgia (20), Alabama (9), South Carolina (8), and Tennessee (9), two distribution centers (DIST-1 Florida, DIST-2 Georgia), and online ordering with curbside pickup and home delivery. It has 12,000 employees, about 3.1 million loyalty members, and about $4.8 billion in annual revenue (about $13.2 million per calendar day). The technology estate is described in `../00_company-facts.md` section 3: the POS platform (SYS-01), payment switch (SYS-02), e-commerce platform (SYS-03), loyalty and CDP (SYS-04), identity platform (SYS-05), a multi-cloud estate across two public cloud providers plus two colocation sites (SYS-06), store networks (SYS-07), store operational technology including refrigeration (SYS-08), ERP and warehouse systems (SYS-09), and about 1,100 vendors (SYS-11). Fourteen stores acquired on 2025-10-01 (the acquired banner, AB) still run their legacy stack (SYS-14).

## 3. Impact categories and values
Dollar thresholds are scaled to about $13.2 million of revenue per calendar day and to the company's materiality framework (P08 section 6). Values are per 24 hours of outage unless stated.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $1 million per day, or more than $10 million cumulative | $100,000 to $1 million per day | Less than $100,000 per day |
| Operations | Checkout, online ordering, or replenishment stops at more than 20 stores, or a DC stops | One region, one banner, or up to 20 stores affected | Staff slowed but working |
| Regulatory and contractual | Card data compromise; missed SEC filing; SNAP retailer agreement breach; Tennessee or state AG inquiry | Missed contractual or documentation deadline; single-store EBT issue | Internal policy deviation |
| Safety (food and people) | Unsafe food reaches customers; refrigeration failure undetected | Product discarded with no customer exposure | None |
| Reputation | National media, analyst or ratings action, or loss of major CPG or supplier clients | Regional media; client complaints | Internal only |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO | Quantified impact per 24 h |
|---|---|---|---|---|---|
| BP-01 In-store checkout and card payment (98 core stores) | High | 4 h | 1 h | 15 min | $7.40M |
| BP-02 SNAP EBT acceptance (all 112 stores) | High | 4 h | 2 h | 15 min | $0.75M |
| BP-08 Cold chain and refrigeration monitoring | High | 4 h | 2 h | 15 min | $0.35M |
| BP-09 Checkout and payment at the 14 acquired-banner stores | High | 4 h | 4 h | 15 min | $1.07M |
| BP-03 E-commerce ordering and online payment | High | 8 h | 4 h | 15 min | $0.95M |
| BP-04 Online order fulfillment (picking, curbside pickup, home delivery) | High | 12 h | 6 h | 1 h | $0.60M |
| BP-06 Item, price, and promotion management | High | 24 h | 8 h | 1 h | $0.90M |
| BP-07 Loyalty and personalized offers | Moderate | 24 h | 8 h | 1 h | $0.45M |
| BP-10 Customer contact center | Moderate | 24 h | 8 h | 24 h | $0.08M |
| BP-05 Store replenishment and distribution center operations | High | 24 h | 12 h | 1 h | $2.10M |
| BP-14 Retail media and data clean room (SL-1) | Moderate | 72 h | 24 h | 4 h | $0.40M |
| BP-15 Supplier collaboration portal (SL-2) | Moderate | 72 h | 24 h | 4 h | $0.05M |
| BP-16 Asset protection and CCTV | Low | 72 h | 24 h | 24 h | $0.06M |
| BP-11 Procurement, supplier payments, and EDI | Moderate | 72 h | 48 h | 4 h | $0.20M |
| BP-12 Payroll and timekeeping | Moderate | 72 h | 48 h | 24 h | $0.25M |
| BP-17 Workforce scheduling and HR services | Low | 72 h | 48 h | 24 h | $0.05M |
| BP-13 Financial close and SEC reporting | Moderate | 120 h | 72 h | 24 h | $0.15M |

The quantified impacts add to about $15.8 million for a 24-hour outage of every process at once. That is an upper bound for planning; a single event rarely stops every process.

**What drives the values:**
- **Customers at the lane** set the shortest MTDs. Store-and-forward authorization lets the core stores keep taking cards for about 4 hours within floor limits (BP-01). The 14 AB stores have no store-and-forward, so their MTD is the same 4 hours but they fall to cash only immediately (BP-09).
- **Food access and food safety** also set 4-hour MTDs. SNAP households cannot buy food without EBT, and state retailer agreements define how manual vouchers and downtime liabilities work (BP-02). Refrigeration alarms that go unseen for more than 4 hours lead to discarded product and food safety exposure (BP-08).
- **Cash, not time,** drives replenishment (BP-05): out-of-stocks and spoilage build within a day, so the MTD is 24 hours even though stores can reorder manually.
- **Regulation** tightens financial close (BP-13) during the quarter-end window, when the MTD drops to 48 hours because of SEC filing deadlines.
- **Contracts** set the retail media (BP-14) and supplier portal (BP-15) objectives, because external clients rely on them (P09).

## 5. Dependency mapping and third parties
The full map is in `dependency-map.csv`. Key findings:

1. **Primary processor concentration (DEP-01, DEP-12).** One processor carries about 98% of card volume, all online card payments, and the hosted payment fields. Store-and-forward covers about 4 hours; the plan for a longer processor outage (limits, cash logistics, customer messaging) has never been written or tested. This is P01 risk R-005 and POA&M item POAM-016.
2. **SNAP EBT routing in failover (DEP-02, DEP-03).** The 2026-05-09 payment switch failover moved card routing in 9 minutes but did not include SNAP EBT routing. Manual voucher drills covered 3 of 112 stores and none of the AB stores (R-017; POAM-011).
3. **Acquired banner (DEP-16, DEP-17).** The AB stores depend on a legacy processor link and one store server per store, with no store-and-forward, no tested restore, and a shared local administrator account. Conversion removes these dependencies (R-003, R-018; POAM-001, POAM-008).
4. **Delivery concentration (DEP-11).** Provider A carries 62% of home deliveries, and providers B and C together have spare capacity for about 40% of that volume. The shift has never been tested at volume (R-016; POAM-022).
5. **Refrigeration monitoring (DEP-14).** All alarm notifications at core stores flow through one vendor's cloud dashboard; the manual 2-hour temperature check fallback has never been exercised, and two refrigeration vendors use always-on remote tools (R-007; POAM-004).
6. **Payment page scripts (DEP-13).** Not an availability single point of failure, but the largest integrity dependency for BP-03: 47 scripts load on payment pages, and those on the express checkout and cart pages are outside the script controls (R-002; POAM-002).

## 6. Resource requirements
| Resource / component | Description | Supports process |
|---|---|---|
| SYS-01 POS platform | Lanes, self-checkouts, store controllers, E2EE PIN pads | BP-01; BP-02; BP-06; BP-07 |
| SYS-02 Payment switch | Card and EBT routing, active-active in COLO-1 and COLO-2 | BP-01; BP-02 |
| SYS-03 E-commerce platform (Cloud A) | Web, apps, order management, pickup and delivery scheduling | BP-03; BP-04; BP-14 |
| SYS-04 Loyalty and CDP (Cloud B) | Member data, offers, audiences | BP-07; BP-14 |
| SYS-05 Identity platform | SSO, MFA, privileged access, identity governance | All |
| SYS-07 Store and enterprise network | SD-WAN with two carriers and cellular failover | All store-based processes |
| SYS-08 Store OT | Refrigeration controllers, building management, ESL, CCTV | BP-06; BP-08; BP-16 |
| SYS-09 ERP and warehouse management | Item and price file, procurement, finance, DC operations, supplier portal | BP-05; BP-06; BP-11; BP-13; BP-15 |
| SYS-14 AB legacy stack | Legacy POS, store servers, legacy processor link | BP-09 |
| Immutable backups | Separate backup accounts with write-once retention; weekly copy to COLO-2 | RPO for all Cloud A and B workloads |
| People | Store front-end teams, pickers and drivers, DC staff, SOC, store technology, payment switch team | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-05 identity platform and break-glass accounts | 1 h | Sealed break-glass accounts; secondary region |
| 2 | Network core, SD-WAN, DNS, and colocation connectivity | 1 h | Second carrier and cellular failover at stores |
| 3 | Payment switch (card and EBT routing) and processor connectivity | 1 h | Other colocation site; store-and-forward; manual EBT vouchers |
| 4 | POS platform: store controllers and lanes | 1 h | Store-and-forward; cash |
| 5 | Security tooling (EDR console, SIEM) for clean-room validation | 2 h | MSSP tooling |
| 6 | Refrigeration monitoring and alarm notifications | 2 h | Local alarms; manual checks every 2 hours |
| 7 | AB legacy POS and legacy processor link | 4 h | Cash; manual EBT vouchers |
| 8 | E-commerce platform and hosted payment fields | 4 h | Pickup orders paid in store; redirect to stores |
| 9 | Order fulfillment (handhelds, order management, delivery handoff) | 6 h | Printed pick lists; shift delivery providers |
| 10 | ERP price file and promotions | 8 h | Last good price file on store controllers |
| 11 | Loyalty and offers; contact center | 8 h | Honor member prices; overflow partner |
| 12 | Warehouse management and transportation | 12 h | Paper dock operations |
| 13 | Retail media, clean room, and supplier portal | 24 h | Pause campaigns; file exports |
| 14 | Payroll, procurement, financial close, HR | 48 h | Repeat prior payroll; manual purchase orders |

## 8. Gaps carried to other deliverables
| Gap | Carried to |
|---|---|
| No plan for a processor outage longer than the store-and-forward window | P01 R-005; P03 G-071 (PCI DSS 12.10); POAM-016 |
| SNAP EBT routing not included in switch failover; manual voucher drills limited | P01 R-017; P03 G-095; POAM-011 |
| AB stores: legacy processor link, no store-and-forward, no tested restore, shared admin account | P01 R-003, R-018; POAM-001; POAM-008 |
| Delivery provider concentration without tested surge | P01 R-016; POAM-022 |
| Refrigeration monitoring fallback never exercised; vendor remote tools | P01 R-007; POAM-004 |
| Payment page scripts outside controls on express checkout and cart pages | P01 R-002; P03 G-027, G-063; POAM-002 |
