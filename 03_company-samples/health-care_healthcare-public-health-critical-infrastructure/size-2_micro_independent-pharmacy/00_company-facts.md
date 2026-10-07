# Scenario facts: Cris Santos Company | Healthcare and Public Health | Micro

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes and of the Health Care (NAICS 62) samples. Where a fact comes from a regulation, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (operator of one independent community pharmacy; the store's trade name is not used in this sample) |
| Business | Independent community pharmacy (NAICS 456110 Pharmacies and Drug Retailers), open since 2012. Holds a Florida community pharmacy permit; the pharmacist-owner is the designated prescription department manager (Fla. Stat. 465.018(2)). DEA-registered retail pharmacy that dispenses Schedule II to V controlled substances. Services: retail prescriptions, free local delivery, and weekly multi-dose adherence packaging. No compounding and no immunizations |
| Location | Florida. One storefront in a neighborhood shopping center: front store and register, pickup counter, prescription department with a locked Schedule II safe, an adherence packaging room, and a back office. Open Monday to Friday 9:00 a.m. to 7:00 p.m. and Saturday 9:00 a.m. to 1:00 p.m. (about 306 business days a year) |
| Workforce | 7 employees: the pharmacist-owner, 1 staff pharmacist, 1 Store Manager (a registered pharmacy technician), 1 lead pharmacy technician, 1 pharmacy technician, 1 front-store clerk, and 1 delivery driver |
| Patients | About 3,100 active patients. About 55 prescriptions a business day (about 16,800 a year); about 12% are controlled substances. About 70 patients receive weekly adherence packs, including about 40 residents of two assisted living facilities (ALFs) operated by one management company. About 25 deliveries a day. The pharmacy management system holds records for about 11,500 individuals (every patient since 2012) |
| Revenue | About $1.1 million a year (fictional), about $3,600 per business day. SBA-small (standard $37.5 million for NAICS 456110; 13 CFR 121.201) |
| Payers | Medicare Part D plans, Florida Medicaid, and commercial plans, all through pharmacy benefit managers (PBMs); about 7% of prescriptions are cash. The pharmacy is an enrolled Florida Medicaid provider. Medicaid is federal financial assistance, so Section 1557 (45 CFR Part 92) applies |
| HIPAA status | **Covered entity.** The pharmacy management system submits retail pharmacy drug claims to PBMs electronically, in real time, through a claims switch, using the adopted NCPDP Telecommunication Standard (45 CFR 160.103; 45 CFR 162.1102(c)) |
| DEA status | The pharmacy management system is the pharmacy application that receives and processes electronic prescriptions for controlled substances (EPCS), so the pharmacy duties in 21 CFR 1311.200 and 1311.215 and the recordkeeping rules in 1311.305 apply. Schedule II stock is ordered electronically from the wholesaler with the pharmacist-owner's CSOS digital certificate (21 CFR 1311.30) |
| Florida pharmacy duties used here | Report each controlled substance dispensed to the prescription drug monitoring program (PDMP) by the close of the next business day (Fla. Stat. 893.055(3)(a)); consult the PDMP before dispensing a controlled substance to a patient aged 16 or older, except when the system cannot be accessed because of a temporary technological or electrical failure, in which case the reason is documented and no more than a 3-day supply is dispensed (893.055(8)); keep controlled substance records for at least 2 years (893.07(4)) and report a theft or significant loss of controlled substances to the county sheriff within 24 hours of discovery (893.07(5)(b)); one-time emergency refill of up to a 72-hour supply when the prescriber cannot readily be reached (465.0275(1)), and up to a 30-day supply of non-Schedule II maintenance drugs in counties covered by a Governor's state of emergency (465.0275(2)); pharmacy dispensing records may be released only as chapter 465 and related chapters allow (465.017(3)) |
| Not in scope | **42 CFR Part 2**: the pharmacy does not hold itself out as providing substance use disorder diagnosis, treatment, or referral, so it is not a "program" (42 CFR 2.11). **FTC Health Breach Notification Rule**: excludes HIPAA covered entities (16 CFR 318.1). **CMS emergency preparedness rule** (C-HPH-R07): pharmacies are not among the provider and supplier types it covers. **CIRCIA** (C-HPH-R11): proposed only; even as proposed, the pharmacy is SBA-small and meets none of the proposed health care sector criteria. **Payment cards**: a standalone card terminal supplied by the card processor under the merchant agreement; it never touches the store network or the pharmacy management system. **Drug supply chain tracing (DSCSA)**: a product-tracing duty handled outside these security deliverables |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notice, Fla. Stat. 501.171; the pharmacy duties listed above) |

## 2. People and contracted services (role titles only)
| Role | Security and privacy duties |
|---|---|
| Pharmacist-owner (managing member) | Prescription department manager; accepts risk; approves policies and spending; DEA registrant contact; holder of the only CSOS certificate; backup pharmacy management system administrator |
| Store Manager (registered pharmacy technician) | HIPAA **Privacy Officer and Security Officer** (combined; designated in writing on 2026-07-10). Front store, purchasing, scheduling, and payroll coordination; keeps vendor contracts and the BAA folder; primary pharmacy management system administrator; the MSP's day-to-day contact |
| Staff Pharmacist | Verifies and dispenses prescriptions; covers Saturdays and the owner's days off; clinical lead for the pharmacy management system's controlled substance risk score (P10) |
| Lead Pharmacy Technician | Prescription intake and claims; leads adherence packaging and the ALF relationship |
| Pharmacy Technician | Intake, filling, and pickup |
| Front-Store Clerk | Register and pickup counter support |
| Delivery Driver | Deliveries with the store delivery phone and the proof-of-delivery app |
| Managed service provider (MSP) | Help desk, patching, antivirus, firewall and Wi-Fi, and backup administration. A business associate (BAA on file since 2021) |
| Pharmacy management system vendor | Hosts the pharmacy management system. Business associate (BAA since the 2019 move to the hosted version). Reaches the e-prescribing network, the claims switch, and the PDMP under its own subcontractor agreements |
| Adherence packaging equipment vendor | Supplies and services the strip packager and its controller workstation. Its support team keeps an always-on remote-support connection. **No BAA** |

## 3. Systems
| ID | System | Hosting | Holds ePHI? | Notes |
|---|---|---|---|---|
| SYS-01 | Pharmacy management system (PMS): patient profiles, e-prescription intake including EPCS, drug utilization review (DUR) alerts, labels, real-time claims through the switch, the nightly PDMP reporting file, the refill phone line, refill text reminders, pickup signature capture, and the order interface to SYS-05 | Vendor SaaS | Yes | System of record for prescriptions, patients, and billing. BAA; SOC 2 Type 2 report; EPCS third-party audit report. Named accounts for every user. MFA only for web sign-in from outside the store; in-store sign-in is **password only** |
| SYS-02 | Business productivity suite (email, calendar, shared drive) | SaaS | Yes | BAA accepted in the admin console in 2024. MFA on all 7 accounts since 2025. The shared drive holds ALF order sheets and medication lists, packaging schedules, controlled substance inventory spreadsheets, delivery logs, invoices, and HR files |
| SYS-03 | Endpoints: 5 desktops (2 intake stations, 1 pharmacist verification station, 1 pickup counter station with a signature pad, 1 back-office desktop), 2 laptops (pharmacist-owner, Store Manager), 1 store delivery phone | MSP-managed | Yes (cached reports, downloaded faxes) | Laptops encrypted; **desktops not encrypted**. The 3 counter desktops sign in automatically to one shared operating system account; each user then signs in to the PMS |
| SYS-04 | Store network: small-business firewall, staff Wi-Fi, guest Wi-Fi | On-premises | Yes (in transit) | MSP-managed. Guest Wi-Fi is separated. Desktops, the SYS-05 controller workstation, VoIP phones, and the camera recorder share **one staff network** |
| SYS-05 | Adherence packaging system: strip packager and its controller workstation | On-premises | Yes | Receives orders from SYS-01; stores patient names, drugs, and administration times. Runs an operating system version whose vendor support has ended. One shared "packaging" login. Equipment vendor's always-on remote-support connection |
| SYS-06 | Cloud fax | Vendor SaaS | Yes | BAA on file. New prescriptions, refill authorizations, and ALF orders |
| SYS-07 | Cloud backup service | SaaS (MSP-operated) | Yes | Nightly copy of the shared drive and nightly images of the back-office desktop and the SYS-05 controller workstation; 30 days of versions. **Never restore-tested** |
| SYS-08 | Proof-of-delivery app (free tier) on the store delivery phone | Vendor SaaS | Yes | Route list with patient names, addresses, prescription numbers, and signature photos. **No BAA** |
| SYS-09 | Controlled substance risk score | Feature of SYS-01 (PMS vendor) | Yes | Machine-learning score shown on each incoming controlled substance prescription. Switched on by the vendor's May 2026 release (see P10) |

Other business SaaS without ePHI (not given system IDs): the drug wholesaler's ordering portal, the payroll service, and the accounting SaaS.

**SSP system (P02):** the *Pharmacy Core SaaS Stack*: SYS-01 to SYS-08, with the pharmacy management system (SYS-01) as the client and billing records system; the SYS-09 feature is assessed separately in P10.

## 4. Current security posture: early to partial
**In place today:**
- Vendor-hosted PMS under a BAA, with the vendor's backups, disaster recovery, SOC 2 Type 2 report, and EPCS third-party audit
- Named PMS accounts for every workforce member, with pharmacist-only verification rights
- MFA on the productivity suite and on PMS web sign-in from outside the store
- MSP patching, antivirus, firewall, and separated guest Wi-Fi
- BAAs with the PMS vendor, the MSP, the cloud fax vendor, and the productivity suite vendor
- Laptop encryption
- Locked Schedule II safe, monitored burglar alarm, and security cameras
- PDMP reports sent automatically each night by the PMS
- A cyber liability insurance policy with a breach hotline (since the 2024 renewal)
- A HIPAA privacy video at hire

**Missing:**
1. No security risk analysis. The only document is a 2022 HIPAA checklist from the PMS vendor (Required, 45 CFR 164.308(a)(1)(ii)(A)).
2. A purchased policy binder (2019) was never tailored or adopted; there is no incident procedure.
3. EPCS duties are not run: the PMS generates the daily internal audit report (21 CFR 1311.215(b)) but nobody opens it; there is no procedure for the one-business-day report to DEA and the PMS vendor (1311.215(c)); and the current EPCS audit report has not been obtained since the 2019 go-live (1311.200(a), 1311.300(a)(2)).
4. PMS logical access for controlled substance records is wider than intended: the Lead Pharmacy Technician and the Store Manager hold a permission that lets them annotate and alter dispensed controlled substance prescription records (1311.200(e)).
5. The Store Manager places Schedule II orders on the pharmacist-owner's laptop with the owner's CSOS certificate (1311.30(a), (c)).
6. The 5 desktops are not encrypted, and the 3 counter desktops sign in automatically to one shared operating system account.
7. The SYS-05 packaging workstation uses one shared login, runs an unsupported operating system, sits on the staff network, and has an always-on vendor remote-support connection with no BAA.
8. The backup (SYS-07) has never been restore-tested, keeps only 30 days of versions, and its console uses a password only.
9. Account removal depends on memory; there is no access review.
10. No incident response plan, downtime procedure, or contact list.
11. No contingency plan; one internet line with no failover.
12. No security training beyond the privacy video at hire; no phishing awareness.
13. The proof-of-delivery app (SYS-08) handles ePHI without a BAA.
14. The controlled substance risk score (SYS-09) went live without review (P10).

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| Primary system | The registry default ("Core business SaaS stack: email, files, client and billing records") is kept and named the Pharmacy Core SaaS Stack. In a pharmacy, the client and billing records system is the PMS |
| P03 | HIPAA Security Rule (69 rows), plus the pharmacy's own DEA duties for EPCS and CSOS in 21 CFR Part 1311 (13 rows), because the brief names DEA EPCS and both rules bind the pharmacy directly |
| P08 incident | Ransomware on the store's own computers forces PMS downtime at the counter and the diversion of prescriptions to nearby pharmacies, with data theft from the shared drive. Adapted from the registry default ("ransomware forcing EHR downtime and ambulance diversion"): a pharmacy has no EHR or ambulances; its equivalents are the PMS and sending patients and prescriptions to other pharmacies. The MSP and the cyber insurer are in the notification chain |
| P09 SOC 2 | Security plus Availability. The readiness self-assessment answers a vendor questionnaire from the ALF management company; plus a review of the PMS vendor's SOC 2 Type 2 report and EPCS audit report |
| P10 AI | The PMS controlled substance risk score (SYS-09). Adapted from the registry default (a sepsis prediction model), which needs an inpatient setting a pharmacy does not have. Like a sepsis model, it is a vendor-built predictive score that supports clinical decisions, so Section 1557 (45 CFR 92.210) applies |
| Cloud | SaaS plus one cloud workload: the MSP-operated cloud backup service (SYS-07). Vendor-agnostic |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-07-10 | Store Manager designated Privacy Officer and Security Officer in writing |
| 2026-07-13 to 2026-07-24 | BIA, risk analysis, and gap analysis with the MSP lead technician |
| 2026-08-04 to 2026-08-06 | Control assessment by an independent consultant (on-site tests 2026-08-05 after closing) |
| 2026-08-12 | PMS vendor SOC 2 Type 2 report and EPCS audit report reviewed |
| 2026-08-17 to 2026-08-19 | Controlled substance risk score review (P10) |
| 2026-08-28 | Deliverables approved by the pharmacist-owner |

## 7. Facts added while building the deliverables
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| Partner pharmacy | A nearby independent pharmacy has agreed informally to accept transferred prescriptions and lend stock during outages; the arrangement is to be put in writing in the contingency plan (due 2026-11-30) | P05, P08, P09 |
| Operating rhythm | Adherence packs are built 2 days before the Wednesday delivery; a printed list of the week's packs and ALF residents' medications is refreshed each Monday (from 2026-09). The wholesaler delivers next day and fast movers are stocked for about 2 days. A cash reserve covers about 3 weeks of expenses. Payroll is biweekly through the payroll service | P01, P05, P08 |
| MSP and equipment contracts | The MSP contract covers help desk, patching, antivirus, firewall, Wi-Fi, and backup administration, with a 4-business-hour response time and no recovery time commitment. The SYS-07 subscription is resold by the MSP, so the backup service is the MSP's subcontractor (flow-down unverified). The packaging equipment vendor's service contract gives next-business-day on-site support | P02, P04, P05, P07 |
| PMS settings | The vendor treats the store network as a trusted location, so in-store sign-in has no second factor. The store asked the vendor in 2019 to raise the idle timeout from 15 to 60 minutes. The PMS password rule is the vendor default of 8 characters. The Store Manager used the PMS administrator role for daily work | P01, P02, P03, P07 |
| Controlled substance permission | The permission to annotate and alter dispensed controlled substance records was given to the Lead Pharmacy Technician and the Store Manager in 2019 to fix claim errors. Found 2026-07-16 and removed 2026-07-17; the pharmacist-owner reviewed 12 months of alterations and found no change to a drug, quantity, or patient | P01, P02, P03, P07 |
| EPCS audit report | The daily report had never been opened. A review of the 90 retained reports on 2026-07-21 found 4 failed sign-ins and the claim-correction alterations by the 2 non-pharmacists; none was a security incident. A sample of 10 EPCS records and a retrieval test were done the same day. The vendor's EPCS third-party audit report (by a Certified Information Systems Auditor, dated 2025-10-15) was obtained and the 21 CFR 1311.200(a) determination recorded on 2026-08-12 | P03, P07, P09 |
| CSOS certificate | The certificate password had been saved in the owner laptop browser. The certificate was revoked on 2026-07-17 and reissued to the pharmacist-owner on 2026-08-03 (paper DEA order forms in between); the wholesaler order history showed no unrecognized orders. The Store Manager will apply for a separate certificate under a power of attorney | P01, P03, P06 |
| Former technician | Left in late April 2026; PMS and email accounts stayed active about 11 weeks and were disabled on 2026-07-14; sign-in logs showed no use after the last day. The technician held no keys or devices | P01, P02, P03, P07 |
| Past events | A fax with an ALF resident's medication list went to a wrong number in March 2026 and was never assessed or logged. A desktop retired in 2024 has no wipe or destruction record. 4 of 10 sampled July 2026 emails to the ALFs with medication lists were sent unencrypted | P01, P02, P03, P07 |
| Shared drive contents | Monthly delivery log exports since 2021 (names, addresses, prescription numbers), ALF order sheets and medication lists, packaging schedules, and controlled substance inventory spreadsheets. Counter desktops hold downloaded faxes in their download folders | P01, P04, P08 |
| Shared logins | The 3 counter desktops sign in automatically to one operating system account that has local administrator rights. The delivery app has one shared driver login used since 2025. The MSP set the same local administrator password on all 5 desktops and the packaging workstation in 2021 (found in P07 testing on 2026-08-05) | P01, P02, P07 |
| Store and network | Keys and alarm codes are held by the pharmacist-owner, the Staff Pharmacist, and the Store Manager; vendor technicians are escorted by a pharmacist. The pickup counter screen faced the waiting line. Staff Wi-Fi uses WPA2 with a password unchanged since 2021. Store walkthrough 2026-07-15 | P02, P03, P07 |
| Workforce records | Pharmacist and technician licenses are checked at hire, and the application asks the DEA employee screening question. The employee handbook has no security or privacy sanctions rule. The HIPAA privacy video dates from 2019 | P03, P07, P09 |
| BAA terms | The PMS vendor BAA says security incidents are reported "promptly"; the MSP BAA says within 30 days | P03, P09 |
| Assessment details | The P07 assessor is an independent HIPAA security consultant who took no part in P01 or P03. MSP evidence was requested on 2026-07-28. The risk analysis was reviewed with the pharmacist-owner on 2026-07-28. An after-hours test alert on 2026-08-05 was not seen by the MSP until 8:40 a.m. the next day. The July MSP patch report showed 2 desktops 34 days behind on a critical update | P07 |
| Cyber insurance | The policy (since the 2024 renewal) has a 24x7 breach hotline and panel breach counsel and forensics, and requires prompt notice before outside firms are hired | P06, P08 |
| ALF questionnaire | The ALF management company sent a security questionnaire organized by the Trust Services Criteria in July 2026; the response is due 2026-09-30; a self-assessment is accepted | P09 |
| PMS vendor SOC 2 report | Type 2, unqualified, 12 months ending 2026-03-31; Security, Availability, and Confidentiality; e-prescribing network, claims switch, and hosting provider carved out; 1 exception (2 of 40 releases deployed without documented approval, remediated 2026-02); stated RTO 4 hours and RPO 30 minutes; customer incident notice within 72 hours | P05, P09 |
| Controlled substance risk score | Inputs: age, sex, prescriber and pharmacy counts, morphine milligram equivalents, early refill history, payment type, and patient-to-prescriber distance; no PDMP data. Release notes for the May 2026 release went unread. Review of 342 controlled substance prescriptions (2026-06-01 to 2026-07-31) gave the results in P10. Display limited to pharmacists on 2026-08-19; staff briefed on 2026-08-21 | P01, P10 |
| Budget | Funded treatments of about $5,200 one-time and $3,240 a year, approved 2026-08-28 (P01 section 4) | P01, P07 |
