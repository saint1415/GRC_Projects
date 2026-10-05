# Scenario facts: Cris Santos Company | Water and Wastewater Systems | Enterprise

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a law, regulation, or standard, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (publicly traded SEC registrant; parent of state-regulated water utility subsidiaries) |
| Business | Investor-owned community water systems (NAICS 221310): source water, treatment, storage, and distribution of drinking water through four state-regulated utility subsidiaries, plus two market-based service lines offered to municipal utilities (contract operations and utility billing services). **No wastewater service**: municipal utilities collect and treat wastewater in the company's service areas, and the company operates no publicly owned treatment works |
| Location | Headquartered in Florida. Regulated subsidiaries in Florida, Georgia, North Carolina, and Tennessee. **State laws are handled generically:** customer data breach notice follows the law of each state where affected individuals reside, with Florida as the worked example. State public utility commissions set rates in each state; rate matters are outside these deliverables |
| Water systems | **126 community water systems** (each with its own public water system ID under the state primacy agency), about **9.6 million people served** through about 3.5 million metered connections. 214 treatment plants (surface water, groundwater, and brackish reverse osmosis), about 1,900 remote sites (wells, booster stations, storage tanks), and 5 regional operations control centers (ROCCs) |
| Workforce | 12,000 employees: about 5,300 in operations and maintenance (including about 2,900 state-licensed operators), 1,100 in water quality and laboratories, 1,500 in customer operations, 900 in IT, OT engineering, and security, and the rest in engineering, field services, and corporate functions |
| Revenue | About $4.8 billion a year (fictional): regulated water utilities $4.3 billion; contract operations (SL-1) $310 million; utility billing services (SL-2) $190 million. Not SBA-small (the SBA standard for NAICS 221310 is $41.0 million in average annual receipts; 13 CFR 121.201) |
| SDWA section 1433 status | **86 of the 126 systems are covered**: community water systems (42 U.S.C. 300f(15)) serving a population greater than 3,300 persons (42 U.S.C. 300i-2(a)(1)). The other 40 serve 3,300 or fewer and are outside section 1433; the enterprise program covers them voluntarily. Coverage is per system, so the company runs a portfolio of RRA and ERP cycles (section 6) |
| Added at this size | SEC cybersecurity disclosure (Form 8-K Item 1.05; Reg S-K Item 106, 17 CFR 229.106); SOX IT general controls over ERP and billing revenue; growth by acquisition of municipal and private systems (6 acquired in 2025-2026); EPA Risk Management Program at 9 plants that store gaseous chlorine above the 2,500-pound threshold (40 CFR 68.130); hazardous substance release reporting (40 CFR 302.6; 40 CFR 355.40) |
| Not in scope | Wastewater (POTW) requirements. Federal contracts (none). HIPAA (not a covered entity; the employee health plan is handled by the benefits program). Card data: customers pay through the payment processor's hosted pages and IVR, so card numbers never enter company systems (PCI DSS duties are contractual and sit mostly with the processor) |

## 2. People (role titles only)
| Role | Duties |
|---|---|
| Board (audit committee; safety, environmental, and risk committee) | The safety, environmental, and risk committee oversees cybersecurity and resilience risk (Item 106 governance); the audit committee oversees Internal Audit, SOX, and disclosure controls |
| Chief Executive Officer; Chief Financial Officer | Accept Very High risk; take part in materiality determinations with the disclosure committee |
| Chief Information Security Officer (CISO) | Owner of the converged IT and OT security program; reports to the CEO and to the board committee quarterly |
| Director of OT Security | OT security architecture, OT remote access gateway, OT monitoring (reports to the CISO) |
| Director of Security Operations | 24x7 security operations center (SOC) with OT analysts; MSSP overflow |
| Chief Risk Officer | Enterprise risk management (ERM); owns the enterprise risk register |
| Chief Operating Officer | Regulated utility operations; business owner of treatment and distribution |
| Senior Vice President, Water Quality and Environmental Compliance | Water quality, laboratories, public notification, primacy agency relations; business owner of the anomaly detection model (P10) |
| Vice President, Resilience and Emergency Management | Enterprise RRA and ERP program for all 86 covered systems; EPA certification calendar |
| State utility presidents (4) | Lead each regulated subsidiary; sign the EPA RRA and ERP certifications for their state's systems |
| General Counsel | Chairs the disclosure committee; legal and regulatory counsel |
| Chief Privacy Officer (in Legal) | Customer personal information; breach determinations |
| Chief Audit Executive | Heads Internal Audit (third line); co-sources OT testing with an independent OT assessment firm |
| GRC team (10), SOC (24x7, in-house with MSSP overflow), Internal Audit (in-house, OT co-sourced) | Three lines model |
| Disclosure committee | 8-K materiality decisions (General Counsel chairs) |

## 3. Systems
| ID | System | Notes |
|---|---|---|
| SYS-01 | Regional SCADA systems: 5 ROCCs, each with a backup control center, supervising plants and remote sites | 9 SCADA platforms from 4 vendors (legacy platforms at acquired systems) |
| SYS-02 | PLCs, RTUs, and field devices: about 6,800 controllers at plants and remote sites, including chemical feed control | About 1,150 controllers are past vendor support. Chemical feed pumps at every plant have hardwired stroke or rate limits and independent hardwired analyzer alarms |
| SYS-03 | Telemetry: private LTE, licensed radio, leased fiber, and cellular gateways | About 2,100 telemetry endpoints |
| SYS-04 | OT remote access gateway (privileged remote access with MFA, per-session approval, and recording) | Covers 97 of 126 systems. The other 29 (including AQ-04 to AQ-06) still use legacy vendor tools or site VPNs |
| SYS-05 | Identity platform: SSO, MFA, privileged access management (PAM), identity governance; separate OT identity domains per region, federated to the OT remote access gateway | OT domain accounts are not driven by identity governance (manual disablement) |
| SYS-06 | Multi-cloud estate (two public cloud providers, vendor-agnostic) plus 2 colocation data centers | Enterprise data platform with historian replicas, AI workloads, customer portal and mobile app, CIS |
| SYS-07 | Customer information system (CIS) and billing, customer-managed on Cloud provider A | About 3.5 million company accounts, plus separate tenants for 27 SL-2 municipal clients (about 610,000 accounts) |
| SYS-08 | AMI head-ends and meter data management (two AMI vendors, SaaS) | About 2.6 million of 3.5 million company meters on AMI |
| SYS-09 | Laboratory information management system (LIMS), SaaS | 6 state-certified company laboratories |
| SYS-10 | GIS and enterprise asset and work management, SaaS | System maps and critical asset locations (Restricted) |
| SYS-11 | ERP, payroll, and supply chain, SaaS | SOX-relevant; chemical ordering |
| SYS-12 | Enterprise network and endpoints: SD-WAN at about 640 sites; about 16,000 workstations and laptops; about 9,000 field tablets and phones | IT/OT boundary at each ROCC and plant through an OT DMZ |
| SYS-13 | Third parties: about 1,600 vendors, including about 140 SCADA integrators and OT vendors (23 with remote access) and 11 bulk chemical suppliers | Tiered third-party risk program |
| SYS-14 | AI portfolio (11 use cases) | Governed by the AI governance committee formed in 2025 |
| SYS-15 | Physical security: card access, video, and intrusion alarms at plants and remote sites, monitored by the corporate security operations center | |

**SSP system (P02):** the *Gulf Coast Regional Water Treatment SCADA System (GCR-WTSS)*: the regional SCADA system for the company's largest community water system (Gulf Coast Regional System, Florida, about 1.24 million people served), covering the ROCC and its backup control center, the SCADA servers, HMIs, engineering workstations, and historians, the PLCs and RTUs at its 3 treatment plants and 111 remote sites, its telemetry, and its OT networks, and inheriting enterprise OT common controls (remote access gateway, OT monitoring, OT DMZ, identity, backup).

## 4. Current security posture: mature, with residual gaps
**In place today:**
- A converged IT and OT security program aligned to CSF 2.0, with SP 800-82 Rev. 3 as the OT guide
- Annual enterprise risk analysis tied to ERM (NIST IR 8286)
- A policy hierarchy of policies, standards, procedures, and exceptions
- 24x7 SOC with OT analysts
- OT remote access gateway at 97 of 126 systems
- Passive OT network monitoring at 31 systems that together serve about 84% of the population served
- An OT DMZ at every ROCC and at every plant of the 31 monitored systems
- PAM and quarterly access certification for IT
- Immutable IT backups, and offline PLC and HMI backups for every ROCC-supervised system
- Annual DR tests for tier-1 IT systems; manual-operation drills at every plant twice a year
- Hardwired chemical feed limits and independent analyzer alarms at every plant
- An enterprise RRA and ERP program with a cyber element template built on CSF 2.0 and SP 800-82 Rev. 3
- Water-sector information sharing center membership
- Annual SOC 2 Type 2 for the contract operations service line (SL-1) since 2024
- Tiered vendor reviews
- SEC Item 106 disclosure in the 10-K

**Residual gaps:**
1. **Acquisition integration.** 3 of the 6 systems acquired in 2025-2026 (AQ-04, AQ-05, AQ-06) still run legacy SCADA with vendor remote desktop tools (always on at AQ-05), shared local HMI accounts, and flat networks, and connect to the enterprise network by site VPN.
2. **Legacy OT.** About 1,150 of 6,800 controllers are past vendor support, and 38 SCADA or HMI servers and workstations run an unsupported operating system (3 engineering workstations and 1 plant historian of them are in the GCR-WTSS).
3. **Third-party OT access.** 6 of 23 integrators with remote access still use their own tools outside the gateway, at 11 legacy systems. 31 of about 140 OT vendor contracts lack security terms (mostly inherited or pre-2023 contracts).
4. **OT monitoring coverage.** 55 covered systems (about 16% of the population served) have no OT network monitoring, and HMI events at those systems are not logged centrally.
5. **ERP cycle.** 24 of the 58 smaller-category (3,301-49,999) ERP review certifications are still due (the last by 2026-12-26). 12 of those systems' 2026 RRA reviews used EPA's small-system checklist for the cyber element instead of the enterprise template, and AQ-05 and AQ-06 used their former owners' approach.
6. **AI.** 11 AI use cases, of which 7 have completed committee review. The water-quality anomaly detection model (AI-001) is in production at the Gulf Coast Regional System without drift monitoring, and its validation for two newer pilot systems relies on vendor data.
7. **Materiality.** The disclosure committee's playbook was built around data breaches. It has never been exercised with an OT or public health scenario, and no operations executive sits on the committee.
8. **Independence.** The 2025 OT control review was a self-assessment by the OT security team that operates the controls. 2026 is the first independent OT assessment (Internal Audit with a co-sourced OT firm).

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 | Primary: SDWA section 1433 (42 U.S.C. 300i-2) across the 86 covered systems, with the cyber element benchmarked against CSF 2.0 and SP 800-82 Rev. 3, and evidence sampled across systems. Also: SDWA public notification rule (40 CFR Part 141 Subpart Q) and reporting (141.31); SEC Form 8-K Item 1.05 and Reg S-K Item 106; hazardous substance release reporting (40 CFR 302.6, 355.40); state breach and data security laws (Florida worked example); CIRCIA tracked as proposed |
| P08 | Remote-access compromise of a treatment-plant HMI, with Tier 1 public notice, an **SEC materiality assessment and 8-K Item 1.05** step, and a crisis management and disclosure committee workflow |
| P09 | SOC 2 Type 2 readiness across two service lines offered to municipal utilities: SL-1 contract operations and remote monitoring; SL-2 utility billing and customer care |
| P10 | Enterprise AI portfolio (11 use cases) under the AI governance committee, with a full assessment of AI-001 water-quality anomaly detection (the registry default) |
| Cloud | Multi-cloud (vendor-agnostic) with common controls. OT stays on-premises; the cloud holds historian replicas, analytics, AI, and customer systems |
| Registry defaults | Primary system "Water treatment SCADA", incident "Remote-access compromise of treatment-plant HMI", and AI use case "Water-quality anomaly detection" all fit this size and are kept. At Enterprise the SSP covers one regional SCADA system (the highest-value one) and the incident runbook covers any of the 126 systems |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2025-03-31 and 2025-09-30 | Second-cycle RRA and ERP certifications due for the 11 systems serving 100,000 or more (all certified on time) |
| 2025-12-31 and 2026-06-30 | Second-cycle RRA and ERP certifications due for the 17 systems serving 50,000-99,999 (all certified on time) |
| 2026-04-15 to 2026-06-26 | Second-cycle RRA review certifications for the 58 systems serving 3,301-49,999 (AQ-05 certified by its former owner on 2026-02-20) |
| 2026-06-01 to 2026-07-31 | Enterprise risk analysis and gap analysis (evidence sampling completed 2026-08-14) |
| 2026-07-13 to 2026-08-28 | Control assessment (Internal Audit with a co-sourced OT assessment firm) |
| 2026-09-08 | Executive risk committee approvals |
| 2026-09-10 | Results to the board's safety, environmental, and risk committee and the audit committee |
| 2026-11-12 | Disclosure committee tabletop with an OT and public health scenario |
| 2026-12-26 | Last ERP review certification due for the smaller-category systems (six months after the last RRA certification) |

## 7. Facts added for the deliverables
These facts were added while building the deliverables. They do not change sections 1-6.

**Systems by section 1433 size category.**
| Category (population served) | Systems | RRA review due (EPA second cycle) | ERP review due | Status on 2026-09-30 |
|---|---|---|---|---|
| 100,000 or more | 11 | March 31, 2025 | September 30, 2025 | All RRA and ERP certifications on time |
| 50,000-99,999 | 17 (includes AQ-01 and AQ-04) | December 31, 2025 | June 30, 2026 | All on time |
| 3,301-49,999 | 58 (includes AQ-02, AQ-03, AQ-05, AQ-06) | June 30, 2026 | Six months after each RRA certification (EPA) | 58 RRA reviews certified; 34 ERPs certified, 24 due by 2026-12-26 |
| 3,300 or fewer | 40 | Not covered | Not covered | Enterprise program applies voluntarily |

**Gulf Coast Regional System (GCR) and the GCR-WTSS.** About 1.24 million people served through about 452,000 connections. Average day demand 168 MGD; maximum day 205 MGD. Three plants: **TP-A** surface water plant (120 MGD; conventional treatment with chloramine disinfection; gaseous chlorine in one-ton containers, an RMP-covered process), **TP-B** groundwater lime-softening plant (60 MGD; fed by 46 wells; also hosts the backup control center), and **TP-C** brackish groundwater reverse osmosis plant (30 MGD; sodium hypochlorite). Distribution: 28 booster stations and 37 storage tanks (111 remote sites in total with the wells). SCADA: commercial SCADA platform with redundant servers at the ROCC and a standby set at TP-B; 64 operator HMI stations; 9 engineering workstations; a plant historian at each plant and a regional historian; 412 PLCs and 166 RTUs; telemetry over private LTE (124 sites) and licensed radio (14 legacy RTUs). The ROCC is staffed 24x7 by licensed operators; plants are staffed 24x7.

**Acquired systems.** AQ-01 to AQ-06 (acquired 2025-2026). AQ-01 to AQ-03 are fully integrated. AQ-04 (Tennessee, acquired 2025-11, about 88,000 people), AQ-05 (Florida, acquired 2026-03, about 38,500 people), and AQ-06 (Georgia, acquired 2026-05, about 12,800 people) remain on legacy SCADA, local accounts, and flat networks (the "3 of 6"). Together they have 5 plants and about 210 workforce members. AQ-05's RRA review was certified by its former owner on 2026-02-20 and its ERP review by the company on 2026-08-18; AQ-06's RRA review was certified by the company on 2026-06-22 using the former owner's checklist, and its ERP review is due 2026-12-22.

**Revenue per day.** About $13.2 million per calendar day across the company; regulated water revenue is about $11.8 million per calendar day. GCR revenue is about $1.6 million per calendar day.

**Additional roles (titles only).**
| Role | Duties in the deliverables |
|---|---|
| Chief Information Officer (CIO) | IT operations; owns the enterprise platform (common control provider) |
| Vice President, Gulf Coast Regional Operations | GCR-WTSS system owner; authorizing official equivalent is the COO |
| GCR SCADA Manager | Day-to-day GCR-WTSS administration, change control, and backups |
| Director of OT Engineering | OT standards, controller lifecycle, PLC change control, OT vulnerability remediation |
| Director of Identity and Access Management | Identity platform (SYS-05) and OT identity domains |
| Director of Cloud Platform Engineering | Cloud landing zones in both clouds (common control provider) |
| Director of Network Engineering | Enterprise network, SD-WAN, private LTE, radio, OT DMZ network build |
| Director of Endpoint Engineering | IT workstations, EDR, and endpoint baselines |
| Director of Third-Party Risk Management | Vendor tiering, contract security terms, SOC report reviews (in the GRC team) |
| Vice President, Integration Management Office | Integration of acquired systems |
| Vice President, Customer Operations | CIS, billing, contact centers, AMI |
| Vice President, Contract Services | SL-1 service line owner |
| Vice President, Utility Billing Services | SL-2 service line owner |
| Vice President, Supply Chain | Chemicals and critical spares |
| Vice President, Corporate Security | Physical security of plants and remote sites; corporate security operations center |
| Vice President, Corporate Communications | Media and customer communications during incidents |
| Vice President, Investor Relations | Investor communications; member of the disclosure committee |
| Chief Human Resources Officer | Onboarding, terminations, training records |
| Controller | SOX program owner for financial reporting controls |
| Director of Data Science | AI model development and monitoring; secretary of the AI governance committee |
| Director of Environmental Health and Safety | RMP programs, release reporting, LEPC liaison |
| Regional water quality managers | Tier 1 public notice decisions with the state utility president for each system |

**Disclosure committee membership (P08).** General Counsel (chair), CFO, Controller, CISO, Chief Privacy Officer, Chief Risk Officer, and Vice President, Investor Relations, advised by outside securities counsel. Adding the Chief Operating Officer is a remediation item (POAM-014).

**Service lines offered to municipal clients (P09).** SL-1 contract operations and remote monitoring: the company operates 38 municipal and industrial drinking water systems under operations and maintenance contracts, including 24x7 remote monitoring from the ROCCs through a contract-services monitoring platform. SL-1 has had an annual SOC 2 Type 2 report (Security, Availability) since 2024. The client systems' owners, not the company, certify their own RRAs and ERPs. SL-2 utility billing and customer care: billing, payments, contact center, and meter data management for 27 municipal utilities (about 610,000 accounts) in separate CIS tenants. SL-2 has no SOC 2 report yet.
