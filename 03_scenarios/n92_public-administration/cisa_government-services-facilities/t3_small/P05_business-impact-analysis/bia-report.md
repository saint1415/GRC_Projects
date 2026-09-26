# Business Impact Analysis: Cris Santos Company | Government Services and Facilities | Small

**Organization:** Cris Santos Company, LLC (facilities support contractor operating government buildings) | **Tier:** Small (60 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** IT Manager (Information Security Officer) with the Director of Operations, Controls Engineering Manager, Security Systems Supervisor, and Site Managers | **Approved:** Chief Operating Officer, 2026-08-31

## 1. Overview and purpose
This BIA identifies which business processes the company depends on, how long each can be down, and how much data it can lose. It supports:
- the contingency plan the state contract requires (SP 800-53 CP-2, due 2026-12-31);
- the manual-mode (building recovery) procedures for state and county buildings, modeled on the procedures GSA requires at the federal building (BTTRG v3.0, section 1.6.2);
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08).

## 2. System and business description
The company runs three contracts from its headquarters and Remote Operations Center (ROC): a GSA federal office building, a state agency office complex, and a county government center with 4 service centers. It has 60 employees. For the state and county it operates the building automation and access control layers on the Facility Operations Technology Platform (FOTP). For GSA, company staff operate GSA's own BAS through GSA's virtual desktop. See `../scenario-facts.md` sections 1 and 3.

**A key property of building systems:** field controllers keep running their last programs and schedules, and door controllers cache credentials for up to 72 hours. A loss of the company's platform does not stop the buildings at once. What stops is *change* (new badges, revocations, schedule changes) and *visibility* (alarms). That is why the MTDs below are longer than a typical office IT system, except where people's safety or security depends on an alarm or a revocation.

## 3. Impact categories and values
Dollar values are scaled to $28.2 million in annual revenue, about $113,000 per business day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $250,000 (contract penalties, emergency labor, or lost payment) | $50,000 to $250,000 | Less than $50,000 |
| Operations | A customer building closes or cannot be secured | One site or one service degraded | Staff slowed but working |
| Contract and regulatory | Contract default notice, missed legal notice clock, or loss of eligibility (for example FAR 52.204-25) | Missed contract report or SLA credit | Internal deviation |
| Safety and physical security | People harmed or a government building left unsecured | Delayed response to a security or environmental alarm | None |
| Reputation | Local media or loss of a government customer | Customer complaint or corrective action request | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Remote alarm monitoring and response | High | 8 h | 4 h | 24 h |
| BP-02 Access control administration | High | 24 h | 8 h | 1 h |
| BP-04 Federal building operations and maintenance | High | 24 h | 8 h | 24 h |
| BP-03 Building automation supervision (state and county) | Moderate | 24 h | 12 h | 24 h |
| BP-05 Work order and preventive maintenance | Moderate | 72 h | 24 h | 24 h |
| BP-06 Video surveillance support and exports | Moderate | 72 h | 24 h | 24 h |
| BP-07 Controller program engineering and changes | Moderate | 72 h | 48 h | 24 h |
| BP-08 Contract reporting and invoicing | Moderate | 120 h | 72 h | 24 h |
| BP-09 Payroll and HR | Low | 120 h | 72 h | 24 h |

**What drives the values:**
- **Safety and security drive BP-01 and BP-02.** Freeze and flood alarms and forced-door alarms need a response within hours. A county employee fired in the morning must not keep building access for days.
- **BP-02 has a 1-hour RPO** because lost badge revocations are a security gap, not only lost data.
- **BP-03 tolerates a day** because controllers run locally, but not longer in a Florida summer or when events need schedule changes.
- **BP-04 depends on GSA, not the FOTP.** GSA's BSN, virtual desktop, and PIV infrastructure are GSA's to recover. The company's part is people with valid PIV cards and the tested building recovery procedures.

**Key findings:**
1. **The 48-hour RTO for BP-07 is unproven.** Controller programs are only on technicians' laptops; there is no central copy and no restore test (P01 R-007).
2. **The 12-hour RTO for BP-03 is unproven.** The supervisory server backups are in the same cloud account as production and have never been restored (R-006).
3. **State and county buildings have no manual-mode procedures.** The federal building does, because GSA requires them (R-008).
4. **The access control vendor's recovery commitments must meet BP-02** (RTO 8 h, RPO 1 h). The vendor's SOC 2 report (P09) states an RTO of 4 hours and an RPO of 15 minutes, which meets the BIA.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-06 Identity provider | Sign-in and MFA for all company systems and administrator portals | All |
| SYS-03 Jump host and client VPN | Remote access path to site OT | BP-01, BP-03, BP-07 |
| SYS-02 Access control and video tenants | Cardholders, door schedules, alarms, video | BP-01, BP-02, BP-06 |
| SYS-01 BAS supervisory platform | Schedules, setpoints, alarms, trends | BP-01, BP-03, BP-07 |
| SYS-04 File storage and backup vault | Drawings, controller programs, backups | BP-03, BP-07 |
| SYS-05 Site edge firewalls and ISPs | Connectivity to 6 sites | BP-01, BP-03 |
| SYS-08 CMMS | Work orders, asset lists | BP-04, BP-05, BP-08 |
| SYS-10 GSA virtual desktop and PIV cards | Access to GSA's BAS | BP-04 |
| People | ROC operators, BAS and security systems technicians, 16 PIV-credentialed staff | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-06 Identity provider and break-glass accounts | 1 h | Two break-glass administrator accounts stored offline (to be created) |
| 2 | ROC connectivity and SYS-03 jump host | 2 h | ROC runs from laptops over cellular; jump host rebuilt from image |
| 3 | SYS-02 administrator access (vendor-hosted) | 4 h | Customer security staff use printed emergency revoke lists |
| 4 | SYS-01 BAS supervisory server | 12 h | Manual-mode procedures; changes at the controller |
| 5 | SYS-08 CMMS (vendor-hosted) | 24 h | Paper work orders |
| 6 | NVR exports and video management | 24 h | Export at the NVR on site |
| 7 | Controller program repository | 48 h | Laptop copies; vendor commissioning files |
| 8 | Invoicing and reporting | 72 h | Accounting records |
| 9 | Payroll | 72 h | Repeat prior payroll |

GSA access (SYS-10) is outside this list. GSA recovers its own systems; the company keeps PIV holders available and runs the building recovery procedures.
