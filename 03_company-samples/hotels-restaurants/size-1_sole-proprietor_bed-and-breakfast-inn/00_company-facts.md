# Scenario facts: Cris Santos Company | Accommodation and Food Services | Sole Proprietorship

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a law, regulation, or standard, the citation is given. Facts about the payment facilitator, its agreement, and vendors are fictional.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship; the owner-innkeeper files Schedule C) |
| Business | One **six-room bed-and-breakfast inn** (NAICS 721191) in a restored historic family home. Breakfast is served to overnight guests only. Florida classifies it as a bed and breakfast inn: "a family home structure, with no more than 15 sleeping rooms," modified to serve as a transient public lodging establishment (Fla. Stat. 509.242(1)(f)) |
| Location | Florida, in a small historic coastal town. The owner lives in an owner's apartment in the same house. Hurricane season (June to November) is the main natural hazard |
| Workforce | The owner-innkeeper only (0 employees). An unpaid adult family member covers as relief innkeeper. Cleaning, bookkeeping, and IT help are contracted |
| Guests | About 600 stays a year (about 1,100 room-nights, about 50% occupancy). The innkeeping software holds about 3,400 guest profiles created since it was adopted in 2019. About 55% of guests live in Florida; most others live in other states |
| Revenue | About $180,000 a year (fictional): average daily rate about $155 with breakfast included, plus a **mandatory $15 per-stay housekeeping fee**. SBA-small (standard $9.0 million in average annual receipts for NAICS 721191, 13 CFR 121.201) |
| Card acceptance | About 1,050 card transactions a year (about $165,000), all as a **sub-merchant of a payment facilitator** that is integrated with the innkeeping software: about 420 booking engine deposits, about 160 online travel agency (OTA) virtual cards charged through the innkeeping software, about 120 phone bookings keyed by the owner, and about 350 card-present payments at check-in on a mobile reader |
| PCI DSS status | **Merchant (sub-merchant).** PCI DSS v4.0.1 applies through the payment facilitator's sub-merchant agreement (contract, not law). The agreement (fictional terms) requires annual validation by self-assessment questionnaire (SAQ) in the facilitator's compliance portal, and notice to the facilitator within 24 hours of suspecting a compromise. **The owner has never completed validation.** Since March 2024 the facilitator has charged a $19.95 monthly PCI non-compliance fee (fictional) |
| Payment design | **Booking engine:** a vendor-hosted booking and payment page on the innkeeping vendor's own web address; the inn's website only links to it, and the inn receives a token. **OTA reservations:** virtual card numbers arrive through the channel manager into the innkeeping software's card vault; the owner's administrator account can display full numbers. **Phone bookings:** the owner keys card numbers into the innkeeping software's payment screen in a browser on the laptop, or, when away from the laptop, writes them on a paper reservation pad (with the security code) and keys them later. **Card authorization forms:** third-party payers (wedding parties, parents) email forms with card numbers. **Card-present:** a chip and contactless mobile reader paired with the facilitator's app on the owner's phone. The facilitator's documentation says the reader is part of a **PCI-listed validated P2PE solution**; the owner confirmed the listing on the PCI SSC website on 2026-07-21 |
| Franchise status | **Independent; no brand or franchisor.** In *FTC v. Wyndham Worldwide Corp.*, 799 F.3d 236 (3d Cir. 2015), the court affirmed that the FTC may challenge unreasonable cybersecurity as an unfair practice under 15 U.S.C. 45(a), in a case about a franchisor that managed its branded hotels' systems. With no franchisor, the owner alone carries these duties |
| Not in scope | **FTC Disposal Rule (16 CFR 682.3):** the inn obtains no consumer reports (no employees, no background checks, no tenant screening). **Illinois BIPA (N72-R05):** no Illinois operations and no biometric collection. **CIRCIA (N72-R06):** proposed only, and the inn is far below the SBA size standard. **HIPAA, FTC Safeguards and Red Flags Rules:** not a covered entity; no consumer credit. **CCPA:** no California operations, and revenue is far below its thresholds. **Florida Digital Bill of Rights:** a "controller" under Fla. Stat. 501.702 must exceed $1 billion in global gross annual revenue and meet one of three further tests (50% or more of revenue from online advertising, a smart speaker and voice command service, or an app store with at least 250,000 applications); the inn meets none. **SEC:** not publicly traded. **Federal contracts:** none |
| Other applicable law | FTC Act Section 5, 15 U.S.C. 45(a) and (n), for guest data security, privacy statements, and price claims (N72-R02); FTC Rule on Unfair or Deceptive Fees, **16 CFR Part 464** (90 FR 2066, rule text at 2166; published 2025-01-10; effective 2025-05-12), whose "covered good or service" includes short-term lodging "at a hotel, motel, inn, short-term rental, vacation rental, or other place of lodging" (464.1); Florida guest register, **Fla. Stat. 509.101(2)**; Florida reasonable security, disposal, and breach notice, **Fla. Stat. 501.171** (a "covered entity" expressly includes a sole proprietorship, 501.171(1)(b)) (N72-R04); Florida unconscionable prices during a declared state of emergency, **Fla. Stat. 501.160** (P10 pricing) |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notice, guest register, emergency pricing). Other states are treated generically ("each state where affected individuals reside") |

## 2. People and contracted services (role titles only)
| Role | Duties |
|---|---|
| Owner-innkeeper | Every role: owner, security and privacy lead, PCI DSS contact with the payment facilitator, risk acceptor, incident commander. Runs reservations, check-ins, breakfast, and the books |
| Relief innkeeper (unpaid adult family member) | Covers about two weekends a month and the owner's days off: check-ins, phone bookings, breakfast. **Uses the owner's logins** to the innkeeping software and one OTA portal |
| Cleaning service (contractor) | Two cleaners turn rooms daily. Use the house master door code (unchanged since 2022). No access to any system |
| Bookkeeper (contractor, remote) | Monthly bookkeeping and Florida sales and tourist development tax returns in the accounting SaaS, through its own user account |
| On-call IT consultant | Hourly help with the laptop, router, and door locks. Signed a confidentiality agreement on 2026-07-17. Uses a remote-support tool only when the owner starts a session |
| Key vendors | Innkeeping software vendor; payment facilitator; two OTAs; consumer email and file provider; accounting SaaS vendor; website builder; smart lock vendor; internet service provider |

## 3. Systems
| ID | System | Hosting | Card or personal data? | Notes |
|---|---|---|---|---|
| SYS-01 | Innkeeping software: reservations calendar, guest profiles, folios, guest register, booking engine, channel manager, guest messaging, door code integration | Vendor SaaS | Guest names, addresses, phones, emails, stay history; card tokens; **full OTA virtual card numbers in the vendor's vault, displayable by the administrator** | System of record. One administrator account, **shared with the relief innkeeper**. MFA available but off. Vendor holds a SOC 2 Type 2 report (Security and Availability, 12 months ending 2026-03-31) and a PCI DSS service provider attestation of compliance (AOC) |
| SYS-02 | Integrated payments from the payment facilitator: processing, card vault, pay-by-link (available, unused), phone app with a Bluetooth mobile reader | Service provider plus the reader | Card data on the provider side; the reader encrypts at the card (validated P2PE solution) | Facilitator AOC (service provider) obtained 2026-07-22. Receipts show only the last 4 digits |
| SYS-03 | OTA partner portals (two OTAs) | OTA extranets | Reservations, guest names and messages, virtual card numbers (displayable) | OTA-1 sends a sign-in code to the owner's phone. OTA-2 uses a password only (MFA available, off); its login is shared with the relief innkeeper |
| SYS-04 | Email, file storage, and photo backup (consumer account) | SaaS | **Yes: about 85 emails with card numbers (31 with security codes) back to 2022; guest ID photos synced from the phone** | Personal consumer account used for the inn. Password only, no MFA |
| SYS-05 | Accounting SaaS | Vendor SaaS | Payout and bank records; no card numbers | MFA enforced by the vendor. Bookkeeper has a named user |
| SYS-06 | Inn website (website-builder SaaS) | Vendor SaaS | Contact form messages | Rooms, rate table, policies, privacy statement, link to the booking engine, and the AI chat widget (SYS-11). The rate table shows nightly rates without the housekeeping fee. The privacy statement says "we never store your card details" |
| SYS-07 | Laptop | Owner device | Yes: keyed card numbers pass through its browser; saved passwords; downloaded reports | Used for the inn and by family for personal browsing and games. Passwords saved in the browser. No full-disk encryption. Built-in antivirus; automatic updates |
| SYS-08 | Mobile phone | Owner's personal device | Yes: guest ID photos; guest texts; payment app | Payment app and reader; OTA, innkeeping, and email apps; sign-in codes for OTA-1 and the accounting SaaS. Passcode and device encryption on. About 1,900 guest ID photos in the camera roll since 2021 |
| SYS-09 | Inn network | ISP-provided router | Card data in transit (keyed entry on the laptop) | One network for guest Wi-Fi and the owner's devices. Wi-Fi password printed in every room. Router administrator password is still the default. Firmware never updated |
| SYS-10 | Smart door locks: keypads on the front door and 6 guest rooms | Lock vendor cloud app | Guest names and room assignments | Per-reservation codes sent by the innkeeping software and expiring at checkout. One house master code (owner, relief innkeeper, cleaners) unchanged since 2022. Mechanical override keys in a lockbox |
| SYS-11 | AI add-on in the innkeeping software: rate suggestions and a website guest chat assistant | Vendor SaaS | Guest questions and contact details in chat transcripts; booking and rate history | Turned on 2026-05-01. Rate suggestions auto-apply. See P10 |

**SSP system (P02):** the *Inn Business Systems Profile (IBSP)*: SYS-01 to SYS-11, the owner's SaaS stack (reservations, payments, OTA portals, email and files, accounting, website, AI add-on), the laptop and phone, the inn network, and the door locks.

## 4. Current security posture: early (few formal controls)
**In place today:**
- Booking engine payments on the innkeeping vendor's hosted page; the inn receives tokens only
- Card-present payments on a PCI-listed validated P2PE mobile reader; truncated receipts
- MFA enforced by the accounting SaaS; sign-in codes on OTA-1
- The innkeeping vendor's backups, SOC 2 Type 2 report, and PCI DSS AOC; the payment facilitator's AOC
- Automatic operating system updates and built-in antivirus on the laptop and phone; phone passcode and encryption
- Per-reservation door codes that expire at checkout
- A home cross-cut shredder for paper

**Missing:**
1. PCI DSS validation has never been completed; the facilitator charges a monthly non-compliance fee. Nobody has listed where card data flows or is stored.
2. Phone bookings are keyed on the general-purpose family laptop, and card numbers with security codes are written on a paper reservation pad. About 140 pad pages since 2023 sit in an unlocked desk drawer.
3. About 85 emails with card numbers (31 with security codes) sit in the consumer email account, back to 2022.
4. No MFA on the innkeeping software, OTA-2, or email. Passwords are saved in the laptop browser, and one password is reused for the innkeeping software and email.
5. Shared access: the relief innkeeper uses the owner's logins, and the house master door code has not changed since 2022 (former cleaners know it).
6. Full OTA virtual card numbers can be displayed in the innkeeping software and the OTA portals, and the owner displays them about once a month to check a declined card.
7. The owner photographs every guest's driver license or passport at check-in. About 1,900 ID photos sit in the phone camera roll and sync to the consumer photo backup, with no retention limit.
8. The laptop is not encrypted and is shared with family.
9. One router serves guest Wi-Fi and the owner's devices; its administrator password is the default and its firmware has never been updated.
10. No incident plan and no contact list. The owner did not know the facilitator's 24-hour notice term.
11. No backup of laptop files (contracts, receipts, tax documents); the innkeeping data has never been exported.
12. The website rate table, phone quotes, and AI chat answers show nightly rates without the mandatory $15 housekeeping fee, and the booking engine adds the fee only at the final payment step (16 CFR 464.2).
13. The AI add-on applies rate suggestions automatically with no ceiling and no rule for a declared state of emergency (Fla. Stat. 501.160). The chat assistant quotes rates without the fee, and guests have typed card numbers into chat.
14. No security training. The owner has never had any.
15. The website privacy statement says "we never store your card details," which is not true while the paper pad and email forms exist (15 U.S.C. 45(a)).

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
| 2026-07-17 | On-call IT consultant signs a confidentiality agreement |
| 2026-07-20 to 2026-07-24 | Self-assessment with the on-call IT consultant (inn walkthrough 2026-07-21; tests 2026-07-23) |
| 2026-08-14 | Payment facilitator email accepting SAQ A plus SAQ P2PE after the design changes |
| 2026-08-24 to 2026-08-25 | AI add-on assessment (P10) |
| 2026-08-31 | Deliverables adopted by the owner-innkeeper |
| 2026-12-31 | 2026 SAQs and attestations of compliance due to the payment facilitator |

## 7. Facts added while building the deliverables
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| Placeholder | Filled in as the deliverables are built | |
