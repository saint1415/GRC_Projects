# Scenario facts: Cris Santos Company | Mining, Quarrying, and Oil and Gas Extraction | Mid-Market

All 11 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a regulation or standard, the citation is given. This scenario is independent of the other sizes.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (privately held; private equity-backed; board with an audit committee) |
| Business | Independent crude oil producer and operator (NAICS 211120 Crude Petroleum Extraction). Operates mature onshore oil fields under waterflood, with field SCADA at every well pad and facility. Also owns and operates a crude oil gathering system in the Panhandle that carries its own crude and that of 5 third-party producers (shippers) to a third-party transmission pipeline |
| Location | Headquarters (administration, accounting, engineering, IT) in northwest Florida. Three onshore operating areas, each with a field office: **Panhandle** (Florida; also houses the Operations Control Center (OCC) and the Panhandle Central Facility), **South Florida** (Florida), and **Southwest Alabama** (Alabama; also houses the Backup Control Center (BCC)). No offshore, Outer Continental Shelf, or waterfront facilities |
| Workforce | 850 employees (see section 2 for the breakdown) |
| Assets operated | 640 wells: 420 producing oil wells (290 rod pump, 130 electric submersible pump (ESP)), 160 water injection wells, 24 saltwater disposal wells, 36 shut-in wells. 16 central tank batteries (8 Panhandle, 4 South Florida, 4 Alabama), 3 water injection plants (one per area), 4 associated-gas compression stations (3 Panhandle, 1 Alabama), and the Panhandle Central Facility (gathering pump station and 6 lease automatic custody transfer (LACT) units with flow computers) |
| Producing wells by area | About 220 in the Panhandle (radio), 110 in South Florida (mostly cellular, polled every 15 minutes), and 90 in Southwest Alabama (radio); used for the AI-001 bias testing in P10 |
| Gathering system | 92 miles of crude oil gathering lines (all 8 5/8 inch nominal outside diameter or smaller) in the Panhandle, from the 8 Panhandle tank batteries and the 5 shippers' leases to the Panhandle Central Facility. **14 miles of 8-inch trunk line** run in a rural area within one-quarter mile of a drinking water unusually sensitive area and operate above 20% of specified minimum yield strength, so they are **regulated rural gathering lines** (49 CFR 195.11(a)). The other **78 miles** are **reporting-regulated-only gathering lines** (49 CFR 195.1(a)(5), 195.15). Segment record: EV-045; obligations register N21-P195-RRGL and N21-P195-RPT. Crude leaves the company at the LACT units into the third-party transmission pipeline |
| Production | About 9,800 barrels of oil per day gross operated (Panhandle 5,600; South Florida 2,100; Alabama 2,100), plus associated gas and about 340,000 barrels of produced water per day that is reinjected or disposed of. The gathering system also carries about 1,400 barrels per day for third-party shippers (EV-056) |
| Revenue | About $265 million a year (fictional): crude oil sales about $240 million (about $660,000 per day: Panhandle $375,000, South Florida $140,000, Alabama $140,000), associated gas and natural gas liquids about $13 million, gathering fees from shippers about $6 million, operator overhead recoveries and other about $6 million (EV-055) |
| Size status | SBA-small. NAICS 211120 uses an employee-based standard of 1,250 employees (13 CFR 121.201); 850 employees is below it (EV-003). The Mid-Market tier is used for its program depth (500 to 999 employees), as the README sizing note explains. The effect on the proposed CIRCIA size test is recorded in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (N21-R03) |
| How product leaves the lease | Panhandle crude: through the company's gathering system and LACT units into the third-party transmission pipeline. South Florida and Alabama crude: sold at the lease tank batteries and hauled by the purchaser's tank trucks. Associated gas is sold at lease sales meters into third-party gas gathering systems. Well-to-battery flow lines are production facilities that Part 195 excludes (195.1(b)(8)); tank truck movements are excluded too (195.1(b)(9)(i)) |
| Owners and partners | A private equity fund holds about 80%; management holds the rest. The board has 7 directors, including 1 independent director who chairs the audit committee. The company is operator for 22 non-operating working interest owners (joint interest billing) and pays about 14,000 royalty owners monthly. A reserve-based credit facility is provided by a bank group |
| Sensitive data | Seismic and reservoir data (trade secret); well control, process safety, and pipeline safety data (shutdown logic, maximum operating pressure (MOP) settings, segment identification records); royalty owner records for about 14,000 owners (names, Social Security or taxpayer numbers, bank account numbers); employee records for 850 employees (Social Security numbers, driver license and commercial driver license numbers, health plan IDs); vehicle telematics locations; shippers' volumes and crude quality data (confidential under the gathering agreements) |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): offshore/OCS and MTSA facilities (none; N21-R01, BSEE), TSA-designated pipelines (none; the company has received no TSA notification; N21-R02), EAR-controlled technology (none identified), SSI under 49 CFR Part 1520 (none held), federal contracts (none), payment cards (not accepted), and SEC reporting (private company) |
| State law approach | The company operates in Florida and Alabama, and its royalty owners live in more than 40 states. State breach and data security law is treated generically: the law of each state where affected individuals reside applies, and **Florida (Fla. Stat. 501.171) is the worked example** (obligations register FL-501.171 and ST-BREACH). Alabama and other states' requirements are confirmed by counsel at the time of an incident rather than restated here. State oil and gas program requirements (permits, production reports, injection permits) are operational, not cybersecurity rules, and are cited only where a cyber event could cause a violation |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Board audit committee | Oversees cyber risk; receives quarterly reports on top risks, POA&M status, and incidents |
| Chief Executive Officer (CEO) | Accepts High risks; approves the risk appetite, POL-01, and the security budget |
| Chief Operating Officer (COO) | Executive sponsor of the security program and system owner of the Field SCADA and Production Accounting System (FSPA); accepts Moderate risks; chairs the crisis management team |
| Chief Financial Officer (CFO) | Owns production accounting, revenue distribution, treasury, and cyber insurance; approves payment and finance controls |
| General Counsel | Legal privilege, breach determinations with outside counsel, contract security terms, regulatory notices |
| Vice President of Information Technology (VP IT) | Owns business IT, cloud, and the identity provider; reports to the CFO |
| Security Manager | Information Security Lead and program owner; reports to the VP IT with a dotted line to the audit committee chair; leads a GRC Analyst and a Security Analyst; oversees the MDR provider |
| GRC Analyst | Risk register, policy and standard upkeep, vendor reviews, evidence for audits and SOC 2 |
| Security Analyst | SIEM and MDR liaison, vulnerability management, identity security |
| Vice President of Operations (VP Operations) | Business owner of field operations; must agree to any risk acceptance that affects field operations or safety |
| Field Superintendents (3) | Panhandle, South Florida, Southwest Alabama; manual operations and shut-in decisions; field site access |
| SCADA and Automation Manager | OT technical owner; manages 3 area automation supervisors, 18 automation technicians, and the SCADA integrator |
| OT Security Engineer | OT security day to day (OT DMZ, jump host, OT monitoring sensors, OT patching); reports to the SCADA and Automation Manager with a dotted line to the Security Manager |
| Control Room Manager | Runs the 24x7 OCC and the BCC; supervises 14 Production Controllers |
| Production Controllers (14) | Staff the OCC around the clock (3 per shift); monitor alarms, start and stop wells, and run the gathering pump station remotely |
| Pipeline Compliance Manager | Owns 49 CFR Part 195 compliance for the gathering system: segment identification, MOP, operator qualification, damage prevention, public awareness, accident and annual reporting |
| Measurement Supervisor | LACT proving, flow computer configuration, shipper volume statements |
| HSE Director | Spill and release reporting, H2S safety, emergency response plan |
| Production Accounting Director | Allocations, run tickets, royalty and revenue distribution, joint interest billing, shipper invoicing |
| Production Engineering Manager | Owner of the predictive maintenance model (AI-001) |
| Reservoir Engineering Manager | Owner of seismic and reservoir data (trade secret) |
| HR Director | Onboarding, terminations, background checks, training records |
| SCADA integrator (contractor) | Configures SCADA servers, HMIs, and field controllers; remote access through the jump host |
| MDR provider (contractor) | 24x7 managed detection and response for corporate endpoints, servers, identity, and cloud; may isolate hosts |
| Co-sourced internal audit firm | Annual IT audit and the P07 control assessment; reports to the audit committee |
| External auditor | Financial statement audit (not the P07 assessor and not the future SOC 2 service auditor) |

Headcount (850): executives and managers 30; field operations (superintendents, foremen, lease operators) 210; Production Controllers 14; well servicing rigs and crews 120; roustabout crews 85; water handling and injection plants 52; gathering operations and measurement 26; water and fluid haul drivers 70; mechanics and compressor technicians 48; SCADA and automation 24 (including the OT Security Engineer); engineering and geoscience 34; HSE and regulatory 18; production accounting 32; finance, joint interest billing, and treasury 22; land 10; HR 9; legal 3; IT and security 22 (18 IT, 4 security); supply chain and warehouse 21.

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv). Suppliers are in [`step-00_P00_intake/vendor-register.csv`](step-00_P00_intake/vendor-register.csv).

| ID | System | Hosting | Sensitive data? | Notes |
|---|---|---|---|---|
| SYS-01 | SCADA control centers: primary SCADA server pair, historian, 12 HMIs and 4 engineering workstations at the OCC; 3 HMIs at the South Florida field office; Backup Control Center (BCC) at the Alabama field office with a standby SCADA server and 4 HMIs | On-premises: OCC (Panhandle field office), South Florida field office, BCC (Alabama field office) | Yes (process data, well control, pipeline safety data) | Primary OCC upgraded to a supported SCADA and operating system version in 2025. The BCC standby server and the 3 South Florida HMIs still run an operating system past end of vendor support (EV-015) |
| SYS-02 | Field control devices and communications: about 610 RTUs and PLCs, 130 ESP variable speed drives, 260 electronic flow meters, 6 LACT units with flow computers, gathering pump station PLC, licensed radio network (Panhandle and Alabama), 180 cellular modems on the carrier's private network (South Florida and remote sites), 2 microwave backhaul links | Field sites | Yes (control logic, measurement configuration) | Safety shutdowns (H2S detection, tank high-level, compressor emergency shutdown) and the pump station's high-pressure shutdown switches are hardwired and do not depend on SCADA. About 140 older RTUs cannot support authenticated protocols (EV-014, EV-045) |
| SYS-03 | Production accounting and revenue distribution | Vendor SaaS (SOC 2 Type 2; EV-051) | Yes (royalty owner PI, volumes, revenue) | Allocations, run tickets, state production reports, royalty payments to about 14,000 owners, joint interest billing to 22 partners, shipper invoicing |
| SYS-04 | Cloud landing zone with 5 accounts (identity and security, connectivity, OT data, business workloads, backup) | Public cloud provider (vendor-agnostic) | Yes | OT data account: historian replica and measurement data service. Business workloads account: field data capture app, volume integration service, shipper portal, data platform (reservoir and seismic data, historian exports), machine learning workspace (AI-001). Backup account: immutable vault in a second region (EV-026, EV-029) |
| SYS-05 | Identity provider (single sign-on and MFA) | SaaS | No (identities only) | Protects SYS-03, SYS-04, SYS-06, SYS-07, SYS-10, SYS-11, and the OT jump host. SCADA HMIs at the OCC use named SCADA accounts synchronized from an OT directory, not the identity provider (EV-001, EV-005) |
| SYS-06 | ERP (general ledger, payables, purchasing, maintenance work orders) | Vendor SaaS | Yes (vendor banking) | Work order history feeds AI-001; invoice coding feature (AI-005) |
| SYS-07 | Productivity suite (email, files, chat) | SaaS | Yes (incidental) | Enterprise generative AI assistant (AI-002) licensed for 300 users (EV-031, EV-058) |
| SYS-08 | Corporate and OT networks | On-premises | Yes (in transit) | SD-WAN linking headquarters and 3 field offices. **OT DMZ at the OCC (built 2025)**: the historian replica feed, the OT jump host, and patch staging are the only crossings. The South Florida field office HMIs and the BCC reach the OCC over the corporate SD-WAN through site firewalls without a DMZ (EV-017, EV-019) |
| SYS-09 | Corporate endpoints | On-premises and mobile | Yes (cached) | 520 laptops and desktops, 240 rugged tablets (lease operators and gaugers), 300 managed smartphones. EDR on laptops, desktops, and servers (EV-012, EV-013) |
| SYS-10 | HR and payroll | Vendor SaaS | Yes (employee PI) | Includes an AI candidate-screening feature that is licensed but switched off (AI-004; EV-058) |
| SYS-11 | Fleet telematics | Vendor SaaS | Yes (employee geolocation) | GPS units in 380 vehicles and trucks |
| SYS-12 | OT remote access | Jump host in the OT DMZ with MFA and session recording (since 2025; EV-018) | Access path | SCADA integrator and company engineers use it. **Exceptions:** the compressor packager's always-on cellular gateways at the 4 compression stations and the flow computer vendor's support modem at the Panhandle Central Facility bypass it (EV-018) |
| SYS-13 | Security tooling | SaaS and on-premises | Logs | SIEM operated with the MDR provider (identity, cloud, firewall, EDR, jump host logs; 1-year retention); OT passive monitoring sensors at the OCC and the Panhandle Central Facility only; vulnerability scanner; privileged access management for cloud and directory administrators (EV-022, EV-024, EV-025, EV-006) |
| SYS-14 | Crude measurement and shipper services | SCADA network (flow computer polling), OT data account (measurement data service), business workloads account (shipper portal) | Yes (shipper confidential data) | LACT tickets, meter proving records, and daily shipper volume statements; 5 shippers log in to the portal (EV-027) |

**SSP system (P02):** the *Field SCADA and Production Accounting System (FSPA)*: SYS-01, SYS-02, SYS-12, and SYS-14; the OT DMZ and SCADA segments of SYS-08; the SYS-04 accounts that carry FSPA workloads (OT data account, the field data capture app, volume integration service, and shipper portal in the business workloads account, and the backup account); the company's configuration of SYS-03 and SYS-05; the 240 rugged tablets of SYS-09; and the OT monitoring sensors of SYS-13.

**Data flow in one line:** field devices and flow computers (SYS-02) report to the SCADA servers (SYS-01); the historian pushes data through the OT DMZ to the historian replica and measurement data service in the OT data account (SYS-04); lease operators enter tank gauges and run tickets on tablets in the field data capture app; the volume integration service sends daily allocated volumes to production accounting (SYS-03); the shipper portal publishes daily volume statements to the 5 shippers.

## 4. Where the evidence is

This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Every item has a source system, an owner, and as-of and collected dates.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps against the NIST CSF 2.0 and SP 800-82 Rev. 3 benchmark, the Part 195 gathering line duties, and Fla. Stat. 501.171** are judged in the gap analysis (P03), and **whether controls work** is tested in the control assessment (P07), including the packager gateway finding made during P07 testing (EV-SC-7). Both cite evidence IDs.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 benchmark | **NIST CSF 2.0 with NIST SP 800-82 Rev. 3 (voluntary benchmark)** as the primary structure, because no binding federal sector cyber rule applies (decided in the intake obligations register, N21-R01 to N21-R03): USCG rule N21-R01 does not apply (onshore only; no facility required to have a security plan under 33 CFR parts 104 to 106); TSA Security Directive N21-R02 does not apply (no TSA notification); CIRCIA N21-R03 is proposed only, and as proposed the company would be outside it (SBA-small and no sector criterion met). **Binding rules analyzed in the same workbook:** 49 CFR Part 195 for the gathering system (regulated rural gathering line requirements in 195.11 and the Subpart B reporting duties), and Fla. Stat. 501.171 as the state law worked example |
| Regulatory driver labels | `N21-BM (...)` means the P03 voluntary benchmark, with the SP 800-82 Rev. 3 section (or, for business IT items, the CSF 2.0 subcategory) in parentheses. `N21-P195 (...)` means the binding Part 195 gathering line rules, with the section in parentheses. Both are scenario labels, not rows in `requirements.csv`. `N21-R03 (proposed)` marks CIRCIA items tracked but not required. `Fla. Stat. 501.171(x)` marks the state data security and breach duties |
| P05 scope | All business units: 3 operating areas, the gathering system, the OCC and BCC, production accounting and revenue, finance, engineering, and corporate support |
| P08 incidents | **Two incident types:** (1) ransomware that starts in business IT and spreads toward field SCADA (registry default, `ir-runbook.md`); (2) unauthorized remote command of field equipment through a third-party remote access path, with a possible release from the gathering system (`ir-runbook-ot-remote-access.md`). Both integrate the crisis management team, General Counsel, and the pipeline emergency procedures |
| P09 SOC 2 | Readiness for a **SOC 2 Type 2** examination of the company's **crude gathering and measurement services**, requested by the largest shipper (Security, Availability, Processing Integrity, Confidentiality), plus the vendor SOC 2 review program. Joint interest billing and revenue distribution affect partners' financial reporting, so a SOC 1 is noted as a later option, not in scope |
| P10 AI | AI use-case portfolio: AI-001 predictive maintenance model for well equipment (registry default, fits this size), AI-002 enterprise generative AI assistant, AI-003 gathering line leak analytics (vendor add-on, advisory to controllers), AI-004 HR candidate-screening feature (licensed, switched off pending review), AI-005 ERP invoice coding |
| Cloud | Multi-account landing zone, vendor-agnostic. Services are described by category, with AWS, Azure, and Google Cloud equivalents only in a reference table |
| Registry defaults | Kept: the primary system, the ransomware incident, and the predictive maintenance use case all fit a producer of this size. The second incident type and the AI portfolio were added because the tier calls for two incident types and a portfolio |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-06-15 to 2026-07-02 | Intake: evidence requests, exports, document reviews, inventories, obligations register |
| 2026-07-06 to 2026-07-31 | BIA, risk assessment, and gap analysis fieldwork (site walkthroughs: Panhandle and OCC 2026-07-14 and 2026-07-15; South Florida 2026-07-16; Alabama and BCC 2026-07-17) |
| 2026-07-27 to 2026-07-31 | 2026 policies (POL-01 to POL-05), standards drafts, and the P08 runbooks drafted from the gap analysis |
| 2026-08-03 to 2026-08-21 | Control assessment by the co-sourced internal audit firm (field testing 2026-08-11 to 2026-08-13): operating tests of controls already in place; design review of the draft policies, procedures, and runbooks |
| 2026-08-24 to 2026-09-10 | AI governance assessment (P10) |
| 2026-09-16 | Deliverables approved: COO (Moderate and below, system owner), CEO (High risks, appetite, budget), with field-operations items agreed by the VP Operations; results presented to the audit committee the same day |
| 2026-10-01 | 2026 policies take effect |
| 2027-04 (planned) | Follow-up assessment: operating effectiveness of the controls the new policies and standards introduced, after at least one quarter of operation |
