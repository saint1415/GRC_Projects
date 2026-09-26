# Business Impact Analysis: Cris Santos Company | Emergency Services | Small

**Organization:** Cris Santos Company, LLC (licensed private ambulance service) | **Tier:** Small (60 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** IT Manager (Security Officer) with the Communications Center Supervisor, Operations Manager, and Billing and Compliance Manager | **Approved:** COO, 2026-09-04

## 1. Overview and purpose
This BIA identifies which business processes the company depends on, how long each can be down, and how much data it can lose. It supports:
- the contingency plan required by the HIPAA Security Rule (45 CFR 164.308(a)(7)), including the Applications and Data Criticality Analysis (164.308(a)(7)(ii)(E));
- the High availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08).

## 2. System and business description
The company runs a 24x7 dispatch center at headquarters, 9 ambulances from two stations, and about 44 transports a day. Dispatch and patient care run on the Dispatch and Patient Care Platform (DPCP): a CAD run in the company's cloud tenant, a SaaS ePCR, an identity provider, a hosted phone system, fleet mobile systems, site networks, and endpoints. The county operates the 911 PSAP and the P25 radio system that the company's crews and dispatchers use. See `../scenario-facts.md` sections 3-4.

## 3. Impact categories and values
Dollar values are scaled to $13.5 million in annual revenue, about $37,000 per day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $110,000 (about 3 days of revenue) | $25,000 to $110,000 | Less than $25,000 |
| Operations | Emergency or interfacility dispatch stops or runs manually without unit tracking | One process or one station degraded | Staff slowed but working |
| Regulatory | Reportable breach; state license action; county agreement default | Missed documentation or reporting deadline (for example, the 48-hour hospital record rule) | Internal policy deviation |
| Safety | Plausible delay of an emergency response or loss of the life-safety radio channel | Delayed but safe care (for example, a late discharge transport) | None |
| Reputation | County or hospital partners lose confidence; regional media | Facility complaints | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 911 emergency call intake and dispatch | High | 2 h | 1 h | 15 min |
| BP-02 Interfacility and non-emergency transport dispatch | High | 8 h | 4 h | 1 h |
| BP-03 Patient care documentation and hospital record delivery | Moderate | 24 h | 8 h | 1 h |
| BP-04 Field communications and vehicle tracking | High | 2 h | 1 h | 24 h |
| BP-05 Billing and claims | Moderate | 72 h | 48 h | 24 h |
| BP-06 Medical necessity documentation intake | Moderate | 48 h | 24 h | 24 h |
| BP-07 Crew scheduling, payroll, and credential tracking | Low | 120 h | 72 h | 24 h |
| BP-08 State and county reporting | Low | 336 h | 168 h | 24 h |

**What drives the values:**
- **Emergency response drives BP-01 and BP-04.** Dispatch never fully stops: dispatchers switch to paper and radio at once. The 2-hour MTD is how long the Communications Center Supervisor judges manual mode to be safe before unit tracking errors and delays grow. After that, the county PSAP is asked to send new calls to the mutual-aid provider.
- **Revenue drives BP-02.** Interfacility work is about 70% of revenue, and facilities move to competitors after repeated delays.
- **A state records rule drives BP-03.** The receiving hospital must be able to get the patient care record on request within 48 hours of dispatch (Rule 64J-1.014, F.A.C.). Tablets work offline, so short ePCR outages rarely lose data.
- **Medicare documentation rules drive BP-06.** Certification statements must be on file for non-emergency transports (42 CFR 410.40(e)).

**Key findings:**
- **The 1-hour RTO for CAD is unproven.** The CAD database has point-in-time restore, but no one has ever restored it or rebuilt the CAD server, and the backups share the production account (P01 R-002). Until POAM-004 and POAM-005 close, assume a CAD rebuild after ransomware takes days. Manual mode must therefore be drilled and able to run for days, not hours, with county help.
- **The ePCR vendor's stated recovery objectives (RTO 4 h, RPO 15 min) meet BP-03** (P09 vendor report review).
- **The radio is outside the company's control.** The county P25 system is the fallback for everything. The company should confirm with the county how it is notified of radio outages.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| County P25 radio system | Radios in every ambulance and control stations at dispatch | BP-01, BP-02, BP-04 |
| SYS-01 CAD (on SYS-06) | Incident entry, unit recommendation, AVL map, CAD-to-CAD link | BP-01, BP-02, BP-04, BP-08 |
| SYS-06 Cloud tenant | CAD server and database (7-day point-in-time restore), integration engine, recording archive, backup vault | BP-01 to BP-05 |
| SYS-08 Hosted phone system | Request lines and transferred callers | BP-01, BP-02 |
| SYS-04 Identity provider | Single sign-on and MFA for ePCR, billing, email | BP-03, BP-05, BP-06 |
| SYS-07 and SYS-10 Dispatch center and networks | Consoles, UPS and generator, two ISPs at headquarters | BP-01, BP-02 |
| SYS-09 Fleet mobile systems | Routers, MDCs, tablets | BP-03, BP-04 |
| SYS-02 ePCR (SaaS) | Patient care records, hospital delivery, state data export (vendor backups, RPO 15 min) | BP-03, BP-08 |
| SYS-03 Billing and clearinghouse | Claims | BP-05, BP-06 |
| People | Dispatchers, crews, supervisors, IT Manager, MSP | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | County P25 radio and manual dispatch mode | Immediate | Paper incident cards and status board from the manual dispatch binder |
| 2 | SYS-08 Phone lines | 30 min | Forward request lines to supervisor cell phones |
| 3 | SYS-04 Identity provider and break-glass accounts | 1 h | Two break-glass admin accounts stored offline (to be created; P03 164.312(a)(2)(ii)) |
| 4 | SYS-10 Headquarters network and clean dispatch consoles | 1 h | 3 pre-imaged spare laptops for dispatch (to be purchased); cellular hotspot |
| 5 | SYS-01 CAD server and database (SYS-06) | 1 h target; unproven | Restore database to a point in time; rebuild server from a clean image; manual mode until then |
| 6 | SYS-09 Vehicle routers and MDCs | 2 h | Radio position reports |
| 7 | SYS-06 Integration engine (county link, ePCR push) | 4 h | County PSAP voice transfers and radio announcements |
| 8 | SYS-02 ePCR | 8 h | Vendor-hosted; paper patient care records |
| 9 | SYS-03 Billing | 48 h | Queue trips |
| 10 | Scheduling and payroll SaaS | 72 h | Printed schedule; repeat prior payroll |
