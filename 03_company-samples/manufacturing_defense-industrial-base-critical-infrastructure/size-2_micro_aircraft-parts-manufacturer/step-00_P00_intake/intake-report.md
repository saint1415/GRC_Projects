# Intake Report: Cris Santos Company | Defense Industrial Base | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (aircraft parts machine shop, DoD subcontractor, one leased Florida unit) |
| Intake window | 2026-07-06 to 2026-07-10 |
| Collected by | Office Manager (Security and Compliance Coordinator), with the MSP lead technician for the MSP exports |
| Approved | President, 2026-08-31 |

## 1. Purpose and scope
Intake collected the company's own records before any assessment work began on 2026-07-13. It covers the organization, the systems that hold or protect controlled unclassified information (CUI) and federal contract information (FCI), the suppliers that touch them, and the rules that may bind the company. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, tests) to the same register, so one list backs every deliverable.

A 7-person shop has no HR system, CMDB or accounts payable vendor master. Its systems of record are the admin consoles of the CUI suite, the commercial suite and the ERP, the payroll service, the MSP's exports and monthly report, the contracts folders, the bank and card statements, the President's SPRS and export compliance files, the machine records, and what can be seen in the shop.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| People and records | EV-001 to EV-004 | Payroll service; HR files; President's files | 2026-06-30 to 2026-07-06 |
| CUI suite, commercial suite and ERP | EV-005 to EV-009 | Admin consoles of SYS-01, SYS-02 and SYS-09 | 2026-07-07 to 2026-07-08 |
| Devices, network and backup | EV-010 to EV-018 | MSP device, policy, encryption and antivirus consoles; MSP monthly report; firewall documentation; backup console; MSP tickets and RMM log; MSP contract | 2026-06-30 to 2026-07-07 |
| Shop and facility | EV-019 to EV-022 | Machine records; visitor log; alarm contract; insurance policies | 2026-07-07 to 2026-07-08 |
| Contracts and compliance | EV-023 to EV-029 | Customer purchase orders; email inbox; ERP purchasing; SPRS; policies folder; export compliance files | 2025-12-15 to 2026-07-08 |
| Business volume and suppliers | EV-030 to EV-034 | Accounting SaaS; bank and card statements; service agreements; FedRAMP Marketplace and provider documentation; Prime A portal | 2025-12-31 to 2026-07-08 |
| Walk-through and interviews | EV-035 to EV-038 | Building walk-through; interviews with the Office Manager, the President and the shop staff | 2026-07-09 to 2026-07-10 |

## 3. Observations by area
**People and records.** Payroll lists 7 active employees and 1 separation from January to June 2026, a part-time CNC programmer whose last day was 2026-03-27 (EV-001). Each personnel file holds a reference check and a U.S.-person status record made at hire, and there is no offboarding checklist (EV-002). Training records show only a one-page hire orientation checklist with one line about drawings (EV-003). The Office Manager was designated Security and Compliance Coordinator in writing on 2026-07-06 (EV-004).

**CUI suite, commercial suite and ERP.** The CUI suite has 6 accounts: 4 named users, 1 MSP administrator account and 1 break-glass account, all with MFA by authenticator app (EV-005). Lockout is on, external sharing is at the provider default (anyone with a link), audit logging is at the default retention, no alert or device rules are set, and the suite mobile app is on the President's personal phone (EV-006). About 900 controlled files sit in the job folders, shared with all 4 users as one group, including the ITAR folders; the sync client runs on SYS-03, SYS-04 and both laptops (EV-007). The commercial suite has 5 user accounts with MFA and a shared orders mailbox with no MFA and legacy sign-in allowed, and 2024 and 2025 job folders remain in its file storage (EV-008). The ERP uses named accounts with MFA, and 31 job records have drawing PDFs attached (EV-009).

**Devices, network and backup.** The MSP device list shows 4 computers (the CAM workstation, the quality PC and 2 laptops) and no machines, printer, phones, network devices or SaaS services (EV-010). The laptops are encrypted; SYS-03 and SYS-04 are not. The CNC Programmer's account on SYS-03 is a local administrator, SYS-04 uses a shared QC login, the two shop PCs are exempt from screen lock and have no local lockout policy, and SYS-04 has remote desktop enabled (EV-011). The MSP patches operating systems and common applications monthly; CAM, DNC and CMM software are outside its patch scope, and its services do not include scanning or log monitoring (EV-012). Antivirus runs on all 4 computers and scans USB drives on insertion (EV-013). The firewall denies unsolicited inbound traffic and allows all outbound traffic; office, CAM, quality, machine, printer and phone traffic share one subnet; guest Wi-Fi is separate; the staff Wi-Fi key was last changed in 2023 (EV-014). Nightly images of SYS-03 and SYS-04 are kept 30 days, with no restore jobs from April to June (EV-015). MSP tickets show no wipe record for a computer retired in 2024 or a CAM workstation drive sent for repair in 2025, and one file restore in 2025 (EV-016). RMM sessions are logged by the MSP (EV-017). The MSP contract has a 4-business-hour response time, no recovery time, and no responsibility matrix, U.S.-person or incident notice term; the image backup runs through an MSP subcontractor's commercial cloud service (EV-018).

**Shop and facility.** The shop has 3 networked CNC machines and 2 older machines built in 2004 and 2009 whose controllers the builder no longer supports; service engineers connect their own laptops or USB media, including during a builder visit in May 2026 (EV-019). The paper visitor log has a few entries for June and July 2026 and no escort or citizenship field (EV-020). The after-hours alarm is monitored (EV-021). A cyber liability policy with a breach hotline and panel vendors, and a property and business interruption policy, are on file (EV-022).

**Contracts and compliance.** Current Prime A and Supplier B purchase orders include DFARS 252.204-7012, 252.204-7019, 252.204-7020 and FAR 52.204-21, and none includes DFARS 252.204-7021 (EV-023). Prime A's notice of 2026-06-15 says purchase orders under its new program issued from 2027-04-01 will require CMMC Level 2 (Self) (EV-024). Customer C sent a supplier security questionnaire on 2026-07-08, due 2026-09-30 (EV-025). Purchase orders to the 2 outside processors use a commercial template without DFARS clauses (EV-026). The SPRS score of 110 posted on 2025-12-15 rests on a yes/no checklist with no SSP or evidence attached (EV-027). A purchased policy template set was never adopted, and the request for an SSP, risk assessment, incident response plan, contingency plan, inventory, network diagram and disposal records returned none (EV-028). DDTC registration is current; about 60 of 140 active part numbers have CUI drawings, about 25 of them ITAR defense articles (EV-029).

**Business volume and suppliers.** FY2025 revenue was about $1.1 million over about 250 production days, about $4,400 of shipments per production day, with Prime A about 40% and Supplier B about 15%; the cash reserve covers about 45 days (EV-030). The statements show recurring payments to the cloud, software, MSP, payroll, accounting, telecom, alarm and insurance suppliers, and no AI tool charges (EV-031). There is one internet line with no failover (EV-032). The CUI suite offering is listed as FedRAMP authorized at Moderate or higher, and its customer responsibility matrix is not in the company's files (EV-033). Prime A portal accounts are named and use the prime's MFA (EV-034).

**Walk-through and interviews.** The walk-through counted 5 CNC machines, the CMM, 4 computers, a printer, 4 VoIP desk phones, and the firewall and switch in an office closet (EV-035). The Office Manager says Supplier B emails drawing packages to the orders mailbox, nobody reviews logs, and drawing copies go on paper to the outside processors (EV-036). The President says the company has no incident response plan, no DoD medium assurance certificate and no DIBNet account, and that a foreign-national builder engineer worked at a machine with a drawing posted on it in May 2026 (EV-037). The shop staff describe the shared QC login, USB loading of the older machines with personal drives, and scrap drawings going in the general trash (EV-038).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Customer responsibility matrix (CRM) for the CUI suite | Government-community cloud provider (support portal) | 2026-07-08 | Not received at intake; tracked in the SSP (P02) and POAM-009, due 2026-09-30 |
| MSP technician list with MFA status, U.S.-person confirmation, and the MSP's own security assurance | MSP lead technician | 2026-07-08 | Not provided at intake; asked again in P07, where the technician list and the MSP SOC 2 report arrived (EV-AC-2, EV-SA-9) and the U.S.-person confirmation did not (POAM-009) |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Processes and owners (EV-001), revenue, invoicing and cash (EV-030), backup schedule and restore history (EV-015, EV-016), the MSP contract (EV-018), the machine list (EV-019), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-005 to EV-018 and the walk-through (EV-035) |
| P04 Cloud mapping | SaaS components and the MSP-operated backup (EV-005 to EV-009, EV-015, EV-018) and provider documentation (EV-033) |
| P01 Risk register | Likelihood inputs from the console and MSP exports, the contracts folder, the SPRS record (EV-027), the walk-through and the intake interviews (EV-035 to EV-038) |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the requirements |
| P06 Policies | The unused template set (EV-028) and the designation letter (EV-004) |
| P07 Control assessment | Populations to test from (EV-001, EV-005, EV-008, EV-010, EV-020) |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register; the cyber policy (EV-022) and purchase order clauses (EV-023) |
| P09 SOC 2 | Customer C's questionnaire (EV-025) and vendor assurance on file (EV-033) |
| P10 AI governance | AI tools found later in fieldwork (EV-043, EV-049) and the statements with no AI tool charges (EV-031) |

The asset inventory in this folder is the assessment's list, built from the evidence above. It is not a company-maintained inventory; the SSP (CM-8) plans one by 2026-09-30.
