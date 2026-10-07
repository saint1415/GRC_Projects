# Scenario facts: Cris Santos Company | Defense Industrial Base | Multi-Sector

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or contract clause, the citation is given. Regulatory text was checked on eCFR (version date 2026-09-23) and the Federal Register between 2026-09-26 and 2026-10-04.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company Holdings, Inc. (publicly traded SEC registrant) |
| Structure | A holding company with three divisions and corporate shared services. Each division is a wholly owned operating subsidiary with its own CAGE codes |
| Division 1: Aircraft Parts (NAICS 336413), **focus of this scenario** | Machined and additively manufactured structural fittings, hydraulic and fuel system assemblies, and spares for military and commercial aircraft. 9 plants. About 25,500 employees. About 55% of division revenue is defense work: DoD spares and sustainment contracts held directly, plus subcontracts under four airframe prime contractors (Primes A to D). The rest is commercial aerospace |
| Division 2: Engineering Services (NAICS 541330, sector 54 Professional, Scientific, and Technical Services) | Design engineering, stress analysis, test and evaluation, and sustainment engineering for DoD program offices and prime contractors. 4 engineering centers plus about 1,200 engineers working on customer sites. About 10,800 employees. A cleared defense contractor at 2 of its 4 centers |
| Division 3: Defense Software and Data Services (NAICS 513210, sector 51 Information) | A sustainment analytics platform for military aircraft maintenance and readiness data, sold in two editions (section 3). About 4,700 employees |
| Corporate shared services | Identity, network, security operations, cloud platform, ERP, HR, finance, legal, export compliance, and internal audit. About 4,000 employees |
| Location | Headquartered in Florida. Plants and engineering centers in several states. **State law is handled generically** ("each state where affected individuals reside"), with Florida as the worked example |
| Workforce / revenue | 45,000 employees; about $18.0 billion revenue (fictional) |
| Ownership | Public shareholders. As an SEC registrant the group files Form 8-K Item 1.05 for material cybersecurity incidents and makes the annual Regulation S-K Item 106 disclosure |
| SBA size status | Not small (SBA standard for NAICS 336413 is 1,250 employees, 13 CFR 121.201) |
| CUI handled | Controlled technical information (CTI) as defined in DFARS 252.204-7012(a): drawings, 3D models, specifications, NC programs and build files, stress and test reports, and sustainment data. It is covered defense information (CDI) and CUI. Many parts are ITAR defense articles, so their technical data is ITAR-controlled; commercial parts carry EAR-controlled technology |
| Contract clauses | Aircraft Parts and Engineering Services: DFARS 252.204-7012 (MAY 2024), 252.204-7019 and 252.204-7020 (NOV 2023), FAR 52.204-21 (NOV 2021); awards made from 2025-11-10 also include DFARS 252.204-7021 (NOV 2025). Defense Software DoD edition contracts: DFARS 252.239-7010 (JAN 2023) and 252.204-7012 |
| CMMC requirement | DoD program offices and Primes A to D have told the group that solicitations issued from 2026-11-10 (Phase 2, 32 CFR 170.3(e)(2)) will require **CMMC Level 2 (C3PAO)** for CUI work. One Aircraft Parts program (**Program H**, a high-priority military aircraft program) has told the group to expect **Level 3 (DIBCAC)** from Phase 3 (2027-11-10, 32 CFR 170.3(e)(3)) |
| Export controls | Aircraft Parts and Engineering Services are registered with the State Department's Directorate of Defense Trade Controls (22 CFR 122.1). Each holds technical assistance agreements and licenses managed by the group export compliance office |
| Classified work | Engineering Services holds facility clearances at 2 engineering centers. Classified systems there are authorized by DCSA and are **outside the scope of these samples**, except for reporting duties and the insider threat program (32 CFR Part 117) |

## 2. People (role titles only)
| Role | Duties |
|---|---|
| Board audit and risk committee | Group cyber oversight; accepts Very High risks; receives internal audit results |
| Disclosure committee | SEC materiality of cybersecurity incidents (Form 8-K Item 1.05) |
| Group CISO | Group security program, group policies, common controls (SYS-G1, SYS-G2, SYS-G3); co-accepts High risks |
| Group Chief Risk Officer | Group risk register and ERM roll-up (NIST IR 8286 Rev. 1); co-accepts High risks |
| Group General Counsel | Contracts, notification matrix, SEC and customer notices |
| Group CMMC program director | Assessment scopes, SPRS submissions, C3PAO and DIBCAC coordination; reports to the Group CISO |
| Group export compliance director | ITAR and EAR program; supervises the division Empowered Officials |
| Group Chief Privacy Officer | Employee personal information and state breach laws |
| Group insider threat program senior official (ITPSO) | One entity-wide insider threat program for the cleared entities (32 CFR 117.7(b)(4)(iii)) |
| Division presidents (3) | Accept Moderate risks; **CMMC Affirming Official** for their division's CAGE codes (32 CFR 170.22) |
| Division security and compliance leads (3) | Division registers, division supplements, division regulators and customers; accept Low risks |
| Division Empowered Officials (Aircraft Parts, Engineering Services) | ITAR Empowered Officials; export disclosure decisions |
| Facility security officers (Engineering Services, 2 cleared centers) | NISPOM duties at each cleared center (32 CFR 117.7(b)(3)) |
| Group internal audit | Independent assessor: reports to the board audit and risk committee; assesses common controls once and samples division controls |
| Group SOC director | 24x7 SOC; incident commander for incidents in shared services |
| Group data and engineering platforms director | System owner of the SSP system (GCEE) |

## 3. Systems
| ID | System | Owner | CUI? |
|---|---|---|---|
| SYS-G1 | Group identity platform: a government-community tenant for every CUI environment (with a verified U.S.-person attribute) and a commercial tenant for other workforce use; single sign-on, MFA, privileged access management (PAM), identity governance | Corporate | Security Protection Asset |
| SYS-G2 | Group SOC (24x7, in-house), SIEM hosted in the government-community cloud, and EDR | Corporate | Security Protection Asset |
| SYS-G3 | Group cloud platform: a government-community landing zone on provider A for CUI workloads (offering FedRAMP authorized at High) and a commercial landing zone on provider B for non-CUI workloads | Corporate | Yes (provider A) |
| SYS-G4 | Group ERP: orders, purchasing, DCAA-compliant cost accounting (commercial SaaS) | Corporate | No CUI by policy; holds FCI |
| SYS-G5 | Group CUI collaboration suite: email, file storage, and chat in a government-community SaaS offering (FedRAMP authorized at Moderate or higher) | Corporate | Yes |
| SYS-D1 | Aircraft Parts plant systems: MES, DNC, about 1,140 CNC machines, additive machines, and CMMs, and the plant enclave networks at 9 plants | Aircraft Parts | Yes |
| SYS-D2 | Engineering Services engineering systems: HPC simulation cluster, test and evaluation data acquisition systems, field engineering laptops | Engineering Services | Yes |
| SYS-D3 | Sustainment analytics platform, **DoD edition**: operated on behalf of DoD under DFARS 252.239-7010; holds a FedRAMP Moderate authorization and a DoD provisional authorization | Defense Software | Yes (Government data) |
| SYS-D4 | Sustainment analytics platform, **industry edition**: multi-tenant SaaS for 14 defense contractor tenants (CUI, including the Aircraft Parts division) and 63 commercial airline and MRO tenants (no CUI) | Defense Software | Yes (14 tenants) |
| SYS-D5 | Defense Software software factory: source repositories, CI/CD pipelines, code signing | Defense Software | Export-controlled source code; no customer CUI by policy |

**SSP system (P02):** the *Group CUI Engineering Enclave (GCEE)*: the shared CAD/PLM environment (PLM application and vault, CAD virtual workstations, engineering data exchange gateway, and the Program H project enclave) used by Aircraft Parts and Engineering Services, hosted on the SYS-G3 government-community landing zone and inheriting common controls from SYS-G1, SYS-G2, SYS-G3, and SYS-G5.

## 4. Current security posture: a defined program, mostly compliant, with gaps in scale
**In place today:**
- Group policies aligned to CSF 2.0 and a CMMC program office
- The GCEE in a government-community cloud, with every CUI user verified as a U.S. person before access
- MFA for every CUI environment; phishing-resistant hardware keys for administrators; PAM with just-in-time elevation
- 24x7 group SOC with EDR on all managed endpoints and servers
- Quarterly access certification; immutable backups
- A DCMA DIBCAC High Assessment of the Aircraft Parts CUI environment in 2024 (score 98)
- SSPs for the GCEE and for each plant enclave
- DDTC registration, an export compliance program, and an entity-wide insider threat program
- Defense Software: SOC 2 Type 2 report for the industry edition; FedRAMP Moderate authorization and DoD provisional authorization for the DoD edition
- Reg S-K Item 106 disclosure and annual group internal audit of common controls

**Gaps:**
1. **Plant 9.** The plant acquired on 2025-10-01 still runs its own legacy network and file server, holding about 6,000 CUI drawings outside the GCEE. FIPS-validated encryption is not confirmed on its site VPN and its visitor log is on paper. DFARS 252.204-7012 applies to it now; it is outside the planned Level 2 assessment scope until it migrates (due 2027-03-31).
2. **Specialized Assets at scale.** About 1,140 CNC, additive, and CMM machines at 9 plants. 212 run unsupported controller software; 61 at 3 plants are still loaded by USB drive. Two plants' asset inventories and network diagrams are incomplete.
3. **Supplier flowdown at scale.** About 1,450 suppliers receive CUI. DFARS 252.204-7012 flowdown is confirmed for 92% of them, but CMMC status has been verified for only 38% of those that will need Level 2 (C3PAO) on Phase 2 subcontracts (252.204-7021; 32 CFR 170.23).
4. **Industry edition FedRAMP Moderate equivalency.** SYS-D4 stores CUI for 14 defense contractor tenants, including the Aircraft Parts division's sustainment data. It is not FedRAMP authorized, and its 2026 third-party (3PAO) assessment left 23 open findings, so the division cannot yet show that it meets security requirements equivalent to the FedRAMP Moderate baseline (DFARS 252.204-7012(b)(2)(ii)(D); 32 CFR 170.19(c)(2)).
5. **Engineering Services field work.** About 1,200 engineers work on customer sites with government furnished equipment (GFE) and customer systems. There is no inventory of which CUI is held on GFE versus company systems, and some engineers sync CUI to company laptops outside the GCEE.
6. **Common control inheritance.** Documented for Aircraft Parts and the GCEE; not documented for the Engineering Services HPC cluster and test systems, which joined the CUI environment in 2026.
7. **Generative AI with CUI.** An engineering assistant inside the government-community suite is in a 300-user pilot; engineers at two Engineering Services centers were found using public chatbots with CUI; a Group AI Standard was adopted only in 2026-06.
8. **Multi-regulator incident notification.** A shared GCEE incident would trigger DoD reports under several divisions' contracts, cloud service provider duties for Defense Software, export disclosure decisions, NISPOM reports, customer notices, and an SEC materiality decision. The group notification matrix has not been exercised, and no one in Defense Software holds a DoD-approved medium assurance certificate.
9. **Division supplement drift.** The Engineering Services supplement was last aligned to group policy in 2024. Its field-engineering standards conflict with group rules on removable media and cloud storage.
10. **Logging at plants.** MES and DNC logs at 4 of 9 plants are not collected in the SIEM.
11. **Level 3 readiness.** Program H expects Level 3 (DIBCAC) in Phase 3. A Final Level 2 (C3PAO) status for the Level 3 scope is a prerequisite (32 CFR 170.18(a)(1)); threat hunting, supply chain risk planning, and Specialized Asset security for Level 3 are not yet in place.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P08 | Exfiltration of CUI spanning divisions: a stolen single sign-on session of an Engineering Services engineer is used to take Aircraft Parts and Engineering Services data from the GCEE and two prime customers' data from the industry edition (SYS-D4). A multi-regulator notification matrix and SEC materiality |
| P09 | SOC 2 scoped per division: the Defense Software industry edition is in scope as a true service organization (Type 2); Aircraft Parts and Engineering Services are out of scope (CMMC is their assurance); the DoD edition relies on FedRAMP and its DoD authorization |
| P10 | Group AI governance program. Priority use case: the generative AI assistant used with CUI engineering documents (registry default, kept), plus division use cases with regulator-specific rules |
| Cloud | Shared corporate platform plus division workloads, vendor-agnostic: provider A (government-community, for CUI) and provider B (commercial, for non-CUI) |

**Registry defaults kept:** the primary system (CUI engineering enclave, CAD/PLM) is kept and made a shared corporate system because both CUI divisions use one PLM environment; the P08 incident and the P10 use case are kept as given.

## 6. Assessment calendar (fictional unless a regulation is cited)
| Date | Event |
|---|---|
| 2024-05-13 to 2024-05-24 | DCMA DIBCAC High Assessment of the Aircraft Parts CUI environment; score 98 posted in SPRS on 2024-06-07 |
| 2025-10-01 | Plant 9 acquired |
| 2025-11-10 | CMMC Phase 1 begins (DFARS rule effective date, 90 FR 43560) |
| 2026-05-04 to 2026-07-31 | Group and division risk analyses, BIAs, and gap analyses |
| 2026-07-06 to 2026-08-28 | Common control assessment (group internal audit) plus division samples |
| 2026-09-15 | Results to the board audit and risk committee; deliverables approved |
| 2026-11-10 | CMMC Phase 2 begins (32 CFR 170.3(e)(2)) |
| 2026-12-07 to 2026-12-18 | Target window for the Level 2 certification assessment by a C3PAO of the Enterprise CUI Environment (GCEE, plants 1 to 8, Engineering Services centers) |
| 2027-03-31 | Plant 9 migration into the GCEE due |
| 2027-11-10 | CMMC Phase 3 begins; Program H Level 3 (DIBCAC) expected (32 CFR 170.3(e)(3)) |

## 7. Facts added while building the deliverables
These facts were added so the deliverables could be completed. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| Revenue split (fictional) | Aircraft Parts about $11.4 billion; Engineering Services about $4.8 billion; Defense Software about $1.8 billion. Per day: Aircraft Parts about $45.6 million of shipments per production day (about 250 days); Engineering Services about $19.2 million per working day; Defense Software about $4.9 million per calendar day | P05 |
| GCEE size | About 12,600 named users (6,900 Aircraft Parts, 5,200 Engineering Services, 120 Defense Software, 380 corporate) and 140 service accounts; about 4.8 million controlled documents; 2,400 concurrent virtual workstation sessions; about 1,100 thick CAD workstations; engineering laptops reach CAD in keyboard-video-mouse mode only | P02, P04 |
| Recovery | PLM restore tested twice a year; hourly vault snapshots; nightly MES backups to the provider A vault for plants 1 to 8; Plant 9 backs up weekly to an unencrypted local disk and has one internet circuit; plants 1 to 8 have a second carrier; one MES vendor support contract covers all 9 plants; 3 plants can absorb urgent DoD spares work; identity RTO met in both 2026 tests | P05, P01 |
| Risk acceptance | Low: division security and compliance lead. Moderate: division president. High: Group Chief Risk Officer with the Group CISO, reported to the board audit and risk committee. Very High: board committee only. High risks that could put a nonconforming part on an aircraft or involve unauthorized export may not be accepted | P01, P06 |
| Plant details | MES and DNC logs reach the SIEM at plants 1, 2, 3, 5 only; USB device control at plants 1, 2, 5 only (61 USB-loaded machines at plants 3, 6, 8); MES local accounts not disabled at plants 3, 6, 8; plants 4 and 7 SSP annexes and inventories predate the 2025 MES upgrade; plants 6 and 8 have flat MES VLANs; 212 unsupported controllers; Plant 9 has had EDR since 2026-02 | P01, P03, P04, P07 |
| SPRS records | DIBCAC High Assessment of Aircraft Parts, 98 (2024-06-07); Engineering Services Basic Assessment, 101 (2025-03). No Phase 1 award to the group has required Level 2 (Self) | P03 |
| Certificate holders | Aircraft Parts 4; Engineering Services 2 (both at one center); Defense Software none | P03, P08 |
| Suppliers and subconsultants | DFARS 252.204-7012 flowdown confirmed for 92% of about 1,450 CUI suppliers (about 115 without); 46 Engineering Services subconsultant agreements predate the 2025 clause templates | P03, P07 |
| Defense Software | 5 DoD program offices use the DoD edition; 77 industry edition tenant contracts (14 CUI, 63 commercial); CUI tenants in a separate cluster since 2026-04; SOC 2 Type 2 reports issued since 2023 (period ending September 30); 3PAO assessment against the FedRAMP Moderate baseline in 2026-06 left 23 open findings; website and proposals described the industry edition as "FedRAMP-ready" and "CMMC compliant"; the 2026-05 model retraining combined DoD edition telemetry with industry data; 2 subcontracts lack the DFARS 252.239-7010 flowdown; 3 subcontracts put Defense Software staff in contact with CUI support data, so its CAGE code joined the Enterprise CUI Environment in 2026-08 | P01, P03, P09, P10 |
| Engineering Services field work | Field survey of 60 engineers: 14 had synced customer CUI to company laptops; 6 of 41 test data shipments in 2026 used unencrypted drives; HPC nodes deviate from the group baseline on 31 settings | P03, P07 |
| Export tags | About 3% of sampled PLM documents had no export tag | P01, P03 |
| AI | Group AI council chaired by the Group Chief Risk Officer; AI-001 pilot test results (109 of 120 correct; 3 wrong numeric values; 37 of 412 project spaces open division-wide); provider boundary confirmation received 2026-08-14; enterprise assistant pilot with 2,000 non-CUI users | P10 |
| P08 exercise scenario | The test range badging roster in one Engineering Services project held names and Social Security numbers of 640 employees (280 in Florida, 360 in 5 other states); the tenant agreements of Prime A and Prime D require incident notice within 72 hours | P08 |
