# Scenario facts: Cris Santos Company | Other Services | Sole Proprietorship

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a law, regulation, or standard, the citation is given. Facts about the payment processor, vendors, contractors, and customers are fictional.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship; the owner-technician files Schedule C) |
| Business | Electronics and device repair (NAICS 811210): phone, tablet, laptop, and game console repair (screens, batteries, charging ports, basic board repair), **data transfer** to a new device, basic **logical data recovery** from working or lightly damaged devices (no clean room), and a free **recycling drop-off** for old devices with data wiping |
| Location | Florida. One leased storefront of about 600 square feet in a strip plaza: a front counter, a repair bench behind a half wall, and a locked storage cabinet for devices waiting for repair or pickup. Open Tuesday to Saturday, 10:00 to 18:00. Closed Sunday and Monday |
| Workforce | The owner-technician only (0 employees). Uses contracted help instead of staff |
| Revenue | About $180,000 a year (fictional), about $720 per business day (about 250 business days). About 80% repairs, 12% data transfer and recovery, 8% accessories. SBA-small (standard $34.0 million for NAICS 811210, 13 CFR 121.201) |
| Volume | About 1,400 repair tickets a year (about 6 per business day). About 220 data transfer jobs and 40 data recovery jobs a year. About 150 recycling drop-off devices a year. At any time about 25 customer devices are in the shop's custody |
| Customers | About 5,600 customer records in the ticketing system (every customer since 2019): names, phone numbers, email addresses, some mailing addresses, device make, model, serial number or IMEI, repair history, and intake photos. About 12% have out-of-state addresses (seasonal residents and visitors). Consumers only; no business service contracts |
| Card acceptance | About 1,250 card transactions a year on **one countertop card terminal** that belongs to a **validated PCI-listed P2PE solution** from the payment processor. A few customers a month pay by phone (usually a relative paying for a repair); the owner keys those card numbers directly into the terminal. No online checkout and no payment links |
| PCI DSS status | **Merchant.** PCI DSS v4.0.1 applies through the merchant agreement (a contract, not law). The processor's merchant portal asks for annual validation on **SAQ P2PE** (PCI DSS v4.0.1 SAQ P2PE, October 2024), with the 2026 SAQ due **2026-12-31** (fictional term). The owner has **never completed an SAQ**; the processor charges a monthly non-validation fee (fictional term). Merchant levels are set by the card brands and the acquirer and are not stated here |
| Not in scope | **FTC Safeguards Rule (16 CFR Part 314):** the business offers no credit or financing, so it is not a "financial institution" (16 CFR 314.1(b)). **FTC Disposal Rule (16 CFR Part 682):** the business obtains no consumer reports (no employees, no background checks), so it holds no "consumer information" (682.1(b)); revisit before any hire or background check. **HIPAA:** not a covered entity or business associate; health data on customer devices is not PHI in the shop's hands. **COPPA:** the website and booking form are not directed to children. **Florida Digital Bill of Rights:** a "controller" must exceed $1 billion in global gross annual revenue (Fla. Stat. 501.702), so it does not apply. **Trade-ins and resale:** the business does not buy or resell used devices. **SEC disclosure:** not publicly traded |
| Other applicable law | **FTC Act Section 5** (15 U.S.C. 45(a)(1) and 45(n)): unfair or deceptive practices, including untrue privacy promises and unreasonable handling of customer devices and data. **Fla. Stat. 501.171** (2026): the definition of "covered entity" expressly includes a sole proprietorship ((1)(b)); reasonable security measures (2), breach notice (3) to (6), and disposal of customer records (8). Other states' breach laws for out-of-state customers |
| Benchmark | NIST CSF 2.0 (voluntary; no sector cybersecurity rule applies). **NIST SP 800-88 Rev. 2**, *Guidelines for Media Sanitization* (final, September 2025; supersedes Rev. 1 of December 2014), for wiping customer and recycled devices |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (Fla. Stat. 501.171). Other state law is treated generically ("each state where affected individuals reside") |

## 2. People and contracted services (role titles only)
| Role | Duties |
|---|---|
| Owner-technician | Every role: owner, only technician, security and privacy lead, incident lead, and risk acceptor. Runs the shop's own IT |
| Fill-in technician (independent contractor) | A local repair technician who covers the shop about 12 days a year (owner vacation or illness), paid by the day. **No written agreement. Uses the owner's ticketing login** |
| Bookkeeper (independent contractor) | Monthly bookkeeping and sales tax filing in the accounting SaaS through a named bookkeeper account. No access to the ticketing system |
| Independent security consultant | Engaged for 8 paid hours under a confidentiality agreement to help run the July 2026 self-assessment and tests. No standing access |
| Ticketing and POS vendor | SaaS repair-shop management platform. Provides a SOC 2 Type 2 report under a nondisclosure agreement |
| Payment processor | P2PE solution provider and processor for the acquiring bank. A PCI DSS validated service provider |
| Certified electronics recycler | Collects recycling drop-off devices and scrap parts each quarter and issues a certificate of destruction per lot. **Contract has no data security terms** |

## 3. Systems
| ID | System | Hosting | Personal or card data? | Notes |
|---|---|---|---|---|
| SYS-01 | **Service ticketing and point-of-sale platform**: intake, tickets, customer records, parts inventory, invoices, payment recording, SMS and email status updates | Vendor SaaS | Yes: 5,600 customer records; **device passcodes and some account passwords in a free-text ticket notes field** (see gaps); no card data by design | System of record. One account only (the owner's administrator account), used by the owner and the fill-in technician. MFA available but **off** |
| SYS-02 | Payment processor P2PE terminal and merchant portal | Service provider | Card data (processor side only) | One countertop terminal (Wi-Fi with cellular fallback). The owner never holds decryption keys. Portal MFA enforced by the processor |
| SYS-03 | Productivity suite (business email, calendar, file storage) | SaaS, business plan | Yes (customer emails, scanned forms, supplier records) | MFA on. File version history on |
| SYS-04 | Accounting SaaS and business bank portal | SaaS | Yes (invoice names and totals; no card numbers) | MFA on for both. Bookkeeper has a named account |
| SYS-05 | Owner laptop | Owner device | Yes (cached email and files) | Full-disk encryption on; automatic updates; built-in antivirus. Used for administration, never connected to customer devices |
| SYS-06 | **Repair bench PC and two external transfer drives** | Owner devices (shop) | Yes: **customer device data from transfers and recoveries** | Desktop PC running diagnostic, flashing, and data transfer tools. **One local administrator account with no password; no disk encryption; drives unencrypted.** About 1.6 TB of customer data from about 350 jobs since 2021 kept on the PC and drives (see gaps) |
| SYS-07 | Counter tablet | Owner device | Yes (cached SYS-01 data; customer signatures) | Runs the SYS-01 app for intake and checkout. Passcode lock after 2 minutes |
| SYS-08 | Owner mobile phone | Owner device | Yes (business texts, intake photos until uploaded) | Business number; texts with customers; authenticator app for MFA; camera for intake photos |
| SYS-09 | Shop network | Internet provider router (on site) | Card data in transit (encrypted by P2PE) | **One flat Wi-Fi network** shared by the laptop, tablet, bench PC, terminal, customer devices under repair, and customers (guest password posted on the wall). Router administrator password never changed from the default |
| SYS-10 | Cloud security cameras (2: counter and bench) | Consumer camera vendor cloud | Video (customers; the bench camera can see device screens) | 30-day cloud retention. Camera account uses a password only |
| SYS-11 | Website and online booking form | Website builder SaaS | Yes (name, phone, email, device, problem description) | Booking requests arrive by email (SYS-03) |
| SYS-12 | General-purpose generative AI assistant (consumer plan) | AI vendor SaaS | Yes (pasted ticket notes, error logs, device screen photos) | Used for diagnostics and to draft customer messages since 2026-02. Default setting lets the vendor use chats to train its models. See P10 |

**SSP system (P02):** the *Service Ticketing and Point-of-Sale System (STPS)*: the ticketing and POS platform (SYS-01) and every account, device, and network that reaches it or holds customer data (SYS-01 to SYS-12).

## 4. Current security posture: early (few formal controls)
**In place today:**
- A validated P2PE terminal for every card payment
- MFA on the productivity suite, the accounting SaaS, the bank portal, and the processor's merchant portal
- A password manager used by the owner for the owner's own accounts
- Full-disk encryption, automatic updates, and built-in antivirus on the owner laptop; automatic updates on the tablet and phone; built-in antivirus on the bench PC
- The ticketing vendor's backups and its SOC 2 Type 2 report on request
- A printed intake form signed by each customer, with consent to power on and test the device
- A locked storage cabinet for devices in custody, a monitored shop alarm, and cloud security cameras
- A certified electronics recycler that issues certificates of destruction per lot

**Missing:**
1. Device passcodes, and sometimes the customer's email and account password (to remove an activation lock or sign in after a repair), are typed into the **free-text ticket notes field**. Paper intake tags taped to devices also show the passcode. A search on 2026-07-20 found about 3,100 tickets with passcodes and 85 with account passwords.
2. **One shared SYS-01 login** (the owner's administrator account) is used by the owner and the fill-in technician. MFA is off so that the account can be shared.
3. The bench PC has **no password and no disk encryption**, and the two external transfer drives are unencrypted. About 1.6 TB of customer data from about 350 transfer and recovery jobs since 2021 has never been deleted.
4. **No media sanitization procedure.** Recycling drop-off devices get a factory reset when time allows, with no record per device and no verification. The recycler's certificates cover lots, not serial numbers.
5. The shop network is **flat**: business devices, the card terminal, customer devices under repair (some infected), and customers' own phones share one Wi-Fi network. The router still has its default administrator password.
6. Card numbers for phone payments are sometimes written on sticky notes, **with the security code**, before being keyed into the terminal. P03 found 6 old notes in the counter drawer and 4 tickets with full card numbers typed into the notes. The terminal is never inspected, and no SAQ has ever been completed.
7. The intake form says **"We never access your personal data."** That is not true: testing a camera, a microphone, or a data transfer requires access.
8. No written policies, no incident plan, and no contact list.
9. No log review. SYS-01 records sign-ins and exports, but nobody has ever looked.
10. Customer data has been pasted into a **consumer generative AI assistant** (ticket notes, error logs, and screen photos), with the vendor's training setting left on.
11. **No vendor list and no contract terms**: the fill-in technician has no confidentiality agreement, the recycler contract has no data terms, and the AI assistant is on consumer terms.
12. **Single-person dependency**: the owner holds every credential and is the only technician; nobody else can return customer devices if the owner is unavailable.
13. No security training beyond what the owner reads on repair forums.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 primary benchmark | NIST CSF 2.0 (voluntary; all 106 subcategories), checked by self-attestation. Secondary: the binding legal baseline (FTC Act Section 5 and Fla. Stat. 501.171, plus other states' breach laws), PCI DSS v4.0.1 SAQ P2PE (binding by contract), and an applicability screen |
| Regulatory driver IDs | N81-R01 FTC Act Section 5; N81-R02 state breach laws (Fla. Stat. 501.171 as the worked example); N81-R03 PCI DSS v4.0.1. N81-R04 (Disposal Rule), N81-R05 (COPPA), and N81-R06 (HIPAA) do not apply at this size (P03 applicability screen). `N81-BM` points to the NIST CSF 2.0 benchmark and SP 800-88 Rev. 2 |
| P08 incident | **Ticketing and POS account takeover exposing customer device data**: the shared SYS-01 login (no MFA) is phished; the attacker exports customer records and ticket notes holding device passcodes, account passwords, and a few card numbers, and texts customers fake "pay now" links. This adapts the registry default ("customer device data exposure and point-of-sale compromise") to one incident type a one-person shop can run in the first 24 hours |
| P09 SOC 2 | Security criteria only. The shop is not a service organization and will never obtain a SOC 2 report. Used as (a) the owner's self-check and (b) a checklist for reading the ticketing vendor's SOC 2 report |
| P10 AI | **AI-001: the consumer generative AI assistant (SYS-12) used for diagnostics and drafting customer messages.** The registry default ("AI-assisted diagnostics and customer chatbot") is adapted: a one-person shop does not run its own diagnostics model or chatbot. The ticketing vendor's website chatbot add-on (AI-002) was trialed and not adopted; it is listed in the inventory only |
| Cloud | SaaS only. No IaaS or PaaS. Vendor-agnostic |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-07-20 to 2026-07-27 | Self-assessment (risk, gaps, and controls). The security consultant worked on site on Monday 2026-07-20 and Monday 2026-07-27, when the shop is closed; the owner did the self-review on the evenings in between |
| 2026-08-03 | AI use assessment and review of the ticketing vendor's SOC 2 report |
| 2026-08-31 | Deliverables adopted by the owner-technician |
| 2026-12-31 | 2026 SAQ P2PE due to the processor (fictional term) |

## 7. Facts added while building the deliverables
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| Ticketing vendor assurance | The ticketing and POS vendor's SOC 2 Type 2 report covers Security and Availability for the 12 months ending 2026-03-31 (unqualified; one change-approval exception, remediated). Its system description states RTO 4 hours and RPO 1 hour, notice to affected customers within 72 hours of confirming an incident, and a restricted credential field with automatic purge that is off by default. The owner reviewed it on 2026-08-03 | P02, P03, P04, P09 |
| SYS-01 logging and alerts | SYS-01 keeps sign-ins (with device and location), ticket views, and customer list exports for 90 days. Its new-sign-in alert emails were filtered into an email folder the owner does not read | P02, P03, P07, P09 |
| Fill-in technician access | The fill-in technician's last cover period was 2026-06-09 to 2026-06-13. On 2026-07-27 the SYS-01 account was still signed in on the fill-in technician's personal phone (last active 2026-06-13); the owner ended the session during the test. The shared SYS-01 password had not changed since 2024 | P02, P03, P07 |
| Processor notice term | The merchant agreement requires notice to the processor within 24 hours of suspecting a card data compromise (fictional term) | P02, P06, P08 |
| Shop router | The provider router supports a separate guest network that was never turned on (found in P04 mapping). An external port check on 2026-07-27 found no open inbound ports. The connected-device list showed 14 devices, including 5 customer devices under repair and 3 customers' phones, and a customer device on the bench could reach the counter tablet | P02, P04, P07 |
| Website wiping claim | The website's recycling page said drop-off devices are "wiped to military standards". In practice they get a factory reset when time allows | P03, P06, P07, P09 |
| Bench software and drives | Some flashing and unlocking tools on the bench PC came from repair forum links; autoplay was on for USB devices. The transfer drives are reused between customers and still held earlier customers' folders on 2026-07-27 | P03, P07, P09 |
| Drop-off bin test | On 2026-07-27 the drop-off bin held 9 devices: 4 had not been reset and 1 powered on to a home screen with photos | P07 |
| Paper records | Paper intake forms are kept one year in the locked cabinet and then cross-cut shredded with the shop's shredder. Printed day lists back to 2024 were kept in a box under the counter. All devices run vendor-supported operating system versions (checked 2026-07-20) | P03, P06, P07 |
| Cyber insurance | No standalone cyber insurance. Whether the general liability policy has a cyber endorsement is unconfirmed (owner action in P08) | P08 |
| AI-001 history review | Review on 2026-08-03 of the assistant's chat history: 212 chats since 2026-02; 31 included customer first names, 9 included ticket notes with device passcodes, and 14 included screen photos (3 showing a customer's notifications). Training setting turned off and chat deletion requested the same day. On 40 recent tickets, the first AI suggestion matched the confirmed fault 27 times; 2 suggestions were unsafe. The vendor offers a business plan with no-training terms | P01, P03, P10 |
| AI-002 chatbot trial | The ticketing vendor's website chatbot add-on ran as a free trial 2026-05-05 to 2026-05-19 (41 chats): 5 off-list price quotes, 3 chats with device passcodes, no AI disclosure. Not adopted; transcript deletion requested 2026-08-03 | P03, P10 |
| Other contracts | The bookkeeper works under an engagement letter. Customer status links in SYS-01 show one ticket only | P02 |
| Budget and costs | Security budget approved 2026-08-31: about $450 one-time (two hardware-encrypted drives, about $350, and one consultant hour, about $100), plus an AI business plan (about $25 a month) if kept and a SYS-01 extra user fee (about $20 a month, cover months only) | P01, P07 |
| Device lock times | Laptop 5 minutes, tablet 2 minutes, phone 1 minute; bench PC none until fixed | P02, P06 |
