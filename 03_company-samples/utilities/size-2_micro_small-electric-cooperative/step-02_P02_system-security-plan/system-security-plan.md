# System Security Plan: Distribution SCADA and Outage Management System (DSOMS)

**Organization:** Cris Santos Electric Cooperative, Inc. (member-owned electric distribution cooperative) | **Tier:** Micro (7 employees) | **Vertical:** Utilities
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Distribution SCADA and Outage Management System (**DSOMS**), identifier CSEC-SYS-001.

## 2. System Overview
The DSOMS is how the cooperative sees and controls its grid and how it finds and fixes outages. It covers Substation 1, 3 feeders, 128 miles of line, and about 820 meters. The 4 field staff (Line Superintendent, 2 Journeyman Lineworkers, Meter and Service Technician) use it every day and on the after-hours on-call rotation. The Member Services Representative, the Office and Finance Manager, and a contracted after-hours call center use the outage module.

The cooperative owns no servers. SCADA, the AMI head-end, and the outage module are vendor SaaS. On site are the substation and field control devices and a few operations endpoints. This plan therefore states, for each control, what the cooperative does itself, what the MSP does for it, and what it inherits from a vendor.

**Major components:**
- **SYS-01:** hosted distribution SCADA service: master station, web HMI, historian, alarm texts (vendor SaaS)
- **SYS-02:** substation and field control devices: the Substation 1 RTU, 3 feeder recloser controls, 3 regulator controls, the cellular gateway with a VPN to the SCADA vendor, and 6 line recloser controls, each with its own cellular modem
- **SYS-03:** AMI head-end, meter data management, and load management (vendor SaaS), 2 collectors, about 820 meters (120 with a remote disconnect switch), and 310 water-heater load-control switches
- **SYS-04 (outage module only):** outage management, outage map, and crew tickets in the utility business suite (vendor SaaS)
- **SYS-06 (operations endpoints only):** the operations workstation, the Line Superintendent's and Meter and Service Technician's laptops, 3 rugged truck tablets, and the 4 field staff's company smartphones
- **SYS-07 (settings backups only):** recloser, regulator, and RTU settings files and the SCADA point database export in the cloud backup vault

**What the system does not do.** Reclosers and regulators protect the lines on their own. If the DSOMS stops, power keeps flowing and crews operate devices at the device (P05). The risk that matters most is the opposite: someone using the DSOMS to operate devices (P01 R-001 to R-003).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies to the DSOMS |
|---|---|---|---|
| RUS O&M rule | RUS electric system operations and maintenance | 7 CFR Part 1730, Subpart B (1730.20 to 1730.28) | Binding through the RUS loan contract and mortgage. Records of the cyber condition and security of the system (1730.20), inspections (1730.21), borrower analysis (1730.22), the VRA (1730.27), and the ERP with its Business Continuity Section (1730.28) |
| DOE-417 | Electric Emergency Incident and Disturbance Report | Federal Energy Administration Act of 1974 sec. 13(b) (Pub. L. 93-275); OMB 1901-0288 | A cyber event that interrupts electrical system operations must be reported within 1 hour (P08) |
| State | Florida Information Protection Act | Fla. Stat. 501.171 | The outage module holds member names, addresses, phone numbers, and the medical-needs list (physical condition data, 501.171(1)(g)1.a.(IV)) |
| Voluntary | NIST CSF 2.0 and SP 800-82 Rev. 3 (Guide to OT Security) | Benchmark | Control selection for SCADA and field devices, which no binding cyber rule covers |
| Internal | POL-02, POL-03, POL-04 | P06 | All components |

Not applicable (P03 records each decision):
- **NERC CIP (N22-R01) and NERC EOP-004:** the cooperative is not on the NERC Compliance Registry. It meets none of the Distribution Provider criteria in NERC Rules of Procedure Appendix 5B (peak 2.6 MW; no UFLS, UVLS, Remedial Action Scheme, or transmission Protection System).
- **TSA pipeline directives (N22-R02), NRC 10 CFR 73.54 (N22-R03), SDWA section 1433 (N22-R04):** no pipelines, reactors, or water system. The county water plant is a member served by the cooperative, not a system it operates.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the General Manager (system owner) on 2026-08-31. Presented to the Board of Trustees on 2026-09-17 with the P06 policies and the High-risk treatment plans.

### 4.2 System Authorization Decision
The cooperative is not a federal agency, so there is no formal authorization. The equivalent internal decision: on 2026-08-31 the General Manager accepted continued operation of the DSOMS on two conditions. First, the three High risks in P01 (R-001, R-002, R-004) must be treated by their dates, with the Board approving the plans on 2026-09-17. Second, the P07 POA&M items must be completed by their scheduled dates. Named SCADA accounts with MFA (POAM-001) are the first condition and are due 2026-10-31.

### 4.3 System Operational Status
Operational. Planned changes: named SCADA accounts with MFA (R-001, 2026-10-31); line recloser modems moved to the private cellular network (R-002, 2026-12-31); operations workstation and tablets enrolled in MSP management (R-016, 2026-10-31); second carrier in the substation gateway (R-011, 2027-03-31). The 2027 RUS loan application (substation transformer replacement and AMI upgrade) will be a major modification and will trigger a plan update.

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner and risk acceptor | General Manager | Overall accountability; accepts Moderate risks; signs VRA and ERP certifications to RUS (7 CFR 1730.26(b)) |
| Governing body | Board of Trustees | Approves policies, the ERP, the security budget, and High-risk treatment plans |
| Security Coordinator | Office and Finance Manager | Maintains this plan, the risk register, and vendor files; accounts in the business suite and AMI; MSP contact |
| OT lead and SCADA administrator | Line Superintendent | SCADA accounts, recloser and RTU settings, Substation 1, settings backups; operational incident commander |
| AMI administrator | Meter and Service Technician | AMI meters and collectors, remote disconnect and load-control rights |
| IT operations (office) | MSP | Office computers, firewall, Wi-Fi, email administration, backup vault |
| Service providers | Hosted SCADA vendor; AMI vendor; business suite vendor; cellular carrier | Operate their services; vendor support access (SCADA) |
| Independent assessor | Consultant with OT experience | Annual control assessment (P07) |

**Role overlap and how it is covered.** Seven people cannot separate every duty. The Line Superintendent both administers SCADA and uses it. That is covered by monthly log review by the Security Coordinator from 2026-11 (AU-6) and by the yearly independent assessment (CA-2). The Office and Finance Manager both creates accounts and releases vendor payments. A bank detail change needs the General Manager's callback approval (POL-02 C.7).

## 6. System Information Types and System Categorization
Information types follow NIST SP 800-60 Vol. 2 Rev. 1 where a close match exists and are defined by the cooperative otherwise. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Energy supply: distribution monitoring and control (SCADA commands, alarms, settings) | Moderate | **High** | Moderate | A false or unauthorized command can open all 3 feeders and drop every member, including the water plant, the fire station, and 26 members on the medical-needs list, or re-close onto a line where a crew is working. Losing SCADA alone is Moderate: devices protect themselves and crews can switch locally (P05 BP-02 MTD 24 h) |
| Outage and member contact records (outage module, medical-needs list) | Moderate | Moderate | Moderate | Personal information under Fla. Stat. 501.171; wrong data sends crews to the wrong place. The outage process can run on paper for 4 hours (P05 BP-01 and BP-03 MTD 4 h) |
| Metering commands (remote disconnect, load control) | Low | Moderate | Low | A wrong command reaches at most 120 disconnect meters or 310 water heaters; reads can wait (P05 BP-04 MTD 72 h) |
| Device settings and network details | Moderate | Moderate | Low | Useful to an attacker; needed only to restore a device |
| **DSOMS category (high-water mark)** | **Moderate** | **High** | **Moderate** | |

**Baseline.** Because integrity is High, the reference is the NIST SP 800-53B High baseline, tailored for a 7-person cooperative with the OT guidance in SP 800-82 Rev. 3. The plan documents 44 controls that address the risks in P01 and the RUS duties in P03 (see `control-implementation.csv`). All other High-baseline controls are handled one of two ways:
- **Inherited** from the SaaS vendors (platform, data center, and application controls), with SOC 2 reports as the evidence where available (P09).
- **Tailored out**, as a recorded decision, where the control assumes staff or equipment a 7-person cooperative does not have (for example, a separate security operations function, dual authorization for every change, or device lockout on field controls, which would stop a lineworker from operating a recloser in an emergency).

## 7. Authorization Boundary Description
The boundary holds what the cooperative controls or pays someone to control for it:
- **Inside:** the cooperative's SCADA tenant (accounts, roles, settings, alarm routing); the Substation 1 RTU, recloser and regulator controls, and gateway; the 6 line recloser controls and modems; the AMI head-end tenant, 2 collectors, meters, and load-control switches; the outage module configuration and roles; the operations endpoints; and the settings backups in the vault.
- **Outside (interconnected):** the vendors' own platforms and data centers; the cellular carrier's network; the G&T's 69 kV tap line, circuit switcher, protection, and wholesale meter; the rest of the business suite (billing, accounting) and the office computers, which share the office network; the MSP's remote management platform; and the AMI vendor's peak-forecasting add-on (assessed separately in P10).

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Agreement |
|---|---|---|---|
| Hosted SCADA vendor to Substation 1 gateway | Bidirectional | DNP3 polling and control commands inside a VPN on the carrier's private network | SCADA service contract (no security terms: gap) |
| Line recloser modems (public-IP data plans) | Bidirectional | Recloser status and control | SCADA service contract; carrier data plans |
| AMI head-end to outage module | Outbound | Meter outage and restoration events | AMI and business suite contracts |
| SCADA vendor support staff | Inbound administrative access | SCADA and gateway administration | SCADA service contract (standing access: gap) |
| After-hours call center to outage module | Inbound | Outage tickets | Service agreement; named account with MFA |
| G&T control center | Phone and email | Delivery point status, switching, peak advisories (no data link to the DSOMS) | Wholesale power contract |
| AMI vendor peak-forecasting add-on | Within the AMI service | Member interval usage data | AMI contract; add-on trial terms not reviewed (gap; P10) |
| MSP remote management platform | Inbound administrative access | Office computers (not yet the operations workstation) | MSP service contract (no security terms: gap) |

## 9. System Component Inventory
| Component | Type | Location or provider | Owner |
|---|---|---|---|
| SCADA tenant (SYS-01) | SaaS | Hosted SCADA vendor | Line Superintendent |
| Substation RTU, 3 feeder recloser controls, 3 regulator controls, cellular gateway (SYS-02) | OT field devices | Substation 1 | Line Superintendent |
| 6 line recloser controls with cellular modems (SYS-02) | OT field devices | Pole-mounted on the 3 feeders | Line Superintendent |
| AMI head-end tenant, 2 collectors, about 820 meters, 310 load-control switches (SYS-03) | SaaS plus field devices | AMI vendor; Substation 1 and headquarters; member premises | Meter and Service Technician |
| Outage module and outage map (SYS-04) | SaaS | Business suite vendor | Office and Finance Manager |
| Operations workstation; 2 laptops; 3 truck tablets; 4 field smartphones (SYS-06) | Endpoints | Headquarters; trucks | Line Superintendent (not yet MSP-managed, except the laptops) |
| Settings and point database backups (SYS-07) | IaaS object storage | Cooperative-owned cloud account, MSP-administered | Line Superintendent |

**No OT inventory with firmware versions exists yet** (CM-8, POAM-005). This table is the starting point for it.

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 44 controls:
- Implemented: 8
- Partially implemented: 28
- Planned: 8
- Not applicable: 0

By responsibility: 20 system-specific (the cooperative), 20 hybrid (the cooperative with a vendor or the MSP), 4 common/inherited (provided by SaaS vendors).

### 10.2 Inherited and MSP-provided controls
| Provider | What the cooperative relies on | Evidence | What the cooperative must still do |
|---|---|---|---|
| Hosted SCADA vendor | Master station hosting, backups and second site (CP-9), lockout (AC-7), event logging (AU-2), TLS (SC-8) | SOC 2 Type 2 report reviewed 2026-08-20 (P09) | Complementary user entity controls: named accounts, MFA, removing users, reviewing vendor access and logs. **All four are open gaps today** |
| AMI vendor | Head-end hosting, command logging, TLS | None yet; SOC 2 report requested 2026-08-14 | Disconnect rights, MFA, data-use terms for the add-on |
| Business suite vendor | Outage module hosting, MFA, roles, backups | SOC 2 Type 2 report on file | Roles for staff and the call center; termination |
| MSP | Office patching (SI-2), antivirus (SI-3), firewall (SC-7), vault administration (CP-9) | Monthly MSP reports; P07 evidence requests | Bring the operations workstation and tablets under management; MFA on the vault login; annual MSP review (R-009) |
| Cellular carrier | Private network for the substation gateway (SC-7) | Carrier order | Move the 6 line recloser modems onto it (R-002) |

**Inherited does not mean done.** The SCADA vendor's report assumes its customers use named accounts and MFA. The cooperative did neither until this assessment.

### 10.3 Control assessment status
Assessed 2026-08-10 to 2026-08-12 by an independent consultant, with field testing on 2026-08-11. See P07 `assessment-results.csv` and `poam.csv`. The most serious finding (LR-4 modem reachable from the internet with a default password) was fixed on 2026-08-12.

## 11. Digital Identity Acceptance Statement
- **SCADA:** today one shared password, which gives no accountability and fails AAL1 for individual users. Target by 2026-10-31: named accounts with a password and an authenticator app (AAL2), because a SCADA command can drop every member. View-only accounts may use a longer session timeout.
- **Outage module and AMI:** business suite accounts already use a password and an authenticator app (AAL2). The AMI head-end moves to the same by 2026-11-30.
- **Vendor support:** named vendor accounts with MFA, enabled only on request.
- **Field devices:** local operation needs a physical key to the cabinet. Remote management passwords are unique per device (from 2026-08-12 for the modems).

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`); BIA (P05); cloud control map (P04); risk register (P01); gap analysis (P03); policies (P06); assessment and POA&M (P07); incident response runbook (P08); SOC 2 readiness and the SCADA vendor report review (P09); AI risk assessment (P10); the 2021 ERP; the 2005 VRA.

## 13. Acronym List and Glossary
- **AMI:** advanced metering infrastructure
- **DSOMS:** Distribution SCADA and Outage Management System
- **ERP:** Emergency Restoration Plan (7 CFR 1730.28)
- **G&T:** generation and transmission cooperative (the wholesale supplier)
- **HMI:** human-machine interface
- **MSP:** managed service provider
- **RTU:** remote terminal unit
- **RUS:** Rural Utilities Service (USDA)
- **SCADA:** supervisory control and data acquisition
- **VRA:** Vulnerability and Risk Assessment (7 CFR 1730.27)

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan | Office and Finance Manager (Security Coordinator) with the Line Superintendent |
