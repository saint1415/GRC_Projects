# Scenario facts: Cris Santos Company | Management of Companies and Enterprises | Mid-Market

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or standard, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (the holding company; Florida corporation; privately held; private equity-backed; board of directors with an audit committee) |
| Business | Holding company (NAICS 551112, Offices of Other Holding Companies) that owns 100% of four operating subsidiaries and runs their shared services: IT and security, HR, payroll and benefits, accounting and consolidation, treasury, legal, procurement, and corporate development. The subsidiaries pay management fees under an intercompany services agreement |
| Subsidiaries | **CSC Building Supply, LLC** ("Supply"): wholesale distributor of building materials to contractors (NAICS 423310), with a distribution center and 3 branches. **CSC Home Services, LLC** ("Home Services"): residential heating, air conditioning, and plumbing service and replacement (NAICS 238220), with 3 shops (South, Central, North) and 85 service vans. **CSC Fabrication, LLC** ("Fabrication"): sheet metal ductwork and fittings manufacturing (NAICS 332322), one plant; it sells to contractors and to Home Services. **CSC Consumer Finance, LLC** ("Finance"): state-licensed consumer lender making installment loans for home improvement and heating and air conditioning equipment (NAICS 522291). Customers apply directly with Finance; Home Services gives customers Finance's application link but does not take, evaluate, or broker applications |
| Recent acquisition | On 2026-04-01 Home Services bought a regional heating and air conditioning company (about 45 employees). It operates as **Home Services North** and is not yet integrated into group IT (gap 2) |
| Location | Florida only. 9 sites: **HQ** (holding company and Finance), the **Supply distribution center** and **Supply Branches 1-3**, the **Home Services South, Central, and North shops**, and the **Fabrication plant** |
| Workforce | 600 employees: holding company 75, Supply 250, Home Services 180 (including 45 at Home Services North), Fabrication 65, Finance 30 |
| Receipts | About $100.0 million a year, consolidated (fictional): Supply $54.0 million, Home Services $26.0 million, Fabrication $12.0 million (external sales; sales to Home Services eliminate on consolidation), Finance $8.0 million (interest and fees). SBA counts the receipts of the concern and all its affiliates (13 CFR 121.103(a)(6); 121.104(d)(1)). $100.0 million exceeds the $45.5 million standard for NAICS 551112 (13 CFR 121.201), so the group is **not** SBA-small |
| Finance portfolio | About 11,800 active loans ($61 million outstanding) and about 1,000 applications a month. Finance holds customer information on about **34,000 consumers** (active borrowers, paid-off borrowers within the retention period, and declined applicants) |
| Ownership and securities status | **Privately held.** A private equity fund has owned about 70% since a 2023 recapitalization; the founder (Executive Chair) holds about 25%, and 22 managers hold the rest (24 holders of record). No class of securities is registered with the SEC, and the company files no reports under Exchange Act sections 13(a) or 15(d). With fewer than 2,000 holders of record, section 12(g) registration is not required (17 CFR 240.12g-1) |
| Financing | A senior secured credit facility with a bank syndicate at the holding company, and a separate warehouse line of credit at Finance. Both agreements require prompt notice of material adverse events and annual audited financial statements. These are contract terms, not law |
| Banking status | Not a bank holding company or savings and loan holding company: no subsidiary is a bank or savings association (12 CFR 225.2(b)-(c)). Finance takes no deposits |
| Safeguards Rule status | **Finance is a financial institution** under 16 CFR 314.2(h) (extending credit is a financial activity; 314.1(b) names "finance companies"), under FTC jurisdiction. It maintains customer information on more than 5,000 consumers, so the 314.6 exception does not apply. **The holding company is reached as Finance's affiliate and service provider:** it employs Finance's Qualified Individual (314.4(a)(1)-(3)) and receives, maintains, and processes Finance's customer information through shared identity, email, files, backups, the reporting warehouse, and bank file transfers (314.2(r); 314.4(f)). Supply, Home Services, and Fabrication are not financial institutions |
| Group health plan | **Self-funded** medical and pharmacy plan since 2024-01-01, sponsored by the holding company for all five employers. About 470 participants (enrolled employees) and about 1,100 covered persons. A third-party administrator (TPA) pays claims and a pharmacy benefit manager (PBM) runs the drug benefit; both are business associates of the plan. A stop-loss policy covers large claims. The plan is a **HIPAA covered entity** (a group health plan with 50 or more participants, 45 CFR 160.103). The holding company's Benefits team receives PHI for plan administration (appeals, stop-loss reimbursement files, monthly high-cost claimant reports), so the 164.530(k) relief for fully insured plans does **not** apply, and the plan documents must carry the 164.504(f) and 164.314(b) sponsor terms. The **Benefits Committee** (CFO, VP of Human Resources, General Counsel) is the plan administrator |
| Bank partner program | On 2026-08-15 Finance signed a forward-flow participation agreement with a community bank. From 2027-01 the bank will buy participations in new Finance loans, and Finance will service them. The bank's third-party risk program requires a SOC 2 Type 2 report covering Finance's servicing and the shared platform, and a separate SOC 1 Type 2 report on servicing controls relevant to its financial reporting |
| Payment cards | Supply counters and the Supply contractor portal, and Home Services technicians, take cards only through a processor's point-to-point encrypted terminals and readers and a hosted payment page. PCI DSS duties are contractual and noted, not assessed |
| Not in scope | SEC Regulation S-K Item 106, Form 8-K Item 1.05, and SOX section 404 (not an SEC registrant or issuer). Federal Reserve Regulation Y Subpart N and 12 CFR Part 225 Appendix F (not a bank holding company). FAR reporting clauses (no federal contracts or subcontracts). The Florida Digital Bill of Rights (a "controller" under Fla. Stat. 501.702 must exceed $1 billion in global gross annual revenue; the group has about $100 million) |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notification, Fla. Stat. 501.171; recording consent, Fla. Stat. 934.03). Former borrowers and employees who now live in other states are handled generically: apply the law of each state where affected individuals reside, with Florida as the worked example |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Board of directors (7 directors: 3 sponsor directors, the founder as Executive Chair, the CEO, 2 independent directors) | Approves the risk appetite; oversees cybersecurity risk through the audit committee; may grant a temporary exception for a Very High risk |
| Audit committee (2 independent directors and 1 sponsor director; chaired by an independent director) | Receives the group cybersecurity report each quarter (quarterly since 2026-09; annual before that); oversees internal audit and the POA&M |
| Private equity sponsor operating partner | Receives quarterly portfolio cyber metrics; the sponsor's portfolio cybersecurity standard requires an annual independent control assessment (contract with the sponsor) |
| Chief Executive Officer (CEO) | Accepts High risks; approves group policies, the security budget, and High-tier AI decisions |
| Chief Financial Officer (CFO) | Executive sponsor of the group security program; system owner of the Shared Corporate Services Platform; accepts Moderate risks; chairs the Benefits Committee |
| General Counsel | Legal and regulatory decisions, breach and notification determinations with outside counsel, privilege; Corporate Secretary |
| Virtual CISO (vCISO, part-time contractor, 2 days a week) | Program strategy, standards approval, audit committee reporting; reports to the CFO with a dotted line to the audit committee chair |
| VP of Information Technology | Runs shared IT (14 staff: infrastructure, service desk, applications); technical owner of the shared platform; owns recovery |
| Security Manager | Runs security day to day with 2 security analysts and 1 GRC analyst; **Qualified Individual for Finance** under 16 CFR 314.4(a), designated in writing in 2025; **HIPAA Security Official for the group health plan** (45 CFR 164.308(a)(2)) |
| Controller | Owns the ERP, the financial close, and ERP access roles |
| Treasurer | Owns the treasury management system and bank portals; approves wires with the CFO |
| VP of Human Resources | Owns the HRIS; **HIPAA Privacy Official for the group health plan**; sanctions with the General Counsel |
| Benefits Manager and Benefits Analyst | The only employees authorized to receive plan PHI for plan administration |
| VP of Corporate Development | Acquisitions, data rooms, and integration of acquired companies; handles material non-public deal information |
| Director of Procurement | Vendor onboarding and contracts |
| Subsidiary Presidents (Supply, Home Services, Fabrication, Finance) | Own their subsidiary's business risk and local systems; approve access for their staff; sit on the monthly cyber risk forum (new in 2026-10) |
| Finance President | The **senior member of Finance's personnel** who directs and oversees the Qualified Individual (16 CFR 314.4(a)(2)) |
| Finance Board of Managers (CEO, CFO, Finance President) | Finance's governing body; receives the Qualified Individual's annual written report (16 CFR 314.4(i)) |
| Finance Compliance Officer | Consumer credit compliance, adverse action notices, complaint handling; business reviewer for Finance AI use |
| Fabrication Plant Manager | Plant systems and machine vendors' remote access |
| Co-sourced internal audit firm | Reports to the audit committee; annual IT general controls review and the P07 control assessment; does not design or operate any assessed control |
| Managed security service provider (MSSP) | 24x7 EDR and SIEM monitoring; may isolate hosts without prior approval |

## 3. Systems

| ID | System | Hosting | Sensitive data | Notes |
|---|---|---|---|---|
| SYS-01 | Cloud ERP (multi-entity general ledger, payables, receivables, intercompany, consolidation, fixed assets) | Vendor SaaS | Financial reporting data; vendor bank details | System of record for all five entities. Vendor SOC 2 Type 2 |
| SYS-02 | Hybrid identity: one on-premises directory forest (2 domain controllers at HQ, 1 in the cloud shared services account) synchronized to a cloud identity provider (single sign-on, MFA, conditional access) | On-premises and SaaS | Identities for all integrated users | Home Services North is not yet in it |
| SYS-03 | Productivity suite (email, files, chat, phones, device management), one tenant with five email domains | SaaS | All categories, including Finance customer information, plan PHI, and deal information in files and email | 96 collaboration sites. Third-party backup since 2025. Includes the generative AI assistant (SYS-16) |
| SYS-04 | Cloud landing zone: 5 accounts (management, security and log archive, shared services, workloads, backup) | Public cloud (vendor-agnostic) | Customer bank account numbers (ACH files); consolidated financials; scanned invoices | Workloads: integration service, reporting data warehouse, bank file transfer (SFTP) server, invoice imaging |
| SYS-05 | HRIS, payroll, and benefits enrollment | Vendor SaaS | Employee SSNs, bank accounts, enrollment data | Five employer entities |
| SYS-06 | Treasury management system and bank portals | SaaS and bank-hosted | Bank credentials and payment instructions | Wires, ACH origination (Finance collections), positive pay; dual approval |
| SYS-07 | Board portal and virtual data room | Vendor SaaS | Board materials; acquisition material non-public information | Board, audit committee, and deal teams |
| SYS-08 | Endpoints | On-premises and mobile | Cached data of all types | 430 managed laptops and desktops, 95 technician tablets, 120 rugged warehouse scanners; 38 Home Services North laptops not yet managed |
| SYS-09 | Site networks at 9 sites on SD-WAN | On-premises; SD-WAN managed service | In transit | Firewalls, switches, Wi-Fi; site-to-cloud VPN |
| SYS-10 | On-premises servers: HQ server room (domain controllers, 3 file servers, print server, scanner management) and the Fabrication plant production server | On-premises | Legacy Supply department shares; production files | Backed up to a NAS at HQ; plant server backed up weekly to a removable drive |
| SYS-11 | Security operations stack: EDR, SIEM, vulnerability scanner | SaaS; MSSP-operated SIEM | Security logs | SIEM receives identity, suite, EDR, firewall, directory, and cloud logs |
| SYS-12 | Supply distribution and warehouse management system and contractor portal | Vendor SaaS (subsidiary system) | Contractor accounts, pricing, credit terms | Single sign-on for staff; contractor portal accounts managed by the vendor |
| SYS-13 | Home Services field-service management system | Vendor SaaS (subsidiary system) | Consumer names, addresses, service history | Single sign-on for South and Central. **Home Services North runs a separate field-service product with local accounts** |
| SYS-14 | Finance loan origination and servicing system, with the vendor's machine-learning credit scorecard | Vendor SaaS (subsidiary system) | Customer information: SSNs, bank accounts, credit reports, payment history | Single sign-on. Vendor SOC 2 Type 2 |
| SYS-15 | Fabrication plant systems: nesting and production scheduling software on the plant server; 4 CNC plasma tables and 6 press brakes on the plant floor network | On-premises (operational technology) | Production programs | 2 machine controllers run an unsupported embedded Windows version; machine vendors use an always-on remote access tool |
| SYS-16 | Generative AI assistant (enterprise add-on to SYS-03) | SaaS | Whatever the user can reach in SYS-03 | 180 licensed users across all five entities since 2026-05-04 |
| SYS-17 | Third-party services | Various | Various | About 160 vendors with access to group systems or data, including the health plan TPA and PBM, the MSSP, payroll tax and benefits carriers, and the AI vendors (P10) |

**SSP system (P02):** the *Shared Corporate Services Platform (SCSP)*: SYS-01 to SYS-11 and SYS-16, with interfaces to the subsidiary systems SYS-12 to SYS-15. Moderate baseline with tailoring.

## 4. Current security posture: defined program, gaps in scale

**In place today:**
- Single sign-on with MFA (push with number matching) for all integrated users of the ERP, email, HRIS, treasury system, loan servicing system, distribution system, and cloud consoles; conditional access requiring a compliant device for administrators
- EDR on all managed laptops, desktops, and servers, monitored 24x7 by the MSSP since 2025
- SIEM operated by the MSSP, with identity, suite, EDR, firewall, directory, and cloud logs
- Group information security policy set adopted in 2024; Finance's written information security program updated in 2025
- Annual group risk assessment (last 2025-08) and Qualified Individual reports to Finance's Board of Managers
- Quarterly external and internal vulnerability scans of HQ and the cloud landing zone; annual external penetration test (last 2025-11)
- Immutable backups of cloud workloads in a separate backup account (35-day write-once retention); third-party backup of the productivity suite
- ERP role-based access with payables segregation of duties; bank-enforced dual approval for wires and ACH; positive pay on all operating accounts
- Annual security awareness training and quarterly phishing simulations
- Annual co-sourced internal audit of IT general controls supporting the financial statement audit
- Cyber insurance and a crime policy with a social engineering fraud sublimit
- Privileged access broker with just-in-time elevation for cloud consoles

**Missing or weak, found in the 2026 assessments:**
1. Group governance has not kept pace with growth. The risk appetite (2025) is one paragraph with no measures, subsidiary Presidents have no written cyber duties, and until 2026-09 the audit committee received cyber reporting once a year. The Qualified Individual's 2025 report reached Finance's Board of Managers 5 months late (2026-02).
2. Home Services North (acquired 2026-04-01) is outside group controls: its own email tenant, a separate field-service product with local accounts, 38 laptops without group EDR or device management, and the seller's IT provider still holds administrator rights to its small server. The group has no written cyber due diligence or day-1 integration standard for acquisitions.
3. Identity is hybrid and over-privileged. The on-premises directory has 14 Domain Admins members (4 of them service accounts) and 61 service accounts, 23 with non-expiring passwords. Directory compromise reaches the cloud through synchronization. Administrators use push MFA, not phishing-resistant MFA, and privileged access management covers only the cloud consoles.
4. The access lifecycle is weak across entities. ERP access is reviewed twice a year for the financial statement auditor; no other system is reviewed. Transfers between subsidiaries keep old access, and subsidiary terminations reach shared IT on average 2 business days late.
5. Third-party risk management does not scale. About 160 vendors have access to group systems or data; 22 are critical, but SOC 2 reports are reviewed for only 8 of them. Finance's service provider oversight (16 CFR 314.4(f)) has no current inventory.
6. The self-funded health plan's security program is incomplete. No HIPAA Security Rule risk analysis covers plan PHI held by the sponsor; the plan documents carry the 164.504(f) privacy terms but not the 164.314(b) security terms; stop-loss and high-cost claimant files sit on an HR collaboration site open to 11 HR staff, not only the 2 authorized benefits staff.
7. Recovery is proven only for cloud workloads (restore test 2026-03). The domain controllers, HQ file servers, and the Fabrication plant server have never been restore-tested, there is no tested directory forest recovery, and the plant server backup is a weekly removable drive.
8. Logging coverage stops at the core. The HQ file servers, the plant network, Home Services North, and the SaaS line-of-business systems (SYS-12 to SYS-14), the ERP, and the HRIS do not send logs to the SIEM.
9. The Fabrication plant floor network is flat with the plant office network. Two machine controllers run an unsupported embedded Windows version, and machine vendors connect through an always-on remote access tool.
10. Vulnerability scanning covers only HQ and the cloud; branches, shops, and the plant are not scanned. 18% of critical findings in the first half of 2026 missed the 30-day remediation target.
11. The group incident response plan (2024) was exercised once, as a holding-company tabletop. Subsidiaries were not included, there is no payment-fraud playbook, and there is no procedure for a breach of plan PHI.
12. AI governance is missing. The generative AI assistant went to 180 users in 2026-05 without a data-access review; Finance's credit scorecard makes automated decisions with no model risk review or adverse action reason validation; Supply and Home Services adopted an applicant-ranking feature in their recruiting software without review; Home Services' after-hours AI voice agent triages emergency calls.
13. Data retention is not enforced. Finance keeps declined-applicant files and ACH collection files indefinitely, and there is no group retention schedule for shared file stores (16 CFR 314.4(c)(6)).

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P02 system | The registry default (shared corporate services platform, ERP and identity) fits this size and is kept: the SCSP is the platform every subsidiary depends on |
| P03 benchmark and regulations | NIST CSF 2.0 group profile (voluntary), now covering all 106 subcategories, with subsidiary profiles, built with NIST SP 1301. Binding rules for the main line of business analyzed at requirement level: the FTC Safeguards Rule (16 CFR Part 314) for Finance and the holding company as its service provider, and the HIPAA Security Rule and plan sponsor requirements for the self-funded group health plan |
| P08 incidents | **Two incident types:** (1) compromise of shared services affecting subsidiaries (the registry default): a stolen administrator session leads to directory compromise, data theft from shared file stores, and ransomware across subsidiaries; (2) treasury payment fraud through business email compromise. Integrated with crisis management and legal |
| P09 SOC 2 | Readiness for a SOC 2 Type 2 examination requested by Finance's bank partner (Security, Availability, Processing Integrity, Confidentiality), plus a vendor SOC 2 review program |
| P10 AI | AI use-case portfolio: the enterprise generative AI assistant across subsidiaries (the registry default, AI-001) plus the other AI uses found in the inventory |
| Cloud | One public cloud provider in a 5-account landing zone, plus SaaS and on-premises systems. Vendor-agnostic; AWS, Azure, and Google Cloud names appear only in an equivalents table |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-07-13 to 2026-08-07 | BIA, risk assessment, CSF group profile, and regulatory gap analysis fieldwork (interviews and walkthroughs at 6 of 9 sites) |
| 2026-08-17 to 2026-09-04 | Control assessment fieldwork (co-sourced internal audit firm) |
| 2026-09-22 | Deliverables approved (CEO for High risks and policies; CFO for Moderate); results to the audit committee; Qualified Individual's 2026 written report to Finance's Board of Managers; plan risk analysis accepted by the Benefits Committee |
