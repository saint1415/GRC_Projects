# Scenario facts: Cris Santos Company | Information | Small

All 11 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a regulation, standard, or FTC guidance page, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (privately held; the majority owner is the Chief Executive Officer) |
| Business | B2B SaaS software publisher (NAICS 513210). Sells a multi-tenant workforce scheduling and timekeeping platform to mid-size businesses in retail, hospitality, and logistics |
| Location | Florida. One office; about a third of staff work remotely from other U.S. states. No offshore staff, contractors, or hosting |
| Workforce | 60 employees: 3 executives, 21 engineering (including platform engineering), 5 product and design, 10 customer support, 5 customer success and implementation, 10 sales and marketing, 6 finance, people operations, and IT |
| Customers | About 310 customer organizations (typically 100 to 1,500 employees each) in 46 states. About 140,000 active worker profiles, of which about 18,000 are Florida residents and about 9,500 are California residents (per customer-provided work location) |
| Revenue | $28.2 million annual receipts (fictional), about $77,000 per calendar day. Under the SBA standard of $47.0 million for NAICS 513210, so SBA-small |
| Data processed | Customer employees' (workers') names, work email and mobile phone numbers, employee ID, job role, work location, availability, schedules, time punches and hours worked, pay rates, and optional preferred language; login credentials (salted, hashed passwords) for workers who sign in with a platform account. **No** Social Security numbers, health data, geolocation, or payment card data (customers are billed through a payment processor) (EV-045) |
| Role under privacy and breach laws | For customer worker data: a **service provider** acting on customers' written instructions under the DPA (the customer owns the data). For its own employee data, customer administrator and billing contacts, and prospect data: the business that owns the data |
| Customer commitments (MSA and DPA) | 99.9% monthly availability SLA with service credits; notice of a security incident affecting customer data without undue delay and within 72 hours of confirmation (3 enterprise customers negotiated 48 hours); 30 days' advance notice of new sub-processors with a right to object; deletion of customer data within 90 days after termination; customer data used only to provide the service; SOC 2 report available under NDA; CCPA service-provider terms (EV-038) |
| Public statements | The website security page states that customer data is encrypted, that "access to customer data is limited to authorized personnel and every access is logged," and that "we never use your data for anything other than running your schedules" (page captured 2026-08-12, EV-049) |
| Assurance | SOC 2 **Type 1** (Security and Confidentiality), as of 2026-02-28, issued 2026-03-27 by an independent CPA firm: unmodified opinion with **3 exceptions** (EV-030). SOC 2 **Type 2** (Security, Availability, Confidentiality) observation period planned for 2026-11-01 to 2027-04-30 |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): HIPAA and the FTC Health Breach Notification Rule (no health data); PCI DSS (no card data); COPPA (a B2B service used by employers and their adult and teen workers, not directed to children under 13); FCC CPNI rules (not a carrier); FedRAMP (no federal customers); SEC disclosure rules (private); bank service provider notification rules (no banking customers) |
| State law approach | Florida law is cited where a Florida duty is unavoidable (breach notification, Fla. Stat. 501.171). California is cited only for the CCPA applicability check and one verified breach-notice example, because customers' California workers are covered by service-provider contract terms. Otherwise state law is treated generically: "each state where affected individuals reside" |

## 2. People (role titles only)

| Role | Security and privacy duties |
|---|---|
| Chief Executive Officer (majority owner) | Accepts High and Very High risks; approves the security budget and these deliverables; approves customer-facing security statements |
| Chief Technology Officer (CTO) | System owner of the WSP; accepts Moderate risks; owns engineering and the AI assistant |
| Chief Operating Officer (COO) | Contracts, DPAs, sub-processor agreements, cyber insurance, finance; designated **privacy lead** |
| IT Manager | **Security and compliance lead** (part-time security duties). Runs the identity provider, endpoints, corporate SaaS, the SOC 2 program, and the policy set; accepts Low risks |
| Platform Engineering Lead | Cloud accounts, CI/CD, infrastructure as code, backups, on-call rotation; technical lead for incidents |
| Engineering Manager | Application development, code review, secure development practices |
| Director of Product | Product decisions, including the AI assistant; co-approves AI features with the CTO |
| Customer Support Manager | Support team and tooling; customer communications during incidents |
| People Operations Manager | Onboarding, terminations, transfers, training records |
| Outside privacy counsel (retainer) | Breach notification and contract advice |
| SOC 2 service auditor (independent CPA firm) | Issued the Type 1; engaged for the Type 2 |
| Independent assessor (contracted) | Performed the P07 control assessment; not the service auditor and not involved in operating the controls |

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv).

| ID | System | Hosting | Holds customer worker data? | Notes |
|---|---|---|---|---|
| SYS-01 | WSP production environment: web application, mobile API, background workers (notifications, payroll exports), AI service, managed relational database, object storage (payroll export files), cache, message queue, key management, secrets manager | Public cloud, production account, one primary region (vendor-agnostic) | Yes | Multi-tenant. Tenant isolation is enforced in the application (every query scoped by tenant ID, EV-054). Database point-in-time recovery for 7 days; daily snapshots copied to a second region (EV-015) |
| SYS-02 | Staging and development environment | Public cloud, separate account | Yes (copies) | Refreshed monthly from a production snapshot without masking; all 21 engineers have write access (EV-005, EV-017) |
| SYS-03 | Source repository and CI/CD pipeline | SaaS source hosting and CI service | No (holds secrets) | Deploys to production with long-lived static cloud access keys stored as CI secrets (2 keys older than 1 year) (EV-005, EV-009) |
| SYS-04 | Identity provider (single sign-on and MFA) | SaaS | No (identities only) | Protects the cloud consoles, repository, support tools, and corporate SaaS. Hardware security keys for the 6 engineers with production access (EV-001) |
| SYS-05 | Customer support tooling: support ticketing and chat SaaS, plus the platform's internal admin console | SaaS; admin console is part of SYS-01 | Yes | The admin console's "view as tenant" feature lets any of the 10 support agents open a customer tenant without customer approval (EV-010) |
| SYS-06 | Observability: logging and monitoring SaaS; uptime monitoring | SaaS | Yes (incidental) | Application logs include worker names and phone numbers in some error messages; 30-day retention (EV-021) |
| SYS-07 | Notification delivery: email delivery service and SMS provider | SaaS | Yes | Shift reminders and swap requests to workers |
| SYS-08 | Generative AI model provider (API) | SaaS | Yes | Used by the AI assistant (P10); added in June 2026 (EV-036, EV-040) |
| SYS-09 | Corporate SaaS: productivity suite, chat, HR information system, CRM, finance with a payment processor for customer billing | SaaS | Incidental | Customer contacts and the company's own employee data |
| SYS-10 | Endpoints: 60 company laptops (macOS and Windows) plus 6 spares | Company-managed | Incidental (cached) | Device management, full-disk encryption, endpoint detection and response (EDR) (EV-024) |

**Sub-processors listed in the DPA (6):** the cloud provider (SYS-01, SYS-02), the logging and monitoring SaaS (SYS-06), the email delivery service and the SMS provider (SYS-07), the support SaaS (SYS-05), and the AI model provider (SYS-08) (EV-038, EV-040).

**Approved AI tools (POL-05 4.8):** one company-licensed generative AI assistant for staff drafting and code assistance (AI-003 in P10), with no training on inputs (EV-036, EV-037). Customer data and secrets may not be entered unless the approved tools list allows it.

**SSP system (P02):** the *Workforce Scheduling Platform (WSP)*: the multi-tenant production environment (SYS-01) and the components that build, operate, and support it (SYS-03, SYS-04, the SYS-05 admin console, SYS-06), with interfaces to SYS-07 and SYS-08. The staging environment (SYS-02) is a connected system in scope because it holds copies of production data.

## 4. Where the evidence is

This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Every item has a source system, an owner, and as-of and collected dates.
- **Which rules and commitments apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps against FTC Act Section 5 expectations and the company's own commitments** are judged in the gap analysis (P03), and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 | Gap analysis against FTC Act Section 5 data security expectations (FTC business guidance) and the company's SOC 2 service commitments. CCPA and the DOJ Data Security Program as applicability checks only |
| P08 incident | Cloud credential compromise exposing customer data: a leaked long-lived CI/CD cloud access key used to read payroll export files and copy a database snapshot |
| P09 SOC 2 | SOC 2 Type 2 readiness (Security, Availability, Confidentiality), building on the 3 Type 1 exceptions; audit readiness checklist, evidence calendar, and sub-processor report reviews |
| P10 AI | Generative AI assistant embedded in the product: AI-001 schedule summaries and AI-002 shift-swap suggestions |
| Cloud | Vendor-agnostic. Services are described by category, with AWS, Azure, and Google Cloud equivalents noted only where needed for shared responsibility |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-02-28 | SOC 2 Type 1 report date (issued 2026-03-27) |
| 2026-07-15 | AI assistant beta released to 40 customers |
| 2026-07-27 to 2026-08-07 | Intake: evidence requests, exports, documents, inventories, obligations register |
| 2026-08-10 to 2026-08-21 | BIA interviews, risk assessment and gap analysis fieldwork |
| 2026-08-24 to 2026-08-28 | Policies drafted from the gaps |
| 2026-08-31 to 2026-09-04 | Control assessment fieldwork (independent assessor): operating tests of controls already in place; design review of the draft policies |
| 2026-09-08 to 2026-09-11 | SOC 2 Type 2 readiness assessment and AI risk assessment |
| 2026-09-22 | Deliverables and policies approved by the Chief Executive Officer (High risks) and the CTO (Moderate and below) |
| 2026-10-31 | SOC 2 Type 2 readiness gates due (P09) |
| 2026-11-18 | First incident response tabletop exercise (P08 scenario) |
| 2026-11-01 to 2027-04-30 | Planned SOC 2 Type 2 observation period (report expected by 2027-06-30) |
| 2027-01 (planned) | Follow-up assessment: operating effectiveness of the controls the new policies introduced, after at least one quarter of operation |
