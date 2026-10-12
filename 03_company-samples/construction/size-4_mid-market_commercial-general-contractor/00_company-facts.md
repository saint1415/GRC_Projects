# Scenario facts: Cris Santos Company | Construction | Mid-Market

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or contract clause, the citation is given. Regulatory text was checked on eCFR (version date 2026-09-23) and the Federal Register.

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
| CUI handled | On FC-4 only. The Government furnished CUI-marked site, security, and facility drawings at award, and the A&E subcontractor produces CUI-marked design packages. These are **covered defense information (CDI)** under DFARS 252.204-7012(a). About 6,800 CUI-marked sheets and documents exist. 14 FC-4 trade subcontractors and the A&E firm hold CUI (EV-028, EV-030) |
| CMMC requirement | The Army Corps of Engineers announced at a 2026-06 industry day that the follow-on MATOC solicitation (expected 2027 Q1, award about 2027-07) will require **CMMC Level 2 (C3PAO)**. Phase 2 of the CMMC phase-in was planned for 2026-11-10 (32 CFR 170.3(e)(2)). The DoD (Department of War) CIO memorandum of 2026-07-13 suspends CMMC Phase 2. Until 2028-11-09, DoD includes clause 252.204-7021 only when a program office requires a specific CMMC level, and during the suspension requiring activities may require Level 1 (Self) or Level 2 (Self) (DoD Class Deviation 2026-O0025, Revision 3 (DFARS 240.371-5)). The USACE Level 2 (C3PAO) requirement is therefore suspended under the deviation. The company keeps preparing, because it still owes NIST SP 800-171 Rev. 2 under DFARS 252.204-7012 on FC-4, and keeps the C3PAO assessment as a voluntary choice. The follow-on MATOC is about 15% of planned revenue for 2027 to 2031 (EV-034, EV-056). Applicability is recorded in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (N23-R04) |
| Private and state or local work (about 58% of construction revenue) | A private university research building, two county school campuses, a private hospital medical office building, and private office and mixed-use buildings |
| MBSS clients | 38 client sites (hospitals, a university, county buildings, private offices). Two clients (a hospital system and the university) require a **SOC 2 Type 2** report on MBSS by contract renewal on 2027-12-31 (EV-050) |
| Insurance | Cyber policy with a $10 million aggregate limit, a $1 million social engineering (funds transfer fraud) sublimit, and a $250,000 retention. The carrier's panel supplies breach counsel and forensics; notice goes through the carrier hotline before incident vendors are engaged (EV-048). Performance and payment bonds through a surety |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): classified information (no facility clearance; NISPOM, 32 CFR Part 117, does not apply; EV-027), HIPAA (no PHI is held for clients; the employee health plan is fully insured; EV-049, EV-050), PCI DSS (no card payments accepted; EV-049), SEC cyber disclosure rules (privately held; EV-040), and CIRCIA reporting (final rule not published) |
| State law approach | Florida law is cited only where unavoidable (breach notice for employee and subcontractor-worker personal information, Fla. Stat. 501.171; obligations register FL-501.171). Otherwise the samples stay federal |
| FAR overhaul clause numbers | Background fact, not scored in P03. Contracts awarded before the contracting agency adopted its FAR Part 40 class deviation keep the clauses this sample cites (FAR 52.204-21, 52.204-25 and DFARS 252.204-7019 and -7020) until they are modified. New awards under the deviation carry FAR 52.240-93, which has the same 15 safeguarding requirements as FAR 52.204-21, and FAR 52.240-91, which replaces the separate Kaspersky, Section 889 and FASCSA reports with one report within 72 hours. New DoD awards under DFARS Part 240 (DoD Class Deviation 2026-O0025, Revision 3) carry 252.240-7997 for DoD-led Medium and High NIST SP 800-171 assessments instead of 252.204-7019 and -7020. Sources: SRC-FAR-RFO-PART40 and SRC-DFARS-DEV-2026-O0025 |

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
| Equipment and Fleet Manager | Equipment telematics, time-clock kiosks, and yard systems (SYS-11); owner of the related vendor risks |
| Director of VDC | BIM and CAD standards; model servers; business owner of AI-003 |
| Internal audit (co-sourced firm) | Annual IT audit; performed the P07 control assessment. Reports to the audit committee and operates no control |
| Managed security service provider (MSSP) | 24x7 managed detection and response (MDR) and SIEM for the corporate environment. Not authorized for the CUI Project Enclave |
| C3PAO | To be engaged for the Level 2 certification assessment. Independent of the internal audit firm |

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv). Suppliers are in [`step-00_P00_intake/vendor-register.csv`](step-00_P00_intake/vendor-register.csv).

| ID | System | Hosting | FCI or CUI? | Notes |
|---|---|---|---|---|
| SYS-01 | Construction project management platform (drawings, RFIs, submittals, daily logs, pay app workflow, subcontractor portal) | Commercial vendor SaaS | FCI. **CUI found (spill; EV-029)** | System of record for projects. About 2,600 external subcontractor, owner, and design-team users. Vendor SOC 2 Type 2. Not FedRAMP authorized (EV-006, EV-047) |
| SYS-02 | Construction ERP and accounting (job cost, billing, accounts payable, vendor master with bank details) | Commercial vendor SaaS | FCI | Generates pay apps and ACH payment files. Vendor SOC 2 Type 2 |
| SYS-03 | Payroll, HR, certified payroll, and applicant tracking | Commercial vendor SaaS | FCI (certified payrolls) | Employee personal information (Social Security numbers, bank accounts). Applicant screening feature (AI-006) |
| SYS-04 | Corporate identity provider (single sign-on, MFA, conditional access) | SaaS | No (identities) | About 610 workforce accounts. Push MFA with number matching; FIDO2 security keys for 22 administrators (EV-001) |
| SYS-05 | Corporate productivity suite (email, files, chat) and its generative AI assistant (AI-003) | Commercial SaaS | FCI | Email carries pay apps, lien waivers, and payment correspondence |
| SYS-06 | Corporate cloud landing zone: 5 accounts (security and identity, shared services, corporate workloads, MBSS, backup) | Commercial public cloud (vendor-agnostic) | FCI | Workloads: BIM/CAD file servers with GPU virtual desktops, estimating database, internet-facing file-transfer portal for design teams, data warehouse. MBSS account: SYS-13. Backup account: immutable backups (EV-017, EV-018) |
| SYS-07 | **CUI Project Enclave (CPE)**: separate identity tenant, collaboration suite (CUI email, files), virtual desktops, and 18 dedicated enclave laptops | Government-community cloud, FedRAMP authorized at Moderate or higher (SaaS and virtual desktop service) | **CUI** | Built 2025-03 for FC-4. 52 named accounts: 41 company staff, 8 guest accounts for A&E firm staff, 3 administrators. Phishing-resistant MFA. Provider customer responsibility matrix (CRM) on file (EV-023, EV-024) |
| SYS-08 | Office, yard, and jobsite networks | On-premises | FCI in transit | SD-WAN between headquarters, the regional office, and the yard. 22 jobsite trailers use cellular routers |
| SYS-09 | Endpoints | On-premises and field | FCI; CUI on some tablets (spill; EV-016) | 420 managed laptops and desktops with EDR; 380 managed smartphones; 150 rugged jobsite tablets (110 in device management, **40 not**); 12 commissioning laptops (managed since 2025) (EV-009, EV-010) |
| SYS-10 | Bank treasury portal (ACH, wires, positive pay) | Bank-hosted | No | Dual approval for all ACH batches and wires (EV-041) |
| SYS-11 | Jobsite technology: equipment telematics (140 pieces), rented jobsite cameras with AI safety analytics (AI-002), time-clock kiosks, drone photo service | Vendor-operated | No | Out of the FCI scope by policy |
| SYS-12 | SIEM and 24x7 MDR | MSSP-operated, commercial cloud | Security data | Covers SYS-04, SYS-05, SYS-06, endpoint EDR, and office firewalls. **Not covered:** SYS-01 audit logs, SYS-02 vendor-master changes, SYS-07 (CPE), jobsite routers (EV-020) |
| SYS-13 | MBSS platform: remote monitoring and management servers, a remote-access gateway to client sites, a ticketing system, and a client credential vault | MBSS account in SYS-06 | Client facility security details | 38 client sites (EV-050). SOC 2 scope (P09) |
| SYS-14 | Federal portals (SAM.gov, SPRS, federal invoicing, DIBNet) | Government-operated | n/a | Company accounts only. SAM holds the company's EFT information |
| SYS-15 | AI tools | Various | Varies | See P10: AI-001 estimating and bid assistant, AI-002 jobsite safety video analytics, AI-003 productivity suite generative AI assistant, AI-004 accounts payable invoice capture and coding, AI-005 MBSS alarm triage, AI-006 applicant screening (EV-058) |

Client-installed systems (video surveillance, access control, BAS) are owned by clients. During installation, warranty, and MBSS service the company holds their configurations and administrator credentials: **client facility security details**.

**SSP system (P02):** the *Project Delivery and Payment Platform (PDPP)*: SYS-01, SYS-02, SYS-04, SYS-05, SYS-06 (except the MBSS account), SYS-07 (the CUI Project Enclave, documented as a subsystem with its own boundary), SYS-08, SYS-09, and SYS-12, with interfaces to SYS-03, SYS-10, SYS-14, and AI-001. Moderate baseline with tailoring. The CPE subsystem is the proposed CMMC Level 2 assessment scope and the NIST SP 800-171 Rev. 2 system security plan (3.12.4); the rest of the PDPP is the FCI scope (FAR 52.204-21).

## 4. Where the evidence is

This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Every item has a source system, an owner, and as-of and collected dates.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps against NIST SP 800-171 Rev. 2, the DFARS and FAR clauses, and 32 CFR Part 170** are judged in the gap analysis (P03), and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

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
| 2026-06-15 to 2026-07-02 | Intake: evidence requests, exports, walk-throughs at headquarters, the yard, and the FC-4 trailer, inventories, obligations register |
| 2026-07-06 to 2026-07-31 | BIA interviews, risk assessment and gap analysis fieldwork |
| 2026-07-27 to 2026-07-31 | 2026 policies (POL-01 to POL-05) and new standards drafted from the gaps |
| 2026-08-03 to 2026-08-21 | Control assessment by the co-sourced internal audit firm (jobsite and office walkthroughs 2026-08-11 to 2026-08-13): operating tests of controls already in place; design review of the draft policies and standards |
| 2026-08-12 | Covered video surveillance equipment identified at the FC-2 jobsite (P07) |
| 2026-08-13 | Section 889 report to the FC-2 Contracting Officer (FAR 52.204-25(d)(2)(i)) |
| 2026-08-24 to 2026-09-12 | AI governance assessment (P10) |
| 2026-08-26 | Section 889 follow-up report (FAR 52.204-25(d)(2)(ii), due within 10 business days of 2026-08-13) |
| 2026-09-17 | Results to the audit committee. Deliverables and policies approved (POL-01 by the CEO; POL-02 to POL-05 by the COO; STD-04 issued); High and Very High risks, risk appetite, and budget approved by the CEO |
| 2026-09-30 | Corrected SPRS Basic Assessment score due (Director of Contracts and Compliance) |
| 2026-10-01 | 2026 policies take effect |
| 2026-11-10 | Planned start of CMMC Phase 2 (32 CFR 170.3(e)(2)); suspended by the DoD (Department of War) CIO memorandum of 2026-07-13 (DoD Class Deviation 2026-O0025, Revision 3) |
| 2027-03 (planned) | Readiness check by the co-sourced internal audit firm, including a follow-up of the operating effectiveness of the controls the 2026 policies and standards introduced, after at least one quarter of operation |
| 2027-04-12 to 2027-04-23 | Target window for the Level 2 certification assessment by a C3PAO (voluntary while Phase 2 is suspended) |
