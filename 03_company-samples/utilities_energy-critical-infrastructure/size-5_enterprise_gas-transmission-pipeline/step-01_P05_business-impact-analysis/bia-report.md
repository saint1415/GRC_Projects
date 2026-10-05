# Business Impact Analysis: Cris Santos Company | Energy | Enterprise

**Organization:** Cris Santos Company, Inc. (publicly traded interstate natural gas transmission company; 3 owned pipeline systems and 3 operated JV pipelines in 9 states) | **Tier:** Enterprise (12,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, informed by NIST IR 8286D
**Prepared by:** GRC team with process owners, 2026-06-01 to 2026-07-15 | **Approved:** Chief Operating Officer and Chief Risk Officer, 2026-08-14 | **Reported to:** risk committee of the board, 2026-09-10

## 1. Overview and purpose
This enterprise-wide BIA identifies the business processes the company depends on, how long each can be down, how much data each can lose, and what each depends on, including telecommunications carriers, vendors, and the PS-3 acquisition. It feeds:
- the identification of **Critical Cyber Systems** and **business critical functions** in the TSA-approved Cybersecurity Implementation Plan (SD Pipeline-2021-02G Sections III.A and VII.B);
- the Cybersecurity Incident Response Plan, which must reduce the risk of operational disruption to business critical functions (SD 02G Section III.F);
- the availability and integrity ratings and recovery objectives in the PSGCS System Security Plan (P02);
- impact ratings in the enterprise risk register (P01), per NIST IR 8286D;
- the operate-or-shut-down decision and recovery order in the ransomware runbook (P08);
- the Availability criteria for the two SOC 2 service lines (P09).

**Results in one line:** 17 processes were analyzed; 6 are High criticality, 9 Moderate, and 2 Low. 5 processes need recovery within 4 hours. The dependency map (`dependency-map.csv`) lists 25 dependencies, 12 of them single points of failure and 3 never tested.

## 2. System and business description
Cris Santos Company owns three interstate pipeline systems (PS-1 about 5,300 miles, PS-2 about 4,200 miles, PS-3 about 2,100 miles, acquired 2025-03) and operates three joint-venture pipelines (JV-1 to JV-3) for their owners. The network has 96 compressor stations, about 1,480 meter stations, and about 640 remote-controlled valve sites, and serves about 380 shippers. Gas control for PS-1, PS-2, and the JV pipelines runs from GCC-1 in Florida with a hot standby at GCC-2 in Alabama; PS-3 is still controlled from its legacy control room (PS3-CR) in Mississippi. The technology estate is described in `../00_company-facts.md` section 3: SCADA (SYS-01, SYS-02), compressor station controls (SYS-03), field devices (SYS-04), SCADA telecommunications (SYS-05), DMZs and the OT remote access gateway (SYS-06), identity (SYS-07), the hybrid IT estate (SYS-08), the shipper services platform (SYS-09), measurement (SYS-10), ERP (SYS-11), and the integrity and analytics platform (SYS-12).

## 3. Impact categories and values
Dollar thresholds are scaled to about $13.2 million of revenue per calendar day and to the company's materiality framework (P08 section 6). Most revenue is firm reservation charges, so an outage costs money mainly through **reservation charge credits** owed to shippers for curtailed firm service under the tariff, plus response costs. Values are per 24 hours of outage unless stated.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $1 million per day, or more than $10 million cumulative | $100,000 to $1 million per day | Less than $100,000 per day |
| Operations | A pipeline system cannot be controlled remotely, or firm deliveries are curtailed on any system | One region, one service line, or up to 10 compressor stations affected | Staff slowed but working |
| Regulatory | Reportable incident under 49 CFR 191.3; missed TSA, PHMSA, or SEC clock; tariff violation affecting all shippers | Missed contractual or internal deadline | Internal policy deviation |
| Safety | Plausible harm to the public or workers (loss of remote valve control, alarms, or emergency calls) | Reduced safety margin that procedures cover | None |
| Reputation | National media, regulator or analyst action, or loss of a major shipper or JV owner | Regional media; shipper complaints | Internal only |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO | Quantified impact per 24 h |
|---|---|---|---|---|---|
| BP-01 Real-time gas control of PS-1, PS-2, and JV-1 to JV-3 | High | 4 h | 1 h | 0 | $6.80M |
| BP-04 Pipeline emergency response and public safety communications | High | 1 h | 1 h | 0 | $0.20M |
| BP-03 PS-3 gas control (legacy control room PS3-CR) | High | 4 h | 2 h | 0 | $1.90M |
| BP-02 Compressor station operations (96 stations) | High | 8 h | 4 h | 15 min | $3.10M |
| BP-05 Nominations, scheduling, and confirmations (SL-1) | High | 12 h | 4 h | 15 min | $2.40M |
| BP-15 Corporate email, collaboration, and telephony | Moderate | 24 h | 8 h | 4 h | $0.60M |
| BP-09 Capacity release and informational postings | Moderate | 24 h | 8 h | 15 min | $0.20M |
| BP-07 Leak detection and integrity monitoring | Moderate | 24 h | 8 h | 1 h | $0.15M |
| BP-08 Contract operations services for JV pipelines (SL-2) | Moderate | 24 h | 8 h | 4 h | $0.40M |
| BP-12 Regulatory and security reporting | Moderate | 24 h | 12 h | 24 h | $0.05M |
| BP-06 Gas measurement and custody transfer | Moderate | 72 h | 24 h | 0 | $0.30M |
| BP-11 Field work management, dispatch, and operator qualification records | Moderate | 48 h | 24 h | 24 h | $0.35M |
| BP-14 Payroll and timekeeping | Moderate | 72 h | 48 h | 24 h | $0.25M |
| BP-17 Supply chain and materials | Low | 72 h | 48 h | 24 h | $0.08M |
| BP-10 Shipper invoicing and gas accounting | High | 120 h | 72 h | 24 h | $13.00M (deferred) |
| BP-13 Financial close and SEC reporting | Moderate | 120 h | 72 h | 24 h | $0.15M |
| BP-16 Engineering, GIS, and integrity data management | Low | 168 h | 72 h | 24 h | $0.10M |

**What drives the values:**
- **Public safety** sets the shortest MTDs: gas control (BP-01, BP-03), emergency response (BP-04), and compressor stations (BP-02). An RPO of 0 means real-time control data cannot be "restored" from a backup; recovery means regaining trusted, live control.
- **Manual operation sets the gas control MTD.** Station operators and field crews can hold the pipelines in a steady state for about 4 hours. After that, controllers must reduce flows, and firm deliveries are curtailed.
- **PS-3 has no hot standby.** Its RTO of 2 hours is a target the company cannot meet today without manual operation (DEP-03).
- **Cash, not time,** drives invoicing (BP-10). A day of delay in the monthly invoicing window defers about $13 million of collections, so it is High even with a 5-day MTD.
- **Business IT is not needed to move gas safely.** Nominations (BP-05) and measurement (BP-06) have manual workarounds, so their loss alone does not justify a shutdown. This is the central point of the P08 runbook.

## 5. Dependency mapping and third parties
The full map is in `dependency-map.csv`. Key findings:

1. **One SCADA platform at both control centers (DEP-02).** GCC-2 protects against loss of the GCC-1 site, not against a SCADA software fault or compromise that reaches both. The 2026-03 exercise tested IT/OT isolation, not a platform-wide SCADA failure. This is P01 risk R-002.
2. **PS-3 (DEP-03, DEP-06).** PS-3 runs on a legacy SCADA from a single control room with one MPLS carrier and no hot standby. Manual operation of PS-3 has not been drilled at scale since the acquisition. Migration to SYS-01 and GCC-1 is due 2027-06-30 (P01 R-005; POAM-016).
3. **Telecommunications (DEP-05 to DEP-08).** PS-1 and PS-2 have three paths (microwave, two MPLS carriers, satellite at stations). 140 meter and valve sites are cellular-only with no second path (R-024).
4. **Vendors with OT reach (DEP-09, DEP-10, DEP-21).** The SCADA vendor provides no software bill of materials; one compression manufacturer still uses 7 always-on cellular modems outside the OT remote access gateway; the leak model vendor deployed updates outside change control.
5. **IT/OT DMZs (DEP-12).** Closing a DMZ stops measurement and analytics data but not gas control. Isolation was exercised at GCC-1 only (R-012).
6. **Cloud (DEP-14, DEP-15).** The shipper services platform recovered in 3.2 hours against a 4-hour RTO in the 2026-06-09 regional failover test.

## 6. Resource requirements
| Resource / component | Description | Supports process |
|---|---|---|
| SYS-01 SCADA (GCC-1 and GCC-2) | SCADA hosts, consoles, historians, OT domain | BP-01, BP-04, BP-06, BP-07 |
| SYS-02 PS-3 legacy SCADA | Legacy SCADA and PS3-CR | BP-03 |
| SYS-03 Compressor station controls | Unit and station PLCs, station HMIs | BP-02 |
| SYS-04 Field devices | RTUs, PLCs, flow computers, chromatographs | BP-01, BP-03, BP-06 |
| SYS-05 SCADA telecommunications | Microwave, radio, MPLS, satellite, cellular | BP-01 to BP-04, BP-06 |
| SYS-06 DMZs and OT remote access gateway | IT/OT boundary; vendor access | BP-06, BP-07, BP-10 |
| SYS-07 Identity (IT and OT stacks) | SSO and MFA; OT domain and OT privileged access | All |
| SYS-08 Cloud provider A | Shipper services platform, measurement system | BP-05, BP-06, BP-08 to BP-10 |
| SYS-08 Cloud provider B | Integrity, GIS, analytics, AI | BP-07, BP-08, BP-16 |
| SYS-08 Colocation DC-1 and DC-2 | Network core; offline backup copies | Recovery of all IT |
| SYS-11 ERP, payroll, HR | Finance and HR | BP-10, BP-13, BP-14, BP-17 |
| People | Controllers, station operators, field crews, schedulers, SOC, OT engineers | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Gas control for PS-1, PS-2, and JV pipelines (SYS-01 at GCC-1 or GCC-2) | 1 h | Failover to GCC-2; manual operation |
| 2 | Emergency line, field radio, and satellite phones | 1 h | Direct GCC numbers held by 9-1-1 centers |
| 3 | PS-3 gas control (SYS-02) | 2 h target (manual operation today) | Manual station operation |
| 4 | Compressor station controls (SYS-03) | 4 h | Local operation; dispatched crews |
| 5 | OT identity and OT privileged access, then SOC tooling for clean-room validation | 2 h (in parallel with 1 to 4) | Sealed break-glass OT accounts |
| 6 | Enterprise identity platform, network core, and DNS | 2 h | Break-glass accounts; second colocation site |
| 7 | Shipper services platform (nominations and postings) | 4 h | Phone and secure email nominations |
| 8 | Email, collaboration, and telephony | 8 h | Out-of-band conferencing; mobile phones |
| 9 | Integrity analytics and AI-001 | 8 h (after revalidation) | SCADA alarms and patrols |
| 10 | JV owner data portal and statements | 8 h | Secure file transfer |
| 11 | Measurement system | 24 h | Field collection; SCADA estimates |
| 12 | Work management and learning systems | 24 h | Printed rosters |
| 13 | ERP and payroll | 48 h | Repeat prior payroll |
| 14 | Invoicing and gas accounting | 72 h | Prior-month templates |
| 15 | Engineering, GIS, and integrity records | 72 h | Offline map packages |

## 8. Gaps carried to other deliverables
| Gap | Carried to |
|---|---|
| One SCADA platform at both control centers; platform-wide failure not exercised | P01 R-002; P03 G-034; POAM-011 |
| PS-3 without hot standby, single carrier, manual operation not drilled | P01 R-005 and R-024; P03 G-032; POAM-016 |
| GCC-2 and PS3-CR IT/OT isolation not exercised | P01 R-012; P03 G-030 and G-031; POAM-012 |
| 140 cellular-only sites without a second path | P01 R-024; POAM-021 |
| Always-on vendor modems at compressor stations | P01 R-008; P03 G-012; POAM-004 |
| Leak model vendor updates outside change control | P01 R-040; P10; POAM-019 |
