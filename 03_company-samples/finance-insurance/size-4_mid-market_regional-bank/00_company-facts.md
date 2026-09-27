# Scenario facts: Cris Santos Company | Finance and Insurance | Mid-Market

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or supervisory issuance, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (privately held bank holding company; private equity-backed; its only subsidiary is Cris Santos Bank, N.A., a national bank) |
| Business | Regional commercial bank (NAICS 522110): consumer and business deposits, commercial real estate, commercial and industrial and small business lending, residential mortgage and consumer lending, treasury management (wires, ACH origination, positive pay, remote deposit capture), and **correspondent payment services** (wire and ACH processing and settlement) for 18 smaller community banks and credit unions |
| Location | Headquartered in Florida. 28 branches: 22 in Florida and 6 in Georgia. The Florida headquarters campus houses the main office, the operations center, the primary wire room, and an on-premises server room. The Georgia regional office houses the alternate operations site and a secondary wire room. **State breach laws are handled generically:** the bank notifies under the law of each state where affected individuals reside, with Florida as the worked example |
| Charter and supervision | National bank. Primary federal regulator: the Office of the Comptroller of the Currency (OCC). Deposits insured by the FDIC. The holding company, Cris Santos Company, Inc., is a bank holding company supervised by the Federal Reserve; it has no operations other than owning the bank |
| Ownership | Privately held. A consortium of private equity funds holds a minority, non-controlling interest; founders, directors, and management hold the rest. Neither company has securities registered under the Securities Exchange Act, and neither files periodic reports with the SEC |
| Workforce | 600 employees: 250 in the branches, 55 in commercial banking and treasury management, 70 in lending and credit, 85 in operations (deposit, loan, and payments operations, the wire rooms, and correspondent services), 35 in the customer contact center, 38 in IT, 4 in information security, 40 in risk, compliance, BSA/AML, internal audit, and legal, 15 in finance, and 8 in executive, HR, and administration |
| Size | $2.5 billion in total assets (fictional). Above the SBA size standard of $850 million in total assets for NAICS 522110 (13 CFR 121.201), so not SBA-small |
| Revenue | About $105 million a year in net revenue (fictional), about $420,000 per business day over about 250 business days. Used to scale BIA impact values (P05) |
| Customers | About 96,000 consumer and 11,500 business deposit customers. About 68,000 consumer users and 9,200 business users (from 4,100 business customers) are enrolled in online and mobile banking |
| Payments volume | About 380 outgoing wires per business day (about $165 million a day), of which about 120 are sent for respondent institutions. About 1,050 business customers originate ACH through business online banking |
| Correspondent services | 18 respondent institutions (11 community banks and 7 credit unions) submit wire and ACH payment orders through the bank's correspondent portal; the bank sends them through its Federal Reserve accounts and settles with each respondent. About $6 million a year in fee revenue. Several respondents and their examiners have asked for a SOC report (P09) |
| Lending | $1.9 billion loan portfolio. About 650 small business loan applications and about 420 small business originations a year |
| Primary regulation | Interagency Guidelines Establishing Information Security Standards as issued by the OCC, 12 CFR Part 30, Appendix B, with Supplement A (GLBA section 501(b); N52-R02), examined using the FFIEC Information Technology Examination Handbook. Also analyzed for the primary business line (P03): the Computer-Security Incident Notification Rule (12 CFR Part 53, and 12 CFR 225 Subpart N for the holding company); the OCC Identity Theft Red Flags rule (12 CFR 41.90); and SAR reporting (12 CFR 21.11) |
| Not in scope | **OCC heightened standards** (12 CFR Part 30, Appendix D): apply only to banks with average total consolidated assets of $50 billion or more, banks whose parent controls such a bank, or banks the OCC designates (App. D I.A, I.C); the bank is $2.5 billion, its parent controls no other bank, and it has no OCC designation. **FTC Safeguards Rule** (16 CFR Part 314): the bank is supervised by the OCC, not the FTC. **NYDFS Part 500**: not New York-chartered or licensed. **SEC Regulation S-P and S-ID**: no broker-dealer, investment adviser, or trust department. **SEC Form 8-K Item 1.05 and Regulation S-K Item 106**: the companies are privately held and are not Exchange Act reporting companies. **NAIC Model #668**: no insurance agency. **CFPB small business lending data collection** (Regulation B subpart B): the bank originates fewer than the 1,000 covered credit transactions for small businesses in each of two preceding calendar years that define a covered financial institution (12 CFR 1002.105(b)); rechecked each January. **Card data**: debit cards are issued and processed by a card processor; PCI DSS obligations are noted, not assessed |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notification, Fla. Stat. 501.171; funds-transfer liability under UCC Article 4A as enacted in Fla. Stat. ch. 670, which governs the bank's funds transfer agreements). Georgia customers are handled generically ("the law of each state where affected individuals reside"). The samples otherwise stay federal |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Board of Directors (9 directors) | Approves the written information security program and the risk appetite statement (12 CFR 30 App. B III.A); accepts risks rated Very High (temporary only) |
| Board Risk Committee | Oversees the program on the board's behalf; receives the annual information security report (III.F) and quarterly cyber risk reports; approves security policies |
| Board Audit Committee | Oversees internal audit; receives the control assessment (P07) and POA&M status each quarter |
| President and Chief Executive Officer (CEO) | Accepts High risks with the CRO's concurrence and reports each acceptance to the Board Risk Committee; makes regulator notices under 12 CFR Part 53 |
| Chief Risk Officer (CRO) | Second line of defense. Owns enterprise risk management and the risk appetite; the ISO, the IT Risk and Compliance Manager, the Third-Party Risk Manager, and the Model Risk Manager report to the CRO |
| Chief Operating Officer (COO) | Owns deposit, loan, and payments operations, correspondent services, the contact center, and IT; system owner of the SSP system (P02); accepts Moderate risks |
| Chief Information Officer (CIO) | Runs IT (38 staff: infrastructure, applications, cloud, service desk); owns the core processor relationship day to day; reports to the COO |
| Information Security Officer (ISO) | Designated by the board. Leads a team of 3 security analysts; runs the program day to day, vulnerability management, and MSSP oversight; reports to the CRO with a direct line to the Board Risk Committee. **Overlap:** the ISO team also operates some first-line controls (vulnerability scanning, MSSP triage); internal audit tests them independently |
| IT Risk and Compliance Manager (plus 1 analyst) | The small GRC function: risk register, policy set, standards, POA&M tracking, examination requests |
| Third-Party Risk Manager | Vendor inventory and tiering, due diligence, SOC report reviews with the ISO |
| Model Risk Manager | Model inventory and validation program, including AI models (P10) |
| Chief Financial Officer (CFO) | General ledger, liquidity and funding, cyber insurance and the financial institution bond |
| Chief Credit Officer | Credit policy and the loan origination system; business owner of the AI credit underwriting model (AI-001) |
| Chief Compliance Officer | Consumer compliance, GLBA privacy notices, customer incident notices, Red Flags program; also the Privacy Officer. The Fair Lending Officer reports to this role |
| BSA/AML Officer | SARs and FinCEN filings; law enforcement liaison for fraud; business owner of the AML monitoring system (AI-002) |
| General Counsel | Legal advice on incidents, notices, funds-transfer liability, and contracts; engages outside counsel and forensics under privilege |
| Director of Payments Operations | Wire rooms and ACH operations; wire callback standard |
| Treasury Management Director | Business online banking, positive pay, remote deposit capture, and ACH origination agreements |
| Correspondent Services Director | Respondent institution relationships, the correspondent portal, and service agreements |
| Retail Banking Director and 28 Branch Managers | Branch operations, account maintenance at branches, branch security |
| Contact Center Director | Customer service line, fraud reporting line, contact-information changes by phone |
| Director of Marketing and Communications | Customer and media statements during incidents |
| HR Director | Hiring, background checks, terminations and transfers |
| Chief Audit Executive (internal audit department of 3) | Annual audit plan; IT audit is co-sourced with a CPA firm that performed the P07 assessment. Reports to the Audit Committee |
| Managed security service provider (MSSP) | 24x7 SIEM and EDR monitoring; calls the ISO within 30 minutes of a high-severity alert |

## 3. Systems

| ID | System | Hosting | Holds customer information? | Notes |
|---|---|---|---|---|
| SYS-01 | Core banking system (deposits, loans, customer information file, general ledger) | Hosted by a core processor (a bank service provider under the Bank Service Company Act) over private circuits | Yes | System of record. The core processor provides SOC 1 Type 2 and SOC 2 Type 2 reports. The bank administers its own users through the core's security administration module (212 roles) |
| SYS-02 | Online and mobile banking (consumer and business), including business wire, ACH, and positive pay | Vendor-hosted by a digital banking provider, integrated with SYS-01 and SYS-03 | Yes | Business users: MFA required since 2025 (one-time codes by app or SMS). Consumers: SMS code only when signing in from a new device (see gaps) |
| SYS-03 | Payments hub (wire and ACH platform) and the correspondent portal | Licensed vendor software run by the bank in the production account of its cloud landing zone (SYS-06); 4 dedicated payments workstations (2 in each wire room) for access to the Federal Reserve payment services | Yes | Maker-checker for every outgoing wire; callback field required for non-face-to-face wire requests; respondent institutions sign in to the correspondent portal through the bank's customer identity service |
| SYS-04 | Loan origination system (LOS) | Vendor SaaS | Yes | Consumer, mortgage, commercial, and small business applications; adverse action notices |
| SYS-05 | Identity provider (workforce single sign-on and MFA, and the customer identity service for the correspondent portal) | SaaS | No (identities only) | All workforce users have MFA; privileged access management (PAM) covers directory and cloud administrators |
| SYS-06 | Cloud landing zone: 6 accounts (management, security and log archive, shared network, production, non-production, backup) | Public cloud provider (vendor-agnostic) | Yes | Hosts the payments hub and correspondent portal, the credit decisioning service (AI-001), the data warehouse, and the backup vault in a second region |
| SYS-07 | Branch and operations networks, on-premises server room, and endpoints | On-premises | Yes (in use and cached) | 28 branch networks and 2 operations sites on SD-WAN with private circuits to the core processor; about 60 virtual servers at headquarters (directory, file shares, check imaging and item processing, print); 640 workstations and laptops, including 170 teller workstations and the 4 payments workstations |
| SYS-08 | ATMs and interactive teller machines (58) | On-premises devices, driven by the card processor's ATM network service | Yes (card data in transit) | Serviced by an ATM maintenance vendor |
| SYS-09 | Productivity suite (email, files, chat) | SaaS | Yes (incidental) | Relationship managers exchange loan documents and payment requests with customers by email |
| SYS-10 | Credit decisioning service running the AI small business credit model (AI-001) | Vendor model deployed by the bank in the production account (SYS-06), called by SYS-04 | Yes | In production since 2025-10 for small business applications up to $500,000 (see P10) |
| SYS-11 | Card processing and ATM network services | Card processor (bank service provider) | Yes | Debit card authorization, stand-in processing, card fraud monitoring |
| SYS-12 | SIEM and EDR | SIEM operated by the MSSP (SaaS); EDR on all managed endpoints and servers | Security logs | Sources: identity provider, EDR, firewalls, cloud audit logs. Not yet: payments hub application logs and core security administration reports |
| SYS-13 | AML transaction monitoring with machine-learning alert scoring (AI-002) | Vendor SaaS fed nightly from SYS-01 and SYS-03 | Yes (including SAR information) | Used by 14 BSA staff |
| SYS-14 | Third parties | Various | Various | About 260 third parties; 34 rated critical; 7 are bank service providers subject to 12 CFR 53.4 (core processor, digital banking provider, card processor, item processing provider, LOS provider, AML monitoring provider, statement printing and mailing provider) |
| SYS-15 | Other AI tools | Vendors | Varies | Online banking fraud scoring (AI-003), an enterprise generative AI assistant pilot (AI-004), and a customer service chatbot on the website and mobile app (AI-005) |

**SSP system (P02):** the *Core and Online Banking Platform (COBP)*: the bank-managed configuration of SYS-01 core banking and SYS-02 online and mobile banking, the SYS-03 payments hub and correspondent portal in the production account, the SYS-05 identity provider as it protects them, the SYS-06 landing zone accounts that host and protect SYS-03 and SYS-10, the operations center, wire room, and branch endpoints on SYS-07 that access them, and the SYS-12 SIEM as it monitors them. Moderate impact, with baseline tailoring and inherited controls.

## 4. Current security posture: defined program, with gaps in scale

**In place today:**
- A written information security program approved by the board (last in October 2025); an annual information security report to the Board Risk Committee each December
- A board-approved enterprise risk appetite statement (2025), with qualitative statements for operational and cyber risk
- An ISO reporting to the CRO, a small GRC function, and a co-sourced IT audit each year
- Annual information security risk assessment (last completed December 2025)
- MFA for all workforce users; PAM with just-in-time elevation for directory and cloud administrators
- EDR on all managed endpoints and servers, monitored 24x7 by the MSSP through the SIEM
- Maker-checker dual control on every outgoing wire, and a required callback field in the payments hub for wire requests received by email or phone
- MFA required for all business online banking users since 2025
- Monthly authenticated vulnerability scanning; annual external and internal penetration tests
- Quarterly access reviews for the payments hub and the online banking admin console
- A third-party risk program with an inventory, tiering, and annual SOC report collection for critical vendors
- Backups of cloud workloads to a separate backup account in a second region with 35-day write-once retention
- Annual participation in the core processor's disaster recovery test; a documented business continuity plan with an alternate operations site in Georgia
- An incident response plan (2024) that includes the 36-hour OCC notice under 12 CFR 53.3
- A model risk management policy (2023) and a model inventory kept by the Model Risk Manager
- Security policies adopted in 2024; annual training and monthly phishing simulations

**Missing or weak, found in the 2026 assessments:**
1. The risk appetite statement has no measurable cyber tolerances. Board reports describe cyber risk qualitatively, so the board cannot tell whether residual risk is within appetite.
2. Contact-information changes (phone, email, address) on business and consumer accounts can be made from email or phone requests without out-of-band verification, and customers are not alerted to the change. A sample of 40 business contact changes found 11 with no verification evidence. This can defeat the wire callback, because the callback goes to the number on file.
3. Customer authentication is not phishing-resistant. Consumers get an SMS code only when signing in from a new device. About 12% of business users still use SMS codes. New wire beneficiaries added in online banking are not confirmed out of band.
4. Core banking entitlements are not tied to job-role templates. The core's 212 roles are reviewed quarterly by managers who approve what they see; 8 of 30 sampled teller and universal banker users (27%) hold entitlements beyond their role. PAM does not cover the core's security administrators or the payments hub application administrators.
5. Third-party oversight does not scale. SOC reports are collected for the 34 critical vendors, but complementary user entity controls (CUECs) are mapped only for the core processor. 9 critical vendor contracts set no incident notice time frame. Designated 12 CFR 53.4 contacts were given to only 3 of the 7 bank service providers.
6. Recovery of bank-managed workloads is unproven. The payments hub and correspondent portal failover to the second region was tested once (2025) and took 9 hours against a 4-hour target. The alternate operations site has been exercised only for wires.
7. Payments hub application logs, correspondent portal logs, and core security administration reports are not in the SIEM. There are no detection use cases for beneficiary, template, or contact-information changes.
8. The incident response plan includes the OCC 36-hour notice but no criteria for deciding whether an incident is a notification incident. It omits the Federal Reserve notice for the holding company (12 CFR 225.302) and the bank's own outbound notices to respondent institutions as a service provider. Executives have not exercised the plan.
9. AI and model governance lags adoption. The AI credit model (AI-001) had a conceptual review but no outcomes validation on bank data; fair lending testing used the vendor's national data; adverse action reason codes were not reviewed. The website chatbot (AI-005) and a generative AI assistant pilot (AI-004) started without model risk or compliance review.
10. 14 legacy Windows servers in the headquarters server room (check imaging and item processing) run an unsupported operating system. Critical patches missed the 30-day target on 18% of on-premises servers in the first half of 2026.
11. The 2024 policies are in place, but supporting standards (configuration, logging, cryptography, third-party tiering, AI use) are missing or thin.
12. The correspondent services business has no documented service commitments, system description, or control set that respondents or a service auditor could rely on (P09).

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P08 | **Two incident types**, integrated with crisis management and legal: (1) business email compromise and a fraudulent wire, where the attacker first changes the business customer's phone number on file through an emailed request (gap 2), so the wire callback reaches the attacker; (2) a ransomware attack at the core processor that takes the core down for more than a day, which drives the notification incident determination (12 CFR 53.3, 225.302) and the bank's own notices to respondent institutions |
| P09 | Readiness for a **SOC 2 Type 2** examination of the correspondent payment services (Security, Availability, Processing Integrity, Confidentiality), requested by respondent institutions; plus the vendor SOC review program for critical providers |
| P10 | AI use-case portfolio: AI-001 small business credit underwriting model (High), AI-002 AML alert scoring, AI-003 online banking fraud scoring, AI-004 enterprise generative AI assistant (pilot), AI-005 customer service chatbot |
| Cloud | Multi-account landing zone (6 accounts), vendor-agnostic, plus SaaS and bank service providers. AWS, Azure, and Google Cloud names appear only in the equivalents table |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-06-29 to 2026-07-24 | BIA, risk assessment, and gap analysis fieldwork |
| 2026-08-03 to 2026-08-21 | Control assessment fieldwork (co-sourced IT audit firm) |
| 2026-08-24 to 2026-09-04 | AI portfolio assessment; vendor SOC report reviews completed 2026-08-28 |
| 2026-09-15 | Board Risk Committee reviews the results and approves policies POL-01 to POL-05 and the standards index |
| 2026-09-17 | Board Audit Committee receives the control assessment and POA&M |
| 2026-09-18 | Deliverables approved by the President and CEO (High risks) and the COO (system owner) |
| 2026-10-20 | Board meeting: updated information security program and measurable cyber risk tolerances scheduled for approval |

## 7. Facts added during the build (fictional; used across P01-P10)
These details were added so the deliverables could be specific. They do not change sections 1-6.

| Topic | Added fact |
|---|---|
| Branches | Florida branches are numbered FL-01 to FL-22 (FL-01 is the main office on the headquarters campus). Georgia branches are GA-01 to GA-06; the Georgia regional office (alternate operations site and secondary wire room) is in the GA-01 building |
| Revenue split (fictional) | Of about $420,000 net revenue per business day, fee income is about $150,000: card interchange $22,000, correspondent services $24,000, wire fees $18,000, deposit service charges $30,000, treasury management $10,000, ACH $8,000, mortgage banking $4,000, item processing $6,000, other $28,000. Net interest income largely keeps accruing during an outage, so BIA losses are driven by fees, customer compensation, overtime, and fraud and liquidity exposure |
| Cyber insurance and bond | Cyber policy with a $15 million limit and a $500,000 retention; the carrier's panel supplies breach counsel and forensics, and notice goes through the carrier hotline before vendors are engaged. A separate financial institution bond covers fraud losses |
| Core processor recovery commitments | The core processor's SOC 2 system description states RTO 4 hours and RPO 15 minutes; its secondary data center is in another state. Branches have an offline teller mode with per-transaction limits |
| Workforce activity | 142 terminations and 88 internal transfers in the 12 months to 2026-06-30. The last core entitlement review was completed in July 2026. The June 2026 phishing simulation click rate was 5.9% |
| Backups | Daily backups of production workloads to the backup account, 35-day write-once retention, separate administrator credentials; on-premises servers back up to an appliance that replicates to the backup account nightly |
| MSSP | Contract requires a call to the ISO within 30 minutes of a high-severity alert |
| Correspondent service agreements | The respondent agreements (2019 template) promise "commercially reasonable" availability, with no stated recovery time, incident notice time, or security commitments. General Counsel's working view (2026-07) is that the correspondent processing services are likely covered services under the Bank Service Company Act, so the bank treats itself as a bank service provider to its bank respondents for 12 CFR 53.4 and the parallel Federal Reserve and FDIC provisions (12 CFR 225.303; 304.24). For credit union respondents, notice duties are set by contract |
| Terminology | "Core and Online Banking Platform (COBP)" is the SSP system in P02, identifier CSB-COBP-01 |
| Additional role titles | Director of Deposit Operations; Director of Loan Operations; Mortgage Lending Director; Fair Lending Officer; Controller; Cloud Platform Manager; Infrastructure Manager; Service Desk Manager |
| Other operating details | The payments hub has 64 users (wire rooms, ACH operations, correspondent operations); 6 users hold application administrator rights. The data warehouse receives a nightly extract from SYS-01. 34 critical vendors are Tier 1 under the P09 tiering approach; 71 are Tier 2 |
