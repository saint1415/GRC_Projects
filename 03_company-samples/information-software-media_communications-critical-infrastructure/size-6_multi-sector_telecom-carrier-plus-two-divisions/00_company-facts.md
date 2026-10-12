# Scenario facts: Cris Santos Company | Communications | Multi-Sector

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Legal status was checked against eCFR (point in time 2026-09-23), the Federal Register API (through 2026-10-05), and govinfo on 2026-10-05.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company Holdings, Inc. (publicly traded SEC registrant) |
| Structure | A holding company with three divisions and corporate shared services. Each division operates through wholly owned subsidiaries |
| Division 1: Telecom Carrier (NAICS 517111), **focus of this scenario** | Regional broadband and wired telecommunications carrier in 14 states: 9 incumbent local exchange carrier (ILEC) operating companies in rural and suburban territories and 1 competitive (CLEC) fiber affiliate in metro areas. Services: fiber and DSL broadband internet access, wireline voice (copper local exchange and toll), interconnected VoIP, and enterprise, government, and wholesale transport (including fiber backhaul to about 9,800 cell sites). About 31,000 employees. **No** wireless (CMRS) service, **no** video or broadcast service, **no** submarine cable or cable landing station. Its duties as a telecommunications carrier and interconnected VoIP provider (CPNI, CALEA, outage reporting) are decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv) |
| Division 2: Network Engineering Services (NAICS 541330, sector 54 Professional, Scientific, and Technical Services) | Network design, engineering, construction management, equipment procurement and staging, and **Managed Network Operations** (a 24x7 network operations service) for external network operators: rural carriers, municipal broadband utilities, and electric cooperatives. Also engineers networks for 12 federal civilian agency contracts. About 35% of its work is for the Carrier and Tower divisions under intercompany service agreements. About 6,500 employees |
| Division 3: Tower and Fiber Infrastructure (sector 53 Real Estate and Rental and Leasing) | Owns and leases space on about 14,500 towers and 2,100 rooftop and in-building sites, and leases about 26,000 route miles of dark fiber and conduit under long-term, individually negotiated contracts. Tenants are national wireless carriers, the Carrier division, broadcasters, and public safety agencies. About 2,000 employees |
| Corporate shared services | Identity, security operations, cloud and network platforms, ERP (finance, HR, procurement), legal, and internal audit. About 5,500 employees |
| Location | Headquartered in Florida. The Carrier serves 14 states in the Southeast, Mid-Atlantic, and lower Midwest; Engineering works in 24 states; towers are in 22 states. **State law is handled generically** ("each state where affected individuals reside"), with Florida as the worked example. Florida is the Carrier's largest state |
| Workforce / revenue | 45,000 employees; about $18.0 billion revenue (fictional) |
| SBA size status | Not small (SBA standard for NAICS 517111 is 1,500 employees; 13 CFR 121.201) |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): submarine cable rules, CMRS-only CPNI rules, the EAS cybersecurity order, the FTC Safeguards Rule, DFARS 252.204-7012 and CMMC, HIPAA (Engineering), CCPA, and PCI DSS (Tower) do not apply; CIRCIA is not yet in effect |
| FAR overhaul clause numbers | Background fact, not scored in P03. Contracts awarded before the contracting agency adopted its FAR Part 40 class deviation keep the clauses this sample cites (FAR 52.204-21, 52.204-23 and 52.204-25) until they are modified. New awards under the deviation carry FAR 52.240-93, which has the same 15 safeguarding requirements as FAR 52.204-21, and FAR 52.240-91, which replaces the separate Kaspersky, Section 889 and FASCSA reports with one report within 72 hours. Sources: SRC-FAR-RFO-PART40 |

## 2. People (role titles only)
| Role | Duties |
|---|---|
| Board risk committee | Group cyber oversight; accepts Very High risks; approves group policy POL-01 and POL-03 |
| Group CISO | Group security program, group standards, common controls (SYS-G1 to SYS-G3); co-accepts High risks |
| Group Chief Risk Officer | Group risk register and enterprise risk management roll-up; co-accepts High risks; chairs the Group AI council |
| Group Chief Privacy Officer | Data classification, CPNI and personal information use across divisions, state privacy law tracking |
| Group General Counsel | Intercompany agreements, customer and tenant contracts, the multi-regulator notification matrix |
| Disclosure committee | SEC materiality of cybersecurity incidents (Form 8-K Item 1.05) |
| Group internal audit | Assesses common controls once and samples division controls; reports to the board audit committee |
| Division presidents (3) | Accept Moderate risks for their division |
| Division security and compliance leads (3) | Division registers, division supplements, division regulators; accept Low risks |
| Carrier Senior Vice President, Regulatory and Compliance | **CPNI compliance officer**; signs the annual CPNI certifications (47 CFR 64.2009(e)); owns CPNI breach determinations with counsel |
| Carrier Vice President, Network Security and Lawful Intercept | **CALEA senior officer** named in each operating company's system security and integrity (SSI) policy (47 CFR 1.20003(a)) |
| Carrier Network Operations Center (NOC) director | 24x7 NOC; outage escalation; NORS and DIRS filings; 911 special facility notices |
| Carrier customer operations vice president | Contact centers, the two outsourced contact center vendors, and the AI chatbot (business owner) |
| Engineering Managed Network Operations general manager | The Managed Network Operations service and its customer commitments |
| Engineering federal contracts compliance manager | FAR clause compliance for the 12 federal contracts |
| Tower site operations director | Antenna structure compliance (47 CFR Part 17), the tower Alarm Monitoring Center, site access |
| Group procurement director | Supplier screening, including covered equipment checks for all three divisions |
| Other owners named in the deliverables | Group: identity, SOC, cloud platform, and network directors; HR director; chief audit executive; chief accounting officer; communications lead. Carrier: Vice President, Network Operations (approves NORS filings); OSS/BSS platform vice president (system owner of the SSP system); network engineering, billing, enterprise operations, field operations, and marketing vice presidents; digital channels, service delivery, facilities, and credit and collections directors; Carrier security and compliance lead. Engineering: operations, construction, and supply chain leaders; Engineering security and compliance lead. Tower: lease administration, fiber operations, and leasing leaders; Tower security and compliance lead |

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv). Suppliers are in the [vendor register](step-00_P00_intake/vendor-register.csv).

| ID | System | Owner | Holds CPNI or personal information? |
|---|---|---|---|
| SYS-G1 | Group identity platform (single sign-on, MFA, privileged access management, identity governance) | Corporate | Identities only |
| SYS-G2 | Group SOC: SIEM, EDR, security orchestration | Corporate | Logs (may contain CPNI) |
| SYS-G3 | Group cloud platform: landing zones on two public cloud providers (vendor-agnostic), hub network, key management, immutable backup vault | Corporate | Hosts division workloads |
| SYS-G4 | Group ERP (finance, HR, payroll, procurement) | Corporate | Employee and supplier data |
| SYS-C1 | Carrier OSS: network inventory, provisioning and activation, field workforce management, and the **service assurance platform** (fault monitoring, alarm correlation, trouble ticketing) | Carrier | Yes (service records, addresses, tickets) |
| SYS-C2 | Carrier BSS: billing, CRM, CPNI approval flags, account passwords, agent desktop | Carrier | Yes (CPNI and PII) |
| SYS-C3 | Carrier voice mediation and rating, with the call detail record (CDR) store (24 months online) | Carrier | Yes (call detail for every voice line) |
| SYS-C4 | Carrier customer portal, mobile app, and API gateway | Carrier | Yes |
| SYS-C5 | Carrier network management plane: element management systems, AAA (TACACS+ and RADIUS), jump hosts, configuration backup, network syslog collectors, in 6 regional NOC data centers | Carrier | Indirect |
| SYS-C6 | Carrier voice core: IMS and softswitches, 140 session border controllers (SBCs), SS7 and Diameter signaling, legacy TDM switches, 911 trunks to NG911 system service providers | Carrier | Yes (CDRs generated here) |
| SYS-C7 | Carrier IP/MPLS core and access network: core and edge routers, broadband network gateways, optical line terminals (OLTs), DSLAMs, DNS and DHCP | Carrier | Yes (subscriber IP assignments) |
| SYS-C8 | Carrier lawful-intercept (CALEA) mediation and delivery | Carrier | Yes (intercept content and court orders) |
| SYS-C9 | Carrier contact center platform (CCaaS: routing, IVR, call recording) used by in-house agents and two U.S.-based outsourced contact center vendors | Carrier | Yes |
| SYS-C10 | Carrier customer-service AI chatbot with account access (web and app chat) and an AI voice agent pilot in the IVR, on a vendor's large language model platform | Carrier | Yes |
| SYS-E1 | Engineering Managed Network Operations platform: a tenant on the SYS-C1 service assurance platform, remote access gateways into 64 customer networks, and monitoring collectors at customer sites | Engineering | Customer network data; some customer subscriber data in tickets |
| SYS-E2 | Engineering design and project delivery: GIS and CAD design tools, project management, and a separate enclave for federal contract information (FCI) | Engineering | FCI; customer network designs |
| SYS-T1 | Tower site and lease management (vendor SaaS): leases, tenant applications, site access requests, landowner rent payments | Tower | Yes (about 11,800 landowners: names, taxpayer IDs, bank accounts) |
| SYS-T2 | Tower lighting and site monitoring: remote monitoring units (RMUs) at 6,200 lit towers, the Alarm Monitoring Center console (a tenant on the SYS-C1 service assurance platform), and smart locks at 9,000 sites | Tower | Site access records |
| SYS-T3 | Fiber route GIS and dark fiber records (route maps, splice points, customer circuits) | Tower | Network topology (sensitive) |

**SSP system (P02):** the *Network Operations and Customer Billing Platform (OSS/BSS)*: SYS-C1, SYS-C2, SYS-C3, SYS-C4, and SYS-C5, inheriting common controls from SYS-G1 to SYS-G3, with interfaces to SYS-C6, SYS-C7, SYS-C9, SYS-C10, and the two other divisions' tenants on the shared service assurance platform (SYS-E1, SYS-T2).

## 4. Where the evidence is
This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Rows are grouped by division (Group, Telecom Carrier, Network Engineering Services, Tower and Fiber Infrastructure). Every item has a source system, an owner, and as-of and collected dates.
- **Which rules apply** to each division and to the group is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps** against the FCC CPNI rules, CALEA, outage reporting and the covered equipment report (Carrier), FAR 52.204-21, 52.204-23 and 52.204-25 and the MNO customer contracts (Engineering), the antenna structure lighting rules and landowner data duties (Tower), and the group-wide rules are judged in the gap analyses (P03), which also number the ten group gaps cited across this sample, and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 | Carrier: FCC CPNI rules (47 CFR 64.2001-64.2011) as primary, with CALEA SSI rules, outage reporting (47 CFR Part 4), and the covered equipment report (47 CFR 1.50007). Engineering: FAR 52.204-21 for its federal contracts plus customer commitments. Tower: antenna structure lighting rules (47 CFR Part 17) plus landowner data duties. Group: SEC disclosure and state breach law. A regulation-by-division matrix ties them together |
| P08 | A network intrusion exposing CPNI that spans divisions: entry through an Engineering remote access gateway, movement into the Carrier management plane in the acquired regions, theft of call detail records, and loss of tower lighting monitoring during containment |
| P09 | SOC 2 scoped per division: Engineering's Managed Network Operations service is in scope (first Type 2 by the end of 2027); the Carrier and the Tower division are out of scope, with reasons |
| P10 | Group AI governance program: group standard, division use cases, and the regulator-specific rules, with the customer-service chatbot with account access (registry default) as the focus use case |
| Cloud | Shared corporate platform on two public cloud providers plus division workloads, vendor-agnostic |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-03-30 to 2026-04-24 | Intake: evidence requests, exports, walk-throughs, inventories, obligations register |
| 2026-05-04 to 2026-07-31 | Group and division BIAs, risk analyses, and gap analyses |
| 2026-06-01 to 2026-06-26 | Group policies v2026 drafted from the gaps found so far (P06); the Carrier supplement was aligned to the drafts on 2026-06-30 |
| 2026-07-06 to 2026-08-28 | Common control assessment (group internal audit) plus division samples: operating tests of controls already in place; design review of the draft v2026 policies |
| 2026-08-27 | Group AI council assessment |
| 2026-09-17 | Results and treatment plans approved by the board risk committee; deliverables and group policies v2026 approved (policies effective 2026-10-01) |
| 2027-04 (planned) | Follow-up assessment: operating effectiveness of the controls the v2026 policies introduced, after at least one quarter of operation |

## 7. Facts added while building the deliverables
These facts were added so the deliverables could be completed. They do not change sections 1 to 6.

| Topic | Added fact |
|---|---|
| Registry defaults kept | The registry's primary system (OSS/BSS), incident (network intrusion exposing CPNI), and AI use case (customer-service chatbot with account access) all fit the Carrier division at this size and were kept. The SSP covers the Carrier's OSS/BSS because it is the system other divisions share (the service assurance platform) and it holds the group's largest CPNI stores |
| Carrier customers | About 4.9 million mass-market accounts (4.6 million residential, 300,000 small business); about 4.6 million broadband subscribers (2.9 million fiber, 1.7 million DSL); about 1.9 million voice lines on about 1.6 million accounts (800,000 copper lines, 1.1 million interconnected VoIP lines); about 41,000 enterprise, government, and wholesale accounts. About 1.4 million accounts are in Florida. The acquired regions hold about 610,000 voice lines |
| Carrier operating companies | 10 filers for CPNI certifications (9 ILECs, 1 CLEC). SSI policies, filings and certifications are in EV-034 and EV-036. The Carrier sells dedicated transport to federal civilian agencies under contracts that include FAR 52.204-25 (EV-035) |
| Contact centers | About 6,800 in-house agents and about 2,100 agents at two U.S.-based outsourced contact center vendors, all on SYS-C9 and the SYS-C2 agent desktop |
| AI chatbot | In production since 2025-11-03 for signed-in portal and app users; about 1.1 million sessions per month (EV-047). The account recovery feature (group gap 4) handled about 23,000 sessions before it was disabled (EV-086). An AI voice agent in the IVR has been in pilot since 2026-05-11 for outage and billing questions (EV-085) |
| Engineering scale | 64 Managed Network Operations customers (31 rural carriers, 19 municipal broadband utilities, 14 electric cooperatives) with about 210,000 monitored network elements. 41 contracts require notice of a security incident affecting the customer within 24 hours, and 23 within 72 hours. Contracts also require notice within 30 minutes of a detected outage that may be reportable, so customers can meet their own NORS and 911 clocks. The 31 carrier customers' tickets can contain their subscribers' names, addresses, and service details. No Department of Defense contracts, no CUI, and no DFARS 252.204-7012 clauses |
| Tower scale | About 6,200 of the 14,500 towers are registered antenna structures with FAA lighting specifications. About 11,800 ground-lease landowners are paid through SYS-T1. Dark fiber is leased under individually negotiated contracts; group counsel treats it as private carriage, not a telecommunications service offered to the public (EV-084) |
| States | No division has operations, customers, sites, or landowners in California, Colorado, Texas, or Utah. State comprehensive privacy laws in the states served are assessed by the Group Chief Privacy Officer outside this security sample |
| Revenue split (fictional) | Carrier about $12.4 billion; Engineering about $2.3 billion external; Tower about $3.3 billion. Intercompany work is eliminated in consolidation. Total about $18.0 billion, as in section 1 |
| Cloud | Provider A (primary) hosts the corporate landing zone and the Carrier's OSS, BSS, mediation, portal, and API gateway, plus SYS-E2. Provider B hosts the disaster recovery copies of the BSS and OSS, the immutable backup vault, and the SYS-E1 collectors' aggregation tier. The management plane (SYS-C5), voice core, and lawful-intercept systems are on premises in 6 regional NOC data centers. SYS-T1, SYS-C9, and SYS-C10 are vendor SaaS |
| Risk acceptance | Very Low and Low: division security and compliance lead. Moderate: division president. High: Group Chief Risk Officer with the Group CISO, reported to the board risk committee; temporary only, with a dated plan. Very High: board risk committee only. Risks to 911 call completion, tower lighting, or lawful-intercept confidentiality rated High must be treated, not accepted |
| Deposit model | The Carrier uses an in-house model that combines a consumer report score with account history to decide whether a new residential customer must pay a deposit (about 14% of new orders). It is listed in the P10 inventory |
| Testing finding (P07) | Assessment testing on 2026-08-19 found 212 of the 1,100 legacy tower RMUs still accept the manufacturer's default web administrator password. This became P01 risk TF-014 and POAM-022 (EV-T-IA5) |
| Acquired regions (detail) | The 2 operating companies acquired in 2024 stay on a legacy billing system (hosted in provider A since 2025) until 2027-09-30 (EV-016). Their PSAP outage contacts were last confirmed in 2024 (EV-046) |
| Carrier operations (detail) | 64 retail and payment locations (EV-035); 41 NORS reports filed on time in 2025 (EV-046); the FCC CPNI reporting facility was used once, in 2024, for an insider case (EV-034). At one of the two outsourced contact center vendors, supervisors can override the telephone password prompt, and that vendor's contract lacks 24-hour incident notice terms (EV-038, EV-039). The last biennial CPNI opt-out notice was sent in 2025-10 (EV-037) |
| Engineering operations (detail) | 6 project offices handle federal work; about 40 subcontractors, of which 9 subcontracts involve FCI access. 37 MNO customers require a SOC 2 Type 2 report by the end of 2027; the plan is a Type 1 as of 2027-03-31 and a Type 2 for 2027-04-01 to 2027-09-30 |
| Tower operations (detail) | Cameras at about 2,400 of the 9,000 smart-lock sites. About 5,100 newer RMUs are certified under 47 CFR 17.47(c) and support vendor direct alerting (EV-059) |
| AI program | A Group AI Standard and a Group AI council were established in 2026-04. The P10 inventory lists 10 use cases, including an enterprise generative AI assistant piloted with 3,000 workforce users, a generative design assistant (120 designers), MNO alarm triage, tower inspection imagery analysis (800 towers), and lease abstraction (EV-031, EV-085) |
