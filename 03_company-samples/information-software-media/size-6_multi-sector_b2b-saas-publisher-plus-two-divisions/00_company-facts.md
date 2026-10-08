# Scenario facts: Cris Santos Company | Information | Multi-Sector

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company Holdings, Inc. (publicly traded SEC registrant) |
| Structure | A holding company with three divisions and corporate shared services. Each division is a separate legal subsidiary under common ownership |
| Division 1: Cloud Software (NAICS 513210, sector 51 Information), **focus of this scenario** | Publisher of *Workforce Cloud*, a multi-tenant workforce management and HR SaaS (scheduling, time and attendance, HR records, employee self-service mobile app) sold to mid-size and large employers. About 14,000 employees. About 38,000 customer organizations; about 21 million worker profiles in all 50 states. Acts as a **service provider** (processor) for customer worker data. Issues a SOC 2 Type 2 report each year and holds ISO/IEC 27001 certification |
| Division 2: Technology Consulting (NAICS 541512, sector 54 Professional, Scientific, and Technical Services) | Implementation, integration, and managed application services for Workforce Cloud and for third-party ERP and HR platforms. About 16,000 employees, including about 2,600 who joined with a consulting firm acquired in 2025. About 1,900 client organizations, including 14 federal civilian agency contracts that contain FAR 52.204-21 and 31 hospital and health-system clients for which the division is a HIPAA business associate |
| Division 3: Payments and Payroll (NAICS 522320, sector 52 Finance and Insurance) | Embedded payroll (gross-to-net calculation, payroll tax filing, direct deposit) for about 11,500 employers paying about 2.4 million workers, and embedded card and ACH payment acceptance for about 26,000 merchants (Workforce Cloud customers and their locations). Funds move through two sponsor banks. About 9,000 employees. A PCI DSS service provider; treats itself as a financial institution under the FTC Safeguards Rule (P03) |
| Corporate shared services | Identity, network, cloud platform, CI/CD, security operations, data platform, HR, finance, legal, and internal audit. About 6,000 employees |
| Location | Headquartered in Florida. Employees in 44 states; customers and workers in all 50 states. **State law is handled generically** ("each state where affected individuals reside"), with Florida as the worked example. No offshore hosting; no employees, contractors, or vendors located in a country of concern under 28 CFR Part 202 |
| Workforce / revenue | 45,000 employees; about $18.0 billion annual revenue (fictional) |
| Not in scope by fact | FedRAMP (no government edition of Workforce Cloud; federal clients of the consulting division use other cloud products); COPPA (business service, not directed to children under 13); FCC CPNI rules (not a carrier); DFARS 252.204-7012 and CMMC (no DoD contracts); NYDFS Part 500 (no New York license); no bank charter in the group |
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

## 4. Current security posture: a defined, mostly effective program with gaps at scale
**In place today:**
- Group policies aligned to NIST CSF 2.0, with division supplements, and a common control catalog
- 24x7 group SOC, SIEM, and EDR on all managed endpoints and cloud workloads
- Single sign-on with MFA for all workforce users; phishing-resistant authenticators and just-in-time privileged access for administrators
- Quarterly access certification for group and division applications (except the acquired consulting firm, gap 9)
- Immutable backups in the second cloud provider; tested restores twice a year for the WCP
- Annual external penetration tests and a public bug bounty for Workforce Cloud
- SOC 2 Type 2 for Workforce Cloud (Security, Availability, Confidentiality; 12 months ending September 30) and ISO/IEC 27001 certification
- SOC 1 Type 2 for the payroll service; PCI DSS v4.0.1 Report on Compliance for the payments platform (last validated 2026-05-29)
- Board risk committee oversight; SEC Reg S-K Item 106 disclosure in the annual report

**Gaps found in the 2026 assessments:**
1. **Long-lived machine credentials.** About 1,140 static cloud access keys exist across group cloud accounts; 212 are older than 1 year. The consulting data migration toolkit (SYS-D2) uses 37 static keys that can read the WCP export bucket for any tenant being migrated.
2. **Payroll handoff data sprawl.** Nightly payroll handoff files (worker names, Social Security numbers, bank routing and account numbers, pay data) that the WCP sends to the payroll engine stay in the WCP export bucket for more than 400 days instead of 7. The bucket uses provider-managed keys and has no object-level read logging. Neither division has documented that it owns this data.
3. **Consultant access to customer tenants.** About 3,800 consultants hold "implementation partner" access to customer tenants. Access is granted per project but not removed at project close, and client data is copied into the project collaboration workspace without a retention rule.
4. **AI ahead of governance.** The generative *workforce assistant* (launched 2026-03-02) and the predictive *attrition-risk insights* feature went live before the Group AI Standard (adopted 2026-06-15). Attrition-risk insights has no bias testing and no developer documentation for customers ahead of Colorado SB26-189 (effective 2027-01-01). Group HR is piloting an AI resume screening tool without a CCPA ADMT assessment.
5. **Affiliate service provider oversight.** The WCP processes Payments and Payroll customer information (the handoff files) without an intercompany service agreement that carries 16 CFR 314.4(f) safeguards terms, and the division's written risk assessment does not cover that flow.
6. **PCI DSS scope maintenance.** The six-monthly segmentation penetration test (PCI DSS 11.4.6) was missed in the first half of 2026 after a network change, and the payment page script inventory (6.4.3) is incomplete for 2 of 5 hosted checkout pages.
7. **Notification matrix.** The group matrix does not include FTC Safeguards notices, bank service provider notices for about 420 bank and credit union customers of Workforce Cloud (only 256 have given a designated contact), or the 48-hour customer terms negotiated by about 1,240 enterprise customers. It has never been exercised across divisions.
8. **CCPA cybersecurity audit readiness.** The group meets the cybersecurity audit criteria (Cal. Code Regs. tit. 11, 7120). The first audit period starts 2027-01-01; no auditor or audit scope has been selected.
9. **Acquired consulting firm.** The 2,600 consultants from the 2025 acquisition still use a separate identity provider and endpoint stack (migration due 2027-03-31). Their access is not in quarterly certification and their laptops are not in the group EDR.
10. **Common control inheritance.** Inheritance is documented for Workforce Cloud (SOC 2 system description) and Payments and Payroll (PCI DSS responsibility matrix) but not for Technology Consulting.
11. **Federal contract information.** Federal contract information (FCI) from the 14 federal contracts is stored in the general project collaboration workspace without verification of the FAR 52.204-21(b)(1) controls, and 9 of 22 subcontracts under those contracts lack the 52.204-21(c) flowdown.

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
| 2026-05-04 to 2026-07-31 | Group and division BIAs and risk analyses |
| 2026-06-15 | Group AI Standard adopted |
| 2026-07-06 to 2026-08-28 | Common control assessment (group internal audit) plus division samples |
| 2026-08-03 to 2026-08-28 | Regulatory gap analyses (three divisions and group) |
| 2026-08-31 to 2026-09-11 | SOC 2 readiness (both in-scope service lines) and AI risk assessment |
| 2026-09-17 | Results to the board risk committee; deliverables approved |
| 2026-09-30 | Workforce Cloud SOC 2 Type 2 period ends (2025-10-01 to 2026-09-30) |
| 2026-10-01 | Group policies v2026 effective |
| 2026-12-08 | First cross-division incident tabletop (P08 scenario) |
| 2027-01-01 | CCPA cybersecurity audit period starts; Colorado SB26-189 and CPPA ADMT compliance dates |
| 2027-03-31 | Payments and Payroll platform SOC 2 Type 1 date; acquired firm migration due |

## 7. Facts added while building the deliverables
These facts were added so the deliverables could be completed. They do not change sections 1 to 6.

| Topic | Added fact |
|---|---|
| Revenue split (fictional) | Cloud Software about $9.0 billion; Technology Consulting about $5.4 billion; Payments and Payroll about $3.6 billion (net revenue). Total about $18.0 billion, as in section 1 |
| Risk acceptance | Very Low and Low: division security and compliance lead (division CISO where one exists). Moderate: division president. High: Group Chief Risk Officer with the Group CISO, reported to the board risk committee. Very High: board risk committee only |
| Workforce Cloud data | Worker names, work and personal contact details, employee IDs, job and location, schedules, time punches, pay rates, absences, HR case notes, and (for HR core customers) date of birth and Social Security number. About 1.6 million worker profiles are Florida residents and about 2.3 million California residents (by work location). Time clocks use badges and PINs; no biometric data is collected |
| Payroll handoff | Workers enter direct deposit details in the Workforce Cloud self-service app. Each night the WCP export service writes a handoff file per embedded-payroll employer (names, Social Security numbers, bank routing and account numbers, gross pay data) to the WCP export bucket, and the payroll engine (SYS-D3) collects it. About 2.4 million workers are in scope; about 190,000 are Florida residents |
| Customer commitments | Standard DPA: notice of a security incident affecting customer data without undue delay and within 72 hours of confirmation (about 1,240 enterprise customers negotiated 48 hours); 30 days' notice of new sub-processors; deletion within 90 days after termination; customer data used only to provide the service; CCPA service-provider terms. MSA: 99.95% monthly availability. About 3,400 DPAs signed before 2023 do not mention aggregated or de-identified data use |
| Bank customers | About 420 banks and credit unions use Workforce Cloud for their own staff. Counsel treats the Cloud Software division as a bank service provider for them (12 CFR 53.4, 225.303, 304.24). 256 have provided a bank-designated point of contact |
| Sponsor banks | Sponsor bank A holds the payroll for-benefit-of (FBO) accounts and originates ACH; sponsor bank B sponsors card acceptance. Both contracts require notice to the bank within 24 hours of determining a security incident that affects program data or disrupts program services |
| Money transmission | Outside counsel's state-by-state review of whether the payroll funds flow requires money transmitter licenses started in 2025 and is not complete. The group does not assert a conclusion in these deliverables (P03) |
| FTC Safeguards Rule | The Payments and Payroll division regularly transfers money for workers and merchants. Group legal decided in 2024 to treat the division as a financial institution under 16 CFR 314.2(h) (transferring money is a financial activity; see example 314.2(h)(2)(vi)) and to apply the Part 314 program to all payroll and payment data it handles |
| Federal and health clients | 14 federal civilian agency contracts contain FAR 52.204-21; none designates CUI or contains DFARS clauses. 22 subcontracts sit under them. For the 31 hospital clients, consulting builds nurse-staffing integrations that take EHR census feeds; for 9 of them, patient-level admission, discharge, and transfer (ADT) data passes through test environments. BAAs are signed with all 31 |
| AI use cases | Workforce assistant (generative; 6,200 opt-in customers as of 2026-08-31; third-party hosted model under zero-retention terms; sub-processor notice given 2026-01-30). Attrition-risk insights (predictive; since 2024; used by about 9,800 customers). Schedule optimizer (since 2022). Payments merchant risk and payroll anomaly models. Consulting delivery assistant. Engineer coding assistant. Enterprise generative AI assistant (pilot, 3,000 users). Group HR resume screening pilot (since 2026-05; about 41,000 applicants screened, including California applicants) |
| CCPA cybersecurity audit | The group is a CCPA business (revenue test met). In 2025 it processed personal information of more than 250,000 California consumers as a business (marketing site visitors, event registrants, business contacts, applicants, and its own California workforce), so 7120(b)(2)(A) is met. With 2026 revenue over $100 million, the first audit covers 2027-01-01 to 2028-01-01 and the report is due 2028-04-01 (7121(a)(1)) |
| Cloud | Provider A hosts the corporate landing zone, the WCP (primary and warm standby regions), the export bucket, and the group data platform. Provider B hosts the payroll engine, the payments cardholder data environment (separate accounts), and the immutable backup vault for all divisions. Consulting delivery systems are SaaS plus a small workload in provider A |
| Static key leak path (P08) | Consulting engineers keep migration scripts in personal source repositories against policy; secret scanning covers only group-hosted repositories |
