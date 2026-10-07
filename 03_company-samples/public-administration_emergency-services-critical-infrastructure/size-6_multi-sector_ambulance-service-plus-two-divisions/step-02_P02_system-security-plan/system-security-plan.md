# System Security Plan: Dispatch and Patient Care Platform (DPCP)

**Organization:** Cris Santos Company Holdings, Inc. (shared platform used by the Ambulance Services and Billing and Dispatch Services divisions) | **Tier:** Multi-Sector | **Vertical:** Emergency Services
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-16

> **Why this system.** At this tier the SSP can cover one system per division or a shared corporate system. The group chose the **Dispatch and Patient Care Platform**, a shared platform, because it carries the processes with the shortest downtime limits in the group BIA (P05: BP-BD01 and BP-AM01, MTD 2 hours), it is used by two divisions and 14 external EMS agencies at once, it inherits most of its controls from corporate (SYS-G1 to SYS-G3), and it carries the group's top risks (P01 GR-01 and GR-02). Urgent Care's EHR (SYS-D2) and the BDS revenue cycle platform (SYS-D3) keep their own division plans, which inherit from the same common control catalog.

## 1. System Name and Identifier
Dispatch and Patient Care Platform (**DPCP**), identifier CSCH-DPCP-01. It combines the CAD and communications center components of SYS-D4 and the ePCR and fleet mobile systems of SYS-D1 in `../00_company-facts.md`.

## 2. System Overview
The DPCP takes an emergency call or a transport request and carries it through to a completed patient care record:
- **Call and dispatch (BDS):** 4 regional communications centers with about 1,100 telecommunicators take calls transferred from 21 county PSAPs, requests from about 260 facilities, and calls for 14 external EMS agencies. They run the emergency medical dispatch protocol and assign units in the CAD.
- **Response (Ambulance Services):** about 2,400 ambulances receive incidents on mobile data computers (MDCs), report status and location, and send 12-lead ECGs to hospitals.
- **Patient care record (Ambulance Services):** crews document care in the ePCR on rugged tablets. The ePCR delivers records to receiving hospitals, submits state EMS data, and passes billing data to the BDS revenue cycle platform.

About 21 million incident records (7 years) sit in the CAD database. About 20,000 workforce users, 14 client agencies, and 21 county interfaces use the platform.

**Major components:**
- **CAD application and database:** vendor-licensed CAD servers and a managed database in provider A (in the legacy account, see gap 3)
- **Integration engine:** county CAD-to-CAD, CAD to ePCR, ePCR to revenue cycle, and hospital record delivery
- **Communications center equipment:** dispatch consoles, call handling and recording, and radio console gateways to county P25 systems, with UPS and generators
- **ePCR:** vendor SaaS tenant (business associate with a SOC 2 Type 2 report)
- **Fleet mobile systems:** vehicle routers, MDCs, ePCR tablets, and cardiac monitors with the vendor's 12-lead relay
- **AI call triage module:** CAD vendor cloud service (shadow mode at all centers; advisory at the Florida center; see P10)

The platform is described by service category and is vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies to the DPCP |
|---|---|---|---|
| C-EMERGENCY-R04 | HIPAA Security Rule | 45 CFR Part 164, Subpart C | Ambulance Services is a covered entity; BDS and corporate are business associates. The CAD and ePCR hold ePHI (patient names, chief complaints, care records). Each covered entity remains responsible for its own ePHI |
| N62-R03 | HIPAA Breach Notification Rule | 45 CFR 164.400-414 | BDS and corporate notify Ambulance Services and each external client agency (164.410); Ambulance Services notifies individuals, HHS, and media (P08) |
| N62-R07 | Section 1557 patient care decision support tools | 45 CFR 92.210 | The AI call triage module supports decisions on response priority (P10) |
| C-EMERGENCY-R01 | FBI CJIS Security Policy v6.1 | CJISSECPOL v6.1 | **Under review** for one county feed (gap 5). The platform does not connect to criminal justice databases |
| C-EMERGENCY-R05 | CIRCIA (proposed, not in force) | Proposed 6 CFR 226 | Tracked only. A covered cyber incident in the DPCP would be reportable if the rule is finalized as proposed (P08) |
| State EMS law | EMS records and licensing (Florida worked example) | Fla. Stat. 401.30; Rule 64J-1.014, F.A.C. | Accurate call and patient care records; record available to the receiving hospital within 48 hours; 5-year retention. Each state's rules are checked the same way |
| Medicare | Ambulance documentation | 42 CFR 410.40(e), 410.41(c), 424.516(f) | ePCR records support claims and must be kept 7 years |
| State recording law | Call recording (Florida worked example) | Fla. Stat. 934.03(2)(g) | Recording of incoming calls by a licensed ambulance service's employees; counsel confirms line coverage (P10) |
| SEC | Cybersecurity disclosure | Reg S-K Item 106; Form 8-K Item 1.05 | A DPCP incident may be material to the group (P08) |
| Contracts | County ambulance agreements; client dispatch contracts and BAAs | 45 CFR 164.504(e) for BAAs | Outage notice within minutes, response-time standards, and breach notice terms (P08) |
| Internal | Group policies POL-01 to POL-05 and division supplements | P06 | |

Not applicable: 42 CFR Part 2 (no Part 2 program); FTC Health Breach Notification Rule (data held by or for covered entities); FCC EAS rules (not an EAS participant).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Group CISO and the group dispatch and clinical platforms director (system owner) on 2026-09-16, after the board risk committee review.

### 4.2 System Authorization Decision
The group is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- **Decision:** authorized to operate with conditions, 2026-09-16, by the Group CISO and the Group Chief Risk Officer (acceptance authority for High risks).
- **Conditions:** (1) move the CAD out of the legacy account into the landing zone and remove the shared management subnet by 2027-01-31 (POAM-012); (2) remove the CAD vendor's standing accounts and route vendor access through PAM by 2026-11-30 (POAM-003); (3) build and test a CAD standby in provider B by 2027-06-30 (POAM-013); (4) no AI triage advisory mode outside the Florida center until the Group AI council's conditions are met (P10).
- **Reauthorization:** annually, or when the CAD moves to the landing zone.

### 4.3 System Operational Status
Operational. **Major modifications planned:** CAD migration to the landing zone (2027-01-31) and a provider B standby (2027-06-30).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Group dispatch and clinical platforms director | Accountable for the DPCP and this SSP |
| Authorizing official equivalent | Group CISO with the Group Chief Risk Officer | Authorization decision; High risk acceptance |
| Operational owner, communications centers | BDS vice president of communications operations | Centers, telecommunicators, manual dispatch |
| Operational owner, field systems | Ambulance Services fleet technology director | Vehicle routers, MDCs, tablets, cardiac monitors |
| Clinical owner | Ambulance Services chief medical officer | Dispatch protocols, ePCR content, AI triage clinical validity |
| Data owners | Ambulance Services Privacy Officer (patient data); BDS security and compliance lead (client agency partitions) | Approve access and data flows |
| Common control providers | Group identity director (SYS-G1), Group SOC director (SYS-G2), Group cloud platform director (SYS-G3) | Operate inherited controls (common-control-catalog.csv) |
| Independent assessor | Group internal audit | Assesses common controls once and samples division controls (P07) |

Ambulance Services keeps its own HIPAA Security Officer and Privacy Officer, and BDS names its own security and privacy officials as a business associate.

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Emergency response (incidents, unit status, vehicle location, CAD-to-CAD data) | Moderate | **High** | **High** | A wrong address or unit status sends the wrong ambulance or none; a CAD outage delays emergency response (P05 BP-BD01, MTD 2 hours) |
| Health care delivery services (chief complaints in CAD; ePCR care records; 12-lead ECGs) | **High** | High | Moderate | Raised to High for aggregation: about 21 million incident records and the ePCR records of 3.1 million responses a year. A disclosure would mean notices in 7 states and for 14 client agencies, plus an SEC materiality decision |
| Information security (keys, accounts, logs) | High | High | Moderate | Compromise would expose every center and agency partition |
| **DPCP category (high-water mark)** | **High** | **High** | **High** | Overall **High** |

**Baseline:** the NIST SP 800-53B **High** baseline, tailored. The plan documents **121 controls** in `control-implementation.csv`:
- 117 from the High baseline;
- 2 from the privacy baseline (PM-9, PM-10);
- 2 program management controls not in any baseline (PM-1, PM-2).

Other High-baseline controls are fully inherited from the cloud and SaaS providers (for example, most PE controls for data centers, evidenced by their SOC 2 Type 2 reports) or tailored out with a reason in the group tailoring register.

## 7. Authorization Boundary Description
- **Inside:** the CAD servers and database and the integration engine (provider A, legacy account), the 4 communications centers' consoles, call handling, recording, and radio console gateways, the ePCR tenant, and the fleet mobile systems in about 2,400 ambulances.
- **Outside, inherited (common control providers):** SYS-G1 identity platform, SYS-G2 SOC, SIEM, and EDR, SYS-G3 landing zone, keys, log archive, and the provider B backup vault.
- **Outside, interconnected:** 21 county PSAP CAD systems, county P25 radio systems, 14 client agency users, receiving hospitals, state EMS data systems, the BDS revenue cycle platform (SYS-D3), and the CAD vendor's AI triage service.

The diagram is in P04 `cloud-architecture.md` (section 2.2).

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| 21 county PSAP CADs | Inbound | Incident type, address, callback number, notes. **One feed carried premise notes from a sheriff's records system** until 2026-08-20 (gap 5) | County interface agreements |
| County P25 radio systems | Both | Voice; unit status by radio | County radio use agreements |
| 14 external client agencies | Both | Their incidents and unit status in their CAD partition | Dispatch contracts and BAAs |
| Receiving hospitals | Outbound | ePCR records; 12-lead ECGs (via the monitor vendor relay) | ePCR vendor service; treatment disclosures |
| State EMS data systems | Outbound | Incident-level EMS data (Florida: EMSTARS format) | State reporting rules |
| SYS-D3 revenue cycle platform | Outbound | Trip and patient care data for claims | Intercompany BAA; file transfer through the shared management subnet today (gap 3) |
| CAD vendor AI triage service | Outbound audio; inbound suggestions | Live call audio, transcripts, suggested call type and priority | CAD vendor BAA amended 2026-04-30 (internal divisions only, gap 6) |
| CAD vendor remote support | Inbound | Administrative access | Persistent VPN and local accounts (gap 2) |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| CAD application servers and managed database | IaaS virtual machines; PaaS database | Provider A, legacy account | Group dispatch and clinical platforms director |
| Integration engine | IaaS | Provider A, legacy account | Group dispatch and clinical platforms director |
| Client agency portal | PaaS web front end | Provider A landing zone | Group dispatch and clinical platforms director |
| Dispatch consoles (about 520 positions), call handling and recording | On-premises | 4 communications centers | BDS vice president of communications operations |
| Radio console gateways | On-premises appliances | 4 communications centers | BDS vice president of communications operations |
| ePCR tenant | SaaS | ePCR vendor | Ambulance Services clinical quality director |
| Vehicle routers, MDCs, ePCR tablets, cardiac monitors | Mobile devices | About 2,400 ambulances | Ambulance Services fleet technology director |
| AI call triage module | SaaS | CAD vendor cloud | BDS vice president of communications operations |
| Backups (hourly CAD database copies; nightly server images) | Backup service with immutability | Provider B vault | Group cloud platform director |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv` (121 controls) and `common-control-catalog.csv` (95 group common and hybrid controls).

| Status | Controls |
|---|---|
| Implemented | 95 |
| Partially implemented | 26 |
| Planned | 0 |
| Not applicable | 0 |
| **Total** | **121** |

| Inheritance | Controls |
|---|---|
| Common/Inherited (from SYS-G1, SYS-G2, SYS-G3, group functions, or the cloud providers) | 74 |
| Hybrid (group provides the mechanism; the platform configures or operates part) | 21 |
| System-specific | 26 |

**The 26 partially implemented controls** cluster in six places:
- **CAD resilience** (scenario gap 1): CP-2, CP-4, CP-7, CP-10.
- **CAD vendor and vehicle identity** (gap 2): AC-2, AC-6(5), AC-17, IA-2, IA-5.
- **Legacy account and segmentation** (gap 3): AC-4, SC-7, SI-4.
- **Fleet devices outside group management** (gap 4): AC-19, AU-6, CM-2, CM-6, CM-8, IA-3, RA-5, SI-2, SR-6.
- **Data received and shared** (gaps 5 and 6): AC-21, SA-9.
- **Multi-party notification** (gap 7): IR-3, IR-6, IR-8.

### 10.2 Common control inheritance by division
The common control catalog lists 95 controls that corporate provides fully (74) or as the mechanism for a hybrid control (21). Inheritance is **documented** for BDS (its SOC 2 system description carves in the group services), for Urgent Care (2025 inheritance matrix, except the 46 acquired clinics), and for the DPCP (this plan). For Ambulance Services it is **partly documented**: the 2025 matrix covers office systems and the ePCR but leaves out the fleet mobile systems, which the fleet technology team runs outside group configuration management (gap 4; POAM-008).

### 10.3 Control assessment status
Common controls were assessed once, and platform and division controls sampled, from 2026-07-06 to 2026-08-28 by group internal audit. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
- **Workforce users** (telecommunicators, supervisors, crews on the ePCR, administrators) authenticate through SYS-G1 with MFA; dispatch consoles use badge plus PIN, because a phone prompt on a live dispatch floor is not practical. Administrators use phishing-resistant keys and just-in-time PAM.
- **Vehicles** sign in to the CAD with one shared account per vehicle. This does not meet the plan's assurance target, because MDC actions cannot be tied to a person. Crew sign-in on the MDC through SYS-G1 is planned (POAM-002).
- **Client agency users** federate from their own identity providers or use SYS-G1 guest accounts with MFA.
- **No patients or callers** access the DPCP directly.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), group and division risk registers (P01), gap analyses and regulation-by-division matrix (P03), cloud architecture and control map (P04), BIA (P05), group policies and division supplements (P06), assessment and POA&M (P07), incident response runbook and notification matrix (P08), SOC 2 readiness (P09), AI governance (P10).

## 13. Acronym List and Glossary
- **AVL:** automatic vehicle location
- **BAA:** business associate agreement
- **CAD:** computer-aided dispatch
- **CAD-to-CAD:** an interface that passes incidents between two dispatch systems
- **Common control:** a control provided once by corporate and inherited by several systems
- **DPCP:** Dispatch and Patient Care Platform
- **ePCR:** electronic patient care report
- **MDC:** mobile data computer
- **PAM:** privileged access management
- **PSAP:** public safety answering point
- **SIEM:** security information and event management

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-08-28 | Draft after P07 fieldwork | Group dispatch and clinical platforms director |
| 1.0 | 2026-09-16 | Approved with authorization conditions | Group CISO |
