# Business Impact Analysis: Cris Santos Company | Water and Wastewater Systems | Mid-Market

**Organization:** Cris Santos Company, Inc. (PE-backed investor-owned water utility: 11 community water systems and Utility Services for 3 municipal clients) | **Tier:** Mid-Market (600 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Security Manager and the Emergency Management and Resilience Manager, with the process owners named in `bia.csv` | **Fieldwork:** 2026-07-06 to 2026-07-31 | **Approved:** Chief Operating Officer, 2026-09-15 (presented to the audit committee the same day)

## 1. Overview and purpose
This BIA covers every business unit: the Regional, Lakes, and Ridge Systems, the 8 small systems, the Regional Operations Center (ROC), water quality, customer service, Utility Services, field services, engineering, and enterprise support functions. It rates 18 business processes and quantifies what an outage costs in money, operations, regulatory exposure, and public health.

The results feed:
- the risk and resilience assessments (RRAs) and emergency response plans (ERPs) required by SDWA section 1433 for the 3 covered systems, especially the assessment of automated systems, monitoring practices, and operation and maintenance (42 U.S.C. 300i-2(a)(1)(A)(ii), (iii), and (vi)) and the ERP plans and procedures (300i-2(b)(2)) (section 7);
- the FIPS 199 availability and integrity ratings in the SSP (P02);
- impact ratings and exposure estimates in the risk register (P01);
- the recovery order in both incident runbooks (P08);
- the Availability and Processing Integrity criteria in the SOC 2 readiness assessment for Utility Services (P09).

## 2. System and business description
The company serves 273,900 people through 107,800 connections in 11 groundwater systems. Three systems serve more than 3,300 people: the Regional System (171,400 people; WTP-R1, 22 MGD lime softening, and WTP-R2, 10 MGD reverse osmosis), the Lakes System (63,500; WTP-L1, 9 MGD), and the Ridge System (27,400; WTP-G1 and the unstaffed WTP-G2). Eight small systems serve 11,600 people. The Integrated Water Operations SCADA (IWOS, P02) supervises them from the 24x7 ROC. The company also monitors 3 municipal clients' plants after hours and bills 15,600 client accounts in its CIS. Customer, billing, AMI, lab, GIS, and finance systems are SaaS; analytics run in a 4-account cloud landing zone (P04). See `../00_company-facts.md` sections 1, 3, and 7.

## 3. Impact categories and values
Dollar values are scaled to about $100 million in annual revenue, about $274,000 per day. Regulated water revenue is billed monthly in arrears, so most outages defer cash rather than lose it. The real costs of a water outage are emergency response, notices, bottled water, flushing, sampling, overtime, mutual aid, contract credits, and enforcement.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost (per event) | More than $250,000 (about one day of revenue), or more than $1 million of cash delayed | $50,000 to $250,000 | Less than $50,000 |
| Operations | A covered system, or the ROC for all systems, cannot deliver its core function | One plant, pressure zone, small system, or service line stops | Staff slowed but working |
| Regulatory | Tier 1 public notice situation, treatment technique or MCL violation, or a missed EPA certification | Missed reporting deadline, Tier 2 or 3 notice, or a contract service-level breach | Internal policy deviation |
| Public health and safety | Plausible illness or injury from unsafe water or a chemical release | Precautionary boil water notice for a limited area | None |
| Reputation | Regional media coverage, regulator enforcement, or loss of a municipal client | Customer complaints or local news mention | Internal only |

**How loss at MTD was estimated.** Estimated loss is the extra cost the company incurs if the outage lasts exactly to its MTD: overtime and mutual aid, emergency contractor call-outs, sampling, notice delivery, contract service credits, and interest on delayed cash. Costs after the MTD (for example a multi-day boil water notice) are shown in the enterprise scenarios below, not in the per-process figure.

## 4. Process criticality and downtime (from `bia.csv`)
| Priority | Process | Unit | Criticality | MTD (h) | RTO (h) | RPO (h) | Estimated loss at MTD |
|---|---|---|---|---|---|---|---|
| 1 | BP-01 Water treatment and chemical feed | Regional System | High | 8 | 1 | 24 | $180,000 |
| 2 | BP-02 Water treatment and chemical feed | Lakes System | High | 10 | 1 | 24 | $60,000 |
| 3 | BP-03 Water treatment and chemical feed | Ridge System | High | 12 | 2 | 24 | $35,000 |
| 4 | BP-05 Distribution pumping and pressure | All owned systems | High | 4 | 2 | 24 | $120,000 |
| 5 | BP-04 Small-system treatment and disinfection | Small systems | High | 8 | 4 | 24 | $25,000 |
| 6 | BP-08 Emergency response and public notification | Enterprise | High | 24 | 4 | 24 | $75,000 |
| 7 | BP-07 Water quality monitoring, laboratory, and compliance reporting | Water Quality | High | 24 | 8 | 4 | $40,000 |
| 8 | BP-09 Remote monitoring and alarm response for municipal clients | Utility Services | High | 4 | 2 | 1 | $20,000 |
| 9 | BP-14 Field operations, main breaks, and work orders | Field Services | Moderate | 24 | 8 | 24 | $50,000 |
| 10 | BP-10 Customer contact center | Customer Service | Moderate | 24 | 8 | 4 | $30,000 |
| 11 | BP-06 Centralized supervisory monitoring and control (ROC and SCADA) | ROC | High | 48 | 24 | 24 | $210,000 |
| 12 | BP-15 Chemical supply and inventory | Water Operations | Moderate | 72 | 24 | 24 | $15,000 |
| 13 | BP-12 Billing for municipal clients | Utility Services | Moderate | 72 | 48 | 24 | $45,000 |
| 14 | BP-11 Billing and payments (own customers) | Customer Service | Moderate | 120 | 72 | 24 | $90,000 (plus about $1.2 million cash delayed) |
| 15 | BP-16 Payroll, HR, and finance close | Enterprise | Low | 120 | 72 | 24 | $30,000 |
| 16 | BP-13 Meter reading (AMI and manual) | Customer Service | Low | 168 | 120 | 24 | $25,000 |
| 17 | BP-18 Water quality analytics and AI decision support | Water Quality | Low | 168 | 72 | 24 | $5,000 |
| 18 | BP-17 Engineering, capital planning, and asset management | Engineering | Low | 240 | 168 | 24 | $10,000 |

**Summary:** 9 High, 5 Moderate, and 4 Low processes (18 in total). The sum of estimated losses at each process's MTD is $1,065,000.

**Enterprise-wide scenarios.**
- **All plants on manual operation for 72 hours** (for example after a cyber incident that takes the ROC and SCADA offline): about $420,000 in overtime, roving crews, mutual aid, and integrator call-outs, with no lost water revenue if manual operation holds.
- **Precautionary boil water notice for the whole Regional System for 48 hours** (for example after unsafe chemical feed reached distribution): about $1.5 million to $2.5 million (bottled water distribution, flushing, extra sampling, customer credits, notices, and overtime), plus enforcement and reputational harm that the BIA does not price.
- **CIS outage of 5 business days** (for example ransomware at the CIS vendor): about $1.2 million of own-customer cash delayed, about $90,000 of overtime and interest, and Utility Services contract credits.

**What drives the values:**
- **Treatment is separate from SCADA.** Making safe water (BP-01 to BP-04) has short MTDs set by storage (8 to 12 hours). Supervising it from the ROC (BP-06) has a 48-hour MTD because licensed operators can run every plant manually. The 1-hour RTO for BP-01 and BP-02 is the time to switch to manual control, not to restore SCADA. This split is the most important resilience fact in the BIA, and it holds only where manual-mode procedures and staffing are ready.
- **RPO for treatment means known-good control logic.** After a cyber incident, the company must reload PLC logic and HMI projects that it trusts. The Regional System keeps quarterly offline copies. Lakes, Ridge, and the small systems have no in-house offline copy (gap 6), so their 24-hour RPO is **not achievable** today.
- **Regulatory clocks set BP-07, BP-08, and BP-09.** A failure or significant interruption in key treatment processes can require a Tier 1 notice and primacy agency consultation within 24 hours (40 CFR 141.202). A disinfectant residual below the state minimum for more than 4 hours must be reported by the end of the next business day (141.405(a)(1)). The Utility Services contracts require alarm acknowledgment within 15 minutes.
- **Cash, not safety, drives BP-11.** About $7.3 million is billed each month. A delayed cycle defers revenue but does not lose it.

## 5. Key findings
1. **Recovery at the acquired systems is unproven.** Only the Regional SCADA servers have a tested rebuild (2025). Lakes and Ridge depend on Integrator B, whose inherited contracts have no response-time commitment, and the Ridge server runs an unsupported operating system. The 24-hour RTO for BP-06 is a target at Lakes and Ridge, not a demonstrated capability (P01 R-008, R-016; P07 CP-4).
2. **Manual operation is the real recovery strategy, and it is uneven.** The Regional System drills manual mode twice a year; Lakes once a year; Ridge has not drilled since acquisition, and WTP-G2 is unstaffed. Manual-mode procedures for each chemical feed must be written and drilled at every plant (P01 R-019; P03 G-016).
3. **One ROC is a single point of failure for 11 systems and 3 clients.** The ROC has no alternate control room. If the ROC building or its network is lost, plants fall back to local control and client monitoring falls back to the clients' own dialers. An alternate ROC position at WTP-R2 (standby SCADA server is already there) should be equipped and tested (P01 R-021).
4. **Utility Services has the shortest contractual clock.** Alarm acknowledgment for clients within 15 minutes (BP-09, MTD 4 hours) means client monitoring must be restored before most company IT. This is an Availability commitment for SOC 2 (P09 A1.2).
5. **Public notice must work without the CIS or email.** BP-08 needs offline contact exports for 273,900 people and the wholesale city, and Spanish-language templates. Exports exist for the Regional System only (P03 G-058).

## 6. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-02 Field controllers | 41 PLCs and 75 RTUs; local control of wells, treatment, chemical feed, boosters, tanks | BP-01 to BP-06 |
| SYS-01 Regional SCADA | ROC and plant HMIs, historian, alarm notification; standby server at WTP-R2 | BP-06, BP-07, BP-09 |
| SYS-05 Lakes and Ridge SCADA | Local supervision at WTP-L1 and WTP-G1 | BP-02, BP-03, BP-06 |
| SYS-03 Telemetry | Radio, fiber, and 25 cellular modems | BP-04, BP-05, BP-06 |
| SYS-04 OT remote access | Gateway at Regional; site-to-site VPNs; on-call access | BP-06, BP-09 |
| Offline OT backups | Quarterly PLC logic and HMI project copies (Regional only today) | RPO for BP-01 to BP-04 |
| Plant power | Utility power; standby generators at all plants and 30 of 41 wells | BP-01 to BP-05 |
| SYS-10 CIS | Accounts, call campaigns, billing for own and client customers; vendor disaster recovery | BP-08, BP-10, BP-11, BP-12 |
| SYS-12 LIMS and the in-house lab | Results and state reports | BP-07 |
| SYS-13 GIS and work orders | Maps, valves, work orders | BP-14, BP-17 |
| SYS-07 Cloud landing zone | Historian replica, analytics, file services; daily write-once backups in a separate account (35 days) | BP-17, BP-18 |
| SYS-08 Identity provider | Sign-in to SaaS and cloud; MFA for the OT gateway | BP-06 (gateway), BP-07 to BP-18 |
| People | 140 treatment operators, 22 ROC operators, 18 SCADA staff, 20 lab staff, 160 field staff, 70 customer service staff | All |
| External | Integrators A and B, chemical suppliers, electric utility, fuel contractor, WARN mutual aid, cellular and radio carriers, CIS vendor, payment processor, MSSP | As listed in `bia.csv` |

## 7. SDWA section 1433 linkage
The 3 covered systems must assess the resilience of their "electronic, computer, or other automated systems (including the security of such systems)", their monitoring practices, and their operation and maintenance (42 U.S.C. 300i-2(a)(1)(A)(ii), (iii), (vi)), and their ERPs must include plans, procedures, and equipment for a malevolent act or natural hazard (300i-2(b)(2)). This BIA supplies that content:

| 300i-2 element | What this BIA supplies | Status |
|---|---|---|
| (a)(1)(A)(ii) automated systems | Dependencies of every treatment process on SYS-01 to SYS-06; MTD, RTO, and RPO per system | Supplied; feeds the RRA cyber addendum for all 3 covered systems (P01) |
| (a)(1)(A)(iii) monitoring practices | BP-07 sampling fallbacks; BP-18 limits of the AI alerts | Supplied |
| (a)(1)(A)(vi) operation and maintenance | Manual-mode RTOs; integrator dependence at Lakes and Ridge | Gap: manual procedures incomplete at Ridge (finding 2) |
| (b)(2) plans and procedures | Recovery priorities in section 8; workarounds in `bia.csv` | To be written into the Ridge ERP by 2026-12-04 and the Lakes and Regional ERPs at their next revision |
| (b)(3) actions that lessen impact | Hardwired chemical feed limits, manual operation, emergency interconnects, generators | Supplied |
| (c) coordination with LEPCs | Not a BIA item; tracked in P03 | See P03 |

The small systems are not required to certify, but the company applies the same BIA values to them because they are operated by the same ROC and staff.

## 8. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Manual (local) control of treatment and chemical feed at WTP-R1, WTP-R2, WTP-L1 | 1 h | Licensed operators on site; hardwired limits and alarms |
| 2 | Manual control at WTP-G1 and WTP-G2 (Ridge) | 2 h | On-call operator to WTP-G2 |
| 3 | Booster stations and tank levels (all systems) | 2 h | Local pressure-switch control; roving operators |
| 4 | Small-system wells and chlorinators | 4 h | Roving operators; portable test kits |
| 5 | Public notice capability (offline contacts, templates, media) | 4 h | Broadcast media; posting; door hangers |
| 6 | Compliance and process sampling | 4-8 h | Grab samples every 4 hours; portable kits |
| 7 | Client alarm monitoring (Utility Services) | 2 h | Clients' own dialers; ROC phones clients from a printed list |
| 8 | Field dispatch with maps | 8 h | Printed map books; radio |
| 9 | Contact center phones and CIS access | 8 h | Scripts and paper forms |
| 10 | ROC and SCADA, rebuilt or verified clean, one system at a time (Regional first) | 24 h | Manual operation until verified (P08) |
| 11 | Chemical ordering | 24 h | Phone orders |
| 12 | Client billing, then own billing | 48-72 h | Delay cycles with client approval; estimated bills |
| 13 | Remaining systems (payroll, AMI, analytics, engineering) | 72-168 h | Repeat payroll; manual reads; defer |

SCADA is recovered **after** manual operation, sampling, and public notice are stable. After a cyber incident, reconnecting a SCADA system that might still be compromised is more dangerous than running manually for another day.
