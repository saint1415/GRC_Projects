# Scenario facts: Cris Santos Company | Accommodation and Food Services | Sole Proprietorship

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a law, regulation, or standard, the citation is given. Facts about the payment facilitator, its agreement, and vendors are fictional.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship; the owner-innkeeper files Schedule C) |
| Business | One **six-room bed-and-breakfast inn** (NAICS 721191) in a restored historic family home. Breakfast is served to overnight guests only. Florida classifies it as a bed and breakfast inn: "a family home structure, with no more than 15 sleeping rooms," modified to serve as a transient public lodging establishment (Fla. Stat. 509.242(1)(f)) |
| Location | Florida, in a small historic coastal town. The owner lives in an owner's apartment in the same house. Hurricane season (June to November) is the main natural hazard |
| Workforce | The owner-innkeeper only (0 employees; EV-025). An unpaid adult family member covers as relief innkeeper. Cleaning, bookkeeping, and IT help are contracted |
| Guests | About 600 stays a year (about 1,100 room-nights, about 50% occupancy). The innkeeping software holds about 3,400 guest profiles created since it was adopted in 2019. About 55% of guests live in Florida; most others live in other states (EV-004) |
| Revenue | About $180,000 a year (fictional; EV-025): average daily rate about $155 with breakfast included, plus a **mandatory $15 per-stay housekeeping fee**. SBA-small (standard $9.0 million in average annual receipts for NAICS 721191, 13 CFR 121.201) |
| Card acceptance | About 1,050 card transactions a year (about $165,000), all as a **sub-merchant of a payment facilitator** that is integrated with the innkeeping software: about 420 booking engine deposits, about 160 online travel agency (OTA) virtual cards charged through the innkeeping software, about 120 phone bookings keyed by the owner, and about 350 card-present payments at check-in on a mobile reader (EV-008) |
| PCI DSS status | **Merchant (sub-merchant)**, determined in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (N72-R01). PCI DSS v4.0.1 applies through the payment facilitator's sub-merchant agreement (contract, not law). The agreement (fictional terms) requires annual validation by self-assessment questionnaire (SAQ) in the facilitator's compliance portal, and notice to the facilitator within 24 hours of suspecting a compromise (EV-009). **The owner has never completed validation.** Since March 2024 the facilitator has charged a $19.95 monthly PCI non-compliance fee (fictional; EV-007) |
| Payment design | Sources: EV-005, EV-007, EV-010, EV-011, EV-018, EV-020, EV-036. **Booking engine:** a vendor-hosted booking and payment page on the innkeeping vendor's own web address; the inn's website only links to it, and the inn receives a token. **OTA reservations:** virtual card numbers arrive through the channel manager into the innkeeping software's card vault; the owner's administrator account can display full numbers. **Phone bookings:** the owner keys card numbers into the innkeeping software's payment screen in a browser on the laptop, or, when away from the laptop, writes them on a paper reservation pad (with the security code) and keys them later. **Card authorization forms:** third-party payers (wedding parties, parents) email forms with card numbers. **Card-present:** a chip and contactless mobile reader paired with the facilitator's app on the owner's phone. The facilitator's documentation says the reader is part of a **PCI-listed validated P2PE solution**; the owner confirmed the listing on the PCI SSC website on 2026-07-21 |
| Franchise status | **Independent; no brand or franchisor.** In *FTC v. Wyndham Worldwide Corp.*, 799 F.3d 236 (3d Cir. 2015), the court affirmed that the FTC may challenge unreasonable cybersecurity as an unfair practice under 15 U.S.C. 45(a), in a case about a franchisor that managed its branded hotels' systems. With no franchisor, the owner alone carries these duties |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv). **FTC Disposal Rule (16 CFR 682.3):** the inn obtains no consumer reports (no employees, no background checks, no tenant screening). **Illinois BIPA (N72-R05):** no Illinois operations and no biometric collection. **CIRCIA (N72-R06):** proposed only, and the inn is far below the SBA size standard. **HIPAA, FTC Safeguards and Red Flags Rules:** not a covered entity; no consumer credit. **CCPA:** no California operations, and revenue is far below its thresholds. **Florida Digital Bill of Rights:** a "controller" under Fla. Stat. 501.702 must exceed $1 billion in global gross annual revenue and meet one of three further tests (50% or more of revenue from online advertising, a smart speaker and voice command service, or an app store with at least 250,000 applications); the inn meets none. **SEC:** not publicly traded. **Federal contracts:** none |
| Other applicable law | Recorded in the intake [obligations register](step-00_P00_intake/obligations-register.csv). FTC Act Section 5, 15 U.S.C. 45(a) and (n), for guest data security, privacy statements, and price claims (N72-R02); FTC Rule on Unfair or Deceptive Fees, **16 CFR Part 464** (90 FR 2066, rule text at 2166; published 2025-01-10; effective 2025-05-12), whose "covered good or service" includes short-term lodging "at a hotel, motel, inn, short-term rental, vacation rental, or other place of lodging" (464.1); Florida guest register, **Fla. Stat. 509.101(2)**; Florida reasonable security, disposal, and breach notice, **Fla. Stat. 501.171** (a "covered entity" expressly includes a sole proprietorship, 501.171(1)(b)) (N72-R04); Florida unconscionable prices during a declared state of emergency, **Fla. Stat. 501.160** (P10 pricing) |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notice, guest register, emergency pricing). Other states are treated generically ("each state where affected individuals reside") |

## 2. People and contracted services (role titles only)
| Role | Duties |
|---|---|
| Owner-innkeeper | Every role: owner, security and privacy lead, PCI DSS contact with the payment facilitator, risk acceptor, incident commander. Runs reservations, check-ins, breakfast, and the books |
| Relief innkeeper (unpaid adult family member) | Covers about two weekends a month and the owner's days off: check-ins, phone bookings, breakfast. **Uses the owner's logins** to the innkeeping software and one OTA portal (EV-021) |
| Cleaning service (contractor) | Two cleaners turn rooms daily. Use the house master door code (unchanged since 2022; EV-017, EV-022). No access to any system |
| Bookkeeper (contractor, remote) | Monthly bookkeeping and Florida sales and tourist development tax returns in the accounting SaaS, through its own user account |
| On-call IT consultant | Hourly help with the laptop, router, and door locks. Signed a confidentiality agreement on 2026-07-17 (EV-027). Uses a remote-support tool only when the owner starts a session |
| Key vendors | Innkeeping software vendor; payment facilitator; two OTAs; consumer email and file provider; accounting SaaS vendor; website builder; smart lock vendor; internet service provider |

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv). The notes below cite the evidence for each setting.

| ID | System | Hosting | Card or personal data? | Notes |
|---|---|---|---|---|
| SYS-01 | Innkeeping software: reservations calendar, guest profiles, folios, guest register, booking engine, channel manager, guest messaging, door code integration | Vendor SaaS | Guest names, addresses, phones, emails, stay history; card tokens; **full OTA virtual card numbers in the vendor's vault, displayable by the administrator** | System of record. One administrator account, **shared with the relief innkeeper**. MFA available but off. Vendor holds a SOC 2 Type 2 report (Security and Availability, 12 months ending 2026-03-31) and a PCI DSS service provider attestation of compliance (AOC) (EV-001, EV-002, EV-021, EV-030, EV-031) |
| SYS-02 | Integrated payments from the payment facilitator: processing, card vault, pay-by-link (available, unused), phone app with a Bluetooth mobile reader | Service provider plus the reader | Card data on the provider side; the reader encrypts at the card (validated P2PE solution) | Facilitator AOC (service provider) obtained 2026-07-22. Receipts show only the last 4 digits (EV-007, EV-032) |
| SYS-03 | OTA partner portals (two OTAs) | OTA extranets | Reservations, guest names and messages, virtual card numbers (displayable) | OTA-1 sends a sign-in code to the owner's phone. OTA-2 uses a password only (MFA available, off); its login is shared with the relief innkeeper (EV-010, EV-021) |
| SYS-04 | Email, file storage, and photo backup (consumer account) | SaaS | **Yes: about 85 emails with card numbers (31 with security codes) back to 2022; guest ID photos synced from the phone** | Personal consumer account used for the inn. Password only, no MFA (EV-011, EV-012) |
| SYS-05 | Accounting SaaS | Vendor SaaS | Payout and bank records; no card numbers | MFA enforced by the vendor. Bookkeeper has a named user (EV-023) |
| SYS-06 | Inn website (website-builder SaaS) | Vendor SaaS | Contact form messages | Rooms, rate table, policies, privacy statement, link to the booking engine, and the AI chat widget (SYS-11). The rate table shows nightly rates without the housekeeping fee. The privacy statement says "we never store your card details" (EV-005, EV-006) |
| SYS-07 | Laptop | Owner device | Yes: keyed card numbers pass through its browser; saved passwords; downloaded reports | Used for the inn and by family for personal browsing and games. Passwords saved in the browser. No full-disk encryption. Built-in antivirus; automatic updates (EV-013, EV-014) |
| SYS-08 | Mobile phone | Owner's personal device | Yes: guest ID photos; guest texts; payment app | Payment app and reader; OTA, innkeeping, and email apps; sign-in codes for OTA-1 and the accounting SaaS. Passcode and device encryption on. About 1,900 guest ID photos in the camera roll since 2021 (EV-015) |
| SYS-09 | Inn network | ISP-provided router | Card data in transit (keyed entry on the laptop) | One network for guest Wi-Fi and the owner's devices. Wi-Fi password printed in every room. Router administrator password is still the default. Firmware never updated (EV-016, EV-020) |
| SYS-10 | Smart door locks: keypads on the front door and 6 guest rooms | Lock vendor cloud app | Guest names and room assignments | Per-reservation codes sent by the innkeeping software and expiring at checkout. One house master code (owner, relief innkeeper, cleaners) unchanged since 2022. Mechanical override keys in a lockbox (EV-017, EV-018) |
| SYS-11 | AI add-on in the innkeeping software: rate suggestions and a website guest chat assistant | Vendor SaaS | Guest questions and contact details in chat transcripts; booking and rate history | Turned on 2026-05-01. Rate suggestions auto-apply. See P10 (EV-028, EV-029) |

**SSP system (P02):** the *Inn Business Systems Profile (IBSP)*: SYS-01 to SYS-11, the owner's SaaS stack (reservations, payments, OTA portals, email and files, accounting, website, AI add-on), the laptop and phone, the inn network, and the door locks.

## 4. Where the evidence is
This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Every item has a source system, an owner, and as-of and collected dates. For a one-person inn the sources are the vendors' admin portals and reports, the payment facilitator's portal and statements, the bank and card statements, the inbox, signed agreements, the laptop, phone, router and lock app settings, the owner's office, the owner's and relief innkeeper's written intake answers, and the insurance agent's portal.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps against PCI DSS v4.0.1 and the short checks** are judged in the gap analysis (P03), and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P02 system | The registry default "Core business SaaS stack (email, files, client and billing records)" is kept and named the Inn Business Systems Profile. Guest (client) and billing records live in the innkeeping software, the payment facilitator, and the accounting SaaS |
| P03 primary standard | PCI DSS v4.0.1 through the sub-merchant agreement (contractual, N72-R01). Short checks: FTC Act Section 5 with 16 CFR Part 464 (N72-R02); Fla. Stat. 509.101(2), 501.171(2) and (8) (N72-R04). FTC Disposal Rule recorded as not applicable (N72-R03) |
| P03 SAQ decision | The current design would require **SAQ D for Merchants** (keyed entry on a general-purpose laptop, stored card data on paper and in email, displayed virtual cards). Decision: **change the design first**, then validate for 2026 with **SAQ A** (booking engine, pay-by-link for phone bookings, virtual cards charged without display) plus **SAQ P2PE** (mobile reader). The payment facilitator agreed by email on 2026-08-14 (fictional). Attestations due 2026-12-31 (fictional) |
| P08 incident | Registry default "Point-of-sale and reservation system compromise," adapted to an inn with no on-site POS server: an OTA-themed phishing email installs an information stealer on the laptop; saved passwords let the attacker sign in to the innkeeping software, OTA-2, and email; upcoming guests receive fake "payment verification" links; card forms and ID photos in email are exposed. Discovered when a guest calls about the message |
| P09 SOC 2 | Security criteria only. The inn is not a service organization, and PCI DSS validation is its assurance mechanism with the payment facilitator. (a) Owner's self-check; (b) review of the innkeeping vendor's SOC 2 Type 2 report |
| P10 AI | Registry default "Revenue-management pricing and guest chatbot," adapted: a sole proprietor does not buy an enterprise revenue-management system. The innkeeping vendor bundles rate suggestions and a website chat assistant in **one third-party AI add-on** (SYS-11), so the tier's "one third-party AI tool" is that add-on with its two features |
| Cloud | SaaS only. No IaaS |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-07-13 to 2026-07-17 | Intake: the owner collects portal exports, statements, agreements, device, router and lock settings, the office review, and written answers from the owner and the relief innkeeper; inventories; obligations register |
| 2026-07-17 | On-call IT consultant signs a confidentiality agreement |
| 2026-07-20 to 2026-07-24 | Self-assessment with the on-call IT consultant: BIA, risk analysis, gap analysis, and control assessment (inn walkthrough 2026-07-21; tests 2026-07-23) |
| 2026-07-22 | Vendor AOCs and the innkeeping vendor's SOC 2 report received (requested at intake) |
| 2026-07-27 to 2026-08-28 | POL-01 drafted from the gaps and the test results |
| 2026-08-14 | Payment facilitator email accepting SAQ A plus SAQ P2PE after the design changes |
| 2026-08-24 to 2026-08-25 | AI add-on assessment (P10) |
| 2026-08-31 | Deliverables and POL-01 adopted by the owner-innkeeper |
| 2026-12-31 | 2026 SAQs and attestations of compliance due to the payment facilitator |
| 2027-02 (planned) | Follow-up check: operating effectiveness of the controls POL-01 introduced, after at least one quarter of operation |

## 7. Facts added while building the deliverables
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| Innkeeping vendor assurance | The vendor's SOC 2 Type 2 system description states an RTO of 4 hours and an RPO of 1 hour, with an annual recovery test. The report has one remediated exception (a missed quarterly access review of vendor support staff). The AI add-on launched after the report period and is not in its scope. The vendor keeps the activity log for 12 months. The owner reviewed the report and requested a bridge letter on 2026-07-22 (EV-030) | P02, P03, P04, P05, P09 |
| Daily revenue | About $490 a day on average and up to about $930 a night when all six rooms are full; about $3,200 of card payments a week (EV-025, EV-004, EV-008) | P05 |
| Continuity today | No relocation arrangement with another inn exists. The owner already prints a weekly arrivals list for the cleaners and shreds it each week. The relief innkeeper is the natural backup operator once given a named account (EV-033, EV-018) | P05, P07, POL-01 |
| Device settings | The phone locks after 30 seconds. The laptop locks after 20 minutes, and family members know its password. 18 passwords are saved in the laptop's browser, several under 10 characters (EV-013, EV-014, EV-015) | P02, P07 |
| Office and cleaners | The owner's office holds the laptop, the reader, and the pad, and is not locked during the day. The cleaners do not clean the office. One cleaner left the cleaning service in 2024 and the master code was not changed (EV-018, EV-022, EV-017) | P02, P03, P07 |
| Door codes | Per-reservation codes are random 6-digit codes generated by the innkeeping integration (EV-017) | P07 |
| Router | The ISP router has a guest network feature that was never turned on. P07 testing on 2026-07-23 found internet-side remote management turned on; the IT consultant turned it off that day (EV-016, EV-CM-6) | P01, P02, P07 |
| Lock installer account | P07 testing on 2026-07-23 found the lock installer's administrator account in the lock app still active since the 2022 installation. The owner disabled it the same day (EV-SA-9) | P01, P02, P04, P07 |
| Pad stopped | After the walkthrough on 2026-07-21 the owner stopped writing new card numbers on the pad; existing pages remain until shredded (EV-034) | P01 |
| Reader serial | The P2PE reader's serial number was first recorded on 2026-07-23 (EV-039) | P02, P03 |
| Insurance | No standalone cyber insurance. Whether the business owner's insurance policy has a data breach endorsement is unconfirmed (owner action in P08; EV-024, EV-026) | P08, P09 |
| Fee display details | The booking engine shows taxes and the final amount before payment. The OTA-2 listing calls the $15 fee a "resort fee" although the inn has no resort amenities (EV-038) | P03 |
| AI add-on details | Terms read on 2026-08-24: rate suggestions use the inn's own booking history and public OTA rates, and the inn's non-public data is not shared with other inns; chat transcripts are kept with no deletion period. From May to August 2026 the add-on made 214 automatic rate changes; the highest applied rate was $289 on a festival weekend. A 20-question chat test on 2026-08-24 got 18 right, and 0 of 8 rate answers included the fee. 4 transcripts contain card numbers (EV-041 to EV-043) | P03, P04, P10 |
| Costs | Password manager about $40 a year; business email and file plan about $100 a year; pay-by-link included in the facilitator's fees; IT consultant billed hourly | P01, P07 |
