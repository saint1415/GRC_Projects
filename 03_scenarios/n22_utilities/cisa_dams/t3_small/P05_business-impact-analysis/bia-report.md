# Business Impact Analysis: Cris Santos Company | Dams | Small

**Organization:** Cris Santos Company, LLC (licensee of the fictional Cypress Fork Hydroelectric Project) | **Tier:** Small (187 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Plant Manager and IT Manager with the Chief Dam Safety Engineer, Controller, and process owners | **Approved:** Vice President of Operations, 2026-08-31

## 1. Overview and purpose
This BIA identifies which processes the company depends on, how long each can be down, and how much data it can lose. It supports:
- the OT contingency plan and recovery procedure required by the FERC Security Program Section 9 baseline measures ("plan and prepare for the restoration and recovery of control systems", Rev. 3A Table 9.3a) and Form 3 Question 20 (identify essential systems and processes);
- the Internal Emergency Response sub-element of the Group 2 Security Plan (Rev. 3A 7.4.1), which must hand off cleanly to the EAP;
- the availability ratings in the SSP (P02), the impact ratings in the risk register (P01), and the recovery order in the incident runbook (P08).

## 2. System and business description
The company runs one hydroelectric project on one site: a High hazard potential dam with 4 spillway gates, a 30 MW powerhouse, dam safety instrumentation, and downstream sirens, all controlled by the Plant Control and Dam Monitoring System (PCDMS). Around it sit the corporate network and SaaS services, a cloud tenant for reporting and backups, a hydro field services business, and license-required recreation facilities. See `../scenario-facts.md` sections 1 and 3.

**What is different about a dam.** For most processes the question is "how long until we lose money." For the first two processes here it is "how long until someone downstream could be hurt." The company can always fall back to **manual local control**: operators at the gate panels and unit panels, and technicians reading instruments by hand. So the MTDs below measure how long the company can run on those workarounds safely, not how long the dam can go uncontrolled. The dam is never left uncontrolled.

## 3. Impact categories and values
Dollar values are scaled to $21.8 million in annual revenue (about $59,700 per day). Generation alone is about $37,800 per day at average output.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $150,000 (about 4 days of generation) | $25,000 to $150,000 | Less than $25,000 |
| Operations | Gates or units cannot be controlled even locally, or the site must be evacuated | One process runs only on manual workarounds | Staff slowed but working |
| Regulatory | Condition reportable under 18 CFR 12.10, EAP activation, or a FERC directive | Missed internal or contract deadline; late filing | Internal policy deviation |
| Safety | Plausible harm to the public downstream or to recreation users (uncontrolled release, missed warning) | Worker safety exposure during manual operation | None |
| Reputation | Regional media coverage; loss of offtaker or community confidence | Complaints from recreation users or customers | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Reservoir and spillway gate operations | High | 4 h | 2 h | 24 h |
| BP-02 Dam safety monitoring and EAP early warning | High | 8 h | 4 h | 1 h |
| BP-03 Power generation and unit control | High | 24 h | 12 h | 24 h |
| BP-04 Physical security monitoring and access control | Moderate | 8 h | 4 h | 24 h |
| BP-05 Offtaker scheduling, telemetry, and settlement | Moderate | 24 h | 8 h | 24 h |
| BP-06 Corporate communications and email | Moderate | 24 h | 8 h | 24 h |
| BP-07 Regulatory compliance and FERC reporting | Moderate | 72 h | 48 h | 24 h |
| BP-08 Maintenance management and spare parts | Moderate | 72 h | 48 h | 24 h |
| BP-09 Hydro field services | Moderate | 72 h | 48 h | 24 h |
| BP-10 Recreation reservations and visitor operations | Low | 48 h | 24 h | 24 h |
| BP-11 Finance, payroll, and HR | Low | 120 h | 72 h | 24 h |

Totals: 3 High, 6 Moderate, 2 Low.

**What drives the values:**
- **BP-01 (MTD 4 hours).** Running all 4 gates from local panels needs at least 3 operators on site and radio contact. The company can staff that around the clock for about 4 hours before fatigue and shift coverage become unsafe, especially during a flood. After that, the SCADA control must be back.
- **BP-02 (RPO 1 hour).** Data loggers keep 30 days of readings locally, so data is rarely lost. The 1-hour RPO reflects the historian gap tolerated for trend review. Unusual readings are reportable conditions under 18 CFR 12.3(b)(4)(viii), so manual readings must start within 4 hours.
- **BP-03.** Generation revenue drives the value, not safety. Units can run locally at reduced flexibility.

**Key finding: the OT RTOs are unproven.** The 2-hour RTO for the PCDMS depends on rebuilding HMI servers and reloading PLC logic from known-good copies. Today those copies are irregular (last one 2026-04-11), sit on the same network as the systems they protect, and have never been restored (P01 R-009, P07 POAM-006 and POAM-007). Until the first restore test passes, BP-01 and BP-03 depend entirely on manual local control.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 SCADA and HMI | Supervisory control and alarms | BP-01, BP-02, BP-03 |
| SYS-02 Gate control and standby generator | Gate PLC, local panels, hoists | BP-01 |
| SYS-03 Unit control | Unit PLCs, governors, exciters | BP-03 |
| SYS-04 Instrumentation and sirens | Data acquisition, gauges, sirens | BP-01, BP-02 |
| SYS-05 OT network and historian | Control LAN, OT firewall, DMZ replica, historian | BP-01 to BP-03, BP-05 |
| SYS-07, SYS-08, SYS-09 | Corporate network, identity provider, productivity suite | BP-06, BP-07, BP-09, BP-11 |
| SYS-11 Instrumentation SaaS | Trend analysis and AI anomaly module (shadow mode) | BP-02 |
| SYS-12 Business SaaS | ERP and maintenance, payroll, reservations | BP-08 to BP-11 |
| SYS-13 Offtaker RTU link | Telemetry and schedules | BP-05 |
| People | Operators (12, plus 3 supervisors), dam safety technicians, Controls Engineer and 2 I&C technicians, security officers | All |
| Third parties | SCADA integrator, governor vendor, instrumentation vendor, offtaker, county emergency management, sheriff | As listed in `bia.csv` |

**Backup and replication methods behind the RPOs:** historian replication to the DMZ and the cloud tenant (BP-01, BP-03); data logger local buffers and the instrumentation SaaS (BP-02); daily cloud backups of corporate servers and SaaS provider backups (BP-05 to BP-11); PLC and HMI configuration copies (irregular today; after every change once POAM-006 closes).

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Local manual control of gates and units | Immediate (15 minutes to staff panels during the day; 60 minutes at night) | Call-in list; radio |
| 2 | Gate PLC and SCADA supervisory control of gates (from verified logic) | 2 h | Local panels until verified |
| 3 | Instrumentation data acquisition and sirens | 4 h | Manual readings every 4 hours; local siren activation |
| 4 | Unit control through SCADA | 12 h | Local unit control |
| 5 | Security cameras and card access | 4 h | Extra patrols; posted officer |
| 6 | Offtaker RTU telemetry | 8 h | Phone schedules |
| 7 | Corporate email, identity provider access | 8 h | Personal phones; printed contacts |
| 8 | Historian replica, cloud reporting, instrumentation SaaS feed | 24 h | Local historian and data loggers |
| 9 | ERP, maintenance, field services | 48 h | Paper |
| 10 | Reservations; payroll | 24 h and 72 h | Walk-in; repeat prior payroll |

The order follows the process priorities in `bia.csv` (BP-01 to BP-11). Priority 1 is not a system: it is people at panels. Every OT recovery step in P08 starts by putting gates and units in local control and confirming their physical positions before any system is restored.
