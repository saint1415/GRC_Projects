# Scenario facts: Cris Santos Company | Accommodation and Food Services | Micro

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a law, regulation, standard, or court decision, the citation is given. Facts about the acquirer, the merchant agreement, the franchise offer, and vendors are fictional.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (independent motel operator; privately held) |
| Business | Owns and operates **one independent 38-unit roadside motel** (NAICS 721110): a two-story exterior-corridor building with free parking, guest Wi-Fi, coffee and a packaged breakfast, a coin guest laundry, and a small **lobby market** (snacks, drinks, toiletries) sold at the front desk. It meets Florida's motel classification: rental units with an exit to the outside, daily or weekly rates, off-street parking for each unit, a central office, a bathroom for each unit, and at least six units (Fla. Stat. 509.242(1)(b)). The front desk is staffed 24 hours. The Owner-Manager lives in the manager's apartment on site |
| Location | Florida, beside an interstate exit about 70 miles inland. Hurricane season (June to November) is the main natural hazard: power loss, and surges of evacuees when coastal counties evacuate. The motel's county is inside the declared area in most statewide emergency declarations |
| Franchise status | **Independent; never franchised.** The owner bought the motel from its previous independent owner in 2018. In June 2026 an economy brand sent a franchise proposal; the decision is deferred to 2027. A franchise would mandate the brand's property management system and its PCI program. In *FTC v. Wyndham Worldwide Corp.*, 799 F.3d 236 (3d Cir. 2015) (No. 14-3514, opinion filed 2015-08-24), the court affirmed that the FTC may challenge unreasonable cybersecurity as an unfair practice under 15 U.S.C. 45(a), in a case about a franchisor that managed its branded hotels' property management systems. As an independent, Cris Santos Company alone carries these duties today |
| Workforce | **7 employees:** Owner-Manager, Assistant Manager, 2 Front Desk Clerks (day and evening), 1 Night Auditor, 1 Head Housekeeper, 1 Housekeeper and Laundry Attendant. A contracted handyman does maintenance. A contracted bookkeeper keeps the books remotely |
| Revenue | About **$1.1 million** a year (fictional): rooms about $1.04 million (about 10,300 room-nights, occupancy about 74%, average base rate about $95 plus a **mandatory $6 per night property service fee** that covers Wi-Fi, parking, and breakfast); lobby market, laundry, and pet fees about $60,000. About $3,000 a day. Under the SBA standard of $40.0 million for NAICS 721110 (13 CFR 121.201), so SBA-small |
| Guests | About 5,900 stays a year. About 30% of room-nights come from **work crews** (utility line, road construction, and storm restoration contractors) on stays of one to four weeks, under 14 crew accounts. The PMS holds about 31,000 guest profiles created since the 2019 move to the cloud PMS, including about **14,000 scanned driver licenses and ID cards** taken at check-in since 2021 |
| Card acceptance | About 13,800 card transactions a year under **one merchant account** with an acquirer (fictional terms), processed by a payment gateway integrated with the PMS: about 7,600 card-present at the front desk (rooms, deposits, lobby market); about 2,400 **keyed card-not-present** (phone reservations, no-show charges, and about 700 charges from crew card authorization forms); about 2,100 online travel agency (OTA) virtual cards charged through the PMS; and about 1,700 booking engine prepayments |
| PCI DSS status | **Merchant.** PCI DSS v4.0.1 applies through the merchant agreement (contract, not law). The Owner-Manager submitted a **2025 SAQ P2PE** in December 2025 on the gateway sales representative's advice when the current terminals were installed in 2024. The acquirer's PCI program notice dated 2026-05-11 (fictional) asks the motel to confirm SAQ eligibility because the gateway reports keyed card-not-present transactions. The 2026 attestation of compliance is due **2026-12-31** (fictional). Merchant levels are set by the card brands and were not verified, so no level number is stated |
| Payment design | **Front desk card-present:** 2 countertop terminals in a **PCI-listed validated P2PE solution** offered by the gateway, semi-integrated with the PMS (the PMS sends the amount; the terminal sends encrypted card data to the gateway). The listing was confirmed on the PCI SSC website on 2026-07-15. **Phone reservations and no-shows:** clerks key card numbers into the PMS payment screen in a browser on the shared front desk PC. **Crew billing:** crew companies email card authorization forms (many with the card security code) to the shared front desk mailbox; clerks print them into the "crew billing binder" at the front desk and key the numbers into the PMS. **OTA virtual cards:** delivered through the PMS channel manager into the PMS card vault; any user with the "view full card number" permission can display them. **Booking engine:** the PMS vendor's hosted booking and payment page on the vendor's own web address; the motel website only links to it and the motel receives a token. **Lobby market:** rung up in the PMS point-of-sale module and paid on the same terminals or posted to the room |
| Not in scope | **CIRCIA (N72-R06):** proposed only, and the motel is far below the SBA size standard. **Illinois BIPA (N72-R05):** no Illinois operations or employees, and no biometric collection (the time clock uses PINs; CCTV has no facial recognition). **FTC Safeguards Rule and Red Flags Rule:** no consumer credit is extended (two crew companies are invoiced as business accounts). **CCPA:** no California business; revenue far below its thresholds. **Florida Digital Bill of Rights:** a "controller" under Fla. Stat. 501.702 must exceed $1 billion in global gross annual revenue and meet one of three further tests (50% or more of revenue from online advertising, a smart speaker and voice command service, or an app store with at least 250,000 applications); the motel meets none. **HIPAA:** not a covered entity. **SEC:** privately held. **Federal contracts:** none |
| Other applicable law | FTC Act Section 5, 15 U.S.C. 45(a) and (n), for guest data security, privacy statements, and price claims (N72-R02); FTC Rule on Unfair or Deceptive Fees, **16 CFR Part 464** (90 FR 2066, rule text at 2166; published 2025-01-10; effective 2025-05-12), which covers short-term lodging "at a hotel, motel, inn" (464.1) and applies to businesses offering goods or services "in physical locations" as well as online (464.1, definition of business); FTC Disposal Rule, 16 CFR 682.3, for background-check reports on front desk applicants (N72-R03); Florida guest register, **Fla. Stat. 509.101(2)**; Florida reasonable security, disposal, and breach notice, **Fla. Stat. 501.171** (N72-R04); Florida unconscionable prices during a declared state of emergency, **Fla. Stat. 501.160** (P10 pricing) |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notice, guest register, emergency pricing). Other states are treated generically ("each state where affected individuals reside"); most transient guests and many crew members live outside Florida |

## 2. People and contracted services (role titles only)
| Role | Security and privacy duties |
|---|---|
| Owner-Manager | Owns the business and the merchant agreement; signs the SAQ and attestation; accepts Moderate risks and approves treatment plans for High risks; approves policies and spending; holds the cyber insurance policy; business owner of the dynamic pricing tool (P10) |
| Assistant Manager | Designated in writing (2026-07-01) as the **Security and Privacy Lead** and day-to-day PCI DSS contact; front desk lead; manages PMS, email, and lock system accounts; incident lead; liaison with the MSP and the bookkeeper |
| Front Desk Clerks (2) and Night Auditor | Check-in and check-out, phone reservations, key cards, lobby market, night audit and guest register |
| Head Housekeeper | Room status on the housekeeping tablets; lost-and-found (including ID documents left in rooms) |
| Housekeeper and Laundry Attendant | Room cleaning and laundry; no system access beyond the housekeeping tablet |
| Managed service provider (MSP, external) | Firewall, Wi-Fi, patching and antivirus on the 3 PCs, and the cloud backup. Response time 4 business hours; no recovery time commitment |
| Contracted bookkeeper (remote) | Monthly bookkeeping and Florida sales and tourist development tax returns in the accounting SaaS, under a named user |
| Contracted handyman | Maintenance; no system access |
| Key vendors (external) | PMS vendor; payment gateway and P2PE solution provider; acquirer; door lock vendor; productivity suite vendor; dynamic pricing tool vendor; background-check company; payroll service; internet service provider; cyber insurer |

**Overlapping roles.** The Assistant Manager both runs and checks most controls. This is compensated by the Owner-Manager's monthly review, the MSP's reports, an independent assessor for P07, and the vendors' SOC 2 reports and PCI attestations.

## 3. Systems
| ID | System | Hosting | Card or personal data? | Notes |
|---|---|---|---|---|
| SYS-01 | All-in-one cloud PMS: reservations, guest profiles, folios, guest register and night audit, housekeeping module, point-of-sale module for the lobby market, booking engine, channel manager to 3 OTAs, and card vault | Vendor SaaS | Guest profiles, ID scans, stay history; tokens; **full OTA virtual card numbers in the vendor's vault** | System of record. Administrators (Owner-Manager, Assistant Manager) use MFA; other users do not. Every front office user has the "view full card number" permission. Vendor holds a SOC 2 Type 2 report (Security and Availability, 12 months ending 2026-03-31) and a PCI DSS service provider attestation of compliance (AOC) dated 2026-02 |
| SYS-02 | Payment gateway and 2 front desk terminals (validated P2PE solution) | Service provider plus on-premises devices | Card data, encrypted at the terminal | Semi-integrated with the PMS. Gateway also offers a virtual terminal and pay-by-link (not used). Gateway AOC dated 2026-01 and the P2PE Instruction Manual were obtained during fieldwork (2026-07-20); neither was on file before |
| SYS-03 | Endpoints | On-premises | Yes: keyed card numbers pass through the front desk PC browser; cached reports and printed forms | **Front desk PC** (one shared Windows login with automatic sign-in; used for the PMS, email, web browsing, and key card encoding); **back office PC** (named logins for the Owner-Manager and Assistant Manager; hosts the door lock software and database); Owner-Manager's laptop (encrypted); 2 housekeeping tablets; the Owner-Manager's personal phone (PMS, email, and CCTV apps) |
| SYS-04 | Motel network | On-premises | Card data in transit (keyed entry) | One business internet line, no failover. MSP-managed firewall with two networks: an **office network** shared by both PCs, both terminals, the printer, the CCTV recorder, and a staff Wi-Fi network for the tablets; and a **guest Wi-Fi network** (8 access points, client isolation, internet only, separated in 2023) |
| SYS-05 | Productivity suite (business plan): email and file storage | SaaS | **Yes: card authorization forms in the shared front desk mailbox** | 3 mailboxes: Owner-Manager and Assistant Manager (MFA on), and a **shared front desk mailbox** used by all clerks with one password and no MFA |
| SYS-06 | Electronic door lock system: lock software and database on the back office PC, USB key card encoder at the front desk, 41 electronic locks (38 guest rooms, lobby side door, laundry, pool gate) | On-premises with vendor remote support | Guest names and room assignments | Lock vendor's **always-on remote support tool** on the back office PC, with one password shared by the vendor's technicians and no MFA |
| SYS-07 | CCTV: 10 cameras and a recorder in the office | On-premises | Video | 21-day retention; remote viewing app on the Owner-Manager's phone; no facial recognition |
| SYS-08 | Accounting SaaS and payroll service (with a PIN time clock tablet) | Vendor SaaS | Payout and bank records; employee data | MFA enforced by both vendors. No biometrics |
| SYS-09 | Cloud backup service (MSP-operated) | SaaS | Copies of the back office PC and the productivity suite | Nightly, 30 days of versions; MSP console with MFA. The only cloud workload |
| SYS-10 | Dynamic pricing tool | Vendor SaaS | Occupancy, pickup, and rate history from the PMS; public competitor rates | Machine-learning rate recommendations that **publish automatically** to the PMS (and from there to the booking engine and OTAs) since 2025-03, with no ceiling and no emergency rule (see P10) |

**SSP system (P02):** the *Motel Property Management and Point-of-Sale System (MPPS)*: SYS-01 to SYS-07 and SYS-09, with interfaces to SYS-08 and SYS-10.

## 4. Current security posture: early to partial
**In place today:**
- Front desk card-present payments on a PCI-listed validated P2PE solution (SYS-02)
- Booking engine payments on the PMS vendor's hosted page; the motel receives tokens only
- The PMS vendor's backups, SOC 2 Type 2 report, and PCI DSS AOC
- MSP-managed firewall that blocks unsolicited inbound traffic; guest Wi-Fi separated from the office network with client isolation
- MSP antivirus and monthly patching on the 3 PCs; the Owner-Manager's laptop is encrypted
- MFA on the Owner-Manager and Assistant Manager email accounts, PMS administrator accounts, the accounting and payroll SaaS, and the backup console
- Nightly cloud backup of the back office PC and the productivity suite
- Receipts show only the last 4 digits of the card number
- Background checks on front desk applicants through a background-check company
- A cross-cut shredder in the back office
- A cyber liability policy with a 24x7 breach hotline (bought 2025)
- The booking engine shows the total price, including the $6 fee, since May 2025

**Missing:**
1. The **2025 SAQ P2PE was the wrong questionnaire**: keyed entry on a general-purpose PC, card data stored in email and on paper, and displayed virtual cards all fall outside SAQ P2PE eligibility. There is no PCI DSS scope document or card data-flow diagram.
2. Phone and crew card numbers are keyed into the PMS on the shared front desk PC, which is also used for email and web browsing.
3. **Stored card data:** about 640 crew card authorization emails since 2021 (about 260 with the card security code) in the shared front desk mailbox, and printed copies in the unlocked crew billing binder.
4. All 5 front office users can display full virtual card numbers in the PMS; clerks display them routinely to check balances.
5. **Shared and unprotected logins:** one shared Windows login with automatic sign-in on the front desk PC; one shared password, without MFA, for the front desk mailbox; no MFA on non-administrator PMS logins.
6. The lock vendor's always-on remote support tool uses a shared password with no MFA, on the back office PC, on the same network as the front desk PC and terminals.
7. **Flat office network:** PCs, terminals, printer, CCTV recorder, and tablets share one network.
8. No incident response plan. Staff do not know the merchant agreement's 24-hour notice term (fictional) or Visa's 3-day rule.
9. No log collection or review; the firewall keeps about 7 days of logs on the device.
10. No vulnerability scans (internal or ASV) and no endpoint detection and response (EDR); antivirus alerts reach the MSP in business hours only.
11. No security awareness training; front desk staff have no guidance on callers who pose as guests, OTAs, or vendor support.
12. No restore test since the backup was set up in 2024.
13. No retention schedule: the PMS keeps all guest profiles and about 14,000 ID scans indefinitely, although Fla. Stat. 509.101(2) only requires registers to be available for 2 years.
14. The roadside rate sign, the website "rates from" banner, and phone quotes show the base rate without the mandatory $6 fee (16 CFR 464.2).
15. The dynamic pricing tool publishes rates automatically with no ceiling and no rule for a declared state of emergency (Fla. Stat. 501.160).

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P02 system | Registry default kept: "Property management and point-of-sale system," named the Motel Property Management and Point-of-Sale System (MPPS). The point-of-sale part is the PMS point-of-sale module for the lobby market plus the P2PE terminals |
| P03 primary standard | PCI DSS v4.0.1 through the merchant agreement (contractual, N72-R01), analyzed at the requirement-group level for the current design. Short checks: FTC Act Section 5 with 16 CFR Part 464 (N72-R02); FTC Disposal Rule (N72-R03); Fla. Stat. 509.101(2), 501.171(2) and (8) (N72-R04) |
| P03 SAQ decision | The current design is not eligible for SAQ P2PE and would need **SAQ D for Merchants**. Decision: **reduce scope first**, by 2026-11-30: phone and crew payments by the gateway's pay-by-link (or keyed on the P2PE terminal keypad where the P2PE Instruction Manual allows), card forms no longer accepted, stored card data purged, virtual cards charged without display. Then validate for 2026 with **SAQ P2PE** (terminals) plus **SAQ A** (booking engine and pay-by-link). The acquirer agreed by email on 2026-08-19 (fictional), on condition that the redesign is complete before the attestation is signed; if it is not complete by 2026-12-15, the motel validates on SAQ D |
| P08 incident | Registry default "Point-of-sale and reservation system compromise," adapted to a motel with no POS server: an attacker signs in through the lock vendor's always-on remote support tool, moves across the flat office network to the shared front desk PC, and installs a keylogger that captures keyed card numbers (with security codes) and the shared mailbox password. The P2PE terminals are not affected. Discovered when a crew company reports fraud on its card, followed by an acquirer common-point-of-purchase alert |
| P09 SOC 2 | Security plus **Confidentiality**. The motel is not a service organization; PCI DSS validation is its payment assurance. The readiness self-check answers a vendor security questionnaire from the motel's largest crew client, which asks how its corporate card data and crew rosters are protected and disposed of. Also a review of the PMS vendor's SOC 2 Type 2 report |
| P10 AI | Registry default "Revenue-management pricing and guest chatbot," adapted: the motel uses a **dynamic pricing tool** (AI-001, assessed in full) and has **no guest chatbot**. The PMS vendor's AI guest messaging add-on is recorded as proposed and not enabled (AI-002), with conditions for any future switch-on; staff use of public chatbots is AI-003. The tier's "one AI use case" is AI-001 |
| Cloud | SaaS plus one cloud workload: the MSP-operated cloud backup (SYS-09). Vendor-agnostic |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-05-11 | Acquirer PCI program notice questioning the 2025 SAQ P2PE |
| 2026-07-01 | Assistant Manager designated Security and Privacy Lead in writing |
| 2026-07-13 to 2026-07-24 | BIA, risk assessment, and gap analysis with the MSP lead technician (walkthrough 2026-07-15; mailbox search 2026-07-16) |
| 2026-08-03 to 2026-08-05 | Control assessment by an independent consultant (on site 2026-08-04) |
| 2026-08-19 | Acquirer email agreeing to SAQ P2PE plus SAQ A after the redesign |
| 2026-08-20 to 2026-08-21 | SOC 2 self-check, PMS vendor report review, and AI assessment |
| 2026-08-31 | Deliverables approved by the Owner-Manager |
| 2026-11-30 | Target date for the payment redesign (scope reduction) |
| 2026-12-31 | 2026 SAQs and attestation of compliance due to the acquirer |

## 7. Facts added while building the deliverables
These facts were added because the deliverables needed them. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| Front desk volumes | About 16 arrivals a day, mostly between 3 p.m. and midnight; about 27 occupied rooms cleaned or serviced a day; about 38 card transactions a day (about $2,800). A walked guest costs about $150 in another motel's rate and goodwill | P05 |
| Door locks and keys | The locks keep working with existing cards if the lock system fails; staff hold mechanical override keys; the lock vendor needs 1 to 2 days to rebuild the lock software. POL-02 adds a sealed set of emergency key cards in the Owner-Manager's safe | P01, P05, P06, P08 |
| Lock database backup | P07 testing on 2026-08-04 found the lock database folder excluded from the MSP's backup job. The MSP added it on 2026-08-12; it has never been restore-tested | P01, P02, P04, P05, P07 |
| Lock vendor remote tool | In the P07 test the tool accepted a connection request with no prompt at the motel. The MSP set it to start only when the motel accepts a session on 2026-08-05; per-session codes and written terms are still open | P01, P02, P03, P04, P07, P08 |
| Former employees | 2 former employees (left 2026-03 and 2026-05) still had active PMS accounts on 2026-08-04; their activity logs showed no sign-ins after their last day; disabled that day. The Owner-Manager handles departures and did not tell the Assistant Manager | P01, P02, P04, P07 |
| Shared secrets | The shared front desk mailbox password has not changed since 2024 despite 3 departures. The staff Wi-Fi passphrase has not changed since 2023 | P02, P03, P04, P07 |
| Crew billing binder | A count on 2026-08-04 found 410 forms, about 160 with security codes. The binder was moved to a locked drawer in the back office on 2026-08-05 | P01, P02, P07 |
| PMS findings | 41 full card number displays in July 2026, never reviewed; minimum password length below the PCI DSS requirement; a feature to charge virtual cards without display (not used); purge settings for profiles, ID images, and folios (off); PMS-to-lock and PMS-to-pricing-tool interface credentials never changed | P03, P04, P07, P09, P10 |
| Staff awareness | 2 of 5 staff interviewed said they would give a password to a caller from "PMS support"; staff named three different people they would tell about an incident | P07, P09 |
| MSP details | MSP device policy blocks USB storage on the 3 PCs; an after-hours antivirus test alert (21:40 on 2026-08-04) was not seen until 08:15 the next day; the MSP keeps the firewall configuration backed up; evidence was requested on 2026-07-27, and the technician list and security questionnaire were not received by fieldwork end | P05, P07 |
| Administrator logins | The firewall management login uses a password only. The gateway merchant portal has MFA for the Owner-Manager but not the Assistant Manager. The website-builder account has no MFA | P03, P04, P07 |
| CCTV recorder | Still uses its installer's default administrator password (since 2022); firmware never updated; clock 9 minutes off | P02, P03, P04 |
| Website and phone quotes | The website runs on a website-builder SaaS with standard templates and links to the booking engine. Its privacy statement says card details are "processed securely by our payment partner and never stored by the motel." The phone script quotes the base rate and mentions the fee only if asked (3 test calls on 2026-07-21) | P03, P09 |
| Laptop | The Owner-Manager's laptop is used at home and elsewhere and then joins the office network; its host firewall is on by default but not enforced | P03 |
| Pay-by-link | The gateway's pay-by-link is included in the motel's gateway plan at no added fee (fictional) | P01, P03 |
| Security budget | Approved 2026-08-31: about $5,200 one-time and $2,260 a year (itemized in P01 section 4) | P01 |
| 2025 hurricane evacuation | While the county was under a declared state of emergency in 2025, the pricing tool raised rates 61% above the 30-day average for 2 nights. No complaint was received | P01, P10 |
| Dynamic pricing tool | Break-even rate $62 (used as the floor); 9 nights below it since 2025-03; 14-day forecast error 10.4%; no SOC 2 report (short security questionnaire only); MFA available but off; subscription terms allow no pooling of the motel's non-public data; one of the 3 OTAs showed the base rate because the $6 fee is not mapped as mandatory in its feed | P01, P10 |
| AI guest messaging add-on | The PMS vendor offered a free trial in July 2026; the Owner-Manager did not start it | P10 |
| Crew client questionnaire | The largest crew client is a regional utility line contractor (about 18% of room-nights). It sent a vendor security questionnaire in July 2026, due 2026-09-30, about its corporate card data and crew rosters (names, phone numbers, employee ID numbers) and accepts a self-assessment | P09 |
| PMS vendor SOC 2 report | One exception (a missed quarterly access review for vendor support staff), remediated; hosting provider carved out; five complementary user entity controls; customers notified within 72 hours of a confirmed incident; no bridge letter provided | P02, P09 |
| Hurricane checklist | The building hurricane checklist covers shutters and a generator for the office and lobby, not IT | P01, P02 |
| Background-check reports | Printed and filed in an office drawer; shredded under the new POL-04 rule | P01, P03, P06 |
| Assessor | The P07 assessor is an independent security consultant with payment card experience, not a QSA, who took no part in P01 or P03 and operates no control | P07 |
