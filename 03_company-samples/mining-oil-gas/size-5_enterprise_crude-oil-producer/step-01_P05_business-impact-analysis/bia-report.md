# Business Impact Analysis: Cris Santos Company | Mining, Quarrying, and Oil and Gas Extraction | Enterprise

**Organization:** Cris Santos Company, Inc. (publicly traded independent crude oil producer; Permian, Mid-Continent, and Florida operating areas) | **Tier:** Enterprise (12,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, informed by NIST IR 8286D
**Prepared by:** GRC team with process owners, 2026-06-01 to 2026-07-15 | **Approved:** Chief Operating Officer and Chief Risk Officer, 2026-08-14 | **Reported to:** risk committee of the board, 2026-09-10

## 1. Overview and purpose
This enterprise-wide BIA identifies the business processes the company depends on, how long each can be down, how much data each can lose, and what each depends on, including third parties and the acquired Mid-Continent assets (AQ-MC). It feeds:
- the OT and IT contingency plans, including the IOC-to-BCC failover plan and the regional manual-operations procedures;
- the availability rating and recovery objectives in the FSPA System Security Plan (P02);
- impact ratings in the enterprise risk register (P01), per NIST IR 8286D;
- the recovery order in the ransomware runbook (P08) and the production-loss inputs to the SEC materiality worksheet (P08 section 6);
- the Availability and Processing Integrity criteria for the two SOC 2 service lines (P09).

**Results in one line:** 18 processes were analyzed; 9 are High criticality, 8 Moderate, and 1 Low. 2 processes need recovery within 4 hours. The dependency map (`dependency-map.csv`) lists 26 dependencies, 10 of them single points of failure (fully or for part of the estate) and 2 never tested.

## 2. System and business description
Cris Santos Company operates about 8,900 wells in three onshore operating areas: the Permian Basin (about 74% of production), the Mid-Continent (about 22%, including 1,700 wells acquired in 2025), and Florida (about 4%). It produces about 190,000 barrels of oil equivalent per day and about $4.8 billion of revenue a year (about $13.2 million per calendar day). Field SCADA runs 24x7 from the Integrated Operations Center (IOC) in Midland, Texas, with hot standby at the Backup Control Center (BCC) in Oklahoma City and a separate regional control room in Florida. The technology estate is in `../00_company-facts.md` section 3: the enterprise SCADA platform (SYS-01), about 11,000 field controllers and 6,500 cellular modems (SYS-02), hydrocarbon accounting (SYS-03), a two-cloud estate with two colocation data centers (SYS-04), the identity platform (SYS-05), ERP (SYS-06), and the acquired Mid-Continent legacy SCADA (SYS-13).

**A design fact that shapes every number below:** safety shutdowns (gas detection, tank high-level, compressor emergency shutdown, gathering line high-pressure shutdown) are hardwired or run in separate safety controllers, and field controllers keep running on their local logic when SCADA is lost. Losing SCADA therefore removes **visibility and remote control**, not safety protection. The clock that matters is how long the company can watch the field by other means before it must shut wells in.

## 3. Impact categories and values
Dollar thresholds are scaled to about $13.2 million of revenue per calendar day and to the company's materiality framework (P08 section 6). Values are per 24 hours of outage unless stated.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $1 million per day, or more than $10 million cumulative | $100,000 to $1 million per day | Less than $100,000 per day |
| Operations | Remote control lost for an operating area, or more than 10% of production shut in | One field, one facility type, or up to 10% of production affected | Staff slowed but working |
| Regulatory | Reportable release (40 CFR 110.6; 49 CFR 195.50); missed SEC filing; reportable breach of 500 or more individuals | Missed contractual or state report deadline; breach under 500 | Internal policy deviation |
| Safety | Plausible injury, gas exposure, fire, or loss of containment | Delayed but safe operations | None |
| Reputation | National media, analyst or ratings action, regulator inquiry, or loss of SL-1 or SL-2 customers | Regional media; owner or customer complaints | Internal only |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO | Quantified impact per 24 h |
|---|---|---|---|---|---|
| BP-02 Safety and environmental alarm response | High | 4 h | 2 h | 15 min | $9.80M |
| BP-01 Field monitoring and remote control | High | 12 h | 4 h | 15 min | $3.90M |
| BP-04 Produced water gathering, injection, and disposal | High | 12 h | 6 h | 1 h | $6.40M |
| BP-05 Gas compression and associated gas sales | High | 12 h | 6 h | 1 h | $2.20M |
| BP-17 Field operations at the acquired Mid-Continent assets (AQ-MC) | High | 12 h | 8 h | 24 h | $1.10M |
| BP-03 Crude oil gathering and custody transfer | High | 24 h | 8 h | 1 h | $5.10M |
| BP-10 Crude marketing, nominations, and scheduling | High | 24 h | 8 h | 4 h | $1.20M |
| BP-06 Drilling and completions real-time operations | Moderate | 24 h | 12 h | 1 h | $0.90M |
| BP-15 HSE incident management and regulatory reporting | Moderate | 24 h | 12 h | 4 h | $0.05M |
| BP-07 Field maintenance and well servicing dispatch | Moderate | 48 h | 24 h | 4 h | $0.40M |
| BP-12 Water services ticketing and invoicing (SL-2) | Moderate | 48 h | 24 h | 1 h | $0.10M |
| BP-18 Supply chain and field logistics | Moderate | 48 h | 24 h | 24 h | $0.35M |
| BP-08 Production volume capture and allocation | High | 72 h | 24 h | 1 h | $0.30M |
| BP-11 Owner and partner portal and statements (SL-1) | Moderate | 72 h | 24 h | 1 h | $0.15M |
| BP-14 Payroll and timekeeping | Moderate | 72 h | 48 h | 24 h | $0.25M |
| BP-09 Hydrocarbon accounting, revenue distribution, and joint interest billing | High | 120 h | 48 h | 1 h | $0.60M |
| BP-13 Financial close and SEC reporting | Moderate | 120 h | 72 h | 24 h | $0.15M |
| BP-16 Geoscience and reservoir engineering | Low | 168 h | 72 h | 24 h | $0.12M |

**What drives the values:**
- **Safety and the environment** set the shortest MTD: alarm response (BP-02) must be restored or replaced by patrols within 4 hours, because people must still learn about a gas or tank alarm even though the shutdown itself is hardwired, and because 31 tank batteries meet the SPCC overfill requirement through the SCADA alarm (40 CFR 112.9(c)(4)(iv)).
- **Physical storage** sets the field clocks: produced water storage fills in about 12 hours (BP-04), and crude tank storage in about 24 to 36 hours (BP-03). After that, wells shut in and production is deferred.
- **Cash, not time,** drives revenue distribution (BP-09). Owners are paid monthly, so the MTD is 5 days, dropping to 48 hours in the week before the payment run.
- **Regulation** tightens financial close (BP-13) in the quarter-end window and sets the integrity focus of volume capture (BP-08), which feeds SOX controls and SEC reserves and revenue reporting.
- **Contracts** set the SL-1 portal (BP-11) and SL-2 ticketing (BP-12) objectives (P09).

## 5. Dependency mapping and third parties
The full map is in `dependency-map.csv`. Key findings:

1. **Failover does not meet the RTO (DEP-01, DEP-02).** The 2026-04-25 test moved the IOC to the BCC in 9 hours against a 4-hour RTO. The delay came from manual re-pointing of DNS, historian collectors, and alarm call-out. This is P01 risk R-005 and POAM-004.
2. **Florida and AQ-MC have no tested recovery (DEP-03, DEP-04).** Florida's SCADA servers have no off-site standby and back up to a storage device in the same room; AQ-MC's legacy SCADA backups have never been restore-tested and depend on Integrator B under a transition services agreement. These are R-019, R-002, POAM-005, and POAM-009.
3. **Cellular carrier concentration (DEP-05).** One carrier serves 88% of field modems, and about 70% of cellular sites have no second path. A 5-hour carrier outage on 2026-02-11 blinded about 1,900 sites. The carrier contract has no priority restoration term. This is R-009 and POAM-019.
4. **Vendor-operated paths into the field (DEP-08, DEP-09).** Integrator A is the only firm certified on the SCADA platform, and the ESP vendor monitors about 1,800 drives through its own cloud with a remote setpoint-write feature enabled on 260 drives. This is R-003 and POAM-002.
5. **Customers and takeaway (DEP-18, DEP-19).** Three crude purchasers take about 80% of volume. Their outage is a market risk handled by marketing, not a cyber control, but one of the three ticket data exchanges has no security terms (P03).

## 6. Resource requirements
| Resource / component | Description | Supports process |
|---|---|---|
| SYS-01 Enterprise SCADA platform | IOC primary, BCC hot standby, Florida regional servers, historians, HMIs | BP-01 to BP-05, BP-08, BP-12 |
| SYS-02 Field devices and communications | About 11,000 controllers, 1,800 ESP drives, private LTE, licensed radio, 6,500 cellular modems | BP-01 to BP-05, BP-17 |
| SYS-03 Hydrocarbon accounting | Volumes, allocations, revenue distribution, joint interest billing (Cloud A) | BP-08 to BP-11, BP-13 |
| SYS-04 Cloud A and Cloud B workloads | Historian replica, volume integration, SL-1 portal (A); data platform, ML platform, SL-2 portal (B) | BP-06, BP-08, BP-11, BP-12, BP-16 |
| SYS-05 Identity platform and OT identity domain | SSO, MFA, PAM; separate OT directory | All |
| SYS-06 ERP and payroll | Finance, maintenance work orders, supply chain, payroll | BP-07, BP-13, BP-14, BP-18 |
| SYS-07 Network and IT/OT boundary | WAN, SD-WAN, OT DMZs at the IOC and BCC | All |
| SYS-13 AQ-MC legacy SCADA | Seller platform for 1,700 wells | BP-17 |
| Immutable backups | Separate backup accounts with write-once retention; weekly copies to DC-1 and DC-2; offline SCADA images at the BCC | Recovery of all |
| People | Production Controllers, lease operators, automation technicians, revenue accountants, SOC | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Safety alarm call-out (HSE paging, roving patrols) | Immediate (patrols within 2 h) | Local horns and beacons; shut-in on doubt |
| 2 | OT identity domain, SCADA break-glass accounts, OT DMZ jump hosts | 1 h | Sealed local break-glass accounts |
| 3 | Enterprise SCADA (IOC or BCC) and historians, from verified images | 4 h target (9 h demonstrated, POAM-004) | Manual operations by region |
| 4 | Field communications: private LTE, radio, cellular | 4 h | Patrols; second carrier where installed |
| 5 | Water handling and disposal facility control | 6 h | Local control; trucking |
| 6 | Compressor station control | 6 h | Local control; flaring within limits |
| 7 | Gathering line and LACT control and ticketing | 8 h | Trucking; manual proving |
| 8 | AQ-MC legacy SCADA | 8 h target (untested) | Manual operations |
| 9 | Florida regional SCADA | 4 h target (no standby) | Manual operations; IOC monitoring |
| 10 | Identity platform (corporate), EDR console, SIEM | 2 h, in parallel with priorities 2 to 4 | Break-glass; MSSP tooling |
| 11 | Crude marketing and nominations | 8 h | Phone nominations |
| 12 | Field data capture, volume integration, hydrocarbon accounting | 24 to 48 h | Paper tickets; prior month payment run |
| 13 | SL-1 portal and SL-2 water services portal | 24 h | Mailed statements; email volume reports |
| 14 | ERP, payroll, drilling data, data platform, geoscience | 48 to 72 h | Repeat prior payroll; defer work |

The order puts safety first, then control of the field, then the money. Identity and security tooling recover in parallel with SCADA because recovery from ransomware needs clean credentials and working detection (P08 section 8).

## 8. Gaps carried to other deliverables
| Gap | Carried to |
|---|---|
| IOC-to-BCC failover 9 h against a 4 h RTO | P01 R-005; P02 CP-10; POAM-004 |
| Florida servers without standby; same-room backups; AQ-MC backups untested | P01 R-019, R-002; POAM-005; POAM-009 |
| Cellular carrier concentration, no priority restoration | P01 R-009; P03 GV.SC-05, ID.AM-04; POAM-019 |
| ESP vendor cloud path with setpoint write | P01 R-003; POAM-002 |
| SPCC alarm option relies on SCADA without a tested alternate path | P01 R-027; P03 EPA 112.9 row; POAM-022 |
| Production-loss figures needed for SEC materiality | P08 section 6; POAM-012 |
