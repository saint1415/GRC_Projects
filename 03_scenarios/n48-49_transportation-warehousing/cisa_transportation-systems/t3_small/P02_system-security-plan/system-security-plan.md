# System Security Plan: Train Dispatch and PTC Operations Platform (TDPO)

**Organization:** Cris Santos Company, LLC (Class III short line freight railroad) | **Tier:** Small | **Vertical:** Transportation Systems
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Train Dispatch and PTC Operations Platform (**TDPO**), identifier CSC-SYS-001.

## 2. System Overview
The TDPO issues and records movement authority for every train and maintenance-of-way work group on the railroad's 186 route miles, and keeps the railroad's 8 PTC-equipped locomotives able to run on the Class I's PTC line. It supports train dispatching (BIA process BP-01), detector and crossing alarm monitoring (BP-06), and interchange over the trackage-rights segment (BP-03). Users: 6 train dispatchers, the Chief Dispatcher, 2 PTC administrators, the IT staff, and the dispatch system vendor.

**Major components:**
- **SYS-01:** the computer-aided dispatch system (CAD): primary and standby servers at HQ, 6 dispatch consoles, and the chief dispatcher desk
- **SYS-02:** PTC tenant components: onboard PTC apparatus on 8 locomotives, the PTC administration workstation, and the company's tenancy in the vendor-hosted PTC back office service
- **SYS-04 (dispatch part):** the dispatch VLAN, the IP radio gateway and consoles, 7 tower sites, 3 wayside detectors, and 14 crossing remote health monitors
- **SYS-05:** the identity provider (single sign-on and MFA)
- **SYS-08 (operations part):** 8 operations workstations
- **SYS-09 (backup part):** the cloud backup vault for the CAD servers

The cloud tenant is described by service category and is vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
Applicability was decided in P03, section 1.

| ID | Requirement | Citation | Effect on the TDPO |
|---|---|---|---|
| C-TRANSPORTATION-S01 | TSA Security Coordinator and reporting of significant security concerns | 49 CFR 1570.201; 1570.203 and Appendix A to part 1570 | A cyber attack on the TDPO must be reported to TSA within 24 hours of initial discovery |
| C-TRANSPORTATION-S02 | TSA rail security-sensitive materials (RSSM) | 49 CFR part 1580 subpart C | RSSM location answers within 30 minutes of a TSA request depend on TMS data and a working dispatch center |
| C-TRANSPORTATION-S03 | Sensitive Security Information | 49 CFR 1520.9 | Network diagrams and security plans for the TDPO are handled as SSI where TSA has marked them |
| C-TRANSPORTATION-S04 | FRA PTC, tenant duties | 49 CFR 236.1006, 236.1029, 236.1033 | Onboard units must be operative on the trackage-rights segment; service restoration plan |
| C-TRANSPORTATION-S05 | FRA accident/incident reporting | 49 CFR part 225 | Applies if a TDPO failure contributes to a reportable accident |
| C-TRANSPORTATION-BM | NIST CSF 2.0 with SP 800-82 Rev. 3 | Voluntary benchmark | The control objectives this plan measures against |
| C-TRANSPORTATION-R01 | TSA SD 1580-21-01E and 1580/82-2022-01E | Readiness reference only | Not applicable (no TSA designation); used to prioritize controls |
| C-TRANSPORTATION-R06, R07 | TSA surface cyber NPRM; CIRCIA | Proposed only | Tracked, not treated as obligations |
| Internal | Security policies POL-01 to POL-05 | P06 | Approved 2026-08-31 |

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the President and General Manager on 2026-08-31.
### 4.2 System Authorization Decision
The railroad is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- The President and General Manager accepted continued operation of the TDPO on 2026-08-31, with the conditions in the P07 POA&M. The first conditions are MFA on all remote and administrator access and vendor access through a jump host, by 2026-11-30.
- The majority owner accepted the Very High and High risks in P01 (R-001, R-003, R-004, R-005) only with dated treatment plans and the funded 2026 Q4 budget.
### 4.3 System Operational Status
Operational. Major modifications planned: the restricted operations zone (2027-01-31) and the alternate dispatch desk at North Yard (2027-06-30).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Vice President of Operations | Business owner; contingency planning; tenant PTC compliance |
| Risk acceptor (authorizing official equivalent) | President and General Manager | Accepts Moderate risk and system operation; majority owner accepts High and Very High |
| System security lead | IT Manager (proposed Cybersecurity Lead) | Day-to-day security of the TDPO; maintains this plan |
| TSA Security Coordinator | Manager of Safety and Security (primary); Chief Dispatcher (alternate) | TSA reporting and liaison (49 CFR 1570.201) |
| OT and radio owner | Signal and Communications Supervisor | Radio network, tower sites, detectors, crossing monitors |
| Onboard PTC owner | Chief Mechanical Officer | Onboard units and seals |
| Operations support | MSP; dispatch system vendor | Endpoint and firewall administration; CAD support |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1 (Ground Transportation, plus supporting types) and named in railroad terms. Impact levels follow the FIPS 199 definitions and were set by the railroad.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Movement authority (track warrants, track and time, train sheets, bulletins) | Low | **High** | Moderate | A corrupted or wrong authority could let two movements into the same limits, with PIH cars involved; manual dispatch limits the availability impact (P05 MTD 24 h) |
| PTC operational data (locomotive, crew, consist, onboard logs) | Low | Moderate | Moderate | Wrong train data degrades enforcement; outage stops interchange (P05 MTD 48 h) |
| Security and hazmat information (RSSM car lists, SSI, network diagrams) | Moderate | Moderate | Moderate | Disclosure aids an attacker and breaches 1520.9; TSA 30-minute answers need availability |
| Identity and access data | Moderate | Moderate | Moderate | Credential compromise opens every other type |
| **TDPO category (high-water mark)** | **Moderate** | **High** | **Moderate** | |

**Baseline and tailoring.** The high-water mark is High because of integrity. The railroad is not bound by FIPS 200, so it tailored as follows:
- It starts from the **SP 800-53B Moderate baseline**. The integrity of movement authority depends first on the operating rules (written authority, repeat-back, and CAD conflict checking as a second check), not on IT controls alone.
- It adds integrity and resilience controls that matter for a High integrity rating: SI-7, SI-10, and CP-7, all planned or partial today.
- The plan documents **60 controls** that address the P01 risks, the P03 gaps, and core network hygiene (`control-implementation.csv`).
- Other Moderate-baseline controls are either **inherited** from the SaaS and cloud providers (evidenced by SOC 2 reports, P09) or **out of scope** for this tier, recorded as a tailoring decision. Examples: PM-series program controls beyond PM-2.
- The President and General Manager accepted this tailoring on 2026-08-31. It is revisited if TSA designates the railroad (SD 2022-01E would then set the control scope).

## 7. Authorization Boundary Description
- **Inside:** the CAD servers and consoles; the PTC administration workstation; the 8 onboard PTC units; the company's configuration and accounts in the PTC back office service; the dispatch VLAN, radio gateway, tower sites, detectors, and crossing monitors (network and alarm path only); the identity provider tenant; the CAD backup vault in the cloud tenant.
- **Outside (interconnected):** the PTC back office vendor's platform; the Class I's dispatch and PTC systems and the interoperable messaging network; the TMS (SYS-03); the office LAN and office endpoints; the cloud provider's infrastructure; the MSP's remote management tool.
- **Not connected:** crossing warning circuits and detector logic run standalone. The network carries only their alarms.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Class I host railroad (dispatch) | Bidirectional (telephone and radio; train lineups by email) | Train lineups, authority to enter the segment | Trackage-rights agreement; interchange agreement |
| Class I PTC system via the interoperable messaging network | Bidirectional (through the PTC back office) | PTC messages for the company's onboard units | Host railroad requirements; PTC back office contract |
| PTC back office vendor (SaaS) | Bidirectional | Locomotive, crew, and consist data; onboard logs | Contract (99.5% availability; **no restoration time or incident notice**, gap) |
| TMS (SYS-03) | Inbound to the PTC workstation | Train consists | TMS subscription |
| Dispatch system vendor | Inbound remote support | Full server access | Support contract (**no security terms; always-on access**, gap) |
| MSP | Inbound remote management | Endpoint and firewall administration | Service agreement (**no security terms**, gap) |
| Cellular carrier | Inbound alarms | Detector and crossing monitor alarms | Carrier service terms (**public cellular, unencrypted**, gap) |

## 9. System Component Inventory
The OT part of this inventory is incomplete (P03 G-035; POAM-015).

| Component | Type | Location / provider | Owner |
|---|---|---|---|
| CAD primary and standby servers | Physical servers | HQ server room (both in one room, **gap**) | IT Manager |
| Dispatch consoles (6) and chief dispatcher desk | Workstations | Dispatch center | IT Manager |
| PTC administration workstation | Workstation | Dispatch center | Vice President of Operations |
| Onboard PTC apparatus (8) | OT, onboard | Road locomotives | Chief Mechanical Officer |
| PTC back office tenancy | SaaS | PTC back office vendor | Vice President of Operations |
| IP radio gateway and consoles | OT, network | HQ and dispatch center | Signal and Communications Supervisor |
| Tower sites (7) with microwave and cellular backhaul | OT, network | Wayside | Signal and Communications Supervisor |
| Wayside detectors (3) and modems | OT | Wayside | Signal and Communications Supervisor |
| Crossing remote health monitors (14) | OT | Wayside | Signal and Communications Supervisor |
| HQ firewall and dispatch VLAN switches | Network | HQ | IT Manager |
| Identity provider tenant | SaaS | Identity vendor | IT Manager |
| CAD backup vault | Cloud backup service | Cloud tenant (same account as production, **gap**) | IT Manager |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 60 controls:
- Implemented: 8
- Partially implemented: 36
- Planned: 16
- Not applicable: 0

### 10.2 Control assessment status
22 of these controls were assessed 2026-08-03 to 2026-08-07. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
- **Office and SaaS users** authenticate through the identity provider with a password and an authenticator app.
- **Administrators of the identity provider, the cloud console, and the PTC back office portal** use MFA today. Server administrators and VPN users do not yet (POAM-007).
- **Target:** phishing-resistant MFA (hardware security keys) for all administrators, the PTC administrators, and vendor access through the jump host. This is appropriate for High integrity data and remote access to operations systems.
- **Dispatchers** log on to the CAD application with named accounts. Console Windows log-ons must become named as well (POAM-022). Consoles do not lock, because a locked screen during a live authority is a safety risk; the dispatch center is badge-controlled and staffed at all times.

## 12. Referenced Artifacts
Scenario facts (`../scenario-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness and PTC back office vendor review (P09), AI assessment (P10), the 2019 manual dispatch procedure, the hazmat security plan (49 CFR 172.800).

## 13. Acronym List and Glossary
- **CAD:** computer-aided dispatch system
- **EDR:** endpoint detection and response
- **MFA:** multi-factor authentication
- **MSP:** managed service provider
- **OT:** operational technology
- **PIH:** material poisonous by inhalation
- **POA&M:** plan of action and milestones
- **PTC:** positive train control
- **RSSM:** rail security-sensitive materials (49 CFR 1580.3)
- **SSI:** Sensitive Security Information (49 CFR part 1520)
- **TDPO:** Train Dispatch and PTC Operations Platform
- **TMS:** transportation management system
- **TSOC:** TSA Transportation Security Operations Center
- **Track warrant:** written movement authority issued by the dispatcher in non-signaled territory

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan | IT Manager |
