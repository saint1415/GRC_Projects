# Intake Report: Cris Santos Company | Chemical | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (specialty chemical maker, one Florida unit, 7 employees) |
| Intake window | 2026-06-29 to 2026-07-10 |
| Collected by | Office Manager, with the MSP lead technician for the MSP exports and the Operations Manager for the blend room, the HMI PC and the integrator portal |
| Approved | Owner and President, 2026-08-31 |

## 1. Purpose and scope
Intake collected the company's own records before any assessment work began on 2026-07-13. It covers the organization, the batch control system and the office and SaaS systems the business runs on, the suppliers that run or reach them, the regulated chemicals on site, and the rules that may bind the company. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, walkthroughs, tests) to the same register, so one list backs every deliverable.

A 7-person blender has no HR system, CMDB or accounts payable vendor master. Its systems of record are the SaaS admin consoles (productivity suite, accounting and inventory, SDS service), the payroll service, the integrator's portal and the HMI PC's own screens, the MSP's exports and monthly report, the contracts folder and the DOT files, and what can be seen on site.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| People and access | EV-001 to EV-007 | Payroll service; HR files; productivity suite, accounting and SDS service consoles; integrator portal | 2026-06-30 to 2026-07-02 |
| Batch control system | EV-008 to EV-011 | HMI PC screens; integrator email; recipe export log | 2026-07-01 to 2026-07-07 |
| Office devices, network and backup | EV-012 to EV-018 | MSP device, policy, encryption and antivirus consoles; MSP monthly report; firewall documentation; backup console; MSP tickets | 2026-06-30 to 2026-07-03 |
| Suppliers and contracts | EV-019 to EV-023 | Contracts folder; vendor websites and portals | 2026-05-31 to 2026-07-06 |
| Hazmat, chemicals and CFATS | EV-024 to EV-029 | DOT files; accounting and inventory service; supplier SDSs; Top-Screen file; emergency action plan | 2026-06-30 to 2026-07-08 |
| Documents and records | EV-030 to EV-034 | Policies folder and document request; HR files; alarm and video portal; service agreements; insurance policies | 2026-07-06 |
| Business volume and customers | EV-035 to EV-038 | Accounting and inventory service; email inbox; Owner's files | 2025-12-31 to 2026-07-08 |
| Site, people and AI tools | EV-039 to EV-042 | Walk-through; intake interviews; staff survey; payables list | 2026-06-30 to 2026-07-09 |

## 3. Observations by area
**People and access.** Payroll lists 7 active employees. One Blend Operator left on 2026-03-13 and a replacement was hired on 2026-04-20 (EV-001). Termination notes for that operator and for a temporary bookkeeper whose engagement ended in March 2026 record keys, a key fob and a laptop returned, and no account removal step (EV-002). The productivity suite has named accounts for the 7 employees with MFA enforced for all users; sign-in and sharing alerts are available and none notifies anyone, and sharing by link is allowed (EV-003). The accounting and inventory service has 5 named logins, with MFA on the Owner's login only (EV-004). The SDS service has named accounts for the Owner and the QC Technician, and only the Owner can publish (EV-005). The integrator portal has one company login, which the Operations Manager says integrator staff also use; MFA is offered and off (EV-006). Every remote session in June 2026 used that login, and the log has no approval field (EV-007). The lists were compared with each other during the risk assessment (EV-045).

**Batch control system.** The HMI PC runs an operating system edition past its vendor's mainstream support end date, last updated in 2023, with no antivirus and no disk encryption. A remote desktop service, a web browser with a webmail shortcut, and file sharing are on, USB storage is allowed, and the PC sits on the office subnet (EV-008). The HMI has two local logins; the operator login, used by both Blend Operators and the Operations Manager, can edit recipes and alarm limits, and the audit trail is off (EV-009). The integrator's copy of the PLC program and HMI project dates from 2023 and has never been restored, and the gateway is kept powered on (EV-010). Recipes are exported monthly to a USB stick kept in a desk drawer (EV-011).

**Office devices, network and backup.** The MSP device list shows 4 laptops and 2 desktops; the warehouse tablet, the HMI PC, the PLC, the gateway, network devices and SaaS services are not on it (EV-012). Staff have no local administrator rights, a 10-minute screen lock applies to the 6 computers, and disk encryption is on the 4 laptops and not the 2 desktops (EV-013). Antivirus alerts go to the MSP help desk queue in business hours and not to the company (EV-014). The MSP patches the 6 computers monthly; its listed services do not include vulnerability scanning or the HMI PC (EV-015). The firewall exposes no inbound services; one office subnet holds the office computers, printers, phones and the HMI PC, and a guest Wi-Fi network is configured (EV-016). The cloud backup copies the suite daily with 30 days of versions and immutable retention off, has no restore jobs, and does not include the HMI PC or PLC (EV-017). MSP tickets show no restore tests and no tickets for the HMI PC (EV-018).

**Suppliers and contracts.** The MSP contract excludes the batch control system, has a 4-business-hour response time, and has no recovery time commitment, security terms or incident notice term (EV-019). The integrator service agreement has no response or recovery time and no security, incident notice or data-use terms (EV-020). The SaaS vendors describe encryption at rest and in transit (EV-021). The accounting and inventory vendor's SOC 2 Type 2 report covers the 12 months ending 2026-05-31 and states an RTO of 8 hours and an RPO of 1 hour (EV-022). The ERI provider answers the emergency number on shipping papers and receives SDSs by email (EV-023).

**Hazmat, chemicals and CFATS.** The PHMSA registration is valid through 2027-06-30 (EV-024). The DOT training binder holds May 2024 records for 5 of the 6 current hazmat employees and none for the operator hired on 2026-04-20 (EV-025). June 2026 bills of lading show Class 8 and Class 3 products in packagings up to 275-gal totes, with the ERI number; PDFs are stored back to 2021 (EV-026). The highest quantities on hand were 2 totes of 35% hydrogen peroxide, 2 totes each of 50% sodium hydroxide and 12.5% sodium hypochlorite, 1 tote of 75% phosphoric acid, 8 drums of isopropyl alcohol and 4 propane cylinders (EV-027). The Top-Screen file holds the 2009 Top-Screen and the 2010 letter stating the facility is not high risk (EV-028). The emergency action plan covers spills and fire and refers to the office phone system for the release reporting numbers (EV-029).

**Documents and records.** The request for policies, a risk assessment, an incident response plan, a contingency plan, a data classification scheme, an asset inventory, a network diagram, account procedures and vendor reviews returned only the employee handbook (EV-030, EV-031). The building keypad uses one shared code, last changed in 2023, and there is no record of video reviews (EV-032). One internet line carries the office phones, and the phone system holds the contact list (EV-033). A cyber liability policy with a breach hotline is on file, with general and pollution liability policies (EV-034).

**Business volume and customers.** Shipments were about $1.1 million across 250 production days in FY2025, about $4,400 per production day, from about 140 customers; the private-label distributor accounts for about 22% of revenue (EV-035). About $22,000 is invoiced per week (EV-036). The distributor's security and continuity questionnaire is due 2026-09-30 (EV-037). An independent assessor is engaged for a control assessment starting 2026-08-10 (EV-038).

**Site, people and AI tools.** The walk-through counted 4 laptops, 2 desktops and a tablet that opened without a passcode, and found the hardwired emergency stop, the T-1 high-temperature switch, the gateway inside the control panel, the locked raw-material room, and no printed call list at the exits (EV-039). The Owner and the Operations Manager describe recipe changes made with no approval or record, USB sticks used to move recipe files, a paper formulation binder, and no notice from the integrator before the AI feature was switched on (EV-040). The portal shows the AI batch-optimization feature enabled on 2026-05-11 in advisory mode with write-back off (EV-006). The staff survey found the portal recommendations, the SDS service's drafting assistant, and mentions of public chatbots (EV-041). The payables list shows no AI tool charges (EV-042).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Number of staff using public chatbots, and what they enter | Office Manager (staff survey follow-up) | 2026-07-09 | Not established at intake; P10 treats it as unknown |
| MSP technician list and evidence of MFA on the remote management platform | MSP lead technician | 2026-07-03 | Not provided; asked again in P07 on 2026-08-03 (EV-SA-9) and carried into the P01 risk register (R-016) and POAM-013 |
| List of integrator staff who use the shared portal login | Integrator lead engineer | 2026-07-06 | Not provided; asked again in P07 (EV-AC-17) |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Processes and owners (EV-001, EV-040), revenue, cash and order volume (EV-035, EV-036), recipe and backup copies (EV-010, EV-011, EV-017), vendor recovery figures (EV-019, EV-020, EV-022), the call list and phone line (EV-029, EV-033), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-003 to EV-018 |
| P04 Cloud mapping | SaaS components, the portal and the MSP-operated backup (EV-003 to EV-007, EV-017) and provider documentation (EV-021, EV-022) |
| P01 Risk register | Likelihood inputs from the console and MSP exports, the HMI screens, the contracts folder, the walk-through (EV-039) and the intake interviews (EV-040) |
| P03 Gap analysis | The obligations register (which rules apply), the chemical quantities and DOT records (EV-024 to EV-029), and every observation above, compared with the requirements |
| P06 Policies | The policies folder and the handbook (EV-030, EV-031) |
| P07 Control assessment | Populations to test from (EV-001, EV-003, EV-004, EV-009, EV-012) |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register; the emergency action plan and the insurance policies (EV-029, EV-034) |
| P09 SOC 2 | Vendor assurance on file (EV-022) and the distributor's questionnaire (EV-037) |
| P10 AI governance | AI tools found (EV-005, EV-006, EV-041, EV-042) |

The asset inventory in this folder is the assessment's list, built from the evidence above. It is not a company-maintained inventory; the SSP (CM-8) plans one by 2026-10-31.
