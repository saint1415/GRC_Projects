# Scenario facts: Cris Santos Company | Defense Industrial Base | Mid-Market

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or contract clause, the citation is given. Regulatory text was checked on eCFR (version date 2026-09-23) and the Federal Register.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (privately held; private equity-backed since 2023; board with an audit committee) |
| Business | Aircraft parts manufacturer (NAICS 336413, Other Aircraft Parts and Auxiliary Equipment Manufacturing): machined structural fittings, hydraulic manifolds and valve bodies, sheet-metal subassemblies, and metal additively manufactured brackets for military and commercial aircraft. Quality system certified to AS9100. A small additive and engineering services line (launched 2026) prints and engineers parts for commercial customers |
| Location | Florida only. **Plant 1** (headquarters): machining (64 CNC machines, 8 coordinate measuring machines), the engineering center, and a hydraulic test lab with 6 test stands. **Plant 2** (acquired 2024-10-01 from a smaller supplier, about 90 miles away): sheet-metal and assembly lines, 26 CNC machines, 4 coordinate measuring machines, 6 metal additive printers, and a machine-vision inspection cell |
| Workforce | 850 employees: 500 production, 90 engineering (38 design, 32 manufacturing engineering and NC programming, 8 additive engineering, 12 test engineering), 75 quality, 60 supply chain and logistics, 75 administration (finance, HR, contracts and trade compliance, sales, program management, legal), 28 management, 22 IT and security. About 590 work at Plant 1 and headquarters, 260 at Plant 2 |
| Revenue | About $240 million a year (fictional). About 62% defense (three prime contractors) and 38% commercial. The SBA size standard for NAICS 336413 is 1,250 employees (13 CFR 121.201), so the company is still SBA-small. It is sized as Mid-Market by the tier rule (500-999 employees, Census SUSB class) and flagged as such |
| Defense customers | **Prime A** (about 28% of revenue, military transport aircraft structures), **Prime B** (about 20%, fighter aircraft hydraulic components), **Prime C** (about 14%, unmanned aircraft brackets and fittings). The company is a subcontractor. It holds no prime DoD contract |
| Commercial customers | **Customer D**, a commercial airframe manufacturer (about 18%); **Customer E**, a commercial tier-1 supplier (about 9%); aftermarket and spares (about 7%); the additive and engineering services line (about 4%, three commercial customers) |
| CUI handled | Controlled technical information (CTI) as defined in DFARS 252.204-7012(a): controlled drawings, 3D models, specifications, NC programs, additive build files, and test procedures derived from them. It is covered defense information (CDI) and CUI. Parts for Prime A and Prime B are ITAR defense articles, so their technical data is ITAR-controlled |
| Contract clauses in current subcontracts | DFARS 252.204-7012 (MAY 2024), 252.204-7019 and 252.204-7020 (NOV 2023), FAR 52.204-21 (NOV 2021). All current subcontracts were awarded before 2025-11-10 and do not include DFARS 252.204-7021 (EV-030). Which clauses bind the company is decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (C-DIB-R01, C-DIB-R03, C-DIB-R04) |
| CMMC requirement | All three primes notified suppliers that solicitations issued from 2026-11-10 (CMMC Phase 2, 32 CFR 170.3(e)(2)) would flow down DFARS 252.204-7021 (NOV 2025) at **CMMC Level 2 (C3PAO)** (EV-031). That requirement is suspended. The DoD (Department of War) CIO memorandum of 2026-07-13 suspends CMMC Phase 2. Until 2028-11-09, DoD includes clause 252.204-7021 only when a program office requires a specific CMMC level, and during the suspension requiring activities may require Level 1 (Self) or Level 2 (Self) (DoD Class Deviation 2026-O0025, Revision 3 (DFARS 240.371-5)). The company keeps preparing, because it still owes NIST SP 800-171 Rev. 2 under DFARS 252.204-7012, and keeps the C3PAO assessment as a voluntary choice. If a prime contract does require Level 2 (C3PAO), 32 CFR 170.23(a)(3) makes that the minimum for a subcontractor handling CUI. Prime A's next production lot solicitation is expected in 2027 Q1, with award in 2027-06. Status: intake obligations register (C-DIB-R02) |
| Export controls | Registered with the State Department's Directorate of Defense Trade Controls (22 CFR 122.1). A technology control plan limits ITAR technical data to U.S. persons. Customer D and Customer E parts carry EAR-controlled technology. Two foreign-national engineers in the commercial engineering group work only on data the Director of Trade Compliance and Contracts classified as not needing a license (classification records on file, EV-033); they have no enclave accounts (EV-005) |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): classified information: no facility clearance (EV-045), so NISPOM (32 CFR Part 117) does not apply. CIRCIA reporting: the final rule is not published (proposed only). SEC cyber disclosure: the company is privately held. Health, payment card, and consumer data: none beyond employee records |
| State law approach | Florida law is cited only where unavoidable (breach notice for employee personal information, Fla. Stat. 501.171). Otherwise the samples stay federal |
| FAR overhaul clause numbers | Background fact, not scored in P03. Contracts awarded before the contracting agency adopted its FAR Part 40 class deviation keep the clauses this sample cites (FAR 52.204-21, 52.204-25 and DFARS 252.204-7019 and -7020) until they are modified. New awards under the deviation carry FAR 52.240-93, which has the same 15 safeguarding requirements as FAR 52.204-21, and FAR 52.240-91, which replaces the separate Kaspersky, Section 889 and FASCSA reports with one report within 72 hours. New DoD awards under DFARS Part 240 (DoD Class Deviation 2026-O0025, Revision 3) carry 252.240-7997 for DoD-led Medium and High NIST SP 800-171 assessments instead of 252.204-7019 and -7020. Sources: SRC-FAR-RFO-PART40 and SRC-DFARS-DEV-2026-O0025 |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Board audit committee | Quarterly cyber risk and CMMC readiness reporting |
| Chief Executive Officer | Accepts High risk; approves the security budget and risk appetite; **CMMC Affirming Official** (32 CFR 170.22) |
| Chief Operating Officer | Executive sponsor of the security program; **system owner** of the CUI Engineering Enclave; accepts Moderate risk; approves policies |
| Chief Financial Officer | ERP owner; cyber insurance policy holder |
| General Counsel | Legal privilege during incidents; contract and export counsel liaison; breach decisions for employee personal information |
| Virtual CISO (vCISO, part-time contractor) | Program strategy; risk appetite; board reporting |
| IT Director | Infrastructure, cloud landing zone, networks, and recovery lead |
| Security Manager, 2 security analysts, and 1 GRC analyst | Security operations; SSP and POA&M owner (Security Manager); incident commander; MSSP liaison; risk register, evidence, and SPRS score calculation (GRC analyst) |
| Director of Engineering | CUI data owner for engineering data; owns CAD/PLM; business owner of AI-001 |
| Vice President of Operations, Plant 1 Manager, Plant 2 Manager | Shop-floor practices, production recovery, visitor escort on the floor; business owner of AI-003 |
| Director of Quality | Document control, travelers, printed CUI on the shop floor; business owner of AI-002 |
| Director of Trade Compliance and Contracts | DFARS flowdowns, SPRS submissions, prime notifications, DIBNet reporting lead; **ITAR Empowered Official**; technology control plan |
| Manufacturing Systems Manager and 3 manufacturing systems engineers | MES, DNC, CNC, CMM, additive printer, and test lab connectivity (operational technology) |
| Director of Supply Chain | Supplier onboarding, purchase order terms, outside processors |
| HR Director | Screening, onboarding, terminations, training records; business owner of AI-005 |
| Facilities and Security Manager | Badges, visitor management, cameras at both plants |
| Director of Additive and Engineering Services | Owner of the commercial services line in the SOC 2 scope (P09) |
| Internal audit (co-sourced firm) | Annual IT audit; performed the P07 control assessment. Reports to the audit committee and does not operate any control |
| Managed security service provider (MSSP) | 24x7 managed detection and response and SIEM. An External Service Provider that handles Security Protection Data (32 CFR 170.19(c)(2)) |
| C3PAO | To be engaged separately for the Level 2 certification assessment. Independent of the internal audit firm |

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv). Suppliers are in [`step-00_P00_intake/vendor-register.csv`](step-00_P00_intake/vendor-register.csv).

| ID | System | Hosting | CUI? | CMMC asset category (32 CFR 170.19(c)) | Notes |
|---|---|---|---|---|---|
| SYS-01 | Enclave identity provider (single sign-on, MFA, device compliance) | Government-community cloud (SaaS) | No (identities) | Security Protection Asset | 318 enclave accounts: 290 named users, 12 administrators, 4 break-glass, 12 service accounts. Hardware security keys for administrators (EV-001) |
| SYS-02 | Enclave collaboration suite (CUI email, file storage, chat) | Government-community cloud (SaaS) | Yes | CUI Asset | FedRAMP authorized at Moderate or higher; customer responsibility matrix (CRM) on file (EV-020) |
| SYS-03 | Enclave cloud landing zone: 4 accounts (security and identity, shared services, workloads, backup) | Government-community cloud (IaaS/PaaS, same provider) | Yes | CUI Asset (workloads, backup); Security Protection Asset (security account, log pipeline) | Shared services: network hub, VPN gateways, virtual desktop pool (120 sessions), managed file transfer (MFT) gateway. Workloads: PLM application and database, CAD license servers, additive build preparation server, test data repository (EV-018) |
| SYS-04 | CAD/PLM | CAD on SYS-05 workstations; PLM in SYS-03 | Yes | CUI Asset | System of record for about 165,000 controlled documents (drawings, models, NC programs, build files, test procedures) (EV-008) |
| SYS-05 | Enclave endpoints | On-premises and mobile | Yes | CUI Asset | 120 CAD workstations and 110 enclave laptops. Full-disk encryption and EDR (EV-009) |
| SYS-06 | MES and DNC servers with 60 shop-floor terminals | On-premises, both plants | Yes | CUI Asset | **Plant 1:** current MES with single sign-on and badge plus PIN, 40 terminals. **Plant 2:** legacy MES and DNC on a server operating system past end of vendor support, 20 terminals with **shared logins** (EV-008, EV-011) |
| SYS-07 | Operational technology: 90 CNC machines, 12 CMMs, 6 metal additive printers, 6 hydraulic test stands with data acquisition PCs, machine-vision inspection cell | On-premises, both plants | Yes (NC programs, build files, test data) | Specialized Assets | 82 CNC machines receive programs from DNC; **8 legacy machines at Plant 2 are loaded by USB drive**. Additive printer vendor connects through its own remote support tool (EV-010, EV-038) |
| SYS-08 | Plant enclave networks and SD-WAN | On-premises | Yes (in transit) | Security Protection Asset | Enclave firewalls, engineering and shop-floor VLANs, SD-WAN between plants, site-to-cloud VPN. **Plant 2 shop floor is not separated from the Plant 2 corporate network** (EV-012) |
| SYS-09 | Corporate network, commercial productivity suite, and about 410 corporate endpoints | On-premises and commercial SaaS | No (policy) | Out-of-Scope Asset (must stay separated) | Commercial business, office staff, time clocks. MFA on all corporate accounts (EV-003) |
| SYS-10 | ERP (orders, purchasing, inventory, routings, costing) | Commercial SaaS | No CUI; holds DoD purchase order data (FCI) | Out-of-Scope Asset (attachments disabled since 2025; routings cite drawing numbers only) | FAR 52.204-21 applies (EV-035) |
| SYS-11 | Payroll, HR, and applicant tracking SaaS | Commercial SaaS | No | Out-of-Scope Asset | Employee personal information (Florida breach law applies). Includes the applicant ranking feature (AI-005) (EV-004, EV-044) |
| SYS-12 | CUI exchange paths | Mixed | Yes | CUI Asset (company side) | (a) Prime A supplier portal, reached from enclave virtual desktops; (b) MFT gateway in SYS-03 used with Prime B, Prime C, the three services customers, and 22 suppliers and outside processors (FIPS mode on); (c) site-to-cloud VPN from both plants and the SD-WAN tunnel between plants. **FIPS-validated mode not confirmed on the Plant 2 SD-WAN appliance** (EV-012, EV-018) |
| SYS-13 | SIEM and 24x7 managed detection and response | MSSP-operated, hosted in a government-community cloud region | Security Protection Data | Security Protection Asset (ESP services) | Covers SYS-01, SYS-02, SYS-03, enclave and corporate endpoint EDR, and Plant 1 firewalls. **Not covered:** MES and DNC at both plants, Plant 2 network, OT (EV-019) |
| SYS-14 | AI tools | Various | Varies | See P10 | AI-001 enclave generative AI assistant (pilot), AI-002 machine-vision inspection, AI-003 CNC predictive maintenance, AI-004 corporate generative AI assistant, AI-005 applicant ranking, AI-006 public chatbots (prohibited) (EV-044) |

**SSP system (P02):** the *CUI Engineering Enclave (CEE)*: SYS-01 to SYS-08, the company side of SYS-12, and the MSSP services in SYS-13 (as Security Protection Assets), plus the people, printed CUI, and plant areas at both plants that handle CUI. Moderate baseline with tailoring.

## 4. Where the evidence is

This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Every item has a source system, an owner, and as-of and collected dates.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps against NIST SP 800-171 Rev. 2 and the DFARS, CMMC, FAR, ITAR, and EAR duties** are judged in the gap analysis (P03), and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P08 | **Two incident types:** (1) exfiltration of CUI, in which an adversary-in-the-middle phishing page steals an engineer's enclave session and the attacker stages PLM exports and drawings through the virtual desktop pool, with a variant for a CUI breach at a supplier; and (2) ransomware on the Plant 2 shop floor (MES, DNC, OT). Integrated with crisis management and legal |
| P09 | Readiness for a SOC 2 Type 2 examination (Security, Availability, Confidentiality) of the additive and engineering services line, required by its three commercial customers by 2027-12-31. CMMC stays the primary assurance mechanism for defense work. Includes a vendor assurance review program |
| P10 | AI use-case portfolio: AI-001 enclave generative AI assistant used with CUI engineering documents (the registry use case), AI-002 machine-vision inspection, AI-003 CNC predictive maintenance, AI-004 corporate generative AI assistant (no CUI), AI-005 applicant ranking, AI-006 public chatbots (prohibited) |
| Cloud | Multi-account landing zone in a government-community cloud, vendor-agnostic. Services are described by category; AWS, Azure, and Google Cloud equivalents are noted only in an equivalents table |

The registry defaults (primary system, CUI exfiltration incident, generative AI with CUI) fit this business at this size and are kept. The mid-market depth adds a second plant, a second incident type, and an AI portfolio.

## 6. Assessment calendar (fictional unless a regulation is cited)

| Date | Event |
|---|---|
| 2024-10-01 | Plant 2 acquired |
| 2025-05-30 | SSP v3.0 and POA&M written (Plant 1 scope) |
| 2025-06-12 | SPRS Basic Assessment score of 74 posted (self-assessment, Plant 1 scope) |
| 2026-06-15 to 2026-07-02 | Intake: evidence requests, exports, documents, contracts, inventories, obligations register |
| 2026-07-06 to 2026-07-31 | BIA interviews, risk assessment and gap analysis fieldwork |
| 2026-07-27 to 2026-07-31 | 2026 policy revisions (POL-01 to POL-05) and new standards drafted from the gaps |
| 2026-08-03 to 2026-08-21 | Control assessment by the co-sourced internal audit firm (plant walkthroughs 2026-08-11 to 2026-08-13): operating tests of controls already in place; design review of the draft policies and standards |
| 2026-09-17 | Results to the audit committee. Deliverables and policies approved by the Chief Operating Officer; High risks, risk appetite, and budget approved by the Chief Executive Officer |
| 2026-09-30 | Corrected SPRS Basic Assessment score due (Director of Trade Compliance and Contracts) |
| 2026-10-01 | 2026 policies take effect |
| 2026-11-10 | Planned start of CMMC Phase 2 (32 CFR 170.3(e)(2)); suspended by the DoD (Department of War) CIO memorandum of 2026-07-13 (DoD Class Deviation 2026-O0025, Revision 3) |
| 2027-02 (planned) | Readiness re-check by the co-sourced internal audit firm: operating effectiveness of the controls the 2026 policies and standards introduced, after at least one quarter of operation, and the POA&M items |
| 2027-03-08 to 2027-03-19 | Target window for the Level 2 certification assessment by a C3PAO (voluntary while Phase 2 is suspended) |

## 7. Facts added while completing the deliverables (fictional)

| Topic | Added fact | Used in |
|---|---|---|
| Revenue split | Plant 1 machined parts about $132 million, Plant 2 assemblies and additive parts about $98 million, services line about $10 million, over about 250 production days: about $528,000, $392,000, and $40,000 of shipments per production day (EV-042) | P05, P01 |
| Cyber insurance | $15 million aggregate limit, $500,000 retention. The carrier's panel supplies breach counsel and forensics; notice goes through the carrier hotline before vendors are engaged (EV-039) | P01, P08 |
| MSSP terms | Call to the Security Manager within 30 minutes of a high-severity alert; the SIEM keeps 1 year of searchable logs (EV-019) | P02, P08 |
| Workforce activity | 96 terminations and 41 internal transfers in the 12 months to 2026-06-30 (EV-004); the last enclave access review was completed 2026-02-27 (EV-006); the June 2026 phishing simulation click rate was 6.1% (EV-028) | P07 |
| Budget | FY2027 security plan approved by the Chief Executive Officer on 2026-09-17: $1.62 million one-time and $540,000 a year | P01 |
| Services line | About 30 build and engineering jobs a month for three commercial customers; their files arrive and leave through the MFT gateway and are processed in the enclave (EV-043, EV-018) | P05, P09 |
| Vendors | About 60 IT, OT, and service vendors have access to company systems or data (EV-036); 12 are Tier 1 under the P09 tiering approach | P09 |
| Recovery and connectivity | The 2025-04 PLM restore test took 9 hours (EV-017); Plant 1 has two internet circuits and Plant 2 one (EV-012); Plant 2 local server logs are kept 30 days (EV-AC-2) | P05, P07 |
| Sampling populations | 71 new hires with enclave accounts (EV-004); 164 change tickets in 2026 Q2 (EV-014); 38 cloud servers (EV-018); 74 Critical and High vulnerability findings in Q1-Q2 2026 (EV-013); 14 incidents in 12 months (EV-026); 69 July 2026 visits on gate cameras (31 Plant 1, 38 Plant 2) (EV-PE-3) | P03, P07 |
| Assessment findings | 2 of 25 terminations removed late (EV-051, EV-AC-2); 9 Plant 2 operators left without shared passwords changing (EV-AC-2); prior owner's IT contractor account active on the Plant 2 MES server (found and disabled 2026-08-12, EV-AC-2); 11 of 38 Plant 2 July visits missing from the paper log and 2 unescorted visitors (EV-PE-3); drawings in recycling in 3 of 5 Plant 2 cells (EV-MP-6); 5 unowned USB drives (EV-MP-7); default passwords on 2 additive printer panels (EV-IA-5); 6 Plant 2 keys from the prior owner unaccounted for (EV-PE-3); MSSP test alert escalated in 18 minutes (EV-SI-4) | P03, P07 |
| Suppliers and sharing | 31 allow-listed sharing domains in the enclave suite (EV-034); 8 of 22 CUI suppliers have verified SPRS status; 13 of 22 have current DFARS flowdown (EV-056) | P03, P09 |
| Plant 2 scoping decision | Options reviewed 2026-07-29; integrate Plant 2 by 2027-01-31, with a fallback decision on that date to make Plant 2 a non-CUI site | P03 |
| AI tool details | AI-001 enabled 2026-05-11 for 20 users (EV-044) and disabled 2026-09-17; 14 of 61 suite project sites open to all enclave users (P10 section 4); AI-002 in use since 2025-11, model updated twice without notice; AI-003 in use since 2026-03 (EV-044); AI-004 in use since 2026-02 by about 400 users (EV-044), 2 July prompts with CUI referred 2026-07-29 (EV-057); AI-005 enabled by vendor default 2026-04 (about 1,900 applicants a year) (EV-044, EV-004) and disabled 2026-09-17; AI review group first meets 2026-10-06 | P10, P01 |
| Exercises and documents | Policies approved 2026-09-17, effective 2026-10-01; SSP v4.0 approved 2026-09-17; CUI exfiltration tabletop with DIBNet drill 2026-11-18; Plant 2 ransomware exercise 2027-02-24; medium assurance certificates valid to 2027-05 (EV-027); services agreements require notice within 72 hours of confirming a security incident affecting customer data (EV-032) | P06, P02, P08 |
