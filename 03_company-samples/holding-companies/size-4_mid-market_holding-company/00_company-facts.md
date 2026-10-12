# Scenario facts: Cris Santos Company | Management of Companies and Enterprises | Mid-Market

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or standard, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (the holding company; Florida corporation; privately held; private equity-backed; board of directors with an audit committee) |
| Business | Holding company (NAICS 551112, Offices of Other Holding Companies) that owns 100% of four operating subsidiaries and runs their shared services: IT and security, HR, payroll and benefits, accounting and consolidation, treasury, legal, procurement, and corporate development. The subsidiaries pay management fees under an intercompany services agreement |
| Subsidiaries | **CSC Building Supply, LLC** ("Supply"): wholesale distributor of building materials to contractors (NAICS 423310), with a distribution center and 3 branches. **CSC Home Services, LLC** ("Home Services"): residential heating, air conditioning, and plumbing service and replacement (NAICS 238220), with 3 shops (South, Central, North) and 85 service vans. **CSC Fabrication, LLC** ("Fabrication"): sheet metal ductwork and fittings manufacturing (NAICS 332322), one plant; it sells to contractors and to Home Services. **CSC Consumer Finance, LLC** ("Finance"): state-licensed consumer lender making installment loans for home improvement and heating and air conditioning equipment (NAICS 522291). Customers apply directly with Finance; Home Services gives customers Finance's application link but does not take, evaluate, or broker applications |
| Recent acquisition | On 2026-04-01 Home Services bought a regional heating and air conditioning company (about 45 employees). It operates as **Home Services North** and is not yet integrated into group IT (EV-017) |
| Location | Florida only. 9 sites: **HQ** (holding company and Finance), the **Supply distribution center** and **Supply Branches 1-3**, the **Home Services South, Central, and North shops**, and the **Fabrication plant** |
| Workforce | 600 employees: holding company 75, Supply 250, Home Services 180 (including 45 at Home Services North), Fabrication 65, Finance 30 |
| Receipts | About $100.0 million a year, consolidated (fictional): Supply $54.0 million, Home Services $26.0 million, Fabrication $12.0 million (external sales; sales to Home Services eliminate on consolidation), Finance $8.0 million (interest and fees). SBA counts the receipts of the concern and all its affiliates (13 CFR 121.103(a)(6); 121.104(d)(1)). $100.0 million exceeds the $45.5 million standard for NAICS 551112 (13 CFR 121.201), so the group is **not** SBA-small |
| Finance portfolio | About 11,800 active loans ($61 million outstanding) and about 1,000 applications a month. Finance holds customer information on about **34,000 consumers** (active borrowers, paid-off borrowers within the retention period, and declined applicants) |
| Ownership and securities status | **Privately held.** A private equity fund has owned about 70% since a 2023 recapitalization; the founder (Executive Chair) holds about 25%, and 22 managers hold the rest (24 holders of record). No class of securities is registered with the SEC, and the company files no reports under Exchange Act sections 13(a) or 15(d). With fewer than 2,000 holders of record, section 12(g) registration is not required (17 CFR 240.12g-1). Applicability of N55-R01 to N55-R03 is decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (EV-050) |
| Financing | A senior secured credit facility with a bank syndicate at the holding company, and a separate warehouse line of credit at Finance. Both agreements require prompt notice of material adverse events and annual audited financial statements. These are contract terms, not law |
| Banking status | Not a bank holding company or savings and loan holding company: no subsidiary is a bank or savings association (12 CFR 225.2(b)-(c)). Finance takes no deposits (obligations register N55-R04 and N55-R05; EV-050) |
| Safeguards Rule status | **Finance is a financial institution** under 16 CFR 314.2(h) (extending credit is a financial activity; 314.1(b) names "finance companies"), under FTC jurisdiction. It maintains customer information on more than 5,000 consumers, so the 314.6 exception does not apply. **The holding company is reached as Finance's affiliate and service provider:** it employs Finance's Qualified Individual (314.4(a)(1)-(3)) and receives, maintains, and processes Finance's customer information through shared identity, email, files, backups, the reporting warehouse, and bank file transfers (314.2(r); 314.4(f)). Supply, Home Services, and Fabrication are not financial institutions. Determined in the intake obligations register (FTC-314; EV-054, EV-069) |
| Group health plan | **Self-funded** medical and pharmacy plan since 2024-01-01, sponsored by the holding company for all five employers. About 470 participants (enrolled employees) and about 1,100 covered persons. A third-party administrator (TPA) pays claims and a pharmacy benefit manager (PBM) runs the drug benefit; both are business associates of the plan. A stop-loss policy covers large claims. The plan is a **HIPAA covered entity** (a group health plan with 50 or more participants, 45 CFR 160.103). The holding company's Benefits team receives PHI for plan administration (appeals, stop-loss reimbursement files, monthly high-cost claimant reports), so the 164.530(k) relief for fully insured plans does **not** apply, and the plan documents must carry the 164.504(f) and 164.314(b) sponsor terms. The **Benefits Committee** (CFO, VP of Human Resources, General Counsel) is the plan administrator. Determined in the intake obligations register (N55-R06; EV-047) |
| Bank partner program | On 2026-08-15 Finance signed a forward-flow participation agreement with a community bank. From 2027-01 the bank will buy participations in new Finance loans, and Finance will service them. The bank's third-party risk program requires a SOC 2 Type 2 report covering Finance's servicing and the shared platform, and a separate SOC 1 Type 2 report on servicing controls relevant to its financial reporting |
| Payment cards | Supply counters and the Supply contractor portal, and Home Services technicians, take cards only through a processor's point-to-point encrypted terminals and readers and a hosted payment page. PCI DSS duties are contractual and noted, not assessed (obligations register PCI-DSS; EV-049) |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): SEC Regulation S-K Item 106, Form 8-K Item 1.05, and SOX section 404 (not an SEC registrant or issuer). Federal Reserve Regulation Y Subpart N and 12 CFR Part 225 Appendix F (not a bank holding company). FAR reporting clauses (no federal contracts or subcontracts; EV-050). The Florida Digital Bill of Rights (a "controller" under Fla. Stat. 501.702 must exceed $1 billion in global gross annual revenue; the group has about $100 million; EV-052) |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notification, Fla. Stat. 501.171; recording consent, Fla. Stat. 934.03). Former borrowers and employees who now live in other states are handled generically: apply the law of each state where affected individuals reside, with Florida as the worked example |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Board of directors (7 directors: 3 sponsor directors, the founder as Executive Chair, the CEO, 2 independent directors) | Approves the risk appetite; oversees cybersecurity risk through the audit committee; may grant a temporary exception for a Very High risk |
| Audit committee (2 independent directors and 1 sponsor director; chaired by an independent director) | Receives the group cybersecurity report each quarter (quarterly since 2026-09; annual before that, EV-028); oversees internal audit and the POA&M |
| Private equity sponsor operating partner | Receives quarterly portfolio cyber metrics; the sponsor's portfolio cybersecurity standard requires an annual independent control assessment (contract with the sponsor) |
| Chief Executive Officer (CEO) | Accepts High risks; approves group policies, the security budget, and High-tier AI decisions |
| Chief Financial Officer (CFO) | Executive sponsor of the group security program; system owner of the Shared Corporate Services Platform; accepts Moderate risks; chairs the Benefits Committee |
| General Counsel | Legal and regulatory decisions, breach and notification determinations with outside counsel, privilege; Corporate Secretary |
| Virtual CISO (vCISO, part-time contractor, 2 days a week) | Program strategy, standards approval, audit committee reporting; reports to the CFO with a dotted line to the audit committee chair |
| VP of Information Technology | Runs shared IT (14 staff: infrastructure, service desk, applications); technical owner of the shared platform; owns recovery |
| Security Manager | Runs security day to day with 2 security analysts and 1 GRC analyst; **Qualified Individual for Finance** under 16 CFR 314.4(a), designated in writing in 2025 (EV-034); **HIPAA Security Official for the group health plan** (45 CFR 164.308(a)(2)) |
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
| Co-sourced internal audit firm | Reports to the audit committee; annual IT general controls review (EV-029) and the P07 control assessment; does not design or operate any assessed control |
| Managed security service provider (MSSP) | 24x7 EDR and SIEM monitoring; may isolate hosts without prior approval (EV-021) |

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv). Suppliers are in [`step-00_P00_intake/vendor-register.csv`](step-00_P00_intake/vendor-register.csv).

| ID | System | Hosting | Sensitive data | Notes |
|---|---|---|---|---|
| SYS-01 | Cloud ERP (multi-entity general ledger, payables, receivables, intercompany, consolidation, fixed assets) | Vendor SaaS | Financial reporting data; vendor bank details | System of record for all five entities. Vendor SOC 2 Type 2 (EV-041) |
| SYS-02 | Hybrid identity: one on-premises directory forest (2 domain controllers at HQ, 1 in the cloud shared services account) synchronized to a cloud identity provider (single sign-on, MFA, conditional access) | On-premises and SaaS | Identities for all integrated users | Home Services North is not yet in it (EV-001, EV-017) |
| SYS-03 | Productivity suite (email, files, chat, phones, device management), one tenant with five email domains | SaaS | All categories, including Finance customer information, plan PHI, and deal information in files and email | 96 collaboration sites. Third-party backup since 2025 (EV-019). Includes the generative AI assistant (SYS-16) |
| SYS-04 | Cloud landing zone: 5 accounts (management, security and log archive, shared services, workloads, backup) | Public cloud (vendor-agnostic) | Customer bank account numbers (ACH files); consolidated financials; scanned invoices | Workloads: integration service, reporting data warehouse, bank file transfer (SFTP) server, invoice imaging |
| SYS-05 | HRIS, payroll, and benefits enrollment | Vendor SaaS | Employee SSNs, bank accounts, enrollment data | Five employer entities |
| SYS-06 | Treasury management system and bank portals | SaaS and bank-hosted | Bank credentials and payment instructions | Wires, ACH origination (Finance collections), positive pay; dual approval |
| SYS-07 | Board portal and virtual data room | Vendor SaaS | Board materials; acquisition material non-public information | Board, audit committee, and deal teams |
| SYS-08 | Endpoints | On-premises and mobile | Cached data of all types | 430 managed laptops and desktops, 95 technician tablets, 120 rugged warehouse scanners; 38 Home Services North laptops not yet managed (EV-012, EV-017) |
| SYS-09 | Site networks at 9 sites on SD-WAN | On-premises; SD-WAN managed service | In transit | Firewalls, switches, Wi-Fi; site-to-cloud VPN |
| SYS-10 | On-premises servers: HQ server room (domain controllers, 3 file servers, print server, scanner management) and the Fabrication plant production server | On-premises | Legacy Supply department shares; production files | Backed up to a NAS at HQ; plant server backed up weekly to a removable drive (EV-019) |
| SYS-11 | Security operations stack: EDR, SIEM, vulnerability scanner | SaaS; MSSP-operated SIEM | Security logs | SIEM receives identity, suite, EDR, firewall, directory, and cloud logs (EV-021) |
| SYS-12 | Supply distribution and warehouse management system and contractor portal | Vendor SaaS (subsidiary system) | Contractor accounts, pricing, credit terms | Single sign-on for staff; contractor portal accounts managed by the vendor |
| SYS-13 | Home Services field-service management system | Vendor SaaS (subsidiary system) | Consumer names, addresses, service history | Single sign-on for South and Central. **Home Services North runs a separate field-service product with local accounts** (EV-017) |
| SYS-14 | Finance loan origination and servicing system, with the vendor's machine-learning credit scorecard | Vendor SaaS (subsidiary system) | Customer information: SSNs, bank accounts, credit reports, payment history | Single sign-on. Vendor SOC 2 Type 2 (EV-041) |
| SYS-15 | Fabrication plant systems: nesting and production scheduling software on the plant server; 4 CNC plasma tables and 6 press brakes on the plant floor network | On-premises (operational technology) | Production programs | 2 machine controllers run an unsupported embedded Windows version; machine vendors use an always-on remote access tool (EV-016) |
| SYS-16 | Generative AI assistant (enterprise add-on to SYS-03) | SaaS | Whatever the user can reach in SYS-03 | 180 licensed users across all five entities since 2026-05-04 (EV-056) |
| SYS-17 | Third-party services | Various | Various | About 160 vendors with access to group systems or data, including the health plan TPA and PBM, the MSSP, payroll tax and benefits carriers, and the AI vendors (P10) (EV-038) |

**SSP system (P02):** the *Shared Corporate Services Platform (SCSP)*: SYS-01 to SYS-11 and SYS-16, with interfaces to the subsidiary systems SYS-12 to SYS-15. Moderate baseline with tailoring.

## 4. Where the evidence is

This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Every item has a source system, an owner, and as-of and collected dates.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps against the FTC Safeguards Rule, the HIPAA Security Rule and plan sponsor terms, the Breach Notification Rule, Fla. Stat. 501.171 and the CSF 2.0 group profile** are judged in the gap analysis (P03), and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

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
| 2026-06-29 to 2026-07-10 | Intake: evidence requests, exports, inventories, obligations register |
| 2026-07-13 to 2026-08-07 | BIA interviews, risk assessment, CSF group profile, and regulatory gap analysis fieldwork (interviews and walkthroughs at 6 of 9 sites) |
| 2026-08-10 to 2026-08-14 | Policies POL-01 to POL-05, the standards index and the P08 runbooks drafted from the gaps |
| 2026-08-17 to 2026-09-04 | Control assessment fieldwork (co-sourced internal audit firm): operating tests of controls already in place; design review of the draft policies, standards and runbooks |
| 2026-08-17 to 2026-09-10 | AI governance assessment (P10); tests 2026-08-24 to 2026-09-09 |
| 2026-09-22 | Deliverables approved (CEO for High risks and policies; CFO for Moderate); results to the audit committee; Qualified Individual's 2026 written report to Finance's Board of Managers; plan risk analysis accepted by the Benefits Committee |
| 2026-10-01 | 2026 policies take effect |
| 2027-03 (planned) | Follow-up assessment: operating effectiveness of the controls the new policies and standards introduced, after at least one quarter of operation |

## 7. Facts added during the Phase 5 build (fictional; used across P01-P10)
These details were added so the deliverables could be specific. They do not change sections 1-6.

| Topic | Added fact |
|---|---|
| Registry defaults | Primary system kept (shared corporate services platform). Incident kept as runbook 1 (compromise of shared services affecting subsidiaries); a second incident type, treasury payment fraud through business email compromise, was added because mid-market depth calls for two and payments are the group's most likely direct loss. AI use case kept as AI-001 and widened to the portfolio the inventory found (AI-001 to AI-007) |
| Terminology | "Shared Corporate Services Platform (SCSP)" is the SSP system in P02, identifier CSC-SCSP-01. "Tier 1 systems" are the ERP, treasury system, HRIS, loan servicing system, directory, cloud, and benefits site |
| Holders of record | 24 (the sponsor fund, the founder, and 22 managers) (EV-050) |
| Revenue and cash per business day (250 days) | Supply about $216,000 of sales; Home Services about $104,000; Fabrication about $48,000. Finance collects about $220,000 a business day (about 560 payments). Treasury releases about $3.5 million of payments a business day (about 140 outgoing payments and 2 ACH files). Payroll is about $1.4 million per biweekly cycle. Plan claim funding is about $160,000 a week; about 20 plan appeals a year (EV-052, EV-053, EV-047) |
| BIA recovery assumptions | About 40% of lost Supply counter sales, 35% of missed Home Services calls, and 25% of delayed Fabrication orders are not recovered (EV-059) |
| Operating volumes | Supply: about 900 orders and 300 deliveries a day, 22 trucks, 110 distribution center staff, purchasing team of 5. Home Services: about 260 calls and 180 jobs a day in summer, about 25 no-cooling emergency calls a day in July, 12 dispatchers. Fabrication: about 70 production orders a day, 50 plant staff, 6 office staff. Finance: about 45 applications and 20 fundings a business day, 12 servicing staff, 6 underwriters, about 15 complaints a month. Holding company: accounts payable team of 6 (about 4,200 invoices a month), accounting team of 10, HR team of 8, corporate development team of 3, 2 treasury analysts (EV-053, EV-054, EV-059) |
| Insurance | Cyber policy: $10 million limit, $200,000 retention; carrier panel supplies breach counsel and forensics; notice through the carrier hotline before engaging incident vendors. Crime policy with a $250,000 social engineering fraud sublimit (EV-045) |
| Vendor recovery commitments | ERP RTO 12 h and RPO 1 h; loan servicing RTO 8 h and RPO 1 h; HRIS RTO 24 h; treasury system RTO 8 h (per their SOC 2 system descriptions); distribution system contract RTO 24 h (no SOC 2); identity provider and suite availability commitments 99.9% (EV-041, EV-040) |
| Networks and spares | Dual ISPs at HQ and the distribution center; cellular failover at branches and shops; single ISP at the plant; Home Services North not on SD-WAN. 12 pre-imaged spare laptops at HQ and 4 at each Home Services shop (EV-014, EV-012) |
| Security-relevant details | Backup design and restore history, identity and privileged account counts, workforce activity and access review dates, training and phishing results, security operations (incidents, MSSP terms, penetration tests, scan results, firmware, changes, servers, retired devices), vendor and SaaS counts, plan administration, and Finance governance are recorded from the systems of record in the intake evidence register (EV-001 to EV-058), not stated here. Data locations come from the P03 data location review (EV-065), Finance service provider contract terms from the P03 contract sample (EV-068), and the treasury system vendor's qualified SOC 2 opinion from the P09 vendor review |
| Contract notice terms | Bank partner participation agreement: notice within 72 hours of determining a security incident affecting servicing systems or participated-loan data (from 2027-01). Sponsor portfolio standard: notice to the operating partner within 24 hours of a severity 1 incident. Intercompany services agreement security schedule protecting Finance signed 2026-09-22 (EV-044, EV-070; P03 G-111) |
| SOC 2 timeline | Type 1 report as of 2027-06-30; Type 2 observation period 2027-07-01 to 2027-12-31; report expected by 2028-02-29 (the bank requires it by 2028-03-31). The SOC 1 Type 2 requested by the bank is planned separately |
| AI details | AI-001: 180 licensed users since 2026-05-04 (EV-056). AI-002: in use since 2025-10; about 38% of applications decided automatically; automatic approval only under $5,000 (EV-056); 17 of 40 sampled automated declines gave only a generic score reason; auto-decline rate for applicants 62 or older is 1.4 times that of younger applicants (EV-074). AI-003: in use since 2026-01; about 6,500 applicants in 2026; women passed the technician threshold at 0.76 of men's rate (EV-056, EV-075). AI-005: in use since 2026-03; about 70 calls a night in summer; 18 of 20 scripted emergency calls transferred correctly (EV-056, EV-076). AI-007: 14 users of public chatbots found in 30 days of web proxy logs (EV-057) |
| P07 findings logged as risks | The ACH signing service account password was written in an IT runbook readable by 14 IT staff and unchanged since 2021 (R-050). Branch 2 uses 3 shared counter accounts (R-047) (EV-IA-5; EV-AC-2, EV-IA-2) |
| Sample and test results (P03 and P07) | Recorded as P03 fieldwork samples (EV-067, EV-068) and P07 test evidence (EV-AC-2, EV-PS-4, EV-CM-3, EV-CM-6, EV-MP-6, EV-IR-6, EV-AT-2, EV-IA-2(1), EV-SC-7, EV-CP-4, EV-SI-4, EV-SI-3), not stated here |
| Plans and dates | FY2027 security plan: $905,000 one-time and $420,000 a year. Group tabletops on 2026-11-18 (shared services compromise) and 2027-02-17 (payment fraud); first out-of-band channel test 2026-10-15. Fieldwork walkthroughs covered 6 of 9 sites: HQ, the distribution center, Branch 2, the Central shop, the North shop, and the plant (EV-061) |
| Additional role titles | Treasury analysts (2); GRC Analyst; Benefits Analyst; subsidiary office managers; dispatchers; recruiters; underwriters; infrastructure engineers |
