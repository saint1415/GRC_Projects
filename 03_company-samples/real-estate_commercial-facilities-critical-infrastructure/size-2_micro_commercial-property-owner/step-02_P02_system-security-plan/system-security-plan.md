# System Security Plan: Building Automation and Access Control System (BAACS)

**Organization:** Cris Santos Company, LLC (commercial office and retail property owner-operator) | **Tier:** Micro | **Vertical:** Commercial Facilities
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Building Automation and Access Control System (**BAACS**), identifier CSC-SYS-001.

## 2. System Overview
The BAACS runs the building side of the company's two Florida properties: heating, cooling, lighting, and metering at Property A (a 3-story office building with 21 tenants), door access at both properties, and video surveillance at both properties (Property B is a strip retail center with 12 tenants). Its users are 7 employees, the controls contractor, the security integrator, and the MSP. About 300 tenant employees, contractors, and staff hold the building credentials it manages.

The company owns little IT. The access control and video system is a vendor cloud platform, the MSP runs the office network and the backups, and the controls contractor services the BAS. This plan therefore says, for each control, what the company does itself, what a contractor does for it, and what it inherits from a vendor.

**Major components:**
- **SYS-01:** BAS at Property A: one front-end workstation (engineering room), one supervisory network controller, about 60 BACnet field controllers (4 rooftop units, 48 VAV boxes, 2 exhaust fans, a lighting relay panel, 3 utility meters)
- **SYS-02:** cloud access control platform with 9 door controllers and readers, 342 active fobs and phone credentials
- **SYS-03:** 28 cloud-managed cameras on the same platform, 30-day cloud recording
- **SYS-04:** property networks: Property A business firewall (MSP-managed), switches, staff and guest Wi-Fi; Property B ISP-supplied router
- **SYS-08 (part):** nightly cloud backup image of the BAS workstation (MSP-operated)
- **SYS-07 (part):** the Property Manager's and Building Engineer's laptops and the 3 engineering tablets used to administer the system

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies |
|---|---|---|---|
| C-COMMERCIAL-FACILITIES-R05 | CISA Cross-Sector Cybersecurity Performance Goals 2.0 | CISA CPG 2.0 (December 2025) | **Voluntary.** Adopted by the Managing Member as the security benchmark on 2026-07-15. OT lines applied with NIST SP 800-82 Rev. 3 |
| C-COMMERCIAL-FACILITIES-R02 | FTC Act Section 5 | 15 U.S.C. 45(a) | Unreasonable security of credential holder data and video, and any undisclosed use of video analytics |
| State | Florida Information Protection Act | Fla. Stat. 501.171(2), (4), (6), (8) | Reasonable measures for personal information; breach notice; third-party agent notice; disposal. Badge holder names, credential numbers, and door history are not listed data elements; whether door history is "information regarding an individual's geolocation" and whether face match templates are "biometric data" are open questions for counsel (P08, P10) |
| C-COMMERCIAL-FACILITIES-R01 | PCI DSS v4.0.1 (SAQ P2PE) | PCI SSC | **Outside this boundary.** The P2PE terminal (SYS-09) is stand-alone on cellular and never touches the BAACS networks. Analyzed in P03 |
| Internal | Security policies POL-02, POL-03, POL-04 | P06 | Approved 2026-08-31 |

Not applicable: CCPA/CPRA (R03; no California business), SEC disclosure rules (R04; privately held), CIRCIA (R06; proposed rule only, and the company is under its SBA size standard; see P03).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Managing Member on 2026-08-31.

### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization. The equivalent internal decision: on 2026-08-31 the Managing Member accepted continued operation of the BAACS on the condition that the POA&M items in P07 are completed by their dates, and the four High risks in P01 (R-001, R-002, R-003, R-005) are treated by 2026-12-31.

### 4.3 System Operational Status
Operational. Planned changes by 2026-12-31: replacement of the contractor remote-desktop tool with an approved remote access service (R-001), immutable backups and restore tests (R-002), a building-device network segment at each property (R-003), MFA on platform administrator accounts (R-005), and EDR on office computers and the BAS workstation.

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner and risk acceptor | Managing Member | Overall accountability; accepts Moderate and higher risk; approves this plan, policies, and spending |
| Security and privacy lead | Property Manager | Day-to-day security; maintains this plan, the risk register, and the vendor file; owns access control and video; incident lead |
| BAS owner | Building Engineer | BAS workstation and controllers; approves and watches controls contractor sessions; manual operation |
| Credential administration | Tenant Services and Leasing Coordinator | Issues and disables credentials on tenant requests (operator role only) |
| IT operations | MSP | Office computers, Property A firewall and Wi-Fi, suite administration, cloud backup |
| BAS maintenance | Controls contractor | Programs, software, and remote support for the BAS |
| Door and camera hardware | Security integrator | Installation and repair of door hardware and cameras |
| Independent assessor | Security consultant with OT experience | Annual control assessment (P07) |

**Where roles overlap.** The Property Manager both runs access control and leads security, and nobody on staff reviews the Property Manager's own administrator activity. Compensating measures: the Managing Member reviews the platform administrator change report at the monthly security meeting, and the annual assessment is done by an outside consultant.

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Facilities, fleet, and equipment management (building control data: setpoints, schedules, controller programs) | Low | Moderate | Moderate | Wrong setpoints or schedules cause tenant discomfort and possible heat stress; hand operation limits availability impact to about one day (P05 MTD 24 h) |
| Personal identity and authentication (credential holder data, door history, badge photos) | Moderate | Moderate | Moderate | Disclosure harms tenant employees and tenants; altered credentials open doors; doors keep working offline (P05 MTD 24 h) |
| Security management (video, door alarms, floor plans) | Moderate | Moderate | Low | Footage and layouts can help plan theft or attack; patrols cover outages (P05 MTD 48 h) |
| **BAACS category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 7-person company. The plan documents 42 controls that carry the CPG 2.0 goals relevant to building systems and basic cyber hygiene (see `control-implementation.csv`). Other Moderate-baseline controls are handled in one of two ways:
- **Inherited** from the platform vendor (its data centers, application security, encryption, availability), with its SOC 2 Type 2 report as evidence (P09).
- **Tailored out** for this tier where the control assumes federal program management or a dedicated IT staff (for example, a configuration control board or a separate test environment). These are tailoring decisions, not gaps.

**OT tailoring (NIST SP 800-82 Rev. 3).** Controls on the BAS are applied without risking operation: patches and antivirus on the BAS workstation only with the controls contractor's approval and a tested rollback; no active scanning of field controllers during occupied hours; changes to controllers only under a contractor session the Building Engineer has approved.

## 7. Authorization Boundary Description
- **Inside:** the BAS at Property A (SYS-01); the company's tenant of the access control and video platform, its door controllers, readers, and cameras (SYS-02, SYS-03); the Property A firewall, switches, and Wi-Fi and the Property B router (SYS-04); the BAS workstation image in the cloud backup (part of SYS-08); the 2 administrator laptops and 3 engineering tablets (part of SYS-07).
- **Outside (external services, interconnected):** the platform vendor's cloud and data centers; the MSP's remote management platform; the controls contractor's and security integrator's own systems; the productivity suite, property management system, payroll, and tenant screening services (business systems that share users and devices but hold no building control function); the P2PE terminal; life-safety systems (fire alarm, elevators, emergency phones), which have no connection to the BAACS.

**Design rule:** the BAS must never be connected to a fire alarm or elevator control circuit, and no building device may be reachable from the internet. The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Agreement |
|---|---|---|---|
| Platform vendor cloud (from door controllers and cameras) | Bidirectional | Credentials, schedules, door events, video | Platform subscription terms; SOC 2 report |
| Controls contractor (remote-desktop tool on the BAS workstation) | Inbound administrative access | BAS programs, setpoints, graphics | Service agreement; **no security terms (gap)** |
| Security integrator (platform administrator account) | Inbound administrative access | Door and camera configuration | Service agreement; **no security terms (gap)** |
| MSP remote management platform | Inbound administrative access | Office computers and firewall | MSP contract; no incident notice clause (gap) |
| Cloud backup service (MSP subcontractor) | Outbound | BAS workstation image | Through the MSP; no direct agreement |
| Tenant contacts (tenant portal form, email) | Inbound | Credential requests | Lease clauses |
| Property management system (work orders) | None automated | Engineers enter work orders by hand on tablets | Vendor terms |

## 9. System Component Inventory
| Component | Type | Location or provider | Owner |
|---|---|---|---|
| BAS front-end workstation, supervisory controller, about 60 field controllers (SYS-01) | OT endpoint and controllers | Property A engineering room and mechanical spaces | Building Engineer |
| Access control tenant, 9 door controllers and readers (SYS-02) | SaaS plus OT devices | Platform vendor; doors at both properties | Property Manager |
| 28 cameras (SYS-03) | SaaS plus devices | Platform vendor; both properties | Property Manager |
| Property A firewall, switches, Wi-Fi; Property B router (SYS-04) | Network | Network closets | Property Manager (MSP operates Property A) |
| BAS workstation image (SYS-08) | SaaS backup | Cloud backup service (MSP subcontractor) | Building Engineer (MSP operates) |
| 2 administrator laptops, 3 engineering tablets (SYS-07) | Endpoint | Staff | Property Manager |

A full device inventory with serial numbers and firmware does not exist yet (CM-8; POAM-005).

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 42 controls:
- Implemented: 9
- Partially implemented: 24
- Planned: 9
- Not applicable: 0

By responsibility: 17 system-specific (the company), 24 hybrid (the company with a vendor, the MSP, or a contractor), 1 common/inherited (fully provided by vendors: AC-7 lockout).

### 10.2 Inherited and contractor-provided controls
| Provider | What the company relies on | Evidence | What the company must still do |
|---|---|---|---|
| Access control and video platform vendor | Platform security, encryption, availability, backups of the credential database, lockout (AC-7), audit logs (AU-2, AU-11), automatic device firmware | SOC 2 Type 2 report reviewed 2026-08-20 (P09) | Complementary user entity controls: administrator account management and MFA, timely credential removal, review of administrator activity |
| MSP | Patching (SI-2) and antivirus (SI-3) on office computers, Property A firewall (SC-7), backup operation (CP-9), external scans (RA-5) | Monthly MSP reports; P07 evidence requests | Direct the work, approve exceptions in writing, review reports monthly, yearly MSP review |
| Controls contractor | BAS software, controller programs, remote support (MA-4) | Service agreement only | Approve and watch sessions; get copies of controller programs; add security terms |
| Cloud backup service (MSP subcontractor) | Storage of the BAS workstation image (CP-9) | None until the first restore test | Restore test by 2026-10-15; immutable retention |

**Inherited does not mean done.** Two of the platform vendor's complementary user entity controls are open gaps at the company: MFA on administrator accounts (IA-2(1)) and timely credential removal (PE-2, AC-2).

### 10.3 Control assessment status
Assessed 2026-08-10 to 2026-08-12 by an independent consultant. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
Staff sign in to the productivity suite and the property management system with a password and an authenticator app. Platform administrators will use the same once MFA is enabled (POAM-002, due 2026-09-30); until then, platform administrator access is single-factor, which is below what this Moderate system needs. Credential holders authenticate to doors with something they have (a fob or a phone credential); from 2026-10-15, after-hours entry at the Property A front entrance also requires a PIN, the non-biometric alternative chosen in P10.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness and platform vendor report review (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **BAACS:** Building Automation and Access Control System
- **BACnet:** a standard communication protocol for building automation devices
- **BAS:** building automation system
- **CPG:** CISA Cross-Sector Cybersecurity Performance Goals
- **EDR:** endpoint detection and response
- **MFA:** multi-factor authentication
- **MSP:** managed service provider
- **OT:** operational technology
- **P2PE:** point-to-point encryption
- **POA&M:** plan of action and milestones
- **VAV:** variable air volume (a box that controls airflow to one zone)

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan | Property Manager (security and privacy lead) |
