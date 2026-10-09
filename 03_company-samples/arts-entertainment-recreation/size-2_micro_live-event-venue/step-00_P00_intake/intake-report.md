# Intake Report: Cris Santos Company | Arts, Entertainment, and Recreation | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (live event venue operator with ticketing; one leased Florida music club) |
| Intake window | 2026-06-29 to 2026-07-10 |
| Collected by | Venue Manager (designated Security and Privacy Lead on 2026-07-13, EV-043), with the MSP account technician for the MSP exports, the Box Office and Ticketing Manager for the ticketing platform and the Bookkeeper for the acquirer and finance records |
| Approved | Owner and General Manager, 2026-08-31 |

## 1. Purpose and scope
Intake collected the company's own records before any assessment work began on 2026-07-13. The trigger was the acquirer's letter of 2026-06-08 (EV-014), which asks for an SAQ and AOC for each merchant account by 2026-12-15. Intake covers the organization, the systems that hold patron and card data, the suppliers that touch them, and the rules that may bind the company. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, observations, tests) to the same register, so one list backs every deliverable.

A 7-person club has no HR system, CMDB or accounts payable vendor master. Its systems of record are the vendor admin consoles and portals (the ticketing platform, the payment partner, the bar POS, the productivity suite, the website builder, the email marketing service), the acquirer's portal and merchant statements, the payroll and accounting services, the MSP's exports and monthly report, the paper contracts and HR files, the card statements, and what can be seen in the building.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| People and contractors | EV-001 to EV-003 | Payroll service; HR files; staffing contracts | 2026-06-30 to 2026-07-01 |
| Ticketing platform and AI | EV-004 to EV-011 | Ticketing admin console, reports, agreement and customer portal | 2026-06-30 to 2026-07-06 |
| Card acceptance | EV-012 to EV-017 | Payment partner portal; POS back office; acquirer letter, portal and statements; merchant agreements | 2026-06-08 to 2026-07-07 |
| MSP, computers, network and backup | EV-018 to EV-027 | MSP contract; MSP device, policy, encryption and anti-malware consoles; MSP monthly report and tickets; network documentation; backup console; suite admin console | 2026-06-30 to 2026-07-07 |
| Website and email marketing | EV-028 to EV-030 | Website builder admin console; public pages; email marketing console | 2026-07-07 to 2026-07-08 |
| Suppliers, documents and finances | EV-031 to EV-036 | Contracts folder; card statements and invoices; document request; handbook; cyber policy; accounting service | 2021-01-01 to 2026-07-02 |
| Interviews, walk-through and staff question | EV-037 to EV-041 | Owner, Box Office and Ticketing Manager, Venue Manager and Marketing Coordinator interviews; dark-day walk-through; staff AI tool question | 2026-07-08 to 2026-07-09 |
| Vendor documentation | EV-042 | Vendor websites and help centers | 2026-07-10 |

## 3. Observations by area
**People and contractors.** Payroll lists 7 active employees and 1 departure from January to June 2026, the former Marketing Coordinator, whose last working day was in March 2026 (EV-001). Background checks are on file for the Box Office and Ticketing Manager and the Bookkeeper; the departure record lists the laptop and keys returned and no system access removals (EV-002). Two staffing contractors supply about 20 event-night workers a show. The security contractor screens its guards under its license; the hospitality agreement has no screening term, and neither agreement covers card handling, device use or confidentiality (EV-003). Departures are handled by the Owner with no written checklist (EV-037).

**Ticketing platform.** The platform has 9 active venue accounts, including one in the name of the former Marketing Coordinator, the freelance web designer's account with the marketing role, and one shared "door" login with the box office role; the marketing role can export patron lists and the box office role can sell, refund and scan (EV-004). MFA is offered and not enforced for any venue user, the audit log keeps 90 days, and screens show the last 4 digits of card numbers only (EV-005). Patron list exports in the last 90 days came from the Owner's and the Marketing Coordinator's accounts (EV-006). The platform sells about 30,000 tickets a year to about 47,000 patron accounts, about 84% with a Florida billing address; MID-T orders are about 13,500 online, about 2,600 card sales at the door and about 300 phone orders a year (EV-007). Every ticket carries a mandatory $3.50 service fee and $1.50 facility fee; online buyers pay in the vendor's checkout widget; a payment link feature is available and not in use (EV-008). The responsibility matrix assigns to the venue its user accounts and MFA enforcement, roles, API tokens, and the security of any page where it embeds the widget, and the agreement sets no breach notice time (EV-010). The vendor portal offers a PCI DSS AOC dated 2026-03-12 and a SOC 2 Type 2 report; neither is in the company's files (EV-011; EV-031).

**Demand tools (AI).** The demand tools module was switched on 2026-04-06 and its price recommendations were used on 9 shows, with no floor or ceiling prices entered and accessible spaces set up as their own price tier. Bot screening and the on-sale queue run on high-demand on-sales, 6 in the last 12 months; the limit of 4 tickets is applied per account, the audio challenge alternative is off, and the block page gives no contact route (EV-009). The Box Office and Ticketing Manager switched the module on after a vendor webinar (EV-038).

**Card acceptance.** The door uses 2 Bluetooth readers from the payment partner's P2PE solution, and the partner's instruction manual asks for a reader inventory with serial numbers and tamper inspections; no partner AOC is on file (EV-012). The bar uses 4 P2PE readers with manual entry disabled and one shared clerk login per terminal (EV-013). The acquirer classified the company as a Visa Level 3 merchant on 2026-06-08 and requires an SAQ and AOC for each account and quarterly ASV scans for MID-T by 2026-12-15 (EV-014). The acquirer portal pre-selected SAQ A for MID-T and SAQ P2PE for MID-F from 2023 enrollment answers that describe the ticket account as "online only", and no SAQ, AOC or ASV report has ever been submitted (EV-015). The statements show about 57,000 card transactions a year, about 31,000 of them Visa, and a monthly non-validation fee of $39.95 on each account since March 2024 (EV-016). The merchant agreements require notice to the acquirer within 24 hours of a suspected compromise (EV-017). For phone orders, callers' card numbers are typed into the box office web app on the back-office PC, which is also used for email, browsing and bookkeeping, and patrons and corporate renters sometimes email card details to the box office mailbox. Accessible spaces are sold only by phone (EV-038).

**MSP, computers, network and backup.** The MSP contract covers the 5 office computers, firewall and Wi-Fi, suite administration and the suite backup, with a 4-business-hour response time and no recovery time or incident notice term (EV-018). The MSP device list shows the 5 computers and no tablets, scanners, card readers, network devices or SaaS services (EV-019). Staff have no local administrator rights; the screen lock is 10 minutes except on the back-office PC, set to 60 minutes (EV-020). Four of the 5 computers are encrypted; the Owner's laptop is not (EV-021). Anti-malware is signature-based, with alerts to the MSP help desk in business hours (EV-022). The MSP's services do not include vulnerability scanning, endpoint detection and response or log monitoring (EV-023). One staff Wi-Fi, with a password last changed in 2023, carries the office computers, door tablets, scanners and bar POS; the guest Wi-Fi is internet only; there is one internet line (EV-024). The suite backup copies the 7 named mailboxes and shared files daily with 30 days of versions; the 2 shared mailboxes are not in the selection and no restore job has run (EV-025). MFA was enabled on the 7 named suite accounts in 2025 (EV-026). The 2 shared mailboxes allow direct sign-in with a password and no MFA, and named-account MFA uses push approval without number matching (EV-027). Touring crews are given the staff Wi-Fi password, the tablets and scanners update when staff accept prompts, and nobody reviews the ticketing audit log, mailbox sign-ins or website changes. Corporate clients send attendee lists to the shared info mailbox, where 2025 client lists are still kept (EV-039).

**Website and email marketing.** The website builder has one administrator user with MFA off; a countdown timer plugin was last updated in 2024 (EV-028). The Owner, the Marketing Coordinator and the freelance web designer share that login (EV-037). The 2023 privacy notice says patron information is never shared with third parties, the FAQ describes the facility fee as a charge from the ticketing company, and event listings show the base ticket price (EV-029). About 18,000 subscribers are on the email marketing service, uploaded by hand from ticketing exports (EV-030).

**Suppliers, documents and finances.** No written agreement exists with the freelance web designer, and the contracts folder holds no service provider list, vendor AOC or SOC 2 report (EV-031). The card statements show the recurring suppliers and no AI tool charges (EV-032). The request for security policies, a PCI DSS scope document, an incident response plan, a manual door procedure, a card reader inventory or inspection log, training and log review records, a change log, a retention schedule and a service provider list returned none (EV-033). The 2021 employee handbook has one page on computer use (EV-034). A 2025 cyber policy with a breach hotline and panel firms is on file (EV-035). FY2025 revenue was about $1.1 million, about $7,300 per show, and the cash reserve covers about 45 days of expenses (EV-036).

**Building and people.** The dark-day walk-through counted 5 computers, 2 door tablets with no passcode, 3 scanners, 2 door readers and 4 bar readers, 16 CCTV cameras covering the door box office, bar and back office, and standalone production consoles; receipts show the last 4 digits (EV-040). Settlements are done on show night in a suite workbook, and artists' payment details arrive by email (EV-037). The staff AI question found the demand tools and the Marketing Coordinator's use of public chatbots for show descriptions and social posts (EV-041). The suite, website builder and backup vendors describe encryption in transit and at rest (EV-042).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| MSP technician list and evidence of MFA on the remote management tool | MSP account technician | 2026-07-02 | Not provided; asked again in P07 (EV-060, EV-SA-9) and carried into P01 (R-015) and POAM-012 |
| Whether the cyber policy covers card brand assessments | Owner and General Manager (with the broker) | 2026-07-02 | Not confirmed; noted in the P01 treatment summary |
| The ticketing vendor's AOC and SOC 2 report, offered on its portal | Venue Manager | 2026-07-06 | Not downloaded at intake; downloaded and reviewed 2026-08-19 (EV-062, EV-063) |
| Payment partner AOC | Payment partner | 2026-08-14 (after P07 fieldwork) | Not received by the end of fieldwork (EV-061); POAM-012 |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Processes and owners (EV-001, EV-037, EV-038), revenue, show economics and cash reserve (EV-036), sales volumes (EV-007), the backup schedule (EV-025), the MSP's terms (EV-018), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-004 to EV-028 |
| P04 Cloud mapping | SaaS components and the MSP-operated backup (EV-004 to EV-013, EV-025, EV-027, EV-028) and provider documentation (EV-010, EV-042) |
| P01 Risk register | Likelihood inputs from the console and MSP exports, the acquirer records, the walk-through (EV-040) and the intake interviews (EV-037 to EV-039) |
| P03 Gap analysis | The obligations register (which rules apply), the acquirer records (EV-014 to EV-017) and every observation above, compared with PCI DSS and the FTC rules |
| P06 Policies | The 2021 handbook (EV-034), the document request response (EV-033) and the designation letter (EV-043) |
| P07 Control assessment | Populations to test from (EV-001, EV-004, EV-019, EV-027, EV-040) |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register; the merchant agreements (EV-017) and the cyber policy (EV-035) |
| P09 SOC 2 | Vendor assurance offered (EV-011) and the corporate rental client's questionnaire, received after intake on 2026-07-28 (EV-066) |
| P10 AI governance | AI tools found (EV-009, EV-032, EV-038, EV-041) |

The asset inventory in this folder is the assessment's list, built from the evidence above. It is not a company-maintained inventory; the SSP (CM-8) and POL-04 4.5 plan one.
