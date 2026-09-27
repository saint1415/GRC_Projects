# System Security Plan: Building Automation and Access Control System (BAACS)

**Organization:** Cris Santos Company, LLC (commercial office and retail property owner-operator) | **Tier:** Small | **Vertical:** Commercial Facilities
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **OT guidance:** NIST SP 800-82 Rev. 3 (September 2023) | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Building Automation and Access Control System (**BAACS**), identifier CSC-SYS-OT-001.

## 2. System Overview
The BAACS runs the building functions tenants pay for at the company's three Florida properties: cooling, ventilation, lighting, and metering (the building automation system, BAS); doors, turnstiles, and badges (the physical access control system, PACS); and video surveillance. It serves 38 tenants and about 1,300 badge holders at Property A (Office Tower), 44 retail and restaurant tenants at Property B (Retail Center), and 19 tenants and about 450 badge holders at Property C (Office Park).

Users: 24 engineering and maintenance staff (BAS), 9 security operations staff (PACS and video), 2 IT staff, the BAS integrator, the access control and video integrator, and the guard contractor (video viewing only). About 1,750 tenant employees hold credentials but do not log in to the system.

**Major components:**
- **SYS-01 BAS:** supervisory server (a virtual machine on the on-premises host at Property A), 2 engineering workstations, and about 420 BACnet field controllers across all three properties. Field controllers keep running their last programs and schedules if the server is lost.
- **SYS-02 PACS:** a cloud-hosted access control platform (vendor SaaS) with 46 on-premises door controllers, about 180 card readers, and 6 turnstile lanes. Door controllers cache credentials and keep working for up to 72 hours without the cloud service.
- **SYS-03 Video surveillance:** about 260 cameras and 4 network video recorders (NVRs), managed from the same vendor platform as SYS-02. Hosts the tailgating-detection pilot (P10 AI-001).
- **SYS-04 (OT portions):** the OT network segments, the firewalls shared with the corporate network, and the site-to-site VPN.
- **SYS-08 (part):** the BAS historian and energy dashboard, and the backup vault, in the company's cloud tenant.
- **SYS-09 (part):** the 2 engineering workstations, 24 engineering tablets, and 6 security console PCs.

SP 800-82 Rev. 3 names building automation systems and physical access control systems as operational technology (OT), so this plan treats the BAACS as an OT system and uses the SP 800-82 Rev. 3 guidance where IT practices do not fit (for example, no active vulnerability scans of field controllers).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it affects the BAACS |
|---|---|---|---|
| C-COMMERCIAL-FACILITIES-R05 | CISA Cross-Sector Cybersecurity Performance Goals 2.0 (**voluntary**) | CISA CPG 2.0 (December 2025) | Adopted by the COO as the security baseline; goal IDs cited in `control-implementation.csv` (see P03 section 1.2) |
| C-COMMERCIAL-FACILITIES-R02 | FTC Act Section 5 | 15 U.S.C. 45(a) | Security and data practice statements to tenants about badge, visitor, and video data must be accurate and reasonable |
| State | Florida Information Protection Act | Fla. Stat. 501.171(2) (reasonable measures), (3)-(6) (breach notice), (8) (disposal) | PACS and visitor data include personal information, for example driver license numbers from visitor ID scans |
| Contract | Lease security and notice clauses | 2023 and later lease template; 12 tenants with a 72-hour notice clause | Tenant notice after unauthorized access to tenant employee data in the PACS (P08) |
| Guidance | NIST SP 800-82 Rev. 3 | Final, September 2023 | OT architecture (zones and conduits) and the OT overlay (Appendix F) used to tailor this plan |
| Internal | Security policies POL-01 to POL-05 | P06 | Approved 2026-08-31 |

Not applicable to this system:
- **PCI DSS v4.0.1 (C-COMMERCIAL-FACILITIES-R01):** no account data enters the BAACS. Card payments use stand-alone P2PE terminals (SYS-10), which are outside this boundary (see P03).
- **CIRCIA (C-COMMERCIAL-FACILITIES-R06):** proposed rule only; the company would not be covered as proposed (P03).
- **CCPA/CPRA (R03) and SEC disclosure (R04):** the company does not do business in California and is privately held.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Chief Operating Officer (system owner) on 2026-08-31.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- The COO accepted continued operation of the BAACS on 2026-08-31, with the conditions in the P07 POA&M.
- The majority owner accepted the three High risks in P01 (R-001, R-002, R-003) only with dated treatment plans. The first condition is that the integrator's always-on remote-support tool is removed by 2026-10-31 (POAM-001).
### 4.3 System Operational Status
Operational. Major modifications planned:
- Remote access gateway for integrators (POAM-001), due 2026-10-31
- Backup redesign to a separate, immutable account (POAM-004), due 2026-12-31
- OT segmentation at all three properties (POAM-006, POAM-007), due 2027-03-31
- BAS server operating system and software upgrade (POAM-016), due 2027-03-31

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Chief Operating Officer | Overall accountability; accepts Moderate risks; approves this plan |
| Risk acceptor (authorizing official equivalent) | Majority owner (CEO) | Accepts High and Very High risks |
| Security lead | IT Manager | Day-to-day security; maintains this plan, the risk register, and the POA&M |
| BAS owner | Director of Engineering | BAS configuration, integrator oversight, manual operating procedures |
| PACS and video owner | Security Manager | Badge administration, video, visitor management, guard contractor |
| BAS operators | Chief Engineers (3) | Daily operation and hand control of plant equipment |
| Operations support | Managed service provider (MSP) | Firewalls, corporate endpoint patching, EDR monitoring (24x7) |
| Vendor support | BAS integrator; access control and video integrator | Programming, device service, remote support |

## 6. System Information Types and System Categorization
Information types were adapted from NIST SP 800-60 Vol. 2 Rev. 1 for a private company. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Facilities and equipment management (BAS setpoints, schedules, programs, building drawings) | Low | Moderate | Moderate | Tampering can stop cooling or damage equipment. Field controllers keep running and engineers can run plant equipment by hand, so loss is serious but not catastrophic (P05 BP-02 MTD 24 h). Life-safety systems are separate (read-only relays) |
| Physical security management (door schedules, credentials, access events, video) | Moderate | Moderate | Moderate | Credential or video disclosure harms tenant employees; a wrong door schedule leaves entrances unsecured. Cached credentials and guard posts limit availability impact (P05 BP-01 MTD 4 h) |
| Personal identity and authentication (tenant employee badge records and photos, visitor records at the SYS-11 interface) | Moderate | Moderate | Low | Personal information under Fla. Stat. 501.171 when combined with ID numbers; outage handled by paper logs |
| **BAACS category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored with the SP 800-82 Rev. 3 OT overlay for a 60-person company. The plan documents 67 controls (64 from the Moderate baseline and 3 program controls, PM-1, PM-2, and PM-9, selected by tailoring) that implement the CPG 2.0 goals and the OT hygiene the risk register depends on. Every other Moderate-baseline control is treated as follows:
- **Inherited** from the access control platform vendor and the cloud provider, as evidenced by their SOC 2 reports (P09).
- **Out of scope for this tier**, recorded as a tailoring decision, where the control's purpose applies mainly to federal systems or larger programs.
- **Compensating controls** are recorded where OT devices cannot support a control. Example: BACnet traffic is not encrypted, so segmentation (AC-4) compensates for SC-8.

## 7. Authorization Boundary Description
The boundary contains company-managed components and the company's configuration of vendor services:
- **Inside:** the BAS server and 2 engineering workstations; about 420 field controllers; 46 door controllers, about 180 readers, and 6 turnstile lanes; about 260 cameras and 4 NVRs; the OT network segments and the firewalls that enforce them; the company's tenant configuration, roles, and door groups in the access control and video platform; the BAS historian VM and the backup vault in the cloud tenant; 6 security console PCs and 24 engineering tablets.
- **Outside (interconnected external services):** the access control and video platform vendor's cloud infrastructure; the cloud provider's infrastructure; the identity provider (SYS-05, a separate SaaS service); the visitor management service (SYS-11); the integrators' own networks and devices; the life-safety systems (SYS-13).
- **Outside (not connected):** the P2PE card terminals (SYS-10) and all corporate SaaS except the identity provider.

**Life-safety design rule.** Fire alarm panels, elevator controls, and emergency voice communication stay on separate vendor-maintained networks. The BAS reads fire alarm status only through hardwired, read-only relay points. No change may create a network path from the BAACS to a life-safety system (PL-8).

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Access control and video platform (vendor cloud) | Bidirectional (door controllers and NVRs to cloud over TLS) | Credentials, door events, schedules, video clips | SaaS subscription agreement; vendor SOC 2 Type 2 report (P09) |
| Identity provider (SYS-05) | Inbound authentication | Administrator sign-in to the platform portal and cloud console | SaaS agreement |
| Visitor management (SYS-11) | Outbound visitor passes to turnstiles | Visitor name, host, pass validity | SaaS agreement; **no retention or breach terms (gap, R-012)** |
| BAS historian (SYS-08) | Outbound trend data from the BAS server over the site-to-site VPN | Temperatures, run status, energy meters | Company-managed |
| BAS integrator | Inbound remote support | Full BAS server control | Service agreement; **always-on tool, shared account, no MFA (gap, POAM-001)** |
| Access control and video integrator | Inbound, on site and through the vendor portal | Device configuration | Service agreement; **no security terms (gap, POAM-018)** |
| Guard contractor | Inbound video viewing through the vendor cloud console | Live and recorded video | Guard services agreement; named accounts pending (R-029) |
| Life-safety systems (SYS-13) | Inbound only, hardwired relay points | Fire alarm status | Design rule (section 7) |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| BAS supervisory server | Virtual machine (on-premises host) | Property A server room | Director of Engineering |
| Engineering workstations (2) | Endpoint | Property A engineering office | Director of Engineering |
| BACnet field controllers (about 420) | OT device | All properties | Director of Engineering |
| Access control and video platform tenant | SaaS | Platform vendor | Security Manager |
| Door controllers (46), readers (about 180), turnstile lanes (6) | OT device | All properties | Security Manager |
| Cameras (about 260) and NVRs (4) | OT device | All properties | Security Manager |
| Security console PCs (6) | Endpoint | Property A security console | Security Manager |
| Engineering tablets (24) | Mobile device | All properties | Director of Engineering |
| Firewalls (3), OT switches | Network | All properties (MSP-administered) | IT Manager |
| BAS historian VM and backup vault | Cloud VM and backup service | Cloud tenant | IT Manager |

There is no complete device-level OT inventory yet. Building it is POAM-013 (CM-8), due 2026-12-31.

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 67 controls:
- Implemented: 13
- Partially implemented: 39
- Planned: 15
- Inheritance: 47 system-specific, 19 hybrid, 1 common (inherited from providers)

### 10.2 Control assessment status
An independent assessor tested 22 of these controls from 2026-08-03 to 2026-08-07. See P07 `assessment-plan.md`, `assessment-results.csv`, and `poam.csv`. The test of IA-5 found manufacturer default passwords on 12 field controllers at Property B and on 2 NVRs, which were not known before.

## 11. Digital Identity Acceptance Statement
- **Company staff and administrators:** authenticate through the identity provider with a password and a second factor. Administrators of the access control platform and the cloud console use phishing-resistant hardware keys. This is appropriate for privileged access to a Moderate OT system.
- **BAS local accounts:** the BAS software does not support the identity provider. Until the upgrade (POAM-016), BAS access uses named local accounts behind the remote access gateway, which enforces MFA (POAM-001, POAM-003). The shared "engineer" account is being retired (POAM-010).
- **Integrators:** named accounts with MFA through the remote access gateway, with per-session approval by a chief engineer.
- **Tenant employees:** hold physical credentials (cards) only. They do not log in to the system. Card issuance is authorized by each tenant's designated contact (PE-2).

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness and vendor report review (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **BAACS:** Building Automation and Access Control System
- **BACnet:** a standard communication protocol for building automation devices
- **BAS:** building automation system
- **CPG:** CISA Cross-Sector Cybersecurity Performance Goals
- **EDR:** endpoint detection and response
- **MFA:** multi-factor authentication
- **MSP:** managed service provider
- **NVR:** network video recorder
- **OT:** operational technology
- **P2PE:** point-to-point encryption (PCI)
- **PACS:** physical access control system
- **POA&M:** plan of action and milestones

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan | IT Manager |

Next review: 2027-08-31, or sooner after the OT segmentation cutover or the BAS upgrade.
