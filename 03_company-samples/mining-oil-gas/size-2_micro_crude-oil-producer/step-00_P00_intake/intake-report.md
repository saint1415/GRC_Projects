# Intake Report: Cris Santos Company | Mining, Quarrying, and Oil and Gas Extraction | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent crude oil producer, one onshore field in the Florida Panhandle) |
| Intake window | 2026-07-06 to 2026-07-17 |
| Collected by | Office Manager, with the MSP lead technician for the MSP exports and the Field Technician for the SCADA host screenshots |
| Approved | Owner, 2026-08-31 |

## 1. Purpose and scope
Intake collected the company's own records before any assessment work began on 2026-07-20. It covers the organization, the field control system and office systems that hold well control data and personal information, the suppliers that touch them, and the rules that may bind the company. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, walkthroughs, tests) to the same register, so one list backs every deliverable.

A 7-person producer has no HR system, CMDB or accounts payable vendor master. Its systems of record are the vendor admin consoles (productivity suite, production accounting, SCADA vendor portal, bank portal), the payroll service, the MSP's exports and monthly report, screenshots taken on the SCADA host, the integrator's 2019 drawings, the contracts folder, the card statements, the field office binder, and what can be seen at the offices and field sites.

This report records **observations, not findings**. Whether an observation meets the benchmark is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| People and access | EV-001 to EV-008 | Payroll service; HR files; suite, production accounting, bank and SCADA vendor consoles; SCADA HMI user manager | 2026-03-13 to 2026-07-10 |
| Devices, network and backup | EV-009 to EV-015 | MSP device, policy, encryption, mobile device and antivirus consoles; MSP monthly report; main-office firewall; backup console | 2026-06-30 to 2026-07-08 |
| Field systems | EV-016 to EV-022 | SCADA host screenshots; remote access tool inventory; integrator drawings; field office router; integrator email | 2019-09-30 to 2026-07-10 |
| Suppliers and contracts | EV-023 to EV-031 | Contracts folder; SCADA vendor portal; accounting records and card statements | 2019-05-01 to 2026-07-09 |
| Business volume and owners | EV-032 to EV-034 | Production accounting reports; outside accountant | 2025-12-31 to 2026-06-30 |
| Documents and records | EV-035 to EV-039 | Email inbox; document request list; field office binder; Owner's files | 2025-03-01 to 2026-07-09 |
| Field operations and premises | EV-040 to EV-042 | Route sheets; key list; walk-through | 2026-06-30 to 2026-07-14 |
| Interviews, survey and vendor documentation | EV-043 to EV-046 | Field and office interviews; staff questionnaire; vendor websites | 2026-07-10 to 2026-07-15 |

## 3. Observations by area
**People and access.** Payroll lists 7 employees and 1 termination from January to June 2026, a Lease Operator whose last day was 2026-03-13 (EV-001). His termination record lists only the email asking the MSP to disable the suite account, and the return of his phone, keys and truck (EV-002). The suite has 7 staff accounts and 1 MSP administrator, all with MFA enforced, and sign-in alerts with no review record (EV-003). The Geology folder, holding licensed seismic data and reservoir interpretations, is shared with all 7 staff (EV-004). Production accounting requires MFA; the Production Accountant is its administrator, and owner bank detail changes cite emailed requests with no call-back note (EV-005). The bank portal requires MFA and the Owner's approval of every ACH batch (EV-006). The SCADA mobile viewer has individual accounts with MFA available and not enabled (EV-007). The HMI has one shared operator login, last changed in 2019, plus an administrator and a shared integrator login (EV-008).

**Devices, network and backup.** The MSP manages 6 computers; the engineering laptop, the SCADA host and the field equipment are not in its list (EV-009). Staff have no local administrator rights and screens lock after 10 minutes (EV-010). The 4 managed laptops are encrypted, the shared field desktop is not, and the 5 smartphones are enrolled in mobile device management (EV-011). The MSP's June report shows monthly patching and antivirus, and its services do not include the SCADA host, the field office network, vulnerability scanning, or endpoint detection and response (EV-012). Antivirus alerts reach the MSP help desk in business hours (EV-013). The main-office firewall publishes no inbound services and separates guest Wi-Fi (EV-014). The cloud backup copies the 4 main-office computers and the shared drive nightly with 30 days of versions, immutable retention off, one MSP administrator, and no restore jobs; the field computers and SCADA host are not in it (EV-015).

**Field systems.** The SCADA host's last operating system update is from 2024, its antivirus definitions are updated by hand, and a USB backup drive is attached (EV-016). The drive receives a SCADA backup each Friday and is the only copy (EV-017). The host's event logs overwrite at their default size (EV-018). The integrator's remote tool runs at all times with one shared account, no MFA and no session log, and the shared field desktop has a saved remote desktop shortcut to the host (EV-019). The 2019 drawings show 16 pump-off controllers, 2 PLCs, a licensed 900 MHz radio network with 15 remote radios, 3 cellular modems, and safety shutdowns wired at each site independent of SCADA; they include no field office network drawing and no firmware versions (EV-020). The field office router puts the SCADA host, field PCs and Wi-Fi on one network with one Wi-Fi password (EV-021). The integrator confirms the host operating system is past end of support and estimates 2 to 3 days to rebuild without a good backup (EV-022).

**Suppliers and contracts.** The MSP contract has a 4-business-hour response time, no recovery time commitment, and does not cover the SCADA host or field office network (EV-023). The integrator agreement and the SCADA vendor terms contain no security terms; the vendor terms allow aggregated use of customer data (EV-024, EV-025). The Owner accepted a 6-month trial of the vendor's predictive maintenance add-on for 8 wells in May 2026 with no review record (EV-026). The production accounting agreement has no breach notice term, and the vendor's SOC 2 report was not on file (EV-027). Card statements show the recurring suppliers and 2 spare pump-off controllers bought from an online seller in 2025 (EV-028). The cyber policy has ransomware coverage and panel vendors; its application answered yes to MFA on remote access and offline backups (EV-029). The seismic license limits access to named users and renews 2026-12-31 (EV-030). The company operates for 2 non-operating partners, and crude is sold at the lease into the purchaser's trucks (EV-031).

**Business volume and owners.** About 140 royalty owners are paid monthly, about 90 in Florida (EV-032). The field produces about 55 barrels of oil and 1,400 barrels of produced water per day, and associated gas is used as lease fuel (EV-033). FY2025 revenue was about $1.1 million, about $3,000 per day net, with about 60 days of cash (EV-034).

**Documents and records.** The larger partner's security questionnaire is due 2026-09-30 (EV-035). The request for policies, an incident response plan, a cyber contingency plan, an OT inventory, a network drawing, an incident log, training records and a prior cybersecurity risk analysis returned none (EV-036). The emergency response plan covers spills, fire, H2S and hurricanes, with manual operations and shut-ins, and has no cyber section (EV-037). The 2026 business plan states the mission (EV-038). Staff receive occasional MSP tip emails (EV-039).

**Field operations and premises.** Lease Operators visit every well daily and share the after-hours on-call rotation (EV-040). The gate code record shows no change since before the March departure (EV-041). The walk-through counted 7 computers and 5 smartphones, found a 30-minute UPS and no generator at the field office, one internet line there, and fenced, locked facilities with padlocked controller cabinets (EV-042).

**Interviews, survey and vendor documentation.** The field interview found shared passwords unchanged, controller programs only on the unmanaged engineering laptop, no restore ever tried and no field security training (EV-043). The office interview found departures handled by suite access only, owner exports emailed and saved on laptops, bank changes accepted by email, and no log review (EV-044). Staff mention public chatbots used for drafting (EV-045). The suite and backup vendors describe encryption at rest and in transit (EV-046).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Number of staff using public chatbots, and what they enter | Office Manager (questionnaire follow-up) | 2026-07-16 | Not established at intake; P10 treats it as unknown |
| MSP technician list and evidence of MFA on the remote management platform | MSP lead technician | 2026-07-09 | Not provided; asked again in P07 (EV-SA-9) and carried into POAM-013 |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Processes and owners (EV-001, EV-040), production, revenue and cash (EV-033, EV-034), royalty owners (EV-032), SCADA and office backups (EV-015, EV-017), vendor recovery terms (EV-022, EV-023), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-003 to EV-021 |
| P04 Cloud mapping | SaaS components and the MSP-operated backup (EV-003 to EV-007, EV-015, EV-025) and provider documentation (EV-046) |
| P01 Risk register | Likelihood inputs from the console and MSP exports, the SCADA host screenshots, the contracts folder, the walk-through (EV-042) and the interviews (EV-043, EV-044) |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the benchmark |
| P06 Policies | The document request response (EV-036) and the emergency response plan (EV-037) |
| P07 Control assessment | Populations to test from (EV-001, EV-002, EV-003, EV-005, EV-007, EV-008, EV-009) |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register; the cyber policy (EV-029) and the emergency response plan (EV-037) |
| P09 SOC 2 | The partner questionnaire (EV-035), the seismic license (EV-030), and vendor assurance (EV-027, EV-046) |
| P10 AI governance | AI tools found (EV-026, EV-045) |

The asset inventory in this folder is the assessment's list, built from the evidence above. It is not a company-maintained inventory; the SSP plans an OT inventory (CM-8) by 2026-11-30.
