# Scenario facts: Cris Santos Company | Professional, Scientific, and Technical Services | Mid-Market

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, IRS publication, or standard, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (privately held corporation; private equity-backed; board of directors with an audit committee; operates in an alternative practice structure with a separate CPA-owned attest firm) |
| Business | CPA, tax, and advisory firm (NAICS 541211). Individual and business tax preparation and planning (about 55% of receipts), assurance through the attest affiliate (about 22%), client accounting services (CAS: outsourced bookkeeping, bill pay, and payroll for business clients, about 13%), and advisory services (transaction advisory, valuation, and outsourced CFO work, about 10%) |
| Structure | **Alternative practice structure.** Cris Santos Company, Inc. (the Company) employs all staff, owns all systems, and delivers tax, CAS, and advisory services. Attest services (audits, reviews, compilations, and SOC 1 and SOC 2 examinations) are performed by **Cris Santos Assurance, LLP (the Attest Firm)**, a separately licensed CPA partnership owned by its CPA partners. The Attest Firm leases its professional staff from the Company and uses the Company's systems under an administrative services agreement. One security program covers both entities |
| Location | Florida. Headquarters (Office 1) and five other offices (Offices 2 to 6) across the state. The central document processing center (scanning and intake) is at Office 1. About 25% of staff work remotely, including 58 employees who live in 9 other states |
| Workforce | 600 employees: 70 principals and partners (including the Attest Firm's 26 partners), 210 tax professionals (including 14 enrolled agents), 105 assurance professionals, 70 CAS staff, 35 advisory staff, 55 client service and administrative staff, 28 IT, security, and GRC staff, and 27 finance, HR, marketing, and legal staff. From January to April the Company adds about 90 seasonal preparers and intake staff and about 40 interns as temporary employees, who are not counted in the 600 |
| Clients | About 38,000 individual income tax returns (Form 1040 series) a year, covering about 61,000 individual consumers (spouses counted separately); about 9,400 business, trust, and exempt-organization returns; about 1,050 attest engagements, including about 55 SOC examinations; CAS bookkeeping for about 340 business clients and payroll for about 210 business clients with about 8,600 client employees. About 19% of individual clients live outside Florida for part or all of the year |
| Customer information held | Records on about 205,000 consumers (current and former individual clients whose files go back to 2012). The DMS and CAS platform also hold personal information on about 90,000 other individuals (dependents, client employees in payroll and audit files) |
| Revenue | $100.0 million a year (fictional): tax $55 million, assurance $22 million (billed by the Attest Firm, with administrative service fees paid to the Company), CAS $13 million, advisory $10 million. About 250 business days a year, so about $400,000 per business day on average. About 50% of tax receipts are billed from February 1 to April 15. Above the SBA standard of $26.5 million for NAICS 541211 (13 CFR 121.201), so not small |
| GLBA status | **Financial institution under the FTC Safeguards Rule.** 16 CFR 314.2(h)(2)(viii) names "an accountant or other tax preparation service that is in the business of completing income tax returns." Individuals who become tax clients have a customer relationship (314.2(e)(2)(i)(H)). The Company holds customer information on far more than 5,000 consumers, so the 314.6 exception does **not** apply |
| IRS status | Tax return preparer under IRC 7216 (26 CFR 301.7216-1(b)(2)). Authorized IRS e-file Provider acting as an Electronic Return Originator (ERO), with one EFIN for each of its 6 offices. The Director of Tax Operations is the Responsible Official on all six. About 300 PTIN holders, including seasonal preparers. Returns are transmitted through the tax software vendor, itself an Authorized IRS e-file Provider |
| HIPAA status | **Business associate** for 44 health care clients: audits of hospitals and physician groups by the Attest Firm, revenue cycle advisory engagements, and CAS for 9 physician practices. Business associate agreements (BAAs) are on file for all 44. 45 CFR 164.302 makes the Security Rule apply to the Company and the Attest Firm for the ePHI they hold for these clients |
| Not in scope | FAR 52.204-21, DFARS 252.204-7012, and CMMC: no federal contracts or subcontracts. PCAOB: the Attest Firm is not registered and audits no issuers. SEC: the Company is private and is not a registered investment adviser. ABA Model Rules: not a law firm. CIRCIA: proposed rule only. Florida Digital Bill of Rights: a controller must exceed $1 billion in global gross annual revenue and meet one of three business tests (online advertising revenue, a smart speaker service, or an app store), so the Company is not a controller. Payment cards: client payments run through the practice management vendor's hosted payment page and are not assessed |
| Professional standards | The AICPA Code of Professional Conduct (confidential client information and independence, including the rules for alternative practice structures) applies to the CPAs and the Attest Firm as professional standards adopted through state licensing. They are noted but not assessed, because their text was not verified from the source for this sample |
| State law approach | Clients and remote staff are in many states. Florida law is the worked example (Fla. Stat. 501.171). Other states are handled generically: "each state where affected individuals reside" |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Board of directors (5 members: 2 private equity sponsor representatives, the Chief Executive Officer, and 2 independent directors) | The Company's governing body for 16 CFR 314.4(i). Receives the Qualified Individual's written report at least annually |
| Audit committee (the 2 independent directors and 1 sponsor representative) | Quarterly cyber risk reporting; oversees the co-sourced internal audit firm; approves the risk appetite |
| Chief Executive Officer | Accepts High risk; senior officer who oversees the Qualified Individual |
| Chief Operating Officer | Executive sponsor of the security program; accepts Moderate risk; owns business continuity |
| Chief Financial Officer | Cyber insurance; finance processes; payment controls |
| Chief Information Officer | Runs IT (infrastructure, service desk, applications); owner of shared infrastructure |
| Director of Information Security | **Qualified Individual** under 16 CFR 314.4(a), designated in writing on 2024-03-01. HIPAA Security Officer for the business associate work. Leads 3 security engineers and works with the MSSP |
| GRC Manager and GRC Analyst | Risk register, policies and standards, vendor reviews, evidence collection; report to the Director of Information Security |
| General Counsel | Legal; contracts; breach determinations with outside counsel; chairs the AI review group |
| Privacy Officer (reports to the General Counsel) | IRC 7216 consent program; HIPAA privacy for business associate work; privacy notices; decision log for breach determinations |
| National Tax Practice Leader | System owner of the tax platform; business owner of AI-001 and AI-003 |
| Director of Tax Operations | IRS e-file Responsible Official; document processing center; e-file; manages the offshore preparation support program |
| CAS Practice Leader | Owner of the CAS service (SOC 2 scope in P09) |
| Advisory Practice Leader | Advisory engagements |
| Attest Firm Managing Partner | Owner of attest engagements and the audit workpaper application |
| Attest Firm Quality and Independence Partner | Engagement acceptance, independence, and quality management; business owner of AI-004 |
| Chief People Officer | HR, seasonal hiring, training records; business owner of AI-005 |
| Director of Marketing and Communications | Client, staff, and media communications |
| Co-sourced internal audit firm | An unaffiliated CPA firm (not the Attest Firm). Annual IT audit; performed the P07 control assessment; reports to the audit committee |
| Managed security service provider (MSSP) | 24x7 monitoring of EDR and SIEM alerts; first containment. A service provider under 314.4(f) |
| Offshore preparation support vendor | About 30 vendor staff outside the United States who prepare first drafts of individual returns through firm-hosted virtual desktops. A tax return preparer located outside the United States for 26 CFR 301.7216 |

**Where roles overlap.** The Director of Information Security is both the Qualified Individual and the head of security operations, and the GRC Manager reports to that role. The program therefore depends on the co-sourced internal audit firm, which reports to the audit committee, for an independent check (P07).

## 3. Systems

| ID | System | Hosting | Holds customer information? | Notes |
|---|---|---|---|---|
| SYS-01 | Professional tax preparation and e-file software | Vendor SaaS | Yes | System of record for returns. Vendor transmits to the IRS and states; vendor SOC 2 Type 2. Includes the AI document extraction feature (AI-001) |
| SYS-02 | Client portal with e-signature and secure file exchange | Vendor SaaS | Yes | Uploads, Forms 8879, engagement letters, return delivery, IRC 7216 consents. Client MFA optional |
| SYS-03 | Document management system (DMS) | Firm-managed servers in SYS-04 | Yes | Scanned source documents, returns, and correspondence back to 2012 |
| SYS-04 | Cloud landing zone with 5 accounts | Public cloud (vendor-agnostic) | Yes | Management and security account, shared services (network) account, workloads account, restricted data enclave account, and backup account (see P04) |
| SYS-05 | Identity provider (SSO, MFA, conditional access) | SaaS | No (identities only) | MFA with number matching for all staff; privileged access management only for cloud administration |
| SYS-06 | Productivity suite (email, files, chat, calendar) | SaaS | Yes | Includes the enterprise generative AI assistant (AI-002) |
| SYS-07 | Practice management, time and billing, and CRM | Vendor SaaS | Yes | Hosted payment page |
| SYS-08 | CAS platform: cloud accounting, bill pay, and payroll processing services | Vendor SaaS | Yes | Used by CAS staff to run clients' books, payables, and payroll |
| SYS-09 | Audit and SOC engagement platform | Workpaper application in the workloads account; audit analytics in the restricted enclave | Yes | Used by the Attest Firm; client general ledger extracts and PHI samples. Includes the journal entry analytics tool (AI-004) |
| SYS-10 | Office networks (6 offices, SD-WAN) | On-premises | Yes (in transit) | Firewalls, Wi-Fi, site-to-cloud VPN |
| SYS-11 | Endpoints | On-premises and remote | Yes (cached) | 640 laptops, 110 desktops (scanning, reception, and seasonal stations), 26 multifunction printers, 18 high-volume scanners, about 520 phones enrolled in mobile device management |
| SYS-12 | Security tooling | SaaS and cloud | Logs only | EDR, SIEM operated by the MSSP, email security gateway, vulnerability scanner, SaaS discovery |
| SYS-13 | HR, firm payroll, and applicant tracking | Vendor SaaS | Employee and applicant data | Applicant tracking includes an AI resume-screening module (AI-005) |
| SYS-14 | AI tools | Various | Yes | AI-001 to AI-006 (P10) |

About 85 service providers hold or can reach customer information (P09 vendor program).

**SSP system (P02):** the *Tax and Client Data Platform (TCDP)*: SYS-01, SYS-02, SYS-03, SYS-04, SYS-05, SYS-06, SYS-10, SYS-11, and SYS-12, and their interfaces to the IRS and state e-file systems through the tax software vendor.

## 4. Current security posture: defined program with gaps in scale

**In place today:**
- A written information security program (WISP) adopted in 2024, with POL-01 to POL-05; the Qualified Individual designated in writing (2024-03-01)
- Annual written risk assessment (last completed July 2025)
- MFA with number matching for all staff on every federated system; legacy authentication blocked; external auto-forwarding blocked
- EDR on all managed endpoints, monitored 24x7 by the MSSP; SIEM collecting identity, email, EDR, firewall, and cloud logs
- Annual external and internal penetration test (last 2025-11) and quarterly authenticated vulnerability scans
- Full-disk encryption on all laptops; provider encryption at rest for every SaaS service and cloud storage
- Daily backups of SYS-03 and SYS-09 to an immutable vault in a separate backup account in a second region; DMS restore tested in 2025
- Annual security training and quarterly phishing simulations
- A first written report by the Qualified Individual to the board (2025-10)
- Cyber insurance ($15 million limit, $500,000 retention) with a breach hotline and panel vendors
- A records retention schedule (adopted 2024), engagement letters with IRC 7216 consent language, and BAAs with all 44 health care clients
- Weekly checks of returns filed per EFIN and per PTIN in filing season

**Missing or weak, found in the 2026 assessments:**
1. Mailbox takeover by token theft is not mitigated: there is no phishing-resistant MFA for partners, administrators, or finance staff, no device-compliance requirement for mail access, and inbox-rule alerts were suppressed by the MSSP during the 2026 filing season because of noise.
2. Client portal MFA is optional (about 58% of individual clients have enabled it), and staff still email returns and source documents as plain attachments on request.
3. Privileged access management covers only cloud administration. 14 IT staff hold standing directory or productivity suite administrator rights, and 9 service accounts have non-expiring passwords.
4. The offshore preparation program does not meet 26 CFR 301.7216-3(b)(4): SSNs are masked in the tax software but not in the scanned source documents that offshore staff open in the DMS, and 4 of 25 sampled offshore returns had no signed consent before disclosure.
5. Third-party risk: 31 of about 85 service providers have no security terms in their contracts; reviews happen only at onboarding; contractor staff with access have not received the written notice that 301.7216-2(d)(2) requires.
6. Activity in the tax software, client portal, DMS, and CAS platform is not sent to the SIEM, and bulk exports raise no alert (314.4(c)(8)).
7. The 2024 retention schedule has never been executed: client files older than the 7-year retention period, covering about 95,000 former-client consumers, are still in the DMS (314.4(c)(6)).
8. Change management covers infrastructure but not SaaS configuration: the tax practice turned on the tax software's AI drafting feature without review.
9. Recovery: no tested plan for a tax software vendor outage near a deadline; the CAS platform and payroll dependencies have never been exercised; the audit workpaper server restore is untested.
10. SaaS inventory is incomplete: SaaS discovery found 41 unapproved applications, 6 of them holding client data.
11. Seasonal workforce: 18% of seasonal staff got access before completing training, and seasonal accounts were disabled an average of 3 business days after their end date.
12. AI governance: no AI policy or review process; AI tools were turned on by practice leaders; SaaS discovery found client data pasted into public chatbots.
13. PHI from health care engagements sits in the general DMS and workpaper folders instead of a restricted area, and no HIPAA risk analysis covers it.
14. Policies exist, but supporting standards (configuration, logging, vendor risk, retention, AI) are thin or missing.
15. The 2025 report to the board did not cover service provider oversight or penetration test results, as 314.4(i)(2) expects.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 regulations | Primary: FTC Safeguards Rule, 16 CFR Part 314 (full rule; 314.6 does not apply). Also for the primary business line: IRC 7216 and 26 CFR 301.7216-1 to -3 (including the offshore rules), the IRS e-file provider requirements in Pub. 1345 and the WISP expectations in Pubs. 4557 and 5708, and Fla. Stat. 501.171(2) and (8). Secondary line: the HIPAA Security Rule (standard level) and 45 CFR 164.410 for the business associate work |
| P08 incidents | Two incident types: (1) business email compromise and taxpayer data theft (registry default), and (2) ransomware with data extortion during filing season, with a variant for a tax software vendor outage |
| P09 SOC 2 | Readiness for a SOC 2 Type 2 examination of the CAS service (Security, Availability, Processing Integrity, Confidentiality), requested by CAS clients and their auditors. The examination must be done by an unaffiliated CPA firm, not the Attest Firm. Plus a vendor SOC 2 review program |
| P10 AI | AI use-case portfolio: AI-001 tax software AI document extraction and drafting, AI-002 enterprise AI assistant, AI-003 AI tax research assistant, AI-004 audit journal entry analytics, AI-005 AI resume screening, AI-006 public chatbots (prohibited) |
| Cloud | Five-account landing zone, vendor-agnostic |
| Registry defaults | The primary system, the BEC incident, and the generative AI use case all fit a mid-market tax firm and were kept. At this size they were extended: a second incident type, and an AI portfolio instead of one use case |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-07-06 to 2026-07-31 | BIA, risk assessment, and gap analysis fieldwork |
| 2026-08-03 to 2026-08-21 | Control assessment by the co-sourced internal audit firm |
| 2026-09-22 | Deliverables approved by the Chief Operating Officer (Moderate and below) and the Chief Executive Officer (High and above); presented to the audit committee the same day (after the September 15 business-return extension deadline) |
| 2026-10-27 | Qualified Individual's annual written report to the board (after the October 15 extension deadline) |
| 2027-01-15 | Target for High-risk treatments that must be in place before the 2027 filing season |

## 7. Facts added during the build (fictional; used across P01 to P10)

These details were added so the deliverables could be specific. They do not change sections 1 to 6.

| Topic | Added fact |
|---|---|
| Offices and networks | Office 1 (headquarters) holds the document processing center (12 high-volume scanners) and has dual ISPs. Offices 2-6 have a single ISP with untested cellular failover at 3 of them. Network closets at Offices 4 and 6 use keys without a log. Pull printing exists at Offices 1-3 only |
| Remote staff | 58 employees live in 9 other states, including 4 in Colorado and none in California |
| Offshore program | About 30 vendor staff prepare about 5,500 individual return first drafts a season (about 15% of individual returns) through a firm-hosted virtual desktop pool launched in 2025-12. SSNs are masked in the tax software's offshore role but not in DMS images. The vendor holds an ISO/IEC 27001 certificate and has no SOC 2 report |
| Identity | 41 privileged accounts across all admin planes; 14 IT staff with standing directory or productivity suite admin rights; 9 service accounts with non-expiring passwords; 12 scanning stations share one local administrator password; break-glass accounts exist only for the cloud organization; about 220 high-risk users are due for security keys |
| Workforce activity | 96 terminations, 58 transfers, and 412 new accounts in the 12 months to 2026-06-30; 131 seasonal accounts ended in 2026-04 and 2026-05; June 2026 phishing click rate 6.1%; 96% of staff signed the annual acknowledgment; the security team is 4 people (the Director of Information Security and 3 engineers) |
| Testing and monitoring | Last penetration test 2025-11 (scope excluded the portal configuration, virtual desktops, and CAS tenant); 40 critical findings in Q1-Q2 2026, 6 fixed late; 31 configuration deviations on 12 sampled servers; 7 laptops with unapproved remote access tools; the MSSP suppressed inbox-rule alerts from 2026-02-02 to 2026-04-20; in 2026 the MSSP reported token-theft and help desk impersonation attempts against the Company that did not lead to data access |
| SaaS and change | SaaS discovery found 41 unapproved applications, 6 holding client data; 312 change tickets in 2026; the tax practice enabled the AI drafting feature in 2026-03 and it was used on about 2,100 returns until it was turned off on 2026-08-28; two software vendors use their own remote support tools |
| Data handling samples | About 4,800 outbound emails with tax attachments in a sampled March 2026 week (31 of 60 sampled unencrypted); about 1,900 lender and adviser releases a year (2 of 25 sampled preceded consent); 31 security incidents logged in 2025-2026; about 95,000 former-client consumers held past the 7-year retention period |
| Vendors | About 85 service providers: 14 Tier 1, about 40 Tier 2, the rest Tier 3; 31 have no security terms. Tax software vendor SOC 2: RTO 8 h, RPO 1 h, service degraded about 3 hours on 2026-04-14, 72-hour incident notice. Payroll service: SOC 1 and SOC 2 Type 2, RTO 4 h. Accounting service: RTO 24 h, RPO 4 h; bill-pay bridge letter overdue. Portal vendor: RTO 12 h. MSSP: no BAA |
| Contracts | 11 of the 44 BAAs set breach notice terms of 5 to 10 business days; the CAS agreement template sets a 72-hour incident notice; the Company has a credit agreement with lenders and a private equity sponsor operating partner |
| CAS operations | About 40 payroll runs per business day; about 2,600 vendor payments a week; second review documented for 15 of 25 sampled payrolls; 3 former CAS staff local accounts in the payroll and bill-pay services were found active on 2026-08-14 and disabled that day |
| AI tools | AI-001 extraction used on about 21,400 returns in 2026; AI-002 licensed to 250 users since 2026-04; AI-003 used by 120 tax professionals since 2026-06; AI-004 used on 140 engagements by 22 named analysts; AI-005 screened about 6,800 applicants in 2026 for 9 recruiters; AI-006 found in use by 9 staff (3 sanctioned) |
| Program history and budget | The 2025 risk register had 34 risks. FY2027 security plan approved 2026-09-22: $815,000 one-time (including $210,000 for SOC 2 readiness and the Type 2 examination) and $360,000 a year |
| Exercises and tests scheduled | Workpaper application restore test 2026-11-17; BEC tabletop with counsel 2026-11-19; deadline-week vendor outage tabletop 2027-01-12; ransomware executive tabletop 2027-02-24 |
| Terminology | "Tax and Client Data Platform (TCDP)" is the SSP system in P02, identifier CSC-TCDP-01. The Attest Firm is Cris Santos Assurance, LLP |
| Additional role titles | IT Operations Manager; security engineers (3); GRC Analyst; recruiters (9) |
