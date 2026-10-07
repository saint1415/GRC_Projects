# Business Impact Analysis: Cris Santos Company | Emergency Services | Enterprise

**Organization:** Cris Santos Company, Inc. (publicly traded private ambulance provider with a managed transportation division and EMS billing services; FL, GA, AL, SC, TN) | **Tier:** Enterprise (12,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, informed by NIST IR 8286D
**Prepared by:** GRC team with process owners, 2026-06-01 to 2026-07-15 | **Approved:** Chief Operating Officer and Chief Risk Officer, 2026-08-14 | **Reported to:** risk committee of the board, 2026-09-10

## 1. Overview and purpose
This enterprise-wide BIA identifies the business processes the company depends on, how long each can be down, how much data each can lose, and what each depends on, including third parties, county partners, and the acquired operations. It feeds:
- the HIPAA contingency plan, including the applications and data criticality analysis (45 CFR 164.308(a)(7)(ii)(E));
- the availability rating and recovery objectives in the Enterprise Dispatch and Patient Care Platform (EDPCP) System Security Plan (P02);
- impact ratings in the enterprise risk register (P01), per NIST IR 8286D;
- the recovery order in the CAD ransomware runbook (P08);
- the Availability criteria for the two SOC 2 service lines (P09).

**Results in one line:** 17 processes were analyzed; 9 are High criticality, 7 Moderate, and 1 Low. 7 processes need recovery within 4 hours, and 4 of those within 1 hour. The dependency map (`dependency-map.csv`) lists 26 dependencies: 12 are single points of failure, 4 more are partial single points of failure, and 4 have never been tested.

## 2. System and business description
Cris Santos Company runs 231 sites in Florida, Georgia, Alabama, South Carolina, and Tennessee: 210 stations and posts, 4 regional communications centers, 12 fleet maintenance hubs, 3 managed transportation contact centers, a billing center, and headquarters. It has 12,000 employees, about 1,450 ground ambulances, about 1.9 million transports a year, 911 service under 27 county and municipal agreements, and about $4.8 billion in annual revenue. The technology estate is described in `../00_company-facts.md` section 3: the enterprise CAD (SYS-01), the ePCR (SYS-02), the revenue cycle platform (SYS-03), the identity platform (SYS-04), a multi-cloud estate across two public cloud providers plus one colocation data center (SYS-05), the communications centers (SYS-06), fleet mobile systems (SYS-07), and the telephony and contact center platform (SYS-11). AQ-01, the Tennessee operation acquired in 2025-11, still dispatches from its own legacy CAD (SYS-12).

## 3. Impact categories and values
Dollar thresholds are scaled to about $13.2 million of revenue per calendar day and to the company's materiality framework (P08 section 6). Values are per 24 hours of outage unless stated.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $1 million per day, or more than $10 million cumulative | $100,000 to $1 million per day | Less than $100,000 per day |
| Operations | Dispatch stops or runs manually in more than one county, or a service line stops for all clients | One county, one communications center, or one client stops | Staff slowed but working |
| Regulatory | Reportable breach of 500 or more; county agreement default notice; state EMS license action; missed SEC filing | Missed contractual or documentation deadline; breach under 500 | Internal policy deviation |
| Safety | Plausible patient or public harm (delayed emergency response, missed recurring care such as dialysis) | Delayed but safe care | None |
| Reputation | National media, analyst or ratings action, or loss of a county agreement or service line client | Regional media; county or client complaints | Internal only |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO | Quantified impact per 24 h |
|---|---|---|---|---|---|
| BP-01 911 emergency call processing and dispatch (RCC-1 to RCC-3) | High | 2 h | 1 h | 5 min | $2.40M |
| BP-04 Field communications, AVL, and mobile data | High | 2 h | 1 h | 1 h | $0.50M |
| BP-13 Telephony and call recording | High | 2 h | 1 h | 24 h | $0.80M |
| BP-02 911 dispatch at AQ-01 (RCC-4, legacy CAD) | High | 2 h | 1 h | 5 min (actual 24 h) | $0.35M |
| BP-06 12-lead ECG transmission to hospitals | High | 4 h | 2 h | 24 h | $0.05M |
| BP-03 Interfacility and non-emergency transport scheduling and dispatch | High | 8 h | 4 h | 15 min | $1.20M |
| BP-11 Managed transportation trip intake and scheduling (SL-2) | High | 8 h | 4 h | 15 min | $0.90M |
| BP-05 Patient care documentation and hospital record delivery (ePCR) | Moderate | 24 h | 8 h | 1 h | $0.40M |
| BP-07 Crew scheduling and credential verification | Moderate | 24 h | 12 h | 4 h | $0.30M |
| BP-16 Fleet maintenance and medical supply | Moderate | 48 h | 24 h | 24 h | $0.30M |
| BP-09 Medical necessity documentation intake | Moderate | 48 h | 24 h | 24 h | $0.20M |
| BP-10 EMS billing services for public agencies (SL-1) | High | 72 h | 24 h | 4 h | $0.45M |
| BP-14 Payroll and timekeeping | Moderate | 72 h | 48 h | 24 h | $0.25M |
| BP-12 Network provider payments and encounter reporting (SL-2) | Moderate | 120 h | 72 h | 24 h | $0.30M |
| BP-08 Ambulance billing and claims (own transports) | High | 120 h | 72 h | 24 h | $5.75M |
| BP-15 Financial close and SEC reporting | Moderate | 120 h | 72 h | 24 h | $0.15M |
| BP-17 State and county reporting | Low | 336 h | 168 h | 24 h | $0.05M |

**What drives the values:**
- **Life safety** sets the shortest MTDs. A dispatch outage can delay an ambulance, and manual dispatch at full volume stays safe for about 2 hours. That is why BP-01, BP-02, BP-04, and BP-13 have a 2-hour MTD and a 1-hour RTO, and why the EDPCP is rated High for availability in P02.
- **Recurring care** drives managed transportation (BP-11). Members who miss dialysis or chemotherapy trips can be harmed within a day, and state broker contracts carry penalties.
- **Cash, not time,** drives claims (BP-08). Payers accept late claims within filing limits, so the MTD is 5 days, but each day of outage defers about $5.75 million of collections.
- **Contracts** set the objectives for the two service lines (BP-10 and BP-11), because external clients rely on them (P09), and the county agreements set response-time penalties for BP-01 and BP-02.
- **Regulation** tightens financial close (BP-15) during the quarter-end window, when the MTD drops to 48 hours because of SEC filing deadlines.

## 5. Dependency mapping and third parties
The full map is in `dependency-map.csv`. Key findings:

1. **Dispatch recovery time (DEP-01).** The enterprise CAD has a warm standby in a second cloud region, but the 2026-05-14 regional failover test took 1 hour 25 minutes against the 1-hour RTO. Most of the time went to manual DNS and interface cutover for the 26 PSAP CAD-to-CAD links. Center-to-center failover is proven for RCC-1 and RCC-2 but has never been tested for RCC-3. This is P01 risk R-005 and POA&M item POAM-011.
2. **Acquired operation (DEP-23, DEP-24).** AQ-01's legacy CAD backs up nightly, so its real RPO is 24 hours against a 5-minute target, and its restore has never been tested. The legacy network is flat and its site VPN reaches the enterprise integration hub, so a compromise at AQ-01 can spread to BP-01 and BP-03. This is P01 R-003 and R-007, POAM-007 and POAM-016.
3. **Fleet edge (DEP-07, DEP-08).** One router management service configures 1,290 enterprise vehicle routers, and 160 routers run end-of-support firmware. The 160 AQ-01 routers use a single carrier and are not enrolled in the management service (P01 R-006; POAM-009).
4. **Telephony (DEP-14).** The contact center platform's contract RTO is 2 hours, longer than the 1-hour BIA RTO for BP-13 (POAM-019).
5. **Third-party assurance (DEP-13, DEP-18).** The cardiac monitor relay vendor has provided no SOC report (POAM-015). About 1,400 managed transportation network providers reach member PHI through the broker portal; 38% have not completed the annual security attestation (P01 R-014; POAM-013).
6. **Outside the company's control (DEP-09, DEP-10, DEP-26).** County radio systems, PSAP CAD-to-CAD interfaces, and hospital and state receiving systems are single points of failure the company cannot remove. The workarounds are procedural and agreed in the county agreements.

## 6. Resource requirements
| Resource / component | Description | Supports process |
|---|---|---|
| SYS-01 Enterprise CAD | CAD, AVL, mobile data, CAD-to-CAD hub (Cloud provider A, two regions) | BP-01, BP-03, BP-04, BP-17 |
| SYS-02 ePCR | Vendor SaaS with offline tablets | BP-05, BP-08, BP-17 |
| SYS-03 Revenue cycle platform | Vendor SaaS with two clearinghouses | BP-08, BP-09, BP-10 |
| SYS-04 Identity platform | SSO, MFA, privileged access, identity governance | All |
| SYS-05 Cloud provider B workloads | Managed transportation platform, member app, AI services | BP-11, BP-12 |
| SYS-05 Colocation DC-1 | Network core, telephony gateways, offline backup copies | BP-13; recovery of all |
| SYS-06 Communications centers | Consoles, radio console gateways, UPS and generators | BP-01, BP-02 |
| SYS-07 Fleet mobile systems | Vehicle routers, MDCs, tablets, cardiac monitors | BP-04, BP-05, BP-06 |
| SYS-11 Telephony and contact center platform | Request lines, transferred 911 callers, contact centers | BP-03, BP-11, BP-13 |
| SYS-12 AQ-01 legacy estate | Legacy CAD and directory at RCC-4 | BP-02 |
| Immutable backups | Separate backup accounts with write-once retention; weekly copy to DC-1 | RPO for all Cloud A and B workloads |
| People | Dispatchers, field crews, contact center agents, revenue cycle staff, SOC, IT operations | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Manual dispatch mode and county P25 radio (already running when systems fail) | Immediate | Paper incident cards; PSAP voice announcement |
| 2 | SYS-04 identity platform and break-glass accounts | 1 h | Sealed break-glass accounts; secondary region |
| 3 | Network core, SD-WAN, DNS, and communications center connectivity | 1 h | Cellular failover; center-to-center failover |
| 4 | Telephony and call routing for request lines and transferred callers | 1 h | Backup carrier forwarding to supervisor phones |
| 5 | Security tooling (EDR console, SIEM) for clean-room validation | 1 h | MSSP tooling |
| 6 | Enterprise CAD (standby region) and CAD-to-CAD links | 1 h target (1 h 25 min measured) | Manual dispatch; PSAP voice relay |
| 7 | Vehicle routers, MDCs, and AVL | 1 h | Radio status reports |
| 8 | AQ-01 legacy CAD | 1 h target (restore never tested) | Manual dispatch at RCC-4 |
| 9 | 12-lead ECG relay | 2 h | Voice report to the hospital |
| 10 | Managed transportation platform | 4 h | Printed standing orders; phone assignment |
| 11 | ePCR synchronization and hospital delivery | 8 h | Paper patient care records; back-entry within 48 hours |
| 12 | Crew scheduling | 12 h | Printed schedules |
| 13 | Revenue cycle platform for SL-1 clients | 24 h | Queue claims; client status notices |
| 14 | ERP, payroll, fleet maintenance | 24 to 48 h | Repeat prior payroll; paper readiness checks |
| 15 | Clearinghouse connectivity and the own-claims backlog | 72 h | Secondary clearinghouse; payer portals |
| 16 | Data platform and state and county reporting | 168 h | Rebuild from restored data |

## 8. Gaps carried to other deliverables
| Gap | Carried to |
|---|---|
| CAD regional failover 1 h 25 min against a 1 h RTO; RCC-3 center failover never tested | P01 R-005; P02 CP-10; POAM-011 |
| AQ-01 legacy CAD with a 24 h actual RPO and no tested restore | P01 R-007; P03 G-023 and G-024; POAM-007 |
| AQ-01 site VPN reaches the enterprise integration hub | P01 R-003; POAM-016 |
| 160 vehicle routers on end-of-support firmware; AQ-01 routers unmanaged | P01 R-006; POAM-009 |
| Telephony contract RTO 2 h against a 1 h BIA RTO | P01 R-031; POAM-019 |
| Cardiac monitor relay vendor without a SOC report | P01 R-037; POAM-015 |
| Network providers without security attestations | P01 R-014; POAM-013 |
