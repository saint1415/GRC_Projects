# Scenario facts: Cris Santos Company | Management of Companies and Enterprises | Small

All 10 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a regulation or standard, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (the holding company; manager-managed Florida LLC) |
| Business | Holding company managing three operating subsidiaries (NAICS 551112, Offices of Other Holding Companies). It owns 100% of each subsidiary and runs shared services for all of them: IT, human resources and payroll, accounting, treasury, and financial reporting |
| Subsidiaries | **CSC Building Supply, LLC** ("Supply"): wholesale distributor of building materials to contractors (NAICS 423310), one warehouse and sales counter. **CSC Home Services, LLC** ("Home Services"): residential heating, air conditioning, and plumbing service and replacement (NAICS 238220), one shop and 11 service vans. **CSC Consumer Finance, LLC** ("Finance"): state-licensed consumer lender making installment loans for home improvement and HVAC equipment (NAICS 522291). Customers apply directly with Finance; Home Services only hands customers Finance's application link and does not take, evaluate, or broker applications |
| Location | Florida. Three sites: **HQ** (holding company and Finance, one office building), **Supply warehouse** (about 20 miles from HQ), and **Home Services shop** (about 12 miles from HQ) |
| Workforce | 60 employees across the group: holding company 14 (CEO, CFO, Controller, 2 staff accountants, accounts payable specialist, treasury and payments analyst, HR Director, HR and payroll specialist, IT Manager, systems administrator, IT support specialist, corporate development director, executive assistant), Supply 22, Home Services 15, Finance 9 |
| Receipts | $27.3 million a year, consolidated (fictional): Supply $19.6 million, Home Services $4.6 million, Finance $3.1 million (interest and fees). Management fees the subsidiaries pay the holding company eliminate on consolidation. SBA counts the receipts of the concern and all its affiliates (13 CFR 121.103(a)(6); 121.104(d)(1)); $27.3 million is under the $45.5 million standard for NAICS 551112, so the group is SBA-small |
| Finance portfolio | About 3,300 active loans ($14 million outstanding). Customer information on about 8,600 consumers (active borrowers, paid-off borrowers within the retention period, and declined applicants) |
| Ownership and securities status | **Privately held.** Cris Santos is the majority owner; four minority members (family members and two executives) hold the rest. No class of securities is registered with the SEC, and the company files no reports under Exchange Act sections 13(a) or 15(d). It has fewer than 2,000 holders of record, so Exchange Act section 12(g) registration is not required (17 CFR 240.12g-1) |
| Banking status | Not a bank holding company or savings and loan holding company: no subsidiary is a bank or savings association (12 CFR 225.2(b)-(c)). Finance is funded by a bank line of credit |
| Safeguards Rule status | **Finance is a financial institution** under 16 CFR 314.2(h) (extending credit is a financial activity; 314.1(b) names "finance companies"), under FTC jurisdiction. It maintains customer information on more than 5,000 consumers, so the 314.6 exception does not apply. **The holding company is reached as Finance's affiliate and service provider:** it employs Finance's Qualified Individual (314.4(a)(1)-(3)) and receives, maintains, and processes Finance's customer information through shared IT, email, file storage, backups, and bank file transfers (314.2(r); 314.4(f)). Supply and Home Services are not financial institutions |
| Group health plan | Fully insured group health plan for all four employers, about 52 participants. The holding company (plan sponsor) receives only enrollment and disenrollment information and summary health information. The plan therefore gets the relief in 45 CFR 164.530(k), and the plan-document security requirements of 164.314(b) do not apply (exception for disclosures under 164.504(f)(1)(ii)-(iii)) |
| Not in scope | SEC Regulation S-K Item 106 and Form 8-K Item 1.05 and SOX section 404 (the company is not an SEC registrant or issuer). Federal Reserve Regulation Y Subpart N and 12 CFR Part 225 Appendix F (not a bank holding company). Payment card data: Supply and Home Services take cards only through a processor's point-to-point encrypted terminals and hosted payment page; PCI DSS duties are contractual and noted, not assessed |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notification, Fla. Stat. 501.171). The samples otherwise stay federal |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Board of Managers of the holding company (majority owner as Chair, CEO, one independent manager) | Oversees cybersecurity risk for the group; accepts Very High risks; receives the group cybersecurity report twice a year (new, starting 2026-09-25) |
| Majority owner (Cris Santos) | Chairs the Board of Managers |
| Chief Executive Officer (CEO) | Executive sponsor of the group program; accepts High risks and reports each acceptance to the Board of Managers; approves group policies |
| Chief Financial Officer (CFO) | Owner of shared services and of the group security program; accepts Moderate risks; IT reports to the CFO |
| IT Manager | Runs shared IT and the group security program day to day; **Qualified Individual for Finance** under 16 CFR 314.4(a), designated in writing in 2023 |
| Systems Administrator and IT Support Specialist | Identity, endpoint, cloud, and help desk administration |
| Controller | Owns the ERP, the financial close, and ERP access roles |
| Treasury and Payments Analyst | Prepares payments and bank files; bank portal administrator with the CFO |
| HR Director | Owns the HRIS, onboarding and termination notices, and the group health plan administration |
| Corporate Development Director | Runs acquisition projects and the data room; handles material non-public deal information |
| Subsidiary Presidents (Supply, Home Services, Finance) | Own their subsidiary's business risk and local systems; approve access for their staff |
| Finance President | The **senior member of Finance's personnel** who directs and oversees the Qualified Individual (16 CFR 314.4(a)(2)) |
| Finance Board of Managers (CEO, CFO, Finance President) | Finance's governing body; receives the Qualified Individual's annual written report (16 CFR 314.4(i)) |
| Co-managed IT provider (MSP) | After-hours help desk, firewall and server patching. Holds 2 administrator accounts in the group identity tenant |

## 3. Systems

| ID | System | Hosting | Sensitive data | Notes |
|---|---|---|---|---|
| SYS-01 | Cloud ERP (multi-entity general ledger, payables, receivables, intercompany, consolidation) | Vendor SaaS | Financial reporting data; vendor bank details; employee expense data | System of record for all four entities. Vendor has a SOC 2 Type 2 report (reviewed in P09) |
| SYS-02 | Identity provider (single sign-on and MFA), one group tenant | SaaS | Identities for all 60 employees and the MSP | Protects SYS-01, SYS-03, SYS-05, SYS-07, SYS-10, SYS-12, and the cloud console |
| SYS-03 | Productivity suite (email, files, chat, device management), one tenant with four email domains | SaaS | All categories, including Finance customer information in files and email | 41 collaboration sites. Includes the generative AI assistant add-on (SYS-13) |
| SYS-04 | Cloud tenant (IaaS/PaaS) | Public cloud provider (vendor-agnostic) | Customer bank account numbers (ACH files); consolidated financials | Hosts four group-managed workloads: the integration service (subsidiary systems to ERP), the reporting database, the managed file transfer (SFTP) server for bank files, and the backup vault |
| SYS-05 | HRIS and payroll | Vendor SaaS | Employee SSNs, bank accounts, benefits enrollment | Four employer entities, 60 employees |
| SYS-06 | Online banking and treasury portals | Bank-hosted | Operating account credentials | Wires, ACH origination (Finance loan collections), positive pay. Dual approval enforced by the bank |
| SYS-07 | Board portal | Vendor SaaS | Board materials; acquisition materials (MNPI) | Holding company and Finance boards |
| SYS-08 | Endpoints | On-premises and mobile | Cached data of all types | 50 laptops, 10 desktops (warehouse counter and dispatch), 16 tablets (Home Services technicians). Managed through SYS-03 device management |
| SYS-09 | Site networks (HQ, Supply warehouse, Home Services shop) | On-premises | In transit | Firewalls, switches, Wi-Fi; site-to-site VPN to SYS-04 |
| SYS-10 | Supply distribution and warehouse management system | Vendor SaaS (subsidiary system) | Contractor customer accounts and pricing | Single sign-on through SYS-02 |
| SYS-11 | Home Services field-service management system | Vendor SaaS (subsidiary system) | Consumer names, addresses, service history | **Local accounts, not in single sign-on** (see gaps) |
| SYS-12 | Finance loan origination and servicing system | Vendor SaaS (subsidiary system) | Customer information: SSNs, bank accounts, credit reports, payment history | Single sign-on through SYS-02. Vendor has a SOC 2 Type 2 report |
| SYS-13 | Generative AI assistant (enterprise add-on to SYS-03) | SaaS | Whatever the user can reach in SYS-03 | Pilot with 25 users across all four entities since 2026-07-06 (see P10) |

**SSP system (P02):** the *Shared Corporate Services Platform (SCSP)*: SYS-01, SYS-02, SYS-03 (including SYS-13), SYS-04, SYS-05, SYS-08, SYS-09, and their interfaces to SYS-06, SYS-07, SYS-10, SYS-11, and SYS-12.

## 4. Current security posture: partially compliant

**In place today:**
- Single sign-on with MFA (authenticator app push with number matching) for all users of the ERP, email, HRIS, loan servicing system, distribution system, and cloud console
- ERP role-based access with payables segregation of duties (vendor master changes separate from payment release), configured in 2025
- Bank-enforced dual approval for wires and ACH batches; positive pay on all operating accounts
- Endpoint detection and response (EDR) on all laptops and desktops
- Automatic operating system and browser patching on endpoints through device management
- Full-disk encryption on all laptops and desktops; tablets enrolled with a PIN and remote wipe
- Daily backups of cloud tenant workloads (stored in the same account and region)
- SOC 2 Type 2 reports obtained from the ERP, HRIS, and loan servicing vendors
- Annual online security awareness training for all employees since 2025
- Finance's written information security program (WISP, 2023) and the written Qualified Individual designation; a Qualified Individual report was delivered to Finance's Board of Managers in 2024
- Firewalls at all three sites; site-to-site VPN to the cloud tenant; guest Wi-Fi separated
- A group cyber insurance policy with a breach hotline

**Missing or weak, found in the 2026 assessments:**
1. No group-level cybersecurity governance. There is no group risk appetite, no defined cyber roles for the subsidiary Presidents, and no cybersecurity reporting to the Board of Managers.
2. Written security policies exist only in Finance's 2023 WISP, which has not been updated. The holding company, Supply, and Home Services have no adopted policies.
3. The Qualified Individual's annual written report to Finance's Board of Managers was not delivered for 2025, and Finance's written risk assessment has not been updated since 2023 (16 CFR 314.4(b), (i)).
4. The shared identity tenant is flat. It has 7 global administrator accounts (including 2 MSP accounts). Administrators use push MFA, not phishing-resistant MFA. No conditional access policy blocks unmanaged devices.
5. File sharing is too broad. 3 of 41 collaboration sites grant access to all group employees, including Finance's loan-documents archive (about 2,100 files with customer information). This was found on 2026-08-12, when the AI assistant pilot showed a loan document to a Supply user.
6. There is no central log collection or review. Identity sign-in and email audit logs are kept only for the 30 days the current license allows.
7. EDR alerts are monitored only during business hours by the IT team. Nobody covers nights or weekends.
8. Email and files in the productivity suite have no independent backup. Cloud tenant backups share the production account and region. No restore has ever been tested.
9. There is no group incident response plan. The incident section of Finance's WISP has never been tested, and the subsidiaries have no escalation path.
10. Vendor oversight is weak. The ERP and loan servicing vendors' SOC 2 reports were received but never reviewed. There is no inventory of service providers with access to Finance customer information, and the MSP contract has no security requirements.
11. Offboarding is slow. Subsidiary terminations reach shared IT by email, on average 3 business days later. The Home Services field-service system (SYS-11) uses local accounts outside single sign-on.
12. Payment fraud controls are informal. Vendor bank-detail changes are accepted by email without an independent callback, and callbacks on new wire payees are not documented.
13. There is no vulnerability scanning or penetration testing, which Finance needs under 16 CFR 314.4(d)(2). The Home Services firewall firmware is two major versions behind.
14. ACH collection files with consumer bank account numbers are kept indefinitely on the SFTP server. There is no retention schedule or disposal procedure (16 CFR 314.4(c)(6)).
15. The generative AI assistant pilot started on 2026-07-06 without an approved-use policy, a data-access review, or an approved-tools list.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 benchmark | NIST CSF 2.0 group profile (voluntary): one Group Organizational Profile for the holding company and the shared platform, plus three subsidiary profiles, built with NIST SP 1301 (Quick-Start Guide for Creating and Using Organizational Profiles). Secondary: the FTC Safeguards Rule (16 CFR Part 314) as it applies to Finance and reaches the holding company |
| P08 incident | Compromise of the shared identity and email tenant affecting all subsidiaries: adversary-in-the-middle phishing of the shared-services accounts payable specialist, mailbox takeover, a payment redirection attempt, and access to shared file sites holding Finance customer information and employee records |
| P09 SOC 2 | Security-only self-benchmark (the holding company provides shared services only to its own subsidiaries, not to outside customers), plus a review of the ERP vendor's SOC 2 Type 2 report |
| P10 AI | Enterprise generative AI assistant pilot across the holding company and subsidiaries |
| Cloud | Vendor-agnostic. Services are described by category, with AWS, Azure, and Google Cloud equivalents noted only where needed for shared responsibility |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-08-17 to 2026-08-28 | Risk assessment, CSF group profile, and Safeguards Rule gap analysis fieldwork (interviews at all three sites) |
| 2026-09-08 to 2026-09-11 | Control assessment fieldwork (independent assessor) |
| 2026-09-25 | Deliverables approved by the CEO; High-risk treatment plans approved by the Board of Managers; Qualified Individual's written report delivered to Finance's Board of Managers |
