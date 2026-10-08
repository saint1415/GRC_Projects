# Intake Report: Cris Santos Company | Agriculture, Forestry, Fishing and Hunting | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (precision-agriculture crop farm, about 120 acres in two Florida parcels) |
| Intake window | 2026-07-06 to 2026-07-10 |
| Collected by | Owner-operator (owner, security lead and risk acceptor) |
| Approved | Owner-operator, 2026-08-31 |

## 1. Purpose and scope
Intake collected the farm's own records before the self-assessment began on 2026-07-13. A one-person farm has no HR system, asset database or internal audit, so the systems of record are the vendors' portals and admin consoles (the farm management and irrigation software, the booking platform, the email and file account, the accounting SaaS and online banking, the router, the AI yield trial), bank and card statements, the email inbox, the signed agreements folder, USDA program and permit records, the insurance agent's portal, the FAA drone registration account, and walk-throughs of the Home Farm and the River Field. Intake covers the organization, the systems that hold farm records and personal information or control the irrigation, the vendors and contractors that touch them, and the rules that may bind the farm. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (self-reviews, walk-throughs, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement or the benchmark is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Farm management and irrigation control | EV-001 to EV-008 | FMIS admin settings; FMIS vendor SOC 2 report; dealer agreement and handover notes | 2024-04-15 to 2026-07-06 |
| Fields and buildings | EV-009, EV-010 | Home Farm and River Field walk-throughs | 2026-07-08 to 2026-07-09 |
| Sales and customers | EV-011 to EV-015 | Booking platform console and reports; farm website; merchant agreement; email marketing console | 2026-06-30 to 2026-07-07 |
| Email, files, accounting and banking | EV-016 to EV-019 | Email and file account; accounting SaaS and online banking; statements; inbox | 2026-06-30 to 2026-07-08 |
| Devices and network | EV-020 to EV-022 | Laptop, phone and tablet settings screens; router admin page | 2026-07-08 |
| Sales volume and exemption records | EV-023 to EV-025 | Accounting SaaS reports; 2025 Schedule F; buying point settlement sheets | 2025-12-31 |
| Agreements, programs and insurance | EV-026 to EV-029 | Signed agreements folder; USDA program and permit records; insurance agent portal; FAA registration account | 2026-01-01 to 2026-07-10 |
| Documents | EV-030 | Owner's files (laptop, file account, email, paper) | 2026-07-10 |
| AI tools | EV-031 to EV-033 | AI yield trial account and terms; public chatbot account | 2026-07-10 |

## 3. Observations by area
**Farm management and irrigation control.** SYS-01 has two user accounts: the owner's administrator account and the irrigation dealer's technician account, created at the 2024 installation, whose role can start, stop and schedule irrigation at both sites. Both are active, the vendor support access setting has been on since installation, and there is no record of a user list review (EV-001). The administrator account signs in with a password only; MFA is offered and turned off (EV-002). The activity log records sign-ins and irrigation commands on the vendor's platform, with no record of a review (EV-003). Freeze and pressure alarms go by text message to the owner's phone only, with no second recipient or other route (EV-004). The export history lists no data export (EV-005). Scheduling recommendations are in recommendation mode, with automatic application off (EV-006). The vendor's SOC 2 Type 2 report covers Security and Availability for the 12 months ending 2026-03-31, states vendor-managed backups, RPO 1 hour and RTO 8 hours, and carves out the cellular service that carries commands to the pivot panel (EV-007). The dealer's 2024 service agreement contains no security terms, and the handover notes list about 16 field devices and explain the manual switches without any password or security setting (EV-008).

**Fields and buildings.** The pump house and equipment barn are padlocked, with no door alarm. The pump controller has a Hand-Off-Auto switch and a local/remote selector; the owner showed how freeze protection is started by hand, and no written procedure is posted or kept. There is no surge protection on the pump controller. Signs with the farm name and address stand at the farm stand and the U-pick check-in table, and the customer Wi-Fi password is posted at the stand. Paper program documents and the lease are filed in the home office (EV-009). The River Field pivot panel is in a locked cabinet with the same manual switches and a cellular modem (EV-010).

**Sales and customers.** The booking admin account signs in with a password only, with MFA offered and off. The vendor holds about 1,800 customer accounts, takes prepayments on its hosted page, and sends notices to the owner's personal address (EV-011). U-pick sales are about $70,000 a year, about $4,000 on a typical in-season weekend; 2 U-pick weekends needed refunds in 2025-26; nearly all customers are in Florida (EV-012). The farm website shows the farm name and not the complete business address (EV-013). The processor-managed card reader encrypts card data at the reader, the merchant terms require the farm to protect card data and report suspected compromise, and no self-assessment questionnaire has been requested (EV-014). The email list has about 2,100 subscribers (EV-015).

**Email, files, accounting and banking.** Email and files sit in a consumer plan also used for family mail, with MFA by text message since 2023, file version history off and no backup. File storage holds the 2 scanned W-9s, the customer export spreadsheet, program documents and the lease (EV-016). The accounting SaaS has MFA on and holds the W-9 data; online banking requires MFA and a one-time code before a new payee is added (EV-017). Statements show payments to the farm's SaaS vendors, carriers, insurers, contractors and landowner, and no payment for a cyber insurance policy (EV-018). Payments to the custom operator, the landowner and suppliers are arranged by email (EV-019).

**Devices and network.** The laptop has one administrator account shared with family members. Full-disk encryption, automatic updates and built-in antivirus are on, and no backup is set up. The browser stores every farm password and flags the SYS-01 and booking passwords as reused; the downloads folder holds a copy of the customer export; files arrive from the tractor display by USB stick (EV-020). The phone and tablet have passcodes, encryption and automatic updates; the phone carries the SYS-01 app, the alarm texts, the card reader app and the email codes (EV-021). One network carries the home office, the pump controller and the customer Wi-Fi. The router firewall is on with no port forwards, the admin password is the one on the router label, no firmware update appears in the history, and the router keeps no traffic log (EV-022).

**Sales volume and exemption records.** Food sales averaged about $172,000 a year over 2023 to 2025, about 56% sold directly to consumers and 44% to the buying point, with the records held in the accounting SaaS and the booking platform (EV-023). The 2025 Schedule F shows gross farm receipts of about $180,000 and no wages paid (EV-024). The buying point's 2025 settlement sheets total about $80,000 (EV-025).

**Agreements, programs and insurance.** The River Field is leased for cash rent, and the farm holds W-9s for the landowner and the custom harvest operator (EV-026). The farm has a federal crop insurance policy on peanuts, FSA farm records and acreage reports, a 2024 NRCS cost-share contract for the irrigation automation, and a water use permit; no federal procurement contract is on file (EV-027). The farm liability declarations list no cyber coverage (EV-028). The drone is FAA-registered and carries a camera only; the owner's remote pilot certificate and 2025 recurrent training are on file, and no cybersecurity course appears (EV-029).

**Documents.** No written security policy, risk assessment, incident plan or contact list, freeze-night procedure, contingency plan, mutual-aid arrangement, retention or disposal rule, vendor or device list, network diagram, AI use rule, or written 2026 annual review of qualified exemption eligibility was found. No copy of the SYS-01, booking or accounting records exists outside those systems, and the farm holds no FDA food facility registration (EV-030).

**AI tools.** The AI yield trial (SYS-08) holds 18 weekly image uploads from December 2025 to April 2026 and weekend forecasts by block, which the owner used to set reservation slots (EV-031). Its click-through terms let the vendor use farm imagery and yield data to improve its models (EV-032). The public chatbot history covers drafts of customer emails and website text (EV-033). The SYS-01 scheduling recommendations are listed above (EV-006).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Does the farm liability policy cover cyber events, under an endorsement or otherwise? | Insurance agent | 2026-07-09 | Not answered at intake; P08 carries it as an owner action |
| Which dealer staff use the SYS-01 technician account, and do they use MFA? | Irrigation dealer | 2026-07-09 | Not answered at intake; carried into the P01 risk register (R-004) |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Receipts and sales by channel (EV-012, EV-023 to EV-025), the alarm path and manual switches (EV-004, EV-009, EV-010), the FMIS vendor's recovery objectives (EV-007), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-001 to EV-005, EV-011, EV-014, EV-016, EV-017 and EV-020 to EV-022 |
| P04 Cloud mapping | SaaS components and terms (EV-001, EV-002, EV-011, EV-016, EV-017, EV-032) and provider assurance (EV-007) |
| P01 Risk register | Likelihood inputs from the account, device and router reviews (EV-002, EV-020, EV-022), the dealer records (EV-001, EV-008), the alarm settings (EV-004) and the document search (EV-030) |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with CSF 2.0, the Produce Safety Rule qualified exemption requirements and Fla. Stat. 501.171 |
| P06 Policies | The document search (EV-030): no prior policy existed to start from |
| P07 Control assessment | Populations to test: the 5 SaaS accounts (EV-002, EV-011, EV-016, EV-017), the laptop, phone and tablet (EV-020, EV-021), the router and the about 16 field devices (EV-008, EV-022), and the vendors in the vendor register |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register; insurance status (EV-018, EV-028) |
| P09 SOC 2 | Vendor assurance on file (EV-007) |
| P10 AI governance | AI tools found (EV-006, EV-031 to EV-033) |
