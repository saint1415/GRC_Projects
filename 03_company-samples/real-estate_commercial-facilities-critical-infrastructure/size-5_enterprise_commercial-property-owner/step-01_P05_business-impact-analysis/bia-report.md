# Business Impact Analysis: Cris Santos Company | Commercial Facilities | Enterprise

**Organization:** Cris Santos Company, Inc. (publicly traded office and retail REIT; 140 properties in 6 states) | **Tier:** Enterprise (12,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, informed by NIST IR 8286D
**Prepared by:** GRC team with the process owners named in `bia.csv`, 2026-06-01 to 2026-07-15 | **Approved:** Chief Operating Officer and Chief Risk Officer, 2026-09-10 | **Reported to:** risk committee of the board, 2026-09-10

## 1. Overview and purpose
This enterprise-wide BIA identifies the business processes the company depends on, how long each can be down, how much data each can lose, and what each depends on, including third parties and the 19 properties acquired in November 2025. It covers all 140 operated properties (112 owned, 28 managed for third-party owners), the three Regional Security Operations Centers (RSOCs), the TRS service lines, and corporate functions.

No regulation requires this company to perform a BIA. It is done because the building systems are the product the company sells: tenants pay for space that is secure, cooled, lit, and accessible, and external clients rely on the TRS services. The results feed:
- the recovery goal in the CISA Cross-Sector Cybersecurity Performance Goals (CPG 6.A, execute the incident recovery plan, including operating in a degraded manner) and the backup goal (CPG 3.O);
- the FIPS 199 availability rating and contingency controls in the BAACS System Security Plan (P02);
- impact ratings in the enterprise risk register (P01), per NIST IR 8286D;
- the recovery order and the quantified impact used in the SEC materiality worksheet in the ransomware runbook (P08);
- the Availability criteria for the two SOC 2 service lines (P09).

**Results in one line:** 20 processes were analyzed; 6 are High criticality, 10 Moderate, and 4 Low. 4 processes need recovery within 4 hours. The dependency map (`dependency-map.csv`) lists 26 dependencies: 8 are single points of failure, 2 more are partial single points of failure, and 3 have never been tested.

## 2. System and business description
Cris Santos Company operates 140 properties (about 57 million sq ft) in Florida, Texas, Georgia, North Carolina, Arizona, and California, with about 5,600 tenants, about 212,000 credential holders, about 18,000 visitors per business day, and 12,000 employees. Revenue is about $4.8 billion a year (about $13.2 million per calendar day). Building operations run on the Building Automation and Access Control System (BAACS) described in the SSP (P02): three BAS platforms (Platform A at 64 towers and mixed-use properties, Platform B at 57 office parks and retail centers, Platform C at the 19 acquired properties), the cloud access control and video platform at 121 properties, a legacy PACS at the acquired properties, the property networks and their OT zones, and OT workloads in the cloud landing zone and two colocation data centers. Business operations run on SaaS (property management and ERP, identity, productivity, visitor management, payroll) and on the company-built tenant experience platform. See `../00_company-facts.md` sections 3, 4, and 7.

**Life-safety systems are outside this BIA.** Fire alarm, elevator, and emergency voice systems (SYS-13) run on separate vendor-maintained networks and do not depend on any system in scope. Door releases for emergency egress are hardwired to the fire alarm. The BAS reads fire alarm status only through read-only relay points. Keeping it that way is a design rule in the SSP (P02, PL-8).

## 3. Impact categories and values
Dollar thresholds are scaled to about $13.2 million of revenue per calendar day and to the materiality worksheet in P08 section 6. Rent accrues at about $12.2 million per day (office $7.1 million, retail $3.6 million, mixed-use $1.5 million). Rent is not lost on the first day of an outage. It is put at risk by lease abatement clauses (office leases on the 2023 template after 3 consecutive business days of untenantable premises, about 70% of office rent; retail leases after 5), and by tenant claims and non-renewals. Values are per 24 hours of outage unless stated.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $250,000 per day in extra cost or lost revenue, or more than $1 million of rent put at risk per day, or more than $100 million of cash delayed | $50,000 to $250,000 per day | Less than $50,000 per day |
| Operations | A region or a property group (all towers, all retail) cannot be occupied normally: no cooling, doors not controllable, no monitoring | One property, one platform at one site, or one service line degraded | Staff slowed but working |
| Regulatory and contractual | Breach notice to 500 or more residents in a state; missed SEC filing; loss of the ability to validate PCI DSS; a JV, lender, or SOC 2 client default notice | Missed lease notice, owner reporting deadline, or service level | Internal policy deviation |
| Occupant safety | Plausible harm to occupants (unsecured entrances, no emergency instructions, heat stress on occupied floors, dark parking fields) | Degraded but safe conditions | None |
| Reputation | National media, analyst or ratings action, loss of a major tenant at renewal, or JV partner or SL-2 client loss | Regional media; tenant or client complaints | Internal only |

**How the quantified impact was estimated.** The 24-hour figure is the extra cost of running the process by hand for one day plus lost non-rent revenue: overtime for engineers and security officers, portable cooling and equipment rentals, temporary credentials, lost ancillary revenue (events, after-hours HVAC, parking share), service credits, and finance charges. Rent at risk is shown separately because it becomes a loss only after the lease abatement thresholds. Process owners supplied staffing and rate assumptions (officer and engineer overtime at about $45 to $75 per hour; portable cooling at about $1,500 per tenant data room per day).

## 4. Process criticality and downtime (from `bia.csv`)
| Priority | Process | Criticality | MTD | RTO | RPO | Quantified impact per 24 h | Rent at risk per day after thresholds |
|---|---|---|---|---|---|---|---|
| 1 | BP-01 Physical access control and credentialing | High | 4 h | 2 h | 1 h | $650,000 | n/a |
| 2 | BP-03 Tenant emergency and service communications | High | 4 h | 2 h | 24 h | $150,000 | n/a |
| 3 | BP-02 RSOC monitoring, alarm response, and video | High | 8 h | 4 h | 24 h | $300,000 | n/a |
| 4 | BP-08 Tenant experience platform and mobile credentials | High | 8 h | 4 h | 1 h | $260,000 | n/a |
| 5 | BP-04 Environmental control on BAS Platform A | High | 12 h | 6 h | 4 h | $520,000 | $4,500,000 |
| 6 | BP-06 Building operations at the acquired portfolio | High | 12 h | 8 h | 24 h | $140,000 | $900,000 |
| 7 | BP-20 Corporate collaboration and communications | Moderate | 24 h | 8 h | 4 h | $400,000 | n/a |
| 8 | BP-07 Visitor management | Moderate | 24 h | 8 h | 24 h | $90,000 | n/a |
| 9 | BP-05 Environmental control on BAS Platform B | Moderate | 24 h | 12 h | 24 h | $230,000 | $2,600,000 |
| 10 | BP-17 Parking operations and revenue | Moderate | 24 h | 12 h | 4 h | $300,000 | n/a |
| 11 | BP-12 Treasury, accounts payable, and debt service | Moderate | 48 h | 24 h | 24 h | $60,000 | n/a |
| 12 | BP-09 Engineering work orders and tenant service requests | Moderate | 48 h | 24 h | 4 h | $70,000 | n/a |
| 13 | BP-10 Third-party property management services (SL-1) | Moderate | 72 h | 24 h | 4 h | $120,000 | n/a |
| 14 | BP-11 Rent billing, collections, and tenant accounting | Moderate | 72 h | 48 h | 4 h | $95,000 (plus up to $310 million of cash delayed) | n/a |
| 15 | BP-15 Payroll and HR | Moderate | 72 h | 48 h | 24 h | $50,000 | n/a |
| 16 | BP-13 Financial close, SEC reporting, and REIT compliance | Moderate | 120 h (48 h at quarter end) | 72 h | 24 h | $40,000 | n/a |
| 17 | BP-14 Leasing and lease administration | Low | 120 h | 72 h | 24 h | $35,000 | n/a |
| 18 | BP-16 Card payment acceptance | Low | 120 h | 72 h | 24 h | $15,000 | n/a |
| 19 | BP-18 Energy management and the smart building data platform | Low | 168 h | 120 h | 24 h | $45,000 | n/a |
| 20 | BP-19 Investor relations and JV partner and lender reporting | Low | 168 h | 120 h | 24 h | $20,000 | n/a |

**Summary:** 6 High, 10 Moderate, and 4 Low processes (20 in total). The 24-hour figures add up to about $3.6 million, but they are not additive in practice, because few incidents stop every process at once. The real exposure comes when building systems stay down past the lease abatement thresholds.

**Portfolio-wide scenario (used in P08 section 6).** If BAS Platforms A and B were both without supervisory control for 5 business days (for example, ransomware that reaches the Platform A clusters and the Platform B site servers), the estimated cost is about **$14.4 million**: Platform A manual operation about $2.6 million (5 x $520,000); Platform B manual operation about $1.15 million (5 x $230,000); office tower and mixed-use rent abatement for days 4 and 5, about $9.0 million (2 x $4.5 million); and office park abatement for days 4 and 5, about $1.6 million (2 x $0.8 million of the Platform B figure). Retail abatement would start on day 6. Incident response, legal, notification, and any SL-1 fee credits come on top. The figure is about 0.3% of annual revenue, so the materiality decision in P08 turns as much on qualitative factors (occupant safety, tenant and JV partner relationships, media coverage, regulatory inquiries) as on the dollar amount.

**What drives the values:**
- **Access control (BP-01) and tenant communications (BP-03)** have the shortest MTD. Door controllers cache credentials for up to 72 hours, so doors keep working, but no credential can be issued or revoked, and officers can staff about 900 main entrances for only one shift. During any outage or storm, occupants must receive instructions within hours.
- **The tenant experience platform (BP-08)** is High at this size because about 92,000 tenant employees use only mobile credentials, and SL-2 clients rely on the platform under service agreements.
- **Tower HVAC (BP-04)** can run for a while because field controllers keep their last programs, but manual rounds on 20 to 60 floors exhaust the engineering crews in about 12 hours, and tenant data rooms overheat in the southern and southwestern climates. Rent abatement after day 3 makes long outages expensive.
- **The acquired portfolio (BP-06)** is High because its systems cannot meet the RTO today (section 5) and its properties are in hot climates.
- **Regulation** tightens the financial close (BP-13) at quarter end, when SEC filing deadlines cut the MTD to 48 hours.
- **Contracts** set the SL-1 (BP-10) and SL-2 (BP-08) objectives, because external clients rely on them (P09).

## 5. Dependency mapping and third parties
The full map is in `dependency-map.csv`. Key findings:

1. **Platform vendor concentration (DEP-01).** One access control and video platform vendor runs PACS and video at 121 properties. Its SOC 2 system description states RTO 8 hours and RPO 1 hour for the cloud service, against a BIA RTO of 2 hours for credential administration. The 72-hour credential cache keeps doors working, so the gap is administration (issuing and revoking credentials, video review), not door operation. There is no alternate provider or exit plan. This is P01 R-005 and POA&M item POAM-011.
2. **The acquired portfolio (DEP-10, DEP-12, DEP-14).** The 19 Platform C site servers have no backups, Integrator C holds the only copies of controller programs, the legacy PACS servers back up to a storage device on the same flat network, and the legacy kiosks keep ID images beyond the standard. None of these has been tested. The 8-hour RTO for BP-06 is a target, not a capability (P01 R-003, R-011; POAM-003, POAM-008, POAM-019).
3. **Platform B recovery (DEP-09).** A sampled restore of a Platform B site server took 14 hours in 2026 against a 12-hour RTO, and Integrator B3 holds the only copies of controller programs for 9 properties (POAM-008).
4. **RSOC regional failover (BP-02).** Each RSOC can take over another region, but failover has been tested for 4 hours only, not a full shift (P01 R-012; POAM-013).
5. **Platform A and the clouds meet the BIA.** The Platform A clusters failed over between DC-1 and DC-2 in the 2026-05-16 disaster recovery test, and the tenant experience platform failed over between Cloud provider B regions in 2.5 hours on 2026-06-20.
6. **Messaging (DEP-23).** One SMS and messaging provider carries every push and text notice to occupants. A second provider is under evaluation (P01 R-051).

## 6. Resource requirements
| Resource / component | Description | Supports process |
|---|---|---|
| SYS-01 BAS Platform A | 4 supervisory clusters in DC-1 and DC-2, 110 engineering workstations, about 61,000 field controllers | BP-04, BP-18 |
| SYS-01 BAS Platform B | 57 site supervisory servers, 64 engineering workstations, about 17,500 field controllers | BP-05 |
| SYS-01 BAS Platform C and the legacy PACS | 19 site servers, 23 workstations, about 6,800 field controllers; 2 legacy PACS servers and about 640 door controllers | BP-06 |
| SYS-02 Access control platform | Cloud service, about 6,200 door controllers, 31,000 readers, 540 turnstile lanes | BP-01, BP-07, BP-08 |
| SYS-03 Video and the RSOCs | About 43,900 cameras and 658 NVRs; 3 RSOCs | BP-02 |
| SYS-04 Networks | SD-WAN at 140 properties; OT zones at 121; dual carriers at 98 | BP-01 to BP-09 |
| SYS-05 Identity platform | Single sign-on, MFA, PAM, identity governance | All |
| SYS-07 Property management and ERP | Leases, receivables, work orders, owner reporting | BP-09 to BP-14, BP-19 |
| SYS-08 Cloud provider A | Smart building data platform, OT remote access gateway, OT log pipeline, PAM vault, backup accounts with write-once retention | BP-04, BP-05, BP-10, BP-18, BP-19; RPO for Platform A and B |
| SYS-08 Cloud provider B | Tenant experience platform in two regions | BP-03, BP-08 |
| SYS-08 Colocation DC-1 and DC-2 | Platform A clusters, network core, offline backup copies | BP-04; recovery of all |
| SYS-09 Endpoints | 1,150 console PCs; engineering workstations and tablets; corporate laptops | All |
| SYS-10 P2PE terminals | 182 terminals at 64 offices | BP-16 |
| SYS-11 Visitor management | Enterprise SaaS at 64 properties; legacy kiosks at 6 acquired towers | BP-07 |
| SYS-12 HR and payroll | Payroll provider | BP-15 |
| SYS-14 Tenant experience platform | Mobile credentials, notices, service requests, virtual assistant | BP-03, BP-08, BP-09 |
| Third parties | As listed in `dependency-map.csv` (26 dependencies) | As listed |
| People and facilities | Chief engineers who can run plant equipment by hand; RSOC operators and security officers; Property Managers with printed tenant contact lists; the RSOC rooms in Florida, Texas, and California | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-05 identity platform and break-glass administrator accounts | 1 h | Two sealed break-glass accounts per critical administration plane; PAM vault in a second region |
| 2 | SYS-04 SD-WAN core, property firewalls, and OT zone rules | 2 h | Isolate OT zones; cellular failover at RSOCs and lobby desks |
| 3 | Security tooling (EDR console, SIEM, OT monitoring) for clean-room validation | 2 h | MSSP tooling |
| 4 | SYS-02 access control administration from clean console PCs | 2 h | Doors run on cached credentials; officers at entrances |
| 5 | Tenant notification channels (SYS-14 notices, email, phone tree) | 2 h | Printed contact lists; Property Managers' company phones |
| 6 | RSOC console PCs and SYS-03 video | 4 h | Another RSOC takes over; property desks use local NVR clients |
| 7 | SYS-14 tenant experience platform and mobile credentials | 4 h | Temporary cards at lobby desks |
| 8 | Clean engineering workstations and tablets | 4 h | Pre-imaged spare laptops at each regional engineering office |
| 9 | SYS-01 Platform A supervisory clusters | 6 h | Local hand control and manual rounds; standby cluster in the other data center |
| 10 | SYS-01 Platform C site servers and the legacy PACS | 8 h target (not achievable today) | Local hand control; rebuild by Integrator C (no backups today, POAM-008) |
| 11 | SYS-06 productivity suite and SYS-11 visitor management | 8 h | Out-of-band conferencing; paper visitor logs |
| 12 | SYS-01 Platform B site servers | 12 h | Local hand control; restore from the backup account |
| 13 | Parking interfaces (operator systems) | 12 h | Gates up |
| 14 | SYS-07 property management and ERP, treasury, and bank portals | 24 h | Clean laptops with dual approval |
| 15 | SYS-12 payroll | 48 h | Repeat the prior payroll |
| 16 | SYS-10 P2PE terminals | 72 h | Invoice customers |
| 17 | SYS-08 data platform, energy analytics, and data warehouse | 120 h | BAS on fixed schedules; reports from system exports |

The order (identity, network, security tooling, access control, tenant communications, monitoring, mobile credentials, clean endpoints, then the BAS) is used in the P08 runbook. The BAS RTOs are longer than the access control RTO because field controllers keep running and engineers can operate plant equipment by hand, while an uncontrolled entrance or an uninformed occupant is an immediate exposure.

## 8. Gaps carried to other deliverables
| Gap | Carried to |
|---|---|
| Platform vendor RTO 8 h against BIA RTO 2 h for credential administration; no exit plan | P01 R-005; P03 CPG 1.E; POAM-011 |
| Platform C without backups; Integrator C sole holder of programs; Platform B restore 14 h against 12 h | P01 R-011; P02 CP-9, CP-10; POAM-008 |
| RSOC regional failover tested for 4 hours only | P01 R-012; P02 CP-2; POAM-013 |
| Legacy kiosks keep ID images beyond the standard | P01 R-034; P03 (Cal. Civ. Code 1798.100(a)(3); Fla. Stat. 501.171(8)); POAM-019 |
| One messaging provider for occupant notices; stale printed contact lists | P01 R-051; P03 CPG 5.A; POAM-025 |
| Quantified building-outage impact missing from the materiality worksheet | P01 R-017; P08 section 6; POAM-012 |
