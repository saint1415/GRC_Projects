# Scenario facts: Cris Santos Company | Real Estate and Rental and Leasing | Enterprise

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or rule, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (publicly traded Florida corporation; SEC registrant, not a smaller reporting company; licensed real estate brokerage corporation in each state where it operates) |
| Subsidiaries and affiliates | **Cris Santos Title and Escrow, LLC** ("Title and Escrow"): wholly owned licensed title insurance agency and settlement (closing) agent, managed by a 3-member board of managers. **Cris Santos Relocation, LLC** ("Relocation"): wholly owned corporate relocation services company. A **49% interest in a mortgage brokerage joint venture** that an unaffiliated mortgage lender operates on its own systems and under its own security program. The parent company provides IT, security, HR, legal, and finance services to Title and Escrow and Relocation under a 2021 intercompany services agreement |
| Business | Residential real estate brokerage (NAICS 531210) with four lines: (1) residential sales brokerage, (2) title and settlement services through Title and Escrow, (3) single-family property management and leasing, and (4) corporate relocation services through Relocation |
| Location | Headquartered in Florida. About 410 sales offices in 9 states: Florida, Georgia, North Carolina, South Carolina, Tennessee, Texas, Arizona, Colorado, and California. Title and Escrow acts as settlement agent in Florida, Tennessee, Texas, Arizona, and Colorado (about 140 closing offices). In Georgia, North Carolina, and South Carolina it issues title policies as agent while independent closing attorneys conduct closings; in California, independent escrow companies handle escrow. **State law is handled generically:** "the law of each state where affected individuals reside", with Florida as the worked example |
| Workforce | 12,000 employees: 1,380 corporate (finance, legal, compliance, HR, internal audit); 860 technology, data, and security; 4,150 brokerage operations (460 managing brokers and sales managers, 1,850 transaction coordinators and office staff, 1,040 employed agents in inside sales and new-home sales, 800 marketing and agent services); 2,700 Title and Escrow; 2,210 property management and leasing; 700 Relocation |
| Affiliated sales associates | About 38,000 licensed sales associates who are **independent contractors**, not employees. They work under each state's broker of record and use company systems (transaction management, email, CRM) from their **own devices**. About 9,800 joined and 9,100 left in the 12 months to 2026-06-30 |
| Revenue | About $4.8 billion a year (fictional): brokerage gross commission income $3.92 billion (about $3.1 billion is paid out to agents as commission splits); Title and Escrow $410 million; property management $250 million; Relocation and ancillary services $220 million. About $19.2 million per business day over about 250 business days. Above the SBA standard of $15.0 million for NAICS 531210 (13 CFR 121.201) |
| Sales volume | About 210,000 closed transaction sides a year (about 840 per business day), about $96 billion in sales volume. The brokerage holds the earnest money deposit in its own **sales escrow accounts** in about 44,000 transactions a year (about $1.3 billion in deposits); title companies, closing attorneys, and escrow companies, including Title and Escrow, hold the rest |
| Title and Escrow volume | About 88,000 closings a year (about 350 per business day). About 55% are the brokerage's own transactions; the rest come from other brokerages, lenders, and homebuilders. About 380,000 outgoing disbursement wires a year (about 1,520 per business day), about $34 billion, from 31 **title escrow trust accounts** at 5 banks |
| Property management | About 21,000 single-family rental homes for about 9,500 individual owners and 2 institutional investors. About 64,000 rental applications a year are screened. Rents of about $48 million a month and security deposits are held in **property management escrow accounts**; owner distributions are paid by ACH |
| Relocation | About 280 corporate clients and about 16,000 relocating employees a year. Relocation administers home-sale and move programs that the corporate clients fund; it does not lend or extend credit |
| Consumers | Title and Escrow holds customer information on about 1.2 million consumers (closing files since 2014 in the title production platform, plus about 610,000 scanned files from acquired title agencies, 2009 to 2019, on colocation file servers). Buyers and sellers live in all 50 states; about 31% of buyers live outside the state of the property |
| Primary regulation | **FTC Safeguards Rule, 16 CFR Part 314 (N53-R01): applies to Title and Escrow.** It provides real estate settlement services, which 16 CFR 314.2(h)(2)(x) names as a financial activity (12 CFR 225.28(b)(2)(viii)), as a regular, separately staffed line of business. It holds customer information on more than 5,000 consumers, so the 314.6 exceptions are not available. The parent company's brokerage, property management, and relocation lines are not financial activities (P03 section 1.1), but the parent handles Title and Escrow's customer information as its **affiliate and service provider** (314.2(d), 314.2(r)) and employs its Qualified Individual, so 314.4(a)(1)-(3) applies. The company runs **one enterprise security program** for all entities. Full reasoning in P03 |
| Added at this size | SEC cybersecurity disclosure (Form 8-K Item 1.05; Reg S-K Item 106; N53-R05); California CCPA/CPRA and the 2026 CPPA regulations on cybersecurity audits, risk assessments, and automated decisionmaking technology (N53-R03); Colorado SB26-189 for tenant screening decisions made on or after 2027-01-01; SOX IT general controls; RESPA affiliated business arrangement disclosures (12 CFR 1024.15); growth by acquisition (9 brokerages and title agencies acquired in 2024-2026) |
| Not in scope | **FinCEN residential real estate reporting rule (31 CFR 1031.320):** vacated by the U.S. District Court for the Eastern District of Texas on 2026-03-19; FinCEN, with the Department of Justice, has appealed; reporting persons are not required to file while the order stands (FinCEN website rechecked 2026-10-06). It would reach Title and Escrow as settlement agent, not the brokerage (P03). **PCI DSS (N53-R04):** rent and application fee card payments run only through the property management platform's hosted payment page, and the company stores, processes, and transmits no cardholder data in its own systems; noted, not assessed. **The mortgage joint venture** is a financial institution in its own right (314.2(h)(2)(xi)) under its operating partner's program; the company sends it referred leads only |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Board of directors: risk committee and audit committee | Risk committee oversees cybersecurity risk (Item 106(c) governance) and approves the risk appetite. Audit committee oversees Internal Audit, SOX, and disclosure controls |
| Title and Escrow board of managers (Chief Financial Officer, General Counsel, President of Title and Escrow) | Governing body of the financial institution; receives the Qualified Individual's annual written report (16 CFR 314.4(i)) |
| Chief Executive Officer (CEO); Chief Financial Officer (CFO) | Accept Very High risk; take part in materiality determinations with the disclosure committee |
| Chief Operating Officer (COO) | Business owner for brokerage operations; authorizing official for the TMCC system (P02) |
| Chief Information Security Officer (CISO) | Program owner; reports to the CEO with quarterly reporting to the board risk committee. **Qualified Individual** for Title and Escrow (16 CFR 314.4(a)), employed by the parent company as Title and Escrow's affiliate |
| President, Title and Escrow (licensed title agent) | Senior member of Title and Escrow designated to direct and oversee the Qualified Individual (314.4(a)(2)); TMCC system owner; owns disbursement and payoff verification procedures |
| Chief Risk Officer | Enterprise risk management (ERM); owns the enterprise risk register |
| Chief Privacy Officer | Privacy program, CCPA compliance, breach determinations |
| General Counsel | Chairs the disclosure committee; outside counsel engagement |
| Chief Compliance Officer | Real estate licensing, RESPA, fair housing, and FCRA compliance; second line with the GRC team |
| Chief Audit Executive | Heads Internal Audit (third line); reports functionally to the audit committee; leads the P07 assessment |
| Chief Information Officer (CIO) | IT operations; owns the enterprise platform (common control provider) |
| Chief Data Officer | Chairs the AI governance committee (formed 2025) |
| Brokers of record (one per state; the Florida Broker of Record is the worked example) | Signatories on the sales escrow accounts; real estate commission duties, including escrow dispute notices |
| GRC team (10), Security Operations Center (24x7, in-house with a managed security service provider for overflow), Internal Audit (in-house, 32 staff including 9 IT auditors) | Three lines model |
| Disclosure committee | General Counsel (chair), CFO, Controller, CISO, Chief Privacy Officer, Chief Risk Officer, President of Title and Escrow, and Vice President, Investor Relations, advised by outside securities counsel. Decides Form 8-K Item 1.05 materiality |

## 3. Systems

| ID | System | Hosting | Holds customer information or NPI? | Notes |
|---|---|---|---|---|
| SYS-01 | Transaction management platform (contracts, compliance review, document storage, agent and client portals) | Vendor SaaS | Yes | System of record for all brokerage transactions. About 41,000 users (agents and staff). Vendor SOC 2 Type 2. Contract RTO 24 hours |
| SYS-02 | Title production and closing platform (title orders, settlement statements, disbursement ledger) | Vendor SaaS | Yes | Used by Title and Escrow for about 91% of closings; AQ-09 still uses its own legacy closing software (SYS-02L) |
| SYS-03 | Closing Communications Hub (company-built secure portal for buyers, sellers, lenders, and agents: wire instructions, payoff letters, closing documents, identity and payee bank account verification) | Cloud provider A | Yes | Built and run by the company's closing platform engineering team |
| SYS-04 | Disbursement Hub (company-built service that takes approved disbursements from SYS-02, applies dual approval and payee verification results, and sends payment files to the 5 trust banks; positive pay) | Cloud provider A | Yes | About 1,520 outgoing wires per business day |
| SYS-05 | Identity platform (single sign-on, MFA, conditional access, privileged access management, identity governance) | SaaS plus company-managed components | No (identities only) | About 52,000 identities: employees, contractor agents, and vendor accounts |
| SYS-06 | Productivity suite (email, files, chat) | SaaS | Yes | About 51,000 mailboxes in the enterprise tenant. **Three legacy tenants** at acquired brokerages AQ-06 to AQ-08 (about 2,900 agents and 260 employees). The main BEC target |
| SYS-07 | Multi-cloud estate (two public cloud providers, vendor-agnostic) plus 2 colocation data centers | Cloud provider A; Cloud provider B; DC-1 (Florida) and DC-2 (Texas) | Yes | Cloud A: TMCC workloads, integration platform. Cloud B: consumer website and app, CRM data, data warehouse, AI services. Colocation: legacy file servers with scanned closing files, network core, offline backup copies |
| SYS-08 | Enterprise network and offices | On-premises and SD-WAN | Yes (in transit) | SD-WAN at about 410 sales offices and 140 closing offices; office Wi-Fi; cloud-managed badge access and CCTV at offices |
| SYS-09 | Endpoints | Company-managed | Yes (cached) | About 14,500 company laptops and desktops with EDR. Contractor agents use their own laptops and phones through the browser, under conditional access (unmanaged devices) |
| SYS-10 | Property management platform with tenant portal, hosted rent payments, and integrated tenant screening | Vendor SaaS | Yes (consumer reports; card and bank data handled by the platform's payment processor) | AI-001 in P10 |
| SYS-11 | CRM and lead platform with buyer lead scoring and a buyer pre-qualification assistant | Vendor SaaS plus company models on Cloud B | Yes (contact, pre-approval, and preference data) | AI-002 in P10 |
| SYS-12 | ERP, payroll, and agent commission platform | Vendor SaaS | Limited (employee and agent pay data) | SOX-relevant; SOX IT general controls tested annually |
| SYS-13 | Relocation management platform | Vendor SaaS | Yes (relocating employees' personal and household data) | SL-2 service line (P09) |
| SYS-14 | About 1,400 third-party vendors (230 with customer information or other personal data) | n/a | n/a | Tiered third-party risk program |
| SYS-15 | AI portfolio (12 use cases) | Mixed | Mixed | Governed by the AI governance committee formed in 2025 |

**SSP system (P02):** the *Transaction Management and Closing Communications System (TMCC)*: the Closing Communications Hub (SYS-03) and the Disbursement Hub (SYS-04) on Cloud provider A, the company's tenant configurations of the transaction management platform (SYS-01) and the title production platform (SYS-02), and their interfaces to the trust banks and the e-signature service, inheriting common controls from SYS-05 to SYS-09.

## 4. Current security posture: mostly compliant, with targeted gaps

**In place today:**
- A mature program aligned to CSF 2.0, with a written FTC Safeguards Rule program for Title and Escrow and a Qualified Individual designated in writing (2022)
- Annual enterprise risk assessment tied to ERM (NIST IR 8286)
- A policy hierarchy of policies, standards, procedures, and exceptions
- 24x7 SOC with EDR, SIEM, and mailbox threat detection on the enterprise email tenant
- MFA for every employee and contractor agent (authenticator app push with number matching); phishing-resistant security keys for privileged users and for Title and Escrow staff who handle funds (since 2025)
- PAM and quarterly access certification for employees
- Wire instructions delivered only inside the Closing Communications Hub, with payee bank account ownership verification for about 86% of outgoing disbursements
- Dual approval on every wire from the enterprise title escrow trust accounts; positive pay on escrow and trust account checks
- DMARC at reject on the company's primary domains; look-alike domain monitoring and takedown
- Immutable backups and annual DR tests for tier-1 systems
- Annual penetration tests of internet-facing applications and continuous vulnerability scanning
- A tiered third-party risk program
- An annual SOC 2 Type 2 report for Title and Escrow's settlement services (since 2024)
- SEC Item 106 disclosure in the annual report on Form 10-K

**Targeted gaps:**
1. **Acquisition integration.** AQ-06, AQ-07, and AQ-08 (brokerages acquired 2025-2026) still run their own email tenants without the enterprise email security stack or SIEM mailbox audit feeds. AQ-09 (a Texas title agency acquired 2026-03) still runs its legacy closing software and its own trust accounts, with a single approver for wires below $100,000 and no payee bank account verification.
2. **Contractor agent identity.** The 38,000 contractor agents use push MFA that adversary-in-the-middle phishing kits can relay, from unmanaged devices. Departures reach identity governance only when a managing broker files a notice, so some departed agents keep access for days.
3. **Wire verification coverage.** Payee bank account verification covers about 86% of outgoing disbursements. Payoffs to lenders that do not use the portal, AQ-09, and some exchange accommodator disbursements rely on manual callback. Title and Escrow had 3 diverted-wire incidents in 2026 H1 ($1.2 million; $0.8 million recovered).
4. **Platform concentration.** The transaction management platform carries 100% of brokerage transactions and the title production platform about 91% of closings. Neither has a tested fallback beyond the vendor's own recovery, and the transaction platform's contract RTO (24 hours) exceeds the BIA RTO (8 hours).
5. **AI.** 12 AI use cases, but only 7 have completed AI governance committee review. Tenant screening is used in Colorado and California, where Colorado SB26-189 and the CPPA ADMT rules apply from 2027-01-01. Bias testing has been done only on vendor-supplied data.
6. **Materiality.** The materiality playbook and the 2025 disclosure committee tabletop covered ransomware only. There is no fraud-loss (BEC) scenario and no method for assessing a series of related incidents together.
7. **California cybersecurity audit.** The first CPPA cybersecurity audit report is due 2028-04-01 (audit period 2027), and risk assessments are needed for tenant screening and lead scoring.
8. **Legacy data.** About 610,000 scanned closing files from acquired title agencies (2009 to 2019) sit on colocation file servers with no retention review, and tenant screening reports are kept indefinitely in the property management platform.

## 5. Scenario choices

| Deliverable | Choice |
|---|---|
| P08 | Business email compromise targeting closing funds at enterprise scale: a coordinated campaign that relays MFA to take over agent and closer mailboxes, sends altered wire instructions and a spoofed payoff letter, and copies closing documents. Includes an **SEC materiality assessment and Form 8-K Item 1.05** step (with the "series of related occurrences" question), FTC Safeguards Rule notice, and a multi-state breach-notification workflow |
| P09 | SOC 2 Type 2 readiness across two service lines offered to business clients: SL-1 title and settlement services (lenders, other brokerages, homebuilders) and SL-2 corporate relocation services |
| P10 | Enterprise AI portfolio (12 use cases) with the AI governance committee operating model; full assessment of AI-001 automated tenant screening and AI-002 buyer lead scoring and pre-qualification |
| Cloud | Multi-cloud (vendor-agnostic) with common controls; AWS, Azure, and Google Cloud names appear only in an equivalents table |

The registry defaults (primary system "Transaction management and closing communications system", incident "Business email compromise targeting closing funds", AI use case "Automated tenant and buyer screening") fit this business at this size and are kept. At enterprise size the system is the company-built closing communications and disbursement layer that sits between the two vendor platforms, the incident is a multi-mailbox campaign that raises the SEC question, and screening becomes one part of an AI portfolio.

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-06-01 to 2026-07-31 | Enterprise risk assessment and regulatory gap analysis (evidence sampling completed 2026-08-14) |
| 2026-07-13 to 2026-08-28 | Control assessment (Internal Audit, third line) |
| 2026-09-04 | Assessment report issued |
| 2026-09-08 | Executive risk committee approves the register, treatments, and policies |
| 2026-09-10 | Results to the board risk committee and the audit committee |
| 2026-09-15 | Qualified Individual's annual report to the Title and Escrow board of managers |
| 2026-10-06 | FinCEN rule, HUD disparate impact proposals, and SEC rule status rechecked before publication |
