# Scenario facts: Cris Santos Company | Communications | Enterprise

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, court decision, or Federal Register document, the citation is given. Legal status was checked against eCFR (point in time 2026-09-23), the Federal Register (searched through 2026-10-05), and govinfo on 2026-10-05.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (publicly traded SEC registrant; parent of the operating carrier subsidiaries) |
| Business | Regional broadband and wired telecommunications carrier (NAICS 517111). Incumbent local exchange carrier (ILEC) in rural and suburban territories, with competitive fiber in adjacent metro areas. Services: consumer fiber and DSL broadband; wireline voice (legacy copper local exchange service and interconnected VoIP over fiber); business services (dedicated Ethernet, wavelengths, managed network services, hosted unified communications); wholesale transport and wireless backhaul for other carriers; SS7 signaling transport for 14 small rural carriers. **No** video service, **no** wireless (CMRS) service, **no** submarine cable or cable landing station |
| Location | Headquartered in Florida. ILEC and fiber territories in Florida, Georgia, South Carolina, and North Carolina: 410 central offices, about 9,600 remote terminals and cabinets, two network operations centers (NOC-1 in Florida, NOC-2 in Georgia), and two company data centers (DC-1 Florida, DC-2 Georgia). **State breach laws are handled generically:** notify under the law of each state where affected individuals reside, with Florida as the worked example |
| Workforce | 12,000 employees: about 4,800 field technicians and construction staff, 2,600 customer care and sales, 1,050 network operations and engineering, 1,100 IT and security (including about 150 in security and GRC), and 2,450 in corporate, finance, billing, and other functions |
| Customers | About 3.0 million accounts (2.89 million residential, 110,000 business). About 2.6 million broadband subscribers (1.75 million fiber, 0.85 million DSL). About 1.15 million voice lines on about 1.02 million accounts: 520,000 legacy copper lines and 630,000 interconnected VoIP lines. 1,900 enterprise and government accounts have a dedicated account representative and a contract that addresses CPNI protection. 64 wholesale carrier customers |
| Revenue | About $4.8 billion a year (fictional), about $13.2 million per calendar day. Not SBA-small (the SBA standard for NAICS 517111 is 1,500 employees; 13 CFR 121.201) |
| Regulatory status | **Telecommunications carrier** for local exchange, interexchange, and wholesale common carrier services (47 U.S.C. 153; the CPNI rules use this definition, 47 CFR 64.2003(o)). **Interconnected VoIP provider**, which the CPNI rules treat as a carrier (64.2003(o)). **Broadband internet access provider**: after *Ohio Telecom Ass'n v. FCC* (6th Cir. Jan. 2, 2025), broadband is an information service, and the FCC conformed its rules on 2025-08-08 (90 FR 38406). **Wireline, interconnected VoIP, and SS7 provider** for outage reporting (47 CFR 4.3, 4.9(d), (f), (g)). **Telecommunications carrier under CALEA** (47 U.S.C. 1001(8)(A); 47 CFR Part 1, Subpart Z). **Federal contractor**: circuits and managed services for federal agencies under contracts that include FAR 52.204-23, 52.204-25, and 52.204-30 |
| Added at this size | SEC cybersecurity disclosure (Form 8-K Item 1.05, including the Item 1.05(d) delay for carriers subject to 47 CFR 64.2011; Reg S-K Item 106); SOX IT general controls; growth by acquisition (three rural carriers acquired 2025-2026); federal contract reporting clauses; two service lines that business customers rely on for their own controls (SOC 2) |
| Not in scope | CMRS-only rules, including SIM change authentication (47 CFR 64.2010(h)); Emergency Alert System rules (no video or broadcast service); FCC submarine cable landing license rules (C-COMMUNICATIONS-R04; no cable or SLTE); covered 911 service provider rules (47 CFR 9.19), because 911 routing to PSAPs is provided by state and regional NG911 system service providers, not the company; HIPAA (the company signs no business associate agreements, and SL-2 terms prohibit storing PHI); payment card data (tokenized by the payment processor; PCI DSS duties are contractual and outside this sample) |

## 2. People (role titles only)
| Role | Duties |
|---|---|
| Board (audit committee plus a risk and technology committee) | Cyber oversight (Item 106 governance); the risk and technology committee receives quarterly cyber risk reporting |
| Chief Executive Officer; Chief Financial Officer | Accept Very High risk; take part in materiality determinations with the disclosure committee |
| Chief Information Security Officer (CISO) | Program owner; reports to the CEO and quarterly to the risk and technology committee |
| Chief Compliance Officer | Regulatory compliance program; **CPNI compliance officer**; signs the annual CPNI certification for each operating carrier subsidiary (47 CFR 64.2009(e)) |
| Chief Privacy Officer | Privacy program; breach determinations with counsel, including the CPNI "reasonable determination" (64.2011(b)) |
| Chief Risk Officer | Enterprise risk management (ERM); owns the enterprise risk register |
| Chief Network Officer | Network engineering and operations, both NOCs; authorizes NORS filings |
| Director, Lawful Intercept Compliance | **CALEA senior officer** for the main operating company (47 CFR 1.20003(a)); reports to the General Counsel |
| GRC team (10), Security Operations Center (24x7, in-house), Network Operations Centers (24x7, two sites), Internal Audit (in-house) | Three lines model |
| Disclosure committee | Form 8-K materiality decisions (General Counsel chairs) |

## 3. Systems
| ID | System | Notes |
|---|---|---|
| SYS-01 | Converged BSS: billing, customer care (CRM and agent desktop), CPNI approval flags, account passwords | Commercial billing software, customer-managed on Cloud provider A. System of record for about 2.7 million accounts; AQ-02 and AQ-03 still bill on their own legacy systems |
| SYS-02 | OSS: network inventory, provisioning and activation orchestration, service assurance and trouble ticketing, workforce management | Cloud provider A, with adapters to element managers |
| SYS-03 | Usage mediation, rating, and CDR store (36 months of call detail for all voice lines) | Cloud provider A; collectors in DC-1 and DC-2 pull CDRs from the voice core |
| SYS-04 | Customer portal, mobile app, and API gateway | Cloud provider A; about 1.9 million registered users |
| SYS-05 | Identity platform: SSO, MFA, privileged access management (PAM), identity governance | AQ-02 and AQ-03 workforce still on their legacy directories |
| SYS-06 | Voice core: IMS core and softswitches, session border controllers (SBCs), 61 legacy TDM switches, company-owned STP pairs, 911 trunks to NG911 system service providers | On-premises in central offices; TDM retirement planned for 2028 |
| SYS-07 | IP/MPLS backbone, metro and access network: core and edge routers, broadband network gateways, OLTs, DSLAMs, cabinet switches, DNS and DHCP | About 41,000 managed network elements |
| SYS-08 | Network management plane: NOC surveillance, element managers, TACACS+ servers, jump hosts, configuration archive, network telemetry | DC-1 and DC-2. TACACS+ with named accounts and MFA covers 82% of network elements |
| SYS-09 | Lawful-intercept (CALEA) platform: intercept access functions, mediation, delivery to law enforcement | Isolated enclave in DC-1 and DC-2; about 30 authorized employees. Covered by the CALEA SSI plans, outside the SSP boundary |
| SYS-10 | Contact center platform (CCaaS: routing, IVR, recording) and the customer-service chatbot | Vendor SaaS; used by in-house agents and 3 outsourced care vendors (about 2,600 agents) |
| SYS-11 | Multi-cloud estate (two public cloud providers, vendor-agnostic) plus DC-1 and DC-2 | Cloud A: OSS/BSS, mediation, portal. Cloud B: SL-2 UCaaS platform, data and AI platform |
| SYS-12 | Endpoints: about 15,500 laptops and desktops and 6,200 field technician tablets | EDR on laptops and desktops; tablets under mobile device management |
| SYS-13 | ERP and payroll (SOX-relevant) | SOX IT general controls tested annually |
| SYS-14 | About 1,400 third-party vendors (230 with CPNI or customer personal information) | Tiered third-party risk program |
| SYS-15 | AI portfolio (12 use cases) | Governed by an AI council formed in 2025 |

**SSP system (P02):** the *Customer Billing and Network Operations Platform (OSS/BSS)*: SYS-01, SYS-02, SYS-03, and SYS-04 with their network management adapters, a high-value system categorized Moderate with confidentiality treated at High for CPNI, inheriting common controls from the enterprise platform.

## 4. Current security posture: mostly compliant, with targeted gaps
**In place today:**
- A mature program aligned to CSF 2.0, with the CISA Cross-Sector Cybersecurity Performance Goals used to prioritize network work
- Annual risk analysis tied to ERM (NIST IR 8286)
- A policy hierarchy of policies, standards, procedures, and exceptions
- 24x7 SOC and two 24x7 NOCs
- PAM and quarterly access certification for IT systems
- Immutable backups for cloud workloads
- Annual DR tests for tier-1 IT systems; storm and outage procedures exercised every hurricane season
- Customer authentication that meets 47 CFR 64.2010 for in-house care, the main portal, and retail stores
- Annual CPNI certifications filed by March 1; CALEA SSI policies on file for the main operating company
- Tiered vendor reviews
- Annual SOC 2 Type 2 report for the managed network services line (SL-1)
- SEC Item 106 disclosure in the 10-K

**Targeted gaps:**
1. **Acquisition integration.** Of three carriers acquired in 2025-2026, AQ-02 and AQ-03 still run legacy billing, legacy identity directories, and flat management networks that reach the enterprise over site VPNs. AQ-02's customer portal resets passwords with date of birth and the last 4 digits of the SSN. AQ-03's CALEA SSI policies were not refiled within 90 days of closing (47 CFR 1.20005(a)).
2. **Network management plane.** About 7,400 legacy access elements (DSLAMs, older OLTs, and cabinet switches, including about 2,900 at AQ-02 and AQ-03) still use shared local administrator accounts outside TACACS+ and MFA. In 2024 a state-sponsored threat group was publicly reported to have infiltrated at least eight U.S. communications companies by exploiting publicly known vulnerabilities and avoidable weaknesses (FCC, 90 FR 58006).
3. **Network security monitoring.** The SIEM covers IT and cloud fully, but only 58% of network element logs, and no flow telemetry from the AQ networks. NOC-to-SOC handoffs are manual.
4. **Outsourced care.** Three care vendors (about 2,600 agents) handle 35% of calls. Agents at one vendor released call detail after non-compliant authentication in sampled calls (64.2010(b)), and 91% of vendor agents have completed CPNI training.
5. **AI.** 12 AI use cases; 8 have completed council review. The customer-service chatbot with account access is in production and shows a language accuracy gap.
6. **Materiality.** The materiality playbook does not yet build in the 64.2011 law enforcement hold or the Item 1.05(d) EDGAR correspondence, and it has not been exercised with the three disclosure committee members who joined in 2026.
7. **Legacy.** 61 TDM switches and two AQ-02 SBC clusters run releases past vendor support, and the AQ legacy billing systems send no audit logs to the SIEM.
8. **Third parties.** Contracts inherited from AQ-02 and AQ-03, and the care vendor and chatbot contracts, lack CPNI terms or allow 72 hours for incident notice.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 | All applicable regulations across the enterprise: FCC CPNI rules (primary, 47 CFR 64.2001-64.2011 as in force on 2026-09-23), CALEA SSI rules (47 CFR Part 1, Subpart Z), FCC outage reporting (47 CFR Part 4), SEC Form 8-K Item 1.05 and Reg S-K Item 106, state breach laws (Florida worked example), FAR reporting clauses, and a NIST CSF 2.0 network security benchmark |
| P08 | Network intrusion exposing CPNI across the management plane and the CDR store, including the **SEC materiality assessment and Form 8-K Item 1.05** step, the Item 1.05(d) CPNI delay, and a multi-state notification workflow |
| P09 | SOC 2 Type 2 readiness across two service lines offered to business customers: SL-1 managed network services and SL-2 hosted unified communications |
| P10 | Enterprise AI portfolio (12 use cases), with the council operating model and a full assessment of the customer-service chatbot with account access (registry default kept: it is the highest-exposure customer-facing use case at this size) |
| Cloud | Multi-cloud (vendor-agnostic) with common controls; AWS, Azure, and Google Cloud names appear only in the P04 equivalents table |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-06-01 to 2026-07-31 | Enterprise risk analysis and gap analysis |
| 2026-07-13 to 2026-08-28 | Control assessment (Internal Audit, third line) |
| 2026-09-10 | Results to the risk and technology committee of the board |

## 7. Facts added for the deliverables
These facts were added while building the deliverables. They do not change sections 1-6.

**Revenue mix (fictional, annual).** Consumer broadband $2.30 billion; consumer voice $0.45 billion; business and enterprise $1.45 billion (including SL-1 $0.32 billion and SL-2 $0.21 billion); wholesale $0.45 billion; other $0.15 billion.

**Additional roles (titles only).**
| Role | Duties in the deliverables |
|---|---|
| Chief Operating Officer (COO) | Authorizing official equivalent for the OSS/BSS (P02); chairs the crisis management team |
| Chief Information Officer (CIO) | IT operations; owns the enterprise platform (common control provider) |
| Chief Customer Officer | Customer care, outsourced care vendors, portal, and chatbot (business owner of AI-001) |
| General Counsel | Chairs the disclosure committee; supervises the Director, Lawful Intercept Compliance |
| Chief Audit Executive | Heads Internal Audit; reports to the audit committee; leads the P07 assessment |
| Chief Data Officer | Chairs the AI council |
| Chief Human Resources Officer | Onboarding, terminations, training records |
| Chief Accounting Officer | SOX program owner; member of the disclosure committee |
| Vice President, OSS/BSS Platforms | System owner of the OSS/BSS (P02) |
| Vice President, Billing and Revenue Assurance | BSS business configuration, CPNI approval flags, mediation |
| Vice President, Network Operations Center | Both NOCs; NORS, DIRS, and PSAP notifications |
| Vice President, Regulatory Affairs | FCC filings (CPNI certifications, CALEA filings through CEFS, NORS final reports); tracks rule changes |
| Vice President, Integration Management Office | Integration of acquired carriers |
| Vice President, Managed Services | SL-1 service line owner |
| Vice President, Unified Communications | SL-2 service line owner |
| Vice President, Marketing | Campaigns that use CPNI; opt-out notices |
| Vice President, Corporate Communications | Media and customer communications during incidents |
| Vice President, Investor Relations | Investor communications; member of the disclosure committee |
| Vice President, Facilities and Real Estate | Physical security of central offices and data centers |
| Director of Security Operations | Runs the SOC; incident commander for security incidents |
| Director of Identity and Access Management | Identity platform (SYS-05) |
| Director of Network Security Engineering | Management plane security: TACACS+, jump hosts, element hardening (common control provider) |
| Director of Cloud Platform Engineering | Cloud landing zones in both clouds (common control provider) |
| Director of Endpoint Engineering | Workstations, tablets, EDR (common control provider) |
| Director of Third-Party Risk Management | Vendor tiering, CPNI contract terms, SOC report reviews (in the GRC team) |
| Director of Outsourced Care | Oversight of the three care vendors |
| BSS Application Manager | Day-to-day BSS administration and change control (reports to the Vice President, OSS/BSS Platforms) |
| Data science lead | Model validation and fairness testing for the AI council |

**Acquired carriers.** AQ-01 (closed 2025-03-31; about 38,000 accounts) is fully integrated. AQ-02 (closed 2025-10-31; about 145,000 accounts) and AQ-03 (closed 2026-05-15; about 92,000 accounts) remain separate carrier subsidiaries until they are merged into the main operating company (planned 2027). Together they have about 1,050 employees and 58 central offices (included in the 410). AQ-02 refiled its CALEA SSI policies on 2026-01-20, within 90 days of closing; AQ-03's refiling was due by 2026-08-13 and is still open. BSS migration targets: AQ-02 by 2027-03-31; AQ-03 by 2027-09-30.

**Outsourced care.** Three U.S.-based care vendors (CV-1, CV-2, CV-3) handle about 35% of care calls (about 1.1 million calls a month in total), using the BSS agent desktop through the identity platform. The sampled authentication failures were at CV-2.

**Federal contracts.** About 140 federal agency circuits and managed service contracts (about $60 million a year). The company has no covered telecommunications equipment in its network; AQ-03 due diligence confirmed the same for its network before closing.

**Service lines offered to business customers (P09).** SL-1 managed network services (managed SD-WAN, managed firewall, managed Wi-Fi) for about 3,400 business customers; SOC 2 Type 2 (Security, Availability, Confidentiality) every year since 2024. SL-2 hosted unified communications (cloud voice, collaboration, and contact center seats) for about 1,250 business customers and about 96,000 seats, hosted on Cloud provider B; no SOC 2 report yet.

**Disclosure committee membership (P08).** General Counsel (chair), CFO, Chief Accounting Officer, CISO, Chief Privacy Officer, Chief Compliance Officer, Chief Risk Officer, and Vice President, Investor Relations, advised by outside securities counsel. The Chief Privacy Officer, Chief Risk Officer, and Vice President, Investor Relations joined in 2026.

**CPNI certifications.** The certifications for calendar year 2025 were filed on 2026-02-27 for the main operating company, AQ-01, and AQ-02, each signed by the Chief Compliance Officer as an officer of that carrier. AQ-03 joined after that filing; its first certification under company ownership is due by 2027-03-01.

**Recording consent.** Care calls and SL-2 recordings use an all-party consent announcement in every state, using Florida (Fla. Stat. 934.03(2)(d)) as the worked example.
