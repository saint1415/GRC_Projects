# Intake Report: Cris Santos Company | Chemical | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (specialty chemical formulator and packager, one Florida plant) |
| Intake window | 2026-06-29 to 2026-07-10 |
| Collected by | IT Manager, with the Controls Engineer and the EHS Manager |
| Approved | VP Operations, 2026-09-04 |

## 1. Purpose and scope
Intake collected the company's own records before any assessment work began on 2026-07-13. It covers the organization, the business and process control systems, the suppliers that touch them, the process safety records the control system supports, and the rules that may bind the company. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, the plant walkthrough, scans, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement or benchmark is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Users and access | EV-001 to EV-008 | Identity provider; HR and payroll system; help desk ticketing; HR files; DCS server pair; loading rack system; ERP admin console | 2026-06-30 to 2026-07-07 |
| Devices, OT and network | EV-009 to EV-016 | EDR console; Controls Engineer's files and DCS vendor project file; firewall and historian; OT workstations; DCS; maintenance system and DCS vendor portal; badge and video systems | 2026-07-01 to 2026-07-07 |
| Cloud and data | EV-017 to EV-020 | Cloud provider console; backup service; managed file service; IT documentation | 2026-06-30 to 2026-07-02 |
| Documents and records | EV-021 to EV-028 | Shared drive; process engineering files; DCS engineering workstation; HR learning records; help desk; HR files; EHS Manager's files | 2026-06-30 to 2026-07-07 |
| Process safety (RMP) and emergency notification | EV-029 to EV-036 | EPA RMP submission records; EHS Manager's files; maintenance system; IT documentation | 2024-02-15 to 2026-07-06 |
| Suppliers and contracts | EV-037 to EV-040 | ERP accounts payable; contracts folder; vendor and provider portals | 2026-03-31 to 2026-07-06 |
| Business volume, customers and insurance | EV-041 to EV-044 | ERP reports; Customer Service Manager's email; Controller's insurance files | 2025-12-31 to 2026-07-06 |
| AI tools, disposal and email | EV-045, EV-046, EV-054 | Accounts payable list, identity provider app list, cloud console and staff survey; shredding certificates; productivity suite admin console | 2026-06-30 to 2026-07-07 |

## 3. Observations by area
**Users and access.** Each employee account in the identity provider has MFA registered, and 2 accounts administer the cloud tenant. The DCS, SIS and historian use their own local accounts (EV-001). MFA is required for email, the ERP, the cloud console and the employee VPN (EV-002). HR lists 162 employees and 14 terminations from July 2025 to June 2026 (EV-003). Each of the 14 termination tickets closed with the identity provider account disabled on the last working day, and neither the ticket template nor the HR checklist has a step for DCS accounts or loading rack driver cards (EV-004, EV-005). The DCS has one shared operator account per HMI, one shared engineering account, and one integrator account with engineer rights. Two active DCS accounts and one active rack driver card carry the names of people on the HR terminations report. Recipe release needs one approval, held by the Process Engineer (EV-006, EV-007). One ERP user can post an inventory adjustment, including for hydrogen peroxide, without a second approval (EV-008).

**Devices, OT and network.** The EDR console lists 118 office laptops and desktops with the EDR agent and monthly patching. The 16 OT workstations are not enrolled (EV-009). The newest OT network diagram is from the 2019 CFATS Site Security Plan, and the request for an OT asset inventory, configuration baseline, control system change log, OT contingency plan, restore test record, wireless survey and OT monitoring records returned none (EV-010). The IT/OT firewall has "any" rules for the integrator remote tool and the historian, and logs errors only. The historian has one network interface on the business network and one on the control network (EV-011). A remote desktop tool for the DCS integrator starts automatically on the EWS, with one shared login and no MFA, session approval or recording. USB storage is enabled on all HMIs (EV-012). Nightly DCS configuration and recipe exports are kept on the EWS and one USB drive in the control room, with no restore recorded and no record of comparing the SIS program copy with the running logic (EV-013). The DCS journal keeps about 90 days of operator actions under shared account names (EV-014). OT patches were installed only at the October 2025 turnaround, the DCS is two major releases behind, and vendor security notices go to a former employee's mailbox (EV-015). The plant has a perimeter fence, badge readers on the gates, control room and server room, 42 cameras, and a day-shift gate guard (EV-016).

**Cloud and data.** The cloud tenant holds the LIMS, the order interface, the historian replica and analytics store, the AI-001 model service, the file shares, the backup vault and the log workspace. The 2 administrators also administer the backup vault, and the analytics service account can write to the historian replica. The log workspace keeps 90 days and has no plant or OT sources (EV-017). Daily backups of the LIMS and file shares complete with a second-region copy, in the production account, with immutability off (EV-018). The folder holding legacy CVI, the 2019 Site Security Plan and formulation files is open to 40 users (EV-019). The order interface sends order records to the batch management system through the IT/OT firewall and rejects batch sizes outside the recipe limits (EV-020).

**Documents and records.** The policy set is a 2019 template with no OT content, and the IT incident response plan (2023) and IT contingency plan cover office systems only (EV-021). The MOC procedure (rev. 2021) covers process chemistry and equipment, and the MOC log has no entries for DCS, SIS, PLC, recipe or firewall changes (EV-022). The DCS alarm export lists alarm limits and clamps for the ammonia process, with no record of a comparison with the RMP safe operating limits (EV-023). Office staff complete annual awareness training; operators, maintenance staff and contractors have none assigned (EV-024). Security tickets come from office systems only (EV-025). No document assigns OT security; the IT Manager holds part-time security duties for office IT (EV-026). The legacy CFATS records include the 2008 Top-Screen, the tier notice and the Site Security Plan last revised in 2019, and paper CVI is kept in a locked cabinet (EV-028).

**Process safety (RMP) and emergency notification.** The ammonia process is registered under Program 2, with the five-year update submitted 2024-03-18 (EV-029). The process safety information lists the maximum intended inventories used in the obligations register (EV-030). The 2024 hazard review covers instrument failures and operator errors and lists no scenario of changes to DCS setpoints or logic (EV-031). The 2025 compliance audit was completed on 2025-06-12 with each finding closed (EV-032). The emergency action plan calls responders and agencies by phone from the control room; coordination with county fire rescue and the LEPC took place on 2025-10-09 and the notification exercise on 2025-11-06 (EV-033). All 64 operators are trained under the RMP training matrix, and the operating procedures include an emergency shutdown procedure (EV-034). The SIS was proof-tested on 2025-10-21, and UPS units on the DCS, SIS, gas detectors and control room were tested at the October 2025 turnaround (EV-035). The control room and gatehouse phones are VoIP phones on the business network (EV-036).

**Suppliers and contracts.** Payments go to 15 suppliers that touch systems or data, including the DCS integrator and the data science contractor, and to one internet provider (EV-037). The integrator and data science contractor agreements have no security clauses, and no SOC 2 report from the HR and payroll vendor is on file (EV-038). The ERP vendor's SOC 2 Type 2 report covers the 12 months ending 2026-03-31, with no earlier review on record (EV-039). The cloud provider's SOC 2 report and shared responsibility description are on file (EV-040).

**Business volume, customers and insurance.** FY2025 revenue was $74 million across 250 production days, from about 600 customers; the largest private-label customer accounts for about 18% (EV-041). The plant runs about 35 batches and 25 outbound truckloads a day, with about 80% of volume blended in Blend Hall A (EV-042). That customer's security questionnaire asks how formulations and order data are protected and how supply would continue after a cyber incident (EV-043). A cyber insurance policy is in force (EV-044).

**AI tools, disposal and email.** The AI-001 process-optimization model has run in pilot on 2 Blend Hall A tanks since May 2026, and no AI risk assessment or approved-tools list was found. Staff report using public chatbots, and an enterprise assistant is under evaluation (EV-045). Paper destruction certificates are on file (EV-046). Spam and malicious attachment filtering is on for all mailboxes (EV-054).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Number of staff using public chatbots, and what they paste | IT Manager (staff survey follow-up) | 2026-07-08 | Not established at intake; P10 treats it as unknown |
| HR and payroll vendor SOC 2 report | Controller | 2026-07-06 | Not provided; carried into the P01 risk register (R-031) |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Revenue and volume (EV-041, EV-042), the DCS backup schedule (EV-013), the emergency notification path (EV-033, EV-036), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-006, EV-009 to EV-015 and EV-023 |
| P04 Cloud mapping | Cloud and SaaS components (EV-017 to EV-020, EV-037) and provider assurance (EV-039, EV-040) |
| P01 Risk register | Likelihood inputs from the exports, documents and process safety records above |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the RBPS 8 benchmark, the OT benchmark and RMP Program 2 |
| P06 Policies | The existing 2019 template (EV-021) and the MOC procedure (EV-022) |
| P07 Control assessment | Populations to sample from (EV-003, EV-004, EV-006, EV-007, EV-009) |
| P08 IR runbook | Notification duties from the obligations register; the emergency action plan (EV-033); contacts from the vendor register |
| P09 SOC 2 | The customer questionnaire (EV-043) and vendor assurance on file (EV-039, EV-040) |
| P10 AI governance | AI tools found (EV-037, EV-045) |
