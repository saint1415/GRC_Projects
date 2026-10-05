# System Security Plan: Train Dispatch and PTC Operations Platform (TDPO)

**Organization:** Cris Santos Company, Inc. (PE-backed Class II regional freight railroad) | **Tier:** Mid-Market | **Vertical:** Transportation Systems
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-15

## 1. System Name and Identifier
Train Dispatch and PTC Operations Platform (**TDPO**), identifier CSC-TDPO-01. The TDPO is the company's major system and the core of the Critical Cyber Systems listed in its TSA-approved Cybersecurity Implementation Plan (CIP). It comprises the components in section 2, drawn from SYS-01 to SYS-09 in `../00_company-facts.md`.

## 2. System Overview
The TDPO controls and records every train movement on 512 route miles of company track and on the 52-mile trackage-rights segment, and it dispatches the 2 affiliated short lines. It supports the High-criticality processes in the BIA (P05): dispatching (BP-01, BP-02), CTC field operation (BP-04), PTC tenant operations (BP-03), crew calling (BP-05), and the RSSM location duty (BP-07). About 70 people use it directly (36 dispatchers, PTC administrators, signal maintainers, crew callers), and every train crew depends on it.

**Major components:**
| ID | Component | Hosting and service model |
|---|---|---|
| SYS-01 | CAD/CTC office system: CTC control, track warrants, train sheets, work authority, bulletins; 22 consoles | On premises: primary cluster in the HQ data center, hot standby at the backup NOC |
| SYS-02 | PTC tenant systems: back office server (BOS) pair, 3 PTC administration workstations, onboard apparatus on 46 locomotives, messaging link to the host Class I | On premises and onboard; PTC vendor managed service through the PAM jump host |
| SYS-03 | CTC field network: 150 wayside signal locations with non-vital communication controllers; code line over radio, microwave, and 2 leased circuits | Wayside OT |
| SYS-04 (part) | Radio-over-IP gateways and dispatcher radio consoles; tower site backhaul that carries the code line | On premises and wayside OT |
| SYS-05 (part) | Directory domain for the dispatch zones; identity provider for remote and privileged access | On premises and SaaS |
| SYS-07 | Crew management and hours-of-service application | Company cloud, operations workloads account (P04) |
| SYS-08 (part) | Operations workloads account and backup and recovery account (write-once vault for SYS-01, SYS-02, SYS-07) | Public cloud IaaS/PaaS, vendor-agnostic (P04) |
| SYS-09 (part) | Dispatch zones at the HQ data center and both NOCs, IT/OT boundary firewalls, 28 operations workstations | On premises |

Detectors and crossing monitors (rest of SYS-04), the TMS (SYS-06), and the security tooling (SYS-10) connect to the TDPO as interconnected systems (section 8).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it affects the TDPO |
|---|---|---|---|
| C-TRANSPORTATION-R01 | TSA SD 1580/82-2022-01E, Rail Cybersecurity Mitigation Actions and Testing | Sections II to VI | The TDPO components are Critical Cyber Systems; segmentation, access control, monitoring, patching, and assessment measures in the TSA-approved CIP apply. Mapped in `control-implementation.csv` |
| C-TRANSPORTATION-R01 | TSA SD 1580-21-01E, Enhancing Rail Cybersecurity | Sections II.B to II.E | Cybersecurity Coordinators, 72-hour CISA incident reporting, Cybersecurity Incident Response Plan and annual exercises |
| C-TRANSPORTATION-S01 | TSA Security Coordinator and significant security concern reports | 49 CFR 1570.201, 1570.203 | Cyber attacks on the TDPO are reportable to TSA within 24 hours; a CISA report under the SD that says so satisfies 1570.203 (SD 1580-21-01E II.C.5) |
| C-TRANSPORTATION-S02 | RSSM location and chain of custody | 49 CFR 1580.203, 1580.205 | Dispatcher train sheets and the TMS answer TSA's 30-minute requests |
| C-TRANSPORTATION-S03 | SSI | 49 CFR part 1520 | CIP, CAP, assessment results, and incident reports about the TDPO are SSI |
| C-TRANSPORTATION-S04 | PTC tenant duties; signal housing security | 49 CFR 236.1006, 236.1029, 236.1033; 236.3 | Onboard apparatus and BOS must keep company trains able to run under the host's certified PTC system; signal housings locked |
| C-TRANSPORTATION-S09 | Hours of duty records | 49 CFR 228.11 | The crew management application keeps the records |
| C-TRANSPORTATION-R06, R07 | TSA surface cyber NPRM; CIRCIA | 89 FR 88488; 89 FR 23644 | **Proposed only.** Tracked in P03 section 6 |
| Contract | Services agreements with the affiliated and contracted short lines | Contract | Dispatch restoration within 2 hours; SOC 2 Type 2 report on the shared service (P09) |
| Internal | Security policies POL-01 to POL-05 and supporting standards | P06 | Policy basis for every control |

Not applicable:
- **PTC on company track (49 CFR 236.1005(b)(1)).** The company is not a Class I railroad and does not host passenger service.
- **SEC cybersecurity disclosure.** The company is privately held.
- **PCI DSS.** No card payments.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Chief Operating Officer (system owner) on 2026-09-15, after the control assessment (P07) and before the audit committee meeting the same day.

### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization to operate. TSA approves the CIP, not the system. The equivalent internal decision:
- **Decision:** operation of the TDPO accepted with conditions, 2026-09-15.
- **Authorizing official equivalent:** Chief Executive Officer for High and Very High risks; Chief Operating Officer for Moderate and below (P01 acceptance authorities).
- **Conditions:** the High-risk POA&M items in P07 must meet their milestones; the CIP amendment for field zones and newly identified Critical Cyber Systems is filed with TSA within 50 days of the permanent change (SD 1580/82-2022-01E VI.D); re-decision by 2027-09-30 or after a major change.

### 4.3 System Operational Status
Operational. Major modifications planned:
- Field zone segmentation of the backhaul at the 38 tower sites (due 2027-03-31)
- Moving the radio and detector vendors' access to the PAM jump host (due 2026-12-31)
- Forwarding CAD/CTC, BOS, and field device logs to the SIEM and extending the MSSP contract to OT (due 2027-01-31)
- Clean-room recovery environment for CAD/CTC and the BOS in the backup account (due 2027-03-31)

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Chief Operating Officer | Accountable for the TDPO; accepts Moderate risk; executive sponsor of the security program |
| Authorizing official equivalent (High risk) | Chief Executive Officer | Accepts High risk; approves the risk appetite |
| Oversight | Board audit committee | Quarterly cyber risk reporting |
| Program strategy | vCISO (part-time contractor) | Program strategy, board reporting, SSP review |
| System security lead | Cybersecurity Manager | Primary TSA Cybersecurity Coordinator; owner of the CIP and CAP; day-to-day control owner |
| Infrastructure | Director of Information Technology | Servers, networks, identity, cloud; alternate Cybersecurity Coordinator |
| Business owner (dispatch) | Director of Network Operations | Dispatch procedures, manual dispatch, consoles, access approvals |
| Business owner (PTC) | PTC Program Manager | BOS, onboard apparatus data, host coordination |
| Field OT | Director of Signals and Communications | CTC field equipment, code line, radio, tower sites |
| Physical and TSA security | Director of Safety, Security, and Hazmat | Primary Security Coordinator; NOC and housing physical security; SSI |
| Independent assessment | Co-sourced internal audit firm | Annual IT audit; P07; CAP assessments |
| Monitoring | MSSP | 24x7 monitoring of IT logs and EDR |

## 6. System Information Types and System Categorization
Information types come from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Ground transportation (movement authority, train sheets, CTC indications, PTC data) | Low | Moderate | Moderate | Movement data is not secret, but altered authority or indications could contribute to a collision; vital field logic and PTC enforcement independently protect signals and the trackage-rights segment; manual dispatch keeps trains moving at reduced capacity (P05 MTD 4 hours) |
| Hazardous materials transportation (RSSM car locations, consists) | Moderate | Moderate | Moderate | PIH car locations are security-sensitive; TSA's 30-minute duty makes availability important, but the printed fallback limits the impact |
| Security information (CIP, network designs, assessment results) | Moderate | Moderate | Low | SSI under 49 CFR part 1520; disclosure would aid an attacker |
| Human resources management (crew identities, hours of duty records) | Moderate | Moderate | Moderate | Personal information; hours records are regulatory records (228.11) |
| System and network monitoring (logs) | Moderate | Moderate | Low | Needed for incident investigation and TSA reporting |
| **TDPO category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Integrity was considered for High.** An attacker who could change CTC route requests or track warrants could put trains in conflict. The team kept integrity at Moderate for three reasons: vital interlocking logic in the field will not display a proceed signal for a conflicting route, whatever the office system sends; PTC enforces authority on the trackage-rights segment; and dispatchers and crews repeat and confirm every track warrant by radio. To compensate, the baseline adds integrity tailoring: CM-3 for field controller changes, SI-7 for software and firmware, SI-10 for consist validation before PTC initialization, and CA-8 (adversarial testing) added by tailoring.

## 7. Authorization Boundary Description
**Inside the boundary:**
- CAD/CTC servers, databases, and 22 consoles at both NOCs;
- BOS pair, PTC administration workstations, and the onboard apparatus on 46 locomotives (configuration and data, not the host's certified system);
- 150 CTC field communication controllers and the code line;
- radio-over-IP gateways, dispatcher radio consoles, and the tower site backhaul;
- the dispatch zone directory domain and the identity provider policies that protect remote and privileged access;
- the operations workloads and backup and recovery accounts in the cloud landing zone (crew management application, backup vault);
- the dispatch zones, IT/OT boundary firewalls, and PAM jump hosts.

**Outside the boundary (interconnected):**
- the host Class I's PTC system and back office, and the industry interoperable messaging network;
- the 2 Class I interchange partners' EDI services;
- the TMS (vendor SaaS);
- the corporate network, office endpoints, email, and ERP;
- detectors and crossing monitors (they share the backhaul but are separate systems in the CIP);
- the MSSP's SIEM and EDR platforms;
- the affiliated short lines' crews and radio users.

The diagram is in P04 `cloud-architecture.md`, and the field zone diagram is in the CIP (SSI, not reproduced here).

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Host Class I PTC system (via the interoperable messaging network) | Bidirectional | PTC messages, track data, locomotive and train data | PTC interoperability and trackage-rights agreements |
| Class I interchange partners (2) | Bidirectional (EDI over TLS through the TMS) | Interchange reports, consists | EDI agreements |
| TMS (vendor SaaS) | Inbound consists and car data; outbound train movement events | Consists, waybill references, RSSM car flags | Contract; SOC 2 Type 2 reviewed (P09) |
| Crew tablets (MDM-managed) | Outbound bulletins and train lists; inbound hours entries | Bulletins, train lists, hours | Internal |
| Affiliated short lines | Radio and phone; read-only train sheet view | Movement authority | Services agreements (**no interconnection terms**, gap in CA-3) |
| MSSP | Outbound logs from IT parts of the boundary; remote EDR actions | Security logs | Contract (**excludes OT**, gap 10) |
| CAD/CTC vendor and PTC vendor | Inbound support sessions through the PAM jump host | Configuration, logs | Support contracts |
| Radio system vendor and detector vendor | Inbound always-on access | Configuration | **No security terms; access outside the jump host (gap 3)** |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| CAD/CTC server cluster and database | Servers | HQ data center (primary); backup NOC (standby) | Director of Network Operations |
| Dispatch consoles (16 primary NOC, 6 backup NOC) | Endpoint (OT) | Both NOCs | Director of Network Operations |
| CTC maintenance workstations (3) | Endpoint (OT) | HQ, backup NOC, Southern Yard | Director of Signals and Communications |
| BOS pair | Servers | HQ data center; backup NOC | PTC Program Manager |
| PTC administration workstations (3) | Endpoint (OT) | HQ NOC | PTC Program Manager |
| Onboard PTC apparatus (46) | Onboard OT | Road locomotives | Chief Mechanical Officer (hardware); PTC Program Manager (data) |
| CTC field communication controllers (150) | Wayside OT | Signal locations | Director of Signals and Communications |
| Code line radios, microwave, 2 leased circuits | Network (OT) | 38 tower sites | Director of Signals and Communications |
| Radio-over-IP gateways and dispatcher radio consoles | Network (OT) | Both NOCs | Director of Signals and Communications |
| IT/OT boundary firewalls and dispatch zone switches | Network | HQ data center; both NOCs | Director of Information Technology |
| PAM jump hosts | Servers | HQ data center | Cybersecurity Manager |
| Dispatch zone directory domain controllers | Servers | HQ data center; backup NOC | Director of Information Technology |
| Crew management application and database | Virtual machines and managed database | Operations workloads account | Director of Transportation |
| Backup vault (35-day write-once) | Backup service | Backup and recovery account (second region) | Director of Information Technology |
| OT network sensors | Appliances | HQ data center; both NOCs | Cybersecurity Manager |

## 10. Control Implementation Details
### 10.1 Control implementation status
**Baseline and tailoring.** The TDPO uses the NIST SP 800-53B **Moderate** baseline (287 controls and enhancements), tailored as follows:
- **Documented here: 110 controls** in `control-implementation.csv`. They cover every control that maps to a TSA directive requirement in the CIP (SD 1580/82-2022-01E III.A to III.F, SD 1580-21-01E II.B to II.E), plus the Moderate controls that address the risks in P01 (field segmentation, shared OT accounts, vendor access, recovery, logging).
- **Selected by tailoring (added, 5):** CA-8 penetration testing (High baseline only, added because SD III.F.2.c calls for penetration and adversarial testing), and PM-1, PM-2, PM-9, and PM-16 (program management, needed for the Cybersecurity Coordinator and threat information duties).
- **Integrity tailoring:** CM-3, SI-7, and SI-10 statements cover field controller changes, firmware verification, and consist validation before PTC initialization (section 6).
- **Inherited without separate statements:** the remaining Moderate physical and environmental controls for the cloud provider's and SaaS providers' data centers, and platform-level SA and SC controls, evidenced by their SOC 2 Type 2 reports (P09 `vendor-soc2-review.csv`).
- **Deferred:** other Moderate controls with no directive mapping and no Moderate-or-higher risk in P01 (for example SA-11 developer testing and SA-15 development process, because the company does not develop the CAD/CTC or PTC software). Recorded as tailoring decisions and reviewed yearly.
- **CSF 2.0 mapping:** the `csf2_subcategories` column uses the official NIST CSF 2.0 to SP 800-53 Rev. 5.2.0 mapping (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`). For 13 controls the official mapping has no entry (for example AC-11, AU-8, MA-4, MP-3, PS-3); those cells are an **author mapping**. The `regulatory_driver` mapping to directive sections is also an author mapping.

**Status of the 110 documented controls:**
| Status | Count |
|---|---|
| Implemented | 48 |
| Partially implemented | 61 |
| Planned | 1 |
| Not applicable | 0 |

**Inheritance of the 110 documented controls:**
| Inheritance | Count | Main providers |
|---|---|---|
| System-specific | 77 | Company |
| Hybrid | 28 | Identity provider vendor, cloud provider, MSSP, PTC vendor, TMS vendor, CAD/CTC vendor, leased circuit carrier |
| Common/Inherited | 5 | Cloud provider (AU-9 write-once log storage, CP-6 backup region), MSSP and insurer panel (IR-7), PTC vendor and host key management (SC-12, SC-13) |

The Partially implemented statements trace to the 12 known gaps in `../00_company-facts.md` section 4 and to the P07 findings. The one Planned control is SR-2 (supply chain risk management plan), which waits on the vendor risk standard STD-03.

### 10.2 Control assessment status
The co-sourced internal audit firm assessed 34 controls from 2026-08-03 to 2026-08-21 (P07 `assessment-plan.md`, `assessment-results.csv`, and `poam.csv`). Those results also count toward the TSA Cybersecurity Assessment Plan for the current plan year (SD III.F.2.d). Weaknesses are tracked in the POA&M and reported quarterly to the audit committee.

## 11. Digital Identity Acceptance Statement
- **Office and remote users.** Password plus push MFA with number matching through the identity provider for email, VPN, TMS, and cloud. This meets the company's authenticator standard for a Moderate system.
- **Dispatchers.** Consoles use individual directory logins without MFA because a second factor at every console handover would delay safety-critical work. The CIP documents compensating controls under SD III.C.2: consoles only in badge-controlled NOCs, deny-by-default dispatch zones, no internet access, and per-dispatcher logins. The 2 shared logins at the backup NOC break that compensating control and are being removed (P07 POAM-002).
- **Administrators and vendors.** All privileged and vendor access to the TDPO goes through the PAM jump host with phishing-resistant MFA (FIDO2 keys for administrators since 2026-05) and session recording, except the radio and detector vendors (gap 3).
- **Onboard PTC components.** Under SD III.C.6, the company relies on the physical security of the locomotive housings and seals (49 CFR 232.105(h) exterior locks for unattended locomotives outside yards, and 236.3 for housings) instead of logical access controls, as the CIP specifies.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`); BIA (P05); cloud architecture and control map (P04); risk register (P01); gap analysis and roadmap (P03); policies and standards index (P06); assessment and POA&M (P07); incident runbooks (P08); SOC 2 readiness and vendor reviews (P09); AI governance assessment (P10). The CIP, CAP, and CAP annual report are SSI and are held in the restricted SSI library.

## 13. Acronym List and Glossary
- **BOS:** PTC back office server
- **CAD/CTC:** computer-aided dispatch and centralized traffic control office system
- **CAP:** TSA Cybersecurity Assessment Plan
- **CIP:** TSA Cybersecurity Implementation Plan
- **Critical Cyber System:** any IT or OT system or data that, if compromised or exploited, could result in operational disruption (SD 1580/82-2022-01E VII.D)
- **HTUA:** high threat urban area (Appendix A to 49 CFR part 1580)
- **KEV:** CISA Known Exploited Vulnerabilities catalog
- **MSSP:** managed security service provider
- **NOC:** network operations center (dispatch center)
- **PAM:** privileged access management
- **PTC:** positive train control
- **RSSM:** rail security-sensitive materials
- **SSI:** Sensitive Security Information (49 CFR part 1520)
- **TMS:** transportation management system

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-07-31 | Draft from the BIA, risk assessment, and gap analysis | Cybersecurity Manager |
| 1.0 | 2026-09-15 | Updated with P07 results; approved by the Chief Operating Officer | Cybersecurity Manager |
