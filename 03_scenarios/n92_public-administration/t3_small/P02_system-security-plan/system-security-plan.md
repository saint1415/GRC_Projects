# System Security Plan: Agency Case Management Platform (ACMP)

**Organization:** Cris Santos Company, LLC (GovTech systems integrator) | **Tier:** Small | **Vertical:** Public Administration
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Agency Case Management Platform (**ACMP**), identifier CSC-SYS-001.

## 2. System Overview
The ACMP is a multi-tenant case management service that the company builds, hosts, and supports for 11 Florida agencies. Agency staff use it to run casework: pretrial and probation supervision for a sheriff's office (AC-02), benefits application intake and verification for a state human services agency (AC-03), tax compliance casework for a state revenue agency (AC-01), and constituent and code enforcement cases for 8 counties and cities. About 455,000 individuals have records in the platform.

**Major components:**
- **SYS-01:** the production application: managed container service, managed relational database cluster, a dedicated database instance for AC-01, object storage for documents, and a message queue
- **SYS-02:** the integration gateway (file transfer from AC-01, API link to the AC-02 message switch, API link to the AC-03 eligibility system)
- **SYS-04:** agency user sign-in (federation with agency identity providers; local accounts for municipal tenants)
- **SYS-10:** development, test, and staging environments in separate cloud accounts
- **SYS-11:** the AI eligibility assistant pilot for AC-03
- **SYS-12 and SYS-13:** backups, and logging and monitoring

Supporting services that administer the system: the workforce identity provider (SYS-03), the repository and CI/CD pipeline (SYS-06), and administrator laptops (part of SYS-08). The cloud tenant is described by service category and is vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it reaches the company |
|---|---|---|---|
| Contract | NIST SP 800-53 Rev. 5 (Release 5.2.0) Moderate baseline | SP 800-53B Moderate baseline | All 11 agency contracts |
| N92-R02 | FBI CJIS Security Policy | CJISSECPOL v6.1 (06/25/2026); 28 CFR 20.33(a)(7) | CJIS Security Addendum in the AC-02 contract |
| N92-R01 | IRS Publication 1075 (FTI safeguards) | 26 U.S.C. 6103(p)(4); 26 CFR 301.6103(n)-1; Pub. 1075 (Rev. 11-2021) | Exhibit 7 language in the AC-01 contract |
| N92-R04 | Medicaid applicant and beneficiary safeguards | 42 CFR 431.300-431.307 | AC-03 contract confidentiality terms (with SNAP, 7 CFR 272.1(c)) |
| State | Florida Cybersecurity Standards | Rule 60GG-2, F.A.C.; Fla. Stat. 282.318(4)(h) | Security terms in AC-01 and AC-03 contracts |
| State | Florida Information Protection Act | Fla. Stat. 501.171(2) and (6) | Directly, as a third-party agent |
| N92-R08 | GovRAMP (formerly StateRAMP) | GovRAMP program (not law) | Requested by prospective customers (P09) |
| Internal | Security policies POL-01 to POL-05 | P06 | Company policy |

Not applicable:
- HIPAA Security Rule (N92-R03): no customer has designated the company a business associate.
- Driver's Privacy Protection Act (N92-R05): no motor vehicle agency customers.
- FTI in the AC-03 tenant: prohibited by contract, because human services agencies may not disclose FTI to contractors (Pub. 1075 section 2.C.11.2).
- CIRCIA (N92-R07): proposed rule only.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Chief Operating Officer (system owner) on 2026-08-31.
### 4.2 System Authorization Decision
The company is not a federal agency and there is no formal federal authorization. The equivalent decisions:
- The Chief Operating Officer accepted continued operation of the ACMP on 2026-08-31 with the conditions in the P07 POA&M.
- The Chief Executive Officer accepted the Very High and High risks listed in P01 only with dated treatment plans, and directed that the 4 unscreened staff lose access to AC-01 and AC-02 data until screening is complete.
- AC-01 and AC-02 will receive this SSP, the P07 assessment, and the POA&M by 2026-12-31 (CA-6).
### 4.3 System Operational Status
Operational. Major modifications planned: backup redesign into a separate account and second U.S. region (P01 R-001), FIPS 140-3 certified TLS on CJI paths by 2026-09-21 (SC-13), and a 7-year log archive (AU-11).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Chief Operating Officer | Overall accountability; risk acceptance up to Moderate |
| Risk acceptor (authorizing official equivalent) | Chief Executive Officer | Acceptance of High and Very High risks |
| Information Security Officer | IT Manager | Day-to-day security; security contact named in agency contracts |
| Privacy and contract compliance | Contracts and Compliance Manager | Agency security terms; breach notices to agencies |
| System operations | Cloud Operations Lead | Production tenant, backups, logging, patching |
| Development | Director of Engineering | Code, pipeline, change management |
| AI feature owner | Data and AI Lead | SYS-11 (P10) |
| Agency counterparts | AC-01 disclosure officer; AC-02 local agency security officer; AC-03 information security manager | Receive notices; approve agency users; hold Security Addendum certifications (AC-02) |

## 6. System Information Types and System Categorization
Information types were modeled on the mission-based categories in NIST SP 800-60 Vol. 2 Rev. 1. Impact levels are the company's FIPS 199 determinations, agreed with the three large customers.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Criminal justice supervision records (CJI, including CHRI) for AC-02 | Moderate | Moderate | Moderate | Disclosure harms supervisees and is restricted by 28 CFR Part 20; wrong conditions or violation data could lead to wrongful arrest; the sheriff can run one shift on paper (P05 MTD 12 h) |
| Taxation management records with FTI for AC-01 | Moderate | Moderate | Low | Unauthorized disclosure carries criminal and civil penalties (IRC 7213, 7213A, 7431); agency tax system keeps collections running (P05 MTD 48 h) |
| Benefits application records for AC-03 (SNAP, TANF, Medicaid) | Moderate | Moderate | Moderate | Social Security numbers and income data; errors or delays affect food and medical assistance timeliness (P05 MTD 24 h) |
| Constituent service records for municipal customers | Low | Low | Low | Names, addresses, some driver license numbers; paper workaround for 3 days |
| System and security information (credentials, logs, keys) | Moderate | Moderate | Moderate | Compromise gives access to all tenants |
| **ACMP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** the NIST SP 800-53B **Moderate** baseline, as every agency contract requires: 177 base controls with 110 enhancements. `control-implementation.csv` has one row per base control, and each statement covers the control's Moderate enhancements. Tailoring decisions:
- **Not applicable (4):** AC-18, MA-3, MP-5, SC-15, with reasons in each row.
- **Inherited or hybrid:** physical, environmental, and infrastructure controls are inherited from the FedRAMP Moderate authorized cloud provider (PE family, SC-4, SC-39, and others).
- **Overlay values:** where CJISSECPOL v6.1 or Pub. 1075 sets a stricter value (for example, 5 failed logons in 15 minutes for AC-7, 1-year and 7-year log retention for AU-11, FIPS 140-3 for SC-13), the stricter value governs. Recording all of them as organization-defined values is an open item (PL-11).
- IA-2(12) (acceptance of PIV credentials) has no effect because no users hold PIV credentials.

## 7. Authorization Boundary Description
The boundary contains the company's cloud accounts for production and non-production, and the company's configuration of the cloud and SaaS services that administer them:
- **Inside:** the production account (SYS-01, SYS-02, SYS-04, SYS-11 application components, SYS-12, SYS-13), the non-production accounts (SYS-10), identity provider configuration (SYS-03), pipeline configuration and secrets (SYS-06), and the 18 administrator and support laptops with production access.
- **Outside (external services, interconnected):** the cloud provider's infrastructure and managed services (FedRAMP Moderate authorized), the managed large language model service used by SYS-11, the support ticketing service (SYS-07), the productivity suite (SYS-05), agency identity providers, and agency systems on the other end of each interface.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| AC-01 tax system | Inbound nightly file transfer; outbound case status | FTI and state tax data | Contract with Exhibit 7; IRS 45-day notification (2024) |
| AC-02 message switch | Inbound criminal history summaries; outbound supervision status | CJI including CHRI | Contract with CJIS Security Addendum; interface specification |
| AC-03 eligibility system | Bidirectional API | Applicant and household data | Contract; **no interconnection security agreement yet (gap, CA-3)** |
| Agency identity providers (AC-01, AC-02, AC-03) | Inbound assertions | User identity and roles | Federation agreements in contracts |
| Managed model service (SYS-11) | Outbound prompts, inbound text | AC-03 applicant documents and extracted data | Provider standard terms; **vendor review pending (gap, SR-6)** |
| Ticketing vendor (SYS-07) | Inbound from agencies | Ticket text and screenshots (**FTI and CJI observed; gap, SA-9**) | Click-through terms only |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| Web and application containers | Managed container service | Cloud tenant, U.S. region A, 3 zones | Cloud Operations Lead |
| Shared database cluster (AC-02, AC-03, municipal tenants) | Managed relational database | Cloud tenant | Cloud Operations Lead |
| AC-01 dedicated database instance, customer-managed key | Managed relational database | Cloud tenant | Cloud Operations Lead |
| Document storage | Object storage | Cloud tenant | Cloud Operations Lead |
| Integration gateway | Containers, file transfer service, API gateway | Cloud tenant | Director of Engineering |
| AI eligibility assistant | Containers plus managed model service | Cloud tenant; provider AI service | Data and AI Lead |
| Backups | Database point-in-time recovery and snapshots | Same account and region (**gap**) | Cloud Operations Lead |
| Logging | Managed log service, 90-day retention (**gap**) | Cloud tenant | Cloud Operations Lead |
| Non-production environments | Separate accounts | Cloud tenant | Director of Engineering |
| Administrator and support laptops (18) | Endpoint | Headquarters and remote (U.S.) | IT Manager |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 177 base controls:
- Implemented: 59
- Partially implemented: 97
- Planned: 17
- Not applicable: 4

By inheritance: 126 system-specific, 26 hybrid, and 25 common or inherited.

### 10.2 Control assessment status
20 controls were assessed 2026-08-03 to 2026-08-07. See P07 `assessment-results.csv` and `poam.csv`. The P03 gap analysis rated all 177 controls plus the CJIS and Pub. 1075 overlays.

## 11. Digital Identity Acceptance Statement
- **Workforce:** every user signs in through the identity provider with a password and an authenticator app with number matching. The 5 cloud administrators use phishing-resistant hardware keys. This meets CJISSECPOL IA-2(1) and IA-2(2) ([Priority 1]) and Pub. 1075 IA-2 multi-factor requirements.
- **Agency users:** AC-01, AC-02, and AC-03 users are authenticated by their agencies' identity providers, which enforce MFA; the agencies own identity proofing. Municipal local accounts do not all require MFA today (gap, IA-8), which is acceptable only because those tenants hold no CJI, FTI, or benefits data. MFA for them is due 2026-11-30.

## 12. Referenced Artifacts
Scenario facts (`../scenario-facts.md`), risk register (P01), gap analysis (P03), cloud control map (P04), BIA (P05), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **ACMP:** Agency Case Management Platform
- **CHRI:** criminal history record information
- **CJI:** criminal justice information
- **CJISSECPOL:** FBI CJIS Security Policy
- **CSO:** CJIS Systems Officer
- **FTI:** federal tax information
- **MFA:** multi-factor authentication
- **POA&M:** plan of action and milestones
- **TIGTA:** Treasury Inspector General for Tax Administration

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan, replacing the 2023 proposal document | IT Manager |
