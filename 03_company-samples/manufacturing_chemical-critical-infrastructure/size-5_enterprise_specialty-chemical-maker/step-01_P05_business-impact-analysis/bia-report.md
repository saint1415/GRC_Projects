# Business Impact Analysis: Cris Santos Company | Chemical | Enterprise

**Organization:** Cris Santos Company, Inc. (publicly traded specialty chemical formulator and packager, NAICS 325998) | **Tier:** Enterprise (12,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, informed by NIST IR 8286D
**Prepared by:** GRC team with process owners and plant managers, 2026-05-04 to 2026-07-10 | **Approved:** Chief Operating Officer and Chief Risk Officer, 2026-09-08 | **Reported to:** risk committee of the board, 2026-09-10

## 1. Overview and purpose
This enterprise-wide BIA identifies the business processes the company depends on across 14 plants, 9 distribution centers, and 2 R&D centers, how long each can be down, how much data each can lose, and what each depends on, including third parties and the three plants acquired in 2025. It feeds:
- the OT contingency plans for each plant and the IT disaster recovery plan;
- the availability rating and recovery objectives in the Gulf Coast Complex Process Control and Batch Management System (GC-PCBMS) System Security Plan (P02);
- the emergency response and notification elements of the RMP and PSM programs at the 8 RMP plants (40 CFR 68.90 and 68.95; 29 CFR 1910.119(n)), which must work when the business network does not;
- the PLT-01 MTSA Cybersecurity Plan, whose incident response and resilience sections need recovery targets for the terminal systems (33 CFR 101.650(g) and (h));
- impact ratings in the enterprise risk register (P01), per NIST IR 8286D;
- the recovery order in the OT intrusion runbook (P08);
- the Availability and Processing Integrity criteria for the two SOC 2 service lines (P09).

**Results in one line:** 18 processes were analyzed; 11 are High criticality and 7 Moderate. 6 processes need recovery within 8 hours, and 3 within 4 hours. The dependency map (`dependency-map.csv`) lists 28 dependencies, 15 of them single points of failure and 5 never tested.

## 2. System and business description
Cris Santos Company formulates, blends, packages, and ships specialty chemicals from 14 plants in eight states, with about $4.8 billion of revenue a year (about $13.2 million per calendar day). The flagship PLT-01 Gulf Coast Complex in Florida produces about 19% of company volume and is the only plant where MTSA, OSHA PSM, RMP Program 3, and the DOT hazmat security plan all meet. The technology estate is described in `../00_company-facts.md` section 3: plant process control (SYS-01 at PLT-01, SYS-02 at the other plants), the enterprise OT security services (SYS-03), the identity platform (SYS-04), the ERP and MES (SYS-05), the LIMS (SYS-06), a multi-cloud estate with two colocation data centers (SYS-07), the SD-WAN (SYS-08), the SL-1 telemetry platform (SYS-10), and the transportation management system (SYS-11). PLT-12, PLT-13, and PLT-14 were acquired in 2025 and still run legacy OT and a legacy ERP.

**How a chemical BIA differs.** For most processes the first question is not "how long until we lose money" but "how long can the plant run safely without this". Two processes (BP-02 safety instrumented functions and BP-13 emergency notification) have no revenue impact at all and still carry the shortest recovery targets, because they protect workers and the public. A plant whose control system cannot be trusted goes to a safe state first; revenue loss follows from that decision.

## 3. Impact categories and values
Dollar thresholds are scaled to about $13.2 million of revenue per calendar day and to the company's materiality framework (P08 section 6). Values are per 24 hours of outage unless stated.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $2 million per day, or more than $10 million cumulative | $250,000 to $2 million per day | Less than $250,000 per day |
| Operations | A plant or enterprise service stops, or more than 3 plants are affected | One unit, one product family, or one region is affected | Staff slowed but working |
| Regulatory | Reportable release; RMP, PSM, or MTSA finding; missed SEC filing or 8-K | Missed contractual or documentation deadline | Internal policy deviation |
| Safety | Plausible loss of containment of a toxic or flammable chemical, worker injury, or loss of drinking water treatment supply | Reduced safety margin with compensating manual measures | None |
| Reputation | National media, analyst or ratings action, community or regulator scrutiny, or loss of major customers | Regional media; customer complaints | Internal only |

**Criticality rule.** High when Safety is Severe, or when two or more categories are Severe and the MTD is 72 hours or less. Otherwise Moderate when any category is Moderate or Severe.

## 4. Process criticality and downtime (from `bia.csv`)
Rows are in recovery priority order.

| Process | Criticality | MTD | RTO | RPO | Quantified impact per 24 h |
|---|---|---|---|---|---|
| BP-02 Safety instrumented functions and emergency shutdown (PLT-01, PLT-04, PLT-05) | High | 8 h | 4 h | 0 (approved logic) | $2.00M |
| BP-13 Emergency notification and release reporting | High | 1 h | 0.5 h | 24 h | Not a revenue process |
| BP-01 Controlled batch production at PLT-01 | High | 24 h | 12 h | 24 h | $2.50M |
| BP-03 Ammonia unit and Chlor Unit operations at PLT-01 | High | 24 h | 12 h | 24 h | $0.90M |
| BP-05 Batch production at PLT-02 to PLT-11 | High | 24 h | 12 h | 24 h | $8.45M (enterprise-wide event) |
| BP-06 Order to ship and hazmat shipping documentation | High | 24 h | 8 h | 1 h | $6.50M |
| BP-07 Truck and rail loading | High | 24 h | 8 h | 24 h | $3.20M |
| BP-08 Quality release and certificates of analysis | High | 24 h | 8 h | 1 h | $5.90M |
| BP-09 Supply to municipal water utilities | High | 72 h | 24 h | 24 h | $1.10M |
| BP-04 Marine terminal receipts at PLT-01 | Moderate | 72 h | 24 h | 24 h | $0.18M |
| BP-10 Tank telemetry and VMI service (SL-1) | High | 24 h | 4 h | 15 min | $0.42M |
| BP-18 Production at the acquired plants (PLT-12 to PLT-14) | High | 24 h | 24 h | 24 h (target; real RPO unknown) | $2.20M |
| BP-17 Process safety records (MOC, PHA, mechanical integrity) | Moderate | 72 h | 24 h | 24 h | $0.10M |
| BP-11 Toll manufacturing and contract formulation (SL-2) | Moderate | 72 h | 24 h | 1 h | $0.55M |
| BP-12 Procurement and inbound raw materials | Moderate | 72 h | 48 h | 24 h | $0.30M |
| BP-16 Customer and technical service, including SDS distribution | Moderate | 48 h | 24 h | 24 h | $0.20M |
| BP-14 Payroll and timekeeping | Moderate | 72 h | 48 h | 24 h | $0.25M |
| BP-15 Financial close and SEC reporting | Moderate | 120 h | 72 h | 24 h | $0.15M |

IT and cloud recoveries (BP-06, BP-08, BP-10) run in parallel with plant recovery under separate teams, so a lower priority number does not mean a later start.

**What drives the values:**
- **Safety** sets the shortest MTDs. If the safety instrumented systems (BP-02) cannot be trusted, the ammonia unit and Chlor Unit must be isolated and emptied within one shift. Emergency notification (BP-13) must work within the hour because CERCLA and EPCRA release notices are due immediately (40 CFR 302.6(a); 355.40), and RMP sources must have a working mechanism to notify emergency responders (68.90(b)(3); 68.95(a)(1)(i)).
- **Trust, not time,** sets the RPO for safety logic. The only acceptable restore point for SIS programs and DCS control logic is the copy approved through management of change, so the RPO is "approved logic" rather than a number of hours.
- **Revenue concentration** drives the production processes. An enterprise-wide OT event (a shared service such as the remote access gateway or the OT backup vault compromised) would stop about $13.15 million a day across BP-01, BP-05, and BP-18, which is nearly all daily revenue.
- **Public health** drives water utility supply (BP-09). Utilities hold 5 to 7 days of stock, so the MTD is 72 hours, but a longer outage could affect drinking water treatment.
- **Contracts** set the SL-1 telemetry (BP-10) and SL-2 toll manufacturing (BP-11) objectives, because external customers rely on them (P09).
- **Regulation** tightens financial close (BP-15) during the quarter-end window, when the MTD drops to 48 hours because of SEC filing deadlines.

## 5. Dependency mapping and third parties
The full map is in `dependency-map.csv`. Key findings:

1. **Shared OT services are a single point of failure across plants (DEP-04).** The central remote access gateway serves 11 plants and the OT backup vault serves 11. This is good for control, but a compromise of either would affect every plant at once. Only 1 of 3 PLT-01 DCS areas has had a restore test from the vault (POAM-003).
2. **Acquired plants (DEP-24 to DEP-26).** PLT-12, PLT-13, and PLT-14 run flat IT/OT networks with integrator remote tools outside the gateway and local, untested OT backups. Their real RPO is unknown and recovery could take weeks. PLT-14 supplies water utilities in North Carolina, so it also affects BP-09 (POAM-014; POAM-015).
3. **Safety system dependencies (DEP-03).** Each SIS is a single logic solver by design, to stay independent of the DCS. That is correct, but comparison of the running programs with the approved copies is manual and irregular (POAM-009).
4. **Emergency notification depends on the business network at 9 plants (DEP-27).** VoIP on the business network is the primary call path. Cellular phones, printed call lists, and radios are in place at PLT-01, PLT-04, and PLT-05 only (POAM-017).
5. **Raw material single sources (DEP-14, DEP-15).** One supplier provides all anhydrous ammonia and one provides all chlorine ton containers. These are supply risks, not cyber risks, but they shape how fast BP-03 and BP-09 can recover.
6. **OT vendors and integrators (DEP-01, DEP-02).** The PLT-01 DCS vendor's support contract has no security notification clause, and 2 of the 6 enterprise integrators have no security clauses (POAM-010). Three PLT-01 integrator accounts on the gateway were shared (POAM-005).
7. **Telemetry carrier concentration (DEP-10).** One cellular carrier serves about 80% of the 41,000 tank sensors. Dual-SIM sensors are rolled out at contract renewal.
8. **Cloud and SaaS (DEP-06 to DEP-09, DEP-19, DEP-20).** All met their recovery targets in the 2026 tests or by contract. The ERP is a single SaaS instance and the most important IT dependency for shipping.

## 6. Resource requirements
| Resource / component | Description | Supports process |
|---|---|---|
| SYS-01 GC-PCBMS (PLT-01) | DCS, batch management, Ammonia Unit SIS, Chlor Unit SIS, terminal automation and safety PLC, historian | BP-01 to BP-04, BP-07, BP-11 |
| SYS-02 plant process control | 3 DCS platforms, about 420 PLCs, SIS at 8 plants | BP-02, BP-05, BP-07, BP-18 |
| SYS-03 enterprise OT security services | Remote access gateway, OT backup vault, OT monitoring, patch and media staging | All plant processes |
| SYS-04 identity platform | SSO, MFA, PAM, identity governance, gateway authentication | All IT processes; remote OT engineering |
| SYS-05 ERP and MES | Orders, inventory, bills of material, shipping, finance | BP-06, BP-09, BP-12, BP-14, BP-15 |
| SYS-06 LIMS | Testing, release, certificates of analysis | BP-08, BP-11 |
| SYS-07 cloud estate and colocation | Cloud provider A (LIMS, data platform, AI/ML), Cloud provider B (SL-1), DC-1 and DC-2 | BP-08, BP-10, BP-11, BP-15 |
| SYS-10 telemetry and VMI platform | Tank sensors, customer portal, replenishment orders | BP-09, BP-10 |
| SYS-11 TMS and fleet telematics | Hazmat shipments and en route security | BP-06, BP-07 |
| Emergency notification kit | Cellular phones, printed call lists, radios, mass notification service | BP-13 |
| People | About 310 PLT-01 operators, controls engineers, I&E technicians, QC lab staff, the PLT-01 hazardous materials team, the SOC, and the OT Security Center of Excellence | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Safe state of the PSM units: SIS verified against approved logic; ammonia unit and Chlor Unit isolated if trust is lost | Immediate; SIS trust confirmed within 4 h | Manual emergency shutdown from field stations; continuous operator rounds |
| 2 | Emergency notification path (cellular phones, call lists, radios, mass notification) | 30 min | Radios and runners to the gate; 911 by cellular |
| 3 | Identity platform, break-glass accounts, and security tooling (EDR console, SIEM, OT monitoring) for clean-room validation | 1 to 2 h | Sealed break-glass accounts; MSSP tooling |
| 4 | OT backup vault and clean engineering workstations | 4 h | Second vault copy at DC-2 |
| 5 | PLT-01 DCS and batch management, one area at a time (ammonia unit and Chlor Unit first, then blend halls and additives unit) | 12 h per area | Hold batches; manual batches in Blend Hall 3; shift volume to PLT-03 and PLT-06 |
| 6 | DCS and PLCs at PLT-02 to PLT-11 (plants with RMP processes first) | 12 h per plant | Shift volume between plants |
| 7 | ERP, TMS, and shipping documentation | 8 h | Manual bills of lading and printed shipping papers |
| 8 | Loading rack automation | 8 h | Manual loading with weigh-scale verification at the 4 largest plants |
| 9 | LIMS and certificates of analysis | 8 h | Paper results; templated certificates signed by the plant quality manager |
| 10 | Water utility allocation (ERP and telemetry) | 24 h | Allocate from DC inventory; daily calls to the top 200 utilities |
| 11 | PLT-01 terminal automation and tank gauging | 24 h | Delay barges; manual gauging with two-person checks |
| 12 | SL-1 telemetry platform (Cloud provider B, parallel team) | 4 h | Customers phone in orders |
| 13 | Legacy OT at PLT-12 to PLT-14 | 24 h target (real recovery unknown) | Safe state; move volume to PLT-02, PLT-03, PLT-07, PLT-10, and PLT-11 |
| 14 | MOC and PSM records, toll batch records portal | 24 h | Paper MOC; batch records by encrypted email |
| 15 | Procurement, customer service, payroll, and financial close | 48 to 72 h | Phone orders; repeat prior payroll; extended close calendar |

## 8. Gaps carried to other deliverables
| Gap | Carried to |
|---|---|
| OT restore tested for 1 of 3 PLT-01 DCS areas | P01 R-007; P02 CP-4; POAM-003 |
| SIS program comparison manual and irregular | P01 R-003; P02 SI-7; POAM-009 |
| Acquired plants with flat networks, outside remote access, and untested local backups | P01 R-010 and R-011; P03 G-097 and G-098; POAM-014 and POAM-015 |
| Emergency notification depends on business VoIP at 9 plants | P01 R-021; P03 G-061 and G-074; POAM-017 |
| DCS vendor and 2 integrators without security clauses; shared integrator accounts | P01 R-013; P02 SR-6 and AC-2; POAM-005 and POAM-010 |
| TMS and telematics not in the DOT security plan risk assessment | P01 R-024; P03 G-077; POAM-018 |
| Single cellular carrier for 80% of telemetry sensors | P01 R-047 |
