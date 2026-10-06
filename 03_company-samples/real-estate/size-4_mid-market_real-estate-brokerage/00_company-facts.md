# Scenario facts: Cris Santos Company | Real Estate and Rental and Leasing | Mid-Market

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or rule, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (privately held Florida corporation; private equity-backed; board with an audit committee; registered Florida real estate brokerage corporation) |
| Subsidiary and affiliate | **Cris Santos Title and Closing, LLC** ("Title and Closing"): a wholly owned Florida limited liability company, licensed title insurance agency, and settlement (closing) agent. Manager-managed by a 3-member board of managers. The parent company provides all IT, security, HR, and finance services to it under a 2022 intercompany services agreement. The company also holds a **49% interest in a mortgage brokerage joint venture** that an unaffiliated mortgage lender operates on its own systems and under its own security program |
| Business | Residential real estate brokerage (NAICS 531210) with four lines: (1) residential sales brokerage, (2) residential property management and leasing, (3) title and closing services through Title and Closing, and (4) referral, relocation, and ancillary services |
| Location | Florida only. Headquarters (executive offices, IT, finance, the title operations center, and the central property management office) and 22 sales offices in five Florida metropolitan areas. Title and Closing has closing rooms at headquarters and 8 of the sales offices. Property management has 3 regional leasing teams working from sales offices |
| Workforce | 600 employees: 18 executive and senior management; 26 sales management (4 regional managing brokers, 22 office managing brokers); 44 finance, accounting, and escrow accounting; 88 transaction coordination; 112 Title and Closing; 118 property management and leasing; 56 marketing, agent services, and recruiting; 48 inside sales and relocation (employed licensed agents); 24 IT and security; 22 HR, legal, and compliance; 44 office administration |
| Affiliated sales associates | About 1,650 licensed sales associates who are **independent contractors**, not employees. They work under the Broker of Record's supervision and use company systems (transaction management, email, CRM) from their **own devices**. About 410 left and 380 joined in the 12 months to 2026-06-30 |
| Revenue | $100.0 million in annual receipts (fictional): brokerage company dollar after agent splits $58.0 million; Title and Closing $24.0 million (settlement fees and retained title premium); property management fees $14.0 million; referral, relocation, and ancillary $4.0 million. About $400,000 per business day over about 250 business days. Above the SBA standard of $15.0 million for NAICS 531210 (13 CFR 121.201), so not SBA-small |
| Sales volume | About 12,600 closed transaction sides a year (about 50 per business day). The brokerage holds the earnest money deposit in its own **sales escrow account** in about 3,800 transactions a year (about $110 million a year in deposits); title companies or attorneys, including Title and Closing, hold the rest |
| Title and Closing volume | About 8,400 closings a year (about 34 per business day). About 62% are the brokerage's own transactions; the rest come from other brokerages, lenders, and a national homebuilder. About 35,000 outgoing disbursement wires a year (about 140 per business day), about $3.6 billion a year, from **title escrow trust accounts** at 2 banks |
| Property management | About 4,800 rental homes for about 3,300 owners. About 15,500 rental applications a year are screened. Rents (about $9.6 million a month) and security deposits (about $11 million held) are kept in **property management escrow accounts**. Owner distributions are paid by ACH each month |
| Consumers | Title and Closing holds customer information on about 98,000 consumers (closing files since 2019 in the title production software, plus scanned files from 2012 to 2018 on a headquarters file server). About 25% of buyers live outside Florida |
| Primary regulation | **FTC Safeguards Rule, 16 CFR Part 314 (N53-R01): applies to Title and Closing.** It provides real estate settlement services, which 16 CFR 314.2(h)(2)(x) names as a financial activity (12 CFR 225.28(b)(2)(viii)), as a regular, separately staffed business (24% of receipts). It holds customer information on more than 5,000 consumers, so the 314.6 exceptions are not available. The parent company's brokerage and property management lines are not financial activities (P03 section 1.1), but the parent handles Title and Closing's customer information as its **affiliate and service provider** (314.2(d), 314.2(r)), and the Qualified Individual is a parent employee, so 314.4(a)(1)-(3) applies. The company runs **one enterprise security program** for both entities. Full reasoning in P03 |
| Secondary rules (wire fraud anchor) | Florida broker escrow duties: Fla. Stat. 475.25(1)(d)1. and (1)(k), Fla. Admin. Code ch. 61J2-14 and r. 61J2-10.032. Title and Closing's trust funds: Fla. Stat. 626.8473. Florida data security and disposal duties: Fla. Stat. 501.171(2) and (8) |
| Not in scope | **FinCEN residential real estate reporting rule (31 CFR 1031.320):** vacated by the U.S. District Court for the Eastern District of Texas on 2026-03-19; FinCEN and the Department of Justice have appealed; no reports are required while the order stands (FinCEN website rechecked 2026-10-06). It would reach Title and Closing as settlement agent, not the brokerage (P03). **CCPA/CPRA (N53-R03):** receipts exceed the threshold, but the company has no California offices, employees, or marketing; General Counsel's 2025 position is that it is not doing business in California, reviewed each year; settlement data is GLBA data in any case (Civ. Code 1798.145(e)). **SEC disclosure (N53-R05):** privately held. **PCI DSS (N53-R04):** rent and application fee card payments run only through the property management platform's hosted payment page; the company stores, processes, and transmits no card data in its own systems. Noted, not assessed. **The mortgage joint venture** is a financial institution in its own right (314.2(h)(2)(xi)) but runs on the partner lender's systems and program; the company only sends it referred leads (P02 section 8) |
| State law approach | Florida law is cited only where a Florida duty is unavoidable: broker and title escrow (Fla. Stat. 475.25, 626.8473; ch. 61J2-14; r. 61J2-10.032), data security and breach notification (Fla. Stat. 501.171). For the 25% of buyers who live elsewhere, the samples apply "the law of each state where affected individuals reside" generically |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Board of directors, audit committee | Quarterly cyber risk reporting; receives the Qualified Individual's annual written report for the enterprise program |
| Title and Closing board of managers (Chief Executive Officer, Chief Financial Officer, President of Title and Closing) | Governing body of the financial institution for the annual report under 16 CFR 314.4(i) |
| Chief Executive Officer (CEO) | Accepts High risk; approves the risk appetite and the security budget |
| Chief Operating Officer (COO) | Executive sponsor of the security program; TMCC system owner; accepts Moderate risk |
| Chief Financial Officer (CFO) | Owns treasury and the banking relationships for all escrow and trust accounts; the Controller and the Title Escrow Accounting Manager report to the CFO |
| President, Title and Closing (licensed title agent) | Senior member of Title and Closing designated to direct and oversee the Qualified Individual (314.4(a)(2)); owns disbursement, wire release, and payoff verification procedures |
| Broker of Record (licensed broker; corporate officer) | Signatory on the sales escrow accounts; Florida Real Estate Commission duties, including escrow dispute notices (r. 61J2-10.032); supervises sales associates through the managing brokers |
| Virtual CISO (vCISO, part-time contractor) | Program strategy; board reporting support; security reviewer for AI use cases (P10) |
| IT Director | IT operations, infrastructure, the cloud landing zone, recovery, and the IT side of agent onboarding and offboarding |
| Security Manager | **Qualified Individual** (16 CFR 314.4(a)), employed by the parent company; runs security operations, vulnerability management, MSSP oversight, and GRC with 2 security analysts and 1 GRC analyst |
| General Counsel (also Chief Compliance Officer) | Breach and notification decisions; RESPA, Fair Housing, and FCRA compliance; contract terms with service providers |
| Controller | Sales and property management escrow records and monthly reconciliations (r. 61J2-14.012); commission disbursement |
| Title Escrow Accounting Manager | Daily and monthly reconciliation of the title escrow trust accounts |
| Director of Transaction Services | Transaction management platform (SYS-01) workflows; 88 transaction coordinators |
| Director of Property Management | Property management platform (SYS-10); tenant screening (P10 AI-001); property management escrow operations |
| Director of Leasing | Leasing teams; leasing assistant chatbot (P10 AI-004) |
| Director of Inside Sales and Relocation | CRM and buyer lead scoring (P10 AI-002); lead referrals to the mortgage joint venture |
| Director of Marketing | Websites; generative AI for marketing (P10 AI-003) |
| Director of Agent Services | Sales associate onboarding and offboarding records; agent training |
| Regional and office managing brokers (26) | Supervise sales associates; request onboarding and offboarding |
| HR Director | Employee onboarding, transfers, terminations, and training records |
| Co-sourced internal audit firm | Annual IT audit; P07 assessment. Reports to the audit committee |
| Managed security service provider (MSSP) | 24x7 EDR and SIEM monitoring. A service provider under 16 CFR 314.4(f) |

## 3. Systems

| ID | System | Hosting | Holds customer information or NPI? | Notes |
|---|---|---|---|---|
| SYS-01 | Transaction management platform (contracts, compliance review, document storage, agent and client portal) | Vendor SaaS | Yes | System of record for about 12,600 sides a year. Used by employees and about 1,650 contractor agents. Vendor SOC 2 Type 2 |
| SYS-02 | Title production and closing software (title orders, settlement statements, disbursement ledger, positive pay files) | Vendor SaaS | Yes | Used by 112 Title and Closing staff and title escrow accounting. Vendor SOC 2 Type 2; vendor states RTO 24 hours, RPO 1 hour |
| SYS-03 | Identity provider (single sign-on, MFA, conditional access) | SaaS | No (identities only) | Employees and contractor agents. About 2,300 active identities |
| SYS-04 | Productivity suite (email, files, chat) | SaaS | Yes | Email for employees and contractor agents. The main BEC target |
| SYS-05 | Cloud landing zone: 4 accounts (identity, shared services, workloads, backup) | Public cloud (vendor-agnostic) | Yes | Workloads: the **Closing Communications Portal** (company web application that delivers closing documents and wire instructions; built and maintained by a contract development firm), the integration service (syncs SYS-01, SYS-02, SYS-10, SYS-11, SYS-13), and the reporting data warehouse |
| SYS-06 | Office networks at 23 sites (headquarters and 22 sales offices) on SD-WAN | On-premises; SD-WAN managed service | Yes (in transit) | Includes the headquarters file server holding scanned closing files (2012 to 2018) |
| SYS-07 | Endpoints | Company-managed | Yes (cached) | 660 company laptops and desktops (including closing-room PCs) and 80 company phones. Contractor agents use about 3,000 personal laptops and phones |
| SYS-08 | SIEM operated by the MSSP | SaaS | Security logs | Receives identity provider, email, cloud, firewall, and EDR logs. SYS-01, SYS-02, and SYS-10 audit logs are not sent to it |
| SYS-09 | Commercial online banking and treasury platforms for the escrow, trust, and operating accounts | Bank-hosted (3 banks) | Yes | Sales escrow, property management escrow, and title escrow trust accounts; positive pay; ACH origination for owner distributions |
| SYS-10 | Property management platform with tenant portal, online rent payments, and integrated tenant screening | Vendor SaaS | Yes (consumer reports; bank data handled by the platform's payment processor) | P10 AI-001 |
| SYS-11 | CRM and lead management with buyer lead scoring | Vendor SaaS | Yes (contact and pre-approval data) | P10 AI-002; lead referrals to the mortgage joint venture by API |
| SYS-12 | E-signature service | Vendor SaaS | Yes | Integrated with SYS-01 and SYS-02 |
| SYS-13 | Accounting system (general ledger, commission and agent payouts) | Vendor SaaS | Limited | Agent payout bank details |
| SYS-14 | Third-party service providers | Various | Some | About 85 vendors; 42 are service providers with access to customer or consumer information |
| SYS-15 | AI tools | Vendors | Some | Tenant screening (AI-001), buyer lead scoring (AI-002), generative AI assistant (AI-003), leasing assistant chatbot (AI-004), identity verification for closings (AI-005) |

**SSP system (P02):** the *Transaction Management and Closing Communications System (TMCC)*: SYS-01 to SYS-08 and their interfaces to SYS-09 (banking) and SYS-12 (e-signature). Moderate baseline with High-integrity tailoring.

## 4. Current security posture: defined program with gaps in scale

**In place today:**
- A written information security program (2024) and five policies adopted in 2024; the Security Manager was designated Qualified Individual in 2024
- Annual risk assessment using NIST SP 800-30 (last done July 2025)
- MFA for all 600 employees through the identity provider; phishing-resistant security keys for the 46 staff who release or approve wires and for all administrators
- EDR on all company endpoints with 24x7 MSSP monitoring; SIEM for identity, email, cloud, firewall, and EDR logs
- Email security gateway; DMARC at reject on the company's main domain since 2025; external-sender banner
- The Closing Communications Portal is the only channel for wire instructions from Title and Closing (since 2023); a callback to a verified number is required before any outgoing title wire to a new payee or changed account; dual approval on all title trust account wires; positive pay on all escrow and trust accounts
- Monthly reconciliations of all escrow and trust accounts, signed by the Broker of Record (sales escrow) and the President of Title and Closing (title trust)
- Quarterly external vulnerability scans; annual external penetration test of the Closing Communications Portal (last 2025-11)
- Immutable backups of cloud workloads in a separate backup account
- Annual training and quarterly phishing simulations for employees
- Annual IT audit by the co-sourced internal audit firm
- Cyber insurance with a funds transfer fraud and social engineering sublimit

**Missing or weak, found in the 2026 assessments:**
1. Contractor agent MFA is incomplete. About 310 of the 1,650 agents (19%) still sign in to email and the transaction platform with a password only, under an exception that expired on 2026-06-30 (314.4(c)(5)).
2. Payee verification covers only Title and Closing's outgoing wires. Sales escrow refund wires need one approver and no callback; property owners can change payout bank accounts in the owner portal with no out-of-band check; agent commission payout account changes are accepted by email.
3. Application audit logs from SYS-01, SYS-02, and SYS-10 do not reach the SIEM, and nothing alerts on payee or bank-account changes in those systems (314.4(c)(8)).
4. Service provider oversight is thin. Of 42 service providers with customer or consumer information, 18 have security terms in their contracts, and SOC reports are reviewed only at onboarding. The intercompany services agreement between the parent and Title and Closing has no security terms (314.4(a)(3), (f)).
5. Recovery is unproven. The title production vendor's stated RTO (24 hours) exceeds the BIA need (4 hours). Email and transaction platform data have no independent backup. Only the Closing Communications Portal has a tested restore.
6. Access lifecycle gaps. Quarterly access reviews happen only in SYS-02. Departing contractor agents keep access for 6 days on average (up to 21) because managing brokers report departures late. SYS-01 uses office-wide visibility, so every agent can open every transaction in their office.
7. No retention and disposal schedule; customer information is kept indefinitely (314.4(c)(6)). The headquarters file server holds scanned closing files from 2012 to 2018 with broad staff access, and paper files remain at 4 offices.
8. The Qualified Individual's 2025 annual report went to the parent's audit committee, not to Title and Closing's board of managers, and it did not cover service provider arrangements or testing results (314.4(i)).
9. No AI governance. Five AI tools were adopted by departments without a security, privacy, or fair housing review. Tenant screening outcomes have never been tested for disparities.
10. The Closing Communications Portal has no secure development standard in the developer's contract, no automated code scanning, and informal change approval (314.4(c)(4), (c)(7)).
11. The 2024 incident response plan is generic. It has no funds recovery steps, the banks' fraud desk contacts are out of date, and it does not include the FTC notification process (314.4(h), (j)). The last tabletop exercise was in 2024.

## 5. Scenario choices

| Deliverable | Choice |
|---|---|
| P08 | **Two incident types:** (1) business email compromise targeting closing funds (registry default, kept: it is the top risk at this size); (2) ransomware with data theft at Title and Closing. Integrated with crisis management and legal |
| P09 | Readiness for a SOC 2 Type 2 examination of Title and Closing's closing and escrow disbursement services (Security, Availability, Confidentiality, Processing Integrity), requested by two lender clients and a national homebuilder; plus a vendor SOC 2 review program |
| P10 | AI use-case portfolio built around the registry default "Automated tenant and buyer screening": AI-001 tenant screening recommendations, AI-002 buyer lead scoring, AI-003 generative AI assistant for marketing, AI-004 leasing assistant chatbot, AI-005 identity verification for closings (kept and extended to a portfolio because the Mid-Market tier calls for one) |
| Primary system | Registry default kept: Transaction management and closing communications system |
| Cloud | Multi-account landing zone, vendor-agnostic. AWS, Azure, and Google Cloud names appear only in the P04 equivalents table |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-07-13 to 2026-08-07 | BIA, risk assessment, and gap analysis fieldwork |
| 2026-08-17 to 2026-09-04 | Control assessment fieldwork (co-sourced internal audit) |
| 2026-09-29 | Deliverables approved; results presented to the audit committee and to Title and Closing's board of managers |
| 2026-10-06 | FinCEN rule and HUD disparate impact proposals rechecked before publication |

## 7. Supporting details (fictional; used across P01-P10)

| Topic | Detail |
|---|---|
| Revenue per business day | Brokerage about $232,000; Title and Closing about $96,000; property management about $56,000; other about $16,000 |
| Money in motion | Title and Closing disburses about $14.4 million per business day. A typical buyer cash-to-close wire is $60,000 to $250,000; a typical payoff wire is $150,000 to $400,000 |
| Banks | Title trust accounts at 2 banks; sales escrow and property management escrow accounts at a third bank. All three offer positive pay and dual approval |
| Cyber insurance | $10 million aggregate limit, $250,000 retention, $1 million sublimit for funds transfer fraud and social engineering. The carrier's panel supplies breach counsel and forensics; notice through the carrier hotline comes before incident vendors are engaged. Title and Closing also holds closing protection letters from its title insurance underwriter |
| MSSP | 24x7 monitoring; must call the Security Manager within 30 minutes of a high-severity alert |
| Workforce activity | 96 employee terminations and 40 transfers in the 12 months to 2026-06-30; 410 agent departures and 380 agent onboardings. June 2026 employee phishing simulation click rate 6.1%; agents are not included in simulations |
| Fraud history | In the 12 months to 2026-06-30, staff stopped 37 attempted payee changes. One loss: in 2025-11 a seller's proceeds wire of $186,000 from the sales escrow account went to a fraudulent account after an agent's mailbox was taken over; $121,000 was recovered |
| Closing Communications Portal | About 28,000 buyer and seller accounts; MFA by one-time code to a phone number verified at contract |
| Intercompany agreement | 2022 intercompany services agreement; no security, confidentiality, or audit terms |
| Mortgage joint venture | Leads go from SYS-11 to the joint venture by API only after the buyer consents; Affiliated Business Arrangement Disclosure Statements are given at referral (12 CFR 1024.15(b)(1)) |
| SOC 2 driver | Two regional mortgage lenders and a national homebuilder (new-home closings in 2 Florida communities, about 900 closings a year) require a SOC 2 Type 2 report from Title and Closing by 2027 |
| Terminology | "Transaction Management and Closing Communications System (TMCC)" is the SSP system in P02, identifier CSC-TMCC-01 |
