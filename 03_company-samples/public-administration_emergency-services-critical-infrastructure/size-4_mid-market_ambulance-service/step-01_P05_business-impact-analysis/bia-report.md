# Business Impact Analysis: Cris Santos Company | Emergency Services | Mid-Market

**Organization:** Cris Santos Company, Inc. (licensed private ambulance service; PE-backed) | **Tier:** Mid-Market (600 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Security Manager with the vCISO, the process owners named in `bia.csv`, and the Medical Director | **Fieldwork:** 2026-07-06 to 2026-07-31 | **Approved:** Chief Operating Officer, 2026-09-16 (presented to the audit committee the same day)

## 1. Overview and purpose
This BIA covers every business unit: the two communications centers, field operations (92 ambulances, 14 support vehicles, 13 stations), clinical services, the revenue cycle, the billing services line, and enterprise support functions. It rates 15 business processes and quantifies what an outage costs in money, operations, regulatory and contract exposure, and patient safety.

The results feed:
- the HIPAA contingency plan and its Applications and Data Criticality Analysis (45 CFR 164.308(a)(7), including (7)(ii)(E));
- the communications center continuity plan that the County A agreement requires (section 7 below);
- the FIPS 199 availability rating and contingency controls in the SSP (P02);
- impact ratings and exposure estimates in the risk register (P01);
- the recovery order in both incident runbooks (P08);
- the Availability and Processing Integrity criteria for the billing services SOC 2 readiness assessment (P09).

## 2. System and business description
The company is the exclusive 911 ambulance provider for County A (about 520,000 residents), the 911 provider for 2 zones in County B (about 210,000 residents), and an interfacility provider in 3 counties. It makes about 150,000 transports a year (about 410 a day). Dispatch and patient care run on the Dispatch and Patient Care Platform (DPCP) described in the SSP (P02): the CAD in the company's cloud landing zone, the SaaS ePCR, the identity provider, the hosted phone system, two communications centers, fleet mobile systems, 14 site networks, endpoints, and the MSSP-operated SIEM. The billing platform (SYS-03) serves both the company and the 4 billing services clients. See `../00_company-facts.md` sections 1, 3, 4, and 7.

## 3. Impact categories and values
Dollar values are scaled to about $100 million in annual revenue: about $153,000 a day from 911 transports, $112,000 a day from interfacility transports, and $8,200 a day in billing services fees. About $1.87 million of company collections (about $373,000 per business day) and about $1.0 million of client collections (about $200,000 per business day) move through the billing platform each week.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost (per day of outage) | More than $150,000 of lost revenue or extra cost, or more than $1 million of cash delayed | $30,000 to $150,000 | Less than $30,000 |
| Operations | Emergency or interfacility dispatch stops, or runs manually without unit tracking | One process, one center, or one county degraded | Staff slowed but working |
| Regulatory and contract | Reportable breach; state license action; county agreement default; breach of a client BAA | Missed documentation or reporting deadline (for example the 48-hour hospital record rule); county liquidated damages | Internal policy deviation |
| Patient safety | Plausible delay of an emergency response, loss of the life-safety radio channel, or loss of a heart attack pre-alert | Delayed but safe care (for example a late discharge transport) | None |
| Reputation | County, hospital, or billing client loses confidence; regional media | Facility or client complaints | Internal only |

**How loss at MTD was estimated.** Estimated loss is revenue not recovered plus extra cost (overtime, mutual-aid charges, back-entry labor, denials, service credits) over the MTD. The process owners supplied the assumptions: about 40% of the revenue on deferred interfacility trips is not recovered, back-entry of a paper patient care record takes about 20 minutes, and about 3% of trips documented on paper are later denied. For the billing processes (BP-08, BP-09) the loss is overtime, denials, service credits, and interest; the delayed cash is shown separately.

## 4. Process criticality and downtime (from `bia.csv`)
| Priority | Process | Unit | Criticality | MTD (h) | RTO (h) | RPO (h) | Estimated loss at MTD |
|---|---|---|---|---|---|---|---|
| 1 | BP-01 911 call intake, EMD, and dispatch (County A) | Communications | High | 2 | 1 | 0.25 | $15,000 |
| 2 | BP-02 911 dispatch for the County B zones | Communications | High | 2 | 1 | 0.25 | $5,000 |
| 3 | BP-03 Field communications, unit tracking, and station alerting | Field Operations | High | 2 | 1 | 24 | $5,000 |
| 4 | BP-04 Interfacility and non-emergency scheduling and dispatch | Communications | High | 8 | 4 | 1 | $20,000 |
| 5 | BP-06 12-lead ECG transmission and hospital pre-alerts | Clinical Services | Moderate | 8 | 4 | 24 | $1,000 |
| 6 | BP-07 System status management and unit posting | Communications | Moderate | 8 | 4 | 24 | $8,000 |
| 7 | BP-05 Patient care documentation and hospital record delivery | Clinical Services | Moderate | 24 | 8 | 1 | $14,000 |
| 8 | BP-11 Crew scheduling, timekeeping, and credential tracking | Field Operations | Moderate | 72 | 24 | 24 | $12,000 |
| 9 | BP-10 Medical necessity documentation intake | Revenue Cycle | Moderate | 48 | 24 | 24 | $8,000 |
| 10 | BP-08 Company billing and claims | Revenue Cycle | Moderate | 72 | 48 | 24 | $35,000 (plus about $1.1 million of cash delayed) |
| 11 | BP-09 Billing services for municipal clients | Billing Services | Moderate | 72 | 48 | 24 | $15,000 (plus about $600,000 of client cash delayed) |
| 12 | BP-14 Fleet maintenance and supply | Field Operations | Low | 120 | 72 | 24 | $5,000 |
| 13 | BP-12 Payroll and HR | Enterprise | Low | 120 | 72 | 24 | $10,000 |
| 14 | BP-15 Clinical quality review and protocol management | Clinical Services | Low | 168 | 120 | 24 | $1,000 |
| 15 | BP-13 County performance reporting and state data reporting | Enterprise | Low | 336 | 168 | 24 | $2,000 |

**Summary:** 4 High, 7 Moderate, and 4 Low processes (15 in total). The sum of estimated losses at each process's MTD is $156,000.

**Why the dollar figures are small for the dispatch processes.** An ambulance service does not stop earning when CAD fails: crews keep transporting on radio dispatch. The real cost of BP-01 to BP-03 is patient safety and county trust, so those rows are High on safety and operations even though their dollar loss at a 2-hour MTD is modest.

**Enterprise-wide scenario.** If CAD were down at both centers for 72 hours (for example, ransomware), the estimated cost is about $300,000: about $90,000 in overtime to double-staff both centers, about $40,000 in mutual-aid charges, about $134,000 of interfacility revenue not recovered, about $20,000 of back-entry labor, and a possible $10,000 of County A liquidated damages if monthly response-time compliance falls below 90%. Incident response, forensics, and breach notification costs come on top (see P01 R-001 and R-002).

**What drives the values:**
- **Emergency response** drives BP-01 to BP-03. Dispatch never fully stops, because telecommunicators switch to paper and radio at once. The 2-hour MTD is how long the Director of Communications and the Medical Director judge manual mode to be safe at current call volume before unit tracking errors and delays grow. After that, County A is asked to send overflow calls to the mutual-aid provider.
- **Revenue and facility relationships** drive BP-04. Interfacility work is about 42% of revenue.
- **A state records rule** drives BP-05. The receiving hospital must be able to get the patient care record on request within 48 hours of dispatch (Rule 64J-1.014, F.A.C.).
- **Cash flow and client trust**, not time, drive BP-08 and BP-09. Payers accept late claims within their filing limits, but the billing services clients judge the company by how quickly their claims go out.
- **Medicare documentation rules** drive BP-10 (42 CFR 410.40(e)).

## 5. Key findings
1. **The 1-hour RTO for CAD is unproven.** Only the CAD database restore has been tested (October 2025). The application servers, the integration engine, and the AVL gateway have never been rebuilt, and the integration engine and call recordings are not in write-once backups (gap 1; P01 R-001, R-003; P07 POAM-011 and POAM-012). Until those items close, assume a CAD rebuild after ransomware takes days, not hours. Manual mode must be able to run for days at both centers, with county help.
2. **The backup communications center does not protect against a CAD outage.** Station 10 is a good answer to losing the headquarters building (hurricane, fire), and the 2025 relocation drill worked. Both centers use the same cloud CAD, the same identity provider, and the same console image, so ransomware or a CAD failure hits both at once (P01 R-001, R-008). Action: a warm CAD standby in the backup region, isolated from production administration, by 2027-06-30, and a ransomware manual dispatch drill at both centers by 2026-11-30 (POAM-011).
3. **The ePCR vendor's stated recovery objectives meet BP-05.** Its SOC 2 system description states RTO 4 hours and RPO 15 minutes (P09 vendor review VEN-02). Offline tablets reduce data loss further.
4. **The billing platform is a single point of failure for two lines of business.** One vendor and one clearinghouse carry all company and client claims. A vendor breach would make the company both a covered entity with its own notices and a business associate owing notices to 4 clients (P01 R-013, R-047; P08 `ir-runbook-billing-vendor-breach.md`).
5. **County systems are outside the company's control.** The county P25 radio systems are the fallback for everything, and the CAD-to-CAD links are the only electronic path for County B calls. Neither link has written interconnection security terms or an agreed outage procedure (P01 R-010, R-011; POAM-008).
6. **Station alerting depends on CAD and on flat station networks.** Losing station alerting adds about a minute to turnout on every call. The P07 assessment found station alerting controllers reachable from crew Wi-Fi (P01 R-050).

## 6. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| County P25 radio systems | Radios in every vehicle and console positions at both centers (county-operated) | BP-01 to BP-04, BP-07 |
| SYS-01 CAD (in SYS-06 dispatch production account) | Incident entry, EMD, unit recommendation, AVL map, posting module, CAD-to-CAD links; 14-day point-in-time restore on the database | BP-01 to BP-04, BP-07, BP-13 |
| SYS-06 Cloud landing zone | Dispatch production (CAD, integration engine, recording archive, AVL gateway), data and reporting (reporting database, AI-004), backup account in a second region | BP-01 to BP-09, BP-13 |
| SYS-08 Hosted phone system | Transferred 911 callers, request lines, facility lines | BP-01, BP-04 |
| SYS-04 Identity provider | SSO and MFA for CAD consoles, ePCR, billing, email, cloud | All |
| SYS-07 and SYS-10 Communications centers and networks | 18 positions at headquarters, 6 at Station 10; UPS, generators, and two ISPs at both; SD-WAN to 13 stations | BP-01 to BP-04, BP-07 |
| SYS-09 Fleet mobile systems | 106 routers, 92 MDCs, 210 tablets, 92 cardiac monitors | BP-03, BP-05, BP-06 |
| Station alerting controllers (part of SYS-10) | Tones and bay doors at 13 stations, triggered by CAD | BP-03 |
| SYS-02 ePCR (SaaS) | Patient care records, hospital delivery, state export (vendor RTO 4 h, RPO 15 min) | BP-05, BP-13, BP-15 |
| SYS-03 Billing platform and clearinghouse (SaaS) | Company and client workspaces, claims, remittances | BP-08, BP-09, BP-10 |
| SYS-05 Productivity suite and cloud fax | PCS intake, email, files | BP-10, BP-11 |
| SYS-12 SIEM (MSSP) | Detection and validation of clean recovery | Recovery of all |
| SYS-13 Workforce systems | Scheduling, timekeeping, credentials, payroll, fleet maintenance | BP-11, BP-12, BP-14 |
| People | 44 telecommunicators and 8 supervisors, 420 field clinicians, IT and security team, MSSP, Medical Director | All |

## 7. County agreement linkage
The County A agreement and the County B zone agreement are contracts, not regulations, but they set the availability expectations the counties will judge the company by. The terms below are the fictional contract terms recorded in `../00_company-facts.md` section 7.

| Contract term (summarized) | What this BIA supplies | Status |
|---|---|---|
| County A: written communications center continuity plan, reviewed by the county EMS office each year | BP-01 to BP-04 MTD, RTO, and RPO; the recovery priorities in section 8; the two-center and manual-mode strategies | Plan exists (2023) but covers only building loss; update due 2026-12-15 (POAM-011) |
| County A: notice to the county PSAP of any dispatch system outage longer than 15 minutes | Detection and notice steps in P08 runbook section 3 | Procedure written in P08; not yet exercised |
| County A: 90th percentile response-time standards, with liquidated damages of $10,000 for each month that compliance falls below 90% | Loss estimates for BP-01, BP-03, and BP-07 | Included in the enterprise scenario |
| County A: notice of any security incident affecting county data within 24 hours; County B: within 72 hours | Notification steps in the P08 matrix | Added to P08 |
| County A and County B: annual joint exercise | Joint ransomware tabletop with both counties scheduled 2027-01-20 (POAM-014) | Planned |

## 8. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | County P25 radio and manual dispatch mode at both centers | Immediate | Paper incident cards, status boards, and run cards from the manual dispatch binder |
| 2 | SYS-08 phone lines and the County A transfer path | 30 min | County A PSAP voice-announces calls instead of transferring callers; request lines forwarded to supervisor cell phones |
| 3 | SYS-04 identity provider and break-glass accounts | 1 h | Two break-glass accounts per critical system, stored offline |
| 4 | SYS-10 networks and clean consoles at the primary center (then the backup center) | 1 h | 6 pre-imaged spare console laptops kept offline at each center |
| 5 | SYS-01 CAD servers and database (SYS-06) | 1 h target; unproven | Point-in-time database restore; rebuild servers from clean images; warm standby in the backup region (planned 2027-06-30) |
| 6 | Station alerting controllers | 1 h | Supervisors alert stations by phone and radio |
| 7 | SYS-09 vehicle routers and MDCs | 2 h | Radio position reports |
| 8 | SYS-06 integration engine (both county CAD-to-CAD links, ePCR push) | 4 h | County voice announcements; ePCR incidents created by crews |
| 9 | SYS-12 SIEM feeds and EDR console | 4 h | MSSP runs from its own platform; needed to confirm clean recovery |
| 10 | Cardiac monitor relay (vendor) | 4 h | Phone report to the emergency department |
| 11 | CAD posting module and AI-004 model | 4 h | Printed posting plans |
| 12 | SYS-02 ePCR | 8 h | Vendor-hosted; paper patient care records |
| 13 | SYS-13 scheduling and timekeeping | 24 h | Printed 2-week schedule |
| 14 | SYS-05 cloud fax and PCS intake | 24 h | Paper PCS at pickup |
| 15 | SYS-03 billing platform and clearinghouse (vendor) | 48 h | Queue claims; payer portals for high-dollar claims; daily client status calls |
| 16 | Payroll, fleet maintenance, and the reporting database | 72 h to 168 h | Repeat prior payroll; paper checklists; rebuild reports from restored data |
