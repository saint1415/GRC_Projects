# System Security Plan: Dispatch and Patient Care Platform (DPCP)

**Organization:** Cris Santos Company, Inc. (licensed private ambulance service; PE-backed) | **Tier:** Mid-Market | **Vertical:** Emergency Services
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-16

## 1. System Name and Identifier
Dispatch and Patient Care Platform (**DPCP**), identifier CSC-DPCP-01. The DPCP is the company's major system. It comprises SYS-01, SYS-02, SYS-04, SYS-06, SYS-07, SYS-08, SYS-09, SYS-10, SYS-11, and SYS-12 in `../00_company-facts.md`.

## 2. System Overview
The DPCP supports every step of an ambulance response for about 730,000 residents in two counties' 911 service areas and for interfacility work in three counties: call intake and emergency medical dispatch, unit recommendation and tracking, station alerting, patient care documentation, hospital record delivery, and the hand-off of trip data to billing. It serves 600 workforce members, two communications centers, 13 stations, 92 ambulances, and 14 support vehicles, and handles about 410 transports a day.

**Major components:**
| ID | Component | Hosting and service model |
|---|---|---|
| SYS-01 | Computer-aided dispatch (CAD): 2 application servers (active and standby), managed database, AVL gateway, posting module, CAD-to-CAD interfaces | Vendor-licensed software run by the company in the dispatch production account (IaaS and PaaS) |
| SYS-02 | Electronic patient care reporting (ePCR) with hospital delivery and state export | Vendor SaaS; vendor SOC 2 Type 2 |
| SYS-04 | Identity provider with SSO, MFA, and conditional access | SaaS |
| SYS-06 | Cloud landing zone: identity and security, shared services, dispatch production, data and reporting, and backup accounts | Public cloud IaaS and PaaS, vendor-agnostic (P04) |
| SYS-07 | Primary communications center (18 positions) and backup center at Station 10 (6 positions) | On-premises |
| SYS-08 | Hosted phone system with call recording | Vendor SaaS; business associate |
| SYS-09 | Fleet mobile systems: 106 routers, 92 MDCs, 210 rugged tablets, 92 cardiac monitors | In vehicles |
| SYS-10 | Networks at 14 sites on SD-WAN, including station alerting controllers | On-premises; SD-WAN managed service |
| SYS-11 | 340 workstations and laptops (24 consoles), 210 tablets, 92 MDCs | Company-managed |
| SYS-12 | SIEM operated by the MSSP (a business associate) | SaaS |

The billing platform (SYS-03), the AI tools AI-001 (call triage) and AI-004 (posting model), the county CADs, hospitals, and the state EMS data system connect to the DPCP as external services (section 8).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it affects the DPCP |
|---|---|---|---|
| C-EMERGENCY-R04 | HIPAA Security Rule | 45 CFR Part 164, Subpart C | Primary control requirement. The company is a covered entity (45 CFR 160.103), and also a business associate for its billing services clients. Mapped in `control-implementation.csv` |
| Related | HIPAA Breach Notification Rule | 45 CFR 164.400-164.414 | Logging and investigation must support breach determinations, including the company's notices to its billing clients as a business associate (P08) |
| C-EMERGENCY-R05 | CIRCIA (proposed, not in force) | Proposed 6 CFR 226 (89 FR 23644) | Tracked only. If finalized as proposed, the company would be covered (it exceeds the SBA size standard, and proposed 226.2(b)(5) also reaches EMS providers serving 50,000 or more people) |
| Related | HIPAA Security Rule NPRM (proposed, not in force) | 90 FR 898 (2025-01-06) | Tracked in P03 only |
| Medicare | Ambulance coverage and documentation | 42 CFR 410.40(e); 410.41(c); 424.516(f) | Trip data and certification statements flow from the DPCP to billing; documentation kept 7 years |
| State | EMS records and patient care records | Fla. Stat. 401.30; Rule 64J-1.014, F.A.C. | Accurate call records; patient care record to the receiving hospital on request within 48 hours of dispatch; 5-year retention; state data reporting |
| State | Call recording by a licensed ambulance service | Fla. Stat. 934.03(2)(g) | Recording of incoming calls in the communications centers (P10 for AI-001) |
| State | Florida Information Protection Act | Fla. Stat. 501.171 | Breach notification; as a third-party agent for billing clients, notice to the client within 10 days (P08) |
| Federal | Section 1557 patient care decision support tools | 45 CFR 92.210 | Relevant to AI-001 call triage (P10) |
| Contract | County A ambulance service agreement and County B zone agreement | Contracts | Response-time standards, communications center continuity plan, outage and security incident notices, CAD-to-CAD interfaces |
| Internal | Security policies POL-01 to POL-05 and supporting standards | P06 | Policy basis for every control |

Not applicable:
- **FBI CJIS Security Policy (C-EMERGENCY-R01) and 28 CFR 20.21 and Part 23 (C-EMERGENCY-R02, R03).** The DPCP does not store, process, or view criminal justice information. Both CAD-to-CAD feeds carry EMS incident data only. County A's 2026 proposal to add premise hazard and officer-safety flags is tracked as a trigger (P03 section 1; P01 R-037).
- **FCC EAS rules (C-EMERGENCY-R06).** The company is not an EAS participant and does not originate public alerts.
- **42 CFR Part 2.** The company runs no federally assisted substance use disorder program.
- **HIPAA group health plan requirements (164.314(b)).** The employee health plan is fully insured, and the company receives only summary health and enrollment information (P03).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Chief Operating Officer (system owner) on 2026-09-16, after the control assessment (P07), and presented to the audit committee the same day.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization to operate. The equivalent internal decision:
- **Decision:** operation of the DPCP accepted with conditions, 2026-09-16.
- **Authorizing official equivalent:** Chief Executive Officer for High and Very High risks; Chief Operating Officer for Moderate and below (P01 acceptance authorities).
- **Conditions:** the High-risk POA&M items in P07 must meet their milestones; the ransomware manual dispatch drill at both centers must be held by 2026-11-30; the audit committee receives POA&M status each quarter; re-decision by 2027-09-30 or after a major change (for example the warm CAD standby or AI-001 expansion).
### 4.3 System Operational Status
Operational. Major modifications planned:
- Write-once backups for the integration engine and recording archive, and a CAD rebuild test (due 2026-12-31)
- Segmentation of crew Wi-Fi and station alerting at 9 stations (due 2027-03-31)
- Named, MFA-protected CAD sign-in on MDCs (due 2027-03-31)
- Warm CAD standby in the backup region (due 2027-06-30)

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Chief Operating Officer | Accountable for the DPCP; accepts Moderate risk; executive sponsor of the security program |
| Authorizing official equivalent (High risk) | Chief Executive Officer | Accepts High risk; approves the risk appetite |
| Oversight | Board audit committee | Quarterly cyber risk reporting |
| Program strategy | vCISO (part-time contractor) | Program strategy, board reporting, SSP review |
| Security Officer | Director of IT | HIPAA Security Officer (45 CFR 164.308(a)(2)); day-to-day control owner; cloud landing zone |
| Security operations and GRC | Security Manager and 2 security analysts | Vulnerability management, MSSP oversight, GRC |
| Privacy Officer | Compliance and Privacy Officer | Privacy Rule, breach determinations, BAAs in both directions |
| Dispatch operations | Director of Communications | CAD use, manual dispatch mode, both centers, CAD access approvals |
| Field systems | Director of Field Operations | Fleet mobile systems, station alerting, station facilities |
| Clinical oversight | Medical Director | Dispatch and patient care protocols; AI-001 clinical validation |
| Independent assessment | Co-sourced internal audit firm | Annual IT audit; P07 assessment |
| Monitoring | MSSP (business associate) | 24x7 EDR and SIEM monitoring |

## 6. System Information Types and System Categorization
Information types come from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Emergency response (call, dispatch, and unit data) | Moderate | Moderate | **High** | A CAD outage during an emergency can delay an ambulance, which can contribute to loss of life. Manual dispatch reduces that harm but cannot remove it at about 410 calls a day across two counties (P05 MTD 2 hours) |
| Health care delivery services (patient care records, ePHI) | Moderate | Moderate | Moderate | Disclosure of records for up to about 150,000 patients a year triggers breach duties and is serious but not catastrophic; wrong data could affect hospital care; paper records cover short outages (P05 MTD 24 hours) |
| Health care administration (trip data to billing, certification statements) | Moderate | Moderate | Low | Financial and identity data; payers accept late claims (P05 MTD 72 hours) |
| Human resources management (workforce identities) | Moderate | Low | Low | Account data; limited harm if unavailable |
| System and network monitoring (security logs) | Moderate | Moderate | Low | Needed for breach investigations |
| **DPCP category (high-water mark)** | **Moderate** | **Moderate** | **High** | Overall: **High** |

**Why availability is High while the baseline is Moderate.** Only availability reaches High, and only for the emergency response information type. Confidentiality and integrity are Moderate. The company therefore starts from the NIST SP 800-53B **Moderate** baseline and adds the High-baseline contingency enhancements that serve availability (section 10.1), rather than adopting the full High baseline. This follows the tailoring guidance in SP 800-53B and matches the BIA. **Integrity was considered for High** because altered unit times or addresses could misdirect a crew. It stays at Moderate because CAD time stamps can be changed only by supervisors with a logged reason, addresses are verified by voice with the caller, and the ePCR locks records after signature (SI-7). P01 R-029 and R-049 track the residual risk.

## 7. Authorization Boundary Description
**Inside the boundary:**
- the CAD application servers, database, AVL gateway, integration engine, and call recording archive in the dispatch production account;
- the identity and security, shared services, data and reporting, and backup accounts of the landing zone;
- the ePCR tenant configuration and user roles;
- the identity provider tenant;
- both communications centers;
- networks at 14 sites, including station alerting controllers;
- 340 workstations and laptops, 210 rugged tablets, 92 MDCs, 106 vehicle routers, and 92 cardiac monitors;
- the company's SIEM tenant and its use cases.

**Outside the boundary (external services, interconnected):**
- the ePCR vendor's platform;
- the cloud provider's infrastructure;
- the MSSP's platform;
- the billing platform and clearinghouse (SYS-03), which have their own scope in P09;
- the hosted phone system's platform;
- the AI services behind AI-001;
- the cardiac monitor relay;
- the County A and County B CADs and P25 radio systems;
- receiving hospitals and the state EMS data system.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| County A CAD (sheriff's office PSAP) | Inbound incidents; outbound unit status and times | Incident type, address, callback number, notes, unit times | County A agreement. **No interconnection security terms (gap, CA-3)** |
| County B CAD (consolidated communications center) | Inbound incidents for 2 zones; outbound unit status | Same as above | County B zone agreement. **No interconnection security terms (gap, CA-3)** |
| Billing platform and clearinghouse (SYS-03) | Outbound trip data from the ePCR through the integration engine | Demographics, service level, mileage, certification statements | BAA; contract |
| Receiving hospitals | Outbound | Patient care records through the ePCR hospital portal; 12-lead ECGs through the monitor relay | Treatment disclosures; portal terms; relay BAA |
| State EMS data system (EMSTARS) | Outbound | Incident-level ePCR data in the state format | Rule 64J-1.014, F.A.C. |
| Hosted phone system (SYS-08) | Bidirectional | Calls and recordings | BAA |
| AI call triage service (AI-001) | Outbound live audio; inbound upgrade prompts | Call audio, transcripts, suggested call type and priority | CAD vendor BAA; **AI amendment pending (gap, P10)** |
| MSSP | Inbound logs; remote containment actions | Security logs (may include PHI fragments) | BAA; SOC 2 Type 2 |
| CAD vendor support | Remote administration | Full CAD access | BAA; **no session approval or recording (gap, MA-4)** |
| Station alerting vendor | Remote support to controllers | Alert configuration | Service contract; **remote access unmanaged (gap, MA-4)** |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| CAD application servers (2) and AVL gateway | Cloud virtual machines | Dispatch production account | Director of IT |
| CAD database | Managed database (PaaS) | Dispatch production account | Director of IT |
| Integration engine | Cloud virtual machine | Dispatch production account | Director of IT |
| Call recording archive | Object storage | Dispatch production account | Director of Communications |
| Reporting database and posting model (AI-004) | Managed database and analytics service | Data and reporting account | Director of Government Contracts |
| Backup vault | Backup service with write-once retention | Backup account (second region) | Director of IT |
| Network hub, cloud firewall, VPN, log pipeline | Network and management services | Shared services and identity and security accounts | Director of IT |
| ePCR tenant | SaaS | ePCR vendor | Director of Clinical Services |
| Identity provider tenant | SaaS | Identity vendor | Director of IT |
| Consoles (18 at headquarters, 6 at Station 10) | Endpoint | Communications centers | Director of Communications |
| SD-WAN edges, firewalls, switches, Wi-Fi, station alerting controllers | Network and OT | 14 sites | Director of IT; Director of Field Operations (alerting) |
| Workstations and laptops (316 outside the centers) | Endpoint | All sites | Director of IT |
| Rugged tablets (210), MDCs (92), routers (106), cardiac monitors (92) | Endpoint, network, medical device | Vehicles | Director of Field Operations |
| SIEM tenant | SaaS | MSSP | Security Manager |

## 10. Control Implementation Details
### 10.1 Control implementation status
**Baseline and tailoring.** The DPCP uses the NIST SP 800-53B **Moderate** baseline (287 controls and enhancements), tailored as follows:
- **Documented here: 119 controls** in `control-implementation.csv`. They cover every SP 800-53 control mapped to a HIPAA Security Rule standard or implementation specification in the Health Care crosswalk (an author mapping), plus the controls that address the risks in P01 (recovery, consoles, vehicles, stations, vendor access, monitoring).
- **Added for High availability:** CP-2(5) (continue mission functions) and CP-4(2) (alternate processing site testing), both from the High baseline. CP-6(2), CP-7(4), and CP-9(3) are scheduled for the 2027 plan update with the warm CAD standby.
- **Selected by tailoring (added):** PM-1, PM-2, and PM-9. They are not in the Moderate baseline but are needed for HIPAA 164.308(a)(1)-(2).
- **Inherited without separate statements:** the remaining Moderate-baseline physical and environmental controls for cloud and SaaS data centers (for example PE-9 to PE-17) and platform-level SA and SC controls, inherited from the ePCR vendor, the identity vendor, the cloud provider, the hosted phone vendor, and the MSSP and evidenced by their SOC 2 Type 2 reports (P09 `vendor-soc2-review.csv`).
- **Deferred:** other Moderate controls with no HIPAA mapping and no Moderate-or-higher risk in P01 (for example SA-11 developer testing and SA-15 development process, because the company does not develop software). They are recorded as tailoring decisions and reviewed yearly.

**Status of the 119 documented controls:**
| Status | Count |
|---|---|
| Implemented | 48 |
| Partially implemented | 67 |
| Planned | 4 |
| Not applicable | 0 |

**Inheritance of the 119 documented controls:**
| Inheritance | Count | Main providers |
|---|---|---|
| System-specific | 72 | Company |
| Hybrid | 33 | Cloud provider, identity vendor, ePCR vendor, MSSP, CAD vendor |
| Common/Inherited | 14 | Identity vendor (for example AC-7, IA-2(1)), cloud provider (CP-6, SC-12, SC-13), MSSP (IR-7), ePCR vendor (AC-12, SI-7) |

The Partially implemented statements trace to the 12 known gaps in `../00_company-facts.md` section 4 and to the P07 findings.

### 10.2 Control assessment status
The co-sourced internal audit firm assessed 36 controls from 2026-08-03 to 2026-08-21 (P07 `assessment-plan.md`, `assessment-results.csv`, and `poam.csv`). Weaknesses are tracked in the POA&M and reported quarterly to the audit committee.

## 11. Digital Identity Acceptance Statement
- **Workforce.** All workforce users authenticate through the identity provider with a password and push MFA with number matching, under conditional access that checks device compliance. Given the Moderate confidentiality rating and remote access to ePHI, this meets the company's authenticator standard for general users.
- **Communications center consoles.** Telecommunicators sign in to CAD with named federated accounts at the start of a shift. Consoles do not lock during a shift, because live calls must stay visible; the badge-controlled center rooms are the documented equivalent measure.
- **Administrators.** Administrators will move to phishing-resistant authenticators (FIDO2 security keys) by 2027-03-31 (P01 R-022). Until then, cloud administrator roles require MFA on every elevation.
- **Exception: MDCs.** The CAD mobile client signs in automatically with 92 per-vehicle accounts. The company accepts this only until named, MFA-protected crew sign-in is deployed (POAM-004, due 2027-03-31). Compensating controls until then: device management with encryption and remote wipe, VPN certificates per vehicle, and a read-only mobile role.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`); BIA (P05); cloud architecture and control map (P04); risk register (P01); gap analysis and roadmap (P03); policies and standards index (P06); assessment and POA&M (P07); incident runbooks (P08); SOC 2 readiness and vendor reviews (P09); AI governance assessment (P10).

## 13. Acronym List and Glossary
- **AVL:** automatic vehicle location
- **BAA:** business associate agreement
- **CAD:** computer-aided dispatch
- **CCT:** critical care transport
- **DPCP:** Dispatch and Patient Care Platform
- **EDR:** endpoint detection and response
- **EMD:** emergency medical dispatch
- **EMSTARS:** Emergency Medical Services Tracking and Reporting System (Florida)
- **ePCR:** electronic patient care report
- **MDC:** mobile data computer
- **MSSP:** managed security service provider
- **MTD, RTO, RPO:** maximum tolerable downtime, recovery time objective, recovery point objective
- **PCS:** physician certification statement
- **POA&M:** plan of action and milestones
- **PSAP:** public safety answering point
- **SD-WAN:** software-defined wide area network

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-07-31 | Draft from the risk analysis and gap analysis | Security Manager |
| 1.0 | 2026-09-16 | Updated with P07 results; approved by the Chief Operating Officer | Director of IT (Security Officer) |
