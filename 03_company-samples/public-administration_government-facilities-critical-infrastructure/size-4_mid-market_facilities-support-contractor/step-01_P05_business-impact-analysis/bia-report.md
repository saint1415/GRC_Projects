# Business Impact Analysis: Cris Santos Company | Government Services and Facilities | Mid-Market

**Organization:** Cris Santos Company, Inc. (facilities support contractor operating government buildings) | **Tier:** Mid-Market (600 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Security Manager and the GRC analyst with the vCISO, the process owners named in `bia.csv`, and the five program managers | **Fieldwork:** 2026-07-06 to 2026-07-31 | **Approved:** Chief Operating Officer, 2026-09-15 (presented to the audit committee the same day)

## 1. Overview and purpose
This BIA covers every business unit: the Remote Operations Center (ROC), Building Technology (BAS and access control), Federal Programs, State and Local Programs, field Operations, and the corporate functions (finance, HR, contracts, legal, IT). It rates 16 business processes and quantifies what an outage costs in money, operations, contract and regulatory exposure, and safety.

The results feed:
- the contingency plan the state contract requires (SP 800-53 CP-2, due 2027-03-31);
- manual-mode (building recovery) procedures for County A, County B, the City, and the school district, modeled on the procedures GSA requires at the federal buildings (BTTRG v3.0, section 1.6.2);
- the FIPS 199 availability rating in the SSP (P02);
- impact ratings and exposure estimates in the risk register (P01);
- the recovery order in both incident runbooks (P08);
- the Availability criteria in the SOC 2 readiness assessment (P09).

## 2. System and business description
The company runs six contracts from its headquarters, a 24x7 primary ROC, a backup ROC, and three regional offices: 5 GSA federal buildings, a state agency portfolio of 9 buildings (including the agency's data center building), County A (19 sites including the Emergency Operations Center and the elections warehouse), County B (9 sites), the City (12 sites), and BAS energy management for a school district (62 schools). For the 46 state, county, and city sites it operates the building automation and access control layers on the Integrated Facility Operations Platform (IFOP). For GSA, company staff operate GSA's own BAS through GSA's virtual desktop. See `../00_company-facts.md` sections 1, 3, and 7.

**A key property of building systems:** field controllers keep running their last programs and schedules, and door controllers cache credentials for up to 72 hours. A loss of the company's platform does not stop the buildings at once. What stops is *change* (new badges, revocations, schedule changes) and *visibility* (alarms). That is why most MTDs are longer than for a typical office system. The exceptions are the processes where people's safety or security depends on an alarm, a revocation, or a critical room's cooling.

## 3. Impact categories and values
Dollar values are scaled to about $100 million in annual revenue over about 250 business days, about $400,000 per business day. The federal contract is about $144,000 per business day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost (per outage) | More than $150,000 (performance deductions, emergency labor, or delayed payment of a full invoice cycle) | $30,000 to $150,000 | Less than $30,000 |
| Operations | A customer facility closes or cannot be secured, or the ROC is blind for more than its MTD | One site, one contract, or one service degraded | Staff slowed but working |
| Contract and regulatory | Contract default or cure notice, a missed customer or legal notice clock, or loss of federal eligibility (for example FAR 52.204-25) | Missed contract report or SLA credit | Internal deviation |
| Safety and physical security | People harmed, a critical facility (EOC or data center) lost during an emergency, or a government building left unsecured | Delayed response to a security or environmental alarm | None |
| Reputation | Regional media coverage or loss of a government customer at rebid | Customer corrective action request | Internal only |

**How loss at MTD was estimated.** Estimated loss is contract performance deductions and SLA credits, plus extra labor (overtime and emergency site visits) over the MTD. Process owners supplied the assumptions: a site run manually needs about 2 technician hours a day; an unmonitored ROC needs about 12 extra site visits an hour; deductions follow each contract's quality assurance plan. Delayed cash is shown separately.

## 4. Process criticality and downtime (from `bia.csv`)
| Priority | Process | Unit | Criticality | MTD (h) | RTO (h) | RPO (h) | Estimated loss at MTD |
|---|---|---|---|---|---|---|---|
| 1 | BP-03 Critical environment support (County A EOC, state data center building) | Operations | High | 4 | 2 | 24 | $40,000 |
| 2 | BP-01 24x7 remote alarm monitoring and dispatch | ROC | High | 4 | 2 | 1 | $25,000 |
| 3 | BP-06 Emergency and hurricane operations | Operations | High | 8 | 4 | 24 | $35,000 |
| 4 | BP-15 Customer communications and incident notification | Corporate | High | 8 | 4 | 24 | $10,000 |
| 5 | BP-02 Access control administration | Building Technology | High | 12 | 4 | 0.25 | $15,000 |
| 6 | BP-04 Federal building O&M (5 GSA buildings) | Federal Programs | High | 24 | 8 | 24 | $30,000 |
| 7 | BP-05 BAS supervision (state, counties, city) | Building Technology | Moderate | 24 | 12 | 24 | $45,000 |
| 8 | BP-16 Corporate email, collaboration, and phones | Corporate | Moderate | 24 | 8 | 4 | $10,000 |
| 9 | BP-13 Onboarding, background checks, PIV sponsorship, and terminations | Corporate | Moderate | 48 | 24 | 24 | $10,000 |
| 10 | BP-07 Work order and preventive maintenance | Operations | Moderate | 72 | 24 | 4 | $60,000 |
| 11 | BP-08 Video surveillance support and evidence exports | Building Technology | Moderate | 72 | 24 | 24 | $5,000 |
| 12 | BP-09 Controller program engineering, backup, and restore | Building Technology | Moderate | 72 | 48 | 24 | $20,000 |
| 13 | BP-12 Payroll and timekeeping | Corporate | Moderate | 96 | 48 | 24 | $15,000 |
| 14 | BP-11 Contract reporting, invoicing, and collections | Corporate | Moderate | 120 | 72 | 24 | $25,000 (plus up to $8.3 million of a month-end invoice cycle delayed) |
| 15 | BP-14 Procurement and supplier screening | Corporate | Moderate | 120 | 72 | 24 | $5,000 |
| 16 | BP-10 School district energy management and fault analytics | State and Local Programs | Low | 168 | 72 | 24 | $8,000 |

**Summary:** 6 High, 9 Moderate, and 1 Low process (16 in total). The sum of estimated losses at each process's MTD is $358,000.

**Enterprise-wide scenario.** If the whole IFOP were down for 72 hours (for example, ransomware in the cloud landing zone), the estimated loss is about $610,000: emergency staffing and overtime to run 46 sites by hand (about $290,000), contract performance deductions and SLA credits (about $180,000), and deferred billable project work (about $140,000). Incident response and notification costs come on top (P01 R-002 and R-005). The federal buildings would keep running, because GSA's BAS is outside the IFOP.

**What drives the values:**
- **Safety and critical facilities** drive BP-01, BP-03, and BP-06. The EOC and the state data center building have the shortest MTD (4 hours) because cooling and power monitoring there protect an emergency coordination center and a data center.
- **Security** drives BP-02. Its 15-minute RPO exists because a lost badge revocation is a security gap, not only lost data.
- **Contract clocks** drive BP-15. County A requires notice within 6 hours of suspected ransomware, so the notification path must be back within 4 hours even if company email is down.
- **Cash flow**, not time, drives BP-11. Customers pay late invoices, but a missed month-end cycle delays about $8.3 million.

## 5. Key findings
1. **The 2-hour ROC RTO depends on a failover that has been tested only once.** The backup ROC took 2 hours 40 minutes to take over in the 2026 hurricane season drill, because 4 of the 10 backup workstations lacked current alarm console profiles (P01 R-024; P07 CP-4).
2. **Recovery of the BAS supervisory layer is unproven.** Backups are isolated and write-once, but only one supervisory cluster restore (CT-S) has been tested, and it took 11 hours against a 12-hour RTO (P01 R-006).
3. **The controller program repository is incomplete.** About 45% of controllers have no current program backup, so the 48-hour RTO for BP-09 cannot be met for those sites (P01 R-007).
4. **Manual-mode procedures exist only at the federal and state sites.** County A, County B, the City, and the school district have none. For County A this includes the EOC (P01 R-008).
5. **The access control vendor's recovery commitments meet BP-02.** The vendor's SOC 2 system description states an RTO of 4 hours and an RPO of 15 minutes (P09 `vendor-soc2-review.csv`). The company's own dependency is the identity provider and the broker, which must come back first.

## 6. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-06 Identity provider | Sign-in and MFA for all company systems and administrator portals | All |
| SYS-14 Primary and backup ROC | Alarm consoles, video wall, out-of-band phones | BP-01, BP-06, BP-15 |
| SYS-03 Remote access broker | The approved path to site OT and the school district BAS | BP-01, BP-05, BP-09, BP-10 |
| SYS-02 Access control and video tenants | Cardholders, door schedules, alarms, video | BP-01, BP-02, BP-08 |
| SYS-01 BAS supervisory platform | Schedules, setpoints, alarms, trends (8 clusters) | BP-01, BP-03, BP-05, BP-09 |
| SYS-04 Landing zone file storage, program repository, and backup vault | Drawings, CUI library, controller programs, backups (30-day write-once) | BP-05, BP-09; recovery of SYS-01 and SYS-03 |
| SYS-05 Site edge firewalls and ISPs | Connectivity to 46 sites | BP-01, BP-03, BP-05 |
| SYS-08 CMMS | Work orders, asset lists, change tickets | BP-04, BP-06, BP-07, BP-11 |
| SYS-10 GSA virtual desktop and PIV cards | Access to GSA's BAS | BP-04 |
| SYS-11 ERP and HR suite | Invoicing, payroll, HR records | BP-11, BP-12, BP-13, BP-14 |
| SYS-12 SIEM and MDR | Detection and recovery validation | Recovery validation for all |
| Third parties | Access control SaaS vendor, cloud provider, CMMS vendor, MSSP, ISPs, mobile carrier, BAS software vendor, GSA IT | As listed in `bia.csv` |
| People and facilities | 23 ROC operators, 57 BAS and security systems technicians and engineers, 152 PIV holders, on-site engineers at the EOC and data center building, regional offices | All |

## 7. Customer continuity linkage
The customers' own continuity duties depend on this BIA:

| Customer requirement | What this BIA supplies | Status |
|---|---|---|
| GSA: building recovery procedures for the BAS (BTTRG v3.0 section 1.6.2) | BP-04 MTD 24 hours; PIV staffing as the key resource | In place; exercised with GSA in March 2026 |
| CT-S exhibit: contingency plan and testing (SP 800-53 CP-2, CP-4) | MTD, RTO, and RPO for every IFOP process; recovery priorities in section 8 | Plan due 2027-03-31 (P07 POAM-009) |
| County A: EOC support during activations | BP-03 MTD 4 hours; local operator workstation and on-site engineer | Manual-mode procedure for the EOC due 2026-12-15 (P07 POAM-010) |
| County B, City, and school district: continuity of building operations | BP-05 and BP-10 values; manual-mode procedure template from the state sites | Procedures due 2027-03-31 |
| Supervisor of Elections annex: cage access log export after each election | BP-02 RPO 15 minutes keeps access history complete | Met by the access control vendor's retention |

## 8. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-06 identity provider and break-glass accounts | 1 h | Two break-glass administrator accounts per critical system, sealed and stored offline |
| 2 | Local operator workstations at the EOC and the state data center building | 0 h (local) | On-site engineer runs equipment in hand mode |
| 3 | SYS-14 ROC (primary, or failover to the backup ROC) | 2 h | Backup ROC; satellite phones and printed site lists |
| 4 | SYS-03 remote access broker | 2 h | Rebuild from image in the shared services account; site visits until then |
| 5 | SYS-12 SIEM and EDR consoles | 4 h | MSSP runs from its own platform; needed to validate a clean recovery |
| 6 | SYS-02 administrator access (vendor-hosted) | 4 h | Customer security staff use printed emergency revoke lists |
| 7 | SYS-07 email, chat, and phones | 8 h | Mobile phones and the out-of-band messaging group |
| 8 | SYS-01 BAS supervisory clusters (County A and CT-S first) | 12 h | Manual-mode procedures; changes at the controller |
| 9 | SYS-08 CMMS (vendor-hosted) | 24 h | Paper work orders |
| 10 | NVR exports and video management | 24 h | Export at the NVR on site |
| 11 | SYS-04 controller program repository | 48 h | Laptop copies; vendor commissioning files |
| 12 | SYS-11 HR, payroll, and ERP (vendor-hosted) | 48 h (payroll), 72 h (ERP) | Repeat prior payroll; invoice from accounting extracts |
| 13 | School district analytics | 72 h | District runs its own server |

GSA access (SYS-10) is outside this list. GSA recovers its own systems; the company keeps PIV holders available and runs the building recovery procedures.
