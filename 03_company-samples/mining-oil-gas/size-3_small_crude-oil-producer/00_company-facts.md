# Scenario facts: Cris Santos Company | Mining, Quarrying, and Oil and Gas Extraction | Small

All 11 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a regulation or standard, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (independent crude oil producer and operator) |
| Business | Independent crude oil producer (NAICS 211120 Crude Petroleum Extraction). Operates mature, high-water-cut onshore oil fields under waterflood, with field SCADA at every well pad and facility |
| Location | Florida, onshore only. **Headquarters** (administration, accounting, engineering) in northwest Florida. **Panhandle operating area** with the Panhandle field office and the Operations Control Center (OCC), about 30 miles from headquarters. **South Florida operating area** with the South Florida field office. No offshore, Outer Continental Shelf, or waterfront facilities |
| Workforce | 250 employees (see section 2 for the breakdown; HR roster EV-003). Headcount is high for the production volume because the company runs its own well servicing rigs, roustabout crews, water hauling, and injection plant |
| Assets operated | 118 wells: 74 producing oil wells (52 rod pump, 22 electric submersible pump), 28 water injection wells, 6 saltwater disposal wells, 10 shut-in wells. 5 central tank batteries with truck loading (3 Panhandle, 2 South Florida), 1 water injection plant (Panhandle), 2 associated-gas compression stations (Panhandle) |
| Production | About 1,600 barrels of oil per day gross operated, plus associated gas and about 55,000 barrels of produced water per day that is reinjected or disposed of |
| Revenue | About $42 million a year (fictional); oil sales of about $104,000 per day |
| Size status | SBA-small. NAICS 211120 uses an employee-based standard of 1,250 employees (13 CFR 121.201); 250 employees is below it |
| How product leaves the lease | Crude is sold at the lease tank batteries and hauled away by the purchaser's tank trucks. Associated gas is sold at a lease sales meter into a third-party gathering system. The company owns only production facilities and flow lines, which PHMSA excludes from 49 CFR Part 195 (195.1(b)(8) and (b)(9)(i)) |
| Owners and partners | Majority owner (Cris Santos) and 2 minority members. The company is operator for 9 non-operating working interest owners (joint interest billing) and pays about 2,300 royalty owners monthly |
| Sensitive data | Seismic and reservoir data (trade secret); well control and process safety data (H2S monitoring, shutdown logic); royalty owner records (names, Social Security or taxpayer numbers, bank account numbers for direct deposit); employee records (Social Security numbers, commercial driver license numbers, health plan IDs); vehicle telematics locations of field employees |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): offshore/OCS and MTSA facilities (none). TSA-designated pipelines (none). EAR-controlled technology (none identified; the company buys commercial well equipment). SSI under 49 CFR Part 1520 (the company holds none). Federal contracts (none). Payment cards (not accepted). SEC reporting (private company) |
| State law approach | Florida law is cited only where a Florida duty is unavoidable: the Florida Information Protection Act, Fla. Stat. 501.171 (data security, breach notice, disposal). State oil and gas program requirements (permits, production reports) are operational, not cybersecurity rules, and are not analyzed |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Majority owner (President) | Accepts High and Very High risks; approves the security budget |
| Chief Financial Officer (CFO) | Executive sponsor of the security program; accepts Moderate risks; owns production accounting, revenue distribution, and cyber insurance |
| Vice President of Operations (VP Operations) | Business owner of field operations and the SCADA system; must agree to any risk acceptance that affects field operations or safety |
| IT Manager | Part-time Information Security Lead (designated in writing 2026-08-31); runs IT with 2 Systems Administrators, a Network Administrator, and a Help Desk Technician |
| SCADA and Automation Supervisor | OT security lead in practice; manages 4 automation (instrument and electrical) technicians and the SCADA integrator |
| Production Controllers (6) | Staff the 24x7 Operations Control Center at the Panhandle field office; monitor alarms and remotely start and stop wells |
| Field Superintendents (2) | Panhandle and South Florida; manual operations and shut-in procedures; field site access |
| Production Accounting Manager | Production volumes, run tickets, allocations, royalty and revenue distribution, joint interest billing |
| HSE and Regulatory Manager | H2S safety, spill reporting, state oil and gas reporting; emergency response plan |
| Production Engineering Manager | Owner of the predictive maintenance model (P10) and artificial lift performance |
| Reservoir Engineering Manager | Owner of seismic and reservoir data (trade secret) |
| HR Manager | Onboarding, terminations, background checks, training records |
| SCADA integrator (contractor) | Configures SCADA servers, HMIs, and field controllers; has remote access (EV-014) |
| External auditors | Financial statement audit; security assessments are contracted as needed (the P07 assessor) |

Headcount (250): executives and managers 8; field operations (superintendents, foremen, lease operators) 72; Production Controllers 6; well servicing crews 30; roustabout crews 28; water handling and injection plant 14; water and fluid haul drivers 22; mechanics and compressor technicians 16; SCADA and automation 5; engineering and geoscience 10; HSE and regulatory 6; production accounting 9; finance and joint interest billing 6; land 3; HR 3; IT 5; supply chain and warehouse 7.

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv).

| ID | System | Hosting | Sensitive data? | Notes |
|---|---|---|---|---|
| SYS-01 | SCADA control center: SCADA master servers (primary and standby), historian, 6 HMI workstations (4 at the OCC, 2 at the South Florida field office), 2 engineering workstations | On-premises, OCC server room (Panhandle field office) | Yes (process data, well control and safety data) | The integrator states that the SCADA servers and HMIs run an operating system version past end of vendor support (EV-013). Primary and standby servers sit in the same room (EV-011) |
| SYS-02 | Field control devices and communications: 96 RTUs and PLCs (well pads, tank batteries, injection plant, compressor stations), 22 ESP variable speed drives, 40 electronic flow meters, licensed 900 MHz radio network (Panhandle), 46 cellular modems (34 South Florida, 12 remote Panhandle sites) | Field sites | Yes (control logic) | Safety shutdowns (H2S detection, tank high-level, compressor emergency shutdown) are hardwired and do not depend on SCADA (EV-011) |
| SYS-03 | Production accounting and revenue distribution | Vendor SaaS (SOC 2 Type 2) | Yes (royalty owner PI, volumes, revenue) | Run tickets, allocations, state production reports, royalty payments, joint interest billing |
| SYS-04 | Cloud tenant (IaaS/PaaS) | Public cloud provider (vendor-agnostic) | Yes | Hosts: historian replica, volume integration service, field data capture app for tablets (web app and managed database), data platform (reservoir and seismic data, historian exports), machine learning workspace (P10), backup vault |
| SYS-05 | Identity provider (single sign-on and MFA) | SaaS | No (identities only) | Protects SYS-03, SYS-04, SYS-06, SYS-07, SYS-09. Not integrated with SCADA (SCADA uses local accounts; EV-006) |
| SYS-06 | ERP (general ledger, payables, purchasing, maintenance work orders) | Vendor SaaS | Yes (vendor banking) | Work order history feeds the P10 model |
| SYS-07 | Productivity suite (email, files, chat) | SaaS | Yes (incidental) | The shared file area also holds reservoir interpretation files (EV-025) |
| SYS-08 | Corporate network | On-premises | Yes (in transit) | Firewalls at headquarters and both field offices; site-to-site VPN to SYS-04; one firewall between the corporate network and the SCADA network at the OCC (EV-019) |
| SYS-09 | Corporate endpoints | On-premises and mobile | Yes (cached) | 170 laptops and desktops, 70 rugged tablets (lease operators), 45 managed smartphones. EDR on laptops and desktops (EV-016) |
| SYS-10 | HR and payroll | Vendor SaaS | Yes (employee PI) | |
| SYS-11 | Fleet telematics | Vendor SaaS | Yes (employee geolocation) | GPS units in 110 field vehicles and trucks |
| SYS-12 | SCADA integrator remote access | Third-party remote access tool installed on the SCADA primary server | Access path | Runs as an automatically starting service with one shared, password-only vendor account (EV-014) |

**SSP system (P02):** the *Field SCADA and Production Accounting System (FSPA)*: SYS-01, SYS-02, the SCADA network segment and IT/OT firewall of SYS-08, the SYS-04 workloads that carry production data (historian replica, volume integration service, field data capture app, backup vault), the company's configuration of SYS-03 and SYS-05, the 70 rugged tablets of SYS-09, and the remote access path SYS-12.

**Data flow in one line:** field devices (SYS-02) report to the SCADA servers (SYS-01); the historian pushes hourly data over the VPN to the historian replica in the cloud tenant (SYS-04); lease operators enter tank gauges and run tickets on tablets in the field data capture app (SYS-04); the volume integration service sends daily allocated volumes to production accounting (SYS-03).

## 4. Where the evidence is

This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Every item has a source system, an owner, and as-of and collected dates.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps against the voluntary benchmark** (NIST CSF 2.0 with SP 800-82 Rev. 3) and the Florida statute are judged in the gap analysis (P03), and **whether controls work** is tested in the control assessment (P07), including the field site tests. Both cite evidence IDs.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 benchmark | **NIST CSF 2.0 with NIST SP 800-82 Rev. 3 (voluntary benchmark).** No binding federal sector cyber rule applies: USCG Marine Transportation System rule N21-R01 does not apply (onshore only, no facility or OCS facility required to have a security plan, 33 CFR 101.605); TSA Security Directive N21-R02 does not apply (not a TSA-notified pipeline owner or operator); CIRCIA N21-R03 is proposed only, and as proposed the company would be outside it (SBA-small and no sector criterion met). Secondary binding rule: Fla. Stat. 501.171 |
| Regulatory driver labels | `N21-BM (...)` means the P03 voluntary benchmark (NIST CSF 2.0 with SP 800-82 Rev. 3), with the specific SP 800-82 Rev. 3 section (or, for business IT items, the CSF 2.0 subcategory) in parentheses. It is a scenario label, not a row in `requirements.csv`. `N21-R03 (proposed)` marks items tracked for CIRCIA but not currently required. `Fla. Stat. 501.171(x)` marks the binding state data security and breach duties |
| P08 incident | Ransomware that starts in business IT (credential phishing to the corporate network) and spreads toward the field SCADA network through the IT/OT firewall and the dual-homed engineering workstation |
| P09 SOC 2 | The company is not a service organization for its customers (it sells crude oil). P09 is (a) a Security-only self-benchmark against the Trust Services Criteria, used to answer the reserve-based lender's and non-operating partners' security questions, and (b) a review of the production accounting vendor's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| P10 AI | Predictive maintenance model for well equipment (rod pumps and ESPs), built on the cloud machine learning workspace with a contracted data science firm, in pilot since May 2026. Second inventory entry: staff use of general-purpose generative AI |
| Cloud | Vendor-agnostic. Services are described by category, with AWS, Azure, and Google Cloud equivalents noted only where needed for shared responsibility |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-06-29 to 2026-07-10 | Intake: evidence requests, SCADA and system exports, inventories, obligations register |
| 2026-07-13 to 2026-07-24 | BIA interviews, risk assessment and gap analysis fieldwork (OCC and field site walkthroughs 2026-07-15 and 2026-07-16) |
| 2026-07-27 to 2026-07-31 | Policies drafted from the gaps |
| 2026-08-03 to 2026-08-07 | Control assessment fieldwork (field site testing 2026-08-05): operating tests of controls already in place; design review of the draft policies |
| 2026-08-31 | Deliverables and policies approved by the CFO, with High risks accepted by the majority owner and field-operations items agreed by the VP Operations |
| 2027-02 (planned) | Follow-up assessment: operating effectiveness of the controls the new policies introduced, after at least one quarter of operation |
