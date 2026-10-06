# Scenario facts: Cris Santos Company | Other Services | Micro

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a law, regulation, or standard, the citation is given. Facts about the payment processor, customers, and vendors are fictional.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (independent electronics and device repair shop) |
| Business | Electronics and device repair (NAICS 811210): phones, tablets, laptops, desktops, and game consoles. Screen, battery, and port repairs; board-level (microsoldering) repair; **data transfer** to a new device; **basic data recovery** from working or lightly damaged devices (severe cases go to an outside data recovery lab); and a free **device recycling drop-off** with data wiping. An **independent shop**: not a manufacturer-authorized service provider |
| Location | Florida. **One storefront** in a strip shopping center: a front counter and a back repair room. Open 10:00 to 19:00, Monday to Saturday |
| Workforce | 7 employees: the Owner, 1 Shop Manager, 1 Senior Technician, 2 Repair Technicians, and 2 Counter Associates |
| Revenue | About $1.1 million a year (fictional), about $3,600 per business day. Under the SBA standard of $34.0 million for NAICS 811210 (13 CFR 121.201), so SBA-small |
| Volume | About 6,800 repair tickets a year (about 22 per business day). About 380 data transfer or recovery jobs a year, of which about 25 go to the outside lab. About 900 recycling drop-off devices a year. About 4% of customers give an out-of-state address (seasonal residents and visitors) |
| Customers | About 15,500 customer records in the ticketing system (every customer since 2019): names, phone numbers, email addresses, device make, model, serial number or IMEI, and repair history. **18 business accounts** (real estate offices, a property management company, and restaurants) are invoiced monthly and pay by ACH or check |
| Card acceptance | About 6,100 card transactions a year on **2 payment terminals plus 1 spare** that belong to a **validated PCI-listed P2PE solution** from the payment processor. The terminals are semi-integrated with the ticketing system: the system sends the amount, and the terminal returns only an approval and a truncated card number. Phone payments are keyed directly into a terminal. No e-commerce checkout |
| PCI DSS status | **Merchant.** PCI DSS v4.0.1 applies through the merchant agreement. It is a contractual standard, not law. In a letter dated 2026-04-15 (fictional), the processor confirmed annual validation on **SAQ P2PE** (PCI DSS v4.0.1 SAQ P2PE, October 2024), due 2026-12-15. Merchant levels are set by the card brands and are not stated here |
| Not in scope | **FTC Safeguards Rule (16 CFR Part 314):** the company extends no credit and offers no financing, so it is not a "financial institution" (16 CFR 314.1(b)). **HIPAA:** not a covered entity or business associate; the business accounts are not health care providers or health plans. **COPPA:** the website and messaging are not directed to children. **Florida Digital Bill of Rights:** does not apply; a "controller" under Fla. Stat. 501.702 must exceed $1 billion in global gross annual revenue. **Trade-ins:** the company does not buy or resell used devices. **SEC disclosure:** privately held |
| Other applicable law | **FTC Act Section 5** (15 U.S.C. 45(a)(1), 45(n)). **Fla. Stat. 501.171** (2026): reasonable security measures (2), breach notice (3)-(6), and disposal of customer records (8). **FTC Disposal Rule** (16 CFR Part 682): applies **only to consumer report information**, which here means the 2 background check reports on technicians hired in 2025. Other states' breach laws for customers who live elsewhere |
| Benchmark | NIST CSF 2.0 (voluntary; no sector cybersecurity rule applies). **NIST SP 800-88 Rev. 2**, *Guidelines for Media Sanitization* (final, September 2025), for wiping recycled devices and retired shop equipment |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notice and disposal, Fla. Stat. 501.171). Other state law is treated generically ("each state where affected individuals reside") |

## 2. People (role titles only)
| Role | Security and privacy duties |
|---|---|
| Owner | Works full time in the business as general manager and repairs on busy days. Accepts Moderate risk; approves treatment plans for High risks, policies, and spending |
| Shop Manager | **Security and Privacy Lead** (designated in writing on 2026-07-15). Runs the counter, scheduling, vendor contracts, the merchant agreement and SAQ, the cyber insurance policy, and the business accounts. Day-to-day owner of the security program |
| Senior Technician | Board-level repair, data transfer, and data recovery. Maintains the bench workstations and bench storage **informally** (not trained or designated for it). Business owner of the diagnostic side of the AI assistant (P10) |
| Repair Technicians (2) | Repairs, diagnostics, recycling drop-off wiping |
| Counter Associates (2) | Intake, customer communication, payments, device release |
| Managed service provider (MSP) (external) | Office endpoints, firewall and Wi-Fi, productivity suite administration, and the cloud backup. Does **not** manage the bench workstations or bench storage |
| Ticketing and POS vendor (external) | SaaS repair-shop management platform with the built-in AI assistant. SOC 2 Type 2 report (Security) available under NDA (P09) |
| Payment processor (external) | P2PE solution provider and processor; PCI DSS validated service provider |
| E-waste recycler (external) | Collects recycling drop-off devices and retired equipment each quarter |
| Outside data recovery lab (external) | Receives severely damaged drives by courier for clean-room recovery |
| Outside bookkeeper and payroll service (external) | Bookkeeping and biweekly payroll |

## 3. Systems
| ID | System | Hosting | Personal or card data? | Notes |
|---|---|---|---|---|
| SYS-01 | **Service ticketing and point-of-sale platform**: intake, tickets, customer records, parts inventory, invoicing, POS, text and email status updates | Vendor SaaS | Yes: 15,500 customer records; **device passcodes and account passwords in a free-text ticket note field** (see gaps); no card data by design | System of record. Named accounts for the Owner, Shop Manager, and 3 technicians with MFA; **one shared "Counter" login without MFA** on the counter PCs |
| SYS-02 | Payment processor P2PE solution and merchant portal | Service provider | Card data (processor side only) | 2 counter PIN pads and 1 spare. The company never holds decryption keys. Merchant portal used by the Shop Manager with MFA |
| SYS-03 | Productivity suite (email, files, calendar) | SaaS | Yes (customer emails, business account invoices, HR files) | MSP administers; MFA on all named accounts; a shared "repairs" mailbox opened from the counter PCs |
| SYS-04 | Office endpoints | On-premises, MSP-managed | Yes (cached) | 2 counter PCs, the Shop Manager's laptop, and the Owner's laptop. MSP antivirus and patching; laptops encrypted, **counter PCs not encrypted** |
| SYS-05 | Bench workstations | On-premises, **not MSP-managed** | Yes (customer data during transfers and diagnostics) | 3 bench PCs and 1 data transfer station running diagnostic, flashing, and data transfer tools. **One shared local "bench" account**; USB storage allowed; built-in antivirus often turned off because flashing tools trigger it |
| SYS-06 | Bench storage | On-premises (back room) | Yes (customer data copies and recovery images) | A small network storage device (8 TB) used to stage data transfers and keep recovery images. **Kept indefinitely** (see gaps) |
| SYS-07 | Shop network | On-premises, MSP-managed | Card data in transit (encrypted by P2PE) | Firewall and router, staff Wi-Fi, separate guest Wi-Fi. **Customer devices under repair join the staff Wi-Fi**, which also carries the counter PCs, bench PCs, and bench storage. One business internet line; no failover |
| SYS-08 | Cloud backup | SaaS, operated by the MSP | Yes | Nightly backup of the productivity suite and of the bench storage; 1-year retention; one MSP administrator login; **never restore-tested** |
| SYS-09 | Security cameras | Cloud-managed cameras | Video | Counter and bench areas; 30-day retention; viewed on the Owner's phone app |
| SYS-10 | AI assistant built into SYS-01 | Vendor SaaS (the SYS-01 vendor with a model provider as its subprocessor) | Yes (chat and text transcripts; ticket notes and symptoms) | **AI-001.** Answers website chat and text messages (status, hours, price ranges) and suggests likely faults and parts to technicians from the intake notes. Turned on 2026-05-04 (P10) |

**SSP system (P02):** the *Service Ticketing and Point-of-Sale System (STPS)*: SYS-01 to SYS-08, with interfaces to SYS-09 and SYS-10.

## 4. Current security posture: early to partial
**In place today:**
- Validated P2PE terminals for all card payments; the processor confirmed SAQ P2PE
- MFA on the productivity suite, the merchant portal, and named SYS-01 accounts
- MSP patching, antivirus, and firewall on the 4 office endpoints; guest Wi-Fi separated
- Laptop encryption
- A printed intake form with the customer's signed consent to power on and test the device
- Security cameras at the counter and bench; a keypad lock on the back room; an after-hours alarm
- A quarterly e-waste pickup with a certificate of recycling per pickup
- Background checks on the 2 technicians hired in 2025
- A cyber liability endorsement on the business insurance policy, with a breach hotline

**Missing:**
1. Device passcodes, and sometimes the customer's account email and password (for activation lock or account sign-in), are typed into a **free-text SYS-01 ticket note visible to every user**. Paper intake tags taped to devices also show the passcode. A search on 2026-07-22 found about 5,200 tickets with passcodes and 310 with account passwords.
2. No rule limits what technicians may open on a customer device. Bench PCs use one shared local account, USB storage is allowed, and nothing is logged. A customer complaint on 2026-03-14 alleged that a technician looked through personal photos; it was looked into informally and was inconclusive.
3. Customer data is kept indefinitely: about 2.3 TB on the bench storage from about 610 jobs older than 30 days, and copies in the cloud backup for a year.
4. No media sanitization standard. Recycling drop-off devices get a factory reset by whichever technician is free, with no record per device and no check. The recycler's certificates cover pickups, not devices.
5. The counter PCs share one SYS-01 login without MFA. Its password has not changed since 2024, although a Counter Associate who knew it left on 2026-05-08.
6. During phone payments, staff sometimes write card numbers on sticky notes or in ticket notes before keying them into the terminal. PIN pad inspections are not done.
7. No written incident response plan. Staff do not know the processor's notice term.
8. Customer devices under repair, some of them infected, join the same Wi-Fi as the counter PCs, bench PCs, and bench storage.
9. No security policies. The only document is the intake form, which tells customers that "our technicians never access your personal data".
10. No security awareness training; new staff get an informal walkthrough.
11. The cloud backup has never been restore-tested, and its only administrator login (held by the MSP) has no MFA.
12. The AI assistant was turned on by the Shop Manager without any review. The website says "AI diagnosis in minutes, right every time".
13. No vendor list with data flows. The outside data recovery lab, the courier, and the recycler handle customer data with no contract security terms.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 primary benchmark | NIST CSF 2.0 (voluntary; all 106 subcategories). Secondary: the binding legal baseline (FTC Act Section 5, Fla. Stat. 501.171, other states' breach laws, the FTC Disposal Rule for background reports) and PCI DSS v4.0.1 SAQ P2PE (binding by contract), with an applicability screen |
| Regulatory driver IDs | N81-R01 FTC Act Section 5; N81-R02 state breach and data security laws (Fla. Stat. 501.171 as the worked example); N81-R03 PCI DSS v4.0.1; N81-R04 FTC Disposal Rule (background reports only); `N81-BM` for the NIST CSF 2.0 benchmark and SP 800-88 Rev. 2. N81-R05 (COPPA) and N81-R06 (HIPAA) are screened out in P03 |
| P08 incident | Customer device data exposure and point-of-sale compromise: (A) a technician copies personal data from a customer device in the shop's custody, or (B) the shared counter login is phished and ticket notes with passcodes, account passwords, and card numbers are exported. The MSP and the cyber insurer are in the notification chain |
| P09 SOC 2 | Security plus Confidentiality. The company is not a SOC 2 service organization. The readiness check answers a vendor security questionnaire from the property management business account (due 2026-10-30); also a review of the ticketing and POS vendor's SOC 2 Type 2 report |
| P10 AI | One use case, AI-001: the SYS-01 AI assistant. The registry default ("AI-assisted diagnostics and customer chatbot") is kept, because at this size both functions come from one vendor feature: customer chat and text replies, and fault and parts suggestions to technicians |
| Cloud | SaaS plus one cloud workload: the MSP-operated cloud backup (SYS-08). Vendor-agnostic |
| Primary system | Registry default kept: the service ticketing and point-of-sale system (SYS-01) and what supports it |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-04-15 | Processor letter confirming SAQ P2PE validation |
| 2026-07-20 to 2026-07-31 | Risk assessment and gap analysis with the MSP (shop walkthrough and SYS-01 searches 2026-07-22) |
| 2026-08-10 to 2026-08-12 | Control assessment by an independent consultant (on site 2026-08-11) |
| 2026-08-17 to 2026-08-21 | SOC 2 readiness self-assessment, vendor report review, and AI assessment |
| 2026-08-31 | Deliverables approved by the Owner |
| 2026-10-30 | Response due to the property management account's security questionnaire |
| 2026-12-15 | 2026 SAQ P2PE and attestation due to the processor |

## 7. Facts added while building the deliverables
These facts were added because the deliverables needed them. They do not change sections 1-6.

| Topic | Added fact | Used in |
|---|---|---|
