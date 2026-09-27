# Business Impact Analysis: Cris Santos Company | Water and Wastewater Systems | Small

**Organization:** Cris Santos Company, LLC (investor-owned community water system) | **Tier:** Small (60 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** IT Manager with the Operations Manager, Water Quality Supervisor, Field Services Supervisor, and Customer Service and Billing Manager | **Approved:** General Manager, 2026-08-31

## 1. Overview and purpose
This BIA identifies which business processes the company depends on, how long each can be down, and how much data it can lose. It supports:
- the RRA and ERP required by SDWA section 1433, especially the assessment of automated systems and operation and maintenance (42 U.S.C. 300i-2(a)(1)(A)(ii) and (vi)) and the ERP plans and procedures (300i-2(b)(2));
- the availability and integrity ratings in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08).

## 2. System and business description
The company serves 46,200 people through about 18,400 connections from 14 wells and two treatment plants (WTP-1, 6.0 MGD; WTP-2, 2.5 MGD). Average day demand is 5.2 MGD. Storage totals 4.6 million gallons in 4 tanks, with 6 booster stations. The Water Treatment SCADA System (WTSS) supervises the plants and remote sites. Customer, billing, AMI, lab, and GIS systems are SaaS. See `../00_company-facts.md` sections 3-4.

## 3. Impact categories and values
Dollar values are scaled to $24.6 million in annual revenue, about $67,000 per day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $200,000 (about 3 days of revenue) | $50,000 to $200,000 | Less than $50,000 |
| Operations | Customers lose water or pressure in a large area | One plant, pressure zone, or service stops | Staff slowed but working |
| Regulatory | Tier 1 public notice situation, treatment technique or MCL violation, or missed EPA certification | Missed reporting deadline or Tier 2 or 3 notice | Internal policy deviation |
| Public health and safety | Plausible illness or injury from unsafe water or a chemical release | Precautionary boil water notice for a limited area | None |
| Reputation | Regional media coverage or regulator enforcement | Customer complaints or local news mention | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Water treatment and chemical feed | High | 12 h | 1 h | 24 h |
| BP-02 Distribution pumping and pressure | High | 6 h | 2 h | 24 h |
| BP-03 Supervisory monitoring and control (SCADA and telemetry) | High | 72 h | 48 h | 24 h |
| BP-04 Water quality monitoring and compliance sampling | High | 24 h | 12 h | 4 h |
| BP-05 Emergency response and public notification | High | 24 h | 4 h | 24 h |
| BP-06 Customer service and call center | Moderate | 48 h | 24 h | 4 h |
| BP-07 Billing and payments | Moderate | 120 h | 72 h | 24 h |
| BP-08 Meter reading (AMI and manual) | Low | 168 h | 120 h | 24 h |
| BP-09 Field operations and work orders | Moderate | 24 h | 8 h | 24 h |
| BP-10 Laboratory information management | Low | 72 h | 48 h | 24 h |
| BP-11 Payroll and HR | Low | 120 h | 72 h | 24 h |
| BP-12 Water quality analytics (anomaly detection pilot) | Low | 168 h | 72 h | 24 h |

**What drives the values:**
- **Treatment is separate from SCADA.** BP-01 (making safe water) has a 12-hour MTD set by storage. BP-03 (supervising it from the control room) has a 72-hour MTD because licensed operators can run both plants manually. The 1-hour RTO for BP-01 is the time to switch to manual control, not to restore SCADA. This split is the most important resilience fact in the BIA, and it only holds if manual-mode procedures and staffing are ready (P01 R-018).
- **RPO for BP-01 and BP-03 means known-good control logic.** After a cyber incident, the company must reload PLC logic and HMI projects that it trusts. Today the only in-house copy sits on the engineering workstation (P01 R-006), so the 24-hour RPO is **not achievable** until offline backups exist (POAM-006).
- **Regulatory clocks set BP-04 and BP-05.** A failure or significant interruption in key treatment processes can require a Tier 1 notice and primacy agency consultation within 24 hours (40 CFR 141.202). BP-05 therefore has a 4-hour RTO: the team must be able to decide and draft a notice well inside the 24 hours, even if the CIS and email are down.
- **Cash, not safety, drives BP-07.** About $2.0 million is billed each month. A delayed billing cycle defers revenue but does not lose it.

**Key finding:** the SCADA integrator is the only party that can rebuild the SCADA servers today, and its contract has no response-time commitment. The 48-hour RTO for BP-03 is **unproven** until the company has rebuild media, offline backups, and a tested OT recovery procedure (P03 G-043).

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-02 PLCs and RTUs | Local control of wells, treatment, chemical feed, boosters, tanks | BP-01, BP-02, BP-03 |
| SYS-01 SCADA servers and HMIs | Control room supervision, alarms, historian | BP-03, BP-04 |
| SYS-03 Telemetry | Radio and cellular links to 24 remote sites | BP-02, BP-03 |
| Plant power | Utility power with standby generators at both plants and 10 wells | BP-01, BP-02 |
| SYS-08 CIS | Accounts, call campaigns, billing | BP-05, BP-06, BP-07 |
| SYS-10 LIMS and contract lab | Lab results and reports | BP-04, BP-10 |
| SYS-12 GIS and work orders | Maps, valves, work orders | BP-09 |
| SYS-06 Identity provider | Sign-in to SaaS and cloud | BP-05 to BP-12 |
| People | 14 licensed operators, 2 SCADA technicians, lab, field crews, customer service | All |
| External | SCADA integrator, chemical suppliers, electric utility, fuel contractor, WARN mutual aid, neighboring utility interconnect (1.5 MGD) | BP-01 to BP-03 |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Manual (local) control of plants and chemical feed | 1 h | Licensed operators on site; hardwired limits and alarms |
| 2 | Booster stations and tank levels | 2 h | Local pressure-switch control; roving operators |
| 3 | Compliance and process sampling | 4 h | Grab samples every 4 hours; portable kits |
| 4 | Public notice capability | 4 h | Offline contact list; broadcast media; posting |
| 5 | Field dispatch with maps | 8 h | Printed map books; radio |
| 6 | Customer service phones and CIS | 24 h | Scripts and paper forms |
| 7 | SCADA servers and HMIs, rebuilt from known-good media | 48 h | Manual operation until verified clean (P08) |
| 8 | Billing and payments | 72 h | Delay the billing cycle |
| 9 | Remaining systems (AMI, LIMS, payroll, analytics) | 72-120 h | Manual reads, paper bench sheets, repeat payroll |

SCADA is recovered **after** manual operation, sampling, and public notice are stable. After a cyber incident, reconnecting a SCADA system that might still be compromised is more dangerous than running manually for another day.
