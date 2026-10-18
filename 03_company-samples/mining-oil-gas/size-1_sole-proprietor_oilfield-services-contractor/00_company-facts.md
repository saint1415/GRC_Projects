# Scenario facts: Cris Santos Company | Mining, Quarrying, and Oil and Gas Extraction | Sole Proprietorship

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship; the owner-operator files Schedule C) |
| Business | Owner-operated oilfield services contractor (NAICS 213112 Support Activities for Oil and Gas Operations). Two service lines: **contract pumping** (daily lease operating rounds: gauging tanks, checking wells and tank batteries, chemical treatment, recording run tickets) and **well-site automation service** (programming and troubleshooting remote terminal units (RTUs), programmable logic controllers (PLCs), rod pump controllers, electronic flow meters, and cellular modems) |
| Why a contractor and not a producer | Size substitution from the vertical's primary industry (NAICS 211120): a sole proprietor does not typically operate crude production. The business supports producers under master service agreements (MSAs), so most sector security expectations reach it through contract flow-down |
| Location | Florida. Home office and equipment shed at the owner's residence in northwest Florida. Field work at customers' onshore well sites and tank batteries in the Florida Panhandle, within about 60 miles of home |
| Workforce | The owner-operator only (0 employees). Two independent helpers are hired by the day for rig-up or tank cleaning work (paid on Form 1099). Helpers have no access to any system (EV-001, EV-003, EV-005) |
| Customers | 4 small independent producers, each under an MSA. The owner pumps 34 wells (Customer A 18, Customer B 6, Customer C 6, Customer D 4) and provides automation service to Customers A and B (about 60 field devices) (EV-004, EV-028) |
| Revenue | About $180,000 a year (fictional): contract pumping about $115,000, automation service about $65,000. Customer A is about 45% of receipts (EV-004, EV-005). SBA-small (standard $47.0 million in average annual receipts for NAICS 213112, 13 CFR 121.201) |
| Customer A MSA security schedule (2025 renewal) | (1) protect Customer A confidential information (production data, control programs, network details, credentials) with reasonable safeguards and never in personal accounts; (2) remote access only through Customer A's VPN with Customer A-issued MFA; (3) notify Customer A's production superintendent of any suspected security incident that could affect Customer A data or systems **within 24 hours** of discovery; (4) no change to control logic or setpoints without the production superintendent's written (email) approval, and a record of each change; (5) no disclosure of Customer A data to third parties, including software services, without written consent; (6) return or destroy Customer A data within 30 days after the MSA ends; (7) answer an annual security questionnaire (organized by NIST CSF 2.0; 2026 answers due 2026-09-30); (8) carry technology errors and omissions or cyber liability coverage of at least $1 million while holding remote access (EV-010) |
| Other MSAs | Customers B, C, and D: standard confidentiality clause only (customer information is confidential and must be returned on request) (EV-011) |
| Personal information held | W-9 forms (names and Social Security numbers) for the 2 helpers. Customer contacts are business contacts. The owner holds no royalty owner, employee, or consumer records (EV-002, EV-003) |
| Contrast worth noting | If the owner only pumped wells and never connected a laptop to a customer's control equipment, the cyber-physical exposure and most of Customer A's security schedule would fall away. Function, not size, decides the exposure |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): offshore, Outer Continental Shelf, MTSA facilities, and vessels (none). Pipelines: the owner works only on production facilities and flow lines; no work on regulated gathering or transmission lines. TSA Security Sensitive Information (none held). EAR-controlled technology (none; commercial field equipment only). Federal contracts (none). Payment cards (not accepted; customers pay by ACH) |
| State law approach | Florida law is cited only where unavoidable: Fla. Stat. 501.171 (data security, breach notice, disposal), which names a sole proprietorship as a covered entity (501.171(1)(b)); applicability is recorded in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (FL-501.171) |

## 2. People and contracted services (role titles only)
| Role | Duties |
|---|---|
| Owner-operator | Every role: owner, security lead, risk acceptor, incident commander, policy approver, and the person being assessed |
| On-call IT technician | Hourly help with the laptop, phone, and home network. No standing access; uses an attended remote-support session that the owner starts (EV-006, EV-019) |
| Day helpers (2, independent contractors) | Field labor only. No system access. Their W-9 forms are the only personal information the business holds |
| Customer A production superintendent | Approves logic and setpoint changes; receives incident notices under the MSA security schedule |
| Customer A IT and SCADA contact | Issues the VPN account and MFA token; sends the annual security questionnaire |
| Customer B operations manager | Gave the owner the shared remote-desktop login to Customer B's SCADA operator workstation |
| Independent contract pumper (nearby) | Informal mutual coverage when either pumper is sick or away. No written agreement (EV-020, EV-028) |
| Insurance agent | General liability and commercial auto policies (required by the MSAs). No cyber coverage (EV-018) |

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv).

| ID | System | Hosting | Sensitive data? | Notes |
|---|---|---|---|---|
| SYS-01 | Business productivity suite: email, calendar, cloud file storage (business plan, basic tier) | SaaS | Yes | System of record for customer reports: daily gauge sheets, run ticket copies, PLC and RTU program backup copies (synced folder), customer network notes, helper W-9 scans. MFA on with text-message codes. File version history kept 30 days by default (EV-001, EV-002) |
| SYS-02 | Accounting and invoicing service | SaaS | Yes | Invoices, customer billing contacts, ACH receipts, bank feed, helper 1099 data. Password only (MFA available, off) (EV-003) |
| SYS-03 | Field laptop (rugged) | Owner device | Yes | Business IT and OT engineering tool in one: email and web, PLC, RTU, and flow meter configuration software, Customer A VPN client, Customer B remote-desktop client with the saved shared login, and a spreadsheet of customer site passwords. Full-disk encryption on. The owner signs in with an administrator account for everything (EV-006; saved Customer B password found in P07 testing, EV-IA-5) |
| SYS-04 | Smartphone | Owner device (business and personal use) | Yes | Email, text-message MFA codes, hotspot for the laptop, Customer A alarm viewer app (view only), photos of gauges and run tickets (EV-007) |
| SYS-05 | Customer remote access paths | Customer-owned (outside the boundary) | Access path | Customer A: VPN with Customer A-issued MFA. Customer B: a third-party remote-desktop tool on Customer B's SCADA operator workstation, unattended access on, one shared login, no MFA. Customers C and D: none (EV-012, EV-013) |
| SYS-06 | Removable media and programming cables | Owner equipment | Yes (control programs) | 3 USB drives (one also used for personal files) and serial and Ethernet programming cables used at well sites (EV-008) |
| SYS-07 | Home office network | Internet service provider router at the residence | Yes (in transit) | Router admin password never changed from the default. Family devices share the same Wi-Fi (EV-009, EV-029) |
| SYS-08 | Dynamometer card analysis service with AI failure prediction | Vendor SaaS (subscription, priced per well) | Yes (customer production data) | Used since March 2026 for 14 rod-pumped wells (Customers A and B). The owner uploads dynamometer cards and run time data. Vendor terms allow use of uploaded data to improve its models (EV-022, EV-023). See P10 |

**SSP system (P02):** the *Field Service Business Systems (FSBS)*: SYS-01 to SYS-04, SYS-06 to SYS-08, and the owner's credentials and client software for the SYS-05 customer remote access paths.

**Data flow in one line:** the owner reads tank gauges and well conditions on rounds (paper gauge book and phone photos), types them into a daily gauge sheet emailed to each customer (SYS-01), connects the laptop (SYS-03) to customer RTUs and PLCs on site by cable or remotely through SYS-05, saves program copies to the synced folder (SYS-01) and USB drives (SYS-06), uploads dynamometer cards to SYS-08, and bills each customer monthly from SYS-02.

## 4. Where the evidence is
This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Every item has a source system, an owner, and as-of and collected dates. For a one-person contractor the sources are the SaaS admin consoles, the accounting service's reports, bank and card statements, the inbox, signed agreements, the laptop and phone settings, the internet provider's app, and the insurance agent's portal.
- **Which rules and contracts apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps against the benchmark and the binding duties** are judged in the gap analysis (P03), and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

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
| 2026-07-13 to 2026-07-17 | Intake: the owner collects SaaS settings, accounting reports, statements, agreements, device settings and inbox records; inventories; obligations register |
| 2026-07-20 to 2026-07-24 | Self-assessment by the owner-operator with the on-call IT technician: BIA, risk assessment, gap analysis, and control assessment (tests on 2026-07-23; home office and truck walkthrough 2026-07-21) |
| 2026-07-27 to 2026-08-28 | POL-01 drafted from the gaps and the test results |
| 2026-08-31 | Deliverables and POL-01 adopted by the owner-operator |
| 2026-09-30 | Customer A annual security questionnaire due (answered from P03 and P09) |
| 2027-02 (planned) | Follow-up check: operating effectiveness of the controls POL-01 introduced, after at least one quarter of operation |

## 7. Facts added while building the deliverables
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| Customer B remote tool | During P07 testing on 2026-07-23 the owner found that the Customer B remote-desktop client on the laptop also stored the password, so anyone using the laptop's admin session could connect without typing it. The owner removed the saved password that day and emailed Customer B's operations manager on 2026-07-24 asking for named accounts and MFA (EV-IA-5, EV-032) | P01, P04, P07, P08 |
| AI chatbot use | Between April and July 2026 the owner pasted well names and daily production numbers for Customers A and C into a free generative AI chatbot to draft monthly service summaries (about 12 times) (EV-025). Use stopped 2026-07-24 | P01, P10 |
| Dynamometer service terms | The service's standard terms allow it to use uploaded data to improve its models; a paid tier offers a no-training option. Customer A never gave written consent for the uploads (MSA-A (5)) (EV-023, EV-024) | P03, P10 |
| Customer A program changes | In the 12 months before the assessment the owner made 23 logic or setpoint changes for Customer A; 4 had email approval, the rest were approved by phone (EV-030, EV-CM-3) | P03, P07 |
| Laptop software | The PLC and flow meter configuration software is licensed per device. Moving it to a replacement laptop takes the IT technician about one working day, including license transfer (EV-028) | P05, P08 |
| Productivity suite assurance | The productivity suite provider publishes a SOC 2 Type 2 report (Security, Availability, Confidentiality) on its trust portal for business customers. The owner downloaded and reviewed it on 2026-07-22 (EV-031) | P02, P09 |
| AI chatbot clean-up | On 2026-07-24 the owner turned off chat history in the chatbot account and deleted the earlier chats | P10 |
| Field device sample | During routine Customer A and B site visits on 2026-07-21 and 2026-07-23, the owner viewed (did not change) the settings of 6 customer field devices, with each customer's permission, to check for default passwords (EV-IA-5) | P07 |
| Cyber coverage quote | The insurance agent's estimate for cyber liability coverage of $1 million is about $1,300 a year (EV-027) | P01, P03 |
