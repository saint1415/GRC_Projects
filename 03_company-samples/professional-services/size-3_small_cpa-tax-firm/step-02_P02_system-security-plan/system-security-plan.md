# System Security Plan: Tax Preparation and Client Portal Platform (TPCP)

**Organization:** Cris Santos Company, LLC (CPA and tax preparation firm) | **Tier:** Small | **Vertical:** Professional, Scientific, and Technical Services
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Tax Preparation and Client Portal Platform (**TPCP**), identifier CSC-SYS-001.

## 2. System Overview
The TPCP supports the firm's tax practice and the document handling for its assurance practice: client document intake, return preparation and review, e-signature of Forms 8879, electronic filing through the tax software vendor, delivery of returns, and storage of prior-year returns and workpapers. It serves 60 workforce members (plus about 6 seasonal preparers from January to April) and clients filing about 5,750 returns a year.

**Major components:**
- **SYS-01:** a vendor-hosted professional tax preparation and e-file application (SaaS). The vendor is an Authorized IRS e-file Provider that transmits returns to the IRS and states
- **SYS-02:** a SaaS client document portal with e-signature
- **SYS-03:** the document management system (DMS) and audit workpaper application, running as firm-managed workloads in SYS-04
- **SYS-04:** a public-cloud tenant hosting the DMS server and file storage, the workpaper application server, the remote access VPN gateway, and the backup vault
- **SYS-05:** an identity provider for single sign-on and MFA
- **SYS-06:** the productivity suite (email, files, chat)
- **SYS-08:** networks at the Main and Branch offices
- **SYS-09:** endpoints (62 laptops, 12 desktops, 4 printer-scanners)

The cloud tenant is described by service category and is vendor-agnostic (see P04). The generative AI features in pilot (SYS-11) sit inside SYS-01 and SYS-06 and are assessed in P10.

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| N54-R01 | FTC Standards for Safeguarding Customer Information (Safeguards Rule) | 16 CFR Part 314. Applies in full: the firm is a financial institution under 314.2(h)(2)(viii) and holds customer information on more than 5,000 consumers, so the 314.6 exception does not apply |
| N54-R02 | Disclosure or use of tax return information by preparers | 26 U.S.C. 7216; 26 CFR 301.7216-1 to -3 (civil penalty in 26 U.S.C. 6713, as described in 301.7216-1(a)) |
| N54-R03 | IRS data security expectations and e-file provider rules | IRS Pub. 4557 (Rev. 6-2024); Pub. 5708 (Rev. 8-2024); Pub. 1345 (Rev. 12-2025), including next-business-day reporting of security incidents; Form W-12 (Rev. 10-2025) line 11 data security acknowledgment |
| State | Florida Information Protection Act (data security, disposal, breach notification) | Fla. Stat. 501.171 |
| Internal | Security policies POL-01 to POL-05 | P06 |

Not applicable (reasons in `../00_company-facts.md` section 1):
- HIPAA as a business associate (N54-R06): the firm does not receive PHI on behalf of covered entities.
- FAR 52.204-21 and DFARS 252.204-7012 with CMMC (N54-R04, N54-R05): no federal contracts.
- ABA Model Rules (N54-R07): not a law firm.
- CIRCIA (N54-R09): proposed rule only.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Firm Administrator on 2026-08-31.
### 4.2 System Authorization Decision
The firm is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- The Firm Administrator accepted continued operation of the TPCP on 2026-08-31, with the conditions in the P07 POA&M.
- The Managing Partner accepted the five High risks in P01 temporarily, with dated treatment plans, all due by 2027-01-15.
### 4.3 System Operational Status
Operational. Major modifications planned before the 2027 filing season: number-matching and phishing-resistant MFA and 24x7 monitoring (P01 R-001, R-004), and mandatory client MFA on the portal (R-007).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Tax Partner | Business owner of the tax practice and the TPCP |
| Program owner | Firm Administrator | Day-to-day program owner; risk acceptance up to Moderate |
| Risk acceptor (authorizing official equivalent) | Managing Partner | Acceptance of High and Very High risks; oversight of the Qualified Individual (314.4(a)(2)) |
| Qualified Individual | IT Manager | Oversees and enforces the information security program (314.4(a)) |
| Privacy and professional standards lead | Risk and Quality Partner | IRC 7216 compliance, breach determinations with counsel, AI use review |
| Operations support | Managed service provider | After-hours help desk, patching, firewall, backup monitoring, EDR |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Taxation management (client tax return information, SSNs, bank account numbers) | Moderate | Moderate | Moderate | Disclosure enables identity theft refund fraud and triggers FTC, IRS, and state duties; altered data leads to wrong returns and preparer penalties; outages near a deadline cause late filings (P05 MTD 24 h in season) |
| Financial audit (assurance workpapers and client financial statements) | Moderate | Moderate | Low | Confidential client financial data; engagements can slip a few days (P05 MTD 120 h) |
| Customer services (portal accounts, engagement letters, client communications) | Moderate | Low | Moderate | Account data; clients depend on the portal to sign Forms 8879 in season |
| **TPCP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

The firm chose Moderate, not High, for confidentiality. A breach would cause serious harm to affected clients, but the harm is financial and recoverable (IRS Identity Protection PINs, credit monitoring, corrected returns), which fits the FIPS 199 "serious adverse effect" description.

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 60-person firm. The plan documents 64 controls that implement the Safeguards Rule elements and core network hygiene (see `control-implementation.csv`). Four controls outside the Moderate baseline were added by tailoring: CA-8 (penetration testing, required by 314.4(d)(2)(i) absent continuous monitoring) and PM-1, PM-2, and PM-9 (program, Qualified Individual, and risk strategy). Every other Moderate-baseline control is treated as follows:
- **Inherited** from the SaaS and cloud providers, as evidenced by their SOC 2 reports (P09).
- **Out of scope for this tier**, recorded as a tailoring decision, where the control's purpose applies only to federal systems (for example, most PM-series and PT-series controls).

## 7. Authorization Boundary Description
The boundary contains firm-managed components and the firm's configuration of vendor services:
- **Inside:** the tax software tenant configuration and user roles, the client portal tenant, the DMS and workpaper servers and storage, the cloud tenant (VPN gateway, backup vault), the identity provider and productivity suite tenants, both office networks, 74 laptops and desktops, and 4 printer-scanners.
- **Outside (external services, interconnected):** the tax software vendor's platform and its AI sub-processor, the IRS and state e-file systems (reached only through the vendor), the portal vendor's platform, the cloud provider's infrastructure, the practice management SaaS, the payroll SaaS, and the MSP's remote management platform.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| IRS and state e-file systems (via tax software vendor) | Outbound returns; inbound acknowledgments | Returns, acknowledgments, rejects | IRS e-file program rules (Pub. 1345); vendor contract |
| Tax software vendor's AI sub-processor | Outbound documents; inbound extracted data | Scanned source documents (W-2, 1099, K-1) | **Sub-processor terms and IRC 7216 basis under review (gap)** |
| Clients (portal) | Bidirectional | Source documents, Forms 8879, engagement letters, returns | Portal terms; engagement letter |
| Clients (email) | Bidirectional | Documents emailed by clients; returns emailed on request | **No encryption enforced (gap)** |
| Client lenders and advisers (on request) | Outbound | Copies of returns | Signed IRC 7216 consent (301.7216-3) |
| MSP remote management | Inbound management | Endpoint administration | **MSP contract has no security terms (gap)** |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| Tax preparation and e-file tenant | SaaS | Tax software vendor | Tax Partner |
| Client document portal | SaaS | Portal vendor | Client Services Supervisor |
| DMS server and file storage | Cloud virtual machine and file storage | Cloud tenant | IT Manager |
| Audit workpaper application server | Cloud virtual machine | Cloud tenant | Assurance Partner |
| Remote access VPN gateway | Cloud VPN service | Cloud tenant | IT Manager |
| Backup vault | Cloud backup service (immutable, second region) | Cloud tenant | IT Manager |
| Identity provider tenant | SaaS | Identity vendor | IT Manager |
| Productivity suite tenant | SaaS | Productivity vendor | IT Manager |
| Office firewalls (2), switches, Wi-Fi | Network | Main and Branch offices | IT Manager |
| Laptops (62), desktops (12) | Endpoint | Both offices and remote | IT Manager |
| Printer-scanners (4) | Leased device | Both offices | Firm Administrator |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 64 controls:
- Implemented: 21
- Partially implemented: 32
- Planned: 11

### 10.2 Control assessment status
Assessed 2026-08-03 to 2026-08-07 by an independent assessor. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
- **Staff:** all workforce users authenticate through the identity provider with a password and a second factor. Today that is a push approval; number matching for all users and phishing-resistant hardware keys for administrators are due 2026-11-30 (R-001, R-010). The Safeguards Rule requires MFA for any individual accessing any information system (314.4(c)(5)), and the firm applies it without exception.
- **Clients:** clients use the portal vendor's sign-in with identity checks at enrollment. MFA becomes mandatory for all client accounts by 2027-01-15. Clients who sign Forms 8879 electronically go through the identity verification that IRS Pub. 1345 requires for electronic signatures in remote transactions, provided by the tax software.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), risk register (P01), gap analysis (P03), cloud control map (P04), BIA (P05), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 self-benchmark and vendor review (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **BEC:** business email compromise
- **DMS:** document management system
- **EDR:** endpoint detection and response
- **EFIN:** Electronic Filing Identification Number
- **ERO:** Electronic Return Originator
- **MSP:** managed service provider
- **PTIN:** Preparer Tax Identification Number
- **Qualified Individual:** the person who oversees the information security program under 16 CFR 314.4(a)
- **TPCP:** Tax Preparation and Client Portal Platform
- **WISP:** written information security program (plan)

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan; replaces the system description in the 2023 WISP | IT Manager |
