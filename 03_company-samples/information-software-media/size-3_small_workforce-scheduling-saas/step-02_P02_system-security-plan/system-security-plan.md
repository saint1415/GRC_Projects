# System Security Plan: Workforce Scheduling Platform (WSP)

**Organization:** Cris Santos Company, LLC (B2B SaaS software publisher) | **Tier:** Small | **Vertical:** Information
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-22

## 1. System Name and Identifier
Workforce Scheduling Platform (**WSP**), identifier CSC-WSP-001. The WSP is the multi-tenant SaaS production platform the company sells to customers.

## 2. System Overview
The WSP lets about 310 customer organizations in retail, hospitality, and logistics build and publish shift schedules, capture time punches (mobile app, web, and shared kiosks), approve timesheets, export hours and pay rates to their payroll systems, and let workers swap shifts. About 140,000 workers and 6,000 customer managers and administrators use it. The AI assistant (schedule summaries and shift-swap suggestions) is in beta with 40 customers (P10).

**Major components:**
- **SYS-01:** the production environment in one public-cloud account: web application, mobile API, background workers (notifications and payroll exports), the AI service, a managed relational database, object storage for payroll export files, cache, message queue, key management, and a secrets manager
- **SYS-03:** the SaaS source repository and CI/CD pipeline that build and deploy the WSP
- **SYS-04:** the identity provider for workforce single sign-on and MFA
- **SYS-05 (admin console):** the internal console used by support agents, including the "view as tenant" feature
- **SYS-06:** logging, monitoring, and uptime services

The cloud tenant is described by service category and is vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it affects the WSP |
|---|---|---|---|
| N51-R01 | FTC Act Section 5 | 15 U.S.C. 45(a); unfairness test 45(n) | Reasonable security for worker data, and accuracy of the company's security and data-use statements. Gap analysis in P03 |
| N51-R03 | CCPA/CPRA and CPPA regulations | Cal. Civ. Code 1798.100 et seq.; 1798.140 | The company is a CCPA "business" (revenue above $26,625,000) and a service provider for customers' California workers. Applicability check in P03; no gap table |
| N51-R04 | DOJ Data Security Program | 28 CFR Part 202 | Applicability check only: no covered data transactions with countries of concern or covered persons (P03) |
| Contract | Customer MSA and DPA | Contract | 99.9% SLA, 72-hour (48-hour for 3 customers) incident notice, 30-day sub-processor notice, 90-day deletion |
| Assurance | SOC 2 Trust Services Criteria | AICPA 2017 TSC (2022 points of focus) | Type 1 issued; Type 2 readiness in P09 |
| State | Florida Information Protection Act (breach notification; third-party agent duties) | Fla. Stat. 501.171 | Notice duties in P08; other states handled generically |
| Internal | Security policies POL-01 to POL-05 | P06 | |

Not applicable (see `../00_company-facts.md` section 1): COPPA (N51-R02), FCC CPNI (N51-R06), FedRAMP (N51-R07), SEC disclosure (N51-R08), PADFA (N51-R05, the company is not a data broker), HIPAA, and PCI DSS.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the CTO (system owner) on 2026-09-22.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- The CTO accepted continued operation of the WSP on 2026-09-22, with the conditions in the P07 POA&M.
- The Chief Executive Officer accepted the 4 High risks in P01 only until their dated treatments close (latest 2027-01-31).
### 4.3 System Operational Status
Operational. Major modifications planned: privileged access redesign (R-002, due 2026-10-23), CI/CD credential redesign (R-001, due 2026-10-16), and a separate backup account (R-007, due 2026-12-15).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | CTO | Overall accountability; accepts Moderate risk |
| Risk acceptor (authorizing official equivalent) | Chief Executive Officer (majority owner) | Accepts High and Very High risk |
| Security and compliance lead | IT Manager | Policies, SOC 2 program, identity provider, control monitoring |
| Technical operations lead | Platform Engineering Lead | Cloud accounts, CI/CD, backups, on-call, incident technical lead |
| Application security owner | Engineering Manager | Secure development, tenant isolation, code review |
| Privacy lead | COO | DPAs, sub-processors, breach notification decisions with counsel |

## 6. System Information Types and System Categorization
Information types were chosen with reference to NIST SP 800-60 Vol. 2 Rev. 1 (closest matching types), and impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Customer workforce records (names, contact details, roles, availability, pay rates) | Moderate | Moderate | Low | Disclosure harms workers and breaches the DPA; no Social Security, health, or financial account numbers, so not High |
| Time and attendance and payroll exports (punches, hours, pay rates) | Moderate | Moderate | Moderate | Wrong or lost punches cause pay errors; clock-in outage stops customer operations (P05 MTD 8 h). Mobile and kiosk offline queues limit the impact |
| System development and operations (source code, secrets, configuration) | Moderate | Moderate | Low | Secrets give access to customer data (R-001) |
| **WSP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 60-person SaaS company. `control-implementation.csv` documents 86 controls: the 82 Moderate-baseline controls that matter most for multi-tenant SaaS and SOC 2, plus 4 controls selected by tailoring (CA-8, PM-9, PT-2, SA-3(2)) because of the penetration test commitment, risk acceptance levels, the DPA's purpose limits, and the staging data gap. Every other Moderate-baseline control is treated as follows:
- **Inherited** from the cloud provider and SaaS providers (for example, the PE and MA families), with evidence from their SOC 2 reports (P09 vendor reviews).
- **Not selected at this tier**, recorded as a tailoring decision, where the control mainly serves federal systems (for example, most PM-series program controls).

## 7. Authorization Boundary Description
- **Inside:** the production cloud account (all SYS-01 services), the configuration of the source repository and CI/CD pipeline (SYS-03), the identity provider tenant (SYS-04), the internal admin console, the logging and monitoring configuration (SYS-06), and the company laptops used to administer them (SYS-10).
- **Connected system in scope for data protection:** the staging account (SYS-02), because it holds unmasked copies of production data until the purge due 2026-10-30.
- **Outside (external services, interconnected):** the cloud provider's infrastructure, the email and SMS delivery providers (SYS-07), the AI model provider (SYS-08), the support ticketing SaaS, and the payment processor used for customer billing (no worker data).

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Customer payroll systems | Outbound (file download or API pull by the customer) | Hours, pay rates, employee IDs | MSA and DPA |
| Customer identity providers | Inbound (SAML single sign-on) | Authentication assertions | MSA (customer configuration) |
| Email delivery service (SYS-07) | Outbound | Worker name, email, shift details | DPA (sub-processor) |
| SMS provider (SYS-07) | Outbound | Worker mobile number, shift details | DPA (sub-processor) |
| AI model provider (SYS-08) | Outbound prompts, inbound completions | Schedule data, availability, first names (names to be removed, P10) | Click-through API terms only; **DPA not yet signed (gap)** |
| Logging and monitoring SaaS (SYS-06) | Outbound | Application logs (some incidental personal data) | DPA (sub-processor) |
| Support ticketing SaaS | Bidirectional | Tickets, screenshots from customers | DPA (sub-processor) |
| Staging account (SYS-02) | Outbound snapshot copies (to stop) | Full production data | Internal (**gap**) |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| Web application, mobile API, background workers, AI service | Containers on a managed container service | Production cloud account | Engineering Manager |
| Load balancer and web application firewall | Managed network service | Production cloud account | Platform Engineering Lead |
| Relational database (multi-tenant) | Managed database service | Production cloud account | Platform Engineering Lead |
| Payroll export bucket and other object storage | Object storage | Production cloud account | Platform Engineering Lead |
| Cache and message queue | Managed services | Production cloud account | Platform Engineering Lead |
| Key management and secrets manager | Managed services | Production cloud account | Platform Engineering Lead |
| Snapshots and cross-region copies | Backup service | Production cloud account (same account, **gap**) | Platform Engineering Lead |
| Source repository and CI/CD pipeline | SaaS | Source hosting vendor | Platform Engineering Lead |
| Identity provider tenant | SaaS | Identity vendor | IT Manager |
| Internal admin console | Part of the web application | Production cloud account | Customer Support Manager |
| Logging, monitoring, uptime | SaaS | Observability vendor | Platform Engineering Lead |
| Laptops (60 plus 6 spares) | Endpoint | Company-managed | IT Manager |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 86 controls:
- Implemented: 38
- Partially implemented: 39
- Planned: 9
- Not applicable: 0

By inheritance: 62 system-specific, 17 hybrid, 7 common/inherited.

The three SOC 2 Type 1 exceptions appear here as AC-2 and AC-6 (shared break-glass role), SA-3(2) (production data in staging), and SA-9 (sub-processor oversight).

### 10.2 Control assessment status
Assessed 2026-08-31 to 2026-09-04 by an independent assessor. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
All workforce users authenticate through the identity provider with a password and a second factor. The 6 engineers with production access use hardware security keys, which resist phishing. This fits the Moderate categorization and the privileged access these accounts carry.

Customer users authenticate with platform accounts or their own single sign-on. MFA is enforced for customer administrators, who can see all their workers' data, and is optional for workers, who see only their own schedules. The residual risk of worker account takeover is R-017 in P01.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness (P09), AI assessment (P10), SOC 2 Type 1 report (2026-02-28).

## 13. Acronym List and Glossary
- **CI/CD:** continuous integration and continuous delivery
- **DPA:** data processing agreement
- **EDR:** endpoint detection and response
- **MFA:** multi-factor authentication
- **MSA:** master subscription agreement
- **POA&M:** plan of action and milestones
- **SLA:** service level agreement
- **Sub-processor:** a vendor that processes customer data on the company's behalf
- **WSP:** Workforce Scheduling Platform

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-09-22 | Initial plan (replaces the SOC 2 Type 1 system description as the control reference) | IT Manager |
