# Scenario facts: Cris Santos Company | Arts, Entertainment, and Recreation | Sole Proprietorship

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a law, regulation, standard, or card brand rule, the citation is given. Facts about the payment processor, the merchant agreement, the landlord, and vendors are fictional.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship; the owner files Schedule C) |
| Business | Independent event promoter with its own small room (NAICS 711310, promoters with facilities). The owner holds a 5-year lease on **the Room**, a 280-person standing room (150 seated in cabaret layout) on the ground floor of a mixed-use building. The owner books and promotes concerts, comedy, and spoken-word shows there and rents the Room for private events |
| Location | Florida. The Room has a small office behind the stage. The owner also works from home |
| Activity | About 60 public shows a year (about 12 of them seated) and about 15 private rentals. About 6,800 tickets sold a year in about 3,600 orders, an average of about 110 tickets per show |
| Workforce | The owner only (0 employees). Uses independent contractors instead of staff (section 2) |
| Revenue | About $180,000 a year in gross receipts (fictional): ticket face value about $146,000, the bar concessionaire's revenue share about $19,000, private rentals about $11,000, and sponsorship about $4,000. Under the SBA standard of $40.0 million for NAICS 711310 (13 CFR 121.201), so SBA-small |
| Patrons | About 14,000 patron records on the ticketing platform (anyone who bought a ticket since 2021: name, email, phone, ZIP code, order history) and about 9,500 email subscribers. About 85% of buyers have a Florida ZIP code; the rest live in other states |
| Card acceptance | About 3,600 card orders a year, all through **one merchant account** with a payment processor that is integrated with the ticketing platform. Visa is about 55% of orders (about 2,000 a year). Patrons pay on the ticketing platform's hosted checkout, either on the platform's event pages or in the checkout widget embedded on the owner's website. Walk-up buyers on show nights scan a QR code and buy on their own phones. The owner has **no card reader** and takes no cash at the door. The bar concessionaire runs its own POS under its own merchant account (outside this business) |
| Merchant of record | The owner is the merchant of record for ticket sales. Payouts settle to the business bank account two business days after each sale. The ticketing vendor charges buyers a service fee per ticket, which the vendor keeps |
| PCI DSS status | **Merchant.** The merchant agreement requires compliance with PCI DSS v4.0.1 (PCI SSC) and card brand rules. PCI DSS is a contractual standard, not law (N71-R04). The processor's PCI compliance portal assigned **SAQ A** (all card data functions outsourced to PCI DSS compliant third parties). The owner completed the 2025 SAQ A in the portal on 2025-10-14 and answered "yes" to every question. The 2026 SAQ A is due in the portal on **2026-10-31**. The processor has not stated a merchant level. Visa's current table (*What To Do If Compromised* v10.0, effective 2026-06-25, as verified in the Small sample) puts merchants with 1 to 1,000,000 Visa transactions a year at Level 3 |
| Not in scope | **Gaming** (Nevada Reg. 5.260, NIGC MICS, BSA/AML for casinos): no gaming or wagering. **COPPA:** the website and ticketing pages are general audience, and the ticketing platform requires buyers to be 18 or older. **HIPAA:** no health care. **SEC disclosure:** not a public company. **Federal contracts:** none. **Card-present payments:** none (no reader) |
| Other applicable law | FTC Act Section 5 (15 U.S.C. 45(a)), which reaches "persons, partnerships, or corporations" (45(a)(2)), so it reaches a sole proprietor; the FTC Rule on Unfair or Deceptive Fees (16 CFR Part 464), whose "business" definition includes an individual (464.1) and whose "covered good or service" includes live-event tickets; the BOTS Act (15 U.S.C. 45c), which protects the owner as a ticket issuer (the definition names the sponsor or promoter of an event); Florida breach notification and disposal (Fla. Stat. 501.171), whose "covered entity" definition names a sole proprietorship (501.171(1)(b)); ADA Title III ticketing rules for accessible seating (28 CFR 36.302(f)) on seated shows; Fla. Stat. 817.36 only as noted in P10 |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notification and disposal, and the Florida ticket statute in P10). Other states are treated generically ("each state where affected individuals reside") |

## 2. People and contracted services (role titles only)
| Role | Duties |
|---|---|
| Owner | Every role: owner, promoter, booker, settlement, security and privacy lead, PCI DSS contact, incident lead, and risk acceptor. Signs the SAQ A attestation |
| Freelance marketing assistant (contractor, about 10 hours a week) | Builds event pages, posts to social media, sends email campaigns. **Signs in with the owner's own ticketing platform and website logins** (no own accounts) |
| Door and security contractor (a crowd management company) | Supplies 2 to 3 door and security staff per show. They scan tickets with the ticketing platform's scanner app on 2 business-owned scanning phones, using **one shared "door" login** |
| Freelance sound engineer (contractor) | Runs audio on show nights. No access to business data. Uses the Room's Wi-Fi |
| Bar concessionaire (separate licensed business) | Runs the bar under its own liquor license, staff, POS, and merchant account. Pays the owner a revenue share. Outside the owner's card environment |
| Outside bookkeeper (accounting firm) | Quarterly bookkeeping and tax filings through its own login to the accounting SaaS |
| On-call IT consultant | Hourly help with the laptop, phone, and Wi-Fi. No standing access. Signed a confidentiality agreement on 2026-07-24 before helping with the self-assessment |
| Landlord | Owns the building; controls the street entrance, the fire alarm, and the building's internet service to the Room |
| Ticketing platform vendor (external) | White-label ticketing SaaS. A PCI DSS validated service provider with a SOC 2 Type 2 report |
| Payment processor (external) | The ticketing platform's integrated processing partner. Holds the owner's merchant account, runs the payment fields in the hosted checkout, and runs the PCI compliance portal. A PCI DSS validated service provider |

## 3. Systems
| ID | System | Hosting | Personal or card data? | Notes |
|---|---|---|---|---|
| SYS-01 | Ticketing platform: event setup, hosted event and checkout pages, embeddable checkout widget, patron records, box office order screen, scanner app, reports and exports, payouts, **smart pricing** and **bot protection** features | Vendor SaaS | About 14,000 patron records. Card data only inside the vendor's and processor's PCI environments; the owner sees only the last 4 digits | Owner administrator account with a password only. MFA is available but off. Supports named sub-users with roles, but none were created. The marketing assistant uses the owner's login. One shared "door" login (scanner role, which can also search orders by name) |
| SYS-02 | Payment processor merchant account and portal (settlements, chargebacks, PCI portal) | Service provider SaaS | Card data only inside the processor; the portal shows the last 4 digits | MFA enforced by the processor |
| SYS-03 | Website (website builder SaaS): event calendar pages that embed the ticketing checkout widget | Vendor SaaS | No card data stored. Pages carry the checkout widget | Administrator login with a password only (MFA available, off), and **the same password as SYS-01**. Three third-party scripts on event pages: a social media tracking pixel, a web analytics tag, and a chat widget plugin |
| SYS-04 | Productivity suite: email, calendar, cloud file storage (business plan) | SaaS | Yes: artist contracts, settlement sheets, patron exports, and **emails from fans containing card numbers** | MFA on (authenticator app on the owner's phone). File version history on |
| SYS-05 | Email marketing service and business social media accounts | SaaS | Subscriber emails and preferences | Monthly patron export uploaded by the marketing assistant. Social accounts use the owner's login on the assistant's phone |
| SYS-06 | Accounting SaaS | SaaS | Vendor and artist payment details; business bank data | MFA on; the bookkeeper has its own login |
| SYS-07 | Endpoints: the owner's laptop, the owner's phone, and 2 business-owned scanning phones | Owner devices | Yes (cached exports on the laptop; email, texts, and the authenticator app on the phone) | Laptop has built-in full-disk encryption on and automatic updates. Phone has a passcode and automatic updates. Scanning phones are old phones with only the scanner app, a passcode, and the shared door login |
| SYS-08 | The Room's internet and Wi-Fi | Landlord-provided internet; ISP router in the office | In transit only | One Wi-Fi network for the laptop, scanning phones, the sound engineer, and touring crews. The password is posted backstage. The router still uses its default administrator password |

**SSP system (P02):** the *Ticketing and Venue Operations Platform (TVOP)*: the owner's accounts, settings, and data in SYS-01 to SYS-06, the endpoints in SYS-07, and the Room's network SYS-08.

## 4. Current security posture: informal, basic hygiene with big gaps
**In place today:**
- Online card payments are entered only in the hosted checkout. The payment fields come from the processor, and the owner never sees full card numbers in SYS-01 or SYS-02
- MFA on email (SYS-04), the processor portal (SYS-02, enforced by the processor), and accounting (SYS-06)
- Built-in full-disk encryption, automatic updates, and built-in antivirus on the laptop; passcode and automatic updates on the phones
- The ticketing vendor's platform backups, and version history in cloud file storage
- The ticketing platform's bot protection (vendor default settings) and a posted limit of 6 tickets per order
- General liability insurance for events

**Missing:**
1. SAQ A eligibility is not true today. The owner keys phone orders into the SYS-01 box office order screen on the laptop (about 120 orders in the last 12 months), and some fans email or text their card details. The 2025 SAQ A was attested "yes" throughout without checking eligibility. There is no PCI DSS scope description.
2. No MFA on the ticketing platform or the website builder, and both use the same password.
3. The marketing assistant signs in with the owner's own ticketing and website logins.
4. Three third-party scripts run on the website pages that embed the checkout. None was reviewed. The SAQ A script eligibility criterion has not been confirmed.
5. The shared "door" scanner login has not changed since 2024, and the scanner role can search patron names and emails.
6. Full patron exports are downloaded every month and kept on the laptop and in cloud storage with no retention rule.
7. No incident plan, no contact list, and the owner did not know the merchant agreement's 24-hour notice term (fictional).
8. No written security policies and no security training.
9. The Room's Wi-Fi is one network shared with crews and artists, and the router has its default administrator password.
10. No review of the ticketing platform's activity log, payout changes, or website changes.
11. No cyber insurance. Whether the general liability policy covers any cyber loss is unconfirmed.
12. The smart pricing feature was turned on for 8 shows without a review of total-price display, artist price caps, or accessible seating prices. Social posts and flyers advertise "$X plus fees".
13. No list of service providers and no check of the ticketing vendor's or processor's PCI DSS compliance status.
14. The owner is a single point of failure: every credential and the only authenticator app are on one phone, with no stored recovery codes.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 primary standard | PCI DSS v4.0.1 (contractual), with FTC Act Section 5 and the Rule on Unfair or Deceptive Fees (16 CFR Part 464) as the secondary regulation, Fla. Stat. 501.171(2) and (8), and a one-row BOTS Act applicability check |
| P08 incident | Registry default "Ticketing platform breach exposing customer and card data", **adapted**: takeover of the owner's ticketing platform and website accounts (reused password, no MFA), followed by a patron export and a card-skimming script placed on the website pages that embed the checkout. Adapted because an SAQ A merchant holds no card data of its own; at this size card data is exposed through the owner's accounts and web pages, not through a breach of the vendor's platform |
| P09 SOC 2 | Security criteria only, as the owner's self-check, plus a review of the ticketing vendor's SOC 2 Type 2 report. PCI DSS validation (SAQ A) is the assurance the processor asks for; a sole proprietor would not obtain a SOC 2 report |
| P10 AI | Registry default "Dynamic ticket pricing and bot detection", **adapted** to one third-party tool: the ticketing platform's smart pricing and bot protection features (AI-001). The owner configures them and cannot see the models. A consumer generative AI chatbot used for drafting posts is inventoried as AI-002 |
| Cloud | SaaS only. No IaaS or PaaS |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2025-10-14 | 2025 SAQ A completed in the processor's portal |
| 2026-06-15 | Portal notice: the 2026 SAQ A is due 2026-10-31 |
| 2026-07-27 to 2026-07-31 | Self-assessment with the on-call IT consultant (tests on 2026-07-29; show night observed on 2026-07-30) |
| 2026-08-10 to 2026-08-12 | SOC 2 self-check, ticketing vendor report review, and AI use assessment |
| 2026-08-31 | Deliverables adopted by the owner |
| 2026-10-31 | 2026 SAQ A due in the processor's portal |

## 7. Facts added while building the deliverables (Phase 5)
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| Card data found | On 2026-07-28 the owner and the IT consultant searched the mailbox and phone. They found 23 emails (2023 to 2026) and 4 text messages from fans with full card numbers, 19 of them with the security code. No card numbers were found in files on the laptop or in cloud storage. The emails and texts were deleted from all folders, including trash, on 2026-07-31 | P01, P03, P07 |
| Phone orders | Phone orders are keyed into the SYS-01 box office order screen in the laptop browser while the caller waits. Nothing is written down. The owner will instead send a payment link by text or email (an SYS-01 feature) from 2026-09-01 | P02, P03, P06 |
| Website scripts and new finding | P07 testing on 2026-07-29 found the previous freelance assistant (engaged until 2025-11) still listed as an administrator on the website builder. The owner removed the account the same day. The chat widget plugin can add code to every page, including event pages | P01, P03, P07 |
| Share links | 4 patron export files in cloud storage had "anyone with the link" sharing on, created for the marketing assistant (found 2026-07-28, turned off the same day) | P01, P04, P07 |
| Export retention | 19 monthly patron exports (2024-12 to 2026-07) were on the laptop and in cloud storage on 2026-07-28 | P01, P03, P07 |
| Vendor assurance | The ticketing vendor's PCI DSS AOC as a service provider is dated 2026-03-12 and the processor's is dated 2026-01-30; both were downloaded from the vendors' trust pages on 2026-07-28. The ticketing vendor's SOC 2 Type 2 report (Security and Availability, 12 months to 2026-03-31) was obtained under a nondisclosure agreement and reviewed on 2026-08-11 | P02, P03, P09 |
| Processor notice term | The merchant agreement requires notice to the processor's risk team immediately, and no later than 24 hours, after the merchant suspects a compromise of card data (fictional term) | P03, P08 |
| Payout alerts | SYS-01 emails the owner when payout bank details change, but the owner had never tested it. The test on 2026-07-29 showed the alert goes only to the account email (the owner's) | P01, P07, P08 |
| Smart pricing use | Smart pricing ran in "auto-apply" mode on 8 shows from 2026-05-01 to 2026-07-31 (5 seated, 3 standing), making 37 price changes. On 1 show the price exceeded the artist's agreed cap by 12% for 4 days. Accessible seating stayed at or below same-section prices on all 5 seated shows, but no rule enforces that | P01, P10 |
| Bot protection | The vendor's bot protection is on for every on-sale. On the 2 sold-out on-sales of 2026 it blocked 610 sessions; 3 fans emailed that they were blocked, and there is no appeal route beyond emailing the owner | P10 |
| Fee display | A review of 20 social posts and 6 flyers from 2026 found 17 posts and all 6 flyers showing "$X plus fees" without the total price. The ticketing platform's event pages and checkout show the total price | P03, P10 |
| Generative AI use | The marketing assistant uses a consumer generative AI chatbot (free plan) to draft show descriptions and posts. Once, in 2026-06, a patron complaint email with the patron's name and email was pasted into it | P10 |
| Cyber insurance | No cyber policy. The general liability policy excludes data breach costs (read on 2026-07-30) | P01, P08 |
| Recovery codes | The owner saved recovery codes for email, the processor portal, and accounting on 2026-07-31 and keeps them, with an emergency access sheet, in a sealed envelope held by the owner's attorney (POL-01 7.6) | P01, P05, P06 |
| Router | The ISP router's administrator password was changed from the default on 2026-07-29 during testing. A separate guest network for crews and artists is planned | P01, P07 |
