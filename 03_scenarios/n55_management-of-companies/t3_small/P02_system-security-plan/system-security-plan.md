# System Security Plan: Shared Corporate Services Platform (SCSP)

**Organization:** Cris Santos Company, LLC (holding company with three operating subsidiaries) | **Tier:** Small | **Vertical:** Management of Companies and Enterprises
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-25

## 1. System Name and Identifier
Shared Corporate Services Platform (**SCSP**), identifier CSC-SYS-001.

## 2. System Overview
The SCSP is the IT platform the holding company runs for itself and its three subsidiaries: CSC Building Supply ("Supply"), CSC Home Services ("Home Services"), and CSC Consumer Finance ("Finance"). It supports the shared services that the subsidiaries pay management fees for: accounting and consolidation, treasury and payments, payroll and HR, email and files, identity, and the connections that bring subsidiary sales and loan data into the general ledger. It serves all 60 employees at three Florida sites.

**Major components:**
- **SYS-01:** a SaaS cloud ERP (multi-entity general ledger, payables, receivables, intercompany, consolidation)
- **SYS-02:** one identity provider tenant for single sign-on and MFA across all four entities
- **SYS-03:** one productivity suite tenant (email, files, chat, device management), including the generative AI assistant pilot (SYS-13)
- **SYS-04:** a public-cloud tenant hosting the integration service, the reporting database, the bank file transfer (SFTP) server, and the backup vault
- **SYS-05:** a SaaS HRIS and payroll service for four employer entities
- **SYS-08:** endpoints (50 laptops, 10 desktops, 16 tablets)
- **SYS-09:** site networks at HQ, the Supply warehouse, and the Home Services shop

The cloud tenant is described by service category and is vendor-agnostic (see P04).

**Why this system matters to Finance's regulator.** Finance is a financial institution under the FTC Safeguards Rule. The SCSP receives, maintains, and processes Finance's customer information (in email, files, backups, identity for the loan servicing system, and ACH collection files), so the holding company is Finance's service provider (16 CFR 314.2(r)) and its affiliate that employs Finance's Qualified Individual (16 CFR 314.4(a)). Finance must require the holding company to maintain an information security program that protects Finance as the rule requires (314.4(a)(3)). This SSP is the main evidence of that program.

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it affects the SCSP |
|---|---|---|---|
| Safeguards | FTC Standards for Safeguarding Customer Information | 16 CFR Part 314 | Applies to Finance; reaches the SCSP through 314.4(a)(3) and 314.4(f). Not in the vertical requirements list; added from primary text (see P03) |
| State | Florida Information Protection Act (breach notification) | Fla. Stat. 501.171 | Employee SSNs and bank accounts, and Finance customer information, are personal information |
| N55-R06 | HIPAA (sponsored group health plan) | 45 CFR Part 164 | Limited: the fully insured plan's sponsor receives only enrollment and summary health information (164.530(k)); the HRIS holds enrollment data |
| N55-R07 | CIRCIA (proposed, not in force) | Proposed 6 CFR Part 226 | Tracked only |
| Benchmark | NIST CSF 2.0 group profile | NIST CSWP 29; NIST SP 1301 | Target outcomes for the group (P03) |
| Internal | Security policies POL-01 to POL-05 | P06 | Apply to all four entities |

Not applicable (reasons in P03):
- N55-R01, N55-R02, N55-R03: SEC Regulation S-K Item 106, Form 8-K Item 1.05, and SOX section 404 apply to SEC registrants and issuers. The company is private and files nothing with the SEC.
- N55-R04, N55-R05: Federal Reserve Regulation Y Subpart N and 12 CFR Part 225 Appendix F apply to bank holding companies. The company controls no bank.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the CEO on 2026-09-25.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization. The equivalent internal decisions:
- The CEO accepted continued operation of the SCSP on 2026-09-25, with the conditions in the P07 POA&M.
- The Board of Managers approved the treatment plans for the four High risks in P01 on 2026-09-25.
- Finance's Board of Managers received this plan with the Qualified Individual's 2026 written report on 2026-09-25 (16 CFR 314.4(i)).
### 4.3 System Operational Status
Operational. Major modifications planned:
- Backup redesign to a separate account and region (P01 R-004), due 2027-01-31.
- Identity hardening: fewer global administrators, hardware keys, device-based conditional access (P01 R-001, R-003), due 2026-12-31.
- Expansion of the AI assistant beyond 25 users is on hold pending P10 conditions.

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | CFO | Accountable for the SCSP; accepts Moderate risk |
| Risk acceptor (authorizing official equivalent) | CEO; Board of Managers for Very High | Accepts High risk with a dated plan and reports to the Board |
| Security lead | IT Manager | Day-to-day security; Qualified Individual for Finance (16 CFR 314.4(a)) |
| Oversight of the Qualified Individual | Finance President | Senior Finance officer who directs and oversees the Qualified Individual (16 CFR 314.4(a)(2)) |
| Information owners | Controller (ERP), HR Director (HRIS), Treasury and Payments Analyst (bank files), Finance President (loan data) | Approve access and data handling for their data |
| Subsidiary owners | Supply, Home Services, and Finance Presidents | Approve access for their staff; own their line-of-business systems |
| Operations support | Co-managed IT provider (MSP) | After-hours help desk; firewall and server patching |

## 6. System Information Types and System Categorization
Information types follow the SP 800-60 Vol. 2 Rev. 1 approach. Where the catalog has no fitting type (it was written for federal missions), an organization-defined type is used and marked. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Financial management: payments and collections (vendor payments, ACH collection files, bank details) | Moderate | Moderate | Moderate | A redirected payment or altered ACH file causes serious financial loss; bank dual approval and positive pay limit the harm; BIA MTD 24 h for treasury (P05) |
| Financial management: accounting and reporting (ledger, consolidation, lender reports) | Moderate | Moderate | Low | Errors or leaks harm lender relationships; close can slip several days (P05 MTD 120 h) |
| Human resources management (employee SSNs, bank accounts, enrollment data) | Moderate | Moderate | Low | Breach triggers state notice duties; payroll has 72 h MTD |
| Consumer customer information of Finance (organization-defined) | Moderate | Moderate | Moderate | SSNs, bank accounts, and credit reports of about 8,600 consumers; FTC and state notice duties; collections post daily |
| Acquisition and board information (organization-defined) | Moderate | Low | Low | Leak of deal terms harms negotiations; no public-market trading exposure because the company and targets are private |
| **SCSP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 60-person group, plus program management controls PM-1, PM-2, and PM-9 for group governance. The plan documents **66 controls** that carry the Safeguards Rule elements and the CSF 2.0 group profile's priority outcomes (see `control-implementation.csv`). Every other Moderate-baseline control is treated as follows:
- **Inherited** from the SaaS and cloud providers, as evidenced by their SOC 2 reports (P09).
- **Out of scope for this tier**, recorded as a tailoring decision, where the control's purpose applies only to federal systems.

## 7. Authorization Boundary Description
The boundary contains group-managed components and the group's configuration of vendor services:
- **Inside:** the ERP tenant configuration and roles; the identity provider tenant; the productivity suite tenant, including the AI assistant; the cloud tenant (4 workloads); the HRIS tenant configuration; 50 laptops, 10 desktops, and 16 tablets; and the networks at all three sites.
- **Outside (external or subsidiary systems, interconnected):** the vendors' platforms under each SaaS service; the cloud provider's infrastructure; the bank portals (SYS-06); the board portal (SYS-07); and the three subsidiary line-of-business systems (SYS-10, SYS-11, SYS-12), which the subsidiaries own and which connect through single sign-on or the integration service.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Bank portals and SFTP (SYS-06) | Bidirectional | ACH collection files, positive pay files, wire instructions | Treasury services agreement |
| Supply distribution system (SYS-10) | Inbound to integration service | Daily sales and receivables summary | Intercompany services agreement |
| Home Services field-service system (SYS-11) | Inbound to integration service | Daily invoices and payments | Intercompany services agreement |
| Finance loan servicing system (SYS-12) | Inbound to integration service; SSO outbound | Loan GL summary; user sign-ins | Intercompany services agreement; **no written information security requirements for the holding company as service provider (gap, 16 CFR 314.4(a)(3), (f)(2))** |
| Payroll tax and benefits carrier | Outbound from HRIS | Payroll tax filings; enrollment files | Vendor contracts |
| Board portal (SYS-07) | Outbound | Board materials | Vendor contract |
| MSP remote tools | Inbound administration | Endpoint and server management | MSP contract (**no security terms, gap**) |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| ERP tenant | SaaS | ERP vendor | Controller |
| Identity provider tenant | SaaS | Identity vendor | IT Manager |
| Productivity suite tenant and AI assistant | SaaS | Suite provider | IT Manager |
| Integration service | Cloud serverless functions (PaaS) | Cloud tenant | IT Manager |
| Reporting database | Managed database (PaaS) | Cloud tenant | Controller |
| SFTP server | Cloud virtual machine | Cloud tenant | Treasury and Payments Analyst (data); IT Manager (system) |
| Backup vault | Cloud backup service | Cloud tenant (same account and region, **gap**) | IT Manager |
| HRIS and payroll tenant | SaaS | HRIS vendor | HR Director |
| Firewalls (3), switches, Wi-Fi | Network | HQ, Supply warehouse, Home Services shop | IT Manager |
| Laptops (50), desktops (10), tablets (16) | Endpoint | All sites and field | IT Manager |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 66 controls:
- Implemented: 18
- Partially implemented: 34
- Planned: 14
- Not applicable: 0

By inheritance: 50 system-specific, 12 hybrid, and 4 common or inherited from providers.

### 10.2 Control assessment status
Assessed 2026-09-08 to 2026-09-11 by an independent assessor. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
All workforce users authenticate through the group identity provider with a password and a push notification with number matching. That is acceptable for standard users of a Moderate system today, but it is **not phishing-resistant** and is the weakness behind P01 R-001 and R-003. By 2026-12-31, administrators and users in finance, treasury, HR, and Finance (22 people) will use hardware security keys, and all users will be limited to managed devices.

Finance's borrowers use the loan servicing vendor's customer portal, with the vendor's own identity proofing and MFA. That is governed by the vendor contract and Finance's program, outside this boundary.

## 12. Referenced Artifacts
Scenario facts (`../scenario-facts.md`), risk register (P01), CSF 2.0 group profile and gap analysis (P03), cloud control map (P04), BIA (P05), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 self-benchmark and vendor review (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **ACH:** Automated Clearing House (bank payment network)
- **EDR:** endpoint detection and response
- **ERP:** enterprise resource planning
- **HRIS:** human resources information system
- **MFA:** multi-factor authentication
- **MSP:** managed service provider
- **POA&M:** plan of action and milestones
- **Qualified Individual:** the person who oversees and enforces Finance's information security program (16 CFR 314.4(a))
- **SCSP:** Shared Corporate Services Platform
- **SFTP:** secure file transfer protocol

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-09-25 | Initial plan | IT Manager |
