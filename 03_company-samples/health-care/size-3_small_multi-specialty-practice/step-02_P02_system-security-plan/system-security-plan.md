# System Security Plan: Clinical and Revenue Cycle Platform (CRCP)

**Organization:** Cris Santos Company, LLC (multi-specialty physician practice) | **Tier:** Small | **Vertical:** Health Care and Social Assistance
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Clinical and Revenue Cycle Platform (**CRCP**), identifier CSC-SYS-001.

## 2. System Overview
The CRCP supports every clinical and billing process at the practice's two Florida clinics: scheduling, registration, clinical documentation, e-prescribing, X-ray imaging, lab orders and results, claims, and the patient portal. It serves 60 workforce members and about 18,000 active patients.

**Major components:**
- **SYS-01:** a SaaS electronic health record and practice management system (EHR/PM)
- **SYS-02:** an identity provider for single sign-on and MFA
- **SYS-04:** a public-cloud tenant hosting the imaging archive, the interface engine, and the backup vault
- **SYS-05:** clinic networks
- **SYS-06:** endpoints
- **SYS-07:** medical devices

The cloud tenant is described by service category and is vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| N62-R01 | HIPAA Security Rule | 45 CFR Part 164, Subpart C |
| N62-R02 | HIPAA Privacy Rule | 45 CFR Part 164, Subpart E |
| N62-R03 | HIPAA Breach Notification Rule | 45 CFR 164.400-414 |
| N62-R04 | HIPAA Security Rule NPRM (proposed, not in force) | 90 FR 898 (2025-01-06). Tracked only |
| N62-R07 | Section 1557 patient care decision support tools | 45 CFR 92.210. Relevant to the AI scribe (P10) |
| State | Florida Information Protection Act (breach notification) | Fla. Stat. 501.171 |
| Internal | Security policies POL-01 to POL-05 | P06 |

Not applicable:
- 42 CFR Part 2, because the practice runs no federally assisted SUD program.
- CMS Emergency Preparedness (N62-R08), whose conditions apply to hospitals and 16 other provider types, not to physician offices.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Practice Administrator on 2026-08-31.
### 4.2 System Authorization Decision
The practice is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- The Practice Administrator accepted operation of the CRCP on 2026-08-31, with the conditions in the P07 POA&M.
- The majority owner accepted the High risks listed in P01, with dated treatment plans.
### 4.3 System Operational Status
Operational. Major modification planned: backup architecture redesign (P01 R-005), due 2026-12-31.

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Practice Administrator | Overall accountability; risk acceptance up to Moderate |
| Risk acceptor (authorizing official equivalent) | Majority owner | Acceptance of High and Very High risks |
| Security Officer | IT Manager | Day-to-day security; 45 CFR 164.308(a)(2) designee |
| Privacy Officer | Medical Director | Privacy Rule, breach determinations |
| Operations support | Managed service provider (business associate) | Help desk, patching, backup monitoring |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Health care delivery services (patient records, ePHI) | Moderate | Moderate | Moderate | Disclosure harms patients and triggers breach duties; wrong data could harm care; paper downtime procedures limit availability impact to one clinic day (P05 MTD 8 h) |
| Health care administration (claims, eligibility) | Moderate | Moderate | Low | Financial and identity data; payers accept late claims (P05 MTD 72 h) |
| Human resources management (workforce identities) | Moderate | Low | Low | Account data; limited harm if unavailable |
| **CRCP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 60-person private practice. The plan documents the 70 controls that implement the HIPAA Security Rule and core network hygiene (see `control-implementation.csv`). Every other Moderate-baseline control is treated as follows:
- **Inherited** from the SaaS and cloud providers, as evidenced by their SOC 2 reports (P09).
- **Out of scope for this tier**, recorded as a tailoring decision, where the control's purpose applies only to federal systems. Examples: PM-series program-level controls beyond PM-1, PM-2, and PM-9.

## 7. Authorization Boundary Description
The boundary contains practice-managed components and the practice's configuration of vendor services:
- **Inside:** the EHR tenant configuration and user roles, the identity provider tenant, the cloud tenant (3 workloads), both clinic networks, 70 workstations and laptops, 12 tablets, the X-ray modality workstation, and networked ECG carts and monitors.
- **Outside (external services, interconnected):** the EHR vendor's platform, the cloud provider's infrastructure, the clearinghouse, the reference laboratory, the cloud fax and telehealth services, and the AI scribe service.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Clearinghouse (SYS-08) | Bidirectional | Claims, eligibility, remittance | BAA, contract |
| Reference laboratory (SYS-09) | Bidirectional (HL7 via interface engine) | Orders, results | BAA |
| E-prescribing network (through EHR) | Outbound | Prescriptions | Via EHR vendor BAA |
| Cloud fax (SYS-10) | Bidirectional | Referrals, records requests | **No BAA (gap)** |
| Telehealth video (SYS-10) | Bidirectional | Video visits | **No BAA (gap)** |
| AI scribe (SYS-11) | Outbound audio, inbound draft notes | Visit audio, clinical notes | **BAA under review (gap)** |
| Radiology reading group | Outbound images | X-ray studies | BAA |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| EHR/PM tenant | SaaS | EHR vendor | Practice Administrator |
| Identity provider tenant | SaaS | Identity vendor | IT Manager |
| Imaging archive | Cloud virtual machine and object storage | Cloud tenant | IT Manager |
| Interface engine | Cloud virtual machine | Cloud tenant | IT Manager |
| Backup vault | Cloud backup service | Cloud tenant (same region, **gap**) | IT Manager |
| Clinic firewalls (2) and switches | Network | Clinic A and B | IT Manager |
| Workstations and laptops (70), tablets (12) | Endpoint | Both clinics | IT Manager |
| X-ray unit and modality workstation | Medical device | Clinic A | Clinic A Manager |
| ECG carts (6), vital-sign monitors | Medical device | Both clinics | Clinic Managers |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 70 controls:
- Implemented: 25
- Partially implemented: 32
- Planned: 12
- Not applicable: 1 (AC-4, no clearinghouse function)

### 10.2 Control assessment status
Assessed 2026-08-03 to 2026-08-07. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
All workforce users authenticate through the identity provider with a password and a second factor (a phone authenticator app, or a hardware key for administrators). This is appropriate for remote and privileged access to ePHI given the Moderate categorization.

Patients use the EHR vendor's portal with its own identity proofing and MFA. That is governed by the vendor and outside this boundary.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **BAA:** business associate agreement
- **CRCP:** Clinical and Revenue Cycle Platform
- **EDR:** endpoint detection and response
- **EHR/PM:** electronic health record and practice management
- **ePHI:** electronic protected health information
- **MFA:** multi-factor authentication
- **MSP:** managed service provider
- **POA&M:** plan of action and milestones

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan | IT Manager |
