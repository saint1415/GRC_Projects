# Scenario facts: Cris Santos Company | Defense Industrial Base | Micro

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or contract clause, the citation is given. Regulatory text was checked on eCFR (version date 2026-09-23).

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (privately held; Cris Santos is the sole owner and President) |
| Business | Aircraft parts manufacturer (NAICS 336413, Other Aircraft Parts and Auxiliary Equipment Manufacturing): a build-to-print CNC machine shop making small machined aluminum, steel, and titanium brackets, fittings, bushings, and spacers for military and commercial aircraft programs. The quality system follows AS9100 but is not registered; Prime A approved the shop through its own supplier quality audit in 2025 |
| Location | Florida. One leased industrial unit: shop floor with 5 CNC machines, an inspection room with 1 coordinate measuring machine (CMM), a small office, and a shipping and receiving area |
| Workforce | 7 employees: President (owner), Office Manager, CNC Programmer, Quality Inspector, Lead Machinist, 2 CNC Machinists. All are U.S. persons as defined in 22 CFR 120.62 (one machinist is a lawful permanent resident) |
| Revenue | About $1.1 million a year (fictional), about $4,400 of shipments per production day over about 250 production days. About 55% defense subcontract work (Prime A about 40%, Supplier B about 15%) and 45% commercial aerospace and industrial work (Customer C is the largest). SBA size standard for NAICS 336413 is 1,250 employees (13 CFR 121.201), so the company is SBA-small |
| Defense customers | **Prime A**, a DoD prime contractor (the company is a first-tier subcontractor under purchase orders), and **Supplier B**, a first-tier subcontractor to another prime (the company is a second-tier subcontractor). The company holds no prime DoD contract. It has a CAGE code |
| Commercial customers | **Customer C**, a commercial aerospace tier-1 supplier, plus local industrial customers |
| CUI handled | Controlled technical information (CTI) as defined in DFARS 252.204-7012(a): drawings, 3D models, and specifications received from Prime A and Supplier B, and the CAM files, NC programs, setup sheets, and CMM inspection programs derived from them. It is covered defense information (CDI) and CUI. About 60 of the shop's 140 active part numbers are CUI; about 25 of those are ITAR defense articles, so their technical data is ITAR-controlled |
| Contract clauses in current purchase orders | DFARS 252.204-7012 (MAY 2024), 252.204-7019 and 252.204-7020 (NOV 2023), and FAR 52.204-21 (NOV 2021), in both Prime A's and Supplier B's purchase order terms. No current purchase order includes DFARS 252.204-7021 |
| CMMC requirement | On 2026-06-15 Prime A told suppliers that purchase orders under its new program contract (awarded in 2026 with a CMMC Level 2 (Self) requirement, as Phase 1 allows under 32 CFR 170.3(e)(1)) will flow down DFARS 252.204-7021 (NOV 2025) at **CMMC Level 2 (Self)** for purchase orders issued from **2027-04-01**. A subcontractor that processes CUI needs at least Level 2 (Self) (32 CFR 170.23(a)(2)), and Level 2 (C3PAO) if the prime contract requires it (170.23(a)(3)). Prime A warned that later programs may require Level 2 (C3PAO) once Phase 2 begins on 2026-11-10. Supplier B has not yet stated a level |
| Export controls | Registered with the State Department's Directorate of Defense Trade Controls (22 CFR 122.1: one occasion of manufacturing a defense article requires registration, even with no exports). The President is the Empowered Official (22 CFR 120.67). Some commercial parts carry EAR-controlled technology |
| Not in scope | Classified information: no facility clearance, so NISPOM (32 CFR Part 117) does not apply. CIRCIA reporting: the final rule is not published. Health, payment card, and consumer data: none beyond employee records |
| State law approach | Florida law is cited only where unavoidable (breach notice for employee personal information, Fla. Stat. 501.171). Otherwise the samples stay federal |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| President (owner) | Accepts Moderate, High, and Very High risks; approves policies and spending; **CMMC Affirming Official** (32 CFR 170.22); signs SPRS submissions; **ITAR Empowered Official**; customer contracts and flowdowns; decision maker in an incident |
| Office Manager | **Security and Compliance Coordinator** (designated in writing on 2026-07-06): runs the program day to day with the MSP; keeps the SSP, risk register, and POA&M; onboarding and offboarding; visitor log; training records. Also bookkeeping, HR, purchasing, and shipping documents. Backup DoD reporting contact |
| CNC Programmer | CUI data custodian: downloads drawings and models from customer portals, keeps the controlled job folders, writes CAM and NC programs, sends programs to machines, prints setup sheets |
| Quality Inspector | CMM programs, inspection records, first article reports; printed drawings in the inspection room |
| Lead Machinist | Shop floor: machine setups, USB loading of the 2 older machines, custody of printed drawings on the floor, end-of-shift drawing return |
| CNC Machinists (2) | Run machines from printed drawings and setup sheets. No accounts in the CUI suite |
| Managed service provider (MSP) | Help desk, patching, antivirus, firewall, backups, and tenant administration for both productivity suites under a monthly contract (4-business-hour response). It holds administrator credentials and runs the remote management tool, so it handles Security Protection Data and is an External Service Provider whose services are in the assessment scope as Security Protection Assets (32 CFR 170.4; 170.19(c)(2), Table 4). It is not a cloud service provider for CUI |
| Independent assessor | Consultant experienced in NIST SP 800-171A assessments, engaged for the P07 readiness assessment. Not a C3PAO; did not take part in the risk or gap analysis and operates no control |

## 3. Systems

| ID | System | Hosting | CUI? | CMMC asset category (32 CFR 170.19(c)) | Notes |
|---|---|---|---|---|---|
| SYS-01 | CUI suite: government-community cloud productivity suite (email, file storage with the controlled job folders, identity and MFA) | Government-community cloud SaaS; offering FedRAMP authorized at Moderate or higher | Yes | CUI Asset (identity functions are Security Protection Assets) | Live since 2026-03-09, set up by the MSP. 4 licensed users (President, Office Manager, CNC Programmer, Quality Inspector), 1 MSP administrator account, 1 break-glass account. MFA by authenticator app. Provider customer responsibility matrix (CRM) **not on file** |
| SYS-02 | Commercial productivity suite (business email and files) | Commercial SaaS | **Not intended, but holds CUI today** | Intended Out-of-Scope; in scope until cleaned | 5 user accounts plus a shared "orders" mailbox. Supplier B still emails drawings to the orders mailbox; 2024-2025 job folders with drawings were never migrated. MFA on user accounts; **the shared mailbox has no MFA** |
| SYS-03 | CAD/CAM programming workstation | On-premises desktop | Yes | CUI Asset | CAM software, synced copies of job folders, NC programs. Runs the DNC (program transfer) software for 3 machines. **Not encrypted; CNC Programmer has local administrator rights** |
| SYS-04 | Quality PC with CMM software, and the CMM | On-premises | Yes (models, inspection programs) | PC: CUI Asset. CMM: Specialized Asset (test equipment) | **Shared "QC" login** used by the Quality Inspector and the Lead Machinist. Not encrypted |
| SYS-05 | 2 laptops (President, Office Manager) | Mobile | Yes (suite sync, portal downloads) | CUI Assets | Built-in full-disk encryption on; FIPS mode not confirmed |
| SYS-06 | 5 CNC machines | On-premises | Yes (NC programs) | Specialized Assets (operational technology) | 3 newer machines receive programs over the network from SYS-03; **2 older machines are loaded by USB drive**. Controllers run vendor-embedded software the company cannot patch |
| SYS-07 | Shop network: small-business firewall, one switch, staff Wi-Fi, guest Wi-Fi, shop-floor printer, hosted VoIP desk phones | On-premises, MSP-managed | In transit; printer handles CUI | Firewall: Security Protection Asset. Printer: CUI Asset | **Flat network**: office, CAM, quality, CNC machines, printer, and phones on one subnet. Guest Wi-Fi is separate. Staff Wi-Fi shared key unchanged since 2023 |
| SYS-08 | MSP tools: remote monitoring and management (RMM) agent and console, antivirus console, cloud backup service | MSP-operated SaaS | Security Protection Data; **backup copies hold CUI** | Security Protection Assets (ESP services) | The commercial cloud backup takes nightly images of SYS-03 and SYS-04 (30 days kept). **That backup cloud is not FedRAMP authorized** (DFARS 252.204-7012(b)(2)(ii)(D)) |
| SYS-09 | Job-shop ERP (quotes, orders, routings, purchasing, invoicing) | Commercial SaaS | FCI (DoD purchase order data); **drawing PDFs attached to 31 job records** | Intended Out-of-Scope; scoping position open | Routings should reference drawing numbers only |
| SYS-10 | Customer portals: Prime A supplier portal; Supplier B sends files by email | Customer-hosted | Yes | External systems | Prime A portal uses named accounts with the prime's MFA |
| SYS-11 | Payroll service and accounting SaaS | Commercial SaaS | No | Out-of-Scope Assets | Employee personal information (Florida breach law applies) |
| SYS-12 | Generative AI | Public chatbots (observed); CUI suite assistant (proposed) | Yes if used with engineering data | CUI Asset if enabled in SYS-01 | See P10 |

**SSP system (P02):** the *CUI Machining Enclave (CME)*: SYS-01, SYS-03, SYS-04, SYS-05, SYS-06 and the CMM (as Specialized Assets), SYS-07, and the MSP services in SYS-08 that protect them, plus printed CUI and the shop areas that handle it. SYS-02 and SYS-09 are outside the intended boundary but hold CUI today (scoping gap).

## 4. Current security posture: informal, basic hygiene, big gaps

**In place today:**
- CUI suite in a government-community cloud offering that is FedRAMP authorized at Moderate or higher (since 2026-03-09), with MFA for its 4 users
- MSP patching, antivirus, firewall, and nightly backups
- Laptop full-disk encryption
- DDTC registration; U.S.-person status recorded at hire for every employee
- Prime A portal access with named accounts and the prime's MFA
- Locked building with an alarm; keys held by the President, Office Manager, and Lead Machinist
- Guest Wi-Fi separated from the staff network
- A cyber liability insurance policy with a breach hotline and panel vendors

**Missing:**
1. No system security plan (3.12.4). The SPRS score of **110** posted on 2025-12-15 came from the President answering a checklist "yes" to every item, with no SSP or evidence behind it.
2. CUI outside the enclave: Supplier B emails drawings to the commercial orders mailbox (SYS-02); old job folders with drawings remain in SYS-02; drawing PDFs are attached to 31 ERP job records (SYS-09).
3. The MSP's commercial cloud backup holds nightly images of the CAM workstation and quality PC, which contain CUI, and is not FedRAMP authorized (252.204-7012(b)(2)(ii)(D)).
4. Flat network: CNC machines, the CAM workstation, office PCs, the printer, and phones share one subnet (3.13.1, 3.13.6).
5. Unencrypted desktops, local administrator rights for the CNC Programmer, and a shared "QC" login on the quality PC (3.13.16, 3.1.5, 3.5.1).
6. USB drives load programs into the 2 older CNC machines with no media control (3.8.7, 3.8.8).
7. Printed drawings and setup sheets at the machines are not marked or controlled, and scrap copies go in the general trash (3.8.3, 3.8.4).
8. No incident response plan, no DoD-approved medium assurance certificate, and no DIBNet access (3.6.1, 3.6.2; 252.204-7012(c)).
9. Logs are kept at vendor defaults and never reviewed (3.3.1 to 3.3.5).
10. No vulnerability scanning (3.11.2).
11. No security training after the hire orientation; no CUI or insider threat training (3.2.1 to 3.2.3).
12. Visitors (machine tool service engineers, customer auditors) are not logged or escorted consistently. A foreign-national service engineer worked at a machine with a drawing posted on it in May 2026 (3.10.3 to 3.10.5; ITAR release risk, 22 CFR 120.56).
13. The MSP relationship is undocumented for CMMC: no responsibility matrix, a shared MSP administrator account, and U.S.-person status of MSP technicians not confirmed (32 CFR 170.19(c)(2)(ii)).
14. No written policies; a purchased template set was never adopted.
15. The CNC Programmer pasted text from a Prime A specification into a public generative AI chatbot (P10).

## 5. Scenario choices

| Deliverable | Choice |
|---|---|
| Primary system (P02) | The registry default is a "CUI engineering enclave (CAD/PLM)". A 7-person shop has no PLM: the controlled job folders in the CUI suite (SYS-01) and the CAM workstation (SYS-03) do that job. The system is therefore named the **CUI Machining Enclave (CAD/CAM)** |
| P08 incident | Exfiltration of CUI: an attacker guesses the password of the shared orders mailbox in the commercial suite (SYS-02, no MFA), adds a forwarding rule, and receives Supplier B drawing packages for 3 weeks. The MSP and the cyber insurer are in the notification chain |
| P09 SOC 2 | Security plus Confidentiality readiness self-assessment for Customer C's supplier security questionnaire, plus a review of the MSP's SOC 2 Type 2 report. CMMC remains the primary assurance mechanism |
| P10 AI | Generative AI assistant used with CUI engineering documents: the CUI suite's integrated assistant (proposed) and public chatbots (prohibited) |
| Cloud (P04) | SaaS plus one cloud workload: the CUI suite and commercial SaaS, plus the MSP-operated cloud backup. Vendor-agnostic; AWS, Azure, and Google Cloud equivalents are listed only to help read documentation |

## 6. Assessment calendar (fictional unless a regulation is cited)

| Date | Event |
|---|---|
| 2025-12-15 | SPRS Basic Assessment score of 110 posted (President's checklist self-assessment) |
| 2026-03-09 | CUI suite (SYS-01) live |
| 2026-06-15 | Prime A notice: CMMC Level 2 (Self) for purchase orders issued from 2027-04-01 |
| 2026-07-06 | Office Manager designated Security and Compliance Coordinator |
| 2026-07-13 to 2026-07-24 | BIA, risk assessment, and gap analysis with the MSP lead technician |
| 2026-08-10 to 2026-08-12 | Control assessment by the independent consultant (on site 2026-08-11) |
| 2026-08-31 | Deliverables approved by the President |
| 2026-09-30 | Corrected SPRS score due |
| 2026-11-10 | CMMC Phase 2 begins (32 CFR 170.3(e)(2)) |
| 2027-03-15 | Target: Level 2 self-assessment complete, results and affirmation in SPRS |
| 2027-04-01 | Prime A purchase orders require CMMC Level 2 (Self) |

## 7. Facts added while building the deliverables

| Topic | Added fact | Used in |
|---|---|---|
| Machines | SYS-06: 3 networked machines (a 3-axis vertical machining center, a 5-axis machining center, a CNC lathe) and 2 older 3-axis vertical machining centers loaded by USB. The CMM is driven by the quality PC (SYS-04) | P02, P05 |
| Controlled files | About 900 controlled files in the SYS-01 job folders; a full copy syncs to SYS-03 | P05, P08 |
| Internet | One business internet line; no failover | P01, P05 |
| Cash | A cash reserve covers about 45 days of expenses; payroll runs weekly through the payroll service | P05 |
| Former employee | A part-time CNC programmer left on 2026-03-27. His commercial suite account and his Prime A portal access were still active when found on 2026-07-15; both were disabled that day. Sign-in logs showed no use after his last day | P01, P03, P07 |
| SYS-01 sync | The CUI suite's sync client runs on SYS-03, SYS-04, and both laptops | P02, P04 |
| President's phone | The President reads CUI suite email on his personal phone through the suite's mobile app, with no device management | P01, P03, P07 |
| SPRS legal advice | Counsel advised on 2026-07-28 that the 110 score must be corrected promptly, because knowingly keeping an inaccurate score could create False Claims Act exposure (31 U.S.C. 3729) | P01, P03 |
| Backup decision | On 2026-07-28 the President and counsel documented why the CUI in the commercial backup was treated as a compliance gap and not a cyber incident (no sign of unauthorized access; the backup sets are encrypted and access-controlled). Plan approved 2026-08-31: back up the SYS-01 job folders with a backup service inside the government-community offering, keep CAM workstation settings (post-processors, tool libraries) in a SYS-01 folder, then stop the commercial image backup of SYS-03 and SYS-04 by 2026-09-15 and obtain the backup vendor's deletion confirmation by 2026-09-30 | P01, P03, P04, P05 |
| Budget | Remediation budget approved by the President on 2026-08-31: about $36,000 one-time and $13,000 a year | P01 |
| P07 test details | MSP shared administrator account used by 3 technicians, its password unchanged since a technician left the MSP in May 2026 (changed 2026-08-12); one technician's RMM console login without MFA (MFA enabled 2026-08-12); 4 unlabeled USB drives at the older machines; printed drawings in the general trash on 2026-08-11; visitor log blank for 6 of 9 visits in June and July 2026; a laptop on staff Wi-Fi could open a CNC machine's file share; 4 of 5 employees interviewed could not say what CUI is | P01, P07 |
| Outside processors | 2 outside processors (anodizing and heat treat) receive parts with paper copies of the drawings. Their purchase orders use a commercial template without DFARS clauses | P01, P03 |
| Customer C questionnaire | Received 2026-07-08; response due 2026-09-30; Customer C accepts a self-assessment | P09 |
| MSP SOC 2 report | Type 2, 12 months ending 2026-04-30, reviewed 2026-08-20 | P09 |
| AI paste | On 2026-07-14 the CNC Programmer said he had pasted paragraphs of a Prime A material specification into a public chatbot in June 2026. Referred to the President (Empowered Official) and counsel on 2026-07-15 | P10 |
