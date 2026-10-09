# Intake Report: Cris Santos Company | Food and Agriculture | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (custom-exempt meat processing shop on the owner's Florida homestead) |
| Intake window | 2026-07-20 to 2026-07-24 |
| Collected by | Owner-operator (owner, security lead, and records keeper for the custom exemption) |
| Approved | Owner-operator, 2026-08-31 |

## 1. Purpose and scope
Intake collected the shop's own records before the self-assessment began on 2026-07-27. A one-person shop has no HR system, asset database or internal audit, so the systems of record are the vendors' portals and admin pages (the cold-chain service, the smokehouse app, the booking form, the email and file account, accounting and banking, the router), bank and card statements, the email inbox, the signed agreements folder, the FSIS review record, the insurance agent's portal, the laptop and phone, and a walk-through of the shop. Intake covers the organization, the systems that hold shop data or act on product, the vendors that touch them, and the rules that may bind the shop. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (self-reviews, walk-throughs, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement or the CSF 2.0 benchmark is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Cold-chain monitoring | EV-001 to EV-005 | Cold-chain vendor portal; vendor terms and SOC 2 report | 2026-03-31 to 2026-07-20 |
| Smokehouse controller and app | EV-006, EV-007 | Smokehouse app settings; manufacturer terms | 2026-07-20 |
| Laptop, phone and labels | EV-008 to EV-010 | Laptop and phone settings screens; scale and label printer | 2026-07-21 |
| Email, files and custom records | EV-011, EV-012 | Email and file account; custom records spreadsheet | 2026-07-21 |
| Booking form and vendor contacts | EV-013, EV-014 | Booking form admin console; vendor account settings | 2026-07-21 to 2026-07-22 |
| Accounting, payments and business volume | EV-015 to EV-018 | Accounting SaaS, banking and card reader settings; signed agreements folder; accounting reports; tax files | 2025-12-31 to 2026-07-22 |
| Shop network and building | EV-019, EV-020 | Router admin page; shop walk-through | 2026-07-22 |
| Custom exemption records | EV-021 to EV-023 | Kill sheet photos; FSIS review record; cure sheet and batch sheets | 2026-03-18 to 2026-07-23 |
| AI tools | EV-024, EV-025 | Chatbot account; chatbot terms | 2026-07-23 |
| Vendors, insurance and documents | EV-026 to EV-029 | Bank and card statements; inbox; insurance agent portal; owner's files | 2026-01-01 to 2026-07-24 |

## 3. Observations by area
**Cold-chain monitoring.** The cold-chain account has one user, the owner, with the administrator role; only the administrator can change set points and alert contacts. It signs in with a password only, and MFA is offered and turned off (EV-001). Five sensors report through one gateway on the shop Wi-Fi, with set points of 38 F (carcass cooler) and 10 F (freezer). Alerts go by text and app notification to one contact, the owner's phone, and the "gateway offline" notice is turned off. The anomaly alert feature is on (EV-002). The activity log records sign-ins and setting changes, and the account shows no log review or export (EV-003). The subscription is on click-through terms, and no SOC 2 report had been requested before intake (EV-004). The report received on 2026-07-23 covers Security and Availability for the 12 months ending 2026-03-31 with an unmodified opinion and one remediated exception. It states that the gateway buffers 12 hours of readings offline but cannot send alerts while offline, and that cloud hosting and text-message delivery are carved out (EV-005).

**Smokehouse controller and app.** The app signs in with a password only and offers no MFA. Remote monitoring, start and stop, and remote program editing are on. The controller holds 10 cook programs, with no copy kept elsewhere (EV-006). The app terms were accepted at setup, and the owner has no copy or notes from reading them (EV-007).

**Laptop, phone and labels.** The laptop has one account with administrator rights, used daily and not shared with family. Full-disk encryption, automatic updates, antivirus and the firewall are on, and no backup is set up. The browser stores every shop password and flags the cold-chain and smokehouse passwords as the same. The label templates and the cure sheet exist only on the laptop (EV-008). The phone is encrypted with a passcode and updates automatically. It holds the cold-chain and smokehouse apps, the card reader app, the email codes, kill sheet photos and customer texts, and it is the only device that receives cold-chain alerts (EV-009). A test label showed "Not for Sale" in lettering at least 3/8 inch high, and a preprinted label roll is kept at the scale (EV-010).

**Email, files and custom records.** Email and files sit in a consumer plan also used for personal mail, with MFA by text message since 2024 and no file version history or backup. The tax preparer has a shared link to an export folder (EV-011). The custom records are one spreadsheet for 2024 to 2026 with about 640 livestock and product owners, nearly all at Florida addresses. It holds names, addresses, phones and emails, but no Social Security, license or account numbers. Pickup dates are blank for 2024, and the file shows no earlier versions (EV-012).

**Booking form and vendor contacts.** The booking form admin signs in with a password only, with MFA offered and turned off. Submissions with customer contact details are kept by the vendor and emailed to the owner (EV-013). Every vendor account sends notices to the owner's personal address, and no shop security contact is registered (EV-014).

**Accounting, payments and business volume.** Accounting has MFA on, and the bank requires a one-time code before a new payee is added. The processor-managed card reader encrypts card data at the reader, and no card numbers touch shop-managed systems (EV-015). The merchant agreement requires card data protection and compromise reporting. No agreement exists with the slaughter operator, a neighboring processor, or any source of emergency cooler space or standby power (EV-016). Processing fees were about $180,000 in 2025, about $3,500 a week in the busy season, with no meat sales (EV-017). The 2025 Schedule C shows no wages paid (EV-018).

**Shop network and building.** The provider's router carries the laptop, phone, gateway, smokehouse controller and customers' phones on one network, with no guest network. The firewall is on with no port forwarded. The admin password in use is the one printed on the label, and no firmware update is recorded (EV-019). The walk-through found the shop locked when the owner is away, and curing agents in a locked cabinet with the nitrite content marked. Old cut sheets and kill sheet printouts sit in open boxes behind the counter. The dial thermometers are read at opening and closing. The gateway and router run on wall power with no battery backup, and there is no generator. No outage or storm procedure is posted, and customers get the Wi-Fi password when they ask (EV-020).

**Custom exemption records.** Kill sheet photos list owner, species, carcass number and hot weight. Every carcass recorded is beef, pork, lamb or goat, with no wild game (EV-021). The March 2026 FSIS review noted no noncompliance (EV-022). The cure sheet has no version history, and the 2026 batch sheets do not say how each cure amount was calculated or checked (EV-023).

**AI tools.** The public chatbot account has about 30 conversations since January 2026, mostly cure and brine scaling, with 12 cure answers saved. The training-use setting is on (EV-024). Its consumer terms let the vendor use inputs to improve its service (EV-025). The cold-chain anomaly alert feature is the second AI use found (EV-002).

**Vendors, insurance and documents.** Statements show recurring payments to the shop's SaaS vendors, internet provider and phone carrier. They also show payments to the label software vendor, refrigeration contractor, suppliers, tax preparer and IT technician, and no payment to the chatbot vendor or for a cyber policy (EV-026). The inbox holds the refrigeration contractor's invoices with its 24-hour line and hourly IT technician invoices with no standing access. It also holds a 2023 label software trial sign-up with no cancellation (EV-027). The business liability declarations list no cyber coverage (EV-028). No written security policy, risk assessment, incident plan, contact list, outage or storm procedure, retention or disposal rule, vendor list, device list, AI use rule, printed cook programs, security training record, or FDA registration was found (EV-029).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Does the business liability policy include a cyber endorsement? | Insurance agent | 2026-07-23 | Not answered at intake; P08 carries it as an owner action |
| Does a street address in a business record count as geolocation under Fla. Stat. 501.171(1)(g)1.a.(VII)? | Business attorney | 2026-07-24 | Not answered at intake; carried as the P03 open question for counsel |
| How are gateway firmware updates signed and delivered? | Cold-chain vendor | 2026-07-23 | Not answered at intake; carried in the P09 vendor review |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Fees and volume (EV-017, EV-018, EV-012), the gateway's offline buffer (EV-005), the single alert path (EV-002, EV-009), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-001 to EV-020 |
| P04 Cloud mapping | SaaS and device cloud components and terms (EV-001 to EV-007, EV-011, EV-013, EV-025) and provider assurance (EV-005) |
| P01 Risk register | Likelihood inputs from the account and device reviews (EV-001, EV-002, EV-006, EV-008, EV-019), the shop walk-through (EV-020), the records (EV-011, EV-012, EV-023), and the chatbot records (EV-024, EV-025) |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the binding rules and the CSF 2.0 benchmark |
| P06 Policies | The document search (EV-029): no prior policy existed to start from |
| P07 Control assessment | Populations to test: the vendor accounts the owner signs in to (EV-001, EV-006, EV-011, EV-013, EV-015, EV-024), the laptop and phone (EV-008, EV-009), the router (EV-019), and the 9 vendors that provide shop systems (V-01 to V-09 in the vendor register) |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register; insurance status (EV-028) |
| P09 SOC 2 | Vendor assurance on file (EV-005) |
| P10 AI governance | AI tools found (EV-024, EV-025, EV-002) |
