# Scenario facts: Cris Santos Company | Energy | Micro

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or standard, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (small intrastate natural gas transmission pipeline operator) |
| Business | Owns and operates one short intrastate natural gas transmission line in Florida (NAICS 486210). Receives gas at one tap on an interstate pipeline and delivers it to a municipal gas system and two industrial plants. Transportation only: the company does not own the gas |
| Location | Florida. One **office and operations building** (with the gas control desk, a small warehouse, and a fenced pipe yard) and **7 unstaffed field sites** along the route |
| Pipeline assets | About 26 miles of steel transmission line (8-inch mainline and a 6-inch lateral). **No compressor station**: the line runs on the pressure delivered by the upstream interstate pipeline. 1 receipt meter station at the interstate tap (company-owned meter run, flow control valve, flow computer); 3 delivery meter and regulator (M&R) stations; 3 remote-control mainline valve (RCV) sites. Delivery pressure is held by mechanical regulators and overpressure protection at each M&R station, which work without SCADA. Mostly Class 1 and 2 locations, with a Class 3 segment near the municipal gate station |
| Customers | A municipal gas system that serves about 9,000 homes and businesses, a ceramic tile plant, and a food processing plant. Service is under firm transportation contracts |
| Workforce | 7 employees: Owner (General Manager), Operations Manager, 2 Pipeline Technicians, Corrosion and Measurement Technician, Office Manager, Gas Scheduler and Administrative Assistant |
| Controllers | The Operations Manager and the 2 Pipeline Technicians are the company's qualified controllers. In business hours the Operations Manager monitors and controls the pipeline from the gas control desk. After hours and on weekends one of the three is the **on-call controller** for a week at a time: SCADA alarms call out to their phone, and they work from a company laptop through the hosted SCADA web client, which can open and close the RCVs and the receipt flow control valve |
| Revenue | About $1.1 million a year in transportation revenue (fictional). Under the SBA standard of $41.5 million for NAICS 486210 (13 CFR 121.201), so SBA-small |
| Pipeline safety regulator | Intrastate pipeline. The Florida Public Service Commission (FPSC) inspects and enforces under its 49 U.S.C. 60105 certification with PHMSA. Rule 25-12.005, F.A.C., adopts 49 CFR Parts 191 and 192. The company has controllers who monitor and control the pipeline through SCADA, so 49 CFR 192.631 applies. Because the control room is limited to **transmission without a compressor station**, 192.631(a)(1)(ii) requires written procedures for **only paragraphs (d) fatigue, (i) compliance validation, and (j) compliance and deviations** |
| TSA status | **Not designated.** TSA has never notified the company that its pipeline is critical, so TSA Security Directives Pipeline-2021-01G and Pipeline-2021-02G do not apply (see P03). The Owner confirmed on 2026-07-22 that the company holds no TSA notification letter |
| Not in scope | NERC CIP (not a NERC-registered entity; no Bulk Electric System assets); DOE Form DOE-417 (electric only); CEII (the company files none with FERC); SSI under 49 CFR Part 1520 (none held; it would be if TSA designated the pipeline); SEC disclosure (privately held); payment cards (customers pay by bank transfer); FAR clauses (no federal contracts) |
| State law approach | Florida law is cited only where a Florida duty is unavoidable: breach notification for employee personal information (Fla. Stat. 501.171) and FPSC pipeline accident notice (Rule 25-12.084, F.A.C.) |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Owner (General Manager) | Accepts Moderate and higher risk; approves policies, spending, and any precautionary shutdown or shut-in of the line; incident decision maker |
| Operations Manager | Owns the operations and maintenance manual (49 CFR 192.605), the emergency plan (192.615), and the control room management procedures (192.631). **SCADA owner and administrator**: manages SCADA users, displays, alarm set-points, and field device configurations. Controller in business hours; on-call rotation |
| Pipeline Technicians (2) | Field operations and maintenance; qualified controllers on the on-call rotation |
| Corrosion and Measurement Technician | Cathodic protection, meter and flow computer checks; field backup for manual operation |
| Office Manager | **Security program coordinator** (designated in writing 2026-07-20): risk register, policies, MSP liaison, business IT accounts, vendor contracts, insurance; also billing, HR, and compliance records |
| Gas Scheduler and Administrative Assistant | Daily nominations with the upstream interstate pipeline; customer notices |
| Managed service provider (MSP) | Office IT: help desk, patching, antivirus, firewall, Wi-Fi, productivity suite administration, and backup of the suite. Its remote monitoring and management (RMM) agent is on every company computer |
| Hosted SCADA vendor | Runs the SCADA host, historian, alarm callout, and web client in its hosted environment; vendor support staff can reach the company's tenant and, through it, the field RTUs |

**Where roles overlap.** The Operations Manager both operates SCADA and administers its accounts and configuration. The Office Manager runs the security program but has no OT background. Compensation: the Owner reviews the SCADA user list and the vendor's audit log summary each month; the P07 assessment is done by an independent OT security consultant.

## 3. Systems

| ID | System | Hosting | Notes |
|---|---|---|---|
| SYS-01 | Hosted SCADA service: SCADA host, historian, alarm callout, displays, and web client (the company's tenant) | Vendor SaaS (hosted SCADA vendor) | Primary system. Vendor runs it in two data centers. One shared operator login is used at the gas control desk; no MFA on SCADA logins. Includes an optional **leak-detection anomaly module** switched on as a vendor trial in June 2026 (P10) |
| SYS-02 | Gas control desk: 2 workstations (primary and backup) in the office | On-premises, MSP-managed | Ordinary office desktops on the same flat network as business computers, with email and web browsing and the MSP's RMM agent |
| SYS-03 | Field control devices at 7 sites: 7 RTUs, 4 flow computers, 3 RCV actuators, receipt flow control valve | Field sites | Flow computers keep about 35 days of hourly measurement data locally. RTU programs are kept on the Operations Manager's laptop |
| SYS-04 | SCADA telemetry: 7 cellular gateways on a carrier private network, tunneled to the SCADA vendor | Field; one cellular carrier | No radio backup. A single carrier serves all sites |
| SYS-05 | Business endpoints: 6 laptops and 3 rugged field tablets | MSP-managed | 3 of the laptops (the controllers') are used for after-hours SCADA access |
| SYS-06 | Office network: small-business firewall, Wi-Fi, one fiber internet line | On-premises, MSP-managed | Flat network (no separate segment for the gas control desk). No internet failover |
| SYS-07 | Productivity suite: email, files, shared drive (O&M records, maps, operator qualification records) | SaaS | MFA enforced |
| SYS-08 | Accounting and billing SaaS; payroll through an outside payroll service | SaaS | MFA enforced on accounting; holds employee personal information |
| SYS-09 | SaaS backup of the productivity suite | SaaS, operated by the MSP | Nightly; 30 days of versions; never restore-tested |
| SYS-10 | MSP RMM tool | MSP SaaS | Agent on every company computer, including the gas control desk |
| SYS-11 | Upstream interstate pipeline's customer portal (nominations) | Third-party portal | Named logins for the Gas Scheduler and Operations Manager |

**SSP system (P02):** the *Pipeline SCADA and Gas Control System (PSGCS)*: the company's tenant on the hosted SCADA service (SYS-01), the gas control desk workstations (SYS-02), the field control devices at 7 sites (SYS-03), the cellular telemetry (SYS-04), and SCADA access from the 3 controller laptops (part of SYS-05); the office network, MSP tools, and business SaaS are interconnected but outside the boundary.

## 4. Current security posture: early to partial

**In place today:**
- Written O&M manual (192.605) and emergency plan (192.615), reviewed each year (last review March 2026), with liaison to the county emergency manager and the city fire department
- Written control room management procedures for the reduced scope (2011, revised 2019): hours-of-service limits and records
- Hosted SCADA vendor runs redundant hosts in two data centers and backs up the tenant
- Cellular gateways on a carrier private network (no public IP addresses by design)
- MFA on email, the productivity suite, and accounting
- MSP patching, antivirus, and firewall for office computers
- Nightly backup of the productivity suite (SYS-09)
- Fenced and locked field sites; RTU cabinets padlocked; office alarm
- Annual emergency drill with the city fire department (last held November 2025)

**Missing or weak, found in the 2026 assessments:**
1. No cybersecurity risk assessment has ever been done. There is no inventory of SCADA accounts, field device firmware, or where pipeline information is stored.
2. The gas control desk uses one shared SCADA operator login. SCADA logins have no MFA, including the on-call laptops that can open and close valves from anywhere on the internet.
3. The gas control desk workstations sit on the flat office network, are used for email and web browsing, and carry the MSP's RMM agent.
4. No cybersecurity incident response plan. The emergency plan does not cover cyber events or loss of trust in SCADA, and there are no criteria for choosing between isolating, manual operation, and shutting in the line.
5. The SCADA vendor contract has no security incident notice term, and its SOC 2 report has never been reviewed. The MSP contract has no recovery time commitment.
6. A Pipeline Technician who left on 2026-02-27 kept an active SCADA account until 2026-07-23. The vendor audit log showed no logins after departure.
7. SCADA configuration (displays, points, alarm set-points) has no copy held by the company, and RTU programs exist only on the Operations Manager's laptop.
8. No security awareness training; no phishing awareness.
9. No review of the SCADA audit log (logins and commands), although the vendor portal provides it.
10. The suite backup has never been restore-tested.
11. On-call alarm callouts at night are not counted toward hours-of-service, and fatigue education was last given in 2023 (192.631(d)).
12. One cellular carrier for all SCADA telemetry and one office internet line, with no failover.
13. The leak-detection anomaly module was switched on as a vendor trial in June 2026 and sends advisory alerts to on-call phones without validation, procedures, or approval (P10).
14. A gateway at the municipal gate station was reachable from the internet with its default administrator password (found during P07 testing; see P01 R-023).

## 5. Scenario choices

| Deliverable | Choice |
|---|---|
| P02 system | The registry default "Pipeline SCADA and gas control system" fits. At this size the SCADA host is a vendor-hosted service, so the plan treats the SCADA vendor as the main control provider and the MSP as the provider for the gas control desk |
| P03 regulation | TSA SD Pipeline-2021-02G recorded as **not applicable** (no TSA designation) and kept as a readiness reference. Analyzed instead: 49 CFR 192.631 with its reduced-procedure scope, the SCADA-related duties in 192.605 and 192.615, and NIST CSF 2.0 with SP 800-82 Rev. 3 as a voluntary cyber benchmark |
| P08 incident | The registry default fits: ransomware on the office network that reaches the gas control desk workstations and leads the Owner to consider a precautionary shut-in of the line; the MSP, the SCADA vendor, and the cyber insurer are in the notification chain |
| P09 SOC 2 | Security plus Availability self-assessment, used to answer the municipal gas system's supplier security and reliability questionnaire; plus a review of the hosted SCADA vendor's SOC 2 Type 2 report |
| P10 AI | The registry default fits: the hosted SCADA vendor's leak-detection anomaly module, in a trial since 2026-06-01 |
| Cloud | SaaS-first, vendor-agnostic. The hosted SCADA service is the critical SaaS; the one cloud workload is the MSP-operated SaaS backup of the productivity suite |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-07-20 to 2026-07-31 | Risk assessment and gap analysis with the MSP lead technician (TSA status confirmed 2026-07-22) |
| 2026-08-17 to 2026-08-19 | Control assessment by an independent OT security consultant (field sites visited 2026-08-18) |
| 2026-09-15 | Deliverables approved by the Owner |
