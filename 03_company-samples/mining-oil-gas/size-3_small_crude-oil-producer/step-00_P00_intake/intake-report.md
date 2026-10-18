# Intake Report: Cris Santos Company | Mining, Quarrying, and Oil and Gas Extraction | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent crude oil producer and operator, two Florida operating areas) |
| Intake window | 2026-06-29 to 2026-07-10 |
| Collected by | IT Manager, with the SCADA and Automation Supervisor |
| Approved | CFO, 2026-08-31 |

## 1. Purpose and scope
Intake collected the company's own records before any assessment work began on 2026-07-13. It covers the organization, the field SCADA system and the business systems that connect to it, the suppliers that touch them, and the rules that may bind the company. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, walk-throughs, scans, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets the benchmark is decided in the gap analysis (P03) and the control assessment (P07). No active scan touched the SCADA network during intake; OT records came from SCADA configuration exports, integrator documents and the SCADA and Automation Supervisor.

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Users and access | EV-001 to EV-005 | Identity provider; HR and payroll system; IT help desk; HR files | 2024-09-01 to 2026-07-01 |
| SCADA and field devices | EV-006 to EV-015 | SCADA server configuration, event log and backup software; integrator documents; antivirus logs | 2021-09-30 to 2026-07-07 |
| Corporate devices and network | EV-016 to EV-019 | Endpoint management and EDR consoles; vulnerability scanner; network documentation and firewall management | 2026-06-26 to 2026-07-01 |
| Cloud and applications | EV-020 to EV-025 | Cloud provider console and backup service; app configuration; SaaS admin consoles; productivity suite | 2026-06-30 to 2026-07-02 |
| Documents and records | EV-026 to EV-034 | Document request; HSE files; help desk and IT procedures; learning records; HR files; CFO's files | 2025-01-01 to 2026-07-06 |
| Facilities and field sites | EV-035 to EV-037 | Badge and camera systems; route logs and HSE checklists; carrier portal | 2026-06-30 to 2026-07-01 |
| Suppliers and contracts | EV-038 to EV-046 | Telematics portal; ERP payables, purchasing and work orders; contract files; vendor portals; insurance and questionnaires | 2026-03-01 to 2026-07-06 |
| Operations and business volume | EV-047 to EV-050 | Production accounting; ERP; regulatory files | 2025-12-31 to 2026-07-06 |
| AI tools | EV-051, EV-052 | Staff survey and identity provider app list; statements of work | 2026-04-20 to 2026-07-07 |

## 3. Observations by area
**Users and access.** 250 active named workforce accounts, each with MFA registered; the 4 IT administrator accounts have hardware keys (EV-001). MFA is required for email, the ERP, production accounting, the cloud console, the corporate VPN and the field data capture app. Identity provider sign-in logs are kept 30 days (EV-002). HR recorded 21 terminations from January to June 2026 (EV-003). Each has a disable ticket; tickets for departing field staff closed up to 7 days after the last working day, and contractor accounts are disabled when a manager emails the help desk (EV-004). The HR checklist has no step for SCADA accounts (EV-005).

**SCADA and field devices.** SCADA uses local accounts, including one shared operator account on the OCC HMIs and one shared integrator account (EV-006). One engineering workstation has addresses on both the corporate and SCADA networks, USB storage is not restricted on HMIs, and no screen lock is set on the HMIs (EV-007). The SCADA master polls 96 RTUs and PLCs, 22 ESP drives and 40 flow meters, with no model or firmware fields (EV-008). SCADA logs stay on the servers and overwrite at a fixed size (EV-009). SCADA servers are backed up nightly to a storage device in the same server room and domain; no controller programs are in the jobs and no restores are logged (EV-010). Safety shutdowns are hardwired and work without SCADA, and the radio protocol has no message authentication (EV-011). The integrator states that the SCADA operating system is past vendor support (EV-013). The integrator's remote access tool runs as an automatic service with one password-only vendor account and no session recording (EV-014). HMI antivirus signatures are loaded by hand about monthly (EV-015).

**Corporate devices and network.** The consoles list 170 laptops and desktops, 70 rugged tablets and 45 smartphones. EDR runs on the laptops, desktops and the historian replica VM, and its alerts go to the IT team mailbox with no after-hours routing (EV-016). Corporate OS patches deploy monthly (EV-017). Quarterly authenticated scans cover the corporate network and cloud workloads, not the SCADA network (EV-018). The only network drawing dates from 2019 and covers the corporate network. The IT/OT firewall allows traffic from corporate server subnets to the SCADA network, including remote desktop to HMIs, no DMZ zone is defined, and firewall logs are kept 7 days (EV-019).

**Cloud and applications.** The cloud tenant holds 7 workloads. Its 3 administrator roles also administer the backup vault, and the VPN rules allow return traffic to the SCADA network (EV-020). Data platform storage is readable by a broad staff group, and data-access logging is off (EV-021). Daily cloud snapshots completed from April to June 2026. The vault is in the production account and region, immutability is off, and no restores were run (EV-022). Run tickets can be edited after submission, and the app keeps no change history (EV-023). The shared file area is open to all staff and holds reservoir interpretation files and royalty owner exports. Owner exports go to the outside tax preparer as email attachments (EV-025).

**Documents and records.** The document request returned no incident response plan for cyber events or OT, no SCADA restore procedure, no restore test or tabletop records, no OT change procedure, no OT asset inventory, no access review records, no supplier security procedure, no approved AI tools list and no AI risk review (EV-026). The emergency response plan covers spills, fires, H2S releases and hurricanes, including manual operations and shut-ins, and has no cyber section (EV-027). Corporate changes go through help desk tickets; there are no records of SCADA or controller changes (EV-028). Office staff take awareness training at hire and every year; about 190 field staff have no security module, and there are no phishing exercise records (EV-029).

**Facilities and field sites.** Badge readers control the OCC and its server room, with a visitor log and cameras (EV-035). Lease operator routes visit producing sites, and monthly HSE checklists record fence, gate lock and cabinet padlock condition (EV-036). One carrier serves all 46 modems (EV-037).

**Suppliers and contracts.** Payments go to 15 suppliers, including the SCADA integrator, the data science firm (from May 2026) and the outside tax preparer (EV-039). None of the 5 supplier contracts reviewed sets security requirements, MFA for remote access or a breach notice deadline (EV-040). Spare controllers have been bought from secondary-market sellers (EV-041). The production accounting vendor's SOC 2 Type 2 report covers the 12 months ending 2026-03-31 (EV-043). The cyber policy requires MFA on remote access (EV-045). The lender and two partners sent security questionnaires in 2026 (EV-046).

**Operations and business volume.** 118 wells, 5 tank batteries, an injection plant and 2 compression stations, all onshore; about 1,600 barrels of oil and 55,000 barrels of produced water per day (EV-047). Revenue was about $42 million in FY2025, with oil sales of about $104,000 per day (EV-048). About 2,300 royalty owners and 9 partners (EV-049). There is no Coast Guard, TSA or PHMSA registration or correspondence (EV-050).

**AI tools.** Staff report using public chatbots, and no approved tools list exists. The predictive maintenance pilot has run on 60 wells since May 2026 (EV-051). Its statement of work has no security, data use or deletion terms (EV-052).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Number of staff using public chatbots, and what they paste | CFO | 2026-07-08 | Not established at intake; P10 treats it as unknown |
| Controller models and firmware versions | SCADA integrator | 2026-07-07 | Drawings provided without model or firmware detail (EV-011); carried into P01 (R-012) and POAM-006 |
| Integrator's own security assurance (SOC 2 or questionnaire) | SCADA integrator | 2026-07-07 | Not provided; carried into P01 (R-002, R-019) |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Production and water volumes (EV-047), revenue (EV-048), owners and partners (EV-049), SCADA and cloud backups (EV-010, EV-022), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-001, EV-002, EV-006 to EV-011, EV-014, EV-016, EV-019 and EV-020 to EV-023 |
| P04 Cloud mapping | Cloud components and settings (EV-020 to EV-023) and provider assurance (EV-043, EV-044) |
| P01 Risk register | Likelihood inputs from configuration exports, backup logs, the document request (EV-026), contracts (EV-040) and the insurance policy (EV-045) |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the benchmark |
| P06 Policies | The document request (EV-026), the emergency response plan (EV-027) and the handbook (EV-030) |
| P07 Control assessment | Populations to sample from (EV-003, EV-004 terminations; EV-037 modems; EV-008 field sites) |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register; the insurance policy (EV-045) |
| P09 SOC 2 | Vendor assurance on file (EV-043, EV-044) and the questionnaires (EV-046) |
| P10 AI governance | AI tools found (EV-051, EV-052) |
