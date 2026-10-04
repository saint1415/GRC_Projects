# Scenario facts: Cris Santos Company | Mining, Quarrying, and Oil and Gas Extraction | Sole Proprietorship

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship; the owner-operator files Schedule C) |
| Business | Owner-operated oilfield services contractor (NAICS 213112 Support Activities for Oil and Gas Operations). Two service lines: **contract pumping** (daily lease operating rounds: gauging tanks, checking wells and tank batteries, chemical treatment, recording run tickets) and **well-site automation service** (programming and troubleshooting remote terminal units (RTUs), programmable logic controllers (PLCs), rod pump controllers, electronic flow meters, and cellular modems) |
| Why a contractor and not a producer | Size substitution from the vertical's primary industry (NAICS 211120): a sole proprietor does not typically operate crude production. The business supports producers under master service agreements (MSAs), so most sector security expectations reach it through contract flow-down |
| Location | Florida. Home office and equipment shed at the owner's residence in northwest Florida. Field work at customers' onshore well sites and tank batteries in the Florida Panhandle, within about 60 miles of home |
| Workforce | The owner-operator only (0 employees). Two independent helpers are hired by the day for rig-up or tank cleaning work (paid on Form 1099). Helpers have no access to any system |
| Customers | 4 small independent producers, each under an MSA. The owner pumps 34 wells (Customer A 18, Customer B 6, Customer C 6, Customer D 4) and provides automation service to Customers A and B (about 60 field devices) |
| Revenue | About $180,000 a year (fictional): contract pumping about $115,000, automation service about $65,000. Customer A is about 45% of receipts. SBA-small (standard $47.0 million in average annual receipts for NAICS 213112, 13 CFR 121.201) |
| Customer A MSA security schedule (2025 renewal) | (1) protect Customer A confidential information (production data, control programs, network details, credentials) with reasonable safeguards and never in personal accounts; (2) remote access only through Customer A's VPN with Customer A-issued MFA; (3) notify Customer A's production superintendent of any suspected security incident that could affect Customer A data or systems **within 24 hours** of discovery; (4) no change to control logic or setpoints without the production superintendent's written (email) approval, and a record of each change; (5) no disclosure of Customer A data to third parties, including software services, without written consent; (6) return or destroy Customer A data within 30 days after the MSA ends; (7) answer an annual security questionnaire (organized by NIST CSF 2.0; 2026 answers due 2026-09-30); (8) carry technology errors and omissions or cyber liability coverage of at least $1 million while holding remote access |
| Other MSAs | Customers B, C, and D: standard confidentiality clause only (customer information is confidential and must be returned on request) |
| Personal information held | W-9 forms (names and Social Security numbers) for the 2 helpers. Customer contacts are business contacts. The owner holds no royalty owner, employee, or consumer records |
| Contrast worth noting | If the owner only pumped wells and never connected a laptop to a customer's control equipment, the cyber-physical exposure and most of Customer A's security schedule would fall away. Function, not size, decides the exposure |
| Not in scope | Offshore, Outer Continental Shelf, MTSA facilities, and vessels (none). Pipelines: the owner works only on production facilities and flow lines; no work on regulated gathering or transmission lines. TSA Security Sensitive Information (none held). EAR-controlled technology (none; commercial field equipment only). Federal contracts (none). Payment cards (not accepted; customers pay by ACH) |
| State law approach | Florida law is cited only where unavoidable: Fla. Stat. 501.171 (data security, breach notice, disposal), which names a sole proprietorship as a covered entity (501.171(1)(b)) |

## 2. People and contracted services (role titles only)
| Role | Duties |
|---|---|
| Owner-operator | Every role: owner, security lead, risk acceptor, incident commander, policy approver, and the person being assessed |
| On-call IT technician | Hourly help with the laptop, phone, and home network. No standing access; uses an attended remote-support session that the owner starts |
| Day helpers (2, independent contractors) | Field labor only. No system access. Their W-9 forms are the only personal information the business holds |
| Customer A production superintendent | Approves logic and setpoint changes; receives incident notices under the MSA security schedule |
| Customer A IT and SCADA contact | Issues the VPN account and MFA token; sends the annual security questionnaire |
| Customer B operations manager | Gave the owner the shared remote-desktop login to Customer B's SCADA operator workstation |
| Independent contract pumper (nearby) | Informal mutual coverage when either pumper is sick or away. No written agreement |
| Insurance agent | General liability and commercial auto policies (required by the MSAs). No cyber coverage |

## 3. Systems
| ID | System | Hosting | Sensitive data? | Notes |
|---|---|---|---|---|
| SYS-01 | Business productivity suite: email, calendar, cloud file storage (business plan, basic tier) | SaaS | Yes | System of record for customer reports: daily gauge sheets, run ticket copies, PLC and RTU program backup copies (synced folder), customer network notes, helper W-9 scans. MFA on with text-message codes. File version history kept 30 days by default |
| SYS-02 | Accounting and invoicing service | SaaS | Yes | Invoices, customer billing contacts, ACH receipts, bank feed, helper 1099 data. Password only (MFA available, off) |
| SYS-03 | Field laptop (rugged) | Owner device | Yes | Business IT and OT engineering tool in one: email and web, PLC, RTU, and flow meter configuration software, Customer A VPN client, Customer B remote-desktop client with the saved shared login, and a spreadsheet of customer site passwords. Full-disk encryption on. The owner signs in with an administrator account for everything |
| SYS-04 | Smartphone | Owner device (business and personal use) | Yes | Email, text-message MFA codes, hotspot for the laptop, Customer A alarm viewer app (view only), photos of gauges and run tickets |
| SYS-05 | Customer remote access paths | Customer-owned (outside the boundary) | Access path | Customer A: VPN with Customer A-issued MFA. Customer B: a third-party remote-desktop tool on Customer B's SCADA operator workstation, unattended access on, one shared login, no MFA. Customers C and D: none |
| SYS-06 | Removable media and programming cables | Owner equipment | Yes (control programs) | 3 USB drives (one also used for personal files) and serial and Ethernet programming cables used at well sites |
| SYS-07 | Home office network | Internet service provider router at the residence | Yes (in transit) | Router admin password never changed from the default. Family devices share the same Wi-Fi |
| SYS-08 | Dynamometer card analysis service with AI failure prediction | Vendor SaaS (subscription, priced per well) | Yes (customer production data) | Used since March 2026 for 14 rod-pumped wells (Customers A and B). The owner uploads dynamometer cards and run time data. Vendor terms allow use of uploaded data to improve its models. See P10 |

**SSP system (P02):** the *Field Service Business Systems (FSBS)*: SYS-01 to SYS-04, SYS-06 to SYS-08, and the owner's credentials and client software for the SYS-05 customer remote access paths.

**Data flow in one line:** the owner reads tank gauges and well conditions on rounds (paper gauge book and phone photos), types them into a daily gauge sheet emailed to each customer (SYS-01), connects the laptop (SYS-03) to customer RTUs and PLCs on site by cable or remotely through SYS-05, saves program copies to the synced folder (SYS-01) and USB drives (SYS-06), uploads dynamometer cards to SYS-08, and bills each customer monthly from SYS-02.

## 4. Current security posture: informal (basic hygiene, large gaps)
**In place today:**
- MFA on the business email and file account (text-message codes)
- Full-disk encryption on the laptop (turned on by the IT technician at setup in 2024)
- Automatic operating system updates and the built-in antivirus on the laptop
- Phone passcode and fingerprint unlock
- Customer A remote access goes through Customer A's VPN with Customer A-issued MFA
- File version history in SYS-01 (30 days)
- Paper gauge book carried on rounds
- Customers' hardwired safety shutdowns at tank batteries (tank high-level switches) do not depend on the owner's systems
- General liability and commercial auto insurance

**Missing:**
1. No risk assessment and no written security policy before July 2026.
2. The laptop is used for email, web browsing, and customer control work from one administrator account. Nothing separates business IT from OT engineering use.
3. Customer site passwords (RTU, modem, operator workstation, and the Customer B remote-desktop login) are in a plain spreadsheet on the laptop, synced to SYS-01.
4. Customer B's remote-desktop path uses one shared login with unattended access and no MFA. The owner never raised it with Customer B.
5. No MFA on the accounting service. Email MFA uses text-message codes only.
6. Customer PLC and RTU program backups exist only on the laptop and the synced folder. No offline copy, and no way to tell which version is running in the field.
7. No record of logic and setpoint changes. Customer approvals are given by phone, although Customer A's MSA requires email approval.
8. One USB drive is used for both personal files and program transfers, and drives are not scanned before use on customer equipment.
9. The home router uses its default admin password, and family devices share the network.
10. No incident response plan and no contact list. The owner was not aware of the 24-hour notice clause in Customer A's MSA.
11. No backup of the laptop beyond file sync (sync copies deletions and encrypted files; version history is 30 days).
12. Customer production data went to the AI dynamometer service and a free generative AI chatbot without customer consent.
13. No cyber insurance, although Customer A's MSA requires coverage while the owner holds remote access.
14. No security training.
15. Single-person dependency: nobody else can run the rounds under contract or reach the accounts, and account recovery codes are not stored anywhere.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 benchmark | **NIST CSF 2.0 with NIST SP 800-82 Rev. 3 (voluntary benchmark)**, the vertical's primary benchmark, applied to the owner's own systems and to the owner's touch points with customer OT. No binding federal sector cybersecurity rule reaches the business: USCG Subpart F (N21-R01) and TSA SD Pipeline-2021-02G (N21-R02) do not apply, and CIRCIA (N21-R03) is proposed only. Binding rules checked: Fla. Stat. 501.171 (state law) and the Customer A MSA security schedule (contract flow-down) |
| Regulatory driver labels | `N21-BM (...)` means the P03 voluntary benchmark (NIST CSF 2.0 with SP 800-82 Rev. 3), with the CSF 2.0 subcategory or SP 800-82 Rev. 3 section in parentheses. `MSA-A (n)` means item n of the Customer A MSA security schedule (section 1). `Fla. Stat. 501.171(x)` marks the binding state duties. `N21-R03 (proposed)` marks CIRCIA items tracked but not required |
| P05 functions | 5 business functions, with the single-person dependency called out |
| P08 incident | Registry default kept and scaled: **ransomware on the owner's field laptop (business IT) with a path toward customers' field SCADA** through the saved Customer B remote-desktop login, the Customer A VPN client, the password spreadsheet, and USB or cable connections to field controllers. The owner has no SCADA of its own, so the runbook's job is to stop the spread and warn the customers fast |
| P09 SOC 2 | Security criteria only. The business would not obtain a SOC 2 report (no customer relies on a service it hosts). Used as (a) the owner's self-check to answer Customer A's annual questionnaire and (b) a checklist to read the productivity suite provider's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| P10 AI | Registry default adapted: the business cannot build a predictive maintenance model, so the one third-party AI tool assessed is the **dynamometer card analysis service with AI failure prediction** (SYS-08) that the owner uses for customers' rod-pumped wells. Second inventory entry: a free general-purpose generative AI chatbot used to draft service reports |
| Cloud | SaaS only. No IaaS or PaaS. Provider names are not used |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-07-20 to 2026-07-24 | Self-assessment by the owner-operator with the on-call IT technician (tests on 2026-07-23; home office and truck walkthrough 2026-07-21) |
| 2026-08-31 | Deliverables adopted by the owner-operator |
| 2026-09-30 | Customer A annual security questionnaire due (answered from P03 and P09) |

## 7. Facts added while building the deliverables
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| Customer B remote tool | During P07 testing on 2026-07-23 the owner found that the Customer B remote-desktop client on the laptop also stored the password, so anyone using the laptop's admin session could connect without typing it. The owner removed the saved password that day and emailed Customer B's operations manager on 2026-07-24 asking for named accounts and MFA | P01, P04, P07, P08 |
| AI chatbot use | Between April and July 2026 the owner pasted well names and daily production numbers for Customers A and C into a free generative AI chatbot to draft monthly service summaries (about 12 times). Use stopped 2026-07-24 | P01, P10 |
| Dynamometer service terms | The service's standard terms allow it to use uploaded data to improve its models; a paid tier offers a no-training option. Customer A never gave written consent for the uploads (MSA-A (5)) | P03, P10 |
| Customer A program changes | In the 12 months before the assessment the owner made 23 logic or setpoint changes for Customer A; 4 had email approval, the rest were approved by phone | P03, P07 |
| Laptop software | The PLC and flow meter configuration software is licensed per device. Moving it to a replacement laptop takes the IT technician about one working day, including license transfer | P05, P08 |
| Productivity suite assurance | The productivity suite provider publishes a SOC 2 Type 2 report (Security, Availability, Confidentiality) on its trust portal for business customers. The owner downloaded and reviewed it on 2026-07-22 | P02, P09 |
