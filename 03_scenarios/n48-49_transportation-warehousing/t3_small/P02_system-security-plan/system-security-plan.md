# System Security Plan: Terminal Operations and Gate Platform (TOGP)

**Organization:** Cris Santos Company, LLC (marine cargo terminal operator) | **Tier:** Small | **Vertical:** Transportation and Warehousing
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-04
**Handling:** Contains network and security measure details that will become part of the Cybersecurity Plan. Handle as sensitive security information (SSI) under 49 CFR part 1520 (33 CFR 101.630(b); POL-04).

## 1. System Name and Identifier
Terminal Operations and Gate Platform (**TOGP**), identifier CSC-SYS-001.

## 2. System Overview
The TOGP runs every cargo process at the company's Florida container and breakbulk terminal: vessel and yard planning, equipment dispatch, the truck gate, customs release and hold status, EDI with ocean carriers and trucking companies, and billing. It supports about 5 vessel calls a week, about 160,000 container moves a year and about 800 truck gate transactions a day. Users are 60 employees plus longshore labor, who use vehicle-mounted terminals (VMTs) on yard tractors.

**Major components:**
- **SYS-01:** the terminal operating system (TOS), a commercial product run by the company in its cloud tenant, with TOS gate servers on premises
- **SYS-02:** gate automation: OCR portals, TWIC card readers tied to the physical access control system (PACS), driver kiosks, and the gate transaction server
- **SYS-04:** EDI and data exchange with carriers, trucking companies, the port authority's port community system, and a customs data exchange service
- **SYS-05:** the identity provider (single sign-on and MFA)
- **SYS-10:** the public-cloud tenant hosting the TOS application servers, the TOS database, the EDI gateway and the integration server
- **SYS-07 (gate and yard segment):** the gate and yard network, the internet firewall and the VPNs
- **SYS-08 (operations endpoints):** planner and supervisor workstations, gate booth workstations, checker tablets and VMTs

The cloud tenant is described by service category and is vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| N48-49-R01 | USCG Cybersecurity in the Marine Transportation System | 33 CFR Part 101, Subpart F (101.600-101.670); 90 FR 6298. The TOGP contains critical IT systems and connects to critical OT systems as defined in 101.615 |
| MTSA | Facility security (the FSP, TWIC access control, security records) | 33 CFR Part 105 (for example 105.225 records; 105.255 access control) |
| Reporting | Cyber incident reporting to the FBI, CISA and the Captain of the Port; MTSA reporting to the NRC | 33 CFR 6.16-1; 33 CFR 101.305 |
| SSI | Protection of sensitive security information | 49 CFR part 1520 (the Cybersecurity Plan is SSI per 101.630(b)) |
| Safety | OSHA marine terminal standards (equipment and cargo handling safety) | 29 CFR part 1917. Relevant to OT and the scheduling pilot (P10) |
| State | Florida Information Protection Act (breach notification for employee and driver personal information) | Fla. Stat. 501.171 |
| Internal | Security policies POL-01 to POL-05 | P06 |

Not applicable: TSA rail, pipeline and aviation Security Directives (N48-49-R02 to R04); CMMC (N48-49-R07, no DoD contracts); SEC disclosure (N48-49-R08, private company). CTPAT (N48-49-R05) is voluntary; the company is not a partner.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the General Manager on 2026-09-04.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization. The equivalent internal decisions:
- The General Manager accepted continued operation of the TOGP on 2026-09-04, with the conditions in the P07 POA&M.
- The majority owner accepted the 4 High risks in P01 temporarily, with dated treatment plans.
- The Coast Guard approval that matters for this system is approval of the Cybersecurity Plan (101.630(d)), to be submitted by 2027-05-31, ahead of the 2027-07-16 deadline.
### 4.3 System Operational Status
Operational. Major modifications planned:
- an OT zone behind an internal firewall (P01 R-002), due 2027-03-31
- a backup architecture redesign (P01 R-004), due 2026-12-31
- replacement OCR servers, due 2026-11-30

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | General Manager | Overall accountability; risk acceptance up to Moderate |
| Risk acceptor (authorizing official equivalent) | Majority owner | Acceptance of High and Very High risks |
| Cybersecurity Officer (CySO), proposed | IT Manager | Day-to-day security; Subpart F duties in 101.625 once designated (due 2026-10-31) |
| Alternate CySO, proposed; Facility Security Officer | Security and Safety Manager | FSP, TWIC and PACS, MTSA reporting, drills and exercises |
| Business process owner | Operations Manager | TOS roles, gate procedures, manual release review |
| OT owner | Maintenance Manager | Crane and yard equipment controllers; crane vendor access |
| Operations support | Managed service provider | Help desk, patching, firewall, backup monitoring |
| Application support | TOS vendor | TOS support; hosted truck appointment and customer portal |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Water transportation (vessel, yard and gate operations; container location and status; hazardous cargo class and location) | Moderate | Moderate | Moderate | Wrong status or location data could release a held container or misplace hazardous cargo. Loss stops the terminal, but manual gate and vessel procedures limit the effect to about one shift before severe disruption (P05 MTD 8 to 12 h). Release of container data would help cargo theft |
| Logistics management (EDI with carriers, trucking companies, the port community system and the customs data exchange) | Moderate | Moderate | Moderate | Bills of lading and customs release status are commercially sensitive; false releases enable theft (P01 R-012, R-019) |
| Personal identity and authentication (driver names, license numbers, TWIC reader records) | Moderate | Moderate | Low | Florida personal information (Fla. Stat. 501.171); TWIC reader records are SSI (33 CFR 105.225(c)) |
| Revenue collection (billing, demurrage) | Low | Moderate | Low | Invoicing can wait 72 h (P05) |
| **TOGP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

Availability was considered for High, because a multi-day outage at a port can cause regional economic disruption, which is part of the definition of a transportation security incident (33 CFR 101.105). It was set at Moderate because manual procedures exist and the terminal is one of several at the port. The contingency plan (due 2026-12-31) must keep this assumption true.

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 60-person terminal operator. The plan documents the 73 controls that implement the Subpart F measures and core network hygiene (see `control-implementation.csv`). Two program controls outside the baseline, PM-2 and PM-9, were added by tailoring because Subpart F requires a designated CySO and a risk-based Plan. CSF 2.0 subcategories in the CSV come from the NIST CSF 2.0 to SP 800-53 crosswalk (`00_universal/crosswalks/csf2_to_sp800-53r5.csv`); the column is blank where the crosswalk lists none. Every other Moderate-baseline control is treated as follows:
- **Inherited** from the cloud, identity and TOS portal providers, as evidenced by their SOC 2 reports (P09).
- **Out of scope for this tier**, recorded as a tailoring decision, where the control's purpose applies only to federal systems.

## 7. Authorization Boundary Description
The boundary contains company-managed components and the company's configuration of vendor services:
- **Inside:**
  - the TOS application servers, the TOS database and the EDI and integration servers in the cloud tenant
  - the TOS gate servers, OCR servers, gate transaction server and driver kiosks in the gate complex
  - the gate and yard network, the internet firewall and both VPNs
  - the identity provider tenant
  - operations workstations, gate booth workstations, 12 checker tablets and 30 VMTs
- **Interconnected, outside the boundary:**
  - crane and RTG controllers (SYS-03, owned by the Maintenance Manager)
  - CCTV and the PACS server (SYS-09, owned by the FSO)
  - the scheduling optimization service (SYS-12)
  - the TOS vendor's hosted portal
  - carrier, trucking, port community system and customs data exchange partners

**Boundary weakness.** SYS-03 and the PACS sit on the same flat network segment as the in-boundary gate servers, so the boundary is not enforced at the network level today. The OT zone project (P01 R-002, due 2027-03-31) will enforce it.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Protection | Agreement |
|---|---|---|---|---|
| Ocean carriers (6 services) | Bidirectional EDI | Bay plans, load and discharge lists, container status | AS2 or SFTP for 5; **plain FTP for 1 (gap)** | Terminal services agreements |
| Trucking companies (about 350) | Inbound via hosted portal | Appointments, driver and truck details | TLS | Portal terms of use |
| Port community system (port authority) | Bidirectional API | Vessel schedules, gate status | TLS with API keys | Lease and data sharing terms |
| Customs data exchange service | Inbound | Release and hold status from U.S. Customs and Border Protection | SFTP | Service agreement |
| Crane and RTG controllers (SYS-03) | Bidirectional | Equipment job instructions, completions, positions | **Unencrypted OT protocols on a flat network (gap)** | Internal |
| PACS (SYS-09) | Inbound to gate | TWIC validation results | Flat network (gap) | Internal |
| Scheduling optimization service (SYS-12) | Bidirectional API | Move history, schedules, recommended plans | TLS | Pilot agreement; **no security review (gap)** |
| Crane vendor | Inbound remote access | PLC and HMI diagnostics | **Always-on cellular appliance (gap)** | Service contract with no notification clause |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| TOS application servers (2) | Cloud virtual machines | Cloud tenant | IT Manager |
| TOS database | Managed database service | Cloud tenant | IT Manager |
| EDI gateway and integration server | Cloud virtual machines | Cloud tenant | IT Manager |
| Database snapshots | Provider snapshot service | Cloud tenant (production account, **gap**) | IT Manager |
| Identity provider tenant | SaaS | Identity vendor | IT Manager |
| TOS gate servers (2), gate transaction server | Physical servers | Gate server room | IT Manager |
| OCR servers (2) and 3 OCR portals | Physical servers and camera controllers | Gate complex | Operations Manager |
| Driver kiosks (3) | Kiosk PCs | Gate lanes | Operations Manager |
| Internet firewall, VPN appliance, core and yard switches, Wi-Fi controller | Network | Office and gate server room | IT Manager (MSP administers) |
| Operations workstations (24), gate booth workstations (4), tablets (12), VMTs (30) | Endpoints | Office, gate, yard | IT Manager |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 73 controls:
- Implemented: 11
- Partially implemented: 42
- Planned: 20
- Not applicable: 0

### 10.2 Control assessment status
Assessed 2026-08-10 to 2026-08-14. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
Office, TOS and cloud users authenticate through the identity provider with a unique ID and password. MFA (authenticator app) is enforced today only for email and the TOS administrator group. Given the Moderate categorization, the Subpart F requirement for MFA on password-protected IT systems (101.650(a)(4)), and the ransomware risk (P01 R-001), password-only access is **not acceptable** for the VPN or TOS users. MFA for all TOS users and the VPN is due 2026-11-30. Gate booth workstations will use named accounts with badge-tap sign-in plus a PIN, because gate throughput cannot absorb a phone prompt at every shift change. HMIs that cannot support MFA are not remotely accessible after the OT zone project; their compensating controls will be documented in the Cybersecurity Plan.

Truck drivers do not sign in to the TOGP. They are identified at the gate by TWIC or driver license and appointment number, under the FSP.

## 12. Referenced Artifacts
Scenario facts (`../scenario-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness (P09), AI assessment (P10), Facility Security Plan and Facility Security Assessment (SSI, held by the FSO).

## 13. Acronym List and Glossary
- **CySO:** Cybersecurity Officer (33 CFR 101.615)
- **EDI:** electronic data interchange
- **FSO / FSP / FSA:** Facility Security Officer / Plan / Assessment (33 CFR Part 105)
- **HMI:** human-machine interface
- **KEV:** Known Exploited Vulnerability
- **NRC:** National Response Center
- **OCR:** optical character recognition
- **OT:** operational technology
- **PACS:** physical access control system
- **PLC:** programmable logic controller
- **RTG / STS:** rubber-tired gantry crane / ship-to-shore crane
- **SSI:** sensitive security information (49 CFR part 1520)
- **TOS:** terminal operating system
- **TWIC:** Transportation Worker Identification Credential
- **VMT:** vehicle-mounted terminal

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-09-04 | Initial plan | IT Manager |
