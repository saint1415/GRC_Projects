# Scenario facts: Cris Santos Company | Construction | Small

All 10 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a regulation or standard, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (general contractor; privately held) |
| Business | Commercial and institutional building general contractor (NAICS 236220): new construction and renovation of offices, clinics, schools, and federal facilities. Self-performs concrete, carpentry, and general conditions. A small **technology and security systems group** installs structured cabling, network switches, video surveillance, and access control in client buildings |
| Location | Florida. One **main office** with an adjacent fenced **equipment yard**, plus **8 active jobsites**, each with a field office trailer |
| Workforce | 60 employees: 5 executives and directors, 12 project management staff (project managers, assistant project managers, project engineers), 9 superintendents and assistant superintendents, 4 estimators, 15 self-perform craft workers, 5 in the technology and security systems group, 9 accounting and administration staff, 1 IT Manager |
| Revenue | $27.0 million a year (fictional). Under the SBA standard of $45.0 million for NAICS 236220 (13 CFR 121.201), so SBA-small |
| Billing and payments | Monthly progress payment applications (pay apps) with a schedule of values to each owner, about $2.25 million billed a month. Private and state or local owners pay by ACH or wire. Federal agencies pay by electronic funds transfer to the bank account in the company's SAM registration (FAR 52.232-33(b)). The company pays about 120 active subcontractors and suppliers by ACH, about $1.6 million a month. On federal contracts it must pay subcontractors within 7 days of receiving payment (FAR 52.232-27(c)(1)) |
| Federal work (about 38% of revenue) | **FC-1:** VA outpatient clinic renovation (civilian agency). Substantially complete June 2026; contract open in the one-year warranty period. **FC-2:** GSA federal building HVAC and security upgrade (in progress). The security systems group installs cameras, access control, and network switches. **FC-3:** DoD (Army Corps of Engineers) barracks renovation task order at a Florida installation, under a small-business multiple-award task order contract awarded in 2024. All three include FAR 52.204-21 and FAR 52.204-25. FC-3 also includes DFARS 252.204-7012, but no covered defense information (CUI) has been identified or provided. None includes DFARS 252.204-7021 (CMMC), because they were awarded before CMMC Phase 1 began on 2025-11-10 |
| Federal pipeline | A DoD solicitation expected in 2026 Q4 (another Florida installation renovation) is expected to require **CMMC Level 1 (Self)**. A DoD design-build opportunity with CUI facility drawings would require Level 2; the President decided on 2026-08-31 **not to pursue CUI work before 2028** (see P03) |
| Private and state or local work (about 62%) | A private university science building, county school renovations, and a private hospital medical office building |
| Insurance | Cyber policy with $1 million aggregate limit and a $250,000 social engineering (funds transfer fraud) sublimit. Performance and payment bonds through a surety |
| Not in scope | CUI and NIST SP 800-171 (no CUI held; see P03 escalation plan). HIPAA (the company holds no PHI for clients). PCI DSS (no card payments accepted). SEC rules (privately held) |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notification, Fla. Stat. 501.171). The samples otherwise stay federal |
| FAR overhaul clause numbers | Background fact, not scored in P03. Contracts awarded before the contracting agency adopted its FAR Part 40 class deviation keep the clauses this sample cites (FAR 52.204-21 and 52.204-25) until they are modified. New awards under the deviation carry FAR 52.240-93, which has the same 15 safeguarding requirements as FAR 52.204-21, and FAR 52.240-91, which replaces the separate Kaspersky, Section 889 and FASCSA reports with one report within 72 hours. Sources: SRC-FAR-RFO-PART40 |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| President (majority owner, Cris Santos) | Accepts High and Very High risks. Designated **CMMC Affirming Official** (32 CFR 170.22(a)(1)) and signs SAM representations |
| Chief Financial Officer (CFO) | Executive owner of the security program; approves policies; accepts Moderate risks; owns treasury and payment controls |
| VP Operations | Owns project delivery, superintendents, and jobsite physical security |
| IT Manager | Security lead (part-time, alongside IT operations). Runs IT with a managed service provider; leads the CMMC Level 1 self-assessment and the SSP |
| Accounting Manager | Owns billing (pay apps), accounts payable, the ERP vendor master, and the bank portal administration |
| Contracts Administrator | Prime contracts, subcontract templates and flowdowns, SAM registration (Entity Administrator), Section 889 representations |
| Director of Preconstruction | Owns estimating and bidding; business owner of the AI estimating and bid assistant (P10) |
| Systems Integration Manager | Leads the technology and security systems group; product selection and Section 889 screening for installed equipment; custodian of client system credentials |
| Payroll and HR Specialist | Onboarding and terminations; weekly certified payrolls (FAR 52.222-8) |
| Project Managers (5) | Prepare pay apps and correspond with owners about payment |
| Superintendents | Jobsite trailer security, visitors, and jobsite devices |
| Managed service provider (MSP) | Help desk, patching, endpoint protection console, backup monitoring. Business hours plus on-call; no 24x7 monitoring |

## 3. Systems

| ID | System | Hosting | Holds FCI? | Notes |
|---|---|---|---|---|
| SYS-01 | Construction project management platform (drawings, RFIs, submittals, daily logs, pay app workflow, subcontractor portal) | Vendor SaaS | Yes | System of record for projects. Vendor has a SOC 2 Type 2 report (reviewed in P09). About 400 external subcontractor and design-team users |
| SYS-02 | Construction ERP and accounting (job cost, billing, accounts payable, vendor master with bank details) | Vendor SaaS | Yes | Generates pay apps and ACH payment files |
| SYS-03 | Payroll and HR with certified payroll reporting | Vendor SaaS | Yes (certified payrolls for federal jobs) | Employee PII: Social Security numbers, bank accounts |
| SYS-04 | Identity provider (single sign-on and MFA) | SaaS | No (identities only) | Push-notification MFA; protects SYS-01, SYS-02, SYS-03, SYS-05, SYS-06 |
| SYS-05 | Productivity suite (email, file storage, chat) | SaaS | Yes | Email is the channel for pay apps, lien waivers, and payment correspondence |
| SYS-06 | Cloud tenant (IaaS/PaaS) | Public cloud provider (vendor-agnostic) | Yes | Four workloads: BIM/CAD file server with GPU virtual desktops, estimating database (historical costs), an internet-facing **file-transfer portal** for design teams and subcontractors, and the backup vault |
| SYS-07 | Main office and yard network | On-premises | Yes (in transit) | Firewall, switches, Wi-Fi, site-to-site VPN to SYS-06. Jobsite trailers use cellular routers and reach SaaS directly |
| SYS-08 | Endpoints | On-premises and field | Yes | 44 laptops and 12 desktops (managed), 48 company smartphones (managed), **20 rugged jobsite tablets (not managed)**, **2 shared commissioning laptops (not managed)** |
| SYS-09 | Bank treasury portal (ACH, wires, positive pay) | Bank-hosted | No | Dual approval for wires over $50,000; ACH batches need one approver |
| SYS-10 | Equipment telematics | Vendor SaaS | No | Location and engine data for 35 pieces of heavy equipment |
| SYS-11 | Jobsite technology services (temporary cellular cameras, time-clock kiosks, drone photo service) | Vendor-operated | No | Out of the FCI scope; progress photos for federal jobs move to SYS-01 |
| SYS-12 | AI estimating and bid assistant | Vendor SaaS | Yes (uploaded bid documents) | Pilot since May 2026 with 4 estimators (see P10) |
| SYS-13 | Federal portals (SAM.gov, SPRS, federal invoicing portals) | Government-operated | n/a | Company accounts only. SAM holds the company's EFT (bank) information |

Client-installed systems (video surveillance, access control, building automation) are owned by clients. During installation and warranty the company holds their configurations and administrator credentials: **client facility security details**.

**SSP system (P02):** the *Project Delivery and Payment Platform (PDPP)*: SYS-01, SYS-02, SYS-04, SYS-05, SYS-06, SYS-07, SYS-08, and their interfaces to SYS-03, SYS-09, SYS-12, and SYS-13. The PDPP boundary is also the proposed CMMC Level 1 assessment scope (32 CFR 170.19(b)).

## 4. Current security posture: partially compliant

**In place today:**
- Unique named accounts in the identity provider for office and salaried field staff, with single sign-on to SYS-01, SYS-02, SYS-03, and SYS-05
- Push-notification MFA for all single sign-on users (except shared jobsite accounts)
- Role-based permissions in SYS-01 and SYS-02
- MSP-managed next-generation antivirus on laptops and desktops, with automatic updates, real-time scanning, and weekly full scans
- Automatic operating system patching on laptops and desktops; the MSP patches cloud virtual machines monthly
- Full-disk encryption on laptops and desktops
- Badge access and a reception visitor log at the main office
- Main office firewall with no inbound services exposed; cloud network rules
- Daily backups of SYS-06 workloads (same account and region as production)
- Dual approval in the bank portal for wires over $50,000; positive pay on checks
- Email filtering with an external-sender banner
- Cyber insurance with a social engineering sublimit
- SAM.gov access through the government sign-in service, which enforces MFA

**Missing or weak, found in the 2026 assessments:**
1. No documented FCI scope, asset inventory, or system security plan. No CMMC Level 1 self-assessment has been performed and nothing is in SPRS, which is required before award of the expected DoD contract (32 CFR 170.15(b)).
2. Subcontractor and supplier bank-account changes are accepted by email and entered in the ERP vendor master by one AP clerk, with no call-back to a known phone number and no second approver. Owners have never been told how the company will (and will not) change its own remittance details. A supplier bank-change email in March 2026 was caught only by chance.
3. MFA uses push notifications and is not phishing-resistant. There are no sign-in risk policies. Six shared jobsite trailer accounts are exempt from MFA. The company email domain has DMARC at monitor-only (p=none), and nobody watches for lookalike domains.
4. Security awareness is a 15-minute segment of the annual safety meeting. There are no phishing exercises and no payment-fraud training for Project Managers and accounting staff.
5. Nobody reviews identity provider sign-in logs, mailbox audit logs, or new inbox forwarding rules.
6. No written incident response plan. The March 2026 near miss was handled ad hoc and not recorded.
7. No documented Section 889 "reasonable inquiry" (FAR 52.204-25(a)) or submittal screening for covered telecommunications and video surveillance equipment. SAM representations were renewed without a documented inquiry.
8. Client facility security details (camera layouts, access control and building automation administrator credentials) sit in spreadsheets on the general file share, readable by all staff. The 2 shared commissioning laptops are unmanaged and unencrypted.
9. The internet-facing file-transfer portal sits in the same cloud subnet as the internal BIM/CAD file server.
10. The 20 rugged jobsite tablets are not in device management. Jobsite trailers keep no visitor log, and trailer keys and the yard gate combination are not inventoried or changed.
11. Field staff accounts are disabled up to 10 business days after termination. Subcontractor accounts in SYS-01 are never removed at project closeout (212 stale external accounts found).
12. Retired laptops and phones are wiped informally or given to employees, with no sanitization records.
13. SYS-06 backups sit in the same account and region as production and have never been restore-tested. There is no independent export of SYS-01 project records.
14. The subcontract template incorporates "all applicable FAR clauses" by reference but does not include the substance of FAR 52.204-21 or 52.204-25, as their flowdown paragraphs require.
15. Estimators upload federal bid documents and drawings (FCI) to the AI bid assistant pilot. The vendor's standard terms allow customer data to be used to improve its models. There is no approved-tools list.

**Found during P07 testing (2026-08-05):** the video surveillance system installed at the FC-1 VA clinic includes 2 network video recorders and 14 cameras sold under a distributor's private label that are produced by a covered manufacturer under FAR 52.204-25. The company reported to the Contracting Officer on 2026-08-06 (within one business day, FAR 52.204-25(d)(2)(i)) and filed the 10-business-day follow-up on 2026-08-19 (FAR 52.204-25(d)(2)(ii)). Replacement is scheduled at company cost.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 regulation | FAR 52.204-21 (15 basic safeguarding requirements), verified through CMMC Level 1 (Self) under 32 CFR Part 170, plus FAR 52.204-25 (Section 889) as the most relevant secondary regulation. DFARS 252.204-7012 is analyzed for applicability only |
| P08 incident | Business email compromise redirecting progress payments: a phished Project Manager mailbox is used to redirect an owner's pay app payment, and a spoofed subcontractor requests a bank change |
| P09 SOC 2 | The company is not a service organization. (a) Security-only (CC1-CC9) self-benchmark against the Trust Services Criteria; (b) review of the project management platform vendor's SOC 2 Type 2 report |
| P10 AI | AI estimating and bid assistant pilot (quantity takeoff, pricing, subcontractor bid leveling, proposal drafting) |
| Cloud | Vendor-agnostic. Services are described by category, with AWS, Azure, and Google Cloud equivalents noted only where needed for shared responsibility |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-07-13 to 2026-07-24 | Risk assessment and gap analysis fieldwork |
| 2026-08-03 to 2026-08-07 | Control assessment fieldwork (jobsite and main office walkthroughs 2026-08-05) |
| 2026-08-06 | Section 889 report to the FC-1 Contracting Officer |
| 2026-08-19 | Section 889 10-business-day follow-up report |
| 2026-08-31 | Deliverables approved by the CFO; High and Very High items approved by the President |
