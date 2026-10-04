# System Security Plan: Terminal Operations Platform (TOP)

**Organization:** Cris Santos Company Holdings, Inc. (Marine Terminals division, with corporate shared services) | **Tier:** Multi-Sector | **Vertical:** Transportation and Warehousing
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-15
**Handling:** Contains network and security measure details that feed the terminals' Cybersecurity Plans. Handle as sensitive security information (SSI) under 49 CFR part 1520 (33 CFR 101.630(b); POL-04).

> **Why this system.** At this tier the SSP can cover one system per division or a shared corporate system. The group chose the **Terminal Operations Platform**, the focus division's primary system, because the BIA (P05) ranks vessel, gate and yard operations among the most time-critical processes in the group, because it contains critical IT systems and connects to critical OT systems under 33 CFR 101.615 at six regulated facilities, and because it inherits most of its controls from corporate (SYS-G1 to SYS-G4). Freight Trading's federal sales workspace (SYS-F3) has its own CMMC Level 1 scope document, and the Gulf terminals' legacy TOS (SYS-T1L) has an interim plan until it migrates to the TOP on 2027-06-30. Both inherit from the same common control catalog (`common-control-catalog.csv`).

## 1. System Name and Identifier
Terminal Operations Platform (**TOP**), identifier CSCH-MT-SYS-T1.

## 2. System Overview
The TOP runs every cargo process at terminals T1 to T6 (Florida ports 1 and 2, and the Georgia port): vessel and yard planning, equipment dispatch, the truck gates, customs release and hold status, partner EDI and billing. Those six terminals handle most of the division's 5.6 million container moves a year and about 10,000 of the 14,000 daily truck gate transactions. Users are about 6,200 permanent staff (planners, superintendents, clerks, customer service, billing, IT and OT staff), about 9,500 registered longshore workers who use vehicle-mounted terminals (VMTs), and 212 Freight Trading users under the "group logistics" role (scenario gap 1).

**Major components:**
- **SYS-T1:** the standard terminal operating system (vessel, yard and gate modules, equipment dispatch, billing, EDI adapters), one multi-terminal instance of commercial TOS software run by the division in group cloud provider A, with a warm replica in provider B
- **SYS-T2 at T1 to T6:** gate automation: OCR portals, TWIC readers tied to each terminal's physical access control system (PACS), driver kiosks and gate servers
- **Operations endpoints at T1 to T6:** planner and superintendent workstations, gate booth workstations, checker tablets and VMTs
- **Equipment interface:** the TOS interface servers that send job instructions to crane, RTG and ASC controllers and to the T5 equipment control system (the controllers themselves are SYS-T3, interconnected)

The platform is described by service category and is vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies to the TOP |
|---|---|---|---|
| N48-49-R01 | USCG Cybersecurity in the Marine Transportation System | 33 CFR Part 101, Subpart F (101.600-101.670); 90 FR 6298 | T1 to T6 are facilities required to have an FSP under 33 CFR Part 105, so Subpart F applies (101.605(a)). The TOS, gate automation and the equipment interface are critical IT systems designated by the CySO (101.615) |
| MTSA | Facility security (FSPs, TWIC access control, security records) | 33 CFR Part 105 (for example 105.225 records; 105.255 access control) | PACS records are SSI (105.225(c)); TWIC checks at the gate |
| Reporting | Cyber incident reporting to the FBI, CISA and the Captain of the Port; NRC reporting of breaches of security and suspicious activity | 33 CFR 6.16-1; 33 CFR 101.305; 101.620(b)(7) | Immediate reporting duties for each affected terminal (P08) |
| SSI | Protection of sensitive security information | 49 CFR part 1520 | The Cybersecurity Plan is SSI (101.630(b)) |
| Shipping Act | Marine terminal operator prohibitions | 46 U.S.C. 41106(2) | A marine terminal operator may not give "any undue or unreasonable preference or advantage" to any person. Relevant to the group logistics role and the reserved appointment slots at T3 and T5 (scenario gap 1; P03) |
| Safety | OSHA marine terminal standards | 29 CFR part 1917 | Equipment and cargo handling safety; relevant to the automatic ASC job sequencing at T5 (P10) |
| N48-49-R05 | CTPAT | CBP program (voluntary) | The division is a partner (marine port authority and terminal operator); its cybersecurity criteria are met through group controls |
| N48-49-R08 | SEC cybersecurity disclosure | Reg S-K Item 106; Form 8-K Item 1.05 | A TOP incident may be material to the group (P08) |
| State | Breach notification for employee and driver personal information | Each state where affected individuals reside (Florida worked example: Fla. Stat. 501.171) | Driver names and license numbers in gate transactions |
| Contracts | Terminal services agreements | Confidentiality of customer cargo data | Breached in substance by the group logistics role (P03) |
| Internal | Group policies POL-01 to POL-05 and the Marine Terminals supplement | P06 | |

Not applicable to the TOP: TSA rail, pipeline and aviation Security Directives (N48-49-R02 to R04; the group does not operate those modes); CMMC and DFARS (N48-49-R07; no federal contract information is in the TOP, they apply to Freight Trading's SYS-F3); 49 U.S.C. 41712 (N48-49-R06; airlines only).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Marine Terminals director of terminal systems (system owner), the Division CySO and the Group CISO on 2026-09-15, after the board risk committee review.

### 4.2 System Authorization Decision
The group is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- **Decision:** authorized to operate with conditions, 2026-09-15, by the Group CISO and the Marine Terminals division president, with the Group Chief Risk Officer for the High risks.
- **Conditions:** (1) remove the group logistics role and replace it with a cargo-owner view limited to Freight Trading's own bills of lading by 2026-11-30 (POAM-008); (2) return the T5 optimization service to advisory mode until a safety case and AI council approval exist (POAM-010; P10); (3) change the default passwords found in P07 by 2026-09-30 (POAM-006).
- **Coast Guard approval** that matters for this system is approval of each terminal's Cybersecurity Plan (101.630(d)). The plans for T1 to T6 will be submitted by 2027-04-30, ahead of the 2027-07-16 deadline (101.655).
- **Reauthorization:** annually, and when T7 to T9 join the platform (2027-06-30).

### 4.3 System Operational Status
Operational. **Major modifications planned:** onboarding T7 to T9 (2027-06-30); application allowlisting on operations workstations (2026-12-31); OT inventory and device configuration documentation for T1 to T4 and T6 (2027-03-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Marine Terminals director of terminal systems | Accountable for the TOP and this SSP |
| Authorizing official equivalent | Group CISO with the Marine Terminals division president | Authorization decision; Moderate risk acceptance (division president) |
| High risk acceptance | Group Chief Risk Officer with the Group CISO | Reported to the board risk committee |
| Cybersecurity Officer (CySO) | Marine Terminals Division CySO (designated 2026-03-02 for all 9 facilities, 101.625(b)) | Subpart F duties in 101.625(d); Cybersecurity Plans and Assessments |
| Alternate CySOs | Terminal IT and OT leads, T1 to T6 | 24x7 coverage per terminal |
| Facility Security Officers | One per terminal | FSPs, TWIC and PACS, MTSA drills and reporting |
| OT owner | Marine Terminals director of engineering | SYS-T3 controllers and the equipment interface on the OT side |
| Data owners | Terminal general managers | Approve TOS roles for their terminal's data |
| Common control providers | Group identity director (SYS-G1), Group SOC director (SYS-G2), Group cloud platform director (SYS-G3), Group integration services director (SYS-G4) | Operate inherited controls (`common-control-catalog.csv`) |
| Independent assessor | Group internal audit | Assesses common controls once and samples division controls (P07); meets the independence rule for Cybersecurity Plan audits (101.630(f)(4)) |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Water transportation (vessel, yard and gate operations; container location and status; holds; hazardous cargo class and location; equipment job instructions) | Moderate | **High** | **High** | Wrong job instructions at T5 move automated cranes; a wrong hold status releases a held container; a lost hazardous cargo location endangers responders. Six terminals at three ports share one TOS instance, so a multi-day outage could cause the regional economic disruption that defines a transportation security incident (33 CFR 101.105) |
| Logistics management (carrier EDI, customs status, port community system messages) | Moderate | High | Moderate | Bills of lading and customs status are commercially sensitive; a false release enables theft. Partners can resend messages |
| Customer commercial data (cargo owners' shipments, volumes and appointments) | **Moderate** | Moderate | Low | Confidential under terminal services agreements; affiliate access raises Shipping Act issues (scenario gap 1) |
| Personal identity and authentication (driver names, license numbers, TWIC reader records) | Moderate | Moderate | Low | State breach laws; PACS records are SSI (33 CFR 105.225(c)) |
| Revenue collection (billing, demurrage) | Low | Moderate | Low | Invoicing can wait 72 hours (P05) |
| **TOP category (high-water mark)** | **Moderate** | **High** | **High** | Overall **High** |

**Baseline:** the NIST SP 800-53B **High** baseline, tailored. The plan documents **219 controls** in `control-implementation.csv`:
- 217 from the High baseline;
- 2 program management controls not in any baseline (PM-2, because Subpart F requires a designated CySO, and PM-9, because the Cybersecurity Plan must be risk-based).

The other 153 High-baseline controls are either fully inherited from the cloud providers (for example most PE controls for data centers, evidenced by their SOC 2 Type 2 reports), covered by facility security under the FSPs, or tailored out with a reason in the group tailoring register (for example IA-2(12), which applies to federal PIV credentials). CSF 2.0 subcategories in the CSV come from the NIST CSF 2.0 to SP 800-53 crosswalk (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`, first six listed); the column is blank where the crosswalk lists none.

## 7. Authorization Boundary Description
- **Inside:** SYS-T1 in provider A (application, database, EDI adapters and equipment interface servers) and its replica in provider B; SYS-T2 gate automation at T1 to T6; operations endpoints and VMTs at T1 to T6; the terminal IT and gate zones of SYS-T4 at T1 to T6.
- **Outside, inherited (common control providers):** SYS-G1 identity, SYS-G2 SOC, SIEM and EDR, SYS-G3 landing zone, WAN and backup vault, and SYS-G4 integration hub.
- **Outside, interconnected:** SYS-T3 crane, RTG and ASC controllers and the T5 equipment control system (owned by the director of engineering, in OT zones); SYS-T5 optimization service; SYS-T6 customer portal and truck appointment system; each terminal's PACS; carriers, the customs data exchange service and port community systems (through SYS-G4).
- **Not yet in the platform:** T7 to T9 and SYS-T1L (interim plan; migration due 2027-06-30).

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Protection | Agreement |
|---|---|---|---|---|
| Ocean carriers (through SYS-G4) | Bidirectional EDI | Bay plans, load and discharge lists, container status | AS2 or SFTP; **plain FTP for 2 carriers (gap)** | Terminal services agreements |
| Customs data exchange service (through SYS-G4) | Inbound | Release and hold status from U.S. Customs and Border Protection | SFTP with certificates | Service agreement |
| Port community systems at 3 ports (through SYS-G4) | Bidirectional API | Vessel schedules, gate status | TLS with API keys | Port data sharing terms (the Georgia agreement predates current security terms) |
| SYS-T3 controllers and T5 equipment control system | Bidirectional | Job instructions, completions, positions | OT zone firewall; OT protocols unencrypted inside the zone (compensating control documented) | Internal |
| SYS-T5 optimization service | Bidirectional API | Move history, schedules, recommended plans; **automatic ASC job sequences at T5 since 2026-03 (gap 8)** | TLS | Vendor SaaS agreement |
| SYS-T6 customer portal | Bidirectional API | Appointments, availability, holds shown to cargo owners | TLS | Internal |
| Freight Trading users (group logistics role) | Outbound to users | **Cargo, vessel and appointment data for every customer (gap 1)** | SYS-G1 sign-in with MFA | None. To be removed (POAM-008) |
| Crane and equipment vendors | Inbound remote access | PLC and HMI diagnostics | Group jump host, per-session approval, recording | Service contracts (2 lack notification terms) |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| TOS application and equipment interface servers | Cloud virtual machines in a dedicated account | Provider A | Director of terminal systems |
| TOS database | Managed database service | Provider A, replica in provider B | Director of terminal systems |
| EDI adapters | Containers | Provider A | Director of terminal systems |
| Gate servers, OCR servers and portals, driver kiosks | Physical servers and devices | Gate complexes T1 to T6 | Terminal general managers |
| Operations workstations, gate booth workstations, tablets, VMTs | Endpoints | Terminals T1 to T6 | Director of terminal systems |
| Terminal IT and gate zones, Wi-Fi | Network | Terminals T1 to T6 | Group network operations with terminal IT leads |
| Backups and replica | Backup service and immutable vault | Provider B | Group cloud platform director |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv` (219 controls) and `common-control-catalog.csv` (161 group common controls).

| Status | Controls |
|---|---|
| Implemented | 188 |
| Partially implemented | 31 |
| Planned | 0 |
| Not applicable | 0 |
| **Total** | **219** |

| Inheritance | Controls |
|---|---|
| Common/Inherited (from SYS-G1 to SYS-G4, group functions or the cloud providers) | 124 |
| Hybrid (group provides the mechanism; the division configures or operates part) | 37 |
| System-specific | 58 |

**The 31 partially implemented controls** cluster in four places:
- **Commercial data segregation** (scenario gap 1): AC-2, AC-3, AC-6, AC-6(7), AC-21, CM-12.
- **Subpart F program work at the terminals** (gap 3): AT-2, AT-3, AT-4, CP-3, IR-2, PL-2, PS-7, RA-3, CM-7(2), CM-7(5), CM-8, SI-2, MP-7, IA-5 (the default passwords found in P07).
- **AI and change control at T5** (gap 8): CA-9, CM-4, and the untested T5 restore (CP-4).
- **Incident notification and partners** (gap 7 and supply chain): IR-3, IR-6, IR-8, CA-3, SC-8, SC-8(1), SA-4, SR-8.

### 10.2 Common control inheritance by division
The common control catalog lists 161 controls provided by corporate. Inheritance is **documented for Marine Terminals** (2025 inheritance matrix, now confirmed by this plan) and **for Freight Trading** (2025 matrix, referenced in its CMMC Level 1 scope). It is **not documented for Port Real Estate** (scenario gap 6). Until POAM-019 closes, Port Real Estate cannot show which of its building system and payment safeguards are met by group controls; P07 found its CA-2 statements other than satisfied for this reason.

### 10.3 Control assessment status
Common controls were assessed once, and TOP and division controls sampled, from 2026-07-06 to 2026-08-28 by group internal audit, with OT tests at T5 on the night of 2026-08-12. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
- **Workforce users** authenticate through SYS-G1 federated sign-in with MFA (number matching). **Administrators** use phishing-resistant hardware keys and just-in-time PAM elevation. This meets 101.650(a)(4) for password-protected IT systems.
- **Gate booth workstations** use named badge-tap sign-in plus a PIN, because gate throughput cannot absorb a phone prompt at every shift change.
- **Longshore workers** sign in to VMTs with a TWIC tap plus PIN under individual operator IDs, which meets the separate credentials rule (101.650(a)(6)).
- **Service accounts** for EDI adapters should use certificates or short-lived tokens; 14 still use static passwords (POAM-006).
- **OT HMIs** that cannot support MFA are not remotely accessible except through the jump host; compensating controls will be documented in each Cybersecurity Plan.
- **Truck drivers, carriers and cargo owners** do not sign in to the TOP. Drivers are identified at the gate by TWIC or license and appointment number under the FSP; cargo owners use SYS-T6.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud architecture and control map (P04), group and division risk registers (P01), gap analyses and regulation-by-division matrix (P03), group policies and division supplements (P06), assessment and POA&M (P07), incident response runbook and notification matrix (P08), SOC 2 readiness (P09), AI governance (P10), Facility Security Plans and draft Cybersecurity Plans (SSI, held by the FSOs and the CySO).

## 13. Acronym List and Glossary
- **ASC:** automated stacking crane
- **Common control:** a control provided once by corporate and inherited by several systems
- **CySO:** Cybersecurity Officer (33 CFR 101.615)
- **EDI:** electronic data interchange
- **FSO / FSP:** Facility Security Officer / Facility Security Plan (33 CFR Part 105)
- **HMI / PLC:** human-machine interface / programmable logic controller
- **KEV:** Known Exploited Vulnerability
- **NRC:** National Response Center
- **OCR:** optical character recognition
- **PACS:** physical access control system
- **RTG / STS:** rubber-tired gantry crane / ship-to-shore crane
- **SSI:** sensitive security information (49 CFR part 1520)
- **TOP / TOS:** Terminal Operations Platform / terminal operating system
- **TWIC:** Transportation Worker Identification Credential
- **VMT:** vehicle-mounted terminal

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-08-31 | Draft after P07 fieldwork | Marine Terminals director of terminal systems |
| 1.0 | 2026-09-15 | Approved with authorization conditions | Group CISO |
