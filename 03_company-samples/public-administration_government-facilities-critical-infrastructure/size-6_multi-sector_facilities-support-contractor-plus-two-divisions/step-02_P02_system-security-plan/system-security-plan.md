# System Security Plan: Integrated Building Operations Platform (IBOP)

**Organization:** Cris Santos Company Holdings, Inc. (corporate shared services, serving the Government Facilities Support, Construction and Renovation, and Janitorial and Security Services divisions) | **Tier:** Multi-Sector | **Vertical:** Government Services and Facilities
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-15

> **Why this system.** At this tier the SSP can cover one system per division or a shared corporate system. The group chose the **IBOP**, a shared corporate system, because it is the physical access control and building automation platform for the focus division's state, local, and education customers, it also hosts the Janitorial and Security central monitoring station and the Construction commissioning workspace, it inherits most of its controls from corporate (SYS-G1 to SYS-G3), and it carries the group's top risk (P01 GR-01). Each division keeps its own plans for its own systems; the Construction division's CMMC system security plan for SYS-C2 is one of them and must inherit from the same common control catalog (POAM-028).

## 1. System Name and Identifier
Integrated Building Operations Platform (**IBOP**), identifier CSCH-SYS-G5. SYS-G5 in `../00_company-facts.md`.

## 2. System Overview
The IBOP lets the group operate customers' building systems remotely and at scale. It supports:
- **Government Facilities Support (focus):** supervision of building automation at 296 state, local, and education sites (about 41,000 BACnet controllers), access control administration for 188 sites (about 9,800 doors and 212,000 cardholders), and 24x7 alarm monitoring from two Remote Operations Centers (ROC-1 in Florida, ROC-2 in Texas).
- **Janitorial and Security Services:** the central monitoring station at ROC-2, which monitors video and intrusion alarms at 640 sites and dispatches officers.
- **Construction and Renovation:** a commissioning workspace where engineers stage building automation and access control programming and drawings before turnover. It currently holds controlled drawings from 4 DoD projects.

About 2,400 workforce users (ROC operators, controls and security systems technicians, monitoring operators, commissioning engineers) and about 180 integrator and subcontractor accounts use it.

**Major components:**
- **Supervisory services:** building automation supervisory servers and trend historians (virtual machines in provider A), one database per customer
- **Access control administration:** one access control SaaS tenant per customer, administered by the group; 14 legacy on-premises access control servers at acquired sites
- **Video and alarm monitoring module:** video management SaaS tenants, alarm receivers, and operator consoles at both ROCs
- **OT remote access service:** PAM-brokered jump service with MFA, approval, and session recording
- **Site OT edge gateways:** company-managed firewalls and VPN gateways at all 296 sites
- **Controller program repository:** versioned, hashed copies of controller programs and door schedules (61% of sites)
- **Commissioning workspace:** project file storage and staging supervisory instances for buildings under construction
- **Disaster recovery:** database replica and immutable backup vault in provider B

The platform is described by service category and is vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies to the IBOP |
|---|---|---|---|
| Contract | State agency cybersecurity exhibits | Contract term; Florida worked example: Fla. Stat. 282.318(4)(h) | Require SP 800-53 Rev. 5 Moderate controls for contractor-managed systems holding agency data, incident notice within 24 hours, and an annual independent assessment. This is why the Moderate baseline is binding for the IBOP |
| Contract | County and municipal security addenda | Contract term; Florida worked example: Fla. Stat. 282.3185(4) | Customer cybersecurity standards (NIST CSF based) and notice within 24 hours (12 hours under 9 county contracts). The customers' own reports to the state (282.3185(5)) depend on the group's notice |
| C-GOVERNMENT-R05 | FERPA | 34 CFR 99.31(a)(1)(i)(B), (a)(1)(ii); 99.33(a) | The state university designated the company a school official for about 38,000 students' cardholder records; use only for the contracted purpose and no redisclosure |
| C-GOVERNMENT-R08 | GovRAMP | GovRAMP program (not law) | A 2027 state renewal requires GovRAMP verification of the IBOP by 2027-07-01 (POAM-030) |
| C-GOVERNMENT-R01 | FISMA | 44 U.S.C. 3554(a)(1)(A)(ii) | **Not directly.** Federal building automation stays on agency networks under agency authorizations (SYS-F2). No IBOP service runs on behalf of a federal agency |
| N23-R03 | DFARS 252.204-7012 | 48 CFR 252.204-7012(b)(2), (c)-(e) | The commissioning workspace holds covered defense information, which makes it a covered contractor information system. CUI must move to the Construction enclave (POAM-019); until then any incident there needs a DoD report within 72 hours |
| FAR | FAR 52.204-21, -23, -25, -30 | 48 CFR 52.204-21 to -30 | Federal contract information in the commissioning workspace; Section 889 and FASCSA screening of IBOP equipment, including central monitoring station NVRs (POAM-022) |
| State law | Breach notification and third-party agent duties | Each state where affected individuals reside; Florida worked example: Fla. Stat. 501.171(2), (6) | The group holds cardholder data as a third-party agent of public customers: reasonable security, and notice to the customer within 10 days of a breach determination (P08) |
| State law | Public records | Florida worked example: Fla. Stat. 119.0701; 119.071(3)(a) | Security system plans and layouts are exempt from disclosure; the group routes requests to the customer's custodian |
| SEC | Cybersecurity disclosure | Reg S-K Item 106; Form 8-K Item 1.05 | An IBOP incident may be material to the group (P08) |
| Internal | Group policies POL-01 to POL-05 and division supplements | P06 | |

Not applicable: IRS Pub. 1075 and the CJIS Security Policy as system requirements (no FTI or criminal justice information is processed in the IBOP; customer contracts at those buildings add personnel and training terms, tracked in AT-3 and MA-5); VVSG 2.0 (no election systems).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Group CISO and the Group building technology director (system owner) on 2026-09-15, after the board risk committee review.

### 4.2 System Authorization Decision
The group is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- **Decision:** authorized to operate with conditions, 2026-09-15, by the Group CISO and the Group Chief Risk Officer (acceptance authority for High risks).
- **Conditions:** (1) all 37 acquired sites on the jump service and all integrator accounts with MFA by 2026-12-15 (POAM-003, POAM-009, POAM-010); (2) no new customer tenant onboarded with the standing global administrator role; per-customer just-in-time administration by 2027-03-31 (POAM-011); (3) no new CUI uploaded to the commissioning workspace from 2026-10-01, and existing CUI moved to the Construction enclave by 2026-12-31 (POAM-019).
- **Reauthorization:** annually, or when the conditions are met.

### 4.3 System Operational Status
Operational. **Major modifications planned:** migration of the 37 acquired sites (due 2026-12-15) and OT segmentation of 19 flat sites (due 2027-03-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Group building technology director | Accountable for the IBOP and this SSP |
| Authorizing official equivalent | Group CISO with the Group Chief Risk Officer | Authorization decision; High risk acceptance |
| System security lead | IBOP security lead | Day-to-day security, POA&M, log review |
| Business owner, building automation and access control | Facilities Support controls engineering director; Facilities Support security systems director | Customer configurations, tenant administration, program changes |
| Business owner, central monitoring station | Janitorial and Security monitoring director | Monitoring module operations |
| Business owner, commissioning workspace | Construction commissioning director, with the Construction CUI program manager | Commissioning data, including CUI until it moves |
| Common control providers | Group identity director (SYS-G1), Group SOC director (SYS-G2), Group cloud platform director (SYS-G3), Group HR director, Group procurement director, Group facilities director | Operate inherited controls (`common-control-catalog.csv`) |
| Independent assessor | Group internal audit | Assesses common controls once and samples IBOP and division controls (P07) |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Facility operations and maintenance (building automation control, setpoints, schedules, alarms) | Low | Moderate | Moderate | Wrong setpoints or schedules can damage equipment or make a building unusable; controllers keep running locally (P05 BP-FS03, MTD 24 hours) |
| Physical security (access control, door schedules, video, alarm monitoring, security layouts) | Moderate | Moderate | Moderate | Unauthorized door changes expose people and property at government buildings; monitoring has a 2-hour MTD (P05 BP-JS01); layouts are exempt public records in the Florida worked example (Fla. Stat. 119.071(3)(a)) |
| Personal identity and authentication (cardholder records, badge photos, face templates) | Moderate | Moderate | Low | About 212,000 people, including education records of about 38,000 students; third-party agent duties under state breach laws |
| Controlled technical information (DoD commissioning drawings) | Moderate | Low | Low | CUI Basic is categorized at no less than moderate confidentiality (32 CFR 2002.14(g)); the drawings are copies, so loss of availability is minor |
| Information security (keys, administrator credentials, logs) | Moderate | Moderate | Moderate | Compromise would expose every customer tenant |
| **IBOP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | Overall **Moderate** |

**Why integrity is not High.** A tampered door schedule at a government building is serious, and the group considered High. It stayed Moderate because life-safety functions (fire alarm, smoke control, egress door release) are hardwired and outside the platform, door and BACnet controllers enforce schedules locally, and customers keep security staff on site. P01 still treats cross-tenant door manipulation as the top group risk (GR-01). The authorizing official will revisit the rating if the closed-loop optimization pilot (P10 AI-004) is expanded.

**Baseline:** the NIST SP 800-53B **Moderate** baseline, which state contracts require and the GovRAMP verification will use. All **177 base controls** are documented in `control-implementation.csv`, with their Moderate enhancements assessed inside each base control. Tailoring follows NIST SP 800-82 Rev. 3 for OT (for example passive discovery in place of active scanning during occupied hours, and segmentation to compensate for unencrypted BACnet). No controls were tailored out. Developer controls (SA-10, SA-11, SA-15) are inherited from the platform's software vendors.

## 7. Authorization Boundary Description
- **Inside:** the IBOP accounts in provider A (supervisory services, program repository, commissioning workspace, jump service, logging and network services), the DR replica and backup vault in provider B, the group's administration and configuration of the access control and video SaaS tenants, the 14 legacy on-premises access control servers, the 296 site edge gateways and site engineering workstations, and the operator consoles at ROC-1 and ROC-2.
- **Outside, inherited (common control providers):** SYS-G1 identity platform, SYS-G2 SOC, SIEM, and EDR, the SYS-G3 landing zone (network hub, log archive, guardrails, keys), group HR, procurement, and facilities.
- **Outside, interconnected:** customer-owned field devices and site networks; the access control and video SaaS vendors' platforms; SYS-F1 CMMS; SYS-C2 Construction enclave; integrators' systems; agency systems at federal buildings (SYS-F2, never connected to the IBOP).

The diagram is in P04 `cloud-architecture.md` (the IBOP subgraph).

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| 296 customer site networks (state, local, education) | Both, through edge gateways | BACnet supervision, door events, alarms | Service contracts; technical interconnection terms missing for 41% of local sites (CA-3) |
| Access control SaaS vendor (188 tenants) | Both | Cardholder records, door schedules, events | Vendor contract; annual SOC 2 Type 2 review; face verification module not covered (SA-9) |
| Video management SaaS vendor | Both | Video, alarm events | Vendor contract; SOC 2 review |
| SYS-F1 CMMS | Outbound | Alarm-generated work orders | Internal |
| SYS-C2 Construction enclave | Inbound (from 2026-10) | Commissioning packages after CUI is removed | Internal; CUI stays in SYS-C2 |
| Integrators (about 180 accounts) | Inbound (remote maintenance) | Programming sessions | Subcontracts; security terms missing at acquired sites (PS-7, POAM-017) |
| Customer badging offices | Inbound | Badge requests, revocations | Customer procedures; MFA enforced in 112 of 188 tenants (IA-8) |
| Police and fire dispatch (from the central monitoring station) | Outbound (voice and alarm data) | Alarm details | Monitoring contracts |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| Supervisory servers and historians | IaaS virtual machines | Provider A | Facilities Support controls engineering director |
| Access control tenants (188) | SaaS | Access control vendor | Facilities Support security systems director |
| Legacy access control servers (14) | On-premises servers | Acquired customer sites | Facilities Support security systems director |
| Video and alarm monitoring module | SaaS tenants plus alarm receivers and consoles | Video vendor; ROC-1 and ROC-2 | Janitorial and Security monitoring director |
| OT remote access service | PaaS and IaaS (PAM jump service) | Provider A | IBOP security lead |
| Site edge gateways (296) and engineering workstations | Network appliances; Windows workstations | Customer sites | Facilities Support controls engineering director |
| Controller program repository | Managed source repository with hashing | Provider A | Facilities Support controls engineering director |
| Commissioning workspace | Object storage and staging supervisory instances | Provider A | Construction commissioning director |
| DR replica and immutable backup vault | Database replica; backup service | Provider B | Group cloud platform director |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv` (177 controls) and `common-control-catalog.csv` (139 group common controls).

| Status | Controls |
|---|---|
| Implemented | 130 |
| Partially implemented | 45 |
| Planned | 2 |
| Not applicable | 0 |
| **Total** | **177** |

| Inheritance | Controls |
|---|---|
| Common/Inherited (from SYS-G1, SYS-G2, SYS-G3, group functions, or cloud and SaaS vendors) | 99 |
| Hybrid (group provides the mechanism; the IBOP configures or operates part) | 49 |
| System-specific | 29 |

**The 45 partially implemented controls** cluster in five places:
- **Remote and privileged access** (scenario gaps 1 and 2): AC-2, AC-5, AC-6, AC-17, AC-20, CM-3, CM-7, IA-2, IA-5, MA-4, MP-5, PS-7, SI-2.
- **OT visibility, inventory, and segmentation** (gaps 3 and 4): AU-2, AU-6, AU-11, AU-12, CA-7, CM-2, CM-8, CP-10, IA-3, PL-8, RA-5, SA-22, SC-7, SC-8, SI-4, SI-7.
- **Incident response and contingency** (gap 10 and the P05 findings): CP-2, CP-4, IR-3, IR-4, IR-6, IR-8.
- **CUI and supply chain** (gaps 5 and 6): CM-12, MP-3, SR-3, SR-5, SR-11.
- **Customers and third parties:** AT-3, CA-3, IA-8, SA-4, SA-9.

The 2 planned controls are supply chain controls: SR-8 (supplier compromise notification terms, at 2027 renewals) and SR-10 (inspection of components at acquired sites).

### 10.2 Common control inheritance by division
The common control catalog lists 139 controls provided by corporate: 123 used by every division and 16 physical controls for the ROC buildings that serve only the IBOP. Inheritance is **documented for Facilities Support** (2026 inheritance matrix) and for the IBOP (this plan). It is **not documented for Construction**, whose CMMC system security plan for SYS-C2 lists every requirement as if the division operated it alone, or for **Janitorial and Security**, which still runs its 2022 policy set (scenario gaps 8 and 9). Until POAM-028 closes, Construction cannot show a CMMC assessor which SP 800-171 requirements are met by group identity, SOC, and HR controls.

### 10.3 Control assessment status
Common controls were assessed once, and IBOP and division controls sampled, from 2026-07-06 to 2026-08-28 by group internal audit. See P07 `assessment-results.csv` and `poam.csv`. The P03 gap analysis (`gap-analysis.csv`) uses the same 177 statements, so the two documents do not drift apart.

## 11. Digital Identity Acceptance Statement
- **Workforce users** authenticate through SYS-G1 federated sign-in with MFA (number matching); **administrators** use phishing-resistant hardware keys and just-in-time PAM elevation. This fits a Moderate system whose administrators can change doors at government buildings.
- **Integrators** must use the jump service with MFA. 22 integrator accounts at acquired sites do not yet (POAM-003).
- **Customer badging staff** sign in to their own access control tenant; MFA is enforced in 112 of 188 tenants. Customers that decline MFA sign a risk acceptance at renewal.
- **Cardholders** do not sign in to the IBOP. They present badges (and, at 3 county sites, a face match) to door readers (P10).

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), group and division risk registers (P01), gap analyses and regulation-by-division matrix (P03), cloud architecture and control map (P04), BIA (P05), group policies and division supplements (P06), assessment and POA&M (P07), incident response runbook and notification matrix (P08), SOC 2 readiness (P09), AI governance (P10).

## 13. Acronym List and Glossary
- **BACnet:** a building automation and control network protocol
- **Common control:** a control provided once by corporate and inherited by several systems
- **CUI:** controlled unclassified information
- **IBOP:** Integrated Building Operations Platform
- **NVR:** network video recorder
- **OT:** operational technology
- **PAM:** privileged access management
- **ROC:** Remote Operations Center
- **SIEM:** security information and event management

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-08-28 | Draft after P07 fieldwork | Group building technology director |
| 1.0 | 2026-09-15 | Approved with authorization conditions | Group CISO |
