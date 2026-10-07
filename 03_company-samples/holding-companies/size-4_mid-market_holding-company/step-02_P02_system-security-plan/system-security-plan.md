# System Security Plan: Shared Corporate Services Platform (SCSP)

**Organization:** Cris Santos Company, Inc. (PE-backed holding company with four operating subsidiaries) | **Tier:** Mid-Market | **Vertical:** Management of Companies and Enterprises
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-22

## 1. System Name and Identifier
Shared Corporate Services Platform (**SCSP**), identifier CSC-SCSP-01. The SCSP comprises SYS-01 to SYS-11 and SYS-16 in `../00_company-facts.md`.

## 2. System Overview
The SCSP is the IT platform the holding company runs for itself and its four subsidiaries: CSC Building Supply ("Supply"), CSC Home Services ("Home Services"), CSC Fabrication ("Fabrication"), and CSC Consumer Finance ("Finance"). It delivers the shared services the subsidiaries pay management fees for: accounting and consolidation, treasury and payments, payroll, HR and benefits, email and files, identity, and the integrations that bring subsidiary sales, production, and loan data into the general ledger. It serves 600 employees at 9 Florida sites and supports every process in the BIA (P05).

**Major components:**
| ID | Component | Hosting and service model |
|---|---|---|
| SYS-01 | Cloud ERP (multi-entity general ledger, payables, receivables, intercompany, consolidation, Fabrication order module) | Vendor SaaS; vendor SOC 2 Type 2 |
| SYS-02 | Hybrid identity: on-premises directory forest (3 domain controllers) synchronized to a cloud identity provider (single sign-on, MFA, conditional access) | On-premises and SaaS |
| SYS-03 | Productivity suite (email, files, chat, phones, device management), one tenant with five email domains | SaaS |
| SYS-04 | Cloud landing zone, 5 accounts: integration service, reporting warehouse, SFTP bank file transfer server, invoice imaging, backup vault | Public cloud IaaS and PaaS, vendor-agnostic (P04) |
| SYS-05 | HRIS, payroll, and benefits enrollment | Vendor SaaS |
| SYS-06 | Treasury management system and bank portals | SaaS and bank-hosted |
| SYS-07 | Board portal and virtual data room | Vendor SaaS |
| SYS-08 | 430 laptops and desktops, 95 technician tablets, 120 warehouse scanners | Company-managed |
| SYS-09 | Site networks at 9 sites on SD-WAN | On-premises; SD-WAN managed service |
| SYS-10 | HQ server room (domain controllers, file servers, print, scanner management) and the Fabrication plant production server | On-premises |
| SYS-11 | EDR, SIEM (MSSP-operated), vulnerability scanner | SaaS |
| SYS-16 | Generative AI assistant (add-on to SYS-03), 180 users | SaaS |

The subsidiary line-of-business systems (SYS-12 to SYS-15) and other vendors (SYS-17) connect to the SCSP as interconnected systems (section 8).

**Why this system matters to regulators of group companies.**
- **Finance (FTC Safeguards Rule).** The SCSP receives, maintains, and processes Finance's customer information (email, files, backups, the reporting warehouse, ACH files, and identity for the loan servicing system). The holding company is therefore Finance's service provider (16 CFR 314.2(r)) and the affiliate that employs Finance's Qualified Individual (314.4(a)). Finance must require the holding company to maintain a program that protects Finance as the rule requires (314.4(a)(3)). This SSP is the main evidence of that program.
- **The self-funded group health plan (HIPAA).** The Benefits team keeps plan PHI (appeals, stop-loss files, high-cost claimant reports) in the suite, and the HRIS holds enrollment data. The plan documents must require the sponsor to safeguard that ePHI (45 CFR 164.314(b)). The SCSP's controls are how the sponsor meets that promise.

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it affects the SCSP |
|---|---|---|---|
| Safeguards | FTC Standards for Safeguarding Customer Information | 16 CFR Part 314 | Applies to Finance; reaches the SCSP through 314.4(a)(3) and 314.4(f). Not in the vertical requirements list; cited directly (P03) |
| N55-R06 | HIPAA (sponsored group health plan) | 45 CFR Part 164, Subparts C, D, and E | The plan is a covered entity; the sponsor's handling of plan ePHI must meet the plan document terms (164.504(f), 164.314(b)). Mapped in `control-implementation.csv` |
| N55-R07 | CIRCIA (proposed, not in force) | Proposed 6 CFR Part 226 | Tracked only (P03) |
| State | Florida Information Protection Act | Fla. Stat. 501.171 | Reasonable measures for personal information; breach notice (P08) |
| State | Florida Security of Communications Act | Fla. Stat. 934.03 | All-party consent for call and meeting recording (AI uses in P10) |
| Benchmark | NIST CSF 2.0 group profile | NIST CSWP 29; NIST SP 1301 | Target outcomes for the group (P03) |
| Contract | Bank partner participation agreement; credit agreement; sponsor portfolio cyber standard | Contracts | SOC 2 Type 2 for the bank partner (P09); incident notice to lenders and the sponsor (P08); annual independent assessment (P07) |
| Internal | Security policies POL-01 to POL-05 and supporting standards | P06 | Policy basis for every control |

Not applicable (reasons in P03):
- **N55-R01, N55-R02, N55-R03:** SEC Regulation S-K Item 106, Form 8-K Item 1.05, and SOX section 404 apply to SEC registrants and issuers. The company is private and files nothing with the SEC. Its audited financial statements are a lender requirement, not SOX.
- **N55-R04, N55-R05:** Federal Reserve Regulation Y Subpart N and 12 CFR Part 225 Appendix F apply to bank holding companies. The company controls no bank. The bank partner relationship does not change this: the bank buys participations, and Finance remains a non-bank lender.
- **PCI DSS scope:** card payments use processor point-to-point encrypted devices and a hosted payment page outside the SCSP (noted, not assessed).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the CFO (system owner) on 2026-09-22, after the control assessment (P07) and before the audit committee meeting the same day.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization to operate. The equivalent internal decisions:
- **Decision:** continued operation of the SCSP accepted with conditions, 2026-09-22.
- **Authorizing official equivalent:** CEO for High risks; CFO for Moderate and below; the board for any temporary Very High exception (P01 acceptance authorities).
- **Conditions:** the High-risk POA&M items in P07 meet their milestones; the audit committee receives POA&M status each quarter; re-decision by 2027-09-30 or after a major change (an acquisition counts as one).
- **Finance:** Finance's Board of Managers received this plan with the Qualified Individual's 2026 written report on 2026-09-22 (16 CFR 314.4(i)).
- **Group health plan:** the Benefits Committee accepted the plan's 2026 HIPAA risk analysis (P01 and P03) on 2026-09-22.
### 4.3 System Operational Status
Operational. Major modifications planned:
- Integration of Home Services North into group identity, email, device management, and EDR (due 2027-03-31)
- Privileged access management for directory, identity provider, ERP, and treasury administrators; directory tiering and service account clean-up (due 2027-03-31)
- Off-site, immutable backups for HQ and plant servers and a tested directory forest recovery (due 2027-01-31)
- Plant network segmentation and brokered vendor remote access (due 2027-03-31)
- Expansion of SIEM sources to the ERP, HRIS, subsidiary SaaS, file servers, and the plant (due 2027-03-31)

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | CFO | Accountable for the SCSP; executive sponsor of the security program; accepts Moderate risk |
| Authorizing official equivalent (High risk) | CEO | Accepts High risk; approves policies and the security budget |
| Oversight | Audit committee of the board | Quarterly cyber risk reporting; oversees internal audit |
| Program strategy | vCISO (part-time contractor) | Strategy, standards approval, audit committee reporting, SSP review |
| Security lead | Security Manager | Day-to-day security; Qualified Individual for Finance (16 CFR 314.4(a)); HIPAA Security Official for the plan (45 CFR 164.308(a)(2)) |
| Technical owner | VP of Information Technology | Operates the SCSP; owns recovery and configuration |
| Oversight of the Qualified Individual | Finance President | Senior Finance officer who directs and oversees the Qualified Individual (16 CFR 314.4(a)(2)) |
| Plan Privacy Official | VP of Human Resources | Privacy Rule duties for the plan; plan sponsor firewall (164.504(f)(2)(iii)) |
| Information owners | Controller (ERP), Treasurer (treasury and bank files), VP of Human Resources (HRIS), Benefits Manager (plan PHI), Finance President (loan data), VP of Corporate Development (deal data) | Approve access and data handling for their data |
| Subsidiary owners | Supply, Home Services, Fabrication, and Finance Presidents | Approve access for their staff; own their line-of-business systems |
| Legal | General Counsel | Breach and notification decisions; contracts with security terms |
| Independent assessment | Co-sourced internal audit firm | Annual IT general controls review; P07 assessment |
| Monitoring | MSSP | 24x7 EDR and SIEM monitoring |

## 6. System Information Types and System Categorization
Information types follow the NIST SP 800-60 Vol. 2 Rev. 1 approach. Where the catalog has no fitting type (it was written for federal missions), an organization-defined type is used and marked. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Financial management: payments and collections (vendor payments, ACH files, bank details) | Moderate | Moderate | Moderate | A redirected payment or altered ACH file causes serious financial loss; dual approval and positive pay limit the harm; BIA MTD 24 h for treasury and collections (P05) |
| Financial management: accounting and reporting (ledger, consolidation, lender reports) | Moderate | Moderate | Low | Errors or leaks harm lender relationships; close can slip several days (P05 MTD 120 h) |
| Human resources management (employee SSNs, bank accounts, enrollment data) | Moderate | Moderate | Low | Breach triggers state notice duties for 600 employees; payroll MTD 72 h |
| Consumer customer information of Finance (organization-defined) | Moderate | Moderate | Moderate | SSNs, bank accounts, and credit reports of about 34,000 consumers; FTC and state notice duties; collections post daily |
| Group health plan PHI held by the sponsor (organization-defined; health care administration in the catalog) | Moderate | Moderate | Low | Claims and diagnosis details for up to 1,100 covered persons; HIPAA breach duties; the TPA keeps paying claims if the SCSP is down (P05 MTD 120 h) |
| Acquisition and board information (organization-defined) | Moderate | Low | Low | Leaks harm negotiations and confidentiality agreements; no public-market trading exposure because the company and its targets are private |
| System and network monitoring (security logs) | Moderate | Moderate | Low | Needed for breach investigations and FTC and HIPAA determinations |
| **SCSP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Confidentiality was considered for High.** A breach of all Finance customer information (about 34,000 consumers) would be serious and expensive, but it would not threaten the group's survival or stop it from operating: the cyber insurance limit covers the expected response cost, and the data is not of the kind (for example, authentication secrets for the banks) that would allow catastrophic loss on its own. The team kept Moderate and compensated with stronger tailoring for access and monitoring of Finance data (AC-6, AU-6, SI-4).

## 7. Authorization Boundary Description
**Inside the boundary:**
- the ERP, HRIS, treasury system, and board portal tenant configurations and roles;
- the on-premises directory forest and the cloud identity provider tenant;
- the productivity suite tenant, including the AI assistant;
- all 5 cloud accounts and their workloads;
- the HQ server room and the Fabrication plant production server;
- 430 laptops and desktops, 95 tablets, and 120 scanners;
- site networks at 9 sites;
- the company's EDR, SIEM, and scanner tenants and their use cases.

**Outside the boundary (external or subsidiary systems, interconnected):**
- the vendors' platforms under each SaaS service, the cloud provider's infrastructure, and the MSSP's platform;
- the bank portals' bank-side systems;
- the subsidiary line-of-business systems SYS-12 (Supply), SYS-13 (Home Services), SYS-14 (Finance), and the plant machines in SYS-15, which their subsidiaries own and which connect through single sign-on, the integration service, or the plant network;
- **Home Services North's separate email tenant, field-service product, and server.** They are outside the boundary until integration (due 2027-03-31) and are treated as an untrusted connection meanwhile;
- the health plan TPA and PBM platforms;
- about 160 other vendors (SYS-17).

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Operating banks (SYS-06 portals and SFTP) | Bidirectional | ACH collection files, positive pay files, wire instructions | Treasury services agreements |
| Supply distribution system (SYS-12) | Inbound to integration service; SSO outbound | Daily sales and receivables summary; user sign-ins | Intercompany services agreement |
| Home Services field-service system (SYS-13) | Inbound to integration service; SSO outbound | Daily invoices and payments | Intercompany services agreement |
| Home Services North field-service product | Manual export by email | Daily invoices | **None (gap, integration pending)** |
| Finance loan servicing system (SYS-14) | Inbound to integration service; SSO outbound | Loan general ledger summary; user sign-ins | Intercompany services agreement with a security schedule protecting Finance (16 CFR 314.4(a)(3), (f)(2)), signed 2026-09-22 |
| Fabrication plant server (SYS-15) | Inbound to ERP (orders and shipments) | Production orders | Intercompany services agreement |
| Health plan TPA and PBM | Inbound reports; outbound enrollment files from the HRIS | Claims reports, stop-loss files, enrollment | Business associate agreements (2024) |
| Payroll tax and benefits carriers | Outbound from HRIS | Payroll tax filings; enrollment files | Vendor contracts |
| Bank partner (from 2027-01) | Outbound | Participation reports and loan-level servicing data | Participation agreement (2026-08-15) |
| MSSP | Inbound logs; remote response actions | Security logs (may include personal information fragments) | MSSP contract; SOC 2 Type 2 |
| Machine vendors (plant) | Inbound remote access | Machine programs and diagnostics | **No written security terms (gap)** |
| Seller's IT provider (Home Services North) | Inbound administration | North server and laptops | **No group contract (gap)** |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| ERP tenant | SaaS | ERP vendor | Controller |
| Directory forest (3 domain controllers) | On-premises servers and one cloud virtual machine | HQ server room; shared services account | VP of Information Technology |
| Identity provider tenant | SaaS | Identity vendor | Security Manager |
| Productivity suite tenant and AI assistant | SaaS | Suite provider | VP of Information Technology |
| Integration service | Serverless functions (PaaS) | Workloads account | VP of Information Technology |
| Reporting warehouse | Managed database (PaaS) | Workloads account | Controller |
| SFTP server | Virtual machine | Workloads account | Treasurer (data); VP of Information Technology (system) |
| Invoice imaging | Managed service with object storage | Workloads account | Controller |
| Backup vault | Backup service with write-once retention | Backup account (second region) | VP of Information Technology |
| Network hub, cloud firewall, VPN, privileged access broker | Network and management services | Shared services account | VP of Information Technology |
| Log archive and posture tooling | Storage and security services | Security and log archive account | Security Manager |
| Organization guardrails | Policy services | Management account | Security Manager |
| HRIS and payroll tenant | SaaS | HRIS vendor | VP of Human Resources |
| Treasury system tenant | SaaS | Treasury system vendor | Treasurer |
| Board portal and data room | SaaS | Board portal vendor | VP of Corporate Development |
| File servers (3), print server, scanner management server, NAS | On-premises servers | HQ server room | VP of Information Technology |
| Plant production server | On-premises server | Fabrication plant | Fabrication Plant Manager |
| SD-WAN edges, firewalls, switches, Wi-Fi | Network | 9 sites | VP of Information Technology |
| Laptops and desktops (430), tablets (95), scanners (120) | Endpoint | All sites | VP of Information Technology |
| EDR, SIEM, and scanner tenants | SaaS | Security vendors and MSSP | Security Manager |

## 10. Control Implementation Details
### 10.1 Control implementation status
**Baseline and tailoring.** The SCSP uses the NIST SP 800-53B **Moderate** baseline (287 controls and enhancements), tailored as follows:
- **Documented here: 115 controls** in `control-implementation.csv`. They cover every control mapped to a Safeguards Rule element or a HIPAA Security Rule standard or implementation specification in P03 (author mappings), the controls behind the CSF 2.0 group profile's priority outcomes, and the Moderate controls that address the risks in P01 (identity, privileged access, recovery, monitoring, third parties).
- **Selected by tailoring (added, 4):** PM-1, PM-2, and PM-9 for group governance and the Qualified Individual and Security Official roles, and CA-8 because Finance needs annual penetration testing (16 CFR 314.4(d)(2)(i)). None of the 4 is in the Moderate baseline.
- **Inherited without separate statements:** the physical and environmental controls for provider data centers (for example PE-9 to PE-17) and platform-level SA and SC controls, inherited from the SaaS vendors, the cloud provider, and the MSSP and evidenced by their SOC 2 Type 2 reports, which are reviewed under the vendor program (P09).
- **Deferred:** the other Moderate controls with no regulatory mapping and no Moderate-or-higher risk in P01 (for example SA-11 developer testing and SA-15 development process, because the group does not develop software; the integration service uses vendor connectors configured by IT). They are recorded as tailoring decisions and reviewed each year.

**Status of the 115 documented controls:**
| Status | Count |
|---|---|
| Implemented | 33 |
| Partially implemented | 78 |
| Planned | 4 |
| Not applicable | 0 |

**Inheritance of the 115 documented controls:**
| Inheritance | Count | Main providers |
|---|---|---|
| System-specific | 70 | Company |
| Hybrid | 35 | Identity vendor, cloud provider, suite provider, MSSP, SaaS vendors, SD-WAN provider |
| Common/Inherited | 10 | Identity vendor (for example AC-7, IA-2(1)), cloud provider (SC-12), MSSP (AU-6(1), IR-7), suite provider (AC-12) |

The Partially implemented statements trace to the 13 known gaps in `../00_company-facts.md` section 4 and to the P07 findings. The 4 Planned controls are CM-12 (data map), CP-3 (recovery training), SI-12 (retention schedule), and SR-2 (supply chain plan).

### 10.2 Control assessment status
The co-sourced internal audit firm assessed 36 controls from 2026-08-17 to 2026-09-04 (P07 `assessment-plan.md`, `assessment-results.csv`, and `poam.csv`). Weaknesses are tracked in the POA&M and reported quarterly to the audit committee and, for Finance customer information, in the Qualified Individual's annual report.

## 11. Digital Identity Acceptance Statement
- **Workforce.** Integrated users authenticate through the cloud identity provider with a password and push MFA with number matching. Administrators must also use a compliant device. That is acceptable for standard users of a Moderate system, but it is **not phishing-resistant**, which is the weakness behind P01 R-003.
- **Administrators and high-risk roles.** By 2027-03-31, administrators and users in treasury, payables, HR, benefits, and Finance (about 70 people) will use FIDO2 security keys, and directory administration will require MFA through the privileged access workflow (P01 R-003, R-004).
- **Home Services North.** Its users sign in to their own email tenant and field-service product with passwords only. Until integration, they get group accounts only for the HRIS and ERP, with MFA.
- **Finance borrowers and Supply contractors.** Borrowers use the loan servicing vendor's portal, and contractors use the distribution vendor's portal, each with the vendor's own identity proofing. These are governed by the vendor contracts, outside this boundary. P01 R-046 tracks MFA for the contractor portal.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`); risk register (P01); CSF 2.0 group profile, Safeguards Rule, and HIPAA gap analysis (P03); cloud architecture and control map (P04); BIA (P05); policies and standards index (P06); assessment and POA&M (P07); incident runbooks (P08); SOC 2 readiness and vendor reviews (P09); AI governance assessment (P10).

## 13. Acronym List and Glossary
- **ACH:** Automated Clearing House (bank payment network)
- **EDR:** endpoint detection and response
- **ERP:** enterprise resource planning
- **HRIS:** human resources information system
- **MSSP:** managed security service provider
- **MTD, RTO, RPO:** maximum tolerable downtime, recovery time objective, recovery point objective
- **PBM:** pharmacy benefit manager
- **POA&M:** plan of action and milestones
- **Qualified Individual:** the person who oversees and enforces Finance's information security program (16 CFR 314.4(a))
- **SCSP:** Shared Corporate Services Platform
- **SFTP:** secure file transfer protocol
- **TPA:** third-party administrator (of the group health plan)

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-08-07 | Draft from the BIA, risk assessment, and gap analysis | Security Manager |
| 1.0 | 2026-09-22 | Updated with P07 results; approved by the CFO | Security Manager, reviewed by the vCISO |
