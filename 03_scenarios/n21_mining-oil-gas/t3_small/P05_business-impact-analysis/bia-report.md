# Business Impact Analysis: Cris Santos Company | Mining, Quarrying, and Oil and Gas Extraction | Small

**Organization:** Cris Santos Company, LLC (independent crude oil producer) | **Tier:** Small (250 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, with the OT availability considerations of NIST SP 800-82 Rev. 3 (sections 3.3.9 and 5.3.2)
**Prepared by:** IT Manager with the SCADA and Automation Supervisor, both Field Superintendents, and the Production Accounting Manager | **Approved:** CFO and VP Operations, 2026-08-31

## 1. Overview and purpose
This BIA identifies which business processes the company depends on, how long each can be down, and how much data it can lose. It supports:
- the contingency and recovery planning that the benchmark calls for (CSF 2.0 RC.RP; SP 800-82 Rev. 3 section 3.3.9);
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08).

For an oil producer, "downtime" has two layers. The SCADA system can be down while the wells keep running, because field controllers work locally and the safety shutdowns are hardwired. The real limit is how long people can run the fields by hand before wells must be shut in. The values below reflect that.

## 2. System and business description
The company operates 118 wells and 8 facilities in two Florida operating areas, producing about 1,600 barrels of oil per day and reinjecting or disposing of about 55,000 barrels of produced water per day. Field controllers (RTUs, PLCs, drives, flow meters) report over radio and cellular links to the SCADA servers at the 24x7 Operations Control Center (OCC). Lease operators record tank gauges and run tickets on rugged tablets. Daily volumes flow through the cloud tenant to the production accounting SaaS, which pays about 2,300 royalty owners each month. See `../scenario-facts.md` sections 1-4.

## 3. Impact categories and values
Dollar values are scaled to about $42 million in annual revenue and about $104,000 of oil sales per day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $300,000 (about 3 days of oil sales) | $75,000 to $300,000 | Less than $75,000 |
| Operations | Both operating areas shut in, or the water system stops | One operating area or one facility stops | Staff slowed but production continues |
| Regulatory | Reportable discharge, permit violation, or breach notice to regulators | Late state production report or missed internal deadline | Internal policy deviation |
| Safety and environment | Plausible injury, H2S exposure, or oil or produced water release | Degraded safety monitoring with compensating patrols | None |
| Reputation | Regional media, loss of purchaser or partner confidence, or royalty owner complaints to regulators | Owner or partner complaints | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Emergency alarm call-out and HSE reporting | High | 4 h | 2 h | 24 h |
| BP-02 Produced water injection and disposal | High | 8 h | 4 h | 24 h |
| BP-03 Well monitoring and remote control | High | 24 h | 12 h | 24 h |
| BP-04 Crude oil custody transfer and hauling | High | 72 h | 24 h | 4 h |
| BP-05 Associated gas compression and sales | Moderate | 24 h | 12 h | 24 h |
| BP-06 Production accounting and revenue distribution | Moderate | 120 h | 72 h | 24 h |
| BP-07 Well servicing and maintenance dispatch | Moderate | 72 h | 48 h | 24 h |
| BP-08 Payroll and HR | Low | 120 h | 72 h | 24 h |
| BP-09 Finance, payables, and crude sales settlement | Low | 120 h | 72 h | 24 h |
| BP-10 Reservoir and geoscience analysis | Low | 240 h | 120 h | 24 h |

**What drives the values:**
- Safety drives BP-01. The H2S monitors and tank high-level switches shut sites in locally, but the SCADA call-out is how people learn about it. Roving patrols can stand in for about 4 hours before crews are exhausted.
- Water drives BP-02, not oil. Storage fills in about 8 hours at full rate, and then every producing well must be shut in.
- For SCADA-based processes (BP-01, BP-02, BP-03, BP-05), the RPO is the age of the last good copy of the SCADA configuration and controller programs. Process data from an outage period cannot be recovered and is rebuilt from paper logs.
- BP-04 has the only short RPO (4 hours), because run tickets are the basis for sales and royalty payments. The tablet app caches entries offline, and paper run tickets are the fallback.

**Key findings:**
1. **The SCADA recovery point is unproven.** SCADA servers are backed up nightly to a storage device in the same room, and PLC and RTU programs are not backed up centrally (gap 6 in `../scenario-facts.md`). A ransomware event that reaches the OCC could destroy both the servers and the backups, leaving no copy to meet the 24-hour RPO for BP-01 to BP-03 (P01 R-003).
2. **The 12-hour RTO for BP-03 has never been tested.** No restore of a SCADA server has been attempted. The SCADA integrator estimates 2 to 3 days to rebuild from installation media without a good backup.
3. **The OCC is a single point of failure.** Primary and standby SCADA servers share one room at the Panhandle field office, which sits in a hurricane evacuation zone (P01 R-014).
4. **The production accounting vendor's commitments meet BP-06.** Its SOC 2 report (P09) states an RTO of 24 hours and an RPO of 1 hour, inside the 72-hour and 24-hour targets.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 SCADA servers, historian, HMIs | Primary and standby servers and historian at the OCC; 6 HMIs | BP-01, BP-02, BP-03, BP-05 |
| SYS-02 Field devices and communications | 96 RTUs and PLCs, 22 ESP drives, 40 flow meters, 900 MHz radio, 46 cellular modems | BP-01, BP-02, BP-03, BP-05 |
| SYS-08 Corporate and SCADA networks | Office firewalls, IT/OT firewall, VPN to the cloud tenant | All |
| SYS-05 Identity provider | Single sign-on and MFA for SaaS and cloud | BP-04, BP-06 to BP-10 |
| SYS-04 Cloud tenant | Field data capture app, volume integration service, historian replica, data platform, ML workspace, backup vault | BP-04, BP-06, BP-07, BP-10 |
| SYS-09 Rugged tablets | 70 tablets used by lease operators | BP-04 |
| SYS-03 Production accounting SaaS | Allocations, royalties, joint interest billing | BP-04, BP-06 |
| SYS-06 ERP SaaS | Work orders, payables | BP-07, BP-09 |
| SYS-10 HR and payroll SaaS | Payroll | BP-08 |
| Third parties | SCADA integrator, cellular carrier, electric utility, crude purchaser and carrier, gas gathering company, production accounting vendor | As listed in `bia.csv` |
| People and facilities | Production Controllers and the OCC, lease operators, injection plant operators, automation technicians, HSE on-call | BP-01 to BP-05 |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Field safety call-out (HSE on-call phone tree, roving patrols) | Immediate | Printed HSE on-call binder at each field office |
| 2 | Injection plant and SWD controllers (local PLC panels) | 4 h | Local operation by plant operators; controllers are isolated from SCADA if SCADA is compromised |
| 3 | SCADA servers and OCC HMIs from a clean, verified backup | 12 h (target; untested today) | Manual operations; shut-in order set by the Field Superintendents |
| 4 | Field communications (radio and cellular modems) | 12 h | Manual operations |
| 5 | Compression station controllers | 12 h | Local panel operation; curtail high gas-oil-ratio wells |
| 6 | Identity provider and break-glass accounts | 4 h | Two break-glass administrator accounts (to be created; see P06 POL-02 4.8) |
| 7 | Field data capture app and tablets | 24 h | Paper run tickets |
| 8 | Volume integration service and production accounting | 72 h | Rebuild volumes from run tickets and meter data |
| 9 | ERP, payroll, finance | 72 h | Whiteboard dispatch; repeat prior payroll |
| 10 | Data platform and ML workspace | 120 h | Defer analysis |

Recovery priority 3 depends on a backup that is isolated from the OCC and has been restore-tested. Until POAM-003 and POAM-004 (P07) close, the company cannot rely on meeting it.
