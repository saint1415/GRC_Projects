# System Security Plan: Workforce Cloud Platform (WCP)

**Organization:** Cris Santos Company Holdings, Inc. (Cloud Software division; inherits corporate shared services used by all three divisions) | **Tier:** Multi-Sector | **Vertical:** Information
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-17

> **Why this system.** At this tier the SSP can cover one system per division or a shared corporate system. The group chose the **Workforce Cloud Platform**, the focus division's multi-tenant SaaS production platform, because it holds the most personal data in the group (about 21 million worker profiles), it carries data that belongs to another division (the payroll handoff files of Payments and Payroll), consultants from the third division work inside its customer tenants, and it carries the group's top risk (P01 GR-01). It inherits most of its controls from corporate (SYS-G1 to SYS-G3). The payroll engine (SYS-D3) and the payments platform (SYS-D4) keep division plans that inherit from the same common control catalog (`common-control-catalog.csv`); the payments platform also has its PCI DSS documentation.

## 1. System Name and Identifier
Workforce Cloud Platform (**WCP**), identifier CSCH-SYS-D1-WCP. SYS-D1 in `../00_company-facts.md`.

## 2. System Overview
The WCP is the production environment of *Workforce Cloud*, a workforce management and HR SaaS. It serves about 38,000 customer organizations and about 21 million worker profiles in all 50 states. Customers use it for scheduling, time and attendance, HR records, and an employee self-service mobile app (about 14 million monthly active workers). Two optional AI features run inside it: the generative **workforce assistant** (6,200 opt-in customers) and **attrition-risk insights** (about 9,800 customers).

The WCP is also the front door of the group's embedded finance. Workers enter direct deposit details in the self-service app, and each night the export service writes a **payroll handoff file** per embedded-payroll employer for the payroll engine (SYS-D3) of the Payments and Payroll division. Checkout pages for the payments platform (SYS-D4) are embedded in WCP pages, but card data goes directly to the payments platform and never touches the WCP.

**Major components** (provider A, primary and warm standby regions; immutable backups in provider B):
- **Web and mobile front ends** and the public API gateway
- **Application services** on a managed container platform
- **Tenant databases:** managed relational databases with tenant-scoped roles and customer-managed keys
- **Export and integration service** with the **export bucket** (object storage) for payroll handoff files and customer exports
- **AI services:** workforce assistant orchestration (calls a third-party hosted model under zero-retention terms) and the attrition-risk model
- **Support and admin console** with tenant-scoped support access
- **Implementation interfaces** used by consultants (tenant configuration and data load, including the data migration toolkit's connection)

The platform is described by service category and is vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies to the WCP |
|---|---|---|---|
| N51-R01 | FTC Act Section 5 | 15 U.S.C. 45(a) | Reasonable security for worker data (unfairness, 45(n)) and truthful security and data-use statements (deception). Primary analysis in P03 |
| SOC 2 | Trust Services Criteria (contractual) | AICPA 2017 TSC (2022 points of focus) | Annual Type 2 (Security, Availability, Confidentiality); service commitments in MSAs and DPAs (P09) |
| N51-R03 | CCPA and CPPA regulations | Cal. Civ. Code 1798.140 (service provider); Cal. Code Regs. tit. 11, 7120-7124 | Service-provider use limits for customer data; the group's cybersecurity audit (first period 2027) will include the WCP |
| N51-R04 | DOJ Data Security Program | 28 CFR Part 202 | The WCP holds covered personal identifiers and financial data above the bulk thresholds; no vendor, employee, or investor access from countries of concern is allowed (sub-processor screening) |
| N52-R03 | FTC Safeguards Rule (through the Payments and Payroll division) | 16 CFR 314.4(c), (f) | The WCP acts as an affiliate service provider for the payroll handoff data. The division must oversee it, and the WCP must protect that data to Part 314 standards (encryption, access, retention, monitoring) |
| N51-R08 | SEC cybersecurity disclosure | Reg S-K Item 106; Form 8-K Item 1.05 | A WCP incident may be material to the group (P08) |
| 12 CFR 53.4; 225.303; 304.24 | Bank service provider notification | 12 CFR Part 53, 225, 304 | About 420 bank and credit union customers; notice when an incident disrupts their covered services for 4 or more hours |
| Contracts | MSA, DPA, sub-processor terms | Customer contracts | 99.95% availability; 72-hour incident notice (48 hours for about 1,240 customers); 30 days' sub-processor notice; deletion within 90 days |
| State law | Breach notification | Each state where affected individuals reside; Florida worked example: Fla. Stat. 501.171 | The division is a third-party agent for its customers under Florida law (notice to the customer within 10 days) (P08) |
| Internal | Group policies POL-01 to POL-05 and the Cloud Software supplement | P06 | |

Not applicable: FedRAMP (no government edition), COPPA (not directed to children), HIPAA (no PHI in the WCP; the consulting division's health-system integrations pass only staffing counts into WCP tenants), PCI DSS (no account data in the WCP; checkout posts directly to SYS-D4, which is confirmed each six months in the PCI DSS scope review).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Cloud Software chief technology officer (system owner) and the Cloud Software division CISO on 2026-09-17, after the board risk committee review.

### 4.2 System Authorization Decision
The group is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- **Decision:** authorized to operate with conditions, 2026-09-17, by the Group CISO and the Cloud Software division president, with the Group Chief Risk Officer (acceptance authority for High risks).
- **Conditions:** (1) replace the shared export bucket for payroll handoff files with a per-recipient, short-lived channel with customer-managed keys, read logging, and 7-day retention by 2026-12-31 (POAM-006, POAM-007); (2) revoke all static keys that can read customer exports and move integrations to short-lived workload credentials by 2026-11-30 (POAM-001); (3) no new AI feature or material AI change without the Group AI Standard gate (POAM-010).
- **Reauthorization:** annually, or when the export channel redesign completes.

### 4.3 System Operational Status
Operational. **Major modification planned:** export channel redesign (gap 2) and workload identity for all integrations (gap 1), both due by 2026-12-31.

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Cloud Software chief technology officer | Accountable for the WCP and this SSP |
| Authorizing official equivalent | Group CISO with the Cloud Software division president | Authorization decision; High risks go to the Group Chief Risk Officer |
| Information security lead | Cloud Software division CISO | Security program for the WCP; SOC 2 and ISO/IEC 27001 |
| Data owner, customer worker data | Each customer (the division is a service provider); represented internally by the Group Chief Privacy Officer | Data-use limits, DPA conformance |
| Data owner, payroll handoff data | Payments and Payroll division (financial institution under 16 CFR Part 314); Qualified Individual is the Payments and Payroll division CISO | Safeguards requirements for the handoff; oversight of the WCP as an affiliate service provider (gap 5) |
| Common control providers | Group identity director (SYS-G1), Group SOC director (SYS-G2), Group cloud platform director and Group engineering platform director (SYS-G3) | Operate inherited controls (`common-control-catalog.csv`) |
| Independent assessor | Group internal audit | Assesses common controls once and samples WCP and division controls (P07) |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1 (human resource management and information security groups). Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Compensation management (pay rates, payroll handoff files with Social Security numbers and bank account details) | **High** | **High** | Moderate | Disclosure of about 2.4 million workers' Social Security numbers and bank details would have a severe effect (breach duties in every state, FTC Safeguards notice, SEC materiality). Tampering with bank details redirects pay. Payroll can tolerate a few hours' delay (P05 BP-SW03) |
| Organization and position management; employee performance management (schedules, time, HR records, attrition scores) | Moderate | Moderate | **Moderate** | Raised from Low availability because shift workers cannot clock in during an outage (P05 BP-SW01, RTO 2 hours) |
| Information security (keys, access policies, logs) | High | High | Moderate | Compromise would expose every tenant |
| **WCP category (high-water mark)** | **High** | **High** | **Moderate** | Overall **High** |

**Baseline:** the NIST SP 800-53B **High** baseline, tailored. The plan documents **187 controls** in `control-implementation.csv`:
- 181 from the High baseline;
- 5 from the privacy baseline (PM-9, PM-10, PT-2, PT-3, RA-8), added because data-use limits are the WCP's main privacy commitment as a service provider;
- 1 control in no baseline (AC-3(7), role-based access control), added because support and consultant access is role-based.

Other High-baseline controls are fully inherited from the cloud providers (most PE controls, evidenced by their SOC 2 Type 2 reports) or tailored out with a reason in the group tailoring register (for example, PE controls for data centers the group does not operate). CSF 2.0 subcategories in the CSV come from the NIST CSF 2.0 to SP 800-53 crosswalk in `00_universal-framework/crosswalks/`; where that crosswalk has no row for a control, the subcategory is an author mapping.

## 7. Authorization Boundary Description
- **Inside:** the WCP accounts in provider A (front ends, API gateway, application services, tenant databases, export service and export bucket, AI services, support and admin console) and the WCP backups in the provider B vault.
- **Outside, inherited (common control providers):** SYS-G1 identity platform, SYS-G2 SOC, SIEM, and EDR, and SYS-G3 (landing zone, hub network, log archive, key management, CI/CD).
- **Outside, interconnected:** SYS-D3 payroll engine (reads handoff files), SYS-D4 payments platform (checkout), SYS-D2 consulting migration toolkit (writes tenant data loads; holds static keys, gap 1), the third-party model provider, about 9,000 third-party payroll providers chosen by customers, and customer identity providers.

The diagram is in P04 `cloud-architecture.md` (section 2.2).

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Agreement |
|---|---|---|---|
| SYS-D3 payroll engine (Payments and Payroll) | Outbound nightly | Payroll handoff files: names, Social Security numbers, bank details, gross pay | **No intercompany service agreement with safeguards terms** (gap 5; CA-3; POAM-020) |
| SYS-D4 payments platform | Embedded checkout (browser posts directly to SYS-D4) | Merchant identifiers only on the WCP side | Intercompany services agreement (2024) |
| SYS-D2 consulting migration toolkit | Inbound and outbound during implementations | Customer HR and payroll data loads; export reads | Internal; **37 static keys with read access to all tenant export prefixes** (gap 1) |
| Third-party model provider | Outbound per request | Prompts with schedule and HR context; no Social Security numbers or bank details (filtered) | Sub-processor agreement with zero-retention terms; listed sub-processor (notice 2026-01-30) |
| Third-party payroll providers (about 9,000) | Outbound | Payroll exports chosen by each customer | Customer instruction; customer-held credentials |
| Customer identity providers | Inbound | Federated sign-in assertions | Customer configuration |
| Group data platform (SYS-G3) | Outbound | De-identified product usage data | Data use catalog; about 3,400 pre-2023 DPAs do not mention this use (gap 4; PT-2) |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| Web, mobile, and API front ends | PaaS (managed load balancing, web application firewall) | Provider A | Cloud Software chief technology officer |
| Application services | Managed containers | Provider A | Cloud Software chief technology officer |
| Tenant databases | Managed relational database (PaaS) | Provider A, replicated to standby region | Cloud Software chief technology officer |
| Export service and export bucket | Containers plus object storage | Provider A | Cloud Software integrations director |
| AI services | Containers; external model API | Provider A; model provider | Cloud Software chief product officer |
| Support and admin console | Internal web application | Provider A | Cloud Software division CISO (access policy) |
| Key management | PaaS (customer-managed keys for databases; provider-managed for the export bucket, gap 2) | Provider A | Group cloud platform director |
| Backups | Immutable backup vault | Provider B | Group cloud platform director |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv` (187 controls) and `common-control-catalog.csv` (142 group common and hybrid controls).

| Status | Controls |
|---|---|
| Implemented | 162 |
| Partially implemented | 25 |
| Planned | 0 |
| Not applicable | 0 |
| **Total** | **187** |

| Inheritance | Controls |
|---|---|
| Common/Inherited (from SYS-G1, SYS-G2, SYS-G3, group functions, or the cloud providers) | 110 |
| Hybrid (group provides the mechanism; the WCP configures or operates part) | 32 |
| System-specific | 45 |

**The 25 partially implemented controls** cluster in five places:
- **Payroll handoff data in the export bucket** (gap 2): AC-3, AC-4, AU-2, AU-6, AU-12, SC-28(1), SI-4, SI-4(4), SI-12.
- **Machine credentials and service identities** (gap 1): AC-2, AC-2(12), IA-5.
- **Consultant access to tenants** (gap 3): AC-6, AC-6(7).
- **AI and data use** (gap 4): CM-4, RA-8, SA-11, PT-2, PT-3.
- **Cross-division agreements, notification, and recovery** (gaps 5 and 7): CA-3, SA-9, IR-3, IR-6, IR-8, CP-4.

### 10.2 Common control inheritance by division
The common control catalog lists 142 controls that corporate provides fully (110) or in part (32). Inheritance is **documented for Cloud Software** (its SOC 2 system description carves in the group services), **for Payments and Payroll** (its PCI DSS responsibility matrix and SOC 1 system description), and for the WCP (this plan). It is **not documented for Technology Consulting** (gap 10). Until POAM-019 closes, consulting cannot show its federal and hospital clients which safeguards come from group controls, and P07 found CA-2 statements other than satisfied for this reason.

### 10.3 Control assessment status
Common controls were assessed once, and WCP and division controls sampled, from 2026-07-06 to 2026-08-28 by group internal audit. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
- **Workforce users** authenticate through SYS-G1 with MFA; **administrators** use phishing-resistant hardware keys and just-in-time PAM elevation. This fits a High-confidentiality system with a remote workforce.
- **Consultants** use the same SYS-G1 identities, except the 2,600 from the acquired firm, who federate from their own identity provider until 2027-03-31 (gap 9).
- **Service identities** should use workload identity with short-lived tokens. 214 WCP service identities still include static keys; 37 belong to the consulting migration toolkit (POAM-001, POAM-002).
- **Customer users** sign in through their own identity provider or WCP accounts. MFA is required for customer administrators and offered to workers. Direct deposit changes require re-authentication (IA-11).

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), group and division risk registers (P01), gap analyses and regulation-by-division matrix (P03), cloud architecture and control map (P04), BIA (P05), group policies and division supplements (P06), assessment and POA&M (P07), incident response runbook and notification matrix (P08), SOC 2 readiness (P09), AI governance (P10).

## 13. Acronym List and Glossary
- **CDE:** cardholder data environment (in SYS-D4, outside this boundary)
- **Common control:** a control provided once by corporate and inherited by several systems
- **DPA:** data processing agreement
- **Export bucket:** the object storage location where the export service writes payroll handoff files and customer exports
- **Handoff file:** the nightly file per embedded-payroll employer that the payroll engine collects
- **PAM:** privileged access management
- **Qualified Individual:** the person responsible for the information security program under 16 CFR 314.4(a)
- **WCP:** Workforce Cloud Platform

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-08-28 | Draft after P07 fieldwork | Cloud Software division CISO |
| 1.0 | 2026-09-17 | Approved with authorization conditions | Group CISO |
