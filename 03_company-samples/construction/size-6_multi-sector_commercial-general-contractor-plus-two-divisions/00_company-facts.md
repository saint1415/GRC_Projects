# Scenario facts: Cris Santos Company | Construction | Multi-Sector

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company Holdings, Inc. (publicly traded SEC registrant) |
| Structure | A holding company with three divisions and corporate shared services. Each division is a separate legal subsidiary; corporate shared services sit in the parent |
| Division 1: Commercial Construction (NAICS 236220), **focus of this scenario** | Cris Santos Construction, LLC. Commercial and institutional building general contractor: general contracting, construction management at risk, and design-build for offices, health care facilities, schools, data centers, and federal and defense facilities. About 1,350 active projects. About 31,000 employees, including about 19,000 craft workers. Includes the **Technology and Security Systems Integration (TSSI) unit** (about 900 employees), which installs structured cabling, video surveillance, access control, and building automation controls in client buildings, and sells a remote managed service (monitoring and maintenance of those systems) to 140 clients |
| Division 2: Commercial Property (NAICS 531120, sector 53 Real Estate and Rental and Leasing) | Cris Santos Properties, LLC. Owns and operates 64 commercial properties (office, medical office, industrial, mixed-use) with about 21 million rentable square feet and 18 structured parking facilities. About 1,600 commercial tenants (businesses, not consumers). 9 properties are wholly or partly leased to federal agencies. About 2,400 employees |
| Division 3: Architecture and Engineering (NAICS 541330, sector 54 Professional, Scientific, and Technical Services) | Cris Santos Design, Inc. Licensed architecture and engineering firm. Designer of record for the group's design-build work and for external clients. About 35% of its revenue is federal, mostly Department of Defense architect-engineer task orders that involve controlled unclassified information (CUI). About 7,100 employees |
| Corporate shared services | Identity, network, security operations, cloud platform, finance shared services (ERP, accounts payable, treasury), HR, legal, and internal audit. About 4,500 employees |
| Location | Headquartered in Florida. Operations in 14 states in the Southeast, the Mid-Atlantic, and Texas. No operations or property in California. **State law is handled generically** ("each state where affected individuals reside"), with Florida as the worked example |
| Workforce / revenue | 45,000 employees; about $18.0 billion revenue (fictional): Construction about $14.2 billion, Property about $2.1 billion, A&E about $1.7 billion, after intercompany eliminations |
| Why this combination | Design-build-own. A&E designs, Construction builds, and Property owns and operates. Many projects move through all three divisions, and the divisions share one project delivery and payment platform |

## 2. People (role titles only)
| Role | Duties |
|---|---|
| Board risk committee | Group cyber oversight; accepts Very High risks; approves group policy POL-01 and POL-03 |
| Disclosure committee | SEC materiality of cybersecurity incidents (Form 8-K Item 1.05) |
| Group CISO | Group security program, group policies, common controls (SYS-G1 to SYS-G3, SYS-G5, SYS-G6) |
| Group Chief Risk Officer | Group risk register and enterprise risk management roll-up; co-accepts High risks with the Group CISO |
| Group General Counsel | Notification matrix, contract terms, SPRS affirmation reviews with outside government contracts counsel |
| Group Chief Financial Officer and Group Treasurer | Payment factory (SYS-G4), payment-instruction controls, SEC reporting |
| Director of Federal Contracts Compliance (corporate) | CMMC program office for all divisions: scoping, self-assessments, SPRS entries, flowdown checks |
| Division security and compliance leads (3) | Division registers, division supplements, division regulators and customers; accept Low risks |
| Division presidents (3) | Accept Moderate risks for their divisions. The Construction and A&E division presidents are the **CMMC Affirming Officials** (32 CFR 170.22(a)(1)) for their entities' contractor information systems |
| Systems Integration Director (TSSI unit) | Section 889 screening for installed equipment; custodian of client system credentials; managed service operations |
| Group internal audit | Reports to the board audit committee. Assesses common controls once and samples division controls. Independent of the teams it assesses |

## 3. Systems
| ID | System | Owner | Holds |
|---|---|---|---|
| SYS-G1 | Group identity platform (single sign-on, MFA, privileged access management, identity governance) | Corporate | Identities |
| SYS-G2 | Group SOC: SIEM, EDR, email security, 24x7 monitoring | Corporate | Security logs |
| SYS-G3 | Group cloud platform (commercial landing zone on provider A; disaster recovery and backup vault on provider B) and the group network (WAN, office and jobsite connectivity) | Corporate | All commercial workloads |
| SYS-G4 | Group ERP and treasury payment factory (project accounting, billing, accounts payable, vendor master with bank details, bank connectivity) | Corporate finance shared services | Payment data; FCI (pay applications on federal jobs) |
| SYS-G5 | Group productivity suite (commercial tenant: email, files, chat) | Corporate | FCI; employee PII; must not hold CUI |
| SYS-G6 | **Federal CUI enclave**: a FedRAMP Moderate authorized government-community cloud environment (enclave email and files, virtual desktops with BIM/CAD tools, a CUI file-transfer gateway) | Corporate, operated for Construction federal teams and A&E | CUI (controlled technical information: facility drawings and specifications) |
| SYS-D1 | Construction field systems: jobsite networks, rugged tablets, equipment telematics, drones, field time capture | Construction | FCI; worker data |
| SYS-D2 | TSSI tools: configuration repository and credential vault for client-installed security systems, remote access platform for the managed service | Construction (TSSI unit) | Client facility security details |
| SYS-D3 | Property management platform: lease administration, tenant portal, property accounting with its **own accounts payable** | Property | Tenant contacts, rent and payment data |
| SYS-D4 | Owned-building operational technology: building automation (BAS), access control, video, and parking pay stations at the 64 properties | Property | Badge and video data; card payments (through a parking technology service provider) |
| SYS-D5 | A&E design platform: BIM/CAD authoring, commercial design collaboration service, rendering compute, A&E time and billing | A&E | Client designs (commercial work only) |
| SYS-D6 | AI estimating and bid assistant (vendor SaaS, enterprise tenant) | Construction (also used by A&E cost estimators) | Bid documents; historical costs; FCI |

**SSP system (P02):** the *Project Delivery and Payment Platform (PDPP)*: the shared corporate project management and pay application platform used by all three divisions (the project management SaaS tenant, the integration and payment-instruction services in the group cloud, and the owner and subcontractor portals), inheriting common controls from SYS-G1 to SYS-G5. The PDPP holds FCI and is the group's CMMC Level 1 assessment scope. It must not hold CUI.

## 4. Current security posture: a defined, mostly mature program with group-level gaps
**In place today:**
- Group policies aligned to CSF 2.0, with division supplements
- A common control catalog maintained by the Group CISO's office
- 24x7 group SOC with EDR on all managed endpoints and servers
- Phishing-resistant MFA for administrators, finance and treasury staff, and project executives; number-matching MFA for all other workforce users
- Privileged access management with just-in-time elevation
- Payment factory (SYS-G4) with call-back verification and dual approval for every vendor bank change
- Immutable backups in a separate cloud provider
- CUI enclave (SYS-G6) on a FedRAMP Moderate authorized offering
- Final CMMC Level 1 (Self) for the PDPP scope (status date 2026-01-20) and Final Level 2 (Self) for the CUI enclave (status date 2026-03-16), both entered in SPRS by the Director of Federal Contracts Compliance and affirmed by the division Affirming Officials
- Section 889 submittal screening in the TSSI unit
- Annual Reg S-K Item 106 disclosure; a disclosure committee charter that covers cybersecurity incidents

**Gaps:**
1. **CUI outside the enclave.** Design-build field teams copy CUI-marked drawings from the enclave into the commercial PDPP and commercial email so that superintendents and subcontractors can use them. A data discovery scan on 2026-07-14 found 1,140 CUI-marked files from 9 DoD projects in the PDPP and 212 in commercial mailboxes. The PDPP is not FedRAMP Moderate authorized or equivalent (DFARS 252.204-7012(b)(2)(ii)(D)), and DFARS 252.204-7021(d)(2) allows CUI only on systems with the required CMMC status.
2. **Self-assessment overstated readiness.** The independent pre-assessment by group internal audit (2026-07) found requirements scored MET in the March 2026 Level 2 self-assessment that do not meet every NIST SP 800-171A objective. The enclave SSP has not been updated for the 2026 virtual desktop expansion. The group expects DoD to require Level 2 (C3PAO) on design-build solicitations after Phase 2 begins on 2026-11-10 (32 CFR 170.3(e)(2)).
3. **Uneven payment-instruction controls.** The payment factory verifies bank changes, but the Property division's own accounts payable (SYS-D3) accepts vendor and tenant-refund bank changes with one approver, A&E invoices carry remittance details in emailed PDFs, and owners and tenants have not all been told how the group will (and will not) change its remittance details.
4. **Property building systems.** BAS, access control, video, and parking pay stations sit on flat building networks at 41 of 64 properties. Third-party integrators keep persistent remote access. These systems are not monitored by the group SOC, and the Property division has not documented which group common controls it inherits. Its division supplement was last aligned in 2024.
5. **Section 889 screening is not group-wide.** The TSSI unit screens its submittals, but A&E specifications and Property procurement are not screened, and there is no group approved-manufacturer list.
6. **AI governance lags use.** The AI estimating and bid assistant (SYS-D6) went from a 4-person pilot to about 640 Construction estimators and 85 A&E cost estimators in 2026, including on federal bids. A&E also uses a generative design assistant, and Group HR is piloting an AI resume screening tool for craft hiring.
7. **Cross-division incident notification not exercised.** One incident can trigger DoD reporting, state breach notices, owner and tenant notices, the surety and insurer, and an SEC materiality decision. The group notification matrix has not been exercised across divisions.
8. **Subcontractor CMMC verification.** Subcontract templates were updated in 2025 with FAR 52.204-21, FAR 52.204-25, DFARS 252.204-7012, and DFARS 252.204-7021 flowdowns, but nobody checks a subcontractor's CMMC status before award, as DFARS 252.204-7021(f)(2) requires.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 regulation | Construction (focus): FAR 52.204-21 verified through CMMC Level 1 (Self) for the PDPP, escalating to NIST SP 800-171 R2 and CMMC Level 2 for the CUI enclave, plus FAR 52.204-25 and DFARS 252.204-7012. A&E: DFARS 252.204-7012, NIST SP 800-171 R2, and CMMC Level 2. Property: PCI DSS v4.0.1 for parking payments and FTC Act Section 5; the FTC Safeguards Rule is tested for applicability. Group: SEC disclosure and state breach laws. Regulation-by-division matrix |
| P08 incident | Business email compromise redirecting progress payments, spanning divisions: a compromised Construction project executive mailbox redirects an owner's pay application payment, a spoofed subcontractor bank change goes through Property accounts payable, a lookalike domain targets Property tenants, and the mailbox holds CUI and certified payroll files. Multi-regulator notification matrix and SEC materiality decision |
| P09 SOC 2 | Scoped per division. In scope: the TSSI managed service (Construction) and the A&E digital twin facility data service. Out of scope, with reasons: Construction general contracting and Property leasing |
| P10 AI | Group AI governance program: group standard, division use cases (AI estimating and bid assistant as the priority use case), and the rules specific to each division's regulators and contracts |
| Cloud | Shared corporate platform plus division workloads, vendor-agnostic; the CUI enclave runs on a separate FedRAMP Moderate authorized government-community offering |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-05-04 to 2026-07-31 | Group and division risk analyses and gap analyses |
| 2026-07-06 to 2026-08-28 | Common control assessment and division samples (group internal audit), including the independent CMMC Level 2 pre-assessment of the CUI enclave |
| 2026-07-14 | CUI discovery scan finds CUI in the PDPP and commercial mailboxes |
| 2026-07-16 | Cyber incident report for the CUI spill submitted to DoD at dibnet.dod.mil, within 72 hours of discovery (DFARS 252.204-7012(c)) |
| 2026-09-15 | Results to the board risk committee; deliverables approved |
| 2026-11-10 | CMMC Phase 2 begins (32 CFR 170.3(e)(2)) |
| 2027-02 | Target window for the enclave's Level 2 (C3PAO) certification assessment |

## 7. Facts added while building the deliverables
These facts were added so the deliverables could be completed. They do not change sections 1 to 6.

| Topic | Added fact |
|---|---|
| Legal entities and CAGE codes | Cris Santos Construction, LLC and Cris Santos Design, Inc. each hold their own SAM registration and CAGE codes. Each is an organization seeking assessment (OSA) under 32 CFR Part 170 for its own contractor information systems. The enclave (SYS-G6) and the PDPP are operated for them by corporate shared services, an external service provider in CMMC terms that is part of the same corporate family |
| Federal contracts (Construction) | 212 active federal contracts and task orders: 151 civilian (GSA, VA, and others) and 61 DoD (Army Corps of Engineers, Naval Facilities Engineering Systems Command, Air Force). All carry FAR 52.204-21 and 52.204-25; the 61 DoD awards carry DFARS 252.204-7012, 252.204-7019, and 252.204-7020. CUI is identified on 23 DoD contracts (design-build and secure facility renovations). 13 awards made after 2025-11-10 carry DFARS 252.204-7021: 9 require Level 1 (Self) and 4 require Level 2 (Self) |
| Federal contracts (A&E) | 88 federal architect-engineer contracts and task orders; 47 are DoD awards involving CUI. On 6 DoD design-build projects A&E is a subcontractor to Construction (the design-builder) |
| CUI enclave users | About 3,400 users: 2,100 A&E, 1,200 Construction federal project staff, and 100 corporate administrators and compliance staff. Superintendents use enclave virtual desktops from jobsite trailers |
| PDPP scale | About 21,000 workforce users and 46,000 external users (owners, subcontractors, design consultants) on about 1,350 active projects. About 2,100 pay applications a month (about $1.18 billion billed). 3,800 external accounts from closed projects were still active in July 2026 |
| Payment volumes | Payment factory (SYS-G4): about 9,000 active Construction subcontractors and suppliers, about $900 million disbursed a month. Property accounts payable (SYS-D3): about 2,600 vendors, about $95 million a month, outside the payment factory. Property rent collections: about $175 million a month by ACH from about 1,600 tenants. A&E invoices: about $140 million a month |
| Certified payroll | Construction submits weekly certified payrolls on federal jobs (FAR 52.222-8). Project accountants receive subcontractor certified payrolls by email; many contain full Social Security numbers |
| Property scale | 64 properties in 9 states; 18 parking facilities with pay stations and a mobile parking app run through a parking technology service provider that handles cardholder data; the division is a merchant for parking revenue. The 9 federally leased properties are leased through GSA lease contracts |
| Property building systems | BAS, access control, and video at 41 properties share flat building networks with parking pay stations at 6 garages. 11 integrator firms hold persistent remote access. At 2 federally leased properties, 46 cameras and 3 recorders from a covered manufacturer under FAR 52.204-25 were installed by the previous owner in 2018 (found in P07 testing on 2026-08-12) |
| TSSI managed service | Remote monitoring and maintenance of video, access control, and BAS for 140 clients (hospitals, universities, offices, 11 federal sites). Clients ask for a SOC 2 Type 2 report; 2 federal clients ask for the group's Section 889 procedures |
| A&E digital twin service | Since 2025 A&E hosts building information models and facility data (equipment, maintenance, space data) for 52 owner clients after handover, on the group cloud (provider A). Clients rely on it for facility operations and ask for a SOC 2 report. No CUI is allowed in it |
| Other AI use cases (P10 inventory) | Besides the AI estimating and bid assistant: jobsite safety computer vision (Construction), AI resume screening pilot for craft hiring (Group HR), generative design assistant (A&E), code compliance checking assistant (A&E), lease abstraction (Property), BAS energy optimization (Property), AP invoice and payment anomaly detection (Group finance), and an enterprise generative AI assistant (Group). A Group AI Standard and Group AI council were established in 2026 |
| Cyber insurance | A $100 million cyber insurance tower with a $10 million social engineering (funds transfer fraud) sublimit. Performance and payment bonds through a surety under a general indemnity agreement |
| Out of scope by fact | No HIPAA role (the group designs and builds health care facilities but holds no PHI for clients). No California operations (CCPA not applicable; revisit on entry). Commercial tenants are businesses, so the Property division has no consumer customers. No FedRAMP authorization is sought (the group does not operate federal information systems on behalf of an agency) |
| State footprint detail | None of the 14 states of operation is California, Colorado, Illinois, Connecticut, or New York, and no hiring takes place in New York City. Texas is one of the 14 states |
| Federal revenue share | About 28% of Construction revenue comes from federal contracts (used in P01 section 5) |
| TSSI service staff | About 160 TSSI technicians and engineers deliver the managed service (P09) |
| AI use detail (P10) | AI estimating and bid assistant: about 725 users (640 Construction, 85 A&E). Jobsite safety computer vision pilot at 40 jobsites. BAS energy optimization at 8 properties. Enterprise generative AI assistant pilot with 3,000 users. Group AI council chaired by the Group Chief Risk Officer |
| P07 escalations | Default controller credentials found 2026-08-12; a CUI-marked specification found in the AI estimating assistant tenant on 2026-08-14, removed and reported under POL-03 4.4 |
| Risk acceptance | Low: division security and compliance lead. Moderate: division president. High: Group Chief Risk Officer with the Group CISO, reported to the board risk committee. Very High: board risk committee only. High risks to life safety (jobsite safety systems, building life-safety interfaces) and to federal contract eligibility must be treated, not accepted |
