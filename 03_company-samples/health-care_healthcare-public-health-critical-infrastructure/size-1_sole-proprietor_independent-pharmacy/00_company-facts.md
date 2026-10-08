# Scenario facts: Cris Santos Company | Healthcare and Public Health | Sole Proprietorship

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes and of the Health Care (NAICS 62) samples. Where a fact comes from a regulation, the citation is given.

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
| HIPAA status | **Covered entity**, determined in the intake obligations register (C-HPH-R01): the pharmacy management system submits retail pharmacy drug claims electronically, in real time, to PBMs through a claims switch (EV-005, EV-007; 45 CFR 160.103; the NCPDP Telecommunication Standard adopted at 45 CFR 162.1102) |
| DEA status | Determined in the intake obligations register (DEA-1311-EPCS, DEA-1311-CSOS; EV-005, EV-023, EV-025). The pharmacy management system is the pharmacy application that receives and processes electronic prescriptions for controlled substances (EPCS), so the pharmacy duties in 21 CFR 1311.200 to 1311.215 and the recordkeeping rules in 1311.305 apply. Schedule II stock is ordered electronically from the wholesaler with the owner's CSOS digital certificate (21 CFR 1311.30) |
| Florida pharmacy duties used here | Report each controlled substance dispensed to the prescription drug monitoring program (PDMP) by the close of the next business day unless the department approves an extension or exemption (Fla. Stat. 893.055(3)(a)); keep controlled substance records at least 2 years (893.07); one-time emergency refill of up to a 72-hour supply when the prescriber cannot readily be reached (465.0275(1)) |
| Contrast worth noting | A cash-only pharmacy that never sent a standard electronic transaction would not be a HIPAA covered entity, whatever its size, but the DEA and Florida duties above would still apply. The HIPAA test is function, not size |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv). **42 CFR Part 2**: the pharmacy does not hold itself out as providing substance use disorder diagnosis, treatment, or referral, so it is not a "program" (42 CFR 2.11). **FTC Health Breach Notification Rule**: excludes HIPAA covered entities (16 CFR 318.1). **CMS emergency preparedness rule** (C-HPH-R07): pharmacies are not among the provider and supplier types it covers. **CIRCIA** (C-HPH-R11): proposed only; even as proposed, the pharmacy is SBA-small and outside the sector criteria. **Payment cards**: a standalone terminal supplied by the card processor on its own cellular connection, under the merchant agreement. **Drug supply chain tracing (DSCSA)**: a product-tracing duty handled outside these security deliverables |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notice, Fla. Stat. 501.171; the pharmacy duties listed above) |

## 2. People and contracted services (role titles only)
| Role | Duties |
|---|---|
| Pharmacist-owner | Every role: owner, prescription department manager, Privacy Officer, Security Officer, risk acceptor, DEA registrant contact, CSOS certificate holder, and the only pharmacy management system administrator |
| Relief pharmacist (independent contractor) | Florida-licensed. Covers about 2 business days a month and the owner's vacations. A **workforce member** under 45 CFR 160.103 because the owner directs the work. **Signs in to the pharmacy management system with the owner's account** (EV-001, EV-021, EV-IA-2) |
| Pharmacy management system vendor | Hosts the pharmacy management system. Business associate (BAA on file since 2021). Reaches the e-prescribing network and the claims switch under its own subcontractor agreements. Its support team uses a remote-support agent installed on the store desktop |
| Cloud fax vendor | Business associate (BAA on file) |
| Email and file suite vendor | Business plan. The vendor offers a BAA through its admin console. **The owner never accepted it** (EV-012, EV-019) |
| On-call IT consultant | Set up the store network in 2021; hired by the hour. Signed a BAA on 2026-07-31, before the self-assessment. No standing access (EV-019, EV-022) |
| Drug wholesaler | Ordering portal and electronic Schedule II orders (CSOS). No PHI |
| Accountant | Bookkeeping in an accounting SaaS. No PHI |

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv). The notes below cite the evidence for each as-found setting.

| ID | System | Hosting | Holds ePHI? | Notes |
|---|---|---|---|---|
| SYS-01 | Pharmacy management system (PMS): patient profiles, e-prescription intake including EPCS, drug utilization review (DUR) alerts, labels, claims through the switch, a nightly PDMP reporting file, the refill phone line, and refill text reminders | Vendor SaaS | Yes | System of record for prescriptions, patients, and billing. BAA; SOC 2 Type 2 report; EPCS certification report (EV-019, EV-037, EV-038). MFA is enforced only for web sign-in from outside the store. The store desktop is a "trusted location" with **password-only** sign-in (EV-002) |
| SYS-02 | Email and file storage (business productivity suite) | SaaS | Yes | Faxed prescriptions and refill requests arrive here as attachments (fax-to-email). Holds the compounding master formulation records and compounding logs as spreadsheets. MFA on since 2024. **BAA available but not accepted** (EV-012) |
| SYS-03 | Store desktop at the prescription counter | Owner device | Yes (cached reports; scanned paper prescriptions) | Shared local account with automatic sign-in. **Not encrypted.** Holds the CSOS certificate in the browser certificate store. The PMS vendor's remote-support agent allows **unattended access**. Label printer and document scanner attached (EV-004, EV-014) |
| SYS-04 | Owner laptop (back office and home) | Owner device | Yes (downloads) | Full-disk encryption on. Used for the books, email, and PMS web access from home (EV-015) |
| SYS-05 | Owner mobile phone | Personal device | Yes (email) | Second factor for email and for PMS web access from outside the store (EV-002, EV-015) |
| SYS-06 | Cloud fax | Vendor SaaS | Yes | BAA on file. Delivers each incoming fax to the fax portal and, as a PDF, to the email inbox (EV-013, EV-019) |
| SYS-07 | Store network | ISP-provided router with Wi-Fi | Yes (in transit) | **One network** for the desktop, the security camera recorder, and customer Wi-Fi (password printed at the counter) (EV-016, EV-017) |
| SYS-08 | Consumer generative AI chatbot (free personal account) | Vendor SaaS | Yes (patient details pasted) | No BAA (EV-032, EV-033); see P10 |

Other business SaaS without ePHI (not given system IDs; OTH-05 and OTH-06 in the inventory): the wholesaler ordering portal and the accounting SaaS.

**SSP system (P02):** the *Pharmacy Core SaaS Stack*: SYS-01 to SYS-08, with the pharmacy management system (SYS-01) as the client and billing records system.

## 4. Where the evidence is
This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Every item has a source system, an owner, and as-of and collected dates. For a one-person pharmacy the sources are the vendors' admin portals and reports (the pharmacy management system, the email and file suite, the cloud fax portal, the wholesaler portal), the DEA and Florida Board of Pharmacy records, bank and card statements, the inbox, signed agreements, the devices and router, the store walk-through, and the insurance agent's portal.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv), including the DEA EPCS and CSOS duties and the Florida pharmacy duties.
- **Gaps against the HIPAA Security Rule and the DEA pharmacy duties** are judged in the gap analysis (P03), and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

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
| 2026-07-27 to 2026-07-31 | Intake: the owner collects PMS, email, fax and router settings and reports, statements, agreements, license and registration records, device settings and the store walk-through; inventories; obligations register |
| 2026-07-31 | IT consultant signs a BAA |
| 2026-08-03 to 2026-08-07 | Self-assessment with the IT consultant: BIA, risk analysis, gap analysis, and control assessment (tests on 2026-08-06 after closing) |
| 2026-08-05 | PMS vendor's SOC 2 Type 2 report and EPCS certification report obtained and reviewed |
| 2026-08-10 to 2026-09-03 | POL-01 drafted from the gaps and the test results |
| 2026-08-12 | AI use review (P10) |
| 2026-09-04 | Deliverables and POL-01 adopted by the pharmacist-owner (POL-01 effective 2026-09-08) |
| 2027-03 (planned) | Follow-up check: operating effectiveness of the controls POL-01 introduced, after at least one quarter of operation |

## 7. Facts added while building the deliverables
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Evidence | Used in |
|---|---|---|---|
| PMS vendor recovery | The PMS vendor's SOC 2 system description states an RPO of 1 hour and an RTO of 12 hours, with an annual failover test and backups kept in a separate region. The RPO meets the BIA; the RTO does not meet the 4-hour RTO for dispensing | EV-037 | P02, P04, P05, P07, P08, P09 |
| PMS vendor SOC 2 report | Type 2, Security and Availability, period 2025-04-01 to 2026-03-31, unqualified opinion. One exception: for 2 of 40 sampled departed vendor staff, access was removed later than the vendor's 1-business-day standard (remediated). The e-prescribing network, the claims switch, and the hosting provider are carved out. Bridge letter requested 2026-08-05 | EV-037 | P09 |
| EPCS certification report | Issued 2025-11-14 by a DEA-approved certification organization. Finds the PMS accurately and consistently imports, stores, and displays the required prescription information, the indication of signing, and refills, with no limitation; the last intermediary digitally signs each record before transmission (21 CFR 1311.210(a)(1)). Next report due by 2027-11-14. The owner obtained and read it for the first time on 2026-08-05 | EV-038 | P02, P03, P09 |
| PMS BAA terms | BAA in place since 2021; on 2026-08-05 the owner found it contains the required terms and flows them down to the vendor's subcontractors. It requires breach notice within 30 days and reports other security incidents only on request. The cloud fax BAA is silent on subcontractors | EV-039 | P03, P08, P09 |
| Relief pharmacist practice | Signs in to the PMS with the owner's account. The PMS password was kept on a card in the counter drawer and had not changed since 2023; the card was destroyed and the password changed on 2026-08-06. The owner checked the relief pharmacist's Florida license online in 2025 but kept no record. The contract has no confidentiality or security clause. The relief pharmacist holds a store key and the alarm code, and confirmed the sign-in practice by phone during P07 | EV-001, EV-002, EV-017, EV-021, EV-036, EV-IA-2 | P01, P02, P03, P06, P07, P09 |
| EPCS record sample | 2 of 10 sampled EPCS dispensing records from the last 12 months were filled on relief days but name the owner as the dispensing pharmacist | EV-IA-2 | P03, P07 |
| EPCS daily audit report | The PMS keeps 90 days of daily EPCS audit reports. The first review, on 2026-08-06, found 3 failed sign-ins (all explained by the owner) and no alteration or access-control events | EV-003, EV-AU-6 | P02, P03, P07 |
| Vendor remote-support agent | Allowed unattended access; the session history showed 9 vendor sessions in the past 12 months, none watched. Switched to attended mode on 2026-08-06 during P07 testing | EV-004, EV-AC-17 | P01, P02, P04, P07 |
| Counter desktop contents | Scanned paper prescriptions, daily controlled substance reports downloaded from the PMS, and a 2025 patient mailing-list export of about 2,100 patients (names, addresses, birth dates). The PMS session stays open all day and the desktop never locks. The owner restarts it each Friday after closing | EV-014, EV-017 | P01, P02, P04, P07 |
| Old desktop | The previous counter desktop, replaced in 2024, sits unwiped in the back office with no disposal record | EV-017, EV-030 | P02, P03, P09 |
| Cloud fax MFA | The cloud fax portal supports MFA, but it was off (settings collected at intake; identified as an issue in P04 mapping) | EV-013 | P02, P03, P04 |
| Network scan | On 2026-08-06 the IT consultant's scan found the desktop, the camera recorder, and customer Wi-Fi clients on one network, and no inbound ports open on the router | EV-016, EV-SC-7 | P07 |
| AI chatbot use | Used from 2026-03-02 to 2026-08-07 in about 60 conversations: about 35 drafting counseling sheets, about 15 checking compounding calculations or formulations, about 10 drug information questions. Patient details (names or initials, ages, drugs, doses; allergies in 2) appeared in 6 conversations, each about one patient, found on 2026-08-12. The training setting was on until 2026-08-12. In one conversation the chatbot converted a percentage strength to milligrams incorrectly; the owner caught it against the master formulation record | EV-032, EV-040 | P01, P04, P10 |
| DUR alerts | The PMS's rule-based DUR alerts (AI-002) use age, sex, pregnancy and lactation flags, allergies, medication history, and dose | EV-010 | P10 |
| Refill reminder texts | Contain only the pharmacy name and the words that a prescription is ready, with no drug name | EV-011 | P02, P06, P08 |
| Cyber insurance | No standalone cyber policy. Whether the business owner's or professional liability policy has a cyber or business-interruption endorsement is unconfirmed (owner action in P08) | EV-020, EV-029 | P01, P08 |
| Prescribers and residency | About 10 prescriber offices send most prescriptions. About 30 seasonal patients have addresses in other states | EV-009 | P08 |
| Transfer arrangement | A written arrangement with a nearby independent pharmacy to take transfers and new prescriptions during a closure is planned (not yet signed) | EV-030 | P01, P05, P06, P08 |
| Costs | An extra PMS user license costs about $15 a month; a replacement router about $150 if needed; the IT consultant's network split about 3 hours. Recurring security costs (password manager, consultant time, annual courses) are about $500 a year | Planning estimates (no evidence ID) | P01, P07 |
| Policy dates | POL-01 adopted 2026-09-04 and effective 2026-09-08; daily EPCS report review starts 2026-09-08 | P06 decision (no evidence ID) | P02, P06, P07 |
