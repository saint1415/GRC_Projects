# System Security Plan: Building Automation and Access Control System (BAACS)

**Organization:** Cris Santos Company, Inc. (PE-backed commercial office and retail property owner-operator) | **Tier:** Mid-Market | **Vertical:** Commercial Facilities
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **OT guidance:** NIST SP 800-82 Rev. 3 (September 2023) | **Version:** 1.0, 2026-09-15

## 1. System Name and Identifier
Building Automation and Access Control System (**BAACS**), identifier CSC-BAACS-01. The BAACS is the company's major system. It comprises SYS-01 to SYS-03 and the OT portions of SYS-04, SYS-08, and SYS-09 in `../00_company-facts.md`.

## 2. System Overview
The BAACS runs the building functions tenants pay for at all 14 Florida properties: cooling, ventilation, lighting, and metering (the building automation system, BAS); doors, turnstiles, and credentials (the physical access control system, PACS); and video surveillance, monitored around the clock from the Security Command Center (SCC) at Tower 1. It supports about 420 tenants, about 14,500 credential holders, and the processes rated High in the BIA (P05): BP-01, BP-02, and BP-04.

Users: 212 engineering and maintenance staff (BAS), 162 security operations staff (PACS, video, SCC), 20 IT and security staff, BAS Integrators A and B, the access control and video integrator, and the guard contractor (video viewing only). Tenant employees hold credentials but do not sign in to the system.

**Major components:**
| ID | Component | Hosting and service model |
|---|---|---|
| SYS-01 (Platform A) | Enterprise BAS supervisory server (VM in the Tower 1 data room), 6 engineering workstations, about 5,200 BACnet field controllers at Towers 1-4 and Mixed-Use 1-2 | On-premises (OT) |
| SYS-01 (Platform B) | 8 site supervisory servers (physical PCs), 8 engineering workstations, about 1,600 field controllers at Parks 1-2 and Retail 1-6 | On-premises (OT) |
| SYS-02 | Cloud access control platform with about 410 door controllers, 2,300 readers, and 36 turnstile lanes | Vendor SaaS plus on-premises (OT) |
| SYS-03 | About 3,400 cameras and 46 NVRs managed from the same vendor platform; hosts the video analytics features AI-001 and AI-002 | On-premises plus vendor SaaS |
| SYS-04 (part) | OT segments, property firewalls, SD-WAN edges at 14 sites | On-premises; SD-WAN managed service |
| SYS-08 (part) | BAS historian and energy analytics, remote access gateway, backup vault, log pipeline | Public cloud landing zone (P04) |
| SYS-09 (part) | 40 security console PCs and 190 engineering and security tablets | Company-managed |

SP 800-82 Rev. 3 names building automation systems and physical access control systems as operational technology (OT). This plan treats the BAACS as an OT system and uses SP 800-82 Rev. 3 guidance where IT practices do not fit. For example, field controllers are not actively scanned, and segmentation compensates for unencrypted BACnet traffic.

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it affects the BAACS |
|---|---|---|---|
| C-COMMERCIAL-FACILITIES-R05 | CISA Cross-Sector Cybersecurity Performance Goals 2.0 (**voluntary**) | CISA CPG 2.0 (December 2025) | Adopted by the COO as the security baseline on 2026-07-01; goal IDs cited in `control-implementation.csv` (P03 section 1.2) |
| C-COMMERCIAL-FACILITIES-R02 | FTC Act Section 5 | 15 U.S.C. 45(a) | Statements to tenants and visitors about credential, visitor, video, and analytics data must be accurate, and security must be reasonable |
| State | Florida Information Protection Act | Fla. Stat. 501.171(2) (reasonable measures), (3)-(6) (breach notice), (8) (disposal) | PACS and visitor data include personal information (for example driver license numbers from visitor ID scans); face templates from the AI-002 pilot are treated as biometric data (P10) |
| C-COMMERCIAL-FACILITIES-R06 | CIRCIA (**proposed rule only**) | 6 U.S.C. 681b; proposed 6 CFR Part 226 | Not in effect. The company would be covered under the NPRM's size criterion, so logging and incident records are designed to support a 72-hour report (P03, P08) |
| Contract | JV management agreement | Amended 2026-05 | SOC 2 Type 2 report on property management and building operations services, including this system, by 2027-12-31 (P09) |
| Contract | Lease security and notice clauses | 2024 lease template; 72-hour clauses in 31 leases | Tenant notice after unauthorized access to tenant employee data in the PACS (P08) |
| Guidance | NIST SP 800-82 Rev. 3 | Final, September 2023 | OT architecture (zones and conduits) and the OT overlay used to tailor this plan |
| Internal | Security policies POL-01 to POL-05 and supporting standards | P06 | Policy basis for every control |

Not applicable to this system:
- **PCI DSS v4.0.1 (C-COMMERCIAL-FACILITIES-R01):** no account data enters the BAACS. Card payments use stand-alone P2PE terminals (SYS-10), outside this boundary (P03).
- **CCPA/CPRA (R03) and SEC disclosure (R04):** the company does not do business in California and is privately held.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Chief Operating Officer (system owner) on 2026-09-15, after the control assessment (P07) and before the audit committee meeting the same day.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization to operate. The equivalent internal decision:
- **Decision:** continued operation of the BAACS accepted with conditions, 2026-09-15.
- **Authorizing official equivalent:** Chief Executive Officer for High and Very High risks; Chief Operating Officer for Moderate and below (P01 acceptance authorities).
- **Conditions:**
  1. The Tower 1 any-any rule found in P07 is removed by 2026-09-30, and the internet exposure at Park 2 is closed by 2026-10-15 (POAM-004, POAM-018).
  2. Integrator B's always-on remote-support tool is removed and its access moved to the gateway by 2026-11-30 (POAM-003).
  3. The audit committee receives POA&M status each quarter; re-decision by 2027-09-30 or after a major change (for example the Platform B upgrade or an acquisition).
### 4.3 System Operational Status
Operational. Major modifications planned:
- Integrator B moved to the remote access gateway (POAM-003), due 2026-11-30
- OT asset inventory with passive discovery (POAM-008), due 2026-12-31
- Platform B backups and quarterly restore testing (POAM-010), due 2027-03-31
- OT log collection and monitoring through the MSSP (POAM-006), due 2027-03-31
- OT segmentation at Mixed-Use 1-2, Parks 1-2, and Retail 1-6 (POAM-004), due 2027-06-30
- Platform B server and software upgrade (POAM-015), due 2027-06-30

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Chief Operating Officer | Accountable for the BAACS; accepts Moderate risk; approves this plan |
| Authorizing official equivalent (High risk) | Chief Executive Officer | Accepts High risk; approves the risk appetite |
| Oversight | Board audit committee | Quarterly cyber risk reporting |
| Program strategy | vCISO (part-time contractor) | Program strategy, board reporting, SSP review |
| Information security officer | IT Director | Day-to-day program lead; network, cloud, and backup controls |
| Security operations | Security Manager and 2 security analysts (one OT-focused) | Monitoring, vulnerability management, MSSP liaison |
| GRC | GRC Analyst | Maintains this plan, the risk register, and the POA&M |
| BAS owner | Vice President of Engineering, with the Building Technology Manager | BAS configuration, integrator oversight, degraded-mode procedures |
| PACS and video owner | Director of Security Operations | Credential administration, video, visitor management, SCC, guard contractor |
| BAS operators | Chief Engineers (14) | Daily operation and hand control of plant equipment |
| Independent assessment | Co-sourced internal audit firm | Annual IT audit; P07 assessment |
| Monitoring | MSSP | 24x7 monitoring of IT sources and console PCs |
| Vendor support | BAS Integrators A and B; access control and video integrator | Programming, device service, remote support |

## 6. System Information Types and System Categorization
Information types were adapted from NIST SP 800-60 Vol. 2 Rev. 1 for a private company. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Facilities and equipment management (BAS setpoints, schedules, programs, building drawings) | Low | Moderate | Moderate | Tampering can stop cooling or damage equipment across a property. Field controllers keep running and engineers can run plant equipment by hand, so loss is serious but not catastrophic (P05 BP-02 MTD 12 h, BP-03 MTD 24 h). Life-safety systems are separate |
| Physical security management (door schedules, credentials, access events, video, SCC alarms) | Moderate | Moderate | Moderate | Credential or video disclosure harms tenant employees; a wrong door schedule leaves entrances unsecured. Cached credentials and officer posts limit availability impact (P05 BP-01 MTD 4 h, BP-04 MTD 8 h) |
| Personal identity and authentication (tenant employee credential records and badge photos; visitor records at the SYS-11 interface; mobile credential data from SYS-14) | Moderate | Moderate | Low | Personal information under Fla. Stat. 501.171 when combined with ID numbers; outage handled by paper logs and temporary cards |
| System and network monitoring (security logs, gateway recordings) | Moderate | Moderate | Low | Needed to investigate incidents and to support notice decisions |
| **BAACS category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Integrity was considered for High.** A malicious BAS program change could damage chillers or overheat occupied floors, and a door schedule change could unlock entrances. The team kept integrity at Moderate because field controllers enforce equipment safety limits locally, life-safety systems are separate with hardwired egress release, and chief engineers can take local hand control. To compensate, the baseline adds integrity tailoring (section 10.1).

## 7. Authorization Boundary Description
**Inside the boundary:**
- the Platform A server and 6 engineering workstations; the 8 Platform B servers and 8 engineering workstations; about 6,800 field controllers;
- about 410 door controllers, 2,300 readers, and 36 turnstile lanes; about 3,400 cameras and 46 NVRs;
- the company's configuration of the access control and video platform (tenant, roles, door groups, analytics settings);
- the OT network segments and the property firewalls and SD-WAN edges that enforce them;
- in the cloud landing zone: the BAS historian and energy analytics workload, the remote access gateway, the backup vault, and the log pipeline;
- 40 security console PCs and 190 engineering and security tablets.

**Outside the boundary (interconnected external services):**
- the access control and video platform vendor's cloud infrastructure;
- the cloud provider's infrastructure;
- the identity provider (SYS-05), visitor management (SYS-11), and the tenant experience app (SYS-14);
- the energy optimization vendor (AI-004) and the parking operator's systems (AI-003);
- the integrators' own networks and devices; the MSSP's platform;
- the life-safety systems (SYS-13).

**Outside (not connected):** the P2PE card terminals (SYS-10) and corporate SaaS other than those listed.

**Life-safety design rule.** Fire alarm panels, elevator controls, and emergency voice communication stay on separate vendor-maintained networks. The BAS reads fire alarm status only through hardwired, read-only relay points, and door releases for egress are hardwired to the fire alarm. No change may create a network path from the BAACS to a life-safety system (PL-8). P01 R-047 tracks the risk that an integrator breaks this rule.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Access control and video platform (vendor cloud) | Bidirectional (door controllers and NVRs to cloud over TLS) | Credentials, door events, schedules, video clips, analytics alerts | SaaS agreement; vendor SOC 2 Type 2 (P09) |
| Identity provider (SYS-05) | Inbound authentication | Administrator sign-in to the platform portal, the Platform A server, the gateway, and the cloud console | SaaS agreement |
| Visitor management (SYS-11) | Outbound visitor passes to turnstiles | Visitor name, host, pass validity | SaaS agreement; **no retention or breach terms (gap, POAM-016, POAM-017)** |
| Tenant experience app (SYS-14) | Bidirectional (mobile credential issuance and revocation) | Credential identifiers, user names | SaaS agreement; integration agreement with the platform vendor |
| Energy optimization service (AI-004) | Inbound setpoint writes to Platform A at Towers 1-2; outbound trend data | Setpoints, temperatures, run status | Service agreement; **no written interconnection terms for the write path (gap, CA-3)** |
| BAS historian (SYS-08) | Outbound trend data from the BAS servers over the site VPN | Temperatures, run status, energy meters | Company-managed |
| BAS Integrator A; access control and video integrator | Inbound remote support through the remote access gateway | Device and program configuration | Service agreements with security terms; named accounts, MFA, recording |
| BAS Integrator B | Inbound remote support through its own always-on tool | Full control of the 8 Platform B servers | Service agreement; **no security terms, shared account, no MFA (gap, POAM-003, POAM-016)** |
| Guard contractor | Inbound video viewing through the vendor cloud console | Live and recorded video | Guard services agreement; **shared viewing accounts (gap, POAM-002)** |
| Parking operator (AI-003) | Inbound LPR event exports on request | Plate reads, times, locations | Garage management agreement; **no data use or retention terms (gap, P10)** |
| MSSP | Outbound logs; inbound response actions on console PCs | Security logs | MSSP contract; SOC 2 Type 2 |
| Life-safety systems (SYS-13) | Inbound only, hardwired relay points | Fire alarm status | Design rule (section 7) |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| Platform A enterprise BAS server | Virtual machine | Tower 1 data room | Vice President of Engineering |
| Platform A engineering workstations (6) | Endpoint | Towers 1-4, Mixed-Use 1-2 | Vice President of Engineering |
| Platform B site servers (8) and workstations (8) | Physical PCs (unsupported OS) | Parks 1-2, Retail 1-6 engineering rooms | Vice President of Engineering |
| BACnet field controllers (about 6,800) | OT device | All properties | Vice President of Engineering |
| Access control and video platform tenant | SaaS | Platform vendor | Director of Security Operations |
| Door controllers (about 410), readers (about 2,300), turnstile lanes (36) | OT device | All properties | Director of Security Operations |
| Cameras (about 3,400) and NVRs (46) | OT device | All properties | Director of Security Operations |
| Security console PCs (40) | Endpoint | SCC (Tower 1), backup positions (Tower 3), lobby desks | Director of Security Operations |
| Engineering and security tablets (190) | Mobile device | All properties | Vice President of Engineering; Director of Security Operations |
| Property firewalls (14), SD-WAN edges, OT switches | Network | All properties | IT Director |
| Remote access gateway, log pipeline | Cloud services | Shared services account | IT Director |
| BAS historian and energy analytics | Virtual machines and managed database | Workloads account | Vice President of Engineering |
| Backup vault | Backup service, write-once | Backup account (second region) | IT Director |

The device-level OT inventory is about 55% complete. Completing it is POAM-008 (CM-8), due 2026-12-31.

## 10. Control Implementation Details
### 10.1 Control implementation status
**Baseline and tailoring.** The BAACS uses the NIST SP 800-53B **Moderate** baseline (287 controls and enhancements), tailored with the SP 800-82 Rev. 3 OT overlay:
- **Documented here: 123 controls** in `control-implementation.csv`: 120 from the Moderate baseline and 3 program controls (PM-1, PM-2, PM-9) selected by tailoring because the voluntary CPG 2.0 governance goals (1.A, 1.B) depend on them. The documented set covers every control the CPG 2.0 goals reference for this system, every control behind a Moderate-or-higher risk in P01, and the controls the SOC 2 commitment to the JV partner relies on (P09).
- **Integrity tailoring:** CM-3, CM-4, and SI-7 statements cover BAS program and door schedule changes; PL-8 records the life-safety design rule.
- **Compensating controls for OT limits:** BACnet traffic is not encrypted, so segmentation (AC-4, SC-7) compensates for SC-8 inside OT zones; Platform B servers cannot run EDR, so isolation and the upgrade plan (SA-22) compensate for SI-3 until 2027-06-30.
- **Inherited without separate statements:** physical and environmental controls of the cloud and SaaS data centers (for example PE-9 to PE-17) and platform-level SA and SC controls, inherited from the access control and video platform vendor, the identity vendor, the cloud provider, and the MSSP, and evidenced by their SOC 2 Type 2 reports (P09 `vendor-soc2-review.csv`).
- **Deferred:** the other Moderate controls with no CPG reference and no Moderate-or-higher risk (for example SA-11 developer testing and SA-15 development process, because the company does not develop software). They are recorded as tailoring decisions and reviewed yearly.
- **CSF 2.0 mapping:** taken from `00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv` (the base control's row for enhancements). For 14 controls with no row in that file (for example AC-8, MA-4, PS-4), the CSF subcategories are an author mapping.

**Status of the 123 documented controls:**
| Status | Count |
|---|---|
| Implemented | 47 |
| Partially implemented | 68 |
| Planned | 8 |
| Not applicable | 0 |

**Inheritance of the 123 documented controls:**
| Inheritance | Count | Main providers |
|---|---|---|
| System-specific | 87 | Company |
| Hybrid | 22 | Access control and video platform vendor, cloud provider, identity vendor, MSSP |
| Common/Inherited | 14 | Identity vendor (for example AC-7, IA-2(1)), cloud provider (CP-6, SC-12), MSSP (AU-6(1), IR-7), platform vendor (AC-12, SC-5, SC-13) |

The Partially implemented and Planned statements trace to the 12 known gaps in `../00_company-facts.md` section 4 and to the P07 findings. The pattern is consistent: controls are in place at Towers 1-4 and for IT, and missing or partial at the 8 Platform B properties and for OT logging and recovery.

### 10.2 Control assessment status
The co-sourced internal audit firm assessed 36 controls from 2026-08-03 to 2026-08-21 (P07 `assessment-plan.md`, `assessment-results.csv`, and `poam.csv`). Testing found two weaknesses that were not known before: the Tower 1 any-any firewall rule (P01 R-050) and manufacturer default passwords on 9 of 30 sampled OT devices. Weaknesses are tracked in the POA&M and reported quarterly to the audit committee.

## 11. Digital Identity Acceptance Statement
- **Company staff.** All staff authenticate through the identity provider with a password and push MFA with number matching. This is appropriate for a Moderate system.
- **Administrators.** Identity provider, cloud, and access control platform administrators use phishing-resistant security keys. Platform A server administration uses identity provider sign-in.
- **BAS local accounts.** Platform B software does not support the identity provider. Until the upgrade (POAM-015), Platform B access will use named local accounts reachable only through the remote access gateway, which enforces MFA (POAM-003, POAM-005). The shared site accounts are being retired.
- **Integrators.** Named accounts with MFA through the remote access gateway, with per-session approval by the chief engineer on duty.
- **Tenant employees.** They hold physical cards or mobile credentials only and do not sign in to the system. Each tenant's designated contact authorizes issuance (PE-2). Mobile credential users authenticate to the tenant app vendor, outside this boundary.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`); BIA (P05); cloud architecture and control map (P04); risk register (P01); gap analysis and roadmap (P03); policies and standards index (P06); assessment and POA&M (P07); incident runbooks (P08); SOC 2 readiness and vendor reviews (P09); AI governance assessment (P10).

## 13. Acronym List and Glossary
- **BAACS:** Building Automation and Access Control System
- **BACnet:** a standard communication protocol for building automation devices
- **BAS:** building automation system
- **CPG:** CISA Cross-Sector Cybersecurity Performance Goals
- **EDR:** endpoint detection and response
- **JV:** joint venture
- **MSSP:** managed security service provider
- **NVR:** network video recorder
- **OT:** operational technology
- **P2PE:** point-to-point encryption (PCI)
- **PACS:** physical access control system
- **POA&M:** plan of action and milestones
- **SCC:** Security Command Center

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-07-31 | Draft from the risk assessment and gap analysis | GRC Analyst |
| 1.0 | 2026-09-15 | Updated with P07 results; approved by the Chief Operating Officer | IT Director |

Next review: 2027-09-15, or sooner after the Platform B upgrade, the segmentation cutover, or an acquisition.
