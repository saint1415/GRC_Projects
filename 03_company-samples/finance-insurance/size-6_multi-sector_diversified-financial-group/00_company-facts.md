# Scenario facts: Cris Santos Company | Finance and Insurance | Multi-Sector

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, the citation is given; each citation was read from the primary source (eCFR current through 2026-09-23, or the U.S. Code) for this sample.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company Holdings, Inc. (a bank holding company supervised by the Federal Reserve; publicly traded SEC registrant) |
| Structure | A bank holding company with three divisions and corporate shared services. Each division is one or more legal entities owned by the holding company |
| Division 1: Banking (NAICS 522110), **focus of this scenario** | Cris Santos Bank, N.A., a national bank supervised by the OCC, deposits insured by the FDIC. About 31,000 employees. Average total consolidated assets of about $212 billion, so it is a **covered bank** under the OCC heightened standards (12 CFR Part 30, Appendix D, paragraph I.A: $50 billion or more) |
| Division 2: Financial Software and Data Services (NAICS 513210, sector 51 Information) | Cris Santos Financial Technology, LLC, a nonbank subsidiary of the holding company (not of the bank). Builds and operates a multi-tenant **digital banking platform** (online and mobile banking, business payment initiation) for the group's bank and for 310 client institutions (212 community banks and 98 credit unions), and sells **financial data services** (a cash-flow data service used in credit decisions, and core data conversion). About 5,500 employees. A **bank service provider** under the Bank Service Company Act (12 U.S.C. 1867(c)) and 12 CFR 53.4, 225.303, and 304.24; issues SOC 1 Type 2 and SOC 2 Type 2 reports. Permissible for a bank holding company as data processing (12 CFR 225.28(b)(14)) |
| Division 3: Commercial Real Estate (NAICS 531312, sector 53 Real Estate and Rental and Leasing) | Two nonbank subsidiaries of the holding company, about 3,000 employees in total: (1) **CRE Lending and Servicing**, which originates bridge and construction loans to commercial real estate investors and services commercial real estate loans for the bank and for third-party investors (12 CFR 225.28(b)(1)); (2) **Group Property Management**, which holds and operates the premises the bank uses (branches, operations centers, and the two group data center buildings) and manages foreclosed property for the bank (Bank Holding Company Act section 4(c)(1)(A) and (C), 12 U.S.C. 1843(c)(1)). Group Property Management does not manage property for outside owners, because 12 CFR 225.28(b)(2)(vi) excludes real property management from the permissible servicing activity |
| Corporate shared services | Identity, security operations, data centers and cloud, network, email and collaboration, HR, finance, legal, and group internal audit. About 5,500 employees, employed by the holding company |
| Location | Headquartered in Florida. The bank operates about 820 branches in Florida and 8 other southeastern and south-central states. The Financial Software division serves client institutions in 38 states. CRE Lending makes loans on properties in 24 states. **State law is handled generically** ("each state where affected individuals reside"), with Florida as the worked example |
| Workforce / revenue | 45,000 employees; about $18.0 billion revenue (fictional) |
| Holding company assets | About $226 billion average total consolidated assets. The bank is about 94% of the parent, below the 95% test in Appendix D paragraph I.4, so the bank keeps its own risk governance framework and relies on group components in consultation with the OCC (Appendix D paragraphs I.5 and I.6) |

## 2. People (role titles only)
| Role | Duties |
|---|---|
| Holding company board: risk committee and audit committee | Group cyber and enterprise risk oversight; approves the group information security program and group policies; audit committee oversees group internal audit |
| Bank board of directors and its risk committee | Approves the bank's information security program (12 CFR 30 App. B III.A) and the bank's risk governance framework and risk appetite statement (App. D II.A, II.E, II.G); receives the annual information security report (App. B III.F) |
| Group Chief Executive Officer | Chairs the executive risk committee; owns the strategic plan (App. D II.D) |
| Group Chief Risk Officer | Leads independent risk management (second line); designated the bank's Chief Risk Executive (App. D I.E.3); owns the group risk register and enterprise risk roll-up (NIST IR 8286 Rev. 1) |
| Head of Technology and Cyber Risk | Second line. Independent challenge of cyber, technology, and third-party risk; reports to the Group Chief Risk Officer |
| Group Chief Information Officer | First line. Runs data centers, cloud, network, and group applications |
| Group CISO | First line. Owns the group information security program and group policies; operates common controls (SYS-G1 to SYS-G4); designated by the bank board as the bank's information security officer; reports to the Group CIO with unrestricted access to both boards' risk committees |
| Chief Audit Executive (group internal audit) | Third line. Reports to both audit committees (App. D I.E.8). Assesses common controls once and samples division controls |
| Group Chief Privacy Officer; Group General Counsel; Group Chief Compliance Officer | Customer information use and notice decisions; contracts, intercompany agreements, and the notification matrix; consumer compliance including fair lending |
| Head of Model Risk Management | Second line. Independent validation of credit, fraud, and AML models and of AI models under the group model risk policy |
| BSA/AML Officers (bank; nonbank subsidiaries) | Suspicious activity reports (12 CFR 21.11 for the bank; 12 CFR 225.4(f) for the holding company's nonbank subsidiaries) |
| Division security and compliance leads (3) | Bank business information security officer; Financial Software division CISO (the division has its own CISO because it issues SOC reports to clients); Commercial Real Estate security and compliance lead. Maintain division supplements and division registers |
| Disclosure committee | Chaired by the Group Chief Financial Officer. Decides SEC materiality of cybersecurity incidents (Form 8-K Item 1.05) |
| Bank payments and treasury roles | Head of Commercial Payments Operations (wire and ACH operations); Treasury Management executive (business online banking and business customer agreements) |
| Financial Software division roles | Division president; chief technology officer; client risk and assurance director (SOC reports, client due diligence, bank service provider notices) |
| Commercial Real Estate roles | CRE Lending president; director of loan closing and funding; Group Property Management director |

## 3. Systems
| ID | System | Owner | Hosting |
|---|---|---|---|
| SYS-G1 | Group identity platform (single sign-on, MFA, privileged access management, identity governance) | Corporate | Identity SaaS vendor |
| SYS-G2 | Group SOC, SIEM, EDR, and email security gateway | Corporate | SIEM and EDR SaaS vendors; 24x7 group SOC |
| SYS-G3 | Group hybrid infrastructure: two group data centers (primary and secondary), cloud landing zones in two cloud providers (vendor-agnostic, called provider A and provider B), wide-area network, and the immutable backup vault | Corporate | Group data centers; providers A and B |
| SYS-G4 | Group email and collaboration suite (email, files, chat) for all 45,000 workforce users | Corporate | Productivity SaaS vendor |
| SYS-B1 | Core banking system (deposits, loans, customer information file, general ledger posting) | Bank | Licensed core software run in the two group data centers |
| SYS-B2 | Payments hub (wire transfers through the Federal Reserve payment services and correspondents, ACH, real-time payments) | Bank | Group data centers |
| SYS-B3 | Loan origination and credit decisioning (consumer and small business), including the AI credit underwriting model | Bank | Loan origination SaaS; model served on provider A |
| SYS-B4 | Branch, contact center, and card platforms (card processing and ATM driving outsourced to a card processor) | Bank | Group data centers; card processor |
| SYS-S1 | Digital banking platform (multi-tenant): consumer and business online and mobile banking, business wire and ACH initiation, tenant administration consoles. Tenants: the bank and 310 client institutions | Financial Software | Provider A (primary region and a warm standby region) |
| SYS-S2 | Financial data services platform: cash-flow data service and core data conversion | Financial Software | Provider A |
| SYS-R1 | CRE loan origination, closing, funding, and servicing system | Commercial Real Estate | Loan servicing SaaS vendor |
| SYS-R2 | Property management systems: lease administration, work orders, building automation, and physical access control for branches, operations centers, and data center buildings | Commercial Real Estate | Lease SaaS vendor; on-premises building controllers |

**SSP system (P02):** the *Core and Digital Banking Platform (CDBP)*: the bank's core banking system (SYS-B1) and the multi-tenant digital banking platform (SYS-S1) that the Financial Software division operates for the bank and 310 client institutions, joined by the payment initiation gateway that passes digital wire and ACH requests to the payments hub (SYS-B2); it inherits common controls from SYS-G1 to SYS-G4.

## 4. Current security posture: mature bank program, uneven divisions
**In place today:**
- One group information security program aligned to CSF 2.0, approved by the holding company board and the bank board, with an annual report to both (12 CFR 30 App. B III.A and III.F; 12 CFR 225 App. F)
- The bank's risk governance framework under Appendix D, with a board-approved risk appetite statement that includes cyber and fraud-loss metrics
- A common control catalog for SYS-G1 to SYS-G4
- 24x7 group SOC, EDR on all endpoints and servers, SIEM, and an email security gateway
- Privileged access management with just-in-time elevation; phishing-resistant MFA for administrators; number-matching MFA for all workforce
- Quarterly access certification for bank systems
- Immutable backups and a semiannual core banking failover test between the two data centers
- A bank wire callback standard: callbacks to an independently verified number on file, dual control on every outgoing wire
- Independent model validation for bank credit models (second-line model risk management)
- Financial Software division SOC 1 Type 2 and SOC 2 Type 2 (Security, Availability, Confidentiality) reports each year, period ending September 30
- Reg S-K Item 106 disclosure and a disclosure committee charter that covers cybersecurity incidents

**Gaps:**
1. **Commercial Real Estate funding controls.** CRE Lending (acquired in 2024) still funds loan closings on disbursement instructions received by email. Its callback procedure lets closers call the number in the closing package rather than an independently verified number, and its closers are not in the bank's payment-fraud training.
2. **Division supplements and inheritance.** The Commercial Real Estate supplement is the acquired company's 2023 policy set, never aligned to group policy. Common control inheritance is documented for the bank (2025 matrix) and in the Financial Software division's SOC system descriptions, but not for Commercial Real Estate.
3. **Bank service provider duties.** The Financial Software division holds a bank-designated point of contact (12 CFR 53.4(a)(1)) for only 151 of its 212 client banks. The bank treats the division as an affiliate and has not mapped the division's complementary user entity controls or reviewed its SOC reports as it does for outside vendors (12 CFR 30 App. B III.D).
4. **AI in credit decisions.** The Financial Software division sells a cash-flow data service (attributes and a score) to 64 client banks without developer documentation for them, and the service is not in its SOC 2 system description. The bank's AI credit underwriting model uses the same attributes; its validation found adverse action reasons that do not match the model's cash-flow drivers.
5. **Cross-division incident notification.** One incident can trigger OCC notice (12 CFR 53.3), Federal Reserve notice (225.302), client bank notices (53.4, 225.303, 304.24), SARs, state breach notices, and a Form 8-K decision. The bank's notification matrix does not cover the other two divisions, and no cross-division exercise has been run.
6. **Client tenant MFA.** The digital banking platform lets each tenant decide whether business users need MFA to initiate payments. The bank requires it; 41 of 310 client tenants do not.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P08 | Business email compromise that starts with one stolen session and spans all three divisions: a fraudulent CRE loan disbursement wire sent by the bank, vendor-impersonation emails to client banks, a 5.5-hour suspension of business wires on the digital banking platform, and exposed guarantor and client bank customer data. Multi-regulator notification matrix and SEC materiality |
| P09 | SOC 2 scoped per division: the Financial Software division is a true service organization (in scope; readiness for its Type 2 and for adding Processing Integrity and the cash-flow data service); the bank and Commercial Real Estate are out of scope, with reasons; the bank's review of the division's SOC reports as a user entity |
| P10 | Group AI governance program: group standards, the division use-case inventory, and the regulator-specific rules for the bank's AI credit underwriting model (ECOA and Regulation B, model risk), the Financial Software cash-flow data service (developer duties and client commitments), and the payment fraud model |
| Cloud | Hybrid: two group data centers plus a shared landing zone in two cloud providers, vendor-agnostic; division workloads in their own accounts |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-05-01 to 2026-07-31 | Group and division risk analyses and gap analyses |
| 2026-07-01 to 2026-08-31 | Common control assessment (group internal audit) plus division samples |
| 2026-08-28 | Group AI council review of priority AI use cases |
| 2026-09-10 | Results to the holding company board risk committee and the bank board risk committee |

## 7. Facts added while building the deliverables
These facts were added so the deliverables could be completed. They do not change sections 1 to 6.

| Topic | Added fact |
|---|---|
| Revenue split (fictional) | Bank about $15.2 billion; Financial Software about $1.6 billion; Commercial Real Estate about $1.2 billion. Total about $18.0 billion, as in section 1. About 250 business days a year: the bank earns about $61 million per business day, Financial Software about $6.4 million, Commercial Real Estate about $4.8 million |
| Bank scale | About 6.2 million consumer and 540,000 business customers; 4.1 million consumer and 310,000 business users on the digital banking platform. About 26,000 outgoing wires per business day (about $34 billion). Primary regulator: OCC. The holding company: Federal Reserve |
| Financial Software scale | 310 client institutions: 212 banks (74 OCC-supervised, 31 state member banks, 107 FDIC-supervised state nonmember banks) and 98 credit unions. About 19 million end users across all tenants, including the bank's. Client banks are examined by federal banking agencies, so the Bank Service Company Act applies to the division's services for them; credit unions are supervised by the NCUA, which is not an "appropriate Federal banking agency", so their oversight of the division rests on contract |
| Commercial Real Estate scale | CRE Lending: about $9.1 billion of loans held on its own balance sheet, and $19.4 billion serviced (for the bank and third-party investors). About 1,900 loan closings a year; average disbursement about $14 million. Loans are to businesses; about 2,400 individual guarantors provide personal financial statements. Group Property Management: about 820 branches, 6 operations centers, and 2 data center buildings; about 1,400 leases of surplus space to outside commercial tenants; foreclosed property managed for the bank |
| Customer information by division (GLBA) | The bank holds consumer customer information under 12 CFR 30 App. B. The two nonbank divisions are covered by the holding company's program under 12 CFR 225 App. F section II.A. The FTC Safeguards Rule (16 CFR Part 314) does **not** apply to any group entity: 314.1(b) limits it to financial institutions not subject to another regulator under GLBA section 505, and 15 U.S.C. 6805(a)(1)(A)-(B) assigns national banks to the OCC and bank holding companies and their nonbank subsidiaries to the Federal Reserve. Commercial borrowers and their guarantors obtain credit for business purposes, so they are not "consumers" under 12 CFR 1016.3(e)(1), and Commercial Real Estate holds little GLBA customer information; guarantor data is protected under state breach laws and group policy. Client institutions' customers are not the Financial Software division's consumers (1016.3(e)(2)(v): an institution that only provides processing or other services to another financial institution); the division protects that data as a service provider under client contracts and the clients' own Guidelines duties |
| Cloud and hosting | Provider A hosts the landing zone hub, SYS-S1 (primary and warm standby regions), SYS-S2, the credit model serving (SYS-B3), and the enterprise data platform. Provider B hosts the immutable backup vault and the SYS-S1 disaster recovery copy of backups. SYS-B1 and SYS-B2 run in the two group data centers (active primary, hot secondary). SYS-G1, SYS-G4, SYS-R1, and the lease system in SYS-R2 are SaaS |
| AI use cases (P10 inventory) | AI-001 AI credit underwriting model (bank; consumer installment loans and small business lines up to $250,000; in-house build; in production since 2025-10 for consumer and 2026-03 for small business); AI-002 wire and ACH payment fraud scoring (bank); AI-003 AML alert prioritization (bank); AI-004 contact center generative assistant (bank); AI-005 cash-flow data service (Financial Software, sold to 64 client banks); AI-006 platform login and payment fraud scoring for client tenants (Financial Software); AI-007 engineering coding assistant (Financial Software); AI-008 CRE underwriting assistant (Commercial Real Estate); AI-009 building energy analytics (Group Property Management); AI-010 enterprise generative AI assistant (group, 8,000 pilot users). A Group AI Standard and Group AI council were established in 2026 |
| Risk acceptance | Low: division security and compliance lead. Moderate: division president. High: Group Chief Risk Officer with the Group CISO, reported to the holding company board risk committee (and the bank board risk committee for bank risks). Very High: board risk committee only |
| Regulator contacts | The bank's OCC supervisory office and the Federal Reserve's designated point of contact for the holding company are listed in the incident binder |
