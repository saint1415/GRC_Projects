# Intake Report: Cris Santos Company | Healthcare and Public Health | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (rural critical access hospital, 12 beds, 24-hour ED, one Florida campus) |
| Intake window | 2026-06-29 to 2026-07-10 |
| Collected by | IT Manager (Security Officer), with the Quality and Compliance Manager (Privacy Officer) and the Facilities Manager (Emergency Preparedness Coordinator) |
| Approved | CEO, 2026-08-31 |

## 1. Purpose and scope
Intake collected the hospital's own records before any assessment work began on 2026-07-13. It covers the organization, the systems that create, receive, maintain or transmit ePHI, the building OT that shares their network, the suppliers and contracted clinical groups that touch them, the emergency preparedness program, and the rules that may bind the hospital. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, scans, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Users and access | EV-001 to EV-008 | Identity provider; payroll and HR system; agency and medical staff rosters; help desk tickets; EHR admin console; complaint log | 2026-06-30 to 2026-07-02 |
| Devices, servers and network | EV-009 to EV-015 | MSP remote management console; EDR console; MSP agreement; directory; firewall, wireless and VPN configuration | 2026-06-26 to 2026-07-06 |
| Cloud and backups | EV-016, EV-017 | Cloud provider console; backup appliance and cloud backup service | 2026-06-30 to 2026-07-01 |
| Suppliers and contracts | EV-018 to EV-024 | Vendor portals; productivity suite console; accounting system; contracts folder; license and certification files | 2026-03-31 to 2026-07-06 |
| Business volume | EV-025, EV-026 | Accounting system; EHR reporting | 2025-12-31 to 2026-06-30 |
| Emergency preparedness and downtime | EV-027 to EV-033 | Emergency preparedness program binder; transfer agreements; generator logs; downtime binders and print logs | 2026-06-30 to 2026-07-06 |
| Documents and records | EV-034 to EV-039 | CEO's files; document request list; HR files; learning records; medical staff office | 2023-11-30 to 2026-07-06 |
| Facilities, devices and disposal | EV-040 to EV-046 | Badge system; facility records; destruction certificates; biomedical log; walk-through; interface engine; carrier and phone records | 2026-06-30 to 2026-07-08 |
| Incident history and changes | EV-047, EV-048 | Help desk ticketing (the incident log); MSP tickets and image documentation | 2026-06-30 |
| AI tools | EV-049, EV-050 | EHR release notes and source attribute display; staff survey; identity provider app list | 2026-03-02 to 2026-07-07 |
| Other records | EV-051 to EV-056 | Insurance files; benefits broker letter; privacy notice; public health and HIE agreements; retention schedule; OT walk-through | 2026-07-06 to 2026-07-08 |

## 3. Observations by area
**Users and access.** The identity provider holds named accounts for the 60 employees and for contracted clinicians, agency nurses and vendor users. No contracted or agency account has an expiry date, and generic accounts exist for the ED tracking board, the analyzer middleware workstation and a nursing station unit login (EV-001). MFA is required for email, employee remote access, the identity provider and the cloud console; EHR sign-ins from the hospital network are excluded from that rule, and the 2 cloud administrators and the IT Support Specialist use hardware keys (EV-002). HR recorded 10 employee terminations from January to June 2026 (EV-003). The agency tracking sheet records end dates only when an agency reports one (EV-004). Employee disable tickets close 1 to 2 business days after the HR notice, and there is no ticket type for ending agency or contracted assignments (EV-005). EHR roles come from the vendor catalog, and the nursing station uses a shared unit login (EV-006). The EHR access report ran twice in 12 months, each time after a privacy complaint (EV-007, EV-008).

**Devices, servers and network.** The MSP console lists 88 desktops and workstations on wheels, 12 laptops, 16 barcode scanners and 2 downtime PCs. Encryption is reported on the 12 laptops and on none of the 88 desktops and workstations on wheels. The ED tracking board and the nursing station shared workstation are exempt from screen lock (EV-009). Operating system updates install monthly; the firewall and the infusion pump drug-library server are outside that schedule (EV-010). EDR has run on servers and managed workstations since 2025, with alerts going to an MSP queue staffed in weekday business hours (EV-011, EV-012). The MSP agreement includes no 24x7 monitoring or vulnerability scanning (EV-012). MSP technicians share one standing domain administrator account, and the local backup appliance is joined to the hospital directory (EV-013). One internal network carries workstations, servers, medical devices, building OT and the phones; there is one fiber circuit with a cellular backup, and the firewall firmware is two releases behind (EV-014). The teleradiology group's support VPN profile uses one shared account with a password only and is enabled 24x7 (EV-015).

**Cloud and backups.** The cloud tenant holds the imaging archive, the interface engine (a single VM) and the backup vault. The vault sits in the production account and region with immutable retention off, and backup administration uses the same 2 administrator roles (EV-016). Nightly server backups and daily cloud snapshots completed from April to June 2026, with no restore jobs, including for the imaging archive, and no backups of OT configurations (EV-017).

**Suppliers and contracts.** The EHR vendor's SOC 2 Type 2 report covers the 12 months ending 2026-03-31 and states an RTO of 8 hours and an RPO of 15 minutes (EV-018). Cloud and SaaS provider assurance is on file (EV-019). External email is not encrypted by rule, and patient documents go to transfer partners by email (EV-020). Signed BAAs exist with 8 vendors. None was located for the cloud fax service or the biomedical equipment service contractor, and no vendor security reviews are on file other than the EHR vendor's SOC 2 report (EV-021, EV-022). The clearinghouse agreement covers standard electronic transactions (EV-023). The hospital is licensed and certified as a critical access hospital, lists no substance use disorder program, and is not part of a health system (EV-024).

**Business volume.** Revenue was $28.2 million in FY2025, about $77,000 a day, with Medicare about 55% and about 60 days of cash on hand (EV-025). The ED sees about 7,300 visits a year, the average inpatient and swing-bed census is 7, and the EHR holds records for about 38,000 individuals (EV-026).

**Emergency preparedness and downtime.** The all-hazards plan was reviewed in 2025-06. Its annexes cover hurricanes, surge and utility loss; IT outages have one generic page, there is no cyber annex, and there are no diversion criteria for an IT outage (EV-027). The 2025 hazard vulnerability analysis scores no cyberattack or EHR outage hazard (EV-028). The county full-scale exercise (2026-05-14) and a mass-casualty tabletop (2025-11-12) have after-action reports, and no exercise has been run without the EHR (EV-029). The communication plan relies on VoIP phones, text notification, EMS radio and analog lines in the ED and at the nursing station (EV-030, EV-046). Transfer agreements are in place with two hospitals (EV-031), and generator tests follow the NFPA 110 schedule (EV-032). Downtime procedures date from 2019; the 2 downtime PCs print census and MAR reports every 2 hours, with no record of a test or drill (EV-033).

**Documents and records.** The last risk analysis is a consultant report dated 2023-11-30 that does not cover medical devices, building OT or the cloud tenant; it supported the Promoting Interoperability attestation (EV-034). The request for security policies, an incident response plan, a ransomware runbook, an IT contingency plan, MDS2 forms and scan reports returned none (EV-035). The handbook has no section on security or privacy violations (EV-036). Training records show annual HIPAA training for employees and no completions for contracted clinicians or agency nurses, and no reminders or phishing exercises (EV-037). The Security Officer was designated on 2024-02-01 (EV-038).

**Facilities, devices and disposal.** Badge readers control the server room, pharmacy and ED entrance, and the badge list was reviewed for 2026-Q2 (EV-040, EV-041). Devices leave for repair with no wipe step recorded (EV-042). The biomedical log has no network or software fields (EV-043). The CT acquisition workstation runs an operating system past its support end date, and the drug-library server shows no updates since mid-2025 (EV-044). The interface engine has no queue monitoring (EV-045).

**Incident history and changes.** Nineteen security-related tickets in 12 months were closed by IT or the MSP, with no incident category, incident numbers or post-incident notes (EV-047). Server and network changes are ticketed; the drug library, dispensing cabinet profiles and OT have no change tickets (EV-048).

**AI tools.** The vendor's sepsis prediction model was enabled on 2026-03-02 at the default threshold, with no owner named and no validation or Section 1557 review record (EV-049). Staff report using public chatbots to draft letters and policies, and no approved-tools list was found (EV-050).

**Other records.** Nurse call, building automation, medical gas alarms and generator monitoring connect to the hospital network and are not in any inventory, and OT vendor contracts do not mention configuration backups (EV-056). The employee health plan is fully insured (EV-052).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Number of staff using public chatbots, and what they paste | CEO | 2026-07-08 | Not established at intake; P10 treats it as unknown |
| Count of networked medical devices and OT controllers | Facilities Manager; Imaging and Laboratory Managers | 2026-07-08 | Not established at intake; counted during P07 (EV-CM-8) |
| Productivity suite vendor's BAA or BAA terms | CFO | 2026-07-06 | Not located in the BAA inventory at intake |
| Building automation and nurse call vendors' configuration backup practice | Facilities Manager | 2026-07-08 | Not confirmed by the vendors (P05 key finding 4) |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Processes and owners (EV-003, EV-004), revenue and volume (EV-025, EV-026), backup schedule (EV-017), vendor recovery terms (EV-018), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-001, EV-002, EV-006 to EV-017 and EV-020 |
| P04 Cloud mapping | Cloud and SaaS components (EV-016, EV-021) and provider assurance (EV-018, EV-019) |
| P01 Risk register | Likelihood inputs from the ticket history (EV-047), configuration exports, the walk-throughs (EV-044, EV-056) and the emergency program records (EV-027 to EV-030) |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the HIPAA Security Rule and 42 CFR 485.625 |
| P06 Policies | The document request response (EV-035) and the handbook (EV-036) |
| P07 Control assessment | Populations to sample from (EV-001, EV-003, EV-005, EV-009) |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register; the insurer's response panel (EV-051) |
| P09 SOC 2 | Vendor assurance on file (EV-018, EV-019) |
| P10 AI governance | AI tools found (EV-049, EV-050) |
