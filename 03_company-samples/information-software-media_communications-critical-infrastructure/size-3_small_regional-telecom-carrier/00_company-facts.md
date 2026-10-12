# Scenario facts: Cris Santos Company | Communications | Small

All 11 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a regulation, court decision, or Federal Register document, the citation is given. Legal status was checked against eCFR (current through 2026-09-23), the Federal Register, and Sixth Circuit opinions on 2026-09-26.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (privately held; the majority owner is the Chief Executive Officer) |
| Business | Regional broadband and wired telecommunications carrier (NAICS 517111). A rural incumbent local exchange carrier in north-central Florida that has rebuilt most of its territory with fiber. Services: fiber and DSL broadband internet access; wireline voice (legacy copper local exchange service with resold long distance); interconnected VoIP voice over fiber; dedicated Ethernet and transport for business and government customers. **No** video service, **no** wireless (CMRS) service, **no** submarine cable or cable landing station |
| Location | Florida. Headquarters and main central office (**CO-1**, which also houses the network operations center and the customer care center); a second central office (**CO-2**, about 20 miles away, with a backup NOC workspace); a warehouse and fleet yard; 42 remote fiber and DSL cabinets in the outside plant. Service area: parts of three rural and suburban counties |
| Workforce | 250 employees: 95 field technicians and construction crew, 22 network operations center (NOC) staff, 48 customer care agents and supervisors, 18 sales and marketing, 20 billing and finance, 14 network engineering and planning, 9 IT (including the IT Manager), 12 warehouse and fleet, 12 executive, HR, and regulatory |
| Customers | About 64,000 accounts (59,500 residential, 4,500 business). About 61,000 broadband subscribers. About 23,400 voice lines on about 20,900 accounts: 8,600 legacy copper lines and 14,800 interconnected VoIP lines. 40 enterprise and government accounts have a dedicated account representative and a contract that addresses CPNI protection. About 9% of residential accounts belong to seasonal residents who also have an address in another state |
| Revenue | $92.4 million annual receipts (fictional), about $253,000 per day. The SBA size standard for NAICS 517111 is 1,500 employees (13 CFR 121.201), so the company is SBA-small at 250 employees |
| Regulatory status | **Telecommunications carrier** for its local exchange and toll services (47 U.S.C. 153; the CPNI rules use this definition, 47 CFR 64.2003(o)). **Interconnected VoIP provider**, which the CPNI rules treat as a carrier (47 CFR 64.2003(o)). **Broadband internet access provider**: after *Ohio Telecom Ass'n v. FCC* (6th Cir. Jan. 2, 2025) set aside the FCC's 2024 reclassification order, broadband is an information service, and the FCC conformed its rules on 2025-08-08 (90 FR 38406). **Wireline and interconnected VoIP communications provider** for outage reporting (47 CFR 4.3(g), (h)). **Telecommunications carrier under CALEA** because it provides local exchange service as a common carrier for hire (47 U.S.C. 1001(8)(A)). Each status is determined in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (C-COMMUNICATIONS-R01 to R03), from the services billed (EV-052) |
| Customer commitments | Online privacy policy and CPNI notice; residential terms of service; business contracts for dedicated Ethernet with a 99.95% monthly availability SLA; enterprise contracts that set CPNI authentication terms (47 CFR 64.2010(g)) |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): SEC cybersecurity disclosure rules (privately held; C-COMMUNICATIONS-R06). FCC submarine cable landing license rules (no cable or SLTE; C-COMMUNICATIONS-R04). CMRS-only rules, including SIM change authentication (47 CFR 64.2010(h)). Emergency Alert System rules, including the July 2026 EAS cybersecurity order (91 FR 48289), because the company provides no video or broadcast service. FAR 52.204-25 reporting (no federal contracts). Payment card data: cards are taken through the payment processor's hosted pages and tokenized IVR; PCI DSS duties are contractual and outside this sample |
| State law approach | Florida law is cited only where a Florida duty is unavoidable: breach notification (Fla. Stat. 501.171) and all-party consent for recorded calls (Fla. Stat. 934.03(2)(d)). Seasonal residents are handled generically: "the law of each state where affected individuals reside" |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Chief Executive Officer (majority owner) | Accepts High and Very High risks; approves the security budget |
| Chief Operating Officer (COO) | Executive owner of the security program; **CPNI compliance officer**, signs the annual CPNI certification (47 CFR 64.2009(e)); accepts Moderate risks; approves policies and these deliverables |
| Chief Financial Officer (CFO) | Billing and vendor contracts; cyber insurance |
| Vice President of Network Operations | System owner of the OSS; **CALEA senior officer** (47 CFR 1.20003(a)) since the previous designee left in 2025 (the change has not been filed; EV-037); authorizes NORS filings |
| Director of Customer Operations | Customer care, the overflow call center vendor, and the AI chatbot (business owner) |
| IT Manager | **Security and compliance lead** (part-time security duties). Runs the identity provider, endpoints, cloud tenant, and the policy set; accepts Low risks |
| NOC Manager | 24x7 NOC; outage escalation; NORS and DIRS submissions; 911 special facility notifications |
| Network Engineering Manager | Routers, optical line terminals (OLTs), DSLAMs, session border controllers (SBCs); network device patching |
| Regulatory Affairs Manager | FCC filings (CPNI certification package, CALEA filings, NORS final reports); tracks rule changes; **privacy lead** for breach determinations with counsel |
| Billing Manager | Billing and customer care system (BSS) configuration; billing vendor relationship |
| Marketing Manager | Marketing campaigns that use CPNI; CPNI opt-out notices |
| HR Manager | Onboarding, terminations, training records, disciplinary process |
| Outside telecommunications regulatory counsel (retainer) | CPNI, CALEA, outage, and breach advice |
| Independent assessor (contracted) | Performed the P07 control assessment; not involved in operating the controls |

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv).

| ID | System | Hosting | Holds CPNI or subscriber PII? | Notes |
|---|---|---|---|---|
| SYS-01 | Billing and customer care system (BSS): accounts, CPNI approval flags, account passwords, bills with toll call detail, agent desktop | Vendor SaaS | Yes (CPNI and PII) | System of record for customers. The vendor has a SOC 2 Type 2 report (P09) |
| SYS-02 | OSS: network inventory, provisioning and activation, trouble ticketing, field dispatch | Cloud tenant (SYS-13) | Yes (service configuration, addresses) | Company-managed application |
| SYS-03 | Voice mediation and rating: collects call detail records (CDRs) from SYS-07, rates toll calls, feeds SYS-01; CDR archive (36 months) | Cloud tenant (SYS-13) | Yes (call detail for every voice line) | Service account pulls CDRs from CO-1 over the site-to-site VPN |
| SYS-04 | Customer portal and mobile app: online account access, bills and call detail, password management | Cloud tenant (SYS-13), PaaS web app behind an API gateway | Yes | Password reset uses date of birth and last 4 of SSN (EV-023) |
| SYS-05 | Identity provider (single sign-on and MFA for the workforce) | SaaS | No (identities only) | Also backs the TACACS+ server for core routers |
| SYS-06 | Productivity suite (email, files, chat) | SaaS | Incidental | |
| SYS-07 | Voice core: IP softswitch, two SBCs (CO-1, CO-2), legacy TDM switch (retirement 2027), SS7 through a third-party SS7 hub, 911 trunks to the regional NG911 system service provider | On-premises (CO-1, CO-2) | Yes (CDRs generated here) | The CO-1 SBC runs a release past vendor support (EV-013) |
| SYS-08 | IP/MPLS core and access network: core routers, broadband network gateways, 2 internet edge routers, OLTs, DSLAMs, 42 cabinet aggregation switches, DNS and DHCP | On-premises and outside plant | Yes (subscriber IP assignments) | |
| SYS-09 | Network management plane: NOC availability monitoring, element management systems, TACACS+ server, syslog server (30-day retention), configuration backup server, jump hosts | On-premises (CO-1) | Indirect | Reachable from the corporate network (EV-011) |
| SYS-10 | Lawful-intercept (CALEA) mediation: softswitch intercept function and a mediation appliance linked to a CALEA trusted third party (TTP) | On-premises (CO-1), restricted room | Yes (intercept content and court orders) | 3 named employees have access (EV-038). Outside the SSP boundary; covered by the CALEA SSI plan |
| SYS-11 | Contact center platform: ACD, IVR (tokenized card payments), call recording | Vendor SaaS | Yes | Used by in-house agents and an after-hours overflow call center vendor (U.S.-based) |
| SYS-12 | Customer-service AI chatbot with account access (web and app chat); reads and updates account data through an API to SYS-01 | Vendor SaaS (large language model platform) | Yes | Pilot since 2026-04-06 (see P10) |
| SYS-13 | Cloud tenant (IaaS/PaaS): hosts SYS-02, SYS-03, SYS-04, the API gateway, a reporting data warehouse, and the backup vault | Public cloud provider (vendor-agnostic) | Yes | Site-to-site VPN to CO-1 and CO-2 |
| SYS-14 | Endpoints: 285 Windows laptops and desktops, 105 field technician tablets | Company-managed | Cached | EDR on laptops and desktops; tablets under mobile device management only (EV-009, EV-010) |

**SSP system (P02):** the *Network Operations and Customer Billing Platform (OSS/BSS)*: SYS-01, SYS-02, SYS-03, SYS-04, SYS-05, SYS-09, and SYS-13, with their interfaces to SYS-07 and SYS-08 (element management and CDR feeds), SYS-11, and SYS-12.

## 4. Where the evidence is

This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Every item has a source system, an owner, and as-of and collected dates.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps against the CPNI, CALEA and outage rules** are judged in the gap analysis (P03), and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 regulation | FCC CPNI rules, 47 CFR 64.2001-64.2011, as in force on 2026-09-23 (the 2023 amendments to 64.2011 are not yet effective). Secondary: CALEA system security and integrity rules (47 CFR 1.20003-1.20005) and FCC outage reporting (47 CFR Part 4). Voluntary network security benchmark: NIST CSF 2.0 and the CISA Cross-Sector Cybersecurity Performance Goals |
| P08 incident | Network intrusion exposing CPNI: exploitation of the unsupported CO-1 SBC, movement through the management plane, and theft of call detail records from the mediation system |
| P09 SOC 2 | The company is not a SOC 2 service organization (it provides transmission, not processing that its customers rely on for their own controls). P09 is (a) a Security-only (CC1-CC9) self-benchmark and (b) a review of the BSS vendor's SOC 2 Type 2 report |
| P10 AI | Customer-service chatbot with account access (pilot since 2026-04-06) |
| Cloud | Vendor-agnostic. Services are described by category, with AWS, Azure, and Google Cloud equivalents noted only in P04 |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-07-06 to 2026-07-17 | Intake: evidence requests, exports, inventories, obligations register |
| 2026-07-20 to 2026-07-31 | BIA interviews (2026-07-20 to 2026-07-21), risk assessment and gap analysis fieldwork (walkthrough of CO-1, CO-2, and 3 remote cabinets on 2026-07-28) |
| 2026-08-03 to 2026-08-07 | Policies drafted from the gaps; control assessment plan approved by the COO on 2026-08-05 |
| 2026-08-10 to 2026-08-14 | Control assessment fieldwork: operating tests of controls already in place; design review of the draft policies and runbook |
| 2026-08-24 | AI risk assessment and SOC 2 self-benchmark completed |
| 2026-09-04 | Deliverables and policies approved by the COO; High risk treatment plans approved by the Chief Executive Officer |
| 2027-03 (planned) | Follow-up assessment: operating effectiveness of the controls the new policies introduced, after at least one quarter of operation |
