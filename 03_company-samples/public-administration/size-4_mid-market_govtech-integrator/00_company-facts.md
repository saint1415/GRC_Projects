# Scenario facts: Cris Santos Company | Public Administration | Mid-Market

All 10 deliverables in this folder use the facts below. The company is fictitious, and so are its agency customers. This scenario is independent of the other sizes. Where a fact comes from a regulation, policy, or standard, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (a privately held, private equity-backed GovTech systems integrator; not a government entity) |
| Business | GovTech systems integrator (NAICS 541512, Computer Systems Design Services) with three lines: (1) the hosted **Agency Case Management Cloud (ACMC)**, a configurable case management service for state and local agencies (about 55% of receipts); (2) implementation, integration, and data migration services (about 30%); (3) **application managed services**: remote administration, monitoring, and patching of case and records systems that agencies host on their own premises (about 15%) |
| Ownership and governance | Private equity sponsor holds a majority stake. Board of directors with an audit committee that receives cyber risk reports each quarter |
| Location | Florida. Headquarters office (executives, engineering, cloud operations, security) and a second Florida office, the delivery center (implementation, support, managed services). About 40% of staff work remotely from 9 states. All work, including all support and administration of agency data and agency systems, is performed in the United States |
| Workforce | 600 employees: 30 executives and directors; 180 software engineers and quality analysts; 40 cloud operations and site reliability engineers; 55 managed services engineers; 150 implementation consultants, business analysts, data migration specialists, and trainers; 45 customer support staff; 9 security and GRC staff; 16 corporate IT staff; 10 data and AI staff; 65 corporate staff (finance, HR, legal, contracts, sales) |
| Revenue | About $100 million a year (fictional): ACMC subscriptions and hosting about $55 million, delivery services about $30 million, managed services about $15 million. Over about 250 business days that is about $400,000 per business day ($220,000 ACMC, $120,000 delivery, $60,000 managed services). Above the SBA standard of $34.0 million for NAICS 541512 (13 CFR 121.201), so **not small** |
| Customers | 44 agency customers (43 live, 1 contracted) in Florida and three other states (see the customer table below). About 3.1 million individuals have records in the ACMC |
| Regulatory status | The company is a **private contractor**. The federal data-owner rules bind the agencies directly and reach the company **through its contracts**: IRS Publication 1075 through Exhibit 7 contract language (26 CFR 301.6103(n)-1), the FBI CJIS Security Policy through the CJIS Security Addendum (28 CFR 20.33(a)(7)), Medicaid and SNAP confidentiality rules (42 CFR 431.300-431.307; 7 CFR 272.1(c)) through contract confidentiality terms, the Driver's Privacy Protection Act (18 U.S.C. 2721-2725) through the motor vehicle data terms in the AG-04 contract, and Florida Rule 60GG-2, F.A.C. through the security terms Florida state agencies must put in IT contracts (Fla. Stat. 282.318(4)(h); Rule 60GG-2.001(3)(b)). Every agency contract requires the NIST SP 800-53 Rev. 5 Moderate baseline for the ACMC |
| Florida data security duty | The company is a "third-party agent" of its Florida agency customers under Fla. Stat. 501.171(1)(h). It must take reasonable measures to protect personal information (501.171(2)), notify the agency of a breach no later than 10 days after determining it (501.171(6)(a)), and dispose of customer records securely when they are no longer to be retained (501.171(8)) |
| Not in scope | HIPAA: no customer has designated the company a business associate. AG-03 confirmed in writing that its eligibility case functions sit outside its HIPAA health care component under its hybrid-entity designation (45 CFR 164.105). Election systems: none. Federal contracts (FAR 52.204-21, 52.204-25): none. SLCGP: no grant funds pay for company services. CIRCIA: proposed rule only. Payment cards: agency payments run through each agency's own payment processor, outside the ACMC |
| State law approach | Florida law is cited where a Florida duty is unavoidable (Rule 60GG-2 and Fla. Stat. 282.318 for state agency contracts, Fla. Stat. 282.3185 and 282.3186 for local government customers, and Fla. Stat. 501.171). Customers in State B and State C, and individuals who live outside Florida, are handled generically: "the law of each state where the agency sits or affected individuals reside", confirmed by counsel. Colorado is named only for the Colorado automated decision-making law (SB26-189) that applies to the AG-44 contract |
| FAR overhaul clause numbers | Background fact, not scored in P03. Contracts awarded before the contracting agency adopted its FAR Part 40 class deviation keep the clauses this sample cites (FAR 52.204-21, 52.204-23 and 52.204-25) until they are modified. New awards under the deviation carry FAR 52.240-93, which has the same 15 safeguarding requirements as FAR 52.204-21, and FAR 52.240-91, which replaces the separate Kaspersky, Section 889 and FASCSA reports with one report within 72 hours. Sources: SRC-FAR-RFO-PART40 |

**Agency customers (fictional)**

| ID | Customer | Use of company services | Regulated data | How requirements reach the company |
|---|---|---|---|---|
| AG-01 | A Florida state revenue agency | ACMC tax compliance casework (audit follow-up, collections, taxpayer correspondence) in the **FTI enclave**, a dedicated cloud account. In production since 2022 | **Federal tax information (FTI)** received by the agency under IRC 6103(d), plus state tax data. About 1.2 million taxpayer case records | Contract with Pub. 1075 Exhibit 7 language; the agency's IRS 45-day notification (2022, updated 2025) names the company and its cloud provider (Pub. 1075 Exhibit 6; 26 CFR 301.6103(n)-1); SP 800-53 Moderate; Rule 60GG-2 contract terms |
| AG-02 | A Florida county sheriff's office | ACMC pretrial, probation, and jail program case management, plus **managed services** for the sheriff's on-premises records management system (RMS) and jail management system servers | **Criminal justice information (CJI)**, including criminal history record information (CHRI). About 140,000 supervision and program case records; the RMS holds the sheriff's incident and arrest records | Contract with the CJIS Security Addendum (28 CFR 20.33(a)(7)); CJIS Security Policy v6.1 (06/25/2026); SP 800-53 Moderate |
| AG-03 | A Florida state human services agency | ACMC statewide application intake and verification workflow for SNAP, TANF, and Medicaid, and the **AI eligibility assistant** (AI-001) in 3 of 6 regions | Applicant and household data, Social Security numbers, income documents. About 610,000 applicant households. **FTI is prohibited** in this tenant | Contract confidentiality terms reflecting 7 CFR 272.1(c) (SNAP) and 42 CFR 431.300-431.307 (Medicaid); SP 800-53 Moderate; Rule 60GG-2 contract terms |
| AG-04 | A Florida county tax collector's office | ACMC motor vehicle title and registration casework (title problems, registration holds, dealer complaints) | **Motor vehicle record personal information** (names, addresses, driver license numbers, some photographs) from the state motor vehicle database. About 290,000 case records | Contract terms that apply the state motor vehicle agency's data-access agreement and the DPPA: use only for the agency's functions (18 U.S.C. 2721(b)(1)), no redisclosure (2721(c)); SP 800-53 Moderate |
| AG-05 to AG-38 | 34 Florida counties and cities | ACMC constituent services, code enforcement, permitting complaints, and local business tax cases. 7 of them (AG-08 to AG-14) also buy managed services for on-premises permitting and finance systems | Names, addresses, phone numbers, some driver license numbers in complaint files. About 700,000 constituent records | Contract security terms (SP 800-53 Moderate by reference) |
| AG-39 | A county sheriff's office in **State B** | ACMC probation case management. Live since 2025 | CJI including CHRI. About 38,000 case records | CJIS Security Addendum through State B's CJIS Systems Agency; SP 800-53 Moderate; State B procurement policy requires GovRAMP verification |
| AG-40 to AG-43 | 4 counties and cities in **State B** and **State C** | ACMC constituent services and permitting | Constituent records. About 120,000 | Contract security terms; State B contracts require GovRAMP **Authorized** status by 2027-06-30 |
| AG-44 | A **Colorado** county department of human services | Contract signed 2026-06-15 for benefits intake workflow and the AI eligibility assistant. Go-live planned 2027-04-05. **No data in the ACMC yet** | Will hold applicant and household data | Contract; Colorado SB26-189 (automated decision-making technology), effective 2027-01-01, as the developer of AI-001 (P10) |

**Why FTI is prohibited in the AG-03 tenant.** Human services agencies that receive FTI under IRC 6103(l)(7) "may not contract for services that involve the disclosure of FTI to contractors or sub-contractors" (Pub. 1075 section 2.C.11.2; Exhibit 6). The AG-03 contract therefore forbids FTI in the platform. The agency keeps IRS income match results in its own eligibility system.

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Board audit committee | Quarterly cyber risk reporting; receives the P01, P07, and P09 results |
| Chief Executive Officer | Accepts High risk; approves the risk appetite, the security budget, and High-tier AI use cases |
| Chief Operating Officer | Executive sponsor of the security program; accepts Moderate risk; chairs the crisis management team |
| Chief Technology Officer | **System owner** of the ACMC; approves the SSP and accepts operation of the ACMC |
| Chief Financial Officer | Cyber insurance, budget, and cash-flow decisions in incidents |
| General Counsel | Legal lead for incidents, agency notices, and AI law; engages outside breach counsel |
| Virtual CISO (vCISO, part-time contractor) | Program strategy; board and audit committee reporting; owns POL-01 |
| Director of Information Security | **Information Security Officer**; the security point of contact named in agency contracts; runs the program day to day |
| Security Operations Manager plus 3 security engineers | Security operations, MDR liaison, vulnerability management, incident commander |
| GRC Manager plus 2 GRC analysts | Risk register, SSP, gap analysis, POA&M, SOC 2 and GovRAMP evidence |
| Director of Contracts and Compliance | Privacy and contract compliance lead. Tracks every agency security term (Exhibit 7, CJIS Security Addendum, DPPA terms, Rule 60GG-2 terms); owns notices to agencies |
| VP of Engineering | Owns the ACMC code, the software development life cycle, and change management |
| Director of Cloud Operations | Operates the cloud landing zone: infrastructure, backups, logging, patching, on-call |
| Director of Managed Services | Owns the remote administration of agency-hosted systems and the remote management platform (SYS-10) |
| VP of Customer Delivery | Implementations, data migrations, and agency training |
| Director of Customer Support | 24x7 service desk and agency status communications |
| HR Director (with a Personnel Security Coordinator) | Screening, onboarding, transfers, and terminations; coordinates fingerprint-based checks and Pub. 1075 background investigations through agency customers |
| Director of Data and AI | Owns the AI eligibility assistant (AI-001) and the AI inventory (P10) |
| IT Director | Corporate IT: offices, laptops, productivity suite |
| Internal audit (co-sourced firm) | Annual IT audit; performs the P07 control assessment; reports to the audit committee |
| Managed detection and response (MDR) provider | 24x7 monitoring of the cloud control plane, identity provider, endpoints, and firewalls |
| Agency security contacts (customer roles) | AG-01 disclosure officer; AG-02 local agency security officer; AG-03 information security manager; AG-04 records custodian; AG-39 terminal agency coordinator; IT contacts for the other agencies |

## 3. Systems

| ID | System | Hosting | Holds agency data? | Notes |
|---|---|---|---|---|
| SYS-01 | ACMC application tier, production | Company cloud, production account (IaaS/PaaS) | Yes | Multi-tenant web application on a managed container service, message queue, and object storage for documents. U.S. region A, 3 availability zones |
| SYS-02 | ACMC data tier | Company cloud: production account and the **FTI enclave** account | Yes (FTI, CJI, benefits, motor vehicle, constituent data) | Managed relational database clusters: a "regulated tier" cluster for AG-02, AG-03, AG-04, and AG-39 with customer-managed keys; a shared cluster for municipal tenants; and a dedicated instance for AG-01 in the separate FTI enclave account with its own key and administrator group. Cross-region read replicas in U.S. region B |
| SYS-03 | Integration hub | Production account | Yes (in transit) | Managed file transfer from AG-01, message-switch connectors for AG-02 and AG-39, an API link to AG-03's eligibility system, and the motor vehicle data feed for AG-04 |
| SYS-04 | Workforce identity provider and privileged access management | SaaS | No (identities only) | Single sign-on with MFA for all staff. Just-in-time elevation for cloud administrator roles |
| SYS-05 | Agency user sign-in | Part of SYS-01 | No (identities only) | AG-01, AG-02, AG-03, AG-04, and AG-39 federate with their own identity providers (agency-enforced MFA). Municipal customers use platform-local accounts |
| SYS-06 | Cloud landing zone | Public cloud, 8 accounts | Varies | Management, security tooling and log archive, shared services (network hub, privileged access gateway), production, FTI enclave, staging, development, and backup accounts |
| SYS-07 | Source code repositories and CI/CD pipeline | SaaS | No (code and secrets) | Builds and deploys SYS-01 to SYS-03 through infrastructure as code; signed container images since 2025 |
| SYS-08 | Analytics and agency reporting service | Production account (managed data warehouse) | Yes (replicated tenant data, **FTI excluded by design**) | Agency dashboards and scheduled reports |
| SYS-09 | AI eligibility assistant (feature of SYS-01) | Production account plus the cloud provider's managed large language model service | Yes (AG-03 applicant data) | AI-001 in P10. In production for AG-03 in 3 of 6 regions since 2025-11 |
| SYS-10 | Remote management and privileged access platform for managed services | SaaS remote management service plus jump servers inside 9 agency networks | Yes (sessions into agency systems, including AG-02's CJI systems) | Used by 55 managed services engineers. **Outside the ACMC boundary** |
| SYS-11 | Corporate IT | SaaS productivity suite; 2 office networks; 640 company laptops | Incidental | Laptops have full-disk encryption, EDR, and mobile device management. 120 of them are administrator and support laptops with production access |
| SYS-12 | Security monitoring | SaaS SIEM operated with the MDR provider | Yes (log content) | Cloud control plane, identity provider, EDR, and firewall logs. 1 year searchable; cloud audit logs also archived 7 years in the log archive account |
| SYS-13 | Support ticketing and customer portal | SaaS | Restricted by design | Attachments from regulated tenants are blocked since 2025; regulated cases use in-platform secure support |
| SYS-14 | Backups | Backup account, U.S. region B | Yes | Daily database snapshots copied to a backup vault with 35-day write-once retention and separate administrator credentials; point-in-time recovery (5-minute granularity) in production |
| SYS-15 | Third parties | Various | Some | About 85 vendors; 22 have access to agency data or agency systems |

The cloud provider is described by service category only (vendor-agnostic). The services the company uses are FedRAMP Moderate authorized and run in U.S. regions (checked on the FedRAMP Marketplace in June 2026), as Pub. 1075 section 3.3.1 requires for FTI.

**SSP system (P02):** the *Agency Case Management Cloud (ACMC)*: SYS-01, SYS-02, SYS-03, SYS-05, SYS-06, SYS-08, SYS-09, and SYS-14, with the supporting services that administer them (SYS-04, SYS-07, SYS-12, and the 120 administrator and support laptops in SYS-11). Moderate baseline with tailoring and inherited controls.

## 4. Current security posture: defined program with gaps in scale

**In place today:**
- A security program with a vCISO, a Director of Information Security, a security operations team, and a GRC team; 5 policies adopted in 2024
- Single sign-on with MFA (push with number matching) for all workforce accounts; phishing-resistant security keys for the 40 cloud administrators
- Just-in-time elevation for cloud administrator roles in the production account
- 24x7 managed detection and response for the cloud control plane, identity provider, endpoints, and firewalls
- Separate FTI enclave account for AG-01 with a dedicated database, customer-managed key, and its own administrator group
- Encryption in transit (TLS 1.2 or higher) and at rest (AES-256); customer-managed keys for the regulated tier
- Write-once backups in a separate backup account and second U.S. region
- Weekly authenticated vulnerability scanning of cloud workloads; container image and dependency scanning; signed container images
- Annual external penetration test (last 2026-03)
- Annual risk assessment (last 2025-07) and annual internal IT audit by the co-sourced firm
- Annual security awareness training; CJIS and FTI training for designated staff
- FedRAMP Moderate authorized cloud services in U.S. regions only
- A SOC 2 Type 1 report on the ACMC (Security and Availability) as of 2025-12-31, and GovRAMP Ready status (2025)
- A cyber insurance policy with a breach hotline and panel vendors

**Missing or weak, found in the 2026 assessments:**
1. **Managed services remote access.** The remote management platform (SYS-10) holds standing domain administrator credentials for 9 agencies' on-premises systems, including AG-02's CJI systems. Managed services engineers use push MFA, not phishing-resistant MFA. Sessions are not recorded, and the platform's logs do not reach the SIEM.
2. **Screening has not kept up with hiring.** 186 staff hold CJI access, but 15 of them (implementation consultants and engineers assigned since April 2026) still have fingerprint-based checks or Security Addendum certifications pending. 64 staff hold FTI enclave access, 3 of them with Pub. 1075 background investigations pending, and 7 are overdue for annual FTI disclosure awareness recertification.
3. **Tenant access reviews are annual.** Cloud administrator access is reviewed quarterly, but support and delivery staff access to agency tenants is reviewed only once a year (last 2026-01). Access is not removed when a project closes.
4. **No detection of inappropriate access to regulated records.** Application audit logs (record views, searches, and exports in the FTI, CJI, motor vehicle, and benefits tenants) stay in the application database and are not sent to the SIEM. There is no analytics for unauthorized inspection of FTI or misuse of CJI.
5. **Recovery is designed but not proven at scale.** The largest tenant restore (2025-11 test) took 14 hours against the 8-hour contract recovery time. Region B failover has never been tested. Document object storage is versioned but not in the write-once vault. The 2024 contingency plan predates the landing zone redesign.
6. **FIPS 140-3 is incomplete on CJI paths.** The ACMC web ingress moved to FIPS 140-3 certified modules in 2026-06, but the integration hub's message-switch connectors for AG-02 and AG-39 and the SYS-10 agents still use libraries that do not run in a validated mode. CJIS will not accept FIPS 140-2 certificates after 2026-09-21 (CJISSECPOL v6.1 SC-13).
7. **Vendor reviews lag.** Only 9 of the 22 vendors with access to agency data or systems were reviewed in the last 12 months. The remote management platform vendor has not been reviewed since 2023.
8. **Standards are thin.** The 2024 policies exist, but there are no written standards for remote administration of agency systems, AI use, or personnel screening by position, and the configuration standard covers only the cloud.
9. **AI governance is informal.** The AI eligibility assistant has been in production for AG-03 since 2025-11 after a 2025 pre-launch accuracy review, but with no subgroup (bias) testing since launch and no monitoring of how often caseworkers accept wrong suggestions. Engineering adopted an AI coding assistant in 2026-03 without a security review. The AG-44 contract needs Colorado SB26-189 developer documentation before go-live.
10. **The incident response plan has gaps.** The 2025 plan was tested once (an internal tabletop in 2025-10, without agencies). It lacks the reporting clocks for the out-of-state customers and has no insider-misuse procedure.
11. **Contract-end deletion is incomplete.** A deletion procedure exists since 2025, but archive and backup copies for 3 former municipal customers were not covered.
12. **GovRAMP progression.** The State B contracts require GovRAMP Authorized status by 2027-06-30; the company holds Ready status.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 regulation | NIST SP 800-53 Rev. 5 (Release 5.2.0) Moderate baseline, required by every agency contract, with overlays for the CJIS Security Policy v6.1, IRS Pub. 1075 (Rev. 11-2021), SNAP and Medicaid confidentiality, the Driver's Privacy Protection Act, and Fla. Stat. 501.171 (third-party agent duties) |
| P08 incidents | **Two incident types:** (1) ransomware spread through the managed services remote management platform to agency-hosted systems holding CJI (AG-02) and into the ACMC administration environment, with data theft that may include FTI from the AG-01 enclave; (2) insider unauthorized access to FTI, CJI, or motor vehicle records by a company employee. Integrated with crisis management and legal |
| P09 SOC 2 | The company **is** a service organization. Readiness for its first SOC 2 Type 2 examination of the ACMC (Security, Availability, Confidentiality), building on the 2025 Type 1 report, plus a subservice and vendor SOC 2 review program. GovRAMP Authorized is pursued in parallel |
| P10 AI | AI use-case portfolio: AI-001 AI eligibility assistant (AG-03 production; AG-44 contracted), AI-002 AI coding assistant, AI-003 support ticket summarization, AI-004 public records redaction assistant, AI-005 general-purpose public AI tools |
| Cloud | Multi-account landing zone (8 accounts), vendor-agnostic. Services are described by category, with AWS, Azure, and Google Cloud equivalents noted only where needed for shared responsibility |
| Registry defaults | The registry primary system ("case management system hosted for state and local agencies") is the ACMC. The registry incident ("ransomware affecting agency systems holding CJI and FTI") is kept, routed through the managed services line because at this size the company administers agency-hosted systems as well as its own cloud. The registry AI use case ("AI eligibility determination for public benefits") is kept as AI-001, framed as an assistant: under 7 CFR 272.4(a)(2) and 42 CFR 431.10(b)(3) and (c)(2) the eligibility determination stays with government staff under merit personnel standards, so no AI or contractor may make it |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-07-06 to 2026-07-31 | BIA, risk assessment, and gap analysis fieldwork |
| 2026-08-03 to 2026-08-28 | Control assessment fieldwork (co-sourced internal audit) |
| 2026-09-17 | Results to the board audit committee; deliverables approved |

## 7. Facts added during the Phase 5 build (fictional; used across P01-P10)
These details were added so the deliverables could be specific. They do not change sections 1-6.

| Topic | Added fact |
|---|---|
| Contract service levels | ACMC contracts set a recovery time objective of 8 hours and a recovery point objective of 1 hour for the regulated tenants (AG-01, AG-02, AG-03, AG-04, AG-39), and 24 hours and 4 hours for municipal tenants. Monthly availability target 99.9%, with service credits up to 10% of the monthly fee. Managed services contracts require a response within 4 hours for severity 1 issues |
| Key contract values | AG-03 about $14 million a year; AG-01 about $9.5 million; AG-02 about $5 million (ACMC $3 million, managed services $2 million); AG-04 about $2.2 million; State B and State C customers about $6 million |
| Cyber insurance | $15 million aggregate limit, $500,000 retention. The carrier's panel supplies breach counsel and forensics. The policy requires notice through the carrier hotline before incident vendors are engaged |
| MDR | 24x7 coverage; the contract requires a call to the Security Operations Manager within 30 minutes of a high-severity alert. SYS-10 and the ACMC application audit logs are not in its scope today |
| Workforce activity | 142 terminations and 96 internal transfers in the 12 months to 2026-06-30. The June 2026 phishing simulation click rate was 5.9% |
| Designated positions | 186 staff with CJI access; 64 with FTI enclave access; 48 with AG-04 motor vehicle data access |
| Cloud administrators | 40 cloud administrators (cloud operations and site reliability); 6 of them form the FTI enclave administrator group |
| Managed services footprint | SYS-10 reaches about 410 agency servers at 9 agencies (AG-02 and AG-08 to AG-14) through jump servers inside each agency network |
| Vendors | 9 of the 22 vendors with agency data or agency system access are Tier 1 under the P09 tiering approach |
| AI facts | AI-001 is used by about 310 AG-03 caseworkers; about 118,000 applications were processed with it from 2025-11 to 2026-06. AI-002 coding assistant used by about 150 engineers since 2026-03. AI-004 is sold to 6 municipal customers |
| Planned acquisition | The private equity sponsor plans an add-on acquisition of a smaller GovTech firm in 2027 |
| P07 finding added | On 2026-08-19 P07 testing found the SYS-10 automation API token, which can run scripts on every managed agency server, stored in a shared engineering wiki page readable by 212 staff (P01 R-050) |
| Operating volumes (P05) | About 1,100 sheriff officers and program staff use BP-01; about 3,000 AG-03 caseworkers handle about 2,500 new applications and 9,000 verification tasks a day; about 600 AG-01 auditors and collectors; 9 AG-04 tax collector offices with about 1,200 held cases a day; about 6,000 municipal cases opened a day; about 1.4 million interface messages a day; about 900 support tickets a day; AG-02's jail management system supports about 2,400 inmates; about 25 active delivery projects |
| Recovery test | The 2025-11 full-tenant restore test (AG-03 tenant) took 14 hours |
| Analytics export (P03 PB-09) | Since 2025-04 a nightly job copied AG-01 free-text case note fields to the analytics service (SYS-08) outside the FTI enclave; 14 analysts without Pub. 1075 investigations could query them; 6 of 50 sampled notes contained FTI. The job was stopped on 2026-09-08 and the AG-01 disclosure officer is to be told by 2026-09-30 |
| Access findings | 45 support staff hold read access to all regulated tenants by default; 23 delivery consultants kept tenant access after their projects closed (61 closed assignments in 2026); 9 of 25 sampled transfers kept prior tenant roles; the 18 staff with pending CJIS or Pub. 1075 screening lost regulated access on 2026-09-18 by CEO direction |
| Other operating figures (P03, P07) | 188 new accounts in the 12 months to 2026-06-30; about 1,900 standard and 41 emergency changes in 2026 H1; 31 security incidents in 2025-2026; 212 high and critical vulnerability findings in Q1-Q2 2026, with 2 high findings from the 2026-03 penetration test open past 30 days; 3 of 10 sampled critical updates on AG-02 servers installed after 15 days; 12 managed agency servers at AG-08 to AG-14 run an unsupported operating system; 6 municipal tenants allow local accounts without MFA; about 640 SYS-10 work orders a month; the AG-02 interconnection agreement was last reviewed in 2023 |
| Assurance demand (P09) | AG-03 amended its contract in 2026 to require a SOC 2 Type 2 report covering a period in 2027; AG-01 asked for a Type 2 report before its 2027 renewal. Planned Type 2 period 2027-04-01 to 2027-09-30. The other 3 Tier 1 vendors are the productivity suite, the endpoint protection and device management vendor, and the staffing firm that supplies contract developers |
| FY2027 security budget (P01) | $955,000 one-time and $455,000 a year, approved by the CEO on 2026-09-17 |
| Exercises | Agency tabletop with AG-01, AG-02, and AG-03 on 2026-12-15; insider misuse tabletop on 2027-02-17 |
| AI-001 validation (P10) | 600 applications re-worked blind by AG-03 quality control (2026-05 to 2026-07): outcome agreement 93.0% (42 wrong; caseworkers caught 19 and accepted 23; 9 incorrect denials reopened). SSNs masked since 2026-02. Interim review-first switch from 2026-10-01. AI-003 in production since 2026-05; AI-004 since 2026-02 |
| Terminology | "Agency Case Management Cloud (ACMC)" is the SSP system in P02, identifier CSC-ACMC-01 |
