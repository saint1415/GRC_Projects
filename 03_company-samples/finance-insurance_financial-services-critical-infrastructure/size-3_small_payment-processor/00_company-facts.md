# Scenario facts: Cris Santos Company | Financial Services | Small

All 11 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a regulation, a standard, or a card brand rule, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (a merchant payment processor) |
| Business | Payment processor serving merchants (NAICS 522320). It authorizes, clears, and settles card payments for about 4,200 small and mid-size merchants in the United States: card-present authorization for merchant terminals, an e-commerce payment API with a hosted payment page, a token vault for recurring billing, a merchant portal with a virtual terminal, daily settlement, merchant funding, and chargeback handling |
| Location | Headquarters and only office in Florida. No data center of its own: the platform runs in one public cloud tenant (see section 3). Merchants are located in 41 states. The processor is treated as a **national** business: state law is handled generically ("each state where affected individuals reside") with Florida as the worked example |
| Workforce | 60 employees: 7 executive and administration, 22 engineering (16 software developers, 4 platform engineers, 2 QA), 3 IT, 7 risk, fraud and compliance, 8 settlement operations and finance, 9 merchant support, 4 sales and partner management |
| Size | $28.2 million in annual receipts (fictional), about $77,000 per day (EV-061). Under the SBA size standard of $47.0 million for NAICS 522320, so SBA-small |
| Volume | About 95 million card transactions a year (about 260,000 a day; peak about 45 per second), about $6.8 billion in processed volume. About 38% card-present, 62% card-not-present (EV-062) |
| Sponsor bank | A **national bank** (supervised by the OCC) is the processor's sponsor (acquiring) bank. It holds the card network memberships, registered the processor with the card brands as its third-party processor, and is the originating depository institution for merchant funding ACH files. The sponsor agreement (2023, renewed 2026-01-01) states that the processor's settlement, reconciliation, and merchant funding file services are performed for the bank and are subject to examination under the Bank Service Company Act, 12 U.S.C. 1867(c) |
| Contract commitments | Merchant agreements promise 99.9% monthly availability for authorization. The sponsor agreement requires clearing and merchant funding files by the bank's daily cutoff, and notice to the bank of any suspected account data compromise within 24 hours |
| Second bank (pending) | A letter of intent (2026-06) with an FDIC-supervised **state nonmember bank** for a second sponsor program. Target signing 2027-Q1. No services are performed for it yet |
| PCI DSS status | **Service provider**, PCI DSS v4.0.1, determined in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (PCI-DSS). Level 1 under Visa's service provider levels (more than 300,000 transactions a year; levels are set by the card brands, not PCI SSC). Validates with an annual Report on Compliance (ROC) by a Qualified Security Assessor (QSA), an Attestation of Compliance (AOC), and quarterly external scans by an Approved Scanning Vendor (ASV). Last AOC: "Compliant", dated 2025-12-01 (EV-056). Next ROC fieldwork: 2026-11-02 to 2026-11-13; AOC due to the sponsor bank by 2026-12-01 |
| GLBA status | A non-bank **financial institution** under the FTC Safeguards Rule, 16 CFR Part 314, determined in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (FTC-314): its business is data processing of financial data, an activity listed in 12 CFR 225.28(b)(14) and financial in nature under 12 U.S.C. 1843(k). Holds customer information of other financial institutions' customers (cardholders) (314.1(b)). Not eligible for the 314.6 exception (far more than 5,000 consumers) |
| Bank service provider status | **Bank service provider** to the sponsor bank under 12 CFR 53.2(b)(2) and 53.4 (OCC), determined in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (C-FINANCIAL-R01) from the sponsor agreement (EV-052). The FDIC and Federal Reserve parallels (12 CFR 304.24, 225.303) do not apply today and will apply to the FDIC-supervised bank once the second sponsor agreement is signed (see P03) |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv). NYDFS 23 NYCRR Part 500: the company holds no New York license, registration, or charter. SEC Regulation SCI and Form 8-K: not an SCI entity and not an SEC registrant. NCUA 12 CFR 748.1(c): not a credit union and serves none. Interagency Guidelines (12 CFR 30 App. B): apply to the sponsor bank, reach the processor only through the sponsor contract (III.D). Money transmission licensing: merchant funds settle through the sponsor bank's accounts; licensing is outside this security library. PIN debit: the company does not process PIN transactions and holds no PIN keys |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notification, Fla. Stat. 501.171). For cardholder data the processor is usually a **third-party agent** of its merchants under 501.171(6); for merchant owner data it is itself a covered entity |

**Driver labels used in this folder.** The vertical requirement IDs (C-FINANCIAL-R01 to R06) are used wherever they apply. PCI DSS and the FTC Safeguards Rule are not in the vertical requirements list, so rows cite them directly: "PCI DSS 8.4.2" (requirement number in PCI DSS v4.0.1) and "16 CFR 314.4(c)(5)".

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Majority owner and Chief Executive Officer (CEO) | Accepts High and Very High risks; approves the budget; receives the annual Safeguards Rule report (the company has no board, so the owner and COO are the "senior officer" audience under 314.4(i)) |
| Chief Operating Officer (COO) | Executive owner of the security and compliance program; formally assigned PCI DSS compliance responsibility (PCI DSS 12.4.1); accepts Moderate risks; approves policies |
| Chief Financial Officer (CFO) | Owns settlement, merchant funding, and the sponsor bank relationship's financial terms |
| Chief Technology Officer (CTO) | Owns the payment platform, engineering, and change management |
| IT Manager | **Information Security Lead** (part-time security duties), **Qualified Individual** under 16 CFR 314.4(a), and day-to-day PCI DSS lead. Runs IT with 2 IT support specialists |
| Compliance and Risk Manager | Sponsor bank and card brand compliance, third-party risk, breach and notice decisions with counsel; 2 compliance analysts |
| Risk and Fraud Manager | Merchant risk, fraud operations, and business owner of the fraud-detection model (P10); 3 fraud analysts |
| Platform Engineering Lead | Cloud tenant, CI/CD pipeline, logging, and key management operations (4 platform engineers) |
| Settlement Operations Manager | Daily clearing, reconciliation, merchant funding files, chargebacks |
| Merchant Support Manager | Merchant help desk (9 staff), merchant portal user administration requests |
| HR Manager | Onboarding, background checks, terminations, training records |
| External QSA firm | Annual ROC; independent of all remediation work |
| Approved Scanning Vendor (ASV) | Quarterly external scans |

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv).

| ID | System | Hosting | Card data? | Notes |
|---|---|---|---|---|
| SYS-01 | Payment processing platform: authorization switch, merchant API gateway, terminal gateway, token vault, settlement and funding engine | Cloud tenant (containers, managed relational database, message queue) | **Yes (CDE)** | Stores PAN encrypted in the token vault; builds clearing files and merchant funding ACH files |
| SYS-02 | Payment HSM service | Cloud provider's dedicated payment HSM service (FIPS 140-3 Level 3 validated) | Keys | Key hierarchy for PAN encryption, tokenization, and TLS keys. Dual control for key ceremonies |
| SYS-03 | Merchant portal and virtual terminal | Cloud tenant (web application) | **Yes (CDE)** | 11,500 merchant user accounts. Virtual terminal lets merchant staff key in card numbers |
| SYS-04 | Hosted payment page and embedded payment form (JavaScript) | Cloud tenant, served through a content delivery service | **Yes (CDE)** | Launched 2026-02-09. About 1,600 e-commerce merchants embed it |
| SYS-05 | Identity provider (workforce single sign-on and MFA) | SaaS | No | Protects the cloud console, the bastion, SYS-08, and all SaaS |
| SYS-06 | Office network and endpoints | Florida office | No (connected-to) | 72 laptops (all with EDR and full-disk encryption, EV-012), office firewall, Wi-Fi. Administrators reach the CDE only through the bastion |
| SYS-07 | Security monitoring: log management and SIEM service, EDR console, web application firewall | SaaS plus cloud services | No (security service to CDE) | Alerts go to a shared mailbox and chat channel, watched in business hours only (EV-028) |
| SYS-08 | Source code repository and CI/CD pipeline | SaaS | No (can change CDE code) | Deploys to SYS-01, SYS-03, SYS-04 |
| SYS-09 | Fraud-detection model | Licensed model from a fraud analytics vendor, hosted in the cloud tenant | Uses tokens and transaction features | Scores every authorization. Vendor retrains it quarterly on an extract of labeled transactions (see P10) |
| SYS-10 | Productivity suite (email, files, chat) | SaaS | Incidental (EV-036) | |
| SYS-11 | Merchant onboarding and CRM | SaaS | No card data; merchant owner NPI (SSNs, bank accounts) | Underwriting files |
| SYS-12 | Merchant support ticketing | SaaS | **Unexpected PAN found** (EV-036; EV-076) | Merchants paste card numbers into tickets and email |
| SYS-13 | Cloud data warehouse (analytics and fraud model training extracts) | Cloud tenant | **Unexpected PAN found in P07** (EV-SC-28) | Intended to hold tokens only (EV-034) |
| External | Sponsor bank; card networks (through dedicated encrypted links provisioned under the sponsor bank's membership); cloud provider; fraud analytics vendor; content delivery service; QSA; ASV | | | |

**SSP system (P02):** the *Payment Processing Platform (PPP)*: the cardholder data environment made up of SYS-01 to SYS-04 in the cloud tenant, plus the connected-to and security-impacting systems SYS-05, SYS-07, SYS-08, SYS-09, SYS-13, and the administrative access path from SYS-06.

## 4. Where the evidence is

This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Every item has a source system, an owner, and as-of and collected dates.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps against PCI DSS v4.0.1, the FTC Safeguards Rule and 12 CFR 53.4** are judged in the gap analysis (P03), and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs. Only the QSA's Report on Compliance concludes on PCI DSS compliance.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P08 incident | Compromise of the payment processing environment: an attacker uses a former contractor's still-active code repository token to push a malicious change to the hosted payment page script and the API gateway, captures card data from e-commerce transactions, and exfiltrates it over DNS |
| P09 SOC 2 | (a) SOC 2 readiness self-assessment requested by the sponsor bank in its 2026 annual due diligence and by two software-platform partners: the processor is a service organization, so SOC 2 fits. PCI DSS stays the main assurance for card data. (b) Review of the cloud provider's SOC 2 Type 2 report and AOC for inherited controls |
| P10 AI | AI-001 transaction fraud-detection model (licensed model, scores every authorization); AI-002 staff use of generative AI chatbots |
| Cloud | Vendor-agnostic. Services are described by category, with AWS, Azure, and Google Cloud equivalents noted only where needed for shared responsibility |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-03-14 | Platform cut over from managed hosting to the cloud tenant (significant change) |
| 2026-05-19 | A faulty extract job starts writing full PANs to a data warehouse training table (found 2026-08-05) |
| 2026-06-29 to 2026-07-10 | Intake: evidence requests, exports, inventories, obligations register |
| 2026-07-13 to 2026-07-24 | BIA interviews, risk assessment and gap analysis fieldwork |
| 2026-07-27 to 2026-07-31 | Policies POL-01 to POL-05 drafted from the gaps |
| 2026-08-03 to 2026-08-07 | Control assessment fieldwork: operating tests of controls already in place; design review of the draft policies |
| 2026-08-10 | Sponsor bank's compliance contact informed of the warehouse PAN finding as a PCI DSS compliance matter |
| 2026-08-12 | Notice analysis for the warehouse PAN finding completed: not a notification event (P08 section 6.6) |
| 2026-08-31 | Deliverables and policies approved by the COO (and by the CEO for High risks) |
| 2026-11-02 to 2026-11-13 | QSA ROC fieldwork for the 2026 PCI DSS assessment |
| 2026-12-01 | 2026 AOC due to the sponsor bank |
| 2027-02 (planned) | Follow-up assessment: operating effectiveness of the controls the new policies introduced, after at least one quarter of operation |
