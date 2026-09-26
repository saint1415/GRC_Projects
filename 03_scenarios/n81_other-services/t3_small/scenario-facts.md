# Scenario facts: Cris Santos Company | Other Services | Small

All 10 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a law, regulation, or standard, the citation is given. Facts about the acquirer, the manufacturers' program agreements, customers, and vendors are fictional.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (electronics and device repair service) |
| Business | Electronics and device repair (NAICS 811210): phones, tablets, laptops, desktops, and game consoles. Walk-in repair at **four stores**, mail-in repair, board-level (microsoldering) repair, **data recovery and data transfer**, warranty repair as a **manufacturer-authorized service provider**, repair contracts for about 140 business accounts, and a free **device recycling drop-off** with data wiping |
| Location | Florida. **Stores A to D** in one metro area, and the **Depot** (head office, mail-in intake, board-level repair bench, data recovery lab, parts warehouse) in a separate leased building. Stores open 9:00 to 19:00 Monday to Saturday; the Depot 8:00 to 18:00 Monday to Friday |
| Workforce | 60 employees: 24 store repair technicians, 6 Depot technicians (4 board-level and warranty technicians, 2 data recovery specialists), 12 customer service advisors, 5 parts and logistics staff, 4 Store Managers, and 9 management and administration staff |
| Revenue | $20.4 million a year (fictional), about $78,000 per business day. About 55% consumer repairs, 25% manufacturer warranty reimbursements, 15% business accounts, 5% data recovery premiums, accessories, and recycling rebates. Under the SBA standard of $34.0 million for NAICS 811210 (13 CFR 121.201), so SBA-small |
| Volume | About 52,000 repair tickets a year (about 200 per business day across 5 sites). About 9% are mail-in tickets from customers in other states. About 1,100 data recovery cases a year. About 3,000 recycling drop-off devices a year |
| Customers | About 72,000 customer records in the ticketing system (every customer since 2019): names, phone numbers, email addresses, mailing addresses for mail-in, device make, model, serial number or IMEI, and repair history. About 140 business accounts (small businesses, 2 private schools, a property manager) pay by invoice and ACH |
| Card acceptance | About 41,000 card transactions a year, all on **12 payment terminals** that belong to a **validated PCI-listed P2PE solution** from the payment processor (2 per store, 2 at the Depot counter, 2 spares). Mail-in customers pay by phone: staff key the card number directly into a P2PE terminal. No e-commerce checkout |
| PCI DSS status | **Merchant.** PCI DSS v4.0.1 applies through the merchant agreement with the acquiring bank. It is a contractual standard, not law. In a letter dated 2026-05-20 (fictional), the acquirer confirmed annual validation on **SAQ P2PE** (PCI DSS v4.0.1 SAQ P2PE, October 2024), due 2026-11-30. Merchant levels are set by the card brands and the acquirer and are not stated here |
| Authorized service provider | Authorized service provider for **Manufacturer A** (phones, tablets, computers) at Stores A and B and the Depot, and warranty repair depot for **Manufacturer B** (laptops). The program agreements (fictional terms) require: background checks for technicians who handle customer devices; access to customer data only as the repair requires and with the customer's consent; named, MFA-protected accounts on the manufacturers' service portals and diagnostic tools; parts traceability by serial number; notice to the manufacturer within **24 hours** of a suspected incident involving customer data or devices; and an annual program audit (Manufacturer A's next audit: 2026-10). They are contracts, not law |
| Not in scope | **FTC Safeguards Rule (16 CFR Part 314):** the company does not extend credit or offer in-house financing, so it is not a "financial institution" (16 CFR 314.1(b)). **HIPAA:** the company is not a covered entity or business associate; health app data on customer devices is not PHI in the company's hands. **COPPA:** the website and chatbot are not directed to children. **Florida Digital Bill of Rights:** not analyzed; its revenue threshold is far above the company's size (not verified here). **Trade-ins:** the company does not buy or resell used devices. **SEC disclosure:** privately held |
| Other applicable law | **FTC Act Section 5** (15 U.S.C. 45(a), 45(n)): unfair or deceptive practices, including unreasonable security and privacy promises about customer devices. **Fla. Stat. 501.171** (2026): reasonable security measures (2), breach notice (3)-(6), and disposal of customer records (8). **FTC Disposal Rule** (16 CFR Part 682): applies **only to consumer report information**, which here means the background check reports on technicians and applicants, not customer device data. Other states' breach laws for mail-in customers |
| Benchmark | NIST CSF 2.0 (voluntary; no sector cybersecurity rule applies). **NIST SP 800-88 Rev. 2**, *Guidelines for Media Sanitization* (final, September 2025; supersedes Rev. 1 of 2014), for wiping customer and recycled devices |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notice and disposal, Fla. Stat. 501.171). Other state law is treated generically ("each state where affected individuals reside") |

## 2. People (role titles only)

| Role | Security and privacy duties |
|---|---|
| Majority owner (Cris Santos) | Not an employee. Accepts High and Very High risks; approves the security budget |
| General Manager | Executive owner of the security program; approves policies; accepts Moderate risks |
| IT Manager | Part-time **Information Security Lead** and privacy contact; runs IT with the IT Support Technician |
| IT Support Technician | Endpoint builds, bench workstation images, help desk |
| Operations Manager | Owns the repair process at all sites, technician standards, the Depot, and the manufacturer program relationships. Business owner of AI-assisted diagnostics (P10) |
| Controller | Owns the merchant agreement, the SAQ, the cyber insurance policy, and vendor contracts |
| Customer Experience Manager | Owns the website, the customer chatbot (P10 business owner), intake forms, privacy notice, and marketing claims |
| Data Recovery Lead | Senior data recovery specialist at the Depot; custodian of recovered customer data |
| Store Managers (4) | Store operations, PIN pad inspections, intake and release of devices, physical security |
| Business Accounts Manager | Owns the 140 business accounts and their security questionnaires |
| HR and Payroll Specialist | Onboarding, terminations, background checks, training records |
| Ticketing and POS vendor (external) | SaaS repair-shop management platform. SOC 2 Type 2 report (P09) |
| Payment processor (external) | P2PE solution provider and acquirer's processor. PCI DSS validated service provider |
| Certified electronics recycler (external) | Collects recycling drop-off devices and retired company equipment under a service contract |

## 3. Systems

| ID | System | Hosting | Personal or card data? | Notes |
|---|---|---|---|---|
| SYS-01 | **Service ticketing and point-of-sale platform**: intake, tickets, customer records, parts inventory, invoicing, POS, customer status portal, SMS and email updates | Vendor SaaS | Yes: 72,000 customer records; **device passcodes and account passwords in a free-text ticket field** (see gaps); no card data by design | System of record. Vendor provides a SOC 2 Type 2 report (Security and Availability) |
| SYS-02 | Payment processor P2PE solution and merchant portal | Service provider | Card data (processor side only) | 12 P2PE PIN pads (2 per store, 2 at the Depot counter, 2 spares). The company never holds decryption keys |
| SYS-03 | Identity provider (single sign-on and MFA) | SaaS | No (identities only) | Protects SYS-01, SYS-04, SYS-05, and the manufacturer portals that support single sign-on |
| SYS-04 | Productivity suite (email, files, chat) | SaaS | Yes (customer emails, business account data) | |
| SYS-05 | Cloud tenant (IaaS/PaaS) | Public cloud provider (vendor-agnostic) | Yes (recovered customer data) | Object storage for **recovered-data delivery** (customers download through expiring links), a small serverless function that connects the chatbot to SYS-01 for status lookups, and the backup vault for the Depot data recovery storage |
| SYS-06 | Data recovery lab | On-premises (Depot) | Yes (full images of customer devices) | Network storage array (about 38 TB used), 3 imaging workstations, write blockers, clean-room bench. **Recovered data is kept indefinitely** (see gaps) |
| SYS-07 | Technician bench workstations | On-premises (all sites) | Yes (cached customer data during transfers and diagnostics) | 30 bench PCs and 6 bench laptops running diagnostic, flashing, and data transfer tools. **Shared local accounts per store**; USB storage allowed; excluded from EDR (see gaps) |
| SYS-08 | Manufacturer service portals and diagnostic tools (Manufacturer A and B) | Manufacturer SaaS | Customer device serials, repair records, customer names for warranty claims | Named technician accounts required by the program agreements |
| SYS-09 | Store and Depot networks | On-premises (5 sites) | Card data in transit (encrypted by P2PE) | Firewall at each site, site-to-site VPN to the Depot, guest Wi-Fi (separated), one flat internal network per store shared by office PCs, counter tablets, bench PCs, and **customer devices under repair** (see gaps) |
| SYS-10 | Office endpoints and counter tablets | On-premises | Yes (cached) | 22 office PCs and laptops, 10 counter tablets. EDR and full-disk encryption on office PCs and laptops |
| SYS-11 | AI services | Vendor SaaS | Yes (chat transcripts; device diagnostic logs and photos) | **AI-001 customer chatbot** on the website and SMS (live since 2026-03). **AI-002 AI-assisted diagnostics** pilot at the Depot and Store A (since 2026-06). See P10 |
| SYS-12 | CCTV | On-premises recorders | Video | Counters, bench areas, and the data recovery lab door; 30-day retention |
| SYS-13 | Payroll and HR SaaS, with a background check vendor | Vendor SaaS | Employee data; **consumer reports** (background checks) | Background check reports are consumer report information under the FTC Disposal Rule (16 CFR 682.1(b)) |

**SSP system (P02):** the *Service Ticketing and Point-of-Sale Platform (STPP)*: SYS-01, SYS-03, SYS-05, SYS-06, SYS-07, SYS-09, and SYS-10, with their interfaces to SYS-02, SYS-08, and SYS-11.

## 4. Current security posture: partially compliant

**In place today:**
- Validated P2PE terminals for all card payments; the acquirer confirmed SAQ P2PE
- Single sign-on with MFA for email, the cloud console, and named SYS-01 accounts used from office PCs and laptops
- Background checks for all technicians before hire (required by the Manufacturer A program)
- A printed intake form with a privacy notice and the customer's signed consent to power on and test the device
- EDR and full-disk encryption on the 22 office PCs and laptops
- CCTV at counters, bench areas, and the data recovery lab door
- Locked shredding bins at every site; paper shredded by a vendor with certificates
- A certified electronics recycler that issues certificates of destruction per collection lot
- Nightly backup of the data recovery storage to a cloud backup vault, in the same cloud account
- The ticketing and POS vendor's SOC 2 Type 2 report on file
- Manufacturer A's annual technician course, which includes a customer privacy module

**Missing or weak, found in the 2026 assessments:**
1. Device passcodes, and sometimes the customer's email and account password (for activation lock or account sign-in), are collected at intake and typed into a **free-text ticket field visible to all 60 users**. Paper intake tags taped to devices also show the passcode. A search on 2026-07-22 found about 48,000 tickets with passcodes and 2,900 with account passwords.
2. There is no rule or technical control limiting technician access to device contents. Bench PCs use a shared local account per store, USB storage is allowed, and bench sessions are not logged. A customer complaint in April 2026 alleged that a technician browsed personal photos. It was investigated but was inconclusive.
3. Recovered customer data is kept indefinitely: about 4.2 TB on the lab storage from about 1,300 cases older than 90 days, plus data transfer caches on bench PCs that are never wiped. Recovered-data download links in the cloud tenant do not expire for business accounts.
4. No media sanitization standard. Recycling drop-off devices are wiped by whichever technician is free, with no record per device and no verification. The recycler's certificates cover lots, not serial numbers.
5. During phone payments for mail-in repairs, staff sometimes write card numbers on paper or in the ticket notes before keying them into the terminal (P03 found 37 tickets with full card numbers). PIN pad inspections are not scheduled or recorded. Both threaten SAQ P2PE eligibility.
6. No written incident response plan. Staff do not know the Manufacturer A 24-hour notice term or the acquirer's notice term (notify within 24 hours of suspecting a card data compromise; fictional term).
7. Counter tablets at Stores C and D use one **shared SYS-01 login per store** without MFA. One shared Manufacturer A portal login is used at Store B, which breaches the program agreement.
8. No access reviews in SYS-01. P07 testing found 7 former employees' accounts still active.
9. Each store runs one flat internal network: office PCs, counter tablets, bench PCs, and customer devices under repair (some of them infected) share it.
10. No log review. SYS-01 records exports and ticket views, but nobody reviews them.
11. The lab storage backup is in the same cloud account as production, is not immutable, and has never been restore-tested. SYS-01 data depends only on the vendor's backups; the company keeps no export.
12. No security policies. The only document is a one-page privacy statement from 2022.
13. Security awareness training is limited to the manufacturer's privacy module for technicians. Counter staff and managers get none, and there is no phishing training.
14. The AI chatbot went live without testing. Its transcripts show customers pasting passcodes. The AI-assisted diagnostics pilot has no accuracy measurement, and the website states "AI-powered diagnosis, 99% accurate" without substantiation.
15. No vendor inventory with data flows. The recycler, the courier for mail-in shipments, and the two AI vendors have no contract security or data-use terms.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 primary benchmark | NIST CSF 2.0 (voluntary; all 106 subcategories). Secondary: the binding legal baseline (FTC Act Section 5 and Fla. Stat. 501.171), with PCI DSS v4.0.1 SAQ P2PE (binding by contract) and an applicability screen |
| Regulatory driver IDs | N81-R01 FTC Act Section 5; N81-R02 state breach laws (Fla. Stat. 501.171 as the worked example); N81-R03 PCI DSS v4.0.1; N81-R04 FTC Disposal Rule (background check reports only); `N81-BM` points to the NIST CSF 2.0 benchmark and SP 800-88 Rev. 2. Manufacturer program terms are cited as "Manufacturer A agreement (contract)" |
| P08 incident | Customer data exposure at the repair counter: (A) a technician copies personal data from a customer device in the shop's custody, and (B) the shared counter login is phished and ticket notes with passcodes, account passwords, and card numbers are exported (the point-of-sale compromise) |
| P09 SOC 2 | The company is not a SOC 2 service organization (it repairs devices; it does not operate systems for customers). (a) Security-only readiness benchmark, used to answer business account questionnaires and the Manufacturer A audit; (b) review of the ticketing and POS vendor's SOC 2 Type 2 report |
| P10 AI | AI-001 customer chatbot and AI-002 AI-assisted diagnostics |
| Cloud | Vendor-agnostic. Services are described by category, with AWS, Azure, and Google Cloud equivalents noted only for shared responsibility |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-05-20 | Acquirer letter confirming SAQ P2PE validation |
| 2026-07-20 to 2026-07-31 | Risk assessment and gap analysis fieldwork (store walkthroughs 2026-07-22 and 2026-07-23) |
| 2026-08-10 to 2026-08-14 | Control assessment fieldwork |
| 2026-08-17 to 2026-08-21 | SOC 2 readiness benchmark, vendor report review, and AI assessment |
| 2026-09-04 | Deliverables approved by the General Manager (High risks by the majority owner) |
| 2026-10 | Manufacturer A annual program audit |
| 2026-11-30 | 2026 SAQ P2PE and attestation due to the acquirer |
