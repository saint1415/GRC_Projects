# Scenario facts: Cris Santos Company | Information | Mid-Market

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, standard, or FTC guidance page, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (privately held; private equity-backed; board with an audit committee) |
| Business | B2B SaaS software publisher (NAICS 513210). Sells a multi-tenant **customer service platform** by subscription: ticketing and agent workspace, email, chat, and messaging channels, a public help center (knowledge base), APIs and integrations, and two generative AI features (AI Assist reply drafting for agents and Answer Bot, a customer-facing chatbot) |
| Location | Headquarters in Florida (about 260 staff). An engineering office in a second U.S. state (about 110 staff). The other staff work remotely from 37 states. An engineering services contractor provides 18 developers in Poland with no production access. All hosting is in the United States |
| Workforce | 600 employees: 210 engineering (including 35 platform engineering and site reliability, and the 6-person security team), 40 product and design, 85 customer support, 70 customer success and professional services, 120 sales and marketing, 75 general and administrative (finance, legal, people, corporate IT). Plus the 18 contractors (EV-003, EV-047) |
| Customers | About 2,400 business customers in all 50 states: retail and e-commerce (about 45%), software and technology (25%), consumer and business services (18%), health care (46 customers, about 2%), financial services (including 9 community banks). About 88,000 named agent users (EV-045) |
| End-consumer data | About 92 million end-consumer contact records (the customers' own customers) with ticket, email, and chat history. About 11 million are California residents and about 6 million are Florida residents, based on customer-supplied location data. The healthcare cell holds about 1.3 million patients' records (EV-025) |
| Revenue | $100.0 million annual receipts (fictional, 2025), about $8.33 million a month or $274,000 a calendar day. 60% from Enterprise plan customers, 40% from Standard plan customers. Not SBA-small (standard $47.0 million for NAICS 513210; 13 CFR 121.201). Source: revenue report (EV-052) |
| Data processed | End consumers' names, email addresses, phone numbers, social messaging handles, ticket and chat content (free text), attachments (images, documents), IP addresses, and satisfaction ratings; agent user accounts. Healthcare edition tickets contain protected health information (PHI). Card numbers pasted into tickets are redacted automatically (default on since 2025; EV-058) |
| Role under privacy and breach laws | For customer data: a **service provider or processor** acting on customers' written instructions under the DPA. For the 46 healthcare customers: a **business associate** under signed BAAs (45 CFR 160.103; the Security Rule applies to business associates, 45 CFR 164.302), determined in the intake obligations register (N62-R01; EV-042). For its own employee, customer contact, and marketing data: the business that owns the data |
| Customer commitments (MSA, DPA, BAA) | **Availability:** Standard plan 99.9% monthly, Enterprise plan 99.95% monthly, with service credits (section 7). **Incident notice:** without undue delay and within 48 hours of confirming a security incident affecting customer data; 24 hours for 38 Enterprise customers with negotiated terms. **BAA:** report security incidents and breaches of unsecured PHI to the covered entity within 10 business days of discovery (shorter than the 60-day outer limit in 45 CFR 164.410(b)). **Sub-processors:** 30 days' advance notice with a right to object. **Deletion:** customer data deleted within 30 days after termination (backups age out within 35 days). **Use:** customer data used only to provide the service and never to train AI models. **Residency:** U.S. hosting only. **Bank customers:** contract terms that mirror the bank service provider notification rule (12 CFR 53.4). Source: contract templates and register (EV-044) |
| Public statements (trust center) | "All customer data is encrypted at rest and in transit." "Customer data is never used to train AI models, and our AI providers do not retain your data." "Our staff can access your account only with your permission, and every access is logged." "We maintain a SOC 2 Type 2 report and support HIPAA compliance for healthcare customers." Captured 2026-07-20 (EV-062) |
| Assurance | SOC 2 **Type 2** (Security and Availability), period 2025-04-01 to 2026-03-31, issued 2026-05-29 by an independent CPA firm: unmodified opinion with **4 exceptions** (EV-038). A bridging Type 2 on the same scope covers 2026-04-01 to 2026-12-31. The 2027 report (calendar year) adds **Confidentiality** and brings the healthcare cell and the AI features into the system description (P09). Annual external penetration test (March 2026) and a public bug bounty program since 2024 (EV-016, EV-017) |
| Cyber insurance | $15 million aggregate limit, $500,000 retention. The carrier's panel supplies breach counsel and forensics. The policy requires notice through the carrier hotline before incident vendors are engaged (EV-048) |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): COPPA (a B2B service, not directed to children under 13); PADFA (not a data broker); FCC CPNI rules (no voice service; not a carrier or interconnected VoIP provider); FedRAMP (no federal customers); SEC disclosure rules (private); PCI DSS (the company bills by a payment processor and does not accept card data in the product; card numbers in tickets are redacted, noted and not assessed); FTC Health Breach Notification Rule (PHI is handled as a business associate under HIPAA) |
| State law approach | Florida law is cited where a Florida duty is unavoidable (Fla. Stat. 501.171, including the 10-day third-party agent notice in 501.171(6)(a); Fla. Stat. 934.03 for call recording). California is cited only for the CCPA applicability check and one verified service-provider breach-notice example. Otherwise state law is treated generically: "each state where affected individuals reside" |

## 2. People (role titles only)

| Role | Security and privacy duties |
|---|---|
| Board audit committee | Quarterly cyber risk reporting; receives P07 results and the POA&M |
| Chief Executive Officer | Accepts High risks; approves the risk appetite, the security budget, and these deliverables |
| Chief Technology Officer (CTO) | **System owner** of the Customer Engagement Platform; executive sponsor of the security program; accepts Moderate risks |
| Chief Financial Officer | Cyber insurance, finance systems, service credits, vendor contracts with the General Counsel |
| General Counsel | Legal and privacy lead; breach determinations and notices; approves public security and AI statements |
| Associate General Counsel, Privacy | DPAs, BAAs, sub-processor notices, CCPA and state privacy questions, customer audits |
| Director of Security | Leads the 6-person security team (3 security engineers, 1 application security engineer, 1 detection engineer, and the Director); designated **HIPAA Security Official** for the business associate (45 CFR 164.308(a)(2)); incident commander. Reports to the CTO, with direct access to the audit committee chair |
| GRC Manager (plus 1 GRC analyst) | SOC 2 program, policies and standards, risk register, vendor risk, evidence collection. Reports to the Director of Security |
| VP Platform Engineering | Cloud landing zone, CI/CD platform, site reliability, backups and disaster recovery; technical recovery lead |
| VP Engineering | Application development, secure development lifecycle, code review |
| VP Product | Product decisions, including the AI features; AI product owner |
| Director of Machine Learning | Builds and evaluates the AI features (prompting, retrieval, evaluations) |
| VP Customer Support | The company's own support team, support access to tenants, customer communications during incidents |
| Director of IT | Corporate IT, the workforce identity provider, endpoints, corporate SaaS |
| VP People | Onboarding, terminations, transfers, training records, sanctions with Legal |
| Chief Revenue Officer | Sales commitments and security questionnaire answers |
| Co-sourced internal audit firm | Annual IT audit; performed the P07 control assessment; reports to the audit committee |
| SOC 2 service auditor (independent CPA firm) | Issues the SOC 2 reports. Not the internal audit firm |
| Managed detection and response (MDR) provider | 24x7 monitoring of endpoints and the identity provider; cloud workloads are not in the contracted scope (EV-029) |
| Outside breach counsel (insurer panel) | Directs incident investigations under privilege; confirms notices |

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv). Suppliers are in [`step-00_P00_intake/vendor-register.csv`](step-00_P00_intake/vendor-register.csv).

| ID | System | Hosting | Holds customer data? | Notes |
|---|---|---|---|---|
| SYS-01 | Production platform (primary U.S. region): container cluster running the web, API, real-time chat, and worker services; managed relational database (12 shards); search cluster; object storage for attachments; message streaming; cache; key management; secrets manager; web application firewall and content delivery; AI orchestration service with a per-tenant vector index | Public cloud provider A, production account | Yes | Multi-tenant. Tenant isolation is enforced in application code and by per-tenant search index names, with shared cluster credentials (EV-018) |
| SYS-02 | Healthcare cell: a separate production account for the 46 healthcare customers, with its own database shard, attachment storage, search cluster, and keys | Public cloud provider A, healthcare production account | Yes (PHI) | Same code release as SYS-01. AI Assist uses the model provider's zero-retention endpoint under a BAA; Answer Bot is not enabled (EV-046) |
| SYS-03 | Disaster recovery (second U.S. region): cross-region database replicas, container images, and infrastructure code ("pilot light") | Public cloud provider A, DR account | Yes (replicas) | Search indexes are not replicated. Backups are kept 35 days but are not write-once (EV-019, EV-020) |
| SYS-04 | Cloud landing zone: 10 accounts (management, security tooling, log archive, network hub, production, healthcare production, DR, staging, development, data analytics) plus 22 engineer sandbox accounts | Public cloud provider A | Varies | Organization guardrails block public storage, unencrypted volumes, and regions outside the U.S. (EV-010) |
| SYS-05 | Source hosting, CI/CD pipelines, artifact registry, and image signing | SaaS | No (holds secrets) | 9 long-lived cloud access keys remain in pipelines and jobs (EV-008) |
| SYS-06 | Workforce identity provider (single sign-on, MFA) and just-in-time privileged access tool | SaaS | No (identities only) | Phishing-resistant security keys for the 190 engineers with production or cloud administrator access (EV-001) |
| SYS-07 | Internal admin console and support tooling (the company's own support team runs on its own platform) | Part of SYS-01 | Yes | "Support view" opens a customer tenant; on the Standard plan it needs only a ticket number (EV-009) |
| SYS-08 | Observability and security monitoring: application logging SaaS, cloud-native SIEM, performance monitoring, uptime monitoring and public status page; MDR provider | SaaS and security tooling account | Yes (incidental) | Cloud audit logs kept 1 year in the log archive account (EV-027) |
| SYS-09 | Messaging delivery: email delivery service, SMS provider, social messaging channel connectors | SaaS | Yes | Outbound replies and notifications to end consumers |
| SYS-10 | Generative AI model provider (API): a standard endpoint (prompts retained 30 days for abuse monitoring) and a zero-retention endpoint covered by a BAA; embeddings model | SaaS | Yes | Used by AI Assist and Answer Bot (P10) |
| SYS-11 | Data warehouse and analytics | SaaS data platform hosted on public cloud provider B | Yes | Nightly load of usage, billing, and ticket metadata, including ticket subject lines from the healthcare cell. Loaded by a job that uses a long-lived provider A key (EV-008, EV-023) |
| SYS-12 | Corporate SaaS and endpoints: 640 laptops (macOS and Windows) with device management, full-disk encryption, and EDR (EV-030); productivity suite, chat, CRM, HR information system, billing with a payment processor; headquarters office network | SaaS and on-premises office network | Incidental | Customer contact data and the company's own employee data |

**Sub-processors listed in the DPA (14):** cloud provider A; the data platform on cloud provider B; content delivery and web application firewall provider; email delivery service; SMS provider; AI model provider; application logging SaaS; error-tracking SaaS; performance monitoring SaaS; status page provider; translation API provider; social messaging connector provider; customer data export service; MDR provider (security logs). Six of them receive healthcare cell data (cloud provider A, email delivery, SMS, AI model provider, logging SaaS, error-tracking SaaS); 4 of those have subcontractor BAAs (EV-041, EV-042).

**Approved AI tools for staff (POL-05 4.8):** an enterprise generative AI coding assistant (AI-004) and a meeting and call summarizer for sales and support calls (AI-005) (EV-056). Customer data and secrets may not be entered except where the approved tools list allows it.

**SSP system (P02):** the *Customer Engagement Platform (CEP)*: the production platform (SYS-01), the healthcare cell (SYS-02), and the DR region (SYS-03), with the components that build, operate, and secure them (SYS-04 landing zone, SYS-05 CI/CD, SYS-06 identity, SYS-07 admin console, SYS-08 monitoring), and interfaces to SYS-09, SYS-10, and SYS-11. Moderate baseline with tailoring.

## 4. Where the evidence is

This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Every item has a source system, an owner, and as-of and collected dates. The SOC 2 Type 2 report and its 4 exceptions are EV-038.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps against FTC Act Section 5, the company's own commitments, the HIPAA Security Rule for the healthcare cell, and business associate breach duties** are judged in the gap analysis (P03); **whether controls work** is tested in the control assessment (P07); **SOC 2 readiness** is checked criterion by criterion in P09. All three cite evidence IDs.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 | All applicable rules for the SaaS business line: FTC Act Section 5 reasonable security (FTC business guidance) and deception (the company's own statements and commitments); HIPAA Security Rule as a business associate for the healthcare cell; HIPAA breach notification duties of a business associate. CCPA, other state privacy laws as a processor, and the DOJ Data Security Program as applicability checks. SOC 2 criteria are covered criterion by criterion in P09 |
| P08 | **Two incident types:** (1) cloud credential compromise exposing customer data: the leaked data warehouse loader key is used to download attachments and query the warehouse; (2) extended platform outage (cloud region failure or destructive attack) that breaches the SLA and triggers bank customer notice. Integrated with crisis management and legal |
| P09 | SOC 2 Type 2 readiness for the 2027 examination period with expanded scope (Confidentiality added; healthcare cell and AI features in the system description), building on the 4 exceptions; sub-processor report review program |
| P10 | AI use-case portfolio: AI-001 AI Assist reply drafting, AI-002 Answer Bot (customer-facing generative chatbot), AI-003 ticket triage and priority classifier, AI-004 engineering coding assistant, AI-005 sales and support call summarizer |
| Cloud | Multi-account landing zone on one primary provider (vendor-agnostic) plus a SaaS data platform on a second provider. Services are described by category, with AWS, Azure, and Google Cloud equivalents only in an equivalents table |
| Registry defaults | Kept as given: the primary system is the multi-tenant SaaS production platform (the CEP), the P08 incident is cloud credential compromise exposing customer data, and the P10 use case is the generative AI feature embedded in the product (AI-001 and AI-002). At this size a second incident type and a portfolio of 5 AI uses were added, as the tier requires |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-05-29 | SOC 2 Type 2 report issued (period 2025-04-01 to 2026-03-31) |
| 2026-06-22 to 2026-07-09 | Intake: evidence requests, exports, inventories, obligations register |
| 2026-07-13 to 2026-08-07 | BIA, risk assessment, and gap analysis fieldwork |
| 2026-08-10 to 2026-08-14 | 2026 policy revisions (POL-01 to POL-05) drafted from the gaps |
| 2026-08-17 to 2026-09-04 | Control assessment fieldwork (co-sourced internal audit firm): operating tests of controls already in place; design review of the draft policies and the draft regional DR plan |
| 2026-09-08 to 2026-09-18 | SOC 2 readiness assessment and AI risk assessment |
| 2026-09-29 | Deliverables and policies approved (CEO for High risks, CTO for Moderate and below); results to the audit committee the same day |
| 2026-10-01 | 2026 policies take effect |
| 2026-11-10 | Incident response tabletop: credential compromise (P08 runbook 1) |
| 2026-12-15 | SOC 2 readiness gates due (P09) |
| 2026-12-31 | End of the bridging Type 2 period (report expected by 2027-02-26) |
| 2027-01-01 to 2027-12-31 | Expanded-scope SOC 2 Type 2 examination period |
| 2027-02-17 | Regional failover exercise and platform outage tabletop (P08 runbook 2) |
| 2027-04 (planned) | Follow-up assessment: operating effectiveness of the controls the 2026 policies and standards introduced, after at least one quarter of operation |

## 7. Operating details (fictional; used across P01-P10)

Each detail below comes from a system of record in the intake evidence register.

| Topic | Fact |
|---|---|
| SLA credits | Measured monthly on core service availability (agent workspace, API, and channel ingestion). Standard plan: 10% of the monthly fee below 99.9%, 25% below 99.0%. Enterprise plan: 5% below 99.95%, 10% below 99.5%, 25% below 99.0%. Credits are capped at 25% a month. In a 30-day month, a full outage of 1 hour costs about $583,000 in credits, 4 hours about $833,000, and 8 hours or more about $2.08 million (the cap). Enterprise MSAs also let a customer terminate if monthly availability falls below 99.0% in 2 consecutive months (EV-044) |
| Revenue forecast | 2026 revenue is forecast at about $112 million (relevant to the CCPA cybersecurity audit schedule, P03) (EV-052) |
| Own-purpose personal data | About 70,000 California consumers in data the company holds for its own purposes (employees, customer contacts, prospects, website visitors identified by cookies); no sensitive personal information beyond its 600 employees' HR data (EV-054) |
| Revenue split | Enterprise plan about $5.0 million a month; Standard plan about $3.33 million a month; the healthcare cell about $0.5 million a month (Enterprise plan) (EV-052) |
| Volumes | About 1.9 million tickets and 650,000 chat conversations a day across all tenants; about 140,000 API calls a minute at peak (EV-026) |
| Workforce activity | 96 terminations and 58 internal transfers in the 12 months to 2026-06-30 (EV-003) |
| Recovery today | Database point-in-time recovery 7 days (RPO about 5 minutes in region); cross-region replica lag under 1 minute; February 2026 regional failover test: 9 hours (EV-019, EV-020) |
| Healthcare cell | Launched November 2025. 46 customers (clinics, dental groups, telehealth, health technology) under BAAs (EV-042) |
| Bank customers | 9 community banks use the platform for customer support; their contracts name a point of contact for incident notice (EV-044, EV-045) |
| Terminology | "Customer Engagement Platform (CEP)" is the SSP system in P02, identifier CSC-CEP-01 |
