# Intake Report: Cris Santos Company | Food and Agriculture | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (meat processing plant with a smoked seafood room, one Florida plant) |
| Intake window | 2026-06-29 to 2026-07-10 |
| Collected by | IT Manager (security lead), with the FSQA Manager and the Controls Engineer |
| Approved | General Manager, 2026-09-04 |

## 1. Purpose and scope
Intake collected the company's own records before any assessment work began on 2026-07-13. It covers the organization, the IT and OT systems that run and record food production, the suppliers that touch them, and the rules that may bind the plant. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, the plant walkthrough, record samples, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Users and access | EV-001 to EV-007 | Identity provider; payroll service HR module; IT ticketing; SCADA and recipe-system user administration; records application; historian | 2026-06-30 to 2026-07-03 |
| Devices and network | EV-008 to EV-014 | Device management console; EDR console; scanning service; firewall management; Wi-Fi controller; integrator report and controls drawings | 2025-11-14 to 2026-07-03 |
| Cloud and backups | EV-015 to EV-017 | Cloud provider console; cloud backup service; OT backup software | 2026-06-30 to 2026-07-01 |
| Food safety and food defense records | EV-018 to EV-023 | FSQA document files and logs; HR and FSQA files | 2023-02-20 to 2026-06-30 |
| Documents and IT records | EV-024 to EV-030 | IT shared folder and document request; change records; training platform; General Manager's, HR and Controller's files; IT ticketing and managed detection portal | 2025-01-01 to 2026-07-06 |
| Suppliers, contracts and customers | EV-031 to EV-036 | ERP accounting module; contract files; vendor portals; cold-chain dashboard; customer files | 2026-03-31 to 2026-07-06 |
| Regulatory status and business volume | EV-037 to EV-039 | Regulatory files; PSM and RMP files; ERP accounting and inventory | 2025-12-31 to 2026-07-06 |
| Facilities | EV-040, EV-041 | Badge system, visitor log and CCTV; maintenance management system | 2026-06-30 to 2026-07-01 |
| Data, customers and AI tools | EV-042 to EV-045 | Productivity suite; e-commerce and terminal portals; ERP and WMS consoles; staff survey and identity provider app list | 2026-07-02 to 2026-07-07 |

## 3. Observations by area
**Users and access.** Business and cloud users have named identity provider accounts with MFA, and the 2 cloud administrators use hardware keys. No HMI, SCADA or recipe-system sign-in is connected to the identity provider (EV-001). MFA is required for email, ERP, WMS, the cloud console, the records application and the IT VPN (EV-002). HR lists 250 employees (242 FTE), and 10 of the terminations from January to June 2026 were production staff (EV-003). Office terminations have disable tickets closed on the last working day. Production terminations have no IT ticket, and termination notices do not reach the Controls Engineer (EV-004). HMIs, SCADA and the recipe system use shared accounts, and no approval step is configured for formulation or setpoint changes (EV-005). The records application has one shared administrator, entries are signed with typed initials, and no edit history is kept for signed entries (EV-006). The historian audit trail setting is off (EV-007).

**Devices and network.** Device management lists 85 office laptops and desktops and 40 shared production-floor terminals and tablets, with automatic patching on office endpoints and no control-system host enrolled (EV-008). EDR with managed detection runs on the 85 office endpoints and on no OT host (EV-009). Monthly vulnerability scans cover office endpoints and cloud workloads only (EV-010). The corporate-to-OT firewall allows engineering traffic between any corporate host and the control network, the MES server has addresses on both networks, and the integrator uses one shared, always-enabled VPN account without MFA. The plant has a single ISP. Firewall logs are kept 30 days and VPN logs 90 days (EV-011). The cold-chain sensor gateway is on the corporate Wi-Fi (EV-012). The integrator's 2025 service report lists about 30 PLCs and 12 HMIs, 2 of which run an operating system past its support end date (EV-013). The Line 2 meat brine system has a hardwired CIP interlock; the seafood brine tank drawing shows none (EV-014).

**Cloud and backups.** The cloud tenant holds 4 workloads with 2 administrators, and the backup vault is in the same account as production. Cloud activity logs are kept 90 days (EV-015). Daily cloud backups are kept 35 days, immutability is off, and no restore was run (EV-016). SCADA and MES back up nightly to a domain-joined storage device in the plant server room. No restore was run, no PLC program is in the jobs, and PLC program files are kept on the engineering laptop (EV-017).

**Food safety and food defense records.** The food defense plan is dated 2023-02-20, signed by the General Manager, and covers the seafood process. Its worksheets evaluate 14 steps for a person with physical access and do not list the dosing skid, CIP valve control or smokehouse setpoints. Its mitigation strategies are badge access, a locked cure and ingredient room, CCTV at docks, and visitor sign-in and escort. It has no verification section, the 2024 CCTV modification is unsigned, and no reanalysis followed (EV-018). Weekly lock and seal checks were recorded for 9 of the 12 weeks from April to June 2026, with no reviewer sign-off (EV-019). The FSQA Manager holds the FDA intentional adulteration training certificate (2022); seafood room temporary workers have no awareness entries in 2025 or 2026 (EV-020). No food defense duty is assigned for third-shift sanitation, and agency files hold sign-in sheets only (EV-021). HACCP plans cover four processing categories and the seafood room, with no step for loss of CCP data; the recall procedure does not mention cyber incidents; the 2026 mock recall used the cloud traceability database (EV-022). The retention schedule includes the food defense plan (EV-023).

**Documents and IT records.** IT policies are a 2020 manual with no revision and no data classification. The request for an OT asset inventory, a control network diagram, an incident response plan, a contingency plan, an OT change procedure, a manual temperature log procedure, a downtime labeling procedure, an AI use policy and an AI validation protocol returned none (EV-024). The 2025 recipe-system release and integrator VPN setup carry no review or approval record (EV-025). Office staff complete annual awareness training; no other group is assigned training, and no phishing exercises ran (EV-026). The IT Manager and FSQA Manager were designated in writing on 2026-07-01 (EV-027). The handbook has a code of conduct (EV-028). Security tickets cover office endpoints only and were handled by the IT Manager and the managed detection service (EV-029). A cyber insurance policy with a breach hotline is in force (EV-030).

**Suppliers, contracts and customers.** Payments go to the cloud, SaaS, OT service, AI vision, payroll, staffing, training and insurance suppliers listed in the vendor register (EV-031). The OT vendor, cold-chain and AI vision contracts contain no security terms; the refrigeration contractor monitors the controller through a cellular modem; the AI vision contract has no image retention or reuse terms (EV-032). The cold-chain vendor's SOC 2 Type 2 report covers the 12 months ending 2026-03-31 (EV-033), and the cloud provider's SOC 2 report is on file (EV-034). Cold-chain alerts go by SMS to one on-call supervisor with no escalation (EV-035). Customer agreements require prompt notice of events affecting product safety or supply, and two grocery chains sent security questionnaires in 2026 (EV-036).

**Regulatory status and business volume.** The plant is an FSIS official establishment and has been an FDA-registered food facility since February 2023, with no Coast Guard security plan and no PCII submission (EV-037). The refrigeration system holds about 16,000 lb of anhydrous ammonia under a PSM program and an EPA risk management plan (EV-038). FY2025 human food sales were about $148 million across 250 production days, about $11 million of it from the seafood room, with no federal customer (EV-039).

**Facilities.** Badge door groups cover the plant entrances, cure and ingredient room, server room, engine room and seafood room. CCTV covers the docks and perimeter, with no camera over the seafood dip mixing area (EV-040). The standby generator is tested monthly and carries about 72 hours of fuel (EV-041).

**Data, customers and AI tools.** The food defense plan and formulations sit on a share open to all office staff (EV-042). Online customer accounts hold name, address, email and password; card payments use a hosted page and a vendor-managed terminal (EV-043). The ERP demand forecasting module is enabled and the WMS has 30 handheld scanners (EV-044). The AI vision pilot runs on Line 3 since May 2026, office staff report using public chatbots, and no approved-tools list was found (EV-045).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Number of office staff using public chatbots, and what they paste | General Manager | 2026-07-08 | Not established at intake; P10 treats it as unknown |
| OT asset inventory and control network diagram | Controls Engineer | 2026-07-03 | None exists. P02 records component counts from interviews and the walkthrough; carried into P07 (CM-8, POAM-015) |
| Payroll service SOC 2 report | Controller | 2026-07-06 | Not provided; carried into the P01 risk register (R-021) |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Processes and owners (EV-003), sales, production days and inventory value (EV-039), backup schedules (EV-016, EV-017), cold-chain alerting (EV-035), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-001 to EV-017 and EV-040 to EV-042 |
| P04 Cloud mapping | Cloud and SaaS components (EV-015, EV-031) and provider assurance (EV-033, EV-034) |
| P01 Risk register | Likelihood inputs from the configuration exports, the ticket and incident log (EV-029), the 2023 food defense plan (EV-018), the contracts (EV-032) and the fieldwork interviews and walkthrough |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with Part 121, the FSIS and seafood HACCP record rules and the OT benchmark |
| P06 Policies | The 2020 IT manual and the document request response (EV-024), and the file share permissions (EV-042) |
| P07 Control assessment | Populations to sample from (EV-003, EV-004, EV-005) and the configuration exports to test against |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register; the insurance policy (EV-030) |
| P09 SOC 2 | Vendor assurance on file (EV-033, EV-034) and the customer questionnaires (EV-036) |
| P10 AI governance | AI tools found (EV-031, EV-032, EV-044, EV-045) |
