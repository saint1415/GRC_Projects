# Scenario facts: Cris Santos Company | Financial Services | Enterprise

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, a standard, or a card brand rule, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (publicly traded SEC registrant; a merchant payment processor) |
| Business | Payment processor serving merchants (NAICS 522320). It authorizes, clears, and settles card payments for about 410,000 merchants in all 50 states: card-present authorization for merchant terminals (including PIN debit), an e-commerce gateway and hosted payment pages, a token vault, merchant and partner portals with a virtual terminal, daily clearing and settlement, merchant funding, and chargeback handling. It also embeds payments in about 2,600 software platforms (independent software vendors, ISVs) and offers instant merchant payouts through a licensed subsidiary |
| Business segments | (1) **Merchant Acquiring** (core processing for about 360,000 merchants, including about 300 large enterprise merchants on a dedicated gateway); (2) **Integrated Payments** (about 50,000 merchants through 2,600 ISV partners); (3) **Payouts** (instant and same-day payouts to merchants' debit cards and bank accounts, run by the subsidiary Cris Santos Payouts, LLC); (4) Settlement and Treasury Operations; (5) Risk, Fraud, and Compliance; (6) Merchant Services (onboarding, underwriting, contact centers); (7) Corporate |
| Subsidiary with a New York license | **Cris Santos Payouts, LLC** (wholly owned) is licensed as a money transmitter by the New York State Department of Financial Services (NYDFS), so it is a **covered entity** under 23 NYCRR Part 500 (500.1(e)). It runs on the parent's shared information systems and has adopted the parent's cybersecurity program under 500.2(d). Its gross annual revenue was about $210 million in each of the last two fiscal years and the affiliates that share its systems have about 12,000 employees, so it is a **Class A company** (500.1(d)). It holds money transmitter licenses in other states where it offers the product; licensing itself is managed by Legal and is outside this security library |
| Location | Headquarters in Florida. Operations and contact centers in Florida and four other states. Company-operated data center **DC-1** in Florida (settlement and funding platform, payment HSMs, card network and bank connectivity) and a colocation data center **DC-2** in another state about 800 miles away (disaster recovery for DC-1). Two public cloud providers: **Cloud A** (authorization, portals, token vault, data and AI platform) and **Cloud B** (Integrated Payments and the payouts platform). Merchants and cardholders are in all 50 states. **State law is handled generically** ("each state where affected individuals reside") with Florida as the worked example |
| Workforce | 12,000 employees: about 4,100 in technology (2,900 engineering, 700 infrastructure and operations, 290 in the CISO organization, 210 data and AI), 3,800 in merchant services and contact centers, 1,600 in sales and partner management, 900 in risk, fraud, and compliance, 450 in settlement and treasury operations, and 1,150 in corporate functions. About 1,900 contractors also hold system access |
| Size | About $4.8 billion in annual receipts (fictional), about $13.2 million per calendar day. Not SBA-small (SBA standard for NAICS 522320: $47.0 million; 13 CFR 121.201). Revenue split: Merchant Acquiring about $3.3 billion; Integrated Payments about $1.1 billion; Payouts about $0.21 billion; other about $0.19 billion |
| Volume | About 13.8 billion card transactions a year (about 37.8 million a day; holiday peak about 6,500 per second) and about $780 billion in processed volume (about $2.1 billion of merchant funding per business day). About 58% card-present, 42% card-not-present. Integrated Payments carries about 19% of transactions |
| Ownership and governance | Publicly traded corporation (large accelerated filer). Board of directors with an **audit committee** (Internal Audit, SOX, disclosure controls) and a **risk and technology committee** (cybersecurity risk oversight, risk appetite). Not a bank and not a bank subsidiary |
| Sponsor banks | **Bank A**, a national bank supervised by the OCC (about 62% of volume; sponsor since 2012). **Bank B**, an FDIC-supervised insured state nonmember bank (about 23%; Integrated Payments merchants; since 2019). **Bank C**, a state member bank supervised by the Federal Reserve (about 15%; enterprise merchants and payouts settlement; **since 2026-03-01**). Each bank holds the card network memberships for its program, registered the company with the card brands as its third-party processor, and originates the merchant funding ACH files the company prepares. All three sponsor agreements state that the company's authorization processing, clearing, settlement, reconciliation, and merchant funding file services are performed for the bank and are subject to examination under the Bank Service Company Act, 12 U.S.C. 1867(c) |
| Contract commitments | Merchant agreements promise 99.99% monthly availability for authorization; ISV partner agreements promise 99.95% for the Integrated Payments API. Each sponsor agreement requires clearing files by the networks' cutoffs, merchant funding files by the bank's daily cutoff, and notice to the bank of any suspected account data compromise within 24 hours |
| PCI DSS status | **Service provider**, PCI DSS v4.0.1. Level 1 under Visa's service provider levels (more than 300,000 transactions a year; levels are set by the card brands, not PCI SSC). One Report on Compliance (ROC) by a Qualified Security Assessor (QSA) covers Merchant Acquiring, Integrated Payments, and Payouts, with an Attestation of Compliance (AOC) and quarterly external scans by an Approved Scanning Vendor (ASV). Last AOC: "Compliant", 2025-12-12. 2026 ROC fieldwork: 2026-10-19 to 2026-11-13; AOC due to the three sponsor banks by 2026-12-15. PIN debit acquiring is validated in a separate PCI PIN assessment (out of scope for this library) |
| GLBA status | A non-bank **financial institution** under the FTC Safeguards Rule, 16 CFR Part 314: data processing of financial data is an activity listed in 12 CFR 225.28(b)(14) and financial in nature under 12 U.S.C. 1843(k). It holds customer information of other financial institutions' customers (cardholders) (314.1(b)). Not eligible for the 314.6 exception. It has a board, so the Qualified Individual reports to the board (314.4(i)) |
| Bank service provider status | **Bank service provider** to Bank A under 12 CFR 53.2(b)(2) and 53.4 (OCC), to Bank B under 12 CFR 304.22(b)(2) and 304.24 (FDIC), and to Bank C under 12 CFR 225.301(b)(2) and 225.303 (Federal Reserve) |
| SEC status | Publicly traded SEC registrant: Form 8-K Item 1.05 (material cybersecurity incidents) and Regulation S-K Item 106 (17 CFR 229.106, annual disclosure in the Form 10-K) apply. SOX Section 404 IT general controls over financial reporting systems are tested by a separate SOX program |
| Other assurance | Annual SOC 1 Type 2 report on settlement and merchant funding controls (since 2019). Annual SOC 2 Type 2 report for the Integrated Payments platform (since 2024) |
| Not in scope | SEC Regulation SCI: not an SCI entity. NCUA 12 CFR 748.1(c): not a credit union. Interagency Guidelines (12 CFR 30 App. B; 12 CFR 208 App. D-2; 12 CFR 364 App. B): apply to the sponsor banks and reach the company through the sponsor agreements' service provider terms. ACH network rules: reach the company through the sponsor agreements and are tested by the banks; not analyzed here |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notification, Fla. Stat. 501.171). For cardholder data the company is usually a **third-party agent** of its merchants under 501.171(6) and the matching laws of other states; for merchant owner and workforce data it is itself the covered entity |

**Driver labels used in this folder.** The vertical requirement IDs (C-FINANCIAL-R01 to R06) are used wherever they apply, with the specific section, for example "C-FINANCIAL-R01 (12 CFR 53.4)", "C-FINANCIAL-R01 (12 CFR 304.24)", or "C-FINANCIAL-R05 (500.17(a))". PCI DSS, the FTC Safeguards Rule, and the SEC rules are not in the vertical requirements list, so rows cite them directly: "PCI DSS 8.4.2" (requirement number in PCI DSS v4.0.1), "16 CFR 314.4(c)(5)", "SEC Form 8-K Item 1.05", and "17 CFR 229.106".

**Registry defaults kept.** The primary system ("Payment processing platform (cardholder data environment)"), the P08 incident ("Compromise of payment processing environment"), and the P10 use case ("Transaction fraud-detection model") all fit this business at this size, so they are kept. At this size the primary system is the core platform across two data centers and a cloud (section 3), the P08 incident adds the SEC materiality step and bank, card brand, FTC, and NYDFS notices, and P10 covers the enterprise AI portfolio with the fraud model assessed in full.

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Board risk and technology committee | Oversees cybersecurity risk and the risk appetite; receives the CISO's quarterly report and the annual written Qualified Individual report (16 CFR 314.4(i)) |
| Board audit committee | Oversees Internal Audit, SOX, and disclosure controls; reviews the Item 106 disclosure draft |
| Chief Executive Officer (CEO) | With the CFO, accepts Very High risks; signs the NYDFS annual filing for the payouts subsidiary as its highest-ranking executive (500.17(b)(2)) together with the CISO |
| Chief Financial Officer (CFO) | Settlement and treasury; materiality determinations with the disclosure committee; joined 2026-05 |
| Chief Operating Officer (COO) | Business owner of Merchant Acquiring operations and settlement; **authorizing official** for the core platform (P02) |
| Chief Information Security Officer (CISO) | Program owner; **Qualified Individual** under 16 CFR 314.4(a); **CISO of the payouts subsidiary** under 23 NYCRR 500.4(a) (employed by the parent, an affiliate); assigned PCI DSS responsibility in the executive charter (PCI DSS 12.4.1) |
| Chief Risk Officer (CRO) | Enterprise risk management (ERM); owns the enterprise risk register; model risk management; chairs the AI and model risk committee |
| Chief Technology Officer (CTO) | Payment platforms and engineering; change management |
| Chief Information Officer (CIO) | Corporate IT, data centers, networks, and the enterprise platform (common control provider) |
| Chief Compliance Officer | Sponsor bank, card brand, and licensing compliance; second line with the GRC team |
| General Counsel | Chairs the disclosure committee; privilege; notices; law enforcement contact |
| Chief Audit Executive | Heads Internal Audit (third line); reports functionally to the audit committee; leads the P07 assessment |
| Chief Data and Analytics Officer | Data and AI platform; builds the fraud and risk models |
| GRC team (24), PCI program office (9), Cyber Fusion Center (24x7, 120 staff), Internal Audit (in-house IT audit team of 14, with a co-source firm for specialist skills) | Three lines model |
| Disclosure committee | Form 8-K materiality decisions (General Counsel chairs); members: CFO, Controller, CISO, Chief Risk Officer, Chief Compliance Officer, Vice President Investor Relations, Deputy General Counsel (securities), advised by outside securities counsel. Three of the eight members joined in 2026, including the CFO |

**Role overlap and compensation.** At this size the roles are separated on purpose. The one overlap is the CISO, who is both the Qualified Individual for the FTC Safeguards Rule and the CISO for the payouts subsidiary under Part 500; both duties report to the same board committee, so one report can serve both if it covers each rule's content. Internal Audit is independent of the controls it tests; its co-source firm, which helped build the Cloud A landing zone guardrails in 2024, was excluded from testing those controls in 2026 (P07).

## 3. Systems

| ID | System | Hosting | Card data? | Notes |
|---|---|---|---|---|
| SYS-01 | Authorization platform: authorization switch, terminal gateway (including PIN debit), e-commerce gateway, enterprise merchant gateway, token vault | Cloud A, CDE workload accounts in two regions (active-active) | **Yes (CDE)** | About 37.8 million authorizations a day |
| SYS-02 | Clearing, settlement, and merchant funding platform: clearing file builder, interchange and fee engine, reconciliation, funding file generation, chargeback system | DC-1 (mainframe plus 46 midrange batch servers); disaster recovery in DC-2 | **Yes (CDE)** | Legacy batch platform. 12 midrange servers run an operating system out of vendor support since 2025-10. Batch scheduler service accounts were not vaulted until 2026-08 |
| SYS-03 | Payment HSM estate | Company-owned payment HSMs in DC-1 and DC-2 (FIPS 140-3 Level 3 validated) and Cloud A's dedicated payment HSM service | Keys (including PIN keys) | Key hierarchy for PAN encryption, tokenization, PIN translation, and TLS keys. Dual control and split knowledge for key ceremonies |
| SYS-04 | Merchant and partner portals, virtual terminal, hosted payment pages | Cloud A, served through a content delivery service | **Yes (CDE)** | About 1.1 million merchant user accounts. Payment page script inventory and tamper-detection since 2025-03 |
| SYS-05 | Integrated Payments platform: partner APIs, hosted payment fields loaded in ISV checkouts, partner portal | Cloud B (6 accounts) | **Yes (CDE)** | Has its own SSP. SOC 2 Type 2 since 2024 (P09 SL-1) |
| SYS-06 | Payouts platform (Cris Santos Payouts, LLC) | Cloud B | Debit card tokens; merchant bank account data | Uses settlement outputs from SYS-02 to fund payouts |
| SYS-07 | Identity platform: workforce single sign-on, MFA, privileged access management (PAM), identity governance | SaaS plus DC-1 PAM vault | No | Phishing-resistant MFA for Cloud A and DC administrators; Cloud B engineers still use push-based MFA (gap) |
| SYS-08 | Cyber Fusion Center tooling: SIEM, EDR, network detection, web application firewalls, payment page tamper-detection, data loss prevention, PAN discovery | SaaS plus cloud and DC sensors | No (security service to the CDE) | 24x7, in house |
| SYS-09 | Engineering platform: source code repositories, CI/CD pipelines, artifact registry, infrastructure-as-code | SaaS plus Cloud A | No (can change CDE code) | About 2,900 engineers |
| SYS-10 | Bank and network connectivity: managed file transfer (MFT) appliances, card network interface processors, treasury workstations | DC-1, with standby in DC-2 | **Yes (clearing files carry PAN)** | Sends clearing files to the card networks and funding files to the three sponsor banks. The MFT software is from a third-party vendor |
| SYS-11 | Data and AI platform: data lake and warehouse, machine learning platform, model serving for the fraud models | Cloud A analytics accounts | Tokens by design; **PAN found in one table in 2026 (gap)** | Training data for AI-001 and AI-002 |
| SYS-12 | Merchant onboarding, underwriting, KYC, and CRM | SaaS | No card data; merchant owner NPI (SSNs, bank accounts, ID documents) | About 9,000 new merchants a month |
| SYS-13 | Contact centers and support: contact center platform with call recording, ticketing, website chatbot | SaaS | **Gap:** spoken card data in some call recordings | About 3,000 agents |
| SYS-14 | Corporate IT: about 16,000 endpoints, productivity suite, ERP and payroll (SOX-relevant) | SaaS plus offices | Incidental | |
| SYS-15 | Third parties: about 1,400 vendors, 96 of them PCI DSS service providers | Various | Various | Tiered third-party risk program |
| SYS-16 | AI portfolio (12 use cases) | Various | Various | Governed by the AI and model risk committee (formed 2025) |
| External | Sponsor banks A, B, and C; card networks (dedicated links from DC-1, DC-2, and Cloud A, provisioned under the banks' memberships); Cloud A and Cloud B providers; DC-2 colocation provider; content delivery service; MFT software vendor; QSA; ASV; SOC 1 and SOC 2 service auditor | | | |

**SSP system (P02):** the *Core Payment Processing Platform (CPPP)*: the cardholder data environment for Merchant Acquiring made up of SYS-01 to SYS-04 and SYS-10 across Cloud A, DC-1, and DC-2, plus the security-impacting and connected systems it inherits controls from (SYS-07, SYS-08, SYS-09, SYS-11) and the administrative access path from SYS-14.

## 4. Current security posture: mature, with residual gaps

**In place today:**
- A mature program aligned to CSF 2.0, with three lines of defense and an enterprise policy hierarchy (policies, standards, procedures, exceptions)
- Annual enterprise risk analysis tied to ERM (NIST IR 8286), reported quarterly to the board risk and technology committee
- Annual PCI DSS ROC; 2025 AOC "Compliant" (2025-12-12); quarterly ASV scans passing; semiannual segmentation tests
- PAN encrypted at rest (AES-256) with keys protected by payment HSMs; tokens returned to merchants and ISV partners; TLS 1.2 or higher on all external connections
- Workforce SSO with MFA; phishing-resistant security keys for Cloud A and data center administrators; PAM with session recording for Cloud A and the data centers; quarterly access certification
- 24x7 Cyber Fusion Center with SIEM, EDR on servers and endpoints, network detection, and payment page tamper-detection on the core hosted payment pages
- Active-active authorization across two Cloud A regions (failover tested 2026-02, met its 15-minute target)
- Immutable, write-once backups in separate cloud backup accounts; virtual tape replication from DC-1 to DC-2
- Tiered third-party risk program; annual SOC 1 Type 2 (settlement and funding) and SOC 2 Type 2 (Integrated Payments) reports
- Item 106 disclosure in the Form 10-K; annual written Qualified Individual report to the board; NYDFS certification of compliance for calendar year 2025 filed 2026-04-14
- AI and model risk committee (2025) with an inventory and independent validation of the in-house fraud model (2025-11)
- Cyber insurance tower of $150 million with a $25 million retention

**Residual gaps, found in the 2026 assessments:**
1. **Legacy settlement platform.** 12 of 46 midrange batch servers in DC-1 run an operating system out of vendor support since 2025-10 under compensating controls that are only partly documented. Batch scheduler service account credentials sat in plain text in job scripts until 2026-08 (found during P07). The DC-1 to Cloud A interconnect was re-architected on 2026-05-16 and the semiannual segmentation test found one unintended path (PCI DSS 11.4.6).
2. **Recovery objectives for settlement are not met.** The 2026-04-25 settlement disaster recovery test took 9.5 hours against a 6-hour RTO and would have missed Bank A's funding cutoff. No recovery test has involved the sponsor banks.
3. **Integrated Payments (Cloud B) identity.** 410 Cloud B engineers and operators use push-based MFA, not phishing-resistant authenticators; PAM covers 62% of Cloud B administrative roles; a CI/CD service account holds standing administrator rights.
4. **Third parties at scale.** 11 of 96 PCI DSS service providers lack a current AOC or responsibility matrix (12.8.4, 12.8.5). About 70% of authorization volume depends on one cloud provider. The MFT software is a single-vendor dependency on the settlement path.
5. **Bank C onboarding.** Bank C's designated points of contact for 12 CFR 225.303 notices are not loaded in the incident tooling, and the runbook's 4-hour determination step does not name Bank C's covered services.
6. **Materiality readiness.** The SEC materiality playbook was last exercised in 2025-06. Three of the eight disclosure committee members, including the CFO, joined in 2026 and have not taken part in an exercise. The NYDFS 72-hour notice is not built into the playbook's timeline.
7. **NYDFS Part 500 universal MFA and asset inventory.** Since the mainframe terminal emulator was replaced on 2026-02-09, about 340 settlement operators sign in to mainframe sessions inside DC-1 with a password only (the new emulator does not support the MFA plug-in), and the CISO has not approved compensating controls in writing (500.12(b)). Asset records lack support expiration dates or recovery time objectives for about 18% of assets (500.13(a)).
8. **PAN where it should not be.** Some contact center call recordings hold spoken card numbers when agents miss pause-and-resume. PAN discovery found about 410,000 full PANs in one data lake table in 2026-07 (purged 2026-07-29; notice analysis in P08 section 9).
9. **AI.** 12 AI use cases; 7 have completed committee review. The vendor merchant underwriting model has not been independently validated, and no fairness testing has been done on it.
10. **Independence and assurance gaps.** Internal Audit's co-source firm helped design the Cloud A guardrails it would otherwise have tested; the 2026 plan reassigned that testing to in-house auditors. The settlement service line (SL-2) has a SOC 1 report but no SOC 2 report, which two sponsor banks and the largest enterprise merchants now request.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P08 incident | **Compromise of the payment processing environment**: an attacker exploits a zero-day vulnerability in the third-party managed file transfer software (SYS-10) in DC-1, steals clearing files that carry full PANs and funding files with merchant bank account data, and then deploys ransomware on the settlement batch servers. Merchant funding files to all three sponsor banks are delayed past cutoff. The runbook includes the **SEC materiality assessment and Form 8-K Item 1.05** step, bank service provider notices to three banks, card brand, FTC, and NYDFS notices, and the multi-state third-party agent workflow |
| P09 SOC 2 | SOC 2 Type 2 readiness across two service lines: **SL-1 Integrated Payments platform** (existing Type 2 report; adding Processing Integrity) and **SL-2 Merchant processing and settlement services** (first SOC 2 Type 2, requested by the sponsor banks and enterprise merchants; SOC 1 Type 2 exists) |
| P10 AI | Enterprise AI portfolio (12 use cases) under the AI and model risk committee, with a full assessment of **AI-001 transaction fraud-detection model** (built in house; scores every authorization) |
| Cloud | Multi-cloud and hybrid, vendor-agnostic: Cloud A landing zone, Cloud B landing zone, DC-1, DC-2, and SaaS. Services are described by category, with AWS, Azure, and Google Cloud equivalents only in a reading table |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2025-12-12 | 2025 AOC "Compliant" issued |
| 2026-03-01 | Bank C sponsor agreement in effect |
| 2026-04-14 | NYDFS certification of compliance for calendar year 2025 filed by the payouts subsidiary |
| 2026-04-25 | Settlement disaster recovery test (9.5 hours against a 6-hour RTO) |
| 2026-05-16 | DC-1 to Cloud A interconnect re-architected (significant change) |
| 2026-06-01 to 2026-07-31 | Enterprise BIA, risk analysis, and gap analysis (GRC team, second line) |
| 2026-07-13 to 2026-08-28 | Control assessment fieldwork (Internal Audit, third line) |
| 2026-07-27 | PAN discovery finds full PANs in a data lake table (purged 2026-07-29) |
| 2026-08-12 | Assessors' stop-and-notify finding: batch scheduler credentials in plain text in settlement job scripts (P01 R-058) |
| 2026-09-08 | Executive risk committee approves the deliverables |
| 2026-09-10 | Results to the board audit committee and the risk and technology committee |
| 2026-09-14 | Core platform authorization decision (P02) |
| 2026-10-19 to 2026-11-13 | QSA ROC fieldwork for the 2026 PCI DSS assessment |
| 2026-12-15 | 2026 AOC due to the three sponsor banks |
| 2027-04-15 | NYDFS certification or acknowledgment for calendar year 2026 due (500.17(b)) |

## 7. Facts added during the build (fictional; used across P01-P10)
These details were added so the deliverables could be specific. They do not change sections 1-6.

| Topic | Added fact |
|---|---|
| Settlement timing | Clearing files go to each card network before its daily cutoff. Funding files are due at Bank A by 03:00, Bank B by 04:00, and Bank C by 05:00 Eastern. Each sponsor agreement lets the bank hold its ACH window open for up to 2 hours by agreement |
| CPPP components | About 1,900 authorization containers in two Cloud A regions; one mainframe in each data center; 46 midrange batch servers (12 unsupported); 16 company-owned payment HSMs plus the Cloud A payment HSM service; 4 MFT appliances; 6 card network interface processors; 24 treasury workstations |
| CPPP users | About 2,300 workforce accounts (212 privileged; about 340 settlement operators) and about 1.1 million merchant user accounts. 618 administrators hold CDE administrative access across all platforms |
| Workforce activity | 1,412 terminations of workforce with CDE access (1,180 employees, 232 contractors) and 1,830 hires in 2026-01-01 to 2026-06-30 |
| Data lake PAN event | A settlement extract wrote about 410,000 full PANs (no names, no security codes) to a data lake table from 2026-05-21; found 2026-07-27; purged 2026-07-29; notice analysis completed 2026-08-04; banks' compliance contacts told 2026-08-05 |
| Written approvals after fieldwork | On 2026-09-04 the CISO signed EXC-2026-017 (interim compensating controls for password-only settlement operators, as the written approval under 23 NYCRR 500.12(b) and, as Qualified Individual, under 16 CFR 314.4(c)(5)) and EXC-2026-019 (network detection in place of EDR on the MFT appliances, under 500.14(b)) |
| Key exchange | 41 enterprise merchants manage their own terminal keys and receive key exchange guidance (PCI DSS 3.7.9) |
| AI | The in-house fraud model (AI-001) has been built and run by the data science team since 2024 and is retrained monthly; it also scores instant payouts for the subsidiary |
| Insurance | Cyber insurance tower of $150 million with a $25 million retention; the carrier panel supplies breach counsel, forensics, and PFI options |

**Additional role titles used in the deliverables:** Executive Vice President, Merchant Acquiring (SL-2 owner); Executive Vice President, Integrated Payments (SL-1 owner); Senior Vice President, Core Payment Platforms (CPPP system owner); Senior Vice President, Settlement and Treasury Operations; Senior Vice President, Fraud and Risk Management (AI-001 business owner); Senior Vice President, Merchant Services; Senior Vice President, Partner Management; President, Cris Santos Payouts, LLC (senior member overseeing the CISO's work for the subsidiary under 500.4(a)(2)); Director of Security Operations (Cyber Fusion Center); Director of Identity and Access Management; Director of Cloud Platform Engineering; Director of Data Center and Network Engineering; Director of Infrastructure Engineering; Director of Developer Platform; Director of Settlement Systems; Director of Authorization Platform Engineering; Director of Cryptographic Services; Director of Third-Party Risk Management; PCI Program Director; Head of Model Risk Management; Controller; Chief Human Resources Officer; Vice President, Corporate Communications; Vice President, Investor Relations; Deputy General Counsel (securities).
