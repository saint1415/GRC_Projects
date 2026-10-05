# System Security Plan: Train Dispatching and PTC Back Office Platform (TDPB)

**Organization:** Cris Santos Company Holdings, Inc., Freight Railroad division (72 railroads), inheriting group common controls from corporate shared services | **Tier:** Multi-Sector | **Vertical:** Transportation Systems
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-10

> **Why this system.** At this tier the SSP can cover one system per division or a shared corporate system. The group chose the Freight Railroad division's **Train Dispatching and PTC Back Office Platform**, the registry default, because it is the system every train movement depends on, it holds the Critical Cyber Systems named in the TSA-approved Cybersecurity Implementation Plan (CIP), and it inherits most of its IT controls from corporate (SYS-G1 to SYS-G3). The group common control catalog (`common-control-catalog.csv`) is written for every division, so the Transload and Wholesale and Real Estate division plans can inherit from the same list once their inheritance is documented (scenario gap 10).

## 1. System Name and Identifier
Train Dispatching and PTC Back Office Platform (**TDPB**), identifier CSCH-RR-TDPB. Made up of SYS-R1, SYS-R2, and the CTC office code servers from SYS-R3 in `../00_company-facts.md`.

## 2. System Overview
TDPB issues and records movement authority for the group's 72 railroads and for 11 unaffiliated short lines that buy the contract dispatching and car management service (CDS). It runs the office segment of the PTC system for the 4 railroads that host passenger trains (CR-11 to CR-14) and the back office for the 330 group locomotives with onboard PTC apparatus.

About 640 workforce users (dispatchers, chief dispatchers, PTC administrators, OT engineers, and vendor engineers) use it, from 156 consoles at the primary NOC in Jacksonville, Florida and the backup NOC.

**Major components:**
- **CAD cluster:** track warrant and track and time authority with conflict checking, CTC dispatcher displays, train sheets, bulletins, and speed restrictions. Primary cluster in DC-1, hot standby in DC-2 with real-time replication
- **PTC back office:** PTC server segment for the host railroads (subdivision data, authorities, bulletins, interoperable messaging with Amtrak, the commuter operator, and Class I back offices) and onboard unit management for tenant runs. Primary in DC-1, standby in DC-2
- **PTC key management enclave:** generation, distribution, and revocation of the keys that give PTC messages cryptographic integrity and authentication
- **CTC office code servers:** send dispatcher route and signal requests to field code units over the code line (the vital logic stays in the field)
- **Dispatch consoles:** 156 consoles on the NOC operations network
- **Industrial DMZ:** PAM jump hosts, the TMS interface server, the crew system interface, patch and antivirus relays, and the historian replica

The platform is on premises because of latency and availability needs; supporting services (identity, SIEM, backups) are corporate common controls (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies to TDPB |
|---|---|---|---|
| C-TRANSPORTATION-R01 | TSA rail cybersecurity directives | SD 1580-21-01E; SD 1580/82-2022-01E | TDPB holds Critical Cyber Systems of CR-01 to CR-14, named in the TSA-approved CIP (approved 2023-07-26). PTC systems must be Critical Cyber Systems for railroads required to operate PTC (SD 1580/82-2022-01E III.A.2.a). Segmentation, access control, monitoring, and patching measures (III.B to III.E) and the assessment plan (III.F) apply; incident reports go to CISA (SD 1580-21-01E II.C) |
| C-TRANSPORTATION-S01 | TSA Security Coordinator and significant security concern reports | 49 CFR 1570.201, 1570.203 | A cyber attack on TDPB is a reportable event for every railroad it dispatches ("Cyber Attack", Appendix A to part 1570), within 24 hours |
| C-TRANSPORTATION-S03 | SSI | 49 CFR 1520.5, 1520.9 | The CIP, the CAP and its results, and reports to TSA and CISA are SSI (SD 1580/82-2022-01E IV.B) |
| C-TRANSPORTATION-S04 | FRA PTC | 49 CFR 236.1005, 236.1023, 236.1029, 236.1033 | Host duties for CR-11 to CR-14 (certified PTC system); cryptographic message integrity and key protection (236.1033(a) to (d)); service restoration and mitigation plan (236.1033(f)); vendor and configuration controls (236.1023) |
| C-TRANSPORTATION-S02 | RSSM location | 49 CFR 1580.203 | TDPB does not hold the RSSM data (the TMS does), but NOC staff on TDPB answer TSA requests within 30 minutes |
| C-TRANSPORTATION-S10 | SEC disclosure | Form 8-K Item 1.05; 17 CFR 229.106 | A TDPB incident may be material to the group (P08) |
| Contracts | CDS service agreements with 11 short lines | Contract | 99.9% availability, 4-hour recovery, incident notice within 24 hours; SOC 2 report requested (P09) |
| Internal | Group policies POL-01 to POL-05 and the Freight Railroad supplement | P06 | |

Not applicable: maritime, pipeline, and aviation rules; DFARS and CMMC; the FTC Act does not reach the railroads' common carrier activity (15 U.S.C. 45(a)(2) and 44), and group policy applies the same controls anyway.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Chief Operating Officer, Freight Railroad (authorizing official), the Director, Network Operations Center (system owner), and the Group CISO on 2026-09-10, after the board safety, security, and risk committee review.

### 4.2 System Authorization Decision
The group is not a federal agency, so there is no federal authorization. Two decisions apply:
- **External:** TSA approved the CIP on 2023-07-26. The CIP sets the measures TSA inspects against (SD 1580/82-2022-01E II.B.2).
- **Internal:** authorized to operate with conditions, 2026-09-10, by the Chief Operating Officer, Freight Railroad, with the Group CISO and the Group Chief Risk Officer (acceptance authority for High risks). Conditions: (1) file a CIP amendment request describing the SYS-G5 dependency and its flows by 2026-11-30 (SD VI.B.2 and VI.D; POAM-001); (2) document compensating measures and a timeline for unpatched PTC back office servers by 2026-10-31 (SD III.E.3; POAM-004); (3) meet the 4-hour PTC back office RTO in a retest by 2027-03-31 (POAM-005).
- **Reauthorization:** annually with the CAP update, or when the CIP is amended.

### 4.3 System Operational Status
Operational. **Planned changes:** PTC back office standby rebuild to match production (2027-Q1); OT log forwarding for CTC code servers and the PTC back office (2026-Q4); retirement of the CTC shared administrator accounts (2026-Q4).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Director, Network Operations Center | Accountable for TDPB and this SSP |
| Authorizing official equivalent | Chief Operating Officer, Freight Railroad, with the Group CISO and the Group Chief Risk Officer | Authorization decision; High risk acceptance |
| OT security lead | Director, Rail OT Security | Designs and operates system-specific controls; alternate TSA Cybersecurity Coordinator |
| PTC lead | PTC Program Director | PTC back office, PTCSP duties, key management, vendor coordination |
| TSA Cybersecurity Coordinator | Group CISO (primary); Director, Rail OT Security and Group SOC Director (alternates) | CISA and TSA contact for CR-01 to CR-14, available 24/7 (SD 1580-21-01E II.B) |
| TSA Security Coordinator | Vice President, Rail Security (primary); Director, NOC (alternate) | 1570.201 and 1570.203 for all 72 railroads |
| Common control providers | Group identity director (SYS-G1), Group SOC Director (SYS-G2), Group CIO (SYS-G3), Group HR director, Group Chief Risk Officer | Operate inherited controls (`common-control-catalog.csv`) |
| Independent assessor | Group internal audit with co-sourced OT specialists | Assesses common controls once and samples division controls (P07); the results feed the TSA CAP annual report |

## 6. System Information Types and System Categorization
Information types were chosen with NIST SP 800-60 Vol. 2 Rev. 1 as a guide (ground transportation, information security, and system and network monitoring). The impact levels below are the group's own FIPS 199 determinations for this system, not provisional values.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Movement authority and train control data (warrants, track and time, CTC routes, bulletins, PTC authorities) | Moderate | **High** | **High** | A wrong or missing authority could put two trains or a train and a work crew on the same track; loss stops 83 railroads within minutes (P05 BP-R01 MTD 4 hours) |
| PTC configuration and cryptographic keys | **High** | **High** | **High** | Key compromise would undermine message authentication for host territory (49 CFR 236.1033) |
| Security and architecture information (CIP, network diagrams, CAP results) | Moderate | Moderate | Low | SSI; disclosure could help an attacker |
| System and network monitoring data | Moderate | Moderate | Moderate | Needed to investigate incidents and report to CISA |
| **TDPB category (high-water mark)** | **High** | **High** | **High** | Overall **High** |

**Baseline:** the NIST SP 800-53B **High** baseline, tailored. The plan documents **187 controls** in `control-implementation.csv`: 181 from the High baseline and 6 program management controls that are in no baseline (PM-1, PM-2, PM-5, PM-9, PM-11, PM-16). Other High-baseline controls are tailored out with a reason in the group tailoring register (for example, PT controls, because TDPB processes no personal information beyond workforce account data, and controls for public-facing services, because TDPB has none).

**CSF 2.0 mapping:** the `csf2_subcategories` column uses the official NIST CSF 2.0 to SP 800-53 Rev. 5.2.0 mapping in `00_universal-framework/crosswalks/`, with enhancements mapped through their base control. For 22 controls with no entry in that mapping (for example AC-8, PS-3, SC-23), the column carries an author mapping.

## 7. Authorization Boundary Description
- **Inside:** the CAD cluster (DC-1 and DC-2), the PTC back office (DC-1 and DC-2), the PTC key management enclave, the CTC office code servers, the NOC operations network zone, the industrial DMZ components listed in section 2, and the 156 dispatch consoles.
- **Outside, inherited (common control providers):** SYS-G1 identity platform and the rail OT directory, SYS-G2 SOC, SIEM, and EDR, SYS-G3 data center facilities, network, and the backup vault in provider B.
- **Outside, interconnected:** SYS-R3 field equipment (code units, wayside interface units, radio), onboard PTC apparatus, SYS-R4 TMS, SYS-R5 crew system, SYS-G5 integration platform (through the TMS interface server), Class I railroad, Amtrak, and commuter operator back offices through the interoperable messaging network, and the CDS customers' viewer accounts.

The diagram is in P04 `cloud-architecture.md` (section 2.2).

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| SYS-R4 TMS (cloud provider A) | Inbound and outbound through the DMZ interface server | Train consists for PTC initialization; car lists; train sheets | Internal; documented in the CIP flow list |
| SYS-G5 integration platform | Inbound to the TMS interface server | Car placement and car order updates from the terminals | **Not in the CIP flow list and no interconnection record** (gap 1; POAM-001) |
| SYS-R5 crew system | Inbound | Crew assignments for train sheets | Internal; in the CIP |
| Class I, Amtrak, and commuter operator PTC back offices | Bidirectional through the interoperable messaging network | PTC messages with cryptographic integrity and authentication | Interoperability and operating agreements |
| SYS-R3 field equipment | Bidirectional over the code line and radio network | CTC requests and indications; PTC wayside messages | Internal |
| CDS customers | Viewer access through external identity with MFA | Their own train sheets and authorities | CDS service agreements |
| CAD and PTC vendors | Remote support through PAM jump hosts | Maintenance sessions | Contracts with security terms |

## 9. System Component Inventory
| Component | Type | Location | Owner |
|---|---|---|---|
| CAD application and database cluster | Servers (virtualized) | DC-1; hot standby DC-2 | Director, Rail OT Security |
| PTC back office servers | Servers | DC-1; standby DC-2 (configuration drift found in the DR test) | PTC Program Director |
| PTC key management enclave | Hardware security modules and servers | DC-1 and DC-2 | PTC Program Director |
| CTC office code servers | Servers | Both NOCs | Chief Engineer, Signals and Communications |
| Dispatch consoles (156) | Workstations | Primary and backup NOCs | Director, NOC |
| Industrial DMZ services | Jump hosts, interface servers, relays | DC-1 and DC-2 | Director, Rail OT Security |
| NOC operations network | Switches and firewalls | Both NOCs and data centers | Group CIO (equipment); Director, Rail OT Security (rules) |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv` (187 controls) and `common-control-catalog.csv` (134 group common controls).

| Status | Controls |
|---|---|
| Implemented | 166 |
| Partially implemented | 21 |
| Planned | 0 |
| Not applicable | 0 |
| **Total** | **187** |

| Inheritance | Controls |
|---|---|
| Common/Inherited (from SYS-G1, SYS-G2, SYS-G3, or group functions) | 105 |
| Hybrid (group provides the mechanism; TDPB configures or operates part) | 29 |
| System-specific | 53 |

**The 21 partially implemented controls** cluster in four places:
- **The shared integration platform and the CIP** (gap 1): AC-4, CA-3, CM-8, PL-2, PM-5.
- **PTC back office patching and recovery** (gap 2): SI-2, SA-9, CP-4, CP-7, CP-10.
- **OT access and logging** (gaps 3 and 4): AC-2, AC-2(12), AC-6, IA-5, AU-6, AU-11, AU-12, SI-4.
- **Group-level response and SSI handling** (gaps 8 and 12): IR-3, IR-6, AC-21.

### 10.2 Common control inheritance by division
The common control catalog lists 134 controls provided by corporate (19 of them assessed in P07 this year). Inheritance is **documented for the Freight Railroad division** (the CIP inheritance annex, 2025) and for TDPB (this plan). It is **not documented for Transload and Wholesale or Real Estate** (scenario gap 10). Until POAM-016 closes, those divisions cannot show which of their FAR 52.204-21 safeguards, terminal OT controls, or building controls are met by group controls, and P07 found CA-2 statements other than satisfied for this reason.

### 10.3 Control assessment status
Common controls were assessed once, and TDPB and division controls sampled, from 2026-07-06 to 2026-08-28 by group internal audit. The assessment covered the one-third of CIP measures due in 2026 under the CAP schedule (SD 1580/82-2022-01E III.F.2.d). See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
- **Administrators and vendors** authenticate through PAM with phishing-resistant MFA and session recording.
- **Dispatchers** authenticate to consoles with named rail OT directory accounts without MFA. The CIP documents the compensating controls TSA accepted with the plan (SD 1580/82-2022-01E III.C.2): badge-controlled NOC floor, consoles with no remote access, application allowlisting, and session lock at relief.
- **CDS customer users** authenticate through external identities with MFA and see only their own territory.
- **Onboard and wayside PTC devices** authenticate with device certificates; onboard housings are locked and sealed, the physical alternative SD 1580/82-2022-01E III.C.6 allows for locomotive PTC components.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud architecture and control map (P04), group and division risk registers (P01), gap analyses and regulation-by-division matrix (P03), group policies and division supplements (P06), assessment and POA&M (P07), incident response runbook and notification matrix (P08), SOC 2 readiness for the CDS (P09), AI governance (P10). The CIP and CAP are SSI and are referenced, not reproduced.

## 13. Acronym List and Glossary
- **CAD:** computer-aided dispatch
- **CAP:** Cybersecurity Assessment Plan (SD 1580/82-2022-01E III.F)
- **CDS:** contract dispatching and car management service
- **CIP:** Cybersecurity Implementation Plan (SD 1580/82-2022-01E II.B)
- **Critical Cyber System:** an IT or OT system or data that, if compromised or exploited, could result in operational disruption (SD 1580/82-2022-01E VII.D)
- **CTC:** centralized traffic control
- **Industrial DMZ:** the zone between the corporate network and the NOC operations zone
- **PTC:** positive train control
- **PTCSP:** PTC Safety Plan
- **SSI:** Sensitive Security Information (49 CFR part 1520)

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-08-28 | Draft after P07 fieldwork | Director, Network Operations Center |
| 1.0 | 2026-09-10 | Approved with authorization conditions | Chief Operating Officer, Freight Railroad |
