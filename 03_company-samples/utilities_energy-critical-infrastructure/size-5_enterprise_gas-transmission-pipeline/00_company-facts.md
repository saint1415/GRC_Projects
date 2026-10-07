# Scenario facts: Cris Santos Company | Energy | Enterprise

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or standard, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (publicly traded SEC registrant; parent of three FERC-regulated interstate pipeline subsidiaries) |
| Business | Interstate natural gas transmission (NAICS 486210). Owns and operates three interstate pipeline systems (**PS-1**, **PS-2**, **PS-3**) and is the contract operator of three joint-venture pipelines (**JV-1**, **JV-2**, **JV-3**) in which it holds minority or 50% interests. No storage fields, LNG facilities, gathering, or distribution |
| Location | Headquartered in Florida, with the **Primary Gas Control Center (GCC-1)** at headquarters. **Backup Gas Control Center (GCC-2)** in Alabama. PS-3 is still controlled from its **legacy control room (PS3-CR)** in Mississippi until it migrates to GCC-1. Pipelines cross 9 states: Texas, Louisiana, Mississippi, Alabama, Georgia, Florida, Tennessee, South Carolina, and North Carolina. **State law is handled generically:** breach notices follow the law of each state where affected individuals reside, with Florida as the worked example |
| Pipeline assets | About 11,600 miles of interstate transmission pipe (PS-1 about 5,300 miles; PS-2 about 4,200; PS-3 about 2,100). 96 compressor stations (PS-1 41, PS-2 35, PS-3 20) with about 2.4 million horsepower. About 1,480 receipt and delivery meter stations. About 2,300 mainline valve sites, 640 of them remote-controlled. About 6,900 field RTUs, PLCs, flow computers, and gas chromatographs. Design capacity about 11 billion cubic feet per day. The JV pipelines add about 1,150 miles and 9 compressor stations, controlled from GCC-1 |
| Customers | About 380 shippers under FERC-approved tariffs: local distribution companies, gas-fired power generators, marketers, producers, and industrial plants. The PS-1 mainline is a primary supply path for gas-fired power generation in Florida |
| Workforce | 12,000 employees: about 6,400 in field operations and compression; 1,900 in engineering, integrity, and projects; 310 in gas control (about 150 qualified controllers); 1,050 in IT and operational technology, including about 85 in cybersecurity; 420 in commercial operations; 1,920 in corporate functions |
| Revenue | About $4.8 billion a year (fictional), mostly firm transportation reservation charges. About $13.2 million per calendar day |
| Pipeline safety regulator | PHMSA inspects and enforces 49 CFR Parts 191 and 192 directly, because the pipelines are interstate. The company has control rooms with controllers who monitor and control the pipelines through SCADA, and compressor stations, so **all of 49 CFR 192.631** applies (the reduced-procedure exception in 192.631(a)(1) covers only distribution with fewer than 250,000 services or transmission without a compressor station). Procedures go to PHMSA on request (192.631(i)) |
| Economic regulator | FERC, under the Natural Gas Act (certificates and tariffs). Files FERC Form No. 567 system flow diagrams each year (18 CFR 260.8) and requests CEII treatment for engineering and vulnerability details (18 CFR 388.113) |
| TSA status | **Designated.** TSA notified PS-1, PS-2, and JV-1 before July 26, 2022, that they are critical (SD Pipeline-2021-02G Section II.A.1). PS-3 was designated under its prior owner; after the 2025-03 acquisition the company requested a Cybersecurity Implementation Plan amendment for the change of ownership (SD 02G Section VI.A). **SD Pipeline-2021-01G** (effective 2026-01-16 to 2027-01-15) and **SD Pipeline-2021-02G** (effective 2026-05-03 to 2027-05-02) apply in full |
| Securities | Publicly traded; not a smaller reporting company. SEC Form 8-K Item 1.05 and Regulation S-K Item 106 (17 CFR 229.106) apply. SOX Section 404 IT general controls are tested by a separate SOX program |
| Not in scope | NERC CIP (the company is not a NERC-registered entity and owns no Bulk Electric System assets); DOE Form DOE-417 (electric only); HIPAA (the company is not a covered entity; its employee health plan is administered separately); PCI DSS (shippers pay by wire or ACH); CIRCIA (proposed only, not in effect) |
| Added at this size | SEC disclosure; SOX IT general controls; FERC CEII; Sensitive Security Information under 49 CFR Part 1520 (TSA plans, assessments, and reports); a 2025 acquisition still being integrated (PS-3); two service lines offered to other companies (SL-1 and SL-2) |

## 2. People (role titles only)
| Role | Security and compliance duties |
|---|---|
| Board of directors: audit committee; risk committee | Risk committee oversees cybersecurity and operational risk quarterly (Item 106 governance). Audit committee oversees Internal Audit, SOX, and disclosure controls |
| Chief Executive Officer; Chief Financial Officer | Accept Very High risk jointly; take part in materiality determinations with the disclosure committee |
| Chief Operating Officer (COO) | Accountable executive for pipeline operations; **authorizing official equivalent for the PSGCS (P02)**; approves any precautionary shutdown of a whole pipeline system |
| Chief Information Security Officer (CISO) | Program owner for IT and OT security; alternate TSA Cybersecurity Coordinator |
| Director of OT Security | **Primary TSA Cybersecurity Coordinator** (SD 01G Section II.B); owns the Cybersecurity Implementation Plan and the Cybersecurity Assessment Plan; reports to the CISO |
| Director of Security Operations | 24x7 SOC, including the OT monitoring cell; alternate TSA Cybersecurity Coordinator |
| Chief Risk Officer | Enterprise risk management (ERM); owns the enterprise risk register |
| Chief Audit Executive | Heads Internal Audit (third line); reports functionally to the audit committee; leads the P07 assessment |
| General Counsel | Chairs the disclosure committee; SSI and CEII legal questions |
| Chief Compliance Officer | Regulatory compliance program (second line with the GRC team) |
| Vice President, Gas Control | **PSGCS system owner**; owns the control room management procedures (192.631) for GCC-1, GCC-2, and PS3-CR |
| Director of SCADA Engineering | Administers SCADA hosts, HMIs, historians, OT domain, and field device configurations |
| Vice President, Pipeline Safety and Compliance | PHMSA compliance: O&M manual (192.605), emergency plans (192.615), incident notices (Part 191), operator qualification |
| GRC team (10), SOC (24x7, in-house with managed security service provider overflow), Internal Audit (in-house, co-sourced with an independent OT assessment firm) | Three lines model |
| Disclosure committee | 8-K materiality decisions (General Counsel chairs) |
| AI governance committee | Chaired by the Vice President, Digital and Analytics; reviews and tiers every AI use case; High-tier decisions go to the executive risk committee (P10) |
| Policy governance committee | Chaired by the CISO; maintains the policy hierarchy and exception register (P06) |

## 3. Systems
| ID | System | Hosting | Notes |
|---|---|---|---|
| SYS-01 | Pipeline SCADA host servers, controller consoles, historians, and engineering workstations | On-premises at GCC-1 (primary) and GCC-2 (hot standby) | One SCADA platform for PS-1, PS-2, and JV-1 to JV-3. Separate OT domain with no trust to the business domain |
| SYS-02 | PS-3 legacy SCADA (different vendor) and control room | On-premises at PS3-CR, Mississippi | Migrating to SYS-01 by 2027-06-30. No hot standby; backup is manual station operation |
| SYS-03 | Compressor station control systems: unit control PLCs, station control PLCs, local HMIs, and station networks at 96 stations | On-premises at each station | Emergency shutdown systems are hardwired and independent of SCADA. 22 stations run end-of-support HMIs or PLC firmware |
| SYS-04 | Field devices at meter and valve sites: RTUs, PLCs, flow computers, gas chromatographs | About 1,480 meter stations and 640 remote valve sites | Flow computers keep at least 35 days of measurement data locally |
| SYS-05 | SCADA telecommunications: private licensed microwave and radio, carrier MPLS, satellite backup, and cellular gateways at about 520 sites | Field and carriers | Two carriers on the MPLS core |
| SYS-06 | IT/OT DMZs (one at each GCC) and the OT remote access gateway (privileged access, session recording, per-session approval) | On-premises | All vendor OT access is meant to pass through the gateway |
| SYS-07 | Enterprise identity platform (SSO, MFA, privileged access management for IT, identity governance) and the separate OT identity stack (OT domain, OT privileged access) | SaaS (IT); on-premises (OT) | No trust between the IT and OT domains |
| SYS-08 | Hybrid IT estate: two public cloud providers (Cloud provider A and Cloud provider B, vendor-agnostic) and two colocation data centers (DC-1 Florida, DC-2 Georgia) | Cloud and colocation | About 620 applications; about 16,000 endpoints |
| SYS-09 | Shipper services platform: nominations, scheduling, confirmations, capacity release, informational postings, and invoicing (service line SL-1) | Cloud provider A | Used by about 380 shippers and interconnecting pipelines |
| SYS-10 | Gas measurement and accounting system | Cloud provider A, with data from SYS-04 through the DMZ | Custody transfer volumes and gas quality |
| SYS-11 | ERP, payroll, and HR | SaaS | SOX-relevant; employee personal information |
| SYS-12 | Pipeline integrity, GIS, and analytics platform, including the AI workloads (P10) | Cloud provider B | CEII-level engineering data; historian data arrives one way through the DMZ |
| SYS-13 | Physical access control and video at GCC-1, GCC-2, PS3-CR, and compressor stations | On-premises | Treated as OT under the TSA definition |
| SYS-14 | About 1,100 third-party suppliers, about 140 with OT access or OT data | Various | Tiered third-party risk program |

**SSP system (P02):** the *Pipeline SCADA and Gas Control System (PSGCS)*: SYS-01 at GCC-1 and GCC-2, the SYS-02 PS-3 legacy SCADA as a subsystem in transition, the SCADA interfaces to the SYS-03 compressor station control systems, the SYS-04 field devices, the SYS-05 SCADA telecommunications, the SYS-06 DMZs and OT remote access gateway, the OT identity stack in SYS-07, and physical access control at the control rooms (SYS-13); categorized High.

## 4. Current security posture: mature, with residual gaps
**In place today:**
- A CSF 2.0-aligned program for IT and OT, with a TSA-approved Cybersecurity Implementation Plan since 2022 (amended 2025-09-12 to add the PS-3 integration schedule)
- A Cybersecurity Assessment Plan approved by TSA on 2025-11-14, with an independent architecture design review completed in 2025-04
- Annual enterprise risk analysis integrated with ERM (NIST IR 8286)
- A policy hierarchy of policies, standards, procedures, and exceptions
- A 24x7 SOC with an OT monitoring cell and passive OT network monitoring at GCC-1, GCC-2, and 74 of 96 compressor stations
- Separate OT domain, OT privileged access, and an OT remote access gateway with session recording
- Hot standby gas control at GCC-2, failover tested every year (192.631(c)(4))
- Immutable IT backups and offline SCADA backups at both GCCs
- Annual Cybersecurity Incident Response Plan exercise (SD 02G Section III.F.1.e), most recently 2026-03-18 at GCC-1
- Tiered third-party risk program with OT security terms in new contracts since 2024
- SOC 2 Type 2 report (Security and Availability) for the shipper services platform since 2025
- SEC Item 106 disclosure in the Form 10-K

**Residual gaps found in the 2026 assessments:**
1. **PS-3 integration.** The legacy SCADA has no hot standby, 12 of 20 PS-3 compressor stations have flat networks, and PS-3 still uses local accounts. The amended Cybersecurity Implementation Plan sets conformance by 2027-06-30.
2. **Legacy station controls.** 22 compressor stations (14 on PS-1 and PS-2, 8 on PS-3) run end-of-support station HMIs or PLC firmware with entries in CISA's Known Exploited Vulnerabilities Catalog that cannot be patched without unit outages. Documented mitigations exist for 15 of 22; the timeline slipped.
3. **Shared station accounts.** Shared operator accounts on station HMIs at 31 stations are permitted as critical for operations (SD 02G III.C.4), but 4 of 25 sampled departures did not trigger a password change (III.C.4.b).
4. **OT monitoring coverage.** No passive monitoring at 22 compressor stations (including all 20 PS-3 stations) or at meter and valve sites.
5. **Vendor remote access.** One compression equipment manufacturer monitors turbine units through always-on cellular modems outside the OT remote access gateway. The 2025 architecture design review found 18; 7 remain.
6. **IT/OT isolation testing.** Isolation was exercised at GCC-1 in 2026-03; GCC-2 and PS3-CR isolation has not been tested, and PS-3 manual operation has not been drilled at scale since the acquisition.
7. **Log retention.** 22 stations keep logs locally for 90 days and do not forward them, against a 12-month standard.
8. **Materiality.** The disclosure committee has not exercised an OT shutdown scenario; the materiality playbook does not include curtailment factors such as tariff reservation charge credits and shipper claims.
9. **AI.** 11 AI use cases; 7 have completed committee review. The leak-detection model (AI-001) has not been validated on PS-3, and vendor model updates bypassed change control twice in 2026.
10. **Supplier assurance.** No software bills of materials from the SCADA vendor; 2 of 6 critical OT suppliers lack incident notice terms.
11. **SSI handling.** 3 of 25 sampled TSA submission records were not marked as SSI (49 CFR 1520.13).
12. **OT patching.** 9% of applicable Known Exploited Vulnerabilities items on Critical Cyber Systems are past the plan's timeline.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 | TSA SD Pipeline-2021-02G applies in full and is the primary regulation, analyzed requirement by requirement with evidence sampling. Also analyzed: SD Pipeline-2021-01G, 49 CFR 192.631 (SCADA-relevant duties), 49 CFR Part 1520 SSI handling, FERC CEII handling, SEC Item 1.05 and Item 106, and state breach and data security laws (Florida worked example) |
| P08 | Ransomware on business IT forcing a precautionary shutdown of **one pipeline system (PS-1)**, with TSA incident reporting to CISA, PHMSA notices, and an **SEC materiality assessment and 8-K Item 1.05** step |
| P09 | SOC 2 Type 2 readiness across two service lines offered to other companies: SL-1 shipper services platform and SL-2 contract operations of the JV pipelines |
| P10 | Enterprise AI portfolio (11 use cases) with the AI governance committee, and a full assessment of AI-001, the pipeline leak-detection anomaly model |
| Cloud | Multi-cloud (vendor-agnostic) for business and analytics workloads. **OT stays on-premises;** no SCADA control function runs in a cloud |

**Registry defaults, adapted for this size.** The primary system (Pipeline SCADA and gas control system) and the AI use case (pipeline leak-detection anomaly model) are kept. The incident is kept, but at this size a precautionary shutdown is ordered for one pipeline system rather than the whole network, because GCC-1 runs three systems and the decision has to be made per system and segment.

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-06-01 to 2026-07-31 | Enterprise risk analysis and gap analysis (evidence sampling completed 2026-08-14) |
| 2026-07-13 to 2026-08-28 | Control assessment (Internal Audit with the co-sourced OT assessment firm; site visits to GCC-1, GCC-2, PS3-CR, and 6 compressor stations) |
| 2026-09-10 | Results to the risk committee of the board |
| 2026-11-14 | Annual Cybersecurity Assessment Plan update and annual report due to TSA (SD 02G Sections III.G.3 and III.G.4, 12 months after the 2025-11-14 approval) |
