# Scenario facts: Cris Santos Company | Management of Companies and Enterprises | Enterprise

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, the citation is given and was checked against the eCFR (version of 2026-09-23) or the Federal Register text of SEC Release 33-11216.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (publicly traded SEC registrant; large accelerated filer) |
| Business | Diversified holding company (NAICS 551112, Offices of Other Holding Companies). It owns 100% of four operating subsidiaries and runs **Global Business Services (GBS)**, the shared services organization that provides finance and accounting, treasury, HR and payroll, procurement, legal support, and IT and security to every subsidiary |
| Subsidiaries | **CSC Building Products, Inc.** ("Building Products"): wholesale distribution of building materials to contractors (NAICS 423310), 72 branches and 4 distribution centers. **CSC Home Services, Inc.** ("Home Services"): residential heating, air conditioning, and plumbing service and replacement (NAICS 238220), 48 branches, about 2,300 field technicians. **CSC Climate Manufacturing, Inc.** ("Manufacturing"): manufactures residential and light-commercial HVAC equipment (NAICS 333415) at 3 plants, and runs a connected equipment monitoring service for commercial customers. **CSC Consumer Finance, LLC** ("Finance"): state-licensed, non-depository consumer lender (NAICS 522291) making point-of-sale installment loans for HVAC and home improvement through about 1,400 independent dealers and through Home Services |
| Location | Headquartered in Florida. Operations in six states: Florida, Georgia, Alabama, South Carolina, North Carolina, and Tennessee. Finance is licensed as a consumer lender in all six. **State law is handled generically:** each state where affected individuals reside, with Florida as the worked example |
| Workforce | 12,000 employees: Building Products 3,500; Home Services 4,000; Manufacturing 2,350; Finance 380; corporate and GBS 1,770. About 2,500 contractors also hold accounts |
| Receipts | About $4.8 billion a year, consolidated (fictional): Building Products $2.10 billion, Home Services $1.05 billion, Manufacturing $1.40 billion, Finance $0.25 billion (interest and fees). That is about $13.2 million per calendar day. SBA counts the receipts of the concern and its affiliates (13 CFR 121.103(a)(6)); the group is far above the $45.5 million standard for NAICS 551112, so it is not small |
| Finance portfolio | About 210,000 active loans ($1.6 billion of receivables). Customer information on about 520,000 consumers (active and paid-off borrowers within the retention period, and declined applicants) |
| Securities status | Common stock listed on a national securities exchange. Large accelerated filer: files Forms 10-K, 10-Q, and 8-K. **Reg S-K Item 106 (17 CFR 229.106) and Form 8-K Item 1.05 apply.** SOX section 404(a) management assessment and 404(b) auditor attestation apply (15 U.S.C. 7262). Item 106 disclosure has appeared in Item 1C of the 10-K since fiscal year 2023 |
| Banking status | **Not a bank holding company or savings and loan holding company.** No subsidiary is a bank or savings association; Finance takes no deposits and is funded by bank credit facilities and term securitizations. Federal Reserve Regulation Y Subpart N (12 CFR 225.300-225.303) and 12 CFR Part 225 Appendix F do not apply |
| Safeguards Rule status | **Finance is a financial institution** under the FTC Safeguards Rule (16 CFR 314.1(b); 314.2(h)) and holds customer information on more than 5,000 consumers, so the 314.6 exception does not apply. Finance employs its own **Qualified Individual** (the Finance Information Security Officer). **The holding company is Finance's affiliate and service provider:** GBS runs Finance's identity, email, files, payroll, ACH and bank connectivity, and security operations (314.2(r); 314.4(f)) |
| Group health plan | **Self-insured** group medical plan for all employers in the group: about 9,600 enrolled employees and about 21,000 covered lives. A third-party administrator (TPA) pays claims as a business associate of the plan. The plan is a HIPAA covered entity. The holding company is plan sponsor; a benefits team of 8 in GBS HR receives PHI for plan administration (appeals and stop-loss) under plan documents amended under 45 CFR 164.504(f) and 164.314(b) |
| Payment cards | Building Products and Home Services accept cards. PCI DSS duties are contractual and are assessed each year by a separate PCI program; they are noted, not assessed, in these deliverables |
| Federal contracts | None. No subsidiary holds federal prime contracts or subcontracts, so the FAR reporting clauses do not apply |
| Added at this size | SEC cybersecurity disclosure (Item 106; Form 8-K Item 1.05); SOX IT general controls with auditor attestation; a disclosure committee; plant operational technology (OT); a self-insured health plan; growth by acquisition (AQ-01 acquired 2025-10, AQ-02 acquired 2026-03) |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Board of directors: audit committee and risk committee | The **risk committee** oversees cybersecurity risk (Item 106(c)(1)) and receives the CISO's report each quarter. The **audit committee** oversees Internal Audit, SOX, and disclosure controls |
| Chief Executive Officer (CEO) and Chief Financial Officer (CFO) | Accept Very High risks jointly; certify disclosure controls and ICFR; take part in materiality determinations |
| Chief Information Officer (CIO) | Runs GBS IT; owns the shared corporate services platform infrastructure |
| Chief Information Security Officer (CISO) | Group security program owner; reports to the CIO with direct quarterly reporting to the board risk committee |
| Chief Risk Officer | Enterprise risk management (ERM); owns the enterprise risk register and chairs the executive risk committee |
| Chief Audit Executive | Heads Internal Audit (third line); reports functionally to the audit committee |
| General Counsel | Chairs the disclosure committee |
| Subsidiary Presidents (4) | Own their subsidiary's business risk; each has a **business information security officer (BISO)** who reports to the CISO |
| Finance Information Security Officer | Finance's **Qualified Individual** (16 CFR 314.4(a)), employed by Finance; reports to the Finance President, with a dotted line to the CISO |
| GRC team (11), Security Operations Center (24x7, in-house with a managed security service provider for overflow), Internal Audit (in-house IT audit team of 6, co-sourced with an outside firm) | Three lines model |
| Disclosure committee | Materiality determinations for Form 8-K Item 1.05; chaired by the General Counsel |

## 3. Systems

| ID | System | Notes |
|---|---|---|
| SYS-01 | Group ERP (general ledger, payables, receivables, fixed assets, intercompany) | Commercial ERP software, customer-managed on Cloud provider A. All entities except AQ-01 and AQ-02. SOX in scope |
| SYS-02 | Financial close and consolidation application | Vendor SaaS. Consolidation, SEC reporting packages, disclosure checklists. SOX in scope |
| SYS-03 | Treasury management system and payment hub | Treasury management is vendor SaaS; the payment hub runs on Cloud provider A and sends wires and ACH files to 6 banks over host-to-host connections. About $1.1 billion a week of outgoing payments |
| SYS-04 | Group identity platform | One on-premises directory synchronized to a cloud identity provider (SSO, MFA), privileged access management (PAM), and identity governance. About 14,500 workforce identities and 3,100 service accounts |
| SYS-05 | HRIS and payroll | Vendor SaaS. 12,000 employees in 6 employer entities; benefits enrollment for the group health plan |
| SYS-06 | Productivity suite (email, files, chat, device management) | One tenant for all entities; includes the enterprise generative AI assistant (SYS-13) |
| SYS-07 | Multi-cloud estate and data centers | Cloud provider A (ERP, payment hub, integration platform, data warehouse) and Cloud provider B (Finance loan platform, the dealer financing portal, the connected equipment platform); DC-1 (company-owned, Florida) and DC-2 (colocation, Georgia) host the directory, legacy virtualization, and backup copies |
| SYS-08 | Enterprise network | SD-WAN across about 140 sites |
| SYS-09 | Endpoints and servers | About 15,800 endpoints (9,400 laptops and desktops, 6,400 mobile devices and technician tablets) and about 1,900 servers |
| SYS-10 | Subsidiary line-of-business systems | Building Products distribution and e-commerce; Home Services field-service management; Finance loan origination and servicing; Manufacturing execution system (MES) |
| SYS-11 | Plant operational technology (OT) | 3 plants, about 1,450 OT assets (controllers, operator panels, robots, engineering workstations) |
| SYS-12 | Board portal and M&A data rooms | Vendor SaaS; material non-public information (MNPI) |
| SYS-13 | Enterprise generative AI assistant and AI portfolio | 14 AI use cases governed by the AI governance committee |
| SYS-14 | Third parties | About 2,300 vendors; 420 with access to sensitive data or systems. An outsourced service desk provider runs the 24x7 tier-1 help desk for GBS |
| SYS-15 | Acquired businesses' legacy systems | AQ-01 and AQ-02 still run their own directories and ERPs |

**SSP system (P02):** the *Shared Corporate Services Platform (SCSP)*: the group ERP (SYS-01), financial close and consolidation (SYS-02), treasury management and payment hub (SYS-03), and the group identity platform (SYS-04), with the integration platform that connects them to subsidiary systems and banks. Moderate baseline, with integrity supplemented because the SCSP produces the consolidated financial statements and releases payments.

## 4. Current security posture: mature, with targeted gaps

**In place today:**
- A group security program aligned to CSF 2.0, with a CISO, a GRC team, business information security officers in each subsidiary, and a three lines model
- Annual enterprise risk assessment rolled into ERM (NIST IR 8286)
- A policy hierarchy of policies, standards, procedures, and exceptions
- 24x7 security operations center (SOC)
- SSO with MFA for all workforce users; PAM for administrators
- Quarterly access certification for SOX applications
- SOX IT general controls tested every year by Internal Audit and the external auditor; no material weakness reported
- Immutable backups and annual disaster recovery (DR) tests for tier-1 systems
- A tiered third-party risk program
- Bank-enforced dual approval and positive pay; payment hub release controls
- Finance's written information security program, risk assessment, and the Qualified Individual's annual report to Finance's board
- Annual SOC 2 Type 2 report for the dealer financing platform since 2024
- Item 106 disclosure in the 10-K and a standing disclosure committee

**Targeted gaps:**
1. **Acquisition integration.** AQ-01 and AQ-02 still run their own directories and ERPs. Their results reach consolidation by manual upload, their logs do not reach the SIEM, and their terminations are processed by hand.
2. **Identity recovery.** The outsourced service desk resets passwords and MFA after knowledge-based verification only. Phishing-resistant MFA covers 62% of privileged accounts. 410 of 3,100 service accounts have non-expiring passwords, and directory administrative tiering is incomplete.
3. **Payment integrity at the edges.** Home Services branches still run local payables for small vendors, with vendor bank-detail changes verified inconsistently. Three local bank portals outside the payment hub carry about 6% of payment value.
4. **Plant OT.** The OT asset inventory is 72% complete. Plant 3 has a flat network. 140 operator panels and engineering workstations run unsupported operating systems, and two plants allow vendor remote access through unmanaged tools.
5. **Third parties.** 18 of 64 tier-1 vendor reassessments are overdue. The outsourced service desk contract sets no identity-verification standard.
6. **Independent assurance outside SOX.** Internal Audit tests SOX IT general controls every year, but had not independently assessed the identity platform's non-SOX controls (help desk, service accounts, directory tiering) since 2023.
7. **AI.** 14 AI use cases, only 8 reviewed by the AI governance committee. The generative AI assistant expanded to about 4,000 users across all subsidiaries in 2026-06, before the data-labeling work finished. The credit underwriting model has not had local fairness testing since its 2025 retraining.
8. **Materiality.** The materiality playbook assumes incidents start at the holding company. It does not cover incidents that start in a subsidiary or at a shared-services vendor, or how related incidents across subsidiaries are aggregated. It has not been exercised with the disclosure committee since 2025-03.

## 5. Scenario choices

| Deliverable | Choice |
|---|---|
| P03 | All applicable regulations: SEC Item 106 and Form 8-K Item 1.05; Exchange Act Rule 13a-15 and SOX 404; the FTC Safeguards Rule (Finance, reaching the holding company as service provider); HIPAA plan sponsor duties for the self-insured health plan; state breach and data security laws (Florida worked example); and a **NIST CSF 2.0 group profile** (Govern function, the vertical's voluntary benchmark) with subsidiary profiles. Applicability rows for Regulation Y Subpart N, Appendix F, and CIRCIA |
| P08 | Compromise of shared services affecting subsidiaries: help desk social engineering of the outsourced service desk leads to takeover of a GBS identity administrator account, a fraudulent payment attempt through the payment hub, theft of payroll and Finance customer data, and ransomware staged on shared virtualization. Includes the **SEC materiality step** and a multi-state notification workflow |
| P09 | SOC 2 Type 2 readiness across two service lines offered to outside customers: SL-1 dealer financing platform (Finance) and SL-2 connected equipment monitoring (Manufacturing) |
| P10 | Enterprise AI portfolio (14 use cases) with the AI governance committee operating model; full assessment of AI-001, the enterprise generative AI assistant across subsidiaries |
| Cloud | Multi-cloud (vendor-agnostic) with common controls, two data centers, plant OT, and SaaS |

**Registry defaults kept.** The primary system (shared corporate services platform, ERP and identity), the P08 incident (compromise of shared services affecting subsidiaries), and the P10 use case (enterprise generative AI assistant across subsidiaries) fit a public holding company at this size, so they were kept. The SSP adds treasury and consolidation to the ERP and identity scope because those are where shared-services failures become financial reporting and payment failures.

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-05-04 to 2026-07-17 | BIA, enterprise risk assessment, and regulatory gap analysis (evidence sampling completed 2026-07-31) |
| 2026-07-13 to 2026-08-28 | Control assessment of the SCSP (Internal Audit with its co-source firm) |
| 2026-09-17 | Results to a joint session of the audit committee and the risk committee of the board |

## 7. Facts added while building the deliverables
These facts were added while building the deliverables. They do not change sections 1-6.

**Sites and volumes.** Building Products: 72 branches and 4 distribution centers, about $8.2 million of sales per business day, about 18,000 contractor accounts online. Home Services: 48 branches, about 9,500 service calls a day. Manufacturing: Plant 1 (Florida), Plant 2 (Georgia), Plant 3 (Tennessee), about $5.5 million of shipments per business day, about 900 EDI trading partners. Finance: about 1,900 applications a day (about $4.3 million of loans a day). Contact centers: about 41,000 calls a day, about 700 agents. GBS accounts payable: about 38,000 invoices a week. Payroll: weekly for about 8,900 hourly employees, biweekly for salaried staff. About 140 sites on SD-WAN. DC-1 is on the Florida headquarters campus; DC-2 is a colocation site in Georgia. About 420 virtual machines from every subsidiary run on the shared virtualization layer.

**Acquired businesses.** AQ-01: regional HVAC service company acquired 2025-10, about 640 workforce members, 7 branches in North Carolina and Tennessee, part of Home Services; its payroll stays on its own provider until 2027-01; ERP migration planned 2027-06. AQ-02: building materials distributor acquired 2026-03, about 520 workforce members, 9 branches in Alabama and Georgia, part of Building Products; hosted ERP with a 48-hour contract RTO; ERP migration planned 2027-04. Both are included in the 12,000 employees. Both keep nightly backups only, and their results reach consolidation by manual upload.

**Additional roles (titles only).**
| Role | Duties in the deliverables |
|---|---|
| Chief Accounting Officer | SOX program and consolidation owner; disclosure committee member |
| Treasurer | Treasury management and payment hub owner; payment fraud lead |
| Vice President, Global Business Services | SCSP system owner; GBS accounts payable |
| Chief Compliance Officer | Regulatory compliance program; second line with the GRC team |
| Chief Privacy Officer | Data classification; breach assessments; privacy official support for the group health plan |
| Chief Human Resources Officer | HRIS, terminations, training records, benefits and plan administration |
| Chief Data and Analytics Officer | Chairs the AI governance committee; owns the data warehouse |
| Finance Chief Credit Officer | Credit policy and the credit, collections, and fraud models |
| Vice President, Integration Management Office | Integration of AQ-01 and AQ-02 |
| Vice President, Corporate Development | Acquisition diligence and data rooms |
| Vice President, Customer Operations | Contact centers and the Home Services chat assistant |
| Vice President, Investor Relations | Investor communications (Regulation FD); disclosure committee member |
| Vice President, Corporate Communications | Media and employee communications during incidents |
| Vice President, Facilities | DC-1 physical security and the colocation relationship |
| Director of ERP Platform | ERP, consolidation, and integration platform administration |
| Director of Enterprise Integration | Integration platform and bank connectivity |
| Director of Identity and Access Management | Group identity platform, PAM, identity governance, account recovery |
| Director of Security Operations | SOC, SIEM, vulnerability management, incident command |
| Director of Cloud Platform Engineering | Landing zones in both clouds; backups |
| Director of Network Engineering | SD-WAN, data center and hub firewalls |
| Director of Endpoint Engineering | Endpoint and server baselines, EDR agents, mobile devices |
| Director of OT Security | Plant OT security (reports to the CISO, works with the President, Manufacturing) |
| Director of Third-Party Risk Management | Vendor tiering, contracts, SOC report reviews |
| Finance platform engineering lead; Connected services engineering lead | Engineering owners of SL-1 and SL-2 |

**Committees.** Executive risk committee: Chief Risk Officer (chair), CFO, CIO, CISO, General Counsel; meets monthly. Disclosure committee: General Counsel (chair), CFO, Chief Accounting Officer, CISO, Chief Risk Officer, Vice President, Investor Relations; outside securities counsel advises. AI governance committee: formed 2025, chaired by the Chief Data and Analytics Officer; the intake gate for new AI features went live 2026-06-01. Policy governance committee: chaired by the CISO.

**Shared Corporate Services Platform details.** About 2,900 named ERP, consolidation, and treasury users; about 1,180 privileged accounts, of which 448 (38%) were still on push MFA in 2026-08; 23 domain administrator accounts against a tiering design of 6; 410 service accounts with non-expiring passwords, 96 with no named owner; 8 domain controllers (4 at DC-1, 4 at DC-2); 6 ERP application servers, 2 payment hub servers, 4 middleware servers. Six banks; the primary bank carries 64% of payment value; 3 local bank portals outside the hub (Home Services and AQ-02) carry about 6% of payment value. The outsourced service desk performs about 61% of password and MFA resets (21,880 resets in 2026 H1). The 2026-04-25 tier-1 DR test recovered the ERP in 9.5 hours against an 8-hour RTO. 212 security incidents were logged from 2025-07 to 2026-06.

**Finance.** The Qualified Individual was designated in writing in 2024-01; WISP v4 dated 2026-02; the Qualified Individual's annual report was delivered to Finance's board on 2026-03-12. 27 service providers hold Finance customer information. About 9,800 dealer portal user accounts (1,120 inactive more than 90 days at assessment). About 310,000 declined applications from 2022-2023 exist in the data warehouse population sampled in P03.

**Group health plan.** Plan documents were amended in 2019 for 164.504(f) but not for the 164.314(b) security provisions; they name the 8-person benefits team and 2 HRIS administrators. Plan files sat on a shared HR site open to 140 HR staff until the restricted site goes live (POAM-023).

**Service lines (P09).** SL-1 dealer financing platform: SOC 2 Type 2 every year since 2024 (Security, Availability, Confidentiality, Processing Integrity); Privacy added for the 2027 period; 99.9% monthly availability commitment; dealer agreements require incident notice within 72 hours of confirming dealer data is affected. SL-2 connected equipment monitoring: about 650 commercial customers and about 38,000 units; 99.5% monthly availability commitment; 72-hour notice in customer agreements; Type 1 as of 2027-06-30, then a first Type 2 for 2027-07-01 to 2027-12-31. Units shipped before 2024 share device certificates per model.

**AI (P10).** 14 use cases (AI-001 to AI-014): High 3, Medium 8, Low 3; 8 reviewed. The AI assistant (AI-001) has about 4,000 users (GBS 1,500, Building Products 900, Home Services 700, Manufacturing 600, Finance 300). The tenant has about 9,800 collaboration sites; 212 were shared with all employees and 1,240 sites holding Restricted data had no sensitivity label (labels covered 62% of such sites). Expansion was paused for Finance, HR, benefits, and deal sites on 2026-08-14. The credit model (AI-002) was retrained in 2025-11. The resume ranking feature (AI-005) was disabled on 2026-07-20. Recording consent: all-party prior consent for any transcribed meeting in all six states (Florida worked example, Fla. Stat. 934.03(2)(d)).

**Other dates and figures.** OT security review of the plants: 2026-06 (source of the 72% OT inventory figure). Group tabletop with a payment fraud scenario: 2026-03-19. Full tabletop of the P08 runbook with the disclosure committee: scheduled 2026-11-19. Approval dates: BIA 2026-07-24; P03 2026-08-21; P01, P06 (except POL-01), and P10 decisions by the executive risk committee 2026-09-14; SSP 2026-09-18 (CFO); POL-01 by the board risk committee 2026-09-17. Awareness training completion 97%; phishing simulation click rate 2.9% (2026 H1). Treatment funding 2026 Q4 to 2027 Q2: about $7.4 million. The intercompany services agreement requires GBS to tell an affected subsidiary of a breach within 10 days (POL-03 requires the same day).
