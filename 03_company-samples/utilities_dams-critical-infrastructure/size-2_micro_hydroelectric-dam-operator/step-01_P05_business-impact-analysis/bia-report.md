# Business Impact Analysis: Cris Santos Company | Dams | Micro

**Organization:** Cris Santos Company, LLC (owner and operator of the fictional Bramble Shoals Hydroelectric Project) | **Tier:** Micro (7 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Plant Superintendent and Office and Compliance Administrator, with the Owner and General Manager, the Controls and Electrical Technician, and the MSP and controls integrator by phone, 2026-07-13 to 2026-07-24 | **Approved:** Owner and General Manager, 2026-08-31

## 1. Overview and purpose
This BIA lists every business function of the company, how long each can be down, and how much data each can lose. It supports:
- the OT recovery procedure the company is adopting from the FERC Security Program's Section 9 baseline measures ("plan and prepare for the restoration and recovery of control systems", Rev. 3A Table 9.3a). Section 9 is not mandatory for this Security Group 3 dam, but the company uses it as its benchmark (P03);
- the EAP, which must give operators instructions for a project emergency, including during hours of darkness (18 CFR 12.22(a)(1)(i), 12.22(b)). The plant is unattended at night, so the after-hours function (BP-04) matters;
- the availability ratings in the SSP (P02), the impact ratings in the risk register (P01), and the recovery order in the incident runbook (P08).

## 2. System and business description
One hydroelectric project on one site: a Significant hazard potential concrete dam with 2 motor-operated spillway gates, a 4.4 MW powerhouse with 2 units, a small set of dam safety instruments, and a tailrace warning horn, all run by the Hydro Plant Control and Dam Monitoring System (HPCDMS, P02). Seven people run everything. Office IT is handled by an MSP; the control system is supported by an outside controls integrator; alarms reach the on-call operator through a SaaS monitoring service. See `../00_company-facts.md` sections 1 and 3.

**What is different about a dam.** For most processes the question is how long until the company loses money. For BP-01 and BP-02 the question is how long until someone at the tailrace or downstream could be hurt. The company can always fall back to **local manual control**: a person at the gate panels in the hoist house, a person at the unit panels, and manual instrument readings. The MTDs below measure how long 7 people can keep those workarounds going safely. The dam is never left uncontrolled.

## 3. Impact categories and values
Dollar values are scaled to about $1.1 million in annual revenue (about $3,000 a day). Generation alone is about $2,750 a day at average output.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $15,000 (about 5 days of generation) | $3,000 to $15,000 | Less than $3,000 |
| Operations | Gates or units cannot be controlled even locally, or staff cannot reach the site | One process runs only on manual workarounds | Staff slowed but working |
| Regulatory | Condition reportable under 18 CFR 12.10, EAP activation, or a FERC directive | Missed license or contract deadline | Internal policy deviation |
| Safety | Plausible harm to recreation users or people downstream (sudden release, missed warning) | Worker exposure during manual operation | None |
| Reputation | Regional media coverage; loss of the cooperative's or the county's confidence | Complaints from recreation users or neighbors | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Headpond and spillway gate operations | High | 8 h | 4 h | 24 h |
| BP-02 Dam safety monitoring, public warning, and EAP notification | High | 12 h | 8 h | 1 h |
| BP-03 Power generation and unit control | High | 72 h | 24 h | 24 h |
| BP-04 After-hours monitoring, alarm callout, and remote response | Moderate | 12 h | 8 h | 1 h |
| BP-05 Physical security and recreation area safety | Moderate | 24 h | 12 h | 24 h |
| BP-06 FERC and license compliance | Moderate | 72 h | 48 h | 24 h |
| BP-07 Offtaker coordination and energy settlement | Low | 120 h | 72 h | 24 h |
| BP-08 Office administration, email, accounting, and payroll | Low | 120 h | 72 h | 24 h |

Totals: 3 High, 3 Moderate, 2 Low.

**What drives the values:**
- **BP-01 (MTD 8 hours).** Local gate control needs one person at the hoist house panels at all times. With 7 staff, the company can cover that around the clock for about 8 hours before fatigue and coverage become unsafe, and sooner in a flood. After that, PLC and HMI control must be back.
- **BP-02 (RPO 1 hour).** The data logger keeps 60 days of readings, so readings are rarely lost. The 1-hour RPO is the gap tolerated in the trend record. Manual readings must start within 12 hours.
- **BP-03.** Revenue drives the value, not safety. Units can run in local control while staff are on site.
- **BP-04.** One unanswered night is the limit. After that, someone must stay in the control room overnight, which this staff cannot sustain for long.

## 5. Resource requirements and vendor dependencies
| Resource | Description | Recovery method behind the RPO | Supports |
|---|---|---|---|
| SYS-01 HMI PC and engineering laptop | Supervisory control and alarms; PLC programming | **No company copy of the HMI project.** Integrator copy dated 2023-05-18, never restore-tested | BP-01, BP-03, BP-04 |
| SYS-02 Gate PLC, local panels, standby generator | Gate control and automatic level control | **No company copy of the gate PLC logic** (integrator copy 2023-05-18) | BP-01 |
| SYS-03 Unit PLCs, governors, exciters | Unit control | Integrator copy of PLC logic (2023-05-18); **governor and exciter settings never copied** | BP-03 |
| SYS-04 Instruments, data logger, tailrace horn | Readings and public warning | Data logger keeps 60 days; readings also stored in SYS-07 | BP-02 |
| SYS-05 Control network, firewall, cellular gateway | Links the HMI, PLCs, and data logger | Firewall configuration held by the integrator | BP-01 to BP-04 |
| SYS-06 Remote access paths | Remote desktop tool; integrator cellular VPN | Not needed for recovery; disabled during incidents (P08) | BP-04 |
| SYS-07 Remote monitoring and alarm service (SaaS) | Callouts and trends | Vendor backups (SOC 2: RPO 15 minutes) | BP-02, BP-04 |
| SYS-08, SYS-09, SYS-10, SYS-11 | Office IT, productivity suite, cloud backup, accounting and payroll | Nightly cloud backup of the suite, 30 days of versions | BP-06, BP-07, BP-08 |
| SYS-12 Cameras and locks | Physical security | NVR keeps about 14 days of video | BP-05 |
| People | 7 staff; only 3 operator-mechanics rotate on call | Cross-training: the Controls and Electrical Technician and the Plant Superintendent can operate gates and units | All |

**Vendor dependencies:**
| Vendor | Functions that stop without it | Commitment today | Evidence of recovery capability |
|---|---|---|---|
| Controls integrator | Rebuild of the HMI PC and reload of PLC logic (BP-01, BP-03) | Time-and-materials agreement; "next business day, best effort"; no recovery time | None. Its copies are 3 years old and never tested |
| Remote monitoring service vendor | Alarm callouts and trends (BP-02, BP-04) | Subscription terms | SOC 2 Type 2 (P09): RTO 12 hours, RPO 15 minutes |
| MSP | Office IT and suite recovery (BP-06, BP-08) | 4-business-hour response | One single-file restore test in 2025 |
| Cellular carrier (one carrier) | Monitoring gateway, integrator router, staff phones at the dam (BP-02, BP-04) | Standard business service | None; coverage at the dam is weak |
| Standby generator fuel supplier | Gate operation during a power outage (BP-01) | Delivery on request | Annual load test (18 CFR 12.54(c)) |
| Cooperative | Meter reads and settlement (BP-07) | Power purchase agreement | Reads its own meter |

**Key findings:**
1. **The 4-hour RTO for gate control is unproven.** Recovery of the HMI PC and gate PLC depends entirely on the integrator, whose copies are from May 2023 and have never been restored. The HMI PC runs an unsupported operating system and there is no spare (P01 R-005; P07 POAM-008).
2. **The monitoring service's RTO (12 hours) is longer than the BIA's 8 hours for BP-04.** That is acceptable only because an operator-mechanic can stay in the control room overnight. It is recorded as a known dependency (P09).
3. **One cellular carrier carries the monitoring gateway, the integrator's router, and staff phones at the dam.** A carrier outage at night removes callouts (P01 R-014).
4. **People are the real limit.** Every manual workaround needs one of 7 people on site. The MTDs assume nobody is sick or on leave.

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Local manual control of gates and units (people at the panels) | 30 minutes at night; 10 minutes by day | Call-in list on the printed EAP contact sheet |
| 2 | Gate PLC and HMI supervisory control of gates, from a verified copy | 4 h (target; unproven today) | Local panels until verified |
| 3 | Data logger readings, tailrace horn | 8 h | Manual readings every 12 hours; manual horn switch |
| 4 | Remote monitoring and alarm callouts | 8 h | Operator-mechanic stays overnight |
| 5 | Unit control through the HMI | 24 h | Local unit panels while staffed |
| 6 | Cameras and NVR | 12 h | Extra walk-downs; sheriff patrols |
| 7 | Email and suite files; payroll | 72 h | Phones; payroll service repeats the prior run |
| 8 | Accounting and settlement | 72 h | Cooperative's meter statement |
| Last | Remote access (remote desktop tool, integrator VPN) | Only after P08 section 7 checks | Staff on site |

The order follows the recovery priorities in `bia.csv` (BP-01 first). Priority 1 is not a system: it is people at panels. Every OT recovery step in P08 starts by putting gates and units in local control and confirming their positions by eye before any system is restored.
