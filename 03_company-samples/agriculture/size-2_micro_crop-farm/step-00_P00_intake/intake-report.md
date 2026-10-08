# Intake Report: Cris Santos Company | Agriculture, Forestry, Fishing and Hunting | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (precision-agriculture row crop and watermelon farm, about 420 acres in two parcels in North Florida) |
| Intake window | 2026-07-06 to 2026-07-17 |
| Collected by | Office Manager, with the MSP technician for the MSP exports and the Irrigation and Equipment Technician for SYS-01, the telematics portal and the pump station |
| Approved | Owner and General Manager, 2026-08-31 |

## 1. Purpose and scope
Intake collected the farm's own records before any assessment work began on 2026-07-20. It covers the organization, the systems that run irrigation and hold farm records and worker personal information, the suppliers that touch them, and the rules that may bind the farm. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, tests) to the same register, so one list backs every deliverable.

A 7-person farm has no HR system, CMDB or accounts payable vendor master. Its systems of record are the vendor admin consoles (SYS-01 and its irrigation module, the productivity suite, the telematics portal), the payroll service and the H-2A filing agent's portal, the MSP's exports and monthly report, the irrigation dealer's records, the contracts folder, the bank and card statements, and what can be seen at the shop and the pump station.

This report records **observations, not findings**. Whether an observation meets a requirement or the benchmark is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| People and payroll | EV-001, EV-002 | Payroll service; H-2A filing agent's portal | 2026-06-30 to 2026-07-06 |
| Farm systems and access | EV-003 to EV-008 | SYS-01 admin console and irrigation module; SYS-01 terms; productivity suite admin console | 2026-07-07 to 2026-07-08 |
| Office computers, network and backup | EV-009 to EV-016 | MSP device, policy, encryption and antivirus consoles; MSP monthly report; firewall management; backup console; MSP tickets | 2026-06-30 to 2026-07-08 |
| Suppliers and contracts | EV-017 to EV-024 | Contracts folder; dealer invoices and email; telematics portal; AI vendor account; bank and card statements; grower agreement | 2026-06-30 to 2026-07-14 |
| Assurance, insurance and programs | EV-025 to EV-029 | Food safety audit report; cyber policy; USDA and water use documents; FY2025 accounts; bank portal | 2025-12-31 to 2026-07-09 |
| Documents and records | EV-030 to EV-033 | Training records; HR checklists; document request; service agreements | 2026-06-30 to 2026-07-10 |
| Farm and people | EV-034 to EV-039 | Home Farm walk-through; Technician and Office Manager interviews; staff AI question; vendor documentation; engagement letter | 2026-07-06 to 2026-07-15 |

## 3. Observations by area
**People and payroll.** Payroll lists 7 active employees, including 2 H-2A seasonal workers from February 2026, and 1 termination from January to June 2026, a part-time bookkeeper who left in January 2026. Payroll runs weekly from the daily hours uploaded from SYS-01 (EV-001). The H-2A filing agent's portal holds the 2026 job order for 2 workers through July 2026, with passport and visa numbers, home-country addresses and earnings records for 3 seasons (EV-002).

**Farm systems and access.** SYS-01 has named staff accounts in 3 vendor roles and one shared "field crew" account used on the field tablet; the Owner and General Manager and the Technician hold the administrator role, and the crew role has no irrigation permissions (EV-003). MFA is enforced only on the Owner and General Manager's SYS-01 account; the audit trail records sign-ins, record edits and irrigation commands (EV-004). The irrigation module controls 5 pivots through the pivot manufacturer's connectivity service and receives data from 12 probes, 2 flow meters and a weather station; pivot change alerts are switched off (EV-005). SYS-01 keeps records for the subscription term; its export history shows no farm data export, and no SOC 2 report is on file (EV-006). The productivity suite has 5 named user accounts; MFA is enforced for 3 of them and not for the Field Supervisor's; automatic forwarding to outside addresses is allowed and there are no alert rules (EV-007). The Office folder holds payroll exports, H-2A passport and visa copies and USDA documents, is shared with all 4 current staff accounts, and is synced to the office desktop (EV-008).

**Office computers, network and backup.** The MSP device list shows 1 desktop and 2 laptops and nothing else (EV-009). Laptop users have no local administrator rights; the Office Manager has local administrator rights on the desktop; screens lock after 15 minutes (EV-010). The 2 laptops are encrypted and the desktop is not (EV-011). The MSP patches the 3 computers monthly; its services do not include scanning, endpoint detection and response, log review, or the tablets and phones (EV-012). Antivirus alerts go to the MSP help desk mailbox in business hours and not to the farm (EV-013). The firewall exposes no inbound services; the office desktop, the shop Wi-Fi and the bridge to the pump station share one network; the Wi-Fi password was last changed in 2022; there is no guest network; firewall logs are kept about 7 days (EV-014). The backup copies the mailboxes and the Office folder nightly with 30 days of versions, immutable retention off, one password-only MSP administrator account, and no restore jobs in its history (EV-015). MSP tickets show a replacement desktop in 2025 with no disposal record for the old one, and no restore tests (EV-016).

**Suppliers and contracts.** The MSP contract buys about 6 hours a month, with a 4-business-hour response time, no recovery commitment and no incident notice term (EV-017). The irrigation dealer works under a time-and-materials agreement with no response time or security terms, and set up the cellular gateway in the pump panel in 2019 (EV-018). Its invoices bill 9 remote sessions in 2026, none referencing a farm request (EV-019). The dealer states that the gateway is always on, that its technicians share one login without a second factor, and that the only copy of the controller program is on its service laptop (EV-020). The telematics portal ties operator sign-ins to machine location history and gives dealer technicians standing access, with no access or retention terms (EV-021). The yield prediction pilot started in April 2026 under click-through terms that allow the vendor to use farm imagery and yield data to improve its models; its account uses a password only (EV-022). The statements show 14 recurring suppliers and no generative AI tool charges (EV-023). The grower agreement requires 24-hour notice of events that affect product safety, traceability or committed loads, and its 2026 renewal adds a security and continuity questionnaire due 2026-10-15 (EV-024).

**Assurance, insurance and programs.** The farm passed the packer-shipper's third-party food safety audit in April 2026; it does not cover cybersecurity (EV-025). A cyber liability policy from 2025 has a breach hotline and panel vendors (EV-026). The farm holds crop insurance, FSA records, a 2025 NRCS cost-share agreement and a water use permit, and no federal procurement contract (EV-027). FY2025 receipts were about $1.1 million, about $9,000 per watermelon harvest day, sold almost entirely to the packer-shipper, the buying point and the cotton cooperative, with no card sales; credit and cash cover about 60 days of expenses (EV-028). The bank calls the Owner and General Manager back before adding a payee (EV-029).

**Documents and records.** Training records show Produce Safety training at hire in English and Spanish and no security training (EV-030). The HR checklists cover payroll, I-9 and H-2A paperwork only (EV-031). The request for policies, a risk assessment, a written security owner, an incident response plan, a manual irrigation procedure, an inventory, a retention schedule, an approved AI tools list, log review records and an incident log returned none (EV-032). There is one fixed-wireless internet line with no failover; pivots, probes, the gateway and phones use cellular service (EV-033).

**Farm and people.** The Home Farm walk-through counted 8 IT devices and the pump station equipment, found Hand-Off-Auto switches on every pump and Home Farm pivot, a locked office and a padlocked pump station panel, and a touchscreen PIN that matches the manual's default (EV-034). The Technician is the only person who has run irrigation by hand, and the steps are not written; the tablets and phones are not managed (EV-035). The Office Manager adds and removes accounts when remembered, names where personal information is held, and says nobody reviews logs (EV-036). The only AI tools named by staff are the yield pilot and the Office Manager's occasional use of public chatbots for letters (EV-037). The SaaS vendors describe encryption at rest and in transit (EV-038). The Owner and General Manager engaged the 2026 assessments (EV-039).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| FMIS vendor SOC 2 Type 2 report | FMIS vendor | None on file at intake (EV-006); first requested 2026-08-03 with the P07 evidence request | Received 2026-08-18 (EV-052); reviewed in P09 on 2026-08-20 |
| Copy of the current pump station controller program | Irrigation dealer | Intake request (dealer reply 2026-07-10, EV-020); asked again 2026-08-03 | Not received by the end of P07 fieldwork; the dealer agreed to hand it over by 2026-09-30 (POAM-003) |
| List of MSP technicians with access and evidence of MFA on the remote management tool | MSP technician | Intake request; asked again 2026-08-03 | Statement only (EV-041; EV-SA-9); carried into P01 R-021 and POAM-010 |
| What the Office Manager has entered into public chatbots | Office Manager | 2026-07-16 | Her statement only (EV-037); no chatbot histories reviewed. P10 records it as not established from records |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Processes and owners (EV-001, EV-035, EV-036), receipts, harvest-day value and cash (EV-028), the grower agreement's notice term (EV-024), backup settings (EV-015), the MSP and dealer terms (EV-017, EV-018, EV-020), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-003 to EV-021 |
| P04 Cloud mapping | SaaS components and the MSP-operated backup (EV-003 to EV-008, EV-015, EV-021 to EV-023) and provider documentation (EV-038) |
| P01 Risk register | Likelihood inputs from the console, MSP and dealer records, the contracts folder, the walk-through (EV-034) and the intake interviews (EV-035, EV-036) |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with CSF 2.0 and the binding record rules |
| P06 Policies | The document request (EV-032) and the HR checklists (EV-031) |
| P07 Control assessment | Populations to test from (EV-001, EV-003, EV-007, EV-009, EV-015, EV-021) |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register; the cyber policy (EV-026) and the grower agreement (EV-024) |
| P09 SOC 2 | The grower questionnaire (EV-024), the food safety audit (EV-025) and the vendor documentation (EV-038); the FMIS vendor report arrived later (EV-052) |
| P10 AI governance | AI tools found (EV-022, EV-023, EV-037) |

The asset inventory in this folder is the assessment's list, built from the evidence above. It is not a farm-maintained inventory; the SSP (CM-8) plans one by 2026-10-31.
