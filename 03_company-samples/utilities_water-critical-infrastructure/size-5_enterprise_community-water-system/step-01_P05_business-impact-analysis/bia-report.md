# Business Impact Analysis: Cris Santos Company | Water and Wastewater Systems | Enterprise

**Organization:** Cris Santos Company, Inc. (publicly traded parent of four state-regulated community water utilities, plus contract operations and utility billing service lines) | **Tier:** Enterprise (12,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, informed by NIST IR 8286D, with OT recovery guidance from NIST SP 800-82 Rev. 3
**Prepared by:** GRC team with process owners and the Vice President, Resilience and Emergency Management, 2026-06-01 to 2026-07-15 | **Approved:** Chief Operating Officer and Chief Risk Officer, 2026-08-14 | **Reported to:** safety, environmental, and risk committee of the board, 2026-09-10

## 1. Overview and purpose
This enterprise-wide BIA identifies the business processes the company depends on, how long each can be down, how much data each can lose, and what each depends on, including third parties and the three acquired systems that are not yet integrated. It feeds:
- the SDWA section 1433 risk and resilience assessments (RRAs) and emergency response plans (ERPs) for the 86 covered systems (42 U.S.C. 300i-2(a)(1)(A) and (b)): the BIA supplies the consequence values and the "actions, procedures, and equipment" that keep water flowing when automated systems fail;
- the Tier 1 public notice procedure (40 CFR 141.202) through process BP-05;
- the availability and integrity ratings and recovery objectives in the GCR-WTSS System Security Plan (P02);
- impact ratings in the enterprise risk register (P01), per NIST IR 8286D;
- the recovery order in the HMI compromise runbook (P08);
- the Availability criteria for the two SOC 2 service lines (P09).

**Results in one line:** 17 processes were analyzed; 8 are High criticality, 6 Moderate, and 3 Low. 5 processes need recovery within 4 hours (for treatment and distribution, "recovery" means a safe switch to manual operation, not a SCADA restore). The dependency map (`dependency-map.csv`) lists 27 dependencies, 15 of them single points of failure and 5 never tested.

## 2. System and business description
Cris Santos Company owns and operates 126 community water systems in Florida, Georgia, North Carolina, and Tennessee through four regulated subsidiaries. Together they serve about 9.6 million people through about 3.5 million metered connections, from 214 treatment plants and about 1,900 remote sites, supervised from 5 regional operations control centers (ROCCs). The company has 12,000 employees and about $4.8 billion in annual revenue (about $13.2 million per calendar day). It also sells two services to municipal utilities: contract operations and remote monitoring (SL-1, 38 client systems) and utility billing and customer care (SL-2, 27 clients). It provides no wastewater service.

The technology estate is described in `../00_company-facts.md` section 3: regional SCADA (SYS-01), about 6,800 PLCs and RTUs (SYS-02), telemetry (SYS-03), the OT remote access gateway (SYS-04), the identity platform (SYS-05), a multi-cloud estate plus two colocation data centers (SYS-06), the customer information system (SYS-07), AMI (SYS-08), LIMS (SYS-09), GIS and work management (SYS-10), ERP (SYS-11), the enterprise network (SYS-12), about 1,600 vendors (SYS-13), the AI portfolio (SYS-14), and physical security (SYS-15). Six systems were acquired in 2025-2026; three (AQ-04 to AQ-06) still run legacy SCADA.

## 3. Impact categories and values
Dollar thresholds are scaled to about $13.2 million of revenue per calendar day and to the company's materiality framework (P08 section 6). Values are per 24 hours of outage unless stated.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $1 million per day, or more than $10 million cumulative | $100,000 to $1 million per day | Less than $100,000 per day |
| Operations | Loss of treatment or pressure at a system serving more than 50,000 people, or more than one region affected | One plant, one pressure zone, or one service line degraded | Staff slowed but working |
| Regulatory | Tier 1 public notice; MCL or treatment technique violation; reportable chlorine release; missed EPA certification or SEC filing | Missed monitoring or a report due within 48 hours (40 CFR 141.31(b)); missed contractual deadline | Internal policy deviation |
| Safety | Plausible illness from unsafe water, loss of fire flow, or chemical exposure | Precautionary boil water notice with no known contamination | None |
| Reputation | National media, rating agency or analyst action, public utility commission inquiry, or loss of municipal client contracts | Regional media; client complaints | Internal only |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO | Quantified impact per 24 h |
|---|---|---|---|---|---|
| BP-01 Drinking water treatment and chemical feed | High | 12 h | 1 h (to manual) | 24 h | $4.60M |
| BP-02 Distribution pumping, storage, and pressure | High | 6 h | 2 h | 24 h | $1.90M |
| BP-04 Water quality monitoring, laboratories, and compliance reporting | High | 24 h | 12 h | 4 h | $0.30M |
| BP-05 Emergency response, public notification, and primacy agency coordination | High | 24 h | 4 h | 24 h | $0.25M |
| BP-09 Field operations, dispatch, and work management | Moderate | 24 h | 8 h | 24 h | $0.60M |
| BP-06 Customer contact centers | Moderate | 24 h | 8 h | 1 h | $0.42M |
| BP-10 SL-1 contract operations and remote monitoring | High | 12 h | 4 h | 24 h | $0.30M |
| BP-03 Regional supervisory control (ROCCs, SCADA, and telemetry) | High | 48 h | 8 h | 24 h | $0.85M |
| BP-17 Operations at AQ-04 to AQ-06 (legacy SCADA) | High | 12 h | 1 h (to manual) | 168 h (actual) | $0.38M |
| BP-12 Chemical and critical supply chain | High | 72 h | 48 h | 24 h | $0.15M |
| BP-11 SL-2 utility billing and customer care | Moderate | 72 h | 24 h | 4 h | $0.52M |
| BP-07 Billing, payments, and collections | Moderate | 120 h | 72 h | 24 h | $11.80M (deferred) |
| BP-14 Payroll and timekeeping | Moderate | 72 h | 48 h | 24 h | $0.25M |
| BP-13 Financial close and SEC reporting | Moderate | 120 h | 72 h | 24 h | $0.15M |
| BP-08 Meter data management and AMI | Low | 168 h | 120 h | 24 h | $0.09M |
| BP-16 Water quality analytics and anomaly detection (AI-001) | Low | 72 h | 24 h | 24 h | $0.02M |
| BP-15 Engineering, GIS, and capital project delivery | Low | 168 h | 120 h | 24 h | $0.06M |

**What drives the values:**
- **Public health and storage** set the shortest MTDs. Treated-water storage covers about 8 to 24 hours of demand while holding fire reserve (about 12 hours at the Gulf Coast Regional System), and pressure loss can force a precautionary boil water notice within hours. That is why BP-01 and BP-02 have MTDs of 12 and 6 hours.
- **Manual operation, not SCADA, is the recovery strategy for the physical process.** The RTO for BP-01 and BP-17 is the time for licensed operators to take local control (1 hour). SCADA itself (BP-03) has an 8-hour RTO and a 48-hour MTD because plants can run manually for about two days before staff fatigue and mutual aid limits set in. Hardwired chemical feed limits and analyzer alarms stay active in manual mode.
- **Regulatory clocks** set BP-04 and BP-05: a Tier 1 notice and primacy agency consultation no later than 24 hours after the system learns of a situation such as "a failure or significant interruption in key water treatment processes" (40 CFR 141.202(a) Table 1 item (7) and (b)), and a report to the state within 48 hours of a failure to comply with a monitoring requirement (40 CFR 141.31(b)).
- **Cash, not time,** drives billing (BP-07). Tariff rules allow estimated bills, and a delayed cycle defers about $11.8 million per day rather than losing it, so its MTD is 5 days.
- **Contracts** set the SL-1 and SL-2 objectives (BP-10, BP-11), because municipal clients rely on them (P09).
- **SEC reporting** tightens BP-13 during the quarter-end close, when the MTD drops to 48 hours.

## 5. Dependency mapping and third parties
The full map is in `dependency-map.csv`. Key findings:

1. **Acquired systems (DEP-21 to DEP-23).** AQ-04 to AQ-06 serve about 139,300 people on legacy SCADA with no tested restore. PLC logic backups exist only at the former owners' integrators and are about 7 days old at best, so their real RPO is about 168 hours against the 24-hour enterprise target. They have hardwired limits but no written manual-mode procedure for each chemical, and AQ-05's always-on vendor remote desktop agent is the path in the P08 scenario. This is P01 risks R-001, R-003, and R-022 and POA&M item POAM-001.
2. **Backup control center transfer (DEP-01).** The 2026-05-12 GCR drill transferred supervision to the backup control center at TP-B in 3.5 hours against a 2-hour target. Plants ran manually throughout, so service was not affected, but a longer transfer extends manual operation across 111 remote sites. P01 R-010; POAM-010.
3. **Chlorine gas concentration (DEP-15).** One supplier serves TP-A and 4 other Florida plants. TP-A holds about 14 days of chlorine; a second supplier is qualified but not under contract, and the fallback has never been tested. P01 R-020.
4. **Telemetry (DEP-03).** One private LTE core at the GCR ROCC carries 124 of the 138 GCR telemetry endpoints. Standby hardware is in the same building. P01 R-062. The other 14 endpoints are legacy RTUs that use licensed radio on a legacy protocol without message authentication (P01 R-012; POAM-011).
5. **SCADA integrators (DEP-20).** 23 integrators have remote access; 6 still use their own tools outside the gateway at 11 legacy systems, and rebuild support during a regional event depends on their availability. P01 R-005 and R-055; POAM-001 and POAM-012.
6. **Customer systems (DEP-04, DEP-13, DEP-14).** The CIS met its 24-hour RTO in the 2026-05-16 DR test (19 hours). The mass notification service and the telephony carrier are single points of failure during a boil water notice; both have tested manual or broadcast fallbacks. P01 R-039 and R-040.
7. **Mutual aid (DEP-25).** WARN agreements in all four states supply operators and chemicals. Mutual aid operators run plants manually under company supervision and never receive SCADA accounts, which keeps the identity boundary intact during an emergency.

## 6. Resource requirements
| Resource / component | Description | Supports process |
|---|---|---|
| Licensed operators and plant staff | About 2,900 licensed operators; 24x7 plant and ROCC staffing | BP-01 to BP-03, BP-17 |
| SYS-02 PLCs, RTUs, and field devices; hardwired safeguards | Local control and chemical feed limits | BP-01, BP-02, BP-17 |
| SYS-01 regional SCADA and backup control centers | Supervision, alarms, historians | BP-03, BP-10 |
| SYS-03 telemetry | Private LTE, radio, cellular gateways | BP-02, BP-03 |
| SYS-05 identity platform and OT identity domains | SSO, MFA, PAM; sealed break-glass accounts | All |
| SYS-04 OT remote access gateway | Vendor and on-call remote access | BP-03, BP-10 |
| SYS-09 LIMS and the 6 laboratories | Compliance sampling and results | BP-04 |
| Mass notification service, broadcast media, county alerting | Tier 1 and boil water notices | BP-05 |
| SYS-07 CIS (Cloud provider A) | Accounts, billing, call campaigns | BP-05 to BP-07, BP-11 |
| SYS-10 GIS and work management | Maps, valve locations, work orders | BP-09, BP-15 |
| SYS-11 ERP, payroll, and supply chain | Chemical ordering, finance, payroll | BP-12 to BP-14 |
| Colocation DC-1 and DC-2; immutable and offline backups | WAN core, identity nodes, backup copies, offline PLC and HMI images | Recovery of all |
| Generators and fuel contracts | Standby power at all plants and 71% of remote sites | BP-01 to BP-03 |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Manual (local) control of treatment, chemical feed, and pumping at affected plants | 1 h | Licensed operators; hardwired limits and alarms; manual-mode procedures |
| 2 | Distribution pressure: local pressure-switch and level control; roving crews | 2 h | Neighboring interconnects; WARN mutual aid |
| 3 | Grab sampling and laboratory surge | 4 h to start; 12 h for full laboratory function | Portable kits; contract certified laboratories |
| 4 | Public notice capability (mass notification, media, offline contact lists) | 4 h | Broadcast media; posting; county emergency alerting |
| 5 | SYS-05 identity platform and break-glass accounts | 1 h | Sealed break-glass accounts; secondary region |
| 6 | Network core, SD-WAN, and OT DMZ at the affected region | 2 h | Isolate OT and run it standalone |
| 7 | Security tooling (SIEM, EDR console, OT monitoring) for clean-room validation | 4 h | MSSP tooling; offline forensic kits |
| 8 | Supervisory control from the backup control center | 2 h target (3.5 h achieved) | Manual operation continues |
| 9 | Full SCADA restore from offline known-good images after validation | 8 h | Manual operation; integrator support |
| 10 | SL-1 contract-services monitoring platform | 4 h | Standby at the Georgia ROCC; on-site staffing |
| 11 | Contact centers and telephony; CIS | 8 h (telephony); 24 h (CIS) | Backup carrier; scripted answers |
| 12 | GIS and work management | 8 h | Printed map books; radio dispatch |
| 13 | LIMS | 12 h | Paper bench sheets |
| 14 | SL-2 client tenants; billing cycles | 24 h to 72 h | Delayed cycles with client notice |
| 15 | ERP, payroll, and supply chain | 48 h | Phone orders; repeat prior payroll |
| 16 | AQ-04 to AQ-06 SCADA rebuild | Unknown (no tested media) | Manual operation; integrator rebuild (POAM-001) |
| 17 | Historian replication, AI-001, engineering systems | 24 h to 120 h | SCADA alarms; offline map exports |

## 8. Gaps carried to other deliverables
| Gap | Carried to |
|---|---|
| AQ-04 to AQ-06: 168-hour real RPO, no tested rebuild, no manual-mode procedures for each chemical | P01 R-001, R-003, R-022; P03 G-014, G-033, G-043; POAM-001 |
| GCR backup control center transfer 3.5 h against 2 h | P01 R-010; P02 CP-7 and CP-10; P03 G-038; POAM-010 |
| Single chlorine gas supplier for Florida plants; fallback never tested | P01 R-020 |
| Single GCR private LTE core; 14 radio RTUs without message authentication | P01 R-012, R-062; POAM-011 |
| Integrators outside the gateway; retained rebuild capacity not contracted | P01 R-005, R-055; POAM-012 |
| Mass notification and telephony single points of failure during notices | P01 R-039, R-040; P03 G-051 |
| AQ-04 to AQ-06 public notice SOPs lack a cyber trigger | P01 R-011; P03 G-048; POAM-021 |
