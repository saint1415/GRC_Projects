# Scenario facts: Cris Santos Company | Healthcare and Public Health | Sole Proprietorship

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes and of the Health Care (NAICS 62) samples. Where a fact comes from a regulation, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship; the pharmacist-owner files Schedule C) |
| Business | Independent community pharmacy with a small non-sterile compounding service (NAICS 456110 Pharmacies and Drug Retailers). Holds a Florida community pharmacy permit; the pharmacist-owner is the designated prescription department manager (Fla. Stat. 465.018(2)). DEA-registered retail pharmacy that dispenses Schedule II to V controlled substances. No sterile compounding |
| Location | Florida. One storefront in a small-town retail strip center: front counter, prescription department with a locked controlled substance cabinet, a compounding bench, and a small back office. Open Monday to Friday, 9:00 a.m. to 6:00 p.m.; closed weekends |
| Workforce | The pharmacist-owner only (0 employees). A relief pharmacist (independent contractor) covers about 2 business days a month and the owner's vacations |
| Patients | About 650 active patients. About 14 prescriptions a business day (about 3,500 a year); about 15% are controlled substances; about 40 compounded prescriptions a month. The pharmacy management system holds records for about 2,400 individuals (every patient since the pharmacy opened in 2021) |
| Revenue | About $180,000 a year (fictional), about $720 per business day. SBA-small (standard $37.5 million, NAICS 456110; 13 CFR 121.201) |
| Payers | Medicare Part D plans, Florida Medicaid, and commercial plans, all through pharmacy benefit managers (PBMs); about 10% of prescriptions are cash. The pharmacy is an enrolled Florida Medicaid provider. Medicaid is federal financial assistance, so Section 1557 (45 CFR Part 92) applies |
| HIPAA status | **Covered entity.** The pharmacy management system submits retail pharmacy drug claims electronically, in real time, to PBMs through a claims switch (45 CFR 160.103; the NCPDP Telecommunication Standard adopted at 45 CFR 162.1102) |
| DEA status | The pharmacy management system is the pharmacy application that receives and processes electronic prescriptions for controlled substances (EPCS), so the pharmacy duties in 21 CFR 1311.200 to 1311.215 and the recordkeeping rules in 1311.305 apply. Schedule II stock is ordered electronically from the wholesaler with the owner's CSOS digital certificate (21 CFR 1311.30) |
| Florida pharmacy duties used here | Report each controlled substance dispensed to the prescription drug monitoring program (PDMP) by the close of the next business day unless the department approves an extension or exemption (Fla. Stat. 893.055(3)(a)); keep controlled substance records at least 2 years (893.07); one-time emergency refill of up to a 72-hour supply when the prescriber cannot readily be reached (465.0275(1)) |
| Contrast worth noting | A cash-only pharmacy that never sent a standard electronic transaction would not be a HIPAA covered entity, whatever its size, but the DEA and Florida duties above would still apply. The HIPAA test is function, not size |
| Not in scope | **42 CFR Part 2**: the pharmacy does not hold itself out as providing substance use disorder diagnosis, treatment, or referral, so it is not a "program" (42 CFR 2.11). **FTC Health Breach Notification Rule**: excludes HIPAA covered entities (16 CFR 318.1). **CMS emergency preparedness rule** (C-HPH-R07): pharmacies are not among the provider and supplier types it covers. **CIRCIA** (C-HPH-R11): proposed only; even as proposed, the pharmacy is SBA-small and outside the sector criteria. **Payment cards**: a standalone terminal supplied by the card processor on its own cellular connection, under the merchant agreement. **Drug supply chain tracing (DSCSA)**: a product-tracing duty handled outside these security deliverables |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notice, Fla. Stat. 501.171; the pharmacy duties listed above) |

## 2. People and contracted services (role titles only)
| Role | Duties |
|---|---|
| Pharmacist-owner | Every role: owner, prescription department manager, Privacy Officer, Security Officer, risk acceptor, DEA registrant contact, CSOS certificate holder, and the only pharmacy management system administrator |
| Relief pharmacist (independent contractor) | Florida-licensed. Covers about 2 business days a month and the owner's vacations. A **workforce member** under 45 CFR 160.103 because the owner directs the work. **Signs in to the pharmacy management system with the owner's account** |
| Pharmacy management system vendor | Hosts the pharmacy management system. Business associate (BAA on file since 2021). Reaches the e-prescribing network and the claims switch under its own subcontractor agreements. Its support team uses a remote-support agent installed on the store desktop |
| Cloud fax vendor | Business associate (BAA on file) |
| Email and file suite vendor | Business plan. The vendor offers a BAA through its admin console. **The owner never accepted it** |
| On-call IT consultant | Set up the store network in 2021; hired by the hour. Signed a BAA on 2026-07-31, before the self-assessment. No standing access |
| Drug wholesaler | Ordering portal and electronic Schedule II orders (CSOS). No PHI |
| Accountant | Bookkeeping in an accounting SaaS. No PHI |

## 3. Systems
| ID | System | Hosting | Holds ePHI? | Notes |
|---|---|---|---|---|
| SYS-01 | Pharmacy management system (PMS): patient profiles, e-prescription intake including EPCS, drug utilization review (DUR) alerts, labels, claims through the switch, a nightly PDMP reporting file, the refill phone line, and refill text reminders | Vendor SaaS | Yes | System of record for prescriptions, patients, and billing. BAA; SOC 2 Type 2 report; EPCS certification report. MFA is enforced only for web sign-in from outside the store. The store desktop is a "trusted location" with **password-only** sign-in |
| SYS-02 | Email and file storage (business productivity suite) | SaaS | Yes | Faxed prescriptions and refill requests arrive here as attachments (fax-to-email). Holds the compounding master formulation records and compounding logs as spreadsheets. MFA on since 2024. **BAA available but not accepted** |
| SYS-03 | Store desktop at the prescription counter | Owner device | Yes (cached reports; scanned paper prescriptions) | Shared local account with automatic sign-in. **Not encrypted.** Holds the CSOS certificate in the browser certificate store. The PMS vendor's remote-support agent allows **unattended access**. Label printer and document scanner attached |
| SYS-04 | Owner laptop (back office and home) | Owner device | Yes (downloads) | Full-disk encryption on. Used for the books, email, and PMS web access from home |
| SYS-05 | Owner mobile phone | Personal device | Yes (email) | Second factor for email and for PMS web access from outside the store |
| SYS-06 | Cloud fax | Vendor SaaS | Yes | BAA on file. Delivers each incoming fax to the fax portal and, as a PDF, to the email inbox |
| SYS-07 | Store network | ISP-provided router with Wi-Fi | Yes (in transit) | **One network** for the desktop, the security camera recorder, and customer Wi-Fi (password printed at the counter) |
| SYS-08 | Consumer generative AI chatbot (free personal account) | Vendor SaaS | Yes (patient details pasted) | No BAA; see P10 |

Other business SaaS without ePHI (not given system IDs): the wholesaler ordering portal and the accounting SaaS.

**SSP system (P02):** the *Pharmacy Core SaaS Stack*: SYS-01 to SYS-08, with the pharmacy management system (SYS-01) as the client and billing records system.

## 4. Current security posture: early (few formal controls)
**In place today:**
- Vendor-hosted PMS under a BAA, with the vendor's backups and disaster recovery and a SOC 2 Type 2 report
- MFA on the email and file suite, and on PMS web sign-in from outside the store
- Full-disk encryption on the laptop
- BAAs with the PMS vendor and the cloud fax vendor (and the IT consultant since 2026-07-31)
- Automatic operating system updates and built-in antivirus on the desktop and laptop
- Locked controlled substance cabinet, monitored burglar alarm, and a security camera
- Paper prescriptions filed in a locked cabinet; a cross-cut shredder in the back office
- PDMP reports sent automatically each night by the PMS

**Missing:**
1. No risk analysis ever performed (Required, 45 CFR 164.308(a)(1)(ii)(A)).
2. No written security policies or procedures (only the notice of privacy practices and a privacy template from 2021).
3. The relief pharmacist signs in to the PMS with the owner's account, so dispensing records, including controlled substance records, name the wrong pharmacist (164.312(a)(2)(i); 21 CFR 1311.200(e)).
4. PMS sign-in at the store desktop uses a password only, and the owner's account is the PMS administrator account.
5. The store desktop is not encrypted, signs in automatically to a shared local account, and holds scanned prescriptions, downloaded reports, and the CSOS certificate.
6. Customer Wi-Fi, the camera recorder, and the desktop share one network.
7. The PMS vendor's remote-support agent on the desktop allows unattended access at any time; the owner never sees or approves sessions.
8. The email and file suite vendor's BAA was never accepted, although fax-to-email puts prescriptions in the inbox.
9. EPCS duties are not run: the daily internal audit report (21 CFR 1311.215(b)) has never been opened, there is no procedure for the one-business-day report to DEA and the PMS vendor (1311.215(c)), and the third-party EPCS audit or certification finding was never checked before first use (1311.200(a)).
10. No incident plan, downtime procedure, or contact list.
11. A consumer AI chatbot was used for compounding calculations and counseling sheets, with patient details pasted into it.
12. No security training for the owner or the relief pharmacist, and no cyber insurance.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| Primary system | The registry default ("Core business SaaS stack: email, files, client and billing records") is kept and named the Pharmacy Core SaaS Stack. In a pharmacy the client and billing records system is the PMS |
| P03 | HIPAA Security Rule (69 rows), plus the pharmacy's own duties under the DEA EPCS and CSOS rules in 21 CFR Part 1311 (14 rows), because the brief names DEA EPCS and both rules bind the pharmacy directly |
| P08 incident | Ransomware at the PMS vendor forces a multi-day PMS outage and the diversion of patients to nearby pharmacies; the vendor reports possible data theft. Adapted from the registry default ("ransomware forcing EHR downtime and ambulance diversion") because a pharmacy has no EHR or ambulances: its equivalents are the PMS and sending patients to other pharmacies |
| P09 SOC 2 | Security criteria only. The owner's self-check, plus a review of the PMS vendor's SOC 2 report and EPCS certification report. A self-attestation is enough for PBM network audits and prescriber offices |
| P10 AI | The consumer generative AI chatbot (SYS-08). Adapted from the registry default (a sepsis prediction model), which needs an inpatient setting a pharmacy does not have. The PMS's rule-based DUR alerts are also inventoried for Section 1557 |
| Cloud | SaaS only. No IaaS |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-07-31 | IT consultant signs a BAA |
| 2026-08-03 to 2026-08-07 | Self-assessment with the IT consultant: BIA, risk analysis, gap analysis, and control assessment (tests on 2026-08-06 after closing) |
| 2026-08-05 | PMS vendor's SOC 2 Type 2 report and EPCS certification report obtained and reviewed |
| 2026-08-12 | AI use review (P10) |
| 2026-09-04 | Deliverables adopted by the pharmacist-owner |

## 7. Facts added while building the deliverables
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
