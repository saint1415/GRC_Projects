# Scenario facts: Cris Santos Company | Financial Services | Multi-Sector

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, a standard, or a card brand rule, the citation is given. Federal regulatory text was read from the eCFR (point-in-time text for 2026-09-23) or the U.S. Code for this sample.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company Holdings, Inc. (publicly traded SEC registrant; not a bank and not a bank holding company) |
| Structure | A holding company with three divisions and corporate shared services. Each division is one or more limited liability companies owned by the holding company |
| Division 1: Payment Processing (NAICS 522320), **focus of this scenario** | Cris Santos Payments, LLC, a merchant acquiring processor. It authorizes, clears, and settles card payments for about 920,000 merchants (about 1.3 million locations) in all 50 states: card-present and card-not-present authorization, an e-commerce payment API with hosted payment fields, a token vault, a merchant portal with a virtual terminal, daily clearing and settlement, merchant funding, and chargeback processing. About 24,000 employees. A PCI DSS Level 1 **service provider**, a **bank service provider** to four sponsor banks, and a **financial institution** under the FTC Safeguards Rule |
| Division 2: Payments Software Platform (NAICS 513210, sector 51 Information) | Cris Santos Commerce Software, LLC. Multi-tenant commerce software for about 410,000 merchants (cloud point of sale, online storefronts, invoicing) and a developer platform (payment gateway API, SDKs, and an ISV portal) used by about 1,900 independent software vendors (ISVs). Its gateway routes about 70% of its transactions to the Payment Processing division and 30% to six unaffiliated processors, so it transmits cardholder data in its own right. About 9,500 employees. Issues a SOC 2 Type 2 report each year and validates its gateway separately as a PCI DSS Level 1 service provider |
| Division 3: Merchant Consulting Services (NAICS 541611, sector 54 Professional, Scientific, and Technical Services) | Cris Santos Merchant Advisory, LLC, a payments consulting firm acquired on 2025-04-01. Payments strategy and cost advisory, checkout and integration services performed in clients' environments, PCI DSS readiness advisory (it is **not** a QSA company and never validates compliance), and outsourced chargeback and dispute management. About 6,500 employees serving about 3,800 merchant clients, about 620 of which do not process with the group |
| Corporate shared services | Identity, security operations, data centers and cloud, network, the group data platform, email and collaboration, HR, finance, legal, and group internal audit. About 5,000 employees, employed by the holding company |
| Location | Headquartered in Florida. Two group data centers (primary in Florida, secondary in another state) and operations centers in Florida and three other states. Merchants and consulting clients are in all 50 states. **State law is handled generically** ("each state where affected individuals reside"), with Florida as the worked example |
| Workforce / revenue | 45,000 employees; about $18.0 billion revenue (fictional): Payment Processing about $13.0 billion, Payments Software Platform about $3.4 billion, Merchant Consulting about $1.6 billion |
| Sponsor banks | Four sponsor (acquiring) banks hold the card network memberships, registered the Payment Processing division with the card brands, and are the originating depository institutions for merchant funding ACH files: **Bank A** and **Bank B**, national banks supervised by the OCC; **Bank C**, a state member bank supervised by the Federal Reserve; **Bank D**, a state nonmember bank supervised by the FDIC. Each sponsor agreement states that the division's clearing, settlement, reconciliation, and merchant funding file services are performed for the bank and are subject to examination under the Bank Service Company Act, 12 U.S.C. 1867(c) |
| Bank service provider status | Decided in the obligations register (C-FINANCIAL-R01-PP). The Payment Processing division is a **bank service provider** to all four sponsor banks: 12 CFR 53.4 (Banks A and B, OCC), 12 CFR 225.303 (Bank C, Federal Reserve), and 12 CFR 304.24 (Bank D, FDIC). The other two divisions perform no covered services for any bank |
| PCI DSS status | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (PCI-PP, PCI-SW, PCI-MC). Payment Processing: **service provider**, PCI DSS v4.0.1, Level 1 under Visa's service provider levels (more than 300,000 transactions a year; levels are set by the card brands, not PCI SSC). Annual Report on Compliance (ROC) by a Qualified Security Assessor (QSA), Attestation of Compliance (AOC), and quarterly Approved Scanning Vendor (ASV) scans. Last AOC "Compliant", dated 2026-01-22. Software division gateway (SYS-S2): separate ROC; AOC "Compliant", dated 2026-03-31 (EV-042, EV-056). PIN debit is processed through PIN translation in the payment HSMs; the PCI PIN Security Requirements are assessed separately and are outside this library |
| GLBA status | Decided in the obligations register (N54-R01-PP, N54-R01-SW, N54-R01-MC). No group entity is a bank or is supervised by a federal banking agency, so the FTC Safeguards Rule (16 CFR Part 314) is the GLBA safeguards rule for the group's financial institutions (314.1(b)). **Payment Processing:** a financial institution; data processing and transmission of financial data is listed in 12 CFR 225.28(b)(14), and it holds customer information of other financial institutions' customers (cardholders) (314.1(b)). **Payments Software Platform:** treated as a financial institution on a conservative reading, because its gateway transmits payment transaction data (225.28(b)(14)). **Merchant Consulting:** not significantly engaged in financial activities, so not a financial institution (314.2(h)(3)(iv)); it is a **service provider** (314.2(r)) to the Payment Processing division for dispute services under an intercompany services agreement |
| SEC status | Publicly traded. Reg S-K Item 106 annual disclosure; Form 8-K Item 1.05 for material cybersecurity incidents, decided by a disclosure committee |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv). NYDFS 23 NYCRR Part 500 (no group entity holds a New York license, registration, or charter). SEC Regulation SCI (not an SCI entity). NCUA 12 CFR 748.1(c) (no group entity is a credit union). Interagency Guidelines (12 CFR 30 App. B and parallels): apply to the sponsor banks and reach the division only through the sponsor agreements' service provider terms (III.D). Money transmission licensing: merchant funds settle through the sponsor banks' accounts; licensing is outside this security library. FedRAMP (no federal agency customers), COPPA (no child-directed services), FAR and DFARS clauses (no federal contracts or subcontracts), HIPAA (no division handles PHI for a covered entity) |
| FAR overhaul clause numbers | Background fact, not scored in P03. Contracts awarded before the contracting agency adopted its FAR Part 40 class deviation keep the clauses this sample cites (FAR 52.204-21, 52.204-23 and 52.204-25) until they are modified. New awards under the deviation carry FAR 52.240-93, which has the same 15 safeguarding requirements as FAR 52.204-21, and FAR 52.240-91, which replaces the separate Kaspersky, Section 889 and FASCSA reports with one report within 72 hours. Sources: SRC-FAR-RFO-PART40 |

**Driver labels used in this folder.** The vertical requirement IDs (C-FINANCIAL-R01 to R06) are used wherever they apply. Requirements of the other two divisions use their verticals' IDs: N51-R01 to N51-R08 (Information) and N54-R01 to N54-R09 (Professional Services). PCI DSS, the FTC Safeguards Rule, and card brand rules are not in any requirements list, so rows cite them directly, for example "PCI DSS 8.4.2" and "16 CFR 314.4(c)(5)".

## 2. People (role titles only)
| Role | Security and compliance duties |
|---|---|
| Board of directors: risk committee and audit committee | Risk committee oversees cyber and enterprise risk, approves group policies, accepts Very High risks, and receives the annual Qualified Individual report (16 CFR 314.4(i)). Audit committee oversees group internal audit |
| Group Chief Executive Officer | Chairs the executive risk committee |
| Group Chief Risk Officer | Second line. Owns the group risk register and the enterprise risk roll-up (NIST IR 8286 Rev. 1); co-accepts High risks; chairs the Group AI council |
| Group CISO | First line. Owns the group information security program and group policies; operates common controls (SYS-G1 to SYS-G5); co-accepts High risks. Designated in writing as the group's **Qualified Individual** under 16 CFR 314.4(a) |
| Group Chief Information Officer | Runs the group data centers, cloud landing zones, network, and group applications |
| Chief Audit Executive (group internal audit) | Third line. Reports to the audit committee. Assesses common controls once and samples division controls (P07) |
| Group General Counsel; Group Chief Privacy Officer; Group Chief Compliance Officer | Contracts and the notification matrix; personal information use and notice decisions; card brand, sponsor bank, and consumer compliance |
| Head of Model Risk Management | Second line. Independent validation of the fraud, merchant underwriting, and AI models under the group model risk policy |
| Disclosure committee | Chaired by the Group Chief Financial Officer. Decides SEC materiality of cybersecurity incidents (Form 8-K Item 1.05) |
| Division security and compliance leads (3) | Payment Processing division CISO (also day-to-day PCI DSS program lead); Software division CISO (SOC 2 and gateway PCI DSS program); Merchant Consulting security and compliance lead. Each maintains the division supplement and division risk register |
| Payment Processing division roles | Division president (executive accountable for PCI DSS under 12.4.1); chief technology officer; head of settlement operations; head of bank and network relationships (sponsor bank and card brand liaison; bank service provider notices); head of merchant risk and fraud (business owner of the fraud-detection model); merchant support director |
| Software division roles | Division president; chief technology officer; client trust and assurance director (SOC 2 report, merchant and ISV notices); marketplace director (third-party apps); product lead for the merchant insights assistant |
| Merchant Consulting roles | Division president; dispute services director; integration services director; PCI readiness practice leader |
| External QSA firms; ASV; SOC service auditor (CPA firm) | Annual ROCs for the processor and the gateway; quarterly external scans; SOC 1 and SOC 2 examinations. Independent of all remediation work |

**How roles overlap at this size, and how that is compensated.** Group standards are set once by the Group CISO, who also operates the common controls and is the Qualified Individual; independent challenge comes from the Group Chief Risk Officer (second line) and group internal audit (third line), and the QSAs and service auditor give external assurance. The Merchant Consulting PCI readiness practice never works on the group's own PCI DSS scope, so the group never advises itself on its own validation.

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv). Suppliers are in the [vendor register](step-00_P00_intake/vendor-register.csv).

| ID | System | Owner | Hosting | Card data? |
|---|---|---|---|---|
| SYS-G1 | Group identity platform (single sign-on, MFA, privileged access management, identity governance) | Corporate | Identity SaaS vendor | No (security-impacting) |
| SYS-G2 | Group SOC, SIEM, EDR, and email security gateway | Corporate | SIEM and EDR SaaS vendors; 24x7 group SOC | No (security service to every CDE) |
| SYS-G3 | Group hybrid infrastructure: two group data centers, cloud landing zones in two providers (vendor-agnostic, called provider A and provider B), wide-area network, and the immutable backup vault | Corporate | Group data centers; providers A and B | Hosts CDE segments |
| SYS-G4 | Group data platform (data lake and warehouse for analytics and model training; tokens only by design) | Corporate | Provider A | Tokens only by design; **PAN found 2026-06-18** in raw gateway logs (EV-079) |
| SYS-G5 | Group email and collaboration suite | Corporate | Productivity SaaS vendor | Incidental (EV-037) |
| SYS-P1 | Authorization and switching platform (terminal and API gateways, card network interfaces) | Payment Processing | Both group data centers, active-active | **Yes (CDE)** |
| SYS-P2 | Token vault and payment HSM clusters (FIPS 140-3 Level 3 validated) | Payment Processing | Both group data centers | **Yes (CDE)**; keys |
| SYS-P3 | Clearing, settlement, and merchant funding engine | Payment Processing | Both group data centers | **Yes (CDE)** |
| SYS-P4 | E-commerce payment API and hosted payment fields | Payment Processing | Provider A (two regions) | **Yes (CDE)** |
| SYS-P5 | Merchant portal and virtual terminal (about 2.1 million merchant user accounts) | Payment Processing | Provider A | **Yes (CDE)** |
| SYS-P6 | Chargeback and dispute platform (also used by Merchant Consulting dispute analysts) | Payment Processing | Provider A | **Yes (CDE)** |
| SYS-P7 | Fraud-detection model platform (real-time scoring service; training on SYS-G4) | Payment Processing | Scoring in both data centers; training on provider A | Tokens and transaction features (connected-to) |
| SYS-P8 | Merchant onboarding and underwriting (CRM and underwriting model) | Payment Processing | SaaS plus provider A | No card data; merchant owner personal information |
| SYS-S1 | Commerce software SaaS (cloud point of sale, about 180,000 online storefronts, invoicing, app marketplace) | Software | Provider B | Embeds the gateway's hosted fields (security-impacting) |
| SYS-S2 | Payment gateway and developer platform (APIs, SDKs, ISV portal) | Software | Provider B | **Yes (gateway CDE)** |
| SYS-S3 | Point-of-sale device management (about 640,000 devices) | Software | Provider B | No PAN; device configuration and keys loaded through SYS-P2 |
| SYS-M1 | Consulting engagement, document, and email tenant (from the acquired firm) with its own identity provider | Merchant Consulting | Productivity and document SaaS | **Unexpected PAN** in dispute evidence email (EV-063, EV-081) |
| External | Four sponsor banks; card networks (dedicated encrypted links under the sponsor banks' memberships); providers A and B; six unaffiliated processors (gateway routing); third-party model provider; QSA firms; ASV | | | |

**SSP system (P02):** the *Payment Processing Platform (PPP)*: the Payment Processing division's cardholder data environment made up of SYS-P1 to SYS-P6 in the two group data centers and the division's provider A accounts, plus the connected-to and security-impacting systems SYS-P7 and the administrative access path; it inherits common controls from SYS-G1 to SYS-G3.

## 4. Where the evidence is
This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Rows are grouped by division (Group, Payment Processing, Software, Merchant Consulting). Every item has a source system, an owner, and as-of and collected dates.
- **Which rules apply** to each division and to the group is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps** against PCI DSS, the FTC Safeguards Rule, the bank service provider notice rules, card brand rules and customer commitments are judged in the gap analyses (P03), which also number the eight group gaps cited across this sample, and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P08 incident | Compromise of the payment processing environment spanning divisions: an attacker relays a Merchant Consulting dispute analyst's SMS code through a phishing page, uses the federated session to bulk-export dispute case files with full card numbers from SYS-P6, and reads ISV API credentials from the Software division's ISV support console. Containment halts dispute adjustments and delays one sponsor bank's funding file. Multi-regulator notification matrix and SEC materiality |
| P09 SOC 2 | Scoped per division: the Software division is a true service organization (in scope; readiness for its Type 2 including the AI assistant); the Payment Processing division keeps PCI DSS and SOC 1 as its main assurance and prepares its first SOC 2 at sponsor bank and ISV request (readiness); Merchant Consulting is out of scope, with reasons |
| P10 AI | Group AI governance program: group standards, the division use-case inventory, and the regulator- and brand-specific rules for AI-001 transaction fraud-detection model (focus), the merchant underwriting model, the merchant insights assistant, and consulting use of generative AI |
| Cloud | Hybrid: two group data centers plus a shared landing zone in two cloud providers, vendor-agnostic; division workloads in their own accounts |

**Registry defaults kept.** The registry's primary system (payment processing platform, cardholder data environment), incident (compromise of the payment processing environment), and AI use case (transaction fraud-detection model) all fit a processor of this size, so they are used as given. At this size the incident is built to cross divisions, and the AI use case sits inside a group program.

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-03-02 | Group AI Standard adopted; Group AI council established |
| 2026-03-30 to 2026-04-24 | Intake: evidence requests, exports, walk-throughs, inventories, obligations register |
| 2026-05-01 to 2026-07-31 | BIA interviews (May), group and division risk analyses (risk interviews in June), and gap analyses |
| 2026-05-08 to 2026-06-18 | Gateway debug field writes PAN to the group data platform (found 2026-06-18; purged 2026-06-20) |
| 2026-06-01 to 2026-06-26 | Group policies v2026 drafted from the gaps found so far (P06); the Payment Processing supplement was aligned to the drafts on 2026-06-30 |
| 2026-06-26 | Notice analysis for the data platform PAN finding completed: not a notification event (P08 section 6.6) |
| 2026-07-01 to 2026-08-31 | Common control assessment (group internal audit) plus division samples: operating tests of controls in force under the 2025 group policies; design review of the draft v2026 policies |
| 2026-08-27 | Group AI council review of the AI use cases |
| 2026-09-10 | Results to the board risk committee; deliverables and group policies v2026 approved (policies effective 2026-10-01) |
| 2026-09-30 | End of the SOC 1 and SOC 2 examination periods |
| 2026-11-02 to 2026-12-11 | QSA ROC fieldwork for the Payment Processing division |
| 2026-12-15 | First cross-division incident tabletop |
| 2027-01-31 | 2026 processor AOC due to the four sponsor banks |
| 2027-04 (planned) | Follow-up assessment: operating effectiveness of the controls the v2026 policies introduced, after at least one quarter of operation |

## 7. Facts added while building the deliverables
These facts were added so the deliverables could be completed. They do not change sections 1 to 6.

| Topic | Added fact |
|---|---|
| Payment Processing scale | About 29 billion transactions a year (about 80 million a day; peak about 7,500 per second), about $1.4 trillion processed volume; about 55% card-present. The token vault holds about 640 million unique PANs. Funding files carry about $3.8 billion a day across the four sponsor banks (Bank A about 48% of volume, Bank B 22%, Bank C 18%, Bank D 12%). About $35.6 million revenue per calendar day |
| Software division scale | About 6.2 billion gateway transactions a year (EV-054). About 640,000 point-of-sale devices under management. About $9.3 million revenue per calendar day. SOC 2 Type 2 for the 12 months ending 2025-09-30 was issued 2025-12-12. The merchant insights assistant is enabled for about 58,000 merchants; it sends merchants' sales and order data (including their customers' names and email addresses, never PAN) to a hosted large language model from a third-party model provider under zero-retention terms |
| Merchant Consulting scale | About 2,400 dispute analysts (about 2.9 million chargebacks a year for about 2,100 merchants), 1,500 integration consultants, 1,400 advisory consultants, 300 PCI readiness advisors, and 900 support staff. About $6.4 million revenue per business day |
| Contract notice terms | Sponsor agreements: notice of any suspected account data compromise within 24 hours. Standard ISV agreement (2025): notice within 24 hours of a security incident affecting ISV credentials or ISV data. Software terms of service: notice to merchants without undue delay; 140 enterprise merchants negotiated 48-hour notice. Consulting engagement letters: notice to clients within 72 hours of a confirmed incident affecting client data |
| Availability commitments | Merchant agreements: 99.95% monthly availability for authorization. Software terms: 99.9% monthly for the gateway and point of sale. The 2026-04-18 data center failover moved authorization and the token vault in 22 minutes |
| PPP users | About 8,900 workforce users reach the PPP (including the 2,400 consulting dispute analysts), with 410 privileged administrators and about 860 service identities |
| Merchant Consulting identity details | 14 consulting users were exempt from MFA through a SYS-M1 trusted-location rule (found in P07, EV-M-IA2(2); removed 2026-09-20). 37 departed consultants still had active SYS-M1 accounts on 2026-07-14 (EV-M-AC2). 212 integration consultants held standing access to the ISV support console (EV-C-AC2). Group legal recorded on 2026-06-12 that the division is not a financial institution under the Safeguards Rule (EV-078) |
| Intercompany agreements | Gateway services agreement (2023) and consulting dispute services agreement (2025) with the Payment Processing division; neither has a PCI DSS responsibility matrix, and the 2025 agreement has no safeguards clause (EV-004) |
| Qualified Individual | The Group CISO was designated in writing as Qualified Individual for both financial-institution divisions in 2025-06; the last written report to the board risk committee was dated 2025-12-10 (EV-019) |
| Processor SOC 2 plan | First SOC 2 for the Payment Processing division: Type 1 as of 2027-03-31, then Type 2 for 2027-04-01 to 2027-09-30 (Security, Availability, Processing Integrity), at sponsor bank and ISV request |
| Risk acceptance | From the group risk management strategy (EV-020). Low: division security and compliance lead. Moderate: division president. High: Group Chief Risk Officer with the Group CISO, reported to the board risk committee. Very High: board risk committee only. A High risk of cardholder data compromise may not be accepted; it must be treated |
