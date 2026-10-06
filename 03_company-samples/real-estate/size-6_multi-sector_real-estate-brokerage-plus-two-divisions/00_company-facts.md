# Scenario facts: Cris Santos Company | Real Estate and Rental and Leasing | Multi-Sector

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or rule, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company Holdings, Inc. (publicly traded SEC registrant; Delaware holding corporation headquartered in Florida) |
| Structure | A holding company with three divisions and corporate shared services. Each division is one or more legally separate subsidiaries (section 7) |
| Division 1: Residential Brokerage (NAICS 531210), **focus of this scenario** | Residential sales brokerage, property management and leasing of single-family rentals, and relocation services. About 13,000 employees plus about 52,000 licensed sales associates who are **independent contractors**, not employees |
| Division 2: Mortgage and Title (NAICS 522292 real estate credit and 524210 for the title agency, sector 52 Finance and Insurance) | A nonbank mortgage lender (retail origination; loans sold servicing-released) and a title insurance agency that also acts as settlement (closing) agent. About 11,000 employees. Both subsidiaries are **financial institutions under the FTC Safeguards Rule** (16 CFR 314.2(h)(2)(x) settlement services; lending under 12 CFR 225.28(b)(1)) |
| Division 3: Homebuilding (NAICS 236117, sector 23 Construction) | Builds and sells single-family homes in planned communities. About 16,000 employees (land, construction, purchasing, sales, design studios, warranty). About 9,500 trade partners (subcontractors and suppliers). No federal contracts |
| Corporate shared services | Identity, email and collaboration, security operations, cloud platform, treasury and payments, data platform, HR, finance, legal, internal audit. About 5,000 employees |
| Location | Headquartered in Florida. The brokerage and the mortgage lender operate in **8 southeastern states**; the title agency in 7 of them; homebuilding in 5 of them. No offices, licenses, or marketing in California or New York. **State law is handled generically** ("each state where affected individuals reside"), with Florida as the worked example |
| Workforce | 45,000 employees: Residential Brokerage 13,000; Mortgage and Title 11,000; Homebuilding 16,000; corporate shared services 5,000. Plus about 52,000 contractor sales associates |
| Revenue | $18.0 billion in annual receipts (fictional): Homebuilding $8.0 billion; Residential Brokerage $7.4 billion (gross commission income, before agent splits); Mortgage and Title $2.6 billion (mortgage $1.5 billion; title and settlement $1.1 billion). Above the SBA standard of $15.0 million for NAICS 531210 (13 CFR 121.201), so not SBA-small |
| Why this combination | A real estate group from build to sale to financing: Homebuilding builds the homes, the brokerage sells new and resale homes, Mortgage and Title finances and closes them. Affiliated referrals between divisions are **affiliated business arrangements** under RESPA (12 CFR 1024.15) |

## 2. People (role titles only)
| Role | Security and compliance duties |
|---|---|
| Board of directors: audit committee and risk committee | The risk committee oversees cyber risk and accepts Very High risks; the audit committee oversees group internal audit and SEC disclosure controls |
| Boards of directors of the mortgage and title subsidiaries | Governing bodies of the two financial institutions; each receives the Qualified Individual's annual written report (16 CFR 314.4(i)) |
| Chief Executive Officer; Chief Financial Officer | Chair the disclosure committee with the Group General Counsel |
| Group CISO | Owns the group security program and common controls; **Qualified Individual** for both financial institution subsidiaries (16 CFR 314.4(a)), employed by the parent, an affiliate of each |
| Group Chief Risk Officer | Owns the group risk register and the enterprise risk roll-up (NIST IR 8286 Rev. 1); co-accepts High risks |
| Group Chief Privacy Officer | Data classification, affiliate data sharing, consumer report and fair lending data handling |
| Group General Counsel | Notification matrix, intercompany agreements, RESPA affiliated business compliance, SEC disclosure counsel |
| Group Treasurer | Group treasury and payments hub (SYS-G5); banking relationships for escrow, trust, operating, and trade partner accounts |
| Division presidents (3) | Accept Moderate risks for their divisions |
| Division security and compliance leads (3) | Division registers, division supplements, division regulators; accept Low risks |
| President, Mortgage; President, Title | Each is the senior member of its subsidiary designated to direct and oversee the Qualified Individual (16 CFR 314.4(a)(2)) |
| Broker of Record in each state (licensed brokers; the Florida Broker of Record is a division officer) | Escrow account signatory and real estate commission duties, including escrow dispute notices (Fla. Admin. Code r. 61J2-10.032) |
| Managing brokers (about 640) | Supervise sales associates; request onboarding and offboarding |
| Group internal audit | Assesses common controls once and samples division controls; reports to the audit committee |
| Disclosure committee | SEC materiality decisions (Form 8-K Item 1.05) |
| Group AI council | Approves High-tier AI use cases (P10) |

## 3. Systems
| ID | System | Owner | Holds customer information or NPI? |
|---|---|---|---|
| SYS-G1 | Group identity platform (workforce SSO, MFA, PAM, identity governance) with a separate contractor agent identity tier | Corporate | Identities only |
| SYS-G2 | Group SOC, SIEM, and EDR (24x7) | Corporate | Security logs |
| SYS-G3 | Group cloud platform (two providers, vendor-agnostic) and the Group Data Platform (analytics) | Corporate | Yes |
| SYS-G4 | Group email and collaboration suite (SaaS), used by all employees and all contractor agents. The main business email compromise target | Corporate | Yes |
| SYS-G5 | Group treasury and payments hub: bank connectivity for wires and ACH from all escrow, trust, operating, and trade partner accounts; positive pay; payee verification service | Corporate (Group Treasurer) | Yes |
| SYS-B1 | Transaction management platform (contracts, compliance review, document storage, agent and client portal) | Residential Brokerage | Yes |
| SYS-B2 | Closing Communications Portal (company-built web application that delivers closing documents and wire instructions to buyers and sellers) | Residential Brokerage (product owner); Title (co-data owner) | Yes |
| SYS-B3 | Brokerage CRM, listing, and agent services platform with buyer lead scoring | Residential Brokerage | Yes |
| SYS-B4 | Property management platform with tenant portal, rent payments, and integrated tenant screening | Residential Brokerage | Yes (consumer reports) |
| SYS-M1 | Mortgage loan origination system, borrower point-of-sale portal, pricing engine, and automated valuation model (AVM) integration | Mortgage and Title | Yes |
| SYS-M2 | Title production and escrow accounting system (settlement statements, disbursement ledger, positive pay files) | Mortgage and Title | Yes |
| SYS-H1 | Homebuilding ERP (land, purchasing, construction scheduling, trade partner payments), vendor software on the group cloud platform | Homebuilding | Limited (trade partner bank data) |
| SYS-H2 | Homebuilding sales, design studio, and warranty platforms, and the smart-home device management platform | Homebuilding | Yes (buyer data) |
| SYS-H3 | Sales center and jobsite networks, cameras, and access control | Homebuilding | No |

**SSP system (P02):** the *Transaction Management and Closing Communications System (TMCC)*: the shared system that carries a residential sale from signed contract to disbursed funds across the Residential Brokerage and Mortgage and Title divisions: SYS-B1, SYS-B2, the TMCC integration service, and their interfaces to SYS-M2 (title production), SYS-G5 (payee verification and wire release), SYS-G4 (email), and the e-signature service. It inherits common controls from SYS-G1 to SYS-G5.

## 4. Current security posture: defined group program, maturity varies by division
**In place today:**
- Group policies (2025) aligned to NIST CSF 2.0 and to the FTC Safeguards Rule elements; a common control catalog
- 24x7 group SOC with EDR on all company endpoints and servers
- Phishing-resistant MFA for administrators and for all staff who release or approve wires; app-based MFA for all employees on SYS-G1
- PAM with just-in-time elevation and session recording
- Quarterly access certification for employees
- Title wire controls: the Closing Communications Portal is the only channel for title wire instructions (since 2022); callback to a verified number before any title wire to a new payee or changed account; dual approval on every trust account wire; positive pay on all escrow and trust accounts
- Immutable backups of group cloud workloads in provider B
- Annual penetration tests of internet-facing applications; monthly authenticated vulnerability scans
- The Qualified Individual reports annually in writing to the boards of both financial institution subsidiaries
- Reg S-K Item 106 disclosure in the annual report; a disclosure committee charter that covers cybersecurity incidents
- Cyber insurance with a funds transfer fraud and social engineering sublimit

**Missing or weak, found in the 2026 assessments:**
1. **Contractor agent identities.** About 9,900 of the 52,000 contractor sales associates (19%) still sign in to email (SYS-G4) and the transaction platform (SYS-B1) with a password only, under an exception that expired 2026-06-30. Departing agents keep access for a median of 4 days (up to 31) because managing brokers report departures late. Agents use personal devices.
2. **Payee verification is uneven across divisions.** Title verifies payees out of band; the brokerage's escrow refund wires, property management owner payout changes, and agent commission account changes do not; Homebuilding accepts trade partner bank account changes by email with one approver.
3. **Application logs are not monitored.** Audit logs from SYS-B1, SYS-M2, and SYS-H1 do not reach the SIEM, and nothing alerts on payee or bank account changes in those systems.
4. **Affiliate data flows are not governed.** Buyer leads and files move between the brokerage CRM, the homebuilding sales platform, and the mortgage loan origination system through point-to-point APIs and the Group Data Platform. Data sharing purposes, consent records, and retention are not documented, and brokerage-only data is mixed with Safeguards Rule customer information in the Group Data Platform.
5. **Homebuilding is not fully on group common controls.** It still runs its legacy email tenant and directory for about 3,800 field and sales users (migration to SYS-G1 and SYS-G4 due 2027-03-31). Common control inheritance is documented for the Brokerage and Mortgage and Title divisions, not for Homebuilding, and Homebuilding has no division policy supplement.
6. **AI governance lags deployment.** Tenant screening recommendations (brokerage), a pre-qualification model, and an AVM used in credit decisions (mortgage) are in production. The AVM quality control policy required by 12 CFR 1026.42(i) was adopted in 2025, but no random sample testing or nondiscrimination review has been done; tenant screening outcomes have never been tested for disparities.
7. **The multi-regulator notification matrix has not been exercised.** One incident can trigger FTC notices from two financial institutions, state breach notices in 8 states, state insurance regulator notices for the title agency where a state has enacted NAIC Model #668, investor contract notices, and an SEC materiality decision.
8. **Smart-home handover.** Homebuilding keeps administrator access to the smart-home hubs of about 3,100 closed homes because handover was not completed, and hubs installed in 2023 and 2024 shipped with a shared installer passcode.
9. **Retention.** No disposal schedule is enforced. Title keeps scanned closing files from 2006 to 2015 on a file server, and the brokerage keeps transaction files indefinitely (16 CFR 314.4(c)(6)).

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P08 | Business email compromise targeting closing funds (registry default, kept because it is the group's top risk). It spans divisions: a contractor agent's mailbox is taken over on a new-home sale built by Homebuilding, financed by the mortgage subsidiary, and closed by the title subsidiary; altered wire instructions reach buyers, and the mailbox holds customer information of both financial institutions. A variant covers a trade partner bank change fraud at Homebuilding |
| P09 | SOC 2 scoping per division: the title subsidiary's closing and escrow disbursement services are in scope (lenders and outside homebuilders ask for a Type 2 report); the brokerage, the mortgage lender, and Homebuilding are out of scope with reasons; a vendor SOC report review covers the key SaaS providers of every division |
| P10 | Group AI governance program built around the registry default "Automated tenant and buyer screening": tenant screening (brokerage) and buyer pre-qualification and the AVM (mortgage) are the priority use cases, with the regulator-specific rules for each |
| Primary system | Registry default kept: the Transaction Management and Closing Communications System, as a shared system of the Brokerage and Mortgage and Title divisions |
| Cloud | Shared corporate platform on two providers (vendor-agnostic) plus division workloads |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-05-04 to 2026-07-24 | Group and division BIAs, risk analyses, and gap analyses |
| 2026-07-06 to 2026-08-28 | Common control assessment (group internal audit) plus division samples |
| 2026-09-17 | Results to the board risk committee; deliverables approved; Qualified Individual's annual reports to the mortgage and title subsidiary boards |
| 2026-10-06 | FinCEN residential real estate rule and HUD disparate impact proposals rechecked before publication |

## 7. Supporting facts (fictional; used across P01 to P10)
| Topic | Fact |
|---|---|
| Legal entities | Cris Santos Company Holdings, Inc. (parent; employs corporate shared services staff and the Group CISO). Cris Santos Realty, LLC (brokerage; registered with the real estate commission of each state). Cris Santos Home Loans, LLC ("Home Loans"; nonbank mortgage lender licensed in 8 states; Florida license under Fla. Stat. 494.00611). Cris Santos Title, LLC ("Title"; licensed title insurance agency and settlement agent in 7 states). Cris Santos Homes, Inc. (homebuilder). The parent provides IT, security, and treasury services to every subsidiary under a 2021 intercompany services agreement that has no security or audit terms |
| Brokerage volume | About 170,000 closed transaction sides a year (about 680 per business day). The brokerage holds earnest money in its own escrow accounts in about 41,000 transactions a year (about $1.4 billion in deposits); title companies or attorneys, including Title, hold the rest |
| Property management | About 21,000 rental homes for about 14,000 owners in 5 states. About 68,000 rental applications a year are screened. Owner distributions are paid by ACH each month |
| Mortgage volume | About 58,000 loans funded a year (about $19.5 billion), from about 150,000 applications. Loans are sold servicing-released to investors. Home Loans holds customer information on about 1.3 million consumers (applications since 2019). About 78% of Homebuilding buyers and 14% of brokerage buyers finance with Home Loans |
| Title volume | About 128,000 closings a year (about 510 per business day): 58% for the brokerage's transactions, 15% for Homebuilding, and the rest for outside lenders, brokerages, and builders. About 640,000 outgoing disbursement wires a year (about 2,560 per business day; about $52 billion a year, about $208 million per business day) from title escrow trust accounts at 4 banks. Title holds customer information on about 2.4 million consumers |
| Homebuilding volume | About 19,000 homes closed a year in about 310 active communities. About $5.8 billion a year paid to about 9,500 trade partners by ACH through SYS-G5. Florida buyer deposits (up to 10 percent of the price) are escrowed at a bank unless the buyer waives in writing (Fla. Stat. 501.1375(2)-(3)). Design studios take card deposits for options through a payment processor's hosted payment page |
| Smart-home program | Since 2023 every new home ships with a smart-home package (hub, smart lock, thermostat, video doorbell) managed in SYS-H2. About 38,000 homes have it. The builder holds a community administrator role until the buyer activates the home at closing |
| Contractor agents | About 52,000 contractor sales associates; about 11,000 left and 12,500 joined in the 12 months to 2026-06-30. Agents use group email (SYS-G4), SYS-B1, and SYS-B3 from about 90,000 personal laptops and phones |
| Banks and treasury | Escrow and trust accounts at 6 banks, all connected through SYS-G5. All offer positive pay and dual approval. Wire release for trust accounts requires hardware-key MFA |
| Cyber insurance | $100 million tower; $5 million retention; $10 million sublimit for funds transfer fraud and social engineering. Panel breach counsel and forensics; notice to the carrier comes before vendors are engaged |
| Fraud history | In the 12 months to 2026-06-30, staff stopped 412 attempted payee changes across divisions. Losses: $1.9 million in 9 brokerage and title events (deposit and proceeds wires); $1.1 million in 2 Homebuilding trade partner bank change frauds (2025-11 and 2026-02). $1.3 million recovered |
| Affiliate referrals | The brokerage and Homebuilding refer buyers to Home Loans and Title. An Affiliated Business Arrangement Disclosure Statement is given at referral (12 CFR 1024.15(b)(1)). Leads move by API from SYS-B3 and SYS-H2 to SYS-M1 |
| Out of scope by fact | No federal contracts (FAR 52.204-21 and CMMC do not apply to Homebuilding). No bank charter. No New York licenses (NYDFS Part 500 does not apply). No California operations (CCPA/CPRA business status reviewed each year by the Group General Counsel; GLBA data is exempt at the data level, Cal. Civ. Code 1798.145(e)). Home Loans does not service loans. The group stores, processes, and transmits no card data in its own systems (rent and design studio card payments use processors' hosted pages) |
| Insurance data security law | Title is an insurance licensee in 7 states. Some states of operation have enacted a version of NAIC Model #668; their requirements are tracked by the Title compliance officer. Florida has not enacted Model #668 (Florida Statutes chapters 624 to 628 contain no cybersecurity event provision, as searched on 2026-10-05) |
| Risk acceptance | Low: division security and compliance lead. Moderate: division president. High: Group Chief Risk Officer with the Group CISO, reported to the board risk committee. Very High: board risk committee only. Risks to customer funds rated High must be treated, not accepted |
| FinCEN residential real estate rule | 31 CFR 1031.320 was vacated by the U.S. District Court for the Eastern District of Texas on 2026-03-19; FinCEN and the Department of Justice appealed; reporting persons are not required to file while the order is in force (FinCEN website checked 2026-10-06). If restored, it would reach Title as the settlement agent, not the brokerage |
| AI use cases (P10) | Tenant screening recommendations (SYS-B4), buyer lead scoring (SYS-B3), generative AI listing descriptions, mortgage pre-qualification model and AVM (SYS-M1), identity verification for closings and wire anomaly scoring (Title and SYS-G5), construction schedule optimization (SYS-H1), and an enterprise generative AI assistant piloted with 3,000 employees |
