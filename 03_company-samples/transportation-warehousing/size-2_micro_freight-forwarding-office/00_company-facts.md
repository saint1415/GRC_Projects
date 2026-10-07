# Scenario facts: Cris Santos Company | Transportation and Warehousing | Micro

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Regulatory facts were checked against eCFR (point in time 2026-09-23), the Federal Register, and the Florida Statutes on 2026-10-04.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (privately held by Cris Santos; holds an organizational customs broker license and a national permit) |
| Business | Freight forwarding and customs brokerage office (NAICS 488510 Freight Transportation Arrangement). Arranges ocean import and export shipments for small and mid-size importers and exporters, files import entries and Importer Security Filings (ISF) with U.S. Customs and Border Protection (CBP) through the Automated Broker Interface, and files Electronic Export Information (EEI) as the exporter's authorized agent |
| Licenses | The LLC holds a customs broker license under the organization requirements of 19 CFR 111.11(c): its articles of organization empower it to transact customs business, and its qualifying officer (the owner) is an individually licensed broker. National permit under 111.19, with the Florida office as the broker's office of record. Licensed by the Federal Maritime Commission as an ocean freight forwarder (46 CFR 515.3), with the required $50,000 financial responsibility (46 CFR 515.21(a)(1)). Not an NVOCC |
| Location | Florida. One leased office suite of about 1,800 square feet near a Florida seaport. No warehouse, trucks, or cargo-handling facility. Carriers, terminals, warehouses, and truckers are third parties |
| Workforce | 7 employees: the Owner and President (licensed customs broker), the Office and Compliance Manager, a second Licensed Customs Broker (Entry Supervisor), 2 Entry Writers, 1 Export and Forwarding Coordinator, 1 Accounting Specialist |
| Clients | About 180 active clients: about 150 importers and 30 exporters. About 25 importers are individuals (sole proprietors) whose importer of record number is their Social Security number (19 CFR 24.5(b)(1)(ii)). Six importer clients are CTPAT partners |
| Volume | About 4,500 import entries, 4,000 ISFs, and 1,200 export shipments a year. About 22,000 shipment files since the business started in 2012 |
| Revenue | About $1.1 million a year (fictional): brokerage fees of about $650,000 and forwarding margins of about $450,000. About $4,400 per business day. SBA-small (standard $20.0 million for NAICS 488510; 13 CFR 121.201) |
| Money handled for clients | About 60% of entries are paid on the importer's own periodic monthly statement. For the rest, the company collects duties in advance and pays CBP from its operating account. Ocean carriers and overseas agents are paid by wire. About $9 million of client and carrier money passes through the business account each year |
| Payment cards | None. Clients pay by bank transfer or check |
| Primary regulation for P03 | 19 CFR Part 111 (customs brokers), Subparts A, C, and F, with the 19 CFR 163.5 storage standards that 111.21(c) and 111.23(a) bring in. Modernization rule 87 FR 63267 (2022-10-18), effective 2022-12-19; continuing education rule 88 FR 41224 (2023-06-23), effective 2023-07-24 |
| Not in scope (reasons in P03) | USCG maritime cyber rule, 33 CFR Part 101 Subpart F (N48-49-R01): the company has no vessel or facility security plan under 33 CFR Parts 104 to 106. TSA rail, pipeline, and aviation directives (N48-49-R02 to R04). TSA indirect air carrier rules, 49 CFR Part 1548: the company arranges ocean freight only and does not tender cargo for air transportation. CMMC and FAR clauses (N48-49-R07): no federal contracts. SEC rules (N48-49-R08): privately held. CTPAT (N48-49-R05): voluntary; the company is not a partner, but its six CTPAT importer clients send yearly business partner security questionnaires (see P09) |
| Inland trucking | Booked through a separate licensed freight broker partner. The company holds no motor carrier or property broker authority |
| State law approach | Florida law is cited only where a Florida duty is unavoidable: Fla. Stat. 501.171 (reasonable security, disposal of customer records, and breach notice for individual importers' Social Security numbers and employee data). Clients and employees outside Florida are handled under the law of each state where affected individuals reside |
| Regulatory driver labels | The vertical requirement list (N48-49-R01 to R08) has no entry for the customs broker rules, so `regulatory_driver` columns cite 19 CFR Part 111 and Part 163 sections directly. N48-49-R05 is cited where a CTPAT client questionnaire drives a control. N48-49-R01 is cited only where its non-applicability is recorded |

## 2. People (role titles only)
| Role | Security and compliance duties |
|---|---|
| Owner and President (licensed customs broker) | Qualifying officer for the license (111.11(c)(2)) and national permit qualifier (111.19). Exercises responsible supervision and control (111.28(a)). Accepts Moderate and higher risk; approves policies and spending. CBP point of contact (111.3(b)) |
| Office and Compliance Manager | **Security Coordinator** (designated in writing on 2026-08-31) and the knowledgeable employee responsible for brokerage-wide recordkeeping (111.21(d)). Runs onboarding and terminations, the CBP employee list updates (111.28(b)), and the MSP relationship. Not a licensed broker |
| Licensed Customs Broker (Entry Supervisor) | Second individually licensed broker. Reviews entries prepared by the Entry Writers; backup CBP point of contact after hours; business owner of the AI classification feature (P10) |
| Entry Writers (2) | Prepare entries and ISFs in the customs platform under a signing power of attorney from the company (111.2(a)(2)(ii)(A)) |
| Export and Forwarding Coordinator | Ocean bookings with carriers, overseas agent coordination, EEI filing |
| Accounting Specialist | Client invoicing, duty payments to CBP, wires to carriers and overseas agents, accounting SaaS |
| Managed service provider (MSP) | Help desk, patching, antivirus, firewall, productivity suite administration, and the suite backup. Contract: 4-business-hour response; no recovery time commitment |
| Customs platform vendor | Licenses and hosts the customs brokerage and forwarding platform (SaaS) |
| Cyber insurer | Cyber liability policy with a 24x7 breach hotline, panel breach counsel and forensics, and a social engineering (funds transfer fraud) sublimit of $100,000 |
| Customs counsel | Outside attorney, called as needed for CBP and breach questions |

**Role overlap and how it is compensated.** The Office and Compliance Manager sets up accounts, runs the security program, and checks it. The independent consultant who performs the P07 assessment and the MSP's monthly reports are the outside check. The owner both supervises customs business and accepts risk; the second licensed broker reviews the owner's own entries monthly.

## 3. Systems
| ID | System | Hosting | Holds client records? | Notes |
|---|---|---|---|---|
| SYS-01 | Customs brokerage and forwarding platform: entry, ISF, and EEI preparation and transmission to CBP; client, power of attorney (POA), and shipment files; document imaging per shipment; AI document capture and tariff classification suggestions (since 2026-04) | Vendor SaaS | Yes (system of record, including importer of record numbers) | MFA with an authenticator app, enforced by the vendor since 2025. U.S. hosting stated in the contract. SOC 2 Type 2 report available under NDA |
| SYS-02 | Business productivity suite (email, calendar, chat, cloud files): shared drive with the scanned Client Records Archive (POAs, CBP Form 5106 copies, commercial invoices, client correspondence) | SaaS (business plan) | Yes | MFA enforced for named users with push approval. **The "entries@" mailbox is a licensed user account whose password is shared by the Entry Writers, the Entry Supervisor, and the scan-to-email function of the printer; MFA is excluded for it.** Audit log retention at the plan default (under one year). Data storage region not confirmed |
| SYS-03 | Accounting SaaS: invoices, ledgers, accounts payable, bank feed | SaaS | Yes (client names, amounts, bank details) | MFA on for both users (Accounting Specialist and owner) |
| SYS-04 | Business online banking: ACH payments and wires to ocean carriers and overseas agents | Bank portal | Yes (payment details) | Bank-enforced MFA. The Accounting Specialist creates and releases wires up to $25,000 alone; the owner approves above that. **No call-back step for changed payment instructions** |
| SYS-05 | CBP portals: ACE portal accounts (owner, Entry Supervisor, Office and Compliance Manager) and the eCBP portal for broker submissions | Government-operated | Yes | Outside the boundary; the company protects the credentials |
| SYS-06 | Endpoints: 6 desktops and 3 laptops (owner, Entry Supervisor, Office and Compliance Manager), 1 multifunction printer-scanner. Staff use personal phones for MFA and email | Company-owned (computers); personal (phones) | Yes (synced files, downloads, scans) | MSP-managed: patching, antivirus, full-disk encryption on all 9 computers. No mobile device management. Printer stores the entries@ password for scan-to-email |
| SYS-07 | Office network: small-business firewall, staff and guest Wi-Fi, one internet line | On-premises, MSP-managed | In transit | Guest Wi-Fi separated; no failover line |
| SYS-08 | Cloud backup of the productivity suite (email and shared drive) | SaaS (third-party backup service, resold and operated by the MSP) | Yes | Daily, 1-year retention. **Never restore-tested; administered with one shared MSP login without MFA** |
| SYS-09 | Ocean carrier booking portals and terminal container-status portals (external web accounts) | Carrier and terminal SaaS | Shipment data | **One shared login per carrier, used by 4 staff; passwords kept in a spreadsheet** |
| SYS-10 | Paper records | Locked file cabinets in the office | Yes | Wet-signed POAs and courier documents. Since 2023, paper is scanned into SYS-02 and shredded |

**SSP system (P02):** the *Core Brokerage SaaS Stack*: SYS-01 to SYS-04 (customs platform, productivity suite, accounting, banking), the endpoints and office network that reach them (SYS-06, SYS-07), the suite backup (SYS-08), and paper records (SYS-10), with interconnections to the CBP portals (SYS-05) and the carrier and terminal portals (SYS-09).

**Registry defaults adapted (and why):**
- The primary system "Core business SaaS stack (email, files, client and billing records)" is kept and named the Core Brokerage SaaS Stack.
- The default incident "Ransomware disrupting terminal operating system" is replaced by **business email compromise (BEC) with payment diversion and client record exposure**. A forwarding office runs no terminal operating system. Its most likely serious incident, and its top risk in P01, is a compromised mailbox used to change a carrier's or agent's bank details while the attacker reads client files containing importer identification numbers. That event triggers the 72-hour CBP notice in 19 CFR 111.21(b).
- The default AI use case "Container and berth scheduling optimization" is replaced by the **AI document capture and tariff classification suggestions in the customs platform** (AI-001). The office schedules no berths or containers; classification is where it uses AI and where an error costs clients money and tests the broker's supervision duty (111.28).

## 4. Current security posture: early to partial
**In place today:**
- MFA on the customs platform (vendor-enforced), the productivity suite for named users, the accounting SaaS, and the bank portal
- MSP patching, antivirus, firewall, and full-disk encryption on all 9 computers
- Daily suite backup with 1-year retention (SYS-08)
- Customs platform backups by the vendor (stated in its SOC 2 report)
- Guest Wi-Fi separated from staff devices
- Locked file cabinets and a locked shred bin collected by a shredding service
- CBP point of contact, office of record, and recordkeeping contact current in the eCBP portal
- A 2019 customs procedures manual (entry preparation steps; no security content)

**Missing:**
1. No written security policies, risk assessment, or incident response plan. The only prior document is the MSP's 2018 onboarding checklist.
2. No procedure for the 72-hour breach notice to the CBP Security Operations Center (19 CFR 111.21(b)), and no inventory of where importer identification numbers are stored.
3. The shared "entries@" account has a shared password and no MFA, and the printer stores that password.
4. No call-back verification when a carrier, agent, or client asks to change bank details; one person can create and release wires up to $25,000.
5. Shared logins on ocean carrier and terminal portals, with passwords in a spreadsheet.
6. Terminations are informal. An Entry Writer who left on 2026-03-13 kept customs platform access for 19 days, and her name reached CBP's employee list on day 41, past the 30-day limit in 111.28(b)(3).
7. Paper originals have been shredded after scanning since 2023 without the 30-day advance notice to CBP Regulatory Audit (19 CFR 163.5(b)(1)), written procedures, or a yearly test (163.5(b)(2)(i), (iv)).
8. The suite backup has never been restore-tested, and its administrator login is shared by MSP technicians without MFA.
9. Client terms and POAs do not authorize, in writing, disclosure of client records to service providers (the MSP, SaaS vendors, the AI feature), which 111.24 makes the exception for disclosure. Counsel review pending.
10. No security awareness or phishing training; staff training is customs continuing education only.
11. The customs platform's AI classification suggestions were switched on by the vendor in 2026-04, and Entry Writers accept them with no recorded broker review. Some staff paste invoice text into public chatbots. No AI rules.
12. No review of audit logs or sign-in alerts; suite audit logs kept only for the plan default.
13. Overseas agents send documents through a consumer messaging app on personal phones; copies are not filed in the shipment file.
14. No vulnerability scanning.
15. Continuing broker education for the triennial period ending 2027-01-31 (36 credits, 111.102(b)): the owner has 30 credits and the Entry Supervisor has 18.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 primary regulation | 19 CFR Part 111 duties (Subparts A, C, and F) and the 19 CFR 163.5 storage standards, with secondary rows for 46 CFR 515.33, 15 CFR 30.10, and Fla. Stat. 501.171. Applicability rows record why the USCG cyber rule, the TSA indirect air carrier rule, and CTPAT do not bind the company |
| P08 incident | Business email compromise with payment diversion and client record exposure (adapted from the registry default; see section 3). The MSP, the bank, and the cyber insurer are in the notification chain |
| P09 SOC 2 | Security plus Confidentiality. The readiness check is used to answer the CTPAT importer clients' business partner security questionnaires (the largest is due 2026-10-31); plus a review of the customs platform vendor's SOC 2 Type 2 report |
| P10 AI | AI-001: AI document capture and tariff classification suggestions in the customs platform. The inventory also lists public chatbots (AI-002) and the suite's built-in generative AI assistant (AI-003, not licensed) |
| Cloud | SaaS plus one cloud workload: the SaaS-to-SaaS backup of the productivity suite (SYS-08), operated by the MSP. Vendor-agnostic |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2022-12-19 | Customs broker modernization rule effective (87 FR 63267), including the 72-hour breach notice in 111.21(b) |
| 2026-07-20 to 2026-07-31 | BIA, risk assessment, and gap analysis with the MSP lead technician (P05, P02, P04, P01, P03) |
| 2026-08-10 to 2026-08-12 | Control assessment by an independent consultant (on site 2026-08-11) |
| 2026-08-24 to 2026-08-27 | Customs platform vendor SOC 2 review, AI risk assessment, and SOC 2 readiness self-assessment |
| 2026-08-31 | Deliverables approved by the owner |
| 2026-10-31 | Largest CTPAT client's business partner security questionnaire due |
| 2027-01-31 | End of the triennial period for continuing broker education (36 credits; 111.102(b)) |
| 2027-02-01 | Triennial status report due, with the first continuing education certification (111.30(d); 111.101). License suspended by operation of law if not filed by 2027-03-01 (111.30(d)(4)) |

## 7. Facts added while building the deliverables
| Topic | Added fact | Used in |
|---|---|---|
| Former Entry Writer | Left 2026-03-13. Customs platform account disabled 2026-04-01 (19 days later). Her suite account was disabled on her last day. Her name was sent to CBP on 2026-04-23 (day 41). Her ACE portal account was never created. Platform sign-in logs showed no use after her last day | P01, P03, P07 |
| Printer | P07 testing on 2026-08-11 found the printer's web administration page still used the manufacturer's default password. Changed by the MSP on 2026-08-14 | P01, P07 |
| Payment near-miss | In 2026-05 an email that appeared to come from an overseas agent asked to change bank details. The Accounting Specialist noticed a one-letter difference in the sender domain and did not pay. No record was made | P01, P08 |
| Office security | Keyed suite entry with an after-hours alarm; keys held by the owner and the Office and Compliance Manager; network equipment in a locked closet | P02, P03 |
| Finances | A cash reserve covers about 45 days of expenses. Payroll runs biweekly through an outside payroll service | P01, P05 |
| Retired equipment | Two desktops replaced in 2025 were taken by the MSP; no wipe or destruction record exists | P03, P07 |
| Assessor | The P07 assessor is an independent information security consultant, not involved in the risk or gap analysis and operating no control | P07 |
| AI feature (AI-001) | Pre-fills a 10-digit tariff number per line with a confidence label and a generated rationale, drawing first on the company's own product library. The platform logs which user accepted each suggestion; a setting can hold lines without a product-library match for a broker-role user; the automatic-acceptance setting is off. Model provider, processing location, and training use not disclosed by the vendor. Test on 2026-08-25 of 40 AI-assisted lines: repeat products 20 of 20 correct, new products 13 of 20; 6 wrong numbers filed, 4 with a different duty rate; capture errors in 5 of 40 lines; new-product error rate 20% on English invoices and 50% on other languages | P10 |
| CTPAT questionnaire | The largest CTPAT importer client (about 12% of revenue) sent its yearly business partner security questionnaire in 2026-07, with cybersecurity questions; response due 2026-10-31 | P09 |
