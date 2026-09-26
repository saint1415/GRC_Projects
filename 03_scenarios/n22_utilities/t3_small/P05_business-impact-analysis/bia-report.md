# Business Impact Analysis: Cris Santos Company | Utilities | Small

**Organization:** Cris Santos Company, LLC (electric distribution utility) | **Tier:** Small (250 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** IT Manager with the Manager of System Operations, the Manager of Engineering and Protection, and the Customer Service Manager | **Approved:** President and CEO, 2026-09-04

## 1. Overview and purpose
This BIA identifies which business processes the company depends on, how long each can be down, and how much data it can lose. It supports:
- the SCADA cyber recovery procedure and backup DCC plan (P02 CP-2, CP-7);
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the OT incident response runbook (P08).

Keeping the lights on and keeping crews safe drive the values more than lost revenue does. The company's service restoration duties to its customers are the main downtime driver.

## 2. System and business description
The company delivers power to about 72,000 meters from 22 substations, with a 2025 peak of 410 MW. The 24x7 Distribution Control Center (DCC) runs the Distribution Operations Platform: SCADA, the OMS and GIS in the cloud tenant, the substation and field network, and the OT DMZ. Two substations hold low impact BES Cyber Systems (115 kV line protection relays). Customer processes run on vendor SaaS (CIS and AMI). See `../scenario-facts.md` sections 3 and 4.

## 3. Impact categories and values
Dollar values are scaled to $158 million in annual revenue, about $433,000 per day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $500,000 | $100,000 to $500,000 | Less than $100,000 |
| Operations | Outages cannot be restored or grow; loss of control of the grid | One process or area degraded; slower restoration | Staff slowed but working |
| Regulatory | NERC standard violation, missed DOE-417 or EOP-004 report, or reportable customer data breach | Late documentation or missed internal deadline | Internal policy deviation |
| Safety | Plausible injury to the public or line crews (for example, a line energized during a clearance) | Hazard controlled by manual procedures | None |
| Reputation | Regional media coverage; state regulator inquiry | Customer complaints; local attention | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Real-time distribution monitoring and control | High | 4 h | 2 h | 24 h |
| BP-02 Outage management and crew dispatch | High | 8 h | 4 h | 1 h |
| BP-03 BES line protection at Substation N and Substation E | High | 12 h | 8 h | 0 (last approved settings) |
| BP-04 Customer contact center, IVR, and portal | Moderate | 24 h | 8 h | 1 h |
| BP-05 Metering and AMI operations | Moderate | 72 h | 48 h | 24 h |
| BP-06 Wholesale power scheduling and load forecasting | Moderate | 24 h | 12 h | 24 h |
| BP-07 Internal communications and email | Moderate | 24 h | 8 h | 24 h |
| BP-08 Billing and payments | Moderate | 72 h | 48 h | 24 h |
| BP-09 Engineering, GIS, and work management | Low | 120 h | 72 h | 24 h |
| BP-10 Payroll and HR | Low | 120 h | 72 h | 24 h |

**What drives the values:**
- **Safety drives BP-01.** Without SCADA, every switching step needs a crew at the device. That is slower and riskier for crews working under clearances. The DCC can run on crews and radio for about 4 hours in normal weather.
- **Storms shorten BP-02.** In a hurricane, OMS outage prediction is the difference between hours and days of restoration. The MTD drops from 8 to 4 hours during declared storm events.
- **BP-03 keeps protecting even if IT fails.** The relays work locally, so loss of SCADA or remote access does not stop protection. The recovery case is **doubt about relay integrity** after a cyber event. Then the transmission owner may take the 115 kV line out of service until protection staff reload approved settings and test (about 8 hours).
- **Cost drives BP-06.** A missed or bad day-ahead schedule on a peak day can cost more than $500,000 in wholesale charges (P10).

**Key finding:** the 2-hour RTO for SCADA is **unproven**. Backups sit on the standby server in the same OT network and have never been restored. Failover to the backup DCC was last tested in 2023 (P01 R-006, R-014). If ransomware reached both SCADA servers, a rebuild from vendor media would take an estimated 2 to 3 days, far past the 4-hour MTD. Crews would run the grid by hand for that whole time.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 SCADA (primary at the DCC, standby at the backup DCC) | Monitoring and control; nightly database backup to the standby server | BP-01, BP-02 |
| SYS-03 Substation and field network | Fiber to 9 substations; licensed radio and private cellular to 13 | BP-01, BP-02 |
| SYS-04 Relays and gateways at Substation N and E | 115 kV line protection; approved settings files on the engineering server | BP-03 |
| SYS-12 OT DMZ | Integration server, jump host, historian replica | BP-01, BP-02 |
| SYS-02 OMS and GIS in SYS-09 | Cloud virtual machines and managed database with point-in-time restore; daily backups to a separate backup account | BP-02, BP-09 |
| SYS-11 Truck tablets | OMS mobile over commercial cellular | BP-02 |
| SYS-05 AMI head-end (SaaS) | Outage events and meter operations | BP-02, BP-05 |
| SYS-06 CIS (SaaS) | Customer records, IVR, portal, billing | BP-02, BP-04, BP-08 |
| SYS-13 Load-forecasting model | Day-ahead forecast in the analytics workspace | BP-06 |
| SYS-07 and SYS-08 | Identity provider and productivity suite | BP-07 and all SaaS access |
| People | 12 system operators on rotation, the SCADA/OT Administrator (single point of knowledge, P01 R-029), protection staff, crews, call center | All |
| Facilities | DCC at headquarters; backup DCC at the North operations center | BP-01, BP-02 |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Crews at key substations and radio dispatch (manual operation) | 1 h | Storm restoration plan staffing lists |
| 2 | SYS-01 SCADA on a clean server (standby or rebuilt) at the DCC or backup DCC | 2 h target (unproven) | Offline, immutable backups and a spare server (to be created, POAM-005) |
| 3 | SYS-03 substation communications, verified clean | 2 h | Isolate substations; local control by crews |
| 4 | SYS-02 OMS and its SCADA and AMI feeds | 4 h | Paper trouble tickets and radio dispatch |
| 5 | SYS-04 relay integrity check at Substation N and E | 8 h | Transmission owner keeps the line out of service until settings are verified |
| 6 | SYS-06 CIS, IVR, and portal (vendor-hosted) | 8 h | Recorded outage message; manual call logs |
| 7 | SYS-08 email and chat | 8 h | Phones, text messages, and radio |
| 8 | SYS-13 load forecast and the wholesale schedule | 12 h | Reuse the prior day's schedule |
| 9 | SYS-05 AMI operations | 48 h | Field connects and estimated reads |
| 10 | Billing, engineering, payroll | 48 to 72 h | Delay cycles; repeat payroll |
