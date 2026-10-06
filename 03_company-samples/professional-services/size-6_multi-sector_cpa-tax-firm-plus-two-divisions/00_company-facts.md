# Scenario facts: Cris Santos Company | Professional, Scientific, and Technical Services | Multi-Sector

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, IRS publication, or standard, the citation is given; each citation was read from the primary source (eCFR current through 2026-09-23, the Federal Register, or irs.gov) for this sample or for the verified Small sample of this industry.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company Holdings, Inc. (publicly traded SEC registrant; parent of the tax and advisory, wealth management, and software businesses. Its attest practice is a separate CPA partnership that the public company does not own; see "Ownership of the attest practice") |
| Structure | A holding company with three divisions and corporate shared services. Each division is one or more legal entities owned by the holding company, except the attest firm described below |
| Division 1: CPA and Tax Services (NAICS 541211), **focus of this scenario** | (a) **Cris Santos Tax and Advisory, LLC** ("Tax and Advisory"), a wholly owned subsidiary: assisted individual and business income tax preparation, tax planning, IRS and state notice representation, and client accounting services (outsourced bookkeeping and payroll for small businesses). (b) **Cris Santos CPA Partners, LLP** ("CPA Partners"), the affiliated licensed CPA firm that performs attest work: financial statement audits and reviews of private companies, nonprofits, and employee benefit plans, and SOC 1 and SOC 2 examinations for outside service organizations. About 28,500 employees, including about 2,800 attest professionals who are employed by Tax and Advisory and leased to CPA Partners. About 11,000 seasonal tax professionals join from January to April as temporary employees and are not counted |
| Ownership of the attest practice | A CPA firm that performs attest work is a partnership owned by licensed CPAs, so it cannot be a subsidiary of a public company in the usual way. The group uses an **alternative practice structure**: CPA Partners is owned by its 410 CPA partners, is licensed by the state boards of accountancy where it practices, and buys staff, offices, and technology from the holding company under a 2021 administrative services agreement. **CPA Partners is not publicly traded and is not PCAOB-registered**; it audits no SEC issuer, and it does not audit or examine the holding company or any group entity. State firm-ownership rules vary; group legal confirms them state by state |
| Division 2: Wealth Management (NAICS 523940, sector 52 Finance and Insurance) | **Cris Santos Wealth Advisors, LLC** ("Wealth"), an **SEC-registered investment adviser**. About $540 billion regulatory assets under management for about 980,000 client households. About 6,500 employees, including about 3,100 financial advisers. Client assets are held by three unaffiliated qualified custodians. No broker-dealer, bank, trust company, or insurance company in the group |
| Division 3: Practice Management Software (NAICS 513210, sector 51 Information) | **Cris Santos Practice Cloud, Inc.** ("Practice Cloud"): a multi-tenant SaaS product for accounting and tax firms (client portal with secure document exchange and e-signature, including IRS Form 8879; document management; workflow; time and billing; invoice payment through a payment processor's hosted page). About 26,000 outside customer firms nationwide, plus Tax and Advisory and CPA Partners as internal tenants. About 5,500 employees. Issues an annual SOC 2 Type 2 report |
| Corporate shared services | Identity, security operations, cloud and network, email and collaboration, HR, finance, legal, privacy, and group internal audit. About 4,500 employees, employed by the holding company |
| Location | Headquartered in Florida. Tax and Advisory has about 1,150 tax offices and 58 advisory offices in 31 states; Wealth has advisers in 40 states; Practice Cloud customers are nationwide. **State law is handled generically** ("each state where affected individuals reside"), with Florida as the worked example |
| Workforce / revenue | 45,000 employees; about $18.0 billion revenue (fictional) |
| GLBA status by entity | **Tax and Advisory** is a financial institution under the FTC Safeguards Rule: 16 CFR 314.2(h)(2)(viii) names "an accountant or other tax preparation service that is in the business of completing income tax returns", and its individual tax clients are customers (314.2(e)(2)(i)(H)). It holds customer information on far more than 5,000 consumers, so the 314.6 exception does not apply. **Wealth** is a covered institution under SEC Regulation S-P (17 CFR 248.30(d)(3): an investment adviser registered with the Commission), not under the FTC rule. **Practice Cloud** is treated as a service provider to its customer firms (16 CFR 314.4(f)), not as a financial institution (group legal position, section 7) |
| IRS status | Tax and Advisory is an Authorized IRS e-file Provider acting as an Electronic Return Originator (ERO); every preparer holds a PTIN. Returns are transmitted through the tax engine vendor, itself an Authorized IRS e-file Provider. The group sells no do-it-yourself tax software to the public |
| Not in scope | FAR 52.204-21, DFARS 252.204-7012, and CMMC: no federal contracts or subcontracts in any division. ABA Model Rules: no law practice. PCAOB: CPA Partners audits no issuers. NYDFS Part 500: no group entity is licensed by the New York Department of Financial Services. CIRCIA: proposed rule only. Payment cards: client payments run through payment processors' hosted pages and are outside group systems |

## 2. People (role titles only)
| Role | Security and compliance duties |
|---|---|
| Board risk committee (holding company) | Group cyber and enterprise risk oversight; approves group policies; accepts Very High risks |
| Board audit committee (holding company) | Oversees group internal audit |
| Disclosure committee | Chaired by the Group Chief Financial Officer. Decides SEC materiality of cybersecurity incidents (Form 8-K Item 1.05) |
| Group CISO | Owns the group information security program and group policies; operates common controls (SYS-G1 to SYS-G4). Designated in writing as Tax and Advisory's **Qualified Individual** under 16 CFR 314.4(a). Because the Group CISO is employed by the holding company (an affiliate of Tax and Advisory), 314.4(a)(1) to (3) apply |
| Group Chief Risk Officer | Owns the group risk register and the enterprise risk roll-up (NIST IR 8286 Rev. 1); co-accepts High risks; chairs the Group AI council |
| Group Chief Privacy Officer | Data classification, permitted-purpose rules, IRC 7216 consent program design with the Chief Tax Officer |
| Group General Counsel | Intercompany agreements, customer contracts, and the group notification matrix |
| Chief Audit Executive (group internal audit) | Reports to the board audit committee. Assesses common controls once and samples division controls |
| Tax and Advisory board of managers | Tax and Advisory's governing body for the Qualified Individual's annual written report (16 CFR 314.4(i)) |
| Tax division president | Senior member of Tax and Advisory responsible for direction and oversight of the Qualified Individual (314.4(a)(2)); accepts Moderate risks for the division |
| Chief Tax Officer | Owns the tax practice, the e-file program (Responsible Official for the EFINs), and the IRC 7216 consent process; business owner for the tax AI use cases |
| Tax division security and compliance lead | Division supplement and division risk register; day-to-day Safeguards Rule program management for Tax and Advisory |
| Client accounting services director | Owns the bookkeeping and payroll service line |
| Seasonal workforce director | Hiring, onboarding, and offboarding of seasonal tax professionals |
| CPA Partners managing partner | Leads the attest firm; signs the administrative services agreement |
| CPA Partners risk and quality partner | Quality management, independence, and engagement acceptance; security liaison to the group |
| Wealth division president | Accepts Moderate risks for Wealth |
| Wealth Chief Compliance Officer | Administers Wealth's compliance policies and procedures (17 CFR 275.206(4)-7(c)), including the Regulation S-P program and the Identity Theft Prevention Program (17 CFR 248.201) |
| Wealth security and compliance lead | Division supplement and division risk register |
| Practice Cloud division president | Accepts Moderate risks for Practice Cloud |
| Practice Cloud CISO | Division security lead (the division has its own CISO because it issues SOC 2 reports to customers) |
| Practice Cloud trust and assurance director | SOC 2 report, customer due diligence, customer security notices |
| Practice Cloud chief technology officer | Product engineering and the AI document intake feature |

## 3. Systems
| ID | System | Owner | Hosting |
|---|---|---|---|
| SYS-G1 | Group identity platform (single sign-on, MFA, privileged access management, identity governance) | Corporate | Identity SaaS vendor |
| SYS-G2 | Group SOC, SIEM, EDR, and email security gateway | Corporate | SIEM and EDR SaaS vendors; 24x7 group SOC |
| SYS-G3 | Group cloud platform (landing zones in two public cloud providers, called provider A and provider B), the office network (SD-WAN to about 1,210 offices), and the immutable backup vault | Corporate | Providers A and B; carriers |
| SYS-G4 | Group email and collaboration suite (one tenant for all divisions and seasonal staff) | Corporate | Productivity SaaS vendor |
| SYS-T1 | Tax preparation and e-file platform: a licensed professional tax engine deployed in the Tax division's provider A accounts, in-house preparer workflow and review tools, the return data store, the e-file gateway to the tax engine vendor's transmitter, the AI document extraction service, and the referral interface to SYS-W1 | Tax and Advisory | Provider A |
| SYS-T2 | Client accounting services platform (bookkeeping ledger and payroll SaaS with bank feed connectors) | Tax and Advisory | Vendor SaaS |
| SYS-T3 | Attest engagement platform (audit and SOC workpaper application and engagement file store) used by CPA Partners | CPA Partners (operated by Tax division IT under the administrative services agreement) | Provider A |
| SYS-W1 | Wealth platform: adviser CRM, portfolio management and trading, planning software, custodian data feeds, client portal, and an integration hub | Wealth | Vendor SaaS; integration hub in provider A |
| SYS-S1 | Practice Cloud (multi-tenant): client portal and e-signature, document management, workflow, billing, and the AI document intake feature | Practice Cloud | Provider B (primary region and a warm standby region) |

**SSP system (P02):** the *Tax Preparation and Client Portal Platform (TPCP)*: the SYS-T1 tax preparation and e-file platform, the Tax and Advisory tenant of SYS-S1 Practice Cloud (client document exchange, Form 8879 e-signature, and return delivery), and the referral interface that sends integrated planning data to SYS-W1; it inherits common controls from SYS-G1 to SYS-G4 and service provider controls from the Practice Cloud division.

## 4. Current security posture: defined group program, gaps where divisions meet
**In place today:**
- One group information security program aligned to CSF 2.0, with group policies approved by the board risk committee
- Group CISO designated in writing (2025-02-03) as Tax and Advisory's Qualified Individual, with a written annual report to the Tax and Advisory board of managers since 2024 (16 CFR 314.4(i))
- A common control catalog for SYS-G1 to SYS-G4
- 24x7 group SOC; EDR on all endpoints and cloud workloads; SIEM; email security gateway
- Privileged access management with just-in-time elevation; phishing-resistant MFA for administrators; number-matching MFA for the permanent workforce
- Quarterly access certification for permanent staff
- Immutable backups in provider B, with quarterly restore tests for High-criticality systems
- Annual penetration tests of SYS-T1 and SYS-S1 and continuous vulnerability scanning (the 16 CFR 314.4(d)(2)(i) and (ii) alternative)
- Wealth's Regulation S-P incident response and service provider program, adopted 2025-11-17, before the 2025-12-03 compliance date for larger entities
- Practice Cloud SOC 2 Type 2 report (Security, Availability, Confidentiality) for the 12 months ending September 30, issued each year by an unaffiliated CPA firm
- Weekly EFIN and PTIN return-volume checks during the filing season
- Written IRC 7216 consent templates, with consent captured in the client portal before lender and other third-party releases
- Reg S-K Item 106 disclosure, and a disclosure committee charter that covers cybersecurity incidents

**Gaps:**
1. **Tax-to-wealth data sharing (IRC 7216).** The referral interface sends tax return information about integrated planning clients and referred prospects (income, retirement distributions and contributions from Forms 1099-R and 5498, and investment income) from SYS-T1 to the Wealth CRM. The 2022 consent form describes "financial planning and investment services" generally instead of each specific type of product or service (26 CFR 301.7216-3(a)(3)(i)(B)), and in a 2026 sample of 80 referrals, 9 transfers happened before the signed consent was recorded (301.7216-3(b)(1)). Wealth analytics also builds statistical compilations from those fields.
2. **Seasonal workforce identity.** About 11,000 seasonal tax professionals are onboarded each January. In 2026, 14% of seasonal accounts were activated before training and background checks were complete, and seasonal accounts were disabled an average of 9 days after the season ended.
3. **Email and refund-diversion exposure in the tax offices.** The shared email tenant (SYS-G4) still allows legacy authentication for the 1,150 office intake mailboxes (a 2019 exception) and external automatic forwarding for 212 mailboxes on an old exception list. Inbox-rule alerting covers corporate and Wealth mailboxes but not tax office mailboxes. A call-back rule for refund bank-account changes exists, but a 2026 sample found it was not followed in 11 of 60 changes.
4. **Tax division generative AI.** The in-house AI document extraction assistant, built on a hosted model from a third-party model provider, processed source documents for about 1.9 million returns in the 2026 season. U.S.-only processing and no-training terms are in the contract, but there is no accuracy or bias monitoring by document type, and a drafting assistant pilot that proposes tax treatments started without the IRC 7216 and Circular 230 review that the Group AI Standard requires.
5. **Practice Cloud AI feature.** Practice Cloud launched the "AI document intake" feature on 2026-02-02 for opt-in customer firms without updating its SOC 2 system description, its sub-processor list and customer contracts, or the information customers need to decide their own IRC 7216 basis. The feature sends client documents to a third-party model provider.
6. **Cross-division incident notification.** One incident can trigger the FTC notice (Tax and Advisory), the IRS next-business-day report and state tax agency reports, Regulation S-P customer notices and the 72-hour service provider notice (Wealth), notices to Practice Cloud customer firms under contracts and state third-party agent laws, state breach notices, and a Form 8-K decision. Each division has its own matrix; the combined matrix has never been exercised.
7. **Attest practice under the administrative services agreement.** CPA Partners inherits group controls (identity, SOC, cloud, email) under the 2021 administrative services agreement, but the inheritance is not documented, the agreement has no security or incident notice terms, and the CPA Partners supplement (2023) has not been aligned to the 2026 group policies. Inheritance is documented for Tax and Advisory (2025 matrix), Wealth (its 2025 Regulation S-P program), and Practice Cloud (its SOC 2 system description).

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 | Each division's primary regulation plus group obligations: Tax and Advisory, the FTC Safeguards Rule (full rule) with IRC 7216 and the IRS e-file duties; CPA Partners, HIPAA business associate duties for its health care audit clients; Wealth, SEC Regulation S-P and S-ID and the Advisers Act compliance and books-and-records rules; Practice Cloud, service provider, SOC 2, and FTC Act duties. Regulation-by-division matrix and group roadmap |
| P08 | Business email compromise and taxpayer data theft spanning divisions: a tax office manager's mailbox and Practice Cloud staff session are taken in the filing season; client documents are stolen, refund bank-account changes are requested, and Wealth advisers receive transfer requests from the hijacked internal account. Multi-regulator notification matrix and SEC materiality |
| P09 | SOC 2 scoped per division: Practice Cloud is a true service organization (in scope; readiness for its next Type 2, including the AI feature); client accounting services is a service organization for its small business clients (first readiness assessment); tax preparation, Wealth, and the attest practice are out of scope, with reasons |
| P10 | Group AI governance program: group standards, the division use-case inventory, and the rules for generative AI for tax and document preparation (IRC 7216, Circular 230), Wealth's AI use (Regulation S-P, books and records), and Practice Cloud's AI feature (customer commitments, SOC 2) |
| Cloud | Shared corporate platform in two providers plus division workloads, vendor-agnostic |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-05-04 to 2026-07-31 | Group and division risk analyses and gap analyses (after the filing season) |
| 2026-07-06 to 2026-08-28 | Common control assessment (group internal audit) plus division samples |
| 2026-08-27 | Group AI council review of the priority AI use cases |
| 2026-09-10 | Results to the board risk committee; approvals |
| 2026-10-15 | Qualified Individual's annual written report to the Tax and Advisory board of managers (16 CFR 314.4(i)) |

## 7. Facts added while building the deliverables
These facts were added so the deliverables could be completed. They do not change sections 1 to 6.

| Topic | Added fact |
|---|---|
| Registry defaults | Kept and adapted to the size: the primary system "Tax preparation software and client document portal" became the TPCP (SYS-T1 plus Tax and Advisory's tenant of the group's own Practice Cloud portal); the incident "Business email compromise and taxpayer data theft" was widened to span all three divisions; the AI use case "Generative AI for tax and document preparation" is the anchor of the group AI program (AI-001 and AI-002) |
| Revenue split (fictional) | CPA and Tax Services about $9.4 billion (including administrative service fees from CPA Partners); Wealth about $5.2 billion; Practice Cloud about $3.4 billion. Total about $18.0 billion. About 62% of Tax and Advisory revenue is billed from February through April: about $92 million per business day in season against about $38 million on average |
| Tax and Advisory scale | About 5.6 million individual returns a year (Form 1040 series) covering about 8.9 million individual consumers (spouses counted separately); about 380,000 business, trust, and exempt organization returns; client accounting services for 34,000 small businesses, with payroll for 21,000 of them (about 260,000 employees paid). Customer information on about 24 million consumers (current clients plus former clients within the 7-year retention schedule). About 21% of individual clients live in Florida |
| CPA Partners scale | About 6,200 attest engagements a year, including about 140 SOC 1 and SOC 2 examinations for outside service organizations and about 85 audits of HIPAA covered entities performed under business associate agreements (45 CFR 164.504(e)) |
| Wealth scale | About 980,000 client households. About 210,000 households are "integrated planning clients" whose returns Tax and Advisory prepares; Tax and Advisory receives their custodial account statements and planning data from Wealth under a 2022 intercompany integrated planning agreement. Wealth is a "larger entity" for Regulation S-P (assets under management of $1.5 billion or more), so its compliance date was 2025-12-03. Counsel determined in 2024 that Wealth is within Regulation S-ID (17 CFR 248.201) because advisory agreements let it direct transfers from client accounts to third parties on client instruction |
| Practice Cloud scale | About 26,000 outside customer firms and about 41 million end-client contacts across all tenants (about 9 million in Tax and Advisory's tenant). Standard customer terms: notice of a security incident affecting customer data within 72 hours of confirmation; 140 enterprise customers negotiated 24 hours. SOC 2 Type 2 for the 12 months ending 2025-09-30 was issued 2025-12-12 by an unaffiliated CPA firm. The AI document intake feature had 2,300 opt-in customer firms on 2026-08-31 |
| Practice Cloud legal position | Group legal recorded on 2026-06-10: Practice Cloud is a service provider to its customer firms under 16 CFR 314.4(f) and a third-party agent under state breach laws (Fla. Stat. 501.171(6) worked example). Because it holds itself out to tax return preparers as providing auxiliary services (document exchange and Form 8879 e-signature), it treats itself as a tax return preparer for IRC 7216 (26 CFR 301.7216-1(b)(2)(i)(B)), receiving information from customer firms under 301.7216-2(d)(1). It does not treat itself as a financial institution; counsel revisits this if it begins to move client funds itself |
| Intercompany agreements | Integrated planning agreement between Wealth and Tax and Advisory (2022; no Regulation S-P 72-hour service provider notice term); intercompany services agreement between the holding company and Wealth (amended 2025-11 with the 72-hour term); administrative services agreement between the holding company, Tax and Advisory, and CPA Partners (2021; no security or incident notice terms); Practice Cloud master agreement with Tax and Advisory (2024; standard 72-hour notice) |
| Cloud | Provider A hosts the corporate landing zone hub, SYS-T1, SYS-T3, the SYS-W1 integration hub, and the group data warehouse. Provider B hosts SYS-S1 (primary and warm standby regions) and the immutable backup vault. SYS-G1, SYS-G4, SYS-T2, and the SYS-W1 core applications are SaaS |
| AI use cases (P10 inventory) | AI-001 AI document extraction assistant (Tax; in production); AI-002 tax drafting assistant (Tax; pilot with 300 preparers since 2026-03); AI-003 notice response drafting (Tax; pilot); AI-004 audit analytics and document testing tool (CPA Partners); AI-005 adviser meeting notes and summary assistant (Wealth; pilot with 400 advisers); AI-006 client service email drafting (Wealth); AI-007 AI document intake feature (Practice Cloud); AI-008 engineering coding assistant (Practice Cloud); AI-009 enterprise generative AI assistant (group; 6,000 pilot users). A Group AI Standard and Group AI council were established in 2026 |
| AI-001 details | The model provider processes documents in the United States under a 2025 contract with no-training, no human review of content, and 30-day deletion terms. In the 2026 season, 6,400 preparers used it on documents for about 1.9 million returns. The drafting assistant (AI-002) proposes treatments and explanations to preparers |
| Seasonal workforce | About 11,000 seasonal tax professionals; accounts expire by design on April 30, but extensions of up to 30 days are granted by office managers; 2026 average disablement was 9 days after the season ended (target: same day) |
| Risk acceptance | Low: division security and compliance lead. Moderate: division president (for CPA Partners, its managing partner). High: Group Chief Risk Officer with the Group CISO, reported to the board risk committee. Very High: board risk committee only |
| Regulator and agency contacts | The IRS Stakeholder Liaison contacts for each state where Tax and Advisory has offices, the state tax agency contact list, the SEC regional office for Wealth, and law enforcement contacts are in the offline incident binder |
