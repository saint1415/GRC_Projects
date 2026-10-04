# System Security Plan: Field SCADA and Production Accounting System (FSPA)

**Organization:** Cris Santos Company, Inc. (PE-backed independent crude oil producer with a Panhandle gathering system) | **Tier:** Mid-Market | **Vertical:** Mining, Quarrying, and Oil and Gas Extraction
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-16

## 1. System Name and Identifier
Field SCADA and Production Accounting System (**FSPA**), identifier CSC-FSPA-01. The FSPA is the company's major system. Its components are listed in `../00_company-facts.md` section 3 (SSP system line).

## 2. System Overview
The FSPA lets the company watch and control its oil fields and gathering system, measure what it delivers, and turn production into sales, shipper statements, royalty payments, and partner billings. It covers 3 operating areas (640 wells, 16 tank batteries, 3 injection plants, 4 compression stations) and the 92-mile Panhandle gathering system with its pump station and 6 LACT units. It is staffed around the clock from the Operations Control Center (OCC), with a Backup Control Center (BCC) at the Alabama field office, and used by about 420 people: Production Controllers, lease operators and gaugers, gathering operators, automation technicians, engineers, measurement staff, and production accounting staff.

**Major components:**
| ID | Component | Hosting and service model |
|---|---|---|
| SYS-01 | SCADA control centers: primary server pair, historian, 12 HMIs, 4 engineering workstations (OCC); 3 HMIs (South Florida office); standby server and 4 HMIs (BCC) | On-premises OT |
| SYS-02 | Field devices and communications: about 610 RTUs and PLCs, 130 ESP drives, 260 flow meters, 6 LACT flow computers, pump station PLC, licensed radio, 180 cellular modems, 2 microwave links | Field sites |
| SYS-12 | OT remote access: jump host in the OT DMZ (plus the vendor exceptions in gap 3) | On-premises |
| SYS-14 | Crude measurement and shipper services: flow computer polling, measurement data service, shipper portal | SCADA network; cloud OT data and business workloads accounts |
| SYS-08 (part) | OT DMZ at the OCC; SCADA network segments; site firewalls at the South Florida office and BCC | On-premises |
| SYS-04 (part) | OT data account (historian replica, measurement data service); business workloads account (field data capture app, volume integration service, shipper portal); backup account | Public cloud IaaS/PaaS, vendor-agnostic (P04) |
| SYS-03 (configuration) | Production accounting and revenue distribution tenant | Vendor SaaS; vendor SOC 2 Type 2 |
| SYS-05 (configuration) | Identity provider tenant for FSPA users | SaaS |
| SYS-09 (part) | 240 rugged tablets | Company-managed mobile |
| SYS-13 (part) | OT passive monitoring sensors (OCC and Panhandle Central Facility) | On-premises |

**What the system does not do:** it does not perform safety functions. H2S detection, tank high-level shutdowns, compressor emergency shutdowns, and the gathering pump station's high-pressure shutdown switches are hardwired and work without SCADA. This design limits how much harm a SCADA compromise can cause and is the basis for keeping integrity at Moderate (section 6).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it affects the FSPA |
|---|---|---|---|
| N21-BM | NIST CSF 2.0 with NIST SP 800-82 Rev. 3, including the SP 800-82 Rev. 3 OT overlay (Appendix F) | NIST CSWP 29; SP 800-82 Rev. 3 | Voluntary benchmark adopted by the company (P03); basis for tailoring |
| N21-P195 | Pipeline safety rules for the gathering system | 49 CFR 195.11 (regulated rural gathering line, 14 miles); 195.15 and Subpart B (reporting-regulated lines and reporting) | The FSPA holds the pressure setpoints that support operation at MOP (195.11(b)(5)), the data needed for accident reports (195.50, 195.54), and the alarm path that starts the 1-hour telephone notice (195.52). Records must be retained (195.11(d)) |
| Federal | Oil discharge notice | 40 CFR 110.6 | Applies if a SCADA failure or attack leads to a discharge that reaches water; drives the P08 notification matrix |
| State | Florida Information Protection Act (worked example; other states generically) | Fla. Stat. 501.171(2)-(6) | Royalty owner and employee personal information in production accounting and the data platform |
| Contract | Gathering agreements with 5 shippers | Contract | Measurement accuracy, statement timeliness, confidentiality of shipper data; SOC 2 Type 2 requested by the largest shipper (P09) |
| Contract | Cyber insurance policy | Contract | MFA required on all remote access (gap 3 puts this at risk) |
| Internal | Security policies POL-01 to POL-05 and standards STD-01 to STD-10 | P06 | Policy basis for every control |

**Not applicable** (see P03 section 1):
- N21-R01, the USCG Marine Transportation System cyber rule (33 CFR 101.605): no vessel, waterfront facility, or OCS facility.
- N21-R02, TSA Security Directive Pipeline-2021-02G: the company has received no TSA notification for its gathering system.
- N21-R03, CIRCIA: proposed only; as proposed, the company is SBA-small and meets no sector criterion.
- PHMSA control room management (49 CFR 195.446) and the procedural manual (195.402): not among the requirements that 195.11(b) applies to regulated rural gathering lines. The company applies parts of both voluntarily (alarm review, shift handover, emergency procedures), which is why CP-2 cites 195.402(e) as voluntary.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Chief Operating Officer (system owner) on 2026-09-16, after the control assessment (P07), with the VP Operations agreeing to the field-operations items.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization to operate. The equivalent internal decision:
- **Decision:** continued operation of the FSPA accepted with conditions, 2026-09-16.
- **Authorizing official equivalent:** Chief Executive Officer for High risks; Chief Operating Officer for Moderate and below (P01 acceptance authorities).
- **Conditions:**
  - the compression station packager gateways must be removed from the internet and placed behind the jump host by 2026-10-31 (POAM-002);
  - the High-risk POA&M items must meet their milestones, reported quarterly to the audit committee;
  - re-decision by 2027-09-30 or after a major change (for example a gathering system expansion or a TSA notification).
### 4.3 System Operational Status
Operational. Major modifications planned:
- OT DMZ extended to the BCC and the South Florida office (P01 R-001), due 2027-03-31.
- BCC standby server and South Florida HMIs upgraded to a supported operating system (R-005), due 2027-03-31.
- OT monitoring sensors in South Florida and Alabama with 24x7 OT alert coverage (R-011), due 2027-06-30.
- Full BCC failover test (R-014), due 2027-04-30.

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Chief Operating Officer | Accountable for the FSPA; accepts Moderate risk; executive sponsor of the security program |
| Authorizing official equivalent (High risk) | Chief Executive Officer | Accepts High risk; approves the risk appetite |
| Oversight | Board audit committee | Quarterly cyber risk reporting |
| Information Security Lead | Security Manager | Program owner day to day; SSP owner; corporate, cloud, and SaaS controls; MDR oversight |
| OT technical owner | SCADA and Automation Manager | SCADA servers, HMIs, field devices, integrator oversight, OT change control |
| OT security | OT Security Engineer | OT DMZ, jump host, OT sensors, OT patching (dotted line to the Security Manager) |
| Operations owner | VP Operations | Agrees to risk decisions that affect field operations or safety |
| Control room | Control Room Manager | OCC and BCC operations, Production Controller training, physical access |
| Pipeline compliance | Pipeline Compliance Manager | Part 195 duties for the gathering system |
| Data owners | Production Accounting Director (production and royalty data); Measurement Supervisor (LACT and shipper data) | Data classification, access approval, and integrity checks |
| IT infrastructure | VP IT | Identity provider, cloud landing zone, corporate networks, endpoints |
| Independent assessment | Co-sourced internal audit firm | Annual assessment (P07) |
| Monitoring | MDR provider | 24x7 IT monitoring and host isolation |
| Operations support | SCADA integrator (contractor) | SCADA configuration and remote support through the jump host |

## 6. System Information Types and System Categorization
Information types come from NIST SP 800-60 Vol. 2 Rev. 1, which gives provisional impact levels for federal systems; the company adjusted them for its own operations, as the publication allows. Impact levels follow FIPS 199.

| Information type (SP 800-60 Vol. 2 Rev. 1) | Provisional (C, I, A) | Company rating (C, I, A) | Rationale |
|---|---|---|---|
| Energy Production (D.7.4): process data, setpoints, controller logic, gathering pressures | Low, Low, Low | Low, **Moderate**, **Moderate** | Changed setpoints or logic could cause equipment damage, a release from the gathering system, or an injection permit violation; hardwired shutdowns keep the worst case below High. Loss of SCADA forces manual operations and, after 8 to 24 hours, shut-ins (P05) |
| Energy Supply (D.7.1): LACT tickets, run tickets, shipper volumes, sales | Low, Moderate, Moderate | **Moderate**, Moderate, Moderate | Wrong volumes misstate sales, shipper statements, and royalties; shipper volumes are confidential under the gathering agreements; storage gives 48 to 72 hours before shut-in |
| Payments (C.3.2.5): royalty and partner distributions | Low, Moderate, Low | **Moderate**, Moderate, Low | Owner records include Social Security numbers and bank details covered by state breach laws |
| **FSPA category (high-water mark)** | | **Moderate, Moderate, Moderate** | |

**Integrity was considered for High.** A manipulated pressure setpoint at the gathering pump station could, in theory, contribute to a release near a drinking water unusually sensitive area. The team kept integrity at Moderate because the pump station's high-pressure shutdown switches are hardwired and independent of SCADA, and line riders and the 1-hour notice procedure limit consequences. To compensate, the plan adds integrity-focused tailoring: CM-3, CM-5, and SI-7 statements cover pump station setpoints and flow computer configuration, and the change record for MOP-related setpoints is part of the Part 195 records.

## 7. Authorization Boundary Description
**Inside the boundary:**
- the OCC and BCC server rooms, HMIs, and engineering workstations, and the 3 South Florida HMIs;
- the SCADA network segments, the OT DMZ, and the site firewalls at the South Florida office and BCC;
- all field controllers, LACT flow computers, the pump station PLC, and field communications;
- the OT jump host and the vendor remote access paths (including the gateways to be removed);
- the OT data account, the FSPA workloads in the business workloads account, and the backup account;
- the production accounting tenant configuration and user roles, and the identity provider tenant for FSPA users;
- the 240 rugged tablets and the OT monitoring sensors.

**Outside the boundary (external services, interconnected):**
- the production accounting vendor's platform, the cloud provider's infrastructure, and the identity provider's platform;
- the cellular carrier's private network and the microwave link provider;
- the third-party transmission pipeline (receipt of LACT data), the 5 shippers, the crude purchasers, and the gas gathering companies;
- the SCADA integrator's, compressor packager's, and flow computer vendor's own networks;
- the MDR provider's platform;
- the corporate network beyond the OT DMZ and site firewalls.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Corporate network (SYS-08) | Through the OT DMZ at the OCC; through site firewalls at South Florida and the BCC | Historian replica feed; jump host sessions; patch staging | Internal rule sets; **broad rules at South Florida and the BCC (gap 1)** |
| OT data account (SYS-04) | Outbound from the historian and measurement collector through the OT DMZ | Process data; LACT tickets and proving records | Internal |
| Production accounting SaaS (SYS-03) | Outbound from the volume integration service | Daily allocated volumes, run tickets, LACT tickets | SaaS agreement; SOC 2 Type 2 |
| Shippers (5) | Outbound statements on the shipper portal | Daily volumes and quality | Gathering agreements; **no data handling or incident notice terms (gap 8)** |
| Third-party transmission pipeline | Bidirectional (LACT data, nominations) | Delivered volumes; pressure at the receipt point | Connection agreement |
| SCADA integrator (SYS-12) | Inbound remote access through the jump host | SCADA administration | Master services agreement; security schedule added 2025 |
| Compressor packager | Inbound always-on cellular gateways at 4 stations | Compressor control and diagnostics | Service agreement; **no security terms; bypasses the jump host (gap 3)** |
| Flow computer vendor | Inbound support modem at the Central Facility | Flow computer configuration | Support agreement; **bypasses the jump host (gap 3)** |
| Cellular carrier | Transport (private network) | RTU polling for 180 sites | Carrier contract |
| MDR provider | Inbound logs; remote isolation of IT hosts | Security events | Contract; SOC 2 Type 2; OT excluded |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| Primary SCADA server pair, historian | Servers (supported OS since 2025) | OCC server room | SCADA and Automation Manager |
| HMIs (12) and engineering workstations (4) | Workstations | OCC | Control Room Manager; SCADA and Automation Manager |
| HMIs (3) | Workstations (unsupported OS, **gap 4**) | South Florida field office | SCADA and Automation Manager |
| Standby SCADA server and HMIs (4) | Server and workstations (unsupported OS, **gap 4**) | BCC, Alabama field office | Control Room Manager |
| Offline SCADA image storage | Removable encrypted drives | BCC safe (reachable network location for staging, **gap 1**) | SCADA and Automation Manager |
| RTUs and PLCs (about 610), ESP drives (130), flow meters (260) | Field controllers | Well pads and facilities | SCADA and Automation Manager |
| LACT units (6) with flow computers; pump station PLC | Measurement and control | Panhandle Central Facility | Measurement Supervisor; Pipeline Compliance Manager |
| Licensed radio, microwave links, cellular modems (180) | Communications | Field sites and towers | SCADA and Automation Manager |
| OT DMZ firewalls, jump host, patch staging server | Network and management | OCC | OT Security Engineer |
| Site firewalls | Network | South Florida office; BCC | VP IT |
| OT passive monitoring sensors (2) | Security monitoring | OCC; Central Facility | OT Security Engineer |
| Historian replica, measurement data service | Cloud VM and managed database | OT data account | VP IT |
| Field data capture app, volume integration service, shipper portal | PaaS web apps, functions, managed database | Business workloads account | VP IT; Production Accounting Director; Measurement Supervisor |
| Backup vault | Backup service with write-once retention | Backup account (second region) | VP IT |
| Production accounting tenant | SaaS | Production accounting vendor | Production Accounting Director |
| Identity provider tenant | SaaS | Identity vendor | VP IT |
| Rugged tablets (240) | Mobile endpoints | Lease operators and gaugers | VP IT |
| Compressor packager gateways (4); flow computer vendor modem (1) | Vendor remote access devices (**gap 3**) | Compression stations; Central Facility | SCADA and Automation Manager |

Field devices in South Florida and Alabama are not yet itemized by model and firmware (gap 2; POAM-006).

## 10. Control Implementation Details
### 10.1 Control implementation status
**Baseline and tailoring.** The FSPA uses the NIST SP 800-53B **Moderate** baseline (287 controls and enhancements), tailored with the SP 800-82 Rev. 3 OT overlay (Appendix F):
- **Documented here: 115 controls** in `control-implementation.csv`. They cover the controls that address the P01 risks and the P03 benchmark and Part 195 gaps, plus every control that the vendor reliance and the SOC 2 readiness work (P09) depend on.
- **Selected by tailoring (added):** PM-1, PM-2, and PM-9. They are not in the Moderate baseline but are needed for the program governance that CSF 2.0 GV expects.
- **OT overlay applied** where OT limits a control: device lock on staffed OCC HMIs (AC-11), account lockout on HMIs (AC-7), unauthenticated radio polling (SC-8, accepted until the 2028 radio refresh), and device authentication on older RTUs (IA-3).
- **Integrity tailoring:** CM-3, CM-5, and SI-7 cover pump station setpoints and flow computer configuration (section 6).
- **Inherited without separate statements:** the remaining physical and environmental controls for cloud and SaaS data centers (for example PE-9 to PE-17 at provider sites) and platform-level SA and SC controls. They are inherited from the cloud provider, the identity provider, the production accounting vendor, and the MDR provider, evidenced by their SOC 2 Type 2 reports (P09 `vendor-soc2-review.csv`).
- **Deferred:** the other Moderate controls with no Moderate-or-higher risk in P01 (for example SA-11 developer testing and SA-15 development process, because the company does not develop SCADA software; the field data capture app is maintained by a contractor under SA-4 terms). Recorded as tailoring decisions and reviewed yearly.

The `csf2_subcategories` column uses NIST's official CSF 2.0 informative references to SP 800-53 (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`). Where a control has no official reference, the base control's mapping is used for enhancements, and an author mapping for the rest (AC-11, AU-8, CA-6, CP-3, IR-2, MA-4, MP-6, MP-7, PL-4, PS-3, PS-4, PS-8).

**Status of the 115 documented controls:**
| Status | Count |
|---|---|
| Implemented | 42 |
| Partially implemented | 70 |
| Planned | 3 |
| Not applicable | 0 |

**Inheritance of the 115 documented controls:**
| Inheritance | Count | Main providers |
|---|---|---|
| System-specific | 80 | Company |
| Hybrid | 24 | Identity provider, cloud provider, production accounting vendor, MDR provider, SCADA integrator, cellular carrier, privileged access management vendor |
| Common/Inherited | 11 | Identity provider (AC-2(1), AC-7, IA-2(1), IA-2(2), IA-8), cloud provider (AU-12 with the identity provider, SC-5, SC-12), MDR provider (AU-3, AU-9, IR-7) |

The Partially implemented statements trace to the 14 known gaps in `../00_company-facts.md` section 4 and to the P07 findings. The pattern is a defined program whose controls stop at the edge of the Panhandle: the OCC is segmented, monitored, patched, and under change control, while the South Florida office, the BCC, field controllers outside the Panhandle, and vendor paths are not.

### 10.2 Control assessment status
The co-sourced internal audit firm assessed 36 controls from 2026-08-03 to 2026-08-21 (P07 `assessment-plan.md`, `assessment-results.csv`, and `poam.csv`). Weaknesses are tracked in the POA&M and reported quarterly to the audit committee.

## 11. Digital Identity Acceptance Statement
- **Corporate, cloud, and SaaS users** (including production accounting, the field data capture app, and the jump host) authenticate through the identity provider with a password and push MFA with number matching; administrators use phishing-resistant hardware keys. This is appropriate for the Moderate categorization.
- **Shipper portal users** (5 shippers, about 20 people) authenticate as guests through the identity provider with MFA (IA-8).
- **SCADA users at the OCC** use named accounts synchronized from the OT directory. Production Controllers sign in once per shift with fast user switching, consistent with the SP 800-82 Rev. 3 overlay discussion of IA-2. **South Florida and BCC HMIs** still use a shared engineering account (gap 9); the target is named accounts by 2027-03-31, with a shift sign-in log tied to badge records as the compensating control until then.
- **Vendor access** must use named accounts with MFA at the jump host. The packager gateways' shared password does not meet this statement and is a condition of the operating decision (section 4.2).

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`); BIA (P05); cloud architecture and control map (P04); risk register (P01); gap analysis and roadmap (P03); policies and standards index (P06); assessment and POA&M (P07); incident runbooks and notification matrix (P08); SOC 2 readiness and vendor reviews (P09); AI governance assessment (P10).

## 13. Acronym List and Glossary
- **BCC / OCC:** Backup Control Center / Operations Control Center
- **CAB:** change advisory board
- **DMZ:** demilitarized zone, a buffer network between IT and OT
- **ESP:** electric submersible pump
- **FSPA:** Field SCADA and Production Accounting System
- **HMI:** human-machine interface
- **LACT:** lease automatic custody transfer unit
- **MDR:** managed detection and response
- **MOP:** maximum operating pressure (49 CFR 195.406)
- **OT:** operational technology
- **PLC / RTU:** programmable logic controller / remote terminal unit
- **POA&M:** plan of action and milestones
- **SCADA:** supervisory control and data acquisition

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-07-31 | Draft from the BIA, risk assessment, and gap analysis | GRC Analyst with the OT Security Engineer |
| 1.0 | 2026-09-16 | Updated with P07 results; approved by the Chief Operating Officer | Security Manager |
