# Scenario facts: Cris Santos Company | Accommodation and Food Services | Small

All 10 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a law, regulation, standard, or court decision, the citation is given. Facts about the acquirer, the merchant agreements, and vendors are fictional.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (independent hotel operator) |
| Business | Owns and operates **one independent full-service beachfront hotel** (NAICS 721110): 140 guest rooms, a 120-seat restaurant, a lobby bar, a pool bar, and 4,000 square feet of meeting and event space |
| Location | Florida Gulf Coast. Open 24 hours, every day. Hurricane season (June to November) is the main natural hazard |
| Franchise status | **Independent, not franchised.** The hotel operated under a national brand's franchise agreement until 2021, when the owner let the agreement expire and de-flagged the property. Under the franchise the brand dictated the property management system (PMS), ran the property network connection to the brand's data center, and ran the brand PCI program. Since the 2021 migration the company chooses and runs all of this itself. See "Franchise decision" below |
| Workforce | 60 employees: 8 management and administration, 14 front office and reservations, 12 housekeeping and laundry supervisors and staff, 20 food and beverage, 4 engineering and maintenance, 2 sales and events. About 45 room attendants and valet staff are supplied by a contracted staffing company and are not employees |
| Revenue | $24.0 million a year (fictional): rooms $17.4 million (average daily rate about $425, occupancy about 80%, including a mandatory **$35 per night amenity fee**), food and beverage $5.3 million, other $1.3 million (parking, meeting space, retail). About $66,000 per day. Under the SBA standard of $40.0 million for NAICS 721110 (13 CFR 121.201), so SBA-small |
| Guests | About 15,700 stays a year. The PMS holds about 112,000 guest profiles created since the 2021 migration, including about 61,000 scanned identity documents (driver licenses and passports) taken at check-in. The cloud guest-marketing database holds about 48,000 profiles with email consent |
| Card acceptance | About 97,000 card transactions a year under **two merchant accounts** with the same acquirer (fictional terms): **MID-1 Rooms** (about 24,000 front office transactions, of which about 6,500 are card-not-present card numbers keyed from phone calls and card authorization forms and about 4,000 are online travel agency virtual cards; plus about 5,000 online booking engine prepayments) and **MID-2 Food and beverage** (about 68,000 restaurant and bar transactions) |
| PCI DSS status | **Merchant.** PCI DSS v4.0.1 applies through the two merchant agreements (contract, not law). The acquirer's letter dated 2026-05-20 (fictional) confirms annual self-assessment (SAQ) validation with no Report on Compliance required, questions the 2025 SAQ A, and asks the company to confirm the correct SAQ types. The 2026 attestations of compliance are due **2026-12-31**. Card-brand merchant levels are set by the brands; Visa says a merchant's 12-month Visa transaction volume determines its level, but the level thresholds were not verified from a card brand primary source, so no level number is stated in these documents |
| Payment design | **Front desk (MID-1):** 4 chip terminals (PCI-approved PIN entry devices) that are "semi-integrated" with the PMS through the payment gateway. They are **not** part of a PCI-listed validated P2PE solution. The terminals share one flat network with the front desk PCs. **Phone reservations and card authorization forms (MID-1):** staff key card numbers into the PMS payment screen in a browser on front office PCs. Group and third-party billing forms arrive by email and are printed and filed. **Online travel agency virtual cards (MID-1):** delivered through the channel manager into the PMS card vault; users with the "view full card number" permission can display them. **Online booking engine (MID-1):** a vendor-hosted booking and payment page on the vendor's own web address. The hotel website only links to it; card data never touches hotel systems. **Restaurant and bars (MID-2):** 14 devices (6 countertop, 8 pay-at-table handhelds) in a **PCI-listed validated P2PE solution**. The POS posts room charges to the PMS by room number and guest name only |
| Franchise decision | **Independent.** A franchised hotel usually must use the brand's mandated PMS and follow the brand's PCI program, and the brand shares responsibility for the systems it manages. In *FTC v. Wyndham Worldwide Corp.*, 799 F.3d 236 (3d Cir. 2015) (No. 14-3514, opinion filed 2015-08-24), the court affirmed that the FTC may challenge unreasonable cybersecurity as an unfair practice under 15 U.S.C. 45(a), in a case about a franchisor that managed branded hotels' PMS systems. The alleged failures included card data in clear text, easily guessed and default passwords, no firewalls between hotel PMS systems, the corporate network, and the internet, an out-of-date operating system, no inventory, unrestricted vendor access, and weak incident response; over 619,000 accounts and at least $10.6 million in fraud loss were alleged. As an independent, **Cris Santos Company alone carries these duties**, and several of its 2026 gaps match the Wyndham list (gaps 3, 5, 6, 7, 9 below) |
| Not in scope | **CIRCIA (proposed 6 CFR Part 226):** proposed only; the company is below the SBA size standard and lodging has no sector criterion (N72-R06). **Illinois BIPA (N72-R05):** no Illinois operations or employees; not applicable (its text was not verified). **FTC Safeguards Rule and Red Flags Rule:** no consumer credit is extended. **CCPA:** no California business and revenue below $26,625,000. **HIPAA:** not a covered entity. **SEC:** privately held. **Federal contracts:** none |
| Other applicable law | FTC Act Section 5 (15 U.S.C. 45(a), (n)) for guest data security, privacy statements, and pricing claims (N72-R02); FTC Rule on Unfair or Deceptive Fees, **16 CFR Part 464** (90 FR 2066, published 2025-01-10, effective 2025-05-12), which covers short-term lodging and requires total price, including mandatory fees, in any price display (464.1, 464.2); FTC Disposal Rule, 16 CFR 682.3, for background-check reports (N72-R03); Florida guest register duty, **Fla. Stat. 509.101(2)** (keep a chronological register of guests, dates, and rates; may be electronic; registers older than 2 years need not be made available); Florida breach notice and reasonable security, **Fla. Stat. 501.171** (N72-R04); Florida price gouging during a declared state of emergency, **Fla. Stat. 501.160** (P10 pricing) |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notification, guest register, emergency pricing). Other states are treated generically ("each state where affected individuals reside") |

## 2. People (role titles only)

| Role | Security and privacy duties |
|---|---|
| Majority owner (Cris Santos) | Accepts High and Very High risks; signed the 2025 SAQ A |
| General Manager | Executive owner of the security program; approves policies; accepts Moderate risks |
| Controller | Owns the two merchant agreements, the acquirer relationship, SAQ submissions, and the cyber insurance policy. Business owner of PCI DSS compliance |
| IT Manager | Part-time **Information Security Lead** and PCI DSS technical contact. Runs IT with a managed service provider |
| Front Office Manager | Front desk, reservations, card handling procedures, key card encoders, night audit |
| Revenue Manager | Owns the revenue-management system (P10 AI-001 business owner) |
| Director of Sales and Marketing | Owns the website, guest chatbot (P10 AI-002 business owner), guest-marketing database, group sales and card authorization forms |
| Food and Beverage Director | Owns the restaurant and bar POS and P2PE device inspections |
| HR Manager | Onboarding, terminations, background checks, training records, timekeeping |
| Chief Engineer | Door lock system, building systems, physical security, hurricane preparation |
| Managed service provider (MSP, external) | Help desk, firewall and network management, endpoint patching and anti-malware. Has always-on remote access to hotel PCs and the lock server |
| Key vendors (external) | PMS vendor; payment gateway (PCI DSS validated service provider); POS vendor and its P2PE solution provider; booking engine vendor; channel manager vendor; guest Wi-Fi and TV vendor; door lock vendor; revenue-management vendor; chatbot vendor; web agency; background-check company; staffing company |

## 3. Systems

| ID | System | Hosting | Card or personal data? | Notes |
|---|---|---|---|---|
| SYS-01 | Property management system (PMS): reservations, guest profiles, folios, night audit, card vault, interfaces | Vendor SaaS | Guest profiles, ID scans, stay history; tokens; **full online travel agency virtual card numbers in the vendor's vault** | System of record. Vendor holds a PCI DSS service provider attestation (AOC dated 2026-03) and a SOC 2 Type 2 report (Security and Availability, 12 months to 2026-03-31). 22 front office and reservations users; 14 have the "view full card number" permission (see gaps) |
| SYS-02 | Payment gateway and front desk chip terminals (4) | Service provider plus on-premises devices | Card data (terminals and gateway side) | Semi-integrated with the PMS. Not a validated P2PE solution. Gateway AOC dated 2025-02 on file (expired for annual purposes) |
| SYS-03 | Online booking engine | Vendor SaaS on the vendor's web address | Card data on the vendor side only; the hotel receives a token | Linked from the hotel website. Vendor AOC dated 2026-01 on file |
| SYS-04 | Channel manager (online travel agency connections) | Vendor SaaS | Reservation data and virtual card numbers in transit to the PMS | No AOC on file (see gaps) |
| SYS-05 | Restaurant and bar POS with validated P2PE devices (14) | Vendor-managed: 5 POS stations, vendor cloud back office | Encrypted card data only; room charges by room number | P2PE Instruction Manual on file. Device inspections are informal |
| SYS-06 | Hotel network | On-premises | Card data in transit (front desk terminals and keyed entry) | MSP-managed firewall and switches. **One flat staff network** for front desk PCs, terminals, back office PCs, the lock server, and the CCTV recorder. Guest Wi-Fi and TV run on separate vendor-managed networks (internet only) |
| SYS-07 | Endpoints | On-premises | Yes: keyed card numbers pass through front office browsers; cached reports | 34 Windows PCs and laptops (6 front desk, 2 reservations, 26 back office and managers), 5 POS stations (SYS-05), 12 staff tablets |
| SYS-08 | Door lock system: lock server, 3 key card encoders, 160 electronic locks | On-premises server with vendor remote support | Guest names and room assignments | Interfaced to the PMS. Server runs an operating system out of vendor support since 2023 (see gaps) |
| SYS-09 | Identity provider (single sign-on and MFA) | SaaS | No (identities only) | Protects email, the cloud console, and PMS administrator sign-in |
| SYS-10 | Cloud tenant (IaaS/PaaS) | Public cloud provider (vendor-agnostic) | Guest-marketing profiles; reporting data | Managed database for the guest-marketing hub (48,000 profiles), a reporting database fed nightly from the PMS for the revenue-management system, object storage for PMS report exports, a serverless integration that connects the chatbot to PMS availability, and the backup vault |
| SYS-11 | Productivity suite (email and files) | SaaS | **Yes: card authorization forms in the reservations and sales shared mailboxes** | 1,140 emails with card numbers found during P03 fieldwork (see gaps) |
| SYS-12 | Revenue-management system (AI pricing) | Vendor SaaS | Stay history and bookings (aggregated); public competitor rates | Live since 2024. Automatically publishes daily rates to the PMS, booking engine, and channel manager (see P10). Vendor provides a SOC 2 Type 1 report only |
| SYS-13 | Guest chatbot (generative AI) on the website and text messaging | Vendor SaaS | Guest questions and contact details; transcripts | Live since March 2026. About 2,400 conversations a month. Quotes rates and availability, then links to the booking engine (see P10) |
| SYS-14 | Timekeeping and payroll with finger-scan time clocks (2) | Vendor SaaS plus devices | Employee data and finger templates | Biometric data is personal information under Fla. Stat. 501.171(1)(g)1.a.(VI) |
| SYS-15 | CCTV | On-premises recorder | Video | 30-day retention. No facial recognition |

**SSP system (P02):** the *Property Management and Point-of-Sale Platform (PMPS)*: SYS-01, SYS-02, SYS-05, SYS-06, SYS-07, SYS-08, SYS-09, and SYS-10, with interfaces to SYS-03, SYS-04, SYS-11, SYS-12, and SYS-13.

## 4. Current security posture: partially compliant

**In place today:**
- Restaurant and bar card payments on a PCI-listed validated P2PE solution (SYS-05)
- Online booking payments on the booking engine vendor's own payment page; hotel systems receive only a token
- The PMS stores tokens only for guest cards; virtual card numbers sit in the vendor's vault, not on hotel systems
- MFA through the identity provider for email, the cloud console, and PMS administrator accounts
- Guest Wi-Fi and TV networks separated from the staff network by the Wi-Fi vendor (internet only, client isolation)
- MSP-managed firewall that blocks unsolicited inbound traffic
- Anti-malware on PCs; monthly operating system patching by the MSP (except the lock server)
- Chip terminals at the front desk (no magnetic-stripe-only acceptance)
- Receipts show only the last 4 digits of the card number
- Background checks for managers and front office staff through a background-check company
- Locked shredding bins emptied by a shredding vendor
- The PMS vendor's daily backups; a building hurricane plan (not covering IT)
- Cyber insurance policy with a breach hotline
- Booking engine total price includes the $35 amenity fee (changed in May 2025 for 16 CFR Part 464)

**Missing or weak, found in the 2026 assessments:**
1. The 2025 validation used **SAQ A for both merchant accounts**, on a vendor salesperson's advice. The hotel is not eligible for SAQ A: staff key card numbers into front office PCs and card data is stored in email. There is no documented PCI DSS scope or data-flow diagram (Requirement 12.5.2).
2. **Stored card data outside the vault.** 1,140 emails with card authorization forms (212 including the card security code) sit in the reservations and sales shared mailboxes back to 2021. Printed forms are kept in an unlocked binder at the front desk for 3 years or more. Keeping security codes after authorization is prohibited (Requirement 3.3.1).
3. **Flat staff network.** Front desk PCs, front desk terminals, back office PCs, the lock server, and the CCTV recorder share one network with no segmentation, so the whole staff network is in PCI scope.
4. **Excess card visibility.** 14 of 22 front office and reservations users can display full card numbers in the PMS; 3 need it today.
5. **Shared and stale accounts.** Two front desk PCs use a shared Windows login, the night audit uses one shared PMS account, and P07 testing found 9 PMS accounts of former employees still active. PMS sign-in for non-administrators has no MFA.
6. **Lock server.** It runs an operating system out of vendor support since 2023, sits on the flat network, and (found in P07 testing) still uses the lock vendor's default administrator password.
7. **Vendor remote access.** The MSP and the lock vendor use always-on remote access tools with no MFA and no source restriction.
8. **No incident response plan.** Staff do not know the merchant agreement term (notify the acquirer within 24 hours of suspecting a compromise; fictional) or Visa's 3-calendar-day notice rule.
9. **No logging or review.** Firewall, PC, and lock server logs are not collected; PMS user activity reports are never reviewed.
10. **No vulnerability scans or penetration tests.** No external ASV scans, internal scans, or penetration tests, all of which SAQ D requires.
11. **Training.** No security awareness training since the brand's program ended in 2021. Front office staff get no training on phishing or on callers who try to obtain guest or card information.
12. **Guest chatbot.** 23 transcripts stored by the chatbot vendor contain card numbers that guests typed in. The chatbot quotes nightly rates **without the mandatory $35 amenity fee** (16 CFR 464.2).
13. **Revenue-management system.** Rates publish automatically with no human review, no emergency cap for declared states of emergency (Fla. Stat. 501.160), and a contract clause that lets the vendor pool the hotel's non-public rate and occupancy data into a market benchmark for other clients.
14. **Backups and recovery.** Lock server and file share backups sit in the same cloud account as production and have never been restore-tested. The PMS vendor's recovery objectives are not in the contract.
15. **No retention schedule.** The PMS keeps all guest profiles and 61,000 ID scans indefinitely, although Fla. Stat. 509.101(2) only requires the register to be available for 2 years. Card authorization forms are kept without limit.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 primary standard | PCI DSS v4.0.1 (contractual, N72-R01). Secondary: FTC Act Section 5 with 16 CFR Part 464 (N72-R02). Short checks: FTC Disposal Rule (N72-R03), Fla. Stat. 509.101(2) and 501.171(2) and (8) |
| P03 SAQ decision | MID-1 Rooms: **SAQ D for Merchants** for 2026. MID-2 Food and beverage: **SAQ P2PE**. Acquirer (fictional) agreed by email on 2026-08-12. Target for 2027 after scope reduction: SAQ P2PE for front desk and phone payments plus SAQ A for the booking engine, subject to acquirer approval |
| P08 incident | POS and reservation system compromise: a phishing email to the reservations mailbox leads to a browser form-grabber on front office PCs, capture of keyed card numbers, and PMS access with a stolen front desk login. Discovered through an acquirer common-point-of-purchase alert |
| P09 SOC 2 | The hotel is not a service organization and PCI DSS validation is its assurance mechanism. (a) Security-only self-benchmark against the Trust Services Criteria; (b) review of the PMS vendor's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| P10 AI | AI-001 revenue-management pricing (SYS-12); AI-002 guest chatbot (SYS-13) |
| Cloud | Vendor-agnostic. Services are described by category, with AWS, Azure, and Google Cloud equivalents noted only for shared responsibility |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-05-20 | Acquirer letter questioning the 2025 SAQ A |
| 2026-07-13 to 2026-07-24 | Risk assessment and gap analysis fieldwork (hotel walkthrough 2026-07-15) |
| 2026-08-03 to 2026-08-07 | Control assessment fieldwork |
| 2026-08-12 | Acquirer email agreeing to SAQ D (MID-1) and SAQ P2PE (MID-2) for 2026 |
| 2026-08-17 to 2026-08-21 | SOC 2 benchmark, PMS vendor report review, and AI assessment |
| 2026-08-31 | Deliverables approved by the General Manager (High risks by the majority owner) |
| 2026-12-31 | 2026 SAQs and attestations of compliance due to the acquirer |
