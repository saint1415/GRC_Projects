# Business Impact Analysis: Cris Santos Company | Nuclear Reactors, Materials, and Waste | Enterprise

**Organization:** Cris Santos Company, Inc. (publicly traded nuclear generation company: four stations, seven units, about 8,030 MW) | **Tier:** Enterprise (12,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, informed by NIST IR 8286D
**Prepared by:** GRC team with process owners, 2026-06-01 to 2026-07-15 | **Approved:** Chief Nuclear Officer and Chief Risk Officer, 2026-08-14 | **Reported to:** risk committee of the board, 2026-09-10

## 1. Overview and purpose
This enterprise-wide BIA identifies the business processes the fleet depends on, how long each can be down, how much data each can lose, and what each depends on, including third parties and the acquired Station 4. It feeds:
- the business IT contingency and disaster recovery plans, including the work management system (WMS) plan;
- the availability rating and recovery objectives in the WMS-PBN System Security Plan (P02);
- impact ratings in the enterprise risk register (P01), per NIST IR 8286D;
- the recovery order in the cyber incident runbook (P08);
- the Availability criteria for the two SOC 2 service lines (P09).

**What this BIA does not replace.** Recovery of critical digital assets (CDAs) is governed by each station's cyber security plan (10 CFR 73.54(e)(2)(iv)) and by plant procedures. Reactor safety functions do not depend on business IT. This BIA records the business impact of losing CDA-supported functions so that leadership sees the whole picture, but it sets no requirement for CDAs.

**Results in one line:** 17 processes were analyzed; 9 are High criticality, 7 Moderate, and 1 Low. 6 processes need recovery within 4 hours. The dependency map (`dependency-map.csv`) lists 26 dependencies, 16 of them single points of failure and 7 never tested.

## 2. System and business description
Cris Santos Company operates seven units at four stations: Station 1 (Florida, 2 units), Station 2 (Georgia, 2 units), Station 3 (South Carolina, 2 units), and Station 4 (Alabama, 1 unit, acquired 2025-07-01). It has 12,000 employees and about $4.8 billion in annual revenue, and it adds 1,200 to 1,500 contractors at a station during each refueling outage. The technology estate is described in `../00_company-facts.md` section 3: the plant business networks (SYS-01), the fleet work management system (SYS-02), the identity platform (SYS-03), a multi-cloud estate in two public clouds plus two data centers (SYS-04), the CDAs, security, and emergency preparedness systems under the cyber security plans (SYS-05 to SYS-07), the Generation Dispatch Center (SYS-08), ERP and payroll (SYS-09), access authorization systems (SYS-10), and the two service line platforms (SYS-12, SYS-13). Station 4 still runs the prior owner's directory, network, and work management system under a transition services agreement that ends 2027-06-30.

## 3. Impact categories and values
Dollar thresholds are scaled to about $13.2 million of revenue per calendar day and to the company's materiality framework (P08 section 6). Values are per 24 hours of outage unless stated.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $1 million per day, or more than $10 million cumulative | $100,000 to $1 million per day | Less than $100,000 per day |
| Operations | Loss of generation at a unit, a refueling outage extended, or a station-wide stop of work control | One station or one function slowed but working | Staff slowed, no schedule impact |
| Regulatory | Missed NRC notification or Technical Specification requirement; NERC CIP violation; missed SEC filing | Missed written report or contractual deadline | Internal procedure deviation |
| Safety | Plausible harm to workers (wrong clearance boundary, uncontrolled dose) or to the public | Delayed but safe work | None |
| Reputation | National media, NRC escalated enforcement, analyst or ratings action, loss of service line clients | Regional media; client complaints | Internal only |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO | Quantified impact per 24 h |
|---|---|---|---|---|---|
| BP-01 Unit operation and power generation (7 units) | High | 8 h | 4 h | 15 min | $15.80M (fleet-wide worst case) |
| BP-03 Plant physical security | High | 15 min | 4 h | 15 min | $0.12M per station |
| BP-04 Emergency preparedness and offsite communications | High | 1 h | 1 h | 0 | $0.05M |
| BP-02 Generator operator dispatch and grid communications | High | 1 h | 1 h | 0 | $0.25M |
| BP-05 Radiation protection and worker dose control | High | 8 h | 4 h | 15 min | $0.60M |
| BP-07 Refueling outage execution | High | 12 h | 4 h | 15 min | $3.20M |
| BP-06 Work management, clearance and tagging, and surveillance scheduling | High | 24 h | 8 h | 15 min | $0.75M |
| BP-08 Access authorization and fitness-for-duty processing | High | 24 h | 12 h | 1 h | $0.50M |
| BP-12 Energy scheduling, PPA settlement, and wholesale sales | High | 24 h | 8 h | 1 h | $0.90M |
| BP-09 Engineering, design control, and document management | Moderate | 48 h | 24 h | 4 h | $0.20M |
| BP-15 Monitoring and diagnostics service (fleet and SL-1 clients) | Moderate | 48 h | 24 h | 4 h | $0.18M |
| BP-14 Payroll and timekeeping | Moderate | 72 h | 48 h | 24 h | $0.20M |
| BP-16 Dosimetry processing and dose records (fleet and SL-2 clients) | Moderate | 72 h | 24 h | 4 h | $0.12M |
| BP-11 Supply chain, warehousing, and safety-related procurement | Moderate | 72 h | 48 h | 4 h | $0.25M |
| BP-17 Licensing and regulatory correspondence | Moderate | 24 h | 12 h | 4 h | $0.02M |
| BP-13 Financial close and SEC reporting | Moderate | 120 h | 72 h | 24 h | $0.15M |
| BP-10 Nuclear fuel management and procurement | Low | 168 h | 72 h | 24 h | $0.05M |

The table is in recovery priority order. BP-03 has an MTD of 15 minutes because the security plan requires compensatory measures as soon as a security system is lost; the compensatory measures, not IT recovery, meet that limit.

**What drives the values:**
- **Safety and the license** set the shortest limits: plant security (compensatory measures), emergency preparedness (the Emergency Response Data System must be activated within 1 hour after declaring an Alert or higher, 10 CFR 50.72(a)(4)), and radiation protection.
- **Refueling outages change the numbers.** Online, the WMS can be down for a day using printed schedules and paper clearances. During an outage, each day of delay costs about $3.2 million (about one unit-day of generation plus contractor standby), so the WMS RTO tightens from 8 hours to 4 hours and access authorization from 24 hours to 12 hours.
- **Integrity matters more than availability for the WMS.** A wrong clearance boundary can injure a worker, and a surveillance scheduled past its Technical Specification interval forces required actions. The WMS RPO of 15 minutes protects clearance and surveillance records; P02 treats WMS integrity as High.
- **Cash, not time,** drives energy scheduling and settlement (BP-12): PPA invoices are about $400 million a month.
- **Contracts** set the SL-1 and SL-2 objectives (BP-15, BP-16), and **regulation** sets dose record retention until license termination (10 CFR 20.2106(f)).

## 5. Dependency mapping and third parties
The full map is in `dependency-map.csv`. Key findings:

1. **Single fleet WMS (DEP-01, DEP-02).** One WMS instance serves Stations 1 to 3. It recovered in 11 hours against its 8-hour RTO in the 2026-05-09 disaster recovery test, and the 4-hour outage-mode RTO has never been tested (POAM-010). Read-only edge servers at each station keep printed schedules and clearance indexes available.
2. **Station 4 legacy systems (DEP-23, DEP-24).** The prior owner's directory and work management system run under a transition services agreement with a 48-hour RTO, against the 8-hour BIA RTO. Neither has been tested. The agreement ends 2027-06-30 and the WMS migration is planned for 2027-05 (POAM-022).
3. **Outage contractors (DEP-11, DEP-12).** Two contractors carry about 80% of outage contractor hours. Contractor B's reactor vessel inspection tooling has no substitute inside an outage window. Contractor A's contract does not require prompt notice when its staff leave (POAM-006).
4. **Access authorization (DEP-13 to DEP-15).** The shared industry personnel access database and NRC fingerprint processing are industry-wide single points of failure the company cannot remove. The background screening vendor's contract lacks the confidentiality clause that 10 CFR 73.56(m)(3) requires (P03 G-066).
5. **Defensive architecture (DEP-08).** The one-way data transfer devices are single paths by design. If one fails, plant data stops flowing to the business network, the WMS and M&D center lose live readings, and the CDAs are unaffected. This is the intended failure mode.
6. **Service line vendors (DEP-16, DEP-17).** The M&D analytics vendor has no SOC report (POAM-016), and the dosimetry dose record database has never been restored from backup (POAM-019).

## 6. Resource requirements
| Resource / component | Description | Supports process |
|---|---|---|
| SYS-05 to SYS-07 CDAs, security, and emergency preparedness systems | Plant computers, control systems, security and emergency systems under the cyber security plans | BP-01, BP-03, BP-04, BP-05 |
| SYS-02 Fleet WMS | Work orders, clearances, surveillance schedules, outage schedules | BP-06, BP-07, BP-09, BP-11 |
| SYS-01 Plant business networks | Station LANs, Wi-Fi, outage trailers, edge servers, historian replicas | BP-05 to BP-09 |
| SYS-03 Identity platform | SSO, MFA, PAM, identity governance | All |
| SYS-04 Cloud provider A | WMS workload account, integration services | BP-06, BP-07, BP-11, BP-12 |
| SYS-04 Cloud provider B | M&D platform, dosimetry client portal, AI services | BP-15, BP-16 |
| SYS-04 DC-1 and DC-2 | EDMS, dosimetry database, network core, offline backup copies | BP-09, BP-16; recovery of all |
| SYS-08 Generation Dispatch Center | Primary and backup GDC | BP-02, BP-12 |
| SYS-09 ERP and payroll | Finance, supply chain, payroll | BP-11, BP-13, BP-14 |
| SYS-10 Access authorization and FFD systems | Background investigations, badging, FFD records | BP-08 |
| Immutable backups | Separate backup accounts with write-once retention; weekly copy to DC-2 | RPO for all cloud workloads |
| People | Licensed operators, security force, radiation protection, work control, outage contractors, SOC | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | CDA-supported plant functions (under the cyber security plans) | Per plant procedures | Control room indications; abnormal operating procedures; power reduction or shutdown |
| 2 | Physical security systems | 4 h | Compensatory measures under the security plan |
| 3 | Emergency preparedness systems and offsite communications | 1 h | Backup communications under the emergency plan |
| 4 | Generation Dispatch Center | 1 h | Backup GDC at Station 2; recorded voice dispatch |
| 5 | Identity platform and break-glass accounts | 1 h | Sealed break-glass accounts; secondary region |
| 6 | Network core, station business networks, DNS | 2 h | Cellular backup for critical users |
| 7 | Security tooling (EDR console, SIEM) for clean-room validation | 2 h | MSSP tooling |
| 8 | Radiation protection business systems (electronic dosimetry servers, permits) | 4 h | Paper permits and self-reading dosimeters |
| 9 | WMS and edge servers | 4 h in an outage; 8 h online | Printed schedules; paper clearances with independent verification |
| 10 | Access authorization and badging systems | 12 h (outage); 24 h online | Escorted access; manual verification calls |
| 11 | Energy scheduling and settlement platform | 8 h | Phone and email schedules |
| 12 | EDMS and engineering systems | 24 h | Controlled hard copies at stations |
| 13 | M&D platform and dosimetry systems | 24 h | Route-based monitoring; interim dose estimates |
| 14 | ERP, payroll, and supply chain | 48 h | Repeat prior payroll; manual parts issue |
| 15 | Financial close and fuel management systems | 72 h | Extended close calendar |

## 8. Gaps carried to other deliverables
| Gap | Carried to |
|---|---|
| WMS recovered in 11 h against an 8 h RTO; outage-mode RTO untested | P01 R-010; P02 CP-10; POAM-010 |
| Station 4 legacy systems with a 48 h agreement RTO | P01 R-034, R-035; POAM-022 |
| Outage contractor notice clause missing | P01 R-004; POAM-006 |
| M&D analytics vendor without a SOC report | P01 R-020; POAM-016 |
| Dosimetry dose record database never restore-tested | P01 R-026; P03; POAM-019 |
| Station 4 single carrier | P01 R-033; POAM-021 |
