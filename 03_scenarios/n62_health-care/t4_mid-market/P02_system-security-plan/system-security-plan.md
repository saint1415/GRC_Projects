# System Security Plan: Enterprise Clinical Platform (ECP)

**Organization:** Cris Santos Company, Inc. (PE-backed multi-specialty physician group with an ASC and an imaging center) | **Tier:** Mid-Market | **Vertical:** Health Care and Social Assistance
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-15

## 1. System Name and Identifier
Enterprise Clinical Platform (**ECP**), identifier CSC-ECP-01. The ECP is the company's major system. It comprises SYS-01 to SYS-08 in `../scenario-facts.md`.

## 2. System Overview
The ECP supports every clinical and business process in the BIA (P05) across 8 clinics, the ambulatory surgery center (ASC), the imaging center, and the central business office (CBO). It serves 600 workforce members (including 90 providers) and about 110,000 active patients.

**Major components:**
| ID | Component | Hosting and service model |
|---|---|---|
| SYS-01 | Enterprise EHR/PM, patient portal, e-prescribing, ASC perioperative module | Vendor-hosted SaaS; vendor SOC 2 Type 2 |
| SYS-02 | Identity provider with SSO, MFA, and conditional access | SaaS |
| SYS-03 | PACS and radiology information system, including the FDA-cleared AI triage tool (AI-003) | Vendor-managed software in the company's cloud workloads account |
| SYS-04 | Cloud landing zone: identity, shared services, workloads, and backup accounts; interface engine, data warehouse, file services | Public cloud IaaS/PaaS, vendor-agnostic (P04) |
| SYS-05 | Site networks at 10 sites on SD-WAN | On-premises; SD-WAN managed service |
| SYS-06 | 750 workstations and laptops, 120 tablets | Company-managed |
| SYS-07 | About 400 networked medical devices (ASC infusion pumps and pump server, imaging modalities, ECG, monitors) | On-premises |
| SYS-08 | SIEM operated by the MSSP (a business associate) | SaaS |

Vendors with PHI access (SYS-09) and AI tools (SYS-10) connect to the ECP as external services (section 8).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it affects the ECP |
|---|---|---|---|
| N62-R01 | HIPAA Security Rule | 45 CFR Part 164, Subpart C | Primary control requirement; mapped in `control-implementation.csv` |
| N62-R02 | HIPAA Privacy Rule | 45 CFR Part 164, Subpart E | Minimum necessary access; BAAs |
| N62-R03 | HIPAA Breach Notification Rule | 45 CFR 164.400-164.414 | Detection, logging, and investigation must support breach determinations (P08) |
| N62-R04 | HIPAA Security Rule NPRM | 90 FR 898 (2025-01-06) | **Proposed only.** Tracked in P03; not a current obligation |
| N62-R07 | Section 1557 patient care decision support tools | 45 CFR 92.210 | Applies to AI-002 and AI-003 in the ECP (P10) |
| N62-R08 | CMS emergency preparedness condition for coverage (ASC) | 42 CFR 416.54 | The ECP components at the ASC must support the ASC emergency plan, including a medical documentation system that preserves, protects, and keeps records available (416.54(b)(4)) |
| State | Florida Information Protection Act | Fla. Stat. 501.171 | Breach notification (P08) |
| State | Florida Security of Communications Act | Fla. Stat. 934.03 | All-party consent for AI scribe recording (P10) |
| Contract | Hospital joint venture agreement | Contract | SOC 2 Type 2 report on ECP and CBO services (P09) |
| Internal | Security policies POL-01 to POL-05 and supporting standards | P06 | Policy basis for every control |

Not applicable:
- **42 CFR Part 2.** The company does not operate a federally assisted substance use disorder program.
- **HIPAA group health plan requirements (164.314(b)).** The employee health plan is fully insured, and the company as plan sponsor receives only summary health and enrollment information (P03).
- **PCI DSS scope.** Card payments use a validated point-to-point encryption solution outside the ECP (noted, not assessed).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Chief Operating Officer (system owner) on 2026-09-15, after the control assessment (P07) and before the audit committee meeting the same day.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization to operate. The equivalent internal decision:
- **Decision:** operation of the ECP accepted with conditions, 2026-09-15.
- **Authorizing official equivalent:** Chief Executive Officer for High and Very High risks; Chief Operating Officer for Moderate and below (P01 acceptance authorities).
- **Conditions:** the High-risk POA&M items in P07 must meet their milestones; the audit committee receives POA&M status each quarter; re-decision by 2027-09-30 or after a major change.
### 4.3 System Operational Status
Operational. Major modifications planned:
- Network segmentation at Clinics 4-8 (due 2027-03-31)
- Privileged access management for on-premises and SaaS administrators (due 2027-03-31)
- Onboarding of the PACS, interface engine, and data warehouse to the SIEM (due 2027-01-31)

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Chief Operating Officer | Accountable for the ECP; accepts Moderate risk; executive sponsor of the security program |
| Authorizing official equivalent (High risk) | Chief Executive Officer | Accepts High risk; approves the risk appetite |
| Oversight | Board audit committee | Quarterly cyber risk reporting |
| Program strategy | vCISO (part-time contractor) | Program strategy, board reporting, SSP review |
| Security Officer | IT Director | HIPAA Security Officer (45 CFR 164.308(a)(2)); day-to-day control owner |
| Security operations and GRC | Security Manager and 2 security analysts | Vulnerability management, SIEM liaison, GRC |
| Privacy Officer | Compliance and Privacy Officer | Privacy Rule, breach determinations, BAAs |
| Clinical oversight | Chief Medical Officer | Clinical AI oversight; downtime clinical decisions |
| Business unit owners | ASC Administrator; Imaging Center Director; Director of Clinic Operations; Director of Revenue Cycle | Downtime procedures and access approvals for their units |
| Independent assessment | Co-sourced internal audit firm | Annual IT audit; P07 assessment |
| Monitoring | MSSP (business associate) | 24x7 EDR and SIEM monitoring |

## 6. System Information Types and System Categorization
Information types come from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Health care delivery services (patient records, ePHI, images) | Moderate | Moderate | Moderate | Disclosure of records for up to 110,000 patients is serious but not catastrophic to the organization; wrong data could harm care, but clinicians verify medication and allergy data at each encounter; paper downtime limits availability impact (P05 MTD 4-12 hours) |
| Health care administration (claims, eligibility, prior authorization) | Moderate | Moderate | Low | Financial and identity data; payers accept late claims (P05 MTD 72 hours) |
| Health care research and practitioner safety (quality reporting) | Moderate | Low | Low | Aggregated reporting; can be rebuilt |
| Human resources management (workforce identities) | Moderate | Low | Low | Account data; limited harm if unavailable |
| System and network monitoring (security logs) | Moderate | Moderate | Low | Needed for breach investigations |
| **ECP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Integrity was considered for High.** Medication and implant data at the ASC could contribute to severe harm if altered. The team kept integrity at Moderate for three reasons: clinicians independently verify these data at the point of care, infusion pumps run standalone on a validated library, and the EHR vendor maintains record integrity controls. To compensate, the baseline adds integrity-focused tailoring (section 10.1).

## 7. Authorization Boundary Description
**Inside the boundary:**
- the company's EHR tenant configuration, roles, and interfaces;
- the identity provider tenant;
- the PACS/RIS application stack in the workloads account;
- all 4 cloud accounts and their workloads (interface engine, data warehouse, file services, backups);
- site networks at 10 sites;
- 870 endpoints;
- about 400 networked medical devices;
- the company's SIEM tenant and its use cases.

**Outside the boundary (external services, interconnected):**
- the EHR vendor's platform;
- the cloud provider's infrastructure;
- the MSSP's platform;
- the clearinghouse, reference labs, the health information exchange, and the teleradiology reading group;
- the AI vendors (AI-001, AI-004, AI-005);
- about 140 PHI vendors.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Clearinghouse | Bidirectional (X12 over TLS via interface engine) | Claims, eligibility, remittance | BAA; contract |
| Reference laboratories (2) | Bidirectional (HL7 over TLS) | Orders, results | BAA |
| Health information exchange | Bidirectional | Care summaries | Participation agreement |
| Teleradiology reading group | Outbound images, inbound reports | Studies, reports | BAA |
| E-prescribing network (through the EHR) | Outbound | Prescriptions | Via EHR vendor BAA |
| MSSP | Inbound logs; remote response actions | Security logs (may include PHI fragments) | BAA; SOC 2 Type 2 |
| AI scribe vendor (AI-001) | Outbound audio, inbound draft notes | Visit audio, notes | BAA (vendor standard; amendment pending, P10) |
| Prior-authorization vendor (AI-004) | Bidirectional | Clinical and coverage data | BAA |
| Website chatbot vendor (AI-005) | Inbound patient messages | Names, dates of birth, reasons for visit | **No BAA (gap, P10)** |
| Referring hospitals (4 legacy VPNs) | Bidirectional | Referrals, results | **No written interconnection terms (gap, CA-3)** |
| Hospital joint venture (from 2027) | Bidirectional | Revenue cycle and clinical data for joint venture patients | Joint venture agreement; BAA (P09) |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| EHR/PM tenant and portal | SaaS | EHR vendor | Chief Operating Officer |
| Identity provider tenant | SaaS | Identity vendor | IT Director |
| PACS and RIS, AI triage module | Virtual machines and object storage | Workloads account | Imaging Center Director |
| Interface engine | Virtual machines | Workloads account | IT Director |
| Data warehouse | Managed database service | Workloads account | Chief Financial Officer |
| File services | Managed file service | Workloads account | IT Director |
| Backup vault | Backup service with write-once retention | Backup account (second region) | IT Director |
| Network hub, firewalls, privileged access broker, log forwarding | Network and management services | Shared services account | IT Director |
| Cloud identity federation and organization guardrails | Identity and policy services | Identity account | Security Manager |
| SD-WAN edges, site firewalls, switches, Wi-Fi (10 sites) | Network | Clinics 1-8, ASC, imaging center | IT Director |
| Workstations and laptops (750), tablets (120), downtime report workstations (10) | Endpoint | All sites | IT Director |
| Infusion pumps and pump server | Medical device | ASC | ASC Administrator |
| MRI, CT, X-ray modalities (including 1 legacy MRI console) | Medical device | Imaging center | Imaging Center Director |
| C-arm fluoroscopy (legacy console) | Medical device | ASC | ASC Administrator |
| ECG carts, monitors, other networked devices | Medical device | Clinics | Director of Clinic Operations |
| SIEM tenant | SaaS | MSSP | Security Manager |

## 10. Control Implementation Details
### 10.1 Control implementation status
**Baseline and tailoring.** The ECP uses the NIST SP 800-53B **Moderate** baseline (287 controls and enhancements), tailored as follows:
- **Documented here: 113 controls** in `control-implementation.csv`. These cover every SP 800-53 control mapped to a HIPAA Security Rule standard or implementation specification in the Health Care crosswalk (an author mapping), plus the Moderate controls that address the risks in P01 (segmentation, privileged access, vendor access, monitoring, recovery).
- **Selected by tailoring (added):** PM-1, PM-2, and PM-9. They are not in the Moderate baseline but are needed for HIPAA 164.308(a)(1)-(2).
- **Integrity tailoring:** CM-3 and SI-10 statements cover interface engine and EHR build changes, and SI-7 relies on the EHR vendor's record integrity controls (P01 R-047).
- **Inherited without separate statements:** the remaining Moderate-baseline physical and environmental controls for cloud and SaaS data centers (for example PE-9 to PE-17), and platform-level SA and SC controls. These are inherited from the EHR vendor, the identity vendor, the cloud provider, and the MSSP, and are evidenced by their SOC 2 Type 2 reports, which are reviewed each year (P09 `vendor-soc2-review.csv`).
- **Deferred:** the other Moderate controls with no HIPAA mapping and no Moderate-or-higher risk in P01 (for example SA-11 developer testing and SA-15 development process, because the company does not develop software). They are recorded as tailoring decisions and reviewed yearly.

**Status of the 113 documented controls:**
| Status | Count |
|---|---|
| Implemented | 52 |
| Partially implemented | 58 |
| Planned | 3 |
| Not applicable | 0 |

**Inheritance of the 113 documented controls:**
| Inheritance | Count | Main providers |
|---|---|---|
| System-specific | 66 | Company |
| Hybrid | 31 | EHR vendor, identity vendor, cloud provider, MSSP, PACS vendor, SD-WAN provider |
| Common/Inherited | 16 | Identity vendor (for example AC-7, IA-2(1)), cloud provider (CP-6, SC-12), MSSP (IR-7), EHR vendor (AC-12, SI-7) |

The Partially implemented statements trace to the 9 known gaps in `../scenario-facts.md` section 4 and to the P07 findings.

### 10.2 Control assessment status
The co-sourced internal audit firm assessed 34 controls from 2026-08-03 to 2026-08-21 (P07 `assessment-plan.md`, `assessment-results.csv`, and `poam.csv`). Weaknesses are tracked in the POA&M and reported quarterly to the audit committee.

## 11. Digital Identity Acceptance Statement
- **Workforce.** All workforce users authenticate through the identity provider with a password and push MFA with number matching, under conditional access that checks device compliance and location risk. Given the Moderate categorization and remote access to ePHI, this meets the company's authenticator standard for general users.
- **Administrators.** Administrators will move to phishing-resistant authenticators (FIDO2 security keys) by 2027-03-31 (P01 R-009, R-027). Until then, administrator access to cloud accounts goes through the privileged access broker with just-in-time elevation.
- **Patients.** Patients use the EHR vendor's portal, which provides identity proofing and optional MFA. It is governed by the vendor and outside this boundary. P01 R-049 tracks the plan to promote portal MFA.

## 12. Referenced Artifacts
Scenario facts (`../scenario-facts.md`); risk register (P01); gap analysis and roadmap (P03); cloud architecture and control map (P04); BIA (P05); policies and standards index (P06); assessment and POA&M (P07); incident runbooks (P08); SOC 2 readiness and vendor reviews (P09); AI governance assessment (P10).

## 13. Acronym List and Glossary
- **ASC:** ambulatory surgery center
- **BAA:** business associate agreement
- **CBO:** central business office
- **CUEC:** complementary user entity control (in a SOC 2 report)
- **ECP:** Enterprise Clinical Platform
- **EDR:** endpoint detection and response
- **IdP:** identity provider
- **MSSP:** managed security service provider
- **MTD, RTO, RPO:** maximum tolerable downtime, recovery time objective, recovery point objective
- **PACS, RIS:** picture archiving and communication system, radiology information system
- **POA&M:** plan of action and milestones
- **SD-WAN:** software-defined wide area network

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-07-31 | Draft from the risk analysis and gap analysis | Security Manager |
| 1.0 | 2026-09-15 | Updated with P07 results; approved by the Chief Operating Officer | IT Director (Security Officer) |
