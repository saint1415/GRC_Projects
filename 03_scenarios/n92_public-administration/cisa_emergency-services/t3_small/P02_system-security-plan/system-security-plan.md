# System Security Plan: Dispatch and Patient Care Platform (DPCP)

**Organization:** Cris Santos Company, LLC (licensed private ambulance service) | **Tier:** Small | **Vertical:** Emergency Services
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-04

## 1. System Name and Identifier
Dispatch and Patient Care Platform (**DPCP**), identifier CSC-SYS-001.

## 2. System Overview
The DPCP supports every step of an ambulance response: call intake and dispatch, unit tracking, patient care documentation, hospital record delivery, and the hand-off of trip data to billing. It serves 60 workforce members and about 16,000 transports a year from headquarters, Station 2, and 9 ambulances.

**Major components:**
- **SYS-01:** computer-aided dispatch (CAD), vendor-licensed software run in the company's cloud tenant
- **SYS-02:** a SaaS electronic patient care reporting system (ePCR)
- **SYS-04:** an identity provider for single sign-on and MFA
- **SYS-06:** a public-cloud tenant hosting the CAD server and database, the integration engine, the call recording archive, and the backup vault
- **SYS-07:** the dispatch center at headquarters
- **SYS-09:** fleet mobile systems (vehicle routers, mobile data computers, ePCR tablets, cardiac monitors)
- **SYS-10:** site networks
- **SYS-11:** endpoints

The cloud tenant is described by service category and is vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| C-EMERGENCY-R04 | HIPAA Security Rule | 45 CFR Part 164, Subpart C. The company is a covered entity (45 CFR 160.103) |
| Related | HIPAA Breach Notification Rule | 45 CFR 164.400-414 |
| C-EMERGENCY-R05 | CIRCIA (proposed, not in force) | Proposed 6 CFR 226 (89 FR 23644). Tracked only. If finalized as proposed, 226.2(b)(5) would reach EMS providers serving 50,000 or more people, regardless of size |
| Related | HIPAA Security Rule NPRM (proposed, not in force) | 90 FR 898 (2025-01-06). Tracked only |
| Medicare | Ambulance coverage and documentation | 42 CFR 410.40(e) (certification statements on file); 410.41(c) (billing and reporting); 424.516(f) (keep documentation 7 years) |
| State | EMS records and patient care records | Fla. Stat. 401.30; Rule 64J-1.014, F.A.C. (5-year retention; record to the receiving hospital on request within 48 hours) |
| State | Call recording by a licensed ambulance service | Fla. Stat. 934.03(2)(g) |
| State | Florida Information Protection Act (breach notification) | Fla. Stat. 501.171 |
| Federal | Section 1557 patient care decision support tools | 45 CFR 92.210. Relevant to AI call triage (P10) |
| Contract | County ambulance service agreement | CAD-to-CAD interface and response-time reporting |
| Internal | Security policies POL-01 to POL-05 | P06 |

Not applicable:
- FBI CJIS Security Policy (C-EMERGENCY-R01) and 28 CFR 20.21 and Part 23 (C-EMERGENCY-R02, R03): the DPCP does not store, process, or view criminal justice information. The county CAD-to-CAD feed carries EMS incident data only. See P03 section 1.
- FCC EAS rules (C-EMERGENCY-R06): the company is not an EAS participant.
- 42 CFR Part 2: the company runs no federally assisted substance use disorder program.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the COO on 2026-09-04.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- The COO accepted operation of the DPCP on 2026-09-04, with the conditions in the P07 POA&M.
- The majority owner accepted the High and Very High risks listed in P01, with dated treatment plans.
### 4.3 System Operational Status
Operational. Major modifications planned: backup redesign (P01 R-002, due 2026-11-30), headquarters network segmentation (2026-12-31), and CAD federation to the identity provider (2026-12-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | COO | Overall accountability; risk acceptance up to Moderate |
| Risk acceptor (authorizing official equivalent) | Majority owner | Acceptance of High and Very High risks |
| Security Officer | IT Manager | Day-to-day security; 45 CFR 164.308(a)(2) designee |
| Privacy Officer | Billing and Compliance Manager | Privacy Rule, breach determinations |
| Dispatch operations | Communications Center Supervisor | CAD use, manual dispatch mode, CAD query review |
| Clinical oversight | Medical Director (contracted) | Dispatch and patient care protocols; AI triage validation |
| Operations support | Managed service provider (business associate) | Help desk, patching, cloud administration, backup monitoring |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Emergency response (call and dispatch data) | Moderate | Moderate | **High** | A CAD outage during an emergency can delay an ambulance, which can contribute to loss of life. Manual dispatch reduces but does not remove that harm (P05 MTD 2 h) |
| Health care delivery services (patient care records, ePHI) | Moderate | Moderate | Moderate | Disclosure triggers breach duties; wrong data could affect hospital care; paper records cover short outages (P05 MTD 24 h) |
| Health care administration (claims, certification statements) | Moderate | Moderate | Low | Financial and identity data; payers accept late claims (P05 MTD 72 h) |
| Human resources management (workforce identities) | Moderate | Low | Low | Account data; limited harm if unavailable |
| **DPCP category (high-water mark)** | **Moderate** | **Moderate** | **High** | Overall: **High** |

**Baseline:** a tailored baseline for a 60-person private company. The plan uses the NIST SP 800-53B Moderate baseline as the starting point and adds High-baseline controls where the High availability rating calls for them (CP-2(5) today; more in the 2027 plan update). It documents the 77 controls that implement the HIPAA Security Rule, dispatch continuity, and core network hygiene (see `control-implementation.csv`). Every other Moderate-baseline control is treated as follows:
- **Inherited** from the SaaS and cloud providers, as evidenced by their SOC 2 reports (P09).
- **Out of scope for this tier**, recorded as a tailoring decision, where the control's purpose applies only to federal systems. Examples: PM-series program-level controls beyond PM-1, PM-2, and PM-9.

## 7. Authorization Boundary Description
The boundary contains company-managed components and the company's configuration of vendor services:
- **Inside:** the CAD application server and database, the integration engine, the call recording archive, and the backup vault in the cloud tenant; the ePCR tenant configuration and user roles; the identity provider tenant; the dispatch center; both site networks; 28 workstations and laptops, 22 rugged tablets, 9 mobile data computers, 9 vehicle routers, and 9 cardiac monitors.
- **Outside (external services, interconnected):** the ePCR vendor's platform, the cloud provider's infrastructure, the billing platform and clearinghouse, the hosted phone system, the AI triage service, the cardiac monitor relay, the county CAD and P25 radio system, receiving hospitals, and the state EMS data system.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| County CAD (county PSAP) | Inbound incidents; outbound unit status | Incident type, address, callback number, notes, unit times | County ambulance service agreement. **No interconnection security terms (gap)** |
| Billing platform and clearinghouse (SYS-03) | Outbound trip data; claims to payers | Demographics, service level, mileage, certification statements | BAA, contract |
| Receiving hospitals | Outbound | Patient care records through the ePCR hospital portal | Treatment disclosure; hospital portal terms |
| State EMS data system (EMSTARS) | Outbound | Incident-level ePCR data in the state format | Rule 64J-1.014, F.A.C. |
| Hosted phone system (SYS-08) | Bidirectional | Calls and recordings | **No BAA (gap)** |
| AI triage service (SYS-12) | Outbound call audio; inbound suggestions | Call audio, transcripts, suggested call type and priority | **BAA amendment pending (gap)** |
| Cardiac monitor relay | Outbound | 12-lead ECGs to hospitals | BAA |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| CAD application server | Cloud virtual machine | Cloud tenant | IT Manager |
| CAD database | Managed database (PaaS) | Cloud tenant | IT Manager |
| Integration engine | Cloud virtual machine | Cloud tenant | IT Manager |
| Call recording archive | Object storage | Cloud tenant | Communications Center Supervisor |
| Backup vault | Cloud backup service | Cloud tenant (same region, **gap**) | IT Manager |
| ePCR tenant | SaaS | ePCR vendor | Clinical Services Coordinator |
| Identity provider tenant | SaaS | Identity vendor | IT Manager |
| Dispatch consoles (5) and supervisor position | Endpoint | Headquarters dispatch room | Communications Center Supervisor |
| Firewalls (2) and switches | Network | Headquarters and Station 2 | IT Manager |
| Workstations and laptops (28), rugged tablets (22) | Endpoint | Both sites and ambulances | IT Manager |
| Vehicle routers (9) and mobile data computers (9) | Network and endpoint | Ambulances | Operations Manager |
| Cardiac monitors (9) | Medical device | Ambulances | Operations Manager |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 77 controls:
- Implemented: 21
- Partially implemented: 43
- Planned: 13
- Not applicable: 0

### 10.2 Control assessment status
Assessed 2026-08-10 to 2026-08-14. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
Office, ePCR, and billing users authenticate through the identity provider with a password and a second factor (a phone authenticator app). Administrators will move to hardware security keys by 2026-10-31 (P01 R-022). This is appropriate for remote and privileged access to ePHI given the Moderate confidentiality rating.

**Exception:** CAD users sign in with shared position accounts at the consoles and per-vehicle accounts on the MDCs. The company accepts this only until CAD is federated with the identity provider (POAM-003, due 2026-12-31). During the transition the badge-controlled dispatch room is the compensating control. Dispatch consoles will use a fast sign-in so that named accounts do not slow call handling.

## 12. Referenced Artifacts
Scenario facts (`../scenario-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 self-benchmark (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **AVL:** automatic vehicle location
- **BAA:** business associate agreement
- **CAD:** computer-aided dispatch
- **DPCP:** Dispatch and Patient Care Platform
- **EDR:** endpoint detection and response
- **EMSTARS:** Emergency Medical Services Tracking and Reporting System (Florida)
- **ePCR:** electronic patient care report
- **MDC:** mobile data computer
- **MFA:** multi-factor authentication
- **MSP:** managed service provider
- **PCS:** physician certification statement
- **PSAP:** public safety answering point
- **POA&M:** plan of action and milestones

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-09-04 | Initial plan | IT Manager |
