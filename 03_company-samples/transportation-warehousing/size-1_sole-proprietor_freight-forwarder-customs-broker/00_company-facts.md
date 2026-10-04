# Scenario facts: Cris Santos Company | Transportation and Warehousing | Sole Proprietorship

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Regulatory facts were checked against eCFR (point in time 2026-09-23), the Federal Register, and the Florida Statutes on 2026-10-04.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship; the owner, an individually licensed customs broker, files Schedule C) |
| Business | Freight forwarder and customs broker (NAICS 488510 Freight Transportation Arrangement). Arranges ocean import and export shipments for small importers and exporters, files import entries and Importer Security Filings with U.S. Customs and Border Protection (CBP), and files Electronic Export Information (EEI) as the exporter's authorized agent |
| Licenses | Individual customs broker license and a national permit (19 CFR 111.2, 111.19); the home office is the broker's office of record. Licensed by the Federal Maritime Commission as an ocean freight forwarder (46 CFR 515.3), with the required $50,000 financial responsibility (46 CFR 515.21(a)(1)) |
| Location | Florida. A home office in a spare room of the owner's house, in a Florida port city. No warehouse, no trucks, and no cargo facility. Carriers, terminals, and warehouses are third parties |
| Workforce | The owner only (0 employees). Uses contracted services instead of staff. No one else transacts customs business |
| Clients | About 40 active clients: 32 importers and 8 exporters, mostly small businesses. Six importers are individuals (sole proprietors) whose importer of record number is their Social Security number (19 CFR 24.5(b)(1)(ii)) |
| Volume | About 600 import entries, 600 Importer Security Filings, and 250 export shipments a year. About 3,400 shipment files since the business started in 2019 |
| Revenue | About $180,000 a year (fictional): brokerage fees of about $90,000 and forwarding margins of about $90,000. SBA-small (standard $20.0 million for NAICS 488510; 13 CFR 121.201) |
| Money handled for clients | About two-thirds of importers pay duties through their own accounts on CBP's periodic monthly statement. For the rest, the owner collects duties in advance and pays CBP from the business bank account. The owner pays ocean carriers and overseas agents by wire and invoices clients. About $1.4 million of client and carrier money passes through the business account each year |
| Payment cards | None. Clients pay by bank transfer or check |
| Primary regulation for P03 | 19 CFR Part 111 (customs brokers), Subparts A, C and F, with the 19 CFR Part 163 storage standards that 111.21(c) and 111.23(a) bring in. Modernization rule 87 FR 63267 (2022-10-18), effective 2022-12-19; continuing education rule 88 FR 41224 (2023-06-23), effective 2023-07-24 |
| Not in scope (reasons in P03) | USCG maritime cyber rule, 33 CFR Part 101 Subpart F (N48-49-R01): no vessel or facility security plan. TSA rail, pipeline, and aviation directives (N48-49-R02 to R04). TSA indirect air carrier rules, 49 CFR Part 1548: the business handles ocean freight only and arranges no air transportation of property. CMMC and FAR clauses (N48-49-R07): no federal contracts. SEC rules (N48-49-R08): not a public company. CTPAT (N48-49-R05): voluntary; the owner is not a partner, but three CTPAT importer clients send yearly business partner security questionnaires (see P09) |
| State law approach | Florida law is cited only where a Florida duty is unavoidable: Fla. Stat. 501.171 (reasonable security, disposal of customer records, and breach notice for the six individual importers' Social Security numbers). Clients outside Florida are handled under the law of each state where affected individuals reside |
| Regulatory driver labels | The vertical requirement list (N48-49-R01 to R08) has no entry for the customs broker rules, so driver columns cite 19 CFR Part 111 and Part 163 sections directly. N48-49-R05 is cited where a CTPAT client questionnaire drives a control. N48-49-R01 is cited only where its non-applicability is recorded |

## 2. People and contracted services (role titles only)
| Role | Duties |
|---|---|
| Owner (licensed customs broker) | Every role: owner, security officer, risk acceptor, incident lead, the person responsible for brokerage-wide recordkeeping (19 CFR 111.21(d)), and CBP's point of contact (111.3(b)). Exercises responsible supervision and control over all customs business (111.28(a)). Qualifying individual for the FMC license |
| Contract bookkeeper | Monthly reconciliation in the accounting SaaS. **Signs in with the owner's credentials** (no own account). The previous bookkeeper, replaced in 2025, also knew that password. Does no customs business |
| On-call IT consultant | Hourly help with the laptop, printer, and home network. No standing access. Remote sessions are started by the owner |
| Customs counsel (attorney) | Called as needed for customs and breach questions |
| Backup licensed broker (not arranged) | None today. A nearby broker has agreed in principle to cover urgent entries, but no written agreement or standby powers of attorney exist |
| Key vendors | Customs and forwarding software vendor (SaaS); email and file suite provider; accounting SaaS provider; the business bank; ocean carriers and overseas agents (correspondents) |

## 3. Systems
| ID | System | Hosting | Holds client records? | Notes |
|---|---|---|---|---|
| SYS-01 | Customs and forwarding software: entry, ISF, and EEI preparation and transmission to CBP; client, power of attorney (POA), and shipment files; document storage per shipment | Vendor SaaS | Yes (system of record, including importer of record numbers) | MFA with an authenticator app, enforced by the vendor since 2025. Vendor states U.S. hosting in its contract. SOC 2 Type 2 report available under NDA |
| SYS-02 | Business email and file suite (custom domain): email, calendar, cloud files synced to the laptop, including the scanned records archive | SaaS (business plan) | Yes | MFA by text message on web sign-in. **An app password created in 2023 for the phone's built-in mail app still works and bypasses MFA.** 30-day file version history (vendor default). Data storage region not confirmed |
| SYS-03 | Accounting SaaS: client invoices, ledgers, bank feed | SaaS | Yes (client names, amounts, bank details) | MFA available but **off**. Bookkeeper uses the owner's login |
| SYS-04 | Business online banking: ACH payments to CBP and wires to carriers and agents | Bank portal | Yes (payment details) | Bank-enforced MFA (text code and device registration). One user. No call-back step for changed payment instructions |
| SYS-05 | CBP portals: the ACE trade portal account and the eCBP portal for broker submissions (status report, permit fee, point of contact) | Government-operated | Yes | Outside the boundary; the owner protects the credentials |
| SYS-06 | Laptop (2024) and multifunction printer-scanner | Owner devices | Yes (synced files, downloads, scans) | Full-disk encryption on by default; built-in antivirus; automatic updates. **The previous laptop (2019) sits in a closet, not wiped** |
| SYS-07 | Mobile phone | Personal device used for business | Yes (email, chats, photos of documents) | Email app, a consumer messaging app used with overseas agents and some clients, the authenticator app, and text-message codes |
| SYS-08 | Home network | ISP-provided router and Wi-Fi | Yes (in transit) | Shared with household devices (a game console, smart TV, and family phones). WPA2 Wi-Fi |
| SYS-09 | Consumer generative AI assistant (free personal account, web) | Vendor SaaS | Yes (pasted invoice lines and some whole invoices) | Used since 2026-03 for tariff classification research and drafting client emails. Settings allow use of chats for model training. See P10 |
| SYS-10 | Paper records | Locked file cabinet in the home office | Yes | Wet-signed POAs and paper documents from couriers. Since 2024, paper is scanned into SYS-02 and shredded |

**SSP system (P02):** the *Core Brokerage SaaS Stack*: SYS-01 to SYS-04 (the SaaS and banking accounts), the devices and home network that reach them (SYS-06 to SYS-08), and the paper records (SYS-10), with interconnections to the CBP portals (SYS-05) and the AI assistant (SYS-09).

**Registry defaults adapted (and why):** the primary system "Core business SaaS stack (email, files, client and billing records)" is kept and named the Core Brokerage SaaS Stack. The default incident "Ransomware disrupting terminal operating system" becomes ransomware on the owner's laptop that encrypts the synced records archive and steals client files, because a sole proprietor runs no terminal operating system; the customs SaaS takes the place of the TOS as the system the business cannot work without. The default AI use case "Container and berth scheduling optimization" is replaced by a consumer AI assistant used for tariff classification research, because a forwarder schedules no berths or containers; classification is where this business uses AI and where an error costs clients money.

## 4. Current security posture: early (few formal controls)
**In place today:**
- MFA on the customs software (authenticator app, vendor-enforced) and on the bank portal (bank-enforced)
- A business email plan with a custom domain, and MFA by text message on web sign-in
- Full-disk encryption on the 2024 laptop and a passcode on the phone
- Automatic operating system updates and built-in antivirus on the laptop
- Vendor backups of the customs software (stated in its SOC 2 report) and 30-day version history on cloud files
- A locked file cabinet and a cross-cut shredder in the home office
- The CBP point of contact and addresses kept current in the eCBP portal

**Missing:**
1. No written security policy, risk assessment, or incident plan.
2. No procedure for the 72-hour breach notice to the CBP Security Operations Center (19 CFR 111.21(b)), and no list of where importer of record numbers are stored.
3. Email MFA uses text messages only, and an old app password on the phone bypasses MFA.
4. No call-back verification when a carrier, agent, or client asks to change bank details; wires are sent on an emailed request.
5. The bookkeeper signs in to the accounting SaaS with the owner's credentials; MFA is off there.
6. Passwords are reused across some accounts; no password manager.
7. The home network is shared with household devices.
8. Paper originals have been shredded after scanning since 2024 without the advance notice of an alternative storage method to CBP Regulatory Audit (19 CFR 163.5(b)(1)), and without written procedures, a yearly test, or a separate backup copy (163.5(b)(2)).
9. No backup of the cloud files independent of the sync; ransomware on the laptop would sync encrypted files, leaving only the 30-day version history.
10. Client terms and POAs do not give written authorization to share client records with service providers (cloud vendors, bookkeeper, IT consultant), which 19 CFR 111.24 makes the exception for disclosure; confirmation with counsel pending.
11. Documents are exchanged with overseas agents and clients through a consumer messaging app; copies stay in the phone's chats and camera roll and are not filed in the shipment file.
12. The consumer AI assistant receives client invoice data with training allowed (P10).
13. Single-person dependency: no backup broker agreement, MFA on one phone, and no stored recovery codes.
14. No security training beyond customs continuing education.
15. The 2019 laptop has not been wiped.
16. Continuing broker education: 22 of the 36 credits needed for the triennial period ending 2027-01-31 are complete (19 CFR 111.102(b)).

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 primary regulation | 19 CFR Part 111 duties (Subparts A, C, and F) and the 19 CFR 163.5 storage standards, with secondary rows for 46 CFR 515.33, 15 CFR 30.10, and Fla. Stat. 501.171. Applicability rows record why the USCG cyber rule, the TSA indirect air carrier rule, and CTPAT do not bind the business |
| P08 incident | Ransomware on the owner's laptop that encrypts the synced records archive and steals client files (adapted from the registry default; see section 3). The customs SaaS is not encrypted, but saved browser sessions put it and the bank at risk |
| P09 SOC 2 | Security criteria only. The owner's self-check, used to answer CTPAT importer clients' business partner security questionnaires, plus a review of the customs software vendor's SOC 2 Type 2 report. A SOC 2 report for the business is not sought |
| P10 AI | The consumer AI assistant used for tariff classification research (AI-001). The customs software's document capture feature is listed as AI-002 |
| Cloud | SaaS only. No IaaS or PaaS |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2022-12-19 | Customs broker modernization rule effective (87 FR 63267), including the 72-hour breach notice in 111.21(b) |
| 2026-08-17 to 2026-08-21 | Self-assessment with the on-call IT consultant (P05, P02, P04, P01, P03); P07 tests on 2026-08-20 |
| 2026-08-25 to 2026-08-28 | Customs software vendor SOC 2 review, AI use assessment, and SOC 2 readiness self-check |
| 2026-09-14 | Deliverables adopted by the owner |
| 2027-01-31 | End of the triennial period for continuing broker education (36 credits; 111.102(b)) |
| 2027-02-01 | Triennial status report due with the continuing education certification (111.30(d); 111.101). License suspended by operation of law if not filed by 2027-03-01 (111.30(d)(4)) |
