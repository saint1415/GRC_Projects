# Scenario facts: Cris Santos Company | Transportation Systems | Sole Proprietorship

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Regulatory facts were checked against eCFR (point in time 2026-09-23), the Federal Register, the U.S. Code (govinfo.gov), and the Florida Statutes on 2026-10-05.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship; the owner files Schedule C and holds the FMCSA property broker registration in the business name) |
| Business | Freight broker arranging truck and rail shipments (NAICS 488510 Freight Transportation Arrangement). **Truck:** arranges full-truckload dry van and flatbed moves with FMCSA-authorized motor carriers under the business's own broker authority. **Rail:** arranges carload moves (boxcars, covered hoppers, centerbeam flatcars) and the truck legs to and from transload sites for 4 shippers, acting as the shipper's agent in the railroads' online customer portals. The shipper keeps its own rail contract or uses the railroad's public prices; the broker never takes custody of freight or rail cars |
| Why a broker, not a railroad | A sole proprietor cannot operate a railroad. The registry's vertical is the freight railroad sector; at this size the business sits at the edge of that sector as a customer-side agent using railroad systems |
| Registrations | FMCSA property broker registration (MC and USDOT numbers) since 2021 (49 U.S.C. 13901, 13904). $75,000 surety bond filed on Form BMC-84 (49 CFR 387.307(a)). Process agents designated through a blanket company on Form BOC-3 (49 CFR 366.2T, 366.4T(b)). Unified Carrier Registration paid for 2026 |
| Location | Florida. A home office in a spare room of the owner's house in northeast Florida. No warehouse, no trucks, no rail cars |
| Workforce | The owner only (0 employees). Uses contracted services instead of staff |
| Shippers (customers) | 14 active business shippers (building products, paper, packaged food, plastic resin). 4 of them also use the rail service. No individual or household goods shippers |
| Carriers | 214 motor carriers onboarded since 2021; 88 used in the last 12 months. 37 are owner-operators who gave a W-9 with a Social Security number instead of an employer identification number. 19 carrier packets also hold a copy of a driver's commercial driver's license |
| Volume | About 1,100 truckloads and 260 rail carloads a year; 6 to 10 truckloads in transit on a normal weekday |
| Revenue | About $180,000 a year (fictional): truckload margin of about $154,000 and rail coordination fees of about $26,000. About $1.35 million of truckload freight is billed to shippers and about $1.17 million paid to carriers. SBA-small (standard $20.0 million for NAICS 488510; 13 CFR 121.201, footnote 10) |
| Money handled | Carriers are paid by ACH from the business bank account on 30-day terms. No quick pay, fuel advances, or carrier financing. Shippers pay by ACH or check. No payment cards |
| Hazardous materials | None. The owner declines hazmat loads: the contingent cargo policy excludes them and the business has no hazmat process. So the hazmat security plan rule (49 CFR 172.800) does not reach it |
| TSA and FRA status | **Not covered.** Part 1580 reaches freight railroad carriers, rail hazmat shippers and receivers, host railroads, and private rail car owners (49 CFR 1580.1(a)). A broker is none of these, so the Security Coordinator and reporting duties (1570.201, 1570.203), the RSSM rules, and the TSA rail cyber directives (railroads in 1580.101 or designated by TSA) do not apply. Not an SSI covered person (1520.7) unless TSA or a covered person gives it SSI. Not a railroad, so FRA railroad safety rules do not apply |
| Not in scope | Household goods brokerage (49 CFR 371 Subpart B); payment cards; federal contracts (no FAR clauses); SEC disclosure (private); CIRCIA and the TSA surface cyber NPRM (proposed only; neither would cover this business as proposed, see P03) |
| State law approach | Florida law is cited only where a Florida duty is unavoidable: Fla. Stat. 501.171 (reasonable security, disposal, and breach notice) for carrier and driver personal information (owner-operator Social Security numbers, driver license numbers, and driver location data from load tracking). Carriers and drivers live in many states, so notices follow the law of each state where affected individuals reside, with Florida as the worked example |

**Regulatory driver IDs used in this folder.** The vertical's `requirements.csv` lists C-TRANSPORTATION-R01 to R07. None binds a freight broker: R01 (TSA rail cyber directives) is cited only where its non-applicability is recorded; R02 to R05 (pipeline, aviation, maritime) do not apply; R06 (TSA surface cyber NPRM) and R07 (CIRCIA) are proposed and tracked only. The rules that do bind are not in the registry, so this folder adds **scenario-level driver IDs**, defined here and nowhere else. S07 keeps the meaning it has in the Small sample (Florida breach law); S09 and S10 are new.

| ID | Requirement | Citation | Status for this business |
|---|---|---|---|
| C-TRANSPORTATION-S07 | Florida security of confidential personal information | Fla. Stat. 501.171 (2), (3)-(6), (8) | Applies (covered entity holding personal information) |
| C-TRANSPORTATION-S09 | FMCSA broker registration and financial security | 49 U.S.C. 13901, 13904; 49 CFR 387.307; 49 CFR part 366 | Applies |
| C-TRANSPORTATION-S10 | FMCSA brokers of property: records and conduct | 49 CFR part 371 Subpart A (371.3, 371.7, 371.13) | Applies |
| C-TRANSPORTATION-CT | Customer and railroad contract terms (flow-down) | Master broker-shipper agreement with the largest shipper; railroad customer portal terms of use | Applies by contract, not by regulation |

## 2. People and contracted services (role titles only)
| Role | Duties |
|---|---|
| Owner | Every role: owner, the officer with the experience 49 U.S.C. 13904(c) requires (9 years in carrier sales and operations at a larger brokerage before 2021), security lead, risk acceptor, incident lead, and the only person who books loads, pays carriers, and answers FMCSA, surety, and shipper notices |
| Contract bookkeeper | Monthly reconciliation in the accounting SaaS through the bookkeeper's own login (view and reconcile only; cannot send payments). Engagement letter has a confidentiality clause |
| On-call IT consultant | Hourly help with the laptop, email setup, and home network. Set up the email suite in 2021. No standing access |
| Transportation attorney | Contract templates, claims, and breach questions as needed |
| Insurance agent | Contingent cargo ($100,000 per load), contingent auto liability, and general liability. **No cyber or social engineering fraud coverage** |
| Backup broker (not arranged) | None. A former colleague at another brokerage agreed informally to watch in-transit loads in an emergency; nothing is written |
| Key vendors | TMS vendor; email and file suite provider; accounting SaaS provider; business bank; load board and carrier monitoring service providers; shipment tracking app provider; surety company; blanket process agent company |

## 3. Systems
| ID | System | Hosting | Holds personal or confidential data? | Notes |
|---|---|---|---|---|
| SYS-01 | Broker transportation management system (TMS): shippers, carrier file, loads, rate confirmations, bills of lading (BOLs) and proof of delivery (POD) images, invoices, carrier payables. Includes a document capture feature (AI-001) | Vendor SaaS | Yes (system of record for 49 CFR 371.3 transaction records; carrier W-9s and bank details) | MFA available (authenticator app) but **off**. Vendor holds a SOC 2 Type 2 report |
| SYS-02 | Business email and file suite (custom domain): email, calendar, cloud files synced to the laptop (carrier packet folders, shipper contracts, rail shipping instructions) | SaaS (business plan) | Yes | MFA by text message for the owner's account. 30-day file version history (vendor default). File sharing allows "anyone with the link" |
| SYS-03 | Accounting SaaS: shipper invoices, receivables, carrier payables ledger, bank feed | SaaS | Yes (bank details; W-9 data for 1099 filing) | MFA available but **off** for the owner and the bookkeeper |
| SYS-04 | Business online banking: ACH payments to carriers | Bank portal | Yes | Bank-enforced MFA (hardware token). One user. Payee-change alerts available but off. No call-back step when a carrier asks to change bank details |
| SYS-05 | Carrier sourcing and monitoring: a load board subscription and a carrier monitoring service (authority and insurance alerts, plus a fraud risk score, AI-002) | Vendor SaaS | Yes (carrier contacts) | Load board account is password only; the monitoring service's identity verification add-on was not bought |
| SYS-06 | Shipment tracking app service: drivers accept a text link that shares their phone location for the length of a load; status flows into the TMS | Vendor SaaS | Yes (driver names, phone numbers, and location) | About 300 distinct drivers tracked a year |
| SYS-07 | Laptop (2023) | Owner device | Yes (synced files, downloads) | Full-disk encryption on; built-in antivirus; automatic updates |
| SYS-08 | Mobile phone and business phone line: personal phone used for business, with a cloud VoIP app for the business number | Personal device; VoIP SaaS | Yes (texts with drivers, email, TMS app, photos of documents) | Receives the email MFA text codes. **No port-out or account PIN** on the mobile carrier account |
| SYS-09 | Home network | ISP router and Wi-Fi | Yes (in transit) | Shared with household devices; the router's guest network is not used |
| SYS-10 | Railroad customer portals (two Class I railroads and one short line): car orders, shipping instructions, car tracing, demurrage | Railroad-operated (external) | Yes (shipper data) | The railroads issued the owner individual third-party user IDs for 3 shippers. For the 4th shipper the owner uses **the shipper's own login**, shared since 2024 |
| SYS-11 | FMCSA registration account and the broker's public registration record | Government-operated (external) | Yes | Account recovery goes to the owner's personal consumer email (password reused, no MFA). The phone number on record is the old mobile number |

**SSP system (P02):** the *Freight Brokerage SaaS Stack*: SYS-01 to SYS-06 (the SaaS and banking accounts) and the devices and home network that reach them (SYS-07 to SYS-09), with interfaces to the railroad portals (SYS-10) and the FMCSA registration account (SYS-11).

**Registry defaults adapted (and why):**
- **Primary system:** "Core business SaaS stack (email, files, client and billing records)" is kept and named the Freight Brokerage SaaS Stack. The TMS takes the place of a railroad's dispatch system.
- **P08 incident:** "Ransomware on dispatch and train control back-office systems" becomes ransomware on the owner's laptop, which is the broker's dispatch and back-office workstation, with theft of carrier packets. A broker runs no train control system.
- **P10 AI use case:** "Track and equipment defect detection (computer vision)" becomes the TMS document capture feature, which uses computer vision to read BOL and POD photos and flag damage or shortage notes. That is the closest thing a broker has to defect detection: finding the exception on the paperwork before paying the carrier and billing the shipper.

## 4. Current security posture: early (few formal controls)
**In place today:**
- Full-disk encryption, built-in antivirus, and automatic updates on the laptop; passcode on the phone
- Business email with a custom domain and text-message MFA on the owner's account
- Bank-enforced MFA (hardware token) for ACH payments
- TMS vendor backups and a SOC 2 Type 2 report; 30-day version history on cloud files
- Carrier monitoring service alerts on carrier authority and insurance changes
- FMCSA broker registration, surety bond, and BOC-3 designation all current
- Separate accounting classes for truck brokerage and rail coordination income (49 CFR 371.13)
- A shredder in the home office

**Missing:**
1. No written security policy, risk assessment, or incident plan.
2. MFA is off on the TMS, the accounting SaaS, and the load board. Email MFA uses text messages only.
3. No call-back verification when a carrier asks by email to change its bank details. A look-alike email in 2026-05 got a carrier's bank details changed in the TMS before the owner caught it.
4. Carrier vetting checks authority and insurance but not identity (does the email domain and phone number match the carrier's registered contact?). One load was double brokered in 2025.
5. One railroad portal login belongs to a shipper's former traffic coordinator and is shared with the owner, against the portal's terms.
6. Carrier packets with Social Security numbers and driver license copies sit in email attachments and cloud folders, some shared by "anyone with the link."
7. No backup of the TMS or cloud files independent of the vendors; the TMS vendor's recovery point (24 hours) does not meet the BIA for in-transit tracking.
8. Single-person dependency: no backup broker agreement, MFA on one phone, no stored recovery codes, and no one else who can answer a surety claim within the 7 business days in 49 CFR 387.307(e).
9. The FMCSA registration account recovers to a personal consumer email with no MFA, and the phone number on the FMCSA record is out of date.
10. No port-out or account PIN on the mobile carrier account that receives the email MFA codes.
11. Home network shared with household devices.
12. No records retention rule: the 3-year record duty (49 CFR 371.3(b)) depends on the TMS subscription, and carrier packets from 2021 have never been disposed of.
13. The carrier agreement template (an industry form bought in 2021) asks carriers to waive their right to review transaction records (49 CFR 371.3(c)).
14. The TMS document capture feature was turned on, with automatic approval of carrier pay on "clean" PODs, without an assessment (P10).
15. No security training beyond a load board fraud webinar.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 regulation | The named primary regulation (TSA SD 1580/82-2022-01E) **does not apply**, directly or through contracts. P03 analyzes the rules that bind a freight broker: FMCSA broker registration and financial security (49 U.S.C. 13901, 13904; 49 CFR 387.307; part 366), broker records and conduct (49 CFR part 371 Subpart A), Fla. Stat. 501.171, and two contract flow-down sources. Applicability rows record why the TSA rail rules, SSI, and the hazmat security plan rule do not bind it |
| P08 incident | Ransomware on the owner's laptop (the dispatch and back-office workstation) with theft of carrier packets; TMS and bank sessions at risk |
| P09 SOC 2 | Security criteria only: the owner's self-check, used to answer the largest shipper's yearly security questionnaire, plus a review of the TMS vendor's SOC 2 Type 2 report. A SOC 2 report for the business is not sought |
| P10 AI | TMS document capture (AI-001), adapted from the registry default as explained in section 3. The carrier monitoring service's fraud risk score is listed as AI-002 |
| Cloud | SaaS only. No IaaS or PaaS |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-01-16 | Amended broker financial security rule (49 CFR 387.307) effective |
| 2026-08-10 to 2026-08-14 | Self-assessment with the on-call IT consultant (P05, P02, P04, P01, P03); P07 tests on 2026-08-13 |
| 2026-08-17 to 2026-08-19 | TMS vendor SOC 2 review, AI use assessment, and SOC 2 readiness self-check |
| 2026-09-08 | Deliverables adopted by the owner |

## 7. Facts added while building the deliverables
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| Revenue per day | About 250 business days a year, so about $720 of margin and about 4 to 5 truckloads booked per business day | P05 |
| Forgotten admin account | The IT consultant created a second super administrator account on the email suite in 2021. It used a password only and was last signed in to in 2022-02. Found in P07 testing on 2026-08-13 and disabled the same day | P01, P02, P04, P07 |
| Open sharing links | The P04 mapping on 2026-08-12 found 14 "anyone with the link" shares in the file suite; 9 were carrier packet folders. The owner switched all 14 to named-recipient sharing on 2026-08-12 | P01, P03, P04, P07 |
| Payment change near miss | On 2026-05-19 an email from a look-alike domain asked to change a regular carrier's bank details. The owner changed them in the TMS, then noticed the domain before the weekly ACH batch and reversed the change. No loss | P01, P03, P07 |
| Shared rail portal login | The 4th rail shipper's traffic coordinator gave the owner that coordinator's portal login in 2024. The coordinator left the shipper in 2026-05 and the password has not been changed | P01, P03, P04, P07 |
| FMCSA record | The business moved to a VoIP number in 2026-03; the FMCSA record still shows the old mobile number (more than 30 days, 49 U.S.C. 13904(g)) | P01, P03 |
| TMS vendor assurance | SOC 2 Type 2, Security and Availability, 12 months ending 2026-03-31, unqualified, one exception (2 of 25 sampled quarterly access reviews late). Hosting provider carved out. Stated RTO 8 hours and RPO 24 hours. Reviewed by the owner on 2026-08-17 | P02, P04, P05, P09 |
| Largest shipper contract | The master broker-shipper agreement (2025) requires reasonable safeguards for shipper data, notice of a security incident affecting shipper data within 72 hours of discovery, and an annual security questionnaire | P03, P08, P09 |
| Railroad portal terms | Each railroad's portal terms require individual user IDs, no sharing of credentials, and prompt notice to the railroad of suspected unauthorized use | P03, P08 |
| AI document capture trial | Turned on 2026-06-15; automatic approval of carrier pay on "clean" PODs turned on 2026-07-01. To 2026-08-14 it processed 412 BOL and POD images. The owner's check of 60 sampled documents found 54 with every field right. Of 9 PODs with handwritten exception notes, it flagged 6 and missed 3; it also flagged 2 clean PODs. The 3 missed PODs led to carrier payments approved automatically before the shipper's damage or shortage claims arrived. In 4 of the 60 sampled documents the BOL number was wrong or blank. Vendor terms allow use of customer documents to improve its models unless the customer opts out. The owner turned off automatic approval on 2026-08-17 and opted out of model training on 2026-08-18 | P01, P03, P07, P10 |
| Insurance | No cyber or social engineering fraud coverage. Whether the general liability policy has any data breach endorsement is unconfirmed (owner action in P08) | P01, P08 |
