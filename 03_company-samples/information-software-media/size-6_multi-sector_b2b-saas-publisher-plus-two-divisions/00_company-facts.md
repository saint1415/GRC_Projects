# Scenario facts: Cris Santos Company | Information | Multi-Sector

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company Holdings, Inc. (publicly traded SEC registrant) |
| Structure | A holding company with three divisions and corporate shared services. Each division is a separate legal subsidiary under common ownership |
| Division 1: Cloud Software (NAICS 513210, sector 51 Information), **focus of this scenario** | Publisher of *Workforce Cloud*, a multi-tenant workforce management and HR SaaS (scheduling, time and attendance, HR records, employee self-service mobile app) sold to mid-size and large employers. About 14,000 employees. About 38,000 customer organizations; about 21 million worker profiles in all 50 states. Acts as a **service provider** (processor) for customer worker data. Issues a SOC 2 Type 2 report each year and holds ISO/IEC 27001 certification (EV-042). Its duties as a service provider, a bank service provider and an affiliate custodian of payroll data are decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (N51-R01-CS, N51-R03-CS, BSP-NOTICE, N52-R03-CS) |
| Division 2: Technology Consulting (NAICS 541512, sector 54 Professional, Scientific, and Technical Services) | Implementation, integration, and managed application services for Workforce Cloud and for third-party ERP and HR platforms. About 16,000 employees, including about 2,600 who joined with a consulting firm acquired in 2025. About 1,900 client organizations, including 14 federal civilian agency contracts that contain FAR 52.204-21 and 31 hospital and health-system clients for which the division is a HIPAA business associate (obligations register N54-R04, N54-R06) |
| Division 3: Payments and Payroll (NAICS 522320, sector 52 Finance and Insurance) | Embedded payroll (gross-to-net calculation, payroll tax filing, direct deposit) for about 11,500 employers paying about 2.4 million workers, and embedded card and ACH payment acceptance for about 26,000 merchants (Workforce Cloud customers and their locations). Funds move through two sponsor banks. About 9,000 employees. A PCI DSS service provider; treats itself as a financial institution under the FTC Safeguards Rule. Both decided in the obligations register (PCI-DSS, N52-R03-PP) |
| Corporate shared services | Identity, network, cloud platform, CI/CD, security operations, data platform, HR, finance, legal, and internal audit. About 6,000 employees |
| Location | Headquartered in Florida. Employees in 44 states; customers and workers in all 50 states. **State law is handled generically** ("each state where affected individuals reside"), with Florida as the worked example. No offshore hosting; no employees, contractors, or vendors located in a country of concern under 28 CFR Part 202 |
| Workforce / revenue | 45,000 employees; about $18.0 billion annual revenue (fictional) |
| Not in scope by fact | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv). FedRAMP (no government edition of Workforce Cloud; federal clients of the consulting division use other cloud products); COPPA (business service, not directed to children under 13); FCC CPNI rules (not a carrier); DFARS 252.204-7012 and CMMC (no DoD contracts); NYDFS Part 500 (no New York license); no bank charter in the group |
| FAR overhaul clause numbers | Background fact, not scored in P03. Contracts awarded before the contracting agency adopted its FAR Part 40 class deviation keep the clauses this sample cites (FAR 52.204-21, 52.204-23 and 52.204-25) until they are modified. New awards under the deviation carry FAR 52.240-93, which has the same 15 safeguarding requirements as FAR 52.204-21, and FAR 52.240-91, which replaces the separate Kaspersky, Section 889 and FASCSA reports with one report within 72 hours. Sources: SRC-FAR-RFO-PART40 |

## 2. People (role titles only)
| Role | Duties |
|---|---|
| Board risk committee | Group cyber and AI risk oversight; accepts Very High risks |
| Board audit committee | Oversees group internal audit and SEC reporting |
| Group CISO; Group Chief Risk Officer; Group Chief Privacy Officer; Group General Counsel | Group standards, group risk register, common controls, notification matrix |
| Division presidents (3) | Accept Moderate risks for their division |
| Cloud Software division CISO | Division security and compliance lead; system owner representative for the WCP security program; SOC 2 and ISO/IEC 27001 programs |
| Technology Consulting security and compliance lead | Division register and supplement; also the division's HIPAA Security Official for its business associate work |
| Technology Consulting federal contracts compliance officer | FAR 52.204-21 safeguarding and subcontract flowdown |
| Payments and Payroll division CISO | Division security lead and the **Qualified Individual** under 16 CFR 314.4(a); PCI DSS program owner |
| Payments and Payroll chief compliance officer | Sponsor bank oversight, money transmission licensing analysis (with outside counsel), FTC Safeguards notices |
| Group AI council | Approves High-tier AI use cases under the Group AI Standard (P10) |
| Group internal audit | Independent of the teams it assesses (reports to the board audit committee). Assesses common controls once and samples division controls (P07) |
| Disclosure committee | SEC materiality determinations (Form 8-K Item 1.05) |
| External assurance | SOC 2 and SOC 1 service auditor (independent CPA firm); PCI Qualified Security Assessor (QSA); ISO/IEC 27001 certification body |

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv). Suppliers and affiliates are in the [vendor register](step-00_P00_intake/vendor-register.csv).

| ID | System | Owner |
|---|---|---|
| SYS-G1 | Group identity platform (workforce single sign-on, MFA, privileged access management, identity governance) | Corporate |
| SYS-G2 | Group SOC, SIEM, and endpoint detection and response (EDR) | Corporate |
| SYS-G3 | Group cloud platform: landing zones in two public cloud providers (provider A and provider B, vendor-agnostic), source hosting and CI/CD, secrets management, and the group data platform | Corporate |
| SYS-G4 | Corporate SaaS: productivity and collaboration suite, HR information system, ERP and finance | Corporate |
| SYS-D1 | **Workforce Cloud Platform (WCP)**: multi-tenant web and mobile applications, public APIs, tenant databases, the export and integration service (customer payroll and HR exports), and AI services | Cloud Software |
| SYS-D2 | Consulting delivery systems: project collaboration workspace, data migration toolkit, client access gateway; plus the acquired firm's separate identity provider and endpoint management until migration | Technology Consulting |
| SYS-D3 | Payroll engine and tax filing platform | Payments and Payroll |
| SYS-D4 | Payments platform: card and ACH acceptance, tokenization vault, merchant onboarding and risk scoring (the cardholder data environment, in separate cloud accounts) | Payments and Payroll |

**SSP system (P02):** the *Workforce Cloud Platform (WCP)*: the multi-tenant SaaS production platform (SYS-D1) of the Cloud Software division, including its export and integration service and AI services, which inherits group common controls from SYS-G1 to SYS-G3.

## 4. Where the evidence is
This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Rows are grouped by division (Group, Cloud Software, Technology Consulting, Payments and Payroll). Every item has a source system, an owner, and as-of and collected dates.
- **Which rules apply** to each division and to the group is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps** against FTC Act Section 5 and the Workforce Cloud commitments, FAR 52.204-21 and the HIPAA business associate duties, the FTC Safeguards Rule and PCI DSS, and the group-wide rules are judged in the gap analyses (P03), which also number the eleven group gaps cited across this sample, and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 | Cloud Software (focus): SOC 2 Trust Services Criteria with FTC Act Section 5 data security expectations (vertical profile). Technology Consulting: FAR 52.204-21, HIPAA business associate duties, and client commitments. Payments and Payroll: FTC Safeguards Rule (16 CFR Part 314) and PCI DSS v4.0.1. Group-wide: SEC disclosure, CCPA (cybersecurity audit), DOJ Data Security Program, bank service provider notice, state breach laws. A regulation-by-division matrix ties them together |
| P08 | Cloud credential compromise exposing customer data, spanning divisions: a static key from the consulting migration toolkit leaks and is used to read WCP export files, including payroll handoff files that belong to the Payments and Payroll program |
| P09 | SOC 2 scoped per division: Workforce Cloud in scope (existing Type 2); the Payments and Payroll platform prepares its first SOC 2 (Security, Availability, Confidentiality, Processing Integrity); Technology Consulting out of scope, with reasons |
| P10 | Group AI governance program: group standard, division use cases, and the rules that apply to each (FTC Act Section 5, CCPA ADMT, Colorado SB26-189, customer contracts, FAR and HIPAA client terms) |
| Cloud | Shared corporate platform in two providers plus division workloads, vendor-agnostic |
| Registry defaults | Kept. The primary system is the multi-tenant SaaS production platform (the WCP). The incident (cloud credential compromise exposing customer data) was adapted so that it crosses divisions, which is the point of this tier. The AI use case (generative AI feature embedded in the SaaS product) is AI-001, the workforce assistant |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-03-30 to 2026-04-24 | Intake: evidence requests, exports, interviews, inventories, obligations register, grouped by division |
| 2026-05-04 to 2026-07-31 | Group and division BIAs (BIA interviews in May) and risk analyses (risk interviews in June and July) |
| 2026-06-01 to 2026-06-26 | Group policies v2026 drafted from the intake observations and the risks found so far (P06); the Cloud Software supplement was aligned to the drafts on 2026-06-30 |
| 2026-06-15 | Group AI Standard adopted |
| 2026-07-06 to 2026-08-28 | Common control assessment (group internal audit) plus division samples: operating tests of controls in place under the 2025 group policies; the draft v2026 policies were reviewed for design only |
| 2026-08-03 to 2026-08-28 | Regulatory gap analyses (three divisions and group) |
| 2026-08-31 to 2026-09-11 | SOC 2 readiness (both in-scope service lines) and AI risk assessment |
| 2026-09-17 | Results to the board risk committee; deliverables and group policies v2026 approved (policies effective 2026-10-01) |
| 2026-09-30 | Workforce Cloud SOC 2 Type 2 period ends (2025-10-01 to 2026-09-30) |
| 2026-10-01 | Group policies v2026 effective |
| 2026-12-08 | First cross-division incident tabletop (P08 scenario) |
| 2027-01-01 | CCPA cybersecurity audit period starts; Colorado SB26-189 and CPPA ADMT compliance dates |
| 2027-03-31 | Payments and Payroll platform SOC 2 Type 1 date; acquired firm migration due |
| 2027-04 (planned) | Follow-up assessment: operating effectiveness of the controls the v2026 policies introduced, after at least one quarter of operation |

## 7. Facts added while building the deliverables
These facts were added so the deliverables could be completed. They do not change sections 1 to 6.

| Topic | Added fact |
|---|---|
| Revenue split (fictional) | Cloud Software about $9.0 billion; Technology Consulting about $5.4 billion; Payments and Payroll about $3.6 billion (net revenue). Total about $18.0 billion, as in section 1 (FY2025, EV-003) |
| Risk acceptance | Very Low and Low: division security and compliance lead (division CISO where one exists). Moderate: division president. High: Group Chief Risk Officer with the Group CISO, reported to the board risk committee. Very High: board risk committee only |
| Workforce Cloud data | Worker names, work and personal contact details, employee IDs, job and location, schedules, time punches, pay rates, absences, HR case notes, and (for HR core customers) date of birth and Social Security number. About 1.6 million worker profiles are Florida residents and about 2.3 million California residents (by work location). Time clocks use badges and PINs; no biometric data is collected (EV-041) |
| Payroll handoff | Workers enter direct deposit details in the Workforce Cloud self-service app. Each night the WCP export service writes a handoff file per embedded-payroll employer (names, Social Security numbers, bank routing and account numbers, gross pay data) to the WCP export bucket, and the payroll engine (SYS-D3) collects it. About 2.4 million workers are in scope; about 190,000 are Florida residents (EV-044, EV-063) |
| Customer commitments | Standard DPA: notice of a security incident affecting customer data without undue delay and within 72 hours of confirmation (about 1,240 enterprise customers negotiated 48 hours); 30 days' notice of new sub-processors; deletion within 90 days after termination; customer data used only to provide the service; CCPA service-provider terms. MSA: 99.95% monthly availability. About 3,400 DPAs signed before 2023 do not mention aggregated or de-identified data use (EV-039) |
| Bank customers | About 420 banks and credit unions use Workforce Cloud for their own staff. Counsel treats the Cloud Software division as a bank service provider for them (12 CFR 53.4, 225.303, 304.24). 256 have provided a bank-designated point of contact (EV-038, EV-040) |
| Sponsor banks | Sponsor bank A holds the payroll for-benefit-of (FBO) accounts and originates ACH; sponsor bank B sponsors card acceptance. Both contracts require notice to the bank within 24 hours of determining a security incident that affects program data or disrupts program services (EV-063) |
| Money transmission | Outside counsel's state-by-state review of whether the payroll funds flow requires money transmitter licenses started in 2025 and is not complete. The group does not assert a conclusion in these deliverables (P03; EV-038, EV-092) |
| FTC Safeguards Rule | The Payments and Payroll division regularly transfers money for workers and merchants. Group legal decided in 2024 to treat the division as a financial institution under 16 CFR 314.2(h) (transferring money is a financial activity; see example 314.2(h)(2)(vi)) and to apply the Part 314 program to all payroll and payment data it handles (EV-038) |
| Federal and health clients | 14 federal civilian agency contracts contain FAR 52.204-21; none designates CUI or contains DFARS clauses. 22 subcontracts sit under them. For the 31 hospital clients, consulting builds nurse-staffing integrations that take EHR census feeds; for 9 of them, patient-level admission, discharge, and transfer (ADT) data passes through test environments. BAAs are signed with all 31 (EV-054, EV-055, EV-060) |
| AI use cases | Workforce assistant (generative; 6,200 opt-in customers as of 2026-08-31; third-party hosted model under zero-retention terms; sub-processor notice given 2026-01-30). Attrition-risk insights (predictive; since 2024; used by about 9,800 customers). Schedule optimizer (since 2022). Payments merchant risk and payroll anomaly models. Consulting delivery assistant. Engineer coding assistant. Enterprise generative AI assistant (pilot, 3,000 users). Group HR resume screening pilot (since 2026-05; about 41,000 applicants screened, including California applicants). Sources: EV-031, EV-048, EV-093, EV-094 |
| CCPA cybersecurity audit | The group is a CCPA business (revenue test met). In 2025 it processed personal information of more than 250,000 California consumers as a business (marketing site visitors, event registrants, business contacts, applicants, and its own California workforce), so 7120(b)(2)(A) is met. With 2026 revenue over $100 million, the first audit covers 2027-01-01 to 2028-01-01 and the report is due 2028-04-01 (7121(a)(1)) (EV-003, EV-036) |
| Cloud | Provider A hosts the corporate landing zone, the WCP (primary and warm standby regions), the export bucket, and the group data platform. Provider B hosts the payroll engine, the payments cardholder data environment (separate accounts), and the immutable backup vault for all divisions. Consulting delivery systems are SaaS plus a small workload in provider A (EV-019) |
| Static key leak path (P08) | Consulting engineers keep migration scripts in personal source repositories against policy; secret scanning covers only group-hosted repositories (EV-081, EV-025) |
