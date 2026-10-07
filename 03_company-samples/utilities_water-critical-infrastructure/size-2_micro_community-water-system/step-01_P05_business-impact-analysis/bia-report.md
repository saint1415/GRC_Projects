# Business Impact Analysis: Cris Santos Company | Water and Wastewater Systems | Micro

**Organization:** Cris Santos Company, LLC (privately held community water system, 2,850 population served) | **Tier:** Micro (7 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Office Manager (security and compliance coordinator) with the Chief Operator, the Customer Service and Billing Clerk, and the MSP lead technician, 2026-07-13 to 2026-07-24 | **Approved:** Owner and General Manager, 2026-08-31

## 1. Overview and purpose
This BIA lists every business function of the water system, how long each can be down, and how much data each can lose. It is the first step of the company's first written security and resilience work. It supports:
- the availability and integrity ratings in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08);
- a rewrite of the 2023 emergency plan, which covers hurricanes and power loss but not cyber events.

**Why there is no federal ERP driver here.** SDWA section 1433 requires an RRA and ERP only from community water systems serving more than 3,300 persons (42 U.S.C. 300i-2(a)(1), (b)). The company serves 2,850, so it has no certification duty (P03). The binding clocks that shape this BIA come from the drinking water rules that apply to every community water system: the 24-hour Tier 1 public notice (40 CFR 141.202) and, because the company monitors chlorine residual continuously, the 4-hour grab sampling fallback (40 CFR 141.403(b)(3)(i)(A)).

## 2. System and business description
One Florida service area of 1,190 connections, supplied by 3 wells and one plant site with aeration and sodium hypochlorite disinfection. Average day demand is 0.23 MGD and maximum day 0.42 MGD. Storage is a 300,000-gallon ground tank at the plant and a 150,000-gallon elevated tank. The plant is staffed on weekday day shift; at other times an on-call licensed operator watches alarms by phone and connects to the HMI remotely. The Water Treatment SCADA System (WTSS, P02) supervises the plant and the 2 remote sites. Billing, email, and accounting are SaaS; the MSP runs office IT. See `../00_company-facts.md` sections 3 and 7.

## 3. Impact categories and values
Dollar values are scaled to about $1.1 million in annual revenue, about $3,000 per day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $25,000 (about 8 days of revenue, or an emergency repair or rental the reserve cannot absorb) | $5,000 to $25,000 | Less than $5,000 |
| Operations | Customers lose water or pressure across the system | One well, the remote monitoring, or one office function stops | Staff slowed but working |
| Regulatory | Tier 1 public notice situation, treatment technique violation, or missed residual requirement | Missed monitoring, late report, or Tier 2 or 3 notice | Internal deviation only |
| Public health and safety | Plausible illness or injury from unsafe water or a chemical overfeed | Precautionary boil water notice for part of the system | None |
| Reputation | Regional media coverage, a school closure, or regulator enforcement | Customer complaints or a local news mention | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Water production and treatment | High | 12 h | 1 h | 24 h |
| BP-02 Distribution pumping and pressure | High | 6 h | 1 h | 24 h |
| BP-03 Remote monitoring and alarm response | High | 48 h | 24 h | 24 h |
| BP-04 Compliance monitoring, sampling, and reporting | High | 24 h | 4 h | 4 h |
| BP-05 Emergency response and public notification | High | 24 h | 4 h | 24 h |
| BP-06 Customer service, billing, and payments | Moderate | 120 h | 72 h | 24 h |
| BP-07 Meter reading and field work | Low | 168 h | 120 h | 24 h |
| BP-08 Office administration, accounting, and payroll | Low | 120 h | 72 h | 24 h |

**What drives the values:**
- **Making water is separate from watching it.** BP-01 has a 12-hour MTD set by usable storage at maximum day demand. Its 1-hour RTO is the time to start the wells and chlorine feed by hand, not to restore SCADA. BP-03 (SCADA and remote alarms) tolerates 48 hours because operators can staff the plant, but with only 3 licensed operators that is the limit (P01 R-013).
- **RPO for BP-01 means a trusted PLC program.** After a cyber incident the company must reload a PLC program and setpoints it knows are good. Today the only copies are on the HMI computer and the integrator's laptop, so the 24-hour RPO is **not achievable** until the company keeps its own offline copy (P01 R-004).
- **Regulatory clocks set BP-04 and BP-05.** If the chlorine analyzer or its record is lost, grab samples every 4 hours start at once (RPO and RTO of 4 hours). A Tier 1 notice must reach persons served within 24 hours, so the notice capability needs a 4-hour RTO even if email and the billing system are down.
- **Cash, not safety, drives BP-06 to BP-08.** About $92,000 is billed each month and the cash reserve covers about 45 days.

## 5. Resource requirements and vendor dependencies
| Resource | Description | Recovery method behind the RPO | Supports |
|---|---|---|---|
| SYS-02 Plant PLC and 2 RTUs | Wells, aerator, chlorine pump pacing, high-service pumps, tank levels | PLC program copies on SYS-01 and the integrator's laptop only (**no company backup**) | BP-01, BP-02, BP-03 |
| SYS-01 SCADA HMI computer | Control room supervision, alarms, local historian, PLC programming software | None (no image or project backup) | BP-03, BP-04 |
| SYS-12 Alarm dialer | Chlorine high and low, low tank level, power failure, intrusion | Standalone; configuration written on the panel door | BP-01, BP-03 |
| SYS-03 Cellular modems | Well 3 and elevated tank telemetry | Spare modem held by the integrator | BP-02, BP-03 |
| SYS-04 and SYS-05 | Remote desktop tool; remote monitoring service and mobile app | Vendor-hosted; trend history kept for 2 years | BP-03, BP-04 |
| SYS-07 Billing system | Customer accounts and the contact list for notices | Vendor backups (stated in its service terms) | BP-05, BP-06 |
| SYS-06 Productivity suite | Email, notice templates, emergency plan, lab reports | Nightly copy by SYS-10 (**never restore-tested**) | BP-04, BP-05, BP-08 |
| SYS-08 Accounting and payroll | Payroll and payables | Vendor backups | BP-08 |
| Plant power | Utility power; automatic standby generator at the plant; portable generator hookup at Well 3 | Fuel delivery contract | BP-01, BP-02 |
| People | 3 licensed operators, Utility Field Technician, office staff | Cross-training: the Office Manager covers billing calls | All |

**Vendor dependencies:**
| Vendor | Functions that stop without it | Evidence of recovery capability |
|---|---|---|
| SCADA integrator | Rebuilding SYS-01, reloading the PLC, any HMI change | None. Time-and-materials contract with no response time; the only outside copy of the PLC program |
| Remote monitoring vendor | Remote alarms by app, trend history (BP-03, BP-04) | SOC 2 Type 2 report reviewed in P09 |
| MSP | Office computers, firewall, office backup | 4-business-hour response time; contract excludes plant control systems |
| Billing SaaS vendor | BP-05 contact list, BP-06 | Vendor service terms |
| Cellular carrier and internet provider | Remote sites, remote monitoring, remote access | None; one internet line, no failover (P01 R-021) |
| Chemical supplier, electric utility, fuel contractor | BP-01, BP-02 | Delivery contracts; 30 days of hypochlorite on site |

**Key findings:**
1. **The integrator is a single point of recovery.** Only the integrator can rebuild the HMI computer, and the company holds no copy of its own PLC program (P01 R-004).
2. **Manual operation works but is not written down.** It worked for 2 days in October 2024. The steps live in the operators' heads (P03 G-033).
3. **The contact list for a Tier 1 notice lives in a SaaS system.** If the billing system or the office network is down, the October 2024 printout is the only copy (P01 R-010).
4. **Staffing limits the SCADA outage the company can survive.** Three licensed operators can cover the plant around the clock for about 2 days (P01 R-013).

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Hand operation of wells, aerator, and chlorine feed | 1 h | Licensed operator on site; mechanical stroke limit and alarm dialer stay active |
| 2 | High-service pumps and elevated tank level | 1 h | Run a pump by hand; tank level gauge at the plant; field check at the tank |
| 3 | Chlorine residual monitoring | 4 h | Grab samples every 4 hours with the portable colorimeter, logged on paper |
| 4 | Public notice capability | 4 h | Printed contact list and template in the plant binder; door hangers; local radio |
| 5 | Plant staffing plan | 12 h | 12-hour shifts; relief operator from a neighboring system after 48 hours |
| 6 | SCADA HMI computer, rebuilt from known-good media with a verified PLC program | 24 h | Hand operation and staffed plant until verified clean (P08) |
| 7 | Remote monitoring and alarms by app | 24 h | Alarm dialer covers the critical alarms |
| 8 | Billing and customer service | 72 h | Scripted phone message; delay the billing cycle |
| 9 | Office administration, payroll, and meter reading | 72-120 h | Repeat prior payroll; estimated reads for one cycle |

SCADA comes back **after** safe water, sampling, and notice capability are stable. After a cyber incident, reconnecting a SCADA computer that might still be compromised is more dangerous than running by hand for another day.
