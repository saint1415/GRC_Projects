# Business Impact Analysis: Cris Santos Company | Dams | Enterprise

**Organization:** Cris Santos Company, Inc. (publicly traded hydroelectric generation company: 46 developments, 63 dams, 8,640 MW in six southeastern states) | **Tier:** Enterprise (12,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, informed by NIST IR 8286D
**Prepared by:** GRC team with process owners, the Chief Dam Safety Engineer, and the NERC compliance team, 2026-06-01 to 2026-07-31 | **Approved:** Chief Operating Officer and Chief Risk Officer, 2026-08-14 | **Reported to:** safety, risk, and reliability committee of the board, 2026-09-10

## 1. Overview and purpose
This enterprise-wide BIA identifies the business processes the company depends on, how long each can be down, how much data each can lose, and what each depends on, including third parties and the Piedmont acquisition. It feeds:
- the recovery plans required for the HOC BES Cyber Systems (CIP-009-6 R1) and the OT restoration measures in the FERC Security Program Section 9 baseline ("plan and prepare for the restoration and recovery of control systems", Rev. 3A Table 9.3a; Form 3 Question 16);
- the Internal Emergency Response and Rapid Recovery sub-elements of the Security Plans (Rapid Recovery is required for the 4 Group 1 dams, Rev. 3A 3.3.1 and 7.4.2), which must hand off cleanly to the EAPs;
- the availability rating and recovery objectives in the HFCDMS System Security Plan (P02);
- impact ratings in the enterprise risk register (P01), per NIST IR 8286D;
- the recovery order in the incident runbook (P08) and the quantified inputs to the SEC materiality worksheet (P08 section 7);
- the Availability criteria for the two SOC 2 service lines (P09).

**Results in one line:** 18 processes were analyzed; 10 are High criticality, 7 Moderate, and 1 Low. 10 processes need recovery within 4 hours. The dependency map (`dependency-map.csv`) lists 26 dependencies, 14 of them single points of failure (fully or partly) and 6 never tested.

## 2. System and business description
Cris Santos Company owns 31 FERC licenses covering 46 hydroelectric developments, 63 dams, 151 units, and 8,640 MW in Georgia, Alabama, North Carolina, South Carolina, Tennessee, and Virginia, with headquarters in Florida. It has 12,000 employees and about $4.8 billion in annual revenue, 76% from generation. The two Hydro Operations Centers (HOC-A and HOC-B) run 35 developments remotely; 2 small developments and the 9 Piedmont developments acquired in 2025 are run locally. Two service lines sell to other dam owners: SL-1 contract remote operations for 27 client plants and SL-2 dam safety monitoring for 138 client dams. The technology estate is in `../00_company-facts.md` section 3.

**What is different about a dam operator.** For most processes the question is "how long until we lose money." For BP-01, BP-02, BP-09, BP-10, and BP-11 it is also "how long until someone downstream could be hurt." The company can always fall back to **local manual control**: operators at gate and unit panels, and technicians reading instruments by hand. At fleet scale the limit is people and travel time: 35 developments are normally unattended, so the MTDs below measure how long the company can run on dispatched crews safely, not how long a dam can go uncontrolled. No dam is ever left uncontrolled.

## 3. Impact categories and values
Dollar thresholds are scaled to about $13.2 million of revenue per calendar day (about $10.0 million from generation) and to the company's materiality framework (P08 section 7). Values are per 24 hours of outage unless stated.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $1 million per day, or more than $10 million cumulative | $100,000 to $1 million per day | Less than $100,000 per day |
| Operations | HOC control of the fleet lost, or more than 5 developments on local control, or a service line stopped for all clients | One river system, one service line client group, or up to 5 developments affected | Staff slowed but working |
| Regulatory | Condition reportable under 18 CFR 12.10, EAP activation, Reportable Cyber Security Incident, potential NERC violation, or missed SEC filing | Missed contract or documentation deadline; late filing | Internal policy deviation |
| Safety | Plausible harm to the public downstream or to recreation users (uncontrolled release, missed warning) | Worker safety exposure during manual operation | None |
| Reputation | National media, regulator action, ratings or analyst action, or loss of service line clients | Regional media; client complaints | Internal only |

## 4. Process criticality and downtime (from `bia.csv`, in recovery priority order)
| Process | Criticality | MTD | RTO | RPO | Quantified impact per 24 h |
|---|---|---|---|---|---|
| BP-01 Reservoir and spillway gate operations (including flood passage) | High | 4 h | 2 h | 24 h | $0.45M |
| BP-02 Dam safety monitoring and EAP early warning | High | 8 h | 4 h | 1 h | $0.09M |
| BP-03 Generation dispatch and unit control | High | 8 h | 2 h | 15 min | $3.10M |
| BP-04 Pumped storage operations | High | 12 h | 4 h | 15 min | $1.10M |
| BP-05 Blackstart and ancillary service readiness | High | 8 h | 4 h | 24 h | $0.35M |
| BP-06 Real-time data exchange with Balancing Authorities and Transmission Operators | High | 4 h | 1 h | 15 min | $0.20M |
| BP-07 Energy scheduling, trading, and settlement | High | 24 h | 8 h | 1 h | $2.40M |
| BP-08 Physical security monitoring and access control | Moderate | 8 h | 4 h | 24 h | $0.05M |
| BP-09 Piedmont plant operations (PD-01 to PD-09) | High | 8 h | 4 h | 24 h | $0.48M |
| BP-10 SL-1 contract remote operations for client plants | High | 4 h | 2 h | 15 min | $0.25M |
| BP-11 SL-2 dam safety monitoring service | High | 8 h | 4 h | 15 min | $0.15M |
| BP-12 Maintenance management, outage planning, and spare parts | Moderate | 72 h | 48 h | 24 h | $0.30M |
| BP-13 Hydro Services field and engineering services | Moderate | 72 h | 48 h | 24 h | $0.44M |
| BP-14 Regulatory reporting and compliance | Moderate | 24 h | 8 h | 24 h | $0.02M |
| BP-15 Corporate communications, email, and collaboration | Moderate | 24 h | 8 h | 1 h | $0.40M |
| BP-16 Financial close and SEC reporting | Moderate | 120 h | 72 h | 24 h | $0.10M |
| BP-17 Payroll and timekeeping | Moderate | 72 h | 48 h | 24 h | $0.20M |
| BP-18 Recreation reservations and visitor operations | Low | 72 h | 24 h | 24 h | $0.06M |

The quantified impacts add up to about $10.14M per day if every process were down at once. That figure overstates a realistic event, because several processes share the same lost revenue; P08 uses process-level values, not the sum.

**What drives the values:**
- **Life safety** sets the shortest MTDs: gate operations (BP-01, 4 hours to staff local panels at the 23 Group 1 and 2 dams), dam safety monitoring (BP-02), and SL-1 client plants (BP-10).
- **Grid obligations** set BP-05 and BP-06: the Transmission Operators rely on 6 Blackstart Resources and on real-time data over ICCP (CIP-012-2).
- **Cash** drives generation dispatch (BP-03, about $3.1 million per day) and scheduling (BP-07, about $2.4 million per day).
- **Regulation** sets BP-14: CIP-008-6 R4, EOP-004-4, and 18 CFR 12.10 clocks keep running during an outage, so reporting must work from out-of-band tools.
- **Contracts** set BP-10 and BP-11, because external clients rely on them (P09).

**Key finding: the HOC RTO is not demonstrated.** The 2-hour RTO for BP-01 and BP-03 depends on failing over to HOC-B. The 2026-05-16 exercise took 3.4 hours: 95 minutes to staff HOC-B and the rest to resynchronize the SCADA database. Until the retest passes (POAM-010), BP-01 depends on dispatching crews to local panels, which takes up to 4 hours at the most remote Group 2 dams.

## 5. Dependency mapping and third parties
The full map is in `dependency-map.csv`. Key findings:

1. **Telecom concentration (DEP-04).** 19 plants have only one carrier circuit and no microwave path. A carrier outage puts those plants on local control at once, which consumes the crews BP-01 needs during a flood. This is P01 risk R-021 and POAM-011.
2. **OEM concentration (DEP-06).** One OEM services the governors and exciters of 91 of 151 units through remote sessions. Its 2025 renewal skipped the CIP-013-2 procurement terms, and the fallback (OEM technicians on site in 48 to 72 hours) has never been tested.
3. **Piedmont (DEP-18, DEP-19).** All 9 PD plants depend on one integrator and one legacy VPN concentrator, neither restore-tested. The VPN is the after-hours path and the most likely entry for the P08 scenario.
4. **HOC failover (DEP-01, DEP-02, DEP-26).** The failover missed its RTO because of staffing time and database resynchronization, not equipment failure.
5. **Service lines (DEP-12, DEP-20).** The DSMS ingestion service rebuilt in 5.1 hours against a 4-hour RTO. 6 of 27 SL-1 client endpoints still use shared COC credentials.
6. **Unavoidable external dependencies (DEP-08, DEP-09, DEP-17).** Balancing Authorities, Transmission Operators, and county emergency management agencies cannot be duplicated; the fallbacks are procedural and are drilled.

## 6. Resource requirements
| Resource / component | Description | Supports process |
|---|---|---|
| SYS-01 Fleet SCADA at HOC-A and HOC-B | Supervisory control, AGC interface, ICCP, historian | BP-01, BP-03 to BP-06 |
| SYS-02 Plant control systems | Unit PLCs, governors, exciters, plant HMIs | BP-03, BP-04, BP-05 |
| SYS-03 Spillway and gate control | Gate PLCs, local panels, hoists, standby generators | BP-01 |
| SYS-04 Instrumentation and early warning | Data acquisition, gauges, sirens | BP-01, BP-02 |
| SYS-05 OT WAN and DMZs | Microwave, leased circuits, gateways, Intermediate Systems, data diodes | BP-01 to BP-06 |
| SYS-06 Piedmont legacy OT | Local SCADA, legacy VPN | BP-09 |
| SYS-07 Identity | Corporate SSO and the separate OT domain | All |
| SYS-08 Clouds and data centers | Scheduling platform, DSMS, AI platform, ERP | BP-07, BP-11, BP-12, BP-16, BP-17 |
| SYS-11 Scheduling platform | Schedules, trades, settlements | BP-07 |
| SYS-12 DSMS | Instrument data and alerts | BP-02, BP-11 |
| SYS-13 Contract Operations platform | COC consoles and client portal | BP-10 |
| People | 82 HOC operators, plant crews, about 140 dam safety technicians, 34 COC operators, 48 DSMS analysts | All |

**Backup and replication behind the RPOs:** historian replication between HOC-A and HOC-B (BP-01, BP-03 to BP-06); offline SCADA backups at both HOCs; PLC and HMI configuration copies (current at 21 plants, older than 12 months at 14 plants, POAM-008); datalogger buffers and DSMS cross-region replication (BP-02, BP-11); immutable cloud and data center backups (BP-07, BP-12 to BP-18).

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Local manual control of gates and units at affected dams | Immediate at staffed plants; up to 4 h at remote unattended dams | Call-out plan by river system; radio |
| 2 | HOC control from HOC-A or HOC-B (fleet SCADA, gate commands) | 2 h target (3.4 h demonstrated) | Local control until verified |
| 3 | Dam safety instrumentation and sirens | 4 h | Manual readings every 4 hours; local siren activation |
| 4 | ICCP and real-time data to the Balancing Authorities | 1 h | Voice on recorded lines |
| 5 | Identity (OT domain, then corporate) and break-glass access | 1 h | Sealed break-glass accounts |
| 6 | SL-1 Contract Operations Center | 2 h | Client local staffing |
| 7 | Pumped storage and Blackstart Resource readiness | 4 h | Local start procedures |
| 8 | DSMS ingestion and client alerting | 4 h | Phone alerts to High hazard clients |
| 9 | Physical security monitoring | 4 h | Posted officers |
| 10 | Piedmont plants (local) | 4 h | Local operators on site |
| 11 | Scheduling platform | 8 h | Balancing Authority portals |
| 12 | Email, collaboration, regulatory reporting tools | 8 h | Out-of-band phones; printed forms |
| 13 | ERP, maintenance, payroll, field services | 48 h | Paper; repeat prior payroll |
| 14 | Financial close and recreation reservations | 24 to 72 h | Extended close; walk-in sites |

Priority 1 is not a system: it is people at panels. Every OT recovery step in P08 starts by putting gates and units in local control and confirming their physical positions before any system is restored.

## 8. Gaps carried to other deliverables
| Gap | Carried to |
|---|---|
| HOC failover 3.4 h against a 2 h RTO | P01 R-012; P02 CP-7 and CP-10; P03 G-015; POAM-010 |
| Single carrier at 19 plants; HOC-B single ICCP entrance | P01 R-021; P03 G-211 and G-028; POAM-011 |
| OEM concentration and missing CIP-013 terms | P01 R-024; P03 G-050; POAM-014 |
| Piedmont integrator and VPN never tested | P01 R-003; P03 G-096, G-100, G-101; POAM-001 |
| PLC logic backups older than 12 months at 14 plants | P01 R-013; P03 G-054; POAM-008 |
| DSMS ingestion rebuild 5.1 h against 4 h RTO | P01 R-041; P09 A1.3 (SL-2); POAM-020 |
| SL-1 shared COC credentials at 6 client endpoints | P01 R-043; P09 CC6.1 and CC6.2 (SL-1); POAM-021 |
