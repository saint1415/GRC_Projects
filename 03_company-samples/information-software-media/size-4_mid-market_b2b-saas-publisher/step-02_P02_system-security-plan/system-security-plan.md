# System Security Plan: Customer Engagement Platform (CEP)

**Organization:** Cris Santos Company, Inc. (PE-backed B2B SaaS publisher of a multi-tenant customer service platform) | **Tier:** Mid-Market | **Vertical:** Information
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-29

## 1. System Name and Identifier
Customer Engagement Platform (**CEP**), identifier CSC-CEP-01. The CEP is the company's major system and the product it sells. It comprises SYS-01 to SYS-08 in `../00_company-facts.md`.

## 2. System Overview
The CEP is a multi-tenant customer service platform. About 2,400 business customers and their 88,000 agents use it to answer end consumers by email, chat, messaging, and a public help center, with APIs for their own systems and two generative AI features. It supports every customer-facing process in the BIA (P05 BP-01 to BP-08) and holds about 92 million end-consumer contact records, including about 1.3 million patients' records in the healthcare cell.

**Major components:**
| ID | Component | Hosting and service model |
|---|---|---|
| SYS-01 | Production platform in the primary U.S. region: container cluster (web, API, chat, workers), managed relational database (12 shards), search cluster, attachment storage, streaming, cache, key management, secrets manager, WAF and content delivery, AI orchestration with per-tenant vector index | Public cloud provider A, IaaS and PaaS (P04) |
| SYS-02 | Healthcare cell: separate production account for 46 healthcare customers with its own database shard, storage, search, and keys | Public cloud provider A |
| SYS-03 | DR region: cross-region database replicas, images, infrastructure code, 35-day backups | Public cloud provider A |
| SYS-04 | Landing zone: 10 accounts plus 22 sandbox accounts, organization guardrails | Public cloud provider A |
| SYS-05 | Source hosting, CI/CD, artifact registry, image signing | SaaS |
| SYS-06 | Workforce identity provider and just-in-time privileged access tool | SaaS |
| SYS-07 | Internal admin console and "support view" | Part of SYS-01 |
| SYS-08 | Logging SaaS, cloud-native SIEM, performance and uptime monitoring, status page; MDR provider | SaaS and security tooling account |

Messaging delivery (SYS-09), the AI model provider (SYS-10), and the data warehouse on cloud provider B (SYS-11) connect as external services (section 8).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it affects the CEP |
|---|---|---|---|
| N51-R01 | FTC Act Section 5 | 15 U.S.C. 45(a) | Reasonable security for customer and end-consumer data (unfairness), and truthful security, privacy, and AI statements (deception). Main driver in `control-implementation.csv` |
| HIPAA | HIPAA Security Rule, as a business associate | 45 CFR Part 164, Subpart C (164.302 applicability) | Applies to the ePHI the CEP holds for the 46 healthcare customers (SYS-02 and any copies, such as the warehouse feed) |
| HIPAA | Breach notification by a business associate | 45 CFR 164.410 | Notice to the covered entity without unreasonable delay and no later than 60 days after discovery; the BAAs shorten this to 10 business days (P08) |
| N51-R03 | CCPA/CPRA and CPPA regulations | Cal. Civ. Code 1798.100 et seq.; Cal. Code Regs. tit. 11, 7000 et seq. | The company is a service provider for customer data and a business for its own data; the cybersecurity audit question is open (P03) |
| N51-R04 | DOJ Data Security Program | 28 CFR Part 202 | Applicability check for contractor and sub-processor access (P03) |
| Bank customers | Bank service provider notification | 12 CFR 53.4 (OCC), with parallel FDIC and Federal Reserve rules | Notice to bank customers of incidents that disrupt covered services for 4 or more hours (P08) |
| State | Florida Information Protection Act | Fla. Stat. 501.171 | Third-party agent notice to customers within 10 days (501.171(6)(a)); breach notice for company-owned data (P08) |
| Contract | MSA, DPA, BAAs, and SOC 2 | Contracts; AICPA Trust Services Criteria | 99.9% and 99.95% availability; 24- or 48-hour incident notice; 30-day sub-processor notice; 30-day deletion; SOC 2 Type 2 report (P09) |
| Internal | Security policies POL-01 to POL-05 and supporting standards | P06 | Policy basis for every control |

Not applicable:
- **COPPA (N51-R02).** The service is B2B and not directed to children.
- **FCC CPNI rules (N51-R06).** The CEP has no voice service, and the company is not a carrier or interconnected VoIP provider.
- **FedRAMP (N51-R07).** No federal customers.
- **SEC disclosure rules (N51-R08).** The company is privately held.
- **PCI DSS.** The CEP does not accept card payments. Card numbers pasted into tickets are redacted automatically (noted, not assessed).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Chief Technology Officer (system owner) on 2026-09-29, after the control assessment (P07) and before the audit committee meeting the same day.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization to operate. The equivalent internal decision:
- **Decision:** continued operation of the CEP accepted with conditions, 2026-09-29.
- **Authorizing official equivalent:** Chief Executive Officer for High risks; Chief Technology Officer for Moderate and below (P01 acceptance authorities).
- **Conditions:** the High-risk POA&M items in P07 must meet their milestones; the SOC 2 readiness gates in P09 must close by 2026-12-15; the audit committee receives POA&M status each quarter; re-decision by 2027-09-30 or after a major change.
### 4.3 System Operational Status
Operational. Major modifications planned:
- Replace the 9 long-lived cloud access keys with federated short-lived credentials (due 2026-10-31)
- Database-level tenant isolation as a second layer, and per-tenant search credentials (due 2027-03-31)
- Warm standby in the DR region with replicated search snapshots (due 2027-06-30)
- Object-level and database audit logging, and MDR coverage of cloud workloads (due 2026-12-31)

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Chief Technology Officer | Accountable for the CEP; accepts Moderate risk; executive sponsor of the security program |
| Authorizing official equivalent (High risk) | Chief Executive Officer | Accepts High risk; approves the risk appetite |
| Oversight | Board audit committee | Quarterly cyber risk reporting |
| Security official | Director of Security | HIPAA Security Official for the business associate (45 CFR 164.308(a)(2)); day-to-day owner of security controls; incident commander |
| GRC | GRC Manager and GRC analyst | SOC 2 program, policies and standards, risk register, vendor risk |
| Platform owner | VP Platform Engineering | Landing zone, CI/CD, site reliability, backups and DR |
| Application owner | VP Engineering | Application security, tenant isolation, secure development |
| Identity and corporate IT | Director of IT | Identity provider, endpoints, corporate SaaS |
| Privacy and legal | General Counsel; Associate General Counsel, Privacy | DPAs, BAAs, sub-processors, notices, public statements |
| AI product owner | VP Product, with the Director of Machine Learning | AI Assist and Answer Bot (P10) |
| Support access owner | VP Customer Support | Support view use and review |
| Independent assessment | Co-sourced internal audit firm | Annual IT audit; P07 assessment |
| Monitoring | MDR provider | 24x7 monitoring of endpoints and the identity provider |

**Where roles overlap.** The Director of Security reports to the CTO, who is also the system owner and accepts Moderate risks. To compensate, the Director has direct access to the audit committee chair, the co-sourced internal audit firm assesses controls independently (P07), and High risks go to the CEO.

## 6. System Information Types and System Categorization
Information types are company-defined and rated with FIPS 199, following the SP 800-60 Rev. 1 method.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Customer service content (tickets, chats, attachments, end-consumer contact data) | Moderate | Moderate | Moderate | Disclosure across 92 million records would seriously harm customers and the company, but the content is mostly contact data and service requests, not financial account or government ID data; wrong data could misdirect replies; outages are recoverable (P05 MTD 4 hours) |
| ePHI in the healthcare cell | Moderate | Moderate | Moderate | Patient messages to clinics; HIPAA safeguards apply; clinics have phone fallbacks |
| Customer configuration and integration credentials (API tokens, webhook secrets) | Moderate | Moderate | Moderate | Misuse could reach customers' own systems |
| Workforce identities and security logs | Moderate | Moderate | Low | Needed for investigations; short outages tolerable |
| Billing and usage data | Low | Moderate | Low | Recoverable; monthly cycle |
| **CEP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Availability was considered for High.** Most credit exposure falls in the first hour, and the 9 bank customers must be notified at 4 hours. The team kept availability at Moderate because the harm is financial and contractual and is recoverable, not severe or catastrophic. To compensate, the CP controls are tailored to the BIA's 1-hour RTO for the core service (section 10.1).

## 7. Authorization Boundary Description
**Inside the boundary:**
- the production, healthcare production, and DR accounts and all workloads in them;
- the management, security tooling, log archive, network hub, staging, and development accounts;
- the company's tenants and configuration in the identity provider, source hosting and CI/CD, logging SaaS, and SIEM;
- the admin console and support view.

**Outside the boundary (external services, interconnected):**
- cloud provider A's infrastructure and managed services (inherited controls);
- the data warehouse on cloud provider B (SYS-11), which receives a nightly feed;
- the email delivery service, SMS provider, and social messaging connectors (SYS-09);
- the AI model provider (SYS-10);
- the MDR provider's platform;
- customer systems connected through the API and webhooks;
- the 22 engineer sandbox accounts (no customer data; guardrails apply);
- corporate SaaS and laptops (SYS-12), except as access paths.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Customer systems (API, webhooks, single sign-on) | Bidirectional | Tickets, users, events | MSA; DPA; API terms |
| Email delivery service | Outbound and inbound | Replies, notifications, inbound mail | DPA; subcontractor BAA |
| SMS provider | Outbound | Notifications and replies, including healthcare cell messages | DPA; **no subcontractor BAA (gap 8)** |
| Social messaging connector provider | Bidirectional | Messages | DPA |
| AI model provider | Outbound prompts, inbound completions | Ticket text, knowledge base passages | DPA; BAA for the zero-retention endpoint only |
| Data warehouse on cloud provider B | Outbound nightly | Usage, billing, ticket metadata including healthcare cell subject lines | DPA with the data platform; **not covered by a BAA or a data flow approval (gap 3)** |
| Logging SaaS and error-tracking SaaS | Outbound | Application logs and errors that can contain personal data | DPA; subcontractor BAA for logging; **none for error tracking (gap 8)** |
| MDR provider | Inbound telemetry; response actions | Endpoint and identity events | Contract; DPA |
| Engineering services contractor (Poland) | Virtual desktops to source code | Source code; no customer data | Services agreement; **no Data Security Program screening (gap 15)** |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| Container cluster and services | Managed container platform | Production account | VP Platform Engineering |
| Relational database (12 shards) | Managed database | Production account; replicas in DR | VP Platform Engineering |
| Search cluster | Self-managed on virtual machines | Production account | VP Engineering |
| Attachment storage | Object storage | Production account | VP Platform Engineering |
| AI orchestration and vector index | Container service and managed vector store | Production and healthcare accounts | Director of Machine Learning |
| Healthcare cell (database, storage, search, keys) | Same as above | Healthcare production account | VP Platform Engineering |
| Key management and secrets manager | Managed services | Each workload account | Director of Security |
| WAF and content delivery | SaaS edge service | Content delivery provider | VP Platform Engineering |
| Network hub and egress firewall | Network services | Network hub account | VP Platform Engineering |
| Log archive (write-once) | Object storage | Log archive account | Director of Security |
| Posture management, threat detection, SIEM | Security services | Security tooling account and SaaS | Director of Security |
| Backups and replicas | Backup service, replicas | DR account (second region) | VP Platform Engineering |
| CI/CD, artifact registry, signing | SaaS and runners | Source hosting vendor; development account | VP Platform Engineering |
| Identity provider and just-in-time tool | SaaS | Identity vendor | Director of IT |
| Admin console and support view | Application module | Production account | VP Customer Support |
| Engineer laptops (190 with production access) | Endpoint | Remote and offices | Director of IT |

## 10. Control Implementation Details
### 10.1 Control implementation status
**Baseline and tailoring.** The CEP uses the NIST SP 800-53B **Moderate** baseline (287 controls and enhancements), tailored as follows:
- **Documented here: 107 controls** in `control-implementation.csv`. They cover the Moderate controls that implement the FTC guidance practices tested in P03, every SP 800-53 control mapped to a HIPAA Security Rule standard or specification in the repository's HIPAA crosswalk (an author mapping, used here for the healthcare cell), and the controls that address the High risks in P01 (credentials, tenant isolation, monitoring, recovery).
- **Selected by tailoring (added, 5):** CA-8 penetration testing (High baseline), IA-5(7) no embedded unencrypted static authenticators, and SA-3(2) use of live data, because the FTC guidance and the P08 scenario turn on them; PM-9 and PT-2 from the privacy baseline, to support HIPAA risk management and the data-use commitments.
- **Availability tailoring:** CP-2, CP-4, CP-7, CP-9, and CP-10 statements use the BIA's 1-hour RTO for the core service, stricter than a typical Moderate system (section 6).
- **Inherited without separate statements:** the other physical and environmental controls (PE-2, PE-6, PE-8 to PE-17) and platform-level SC controls, inherited from cloud provider A and evidenced by its SOC 2 Type 2 report, reviewed each year (P09 `vendor-soc2-review.csv`).
- **Deferred:** Moderate controls with no FTC, HIPAA, or P01 driver at Moderate or above (for example MA-2 to MA-6, because the company maintains no hardware in the boundary, and AC-18 wireless, because there is no wireless in the boundary). They are recorded as tailoring decisions and reviewed yearly.

**Status of the 107 documented controls:**
| Status | Count |
|---|---|
| Implemented | 50 |
| Partially implemented | 57 |
| Planned | 0 |
| Not applicable | 0 |

**Inheritance of the 107 documented controls:**
| Inheritance | Count | Main providers |
|---|---|---|
| System-specific | 66 | Company |
| Hybrid | 32 | Cloud provider A, identity provider vendor, source hosting and CI vendor, MDR provider, SIEM provider, content delivery provider, sub-processors |
| Common/Inherited | 9 | Identity provider vendor (AC-2(1), AC-7, IA-2, IA-2(1), IA-2(2)), cloud provider A (CP-6, MP-6, PE-3, SC-13) |

The Partially implemented statements trace to the 15 gaps in `../00_company-facts.md` section 4 and to the P07 findings.

### 10.2 Control assessment status
The co-sourced internal audit firm assessed 36 controls from 2026-08-17 to 2026-09-04 (P07 `assessment-plan.md`, `assessment-results.csv`, and `poam.csv`). Weaknesses are tracked in the POA&M and reported quarterly to the audit committee. The SOC 2 service auditor tests the same controls for the Type 2 report (P09).

## 11. Digital Identity Acceptance Statement
- **Workforce.** All workforce users authenticate through the identity provider with MFA from managed devices. Engineers with production or cloud administrator access use phishing-resistant security keys, and production access is just-in-time. This meets the company's authenticator standard (STD-06).
- **Machine identities.** Workloads use provider-issued short-lived roles. The 9 long-lived keys in pipelines and jobs are the exception and are being replaced by federated short-lived credentials by 2026-10-31 (P01 R-001; POAM-002).
- **Customer agents and administrators.** They authenticate with a platform password plus MFA or with their own single sign-on. MFA is enforced for customer administrators and optional for agents. P01 R-017 tracks the plan to require MFA for agents of Enterprise and healthcare tenants by default.
- **End consumers.** They do not sign in. They are identified by email address or chat session, and the platform does not expose account data to them beyond their own conversations.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`); BIA (P05); cloud architecture and control map (P04); risk register (P01); gap analysis and roadmap (P03); policies and standards index (P06); assessment and POA&M (P07); incident runbooks (P08); SOC 2 readiness and vendor reviews (P09); AI governance assessment (P10).

## 13. Acronym List and Glossary
- **BAA:** business associate agreement
- **CEP:** Customer Engagement Platform
- **CI/CD:** continuous integration and continuous delivery
- **DPA:** data processing agreement
- **DR:** disaster recovery
- **EDR:** endpoint detection and response
- **MDR:** managed detection and response
- **MSA:** master subscription agreement
- **MTD, RTO, RPO:** maximum tolerable downtime, recovery time objective, recovery point objective
- **POA&M:** plan of action and milestones
- **SIEM:** security information and event management
- **Support view:** the admin console feature that opens a customer tenant for troubleshooting
- **WAF:** web application firewall

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-08-07 | Draft from the BIA, risk assessment, and gap analysis | GRC Manager |
| 1.0 | 2026-09-29 | Updated with P07 results; approved by the Chief Technology Officer | Director of Security |
