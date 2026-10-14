# Scenario facts: Cris Santos Company | Defense Industrial Base | Multi-Sector

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or contract clause, the citation is given. Regulatory text was checked on eCFR (version date 2026-09-23) and the Federal Register between 2026-09-26 and 2026-10-04.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company Holdings, Inc. (publicly traded SEC registrant) |
| Structure | A holding company with three divisions and corporate shared services. Each division is a wholly owned operating subsidiary with its own CAGE codes |
| Division 1: Aircraft Parts (NAICS 336413), **focus of this scenario** | Machined and additively manufactured structural fittings, hydraulic and fuel system assemblies, and spares for military and commercial aircraft. 9 plants. About 25,500 employees. About 55% of division revenue is defense work: DoD spares and sustainment contracts held directly, plus subcontracts under four airframe prime contractors (Primes A to D). The rest is commercial aerospace |
| Division 2: Engineering Services (NAICS 541330, sector 54 Professional, Scientific, and Technical Services) | Design engineering, stress analysis, test and evaluation, and sustainment engineering for DoD program offices and prime contractors. 4 engineering centers plus about 1,200 engineers working on customer sites. About 10,800 employees. A cleared defense contractor at 2 of its 4 centers (EV-042) |
| Division 3: Defense Software and Data Services (NAICS 513210, sector 51 Information) | A sustainment analytics platform for military aircraft maintenance and readiness data, sold in two editions (section 3). About 4,700 employees |
| Corporate shared services | Identity, network, security operations, cloud platform, ERP, HR, finance, legal, export compliance, and internal audit. About 4,000 employees |
| Location | Headquartered in Florida. Plants and engineering centers in several states. **State law is handled generically** ("each state where affected individuals reside"), with Florida as the worked example |
| Workforce / revenue | 45,000 employees; about $18.0 billion revenue (fictional) |
| Ownership | Public shareholders. As an SEC registrant the group files Form 8-K Item 1.05 for material cybersecurity incidents and makes the annual Regulation S-K Item 106 disclosure (EV-004). Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (N51-R08) |
| SBA size status | Not small (SBA standard for NAICS 336413 is 1,250 employees, 13 CFR 121.201; workforce in EV-002) |
| CUI handled | Controlled technical information (CTI) as defined in DFARS 252.204-7012(a): drawings, 3D models, specifications, NC programs and build files, stress and test reports, and sustainment data. It is covered defense information (CDI) and CUI. Many parts are ITAR defense articles, so their technical data is ITAR-controlled; commercial parts carry EAR-controlled technology |
| Contract clauses | Aircraft Parts and Engineering Services: DFARS 252.204-7012 (MAY 2024), 252.204-7019 and 252.204-7020 (NOV 2023), FAR 52.204-21 (NOV 2021); awards made from 2025-11-10 also include DFARS 252.204-7021 (NOV 2025). Under DoD Class Deviation 2026-O0025, Revision 3, contracting officers remove those CMMC requirements by modification before the next option period or at the next scheduled administrative modification. Defense Software DoD edition contracts: DFARS 252.239-7010 (JAN 2023) and 252.204-7012 (EV-005). Which clauses bind which division is decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (C-DIB-R01, C-DIB-R03, C-DIB-R04, DFARS-252.239-7010) |
| CMMC requirement | DoD program offices and Primes A to D told the group that solicitations issued from 2026-11-10 (Phase 2, 32 CFR 170.3(e)(2)) would require **CMMC Level 2 (C3PAO)** for CUI work. One Aircraft Parts program (**Program H**, a high-priority military aircraft program) told the group to expect **Level 3 (DIBCAC)** from Phase 3 (2027-11-10, 32 CFR 170.3(e)(3)). The DoD (Department of War) CIO memorandum of 2026-07-13 suspended CMMC Phase 2. Until 2028-11-09 DoD includes DFARS 252.204-7021 only when a program office requires a specific CMMC level, and during the suspension requiring activities may require Level 1 (Self) or Level 2 (Self) (DoD Class Deviation 2026-O0025, Revision 3, DFARS 240.371-5). Those Level 2 (C3PAO) and Level 3 requirements are therefore suspended. The group keeps preparing because it still owes NIST SP 800-171 Rev. 2 under DFARS 252.204-7012, and it keeps its C3PAO assessment as a voluntary choice. Notices from program offices and primes: EV-006; status in SPRS: EV-007; decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (C-DIB-R02-AP, C-DIB-R02-ES, C-DIB-R02-DS) |
| Export controls | Aircraft Parts and Engineering Services are registered with the State Department's Directorate of Defense Trade Controls (22 CFR 122.1). Each holds technical assistance agreements and licenses managed by the group export compliance office (EV-032; obligations register C-DIB-R05, C-DIB-R06) |
| Classified work | Engineering Services holds facility clearances at 2 engineering centers. Classified systems there are authorized by DCSA and are **outside the scope of these samples**, except for reporting duties and the insider threat program (32 CFR Part 117). Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (C-DIB-R07-ES, C-DIB-R07-OTHER; EV-042, EV-060) |
| FOCI status | Background fact, not scored in P03. DCSA has not found the group to be under foreign ownership, control, or influence (the test is in 32 CFR 117.11(a)(1)). The holding company files one consolidated SF 328 for the corporate family, as 32 CFR 117.11(c) allows based on CSA guidance, and updates it when significant changes occur. Investor relations watches public filings for foreign holdings that could change this (EV-042) |
| FAR overhaul clause numbers | Background fact, not scored in P03. Contracts awarded before the contracting agency adopted its FAR Part 40 class deviation keep the clauses this sample cites (FAR 52.204-21, 52.204-25 and DFARS 252.204-7019 and -7020) until they are modified. New awards under the deviation carry FAR 52.240-93, which has the same 15 safeguarding requirements as FAR 52.204-21, and FAR 52.240-91, which replaces the separate Kaspersky, Section 889 and FASCSA reports with one report within 72 hours. New DoD awards under DFARS Part 240 (DoD Class Deviation 2026-O0025, Revision 3) carry 252.240-7997 for DoD-led Medium and High NIST SP 800-171 assessments instead of 252.204-7019 and -7020. Sources: SRC-FAR-RFO-PART40 and SRC-DFARS-DEV-2026-O0025 |

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

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv). Suppliers are in the [vendor register](step-00_P00_intake/vendor-register.csv).

| ID | System | Owner | CUI? |
|---|---|---|---|
| SYS-G1 | Group identity platform: a government-community tenant for every CUI environment (with a verified U.S.-person attribute) and a commercial tenant for other workforce use; single sign-on, MFA, privileged access management (PAM), identity governance | Corporate | Security Protection Asset |
| SYS-G2 | Group SOC (24x7, in-house), SIEM hosted in the government-community cloud, and EDR | Corporate | Security Protection Asset |
| SYS-G3 | Group cloud platform: a government-community landing zone on provider A for CUI workloads (offering FedRAMP authorized at High) and a commercial landing zone on provider B for non-CUI workloads | Corporate | Yes (provider A) |
| SYS-G4 | Group ERP: orders, purchasing, DCAA-compliant cost accounting (commercial SaaS) | Corporate | No CUI by policy; holds FCI |
| SYS-G5 | Group CUI collaboration suite: email, file storage, and chat in a government-community SaaS offering (FedRAMP authorized at Moderate or higher) | Corporate | Yes |
| SYS-D1 | Aircraft Parts plant systems: MES, DNC, about 1,140 CNC machines, additive machines, and CMMs, and the plant enclave networks at 9 plants | Aircraft Parts | Yes |
| SYS-D2 | Engineering Services engineering systems: HPC simulation cluster, test and evaluation data acquisition systems, field engineering laptops | Engineering Services | Yes |
| SYS-D3 | Sustainment analytics platform, **DoD edition**: operated on behalf of DoD under DFARS 252.239-7010; holds a FedRAMP Moderate authorization and a DoD provisional authorization (EV-063) | Defense Software | Yes (Government data) |
| SYS-D4 | Sustainment analytics platform, **industry edition**: multi-tenant SaaS for 14 defense contractor tenants (CUI, including the Aircraft Parts division) and 63 commercial airline and MRO tenants (no CUI) (EV-062) | Defense Software | Yes (14 tenants) |
| SYS-D5 | Defense Software software factory: source repositories, CI/CD pipelines, code signing | Defense Software | Export-controlled source code; no customer CUI by policy |

**SSP system (P02):** the *Group CUI Engineering Enclave (GCEE)*: the shared CAD/PLM environment (PLM application and vault, CAD virtual workstations, engineering data exchange gateway, and the Program H project enclave) used by Aircraft Parts and Engineering Services, hosted on the SYS-G3 government-community landing zone and inheriting common controls from SYS-G1, SYS-G2, SYS-G3, and SYS-G5.

## 4. Where the evidence is
This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Rows are grouped by division (Group, GCEE, Aircraft Parts, Engineering Services, Defense Software). Every item has a source system, an owner, and as-of and collected dates.
- **Which rules apply** to each division and to the group is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps** against NIST SP 800-171 Rev. 2, the DFARS and FAR clauses, CMMC, export control, NISPOM and the group-wide rules are judged in the gap analyses (P03), which also number the eleven group gaps cited across this sample, and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

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
| 2026-03-30 to 2026-04-24 | Intake: evidence requests, exports, contract and document collection, inventories, obligations register, grouped by division |
| 2026-05-04 to 2026-07-31 | Group and division BIAs (BIA interviews in May), risk analyses (risk interviews in June), and gap analyses (plant walkthroughs at plants 2, 4, and 7 on 2026-06-16 and 2026-06-17 and at Plant 9 on 2026-06-18; gap analysis interviews from 2026-06-29) |
| 2026-06-01 to 2026-06-30 | Group policies v2026 drafted from the intake observations and the risks and gaps found so far (P06); the Aircraft Parts supplement was aligned to the drafts on 2026-06-30 |
| 2026-07-06 to 2026-08-28 | Common control assessment (group internal audit) plus division samples: operating tests of controls already in place under the 2025 group policies and standards and IR plan v4; the draft v2026 policies were reviewed for design only |
| 2026-07-13 | The DoD (Department of War) CIO memorandum suspends CMMC Phase 2 (DoD Class Deviation 2026-O0025, Revision 3) |
| 2026-09-15 | Results to the board audit and risk committee; deliverables and group policies v2026 approved (policies effective 2026-10-01) |
| 2026-11-10 | Planned start of CMMC Phase 2 (32 CFR 170.3(e)(2)); suspended by the 2026-07-13 CIO memorandum |
| 2026-12-07 to 2026-12-18 | Target window for a voluntary Level 2 certification assessment by a C3PAO of the Enterprise CUI Environment (GCEE, plants 1 to 8, Engineering Services centers) |
| 2027-03-31 | Plant 9 migration into the GCEE due |
| 2027-04 (planned) | Follow-up assessment: operating effectiveness of the controls the v2026 policies introduced, after at least one quarter of operation |
| 2027-11-10 | CMMC Phase 3 date in 32 CFR 170.3(e)(3); Program H's Level 3 (DIBCAC) expectation is suspended under the deviation |

## 7. Facts added while building the deliverables
These facts were added so the deliverables could be completed. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| Revenue split (fictional) | Aircraft Parts about $11.4 billion; Engineering Services about $4.8 billion; Defense Software about $1.8 billion. Per day: Aircraft Parts about $45.6 million of shipments per production day (about 250 days); Engineering Services about $19.2 million per working day; Defense Software about $4.9 million per calendar day (EV-003) | P05 |
| GCEE size | About 12,600 named users (6,900 Aircraft Parts, 5,200 Engineering Services, 120 Defense Software, 380 corporate) and 140 service accounts; about 4.8 million controlled documents; 2,400 concurrent virtual workstation sessions; about 1,100 thick CAD workstations; engineering laptops reach CAD in keyboard-video-mouse mode only (EV-013, EV-043) | P02, P04 |
| Recovery | PLM restore tested twice a year (EV-047); hourly vault snapshots; nightly MES backups to the provider A vault for plants 1 to 8 (EV-027, EV-054); Plant 9 backs up weekly to an unencrypted local disk and has one internet circuit (EV-055); plants 1 to 8 have a second carrier (EV-025); one MES vendor support contract covers all 9 plants (EV-057); 3 plants can absorb urgent DoD spares work (EV-054); identity RTO met in both 2026 tests (EV-071) | P05, P01 |
| Risk acceptance | Low: division security and compliance lead. Moderate: division president. High: Group Chief Risk Officer with the Group CISO, reported to the board audit and risk committee. Very High: board committee only. High risks that could put a nonconforming part on an aircraft or involve unauthorized export may not be accepted | P01, P06 |
| Plant details | MES and DNC logs reach the SIEM at plants 1, 2, 3, 5 only (EV-017, EV-052); USB device control at plants 1, 2, 5 only (61 USB-loaded machines at plants 3, 6, 8) (EV-050, EV-053); MES local accounts not disabled at plants 3, 6, 8 (EV-052); plants 4 and 7 SSP annexes and inventories predate the 2025 MES upgrade (EV-045, EV-050); plants 6 and 8 have flat MES VLANs (EV-051); 212 unsupported controllers (EV-050); Plant 9 has had EDR since 2026-02 (EV-020, EV-055) | P01, P03, P04, P07 |
| SPRS records | DIBCAC High Assessment of Aircraft Parts, 98 (2024-06-07); Engineering Services Basic Assessment, 101 (2025-03). No Phase 1 award to the group has required Level 2 (Self) (EV-007) | P03 |
| Certificate holders | Aircraft Parts 4; Engineering Services 2 (both at one center); Defense Software none (EV-019) | P03, P08 |
| Suppliers and subconsultants | DFARS 252.204-7012 flowdown confirmed for 92% of about 1,450 CUI suppliers (about 115 without) (EV-033, EV-087); 46 Engineering Services subconsultant agreements predate the 2025 clause templates (EV-090) | P03, P07 |
| Defense Software | 5 DoD program offices use the DoD edition; 77 industry edition tenant contracts (14 CUI, 63 commercial) (EV-062); CUI tenants in a separate cluster since 2026-04 (EV-066); SOC 2 Type 2 reports issued since 2023 (period ending September 30) (EV-064); 3PAO assessment against the FedRAMP Moderate baseline in 2026-06 left 23 open findings (EV-092); website and proposals described the industry edition as "FedRAMP-ready" and "CMMC compliant" (EV-065, EV-095); the 2026-05 model retraining combined DoD edition telemetry with industry data (EV-093); 2 subcontracts lack the DFARS 252.239-7010 flowdown (EV-091); 3 subcontracts put Defense Software staff in contact with CUI support data, so its CAGE code joined the Enterprise CUI Environment in 2026-08 (EV-062, EV-103) | P01, P03, P09, P10 |
| Engineering Services field work | Field survey of 60 engineers: 14 had synced customer CUI to company laptops (EV-ES-AC20); 6 of 41 test data shipments in 2026 used unencrypted drives (EV-100); HPC nodes deviate from the group baseline on 31 settings (EV-094) | P03, P07 |
| Export tags | About 3% of sampled PLM documents had no export tag (EV-086) | P01, P03 |
| AI | Group AI council chaired by the Group Chief Risk Officer; AI-001 pilot test results (109 of 120 correct; 3 wrong numeric values; 37 of 412 project spaces open division-wide) (EV-106); provider boundary confirmation received 2026-08-14 (EV-105); enterprise assistant pilot with 2,000 non-CUI users (EV-035) | P10 |
| P08 exercise scenario | The test range badging roster in one Engineering Services project held names and Social Security numbers of 640 employees (280 in Florida, 360 in 5 other states); the tenant agreements of Prime A and Prime D require incident notice within 72 hours (EV-062) | P08 |
