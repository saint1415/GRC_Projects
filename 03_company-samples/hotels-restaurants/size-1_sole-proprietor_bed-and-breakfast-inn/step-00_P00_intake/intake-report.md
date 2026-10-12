# Intake Report: Cris Santos Company | Accommodation and Food Services | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (six-room bed-and-breakfast inn in a small Florida coastal town) |
| Intake window | 2026-07-13 to 2026-07-17 (vendor reports requested at intake arrived 2026-07-22) |
| Collected by | Owner-innkeeper (owner, security and privacy lead, PCI DSS contact) |
| Approved | Owner-innkeeper, 2026-08-31 |

## 1. Purpose and scope
Intake collected the inn's own records before the self-assessment began on 2026-07-20. A one-person inn has no HR system, asset database or internal audit, so the systems of record are the vendors' admin portals and reports, the payment facilitator's portal and statements, the bank and card statements, the email inbox, the signed agreements folder, the laptop, phone, router and lock app settings, the owner's office, and the insurance agent's portal. The owner and the relief innkeeper also answered written intake questions. Intake covers the organization, the systems that store, process or transmit card data and guest personal information, the vendors that touch them, the AI tools in use, and the rules that may bind the inn. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (self-reviews, walk-throughs, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Innkeeping software accounts, logs and register | EV-001 to EV-004 | Innkeeping software admin settings and reports | 2026-06-30 to 2026-07-14 |
| Payments and card data paths | EV-005 to EV-009, EV-012 | Website and booking engine; payment facilitator portal and agreement; mailbox search | 2026-06-30 to 2026-07-14 |
| Partner portals, email and accounting | EV-010, EV-011, EV-023 | OTA extranets; email account; accounting SaaS; engagement letter | 2026-07-14 |
| Devices, network and locks | EV-013 to EV-017 | Laptop, browser, phone, router and lock app settings | 2026-07-15 |
| Office and paper | EV-018 | Owner's office review | 2026-07-15 |
| Documents, practices and people | EV-019 to EV-022 | Owner's files; written intake answers from the owner and the relief innkeeper; cleaning service agreement and email | 2026-07-16 |
| Business volume, contracts and insurance | EV-024 to EV-027 | Bank and card statements; tax files; insurance agent portal; signed agreements folder | 2025-12-31 to 2026-07-17 |
| AI tools | EV-028, EV-029 | Innkeeping add-on settings and transcript screen | 2026-07-13 to 2026-07-17 |
| Vendor assurance (intake follow-up) | EV-030 to EV-032 | Innkeeping software vendor; payment facilitator | 2026-03-31 to 2026-07-22 |

## 3. Observations by area
**Innkeeping software accounts, logs and register.** The innkeeping software has one user account, the administrator account in the owner's name, whose role can display full card numbers. A front desk role exists with no users, and there is no record of a user list review (EV-001). Two-step verification is available and turned off (EV-002). The activity log records sign-ins, card number displays, exports and setting changes for 12 months. It shows full card number displays on OTA virtual cards about once a month, no data export since 2019, and no record of a review (EV-003). The register holds about 600 stays and about 1,100 room-nights a year at an average daily rate of about $155, and about 3,400 guest profiles since 2019. About 55% of guests give a Florida address (EV-004).

**Payments and card data paths.** The website links to the innkeeping vendor's hosted booking and payment page, and online reservations hold a token. The booking engine adds the $15 housekeeping fee on the final payment step (EV-005). The website rate table shows nightly rates with no fee, and the privacy statement says "we never store your card details" (EV-006). The facilitator's portal shows no self-assessment questionnaire ever submitted and a $19.95 monthly PCI non-compliance fee since March 2024. One mobile reader is registered, described as part of a PCI-listed validated P2PE solution. Pay-by-link is available and unused, and receipts show the last 4 digits (EV-007). About 1,050 card transactions (about $165,000) ran in the 12 months to June 2026: about 420 booking engine deposits, 160 OTA virtual cards, 120 keyed phone payments, and 350 card-present payments (EV-008). The sub-merchant agreement requires annual validation and notice within 24 hours of a suspected compromise (EV-009). A mailbox search returned about 85 emails with card numbers since 2022, 31 with security codes (EV-012).

**Partner portals, email and accounting.** OTA-1 sends a sign-in code to the owner's phone. OTA-2 uses a password only, with verification available and turned off. Both portals display full virtual card numbers, and only the owner's login is in use on each (EV-010). The consumer email and file account uses a password only, with two-step verification available and turned off. Photo backup from the phone is on, there is no file version history, and the inbox holds card authorization forms (EV-011). The accounting SaaS enforces MFA for the owner and the bookkeeper's named user (EV-023).

**Devices, network and locks.** The laptop has one user profile that family members also use. Automatic updates, built-in antivirus and the host firewall are on. Full-disk encryption is off, the screen locks after 20 minutes, no backup is configured, and phone payments are keyed in its browser (EV-013). The browser holds 18 saved passwords; one password is used for both the innkeeping software and email, and several are under 10 characters (EV-014). The phone has a passcode, locks after 30 seconds and is encrypted. It runs the payment app and receives the sign-in codes, and its camera roll holds about 1,900 guest ID photos since 2021 that sync to the consumer photo backup (EV-015). One Wi-Fi network serves guests and the owner's devices, its password is printed in every room, the guest network feature is off, and the firmware is the version the ISP installed (EV-016). The locks issue random per-reservation codes that expire at checkout; the house master code was last changed in 2022 (EV-017).

**Office and paper.** The office holds the laptop, the reader, the paper pad and a binder of printed card forms, and is not locked during the day. About 140 pad pages since 2023, with card numbers and security codes, sit in an unlocked desk drawer. A home cross-cut shredder is used for paper, and the weekly arrivals list is shredded each week (EV-018).

**Documents, practices and people.** No written policy, procedure, risk assessment, incident plan, contact list, card data flow list, retention rule, provider list or training record was found (EV-019). The owner keys phone bookings on the laptop or writes them on the pad with the security code, quotes nightly rates by phone without the fee, photographs every guest's ID, has had no security training, had not read the 24-hour notice term, and believed the vendors covered PCI DSS. The router's administrator password is the label password and its firmware has never been updated (EV-020). The relief innkeeper signs in to the innkeeping software and OTA-2 with the owner's username and password (EV-021). Two cleaners enter with the master code, and one cleaner left the cleaning service in 2024 (EV-022).

**Business volume, contracts and insurance.** Statements show recurring payments to the innkeeping vendor, the email and file plan, the accounting SaaS, the website builder, the lock vendor, the ISP, the phone carrier, the cleaning service, the bookkeeper and the business owner's insurer, hourly payments to the IT consultant, and no payment for a standalone cyber policy (EV-024). Gross receipts were about $180,000 in 2025, with no wages paid (EV-025). The business owner's policy declarations list no data breach endorsement (EV-026). The IT consultant signed a confidentiality agreement on 2026-07-17 (EV-027).

**AI tools.** The innkeeping software's AI add-on was turned on 2026-05-01. Its rate suggestions apply automatically, with blank floor, ceiling and daily limit fields and no emergency setting, and its chat assistant quotes rates on the website (EV-028). Transcripts are kept with guests' names and emails, rate answers leave out the fee, and some guest messages contain card numbers (EV-029).

**Vendor assurance (intake follow-up).** The innkeeping vendor's SOC 2 Type 2 report covers Security and Availability for the 12 months ending 2026-03-31, states RTO 4 hours and RPO 1 hour, and does not cover the AI add-on (EV-030). The innkeeping vendor and the payment facilitator provided service provider AOCs (EV-031, EV-032). All three arrived on 2026-07-22.

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| PCI DSS AOCs and the innkeeping vendor's SOC 2 report | Innkeeping software vendor; payment facilitator | 2026-07-14 | Received 2026-07-22 (EV-030 to EV-032, intake follow-up) |
| Does the business owner's policy include a data breach endorsement? | Insurance agent | 2026-07-15 | Not answered at intake; P08 carries it as an owner action |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Revenue and volume (EV-004, EV-008, EV-025), the innkeeping vendor's recovery objectives (EV-030), single-person access (EV-002, EV-015, EV-021), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-001 to EV-018 and EV-023 |
| P04 Cloud mapping | SaaS components and settings (EV-001 to EV-003, EV-010, EV-011, EV-023, EV-028) and provider assurance (EV-030 to EV-032) |
| P01 Risk register | Likelihood inputs from the account, device and router reviews (EV-002, EV-010, EV-011, EV-013 to EV-016), the facilitator's records (EV-007), the stored card data (EV-012, EV-018), and the written intake answers (EV-020, EV-021) |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the requirements; the card data paths (EV-005, EV-007 to EV-009, EV-012, EV-018, EV-020) decide which SAQ the current design needs |
| P06 Policies | The document search (EV-019): no prior policy existed to start from |
| P07 Control assessment | Populations to test: the five SaaS accounts (EV-002, EV-010, EV-011, EV-023), the laptop and phone (EV-013, EV-015), the router (EV-016), the lock app (EV-017), the paper pad and mailbox (EV-012, EV-018), and the providers in the vendor register |
| P08 IR runbook | Notification duties from the obligations register; the facilitator's 24-hour notice term (EV-009); contacts from the vendor register; insurance status (EV-026) |
| P09 SOC 2 | Vendor assurance on file (EV-030 to EV-032) |
| P10 AI governance | AI tools found (EV-028, EV-029) |
