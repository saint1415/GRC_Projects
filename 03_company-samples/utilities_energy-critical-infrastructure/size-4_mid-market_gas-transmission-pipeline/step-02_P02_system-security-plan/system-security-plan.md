# System Security Plan: Pipeline SCADA and Gas Control System (PSGCS)

**Organization:** Cris Santos Company, Inc. (PE-backed interstate natural gas transmission pipeline operator) | **Tier:** Mid-Market | **Vertical:** Energy
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-17

## 1. System Name and Identifier
Pipeline SCADA and Gas Control System (**PSGCS**), identifier CSC-PSGCS-01. It comprises SYS-01 to SYS-07 and physical access control at the control centers and compressor stations (part of SYS-14) in `../00_company-facts.md`.

## 2. System Overview
The PSGCS lets 28 gas controllers and 5 shift supervisors monitor and control about 780 miles of interstate natural gas transmission pipeline, 24 hours a day, from the Gas Control Center (GCC) or the Backup Control Center (BCC). Through it, controllers:
- watch pressures, flows, gas quality, and alarms at 46 M&R stations, 62 valve sites, and 4 receipt interconnects;
- open and close remote-control mainline valves;
- start, stop, and load 14 compressor units at 5 compressor stations;
- monitor and control two third-party laterals under operations services agreements (OSAs).

It is the SCADA system that 49 CFR 192.631 regulates, and it contains Critical Cyber Systems CCS-1 to CCS-6 and CCS-8 under the company's TSA-approved Cybersecurity Implementation Plan (SD Pipeline-2021-02G Section III.A).

**Major components:**
| ID | Component | Hosting |
|---|---|---|
| SYS-01 | Primary SCADA: redundant SCADA servers, 10 HMI consoles, historian, 2 engineering workstations | On-premises, GCC |
| SYS-02 | Backup Control Center: hot-standby SCADA servers, 6 HMIs, historian | On-premises, Compressor Station 3 |
| SYS-03 | About 310 field RTUs and PLCs, flow computers, gas chromatographs | Field sites |
| SYS-04 | Compressor station control systems: station PLCs, unit control panels, 22 station HMIs, hardwired ESD | 5 compressor stations |
| SYS-05 | SCADA telecommunications: private microwave, licensed radio, carrier MPLS, cellular (41 sites), satellite backup (12 sites) | Field and carrier |
| SYS-06 | IT/OT DMZ at the GCC and BCC: firewall pairs, historian replica, patch staging, remote access gateway | On-premises |
| SYS-07 | OT security monitoring: passive sensors at the GCC, BCC, and Compressor Stations 1 and 3 | On-premises; alerts to the MSSP |
| SYS-14 (part) | Badge access and CCTV for control rooms and station control buildings | On-premises |

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it affects the PSGCS |
|---|---|---|---|
| C-ENERGY-R03 | TSA SD Pipeline-2021-02G | Issued under 49 U.S.C. 114; effective 2026-05-03 to 2027-05-02 | **Primary control requirement.** The TSA-approved Cybersecurity Implementation Plan sets the measures TSA inspects against; the `regulatory_driver` column of `control-implementation.csv` names the SD section each control supports |
| C-ENERGY-R02 | TSA SD Pipeline-2021-01G | Issued under 49 U.S.C. 114; effective 2026-01-16 to 2027-01-15 | Cybersecurity Coordinator (II.B); incident reporting to CISA within 72 hours (II.C) |
| C-ENERGY-R04 | PHMSA control room management | 49 CFR 192.631 | Controller roles, point-to-point verification, backup SCADA testing, alarm management, change management, training, records |
| Related | O&M manual; emergency plans; incident reporting | 49 CFR 192.605; 192.615; 191.5, 191.15 | Cyber annex to the emergency plan; Part 191 notices (P08) |
| Related | Sensitive Security Information | 49 CFR Part 1520 (1520.9, 1520.13, 1520.19) | TSA plans, reports, and assessment results are SSI (SD 02G Section IV.B) |
| Related | FERC CEII | 18 CFR 388.113 | Form No. 567 system flow diagrams are filed with a CEII request; detailed PSGCS design is handled as Restricted |
| C-ENERGY-R05 | CIRCIA | 6 U.S.C. 681-681g; proposed 6 CFR Part 226 | **Proposed only.** Tracked in P03; not a current obligation |
| Contract | Operations services agreements | Contract | Notice within 30 minutes of lost lateral monitoring; SOC 2 Type 2 request (P09) |
| Internal | POL-01 to POL-05 and supporting standards | P06 | Policy basis for every control |

Not applicable:
- **C-ENERGY-R01, NERC CIP.** The company is not a NERC-registered entity and owns no Bulk Electric System assets.
- **DOE Form OE-417.** Electric operations only.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Chief Operating Officer (system owner) on 2026-09-17, after the control assessment (P07), and presented to the audit committee the same day.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization to operate. The equivalent internal decision:
- **Decision:** continued operation of the PSGCS accepted with conditions, 2026-09-17.
- **Authorizing official equivalent:** Chief Executive Officer for High and Very High risks; Chief Operating Officer for Moderate and below (P01 acceptance authorities).
- **Conditions:** the High-risk POA&M items in P07 must meet their milestones; the OEM remote connections must be removed or brought through the remote access gateway by 2026-10-31; the Cybersecurity Implementation Plan amendment requests (gap 12) must be filed with TSA by 2026-10-31; re-decision by 2027-09-30 or after a major change.
### 4.3 System Operational Status
Operational. Major modifications planned:
- OT monitoring sensors at Compressor Stations 2, 4, and 5 and a field telecommunications baseline (due 2027-03-31)
- Replacement of the 14 unsupported station HMIs and individual logins at all stations (due 2027-06-30)
- Encryption of the microwave backbone (due 2027-09-30)

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Chief Operating Officer | Accountable for the PSGCS; accepts Moderate risk; approves any precautionary shutdown for cyber reasons |
| Authorizing official equivalent (High risk) | Chief Executive Officer | Accepts High risk; approves the risk appetite |
| Oversight | Board audit committee | Quarterly cyber risk reporting |
| Program strategy | vCISO (part-time contractor) | Program strategy, board reporting, annual review of the TSA plans |
| Security program lead and Cybersecurity Coordinator | Security Manager | Primary TSA Cybersecurity Coordinator; incident commander; owns this SSP |
| OT security | OT Security Engineers (2) | OT access, monitoring, patch mitigations; one is the alternate Cybersecurity Coordinator |
| System administration | SCADA and OT Engineering Manager | SCADA servers, HMIs, OT network, field device configuration, backups |
| Control room management | Director of Gas Control | 192.631 procedures; authority to isolate OT from IT; MOC sign-off |
| Operations and emergency plans | VP Operations | O&M manual (192.605), emergency plan (192.615), stations, physical security |
| Regulatory compliance | Director of Pipeline Safety and Compliance | PHMSA records and Part 191 notices |
| Independent assessment | Co-sourced internal audit firm | P07 assessment and the annual TSA assessment work |
| Monitoring | MSSP | 24x7 SIEM and OT sensor alerting |
| External support | SCADA software vendor; SCADA integrator; compressor OEM | Support through the remote access gateway (OEM: see gap 3) |

## 6. System Information Types and System Categorization
Information types come from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199 and use the BIA (P05).

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Energy supply: pipeline control data and commands | Moderate | **High** | **High** | Wrong commands or false data could cause overpressure or hide a rupture, with potential loss of life. Loss of control beyond the 8-hour MTD (P05 BP-01) forces curtailment to LDCs serving about 1.3 million customers and 7 power plants |
| SCADA configuration, network, and security information (including SSI) | Moderate | **High** | Moderate | Disclosure helps an attacker plan; unauthorized change affects every control function. SSI and CEII handling rules apply to parts of it |
| Emergency response information | Low | Moderate | **High** | Public safety communication cannot stop (P05 BP-03) |
| Contract operations data for the two laterals | Moderate | **High** | **High** | Same control functions on pipelines the company does not own (P05 BP-04) |
| Gas measurement data | Low | Moderate | Low | Flow computers keep 35 days locally (P05 BP-06) |
| **PSGCS category (high-water mark)** | **Moderate** | **High** | **High** | **High** |

**Why High and not Moderate.** The tier guidance for a mid-market major system expects Moderate impact. The team kept High for integrity and availability because the consequences of a compromise are physical and public (P05 sections 3 and 4). Confidentiality stays Moderate: the system holds no personal information, and the most sensitive design information is protected by SSI and CEII handling rules.

## 7. Authorization Boundary Description
**Inside the boundary:**
- the SCADA servers, HMIs, historian, and engineering workstations at the GCC and BCC;
- field RTUs, PLCs, flow computers, and chromatographs at 112 field sites;
- compressor station PLCs, unit control panels, and station HMIs at 5 stations (hardwired ESD systems are included as components but have no network interface);
- the microwave backbone, radio network, cellular gateways, and satellite terminals;
- the DMZ firewall pairs, historian replica, patch staging server, and remote access gateway at the GCC and BCC;
- the OT monitoring sensors;
- badge access and CCTV for control rooms and station control buildings.

**Outside the boundary (interconnected):**
- business IT and endpoints (SYS-08);
- the identity provider and productivity suite (SYS-09, SYS-10);
- the cloud landing zone (SYS-11), including the OT analytics account that receives historian data;
- the customer activities website (SYS-12);
- the carrier networks (MPLS and cellular private network);
- the MSSP and SIEM platform (SYS-15);
- the SCADA vendor, integrator, and compressor OEM systems;
- the two lateral owners' field systems (their RTUs report to the PSGCS over their own telecommunications).

Business IT connects only to the DMZ, never directly to OT. The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| DMZ historian replica to cloud OT analytics account (SYS-11) | Outbound from DMZ only | Pressure, flow, valve, and compressor data for the leak-detection model | Internal; model vendor contract with security terms (2025) |
| DMZ historian replica to measurement application (SYS-11) | Outbound from DMZ only | Hourly volumes and gas quality | Internal |
| Customer activities website (SYS-12) | Inbound scheduled quantities to SCADA displays via the DMZ (file drop, read by the SCADA host) | Scheduled volumes by point | Vendor contract; NAESB WGQ standards |
| SCADA software vendor and integrator | Inbound sessions through the remote access gateway | Support and configuration | Contracts with security terms; individual accounts; MFA; recorded |
| Compressor OEM | Outbound diagnostics from unit control panels | Vibration and performance data | **Contract has no security terms; connection not in the TSA plan (gap 3)** |
| Lateral owners (2) | Inbound telemetry from their RTUs; view-only SCADA accounts | Lateral pressures, flows, alarms | OSAs |
| Interconnecting pipelines (4 receipt points) | Phone and confirmation data, no system-to-system control | Operational coordination | Interconnect operating agreements |
| MSSP | Outbound logs and sensor alerts | Security events | MSSP contract (SOC 2 Type 2) |
| Telecom carrier | Transport | SCADA polling and commands | Carrier contracts (cellular contract lacks security terms) |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| SCADA servers (2 redundant) and development server | Server | GCC | SCADA and OT Engineering Manager |
| HMI consoles (10) and engineering workstations (2) | Workstation | GCC | SCADA and OT Engineering Manager |
| Historian | Server | GCC | SCADA and OT Engineering Manager |
| Hot-standby SCADA servers, historian, 6 HMIs | Server and workstations | BCC (Compressor Station 3) | SCADA and OT Engineering Manager |
| Offline backup media | Encrypted media in a safe | BCC | SCADA and OT Engineering Manager |
| DMZ firewall pairs, historian replica, patch staging, remote access gateway | Network and virtual servers | GCC and BCC | OT Security Engineers |
| OT monitoring sensors (4) | Network appliance | GCC, BCC, Compressor Stations 1 and 3 | OT Security Engineers |
| Field RTUs and PLCs (about 310), flow computers, chromatographs | Field device | 112 field sites | VP Operations (field); SCADA and OT Engineering Manager (configuration) |
| Station PLCs, unit control panels, station HMIs (22), ESD systems | Control system | 5 compressor stations | Compressor Station Supervisors |
| Microwave, radio, cellular gateways (41 sites), satellite terminals (12 sites) | Telecommunications | Field; carriers | SCADA and OT Engineering Manager |
| Badge readers and CCTV | Physical security | Control rooms and station buildings | VP Operations |

The inventory is about 85% complete for field devices, with firmware unknown for about 20% of RTUs and PLCs (gap 4). P07 found an undocumented OEM cellular modem at Compressor Station 4.

## 10. Control Implementation Details
### 10.1 Control implementation status
**Baseline and tailoring.** The PSGCS uses the NIST SP 800-53B **High** baseline (370 controls and enhancements in the catalog), tailored with the OT overlay in NIST SP 800-82 Rev. 3 Appendix F:
- **Documented here: 140 controls** in `control-implementation.csv`. They cover every control that supports a measure in the TSA-approved Cybersecurity Implementation Plan, the SCADA-relevant duties in 192.631, and the High and Very High risks in P01.
- **Selected by tailoring (added):** PM-1, PM-2, PM-9, and PM-11. They are not in the High baseline but support the Cybersecurity Coordinator role (SD 01G II.B) and the definition of business critical functions (SD 02G VII.B).
- **Tailored for safety (compensating controls documented):**
  - AC-7 and AC-11 on control room HMIs. A lockout or screen lock during an abnormal operating condition is a safety risk; compensated by staffed, badge-controlled control rooms with CCTV (PE-3, PE-6).
  - IA-2(2) for controllers at HMIs. Passwords inside staffed control rooms, with the compensating controls documented in the Cybersecurity Implementation Plan as SD 02G Section III.C.2 allows for control rooms regulated under 49 CFR Part 192.
  - No active vulnerability scanning in OT (RA-5). SP 800-82 Rev. 3 warns that active scanning can disrupt control systems; OT vulnerabilities are tracked passively and from vendor advisories.
- **Inherited without separate statements:** physical and environmental controls for the cloud and SaaS providers' facilities, evidenced by their SOC 2 reports (P09).
- **Deferred:** other High-baseline controls with no TSA, 192.631, or High-risk link (for example SA-11 developer testing and SA-15 development process, because the company does not develop SCADA software). They are recorded as tailoring decisions and reviewed yearly.

**CSF 2.0 mapping.** The `csf2_subcategories` column uses the official NIST CSF 2.0 to SP 800-53 Rev. 5.2.0 mapping (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`) wherever it maps the control. For 35 controls the official mapping has no entry, and the column gives an author mapping.

**Status of the 140 documented controls:**
| Status | Count |
|---|---|
| Implemented | 69 |
| Partially implemented | 71 |
| Planned | 0 |
| Not applicable | 0 |

**Inheritance of the 140 documented controls:**
| Inheritance | Count | Main providers |
|---|---|---|
| System-specific | 107 | Company |
| Hybrid | 24 | MSSP, identity provider vendor, remote access gateway vendor, telecom carrier, SCADA software vendor, customer activities website vendor |
| Common/Inherited | 9 | Company-wide security program (AT-1, AT-2, PL-4); identity provider vendor (IA-2(8)); remote access gateway vendor (AC-17(2)); MSSP and IR retainer (IR-7, SI-4(2)); cloud key management (SC-12); productivity suite provider (SI-8) |

The Partially implemented statements trace to the 14 gaps in `../00_company-facts.md` section 4 and to the P07 findings. The pattern: the control center design (segmentation, remote access gateway, BCC, monitoring at the core) is strong; the gaps sit at the edges (3 compressor stations, field devices, the OEM, and record keeping for TSA).

### 10.2 Control assessment status
The co-sourced internal audit firm assessed 34 controls from 2026-08-03 to 2026-08-21 (P07). That work also counts toward the TSA Cybersecurity Assessment Plan schedule (SD 02G III.G.2.d) and the annual report due 2026-11-20. Weaknesses are tracked in the POA&M and reported quarterly to the audit committee.

## 11. Digital Identity Acceptance Statement
- **Controllers** authenticate to the SCADA application with individual passwords inside staffed, badge-controlled control rooms at the GCC and BCC. MFA on control room HMIs was rejected because it could delay a controller in an emergency. The physical controls are the compensating measure, documented in the Cybersecurity Implementation Plan under SD 02G Section III.C.2.
- **Compressor station technicians** at Compressor Stations 2, 4, and 5 use a shared station login today (gap 1). Target: individual logins with badge-tap authentication on the replacement HMIs by 2027-06-30. Until then, the stations' badge access and CCTV are the documented interim mitigation.
- **Administrators, the SCADA vendor, and the integrator** reach OT only through the remote access gateway with MFA (authenticator assurance level 2 as described in NIST SP 800-63B), approval per session, and recording.
- **The compressor OEM** must move to the gateway on the same terms by 2026-10-31 (POAM-003).
- **Business users** use the identity provider with MFA and have no OT access.

## 12. Referenced Artifacts
- Scenario facts (`../00_company-facts.md`)
- Risk register (P01)
- Gap analysis and roadmap (P03)
- Cloud and architecture map (P04)
- BIA (P05)
- Policies and standards index (P06)
- Assessment and POA&M (P07)
- Incident response runbooks (P08)
- SOC 2 readiness and vendor reviews (P09)
- AI governance assessment (P10)
- TSA Cybersecurity Implementation Plan, Cybersecurity Incident Response Plan, and Cybersecurity Assessment Plan (SSI; held in the SSI repository)
- Control room management manual, O&M manual (192.605), and emergency plan (192.615)

## 13. Acronym List and Glossary
- **BCC / GCC:** Backup Control Center / Gas Control Center
- **CCS:** Critical Cyber System (TSA SD 02G Section VII.C)
- **CEII:** critical energy/electric infrastructure information (18 CFR 388.113)
- **DMZ:** demilitarized zone between business IT and OT
- **ESD:** emergency shutdown system
- **HMI:** human-machine interface
- **KEV:** CISA Known Exploited Vulnerabilities Catalog
- **LDC:** local distribution company
- **M&R:** meter and regulator station
- **MOC:** management of change
- **MSSP:** managed security service provider
- **OEM:** original equipment manufacturer (here, the compressor manufacturer)
- **OSA:** operations services agreement
- **OT:** operational technology
- **PLC / RTU:** programmable logic controller / remote terminal unit
- **SSI:** Sensitive Security Information (49 CFR Part 1520)

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-07-31 | Draft from the BIA, risk assessment, and gap analysis | GRC lead with the SCADA and OT Engineering Manager |
| 1.0 | 2026-09-17 | Updated with P07 results; approved by the Chief Operating Officer | Security Manager |
