# Scenario facts: Cris Santos Company | Mining, Quarrying, and Oil and Gas Extraction | Enterprise

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or standard, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (publicly traded SEC registrant; independent crude oil producer and operator) |
| Business | Independent exploration and production company focused on crude oil (NAICS 211120 Crude Petroleum Extraction). It operates its own wells, field facilities, crude oil gathering lines, and produced water systems, with field SCADA at every well pad and facility. A field services division (also NAICS sector 21: drilling, well servicing, and water hauling) works only on the company's own wells, which is why headcount is high for the production volume |
| Location | **Headquarters in Florida** (corporate functions and colocation data center DC-1). Three operating areas, all onshore: **Permian Basin** (West Texas; about 74% of production), **Mid-Continent** (Oklahoma; about 22%, including the assets acquired in 2025), and **Florida** (Panhandle and South Florida mature waterfloods; about 4%). The **Integrated Operations Center (IOC)** in Midland, Texas runs field SCADA 24x7; the **Backup Control Center (BCC)** in Oklahoma City holds the hot standby SCADA servers; the **Florida regional control room** (Panhandle field office) runs the Florida fields. Colocation data center DC-2 is in Texas. **State law is handled generically:** notify under the law of each state where affected individuals reside, with Florida as the worked example |
| Workforce | 12,000 employees: about 3,100 corporate, technical, and office staff and about 8,900 field staff (operations, drilling, well servicing, water hauling, construction, maintenance). About 4,000 contractor workers are on company sites on a typical day |
| Assets operated | About 8,900 operated wells (Permian 5,600; Mid-Continent 2,880, of which 1,700 came with the 2025 acquisition; Florida 420), including about 2,300 water injection and saltwater disposal wells. 375 tank batteries, 46 compressor stations, 34 water handling and disposal facilities, 16 LACT (lease automatic custody transfer) units delivering to third-party pipelines |
| Production | About 190,000 barrels of oil equivalent per day net (about 72% oil), plus about 1.1 million barrels of produced water per day |
| Pipelines | About 850 miles of company-owned **crude oil gathering lines** (Permian and Mid-Continent), all onshore, all in rural areas, all 8 5/8 inch nominal outside diameter or smaller. 44 miles meet the **regulated rural gathering line** criteria (49 CFR 195.11(a)); the rest are **reporting-regulated-only** gathering lines (49 CFR 195.15). About 1,600 miles of produced water pipelines (not a hazardous liquid under Part 195). **No gas pipelines:** associated gas is sold at the outlet of each central facility into third-party gas gathering systems |
| Revenue | About $4.8 billion a year (fictional), about $13.2 million per calendar day |
| Owners and partners | Operator for about 1,400 non-operating working interest owners (joint interest billing) and pays about 68,000 royalty owners monthly, who live in all 50 states |
| Size status | Not small. 12,000 employees is above the SBA standard of 1,250 employees for NAICS 211120 (13 CFR 121.201) |
| Added at this size | SEC cybersecurity disclosure (Form 8-K Item 1.05; Reg S-K Item 106, 17 CFR 229.106); SOX IT general controls over production and revenue accounting; PHMSA gathering line duties; growth by acquisition (Mid-Continent operator acquired 2025-10) |
| Not in scope | Offshore, Outer Continental Shelf, and MTSA facilities (none). TSA-notified pipelines (none). Federal or tribal onshore leases (none; all leases are fee or state). EAR-controlled technology (none identified). SSI under 49 CFR Part 1520 (none held). Federal contracts (none). Payment cards (not accepted). Gas pipelines under 49 CFR Part 192 (none owned) |
| State law approach | Breach notification and data security: the law of each state where affected individuals reside, with Florida (Fla. Stat. 501.171) as the worked example. State oil and gas commission rules (permits, production reports, flaring) are operational, not cybersecurity rules, and are treated generically where they bear on cyber-physical safety |

## 2. People (role titles only)
| Role | Duties |
|---|---|
| Board (audit committee plus a risk committee) | Cyber oversight (Item 106 disclosure); the risk committee receives quarterly cyber and OT risk reporting |
| Chief Executive Officer; Chief Financial Officer | Accept Very High risk; materiality determinations with the disclosure committee |
| Chief Operating Officer (COO) | Business owner of field operations; authorizing official for the FSPA (P02) |
| Chief Information Security Officer (CISO) | Program owner for IT and OT security; reports to the CEO |
| Director of OT Security | OT security lead (reports to the CISO, dotted line to the Vice President, Operations Technology) |
| Chief Risk Officer | Enterprise risk management (ERM); owns the enterprise risk register |
| General Counsel | Chairs the disclosure committee |
| GRC team (10), Security Operations Center (24x7, in-house, with OT analysts and an MSSP for overflow), OT security team (7), Internal Audit (in-house) | Three lines model |
| Disclosure committee | 8-K materiality decisions (General Counsel chairs) |

## 3. Systems
| ID | System | Notes |
|---|---|---|
| SYS-01 | Enterprise SCADA platform: SCADA master servers at the IOC with hot standby at the BCC, regional SCADA servers at the Florida regional control room, historians, about 140 HMIs, 40 engineering workstations | One SCADA software platform for the Permian, the legacy Mid-Continent assets, and Florida. The Florida servers and 18 Florida HMIs run an operating system past end of vendor support |
| SYS-02 | Field control devices and communications: about 11,000 RTUs, PLCs, pump controllers, and flow computers; about 1,800 ESP variable speed drives; private LTE in the Permian core; licensed radio in the Mid-Continent and Florida; about 6,500 cellular modems | Safety shutdowns (gas detection, tank high-level, compressor emergency shutdown, gathering line high-pressure shutdown) are hardwired or run in separate safety controllers and do not depend on SCADA |
| SYS-03 | Hydrocarbon accounting and revenue distribution (commercial software, customer-managed on Cloud provider A) | Volumes, allocations, run tickets, state production and severance tax reports, revenue distribution, joint interest billing. SOX-relevant |
| SYS-04 | Multi-cloud estate (two public cloud providers, vendor-agnostic) plus 2 colocation data centers (DC-1 Florida, DC-2 Texas) | Cloud A: hydrocarbon accounting, historian replica, volume integration, owner and partner portal (SL-1). Cloud B: data platform, machine learning platform (P10), water services portal (SL-2). Two clouds share one landing zone design |
| SYS-05 | Identity platform (SSO, MFA, privileged access management, identity governance) | The OT identity domain (directory in the OT DMZ) is separate and not under identity governance; the acquired Mid-Continent assets still use the seller's directory |
| SYS-06 | ERP (finance, supply chain, maintenance work orders, payroll) | Vendor SaaS; SOX IT general controls tested annually |
| SYS-07 | Enterprise network (MPLS and SD-WAN to 60 field offices and yards), IT/OT boundary | OT DMZs at the IOC and BCC. The Florida regional control room has no OT DMZ, and the acquired Mid-Continent network is flat and reaches the enterprise WAN over a site-to-site VPN |
| SYS-08 | About 14,000 corporate endpoints, 3,500 rugged field tablets, 9,000 managed phones | EDR on 97% of corporate endpoints |
| SYS-09 | Seismic and reservoir data platform (geoscience applications and high-performance computing on Cloud B) | Trade secret data |
| SYS-10 | About 1,600 third-party vendors (210 with remote access to IT or OT) | Tiered third-party risk program; one cellular carrier serves 88% of field modems; the ESP vendor monitors its drives through its own cloud service |
| SYS-11 | Fleet telematics and HSE systems | Vehicle locations of field employees, gas detector data, HSE incident and spill reporting |
| SYS-12 | AI portfolio (11 use cases) | Governed by an AI council formed in 2025 |
| SYS-13 | Acquired Mid-Continent assets (AQ-MC): the seller's legacy SCADA (a different vendor platform) for 1,700 wells, its own control room in Oklahoma, legacy directory and flat network | Migration to the enterprise SCADA platform due 2027-06-30 |

**SSP system (P02):** the *Field SCADA and Production Accounting System (FSPA)*: the enterprise SCADA platform (SYS-01) at the IOC, BCC, and Florida regional control room; the field devices and communications connected to it (SYS-02); the OT DMZs and IT/OT boundary of SYS-07; the FSPA workloads on Cloud provider A (historian replica, volume integration service, field data capture app); and the hydrocarbon accounting system (SYS-03). It inherits common controls from the enterprise platform. The AQ-MC legacy SCADA (SYS-13) is an interconnected system outside the boundary until migration.

**Data flow in one line:** field devices (SYS-02) report to the SCADA servers (SYS-01); historians push data through the OT DMZ to the historian replica on Cloud A; field staff enter tank gauges and run tickets on tablets in the field data capture app; LACT flow computers send custody transfer tickets; the volume integration service sends daily volumes to hydrocarbon accounting (SYS-03), which pays owners and bills partners.

## 4. Current security posture: mostly compliant, with targeted gaps
**In place today:**
- A mature program aligned to CSF 2.0, with an OT security program aligned to NIST SP 800-82 Rev. 3 since 2024
- Annual risk analysis tied to ERM (NIST IR 8286)
- A policy hierarchy of policies, standards, procedures, and exceptions
- 24x7 SOC with OT analysts; passive OT network monitoring at the IOC, the BCC, and about 70% of Permian facilities
- PAM, including a remote access gateway for OT vendors (Permian and BCC)
- Quarterly access certification for IT systems
- Immutable backups for cloud and data center workloads
- Annual DR tests for tier-1 systems
- Tiered vendor reviews
- Annual SOC 2 Type 2 for the owner and partner portal (since 2025)
- SEC Item 106 disclosure in its 10-K

**Targeted gaps:**
1. **Acquisition integration.** The 2025 Mid-Continent acquisition (AQ-MC) still runs the seller's legacy SCADA for 1,700 wells on a flat network that reaches the enterprise WAN over a site-to-site VPN, with shared operator logins and an always-on integrator remote access tool. Migration is due 2027-06-30.
2. **Florida legacy.** The Florida regional control room has no OT DMZ (corporate-to-SCADA rules on one firewall), and its SCADA servers and 18 HMIs run an operating system past end of vendor support.
3. **Field device visibility.** The field device inventory is 82% complete. Devices on cellular backhaul are not seen by passive monitoring, 12% of modems are still on the carrier's public network, and firmware is not tracked for about 40% of controllers.
4. **Vendor remote access.** The ESP vendor monitors about 1,800 drives through its own cloud service, outside the enterprise remote access gateway, with a remote setpoint-write feature enabled on 260 drives.
5. **OT recovery.** The 2026 failover test from the IOC to the BCC took 9 hours against a 4-hour RTO. PLC and RTU programs are backed up centrally only for the Permian.
6. **Materiality.** The SEC materiality playbook has never been exercised for an OT scenario, and it has no agreed method to quantify deferred production quickly.
7. **AI.** 11 AI use cases, 7 with completed council review. The predictive maintenance model (AI-001) was expanded across the Permian before its fairness review by well group was repeated, and a proposal to let an optimization model write setpoints (AI-005) is pending.
8. **Carrier concentration.** One cellular carrier serves 88% of field modems, and about 70% of cellular sites have no second path.
9. **OT identity.** The OT identity domain and local SCADA accounts are outside quarterly access certification.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 | **NIST CSF 2.0 with NIST SP 800-82 Rev. 3 (voluntary benchmark),** enterprise-wide, plus every binding rule that touches cybersecurity or cyber-physical safety: SEC Form 8-K Item 1.05 and Reg S-K Item 106; PHMSA gathering line duties (49 CFR 195.11, 195.15, and Subpart B reporting); EPA oil discharge notice (40 CFR 110.6) and the SPCC high-level alarm option (40 CFR 112.9(c)(4)(iv)); state breach and data security laws (Florida worked example). Applicability screens for N21-R01 (USCG), N21-R02 (TSA), N21-R03 (CIRCIA, proposed), and PHMSA control room management (195.446) |
| Regulatory driver labels | `N21-BM (...)` is the P03 voluntary benchmark, with the specific SP 800-82 Rev. 3 section or CSF 2.0 subcategory in parentheses. It is a scenario label, not a row in `requirements.csv`. `N21-R03 (proposed)` marks CIRCIA items tracked but not yet required. `SEC Item 1.05`, `SEC Item 106`, `PHMSA 195.xx`, `EPA 40 CFR 110.6 / 112.9`, and `State breach laws (Fla. Stat. 501.171 worked example)` mark binding rules |
| P08 | Ransomware that starts in business IT and spreads toward field SCADA, including an **SEC materiality assessment and 8-K Item 1.05** step, PHMSA and oil discharge notices if a release follows, and a multi-state breach workflow for royalty owner and employee data |
| P09 | SOC 2 Type 2 readiness across two service lines offered to outside parties: SL-1 owner and partner services (portal, statements, and payments for royalty owners and non-operating partners) and SL-2 produced water gathering and disposal services for third-party operators |
| P10 | Enterprise AI portfolio (11 use cases) with the council operating model, and a full assessment of AI-001, the predictive maintenance model for well equipment |
| Cloud | Multi-cloud (vendor-agnostic) with common controls |

**Registry defaults kept.** The registry's primary system (field SCADA and production accounting), incident (ransomware from business IT toward field SCADA), and AI use case (predictive maintenance) all fit a producer of this size and were kept. At enterprise scale the SSP covers the shared SCADA platform for three operating areas, the incident adds the SEC disclosure step, and the AI use case sits inside a governed portfolio.

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-06-01 to 2026-07-31 | Enterprise risk analysis and gap analysis (IOC, BCC, Florida control room, and field site walkthroughs in June and July) |
| 2026-07-13 to 2026-08-28 | Control assessment (Internal Audit, third line; GRC team supported scoping) |
| 2026-09-10 | Results to the risk committee of the board |

## 7. Facts added for the deliverables
These facts were added while building the deliverables. They do not change sections 1-6.

**Additional roles (titles only).**
| Role | Duties in the deliverables |
|---|---|
| Chief Information Officer (CIO) | IT operations; owns the enterprise platform (common control provider) |
| Vice President, Operations Technology and Automation | FSPA system owner; SCADA platform, field automation, field communications |
| Vice President, Permian Operations; Vice President, Mid-Continent Operations; Vice President, Florida Operations | Regional field operations, manual operations, and shut-in decisions |
| Vice President, Midstream and Water | Crude gathering lines, produced water systems, LACT units; owner of SL-2 |
| Pipeline Compliance Manager | PHMSA gathering line program (195.11, 195.15, Subpart B reports) |
| Vice President, Health, Safety, and Environment (HSE) | Spill and release reporting, emergency response plans, SPCC plans |
| Vice President, Production and Revenue Accounting | Hydrocarbon accounting (SYS-03) data owner; owner of SL-1 |
| Vice President, Exploration and Reservoir Engineering | Seismic and reservoir data platform (SYS-09); production forecasting (AI-002, AI-003) |
| Vice President, Drilling and Completions | Drilling real-time operations (BP-06); rig data aggregation SaaS; drilling optimization advisory (AI-004) |
| Director, Owner Relations | Royalty owner and partner portal operations (SL-1) |
| Controller | SOX program owner for financial reporting controls |
| Chief Audit Executive | Heads Internal Audit; reports to the audit committee; leads the P07 assessment |
| Chief Compliance Officer | Regulatory compliance program; second line with the GRC team |
| Privacy Counsel (Legal) | Breach determinations and state notification decisions for personal information |
| Vice President, Data and Analytics | Chairs the AI council; owns the data platform and the machine learning platform |
| Director of Security Operations | Runs the SOC (common control provider) |
| Director of Identity and Access Management | Identity platform (SYS-05) |
| Director of Cloud Platform Engineering | Cloud landing zones in both clouds (common control provider) |
| Director of Network Engineering | Enterprise network, SD-WAN, private LTE core, IT/OT boundary firewalls (common control provider) |
| Director of Endpoint Engineering | Corporate endpoints, tablets, EDR (common control provider) |
| Director of Third-Party Risk Management | Vendor tiering, contract security terms, SOC report reviews (in the GRC team) |
| Vice President, Integration Management Office | Integration of AQ-MC |
| Chief Human Resources Officer | Onboarding, terminations, training records |
| Vice President, Corporate Security and Facilities | Physical security of offices, the IOC, the BCC, and field sites |
| Vice President, Investor Relations; Vice President, Corporate Communications | Investor and public communications; Investor Relations sits on the disclosure committee |
| SCADA integrators (2, contracted) | Integrator A supports the enterprise SCADA platform; Integrator B supports the AQ-MC legacy SCADA under a transition services agreement |

**Disclosure committee membership (P08).** General Counsel (chair), CFO, Controller, CISO, Chief Risk Officer, COO, and Vice President, Investor Relations, advised by outside securities counsel. The COO joined in 2026 so that operational impact is in the room.

**Volumes and money.** Oil sales about $9.6 million per day; Permian about 74% of revenue. Royalty and partner distributions about $520 million a month. Water services (SL-2) revenue about $95 million a year from about 35 third-party operators.

**Service lines offered to outside parties (P09).** SL-1: owner and partner services (owner and partner portal on Cloud A, monthly revenue and joint interest billing statements, direct deposit payments) for about 68,000 royalty owners and 1,400 non-operating partners. SL-1 has had a SOC 2 Type 2 report (Security, Availability, Confidentiality) since 2025. SL-2: produced water gathering and disposal for about 35 third-party operators in the Permian (SCADA-measured volumes, the water services portal on Cloud B, monthly invoices). SL-2 has no SOC 2 report yet.

**Operating areas and control.** The IOC controls the Permian and the legacy Mid-Continent assets on the enterprise platform; the BCC can take over all IOC functions; the Florida regional control room controls Florida and can be monitored (not controlled) from the IOC. AQ-MC is controlled from the seller's former control room in Oklahoma, staffed by company employees since closing.

**SPCC high-level alarm option.** 31 tank batteries (Mid-Continent and Florida) meet the overfill prevention requirement of 40 CFR 112.9(c)(4) by the high-level alarm option in (c)(4)(iv); the rest rely on container capacity or overflow equalizing lines.

**Personal information held.** Royalty owners: names, addresses, taxpayer identification numbers (most are Social Security numbers), bank account numbers for direct deposit. Employees: Social Security numbers, driver license and commercial driver license numbers, health plan identifiers, vehicle geolocation from telematics.

**Risk program and funding (P01).** Eight enterprise risks (ER-01 to ER-08) with board-approved tolerance thresholds. Treatment funding approved for 2026 Q4 to 2027 Q2: about $14.6 million.

**Policy set (P06).** 5 policies, 21 standards, and 15 procedures, including STD-01.8 OT Security Standard (the SP 800-82 Rev. 3 overlay and tailoring register), PRC-01.4 Acquisition Security Integration Procedure, PRC-02.5 SCADA Account Management, PRC-02.6 OT Vendor Sessions, and PRC-03.4 Regulatory Release Reporting (PHMSA and EPA).

**Internal Audit team for P07.** An IT audit manager, three IT auditors, and a contracted OT security specialist under the Chief Audit Executive.

**Recent operating history used as samples (P03).** 2025-01-01 to 2026-06-30: 3 severity-1 security incidents (none material), 7 gathering line accidents reported under 49 CFR 195.50, 1 immediate notice under 195.52, and 4 reportable oil discharges under 40 CFR 110.6. None was caused by a cyber event.

**SOC 2 plans (P09).** SL-1 adds Processing Integrity and Privacy for its 2027 report (period 2027-01-01 to 2027-12-31). SL-2's first Type 2 report covers Security, Availability, Confidentiality, and Processing Integrity (period 2027-04-01 to 2027-09-30). SL-2 customer agreements require notice within 24 hours of a service outage and 72 hours of a security incident affecting customer data.

**AI portfolio (P10).** 11 use cases: AI-001 predictive maintenance (Medium), AI-002 production forecasting, AI-003 seismic interpretation assistant, AI-004 drilling optimization advisory, AI-005 production optimization (High; advisory pilot, closed loop refused), AI-006 methane and leak detection analytics, AI-007 invoice coding, AI-008 owner chatbot on the SL-1 portal, AI-009 telematics driver scoring (High; suspended), AI-010 enterprise generative AI assistant, AI-011 SOC triage assistant. Not yet reviewed by the council: AI-006, AI-008, AI-009, AI-011.
