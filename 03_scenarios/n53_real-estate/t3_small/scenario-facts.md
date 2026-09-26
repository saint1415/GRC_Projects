# Scenario facts: Cris Santos Company | Real Estate and Rental and Leasing | Small

All 10 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a regulation or rule, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (Florida limited liability company; registered Florida real estate brokerage; licensed and appointed title insurance agency for its Closing Services division) |
| Business | Residential real estate brokerage (NAICS 531210) with three lines: (1) residential sales brokerage, (2) residential property management and leasing, and (3) an in-house **Closing Services division** that acts as settlement (closing) agent and title insurance agent |
| Location | Florida. Two offices in the same metropolitan area: the **Main Office** (headquarters, Closing Services, Property Management, accounting, IT) and the **Branch Office** (sales) |
| Workforce | 60 employees: 5 executive and sales management, 6 finance and escrow accounting, 10 transaction coordination, 7 Closing Services, 16 property management and leasing, 8 marketing and agent services, 6 inside sales (employed licensed agents), 2 IT |
| Affiliated sales associates | About 140 licensed sales associates who are **independent contractors**, not employees. They work under the Broker of Record's license and use company systems (transaction management, email) from their **own devices** |
| Revenue | $9.0 million in annual receipts (fictional): brokerage company dollar after agent splits $5.9 million, property management fees $1.6 million, Closing Services fees and retained title premium $1.5 million. About $36,000 per business day. Under the SBA standard of $15.0 million for NAICS 531210, so SBA-small |
| Sales volume | About 1,150 closed transaction sides a year. The brokerage holds the earnest money deposit in its own **sales escrow account** in about 380 transactions a year (about $9.5 million a year in deposits); title companies or attorneys hold the rest |
| Closing Services volume | About 620 closings a year (about half are the brokerage's own transactions). About 2,800 outgoing disbursement wires a year (about 11 per business day), about $260 million a year, from the division's **title escrow trust account** |
| Property management | About 430 rental homes for about 310 owners. About 1,700 rental applications a year are screened. Rents and security deposits are held in the **property management escrow account** |
| Consumers | Closing Services holds customer information on about 7,900 consumers (files since 2021 in the closing software, plus older scanned files). About 30% of buyers live outside Florida |
| Primary regulation | **FTC Safeguards Rule, 16 CFR Part 314 (N53-R01): applies.** The Closing Services division provides real estate settlement services, which 16 CFR 314.2(h)(2)(x) names as a financial activity (12 CFR 225.28(b)(2)(viii)). The division is a regular, separately staffed line of business (about 17% of receipts), so the company is "significantly engaged" (314.2(h)(1), (h)(3)(iv)). Customer information exceeds 5,000 consumers, so the 314.6 exceptions are not available. Brokerage alone would **not** have made the company a financial institution: acting as a "finder" (314.2(h)(2)(xiii)) excludes any activity that requires a real estate broker license (12 CFR 225.86(d)(1)(iii)(D)), and property management leases are operating leases (12 CFR 225.28(b)(3)(i)). Full reasoning in P03 |
| Secondary rule (wire fraud anchor) | Florida broker escrow duties: Fla. Stat. 475.25(1)(d)1. and (1)(k), and Fla. Admin. Code ch. 61J2-14 (deposit within 3 business days, monthly reconciliation). Closing funds in the title escrow trust account are trust funds under Fla. Stat. 626.8473 |
| Not in scope | FinCEN residential real estate reporting rule (31 CFR 1031.320): vacated nationwide by the U.S. District Court for the Eastern District of Texas on 2026-03-19 (*Flowers Title Companies, LLC v. Bessent*); FinCEN appealed to the Fifth Circuit; no reports are required while the order stands. It would reach the Closing Services division (as the settlement agent), not the brokerage as such (P03). CCPA/CPRA (N53-R03): no California business and receipts below the threshold. SEC disclosure (N53-R05): privately held. PCI DSS (N53-R04): rent card and ACH payments are taken only through the property management platform's hosted payment page; the company stores no card data. PCI obligations are noted, not assessed. The company does not originate or broker mortgage loans (agents give buyers a list of unaffiliated lenders) |
| State law approach | Florida law is cited only where a Florida duty is unavoidable: broker and title escrow (Fla. Stat. 475.25, 626.8473; ch. 61J2-14) and breach notification (Fla. Stat. 501.171). The samples otherwise stay federal |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Majority owner and Broker of Record | Managing member. The LLC has no board, so the majority owner is the governing body for the Qualified Individual's annual report (16 CFR 314.4(i)). Signatory on all escrow accounts (r. 61J2-14.010(1)). Accepts High and Very High risks |
| Chief Operating Officer (COO) | Executive owner of the information security program; approves policies; accepts Moderate risks |
| IT Manager | **Qualified Individual** (16 CFR 314.4(a)); runs IT with one IT Support Specialist and a contracted managed service provider |
| Closing Services Manager | Licensed title agent. Owns disbursement, wire release, and payoff verification procedures and the title escrow trust account |
| Controller | Owns the sales and property management escrow accounts' records and monthly reconciliations (r. 61J2-14.012), operating accounts, and commission disbursement |
| Director of Property Management | Owns tenant screening (P10 AI-001), owner and tenant communications, and the property management escrow account's operations |
| Transaction Coordination Manager | Owns the transaction management platform workflows and contract-to-close communications |
| Sales Managers (2, licensed brokers) | Supervise the affiliated sales associates; onboard and offboard them |
| Inside Sales Manager | Owns the CRM and the buyer lead scoring feature (P10 AI-002) |
| HR Manager | Employee onboarding, terminations, and training records |
| Managed service provider (MSP) | After-hours help desk, patching, firewall management. A service provider under 16 CFR 314.4(f) |

## 3. Systems

| ID | System | Hosting | Holds customer information or NPI? | Notes |
|---|---|---|---|---|
| SYS-01 | Transaction management platform (contracts, compliance review, document storage, agent and client portal) | Vendor SaaS | Yes | System of record for sales transactions. Used by employees and about 140 contractor agents. Vendor has a SOC 2 Type 2 report (P09) |
| SYS-02 | Closing and escrow software (settlement statements, disbursement ledger, positive pay file) | Vendor SaaS | Yes | Used by the 7 Closing Services staff and the Controller |
| SYS-03 | Identity provider (single sign-on and MFA) | SaaS | No (identities only) | Employees only. Contractor agents sign in to SYS-01 and SYS-04 with a password only (see gaps) |
| SYS-04 | Productivity suite (email, files, chat) | SaaS | Yes | Company email for employees and contractor agents. Main BEC target |
| SYS-05 | Cloud tenant (IaaS/PaaS) | Public cloud provider (vendor-agnostic) | Yes | Hosts three company-managed workloads: the **Closing Communications Portal** (a web application built for the company by a contract developer in 2023 to deliver closing documents and wire instructions to buyers and sellers), the integration service (syncs SYS-01, SYS-02, and SYS-09), and the backup vault |
| SYS-06 | Office networks (Main Office and Branch Office) | On-premises | Yes (in transit) | Firewalls, switches, staff Wi-Fi, guest Wi-Fi; site-to-site VPN to SYS-05. A network storage device at the Main Office holds scanned closing files from 2016 to 2022 |
| SYS-07 | Endpoints | On-premises | Yes (cached) | 64 company laptops and desktops for employees. Contractor agents use personal laptops and phones |
| SYS-08 | Commercial online banking for the escrow and operating accounts | Bank-hosted | Yes | Sales escrow, property management escrow, and title escrow trust accounts. Hardware tokens; dual approval for wires from the title escrow trust account; positive pay on checks |
| SYS-09 | CRM and lead management with buyer lead scoring | Vendor SaaS | Yes (contact and pre-approval data) | AI-002 in P10 |
| SYS-10 | Property management platform with tenant portal, online rent payments, and integrated tenant screening | Vendor SaaS | Yes (consumer reports, bank and card data handled by the platform's payment processor) | AI-001 in P10 |
| SYS-11 | E-signature service | Vendor SaaS | Yes | Integrated with SYS-01 and SYS-02 |
| SYS-12 | Accounting system | Vendor SaaS | Limited | Operating accounts and commission disbursement |

**SSP system (P02):** the *Transaction Management and Closing Communications System (TMCC)*: SYS-01, SYS-02, SYS-03, SYS-04, SYS-05, SYS-06, SYS-07, and their interfaces to SYS-08 and SYS-11.

## 4. Current security posture: partially compliant

**In place today:**
- MFA (authenticator app) for all 60 employees on the identity provider, email, and the cloud console
- Single sign-on for employees to SYS-01, SYS-02, SYS-09, and SYS-10
- Dual approval and hardware tokens for outgoing wires from the title escrow trust account; positive pay on escrow account checks. Wires from the sales and property management escrow accounts need only one approver
- Monthly escrow reconciliations for all three escrow accounts, signed by the Broker of Record (r. 61J2-14.012(2))
- Callback verification for **seller proceeds** wires, using the phone number collected at listing
- A wire fraud warning in every buyer's contract packet and in the transaction management platform's email footer
- Full-disk encryption and automatic OS patching on company laptops
- Signature antivirus on company endpoints
- An external-sender banner and basic spam filtering on email
- Daily backups of the SYS-05 workloads, stored in the same cloud account
- The SaaS vendors' own backups
- A paper shredding vendor at both offices

**Missing or weak, found in the 2026 assessments:**
1. No written risk assessment (16 CFR 314.4(b)(1)). The last review was an informal IT checklist in 2022.
2. The Qualified Individual was designated by email in 2023, not in the program document, and has never given the majority owner a written annual report (314.4(i)).
3. Wire verification is incomplete. Callback is required only for seller proceeds, not for **payoff and lien wires**, for **changed instructions** received by email, or for changes to property owners' payout bank accounts, and staff sometimes call the number printed in the email. Contractor agents forward wire instructions to buyers by ordinary email.
4. The 140 contractor agents sign in to email and the transaction management platform with a password only; MFA is enforced only for employees (314.4(c)(5)). Legacy email authentication protocols are still enabled, and the email domain's DMARC policy is set to monitor only.
5. No review of mailbox audit logs, and no alerts on new inbox forwarding rules or unusual sign-ins (314.4(c)(8)).
6. Encryption gaps: the Main Office network storage device holding scanned closing files (2016 to 2022) is unencrypted, and email carrying closing documents is not encrypted unless the sender chooses to. The Qualified Individual has approved no compensating controls (314.4(c)(3)).
7. No penetration test or vulnerability scanning has ever been performed, and there is no continuous monitoring (314.4(d)(2)).
8. The Closing Communications Portal was built with no secure development standard and has never been security tested (314.4(c)(4)).
9. No written incident response plan (314.4(h)). A March 2026 near miss (a spoofed wire instruction email that the buyer questioned) was handled ad hoc and not documented.
10. No inventory of service providers that access customer information, no security terms in most contracts, and no review of SOC reports (314.4(f)).
11. No retention and disposal schedule; customer information is kept indefinitely (314.4(c)(6)). Paper closing files sit in an unlocked storage room at the Branch Office.
12. Security training is an annual video for employees only. Contractor agents receive none, and there are no phishing exercises (314.4(e)(1)).
13. Departing contractor agents keep access for up to 14 days after they move to another brokerage, and the transaction management platform uses office-wide visibility, so every agent can open every transaction in their office.
14. Backups of SYS-05 share the production account and administrators; SaaS email and transaction data have no independent backup; no restore test has ever been done.
15. Five contractor agent mailboxes have automatic forwarding rules to external personal email accounts (found during P07 testing).

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P08 incident | Business email compromise targeting closing funds: a contractor agent's mailbox is taken over and a buyer is sent altered wire instructions; variant B covers a spoofed payoff letter that diverts an outgoing disbursement from the title escrow trust account |
| P09 SOC 2 | The company is not a service organization for business customers. (a) Security-only self-benchmark against the Trust Services Criteria, requested by the company's title insurance underwriter as part of its agent review; (b) review of the transaction management platform vendor's SOC 2 Type 2 report |
| P10 AI | Automated tenant and buyer screening: AI-001 tenant screening recommendations in the property management platform; AI-002 buyer lead scoring in the CRM |
| Cloud | Vendor-agnostic. Services are described by category, with AWS, Azure, and Google Cloud equivalents noted only where needed for shared responsibility |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-08-03 to 2026-08-14 | Risk assessment and gap analysis fieldwork |
| 2026-08-24 to 2026-08-28 | Control assessment fieldwork |
| 2026-09-21 | Deliverables approved by the COO (and by the majority owner for High risks) |
| 2026-09-26 | Regulatory status of the FinCEN rule and HUD disparate impact proposals rechecked before publication |
