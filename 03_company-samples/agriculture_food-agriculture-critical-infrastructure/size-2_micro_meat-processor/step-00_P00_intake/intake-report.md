# Intake Report: Cris Santos Company | Food and Agriculture | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (USDA-inspected sausage and smoked meats plant, one Florida plant) |
| Intake window | 2026-07-06 to 2026-07-17 |
| Collected by | Office Manager, with the MSP lead technician for the MSP exports and the Maintenance and Sanitation Technician for the plant equipment |
| Approved | Owner and General Manager, 2026-08-31 |

## 1. Purpose and scope
Intake collected the company's own records before any assessment work began on 2026-07-20. It covers the organization, the plant machines and office systems that make and record its food, the suppliers that run or reach them, and the rules that may bind the company. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, record samples, tests) to the same register, so one list backs every deliverable.

A 7-person plant has no HR system, CMDB or accounts payable vendor master. Its systems of record are the vendor admin consoles (productivity suite, accounting service, records app, cold-chain dashboard), the payroll service, the smokehouse controller and its manufacturer's portal, the MSP's exports and monthly report, the food safety binder and the FSIS establishment file, the contracts folder, the inspection and calibration records, the card statements, and what can be seen on a walk-through of the plant.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| People and access | EV-001 to EV-007 | Payroll service; productivity suite, accounting, records app and cold-chain admin consoles | 2026-06-30 to 2026-07-08 |
| Plant equipment and remote access | EV-008 to EV-012 | Smokehouse controller and manufacturer portal; labeling PC; equipment files and maintenance log; contracts folder | 2026-06-15 to 2026-07-09 |
| Office IT run by the MSP | EV-013 to EV-020 | MSP device, policy and antivirus consoles; MSP monthly report; firewall documentation; backup console; MSP tickets; MSP contract | 2026-06-30 to 2026-07-09 |
| Suppliers and contracts | EV-021 to EV-025 | Contracts folder; card statements and vendor invoices; carrier invoices | 2026-06-30 to 2026-07-09 |
| Food safety program records | EV-026 to EV-032 | FSIS establishment file; food safety binder (HACCP plans, reassessment and validation files, SSOPs, recall procedure, training certificates); calibration records | 2026-06-30 to 2026-07-09 |
| Documents, interviews and walk-through | EV-033 to EV-038 | Document request; intake interviews; plant walk-through; alarm contract and visitor log | 2026-07-10 to 2026-07-14 |
| Business volume and customers | EV-039 to EV-042 | Accounting service reports; email inbox | 2025-12-31 to 2026-07-08 |
| AI tools and vendor documentation | EV-043, EV-044 | Staff question; vendor websites and portals | 2026-07-10 to 2026-07-15 |

## 3. Observations by area
**People and access.** Payroll lists 7 active employees and 1 termination from January to June 2026, a production worker who left in March 2026; the payroll service holds records for about 30 current and former employees (EV-001). The productivity suite has 4 named mailboxes with MFA and a shared "plant" mailbox without MFA; the leaver's account was disabled on his last day (EV-002). One shared folder holds the HACCP plans, SSOPs, recall procedure, formulations and HR files, and every suite account can open it (EV-003). The accounting service has 3 named users with MFA and holds the invoices with lot numbers (EV-004). The records app has one shared floor login with typed initials, and its administrator is the vendor-issued default account used by the owner and the Office Manager (EV-005). The cold-chain dashboard sends excursion alerts by text to the Production Supervisor only, has no alert for the gateway going offline, and lists two named accounts, a shared login used by the delivery driver and the leaver's login (EV-006). The gateway went offline 3 times between February and July 2026 with no notification (EV-007).

**Plant equipment and remote access.** The smokehouse controller stores cycles only on the device, keeps 90 days of temperature logs, does not record who changes a cycle, and uses one shared operator PIN. Its remote service module connects to the manufacturer's portal all the time, and the portal has one shared login with MFA not turned on (EV-008). The labeling PC uses one shared production login with administrator rights, runs the packaging vendor's unattended remote desktop tool with a static password, and saves cook-log exports as editable spreadsheets (EV-009). The stuffer HMI dates from 2016 and its vendor states that its operating system is no longer supported; machine settings and recipes have no copies on file; the old packaging controller left in June 2026 with no disposal record (EV-010). The packaging machine's AI camera was turned on at commissioning on 2026-06-15 with automatic uploads and model updates, and the purchase order has no data-use, change-notice or security terms (EV-011). No equipment or SaaS contract has security or incident notice terms, and no vendor SOC 2 report is on file (EV-012).

**Office IT run by the MSP.** The MSP device list has 3 PCs and nothing else (EV-013). The labeling PC is excluded from the screen lock; the owner laptop reports encryption (EV-014). The MSP patches the 3 PCs monthly; its services do not include scanning, endpoint detection and response, or plant equipment (EV-015). Antivirus alerts go to the MSP queue in business hours (EV-016). The firewall blocks unsolicited inbound traffic and allows any outbound connection; one network carries the office computers, plant equipment, the gateway and staff Wi-Fi, with guest Wi-Fi separate; logs are kept 7 days; the firewall management login uses a password only (EV-017). The backup copies the office desktop, the labeling PC and the suite nightly with 30 days of versions, immutable retention off, one MSP administrator login with a password only, and no restore jobs; machine settings are not in any backup set (EV-018). MSP tickets show wipes of retired office computers and no restore tests (EV-019). The MSP contract has a next-business-day response, no recovery time commitment, no incident notice term, and excludes the plant machines (EV-020).

**Suppliers and contracts.** The refrigeration contractor has a 4-hour emergency response, and the refrigeration equipment uses a halocarbon refrigerant with no ammonia (EV-021). The cyber policy bought in 2025 has a 24x7 breach hotline and panel vendors (EV-022). The card terminal is managed by its provider on a cellular link (EV-023). The card statements show 11 recurring suppliers and no AI tool subscriptions (EV-024). There is one internet line and no failover (EV-025).

**Food safety program records.** The plant is an FSIS official establishment with no FDA registration and no open noncompliance records (EV-026). The three HACCP plans were signed at the January 2026 reassessment; the fully cooked plan was modified in March 2026 without a new signature; the flow charts show the old packaging machine; the plans do not describe monitoring when the controller log, the probe or the cold-chain service is unavailable (EV-027). Validation files date from 2019, and no reassessment record exists for the 2025 and 2026 equipment and cycle changes (EV-028). The SSOPs were signed in 2024; the March 2026 update for the records app has no new signature and the new packager's cleaning steps are not in it (EV-029). The 2019 recall procedure refers to a paper invoice book no longer used (EV-030). The owner and the Production Supervisor hold HACCP course certificates from 2019 (EV-031). Handheld thermometers are calibrated weekly; the wireless chilling probe has only its factory certificate (EV-032).

**Documents, interviews and walk-through.** The request for security policies, a risk assessment, an incident response or contingency plan, a manual temperature log procedure, training records, an incident log, an inventory, vendor reviews and a disposal record returned none, and no security lead was designated in writing (EV-033). The owner states that the company is privately held, makes only meat products, sells only in Florida, has no federal contracts and has never submitted information to DHS (EV-034). The Office Manager states that shared passwords and the smokehouse PIN were not changed after the March 2026 departure, that payroll exports are saved to the office desktop, that a 2025 request to change a supplier's bank details was stopped by a call-back and not shared with staff, that she uses public chatbots to draft customer emails, and that staff have had no security training (EV-035). The Production Supervisor and the Maintenance and Sanitation Technician state that cycle, formulation and label template changes are made by whoever has the PIN or login with no record or second check, and that the AI camera has run beside the first-label check with no written test plan (EV-036). The walk-through counted the plant machines, PCs, tablets, phones and sensors, saw the remote desktop password written at the labeling PC, and confirmed keyed doors, an alarm and a locked office (EV-037). The alarm is monitored and visitors sign in (EV-038).

**Business volume and customers.** Sales were about $1.1 million across 250 production days in FY2025, about $4,400 per production day (EV-039). There are about 40 wholesale accounts, all in Florida, including a 12-store grocery chain since May 2026; wholesale deliveries are about $16,500 a week and the retail counter about $1,100 a day (EV-040). Cold storage holds $25,000 to $40,000 of product and raw material (EV-041). The grocery chain's security questionnaire is due 2026-09-30 (EV-042).

**AI tools and vendor documentation.** Staff named the AI camera, the cold-chain anomaly alerts and the Office Manager's use of public chatbots (EV-043). The vendors describe TLS and encryption at rest, sensor buffering during gateway outages, and the anomaly alert feature being on by default (EV-044).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Cold-chain monitoring vendor SOC 2 report | Cold-chain vendor | None on file at intake (EV-012) | Obtained and reviewed 2026-08-20 for P09 (EV-051) |
| Records app vendor SOC 2 report or security summary | Records app vendor | Not requested at intake (EV-012) | Carried into P01 R-018 (request by 2026-11-30) |
| MSP technician list and evidence of MFA on the remote management platform | MSP lead technician | Intake request; asked again 2026-08-03 | Statement only (EV-046); list and MFA statement received 2026-08-12 (EV-SA-9); carried into POAM-011 |
| Packaging vendor's remote access practices | Packaging machine vendor | Asked again in P07 | Not answered by the end of P07 fieldwork (EV-AC-17); carried into POAM-002 |
| What has been entered into public chatbots | Office Manager | 2026-07-16 | Not established from records (EV-043); P10 treats it as unknown |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Processes and owners (EV-001, EV-036), sales, delivery volume and inventory value (EV-039 to EV-041), backup settings (EV-018), the MSP and refrigeration contractor terms (EV-020, EV-021), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-002 to EV-020 |
| P04 Cloud mapping | SaaS components and the MSP-operated backup (EV-002 to EV-006, EV-018, EV-024) and provider documentation (EV-044) |
| P01 Risk register | Likelihood inputs from the console, controller and MSP exports, the contracts folder, the walk-through (EV-037) and the intake interviews (EV-034 to EV-036) |
| P03 Gap analysis | The obligations register (which rules apply), the food safety program records (EV-026 to EV-032) and every observation above, compared with the FSIS rules and the CSF 2.0 benchmark |
| P06 Policies | The document request (EV-033) |
| P07 Control assessment | Populations to test from (EV-001, EV-002, EV-004 to EV-006, EV-013) |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register; the cyber policy (EV-022), the recall procedure (EV-030) and the grocery chain agreement (EV-042) |
| P09 SOC 2 | The grocery chain questionnaire (EV-042) and the vendor documentation (EV-044); the cold-chain vendor report arrived later (EV-051) |
| P10 AI governance | AI tools found (EV-011, EV-036, EV-043, EV-044) |

The asset inventory in this folder is the assessment's list, built from the evidence above. It is not a company-maintained inventory; the SSP (CM-8) plans one by 2026-10-31.
