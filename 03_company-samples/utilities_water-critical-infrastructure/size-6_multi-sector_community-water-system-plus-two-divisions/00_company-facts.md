# Scenario facts: Cris Santos Company | Water and Wastewater Systems | Multi-Sector

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a law, regulation, or standard, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company Holdings, Inc. (publicly traded SEC registrant) |
| Structure | A holding company with three divisions and corporate shared services. Each division is a set of legally separate subsidiaries under common ownership |
| Division 1: Water Utility (NAICS 221310), **focus of this scenario** | Investor-owned, rate-regulated water utility subsidiaries in 6 southeastern states. Owns and operates **58 community water systems** serving about **3.37 million people** through about 1.21 million service connections. About 4,200 employees. Drinking water only: the division runs no wastewater (POTW) systems. Rates are set by each state's utility commission |
| Division 2: Infrastructure Construction (NAICS 237110, sector 23 Construction) | Builds water and wastewater treatment plants, pipelines, and pump stations, and integrates their control systems, for the Water Utility, municipalities, industry, and federal clients including Department of Defense (DoD) installations. About 23,000 employees. Holds DoD contracts with DFARS 252.204-7012 (covered defense information) and other federal contracts with FAR 52.204-21 |
| Division 3: Environmental Services (NAICS 562910, sector 56 Administrative and Support and Waste Management and Remediation Services) | Groundwater and soil remediation, liquid and hazardous waste transport, two liquid waste treatment facilities, and a hosted **remote monitoring and compliance data service** for about 210 client treatment systems. About 13,800 employees. Federal remediation contracts with FAR 52.204-21. Not part of the CISA Water and Wastewater Systems Sector, which covers drinking water and wastewater utilities, not NAICS 562 |
| Corporate shared services | Identity, network, security operations, OT security services, cloud and data platform, finance, HR, legal, and internal audit. About 4,000 employees |
| Location | Headquartered in Florida. The Water Utility operates in 6 southeastern states; Construction and Environmental Services work in about 30 states. **State law is handled generically** ("each state where affected individuals reside"), with Florida as the worked example |
| Workforce / revenue | 45,000 employees; about $18.0 billion revenue (fictional) |
| Why these three divisions | A water group covering supply (Water Utility), construction of water infrastructure (Construction), and treatment and remediation services (Environmental Services) |

## 2. People (role titles only)
| Role | Duties |
|---|---|
| Board risk committee | Group cyber and operational risk oversight; accepts Very High risks |
| Group CISO | Group security program, group policies, common controls (SYS-G1 to SYS-G4) |
| Group Chief Risk Officer | Group risk register and enterprise risk management roll-up; co-accepts High risks |
| Group OT Security Director (reports to the Group CISO) | Group OT security standard, the OT remote access gateway (SYS-G4), and OT monitoring |
| Group Chief Privacy Officer | Customer and employee personal information across divisions |
| Group General Counsel | Contracts, notification matrix, regulator and SEC filings with the disclosure committee |
| Division presidents (3) | Accept Moderate risks for their division |
| Division security and compliance leads (3) | Division registers, division supplements, division-specific regulators |
| Water Utility VP of Water Quality and Compliance | Primacy agency relationships; public notification decisions; RRA and ERP certifications (signs with the Water Utility president) |
| Water Utility Emergency Management Director | RRA and ERP program manager for the 42 covered systems |
| Regional System 1 Director of Operations | System owner of the SSP system (RS1-SCADA) |
| Construction CMMC program owner (the Construction security and compliance lead) | NIST SP 800-171 and CMMC for the CUI enclave; DFARS incident reporting |
| Environmental Services hazmat compliance manager | Hazardous materials security plan (49 CFR 172.800-172.804) |
| Group internal audit | Assesses common controls once; samples division controls; reports to the board audit committee |
| Disclosure committee | SEC materiality decisions |
| Group AI council | AI use-case approval (P10) |

## 3. Systems
| ID | System | Owner | Notes |
|---|---|---|---|
| SYS-G1 | Group identity platform (single sign-on, MFA, privileged access management, identity governance) | Corporate | All IT identities. Each regional OT directory federates to SYS-G1 for MFA at the 14 regional SCADA systems; the 19 acquired water systems use local OT accounts |
| SYS-G2 | Group SOC (24x7), SIEM, EDR, and OT network monitoring | Corporate | Passive OT monitoring sensors at the 6 largest water systems only |
| SYS-G3 | Group cloud platform (two providers, vendor-agnostic) and data platform | Corporate | Historian replicas, analytics, the water-quality anomaly detection model, and hosting for SYS-E1 |
| SYS-G4 | Group OT secure remote access gateway (jump hosts with MFA, per-session approval, and session recording) | Corporate (Group OT Security Director) | Serves Water Utility operators and integrators, Construction commissioning engineers, and Environmental Services technicians. Covers the 14 regional SCADA systems; not yet the 19 acquired systems |
| SYS-G5 | Group ERP, finance, HR, and payroll | Corporate | SaaS |
| SYS-W1 | Water Utility SCADA: 14 regional SCADA systems serving the 39 legacy-owned water systems, plus local SCADA at the 19 acquired systems | Water Utility | Acquired systems migrate to regional SCADA by 2028 |
| SYS-W2 | Customer information and billing system (CIS), customer portal, and AMI head-end | Water Utility | Vendor SaaS; about 1.21 million accounts. Card payments go through a payment processor's hosted page and IVR, so card numbers do not enter group systems |
| SYS-W3 | Laboratory information management system (LIMS) and compliance reporting to primacy agencies | Water Utility | Vendor SaaS |
| SYS-W4 | GIS, work and asset management, and mobile field applications | Water Utility | Vendor SaaS; holds critical asset locations |
| SYS-C1 | Construction project delivery platform (project management, BIM and CAD, document control) | Construction | Commercial cloud. Not authorized for CUI |
| SYS-C2 | Construction CUI enclave (separate tenant in a government-community cloud offering that meets FedRAMP Moderate equivalency, with virtual desktops) | Construction | The only system authorized for covered defense information |
| SYS-C3 | Commissioning and controls integration toolkit (about 600 engineering laptops with PLC and HMI programming software) | Construction | Connect to client and Water Utility OT during commissioning |
| SYS-C4 | Construction ERP and job cost, certified payroll, equipment telematics | Construction | SaaS |
| SYS-E1 | Remote monitoring and compliance data service (multi-tenant, hosted on SYS-G3) with cellular gateways at about 210 client sites | Environmental Services | Clients use the data in their own permit compliance reports |
| SYS-E2 | Environmental Services field operations: fleet routing and telematics, hazardous waste manifests, scale-house systems, and plant control systems at the 2 liquid waste treatment facilities | Environmental Services | |

**SSP system (P02):** the *Regional System 1 Water Treatment SCADA (RS1-SCADA)*: the SCADA servers, HMIs, engineering workstations, historian, PLCs, RTUs, telemetry, and OT networks of Regional System 1's three treatment plants and its remote sites, which inherit common controls from SYS-G1, SYS-G2, SYS-G3, and SYS-G4.

## 4. Current security posture: a defined group program, maturity varies by division
**In place today:**
- Group policies aligned to NIST CSF 2.0 and a common control catalog (2025)
- 24x7 group SOC with EDR on all IT endpoints and servers; passive OT network monitoring at the 6 largest water systems
- Group OT remote access gateway (SYS-G4) with MFA and session recording for the 14 regional SCADA systems
- Privileged access management and quarterly access certification for IT
- Immutable backups for IT and cloud; offline PLC and HMI backups at the 6 largest water systems
- All 42 covered water systems certified their RRAs and ERPs on time in both five-year cycles
- Manual operation capability and annual manual-mode drills at every treatment plant; hardwired chemical feed limits and independent analyzer alarms at the plants of the 15 largest systems
- Construction CUI enclave in operation since 2024; CMMC Level 2 (Self) assessment posted in SPRS on 2025-12-12
- Environmental Services hazardous materials security plan reviewed every year
- SEC Reg S-K Item 106 disclosure; disclosure committee charter covers cybersecurity incidents
- Membership in the water sector's information sharing and analysis center; subscription to CISA advisories

**Gaps:**
1. **OT remote access outside the gateway.** The 19 acquired water systems still use vendor remote desktop tools or password-only VPNs. Inside the gateway, a 2025 exception let the Construction commissioning team for the WTP-A expansion connect to RS-1 without per-session approval.
2. **Acquired water systems not integrated.** The 19 systems acquired since 2021 have flat OT networks, shared HMI logins, end-of-support operating systems, no OT monitoring, and no offline PLC backups.
3. **RRA and ERP consistency.** Each of the 42 covered systems certifies separately. The cyber element of the 27 mid-size RRA reviews (certified 2026-06-24) used a generic checklist without asset inventories or vulnerability data. Their revised ERPs are due by 2026-12-24.
4. **Construction CUI handling.** The 2026 internal audit found covered defense information outside the CUI enclave (on commissioning laptops and SYS-C1) and other requirements recorded as MET in the 2025 CMMC Level 2 (Self) assessment that are not met. The annual affirmation is due 2026-12-12, and DoD CMMC Phase 2 begins 2026-11-10.
5. **Environmental Services monitoring service.** Clients ask for a SOC 2 report; none exists. Cellular gateways at client sites have inconsistent hardening, and the service has no documented service commitments.
6. **Shared incident notification.** A cross-division OT incident may trigger Tier 1 public notices and primacy agency consultations in several states, a DFARS 72-hour report, client contract notices, state utility commission contacts, and an SEC materiality decision. The group notification matrix is not yet exercised.
7. **Common control inheritance.** Documented for the Water Utility (2025) but not for Construction or Environmental Services.
8. **AI governance.** The water-quality anomaly detection model went live at the 6 largest systems before its validation was complete, and operators are told to act on its alerts. Division AI uses (estimating, job-site video analytics, client alerting) are not all inventoried.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 | Water Utility: SDWA section 1433 (42 U.S.C. 300i-2), primary, with the SDWA public notification rule (40 CFR 141 Subpart Q). Construction: DFARS 252.204-7012 with NIST SP 800-171 Rev. 2 and the CMMC Program (32 CFR Part 170), plus FAR 52.204-21 and 52.204-25. Environmental Services: NIST CSF 2.0 as the voluntary baseline, with the binding pieces mapped (FAR 52.204-21, 49 CFR 172.802, 16 CFR 682.3). Group-wide: SEC, state breach laws, OFAC; CIRCIA tracked as proposed only. Regulation-by-division matrix |
| P08 | Remote-access compromise of a treatment-plant HMI at WTP-A (RS-1) through the group OT remote access gateway, using a Construction commissioning engineer's session. The incident spans all three divisions: Water Utility public health notices, Construction DFARS reporting, Environmental Services client service impact, and SEC materiality |
| P09 | Scoping per division. In scope: the Environmental Services remote monitoring and compliance data service (a true service organization). Out of scope, with reasons: the Water Utility and Construction |
| P10 | Group AI governance program, with the water-quality anomaly detection model (registry default, kept because it fits: it now runs at the 6 largest systems) as the priority use case, plus division use cases |
| Cloud | Shared corporate platform (two providers, vendor-agnostic) plus division workloads, and a separate government-community cloud tenant for the Construction CUI enclave |

The registry defaults for the primary system (water treatment SCADA), the incident (remote-access compromise of a treatment-plant HMI), and the AI use case (water-quality anomaly detection) all fit the business at this size and were kept. The incident was widened to cross divisions, because the remote access path is a shared corporate service.

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2025-03-26 | RRA five-year reviews certified for the 6 systems serving 100,000 or more (deadline 2025-03-31); ERPs certified 2025-09-22 |
| 2025-12-17 | RRA reviews certified for the 9 systems serving 50,000 to 99,999 (deadline 2025-12-31); ERPs certified 2026-06-15 |
| 2026-06-24 | RRA reviews certified for the 27 systems serving 3,301 to 49,999 (deadline 2026-06-30) |
| 2026-05-04 to 2026-07-31 | Group and division risk analyses, BIAs, and gap analyses |
| 2026-07-06 to 2026-08-28 | Common control assessment (group internal audit) plus division samples, with site visits to RS-1 and 4 acquired systems |
| 2026-09-15 | Results to the board risk committee; deliverables approved |
| 2026-11-10 | DoD CMMC Phase 2 begins (32 CFR 170.3(e)(2)) |
| 2026-12-11 | Internal target to certify the 27 revised ERPs |
| 2026-12-12 | CMMC annual affirmation due for the CUI enclave |
| 2026-12-24 | Latest ERP certification date for the 27 systems (six months after their 2026-06-24 RRA certifications) |

## 7. Facts added while building the deliverables
These facts were added so the deliverables could be completed. They do not change sections 1 to 6.

| Topic | Added fact |
|---|---|
| SDWA section 1433 coverage by system | 6 systems serve 100,000 or more (about 1,960,000 people; the largest is Regional System 1); 9 serve 50,000 to 99,999 (about 630,000); 27 serve 3,301 to 49,999 (about 756,000); 16 serve 3,300 or fewer (about 26,000) and are outside section 1433, though the group OT standard still applies to them. 42 systems are covered. Each covered system certifies separately to EPA |
| Acquired systems | 19 of the 58 systems were acquired from 2021 to 2025: 2 in the 50,000 to 99,999 tier, 9 in the 3,301 to 49,999 tier, and 8 serving 3,300 or fewer |
| Regional System 1 (RS-1) | Florida; about 640,000 people and 228,000 connections. **WTP-A** (surface water: coagulation, sedimentation, filtration, chloramine disinfection; 120 MGD), **WTP-B** (groundwater lime softening; 60 MGD), **WTP-C** (groundwater nanofiltration; 30 MGD); 61 wells, 24 storage tanks, 41 booster stations. Regional operations center (ROC) control room at WTP-A; backup control room at WTP-B. Sodium hydroxide (caustic) is used for pH adjustment at WTP-A |
| RS1-SCADA components | Redundant SCADA servers at the ROC and the backup control room, 46 HMIs, 3 engineering workstations, a process historian (replicated to SYS-G3), about 150 PLCs, about 290 RTUs, licensed radio and private cellular telemetry. Modernized in 2019 |
| WTP-A expansion | A 40 MGD membrane expansion built by Construction for the Water Utility since 2025 under an intercompany construction contract. 34 Construction commissioning engineers hold SYS-G4 accounts for RS-1; a 2025 exception approved by the Water Utility security and compliance lead waived per-session approval for this team until project completion (2027-06-30) |
| Construction federal work | 14 active DoD contracts with DFARS 252.204-7012 (covered defense information: controlled technical information in facility drawings for installation water and wastewater systems), and 22 other federal contracts with FAR 52.204-21 only. About 1,900 active projects in total |
| CMMC status | A CMMC Level 2 (Self) assessment of the CUI enclave was posted in SPRS on 2025-12-12 with all 110 NIST SP 800-171 Rev. 2 requirements recorded as MET. The annual affirmation is due 2026-12-12. A Level 2 (C3PAO) assessment is scheduled for 2027-02 |
| Environmental Services scale | About 210 client treatment systems on SYS-E1 (industrial pretreatment systems and remediation treatment systems); 31 of them are at federal sites under remediation contracts (FCI). 38 clients have asked for a SOC 2 report. About 1,400 trucks, of which about 160 haul hazardous waste in quantities covered by 49 CFR 172.800(b). Two liquid waste treatment facilities with their own PLC and HMI control systems |
| Intercompany | Construction builds for the Water Utility (about $1.4 billion a year, eliminated in consolidation). Environmental Services hauls treatment residuals from Water Utility plants. The Water Utility does not use SYS-E1 |
| Revenue split (fictional) | Water Utility about $2.4 billion; Construction about $9.4 billion external; Environmental Services about $6.2 billion. Total about $18.0 billion, as in section 1 |
| Cloud | Provider A (primary) hosts the corporate landing zone, the data platform with historian replicas and the anomaly detection model, SYS-E1, and Water Utility cloud workloads. Provider B hosts the disaster recovery replica of the data platform and the immutable backup vault. SYS-C2 runs in a government-community cloud offering of provider A, in a separate tenant with its own identity configuration. SYS-W2, SYS-W3, SYS-W4, SYS-C1, SYS-C4, and SYS-G5 are vendor SaaS |
| AI use cases (P10 inventory) | Besides the anomaly detection model, the inventory lists: main-break prediction for capital planning and AMI leak alerts to customers (Water Utility); a customer service virtual agent (Water Utility); a generative estimating assistant and job-site safety video analytics (Construction); client anomaly alerts in SYS-E1 and route optimization (Environmental Services); and an enterprise generative AI assistant piloted with 3,000 users (Group). The Group AI Standard and Group AI council were set up in 2026 |
| Anomaly detection model | Built in house on SYS-G3 from historian data. Scores turbidity, chlorine and chloramine residual, pH, and flow signals every minute and alerts ROC operators. In production at the 6 largest systems since 2026-03-02. It never changes setpoints |
| Risk acceptance | Very Low and Low: division security and compliance lead. Moderate: division president. High: Group Chief Risk Officer with the Group CISO, reported to the board risk committee. Very High: board risk committee only. Risks to public health or worker safety rated High may not be accepted; they must be treated |
| Out of scope by fact | The group operates no publicly owned treatment works and no wastewater utility. No division handles PHI as a HIPAA covered entity or business associate. No division holds classified contracts. The Water Utility holds no federal contracts |
