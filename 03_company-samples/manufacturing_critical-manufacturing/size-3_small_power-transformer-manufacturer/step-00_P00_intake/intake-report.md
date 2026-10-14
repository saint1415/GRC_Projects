# Intake Report: Cris Santos Company | Critical Manufacturing | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (power and distribution transformer manufacturer, one Florida campus) |
| Intake window | 2026-06-29 to 2026-07-10 |
| Collected by | IT Manager, with the Controls Engineer (plant records) and the Contracts and Compliance Manager (contracts) |
| Approved | VP Operations, 2026-09-04 |

## 1. Purpose and scope
Intake collected the company's own records before any assessment work began on 2026-07-13. It covers the organization, the office and plant systems, the suppliers that touch them, the customer and federal contract terms, and the rules that may bind the company. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, the plant walkthrough, configuration reviews, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets the CSF 2.0 benchmark, a FAR clause or a utility addendum is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Users and access | EV-001 to EV-007 | Identity provider; HR and payroll system; IT ticketing; HR files; ERP and MES administration | 2023-02-01 to 2026-07-06 |
| Endpoints, servers and network | EV-008 to EV-017 | Device management and EDR consoles; MSP patch, scan and network records; MSP agreement; MES server; IT ticketing | 2026-06-26 to 2026-07-06 |
| Cloud and backups | EV-018 to EV-021 | Cloud provider console; cloud backup service; backup appliance; the Controls Engineer's laptop | 2026-06-30 to 2026-07-07 |
| Documents and records | EV-022 to EV-030 | IT shared drive; document request list; HR files; learning records; Controller's files; maintenance records | 2021-03-01 to 2026-07-06 |
| Customers, contracts and suppliers | EV-031 to EV-044 | Contract management system; ERP purchasing and finance; QMS document control; field service records; purchasing files; web filter; vendor portals; productivity suite | 2026-03-31 to 2026-07-07 |
| Facilities | EV-045, EV-046 | Badge access and CCTV systems; visitor log | 2026-07-01 to 2026-07-09 |
| Business volume, products and customers | EV-047 to EV-053 | ERP finance and APS; export files; website; sales and customer service files | 2025-12-31 to 2026-07-06 |

## 3. Observations by area
**Users and access.** Office, engineering, maintenance and field service staff have named identity provider accounts, each with MFA registered. The 3 IT administrators use hardware security keys, and no MES or plant accounts are in the directory (EV-001). MFA is required for email, the ERP, the cloud console and the IT VPN. MES kiosks and plant systems are not in the application list (EV-002). HR lists 200 employees and 24 terminations from January to June 2026, 3 of them field technicians (EV-003). Office accounts are disabled on the last working day. On production tickets the MES account is disabled 0 to 7 days after the last day, and the ticket template has no step for Field Service or utility notices (EV-004, EV-005). The ERP has about 118 named users, with roles by module and a super-user role (EV-006). About 160 production staff sign in to the MES with badge number and PIN. Each shift has one shared supervisor override account, and kiosk PIN sign-ins have no lockout (EV-007).

**Endpoints, servers and network.** Device management lists 140 laptops and desktops and the IT servers. The MES server is listed without software versions, and the kiosks and plant equipment are not listed (EV-008). EDR runs on all 140 endpoints, the IT servers and the cloud VMs, and its alerts go to the IT Manager's mailbox only (EV-009). Laptops are encrypted; the PLM vault, file server and MES server volumes are not (EV-010). The MSP patches IT servers and endpoints monthly; the MES server, kiosks and plant workstations are outside its patch scope (EV-011). The ERP application is two releases behind the vendor's current release (EV-012). The MSP scans the company's internet-facing addresses once a quarter (EV-013, EV-014). The 2019 network drawing does not show the plant network. The edge firewall has no inbound rules, and the campus has one internet carrier (EV-015). The MES server has one interface on the office subnet and one on the plant subnet, backs up its database to its own disk, and has no malicious code protection agent (EV-016). Change tickets exist for ERP releases and firewall rules, and none for MES, PLC or HMI changes (EV-017).

**Cloud and backups.** The ERP, APS, integration service and the AI-001 forecasting job run in one region of the cloud tenant. Three administrator roles are federated from the identity provider, and their permissions include deleting backups. Management events are kept for the default 90 days (EV-018). Daily ERP database backups with 7-day point-in-time restore completed from April to June 2026. They sit in the same account and region as production, immutability is off, and no restore job ran (EV-019). The PLM vault and file server are backed up nightly to an on-premises appliance with a weekly cloud copy. The MES server and test bay PCs are not in the job list (EV-020). Plant programs and winding recipes are copied by hand to the Controls Engineer's laptop; the latest folder is dated 2026-02 (EV-021).

**Documents and records.** The only policy document is a 2021 IT handbook with no plant content (EV-022). The incident procedure is a 2-page IT call list from 2023 (EV-023). The request for a risk assessment, an OT asset inventory, an incident response plan, a contingency plan, recovery and manual production procedures, restore and exercise records, access and log review records, a register of customer security terms, supplier security requirements, and an AI policy returned none (EV-024). The IT Manager's job description includes part-time security duties; the Controls Engineer's has none (EV-025). About 70 office staff completed the annual security module in 2025. No module is assigned to production workers or field technicians, and there are no phishing exercise records (EV-026). The handbook has a monitoring notice reviewed by counsel and no security section (EV-027). The cyber insurance policy has a breach coach and a forensic panel, and no retainer is on file (EV-028). Retired drives go to a recycler without certificates of destruction (EV-029). Standby generators for both server rooms and the test bay controls were load-tested monthly through June 2026 (EV-030).

**Customers, contracts and suppliers.** 12 of the 38 utility supply agreements carry a Supplier Cyber Security Addendum, and no list of their duties, owners or contacts exists (EV-031). The federal contract, awarded 2025-11, includes FAR 52.204-21, 52.204-23 and 52.204-25 and no DFARS clauses (EV-032). The heavy-haul carrier's purchase order attaches the agency's delivery schedule and site drawings (EV-033). Purchase terms and OEM agreements carry no security requirements. Three OEM agreements provide remote support through OEM cellular routers, on the drying oven, core cutting line 1 and welding cell 2 (EV-034). The quality system is ISO 9001 certified, and Quality signs every certified test report (EV-035). TMU firmware is loaded at final test with no hash or signature check step (EV-036). An access notice to a utility is on file for 1 of the 3 field technicians who left in 2026, sent 9 days after the last day (EV-037). Accounts payable shows the cloud, SaaS, MSP, OEM and supplier payments, including a predictive maintenance SaaS vendor from 2026-04 (EV-038). AI-002 was accepted on click-through terms, and its connector sends historian data out over the internet. AI-001 has been in production since 2025-11. Neither has a risk review record (EV-039). Engineering laptops reach public generative AI sites (EV-040). The MSP's SOC 2 Type 2 report covers Security for the 12 months ending 2026-03-31 (EV-041). The cloud provider's SOC 2 report was not downloaded (EV-042). The EDI provider contract has confidentiality and availability terms (EV-043). The productivity suite allows external sharing to any address and has no sensitivity labels (EV-044).

**Facilities.** Badge access covers the offices, the plant and both server rooms, and badge logs are kept 1 year. 46 CCTV cameras are listed by location (EV-045). Visitors sign in and are escorted (EV-046).

**Business volume, products and customers.** FY2025 revenue was $84 million across 250 production days. About 4% came from exports, and customers pay by bank transfer or check (EV-047). The backlog is about 38 weeks, with storm-restoration slots reserved in the APS (EV-048). Products are classified EAR99. Every export order has a screening result, and export records are kept 7 years (EV-049). The company makes transformers, monitoring units and field service, and no vehicle systems (EV-050). Sales posts website content (EV-051). The customer delay notice has no cyber incident wording (EV-052). One addendum utility asked in 2026 whether the company has a SOC 2 report (EV-053).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| OT asset inventory (PLC models, firmware versions, HMI operating systems) | Controls Engineer | 2026-07-06 | None exists; recorded during the plant walkthrough on 2026-07-16 (EV-065) |
| IT/OT firewall rules and OEM router configurations | Controls Engineer | 2026-07-06 | Exported during the plant walkthrough on 2026-07-16 (EV-066, EV-067) |
| Cloud provider SOC 2 report | IT Manager | 2026-07-06 | Not downloaded at intake; P04 lists it as to be obtained |
| Number of staff using public generative AI tools, and what they paste | VP Engineering | 2026-07-08 | Not established at intake; P10 treats the number as unknown |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Processes and owners (EV-003), revenue per production day (EV-047), backlog and storm slots (EV-048), backup schedules (EV-019, EV-020), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-001, EV-002, EV-006 to EV-009, EV-015, EV-016, EV-018 and EV-019 |
| P04 Cloud mapping | Cloud and SaaS components (EV-018, EV-038, EV-044) and provider documentation (EV-041 to EV-043) |
| P01 Risk register | Likelihood inputs from the configuration exports, the contract and supplier records, and the training and backup records |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the CSF 2.0 benchmark, the FAR clauses and the utility addenda |
| P06 Policies | The 2021 IT handbook (EV-022) and the IT call list (EV-023) |
| P07 Control assessment | Populations to sample from (EV-001, EV-003, EV-004, EV-007, EV-008) |
| P08 IR runbook | Notification duties from the obligations register and the addenda (EV-031); contacts from the vendor register |
| P09 SOC 2 | Vendor assurance on file (EV-041) and the utility questionnaires (EV-053) |
| P10 AI governance | AI tools found (EV-018, EV-038, EV-039, EV-040) |
