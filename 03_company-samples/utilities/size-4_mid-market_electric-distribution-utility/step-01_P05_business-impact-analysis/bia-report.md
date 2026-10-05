# Business Impact Analysis: Cris Santos Company | Utilities | Mid-Market

**Organization:** Cris Santos Company, Inc. (investor-owned electric distribution utility, NERC-registered Distribution Provider, with a Utility Services line for 4 client utilities) | **Tier:** Mid-Market (850 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Information Security Manager and the GRC analyst, with the vCISO and the process owners named in `bia.csv` | **Fieldwork:** 2026-07-06 to 2026-07-31 | **Approved:** Chief Operating Officer (CIP Senior Manager), 2026-09-17 (presented to the board audit committee the same day)

## 1. Overview and purpose
This BIA covers every business unit: System Operations, Engineering and Protection, OT Engineering, Field Operations, Customer Operations, Utility Services, Power Supply and Rates, and enterprise support functions. It rates 16 business processes and quantifies what an outage costs in money, operations, regulatory exposure, public and crew safety, and reputation.

Keeping the lights on and keeping crews safe drive the values more than lost revenue does. Retail revenue is not lost during most outages (customers are billed later), so the money values below are mostly extra labor, wholesale imbalance charges, contract credits, and delayed cash.

The results feed:
- the SCADA cyber recovery procedure and backup DCC plan, and the low impact Cyber Security Incident response plan (CIP-003-9 Attachment 1 Section 4) for the relays at Substations N, E, L, and H;
- the FIPS 199 availability rating and contingency controls in the SSP for the Distribution Operations Platform (P02);
- impact ratings and exposure estimates in the risk register (P01);
- the recovery order in both incident runbooks (P08);
- the Availability and Processing Integrity criteria in the SOC 2 readiness assessment for the Utility Services system (P09);
- the EOP-004-4 event reporting Operating Plan and the Form DOE-417 thresholds used in P08.

## 2. System and business description
The company delivers power to about 265,000 meters from 74 substations, with a 2025 summer peak of 1,480 MW, and provides billing, CIS hosting, after-hours outage calls, and meter data management to 4 client utilities (about 58,000 meters). The 24x7 Distribution Control Center (DCC) at headquarters, with a backup DCC at the West Operations Center, runs the Distribution Operations Platform (DOP) described in the SSP (P02): SCADA, the OMS and GIS in the operations workloads account of the cloud landing zone, the substation and field network, the OT DMZ, 310 truck tablets, the ADMS FLISR pilot, and the low impact BES Cyber Systems (26 BES line protection relays) at Substations N, E, L, and H. Customer and Utility Services processes run on vendor SaaS (CIS, AMI head-end, contact center platform). See `../00_company-facts.md` sections 1, 3, and 7.

## 3. Impact categories and values
Dollar values are scaled to about $610 million in annual revenue: about $1.63 million of retail billing a day and about $1.17 million of Utility Services fees a month. Wholesale imbalance charges for a missed or poor day-ahead schedule run about $150,000 on a normal day and up to $1.2 million on a peak day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost (per day of outage) | More than $250,000 of direct cost, or more than $2 million of cash delayed | $50,000 to $250,000 | Less than $50,000 |
| Operations | Outages cannot be restored or grow; loss of remote control of the grid; a whole business unit stops | One process, area, or client degraded; restoration measurably slower | Staff slowed but working |
| Regulatory | Potential violation of a NERC Reliability Standard, a missed DOE-417 or EOP-004 report, or a reportable customer data breach | Late documentation, a missed contract service level, or a missed internal deadline | Internal policy deviation |
| Public and crew safety | Plausible injury to the public or crews (for example, a line energized during a clearance, or a protection misoperation) | Hazard controlled by manual procedures | None |
| Reputation | Regional media coverage, a state regulator inquiry, or loss of a Utility Services client | Customer or client complaints; local attention | Internal only |

**How loss at MTD was estimated.** Estimated loss is extra labor, overtime, contractor and truck costs, contract credits, and wholesale charges over the MTD, as estimated by each process owner. Delayed billing is cash, not lost revenue, so it is shown separately (BP-07). Safety and reliability consequences are described, not priced.

## 4. Process criticality and downtime (from `bia.csv`)
| Priority | Process | Unit | Criticality | MTD (h) | RTO (h) | RPO (h) | Estimated loss at MTD |
|---|---|---|---|---|---|---|---|
| 1 | BP-01 Real-time distribution monitoring and control | System Operations | High | 4 | 2 | 1 | $120,000 |
| 2 | BP-04 Switching orders and clearance management | System Operations | High | 4 | 2 | 0.25 | $30,000 |
| 3 | BP-02 Outage management and crew dispatch | System Operations | High | 8 | 4 | 1 | $150,000 |
| 4 | BP-03 BES line protection at Substations N, E, L, and H | Engineering and Protection | High | 12 | 8 | 0 | $60,000 |
| 5 | BP-05 Customer contact center, IVR, and portal | Customer Operations | Moderate | 24 | 8 | 1 | $90,000 |
| 6 | BP-11 Field work management and mobile workforce | Field Operations | Moderate | 24 | 12 | 4 | $80,000 |
| 7 | BP-09 Wholesale power scheduling and load forecasting | Power Supply and Rates | Moderate | 24 | 12 | 24 | $300,000 |
| 8 | BP-13 ADMS FLISR pilot operations | OT Engineering | Low | 24 | 12 | 1 | $10,000 |
| 9 | BP-14 Internal communications and collaboration | Enterprise | Moderate | 24 | 8 | 24 | $50,000 |
| 10 | BP-08 Contract services for the 4 client utilities | Utility Services | Moderate | 48 | 24 | 1 | $200,000 |
| 11 | BP-07 Billing and payment processing | Customer Operations | Moderate | 72 | 48 | 24 | $40,000 (plus about $4.9 million cash delayed) |
| 12 | BP-06 Metering and AMI operations | Customer Operations | Moderate | 72 | 48 | 24 | $160,000 |
| 13 | BP-10 New accounts, credit, and deposits | Customer Operations | Moderate | 72 | 24 | 24 | $25,000 |
| 14 | BP-12 Engineering, GIS, and design | Engineering and Protection | Low | 120 | 72 | 24 | $40,000 |
| 15 | BP-15 Payroll and HR | Enterprise | Low | 120 | 72 | 24 | $30,000 |
| 16 | BP-16 Finance, procurement, and accounts payable | Enterprise | Low | 120 | 72 | 24 | $20,000 |

**Summary:** 4 High, 8 Moderate, and 4 Low processes (16 in total). The sum of estimated losses at each process's MTD is $1,405,000. The recovery priority follows safety and reliability first, then customer contact, then money; that is why BP-13 (Low) sits above several Moderate processes: its RTO is short because the 40 pilot feeders must be returned to manual restoration through SCADA quickly.

**Enterprise-wide scenario.** If corporate IT, the OMS, and the CIS export area were unavailable for 72 hours (for example, ransomware on corporate IT, the second P08 incident type), the estimated direct cost is about $1.0 million: field productivity and overtime (about $240,000), truck visits for remote connects and disconnects (about $120,000), Utility Services contract credits (up to about $232,000 if all 4 clients miss both service levels), storm call vendor overflow and contact center overtime (about $150,000), and at least one wholesale schedule built by hand (about $150,000 on a normal day, more on a peak day). About $4.9 million of billing would be delayed. Incident response, legal, and breach notification costs come on top (P01 R-002 and R-003). If SCADA were also lost (the first P08 incident type), restoration of every feeder lockout would depend on crews at the device, and the safety exposure would outweigh every money value in this table.

**What drives the values:**
- **Crew and public safety drive BP-01, BP-03, and BP-04.** Without SCADA every switching step needs a crew at the device. The DCC can run on crews and radio for about 4 hours in normal weather and about 2 hours during a declared storm. Lost or wrong clearance status (BP-04) can energize a line where a crew is working.
- **Storms shorten BP-02.** In a hurricane, OMS outage prediction is the difference between hours and days of restoration for the last customers. The MTD drops from 8 to 4 hours during declared storm events.
- **BP-03 keeps protecting even if IT fails.** The relays work locally. The recovery case is doubt about relay integrity after a cyber event, when a transmission owner may take a 230 kV or 115 kV line out of service until approved settings are reloaded and tested (about 8 hours per substation).
- **Contracts drive BP-08.** Client contracts set a 1-business-day billing service level and 99.5% monthly contact center availability, with a 5% monthly fee credit for each miss (about $58,000 per client per miss).
- **Cost drives BP-09.** A missed or poor day-ahead schedule on a peak day can cost up to $1.2 million (P10 AI-001).
- **Cash flow, not time, drives BP-07.** About $1.63 million of billing is delayed for each day of outage.

## 5. Key findings
1. **SCADA recovery is slower than the target (gap 7).** The 2025-11 restore test took 6 hours against a 2-hour RTO and a 4-hour MTD, and failover to the backup DCC was last tested in 2024-04. Hot standby replication protects against hardware failure, not against ransomware or a malicious change that replicates to both servers. The 2-hour RTO is a target, not a demonstrated capability (P01 R-007; P07 CP-4; POAM-007).
2. **The switching and clearance module needs a 2-hour RTO, but the OMS restore took 3 hours 10 minutes.** The 2026-05-19 OMS restore test met the OMS's own 4-hour RTO, but BP-04 depends on the same database. Paper switching orders cover the gap only until planned work stops after 4 hours (P01 R-016).
3. **Relay integrity is the recovery case for the BES assets.** Approved relay settings files are kept on the settings file server in the OT network, with a copy in the PRC-005 records. A clean, offline, hash-verified copy is needed so that settings can be trusted after a cyber event at Substation H or elsewhere (P01 R-005; P08 runbook A).
4. **The CIS vendor's recovery objectives do not meet the BIA.** The CIS vendor's SOC 2 system description states an RTO of 12 hours and an RPO of 1 hour. BP-05 needs 8 hours, and the Utility Services client contracts need billing within 1 business day. The client utilities' partitions are not covered by any availability test (gap 14; P01 R-021; P09 A1.3).
5. **The CIS export area concentrates customer data.** The nightly extract of about 410,000 customer records, including closed accounts and client utilities' customers, is not needed for any process in this BIA beyond reporting and the meter data warehouse. It enlarges the impact of the ransomware and data theft scenario without supporting recovery (gap 12; P01 R-003).
6. **Single points of knowledge.** The load-forecasting model depends on the Lead Load Forecasting Analyst (BP-09), and the OT Windows domain and SCADA database restore depend on 2 of the 4 SCADA and ADMS engineers (BP-01). Cross-training is part of POAM-007 and the P10 conditions.

## 6. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 Distribution SCADA | Master station (primary at the DCC, hot standby at the backup DCC), 14 HMI consoles, historian, 2 engineering workstations; continuous replication; weekly offline backups at the backup DCC | BP-01, BP-02, BP-04, BP-13 |
| SYS-02 OMS and GIS (operations workloads account of SYS-09) | Outage prediction, dispatch, switching and clearance module; managed database with point-in-time restore | BP-02, BP-04, BP-11, BP-12 |
| SYS-03 Substation automation and field network | Company fiber to 40 substations, licensed radio and private LTE to 34; about 1,900 field devices | BP-01, BP-02, BP-13 |
| SYS-04 Low impact BES Cyber Systems | 26 relays and the access control gateways at Substations N, E, L, and H; approved settings files | BP-03 |
| SYS-05 AMI head-end (SaaS) | Outage events, interval reads, remote connect and disconnect; separate tenant for client meters | BP-02, BP-06, BP-08 |
| SYS-06 CIS, billing, portal, IVR (SaaS) | Customer records, billing, payments, client partitions | BP-02, BP-05, BP-07, BP-08, BP-10 |
| SYS-07 Identity provider | Single sign-on and MFA for SaaS, cloud console, VPN, and OT jump hosts | All IT and SaaS access; vendor access to OT |
| SYS-08 Productivity suite and contact center platform | Email, files, chat; call routing and recording | BP-05, BP-08, BP-14 |
| SYS-09 Cloud landing zone | Operations workloads, analytics, backup, and log archive accounts | BP-02, BP-04, BP-08, BP-09, BP-11, BP-12 |
| SYS-10 Corporate network | Headquarters and 4 operations centers; 980 endpoints; VPN | All office work |
| SYS-11 Truck tablets | 310 rugged tablets over cellular | BP-02, BP-04, BP-11 |
| SYS-12 OT DMZ | 2 jump hosts, historian replica, OMS-SCADA integration server, file transfer, patch staging, sensor collector | BP-01, BP-02, BP-09 |
| SYS-13 Security monitoring (MSSP) | SIEM, EDR, OT network sensors at the DCC, backup DCC, and OT DMZ | Recovery validation |
| SYS-14 ADMS FLISR pilot | Automatic restoration on 40 feeders | BP-13 |
| SYS-15 Load-forecasting model (AI-001) | Day-ahead and 7-day forecasts in the analytics account | BP-09 |
| People | 28 system operators and 6 shift supervisors; 22 protection engineers and technicians; OT engineering team of 9; 330 field staff; 160 customer operations staff; 42 Utility Services staff | All |
| Facilities | DCC and primary data room at headquarters; backup DCC at the West Operations Center; 3 other operations centers with crew yards | BP-01, BP-02, BP-04 |
| Third parties | SCADA and ADMS vendor, cloud provider, CIS vendor, AMI vendor, contact center platform vendor, carriers, Transmission Owners A and B, wholesale supplier, payment processor, MSSP, storm call vendor | As listed in `bia.csv` |

## 7. Reliability, regulatory, and contract linkage
The BIA supplies the thresholds and recovery order that the reporting and planning duties need. Applicability of each duty is decided in P03; the notification steps are in the P08 matrix.

| Duty or commitment | What this BIA supplies | Status |
|---|---|---|
| CIP-003-9 R2, Attachment 1 Section 4 (low impact Cyber Security Incident response plan) | BP-03 recovery case: relay integrity check and approved settings reload, about 8 hours per substation | Plan update with the P08 runbook A, due 2026-11-30 |
| CIP-009 recovery plans | Not applicable today (low impact only). If the ADMS load-shedding module goes live as designed (gap 1), CIP-009 recovery plans would apply to it, and BP-13 would need a new row | Watch item for the 2026-12-10 board decision |
| NERC EOP-004-4 (Distribution Provider events) | An uncontrolled loss of 200 MW or more of firm load for 15 minutes or more resulting from a BES Emergency is reportable, as are damage to or physical threats against its Facilities; BP-01 and BP-02 workarounds keep the DCC able to see load loss | In the Operating Plan (reviewed 2026-01) |
| Form DOE-417 | Criterion 3 (cyber event that interrupts electrical system operations, 1 hour) for BP-01; criterion 12 (loss of service to more than 50,000 customers for 1 hour or more, 6 hours) for BP-02 | Added to the P08 matrix |
| Utility Services client contracts | BP-08 MTD and RTO; client notice of security incidents within 48 hours | Availability testing of client partitions is missing (finding 4) |
| Fla. Stat. 501.171 (as third-party agent for the clients) | BP-08 and the CIS export area identify which client customers' data is held | Notice to clients within 10 days of determination (P08 runbook B) |
| State public service commission storm and outage duties | BP-02 storm MTD of 4 hours | Outside this cyber analysis; not assessed |

## 8. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Crews at the 20 largest substations and radio dispatch from the DCC (manual operation) | 1 h | Storm restoration plan staffing lists; printed one-line diagrams |
| 2 | SYS-07 identity provider and break-glass accounts; OT domain break-glass accounts | 1 h | Two break-glass accounts per critical system, sealed and stored offline at the DCC and backup DCC |
| 3 | SYS-01 SCADA on a clean server (hot standby or rebuilt) at the DCC or backup DCC | 2 h target (6 h demonstrated) | Weekly offline backups; spare server at the backup DCC (POAM-007) |
| 4 | SYS-03 substation and field communications, verified clean | 2 h | Isolate substations; local control by crews |
| 5 | SYS-02 OMS switching and clearance module, then outage prediction and dispatch | 2 h (switching), 4 h (full) | Paper switching orders and clearance log; paper trouble tickets |
| 6 | SYS-12 OT DMZ (integration server and historian replica) | 4 h | Manual entry of breaker status into the OMS; vendor access stays disabled |
| 7 | SYS-04 relay integrity check at Substations N, E, L, and H | 8 h per substation | Transmission owner keeps the line out of service until settings are verified |
| 8 | SYS-06 CIS, IVR, and portal (vendor-hosted) | 8 h target (vendor states 12 h) | Recorded outage message; storm call vendor; manual call logs |
| 9 | SYS-08 email, chat, and contact center platform | 8 h | Phones, text messages, radio; printed contact lists |
| 10 | SYS-11 truck tablets and mobile back end | 12 h | Printed work packs and paper maps |
| 11 | SYS-15 load forecast and wholesale schedule | 12 h | Reuse the prior day's schedule adjusted for weather |
| 12 | SYS-14 ADMS FLISR pilot | 12 h | FLISR disabled; manual restoration through SCADA |
| 13 | SYS-13 SIEM and EDR consoles | 8 h (needed before reconnecting IT to OT) | MSSP works from its own platform |
| 14 | Utility Services client partitions in SYS-06 and SYS-05 | 24 h | Clients bill from estimates; after-hours calls roll to client duty officers |
| 15 | SYS-05 AMI operations | 48 h | Field connects and estimated reads |
| 16 | Billing, credit, engineering, payroll, finance | 24 to 72 h | Delay bill cycles; pending deposits; repeat prior payroll |
