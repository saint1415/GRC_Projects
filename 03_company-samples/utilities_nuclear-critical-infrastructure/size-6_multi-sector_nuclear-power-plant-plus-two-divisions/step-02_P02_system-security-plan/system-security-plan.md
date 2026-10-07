# System Security Plan: Plant Business Network and Work Management System (PBN-WMS)

**Organization:** Cris Santos Company Holdings, Inc., Nuclear Generation division (inherits common controls from corporate shared services) | **Tier:** Multi-Sector | **Vertical:** Nuclear Reactors, Materials, and Waste
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-17

> **Why this system.** At this tier the SSP can cover one system per division or a shared corporate system. The group chose the Nuclear Generation **Plant Business Network and Work Management System** because the BIA (P05) ranks its processes (clearance and tagging, outage work, site access) among the most critical, because it is where people and devices from all three divisions meet, and because it is the network an attacker must cross to reach the CDAs (P01 GR-01, GR-02). It inherits most controls from corporate (SYS-G1 to SYS-G3, listed in `common-control-catalog.csv`). The CDAs themselves are **not** in this plan: they are protected under each station's NRC-approved cyber security plan (CSP), which is a separate, inspected program with its own controls (RG 5.71 Rev. 1).

## 1. System Name and Identifier
Plant Business Network and Work Management System (**PBN-WMS**), identifier CSCH-NG-SYS-N1-N2. It combines SYS-N1 and SYS-N2 in `../00_company-facts.md`.

## 2. System Overview
The PBN-WMS is the business side of the three nuclear stations. It supports:
- **Work management:** about 410,000 work orders a year, including about 12,000 per refueling outage; clearance and tagging; outage scheduling; parts reservations; the interface to the corrective action program (CAP).
- **Station business services:** email access, file and print, controlled document access, and the site access processing applications.
- **Plant data for engineering:** each station's business DMZ holds plant data replica servers that receive process data one way from Level 3. Engineering, the Maintenance Rule program, and the predictive maintenance service (P10) read from them.

Users: about 7,300 active WMS users (5,100 Nuclear Generation, 1,450 Engineering and Radiation Services, 450 Radioactive Waste Management, 300 corporate and vendor) and about 6,200 station endpoints.

**Major components:**
- **Station business LANs** (Stations A, B, and C): switches, routers, Wi-Fi, endpoints, file and print servers, and multifunction printers
- **Business DMZ** at each station: plant data replica servers and the receive side of the hardware one-way devices
- **Kiosk update server** (on the Station A server subnet, serving all 9 PMMD kiosks). The server is in the boundary; the kiosks are CSP security controls outside it
- **Fleet work management system:** a commercial enterprise asset management application on the group cloud platform (provider A), with a database replica in provider B
- **Interfaces:** CAP system (SaaS), predictive maintenance service (SaaS), ERP for parts and costs (SYS-G4)

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies to the PBN-WMS |
|---|---|---|---|
| C-NUCLEAR-R01 | NRC cyber security rule | 10 CFR 73.54; RG 5.71 Rev. 1 | The PBN-WMS is not a CDA system. It was analyzed under 73.54(b)(1) and is outside the CSP scope. It matters to 73.54 in three ways: it sits at the lower defensive levels from which the CSP must protect CDAs (73.54(c)(2); RG 5.71 C.7), it hosts the kiosk update server that feeds CSP controls (RG 5.71 B.1.19), and changes at its edge must not weaken the defensive architecture (73.54(d)(3)) |
| C-NUCLEAR-R03 | Cyber security event notifications | 10 CFR 73.77 | A business-network attack that could have reached CDAs, or a report to the FBI about one, can start a 4-hour NRC clock (73.77(a)(2)); CSP weaknesses found here go to the CAP within 24 hours (73.77(b)) |
| C-NUCLEAR-S01 | Safeguards Information | 10 CFR 73.21-73.22 | SGI must never be stored or processed on the PBN-WMS: only stand-alone computers may process it (73.22(g)(1)); reproduction equipment must be evaluated (73.22(e)) |
| C-NUCLEAR-S02 | Access authorization | 10 CFR 73.56 | Staff with administrative control over plant networks identified in 73.54 are a 73.56 population (73.56(i)(1)(v)(B)(4)); PBN administrators who manage the receive side of the one-way devices are included |
| C-NUCLEAR-S03 | Safety/security interface | 10 CFR 73.58 | Changes to the PBN that touch the one-way devices, the kiosks, or site access processing are screened for safety and security effects before implementation |
| C-NUCLEAR-S11 | State breach notification | Each state; Fla. Stat. 501.171 worked example | Personal information of employees and contractors in site access and work records |
| C-NUCLEAR-S10 | SEC cybersecurity disclosure | Form 8-K Item 1.05; Reg S-K Item 106 | A PBN-WMS incident may be material to the group (P08) |
| Internal | Group policies POL-01 to POL-05 and the Nuclear Generation supplement | P06 | |

Not applicable: NERC CIP (the PBN-WMS holds no BES Cyber System; the fleet operations center has its own Electronic Security Perimeter); 10 CFR 73.110 (no Part 53 license); CIRCIA (proposed only).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the fleet IT director (system owner), the work management director, and the Group CISO on 2026-09-17, after the board risk committee review.

### 4.2 System Authorization Decision
The group is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- **Decision:** authorized to operate with conditions, 2026-09-17, by the Group CISO and the Chief Nuclear Officer.
- **Conditions:** (1) station device checks for division-managed laptops and removal of cross-division accounts at the end of each outage assignment by 2027-03-31 (POAM-001, POAM-005); (2) restrict CDA work packages to need-to-know roles by 2026-12-31 (POAM-003); (3) signature verification and a restricted segment for the kiosk update server by 2026-11-30 (POAM-004, POAM-010); (4) default passwords on station multifunction printers changed and SGI reproduction equipment re-evaluated by 2026-10-31 (POAM-002).
- **Reauthorization:** annually, or when a condition is closed early.

### 4.3 System Operational Status
Operational. **Major modification planned:** station network access control for all devices, with division-managed laptops placed in a contractor segment (P01 GR-01), due 2027-03-31.

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Fleet IT director | Accountable for the PBN-WMS and this SSP |
| Business owner (WMS) | Work management director | Roles, module configuration, data owners for work packages |
| Authorizing official equivalent | Group CISO with the Chief Nuclear Officer | Authorization decision |
| Information owner, CDA work packages | Fleet cyber security program manager | Decides who may see CDA details; owns the boundary with the CSP |
| SGI program owner | Fleet security director | SGI screening rules; stand-alone systems (outside this boundary) |
| Common control providers | Group identity director (SYS-G1), Group SOC director (SYS-G2), Group cloud platform director (SYS-G3), Group HR director | Operate inherited controls (`common-control-catalog.csv`) |
| Station IT managers (3) | Station IT managers | Operate station LANs, endpoints, and printers |
| Independent assessor | Group internal audit | Assesses common controls once and samples the PBN-WMS (P07) |
| Independent CSP reviewer | Nuclear Oversight manager | 24-month security program review including cyber (73.55(m)); not part of this SSP's assessment |

## 6. System Information Types and System Categorization
Impact levels follow FIPS 199. Information types are named in the style of NIST SP 800-60 Vol. 2 Rev. 1; levels reflect the group's analysis of this system.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Maintenance and work management records | Moderate | Moderate | Moderate | Outage schedules and work history; outage delay is costly (P05 BP-NG04) but has paper fallbacks |
| CDA-related engineering and work package information | **High** | Moderate | Low | The aggregate of CDA identifiers, firmware versions, and network details across 5 units would give an adversary a target map for CDAs protected to the design basis threat (73.54(a)) |
| Clearance and tagging records | Low | **High** | Moderate | A wrong isolation record can injure a worker. Field verification compensates but does not remove the risk (P05 BP-NG03) |
| Personnel and access processing information | Moderate | Moderate | Moderate | Names, qualifications, and access requests for employees and outage contractors |
| Plant data replicas | Moderate | Moderate | Low | Copies only; nothing flows back to Level 3 |
| Information security (keys, access policies, logs) | High | High | Moderate | Compromise would expose every station |
| **PBN-WMS category (high-water mark)** | **High** | **High** | **Moderate** | Overall **High** |

**Baseline:** the NIST SP 800-53B **High** baseline, tailored. The plan documents **120 controls** in `control-implementation.csv`, all from the High baseline. Other High-baseline controls are fully inherited from the cloud providers (for example most PE controls for cloud data centers, evidenced by their SOC 2 Type 2 reports) or tailored out with a reason in the group tailoring register. CSF 2.0 subcategories come from NIST's CSF 2.0 to SP 800-53 Rev. 5.2.0 reference where it lists the control; for the 18 controls it does not list, the subcategory is an author mapping.

## 7. Authorization Boundary Description
- **Inside:** the business LANs, endpoints, servers, printers, and business DMZ at Stations A, B, and C; the kiosk update server; the fleet work management system in provider A and its replica and backups in provider B.
- **Outside, inherited (common control providers):** SYS-G1 identity platform, SYS-G2 SOC, SIEM, and EDR, and the SYS-G3 landing zone, WAN, and remote access service.
- **Outside, interconnected:** the hardware one-way devices and everything above them (Levels 3 and 4, SYS-N4), the security network (SYS-N5), the PMMD kiosks (SYS-N6), the CAP system (SYS-N3), the predictive maintenance service (SYS-N9), and the ERP (SYS-G4).
- **Never inside:** SGI (stand-alone systems SYS-N8), the CSP documents and CDA inventory (held on the CST's isolated program network), and the fleet operations center (NERC CIP Electronic Security Perimeter, SYS-N7).

The diagram is in P04 `cloud-architecture.md` (section 2.2).

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Level 3 plant networks (SYS-N4) | **Inbound only**, through hardware one-way devices | Plant process data to the replica servers | CSP defensive architecture; no outbound path exists |
| PMMD kiosks (SYS-N6) | Outbound (kiosks pull updates) | Malware signatures and kiosk software | CSP PMMD procedure. **Gap:** update packages are not signature-checked on the server before kiosks pull them (POAM-004) |
| CAP system (SYS-N3) | Two-way | Condition reports linked to work orders | SaaS contract; CAP procedure |
| Predictive maintenance service (SYS-N9) | Outbound | Selected equipment data from the replicas | Vendor contract (P10); outbound only |
| Engineering and Radiation Services and Radioactive Waste Management | Two-way (user access) | Work packages, outage files | Intercompany service agreements. **Gap:** no end-of-assignment notice (POAM-001) |
| External utilities and vendors | Outbound (transmittals) | Selected work packages and drawings | Document transmittal procedure. **Gap:** no screening for CDA details (POAM-003) |
| ERP (SYS-G4) | Two-way | Parts, costs, labor | Internal |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| Station business LANs and Wi-Fi | On-premises network | Stations A, B, C | Station IT managers |
| Endpoints (about 6,200) | Laptops, desktops, tablets | Stations A, B, C | Station IT managers |
| File, print, and application servers (about 140) | On-premises servers | Stations A, B, C | Station IT managers |
| Multifunction printers (about 310) | Network devices | Stations A, B, C | Station IT managers |
| Plant data replica servers (6) | On-premises servers in the business DMZ | Stations A, B, C | Fleet IT director |
| Kiosk update server (1) | On-premises server | Station A | Fleet IT director (operation); fleet cyber security program manager (content) |
| Work management application | Commercial application on managed compute and database (PaaS) | Provider A | Work management director |
| WMS replica and backups | Managed database replica; immutable vault | Provider B | Group cloud platform director |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv` (120 controls) and `common-control-catalog.csv` (91 group common or hybrid controls).

| Status | Controls |
|---|---|
| Implemented | 98 |
| Partially implemented | 22 |
| Planned | 0 |
| Not applicable | 0 |
| **Total** | **120** |

| Inheritance | Controls |
|---|---|
| Common/Inherited (from SYS-G1, SYS-G2, SYS-G3, group functions, station security, or the cloud providers) | 69 |
| Hybrid (group provides the mechanism; the stations or the WMS team configure or operate part) | 22 |
| System-specific | 29 |

**The 22 partially implemented controls** cluster in four places:
- **Cross-division people and devices** (scenario gap 1): AC-2, AC-2(3), AC-6, AC-17, AC-20, IA-3, CM-8, PS-5, PS-7.
- **CDA-related information in the WMS** (gap 2): AC-3, AC-21, AU-6, MP-3.
- **The kiosk update path** (gap 3): SC-7, SI-7.
- **Incident coordination and resilience** (gap 8 and others): IR-3, IR-6, IR-8, CP-4, MA-4, SA-9, SA-22.

### 10.2 Common control inheritance by division
The common control catalog lists 91 controls provided by corporate or by station security. Inheritance is **documented for Nuclear Generation** (2025 inheritance matrix), **for Engineering and Radiation Services** (2026 matrix), and for the PBN-WMS (this plan). It is **not documented for Radioactive Waste Management** (scenario gap 9). Until POAM-016 closes, that division cannot show which of its Part 37 and RCRA record protections rely on group controls, and P07 found CA-2 statements other than satisfied for this reason.

**What does not inherit.** CDAs, the security network, and the fleet operations center do not inherit from SYS-G1 to SYS-G3. Each station's CSP and the NERC CIP program provide their own controls. This separation is deliberate: a compromise of a group shared service must not become a path to CDAs.

### 10.3 Control assessment status
Common controls were assessed once, and the PBN-WMS and division controls sampled, from 2026-06-29 to 2026-08-28 by group internal audit. See P07 `assessment-results.csv` and `poam.csv`. The assessment stopped at the one-way devices; CSP controls are reviewed by Nuclear Oversight and inspected by the NRC.

## 11. Digital Identity Acceptance Statement
- **Workforce users** authenticate through SYS-G1 with MFA (number matching); **administrators** use phishing-resistant hardware keys and just-in-time PAM elevation.
- **Cross-division users** use the same SYS-G1 identities as their home division. That is efficient but means a phished engineer in another division is a station user (P08). The fix is assignment-bound access and a device check, not separate identities.
- **Vendor support** uses named, federated guest accounts with MFA. Sessions are not yet recorded (MA-4).
- **No CDA account** is federated to SYS-G1. CDA access is managed under the CSP.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud architecture and control map (P04), group and division risk registers (P01), gap analyses and regulation-by-division matrix (P03), group policies and division supplements (P06), assessment and POA&M (P07), incident response runbook and notification matrix (P08), SOC 2 readiness (P09), AI governance (P10).

## 13. Acronym List and Glossary
- **CAP:** corrective action program
- **CDA:** critical digital asset (a digital asset protected under the CSP, 73.54(b)(1))
- **CSP:** cyber security plan (73.54(e))
- **CST:** cyber security team (RG 5.71)
- **Defensive levels:** the CSP's security levels; CDAs at Levels 3 and 4, one-way data flow downward, the business network at Level 2 and below
- **One-way device:** a hardware device that lets data flow out of a higher level and allows nothing back
- **PMMD:** portable media and mobile devices; kiosks scan them before they connect to CDAs
- **SGI:** Safeguards Information (73.21-73.22)
- **WMS:** work management system

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-08-28 | Draft after P07 fieldwork | Fleet IT director |
| 1.0 | 2026-09-17 | Approved with authorization conditions | Group CISO |
