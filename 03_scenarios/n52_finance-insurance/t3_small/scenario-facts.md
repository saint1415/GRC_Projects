# Scenario facts: Cris Santos Company | Finance and Insurance | Small

All 10 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a regulation or supervisory issuance, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Bank, N.A. (a national bank wholly owned by Cris Santos Company, its bank holding company) |
| Business | Community commercial bank (NAICS 522110): consumer and business deposits, commercial real estate and small business lending, consumer and residential mortgage lending, and treasury management services (wires, ACH origination, business online banking) |
| Location | Florida. Six branches, including the main office (Branch 1), which also houses the operations center and the wire room |
| Charter and supervision | National bank. Primary federal regulator: the Office of the Comptroller of the Currency (OCC). Deposits insured by the FDIC. The holding company, Cris Santos Company, is a bank holding company supervised by the Federal Reserve; it has no operations other than owning the bank |
| Ownership | Privately held. Cris Santos is the majority shareholder of the holding company and chairs both boards |
| Workforce | 120 employees: 48 in the branches (tellers, universal bankers, branch managers), 22 in lending, 18 in deposit and loan operations (including the wire room), 14 in finance, compliance, BSA and risk, 8 in IT and security, 10 in executive and administrative roles |
| Size | $510 million in total assets (fictional). Under the SBA size standard of $850 million in total assets for NAICS 522110, so SBA-small |
| Revenue | About $20 million a year in net revenue (fictional), about $80,000 per business day; used to scale BIA impact values (P05) |
| Customers | About 13,800 consumer and 2,200 business deposit customers. About 9,000 consumer and 1,400 business users are enrolled in online and mobile banking |
| Payments volume | About 35 outgoing wires per business day (about $4 million per day on average); 140 business customers originate ACH through business online banking |
| Lending | $380 million loan portfolio. About 350 small business loan applications a year, most under $250,000 |
| Primary regulation | Interagency Guidelines Establishing Information Security Standards as issued by the OCC, 12 CFR Part 30, Appendix B (GLBA section 501(b)), examined using the FFIEC Information Technology Examination Handbook. Secondary: the Computer-Security Incident Notification Rule, 12 CFR Part 53 |
| Not in scope | FTC Safeguards Rule (16 CFR Part 314): the bank is supervised by the OCC, not the FTC. NYDFS Part 500: not New York-chartered or licensed. SEC Regulation S-P and S-ID, Form 8-K Item 1.05: the bank has no broker-dealer or adviser and neither company is an SEC registrant. NAIC Model #668: no insurance agency. CFPB small business lending data collection (Regulation B subpart B): the bank originates far fewer than the 1,000 covered transactions a year that define a covered financial institution (12 CFR 1002.105(b)). Card data: debit cards are issued and processed by a card processor; PCI DSS obligations are noted, not assessed |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notification, Fla. Stat. 501.171; funds-transfer liability under UCC Article 4A as enacted in Fla. Stat. ch. 670). The samples otherwise stay federal |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Board of Directors (7 directors) and its Audit and Risk Committee | Approves the written information security program and oversees it (12 CFR 30 App. B III.A); receives the annual information security report (III.F); approves the risk appetite statement |
| Chairman of the Board (majority shareholder) | Chairs the board; with the board, accepts risks rated Very High |
| President and Chief Executive Officer (CEO) | Executive owner of the program; accepts High risks and reports each acceptance to the Audit and Risk Committee |
| Chief Operating Officer (COO) | Owns deposit operations, the wire room, and IT; accepts Moderate risks |
| IT Manager | Designated **Information Security Officer (ISO)** by the board; runs IT with two IT specialists and a managed security service provider. Reports to the COO |
| Chief Credit Officer | Owns lending and the loan origination system; business owner of the AI credit model (P10) |
| Chief Financial Officer | General ledger, model inventory owner for financial models, vendor contract budget |
| Compliance Officer | Fair lending, Regulation B, GLBA privacy notices, customer incident notices; also the Privacy Officer |
| BSA/AML Officer | Suspicious activity reports (SARs) and FinCEN filings; law enforcement liaison for fraud |
| Deposit Operations Manager | Wire room and ACH operations; wire callback standard |
| Treasury Management Officer | Business online banking, wire and ACH origination agreements with business customers |
| Branch Managers (6) | Branch security, branch-originated wire requests, teller workstation areas |
| HR Director | Hiring, background checks, terminations |
| Outsourced internal audit (CPA firm) | Annual independent IT audit and testing of key controls (III.C.3) |
| Managed security service provider (MSSP) | 24x7 monitoring of firewall and endpoint detection and response (EDR) alerts |

## 3. Systems

| ID | System | Hosting | Holds customer information? | Notes |
|---|---|---|---|---|
| SYS-01 | Core banking system (deposits, loans, customer information file, general ledger) | Hosted by a core processor (a bank service provider under the Bank Service Company Act) | Yes | System of record. Teller and platform applications run on bank workstations over private circuits. The core processor provides SOC 1 Type 2 and SOC 2 Type 2 reports. The core includes the AML transaction monitoring module used by the BSA staff |
| SYS-02 | Online and mobile banking (consumer and business), including business wire and ACH initiation | Vendor-hosted by a digital banking provider, integrated with SYS-01 | Yes | **Customer MFA is optional** (see gaps). Bank staff administer users, limits, and entitlements in the provider's admin console |
| SYS-03 | Wire transfer and ACH origination platform | Vendor-hosted payments service, with bank-managed configuration and two dedicated payments workstations in the wire room for access to the Federal Reserve payment services | Yes | Maker-checker (dual control) is enforced for every outgoing wire. Wire requests from branches arrive by phone, email, or in person |
| SYS-04 | Loan origination system (LOS) | Vendor SaaS | Yes | Applications, credit reports, financial statements, adverse action notices |
| SYS-05 | Identity provider (single sign-on and MFA for the workforce) | SaaS | No (identities only) | Protects SYS-02 admin console, SYS-03, SYS-04, SYS-09, and the cloud tenant. The core (SYS-01) uses its own logons |
| SYS-06 | Cloud tenant (IaaS/PaaS) | Public cloud provider (vendor-agnostic) | Yes | Hosts four bank-managed workloads: the credit decisioning service (runs the AI model, SYS-10), the reporting data warehouse, the central log archive, and the backup vault for bank-managed data |
| SYS-07 | Branch networks, teller workstations, and endpoints | On-premises | Yes (in use and cached) | Six branch networks with firewalls and an SD-WAN to the main office and the core processor; 110 workstations and laptops, including 34 teller workstations and the 2 payments workstations |
| SYS-08 | ATMs (9: one at each branch and 3 off-site) | On-premises devices, driven by the card processor's ATM network service | Yes (card data in transit) | Serviced by an ATM maintenance vendor |
| SYS-09 | Productivity suite (email, files, chat) | SaaS | Yes (incidental) | Staff exchange loan documents and wire requests with customers by email |
| SYS-10 | AI small business credit underwriting model | Vendor-developed model deployed in SYS-06, called by SYS-04 | Yes | Pilot since May 2026 at 3 branches for applications under $250,000 (see P10) |
| SYS-11 | Card processing and ATM network services | Card processor (bank service provider) | Yes | Debit card authorization, ATM driving, card fraud monitoring |

**SSP system (P02):** the *Wire and Digital Banking Platform (WDBP)*: SYS-02 online and mobile banking (bank-managed configuration of the vendor-hosted service), SYS-03 wire and ACH origination platform (bank-managed configuration of the vendor-hosted service and the two payments workstations), the SYS-05 identity provider as it protects them, the wire-room and branch endpoints on SYS-07 used to key and approve wires, and the interfaces to SYS-01 and the Federal Reserve payment services.

## 4. Current security posture: partially compliant

**In place today:**
- A written information security program, approved by the board in November 2025, and an annual information security report to the board each December
- An annual information security risk assessment (last completed December 2025)
- MFA for workforce email, remote access, cloud administration, and the online banking and wire platform admin consoles
- Maker-checker dual control on every outgoing wire in SYS-03, and dual approval for business online banking wires above $50,000
- EDR on all workstations and servers, monitored 24x7 by the MSSP
- An annual independent IT audit (outsourced internal audit) and an annual external penetration test
- Contracts with the core processor and the digital banking provider that include confidentiality and security provisions
- SOC reports collected every year from the core processor, the digital banking provider, and the card processor
- Background checks for all employees before hire
- Annual security awareness training and two phishing simulations a year
- Full-disk encryption on laptops; the core processor and the digital banking provider encrypt data at rest and in transit
- A business continuity plan, with annual participation in the core processor's disaster recovery test

**Missing or weak, found in the 2026 assessments:**
1. The annual risk assessment is done, but it is not tied to a board-approved risk appetite. There are no documented tolerance thresholds, so residual risks are not compared to anything the board has approved.
2. Wire callback verification is inconsistent across branches. The written standard requires a callback to the phone number on file for any wire request received by email or phone. Two of six branches skip the callback for "known customers." A sample of 25 branch-originated wires found 7 with no callback evidence.
3. There are no quarterly user access reviews in the core banking system. The last review of core entitlements was 14 months ago, and it did not cover bank-level administrator ("super user") roles.
4. Vendor SOC reports are collected but not reviewed. Complementary user entity controls (CUECs) are not mapped to bank controls, exceptions are not followed up, and no bridge letters are requested.
5. The incident response plan (2023) lacks the step to notify the OCC within 36 hours of determining a notification incident (12 CFR 53.3), and it has no criteria for making that determination. It also omits the parallel Federal Reserve notice for the holding company (12 CFR 225.302).
6. MFA for online banking customers is optional. It is enabled by 31% of consumer users and 58% of business users. Business users who have not enabled MFA can add wire beneficiaries and initiate wires with a password only.
7. The ISO role is held by the IT Manager, who also runs IT operations and reports to the COO. Independence of the security function is limited.
8. The core processor contract (renewal due 2027) predates 12 CFR Part 53 and sets no incident notice time frame. The bank has not given the core processor or the digital banking provider a designated point of contact for 12 CFR 53.4 notices.
9. Audit logs in the online banking admin console and the wire platform are retained but not reviewed. Changes to wire beneficiaries and user limits are not monitored.
10. The wire-room contingency procedure (alternate wire initiation if SYS-03 is unavailable) has not been tested since 2023.
11. The AI credit model went into a pilot without independent validation, fair lending testing, or a review of its adverse action reasons (see P10).
12. Four enabled core banking accounts belong to employees who left the bank between 2 and 11 months ago (found during P07 testing).

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P08 incident | Business email compromise: a business customer's email account is taken over, and a fraudulent wire request is processed at a branch that skipped the callback. The attacker also used the customer's stolen online banking password, because the customer had not enabled MFA |
| P09 SOC 2 | The bank is not a service organization. (a) Review of the core processor's SOC 1 Type 2 and SOC 2 Type 2 reports (`vendor-soc2-review.csv`); (b) a Security-only self-benchmark against the Trust Services Criteria, used as a cross-check of the program before the next OCC examination |
| P10 AI | AI credit underwriting model for small business loans (pilot) |
| Cloud | Vendor-agnostic. Services are described by category, with AWS, Azure, and Google Cloud equivalents noted only where needed for shared responsibility |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-07-13 to 2026-07-24 | Risk assessment and gap analysis fieldwork |
| 2026-08-03 to 2026-08-07 | Control assessment fieldwork |
| 2026-08-20 | Core processor SOC report review completed |
| 2026-08-25 | AI credit model assessment completed |
| 2026-08-27 | Audit and Risk Committee (a committee of the board, as 12 CFR 30 App. B III.A permits) reviews the results and approves policies POL-01 to POL-05 |
| 2026-08-31 | Deliverables approved by the President and CEO |
| 2026-10-15 | Board meeting: risk appetite statement and updated information security program scheduled for approval |
