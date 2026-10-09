# Intake Report: Cris Santos Company | Arts, Entertainment, and Recreation | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent event promoter with one leased room in Florida) |
| Intake window | 2026-07-20 to 2026-07-24 |
| Collected by | Owner (owner, security and privacy lead, PCI DSS contact) |
| Approved | Owner, 2026-08-31 |

## 1. Purpose and scope
Intake collected the business's own records before the self-assessment began on 2026-07-27. A one-person promoter has no HR system, asset database or internal audit, so the systems of record are the vendors' admin portals and reports, the processor's PCI compliance portal, bank and card statements, the inbox, the signed agreements folder, the devices themselves, a walk-through of the Room, the insurance agent's portal, and written answers from the marketing assistant. Intake covers the organization, the systems that hold patron and payment information, the vendors and contractors that touch them, and the rules that may bind the business. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (self-reviews, walk-throughs, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Ticketing platform | EV-001 to EV-007 | Ticketing platform admin settings, reports and activity log | 2026-06-30 to 2026-07-20 |
| Payments and PCI DSS | EV-008 to EV-010 | Processor portal; PCI compliance portal; merchant agreement | 2021-03-01 to 2026-07-21 |
| Website, email and other SaaS | EV-011 to EV-016 | Website builder settings, documentation and pages; productivity suite; email marketing service; accounting SaaS | 2026-07-21 to 2026-07-22 |
| Devices, the Room and network | EV-017 to EV-021 | Laptop and phone settings screens; Room walk-through; lease | 2023-01-01 to 2026-07-22 |
| Contracts, money and business volume | EV-022 to EV-026 | Signed agreements folder; bank and card statements; tax files; accounting reports; bar concession records | 2025-12-31 to 2026-07-24 |
| Documents and practices | EV-027 to EV-029 | Owner's files; owner's written intake account; social accounts and flyer files | 2026-07-23 |
| Insurance and vendor assurance | EV-030 to EV-032 | Insurance agent portal; ticketing vendor (SOC 2 report under a nondisclosure agreement; product documentation) | 2026-01-01 to 2026-07-21 |
| AI tools | EV-004, EV-032, EV-033 | Ticketing platform feature settings; vendor documentation; marketing assistant's answers | 2026-07-20 to 2026-07-22 |

## 3. Observations by area
**Ticketing platform.** Two logins exist: the owner's administrator login and one shared "door" login with the scanner role, set up in 2024 with its password unchanged since. The scanner role can search orders by patron name and email, and no named sub-users exist although the platform supports them (EV-001). The administrator login uses a password only, with MFA available and off (EV-002). The activity log keeps 90 days of sign-ins, setting changes, exports and payout changes, and shows a full patron export each month; a payout-change email alert is set (EV-003). Every event has a limit of 6 tickets per order, bot protection runs on every on-sale with vendor defaults, and smart pricing has run in auto-apply mode on 8 shows since 2026-05-01 with no floor or ceiling prices (EV-004). In the 12 months to 2026-06-30 the platform sold about 6,800 tickets in about 3,600 orders across about 60 public shows, and about 120 orders were entered through the box office order screen (EV-005). It holds about 14,000 patron records, about 85% with a Florida ZIP code, and checkout requires buyers to confirm they are 18 or older (EV-006). Two apps are connected: the email marketing sync and a survey tool with no activity since 2024 (EV-007).

**Payments and PCI DSS.** The processor enforces MFA on its portal, shows only the last 4 card digits, and reports about 3,600 card orders a year, about 55% Visa. It states no merchant level (EV-008). The PCI compliance portal assigned SAQ A. The 2025 SAQ A was submitted on 2025-10-14 with "yes" to every question and no attachments, and the 2026 SAQ A is due 2026-10-31 (EV-009). The merchant agreement makes the owner the merchant of record, requires PCI DSS and card brand rules, and requires notice to the processor's risk team within 24 hours of suspecting a card data compromise (EV-010).

**Website, email and other SaaS.** The website builder's administrator login uses a password only, with MFA available and off. Event pages embed the ticketing checkout widget, and a social media pixel, an analytics tag and a chat widget plugin load on all pages (EV-011). The builder runs a web application firewall and patches its platform; plugins update automatically (EV-012). The privacy notice (a 2022 template) says patron information is never shared with third parties for marketing, and event pages say "limit 6 tickets per customer" (EV-013). Email and files are on a business plan with MFA on, version history on, and a folder of monthly patron exports from 2024-12 onward (EV-014). The email marketing service holds about 9,500 subscribers under one login that the marketing assistant also uses (EV-015). The accounting SaaS has MFA on for the owner, and the bookkeeper has its own login (EV-016).

**Devices, the Room and network.** The laptop has full-disk encryption, automatic updates, built-in antivirus and a host firewall on, locks after 5 minutes, and holds monthly patron exports in its downloads folder; the owner keys phone orders in its browser (EV-017). The owner's phone holds the only authenticator app, for email, the processor portal and accounting, and no recovery codes are saved (EV-018). The 2 scanning phones run only the scanner app with a passcode and the shared door login (EV-019). The Room has one Wi-Fi network, its password is on a sign backstage, and the laptop, the scanning phones, the sound engineer and touring crews use it. The owner states no router setting has changed since the ISP installed it (EV-020). The lease covers a 280-person room; the landlord controls the street entrance, the fire alarm and the internet line (EV-021).

**Contracts, money and business volume.** The door contractor's service agreement has no data or incident notice terms, the bookkeeper has an engagement letter, the IT consultant signed a confidentiality agreement on 2026-07-24, and the marketing assistant and sound engineer have no written terms (EV-022). Statements show SaaS charges, contractor payments, the lease and the general liability premium, and no payment for cyber insurance or any AI tool (EV-023). Gross receipts were about $180,000 in 2025 with no wages paid (EV-024): about $146,000 in ticket face value, $19,000 from the bar share, $11,000 from rentals and $4,000 from sponsorship (EV-025). The bar concessionaire runs its own POS and merchant account (EV-026).

**Documents and practices.** No written security policy, risk assessment, incident plan, contact list, PCI DSS scope description, provider list, vendor AOC, retention rule, training record or stored recovery codes was found (EV-027). The owner's written account says phone orders are keyed while the caller waits, some fans send card details by email or text, the marketing assistant uses the owner's logins, the ticketing and website logins share a password, activity and payout changes have not been reviewed, exports are kept with no rule on how long, the 2025 SAQ A was answered without a separate eligibility check, smart pricing was turned on without a review, and the owner has had no security training (EV-028). 2026 posts and flyers state prices as "$X plus fees" (EV-029).

**Insurance and vendor assurance.** The general liability declarations list no cyber or data breach coverage; the full policy form was requested (EV-030). The ticketing vendor's SOC 2 Type 2 report covers Security and Availability for the 12 months ending 2026-03-31, states RTO 4 hours and near-zero RPO, and carves out the processor and hosting provider (EV-031). The vendor's documentation says the processor serves the payment fields, the scanner app works offline, and smart pricing uses no patron-level data (EV-032).

**AI tools.** Smart pricing and bot protection are built-in ticketing platform features that the owner configures (EV-004, EV-032). The marketing assistant uses a consumer generative AI chatbot on a free plan to draft show descriptions and posts, and no other AI tool (EV-033).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Does the general liability policy cover any cyber loss? (full policy form) | Insurance agent | 2026-07-21 | Not answered at intake; the policy form arrived during fieldwork on 2026-07-30 (EV-036) |
| Current PCI DSS AOCs for the ticketing vendor and the processor | Ticketing vendor and processor trust pages | 2026-07-23 | None on file at intake; downloaded during fieldwork on 2026-07-28 (EV-044, EV-045) |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Ticket volume and revenue (EV-005, EV-024, EV-025), the ticketing vendor's recovery objectives (EV-031), the scanner app's offline mode (EV-032), the single authenticator device (EV-018), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-001 to EV-021 |
| P04 Cloud mapping | SaaS components and settings (EV-001 to EV-016) and provider assurance (EV-031) |
| P01 Risk register | Likelihood inputs from the account and device settings (EV-001, EV-002, EV-011, EV-017 to EV-020), the PCI portal and merchant agreement (EV-009, EV-010), the owner's intake account (EV-028) and the smart pricing settings (EV-004) |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the requirements |
| P06 Policies | The document search (EV-027): no prior policy existed to start from |
| P07 Control assessment | Populations to test: the 5 administrator logins (EV-002, EV-008, EV-011, EV-014, EV-016), the shared door login (EV-001), the laptop and 3 phones (EV-017 to EV-019), and the providers and contractors (EV-010, EV-022) |
| P08 IR runbook | Notification duties from the obligations register and the merchant agreement (EV-010); contacts from the vendor register; insurance status (EV-023, EV-030) |
| P09 SOC 2 | Vendor assurance on file (EV-031) |
| P10 AI governance | AI tools found (EV-004, EV-032, EV-033) |
