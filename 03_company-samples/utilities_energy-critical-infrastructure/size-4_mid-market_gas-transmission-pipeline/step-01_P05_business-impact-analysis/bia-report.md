# Business Impact Analysis: Cris Santos Company | Energy | Mid-Market

**Organization:** Cris Santos Company, Inc. (interstate natural gas transmission pipeline operator) | **Tier:** Mid-Market (600 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** GRC lead with the vCISO, the process owners named in `bia.csv`, and the Director of Gas Control | **Fieldwork:** 2026-07-06 to 2026-07-31 | **Approved:** Chief Operating Officer, 2026-09-17 (presented to the audit committee the same day)

## 1. Overview and purpose
This BIA covers every business unit: Gas Control, Field Operations (including the 5 compressor stations), Pipeline Safety and Compliance, Commercial, Regulatory Affairs, Engineering, Integrity, and Measurement, Finance, Corporate Services, and Cybersecurity. It rates 15 business processes and quantifies what an outage costs in money, operations, regulatory exposure, and public safety.

The results feed:
- the definition of **business critical functions** and the identification of **Critical Cyber Systems** in the TSA-approved Cybersecurity Implementation Plan (SD Pipeline-2021-02G Sections III.A and VII.B and VII.C);
- the measures in the Cybersecurity Incident Response Plan to reduce the risk of operational disruption (SD 02G Section III.F);
- the manual operation and backup SCADA duties in 49 CFR 192.631(c)(3) and (c)(4), and the emergency plan in 192.615;
- the FIPS 199 availability and integrity ratings in the SSP (P02);
- impact ratings and exposure estimates in the risk register (P01);
- the recovery order and the operate-or-shut-down criteria in both incident runbooks (P08);
- the Availability and Processing Integrity criteria in the SOC 2 readiness assessment (P09).

## 2. System and business description
The company moves about 1.0 million dekatherms of natural gas a day through about 780 miles of interstate transmission pipeline from 4 receipt interconnects in southern Alabama and southwest Georgia to 46 delivery points in north and central Florida. Its shippers are 9 local distribution companies (LDCs) serving about 1.3 million homes and businesses, 7 gas-fired power plants, 22 industrial customers, and 6 marketers. The Gas Control Center (GCC) at headquarters runs the pipeline 24x7 through the Pipeline SCADA and Gas Control System (PSGCS). The Backup Control Center (BCC) at Compressor Station 3 is a hot standby. The GCC also operates two third-party laterals under operations services agreements (OSAs). Business IT, the 5-account cloud landing zone, and SaaS services sit behind IT/OT DMZs at the GCC and BCC (see `../00_company-facts.md` sections 3, 4, and 7).

## 3. Impact categories and values
Dollar values are scaled to about $100 million in annual revenue. Firm reservation revenue is about $252,000 per day. Under the tariff, an outage that is not force majeure can require reservation charge credits to affected shippers, and a force majeure outage can require partial credits.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost (per day of outage) | More than $500,000 (about 2 days of reservation revenue), including reservation charge credits, OSA service credits, and response costs | $100,000 to $500,000 | Less than $100,000 |
| Operations | Firm deliveries to an LDC or a power plant are curtailed, or a lateral under an OSA is unmonitored | Deliveries continue with manual operation, reduced pressure, or estimated data | Staff slowed but working |
| Regulatory | Reportable incident under 49 CFR Part 191; a TSA directive violation; a missed FERC posting duty during a service outage | A missed record or interval (for example a 15-month interval under 192.631) | Internal procedure deviation |
| Public safety | Plausible harm to the public or workers (overpressure, an undetected release, loss of gas supply to homes in cold weather) | Degraded monitoring with compensating field coverage | None |
| Reputation | National or regional media coverage; a shipper or lateral owner ends its contract; state utility commissions question supply reliability | Shipper complaints; escalation by an interconnecting pipeline | Internal only |

**How loss at MTD was estimated.** Estimated loss is unrecovered revenue, credits, and extra labor, over the process's MTD. Process owners supplied the assumptions: about 180 field staff on overtime for each 8-hour shift of manual operation; partial reservation charge credits on curtailed firm service; OSA service credits after 4 hours; and imbalance and scheduling costs for missed nomination cycles. Delayed cash from billing is shown separately.

## 4. Process criticality and downtime (from `bia.csv`)
| Priority | Process | Unit | Criticality | MTD (h) | RTO (h) | RPO (h) | Estimated loss at MTD |
|---|---|---|---|---|---|---|---|
| 1 | BP-03 Emergency response and public safety communication | Pipeline Safety and Compliance | High | 1 | 0.25 | 0 | $25,000 |
| 2 | BP-01 Gas control (SCADA monitoring and control) | Gas Control | High | 8 | 1 | 0.25 | $150,000 |
| 3 | BP-04 Contract operation of two third-party laterals | Gas Control | High | 8 | 1 | 0.25 | $15,000 |
| 4 | BP-02 Compressor station operation | Field Operations | High | 12 | 4 | 24 | $120,000 |
| 5 | BP-13 Cybersecurity monitoring, incident response, and TSA coordination | Cybersecurity | Moderate | 12 | 4 | 1 | $10,000 |
| 6 | BP-05 Nominations, scheduling, and confirmations | Commercial | High | 12 | 4 | 1 | $80,000 |
| 7 | BP-08 Informational Postings, critical notices, and capacity release | Regulatory Affairs | Moderate | 24 | 12 | 4 | $15,000 |
| 8 | BP-12 Physical security monitoring | Field Operations | Moderate | 24 | 8 | 24 | $10,000 |
| 9 | BP-11 Engineering, GIS, and emergency maps | Engineering, Integrity, and Measurement | Moderate | 48 | 24 | 24 | $10,000 |
| 10 | BP-10 Field O&M, integrity management, and compliance records | Field Operations | Moderate | 72 | 48 | 24 | $40,000 |
| 11 | BP-07 Leak detection analytics (advisory) | Gas Control | Moderate | 72 | 24 | 24 | $5,000 |
| 12 | BP-06 Gas measurement and custody transfer data | Engineering, Integrity, and Measurement | Moderate | 72 | 48 | 24 | $20,000 |
| 13 | BP-09 Gas accounting, imbalances, and invoicing | Finance | Low | 120 | 72 | 24 | $30,000 (plus about $8.3 million of monthly billing delayed) |
| 14 | BP-15 Payroll, HR, and finance | Corporate Services | Low | 120 | 72 | 24 | $20,000 |
| 15 | BP-14 Supply chain, warehouse, and spare parts | Corporate Services | Low | 120 | 72 | 24 | $10,000 |

**Summary:** 5 High, 7 Moderate, and 3 Low processes (15 in total). The sum of estimated losses at each process's MTD is $560,000.

**Enterprise-wide scenario: a 5-day precautionary shutdown.** If leadership shut the pipeline down for 5 days because it could not trust OT (the scenario in P08 runbook 1), the direct cost would be about:
- reservation charge credits of up to $1.26 million (5 days at about $252,000), depending on whether the outage is force majeure under the tariff (a question for the General Counsel);
- OSA service credits of about $40,000;
- incident response, overtime, and restart costs of about $1.5 million.

The larger harm falls on others. Nine LDCs would draw on storage and line pack and might curtail interruptible customers, and 7 power plants would switch fuel or reduce output. In winter, a multi-day loss of supply to homes is a public safety event in its own right. **A shutdown is never free and never the safe default.** It must be chosen against the criteria in P08.

**What drives the values:**
- **Public safety drives BP-01, BP-02, BP-03, and BP-04.** Controllers must see pressures and alarms to detect a rupture and act. The 8-hour MTD for gas control is how long field crews can hold the line safely in manual operation. After that, the company would reduce pressure and curtail deliveries. Emergency communication cannot pause, because 49 CFR 191.5 requires notice to the National Response Center no later than one hour after confirmed discovery of an incident.
- **Customer supply drives BP-05 and BP-08.** Nominations run on the NAESB cycles of each gas day, and FERC requires the company to post all planned and actual service outages or reductions in service capacity (18 CFR 284.13(d)(1)). Shippers need those notices before any curtailment.
- **Contract terms drive BP-04.** Each OSA requires notice to the lateral owner within 30 minutes of losing SCADA monitoring of its lateral.
- **TSA duties drive BP-13.** The Cybersecurity Coordinator must be reachable 24x7 and incidents must be reported to CISA within 72 hours (SD 01G Sections II.B and II.C).
- **Billing is not time-critical.** BP-09 can stop for 5 days. Measurement data is safe in the flow computers for about 35 days.

## 5. Key findings
1. **A business IT outage alone does not justify shutting down the pipeline.** Gas control, compressor operation, and emergency communication run without any business IT system. The customer activities website (BP-05, BP-08) is vendor SaaS and keeps working if on-premises business IT is lost, as long as the identity provider is not compromised. A precautionary shutdown is justified only when the company cannot confirm that OT is isolated and trustworthy, or cannot staff safe manual operation (P08). The 2025 tabletop showed executives defaulting to shutdown (gap 7).
2. **The Backup Control Center supports the 1-hour RTO for gas control, but only if it is clean.** Failover was tested on 2025-11-04. If an attacker reached both control centers, recovery would depend on a full SCADA rebuild, which has not been tested in the last 12 months (gap 8; P01 R-004).
3. **Compressor station recovery is unproven at 3 of 5 stations.** PLC logic backups are missing for Compressor Stations 2, 4, and 5 (gap 8). If station PLCs had to be reloaded, the 4-hour RTO for BP-02 could not be met there.
4. **Visibility is uneven.** OT monitoring covers the GCC, BCC, and Compressor Stations 1 and 3, but not Compressor Stations 2, 4, and 5 or any field site (gap 2). The company could not quickly prove those sites are clean after an incident, which lengthens the time to restart.
5. **Telecommunications are a shared dependency.** 41 field sites rely on cellular gateways and 12 critical sites have satellite backup. A carrier outage would cut visibility at many delivery points at once (P01 R-024).
6. **Third-party laterals add contract exposure.** OSA notice and credit terms apply even when the cause is a cyber event at the company (P09).

## 6. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 Primary SCADA at the GCC | Redundant SCADA servers, 10 HMIs, historian, engineering workstations | BP-01, BP-02, BP-04, BP-06, BP-07 |
| SYS-02 Backup Control Center | Hot standby at Compressor Station 3; 6 HMIs | BP-01, BP-04 |
| SYS-03 Field control devices | About 310 RTUs and PLCs, flow computers, chromatographs | BP-01, BP-02, BP-06 |
| SYS-04 Compressor station control systems | Station PLCs, unit control panels, 22 station HMIs, hardwired ESD | BP-02 |
| SYS-05 SCADA telecommunications | Microwave backbone, licensed radio, MPLS, cellular at 41 sites, satellite backup at 12 | BP-01, BP-02, BP-03, BP-04 |
| SYS-06 IT/OT DMZ and remote access gateway | Historian replica, patch staging, vendor and staff remote access with MFA | BP-06, BP-07, BP-13 |
| SYS-07 OT security monitoring | Passive sensors at 4 sites | BP-13 |
| SYS-09 Identity provider and SYS-10 productivity suite | Sign-in for business systems and remote access; email and chat | BP-03, BP-05, BP-08, BP-10 |
| SYS-11 Cloud landing zone | Measurement and gas accounting, GIS, leak-detection model, backups | BP-06, BP-07, BP-09, BP-11 |
| SYS-12 Customer activities website | Nominations, scheduling, capacity release, Informational Postings | BP-05, BP-08 |
| SYS-13 Business SaaS | ERP, gas accounting, work management, HR and payroll | BP-09, BP-10, BP-14, BP-15 |
| SYS-14 Physical access control and CCTV | Control rooms, stations, M&R intrusion alarms | BP-12 |
| SYS-15 SIEM and EDR (MSSP) | Detection and recovery validation | BP-13 |
| People | 28 controllers and 5 shift supervisors; about 180 field staff per shift for manual operation; SCADA and OT engineering; security team and MSSP | All |
| Facilities | GCC (headquarters), BCC (Compressor Station 3), 5 compressor stations, 6 area offices | All |

## 7. TSA linkage: business critical functions and Critical Cyber Systems
SD 02G defines **business critical functions** as "the Owner/Operator's determination of capacity or capabilities to support functions necessary to meet operational needs and supply chain expectations" (Section VII.B), and **operational disruption** as a deviation from or interruption of those functions (Section VII.N). A **Critical Cyber System** is any IT or OT system or data that, if compromised, could result in operational disruption, including business services (Section VII.C).

This BIA is the company's documented determination of business critical functions. The 5 High-criticality processes (BP-01 to BP-05) are the business critical functions. The systems they depend on are the 8 Critical Cyber Systems listed in the Cybersecurity Implementation Plan (CCS-1 to CCS-8 in `../00_company-facts.md` section 7):

| Business critical function | Critical Cyber Systems it depends on |
|---|---|
| BP-01 Gas control | CCS-1, CCS-2, CCS-3, CCS-5, CCS-8 |
| BP-02 Compressor station operation | CCS-3, CCS-4 |
| BP-03 Emergency response and communication | None (designed to run without IT); radio is part of CCS-3 |
| BP-04 Contract operation of laterals | CCS-1, CCS-2, CCS-3 |
| BP-05 Nominations and scheduling | CCS-7, CCS-8 |

**Finding:** the OT analytics cloud account (added 2025-05) feeds advisory alerts to controllers (BP-07). It is not a Critical Cyber System today because BP-07 is not a business critical function. That determination, and the account itself, were never submitted to TSA as a Cybersecurity Implementation Plan amendment (gap 12; P03).

## 8. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Emergency communications (phones, radio, satellite phones, printed contact lists) | 15 min | Personal cell phones; printed lists at every site |
| 2 | Clean SCADA at the GCC or BCC (SYS-01 or SYS-02) with SYS-05 telecommunications | 1 h | Manual operation plan with field crews at key sites |
| 3 | Lateral monitoring for the OSA customers (same SCADA) | 1 h | Notify owners within 30 minutes; owners staff their laterals |
| 4 | Compressor station control (SYS-04) | 4 h | Local operation from station control rooms and unit panels |
| 5 | MSSP monitoring, OT sensors, and the Cybersecurity Coordinator channel (SYS-15, SYS-07) | 4 h | MSSP works from its own platform; manual log exports |
| 6 | Identity provider and customer activities website (SYS-09, SYS-12) | 4 h | Phone and email nominations to a spreadsheet |
| 7 | Informational Postings and critical notices (SYS-12) | 12 h | Email and phone notices to all 44 shippers |
| 8 | Physical security systems (SYS-14) | 8 h | Staff posted at control room doors; manual logs |
| 9 | GIS and emergency maps (SYS-11) | 24 h | Printed map books |
| 10 | Field work management and compliance records (SYS-13) | 48 h | Paper work orders |
| 11 | Leak-detection model (SYS-11 OT analytics account) | 24 h after the historian replica is clean | SCADA alarms and line-pack trending |
| 12 | Measurement application (SYS-11) | 48 h | Flow computer archives downloaded on site |
| 13 | ERP and gas accounting (SYS-13) | 72 h | Estimated invoices |
| 14 | Payroll and HR (SYS-13) | 72 h | Repeat prior payroll |
| 15 | Supply chain (SYS-13) | 72 h | Paper purchase orders |

The leak-detection model (priority 11) has a shorter RTO than measurement, but it is restored only after its input data path is clean and the model is revalidated, because controllers act on its alerts (P10).
