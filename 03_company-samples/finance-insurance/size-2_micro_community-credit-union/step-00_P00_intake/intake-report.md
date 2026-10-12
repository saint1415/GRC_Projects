# Intake Report: Cris Santos Company | Finance and Insurance | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Community Federal Credit Union (member-owned federal credit union, one Florida office) |
| Intake window | 2026-06-29 to 2026-07-10 |
| Collected by | Operations Manager (Information Security Officer), with the MSP lead technician for the MSP exports |
| Approved | President and CEO, 2026-08-31 |

## 1. Purpose and scope
Intake collected the credit union's own records before any assessment work began on 2026-07-13. It covers the organization, the systems that hold or reach member information, the suppliers that touch them, and the rules that may bind the credit union. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, samples, tests) to the same register, so one list backs every deliverable.

A 7-person credit union has no HR system, CMDB or internal audit function. Its systems of record are the core processor's user administration and reports, the online banking admin console, the corporate credit union's wire portal, the productivity suite and MSP consoles, the MSP's monthly report and tickets, the payroll service, the board minutes and policy binder, the contracts and SOC report folder, and NCUA filing records.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| People and access | EV-001 to EV-007 | Payroll service; core user administration and reports; online banking admin console; wire portal; productivity suite admin console; Operations Manager interview | 2026-06-30 to 2026-07-08 |
| Devices, network and cloud | EV-008 to EV-015 | MSP device, policy, encryption and antivirus consoles; MSP monthly report; firewall documentation; cloud account export; MSP email and tickets | 2026-06-30 to 2026-07-03 |
| Program documents and records | EV-016 to EV-027 | Policy binder; board minutes; NCUA examination and filing records; management shared folder; HR files; document request list; website | 2019-01-01 to 2026-07-07 |
| Suppliers and contracts | EV-028 to EV-039 | Contracts folder; SOC report folder; vendor portals; LOS admin console; general ledger; Supervisory Committee files | 2019-07-01 to 2026-07-08 |
| Office and records | EV-040 to EV-043 | Key log, alarm contract and cameras; shredding certificates; SAR log; core procedures | 2026-06-30 to 2026-07-08 |
| Business volume | EV-044, EV-045 | Core general ledger; core, admin console, wire portal and LOS reports | 2025-12-31 to 2026-06-30 |
| AI tools | EV-046 | Staff survey | 2026-07-08 |

## 3. Observations by area
**People and access.** Payroll lists 7 active employees and 1 termination from January to June 2026, an MSR whose last working day was 2026-03-13 (EV-001). The core has named accounts in 4 role profiles; all 3 MSRs hold the supervisor override profile. Core sign-in is allowed only from the office's fixed IP address, and the core offers no MFA option for teller users (EV-002). The core's exception reports are printed and filed with no reviewer sign-off (EV-003). The online banking admin console has 5 staff users, all with MFA. Members sign in with a password and get a text code only when they register a new device, and member alerts for changes to email, phone and payees are turned off (EV-004). The wire portal has 1 maker and 2 approvers, each with a hardware token, and every outgoing wire needs a second user's approval (EV-005). The productivity suite has named accounts with MFA. The Member Services mailbox is a licensed user account from 2018, excluded from MFA and signed into with a password that has not changed since before the March 2026 departure; it holds about 3 years of email. Suite sign-in logs are kept for less than one year, no alert rules are set, and no rule encrypts outside mail (EV-006). The Operations Manager states that accounts are requested verbally, that the 3 MSRs and the Operations Manager share the mailbox password, that the mailbox receives loan documents, ID copies and wire request forms, that nobody reviews system logs or reports, and that a 2025 online banking takeover after a phone number change was refunded with no written record (EV-007).

**Devices, network and cloud.** The MSP device list shows 8 desktops, 3 laptops and 2 check scanners, and the MSP agent on the imaging server; it lists no SaaS services or member information locations (EV-008). The 3 laptops report full-disk encryption; the 8 desktops do not. Staff have no local administrator rights, and the 4 teller stations are exempted from the 10-minute screen lock (EV-009). The MSP's June report shows monthly patching of the endpoints and the imaging server, and lists no vulnerability scanning, endpoint detection and response, or restore tests (EV-010). Antivirus alerts go to the MSP help desk in business hours and not to the credit union (EV-011). The firewall exposes no inbound services, guest Wi-Fi is separate, and the VoIP phones share the office's internet line (EV-012). The imaging server sits in a cloud account held in the MSP's name, with daily snapshots kept 14 days in the same account and one administrator login with no MFA registered; the credit union has no login (EV-013). The MSP states that two technicians use that login and that no snapshot has ever been restored (EV-014). MSP tickets show 2 desktops retired in 2024 with no wipe or destruction record, changes made with no recorded approval by the credit union, and no restore or continuity tests (EV-015).

**Program documents and records.** The program and policy manual is a 2019 trade association template with no revision since 2019 (EV-016). Board minutes show no re-approval since 2019, no information security report to the board since 2022, and no written ISO designation (EV-017). The last risk assessment is a 2019 template questionnaire with no likelihood or impact ratings (EV-018), and the 2025 NCUA examination recommended updating it (EV-019). The President and CEO filed the Part 748 certification each year, most recently in January 2026 (EV-020). The 2019 incident response plan has no step for an NCUA report or member notice (EV-021). The 2019 continuity plan has no test record and no catastrophic act report step, and the vital records log dates from 2019 (EV-022). The 2019 wire procedure names makers and approvers and has no callback step (EV-023). Training records show annual BSA training and a security video at hire only (EV-024). The document request for access reviews, log reviews, restore and continuity tests, an incident log, computer disposal records, change approvals, and a validation or fair lending review of the AI add-on returned none (EV-025). The handbook and privacy notice are on file (EV-026, EV-027).

**Suppliers and contracts.** The core processing contract renews 2027-06-30 and sets no time frame for incident notice (EV-028). The core processor's SOC 1 Type 2 and SOC 2 Type 2 reports cover the 12 months ending 2026-03-31 and state an RTO of 8 hours and an RPO of 15 minutes; the folder has no review notes (EV-029). The digital banking provider's SOC 2 Type 2 report states an RTO of 4 hours and an RPO of 15 minutes, also with no review notes (EV-030). The card processor authorizes in stand-in mode when the core is down (EV-031). The corporate credit union offers a phone-initiated wire with a PIN as the alternate procedure (EV-032). The MSP contract has a 4-business-hour response time, no recovery time commitment and no incident notice time frame (EV-033). The LOS vendor switched on the AI credit scoring add-on on 2026-04-06 at the Lending Manager's request; it approves applications above the cutoff automatically, and its terms allow the vendor to use de-identified application data (EV-034). One internet line carries data and phones (EV-035). The cyber policy has a $100,000 social engineering sublimit and renews on 2026-11-01 (EV-036). The accounts payable list shows recurring payments to the suppliers in the vendor register, including an AI scoring add-on fee from April 2026, and no other AI tool charges (EV-037). Vendors describe encryption at rest and TLS in transit (EV-038). The supervisory committee audit is a financial statement audit (EV-039).

**Office and records.** Two people hold office keys, an alarm contract is in force, and camera recordings are kept 90 days (EV-040). Paper shredding has certificates; computers and drives have none (EV-041). SARs are filed from the core's BSA alerts (EV-042). Offline teller mode works from a nightly balance file on the wire and new-accounts desk (EV-043).

**Business volume.** Total assets were $60.0 million and net revenue about $1.1 million in FY2025, about $4,400 per business day (EV-044). There are about 6,400 members, about 3,900 online banking users, about 60 lobby and drive-up transactions a day, and about 25 outgoing wires a month averaging about $38,000 (EV-045).

**AI tools.** The staff survey names the LOS AI scoring add-on and mentions public chatbots used to draft letters (EV-046). The online banking fraud scoring appears in the admin console (EV-004).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Number of staff using public chatbots, and what they enter | Operations Manager (staff survey follow-up) | 2026-07-09 | Not established at intake; P10 treats it as unknown |
| MSP technician list and evidence of MFA on the remote management platform | MSP lead technician | 2026-07-03 | Not provided; asked again for P07 on 2026-07-28 (EV-SA-9) and carried into the P01 risk register (R-014) and POAM-013 |
| LOS vendor SOC 2 report | LOS vendor | 2026-07-02 | Not received; noted in P10 |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Processes and owners (EV-001), revenue and volumes (EV-044, EV-045), vendor recovery figures (EV-029, EV-030, EV-033), offline teller mode and the alternate wire (EV-043, EV-032), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-002 to EV-015 |
| P04 Cloud mapping | SaaS and vendor-hosted components and the MSP-operated imaging server (EV-004 to EV-006, EV-013, EV-037) and provider assurance (EV-029, EV-030, EV-038) |
| P01 Risk register | Likelihood inputs from the console and MSP exports, the contracts and SOC report folder, and the Operations Manager interview (EV-007) |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with Part 748 and its appendices |
| P06 Policies | The 2019 manual and plans (EV-016, EV-021 to EV-023) and the board minutes (EV-017) |
| P07 Control assessment | Populations to test from (EV-001, EV-002, EV-004 to EV-006) |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register; the insurance policies (EV-036) |
| P09 SOC 2 | Vendor assurance on file (EV-029, EV-030) and the cyber insurer's renewal questionnaire (EV-036) |
| P10 AI governance | AI tools found (EV-004, EV-034, EV-037, EV-046) |

The asset inventory in this folder is the assessment's list, built from the evidence above. It is not a credit union-maintained inventory; P03 plans an inventory of member information locations by 2026-11-30.
