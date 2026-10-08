# Scenario facts: Cris Santos Company | Professional, Scientific, and Technical Services | Small

All 10 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a regulation, IRS publication, or standard, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (a licensed CPA firm operating as a limited liability company) |
| Business | CPA and tax preparation firm (NAICS 541211). Individual and business income tax preparation and planning (about 65% of receipts), assurance services (financial statement audits, reviews, and compilations for private companies and nonprofits, about 25%), and client advisory services (about 10%) |
| Location | Florida. Two offices: the **Main office** (partners, tax and assurance teams, reception and document intake, IT) and the **Branch office** (about 20 miles away; tax team and seasonal preparers) |
| Workforce | 60 employees: 8 partners (CPAs), 18 tax professionals (including 2 enrolled agents), 14 assurance professionals, 4 client advisory staff, 11 client service and administrative staff (reception, document intake and scanning, e-file coordination, billing), and 5 operations staff (Firm Administrator, IT Manager, IT Support Technician, HR and Payroll Specialist, Marketing Coordinator). About 6 seasonal tax preparers join from January to April as temporary employees and are not counted in the 60 |
| Clients | About 4,600 individual income tax returns (Form 1040 series) a year, covering about 7,400 individual consumers (spouses on joint returns counted separately); about 1,150 business, trust, and exempt-organization returns; about 180 assurance engagements. About 9% of individual clients live outside Florida for part or all of the year |
| Customer information held | Records on about 21,000 consumers: current clients plus former clients whose files are still in the document management system. Records go back to 2009 because no disposal schedule exists (see gap 8) |
| Revenue | $15.9 million a year (fictional), about $61,000 per business day on average; about 55% of annual receipts are billed between February and April. Under the SBA standard of $26.5 million for NAICS 541211, so SBA-small |
| GLBA status | **Financial institution under the FTC Safeguards Rule.** 16 CFR 314.2(h)(2)(viii) names "an accountant or other tax preparation service that is in the business of completing income tax returns." Individuals who become clients for tax preparation have a customer relationship (314.2(e)(2)(i)(H)). The firm maintains customer information on far more than 5,000 consumers, so the 314.6 exception does **not** apply |
| IRS status | Tax return preparer under IRC 7216 (26 CFR 301.7216-1(b)(2)); every preparer holds a PTIN. Authorized IRS e-file Provider acting as an Electronic Return Originator (ERO) with one EFIN; the Tax Partner is the e-file Responsible Official. Returns are transmitted through the tax software vendor, which is itself an Authorized IRS e-file Provider (transmitter and software developer) |
| Not in scope | HIPAA: the firm is not a business associate. It has no engagements that require it to receive PHI on behalf of a covered entity and its engagement acceptance procedure declines such work. FAR 52.204-21, DFARS 252.204-7012, and CMMC: no federal contracts or subcontracts. ABA Model Rules: not a law firm. SEC and PCAOB: no public company audit clients; not PCAOB-registered. SOC examinations: the firm's assurance practice does not perform SOC 1 or SOC 2 engagements. CIRCIA: proposed rule only. Payment cards: client payments run through the practice management vendor's hosted payment page and are out of scope |
| Professional standards | The AICPA Code of Professional Conduct confidentiality rule applies to the CPAs as a professional standard adopted through state licensing. It is noted but not assessed, because its text was not verified from the source for this sample |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notification and the data security and disposal duties in Fla. Stat. 501.171). Clients who live in other states are handled generically ("each state where affected individuals reside") |
| FAR overhaul clause numbers | Background fact, not scored in P03. Contracts awarded before the contracting agency adopted its FAR Part 40 class deviation keep the clauses this sample cites (FAR 52.204-21) until they are modified. New awards under the deviation carry FAR 52.240-93, which has the same 15 safeguarding requirements as FAR 52.204-21, and FAR 52.240-91, which replaces the separate Kaspersky, Section 889 and FASCSA reports with one report within 72 hours. Sources: SRC-FAR-RFO-PART40 |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Managing Partner (majority owner, Cris Santos) | Executive owner of the program; chairs the Partner Group; accepts High and Very High risks; senior member responsible for direction and oversight of the Qualified Individual |
| Partner Group (8 partners) | The firm's governing body for 16 CFR 314.4(i). Receives the Qualified Individual's written report at least annually |
| Firm Administrator | Runs firm operations; program owner day to day; approves policies; accepts Moderate risks; vendor contracts |
| IT Manager | **Qualified Individual** under 16 CFR 314.4(a), designated in writing 2026-06-15. Runs IT with the managed service provider |
| IT Support Technician | Help desk, endpoint builds, account changes |
| Tax Partner | Owns the tax practice and the tax preparation system; IRS e-file Responsible Official; owns the IRC 7216 consent process; business owner for AI-001 |
| Risk and Quality Partner | Professional standards, engagement acceptance, confidentiality and privacy lead; breach determinations with outside counsel; chairs AI use reviews |
| Assurance Partner | Owns assurance engagement files and the audit workpaper application |
| Client Services Supervisor | Reception, document intake and scanning, client portal administration, e-file coordination (acknowledgments, Form 8879 files) |
| HR and Payroll Specialist | Onboarding, seasonal hiring, terminations, training records |
| Managed service provider (MSP) | After-hours help desk, patching, firewall management, backup monitoring, endpoint detection and response (EDR) console. A service provider under 314.4(f) |

## 3. Systems

| ID | System | Hosting | Holds customer information? | Notes |
|---|---|---|---|---|
| SYS-01 | Professional tax preparation and e-file software | Vendor-hosted (SaaS) | Yes | System of record for returns. Vendor transmits returns to the IRS and states. Vendor has a SOC 2 Type 2 report (reviewed in P09). Includes an AI document-extraction feature in pilot (see SYS-11) |
| SYS-02 | Client document portal with e-signature | Vendor SaaS | Yes | Clients upload source documents, sign Forms 8879 and engagement letters, and download returns. Client MFA is optional (see gaps) |
| SYS-03 | Document management system (DMS) and audit workpaper application | Firm-managed workloads in SYS-04 | Yes | Scanned source documents, prior-year returns, and assurance workpapers back to 2009 |
| SYS-04 | Cloud tenant (IaaS/PaaS) | Public cloud provider (vendor-agnostic) | Yes | Hosts the DMS server and file storage, the audit workpaper application server, the remote access VPN gateway, and the backup vault |
| SYS-05 | Identity provider (single sign-on and MFA) | SaaS | No (identities only) | Protects SYS-01, SYS-02 staff accounts, SYS-06, SYS-07, and the cloud console |
| SYS-06 | Productivity suite (email, files, chat, calendar) | SaaS | Yes (in email and shared files) | Clients routinely email source documents; the main target of business email compromise |
| SYS-07 | Practice management, time and billing | Vendor SaaS | Yes (client list, engagement letters, invoices) | Includes the vendor-hosted payment page |
| SYS-08 | Office networks (Main and Branch) | On-premises | Yes (in transit) | Firewalls, switches, Wi-Fi; site-to-site VPN to SYS-04 |
| SYS-09 | Endpoints | On-premises and remote | Yes (cached) | 62 laptops, 12 desktops (reception, scanning, and seasonal stations), 4 multifunction printer-scanners, about 40 phones with the productivity suite app |
| SYS-10 | Payroll and HR SaaS | Vendor SaaS | Employee data only | Firm's own payroll |
| SYS-11 | Generative AI tools | Vendor SaaS | Yes, in pilot | (a) AI-001: the tax software's generative AI document extraction and return-drafting feature, pilot with 8 preparers since June 2026, which sends documents to the vendor's AI sub-processor; (b) AI-002: an enterprise generative AI assistant in the productivity suite, pilot with 15 users since May 2026 (see P10) |

**SSP system (P02):** the *Tax Preparation and Client Portal Platform (TPCP)*: SYS-01, SYS-02, SYS-03, SYS-04, SYS-05, SYS-06, SYS-08, SYS-09, and their interfaces to the IRS and state e-file systems through the tax software vendor.

## 4. Current security posture: partially compliant

**In place today:**
- MFA (push notification without number matching) for staff on the identity provider, email, tax software, portal staff accounts, and the cloud console
- Unique user accounts in every system; a PTIN for every preparer
- Full-disk encryption on all laptops
- Provider encryption at rest for SYS-01, SYS-02, SYS-06, and the cloud storage behind SYS-03
- EDR on all endpoints, managed by the MSP, with alerts watched during business hours only
- Daily backups of the DMS and audit workpaper servers to an immutable backup vault in a second region (in place since 2025); one restore test in 2025
- Firewalls at both offices and a site-to-site VPN to the cloud tenant; no inbound services exposed
- Annual security awareness training for all staff, delivered each December
- A shredding vendor that provides certificates of destruction for paper
- Engagement letters for every client, and IRC 7216 consent forms for the one routine third-party disclosure (release of returns to a client's lender on request)
- A Qualified Individual designated in writing (2026-06-15)
- A cyber insurance policy with a breach hotline and panel vendors
- Weekly check of returns filed per PTIN during filing season by the Client Services Supervisor

**Missing or weak, found in the 2026 assessments:**
1. The written information security program (WISP) is a 2023 adaptation of the IRS Pub. 5708 template that was never updated. No written risk assessment with the criteria in 16 CFR 314.4(b)(1) existed before this assessment.
2. No written incident response plan meeting 314.4(h). No data theft procedure for the IRS Stakeholder Liaison, state tax agencies, the FTC, or the next-business-day e-file security incident report (IRS Pub. 1345).
3. The Qualified Individual has never reported in writing to the Partner Group (314.4(i)).
4. Email is exposed to business email compromise: push MFA without number matching, legacy authentication still allowed for 4 shared service mailboxes, automatic forwarding to external addresses allowed, and no alerting on new inbox rules.
5. No penetration test has ever been performed, and vulnerability scanning is ad hoc (last scan 2025-03). The firm has no continuous monitoring that would replace them (314.4(d)(2)).
6. Client portal MFA is optional; about 38% of individual clients have turned it on. Staff email returns and source documents to clients as unencrypted attachments on request.
7. The 12 desktops (reception, scanning, and seasonal stations) are unencrypted, and the multifunction printer-scanners keep scanned images on internal drives.
8. No data retention and disposal schedule. Client files go back to 2009, so the two-year disposal requirement in 314.4(c)(6) is not implemented.
9. No service provider inventory or periodic assessment. The MSP contract has no security requirements. The tax software vendor's SOC 2 report was first reviewed in 2026.
10. No documented change management procedure (314.4(c)(7)).
11. Seasonal staff accounts are disabled an average of 6 business days after the season ends; there is no quarterly access review; 3 partners use global administrator rights on their everyday productivity suite accounts.
12. Activity in the tax software and the DMS is logged but never reviewed, and bulk exports raise no alert (314.4(c)(8)).
13. No call-back verification when a client asks by email to change the refund direct deposit account, or when a vendor asks to change payment details.
14. No IRC 7216 consent covers disclosure to the AI extraction feature's sub-processor, and interviews found 3 staff members who pasted client notice text into public generative AI chatbots.
15. Training is annual only. There are no phishing exercises, and seasonal preparers start work before completing training.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 regulations | Primary: FTC Safeguards Rule, 16 CFR Part 314 (full rule; the 314.6 exception does not apply). Secondary: IRC 7216 and 26 CFR 301.7216-1 to -3, with the IRS e-file provider duties in Pub. 1345 and the WISP expectations in Pubs. 4557 and 5708 |
| P08 incident | Business email compromise of a tax manager's mailbox leading to theft of taxpayer data and an attempted refund diversion |
| P09 SOC 2 | The firm is not a service organization for its clients and does not perform SOC examinations. P09 is (a) a Security-only (CC1-CC9) self-benchmark, used to answer business clients' security questionnaires, and (b) a review of the tax software vendor's SOC 2 Type 2 report |
| P10 AI | Generative AI for tax and document preparation: AI-001 (tax software AI document extraction and return drafting) and AI-002 (enterprise AI assistant for client letters and notice responses) |
| Cloud | Vendor-agnostic. Services are described by category, with AWS, Azure, and Google Cloud equivalents noted only where needed for shared responsibility |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-07-13 to 2026-07-24 | Risk assessment and gap analysis fieldwork |
| 2026-08-03 to 2026-08-07 | Control assessment fieldwork |
| 2026-08-31 | Deliverables approved by the Firm Administrator (Moderate and below) and the Managing Partner (High) |
| 2026-10-20 | Qualified Individual's first written report to the Partner Group (after the October 15 extension deadline) |
