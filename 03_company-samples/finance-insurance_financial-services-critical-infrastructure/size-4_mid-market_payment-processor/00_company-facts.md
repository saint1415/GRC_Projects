# Scenario facts: Cris Santos Company | Financial Services | Mid-Market

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, a standard, or a card brand rule, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (a merchant payment processor; private equity-backed; board with an audit committee) |
| Business | Payment processor serving merchants (NAICS 522320). It authorizes, clears, and settles card payments for about 31,000 merchants in all 50 states: card-present authorization for merchant terminals, an e-commerce payment API with a hosted payment page, a token vault for recurring billing, a merchant portal with a virtual terminal, daily clearing and settlement, merchant funding, and chargeback handling. Since the November 2025 acquisition of a payment gateway it also runs an **Integrated Payments** business line that embeds payments in about 420 software platforms (independent software vendors, ISVs) |
| Business units | (1) Merchant Processing (core platform, about 22,000 merchants); (2) Integrated Payments (acquired gateway, about 9,000 merchants through 420 ISV partners); (3) Settlement and Treasury Operations; (4) Risk, Fraud, and Compliance; (5) Merchant Services (onboarding, underwriting, support, contact center); (6) Corporate (finance, HR, legal, IT, security) |
| Location | Headquarters and operations center in Florida. The Integrated Payments team works from the acquired company's office in another state. The core authorization platform runs in a public cloud landing zone (Cloud A). The settlement and funding engine and the company-owned payment HSMs run on premises in a leased colocation cage in Florida, with a disaster recovery cage in a second colocation facility outside Florida. The acquired gateway still runs in a different public cloud provider (Cloud B). Merchants are located in all 50 states. The processor is treated as a **national** business: state law is handled generically ("each state where affected individuals reside") with Florida as the worked example |
| Workforce | 600 employees: 38 executive and administration; 170 engineering (including 30 site reliability and platform engineers; 48 of the 170 are in Integrated Payments); 25 IT; 9 information security; 55 risk, fraud, and compliance; 45 settlement and treasury operations; 160 merchant services (onboarding, support, contact center); 60 sales and partner management; 8 data science; 30 finance, HR, and legal |
| Size | $100.0 million in annual receipts (fictional), about $274,000 per day. Above the SBA size standard of $47.0 million for NAICS 522320 (13 CFR 121.201), so **not SBA-small**. Revenue split: Merchant Processing about $68 million; Integrated Payments about $24 million; equipment, PCI program, and other fees about $8 million |
| Volume | About 820 million card transactions a year (about 2.25 million a day; peak about 260 per second), about $38 billion in processed volume (about $104 million of merchant sales a day). About 45% card-present, 55% card-not-present. Integrated Payments carries about 22% of transactions |
| Ownership and governance | Private equity-backed corporation. Board of directors with an audit committee that receives cyber risk reports each quarter. Not an SEC registrant |
| Sponsor banks | **Bank A**, a national bank supervised by the OCC, sponsor since 2017, about 78% of volume. **Bank B**, an FDIC-supervised insured state nonmember bank, second sponsor since 2025-10-01; the Integrated Payments merchants were moved to Bank B. Each bank holds the card network memberships for its program, registered the company with the card brands as its third-party processor, and originates the merchant funding ACH files the company prepares. Both sponsor agreements state that the company's clearing, settlement, reconciliation, and merchant funding file services are performed for the bank and are subject to examination under the Bank Service Company Act, 12 U.S.C. 1867(c) |
| Contract commitments | Merchant agreements promise 99.95% monthly availability for authorization; ISV partner agreements promise 99.95% for the Integrated Payments API. Each sponsor agreement requires clearing files and merchant funding files by the bank's daily cutoff and notice to the bank of any suspected account data compromise within 24 hours |
| PCI DSS status | **Service provider**, PCI DSS v4.0.1. Level 1 under Visa's service provider levels (more than 300,000 transactions a year; levels are set by the card brands, not PCI SSC). Validates with an annual Report on Compliance (ROC) by a Qualified Security Assessor (QSA), an Attestation of Compliance (AOC), and quarterly external scans by an Approved Scanning Vendor (ASV). Last AOC for the core platform: "Compliant", 2025-12-15. The acquired gateway had its own Level 1 AOC from a different QSA, dated 2025-09-30. **The 2026 ROC is the first combined assessment.** Both sponsor banks agreed in writing (2026-06-12) to accept the combined 2026 AOC by 2026-12-15 instead of a separate 2026 gateway AOC. ROC fieldwork: 2026-11-09 to 2026-11-20. The AOCs and the banks' letters are in the intake evidence (EV-034); the obligations register records the basis (PCI-DSS) |
| GLBA status | A non-bank **financial institution** under the FTC Safeguards Rule, 16 CFR Part 314: its business is data processing of financial data, an activity listed in 12 CFR 225.28(b)(14) and financial in nature under 12 U.S.C. 1843(k). It holds customer information of other financial institutions' customers (cardholders) (314.1(b)). Not eligible for the 314.6 exception. It has a board, so the Qualified Individual reports to the board (314.4(i)). Determined in the intake obligations register (FTC-314) |
| Bank service provider status | **Bank service provider** to Bank A under 12 CFR 53.2(b)(2) and 53.4 (OCC), and to Bank B under 12 CFR 304.22(b)(2) and 304.24 (FDIC). The Federal Reserve parallel (12 CFR 225.303) does not apply: no services are performed for a Board-supervised banking organization. Determined in the intake obligations register (C-FINANCIAL-R01, C-FINANCIAL-R01-FDIC, C-FINANCIAL-R01-FRB) from the sponsor agreements (EV-035) |
| PIN debit | The company does not acquire PIN-based debit transactions and holds no PIN keys. Merchants that need PIN debit get it from a partner processor under a referral agreement. PCI PIN Security Requirements are out of scope (EV-047; obligations register PCI-PIN) |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv). NYDFS 23 NYCRR Part 500: no New York license, registration, or charter. SEC Regulation SCI and SEC disclosure rules: not an SCI entity and not an SEC registrant. NCUA 12 CFR 748.1(c): not a credit union and serves none. Interagency Guidelines (12 CFR 30 App. B; 12 CFR 364 App. B): apply to the sponsor banks and reach the company only through the sponsor agreements' service provider terms. Money transmission licensing: merchant funds settle through the sponsor banks' accounts; licensing is outside this security library |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notification, Fla. Stat. 501.171). For cardholder data the company is usually a **third-party agent** of its merchants under 501.171(6); for merchant owner data it is itself a covered entity |

**Driver labels used in this folder.** The vertical requirement IDs (C-FINANCIAL-R01 to R06) are used wherever they apply, with the specific section, for example "C-FINANCIAL-R01 (12 CFR 53.4)" or "C-FINANCIAL-R01 (12 CFR 304.24)". PCI DSS and the FTC Safeguards Rule are not in the vertical requirements list, so rows cite them directly: "PCI DSS 8.4.2" (requirement number in PCI DSS v4.0.1) and "16 CFR 314.4(c)(5)".

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Board audit committee | Quarterly cyber risk reporting; receives the annual written report of the Qualified Individual (16 CFR 314.4(i)) |
| Chief Executive Officer (CEO) | Accepts High risks; approves the risk appetite and the security budget |
| Chief Operating Officer (COO) | Executive sponsor of the security and compliance program; formally assigned PCI DSS compliance responsibility (PCI DSS 12.4.1); accepts Moderate risks; approves policies |
| Chief Financial Officer (CFO) | Settlement, treasury, and merchant funding; sponsor bank financial terms; cyber insurance |
| Chief Technology Officer (CTO) | System owner of the Payment Processing Platform; engineering and change management for both platforms |
| Chief Risk and Compliance Officer (CRCO) | Sponsor bank and card brand compliance, third-party risk program, model risk management, notice decisions with counsel; chairs the AI and model risk committee |
| General Counsel | Legal privilege, notices, contracts, law enforcement contact |
| Virtual CISO (vCISO, part-time contractor) | Program strategy, risk appetite, and board reporting |
| Director of Information Security | **Qualified Individual** under 16 CFR 314.4(a) and day-to-day security lead; leads a team of 8 (3 security engineers, 2 security operations analysts, 2 GRC analysts, 1 PCI program manager) |
| VP Platform Engineering | Cloud A landing zone, colocation infrastructure, CI/CD, logging, and key management operations |
| Director of Integrated Payments Engineering | The acquired gateway (Cloud B) until it is migrated |
| IT Director | Corporate IT, identity provider, endpoints, productivity suite |
| Director of Settlement and Treasury Operations | Daily clearing, reconciliation, merchant funding files, bank connectivity |
| Director of Fraud and Merchant Risk | Fraud operations and merchant risk monitoring; business owner of the fraud-detection model (P10) |
| Head of Data Science | Builds and maintains the in-house models |
| Director of Merchant Services | Onboarding and underwriting operations, support, and the contact center |
| HR Director | Onboarding, background checks, terminations, training records |
| Co-sourced internal audit firm | Annual IT audit; performed the P07 assessment; independent of the QSA and of control operation |
| Managed security service provider (MSSP) | 24x7 monitoring of the SIEM and EDR for the core platform and corporate environment |
| External QSA firm | Annual ROC; independent of all remediation work |
| Approved Scanning Vendor (ASV) | Quarterly external scans |

**Role overlap and compensation.** The vCISO covers strategy and board reporting part-time, and the Director of Information Security both runs and reports on day-to-day security. The co-sourced internal audit firm and the QSA provide the independent checks. The Director of Integrated Payments Engineering still operates and approves changes to the acquired gateway with a small team; two-person change approval and the P07 assessment compensate until the platform is migrated.

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv). Suppliers are in [`step-00_P00_intake/vendor-register.csv`](step-00_P00_intake/vendor-register.csv).

| ID | System | Hosting | Card data? | Notes |
|---|---|---|---|---|
| SYS-01 | Core payment platform: authorization switch, merchant API gateway, terminal gateway, token vault, recurring billing | Cloud A landing zone: CDE workload accounts in a primary and a secondary region (containers, managed relational database, message queues) | **Yes (CDE)** | Warm standby in the secondary region since 2025 (EV-013) |
| SYS-02 | Settlement and funding engine: clearing file builder, reconciliation, merchant funding file generation, chargeback system | On premises: primary colocation cage (Florida); disaster recovery cage (second colocation, outside Florida) | **Yes (CDE)** | Legacy batch platform; 4 batch servers run an operating system out of vendor support since 2025-10 (EV-016) |
| SYS-03 | Payment HSMs | Company-owned payment HSMs in both colocation cages (FIPS 140-3 Level 3 validated) and the Cloud A provider's dedicated payment HSM service | Keys | Key hierarchy for PAN encryption, tokenization, and TLS keys. Dual control for key ceremonies (EV-023) |
| SYS-04 | Merchant portal and virtual terminal (core) | Cloud A | **Yes (CDE)** | About 64,000 merchant user accounts; MFA required for administrator, refund, funding account, and virtual terminal roles since 2025 (EV-009) |
| SYS-05 | Hosted payment page and embedded payment form (core) | Cloud A, served through a content delivery service | **Yes (CDE)** | About 7,800 e-commerce merchants. Script inventory, integrity checks, and tamper-detection since 2025-03 (EV-022) |
| SYS-06 | Integrated Payments gateway (acquired): partner API, hosted payment fields loaded in ISV checkouts, token vault, partner and merchant portal | Cloud B (a different public cloud provider), 3 accounts | **Yes (CDE)** | Separate identity, pipeline, and logging (EV-007, EV-021, EV-030). Portal users sign in with a password only (EV-009). Migration into Cloud A planned for 2027 |
| SYS-07 | Identity: workforce identity provider (SSO, MFA) and privileged access management (PAM) vault | SaaS | No | PAM covers Cloud A and the colocation sites; it does not yet cover Cloud B (EV-006) |
| SYS-08 | Corporate networks and endpoints | Florida headquarters and the acquired office | No (connected-to) | About 720 laptops and desktops with EDR and full-disk encryption. Administrators reach the CDE only through PAM (EV-011) |
| SYS-09 | Security monitoring: SIEM (SaaS, monitored 24x7 by the MSSP), EDR, web application firewalls, network intrusion detection, file integrity monitoring, payment page tamper-detection | SaaS plus cloud services | No (security service to CDE) | Cloud B and the Integrated Payments gateway do not send logs to the SIEM (EV-028) |
| SYS-10 | Source code repositories and CI/CD pipelines | SaaS: one instance for the core platform, a separate one for Integrated Payments | No (can change CDE code) | Deploy to SYS-01, SYS-04, SYS-05, SYS-06 |
| SYS-11 | Fraud-detection model (built in house since 2025) and model serving | Cloud A | Uses tokens and transaction features | Scores every authorization on both platforms (see P10) |
| SYS-12 | Data platform: cloud data warehouse and model training environment | Cloud A analytics account | Tokens only by design | Training extracts for SYS-11 and the merchant risk model |
| SYS-13 | Merchant onboarding, underwriting, and CRM, with a vendor merchant risk scoring service | SaaS | No card data; merchant owner NPI (SSNs, bank accounts) | Underwriting files for about 650 new merchants a month |
| SYS-14 | Merchant support: ticketing, contact center platform with call recording, website chatbot | SaaS | Spoken card data can be captured in call recordings when pause-and-resume is missed (EV-055, EV-071) | PAN masking in tickets since 2025 (EV-055) |
| SYS-15 | Productivity suite (email, files, chat) | SaaS | Incidental | |
| SYS-16 | Bank connectivity: managed file transfer servers and treasury workstations for the sponsor banks | Primary colocation cage, with a standby at the DR cage | Funding files (no PAN) | Sends merchant funding ACH files to both sponsor banks |
| External | Sponsor banks A and B; card networks (dedicated encrypted links from both colocation cages and from Cloud A, provisioned under the sponsor banks' memberships); Cloud A and Cloud B providers; 2 colocation providers; content delivery service; MSSP; vendor merchant risk scoring service; QSA; ASV | | | |

**SSP system (P02):** the *Payment Processing Platform (PPP)*: the cardholder data environment made up of SYS-01 to SYS-06 across Cloud A, Cloud B, and the two colocation cages, plus the connected-to and security-impacting systems SYS-07, SYS-09, SYS-10, SYS-11, SYS-12, SYS-16, and the administrative access path from SYS-08.

**Registry defaults kept.** The primary system ("Payment processing platform (cardholder data environment)"), the P08 incident ("Compromise of payment processing environment"), and the P10 use case ("Transaction fraud-detection model") all fit this business at this size, so they are kept. At this size the P08 deliverable adds a second incident type and the P10 deliverable covers a portfolio of AI use cases.

## 4. Where the evidence is
This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Every item has a source system, an owner, and as-of and collected dates.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps against PCI DSS v4.0.1, the FTC Safeguards Rule, 12 CFR 53.4 and 304.24, and Fla. Stat. 501.171** are judged in the gap analysis (P03), and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P08 incidents | **Two incident types, integrated with crisis management and legal:** (1) **compromise of the payment processing environment**: an attacker phishes an Integrated Payments engineer, uses the engineer's standing administrator role in Cloud B to deploy a memory-scraping implant on the gateway's API containers, captures card data from card-not-present API requests, and exfiltrates it over HTTPS to attacker-controlled cloud storage; (2) **ransomware on the on-premises settlement and funding environment** that delays merchant funding files to both sponsor banks for more than 4 hours (12 CFR 53.4 and 304.24 notices) |
| P09 SOC 2 | (a) Readiness for a SOC 2 Type 2 examination (Security, Availability, Processing Integrity, Confidentiality) requested by both sponsor banks in their annual due diligence and by the 5 largest ISV partners. PCI DSS stays the main assurance for card data. (b) A tiered vendor SOC 2 and AOC review program for inherited controls |
| P10 AI | Portfolio of 5 use cases: AI-001 transaction fraud-detection model (built in house); AI-002 merchant underwriting and risk monitoring model (vendor scoring service); AI-003 dispute representment drafting assistant (generative AI); AI-004 merchant support chatbot (generative AI); AI-005 engineering code assistant (generative AI) |
| Cloud | Multi-cloud and hybrid, vendor-agnostic: a multi-account landing zone in Cloud A, the acquired 3-account footprint in Cloud B, and 2 colocation cages. Services are described by category, with AWS, Azure, and Google Cloud equivalents only where needed for shared responsibility |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2025-10-01 | Bank B sponsor agreement in effect |
| 2025-11-03 | Acquisition of the payment gateway (Integrated Payments) closes |
| 2026-02-21 | Settlement disaster recovery test (11 hours against an 8-hour target) |
| 2026-04-18 | Colocation-to-cloud interconnect changed (significant change) |
| 2026-06-12 | Both sponsor banks accept the combined 2026 AOC by 2026-12-15 |
| 2026-06-15 to 2026-07-02 | Intake: evidence requests, exports, inventories, obligations register |
| 2026-07-06 to 2026-07-31 | BIA interviews, risk assessment, and gap analysis fieldwork |
| 2026-07-27 to 2026-07-31 | 2026 policies (POL-01 to POL-05), the standards index, and the P08 runbooks drafted from the gaps |
| 2026-08-03 to 2026-08-21 | Control assessment fieldwork (co-sourced internal audit firm): operating tests of controls already in place; design review of the draft policies and runbooks |
| 2026-08-12 | Assessors' stop-and-notify finding: vendor default credentials on settlement server management interfaces (P01 R-050) |
| 2026-08-17 to 2026-09-04 | AI governance assessment (P10) |
| 2026-09-15 | Deliverables, policies, and runbooks approved by the COO (and by the CEO for POL-01 and for High and Very High risks); results presented to the board audit committee |
| 2026-10-01 | 2026 policies take effect |
| 2026-11-09 to 2026-11-20 | QSA ROC fieldwork for the combined 2026 PCI DSS assessment |
| 2026-12-15 | Combined 2026 AOC due to both sponsor banks |
| 2027-03 (planned) | Follow-up assessment: operating effectiveness of the controls the new policies and standards introduced, after at least one quarter of operation |
| 2027-04-01 | Planned start of the SOC 2 Type 2 observation period |

## 7. Facts added during the build (fictional; used across P01-P10)
These details were added so the deliverables could be specific. They do not change sections 1-6.

| Topic | Added fact |
|---|---|
| Cloud A landing zone | 8 accounts under one organization (EV-013): management and security tooling, identity and log archive, shared network hub, CDE production (primary region), CDE recovery (secondary region), non-CDE production (portal content, APIs without card data), analytics and model training, backup vault |
| Cloud B footprint | 3 accounts: gateway production, gateway non-production, shared services. Cloud B workloads are containers, a managed relational database for the gateway token vault, and the cloud provider's general key management service (no payment HSM) (EV-007) |
| Colocation | The colocation providers supply the building, power, cooling, guards, and cage locks under their own AOCs; the company owns everything inside its cages (servers, payment HSMs, firewalls, tape library) (EV-047, EV-048) |
| Settlement timing | Clearing files go to the card networks by about 22:00 Eastern; funding files go to Bank A by 03:00 and to Bank B by 04:00 Eastern for next-day merchant funding. About $104 million of merchant funding moves each business day (EV-053) |
| Workforce activity | 142 terminations and 88 internal transfers in the 12 months to 2026-06-30 (EV-003). The June 2026 phishing simulation click rate was 4.9% (EV-042) |
| Privileged users | 110 core administrators (Cloud A, colocation, HSM custodians); 26 Integrated Payments engineers with standing Cloud B administrator roles (EV-006, EV-007) |
| Service providers | 182 vendors in total; 34 are PCI DSS service providers (can affect account data or the CDE); 41 vendors came with the acquisition (EV-045, EV-046) |
| Data science | The in-house fraud model (AI-001) replaced a licensed vendor model on 2025-06-30 (EV-054). 8 data scientists; the Head of Data Science reports to the CTO |
| Additional role titles | Controller; Director of Sales and Partner Management; Contact Center Manager; Director of Corporate Communications; PCI Program Manager |
| Vendor tiers (P09) | The 34 PCI DSS service providers are Tier 1; about 50 vendors are Tier 2; the rest are Tier 3. The contact center SaaS has no PCI DSS AOC (EV-046, EV-048) |
| AI and model governance (P10) | An AI and model risk committee chaired by the Chief Risk and Compliance Officer was formed on 2026-09-15. An outside model risk firm is engaged for independent validation of AI-001 and AI-002 |
| Merchant contacts | Integrated Payments merchants are often reachable only through their ISV: 31 of 50 sampled had no direct security contact on file (EV-073, P03 fieldwork) |
| Sponsor bank requests | Bank A's internal audit has asked whether a SOC 1 report on the settlement services will be available for 2028 (EV-036) |
| Cloud B log retention | Cloud B audit logs are kept 30 days inside Cloud B (EV-030) |
