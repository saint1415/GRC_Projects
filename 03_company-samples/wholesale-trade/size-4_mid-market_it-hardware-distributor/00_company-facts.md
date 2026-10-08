# Scenario facts: Cris Santos Company | Wholesale Trade | Mid-Market

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or contract clause, the citation is given. Regulatory text was read from eCFR (current as of 2026-09-23).

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (privately held; private equity-backed since 2023; board with an audit committee) |
| Business | IT hardware and software wholesale distributor (NAICS 423430): networking and wireless, video surveillance and collaboration, servers and storage, end-user computing, peripherals, and software licenses and subscriptions. Value-added services: configuration and integration (staging, imaging, asset tagging, kitting) for commercial resellers, and a Federal Integration Lab for DoD programs |
| Locations | Florida: headquarters (offices, IT, customer service); **Distribution Center 1 (DC-1)**, 380,000 sq ft with automated conveyor, sortation, and vertical lift storage, the commercial **Integration Center**, and the caged **Federal Integration Lab (FIL)**; **Distribution Center 2 (DC-2)**, 150,000 sq ft for overflow stock, returns and RMA processing, and cross-dock. 74 field sales employees work remotely in 11 other states (Alabama, Georgia, South Carolina, North Carolina, Tennessee, Virginia, Maryland, Pennsylvania, Ohio, Texas, Louisiana) |
| Workforce | 850 employees: 70 management and administration, 180 sales and account management (including the 74 field sales staff), 45 purchasing and supplier management, 330 warehouse and logistics, 95 integration technicians (22 of them in the FIL), 60 customer service and technical support, 35 finance, 28 IT and security, 7 HR |
| Revenue | About $820 million a year (fictional), about $3.28 million per shipping day over 250 shipping days. Gross margin about 10.5% (about $344,000 gross profit per shipping day). The SBA size standard for NAICS 423430 is 250 employees (13 CFR 121.201), so the company is not SBA-small |
| Customers | About 4,200 active reseller and solution-provider accounts in 15 eastern and central states (about 82% of revenue). The federal channel (about 18% of revenue, $148 million) is 3 DoD prime contractors (Prime A, Prime B, Prime C) and 4 federal systems integrators that buy under subcontract purchase orders |
| Suppliers | 251 active product suppliers: 214 authorized sources (OEM programs and OEM-authorized distributors), 31 independent brokers (about 1.8% of purchase spend), and 6 overseas contract manufacturers that make private-label accessories (cables, racks, mounts; about 2.9% of purchase spend), which the company imports as importer of record through a licensed customs broker |
| Federal Contract Information (FCI) order stream | Orders from the 7 federal channel customers that include kitting, imaging, or asset labeling (about $90 million a year). Their purchase orders contain FAR 52.204-21, FAR 52.204-25, FAR 52.204-30, and, since 2026-01, DFARS 252.204-7021 at CMMC Level 1 (Self). Orders exclusively for commercially available off-the-shelf (COTS) items carry neither FAR 52.204-21 (its paragraph (c)) nor a CMMC requirement (32 CFR 170.3(c)) |
| Controlled Unclassified Information (CUI) order stream | The FIL configures and stages equipment for DoD installations using CUI-marked configuration documents (network drawings, IP addressing plans, device configuration templates, hardened image baselines, site installation drawings) under 3 subcontracts: **Prime A** (network modernization, since 2023), **Prime B** (video surveillance and physical security systems, since 2024), and **Prime C** (server and storage refresh, since 2026-03). About $58 million a year. The subcontracts contain DFARS 252.204-7012, 252.204-7019/-7020, 252.246-7008, FAR 52.204-21, 52.204-25, and 52.204-30. Prime A also flows down DFARS 252.246-7007, which applies to the company through its paragraph (e) even though the company is not subject to the Cost Accounting Standards |
| CMMC Level 2 requirement | Prime A (option period starting **2027-06-01**) and Prime B (task orders issued after **2027-06-01**) have notified the company that it must hold a CMMC Status of **Level 2 (C3PAO)**, flowed down under 32 CFR 170.23(a)(3). Prime C will add the same requirement at its 2027 modification. CMMC Phase 2 (planned for 2026-11-10, 32 CFR 170.3(e)(2)) is suspended by the DoD (Department of War) CIO memorandum of 2026-07-13, so the primes' Level 2 (C3PAO) requirement is suspended under DoD Class Deviation 2026-O0025, Revision 3 (DFARS 240.371-5). Until 2028-11-09 DoD includes clause 252.204-7021 only when a program office requires a specific CMMC level. The company keeps preparing because it still owes SP 800-171 Rev. 2 under DFARS 252.204-7012, and keeps the C3PAO assessment as a customer-driven choice |
| SPRS status | NIST SP 800-171 DoD Basic Assessment posted 2026-01-30 with a score of 81, supported by a documented self-assessment (2025-12) against the enclave SSP version 1.0. CMMC Level 1 (Self) result and affirmation entered 2026-01-30 for the FCI scope, supported by a documented self-assessment |
| Not in scope | SEC disclosure rules (the company is privately held). CCPA/CPRA: the company has no California customers, ship-to addresses, employees, or operations; counsel confirmed in 2026-06 that it does not do business in California. The sponsor's 2027 West Coast expansion plan would change this and is tracked as a pending item. CTPAT: voluntary; the company is an importer of record for private-label accessories and is evaluating membership in 2027, not assessed here. Payment cards: reseller card payments use the portal vendor's hosted payment page; PCI DSS validation is handled with the acquirer and is not assessed here. Exports: the company sells only to U.S. customers for U.S. delivery |
| State law approach | Personal information of employees in 12 states and of reseller contacts in 15 states is protected under each state's breach notification law. Florida law (Fla. Stat. 501.171) is used as the worked example. Otherwise the samples stay federal |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Board audit committee | Quarterly cyber risk and CMMC readiness reporting |
| Chief Executive Officer | Accepts High risk; approves the risk appetite and the security budget |
| Chief Operating Officer | Executive sponsor of the security program; system owner of the SSP system (P02); accepts Moderate risk; **CMMC Affirming Official** (32 CFR 170.22) |
| Chief Financial Officer | Payment controls, cyber insurance, data warehouse owner |
| General Counsel | Legal workstream in incidents, privilege, notifications, contract terms and flowdowns |
| Virtual CISO (vCISO, part-time contractor) | Program strategy, risk method, board reporting |
| Director of Information Technology | Runs IT (22 staff); owns contingency planning; maintains the SSP day to day |
| Security Manager plus 2 security analysts (one security operations, one GRC) | Security operations, MSSP oversight, vulnerability management, GRC, POA&M |
| Director of Federal Programs | Flowdown clauses, SPRS entries, Section 889 and FASCSA screening and reports, DIBNet reports, prime communications. Holds the only DoD-approved medium assurance certificate |
| Federal Integration Lab Manager | Day-to-day custodian of CUI; approves enclave and FIL access |
| Vice President of Supply Chain | Supply chain risk lead; approved supplier list; broker approvals; sourcing order; C-SCRM plan owner |
| Director of Quality and Product Compliance | Counterfeit detection and avoidance system (DFARS 252.246-7007), receiving inspection standard, GIDEP screening, quarantine decisions |
| Director of Distribution Operations | DC-1 and DC-2 operations; owner of the DC automation systems |
| Vice President of Sales Operations | Business owner of the reseller portal, EDI, and API ordering (the Partner Commerce Platform in P09) |
| Director of Inventory Planning | Business owner of demand forecasting and automated reordering (AI-001) |
| Controller | Accounts payable, supplier master data, and bank-detail changes |
| HR Director | Screening, onboarding and terminations, training records, the applicant tracking system |
| Director of Marketing and Communications | External statements in incidents |
| Co-sourced internal audit firm | Annual IT audit; performs the P07 assessment; reports to the audit committee |
| Managed security service provider (MSSP) | 24x7 endpoint detection and response (EDR) and SIEM monitoring, including enclave logs. It handles Security Protection Data, so it is an External Service Provider (32 CFR 170.19(c)(2)) |
| DC automation integrator | Maintains the DC-1 conveyor, sortation, and vertical lift controls under a service contract, with remote access |

## 3. Systems

| ID | System | Hosting | FCI / CUI | Notes |
|---|---|---|---|---|
| SYS-01 | ERP: order-to-cash, procure-to-pay, inventory, finance | Vendor SaaS | FCI; **CUI found** (37 sales orders with CUI attachments) | 610 named users; vendor SOC 2 Type 2; no FedRAMP authorization or documented equivalency; contract states 99.9% monthly availability and an RTO of 24 hours |
| SYS-02 | Warehouse management system (WMS) with 420 RF handhelds | Company-managed in the cloud workloads account (SYS-08) | FCI (DoD ship-to and order data) | Named badge-scan and PIN sign-in on handhelds; interfaces with SYS-01, SYS-05, and SYS-12 |
| SYS-03 | Reseller portal and order API (B2B e-commerce) | Vendor SaaS | None by design (DoD orders excluded by the ERP sync rule) | About 9,600 reseller users at 4,200 accounts; MFA enforced for company administrators and optional for resellers (38% of accounts enforce it); API ordering for 60 large resellers; card payments on the vendor's hosted payment page |
| SYS-04 | EDI service (value-added network) | Vendor SaaS | FCI in federal channel purchase orders | 140 trading partners (suppliers and large resellers) |
| SYS-05 | Transportation management system (TMS) | Vendor SaaS | FCI (ship-to addresses) | Carrier rating, tendering, labels, tracking |
| SYS-06 | Corporate identity provider (single sign-on and MFA) | SaaS | Identities only | MFA for all workforce users (push with number matching); phishing-resistant security keys for administrators since 2025; conditional access |
| SYS-07 | Corporate productivity suite (email, chat, file storage) | Vendor SaaS, commercial tier | FCI; **CUI found** (212 email messages) | Not part of the enclave |
| SYS-08 | Cloud landing zone, commercial region: 5 accounts (security, shared services, workloads, data, backup) | Public cloud (vendor-agnostic) | FCI (WMS) | Hosts the WMS, integration services (order APIs and middleware), file services, and the data warehouse. Backups are write-once for 30 days in the backup account |
| SYS-09 | **Federal Integration Enclave (FIE)** | Government community cloud: a government-community productivity and identity tenant (FedRAMP High authorized) and a dedicated enclave cloud account in a FedRAMP Moderate authorized government region | **CUI** | 64 enclave users; CUI email and file library, virtual desktops, configuration build server, image repository. In production since 2025-11 with an enclave SSP (version 1.0) |
| SYS-10 | Networks: HQ, DC-1, DC-2 on SD-WAN; warehouse Wi-Fi; FIL network | On-premises; SD-WAN managed service | CUI in transit (FIL) | The FIL has its own firewall, a wired-only lab VLAN, and a site-to-cloud VPN to the enclave |
| SYS-11 | Endpoints | Company-managed | CUI (22 FIL workstations); FCI | 880 laptops and desktops, 22 FIL workstations managed from the enclave, 420 RF handhelds, 160 label and document printers |
| SYS-12 | DC automation (operational technology) | On-premises at DC-1 | None | Conveyor and sortation controllers, 2 sorter control servers, 2 operator workstations, and vertical lift modules. Maintained by the integrator |
| SYS-13 | Physical security | On-premises | None | Badge system at all sites, 310 cameras with network video recorders, intrusion alarms, and the FIL cage (badge plus PIN). Cameras were checked against the FAR 52.204-25 covered manufacturers in 2025 (none covered) |
| SYS-14 | Security tooling | SaaS and cloud | Security Protection Data | EDR on all corporate and FIL endpoints; SIEM operated by the MSSP; privileged access broker for cloud and server administrators; vulnerability scanner |
| SYS-15 | Demand forecasting and automated reordering platform | Vendor SaaS connected to SYS-01 | Order history (includes federal channel orders, FCI) | AI-001 in P10. In production since 2025-10; auto-release of purchase orders enabled 2026-02 |
| SYS-16 | Other AI tools | Vendors | Varies | AI-002 enterprise generative AI assistant, AI-003 reseller portal chatbot, AI-004 invoice capture and payment anomaly scoring, AI-005 resume screening in the applicant tracking system |
| SYS-17 | Third parties with system or data access | Various | Varies | About 180 vendors; 22 are Tier 1 under the P09 tiering approach |

**SSP system (P02):** the *Distribution Operations Platform (DOP)*: SYS-01 to SYS-14, a Moderate-impact system that includes the Federal Integration Enclave (SYS-09) and the Federal Integration Lab, which with their security protection assets form the CMMC Level 2 assessment scope under 32 CFR 170.19(c).

## 4. Current security posture: defined program with gaps in scale

**In place today:**
- Single sign-on with MFA for all workforce users; phishing-resistant security keys for administrators
- EDR on all corporate and FIL endpoints, with 24x7 MSSP monitoring and a SIEM
- A Federal Integration Enclave in a government community cloud, with an enclave SSP (2025-11) and a documented SP 800-171 self-assessment (2025-12)
- A privileged access broker for cloud and server administrators
- Write-once backups of landing zone workloads in a separate backup account
- Monthly authenticated vulnerability scanning of corporate servers and endpoints
- Security policies adopted in 2024 and an annual risk assessment (last in 2025-07)
- Annual awareness training, annual CUI training for enclave users, and quarterly phishing simulations
- An approved supplier list in the ERP with an authorized-source flag, and Section 889 manufacturer screening on federal orders since 2025
- Call-back verification for supplier bank-detail changes since 2024
- An annual co-sourced internal IT audit
- Cyber insurance with a carrier breach hotline

**Missing or weak, found in the 2026 assessments:**
1. **CUI has spread outside the enclave.** 37 ERP sales orders carry CUI attachments, 212 email messages with CUI sit in the commercial productivity tenant (most sent by Prime C's program office after 2026-03 to a general federal sales mailbox), and printed CUI configuration sheets were found at Integration Center benches outside the FIL.
2. **Supply chain controls are uneven.** The C-SCRM plan (2025) is a draft that was never approved. 9 of 31 brokers have not been reassessed in 2 years. The DFARS 252.246-7007(c) system criteria are only partly addressed. DC-2 receiving does not perform the authenticity inspection that DC-1 performs. Private-label import contracts have no security or authenticity terms.
3. **Section 889 and FASCSA screening has holes.** 2,140 of about 68,000 active SKUs (3.1%) have no manufacturer of record. Screening does not cover drop-ship orders placed directly with suppliers. The FAR 52.204-30 SAM.gov search for FASCSA orders has never been run or logged.
4. **DC automation is exposed.** The DC-1 conveyor and sortation control network is reachable from corporate VLANs, the integrator uses an always-on remote access tool, and there is no OT asset inventory or monitoring.
5. **Access reviews and privileged access are incomplete.** Access reviews are quarterly for the ERP only; WMS and enclave reviews are annual (last 2025-12). The privileged access broker does not cover ERP, WMS, or enclave tenant administrators.
6. **Recovery is unproven at scale.** WMS and integration service restores were last tested in 2025-09. The ERP vendor's 24-hour RTO does not meet the BIA. Manual pick mode at DC-1 runs at about 40% of normal capacity.
7. **Logging gaps.** ERP, WMS, reseller portal, and DC automation logs are not in the SIEM. FIL firewall logs are kept 30 days. Enclave logs reached the SIEM only in 2026-05.
8. **Third-party oversight lags.** 9 of 22 Tier 1 vendor reviews are overdue. There is no customer responsibility matrix for the MSSP as an External Service Provider.
9. **Reseller portal accounts are weakly protected.** MFA is optional for resellers. A credential-stuffing attack in 2026-04 took over 11 reseller accounts; credit review stopped 3 fraudulent orders worth $96,400.
10. **AI tools were adopted without governance.** Auto-release of purchase orders was enabled in 2026-02 without a formal review. The portal chatbot and the resume screening module were turned on by departments. There is no AI inventory.
11. **Incident response is generic.** The 2024 incident response plan covers ransomware in general terms only. There is no product (counterfeit or tampering) incident runbook. Only one person holds a DIBNet medium assurance certificate. The last tabletop exercise was in 2025-03.
12. **Standards are thin.** Configuration baselines exist for Windows endpoints and enclave virtual desktops only. There are no OT, network device, or SaaS configuration standards.
13. **Found during P07 testing:** 64 optical transceiver modules bought from a broker were received at DC-2 without authenticity inspection. The OEM could not validate 23 of the serial numbers. 18 units had shipped to 2 commercial resellers; none went to a DoD order or a FIL job.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 | Primary: NIST SP 800-171 Rev. 2 (110 requirements) as required by DFARS 252.204-7012 and assessed under CMMC Level 2, scoped to the CMMC Level 2 assessment scope (the enclave, the FIL, their security protection assets, and every place CUI was found). Secondary, for the same federal business line: FAR 52.204-21 (15 requirements, CMMC Level 1) for the FCI stream, and the supply chain and reporting clauses in the subcontracts: FAR 52.204-25, FAR 52.204-30, DFARS 252.246-7007 and 252.246-7008, and the DFARS 252.204-7012, -7019/-7020, and -7021 clause duties. Evidence sampling throughout |
| P08 | **Two incident types:** (1) supplier compromise introducing tampered or counterfeit products into distribution (registry default, kept because it is the company's most distinctive risk), and (2) ransomware halting distribution operations, with possible FCI or CUI exposure. Both integrated with crisis management and legal |
| P09 | SOC 2 Type 2 readiness for the Partner Commerce Platform (reseller portal, order API, EDI, and the order processing behind them), requested by 3 national reseller customers; Security, Availability, Confidentiality, and Processing Integrity. Plus a vendor SOC 2 review program |
| P10 | AI use-case portfolio: AI-001 demand forecasting and automated reordering (registry default, kept; at this size it releases purchase orders automatically), AI-002 enterprise generative AI assistant, AI-003 reseller portal chatbot, AI-004 invoice capture and payment anomaly scoring, AI-005 resume screening for warehouse hiring |
| Cloud | Multi-account landing zone in a commercial region plus the separate government community enclave. Vendor-agnostic; AWS, Azure, and Google Cloud names appear only in an equivalents table |
| Supply chain practice | NIST SP 800-161 Rev. 1 (upd1) C-SCRM practices, applied through SP 800-53 SR controls |
| Registry defaults | The primary system (order management, warehouse, and reseller portal) is kept and named the Distribution Operations Platform. The P08 incident and P10 use case are kept as the registry gives them |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-07-06 to 2026-07-31 | BIA, risk assessment, and gap analysis fieldwork |
| 2026-08-03 to 2026-08-21 | Control assessment (co-sourced internal audit firm) |
| 2026-09-17 | Results to the audit committee; deliverables approved |
| 2026-11-10 | Planned CMMC Phase 2 start (32 CFR 170.3(e)(2)), suspended by the DoD (Department of War) CIO memorandum of 2026-07-13 |
| 2027-03 | Planned CMMC Level 2 (C3PAO) certification assessment (customer-driven while CMMC Phase 2 is suspended) |
| 2027-04-01 to 2027-09-30 | Planned SOC 2 Type 2 observation period |
| 2027-06-01 | Prime A option period and new Prime B task orders were to require CMMC Level 2 (C3PAO); requirement suspended with CMMC Phase 2 |

## 7. Facts added during the build (fictional; used across P01-P10)

| Topic | Added fact |
|---|---|
| Volumes | About 9,800 order lines and 3,600 shipments per shipping day; about 68,000 active SKUs. DC-1 ships about 80% of units. About 1,100 federal channel shipments and 45 FIL configuration jobs a month |
| Order channels | Reseller portal and order API about 55% of order lines, EDI about 25%, orders entered by sales staff about 20% |
| Enclave users | 64: 22 FIL technicians, 14 federal program staff, 10 federal inside sales staff, 8 IT and security administrators, 6 quality and purchasing staff, 4 contracts staff |
| Workforce activity | 214 terminations and 96 internal transfers in the 12 months to 2026-06-30. The June 2026 phishing simulation click rate was 5.9% |
| Cyber insurance | $15 million limit, $500,000 retention. The carrier's panel supplies breach counsel and forensics; the policy requires a call to the carrier hotline before incident vendors are engaged |
| Near misses | 2026-02: a broker's spoofed request to change bank details was stopped by call-back. 2026-04: credential stuffing on the reseller portal (gap 9) |
| Recovery facts | DC-1 and DC-2 have dual ISPs on SD-WAN; HQ has one. The WMS database is replicated every 15 minutes to a standby in a second zone; daily write-once backups. DC-1 manual pick mode (paper pick lists printed from the WMS standby) runs at about 40% of normal capacity |
| Optical transceivers (P07, P08) | 64 units received at DC-2 on 2026-06-18 from broker BRK-17; quarantined 2026-08-13; 18 units shipped to 2 commercial resellers; the broker is suspended pending review (due 2026-10-31) |
| Security budget | FY2027 security and compliance plan approved by the Chief Executive Officer on 2026-09-17: $1.31 million one-time and $585,000 a year (split in P01) |
| Partner Commerce Platform (P09) | 3 national resellers asked for a SOC 2 Type 2 report in 2026-05; one made it a condition of its 2028 contract renewal |
| DIBNet certificates | A second medium assurance certificate (Contracts Compliance Manager, a new role on the Director of Federal Programs' team) is planned by 2026-10-31 |
| Additional role titles | Contracts Compliance Manager; DC-1 General Manager; DC-2 General Manager; Integration Center Manager; Customer Service Director; Credit Manager |
