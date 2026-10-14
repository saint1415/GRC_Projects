# Intake Report: Cris Santos Company | Critical Manufacturing | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (transformer repair and remanufacturing shop, one leased building in Florida) |
| Intake window | 2026-06-29 to 2026-07-10 |
| Collected by | Office Manager (Security Coordinator), with the MSP lead technician for the MSP exports and the Shop Manager for the shop equipment |
| Approved | Owner, 2026-08-31 |

## 1. Purpose and scope
Intake collected the shop's own records before any assessment work began on 2026-07-13. It covers the organization, the office systems and the shop equipment that hold or produce its data, the suppliers that touch them, and the rules and contracts that may bind the shop. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, walkthroughs, tests) to the same register, so one list backs every deliverable.

A 7-person shop has no HR system, CMDB or accounts payable vendor master. Its systems of record are the SaaS admin consoles (ERP, productivity suite, AI portal), the payroll service, the MSP's exports and monthly report, the contracts folders, the bank and card statements, the shop equipment's own screens, manuals and vendor records, and what can be seen in the building.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| People and access | EV-001 to EV-005 | Payroll service; HR files; ERP and productivity suite admin consoles | 2026-06-30 to 2026-07-01 |
| Data | EV-006 | Productivity suite admin console | 2026-07-01 |
| AI portal | EV-007, EV-008 | Oil laboratory analytics portal; vendor website | 2026-07-02 |
| Devices, network and backup | EV-009 to EV-015 | MSP remote management, antivirus and backup consoles; MSP monthly report; MSP network documentation; MSP tickets | 2026-06-30 to 2026-07-02 |
| Suppliers and contracts | EV-016 to EV-021 | Contracts folders; ERP vendor portal; vendor websites; email inbox | 2026-03-10 to 2026-07-07 |
| Business volume and payments | EV-022 to EV-024 | ERP accounting and reporting; bank and card statements | 2025-12-31 to 2026-06-30 |
| Documents and records | EV-025 to EV-027 | Shared drive and document request; Owner's files; contracts folder | 2026-07-01 to 2026-07-06 |
| Shop equipment | EV-028 to EV-032 | Shop Manager's files; test PC screens; test report folder; OEM manual and invoices; order history | 2026-06-30 to 2026-07-07 |
| Building and people | EV-033 to EV-039 | Service agreement; walk-through; key list and alarm account; interviews; staff survey | 2026-07-06 to 2026-07-09 |

## 3. Observations by area
**People and access.** Payroll lists 7 active employees and 1 termination from January to June 2026, a Field Service Technician whose last day was 2026-05-08 (EV-001). HR files cover 7 current and about 15 former employees. His leaver record shows keys, the cooperative badge and the field laptop collected on his last day, and has no step for accounts, shared passwords or the cooperative (EV-002). The ERP has 6 named accounts; the Owner and the Office Manager hold the administrator role (EV-003). ERP MFA is available and not enforced for any account, the password minimum is 8 characters, and the June audit trail shows both administrator accounts doing daily work such as quotes and invoices (EV-004). The productivity suite has a named account for each employee and a shared "shop" account, with MFA enforced for all users since 2025 and a 12-character minimum (EV-005). The Office Manager creates and removes accounts on verbal requests, when remembered, and accounts have never been reviewed (EV-036). The lists were compared with each other during the risk assessment (EV-042).

**Data.** The shared drive is synced to the 3 office desktops and holds the rewind data sheet library (about 1,800 sheets), test report copies, customer drawings, the federal order folder and HR files (EV-006). FCI and customer drawings arrive by email, and there is no list of where sensitive data is kept (EV-036). Anyone-with-the-link sharing is allowed (EV-005).

**AI portal.** Since 2026-04 the Field Service and Test Technician has uploaded DGA results and nameplate data, including site coordinates, for about 900 transformers belonging to 2 cooperatives and 1 municipal utility (EV-007). The portal's standard terms allow the vendor to use uploaded data to improve its models, and no data processing addendum is on file (EV-008).

**Devices, network and backup.** The MSP device list shows 6 managed computers; the tablets, the test PC, the network equipment, the oven controls, the winding machine and the camera recorder are not on it, and the RMM agent has administrator rights on each listed computer (EV-009). Staff have no local administrator rights; the shop-floor PC uses a shared "shop" sign-in and is excluded from the 15-minute screen lock; full-disk encryption is reported on the 2 laptops only (EV-010). The MSP reports monthly patching and antivirus on the 6 managed computers, lists the test PC as excluded from patching at the test set vendor's request, and offers no vulnerability scanning or endpoint detection and response (EV-011, EV-012). Antivirus alerts go to the MSP help desk in business hours (EV-012). One Wi-Fi network serves the office and the shop with no guest network; its password was last changed in 2023; the test PC, the oven HMI, the camera recorder and staff and unnamed phones share one address range; firewall logs are kept 7 days (EV-013). The suite backup runs daily with 1-year retention, one MSP login can delete backups, and the job history has no restores; ERP data and the test PC are not backed up there (EV-014). MSP tickets show an office PC retired in 2025 with no wipe or destruction record, and no restore tests (EV-015).

**Suppliers and contracts.** The MSP contract covers help desk, patching, antivirus, firewall and Wi-Fi, suite administration and the suite backup, with a 4-business-hour response time and no recovery time, incident notice, MFA requirement or technician list. The MSP holds no SOC 2 report and answered a security questionnaire in 2025 (EV-016). The ERP vendor's SOC 2 Type 2 report covers the 12 months ending 2026-03-31 with no exceptions and states an RTO of 8 hours and an RPO of 1 hour (EV-017). The suite, the backup service and the AI portal describe encryption and TLS (EV-018). The G&T cooperative's exhibit, added in 2025, requires incident notice within 72 hours, response coordination, and access-revocation notice within 1 business day; the Shop Manager and the Field Service and Test Technician hold cooperative badges (EV-019). The cooperative sent a vendor security questionnaire in July 2026, due 2026-09-30 (EV-020). The civilian federal purchase order of 2026-03-10 incorporates FAR 52.204-21, 52.204-23 and 52.204-25, has no DFARS clauses, and has no subcontracts (EV-021).

**Business volume and payments.** Receipts were about $1.1 million in FY2025, about $4,200 per working day, and the cash reserve covers about 45 days of expenses (EV-022). The shop handled about 420 units in FY2025 for about 25 customers in Florida and neighboring states; the G&T cooperative is about 20% of receipts; about 30 units are held in storm stock (EV-023). The statements show recurring payments to 9 suppliers and none to AI tool vendors (EV-024).

**Documents and records.** The request for policies, a risk assessment, an incident response plan, a contingency plan, an inventory, an obligations list, training records, an incident log and disposal records returned none (EV-025). The Owner designated the Office Manager as Security Coordinator in writing on 2026-07-01 (EV-026). A cyber policy bought in 2025 has a 24x7 breach hotline and panel vendors (EV-027).

**Shop equipment.** The test set is calibrated every year, and the test set vendor supports the test PC by phone with no written terms for remote sessions (EV-028). The test PC runs an operating system past vendor support, with one shared administrator account, antivirus turned off, remote desktop enabled, and about 6 years of results in a local database that no backup software covers (EV-029). Every unit shipped in June 2026 has a test report signed by the Shop Manager (EV-030). The oven's over-temperature trip and pressure relief are hard-wired and independent of the PLC; recipes are stored in the PLC; the OEM troubleshoots remotely through its own cellular modem with no written terms (EV-031). The camera kit was bought online in 2022 under a store brand with no manufacturer named (EV-032).

**Building and people.** There is one cable internet line and no failover (EV-033). The walk-through counted 3 office desktops, 2 laptops, the shop-floor PC and 2 tablets, the test PC, the oven HMI with its modem light on, a winding machine with no network cable, and the camera recorder on the network shelf; a sign in the break area shows the Wi-Fi password; the office is locked with a monitored alarm and the yard is fenced and locked (EV-034, EV-035). The Wi-Fi password is given to truck drivers on request, and the Office Manager's habit of calling suppliers back before changing bank details stopped a fraudulent request in 2026-03 (EV-036). Only the Owner holds the insurer's hotline number (EV-037). The oven modem stays on, the shop does not hold its credentials or receive session records, recipes exist only in the PLC, winding programs live on USB sticks, and the test software media and license key have not been located (EV-038). The staff survey found the AI portal pilot and the Office Manager's use of a public chatbot to draft emails and quotes (EV-039).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| MSP technician list and evidence of MFA on the RMM platform | MSP lead technician | 2026-07-06 | Not provided; asked again in P07 (EV-SA-9) and carried into the P01 risk register (R-009) and POAM-012 |
| Who holds the oven modem credentials, and a record of OEM remote sessions | Drying oven OEM (through the Shop Manager) | 2026-07-09 | Not provided; carried into P01 R-003 and POAM-006 |
| Test set software media and license key | Shop Manager and test set vendor | 2026-07-09 | Not located; carried into the P05 BIA (test PC recovery) and P01 R-002 |
| What company or customer information staff have entered into public chatbots | Office Manager (staff survey follow-up) | 2026-07-09 | Not established at intake; P10 treats it as unknown |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Processes and owners (EV-001, EV-036, EV-038), receipts, cash and job volume (EV-022, EV-023), backup coverage (EV-014, EV-029), vendor recovery figures (EV-016, EV-017), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-003 to EV-016 and EV-029 |
| P04 Cloud mapping | SaaS components and the MSP-operated backup (EV-003 to EV-008, EV-014, EV-024) and provider documentation (EV-017, EV-018) |
| P01 Risk register | Likelihood inputs from the console and MSP exports, the contracts folders, the shop equipment records (EV-028 to EV-031), the walk-through (EV-034) and the intake interviews (EV-036 to EV-038) |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the CSF 2.0 benchmark and the binding clauses |
| P06 Policies | The document request response (EV-025) and the designation letter (EV-026) |
| P07 Control assessment | Populations to test from (EV-001, EV-003, EV-005, EV-009) |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register; the cooperative exhibit (EV-019) and the cyber policy (EV-027) |
| P09 SOC 2 | Vendor assurance on file (EV-017, EV-018) and the cooperative questionnaire (EV-020) |
| P10 AI governance | AI tools found (EV-004, EV-007, EV-008, EV-024, EV-039) |

The asset inventory in this folder is the assessment's list, built from the evidence above. It is not a shop-maintained inventory; the SSP (CM-8) plans one by 2026-10-31.
