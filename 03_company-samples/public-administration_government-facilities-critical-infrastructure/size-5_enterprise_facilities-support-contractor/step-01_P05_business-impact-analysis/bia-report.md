# Business Impact Analysis: Cris Santos Company | Government Services and Facilities | Enterprise

**Organization:** Cris Santos Company, Inc. (publicly traded facilities support contractor operating government buildings) | **Tier:** Enterprise (12,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, informed by NIST IR 8286D
**Prepared by:** GRC team with process owners, 2026-06-01 to 2026-07-15 | **Approved:** Chief Operating Officer and Chief Risk Officer, 2026-08-14 | **Reported to:** risk committee of the board, 2026-09-10

## 1. Overview and purpose
This enterprise-wide BIA identifies the business processes the company depends on, how long each can be down, how much data each can lose, and what each depends on, including third parties, customers' own systems, and the two acquired businesses (AQ-1 and AQ-2). It feeds:
- the contingency plans the state cybersecurity exhibits require (SP 800-53 CP-2) for the Integrated Building Operations Platform (IBOP);
- the manual-mode (building recovery) procedures for state, local, and education buildings, modeled on the procedures GSA requires at federal buildings (BTTRG v3.0, section 1.6.2);
- the availability rating and recovery objectives in the IBOP System Security Plan (P02);
- impact ratings in the enterprise risk register (P01), per NIST IR 8286D;
- the recovery order in the intrusion runbook (P08);
- the Availability criteria for the two SOC 2 service lines (P09).

**Results in one line:** 18 processes were analyzed; 7 are High criticality, 10 Moderate, and 1 Low. 4 processes need recovery within 4 hours. The dependency map (`dependency-map.csv`) lists 24 dependencies, 12 of them single points of failure and 5 never tested.

## 2. System and business description
Cris Santos Company operates and maintains about 2,134 government buildings in eight states and the District of Columbia: 64 GSA-controlled federal buildings, about 1,050 state and local buildings (including 41 courthouses and 27 public safety buildings), and about 1,020 university and school buildings. It has 12,000 employees and about $4.8 billion in annual revenue across four segments (Federal Facilities, State and Local Government, Education Facilities, Security Integration). The technology estate is described in `../00_company-facts.md` section 3: the IBOP (SYS-01), an identity platform (SYS-02), a multi-cloud estate plus two colocation data centers (SYS-03), OT remote access and about 1,480 site edge gateways (SYS-04), the network, three ROCs, and about 15,500 endpoints (SYS-05), ERP and payroll (SYS-06), the Facility Services Portal (SYS-07), and GSA-furnished access for federal work (SYS-08).

**A key property of building systems:** field controllers keep running their last programs and schedules, and door controllers cache credentials for up to 72 hours. Losing the IBOP does not stop a building at once. What stops is *change* (badge revocations, schedule changes, setpoint changes) and *visibility* (alarms). That is why alarm monitoring and access administration have the shortest objectives, while BAS supervision tolerates about a day.

## 3. Impact categories and values
Dollar thresholds are scaled to about $13.2 million of revenue per calendar day and to the company's materiality framework (P08 section 6). Values are per 24 hours of outage unless stated.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $1 million per day, or more than $10 million cumulative | $100,000 to $1 million per day | Less than $100,000 per day |
| Operations | Alarm monitoring or access administration stops for a whole ROC region, or more than 50 buildings cannot be secured or conditioned | One customer, one state, or up to 50 buildings degraded | Staff slowed but working |
| Contract and regulatory | Contract default or cure notice; missed legal notice clock (customer 24-hour notice, FAR 52.204-25 one business day); missed SEC filing | Missed contract report or SLA credit | Internal deviation |
| Safety and physical security | People harmed, or a government building left unsecured (doors unlocked, life-safety supervision lost) | Delayed response to a security or environmental alarm | None |
| Reputation | National media, analyst or ratings action, or loss of a state or federal customer | Regional media; customer corrective action request | Internal only |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO | Quantified impact per 24 h |
|---|---|---|---|---|---|
| BP-01 ROC alarm monitoring and dispatch | High | 4 h | 2 h | 15 min | $1.90M |
| BP-02 Access control administration | High | 8 h | 4 h | 15 min | $1.10M |
| BP-09 Customer service desk, on-call telephony, and emergency call handling | High | 8 h | 4 h | 24 h | $0.45M |
| BP-03 Building automation supervision and remote operation | High | 24 h | 8 h | 4 h | $0.90M |
| BP-04 Federal building operations and maintenance | High | 24 h | 8 h | 24 h | $0.60M |
| BP-05 Field service dispatch and work order management (FSP) | High | 24 h | 8 h | 1 h | $2.40M |
| BP-16 Corporate email, chat, and file collaboration | High | 24 h | 4 h | 1 h | $0.80M |
| BP-15 CUI and building document management | Moderate | 72 h | 24 h | 4 h | $0.12M |
| BP-06 Video surveillance management and evidence exports | Moderate | 48 h | 24 h | 24 h | $0.25M |
| BP-18 Remote service for the AQ-1 installed base | Moderate | 24 h | 12 h | 24 h | $0.18M |
| BP-07 Controller program and door schedule engineering | Moderate | 72 h | 48 h | 24 h | $0.30M |
| BP-13 Workforce onboarding, background checks, credentialing, and PIV sponsorship | Moderate | 72 h | 48 h | 24 h | $0.20M |
| BP-14 Procurement, parts supply, and supplier screening | Moderate | 72 h | 48 h | 24 h | $0.30M |
| BP-10 Payroll and timekeeping | Moderate | 72 h | 48 h | 24 h | $0.35M |
| BP-12 Financial close and SEC reporting | Moderate | 120 h | 72 h | 24 h | $0.15M |
| BP-11 Contract billing, invoicing, and project accounting | Moderate | 120 h | 72 h | 24 h | $13.20M (deferred) |
| BP-08 Security systems integration projects (SI segment) | Moderate | 120 h | 72 h | 24 h | $0.50M |
| BP-17 Building analytics, energy reporting, and fault detection | Low | 168 h | 72 h | 24 h | $0.06M |

**What drives the values:**
- **Physical safety and security** set the shortest MTDs. Freeze, flood, and forced-door alarms at 1,420 buildings need a response within hours (BP-01), and a revoked badge must reach the door before the person returns (BP-02). This is why BP-02 has a 15-minute RPO: a lost revocation is a security gap, not only lost data.
- **Contracts** set most other values. Response-time SLAs and performance deductions are computed from FSP timestamps (BP-05), and the state and county contracts require 24-hour incident notice, which depends on email and telephony (BP-09, BP-16).
- **Cash, not time,** drives billing (BP-11). Government customers accept late invoices, so the MTD is 5 days, but each day defers about $13.2 million of billing.
- **Regulation** tightens financial close (BP-12) to 48 hours in the quarter-end window because of SEC filing deadlines, and keeps CUI in controlled environments even during an outage (BP-15; 32 CFR 2002.14(c)).
- **GSA, not the company,** recovers federal building systems (BP-04). The company's part is people with valid PIV cards and exercised building recovery procedures.

## 5. Dependency mapping and third parties
The full map is in `dependency-map.csv`. Key findings:

1. **IBOP recovery (DEP-01).** The 2026-05-09 regional failover test restored alarm routing in 1.6 hours (RTO 2 hours, met) but PACS administration in 7.5 hours against its 4-hour RTO. The PACS database restore and tenant re-keying were manual. This is P01 risk R-009 and a POA&M item in P07.
2. **AQ-1 legacy paths (DEP-11, DEP-12).** 142 AQ-1 sites are reached only through AQ-1's legacy always-on remote-support tool, and 620 AQ-1 staff sign in through a legacy directory. Both are single points of failure that have never been tested, and both are the entry point in the P08 scenario. Retirement is due 2027-01-31.
3. **Controller program repository (BP-07).** Known-good copies of controller programs and door schedules are the only safe way to restore a tampered controller. The repository has never been restored at full scale, and AQ-2 programs are not yet in it (DEP-22).
4. **Site circuits (DEP-04, DEP-13).** 38% of buildings have no cellular backup. During a circuit outage the alarms stay local, so the ROC is blind at that building until a technician arrives.
5. **ROC absorption (DEP-21).** Any ROC can take another's load, but the 2026-04-22 exercise proved only 6 hours. A 24-hour absorption needs cross-trained staff and badge rights at the receiving ROC.
6. **GSA dependency (DEP-10).** The company cannot remove its dependency on GSA's BSN and virtual desktop. 2 of 11 contracts have not exercised the building recovery procedures in 2026.
7. **Notification service (DEP-20).** Automated ROC paging and FSP alerts use one SaaS provider with no second provider under contract.

## 6. Resource requirements
| Resource / component | Description | Supports process |
|---|---|---|
| SYS-01 IBOP | Alarm routing, PACS, video management, BAS supervisory servers, program repository | BP-01, BP-02, BP-03, BP-06, BP-07 |
| SYS-02 Identity platform | SSO, MFA, PAM, identity governance | All |
| SYS-03 Cloud provider A | IBOP primary and secondary regions | BP-01 to BP-03, BP-06, BP-07 |
| SYS-03 Cloud provider B | FSP, data platform, AI services | BP-05, BP-17 |
| SYS-03 Colocation DC-1 and DC-2 | Network core, video evidence archive, offline backup copies | BP-06; recovery of all |
| SYS-04 OT remote access gateway and site edge gateways | The approved remote path to customer OT networks | BP-01 to BP-03, BP-07 |
| SYS-05 Network, ROCs, endpoints | SD-WAN, ROC consoles, rugged tablets, laptops | All |
| SYS-06 ERP, payroll, project accounting | Finance, payroll, procurement, billing | BP-08, BP-10 to BP-14 |
| SYS-07 FSP | Work orders, service requests, SLA timestamps | BP-04, BP-05, BP-11 |
| SYS-08 GSA-furnished access | GSA BAS on the BSN through GSA's virtual desktop and PIV | BP-04 |
| SYS-09 Collaboration suite and CUI enclave | Email, chat, files, CUI drawings | BP-15, BP-16 |
| Immutable backups | Separate backup accounts with write-once retention; weekly offline copy to DC-2 | RPO for all cloud workloads |
| People | 210 ROC operators, 1,150 controls and security technicians, 3,700 PIV holders, field staff | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-02 identity platform and break-glass accounts | 1 h | Sealed break-glass accounts; secondary region |
| 2 | ROC connectivity, SD-WAN, and carriers | 2 h | Second carrier; cellular failover |
| 3 | Security tooling (EDR, SIEM, OT network monitoring) | 2 h | MSSP tooling |
| 4 | IBOP alarm routing and ROC consoles | 2 h | Fail over to another ROC; local panels watched by customer staff |
| 5 | IBOP PACS administration | 4 h | Printed emergency revoke lists; cached credentials at controllers |
| 6 | Contact center telephony and service desks | 4 h | Carrier forwarding to mobile phones |
| 7 | Corporate email and chat | 4 h | Out-of-band phone trees; FSP SMS |
| 8 | OT remote access gateway | 4 h | On-site work; break-glass gateway in the second region |
| 9 | IBOP BAS supervisory servers | 8 h | Manual-mode procedures; changes at the controller |
| 10 | FSP | 8 h | Phone and email dispatch; paper work orders |
| 11 | CUI enclave and document libraries | 24 h | Printed drawing sets under the site CUI custodian |
| 12 | Video management and evidence archive | 24 h | Export at the site recording server |
| 13 | Controller program repository | 48 h | Vendor commissioning files |
| 14 | ERP, payroll, HR, and procurement | 48 h | Repeat prior payroll; emergency purchase cards |
| 15 | Project accounting and billing | 72 h | Manual invoices for the 40 largest contracts |
| 16 | Data platform and analytics | 72 h | Monthly reports from IBOP trend exports |

GSA's systems (SYS-08) are outside this list. GSA recovers its own systems; the company keeps PIV holders available and runs the building recovery procedures.

## 8. Gaps carried to other deliverables
| Gap | Carried to |
|---|---|
| IBOP PACS administration recovered in 7.5 h against a 4 h RTO | P01 R-009; P02 CP-10; P07 POA&M |
| AQ-1 legacy remote-support tool and directory (never tested; entry point in P08) | P01 R-002 and R-003; P07 POA&M |
| Controller program repository never restored at full scale; AQ-2 programs missing | P01 R-010; P02 CP-9 |
| 38% of buildings without cellular backup | P01 R-012 |
| ROC absorption proven for only 6 hours | P01 R-013 |
| 2 GSA contracts without a 2026 building recovery exercise | P01 R-047; P03 BTTRG section 1.6.2 |
| No second notification provider | P01 R-014 |
