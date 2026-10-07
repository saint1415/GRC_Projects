# Scenario facts: Cris Santos Company | Finance and Insurance | Enterprise

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or supervisory issuance, the citation is given; each was checked against the primary source (eCFR text current through 2026-09-23, the Federal Register, or the issuing agency's website) on 2026-09-27.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (publicly traded bank holding company and financial holding company; SEC registrant listed on a national securities exchange) |
| Business | Super-regional bank (NAICS 522110 Commercial Banking): consumer and small business banking, commercial and corporate banking, treasury management and payments, consumer lending (mortgage, unsecured personal loans, credit cards), and wealth management |
| Legal entities | **Cris Santos Company, Inc.** (parent, the top-tier holding company); **Cris Santos Bank, N.A.** (national bank, the principal subsidiary, about 98% of consolidated assets); **Cris Santos Investment Services, LLC** (an SEC-registered broker-dealer and investment adviser, a FINRA member, and a subsidiary of the parent; it clears customer trades through an unaffiliated clearing firm on a fully disclosed basis). The group has no insurance agency or insurance underwriting subsidiary |
| Location | Headquartered in Florida. 610 branches and about 1,480 ATMs in six southeastern states: Florida, Georgia, Alabama, South Carolina, North Carolina, and Tennessee. **State breach laws are handled generically:** notify under the law of each state where affected individuals reside, with Florida as the worked example |
| Size | **$86.4 billion in average total consolidated assets** (four quarters to 2026-06-30, from the parent's FR Y-9C reports). The bank's average total consolidated assets are $84.9 billion (Call Reports), 98.3% of the parent's. Deposits about $69.8 billion; loans about $58.3 billion (fictional) |
| Revenue | About $4.8 billion a year (net interest income about $3.6 billion, noninterest income about $1.2 billion; fictional). About $13.2 million per calendar day, about $19 million per business day; pre-tax income about $1.45 billion |
| Workforce | 12,000 employees (about 11,400 at the bank and 600 at the broker-dealer) |
| Customers | About 3.6 million consumer customers and 290,000 business clients, including about 41,000 commercial clients on the treasury management platform. About 2.4 million active consumer digital banking users and 180,000 business digital users. The broker-dealer serves about 210,000 brokerage and advisory accounts |
| Payments volume | About 11,000 outgoing wires per business day (about $36 billion a day), about 3.2 million ACH entries originated per business day, and instant payments through Federal Reserve payment services |
| Growth by acquisition | A $7.8 billion community bank (the "acquired bank") merged into Cris Santos Bank, N.A. on 2025-10-01. Its core banking conversion was completed on 2026-05-16. About 2,900 of its business clients still use its legacy commercial online banking platform until migration, due 2027-02-26 |
| Supervision | **Bank:** Office of the Comptroller of the Currency (OCC), primary federal regulator; deposits insured by the FDIC; the CFPB supervises the bank for federal consumer financial law because it has more than $10 billion in total assets (12 U.S.C. 5515). **Parent:** Board of Governors of the Federal Reserve System (bank holding company and financial holding company). **Broker-dealer and adviser:** SEC and FINRA. **Parent securities:** SEC (Exchange Act reporting company; a large accelerated filer, not a smaller reporting company) |
| Size-driven rules that apply | **OCC heightened standards**, 12 CFR Part 30, Appendix D: apply to a bank with average total consolidated assets of $50 billion or more (App. D I.A and I.E.5). The bank uses the parent's risk governance framework under App. D I.3 because its assets are 95% or more of the parent's (I.4), and documents that assessment every year. **Federal Reserve risk committee rule**, 12 CFR 252.22 (Regulation YY, subpart C): a bank holding company with average total consolidated assets of $50 billion or more (and less than $100 billion) must keep a board risk committee and a chief risk officer (252.21, 252.22). **Model risk guidance:** SR 26-2 (2026-04-17), the interagency revised model risk management guidance, which it says is most relevant to banking organizations with more than $30 billion in total assets |
| Primary regulation | Interagency Guidelines Establishing Information Security Standards as issued by the OCC, 12 CFR Part 30, Appendix B (GLBA section 501(b)), with Supplement A; the Federal Reserve's version for the parent is 12 CFR Part 225, Appendix F. Examined using the FFIEC Information Technology Examination Handbook |
| Other rules in scope | 12 CFR Part 30 Appendix D; 12 CFR Part 53 (bank) and 12 CFR Part 225 Subpart N (parent) incident notification; 12 CFR 252.22; SEC Form 8-K Item 1.05 and Regulation S-K Item 106 (parent); Regulation S-P, 17 CFR 248.30, and Regulation S-ID, 17 CFR 248.201 (broker-dealer and adviser); OCC identity theft red flags rule, 12 CFR 41.90 (bank); SAR rule, 12 CFR 21.11; ECOA and Regulation B for credit models, 12 CFR Part 1002; state breach notification laws |
| Not in scope, with reasons | **NYDFS 23 NYCRR Part 500:** no entity in the group holds a license, registration, or charter under the New York Banking Law, Insurance Law, or Financial Services Law, and the bank has no New York branch or office; the GRC team rechecks at every new product, license, or acquisition. **FTC Safeguards Rule, 16 CFR Part 314:** the bank is OCC-supervised and the broker-dealer and adviser are SEC-regulated; no subsidiary is a financial institution under FTC jurisdiction. **NAIC Model #668:** no insurance licensee. **FDIC rule 12 CFR 304.23 and NCUA 12 CFR 748.1:** not the primary regulator; not a credit union. **PCI DSS:** card data is processed by a card processor; the bank's issuer obligations are handled in the card program and noted, not assessed. **SOX section 404:** IT general controls over financial reporting are tested by the SOX program and not repeated here |

## 2. People (role titles only)
| Role | Security and compliance duties |
|---|---|
| Board of directors of the parent (the bank's board has the same members) | Approves the information security program and risk appetite statement (12 CFR 30 App. B III.A; App. D II.G.1); Item 106 board oversight disclosure |
| Board risk committee | Required by 12 CFR 252.22; chaired by an independent director. Oversees cybersecurity, technology, third-party, and model risk; receives the Chief Risk Officer's reports at least quarterly |
| Board audit committee | Oversees Internal Audit, SOX, and disclosure controls; approves the internal audit charter and plan (App. D I.E.8) |
| Chief Executive Officer (CEO); Chief Financial Officer (CFO) | Accept Very High risks jointly; take part in materiality determinations with the disclosure committee |
| Chief Risk Officer (CRO) | Chief Risk Executive under App. D and chief risk officer under 12 CFR 252.22; leads independent risk management (second line), including Technology and Operational Risk, Model Risk Management, and Third-Party Risk Management; reports to the CEO and the board risk committee |
| Chief Information Officer (CIO) | Leads technology (a front line unit under App. D I.E.6(a)(iii)); owns the common control providers for platform, network, and endpoints |
| Chief Information Security Officer (CISO) | Program owner for information security; designated by the board as responsible for the information security program (App. B III.A.2). **Reports to the CIO** (see gap 1) |
| Chief Audit Executive | Leads Internal Audit (third line); reports functionally to the audit committee; leads the P07 assessment |
| General Counsel | Chairs the disclosure committee |
| Chief Compliance Officer | Compliance risk management (second line); fair lending oversight with the Fair Lending Officer |
| Chief Privacy Officer | GLBA privacy notices, customer notice decisions, state breach law analysis |
| BSA/AML Officer | SARs and FinCEN filings; law enforcement liaison for fraud |
| GRC team (14), Technology and Operational Risk (second line, 22), Cyber Defense Center (24x7, in-house), Internal Audit (in-house, with a 9-person technology audit team) | Three lines model |
| Disclosure committee | Form 8-K materiality decisions: General Counsel (chair), CFO, Controller, CRO, CISO, Chief Privacy Officer, and Vice President, Investor Relations, advised by outside securities counsel |
| AI governance committee | Formed 2025; chaired by the Chief Data and Analytics Officer; reviews AI use cases (P10) |

## 3. Systems
| ID | System | Notes |
|---|---|---|
| SYS-01 | Core banking platform (deposits, loans, customer information file, general ledger feeds) | Licensed core software on a mainframe and distributed servers in the bank's two data centers (DC-1 in Florida, DC-2 in North Carolina). Bank-operated |
| SYS-02 | Digital banking platform (consumer and small business online and mobile banking, including wire, ACH, and person-to-person payment initiation) | Bank-built services on Cloud provider A (managed containers, managed databases) |
| SYS-03 | Payments hub (wire transfer, ACH, instant payments; connection to Federal Reserve payment services) | Licensed payments software in DC-1 and DC-2 with a dedicated wire operations room in Florida and an alternate site in Georgia |
| SYS-04 | Commercial treasury management platform (commercial online banking, wire and ACH initiation, positive pay, host-to-host and API channels) | Vendor-hosted SaaS, integrated with SYS-01 and SYS-03. The acquired bank's legacy commercial online banking platform (vendor-hosted) runs alongside it until 2027-02-26 |
| SYS-05 | Identity platform: workforce SSO, MFA, privileged access management (PAM), identity governance (IGA); customer identity and access management (CIAM) for digital banking | Mainframe access is controlled by the mainframe's own security product, outside IGA (see gap 5) |
| SYS-06 | Multi-cloud and data center estate: Cloud provider A (digital banking, API gateway, fraud analytics), Cloud provider B (enterprise data platform, machine learning platform, credit decisioning service), DC-1 and DC-2 | Vendor-agnostic; landing zones in both clouds |
| SYS-07 | Enterprise network, 610 branches, about 1,480 ATMs | SD-WAN; branch segmentation; ATM network managed with an ATM services vendor |
| SYS-08 | About 22,000 endpoints (workstations, laptops, teller and platform workstations, payments workstations) and about 6,800 servers | EDR on all managed endpoints and servers |
| SYS-09 | Loan origination systems (consumer, mortgage, small business, commercial) | Vendor SaaS; the consumer system calls the credit decisioning service (SYS-06, Cloud B) |
| SYS-10 | Card processing (debit and credit) | Card processor (bank service provider) |
| SYS-11 | Fraud and financial crime platforms (wire and payment fraud scoring, card fraud, AML transaction monitoring, case management) | Mix of vendor software on Cloud A and vendor SaaS |
| SYS-12 | ERP, general ledger, and financial reporting | SaaS; SOX-relevant |
| SYS-13 | Productivity suite (email, files, chat) | SaaS; used by commercial bankers and client service teams to exchange instructions with clients |
| SYS-14 | Broker-dealer and advisory systems | Clearing firm's brokerage platform (SaaS) and the adviser workstation; customer information of about 210,000 accounts |
| SYS-15 | AI portfolio (16 use cases) | Governed by the AI governance committee; models also in the model inventory of Model Risk Management |

Third parties: about 2,400, of which 460 have access to customer information and 41 are rated critical (including the card processor, the treasury management platform vendor, both cloud providers, the clearing firm, and the ATM services vendor).

**SSP system (P02):** the *Core Banking and Digital Channels Platform (CBDC)*: SYS-01 core banking platform in DC-1 and DC-2, SYS-02 digital banking platform on Cloud provider A (including its wire and ACH initiation services), the customer identity service (CIAM) and workforce identity controls from SYS-05 as they protect these systems, the API and integration layer that connects digital banking to the core, and the interfaces to the payments hub (SYS-03), the treasury management platform (SYS-04), and the fraud platforms (SYS-11).

## 4. Current security posture: mature, with residual gaps
**In place today:**
- A mature information security program aligned to NIST CSF 2.0, approved by the board each year (last 2026-01-27), with an annual report to the board risk committee (App. B III.F)
- A board-approved risk appetite statement with qualitative statements and quantitative cyber limits (App. D II.E), reviewed each January
- Annual enterprise cyber risk assessment tied to ERM (NIST IR 8286)
- A policy hierarchy of policies, standards, procedures, and an exceptions register
- A 24x7 Cyber Defense Center with SIEM, EDR, and threat intelligence
- PAM for distributed and cloud administration; quarterly access certification in IGA
- Immutable backups in both clouds and for distributed systems in the data centers
- Annual disaster recovery tests for tier-1 systems, including a DC-1 to DC-2 failover of the core
- A third-party risk management program with tiering, due diligence, and SOC report reviews
- A materiality playbook and a disclosure committee; Item 106 disclosure in the 10-K
- 12 CFR 53.3 and 225.302 determination criteria in the incident response plan
- A wire callback standard for any wire request received by email or phone, run by a central callback team
- Independent model validation by Model Risk Management for credit models

**Residual gaps found in 2026:**
1. **Independence of cyber risk oversight.** The cyber risk oversight team, which the Chief Risk Officer relies on as second-line challenge for cybersecurity, sits inside the CISO's organization, and the CISO reports to the CIO, a front line unit executive. App. D says no front line unit executive should oversee an independent risk management unit (I.E.7(d)).
2. **Third parties and concentration.** 9 of the 41 critical third-party contracts (5 inherited from the acquired bank) have no incident notice time frame and no designated 12 CFR 53.4 contact. SOC report reviews are late for 7 critical third parties, and complementary user entity controls (CUECs) are mapped for 29 of 41. The treasury management platform vendor and the card processor are single points of failure.
3. **Legacy commercial online banking.** About 2,900 business clients of the acquired bank still use its legacy platform, which uses SMS one-time passcodes, has no out-of-band confirmation of new wire beneficiaries, and sends only login events to the SIEM.
4. **Payment fraud controls.** Out-of-band confirmation of new beneficiaries on the main treasury platform is required only for wires of $100,000 or more. Callback evidence was missing for 4 of 60 sampled branch-originated wire requests.
5. **Legacy core access and logging.** Privileged mainframe access and core maintenance transactions (address, phone, and email changes; beneficiary and limit changes made by staff) are logged in the core, but only security events reach the SIEM, and mainframe entitlements are certified outside IGA.
6. **Broker-dealer Regulation S-P.** The amended Regulation S-P (in force for the broker-dealer since 2025-12-03) requires service providers to give notice within 72 hours; 14 of 31 broker-dealer service provider contracts lack that term.
7. **AI and models.** 16 AI use cases; 12 have completed AI governance committee review. The AI credit underwriting model (AI-001) was validated by Model Risk Management, but fair lending testing for the credit card segment is incomplete and 3 of its 40 reason codes are too general for Regulation B adverse action notices. Generative AI use cases, which SR 26-2 excludes from its scope, have only a draft governance standard.
8. **Cyber vault.** Core banking data is replicated from DC-1 to DC-2 and backed up to virtual tape, but there is no logically isolated, immutable copy of core data (cyber vault planned for 2027).

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P08 | Business email compromise and fraudulent wire transfers affecting several commercial clients, including a compromised bank mailbox in commercial client services. The runbook includes the 12 CFR 53.3 and 225.302 notification incident determination, the SAR steps, and an **SEC materiality assessment and Form 8-K Item 1.05** step |
| P09 | SOC 2 Type 2 readiness across two service lines offered to institutional clients: SL-1 commercial treasury management and payments services (SOC 2 Type 2 since 2025 for Security and Availability) and SL-2 institutional trust, custody, and retirement plan services (SOC 1 Type 2 today; first SOC 2 planned) |
| P10 | Enterprise AI portfolio (16 use cases), with a full assessment of AI-001, the machine learning credit underwriting model for consumer unsecured personal loans and credit cards |
| Cloud | Multi-cloud (two public cloud providers, vendor-agnostic) plus two bank data centers, with common controls |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-05-04 to 2026-07-10 | Enterprise cyber risk assessment and regulatory gap analysis (GRC team and Technology and Operational Risk) |
| 2026-06-15 to 2026-08-14 | Control assessment of the CBDC platform and its common controls (Internal Audit) |
| 2026-08-19 | AI governance committee portfolio review |
| 2026-09-15 | Results to the board risk committee and the audit committee; board risk committee approves POL-01 |
| 2026-09-18 | Executive risk committee approves POL-02 to POL-05, risk treatments, the CBDC authorization decision, and AI decisions |

## 7. Facts added for the deliverables
These facts were added while building the deliverables. They do not change sections 1 to 6.

**Additional roles (titles only).**
| Role | Duties in the deliverables |
|---|---|
| Chief Operating Officer (COO) | Business owner for banking operations; authorizing official for the CBDC platform (P02); chairs the crisis management team |
| Head of Consumer and Small Business Banking | Business owner of digital banking and branches |
| Head of Consumer Lending | Business owner of AI-001 |
| Head of Commercial Banking | Commercial client relationships |
| Head of Treasury Management | SYS-04 and the SL-1 service line |
| Head of Payments Operations | Wire operations room, callback team, ACH and instant payments operations |
| Head of Wealth and Institutional Services | SL-2 service line; trust and custody |
| President, Cris Santos Investment Services | Broker-dealer and adviser; its Chief Compliance Officer runs its Regulation S-P and S-ID programs |
| Chief Data and Analytics Officer | Chairs the AI governance committee; owns the data and machine learning platforms |
| Head of Model Risk Management | Second line; model inventory and independent validation (SR 26-2) |
| Fair Lending Officer | Fair lending testing (reports to the Chief Compliance Officer) |
| Director of Technology and Operational Risk | Second line; cyber and technology risk under the CRO |
| Director of Third-Party Risk Management | Second line; vendor tiering, due diligence, SOC report reviews |
| Director of Cyber Defense | Runs the 24x7 Cyber Defense Center; incident commander |
| Director of Identity and Access Management | SYS-05 |
| Director of Cloud Platform Engineering | Landing zones in both clouds (common control provider) |
| Director of Data Center and Mainframe Operations | DC-1, DC-2, and the mainframe (common control provider) |
| Director of Network Engineering | Enterprise network and SD-WAN (common control provider) |
| Director of Endpoint Engineering | Endpoints and EDR (common control provider) |
| Director of Enterprise Resilience | Business continuity and disaster recovery program |
| Head of Core Banking Technology | System owner's technical lead for SYS-01 |
| Head of Digital Banking Technology | Technical lead for SYS-02 |
| Director of Fraud Strategy | Fraud rules and models; payment fraud controls |
| Controller | SOX program owner; member of the disclosure committee |
| Chief Human Resources Officer | Onboarding, terminations, training records |
| Vice President, Integration Management Office | Integration of the acquired bank |
| Vice President, Investor Relations | Investor communications; disclosure committee member |
| Head of Corporate Communications | Media and customer communications during incidents |

**Business volumes used for impact values.** Treasury management fees and commercial deposit spread about $1.6 million per business day. Card interchange about $1.2 million per business day. The broker-dealer earns about $0.9 million in revenue per business day.

**Board.** 13 directors, 11 independent. The board risk committee has 5 independent directors, one with experience managing risk at large, complex financial firms (252.22(a)(4)).

**Regulatory contacts.** The OCC's supervisory office for the bank and the Federal Reserve Bank that supervises the parent each gave the group an email and telephone point of contact for 12 CFR 53.3 and 225.302 notices; both are in the incident binder.

**Platform and program facts used in P02, P03, P07, P09, and P10.**
| Fact | Value |
|---|---|
| CBDC users | About 9,800 workforce users with core roles; about 310 privileged administrators on distributed and cloud components; 41 mainframe IDs with standing privileges; 214 service accounts on CBDC components; about 3.9 million deposit accounts |
| Core middleware | 48 distributed servers in DC-1 and DC-2 (4 on an operating system in vendor extended support until 2027-03-31) |
| Treasury activity (2026-01 to 2026-06) | 18,400 new wire beneficiaries added; 2,940 branch-originated email or phone wire requests; about 120 corporate clients on host-to-host and API channels |
| Commercial client service staff | About 640 staff who exchange payment instructions with clients |
| Consumer authentication | 23% of consumer digital users still use SMS one-time passcodes |
| Broker-dealer service providers | 31 with customer information (including the clearing firm) |
| AI-001 volumes (2026-03-02 to 2026-08-14) | 118,400 applications scored (101,300 personal loans; 17,100 credit cards in a pilot at 15% of digital card applications) |
| Service line SL-2 | Trust, custody, and retirement plan recordkeeping; SOC 1 Type 2 report issued each year; participant portal MFA enrollment 72% |

