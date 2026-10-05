# Scenario facts: Cris Santos Company | Construction | Mid-Market

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or contract clause, the citation is given. Regulatory text was checked on eCFR (version date 2026-09-23) and the Federal Register.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (privately held corporation; private equity-backed since 2022; board with an audit committee) |
| Business | Commercial and institutional building general contractor (NAICS 236220): new construction, additions, and renovations of offices, health care buildings, schools, university buildings, and federal facilities, delivered as general contractor, construction manager at risk, and design-builder. Self-performs concrete, carpentry, framing and drywall, and general conditions, with a prefabrication shop. A **Technology and Security Systems group** installs structured cabling, network switches, video surveillance, access control, and building automation (BAS) integration in client buildings, and since 2025 sells a recurring **Managed Building Systems Services (MBSS)** line: remote monitoring, health checks, and administration of installed client systems after warranty |
| Location | Florida only. **Headquarters** (executive, accounting, preconstruction, IT), a **regional office** about 120 miles away, a **central equipment yard and prefabrication shop**, the **MBSS monitoring room** at headquarters, and **22 active jobsites**, each with a field office trailer |
| Workforce | 600 employees: 16 executives and directors, 72 project management staff (project executives, project managers, assistant project managers, project engineers), 48 superintendents and field engineers, 18 preconstruction and estimating, 318 self-perform craft and prefabrication shop, 46 Technology and Security Systems staff (installers, technicians, MBSS monitoring), 18 safety, quality, and virtual design and construction (VDC), 22 accounting and finance, 10 HR, payroll, and training, 5 contracts and legal, 13 IT and security, 14 equipment, fleet, and yard |
| Revenue | About $100 million a year (fictional): about $94 million construction and about $6 million MBSS. Above the SBA size standard of $45.0 million for NAICS 236220 (13 CFR 121.201), so **not SBA-small**. The company no longer bids small-business set-asides |
| Billing and payments | Monthly progress payment applications (pay apps) with a schedule of values on 22 projects, about $7.8 million billed a month. Private and state or local owners pay by ACH or wire. Federal agencies pay by electronic funds transfer to the bank account in the company's SAM registration (FAR 52.232-33(b)). The company pays about 450 active subcontractors and suppliers by ACH, about $5.2 million a month. On federal contracts it must pay subcontractors within 7 days of receiving payment (FAR 52.232-27(c)(1)) |
| Federal work (about 42% of construction revenue) | **FC-1:** VA outpatient clinic addition (civilian agency, in progress). **FC-2:** GSA federal courthouse security and HVAC modernization (in progress); the Technology and Security Systems group installs cameras, access control, and network switches. **FC-3:** Army Corps of Engineers multiple-award task order contract (MATOC) for renovations at a Florida installation, awarded 2023; 3 open task orders; FCI only. **FC-4:** Army Corps of Engineers **design-build** of a 4-story operations and training facility at a Florida installation ($38 million, awarded 2025-03-17, construction through 2027-09). The design is by an architecture and engineering (A&E) firm under subcontract to the company. All four include FAR 52.204-21 and FAR 52.204-25. FC-3 and FC-4 include DFARS 252.204-7012, 252.204-7019, and 252.204-7020. None includes DFARS 252.204-7021 (CMMC), because all were awarded before CMMC Phase 1 began on 2025-11-10 |
| CUI handled | On FC-4 only. The Government furnished CUI-marked site, security, and facility drawings at award, and the A&E subcontractor produces CUI-marked design packages. These are **covered defense information (CDI)** under DFARS 252.204-7012(a). About 6,800 CUI-marked sheets and documents exist. 14 FC-4 trade subcontractors and the A&E firm hold CUI |
| CMMC requirement | The Army Corps of Engineers announced at a 2026-06 industry day that the follow-on MATOC solicitation (expected 2027 Q1, award about 2027-07) will require **CMMC Level 2 (C3PAO)**. Phase 2 of the CMMC phase-in begins 2026-11-10 (32 CFR 170.3(e)(2)). The follow-on MATOC is about 15% of planned revenue for 2027 to 2031 |
| Private and state or local work (about 58% of construction revenue) | A private university research building, two county school campuses, a private hospital medical office building, and private office and mixed-use buildings |
| MBSS clients | 38 client sites (hospitals, a university, county buildings, private offices). Two clients (a hospital system and the university) require a **SOC 2 Type 2** report on MBSS by contract renewal on 2027-12-31 |
| Insurance | Cyber policy with a $10 million aggregate limit, a $1 million social engineering (funds transfer fraud) sublimit, and a $250,000 retention. The carrier's panel supplies breach counsel and forensics; notice goes through the carrier hotline before incident vendors are engaged. Performance and payment bonds through a surety |
| Not in scope | Classified information (no facility clearance; NISPOM, 32 CFR Part 117, does not apply). HIPAA (no PHI is held for clients; the employee health plan is fully insured). PCI DSS (no card payments accepted). SEC cyber disclosure rules (privately held). CIRCIA reporting (final rule not published) |
| State law approach | Florida law is cited only where unavoidable (breach notice for employee and subcontractor-worker personal information, Fla. Stat. 501.171). Otherwise the samples stay federal |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Board audit committee | Quarterly cyber risk and CMMC readiness reporting |
| Chief Executive Officer (CEO) | Accepts High and Very High risk; approves the risk appetite and security budget; **CMMC Affirming Official** (32 CFR 170.22) |
| Chief Operating Officer (COO) | Executive sponsor of the security program; **system owner** of the PDPP; accepts Moderate risk; approves policies |
| Chief Financial Officer (CFO) | Owner of treasury and payment controls and the ERP; cyber insurance policy holder; business owner of AI-004 |
| General Counsel | Legal privilege during incidents; breach decisions for personal information; False Claims Act and contract counsel liaison |
| Virtual CISO (vCISO, part-time contractor) | Program strategy; risk appetite; board reporting |
| IT Director | Infrastructure, cloud landing zone, networks, endpoints, and recovery lead |
| Security Manager, 2 security analysts, and 1 GRC analyst | Security operations and MSSP liaison; incident commander; SSP and POA&M owner (Security Manager); risk register, evidence, and SPRS score calculation (GRC analyst) |
| Director of Contracts and Compliance | FAR and DFARS flowdowns; SAM Entity Administrator; SPRS submissions; Section 889 reports; DIBNet reporting lead |
| Vice President of Operations | Project delivery, superintendents, jobsite physical security, field devices |
| FC-4 Project Executive | **CUI custodian** for FC-4: CUI intake, distribution to the A&E firm and trade subcontractors, and the FC-4 jobsite |
| Controller | Billing, accounts payable, the ERP vendor master, and bank portal administration |
| Director of Preconstruction | Estimating and bidding; business owner of AI-001 |
| Director of Technology and Security Systems | Leads the installation group and the MBSS service line; Section 889 screening of installed equipment; custodian of client system credentials; business owner of AI-005 |
| Director of Safety | Safety program; business owner of AI-002 |
| HR Director | Screening, onboarding, terminations, training records; business owner of AI-006 |
| Director of VDC | BIM and CAD standards; model servers; business owner of AI-003 |
| Internal audit (co-sourced firm) | Annual IT audit; performed the P07 control assessment. Reports to the audit committee and operates no control |
| Managed security service provider (MSSP) | 24x7 managed detection and response (MDR) and SIEM for the corporate environment. Not authorized for the CUI Project Enclave |
| C3PAO | To be engaged for the Level 2 certification assessment. Independent of the internal audit firm |

## 3. Systems

| ID | System | Hosting | FCI or CUI? | Notes |
|---|---|---|---|---|
| SYS-01 | Construction project management platform (drawings, RFIs, submittals, daily logs, pay app workflow, subcontractor portal) | Commercial vendor SaaS | FCI. **CUI found (spill)** | System of record for projects. About 2,600 external subcontractor, owner, and design-team users. Vendor SOC 2 Type 2. Not FedRAMP authorized |
| SYS-02 | Construction ERP and accounting (job cost, billing, accounts payable, vendor master with bank details) | Commercial vendor SaaS | FCI | Generates pay apps and ACH payment files. Vendor SOC 2 Type 2 |
| SYS-03 | Payroll, HR, certified payroll, and applicant tracking | Commercial vendor SaaS | FCI (certified payrolls) | Employee personal information (Social Security numbers, bank accounts). Applicant screening feature (AI-006) |
| SYS-04 | Corporate identity provider (single sign-on, MFA, conditional access) | SaaS | No (identities) | About 610 workforce accounts. Push MFA with number matching; FIDO2 security keys for 22 administrators |
| SYS-05 | Corporate productivity suite (email, files, chat) and its generative AI assistant (AI-003) | Commercial SaaS | FCI | Email carries pay apps, lien waivers, and payment correspondence |
| SYS-06 | Corporate cloud landing zone: 5 accounts (security and identity, shared services, corporate workloads, MBSS, backup) | Commercial public cloud (vendor-agnostic) | FCI | Workloads: BIM/CAD file servers with GPU virtual desktops, estimating database, internet-facing file-transfer portal for design teams, data warehouse. MBSS account: SYS-13. Backup account: immutable backups |
| SYS-07 | **CUI Project Enclave (CPE)**: separate identity tenant, collaboration suite (CUI email, files), virtual desktops, and 18 dedicated enclave laptops | Government-community cloud, FedRAMP authorized at Moderate or higher (SaaS and virtual desktop service) | **CUI** | Built 2025-03 for FC-4. 52 named accounts: 41 company staff, 8 guest accounts for A&E firm staff, 3 administrators. Phishing-resistant MFA. Provider customer responsibility matrix (CRM) on file |
| SYS-08 | Office, yard, and jobsite networks | On-premises | FCI in transit | SD-WAN between headquarters, the regional office, and the yard. 22 jobsite trailers use cellular routers |
| SYS-09 | Endpoints | On-premises and field | FCI; CUI on some tablets (spill) | 420 managed laptops and desktops with EDR; 380 managed smartphones; 150 rugged jobsite tablets (110 in device management, **40 not**); 12 commissioning laptops (managed since 2025) |
| SYS-10 | Bank treasury portal (ACH, wires, positive pay) | Bank-hosted | No | Dual approval for all ACH batches and wires |
| SYS-11 | Jobsite technology: equipment telematics (140 pieces), rented jobsite cameras with AI safety analytics (AI-002), time-clock kiosks, drone photo service | Vendor-operated | No | Out of the FCI scope by policy |
| SYS-12 | SIEM and 24x7 MDR | MSSP-operated, commercial cloud | Security data | Covers SYS-04, SYS-05, SYS-06, endpoint EDR, and office firewalls. **Not covered:** SYS-01 audit logs, SYS-02 vendor-master changes, SYS-07 (CPE), jobsite routers |
| SYS-13 | MBSS platform: remote monitoring and management servers, a remote-access gateway to client sites, a ticketing system, and a client credential vault | MBSS account in SYS-06 | Client facility security details | 38 client sites. SOC 2 scope (P09) |
| SYS-14 | Federal portals (SAM.gov, SPRS, federal invoicing, DIBNet) | Government-operated | n/a | Company accounts only. SAM holds the company's EFT information |
| SYS-15 | AI tools | Various | Varies | See P10: AI-001 estimating and bid assistant, AI-002 jobsite safety video analytics, AI-003 productivity suite generative AI assistant, AI-004 accounts payable invoice capture and coding, AI-005 MBSS alarm triage, AI-006 applicant screening |

Client-installed systems (video surveillance, access control, BAS) are owned by clients. During installation, warranty, and MBSS service the company holds their configurations and administrator credentials: **client facility security details**.

**SSP system (P02):** the *Project Delivery and Payment Platform (PDPP)*: SYS-01, SYS-02, SYS-04, SYS-05, SYS-06 (except the MBSS account), SYS-07 (the CUI Project Enclave, documented as a subsystem with its own boundary), SYS-08, SYS-09, and SYS-12, with interfaces to SYS-03, SYS-10, SYS-14, and AI-001. Moderate baseline with tailoring. The CPE subsystem is the proposed CMMC Level 2 assessment scope and the NIST SP 800-171 Rev. 2 system security plan (3.12.4); the rest of the PDPP is the FCI scope (FAR 52.204-21).

## 4. Current security posture: defined program with gaps in scale

**In place today:**
- Security policies adopted in 2024, with standards for cloud configuration, endpoints, and encryption
- A CUI Project Enclave in a government-community cloud whose offerings are FedRAMP authorized at Moderate or higher (DFARS 252.204-7012(b)(2)(ii)(D)), with phishing-resistant MFA and a provider CRM on file
- SPRS Basic Assessment score of **71** (self-assessment, CPE scope), posted 2025-02-14 before the FC-4 award
- Single sign-on with push MFA (number matching) for all corporate users; FIDO2 security keys for administrators
- EDR on all managed laptops, desktops, and cloud servers, with 24x7 MSSP monitoring and a SIEM for the corporate environment
- Immutable backups of corporate cloud workloads in a separate backup account (35-day write-once retention); estimating database and BIM/CAD server restores tested in 2026-03
- Quarterly authenticated vulnerability scanning of cloud workloads and office networks
- Payment controls: dual approval of all ACH batches and wires; call-back verification of subcontractor bank changes since 2025; positive pay
- Annual security awareness training, quarterly phishing simulations, and payment-fraud training for accounting staff
- Section 889 submittal screening for federal jobs (since 2025)
- Incident response plan (2024) with a 2025 ransomware tabletop
- Annual co-sourced internal IT audit

**Missing or weak, found in the 2026 assessments:**
1. **CUI outside the enclave.** 1,140 CUI-marked FC-4 sheets and documents sit in the commercial project management platform (SYS-01), visible to 230 external users from 14 subcontractor firms. 26 FC-4 jobsite tablets hold offline CUI drawing sets. Printed CUI sets in the FC-4 trailer are not stored or destroyed as CUI (3.1.3, 3.8.1 to 3.8.5).
2. **SPRS score is not accurate.** The 2025 score of 71 assumed CUI stayed in the CPE. It did not cover the jobsite, tablets, SYS-01, or printed CUI (DFARS 252.204-7019(b)).
3. **Subcontractor flowdown.** 15 FC-4 subcontractors (the A&E firm and 14 trades) receive CUI. Only the A&E subcontract includes DFARS 252.204-7012; SPRS scores of 3 of 15 are verified (252.204-7012(m); 252.204-7020(g)).
4. **Payment controls bypassed under time pressure.** 2 of 25 sampled bank changes had no call-back record ("urgent" overrides). Private owners have not been told how the company will and will not change its remittance details. Push MFA is not phishing-resistant for Project Managers and accounting staff. DMARC is at quarantine with no lookalike-domain monitoring.
5. **Logging gaps.** SYS-01 audit logs, SYS-02 vendor-master changes, jobsite routers, and the CPE do not reach the SIEM. CPE logs are reviewed manually once a week (3.3.5, 3.14.6).
6. **Field devices.** 40 of 150 rugged tablets are outside device management. Jobsite cellular routers are configured one by one with no baseline; 7 of 22 have remote administration open to the internet.
7. **Access reviews** are semiannual. 31 external SYS-01 accounts remain on closed projects. Privileged access management covers the cloud only.
8. **DIBNet reporting readiness.** The only DoD-approved medium assurance certificate (held by the Director of Contracts and Compliance) expired 2026-05-20. There has been no CUI incident exercise (252.204-7012(c)(3)).
9. **Recovery gaps.** The CPE has no independent backup beyond the provider's retention. There is no independent export of SYS-01 project records. The ERP vendor's stated RTO of 24 hours does not meet the billing-week need.
10. **MBSS remote access.** 11 of 38 client sites are reached with shared technician accounts through the client's own remote-access tool, outside the company gateway.
11. **AI adopted without review.** Six AI uses were adopted by departments; none had a security, privacy, or bias review before P10. The productivity suite AI assistant was enabled for all users in 2026-04 and can read FCI. The jobsite safety analytics were deployed without written notice to workers.
12. **Vendor risk** tiering is not done for about 210 vendors; only 9 SaaS SOC 2 reports are reviewed each year.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 regulation | NIST SP 800-171 Rev. 2 (110 requirements) on the CPE scope, as required by DFARS 252.204-7012(b)(2) and assessed for CMMC Level 2 (32 CFR 170.14(c)(3)); plus the other DFARS 252.204-7012 paragraphs, DFARS 252.204-7019, 7020, and 7021, 32 CFR Part 170, FAR 52.204-21 (corporate FCI scope), FAR 52.204-25, and Fla. Stat. 501.171 |
| P08 | **Two incident types:** (1) business email compromise redirecting progress payments (the registry incident): a phished Project Manager mailbox redirects an owner's pay app payment, with a spoofed subcontractor bank change; and (2) compromise of covered defense information: ransomware with data theft at the A&E design subcontractor, with a variant for CUI found on an unauthorized system. Integrated with crisis management and legal |
| P09 | Readiness for a SOC 2 Type 2 examination of the MBSS service line (Security, Availability, Confidentiality), required by two clients by 2027-12-31. Includes a vendor assurance review program |
| P10 | AI use-case portfolio: AI-001 estimating and bid assistant (the registry use case), AI-002 jobsite safety video analytics, AI-003 productivity suite generative AI assistant, AI-004 accounts payable invoice capture and coding, AI-005 MBSS alarm triage, AI-006 applicant screening |
| Cloud | Commercial multi-account landing zone (5 accounts) plus the CUI Project Enclave in a government-community cloud. Vendor-agnostic; AWS, Azure, and Google Cloud equivalents only in an equivalents table |

The registry defaults fit this business and are kept. The primary system is named the Project Delivery and Payment Platform (PDPP), as in the Small sample, because pay apps and payments run through the same platforms as project documents. The mid-market depth adds CUI on one DoD design-build contract, a second incident type, a SOC 2 scope for the MBSS line, and an AI portfolio.

## 6. Assessment calendar (fictional unless a regulation is cited)

| Date | Event |
|---|---|
| 2025-02-14 | SPRS Basic Assessment score of 71 posted (self-assessment, CPE scope) |
| 2025-03-17 | FC-4 awarded |
| 2026-07-06 to 2026-07-31 | Risk assessment and gap analysis fieldwork |
| 2026-08-03 to 2026-08-21 | Control assessment by the co-sourced internal audit firm (jobsite and office walkthroughs 2026-08-11 to 2026-08-13) |
| 2026-08-12 | Covered video surveillance equipment identified at the FC-2 jobsite (P07) |
| 2026-08-13 | Section 889 report to the FC-2 Contracting Officer (FAR 52.204-25(d)(2)(i)) |
| 2026-08-26 | Section 889 follow-up report (FAR 52.204-25(d)(2)(ii), due within 10 business days of 2026-08-13) |
| 2026-09-17 | Results to the audit committee. Deliverables approved by the COO; High and Very High risks, risk appetite, and budget approved by the CEO |
| 2026-09-30 | Corrected SPRS Basic Assessment score due (Director of Contracts and Compliance) |
| 2026-11-10 | CMMC Phase 2 begins (32 CFR 170.3(e)(2)) |
| 2027-04-12 to 2027-04-23 | Target window for the Level 2 certification assessment by a C3PAO |
