# Scenario facts: Cris Santos Company | Construction | Micro

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or standard, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (general contractor; privately held by its owner) |
| Business | Commercial and institutional building general contractor (NAICS 236220) focused on interior renovations and tenant improvements: medical and professional office build-outs, small clinic and school renovations, and accessibility upgrades. Self-performs carpentry, doors and hardware, and general conditions. Subcontracts every other trade (mechanical, electrical, plumbing, low-voltage, finishes) |
| Location | Florida. One leased flex-space **office** with a tool room and a small fenced storage yard, plus 3 to 4 active **jobsites** (4 in July 2026). Jobsites use a padlocked storage container and the superintendent's truck. There are no field office trailers |
| Workforce | 7 employees: the Owner and President, 1 Office Manager, 1 Project Manager and Estimator, 2 Superintendents, 2 Carpenters |
| Revenue | About $1.1 million a year (fictional), about $4,400 per business day. Under the SBA standard of $45.0 million for NAICS 236220 (13 CFR 121.201), so SBA-small |
| Billing and payments | Monthly progress payment applications (pay apps) with a schedule of values to each owner, about $92,000 billed a month in total. The largest single pay app in 2026 was $78,000. Private owners pay by ACH or check. The federal agency pays by electronic funds transfer to the bank account in the company's SAM registration (FAR 52.232-33(b)). The company pays about 25 active subcontractors and suppliers, about $55,000 a month, mostly by ACH. On a federal contract it must pay subcontractors within 7 days of receiving payment (FAR 52.232-27(c)(1)) |
| Federal work (about 30% of revenue) | **FC-1:** a Department of Veterans Affairs firm-fixed-price contract ($186,000, total small business set-aside, awarded 2026-03-16) to renovate exam rooms and restrooms for accessibility at a VA outpatient clinic in Florida. In progress; substantial completion planned 2026-11-30. It includes FAR 52.204-21, 52.204-25, 52.222-8 (weekly certified payrolls), and 52.232-33. The low-voltage subcontractor relocates 4 security cameras and adds a network video recorder in the renovated wing |
| Federal pipeline | A pre-solicitation notice (July 2026) for a DoD renovation of a dormitory day room and restrooms at a Florida Air Force installation (total small business set-aside, estimated $320,000) states that the solicitation, expected in October 2026, will require **CMMC Level 1 (Self)** through DFARS 252.204-7021. Award is expected in January 2027. The company must hold Final Level 1 (Self) and an affirmation in SPRS before award (32 CFR 170.15(b)). No CUI is expected |
| Private and state or local work (about 70%) | A physician group's medical office tenant improvement (largest job), a church education wing renovation, a county parks restroom renovation, and small retail build-outs |
| Insurance | General liability, builder's risk, and payment and performance bonds through a surety for public jobs. **Cyber policy:** $500,000 aggregate limit with a 24x7 breach hotline and panel vendors (breach counsel, forensics), and a **$25,000 social engineering (funds transfer fraud) sublimit** that applies only if the company verified the payment change by a call-back to a known number and kept a record |
| Not in scope | CUI and NIST SP 800-171 (no CUI held; the Owner decided on 2026-08-31 not to bid work that needs CUI). HIPAA (the company works inside medical offices but holds no PHI for clients). PCI DSS (no card payments accepted). SEC rules (privately held) |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notification, Fla. Stat. 501.171). The samples otherwise stay federal |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Owner and President (majority owner) | Approves policies and spending; accepts Moderate risks and approves treatment plans for High and Very High risks. Designated **CMMC Affirming Official** (32 CFR 170.22(a)(1)). SAM Entity Administrator; signs bids and federal representations. Releases (approves) every ACH batch and wire in the bank portal |
| Office Manager | **Designated security and compliance lead** (part-time, in writing on 2026-08-31). Bookkeeping: billing, accounts payable, the vendor list with bank details, and ACH batch preparation. Payroll and weekly certified payrolls; HR onboarding and terminations; the MSP contact |
| Project Manager and Estimator | Runs all projects; prepares pay apps in SYS-01 and emails them to owners; approves submittals; estimating and bids. Business owner of the AI estimating and bid assistant (P10). Adds and removes subcontractor users in SYS-01 |
| Superintendents (2) | Run the jobsites; daily logs and photos on the jobsite tablets; jobsite storage containers, keys, and visitors |
| Carpenters (2) | Self-perform work. No system accounts (paper time cards collected by the superintendents) |
| Managed service provider (MSP) | Help desk, patching, antivirus, firewall and Wi-Fi, productivity suite administration, and backup administration. Business hours, with an after-hours emergency line billed hourly. No 24x7 monitoring |
| Outside government contracts counsel | Reviews federal representations and affirmations on request (hourly) |

**Overlapping roles and how they are compensated.** The Office Manager is the security lead and also the person who edits vendor bank details and prepares payments. The Owner releases every payment and, from 2026-10, reviews a monthly vendor-change report (POL-02 A.6). The Owner both runs the company and accepts risk, so an independent consultant assesses the controls (P07) and the MSP supplies evidence rather than conclusions.

## 3. Systems

| ID | System | Hosting | Holds FCI? | Notes |
|---|---|---|---|---|
| SYS-01 | Construction project management and pay application platform (drawings, RFIs, submittals, daily logs, photos, pay app workflow, subcontractor portal) | Vendor SaaS | Yes | System of record for projects. Vendor has a SOC 2 Type 2 report (reviewed in P09). About 60 external subcontractor and design-team users. MFA is available but not enforced |
| SYS-02 | Small-business accounting with job costing (billing, accounts payable, vendor list with bank details, ACH file export) | Vendor SaaS | Yes (FC-1 pay apps and invoices) | Two users: Office Manager and Owner. Text-message MFA |
| SYS-03 | Payroll service with direct deposit | Vendor SaaS | Yes (certified payroll data for FC-1) | Employee Social Security numbers and bank accounts. Employee self-service for pay stubs and bank changes |
| SYS-04 | Productivity suite (email, calendar, file storage, shared drive) | SaaS | Yes | 5 named users (Owner, Office Manager, Project Manager, 2 Superintendents) with push-notification MFA. One shared "bids" mailbox signed in with a shared password and no MFA. No DMARC record. External auto-forwarding allowed |
| SYS-05 | Endpoints: 4 laptops, 1 office desktop (scanner and plotter host), 5 company smartphones, 2 jobsite tablets | Laptops and desktop MSP-managed; phones and tablets not managed | Yes | Laptops encrypted; desktop not encrypted; one tablet has no passcode |
| SYS-06 | Office network: small-business firewall and router, one Wi-Fi network, multifunction printer and plotter | On-premises, MSP-managed | Yes (in transit) | Visitors and subcontractors are given the office Wi-Fi password; there is no separate guest network |
| SYS-07 | Cloud backup of the productivity suite (email and files) | SaaS backup service, bought and run by the MSP | Yes | Daily, 30-day retention, one MSP administrator account. Never restore-tested. Does not cover SYS-01, SYS-02, or SYS-03 |
| SYS-08 | Bank business online banking (ACH and wires) | Bank-hosted | No | Office Manager initiates; Owner releases. One-time passcodes by text message |
| SYS-09 | AI estimating and bid assistant | Vendor SaaS (monthly subscription on a company credit card) | Yes (FC-1 change-order drawings uploaded) | Trial since 2026-06-01 by the Project Manager and Estimator. Standard terms allow customer data to be used to improve models (see P10) |
| SYS-10 | Federal portals (SAM.gov, the federal invoicing portal; SPRS not yet set up) | Government-operated | n/a | Owner's accounts through the government sign-in service, which enforces MFA. SAM holds the company's EFT (bank) information |

**SSP system (P02):** the *Project and Payment System (PPS)*: SYS-01 to SYS-07, with interfaces to SYS-08, SYS-09, and SYS-10. The PPS boundary is also the proposed CMMC Level 1 assessment scope (32 CFR 170.19(b)).

## 4. Current security posture: informal, basic hygiene, large gaps

**In place today:**
- Named productivity suite accounts with push-notification MFA for the 5 staff who use email
- MSP-managed antivirus with automatic updates, real-time scanning, and weekly full scans on the 4 laptops and the desktop
- Automatic operating system patching on the laptops and the desktop (MSP)
- Full-disk encryption on the 4 laptops
- Firewall with no inbound services open (MSP-managed)
- The Owner releases every ACH batch and wire in the bank portal; the Office Manager cannot release payments
- Daily cloud backup of email and files (SYS-07)
- Cyber insurance with a social engineering sublimit
- Keyed office with an alarm; locked tool room; jobsite storage containers padlocked after hours
- SAM.gov access through the government sign-in service, which enforces MFA
- A SOC 2 Type 2 report is available from the SYS-01 vendor

**Missing or weak, found in the 2026 assessments:**
1. No written security program, policies, or risk assessment, and nobody designated for security. IT decisions are made ad hoc by the Office Manager with the MSP.
2. No documented FCI scope, asset inventory, system security plan, or CMMC Level 1 self-assessment. Nobody has an SPRS account. The expected DoD award needs Final Level 1 (Self) first (32 CFR 170.15(b)).
3. Subcontractor and supplier bank-account changes are accepted by email and entered in SYS-02 by the Office Manager with no call-back. The Owner releases ACH batches without seeing which bank details changed. In May 2026 a spoofed supplier email asked for a bank change; it was caught only because the supplier's sales representative happened to call about another order.
4. Owners have never been told how the company changes its own remittance details. Pay apps go out as PDFs from the Project Manager's mailbox, with the company's bank details on the cover page.
5. The shared "bids" mailbox uses a shared password and no MFA. Push MFA is not phishing-resistant. There is no DMARC record, external auto-forwarding is allowed, and nobody reviews sign-in logs or new inbox rules.
6. MFA is not enforced in SYS-01. A Superintendent who left in April 2026 still had active SYS-01 and productivity suite accounts when found on 2026-07-21. Terminations are handled informally.
7. No written incident response plan. Nobody had the insurer's hotline number at hand, and the company does not keep the call-back records that its social engineering coverage requires.
8. No security awareness training. Payment fraud has never been covered.
9. Superintendents forward drawings, including FC-1 drawings, to personal email to print them at a print shop. The 5 phones and 2 tablets are not in device management, and one tablet has no passcode.
10. Visitors and subcontractors use the office Wi-Fi, which is the same network as the office computers and the printer.
11. No documented Section 889 "reasonable inquiry" (FAR 52.204-25(a)) and no screening of submittals for covered equipment. The SAM representations were renewed in March 2026 without a documented inquiry.
12. The subcontract template does not include the substance of FAR 52.204-21 or 52.204-25.
13. The email and file backup has never been restore-tested, SYS-01 project records are never exported, and the office desktop is not encrypted.
14. Three laptops retired since 2024 were given away or recycled with no wipe record.
15. The Project Manager uploads drawings to the AI estimating trial, including FC-1 change-order drawings (FCI) and private owners' drawings, under standard terms that allow model training. There is no approved-tools list.

**Found during the gap analysis (2026-07-28):** the FC-1 low-voltage subcontractor's submittal for a network video recorder and 4 cameras listed a private-label recorder whose actual manufacturer is a covered entity under FAR 52.204-25. The Project Manager had approved the submittal on 2026-06-10 without screening. The equipment had been ordered but not delivered or installed. The company rejected the submittal and cancelled the order on 2026-07-28. On counsel's advice, the Owner informed the FC-1 Contracting Officer in writing on 2026-07-29. The subcontractor's compliant resubmittal was approved on 2026-08-07.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 regulation | FAR 52.204-21 (15 basic safeguarding requirements), verified through CMMC Level 1 (Self) under 32 CFR Part 170 and DFARS 252.204-7021, plus FAR 52.204-25 (Section 889) as the secondary regulation. DFARS 252.204-7012 is analyzed for applicability only |
| P08 incident | Business email compromise redirecting progress payments (registry default, kept because it is the company's most likely costly incident): a phished Project Manager mailbox is used to send false remittance instructions to the medical office owner, and a spoofed supplier asks for a bank change. The MSP and the cyber insurer are in the notification chain |
| P09 SOC 2 | The company is not a service organization. (a) Security plus Confidentiality readiness self-assessment, used to answer a private hospital system's contractor security questionnaire (due 2026-10-15) before it releases facility drawings and security details; (b) review of the SYS-01 vendor's SOC 2 Type 2 report |
| P10 AI | AI estimating and bid assistant (registry default, kept because the trial is real and touches FCI): one user, the Project Manager and Estimator, on a monthly SaaS subscription |
| Cloud | SaaS plus one cloud workload: the SaaS backup of email and files (SYS-07), operated by the MSP. Vendor-agnostic |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-07-20 to 2026-07-31 | Risk assessment and gap analysis fieldwork (Office Manager with the MSP lead technician; Owner and staff interviews) |
| 2026-07-28 | FC-1 low-voltage submittal finding; submittal rejected and order cancelled |
| 2026-07-29 | Written notice to the FC-1 Contracting Officer |
| 2026-08-17 to 2026-08-19 | Control assessment by an independent consultant (on site 2026-08-18) |
| 2026-08-31 | Deliverables approved by the Owner |
| 2026-12-15 | Target date for Final Level 1 (Self) status and the SPRS affirmation |
