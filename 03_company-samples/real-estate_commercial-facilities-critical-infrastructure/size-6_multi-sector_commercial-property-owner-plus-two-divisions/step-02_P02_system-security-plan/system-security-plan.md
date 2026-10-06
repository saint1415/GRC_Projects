# System Security Plan: Group Building Automation and Access Control System (BAACS)

**Organization:** Cris Santos Company Holdings, Inc. (corporate shared services, serving the Commercial Property, Construction, and Hotels divisions) | **Tier:** Multi-Sector | **Vertical:** Commercial Facilities
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **OT guidance:** NIST SP 800-82 Rev. 3, *Guide to Operational Technology (OT) Security* | **Version:** 1.0, 2026-09-15

> **Why this system.** At this tier the SSP can cover one system per division or a shared corporate system. The group chose the **BAACS**, a shared corporate system, because it controls heating, cooling, and physical access in every building the group owns, operates, or manages; it is serviced by the Construction division's BTI unit; and it carries the group's top risks (P01 GR-01 to GR-03). Each division keeps its own plans for its own primary systems (for example, the Hotels cardholder data environment, SYS-D7, documented for the PCI DSS assessment, and the Construction CUI enclave, SYS-D4, documented for CMMC), and they inherit from the same common control catalog.

## 1. System Name and Identifier
Group Building Automation and Access Control System (**BAACS**), identifier CSCH-SYS-G5. SYS-G5 in `../00_company-facts.md`.

## 2. System Overview
The BAACS lets the group run building systems from one place. It supports:
- **Commercial Property:** HVAC, lighting, metering, and physical access control and video at 142 owned properties, and the same services at 34 buildings managed for 9 investor owners.
- **Hotels:** HVAC, ventilation, and back-of-house door access at 88 hotels. Guest room locks are a separate hotel system (SYS-D8) and are not part of this plan.
- **Construction:** the BTI unit programs, services, and restores BAACS components, and badge access at group jobsites in group properties uses the same access control platform.

About 1,400 workforce users use it (RBOC operators, chief and building engineers, hotel engineers, security operations staff, and BTI technicians), plus about 1,100 tenant administrators who manage their own employees' badges.

**Scale** (section 7 of `../00_company-facts.md`): about 52,000 BAS field controllers, 311 site supervisory controllers at 264 sites, 7,800 door controllers, 26,000 card readers, 640 turnstile lanes, 31,000 cameras, and 1,150 network video recorders.

**Major components:**
- **Central BAS supervisor and historian:** virtual machines in the group cloud (provider A) that supervise every site, store trends and alarms, and push programs and schedules
- **Site supervisory controllers:** one or more per building; they talk BACnet to field controllers and connect to the central supervisor over the WAN
- **BAS field controllers:** chillers, air handlers, terminal units, lighting, and meters; they keep running their last programs and schedules if supervision is lost
- **Enterprise access control and video platform:** a vendor SaaS tenant with on-premises door controllers, readers, turnstiles, and video recorders; door controllers cache credentials for up to 72 hours
- **Remote Building Operations Center (RBOC):** 24x7 operator consoles at headquarters, with a secondary console room
- **Integrator remote access path:** the BTI remote access gateway in the provider A hub (named accounts, MFA, approval, recording) and, at 47 sites, legacy vendor remote-support tools (scenario gap 1)
- **Analytics features:** tailgating detection (23 office properties), the face verification pilot (2 office towers), and the BAS optimization service (41 buildings), all covered by P10

The platform is described by service category and is vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies to the BAACS |
|---|---|---|---|
| C-COMMERCIAL-FACILITIES-R05 | CISA Cross-Sector Cybersecurity Performance Goals 2.0 (voluntary) | CPG 2.0 (December 2025) | The group's adopted baseline for building OT. Voluntary; a gap is not a violation (P03) |
| C-COMMERCIAL-FACILITIES-R02 | FTC Act Section 5 | 15 U.S.C. 45(a) | Unreasonable security of badge holder, visitor, video, and biometric data, and statements to tenants about them |
| State law | State breach and reasonable-security laws | Each state where affected individuals reside (Florida worked example: Fla. Stat. 501.171(2), (3), (8)) | Badge holder records (name with credential data and photos), visitor ID numbers, and face templates are personal information in many states; Florida treats biometric data as personal information (P08) |
| C-COMMERCIAL-FACILITIES-R04 | SEC cybersecurity disclosure | Reg S-K Item 106; Form 8-K Item 1.05 | A BAACS incident affecting many buildings may be material to the group (P08) |
| C-COMMERCIAL-FACILITIES-R03 | CCPA/CPRA and 2026 CPPA regulations | Cal. Civ. Code 1798.100 et seq.; Cal. Code Regs. tit. 11, 7120-7124 | Applies to staff and visitor data at the 2 California hotels; the group's first cybersecurity audit report is due 2028-04-01 (P03) |
| N23-R03 | DFARS 252.204-7012 | 48 CFR 252.204-7012 | Not applicable to the BAACS itself. It matters because the BTI unit, which services the BAACS, also holds client drawings, and CUI was found in its repository (P03, P07) |
| N72-R01 | PCI DSS v4.0.1 | PCI SSC standard (contractual) | Out of scope: no card data in the BAACS. Hotel back-of-house doors on the BAACS protect rooms that hold card terminals, so physical access evidence supports the Hotels assessment |
| Contracts | Leases (2023 and later), property management agreements, intercompany services agreement (2021) | Contract terms | Tenant notice of unauthorized access to badge data (72 hours for 410 tenants); 48-hour incident notice to investor owners; no security terms for the BTI unit (POAM-018) |
| Internal | Group policies POL-01 to POL-05, the OT security standard, and division supplements | P06 | |

Not applicable: HIPAA (no covered entity data), the FTC Safeguards Rule (no consumer financial products), and CIRCIA reporting (proposed rule only; P03).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Group CISO and the Group building technology director (system owner) on 2026-09-15, after the board risk committee review.

### 4.2 System Authorization Decision
The group is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- **Decision:** authorized to operate with conditions, 2026-09-15, by the Group CISO and the Group Chief Risk Officer (acceptance authority for High risks).
- **Conditions:** (1) remove all legacy remote-support tools from site supervisors by 2026-12-31 (POAM-006); (2) back up every site's configuration and controller programs to the group vault by 2027-03-31 (POAM-009); (3) no new analytics or optimization feature may be enabled without Group AI council approval (POAM-023); (4) sign security terms in the intercompany services agreement with the BTI unit by 2026-12-31 (POAM-018).
- **Reauthorization:** annually, or when segmentation reaches every owned property and hotel.

### 4.3 System Operational Status
Operational. **Major modifications planned:** OT segmentation at the remaining 150 owned and hotel sites (through 2027-12-31, POAM-007); a standby central supervisor in provider B (2027 Q2); OT monitoring sensors at all critical-occupancy sites (POAM-003).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Group building technology director | Accountable for the BAACS and this SSP; runs the RBOC |
| Authorizing official equivalent | Group CISO with the Group Chief Risk Officer | Authorization decision; High risk acceptance |
| OT security owner | Group OT security lead | OT standard, segmentation, OT monitoring, OT vulnerability management |
| Access control data owner | Commercial Property director of security operations | Badge issuance and revocation rules; video use; tenant administrator onboarding |
| Building operations owners | Commercial Property vice president of engineering; Hotels vice president of engineering | Site operation, manual procedures, change approval for their buildings |
| Integrator (internal supplier) | BTI unit general manager (Construction division) | Programming, service, restoration; Section 889 product screening |
| Privacy oversight | Group Chief Privacy Officer | Badge, video, visitor, and biometric data rules |
| Common control providers | Group identity director (SYS-G1), Group SOC director (SYS-G2), Group cloud and network director (SYS-G3) | Operate inherited controls (`common-control-catalog.csv`) |
| Independent assessor | Group internal audit | Assesses common controls once and samples BAACS and division controls (P07) |

## 6. System Information Types and System Categorization
Information types follow NIST SP 800-60 Vol. 2 Rev. 1 categories. Impact levels follow FIPS 199 and were adjusted for this system's operating context.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Facilities, fleet, and equipment management (BAS programs, setpoints, schedules, alarms) | Low | **High** | Moderate | Changing control logic at 264 sites at once could create unsafe heat, freezing, or ventilation loss for tenants and hotel guests. Field controllers run locally, so loss of supervision is Moderate (P05 BP-G04) |
| Security management (door schedules, access decisions, alarms, video) | Moderate | **High** | Moderate | Unauthorized access to tenant floors and back-of-house areas; video is evidence |
| Personal identity and authentication (badge holder records for about 236,000 tenant employees and group staff; face templates for about 1,900 pilot enrollees) | Moderate | Moderate | Moderate | Names, employers, photos, credential numbers, and access history. Face templates are handled as biometric data (P10) |
| Information security (integrator credentials, site configurations, keys, network designs) | **High** | **High** | Moderate | One set of credentials and designs opens every building; their loss is the path in the P08 scenario |
| System and network monitoring (logs) | Moderate | Moderate | Low | Needed for investigations and notices |
| **BAACS category (high-water mark)** | **High** | **High** | **Moderate** | Overall **High** |

**Baseline:** the NIST SP 800-53B **High** baseline, tailored with the OT overlay in NIST SP 800-82 Rev. 3. The plan documents **111 controls** in `control-implementation.csv`:
- 106 from the High baseline;
- 3 from the privacy baseline (PM-9, PT-2, PT-3), added because badge, video, and biometric data are the system's main privacy risk;
- 2 program management controls not in any baseline (PM-1, PM-2).

Other High-baseline controls are either fully inherited from the cloud providers and the platform vendor (for example, most PE controls for their data centers, evidenced by their SOC 2 Type 2 reports) or tailored out with a reason in the group tailoring register. OT tailoring examples: account lockout is a documented exception for older site supervisors that cannot support it (AC-7); device authentication is compensated by segmentation where field controllers cannot authenticate (IA-3).

**CSF 2.0 mapping:** the `csf2_subcategories` column uses NIST's CSF 2.0 to SP 800-53 Rev. 5 mapping (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`). For 14 controls the NIST mapping lists no subcategory; for those the column carries an author mapping.

## 7. Authorization Boundary Description
- **Inside:** the central BAS supervisor and historian accounts in provider A; the BAACS backups in the provider B vault; the access control and video platform tenant (configuration and data the group controls); site supervisory controllers, BAS field controllers, door controllers, readers, turnstiles, and video recorders at all 264 sites; RBOC consoles and engineering workstations; the BTI remote access gateway.
- **Outside, inherited (common control providers):** SYS-G1 identity, SYS-G2 SOC, SIEM, and EDR, and the SYS-G3 landing zone and WAN.
- **Outside, interconnected:** SYS-D5 BTI tools (configuration repository and credential vault), SYS-D2 visitor management, SYS-D6 hotel PMS (back-of-house badge requests), SYS-D1 work orders, the BAS optimization service, and the life-safety systems (fire alarm and elevator controls on separate vendor networks, connected only by read-only relay points).
- **Outside, external service providers:** the access control and video platform vendor (its own infrastructure, covered by its SOC 2 report), and the cloud providers.

The diagram is in P04 `cloud-architecture.md` (section 2.2).

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| SYS-D5 BTI configuration repository and credential vault | Both | Programs, site configurations, drawings, device credentials | Intercompany services agreement (2021) with **no security terms** (POAM-018) |
| BTI technicians (gateway and legacy tools) | Inbound sessions | Programming and service | Same; legacy tools at 47 sites bypass the gateway (POAM-006) |
| SYS-D2 visitor management | Inbound | Visitor passes and photos | Vendor contract (security addendum) |
| SYS-D6 hotel PMS | Inbound | Back-of-house badge requests for hotel staff | Internal |
| SYS-D1 property management platform | Both | Work orders; tenant contact lists for badge administration | Vendor contract |
| BAS optimization service | Both | Trend data out; setpoint commands in | Vendor terms only; **not reviewed** (POAM-023) |
| Tenant administrators | Inbound | Badge requests and revocations for their own employees | Lease and platform terms |
| Investor owners (managed buildings) | Outbound | Monthly operating reports | Property management agreements (48-hour incident notice) |
| Life-safety systems | Inbound only | Fire alarm and elevator status (relay points) | Vendor service contracts |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| Central BAS supervisor and historian | Virtual machines and managed database (IaaS/PaaS) | Provider A | Group building technology director |
| BTI remote access gateway | Virtual appliances (IaaS) | Provider A hub | Group OT security lead (operation); BTI unit (users) |
| Access control and video platform | SaaS tenant | Platform vendor | Commercial Property director of security operations |
| Site supervisory controllers (311) | OT appliances and small servers | 264 sites | Regional chief engineers; hotel engineers |
| BAS field controllers (about 52,000) | OT field devices | 264 sites | Regional chief engineers; hotel engineers |
| Door controllers, readers, turnstiles | OT field devices | 264 sites | Security operations |
| Network video recorders (1,150) and cameras (31,000) | OT devices | 264 sites | Security operations |
| RBOC consoles and engineering workstations | Managed endpoints | Headquarters; sites | Group building technology director |
| BAACS backups | Immutable object storage | Provider B vault | Group cloud and network director |

The OT asset inventory is about 74% complete (CM-8, POAM-008), so these counts are estimates for field devices.

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv` (111 controls) and `common-control-catalog.csv` (84 group common controls).

| Status | Controls |
|---|---|
| Implemented | 63 |
| Partially implemented | 47 |
| Planned | 1 (CP-7, standby central supervisor) |
| Not applicable | 0 |
| **Total** | **111** |

| Inheritance | Controls |
|---|---|
| Common/Inherited (from SYS-G1, SYS-G2, SYS-G3, or group functions) | 42 |
| Hybrid (a group provider or the platform vendor supplies the mechanism; the BAACS configures or operates part) | 43 |
| System-specific | 26 |

**The 47 partially implemented controls** cluster where IT practice has not yet reached the buildings:
- **Integrator and supplier access** (scenario gaps 1 and 4), 11 controls: AC-17, AC-17(1), AC-17(3), MA-4, AC-20, CA-3, SA-4, SA-9, SR-3, SR-6, PS-7.
- **Segmentation and hardening** (gap 1), 7 controls: AC-4, SC-7, SC-7(5), CM-6, CM-7, IA-3, CM-2.
- **Accounts and credentials**, 5 controls: AC-2, AC-2(12), AC-6, IA-2, IA-5.
- **Visibility and vulnerability management** (gap 2), 13 controls: AU-2, AU-6, AU-12, SI-4, SI-4(4), CM-8, RA-5, RA-9, SI-2, SA-22, SI-7, CA-8, MP-7.
- **Recovery** (gap 3), 5 controls: CP-2, CP-4, CP-9, CP-10, AT-3.
- **Incident handling and notification** (gap 7), 3 controls: IR-4, IR-6, IR-8.
- **Privacy and analytics** (gap 6), 3 controls: PT-2, PT-3, SI-12.

### 10.2 Common control inheritance by division
The common control catalog lists 84 controls provided by corporate. Inheritance is **documented** for Commercial Property (2025 inheritance matrix), for the Hotels card and guest systems (the PCI DSS responsibility matrix), for the Construction project delivery platform (the CMMC Level 1 scope), and for the BAACS (this plan). It is **not documented** for two places that matter most here:
- **the BTI tools (SYS-D5)**, which run in a Construction cloud account outside the group landing zone and hold credentials for every group building (scenario gap 4; POAM-018);
- **hotel building OT on the BAACS**, which the Hotels supplement does not mention.

### 10.3 Control assessment status
Common controls were assessed once, and BAACS and division controls sampled, from 2026-07-06 to 2026-08-28 by group internal audit. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
- **Workforce users** authenticate through SYS-G1 federated sign-in with MFA (number matching). **Administrators** use phishing-resistant authenticators and just-in-time PAM elevation. This fits a High-integrity system that is reachable remotely.
- **BTI technicians** authenticate through SYS-G1 and the gateway with MFA, except at the 47 sites with legacy tools, where a shared vendor account and no MFA are used (POAM-006).
- **Tenant administrators** authenticate to the platform with MFA (IA-8).
- **Devices:** new site supervisors and door controllers use device certificates; older field controllers cannot authenticate and rely on segmentation (IA-3).
- **Badge holders** are not system users; their credentials are physical or mobile badges managed in the platform. Legacy 125 kHz proximity badges remain at 19 older properties and can be cloned (P01 CF-024).

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), group and division risk registers (P01), gap analyses and regulation-by-division matrix (P03), cloud architecture and control map (P04), BIA (P05), group policies and division supplements (P06), assessment and POA&M (P07), incident response runbook and notification matrix (P08), SOC 2 readiness (P09), AI governance (P10).

## 13. Acronym List and Glossary
- **BACnet:** the building automation and control networking protocol used by field controllers
- **BAS:** building automation system
- **BAACS:** Group Building Automation and Access Control System
- **BTI:** Building Technology Integration unit (Construction division)
- **Common control:** a control provided once by corporate and inherited by several systems
- **NVR:** network video recorder
- **OT:** operational technology
- **RBOC:** Remote Building Operations Center
- **Site supervisor:** a site supervisory controller that connects a building's field controllers to the central supervisor
- **Zone and conduit:** the OT segmentation model in NIST SP 800-82 Rev. 3

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-08-28 | Draft after P07 fieldwork | Group building technology director |
| 1.0 | 2026-09-15 | Approved with authorization conditions | Group CISO |
