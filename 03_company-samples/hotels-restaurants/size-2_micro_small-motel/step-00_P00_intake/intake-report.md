# Intake Report: Cris Santos Company | Accommodation and Food Services | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent 38-unit roadside motel, Florida) |
| Intake window | 2026-07-01 to 2026-07-10 |
| Collected by | Assistant Manager (Security and Privacy Lead), with the MSP lead technician for the MSP exports |
| Approved | Owner-Manager, 2026-08-31 |

## 1. Purpose and scope
Intake collected the motel's own records before any assessment work began on 2026-07-13. It covers the organization, the systems that store, process or transmit card data and guest personal information, the suppliers that touch them, and the rules that may bind the motel. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, scans, tests) to the same register, so one list backs every deliverable.

A 7-person motel has no HR system, CMDB or accounts payable vendor master. Its systems of record are the vendor admin consoles (PMS, gateway merchant portal, productivity suite, pricing tool, door lock software), the payroll service and the accounting SaaS, the MSP's exports and monthly report, the acquirer's portal and letters, the contracts folder, and the Owner-Manager's inbox.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the regulatory analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| People and access | EV-001 to EV-006 | Payroll service; PMS and productivity suite admin consoles | 2026-06-30 to 2026-07-02 |
| Payments | EV-007, EV-008, EV-018 to EV-020, EV-040 | Gateway merchant portal; merchant agreement; acquirer letter and portal; folio and receipt sample | 2026-05-11 to 2026-07-07 |
| Devices, network and backup | EV-009 to EV-016 | MSP device, policy, encryption and antivirus consoles; MSP monthly report; MSP network documentation; backup console; MSP tickets | 2026-06-30 to 2026-07-01 |
| Documents and records | EV-017, EV-021 to EV-023, EV-037 to EV-039 | Contracts folder; document request; Owner-Manager's files; HR files | 2026-07-01 to 2026-07-06 |
| Suppliers and business volume | EV-024 to EV-029, EV-041 | Accounting SaaS; payroll and accounting admin pages; PMS reporting; PMS vendor portal; vendor websites; contracts folder | 2025-12-31 to 2026-07-07 |
| Rates, website and pricing | EV-030 to EV-032 | PMS admin console; website and phone script; pricing tool admin page | 2026-07-02 to 2026-07-06 |
| AI tools and customers | EV-033 to EV-036 | Owner-Manager's inbox; staff question; crew account files | 2026-07-06 to 2026-07-08 |
| Lock system and interviews | EV-042 to EV-044 | Door lock software; Assistant Manager and Owner-Manager interviews | 2026-07-07 to 2026-07-08 |

## 3. Observations by area
**People and access.** Payroll lists 7 active employees, all in Florida, and 3 departures since January 2024, 2 of them in 2026 (March and May) (EV-001). The PMS has named accounts in 3 roles. The 2 administrators sign in with an authenticator app; front office and housekeeping users sign in with a password only. The front office role includes the "view full card number" permission (EV-002). The PMS minimum password length is 8 characters, the activity log records card number displays and exports, the feature that charges virtual cards without display is off, and the purge settings are off (EV-003). The PMS-to-lock and PMS-to-pricing-tool interface credentials show no change since installation (EV-004). The suite has 2 named mailboxes with MFA and a shared front desk mailbox signed in with one password, no MFA, last changed in 2024 (EV-005). A folder in the shared mailbox holds emails since 2021 whose subjects and attachments show crew card authorization forms; their contents were not opened at intake (EV-006).

**Payments.** The gateway portal shows 2 terminals in the gateway's P2PE solution since 2024, virtual terminal and pay-by-link available and not used, pay-by-link included in the plan, and 2 portal users, the Owner-Manager with MFA and the Assistant Manager without (EV-007). The gateway counted about 13,800 transactions in 12 months: about 7,600 card-present, about 2,400 keyed card-not-present, about 2,100 OTA virtual cards and about 1,700 booking engine prepayments (EV-008). The merchant agreement requires PCI DSS compliance, yearly validation and notice within 24 hours of a suspected compromise (EV-018). The acquirer's notice of 2026-05-11 asks the motel to confirm SAQ eligibility because of keyed card-not-present transactions (EV-019). A 2025 SAQ P2PE was submitted in December 2025 with every requirement answered "In Place"; the acquirer portal shows no ASV scans (EV-020). Receipts and folios show the last 4 digits only (EV-040).

**Devices, network and backup.** The MSP device list shows 3 PCs built from its standard image and no terminals, tablets, network devices, recorder, encoder or SaaS services. The back office PC runs the lock software and database and the lock vendor's remote support tool, set to start automatically (EV-009). The front desk PC uses one shared Windows account with automatic sign-in and no screen lock; staff have no local administrator rights and USB storage is blocked (EV-010). Disk encryption is reported on the laptop only (EV-011). The MSP's June report shows monthly patching and current antivirus (EV-012). Antivirus alerts go to the MSP help desk queue in business hours, and no endpoint detection and response agent is installed (EV-013). One office network holds the PCs, terminals, printer, CCTV recorder and staff Wi-Fi; guest Wi-Fi is a separate network with client isolation; the staff Wi-Fi passphrase dates from 2023; the firewall keeps about 7 days of logs (EV-014). The backup copies the back office PC and the suite nightly with 30 days of versions, immutable versions off, and no restore jobs since setup in 2024 (EV-015). A PC replaced in 2025 has no wipe or disposal record (EV-016).

**Documents and records.** The MSP contract has a 4-business-hour response time, no recovery time commitment, and no vulnerability scanning, endpoint detection and response, after-hours alert monitoring or security terms (EV-017). The request for security policies, a PCI DSS scope document, a data-flow or network diagram, an incident response plan, a contingency plan, a retention schedule, a risk assessment, a service provider list and training material returned none (EV-021). The Assistant Manager was designated Security and Privacy Lead in writing on 2026-07-01 (EV-022). Background-check reports are printed and filed with no disposal date; the handbook has one paragraph on confidentiality; there are no training records (EV-023). A cyber liability policy bought in 2025 has a 24x7 breach hotline and panel vendors (EV-037). There is one internet line and no failover (EV-038). The hurricane checklist covers shutters and a generator, not IT (EV-039).

**Suppliers and business volume.** Payments in 12 months went to 14 suppliers, including the dynamic pricing tool vendor since 2025-03, and to no other AI tool (EV-024). The accounting SaaS and payroll service enforce MFA (EV-025). FY2025 revenue was about $1.1 million, about $3,000 a day (EV-026). The PMS recorded about 10,300 room-nights at about 74% occupancy, about 5,900 stays, about 30% of room-nights from 14 crew accounts, and about 16 arrivals a day (EV-027). The PMS vendor's SOC 2 Type 2 report covers the 12 months ending 2026-03-31, states an RTO of 4 hours and an RPO of 15 minutes, and lists five complementary user entity controls; its service provider AOC is dated February 2026 (EV-028). The suite and backup vendors describe encryption at rest and TLS in transit (EV-029). The lock vendor relationship rests on support invoices only, and no gateway AOC or P2PE Instruction Manual is on file (EV-041).

**Rates, website and pricing.** The booking engine is the PMS vendor's hosted page, and it has included the $6 fee in the total since May 2025 (EV-030). The website banner shows a base rate, and the phone script quotes the base rate and mentions the fee only if asked (EV-031). The pricing tool has published rates automatically since 2025-03, with no ceiling, floor, daily limit or emergency rule, and MFA off (EV-032).

**AI tools and customers.** The PMS vendor offered a free trial of an AI guest messaging add-on, which was not started (EV-033). Staff mention using public chatbots to draft emails; how many, and what they entered, was not recorded (EV-034). The largest crew client sent a security questionnaire due 2026-09-30 (EV-035). There are 14 crew account letters; 2 crew companies are invoiced as business accounts (EV-036).

**Lock system and interviews.** The lock software lists 41 locks and one encoder (EV-042). The Assistant Manager describes keyed phone payments on the shared front desk PC, crew card forms emailed, printed into a binder and keyed, virtual card numbers displayed to check balances, no log review, no training, shredding in the back office, and the lock vendor's technicians connecting with one shared password and no MFA (EV-043). The Owner-Manager describes the motel's history, the 2025 SAQ, the deferred franchise offer, and that there are no Illinois, California or federal activities and no facial recognition on the CCTV (EV-044).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Gateway service provider AOC and the P2PE Instruction Manual | Gateway support | 2026-07-06 | Received 2026-07-20, during P03 fieldwork (EV-052) |
| Number of stored card authorization emails and printed forms | Assistant Manager | 2026-07-07 | Counted during fieldwork: mailbox search on 2026-07-16 (EV-049); binder examined on 2026-07-15 (EV-047) and counted on 2026-08-04 (EV-MP-4) |
| Number of staff using public chatbots, and what they enter | Assistant Manager (staff question follow-up) | 2026-07-09 | Not established at intake; P10 records the use without a count |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Processes and owners (EV-001, EV-043), revenue and volumes (EV-008, EV-026, EV-027), backup history (EV-015), vendor recovery figures (EV-017, EV-028), the internet line (EV-038), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-002 to EV-016 and EV-025 |
| P04 Cloud mapping | SaaS components and the MSP-operated backup (EV-002 to EV-007, EV-015, EV-024) and provider assurance (EV-028, EV-029) |
| P01 Risk register | Likelihood inputs from the console and MSP exports, the contracts folder, the pricing tool settings (EV-032) and the intake interviews (EV-043, EV-044) |
| P03 Regulatory analysis | The obligations register (which rules apply) and every observation above, compared with the requirements |
| P06 Policies | The document request result (EV-021), the handbook (EV-023) and the designation letter (EV-022) |
| P07 Control assessment | Populations to test from (EV-001, EV-002, EV-005, EV-007, EV-009) |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register; the merchant agreement (EV-018) and the cyber policy (EV-037) |
| P09 SOC 2 | Vendor assurance on file (EV-028, EV-029) and the crew client questionnaire (EV-035) |
| P10 AI governance | AI tools found (EV-024, EV-032, EV-033, EV-034) |

The asset inventory in this folder is the assessment's list, built from the evidence above. It is not a motel-maintained inventory; the SSP (CM-8) plans one by 2026-10-31.
