# Business Impact Analysis: Cris Santos Company | Commercial Facilities | Mid-Market

**Organization:** Cris Santos Company, Inc. (PE-backed commercial office and retail property owner-operator) | **Tier:** Mid-Market (600 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Security Manager and GRC Analyst with the vCISO, the process owners named in `bia.csv`, and the Vice President of Engineering | **Fieldwork:** 2026-07-06 to 2026-07-31 | **Approved:** Chief Operating Officer, 2026-09-15 (presented to the audit committee the same day)

## 1. Overview and purpose
This BIA covers every business unit: the office portfolio (Towers 1-4, Parks 1-2), the retail portfolio (Retail 1-6), the 2 mixed-use properties, security operations (including the Security Command Center), engineering, parking, and corporate functions (finance, leasing, human resources). It rates 16 business processes and quantifies what an outage costs in money, operations, regulatory and contractual exposure, and occupant safety.

No regulation requires this company to perform a BIA. It is done because the building systems are the product the company sells: tenants pay for space that is secure, cooled, lit, and accessible. The results feed:
- the recovery goal in the CISA Cross-Sector Cybersecurity Performance Goals (CPG 6.A, execute the incident recovery plan, including operating in a degraded manner) and the backup goal (CPG 3.O);
- the FIPS 199 availability rating and contingency controls in the SSP (P02);
- impact ratings and exposure estimates in the risk register (P01);
- the recovery order in both incident runbooks (P08);
- the Availability criteria in the SOC 2 readiness assessment for the joint venture (P09).

## 2. System and business description
The company owns and operates 14 Florida properties (about 4.2 million sq ft) with about 420 tenants, about 14,500 credential holders, and 600 employees. Building operations run on the Building Automation and Access Control System (BAACS) described in the SSP (P02): two building automation platforms (Platform A at the towers and mixed-use properties, Platform B at the retail centers and office parks), the cloud-hosted access control and video platform with on-premises door controllers and recorders, the property networks and their OT segments, and supporting workloads in the cloud landing zone. Business operations run on SaaS (property management and accounting, identity, productivity, visitor management, the tenant experience app, payroll). See `../00_company-facts.md` sections 3, 4, and 7.

**Life-safety systems are outside this BIA.** Fire alarm, elevator, and emergency voice systems (SYS-13) run on separate vendor-maintained networks and do not depend on any system in scope. Door releases for emergency egress are hardwired to the fire alarm. The BAS reads fire alarm status only through read-only relay points. Keeping it that way is a design rule in the SSP (P02, PL-8).

## 3. Impact categories and values
Dollar values are scaled to about $100 million in annual revenue. Rent accrues daily: about $159,000 per day for office, $82,000 for retail, and $25,000 for mixed-use. Rent is not lost on the first day of an outage. It is put at risk by lease abatement clauses (office leases on the 2024 template after 3 consecutive business days of untenantable premises, retail leases after 5), and by tenant claims and non-renewals.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost (per day of outage) | More than $150,000 in extra cost or rent put at risk, or more than $1 million of cash delayed | $30,000 to $150,000 | Less than $30,000 |
| Operations | A property group (all towers, all retail) cannot be occupied normally: no cooling, doors not controllable, no monitoring | One property or one building system degraded | Staff slowed but working |
| Regulatory and contractual | Breach notice under Fla. Stat. 501.171, loss of the ability to validate PCI DSS, or a JV or lender default notice | Missed lease notice, JV reporting deadline, or service level | Internal policy deviation |
| Occupant safety | Plausible harm to occupants (unsecured entrances, no emergency instructions, heat stress in occupied floors) | Degraded but safe conditions | None |
| Reputation | Regional media coverage, loss of a major tenant at renewal, or a JV partner complaint | Tenant complaints | Internal only |

**How loss at MTD was estimated.** Estimated loss is the extra cost of running the process by hand for the length of the MTD: overtime for engineers and security officers, portable cooling and equipment rentals, temporary credentials, lost ancillary revenue (events, after-hours HVAC, parking share), and finance charges. Rent at risk is shown separately because it only turns into a loss after the lease abatement thresholds. Process owners supplied staffing and rate assumptions (security officer and engineer overtime at about $45 to $70 per hour; portable cooling at about $1,500 per tenant data room per day).

## 4. Process criticality and downtime (from `bia.csv`)
| Priority | Process | Unit | Criticality | MTD (h) | RTO (h) | RPO (h) | Estimated loss at MTD |
|---|---|---|---|---|---|---|---|
| 1 | BP-01 Physical access control and credentialing | Security operations | High | 4 | 2 | 1 | $15,000 |
| 2 | BP-05 Tenant emergency and service communications | Property management | High | 4 | 2 | 24 | $5,000 |
| 3 | BP-04 Security Command Center monitoring and video | Security operations | High | 8 | 4 | 24 | $12,000 |
| 4 | BP-02 Environmental control on BAS Platform A | Towers and mixed-use | High | 12 | 8 | 24 | $25,000 (rent at risk $150,700 per day after the abatement threshold) |
| 5 | BP-08 Tenant experience app and mobile credentials | Property management and security | Moderate | 24 | 8 | 4 | $10,000 |
| 6 | BP-06 Visitor management | Security operations | Moderate | 24 | 8 | 24 | $6,000 |
| 7 | BP-03 Environmental control on BAS Platform B | Retail and office parks | Moderate | 24 | 12 | 24 | $15,000 (rent at risk $115,000 per day after the abatement thresholds) |
| 8 | BP-09 Parking access and revenue | Parking (operator) | Moderate | 24 | 12 | 4 | $5,000 |
| 9 | BP-07 Engineering work orders and service requests | Engineering | Moderate | 48 | 24 | 4 | $8,000 |
| 10 | BP-10 Rent billing, collections, and tenant accounting | Finance | Moderate | 72 | 48 | 4 | $20,000 (plus up to $6.5 million cash delayed) |
| 11 | BP-11 Accounts payable, treasury, and debt service | Finance | Moderate | 72 | 48 | 24 | $15,000 |
| 12 | BP-15 Payroll and HR | Human resources | Low | 120 | 72 | 24 | $10,000 |
| 13 | BP-12 Card payment acceptance | Finance | Low | 120 | 72 | 24 | $2,000 |
| 14 | BP-13 Leasing and lease administration | Leasing | Low | 120 | 72 | 24 | $5,000 |
| 15 | BP-14 JV partner and lender reporting | Finance | Low | 168 | 120 | 24 | $5,000 |
| 16 | BP-16 Energy management and tenant submetering | Engineering | Low | 168 | 120 | 24 | $10,000 |

**Summary:** 4 High, 7 Moderate, and 5 Low processes (16 in total). The sum of estimated losses at each process's MTD is $168,000. These figures are small on purpose: they measure the cost of working by hand for a short time. The real financial exposure comes when an outage runs past the lease abatement thresholds (scenario below).

**Portfolio-wide scenario.** If BAS Platforms A and B were both unavailable for 5 business days (for example, ransomware that reaches the BAS servers at every property), the estimated cost is about **$650,000**: engineering overtime and manual rounds about $210,000; portable cooling and equipment rentals about $180,000; security officer overtime about $80,000; and office rent abatement for days 4 and 5 on leases using the 2024 template, about $180,000 (2 days x $150,700 x 60%). Retail abatement would start on day 6. Incident response and any breach notification costs come on top (P01 R-001 and R-016).

**What drives the values:**
- **Access control (BP-01) and tenant communications (BP-05)** have the shortest MTD. Door controllers cache credentials for up to 72 hours, so doors keep working, but no credential can be issued or revoked, and officers can staff about 60 entrances for only one shift. During any outage or storm, occupants must receive instructions within hours.
- **Tower HVAC (BP-02)** can run for a while because field controllers keep their last programs, but manual rounds on 18 to 32 floors exhaust the engineering crews in about 12 hours, and tenant data rooms overheat in the Florida climate. Rent abatement after day 3 makes long outages expensive.
- **Monitoring (BP-04)** is High because the SCC is the only place that sees all 14 properties. Its backup positions have never run a full shift.
- **Cash flow (BP-10, BP-11)** drives the finance processes. About $8.3 million is billed each month and debt service of about $3.1 million is due on fixed dates.

## 5. Key findings
1. **BAS Platform B cannot meet its recovery objectives.** The BIA needs RTO 12 hours and RPO 24 hours for BP-03. The 8 Platform B site servers have no backups, and field controller programs and graphics are held only by BAS Integrator B (gap 4). A failed server would be rebuilt by the integrator from its own copies, if they are current. This drives P01 R-004 and CPG 3.O in P03.
2. **Platform A recovery is designed but unproven.** The enterprise BAS server is backed up nightly to the separate backup account, but it has never been restored. The 8-hour RTO for BP-02 is a target, not a demonstrated capability (P07 CP-4).
3. **The cloud access control platform does not meet the BIA for administration.** The vendor's SOC 2 system description states RTO 8 hours and RPO 1 hour. The BIA needs RTO 2 hours for BP-01. The 72-hour credential cache keeps doors working, so the gap is administration (issuing and revoking credentials), not door operation. The P08 platform runbook (`ir-runbook-access-platform.md`) covers the workaround, and the P09 vendor review raises it at renewal.
4. **The SCC is a single point of failure.** Backup console positions at Tower 3 exist but have never run a full shift, and they rely on the same cloud video platform (P01 R-025).
5. **Tenant communications depend on one SaaS app.** About 40% of the printed tenant contact entries that back up the app are more than 12 months old. Refreshing them quarterly is a P08 preparation item.
6. **Manual (degraded-mode) procedures exist only at Towers 1-4.** The retail centers, office parks, and mixed-use properties have no written procedures for running plant equipment, lighting, or doors by hand (gap 4; P07 CP-2).

## 6. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 BAS Platform A | Enterprise supervisory server (VM, Tower 1 data room), 6 engineering workstations, about 5,200 field controllers | BP-02, BP-16 |
| SYS-01 BAS Platform B | 8 site supervisory servers, 8 engineering workstations, about 1,600 field controllers | BP-03 |
| SYS-02 Access control platform | Cloud service, about 410 door controllers, 2,300 readers, 36 turnstile lanes | BP-01, BP-06, BP-08 |
| SYS-03 Video surveillance | About 3,400 cameras, 46 NVRs, the vendor cloud console | BP-04 |
| SYS-04 Property networks | 14 sites on SD-WAN; firewalls; OT segments at Towers 1-4; one ISP at each retail center and office park, two at the towers | BP-01 to BP-04, BP-06 |
| SYS-05 Identity provider | Single sign-on and MFA | All administration |
| SYS-07 Property management system | Leases, receivables, work orders, tenant contacts | BP-05, BP-07, BP-10, BP-11, BP-13, BP-14 |
| SYS-08 Cloud landing zone | BAS historian and energy analytics, remote access gateway, file storage, data warehouse, backup vault | BP-02, BP-13, BP-14, BP-16 |
| SYS-09 Endpoints | 40 security console PCs, engineering tablets, corporate laptops | All |
| SYS-10 P2PE terminals | Card acceptance | BP-12 |
| SYS-11 Visitor management | Lobby kiosks at 6 properties | BP-06 |
| SYS-12 HR and payroll | Payroll provider | BP-15 |
| SYS-14 Tenant experience app | Mobile credentials, notices, service requests | BP-05, BP-07, BP-08 |
| Third parties | BAS Integrators A and B, access control and video platform vendor, SD-WAN provider, MSSP, parking operator, tenant app vendor, cloud provider | As listed in `bia.csv` |
| People and facilities | Chief engineers who can run plant equipment by hand; SCC operators and security officers; Property Managers with printed tenant contact lists; the SCC room at Tower 1 and backup positions at Tower 3 | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-05 identity provider and break-glass administrator accounts | 1 h | Two break-glass accounts per critical administration plane, sealed offline |
| 2 | SYS-04 SD-WAN, property firewalls, and OT zone rules | 2 h | Isolate OT segments; cellular failover at the SCC and lobby desks |
| 3 | SYS-02 access control administration from clean console PCs | 2 h | Doors run on cached credentials; officers at entrances |
| 4 | Tenant notification channels (SYS-14 notices, email, phone tree) | 2 h | Printed contact lists; Property Managers' company phones |
| 5 | SCC console PCs and SYS-03 video | 4 h | Backup positions at Tower 3; property desks use local NVR clients |
| 6 | Clean engineering workstations and tablets | 4 h | Pre-imaged spare laptops: 2 at each tower, 1 at each other property (to be bought, POAM-009) |
| 7 | SYS-01 Platform A enterprise BAS server | 8 h | Local hand control and manual rounds; restore from the backup account |
| 8 | SYS-14 tenant app and mobile credentials | 8 h | Temporary cards at lobby desks |
| 9 | SYS-11 visitor management | 8 h | Paper log and escort |
| 10 | SYS-01 Platform B site servers | 12 h | Local hand control; rebuild by Integrator B (no backups today, POAM-010) |
| 11 | SYS-07 property management system access and work orders | 24 h | Vendor-hosted; phone and paper requests |
| 12 | Bank portal access for treasury | 48 h | Clean laptop with dual approval |
| 13 | SYS-10 P2PE terminals | 72 h | Invoice customers |
| 14 | SYS-12 payroll | 72 h | Repeat the prior payroll |
| 15 | SYS-08 historian, energy analytics, and data warehouse | 120 h | BAS on fixed schedules; reports from system exports |

The order (identity, network, access control, tenant communications, monitoring, clean endpoints, then the BAS) is used in both P08 runbooks. The BAS RTOs are longer than the access control RTO because field controllers keep running and engineers can operate plant equipment by hand, while an uncontrolled entrance or an uninformed occupant is an immediate exposure.
