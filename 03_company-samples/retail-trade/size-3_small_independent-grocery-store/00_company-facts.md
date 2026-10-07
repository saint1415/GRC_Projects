# Scenario facts: Cris Santos Company | Retail Trade | Small

All 10 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a law, regulation, or standard, the citation is given. Facts about the acquirer, the merchant agreement, and vendors are fictional.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (independent grocery retailer) |
| Business | Independent grocery retailer (NAICS 445110): **one supermarket** of about 32,000 square feet, plus **online ordering** with curbside pickup and local delivery (within about 10 miles of the store) |
| Location | Florida. One store, open 7:00 to 22:00 every day. The store serves six surrounding ZIP codes with different income levels; online delivery covers four delivery zones |
| Workforce | 60 employees: 8 management and office staff, 22 front-end staff (cashiers and customer service), 20 fresh department and grocery staff, 10 e-commerce fulfillment staff (6 order pickers, 4 delivery drivers) |
| Revenue | $24.0 million a year (fictional), about $66,000 per day. Online orders are about 12% of sales (about 95 orders a day). Under the SBA standard of $40.0 million for NAICS 445110 (13 CFR 121.201), so SBA-small |
| Card acceptance | About 480,000 card transactions a year: about 445,000 in the store and about 34,000 online. The company does not take card numbers by phone, mail, or email |
| Customers | About 21,000 active loyalty members (members must be 18 or older) and about 9,500 online shopping accounts |
| PCI DSS status | **Merchant.** PCI DSS v4.0.1 (PCI SSC) applies through the merchant agreement with the acquiring bank. It is a contractual standard, not law. In a letter dated 2026-06-15 (fictional), **the acquirer confirmed the validation type**: an annual self-assessment, using SAQ P2PE for the in-store channel and SAQ A for the e-commerce channel, with the attestations of compliance due by 2026-11-30. The company does not state its merchant level in these documents; levels and validation rules are set by the card brands and the acquirer |
| Scope reduction (why the CDE is small) | **In store:** card data is captured only on PIN pads that are part of a **validated P2PE solution** listed by the PCI SSC. The card data is encrypted inside the device, and the company never holds the decryption keys, so registers, the POS back office, and the store network see only encrypted data. This holds only while the P2PE Instruction Manual is followed and card numbers can be entered only on the P2PE devices (manual card entry on register keyboards is disabled). **Online:** the storefront shows a payment form **embedded from the payment processor** (an inline frame). Card data goes from the customer's browser straight to the processor, and the storefront receives only a token. The storefront page that hosts the frame can still affect the payment, which is why payment-page script controls (PCI DSS v4.0.1 Requirements 6.4.3 and 11.6.1) matter |
| Not in scope | **Pharmacy and HIPAA:** the store has no pharmacy (decision confirmed by the majority owner), so it is not a HIPAA covered entity. **FTC Safeguards Rule and Red Flags Rule:** the company does not issue its own credit card or offer deferred payment (no covered accounts). **CCPA:** the company does not do business in California and its revenue is below the $26,625,000 threshold. **COPPA:** the website is not directed to children and loyalty members must be 18 or older. **INFORM Consumers Act:** no third-party sellers. **SEC disclosure:** privately held. **Facial recognition:** the store's CCTV does not use facial recognition. **SNAP EBT:** accepted on the same devices but outside this analysis |
| Other applicable law | FTC Act Section 5 (15 U.S.C. 45(a), (n)) for loyalty and customer data security, privacy statements, and pricing claims; FACTA receipt truncation (15 U.S.C. 1681c(g)); Florida breach notification (Fla. Stat. 501.171) |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notification, Fla. Stat. 501.171). Other state law is treated generically ("each state where affected individuals reside") |

## 2. People (role titles only)

| Role | Security and privacy duties |
|---|---|
| Majority owner (Cris Santos) | Accepts High and Very High risks; signed the 2025 SAQs personally |
| General Manager | Executive owner of the security program; approves policies; accepts Moderate risks |
| IT Manager | Part-time **Information Security Lead** and PCI DSS contact; runs IT with help from vendors' help desks |
| Controller | Owns the merchant agreement, acquirer relationship, SAQ submissions, and the cyber insurance policy |
| E-commerce and Marketing Manager | Owns the storefront, the loyalty program, and the pricing and offers engine (P10 business owner) |
| Store Manager | Front end, PIN pad inspections, physical security, refrigeration alarms |
| HR and Payroll Specialist | Onboarding, terminations, training records |
| Marketing contractor (external) | Two-person agency. Manages storefront theme and marketing tags; receives monthly loyalty exports by email |
| POS vendor (external) | Manages POS software, the in-store POS back office server, and registers under a service contract; has remote access |
| Payment processor (external) | Provides the P2PE solution, the embedded payment page, tokenization, and the merchant portal. A PCI DSS validated service provider |
| Refrigeration and building controls contractor (external) | Maintains refrigeration controllers, sensors, and energy management; has remote access |

## 3. Systems

| ID | System | Hosting | Personal or card data? | Notes |
|---|---|---|---|---|
| SYS-01 | E-commerce storefront (catalog, customer accounts, ordering, pickup and delivery scheduling) | Vendor SaaS | Customer accounts (name, email, password hash, phone, delivery addresses, order history); **no card data** | Checkout page embeds the processor's payment form. 14 third-party scripts on the checkout page, not inventoried (see gaps). Vendor provides a SOC 2 Type 2 report (Security and Availability, 12 months to 2026-03-31) and a PCI DSS attestation of compliance (AOC) as a service provider, dated 2026-05 |
| SYS-02 | Payment processor services: P2PE solution, embedded payment page, tokenization, merchant portal | Service provider | Card data (processor side only) | Third-party service provider (TPSP). The company sees truncated card numbers and tokens only |
| SYS-03 | Loyalty program database and loyalty API | Company cloud tenant (SYS-04) | About 21,000 members: names, phone numbers, emails, home ZIP codes, purchase history | Built by a contractor in 2022. The POS and storefront call the loyalty API. Monthly full exports are emailed to the marketing contractor (see gaps) |
| SYS-04 | Cloud tenant (PaaS/IaaS) | Public cloud provider (vendor-agnostic) | Yes (loyalty data) | Managed database, application service for the loyalty API, object storage for exports, backup vault |
| SYS-05 | Point-of-sale (POS) system | Vendor-managed: 11 registers (8 lanes, 2 self-checkouts, 1 service desk), in-store back office server, vendor cloud portal | Encrypted card data only (P2PE); loyalty lookups | 11 P2PE PIN pads (PCI-approved PTS devices). **Shared administrator account** on the POS back office (see gaps). POS vendor provides only a SOC 2 Type 1 report (Security, as of 2025-12-31) and no PCI DSS AOC (P09) |
| SYS-06 | Back office and inventory (purchasing, receiving, item and price file) | Vendor SaaS | Employee and supplier data | Sends the price file to the POS and storefront each night |
| SYS-07 | Refrigeration and building IoT monitoring | On-premises controllers and sensors with a vendor cloud dashboard | No | 46 case temperature sensors, 6 refrigeration controllers, HVAC and energy management. **On the corporate network** (see gaps) |
| SYS-08 | Store network and Wi-Fi | On-premises | Encrypted card data in transit only | Firewall, switches, corporate Wi-Fi, guest Wi-Fi (separated, internet only), POS VLAN managed by the POS vendor |
| SYS-09 | Identity provider (single sign-on and MFA) | SaaS | No (identities only) | Protects email, the storefront admin console (for employees), the cloud console, and SYS-06 |
| SYS-10 | Productivity suite (email and files) | SaaS | Yes (loyalty exports as attachments) | Customer service mailbox |
| SYS-11 | Endpoints | On-premises | Yes (cached exports) | 16 Windows PCs and laptops, 18 handheld devices (inventory scanning and order picking) |
| SYS-12 | Pricing and personalized offers engine | Vendor SaaS add-on to the storefront and loyalty program | Loyalty purchase history, ZIP code, delivery zone | Live since March 2026 (see P10). Staff also use an approved generative AI assistant for marketing copy with no customer data (P10 AI-002) |
| SYS-13 | CCTV | On-premises recorder | Video | No facial recognition. 30-day retention |

**SSP system (P02):** the *E-commerce and Loyalty Platform (ELP)*: SYS-01, SYS-03, SYS-04, SYS-09, SYS-12, and the administrator endpoints (SYS-11) that manage them, with interfaces to SYS-02, SYS-05, SYS-06, and SYS-10.

## 4. Current security posture: partially compliant

**In place today:**
- Validated P2PE solution for all in-store card payments; manual card entry on register keyboards is disabled
- Processor's embedded payment page for online checkout; the storefront never receives card numbers
- Receipts show only the last 4 digits of the card number and no expiration date (FACTA)
- MFA through the identity provider for email, the cloud console, and employee access to the storefront admin console
- Guest Wi-Fi separated from the corporate network (internet only)
- The POS vendor patches registers and the POS back office monthly
- Anti-malware on office PCs
- Daily managed backups of the loyalty database, in the same cloud account
- The processor's service provider AOC (dated 2024) and the storefront vendor's SOC 2 Type 2 report on file
- Background checks for managers and office staff
- A one-page "PCI policy" from a template, signed in 2023

**Missing or weak, found in the 2026 assessments:**
1. The 2025 SAQs were completed and signed by the majority owner without scoping help or a QSA. The SAQ A eligibility criterion that the website is not susceptible to script attacks was attested without evidence. There is no documented PCI DSS scope (Requirement 12.5.2).
2. The checkout page's scripts are not inventoried, authorized, or integrity-checked, and there is no change and tamper detection on the payment page (Requirements 6.4.3 and 11.6.1). Fieldwork found 14 third-party scripts on the checkout page, 3 with no known owner. The marketing contractor can add scripts through the storefront's tag manager.
3. One **shared administrator account** on the POS back office is used by the Store Manager, 2 assistant managers, and POS vendor technicians. Its password has not changed since installation in 2022.
4. Refrigeration and building IoT devices sit on the corporate network with office PCs and handhelds. The refrigeration contractor has an always-on remote access tool.
5. Full loyalty database exports (names, phones, emails, ZIP codes, purchase history) are emailed monthly to the marketing contractor as unencrypted spreadsheets. There is no contract clause on security or data use.
6. No written incident response plan. Staff do not know the merchant agreement's notice term (notify the acquirer within 24 hours of suspecting a compromise; fictional).
7. No review of storefront admin, cloud, or identity provider logs.
8. PIN pad inspections are not scheduled or recorded, and the device list has not been reconciled with the processor's inventory (Requirement 9.5.1).
9. No security policies beyond the 2023 one-page template.
10. Security training is limited to skimmer awareness for cashiers at hire. Office staff get no phishing training.
11. Storefront admin console: 9 administrator accounts. The marketing contractor and one legacy account use local passwords without MFA. P07 testing found 4 former employees still active.
12. Loyalty database backups are in the same cloud account as production and have never been restore-tested.
13. The pricing and offers engine went live without fairness testing across ZIP codes and neighborhoods, and without a review of the "personalized savings" claims in marketing.
14. No list of third-party service providers with their PCI DSS responsibilities, and no annual check of their compliance status (Requirement 12.8). The processor's AOC on file is from 2024.
15. The corporate Wi-Fi passphrase has not changed since 2023 and is known to former employees.
16. A search of the customer service mailbox found 2 emails in which customers had typed full card numbers (found in P03 fieldwork).

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 primary regulation | PCI DSS v4.0.1 (contractual standard), with FTC Act Section 5 as the secondary regulation and a one-row FACTA check |
| P08 incident | Payment card data compromise through e-commerce skimming: a malicious script injected into the checkout page through a compromised third-party tag |
| P09 SOC 2 | SOC 2 is **not** the company's assurance mechanism (PCI DSS validation is). (a) Security-only readiness check as an internal benchmark; (b) review of the POS vendor's and e-commerce platform vendor's assurance reports |
| P10 AI | Dynamic pricing and personalized offers (SYS-12) |
| Cloud | Vendor-agnostic. Services are described by category, with AWS, Azure, and Google Cloud equivalents noted only for shared responsibility |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-06-15 | Acquirer letter confirming validation type (SAQ P2PE and SAQ A) |
| 2026-07-20 to 2026-07-31 | Risk assessment and gap analysis fieldwork |
| 2026-08-10 to 2026-08-14 | Control assessment fieldwork |
| 2026-08-24 to 2026-08-28 | SOC 2 readiness benchmark and AI assessment |
| 2026-09-04 | Deliverables approved by the General Manager (High risks by the majority owner) |
| 2026-11-30 | 2026 SAQs and attestations due to the acquirer |
