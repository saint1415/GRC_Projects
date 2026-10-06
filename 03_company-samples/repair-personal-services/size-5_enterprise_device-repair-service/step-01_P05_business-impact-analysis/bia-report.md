# Business Impact Analysis: Cris Santos Company | Other Services | Enterprise

**Organization:** Cris Santos Company, Inc. (publicly traded national electronics and device repair chain: 1,120 stores in 44 states and DC, 3 regional repair depots, a national data recovery lab) | **Tier:** Enterprise (12,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, informed by NIST IR 8286D
**Prepared by:** GRC team with process owners, 2026-06-01 to 2026-07-10 | **Approved:** Chief Operating Officer and Chief Risk Officer, 2026-08-14 | **Reported to:** risk and technology committee of the board, 2026-09-10

## 1. Overview and purpose
This enterprise-wide BIA identifies the business processes the company depends on, how long each can be down, how much data each can lose, and what each depends on, including third parties, manufacturers, clients, and the acquired chain (AC). It feeds:
- the availability rating and recovery objectives in the STPP System Security Plan (P02);
- impact ratings in the enterprise risk register (P01), per NIST IR 8286D;
- the recovery order in the incident response runbook (P08);
- the Availability and Processing Integrity criteria for the two SOC 2 service lines (P09);
- the contingency planning duty for SL-2 ePHI under the business associate agreements (45 CFR 164.308(a)(7), P03).

No law sets recovery times for a repair business. The drivers are revenue, custody of customer property, client contracts (SL-1 and SL-2), the manufacturer program agreements, the merchant agreement, and SEC reporting deadlines.

**Results in one line:** 17 processes were analyzed; 6 are High criticality, 10 Moderate, and 1 Low. 4 processes need recovery within 4 hours. The dependency map (`dependency-map.csv`) lists 24 dependencies, 14 of them single points of failure and 5 never tested.

## 2. System and business description
Cris Santos Company runs 1,120 company-operated repair stores in 44 states and DC (960 core stores and 160 AC stores acquired on 2025-11-03), three regional repair depots (Depot East in Florida, Depot Central in Texas, Depot West in Nevada), a national data recovery lab at Depot East, and a contact center in Florida. It handles about 13.5 million repair tickets a year and has about $4.8 billion in annual revenue. The technology estate is in `../00_company-facts.md` section 3: the company-built Service Ticketing and Point-of-Sale Platform (SYS-01), the payment environment (SYS-02), the identity platform (SYS-03), two public clouds and two colocation sites (SYS-04), the store and depot network (SYS-05), about 14,500 endpoints (SYS-06), depot and lab systems (SYS-07), and the AC legacy stack (SYS-13).

## 3. Impact categories and values
Dollar thresholds are scaled to about $13.2 million of revenue per calendar day and to the company's materiality framework (P08 section 6). Values are per 24 hours of outage unless stated.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $1 million per day, or more than $10 million cumulative | $100,000 to $1 million per day | Less than $100,000 per day |
| Operations | Intake, payment, or release stops at more than 100 stores, or a whole service line stops | One region, one depot, or up to 100 stores stop | Staff slowed but working |
| Regulatory and contractual | Reportable breach in any state; PCI DSS non-compliance or loss of P2PE scope reduction; breach of a manufacturer program agreement; missed SEC filing | Missed contractual deadline (warranty window, SL-1 or SL-2 turnaround, service credits) | Internal policy deviation |
| Safety | Not used: an IT outage at a repair business does not create a plausible safety harm. Battery and electrical safety are handled by shop procedures outside this BIA | | |
| Reputation | National media, loss of a manufacturer authorization, loss of an SL-1 client, or an analyst or ratings action | Regional media; client complaints; negative reviews | Internal only |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO | Quantified impact per 24 h |
|---|---|---|---|---|---|
| BP-03 Store payment and device release (core stores) | High | 8 h | 4 h | 15 min | $4.60M |
| BP-01 Store device intake and check-in (core stores) | High | 8 h | 4 h | 15 min | $3.20M |
| BP-07 SL-1 claims repair fulfillment | High | 12 h | 4 h | 15 min | $2.70M |
| BP-16 Store operations at the 160 AC stores | High | 8 h | 8 h | 1 h (actual 24 h) | $0.85M |
| BP-02 Diagnostics and repair (stores and depots) | High | 24 h | 8 h | 4 h | $2.10M |
| BP-05 Mail-in intake, depot repair, and return logistics | High | 24 h | 12 h | 1 h | $0.90M |
| BP-11 Contact center, customer communications, and phone payments | Moderate | 12 h | 4 h | 24 h | $0.50M |
| BP-04 Website and app booking, status, and deposits | Moderate | 24 h | 8 h | 1 h | $0.60M |
| BP-08 SL-2 depot repair, imaging, and provisioning | Moderate | 48 h | 24 h | 4 h | $0.80M |
| BP-06 Manufacturer warranty claims and parts authorization | Moderate | 72 h | 24 h | 24 h | $2.80M (deferred) |
| BP-09 Data sanitization and IT asset disposition | Moderate | 120 h | 48 h | 1 h | $0.50M |
| BP-10 Data recovery and data transfer | Moderate | 72 h | 48 h | 24 h | $0.40M |
| BP-12 Parts supply chain and inventory | Moderate | 48 h | 24 h | 24 h | $0.70M |
| BP-13 Payroll and timekeeping | Moderate | 72 h | 48 h | 24 h | $0.20M |
| BP-14 Financial close and SEC reporting | Moderate | 120 h | 72 h | 24 h | $0.10M |
| BP-15 Card settlement, reconciliation, and chargebacks | Moderate | 72 h | 24 h | 4 h | $0.15M |
| BP-17 Customer marketing and analytics | Low | 168 h | 72 h | 24 h | $0.05M |

**What drives the values:**
- **Custody of customer property** sets the shortest MTDs (BP-01, BP-03, BP-16). Beyond one business day, devices pile up without tickets and the chance of releasing a device to the wrong person rises. That is a data exposure as well as a lost-property problem.
- **Client contracts** set BP-07. SL-1 clients' agreements include API availability and turnaround commitments with service credits, and claim outcome data drives the clients' own customer payouts.
- **Cash, not time,** drives warranty claims (BP-06). Manufacturers accept claims inside their submission windows, so the MTD is 3 days, but each day defers about $2.8 million of reimbursements.
- **Data integrity, not time,** drives sanitization (BP-09) and data recovery (BP-10). A lost sanitization record removes the proof that a device was wiped, and some failing drives can be read only once. Their RPOs are tighter than their RTOs.
- **Regulation** tightens financial close (BP-14) at quarter end, when the MTD drops to 48 hours because of SEC filing deadlines.

## 5. Dependency mapping and third parties
The full map is in `dependency-map.csv`. Key findings:

1. **Primary processor concentration (DEP-03).** One processor carries about 98% of card volume and provides the P2PE solution, the hosted payment fields, and the tokens. PIN pads can store and forward a limited number of approvals offline, but no fallback for in-store payments beyond those limits has been tested. This is P01 risk R-010 and POA&M item POAM-020.
2. **Acquired chain (DEP-19 to DEP-21).** The AC legacy ticketing service backs up nightly, so its real RPO is 24 hours against a 1-hour target, and no restore has ever been tested. AC card payments depend on a legacy processor link over site VPNs, and AC store IT depends on a legacy managed service provider whose remote tool uses shared credentials. All three end at conversion (wave 1 by 2026-12-15, wave 2 by 2027-03-31; P01 R-004 and R-007; POAM-001, POAM-002, POAM-004).
3. **Manufacturer tools (DEP-08, DEP-09).** Manufacturer A's online tools are the only way to pair and calibrate parts on its devices. No contract states a recovery time. The company cannot remove this dependency; the workaround is to queue repairs and claims.
4. **Logistics (DEP-11).** One national courier carries 81% of mail-in and SL-1 shipments. The secondary courier's surge capacity covers about a third of daily volume and has never been tested at volume (P01 R-034).
5. **Sanitization records (DEP-16).** Depot West stations keep sanitization records locally until a nightly sync, so a station loss can lose a day of proof. This is the same depot where the 2026-05 resale exposure happened (P01 R-006; POAM-006).
6. **Data recovery lab (DEP-15).** A single on-premises site. Case-level restores from the immutable vault met the RPO in July 2026, but a full-array restore of about 1.1 PB has never been tested (P01 R-054).

## 6. Resource requirements
| Resource / component | Description | Supports process |
|---|---|---|
| SYS-01 STPP (Cloud provider A) | System of record for tickets, customers, parts, POS, booking, and the SL-1 claims API | BP-01 to BP-05, BP-07, BP-11 |
| SYS-02 Payment environment | P2PE PIN pads, hosted payment fields, tokens, DTMF masking, virtual terminal | BP-03, BP-04, BP-11, BP-15 |
| SYS-03 Identity platform | SSO, MFA, privileged access, identity governance | All |
| SYS-04 Cloud provider B | SL-2 asset tracking portal, sanitization record store, data platform, AI services, immutable backup vault | BP-08 to BP-10, BP-17 |
| SYS-04 COLO-1 and COLO-2 | Network core, offline backup copies | All |
| SYS-05 SD-WAN and store networks | Site connectivity with cellular failover at core stores | All site-based processes |
| SYS-06 Endpoints | Counter tablets, bench workstations, office and contact center PCs | BP-01 to BP-03, BP-05, BP-11 |
| SYS-07 Depot and lab systems | Depot management, sanitization stations, lab storage | BP-05, BP-08 to BP-10 |
| SYS-08 ERP, payroll, HR | Finance, payroll, supply chain | BP-12 to BP-15 |
| SYS-13 AC legacy stack | Legacy ticketing, POS, directory, networks | BP-16 |
| People | Store staff, technicians, depot and lab staff, contact center, SOC, IT operations | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-03 identity platform and break-glass accounts | 1 h | Sealed break-glass accounts; secondary region |
| 2 | Network core, SD-WAN, DNS, and colocation connectivity | 2 h | Cellular failover at core stores |
| 3 | Security tooling (EDR console, SIEM) for clean-room validation | 2 h | MSSP tooling |
| 4 | SYS-01 STPP: POS, intake, and release functions | 4 h | Paper intake and release; offline PIN pad approvals |
| 5 | Payment environment (processor connectivity, P2PE PIN pads) | 4 h | Processor offline limits; defer payment at pickup |
| 6 | SL-1 claims API | 4 h | Secure file transfer to clients every 4 hours |
| 7 | Contact center telephony and DTMF masking | 4 h | Callback queue; recorded status message |
| 8 | AC legacy ticketing and POS (BP-16) | 8 h target (24 h per vendor contract) | Paper forms; standalone legacy PIN pads |
| 9 | Website and app booking | 8 h | Walk-in; contact center bookings |
| 10 | Bench workstations, manufacturer tool access, depot systems | 8 to 12 h | Reimage from the standard image; queue repairs |
| 11 | SL-2 asset tracking portal and sanitization record store | 24 h | Paper receiving log; hold devices in the secure cage |
| 12 | ERP, payroll, and settlement | 24 to 48 h | Repeat prior payroll; processor portal reports |
| 13 | Data recovery lab storage | 48 h | Restore from the immutable vault; pause new cases |
| 14 | Data platform and marketing tools | 72 h | Pause campaigns |

## 8. Gaps carried to other deliverables
| Gap | Carried to |
|---|---|
| Untested in-store fallback if the primary processor fails | P01 R-010; POAM-020 |
| AC legacy ticketing RPO 24 h against a 1 h target; no tested restore | P01 R-007; POAM-004 |
| AC legacy processor link and remote support tool | P01 R-001, R-004; POAM-001, POAM-002 |
| Courier concentration; surge capacity untested | P01 R-034 |
| Depot West sanitization records kept locally until nightly sync | P01 R-006; POAM-006 |
| Full-array restore of the data recovery lab never tested | P01 R-054 |
| Notification provider single point of failure | P01 R-035 |
