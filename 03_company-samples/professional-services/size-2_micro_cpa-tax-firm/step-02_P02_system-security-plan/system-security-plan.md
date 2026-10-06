# System Security Plan: Client Tax Platform (CTP)

**Organization:** Cris Santos Company, LLC (CPA and tax preparation firm) | **Tier:** Micro | **Vertical:** Professional, Scientific, and Technical Services
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Client Tax Platform (**CTP**), identifier CSC-SYS-001. This is the scenario's primary system: the tax preparation software and the client document portal, with the email, file storage, devices, and network they depend on.

## 2. System Overview
The CTP supports the firm's core work in its single Florida office: receiving client documents, preparing and reviewing returns, collecting e-signatures on Forms 8879, transmitting returns through the tax software vendor to the IRS and states, delivering returns, and answering IRS notices. It serves 7 employees, a seasonal assistant, and about 1,400 individual clients plus 170 business clients a year.

The firm owns almost no infrastructure. Most of the CTP is vendor SaaS, and a managed service provider (MSP) runs the computers, network, and backup. This plan therefore says, for each control, what the firm does itself, what the MSP does for it, and what it inherits from a SaaS vendor.

**Major components:**
- **SYS-01:** professional tax preparation and e-file software (vendor SaaS)
- **SYS-02:** client document portal with e-signature (vendor SaaS)
- **SYS-03:** productivity suite (SaaS): email, calendar, and the client folders in cloud storage
- **SYS-06:** 4 desktops, 4 laptops, and a leased multifunction printer-scanner (MSP-managed); staff-owned phones with the suite email app
- **SYS-07:** office network: firewall, staff Wi-Fi, separate guest Wi-Fi (MSP-managed)
- **SYS-08:** SaaS-to-SaaS backup of the suite (operated by the MSP)

The client accounting and payroll platforms (SYS-04), practice management (SYS-05), and the generative AI assistant (SYS-09) are outside this boundary. They are covered by the risk register (P01), the gap analysis (P03), and, for SYS-09, the AI assessment (P10).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies |
|---|---|---|---|
| N54-R01 | FTC Safeguards Rule (GLBA) | 16 CFR Part 314 | Applies. The firm is a financial institution (314.2(h)(2)(viii)). It holds customer information on about 3,300 consumers, so the 314.6 exception removes 314.4(b)(1), (d)(2), (h), and (i). This SSP is one part of the written program (314.3(a)) |
| N54-R02 | IRC 7216 preparer disclosure and use limits | 26 U.S.C. 7216; 26 CFR 301.7216-1 to -3 | Applies to every disclosure of tax return information, including to vendors and the MSP |
| N54-R03 | IRS Pubs. 4557 and 5708 (guidance); IRS e-file rules in Pub. 1345 | IRS Pub. 4557; Pub. 5708; Pub. 1345 (Rev. 12-2025) | Pub. 1345 binds the firm as an Authorized IRS e-file Provider (next-business-day security incident report; Form 8879 retention). Pubs. 4557 and 5708 are guidance |
| N54-R09 | CIRCIA (proposed) | Proposed 6 CFR Part 226 (89 FR 23644) | Not in force. Tracked only |
| State | Florida Information Protection Act | Fla. Stat. 501.171 | Data security (501.171(2)), breach notice, and disposal (501.171(8)) |
| Internal | Security policies POL-02, POL-03, POL-04 | P06 | Together with this SSP, the risk register, and the runbook, they form the firm's written information security program |

Not applicable:
- HIPAA as a business associate (N54-R06): the firm receives no PHI.
- FAR 52.204-21 and DFARS 252.204-7012 with CMMC (N54-R04, N54-R05): no federal contracts.
- ABA Model Rules (N54-R07): not a law firm.
- AICPA confidentiality rule (N54-R08): a professional standard that applies to the CPAs; noted but not assessed, because its text was not verified for this sample.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Owner CPA on 2026-08-31.

### 4.2 System Authorization Decision
The firm is not a federal agency, so there is no formal authorization. The equivalent internal decision: on 2026-08-31 the Owner CPA accepted continued operation of the CTP, on the condition that the POA&M items in P07 are completed by their dates and the three High risks in P01 are treated before the 2027 filing season (2027-01-15).

### 4.3 System Operational Status
Operational. Planned changes before the 2027 filing season: number matching and alerting in the suite (P01 R-001), desktop encryption (R-011), backup hardening and restore tests (R-022), EDR (R-005), and a cellular failover router (R-017).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner and risk acceptor | Owner CPA | Overall accountability; accepts Moderate risk; approves this plan, the policies, and spending; IRS e-file Responsible Official |
| Qualified Individual (16 CFR 314.4(a)) | Office Manager | Runs the program day to day; maintains this plan, the risk register, and the vendor list; directs the MSP |
| Tax software administrator | Senior Tax Accountant | Tax software users and roles |
| Portal administrator | Client Services Coordinator | Portal staff accounts, e-signature setup, client support |
| IT operations | MSP (service provider) | Computers, patching, antivirus, firewall, Wi-Fi, suite administration on request, backup administration |
| Independent assessor | IT security consultant | Annual control assessment (P07) |

**Where roles overlap.** The Office Manager both runs the program and operates several controls (accounts, log review). The compensating checks are the Owner CPA's monthly review of the POA&M and the independent consultant's annual assessment (P07).

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Taxation management (client tax return information, SSNs, bank accounts) | Moderate | Moderate | Moderate | Disclosure enables identity theft and refund fraud and triggers IRS, FTC, and Florida duties; a wrong bank account on a return diverts a refund; filing deadlines limit downtime to one day (P05 MTD 24 h) |
| Customer services (client contact details, engagement letters, portal accounts) | Moderate | Low | Moderate | Contact data is used for call-back verification; clients must reach the firm in season |
| Human resources management (firm workforce data) | Moderate | Low | Low | Payroll and HR files in the suite |
| **CTP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 7-person firm. The plan documents 44 controls that carry the Safeguards Rule elements, the IRC 7216 duties, and basic cyber hygiene (see `control-implementation.csv`). All other Moderate-baseline controls are handled one of two ways:
- **Inherited** from the SaaS vendors (physical, platform, and application controls), with the tax software vendor's SOC 2 report as the main evidence (P09).
- **Tailored out** for this tier, where the control addresses federal program management or organizations with dedicated IT staff (for example, configuration control boards and separate development environments). These are recorded as tailoring decisions, not gaps.

## 7. Authorization Boundary Description
- **Inside:** the firm's tax software tenant, users, and roles (SYS-01); the portal account and its client accounts (SYS-02); the suite tenant, mailboxes, and client folders (SYS-03); 8 computers and the MFP, plus the suite app on staff phones (SYS-06); the office network (SYS-07); and the firm's backup subscription (SYS-08).
- **Outside (external services, interconnected):** the vendors' own platforms and data centers, the IRS and state e-file systems (reached through the tax software vendor), the MSP's remote management platform, SYS-04, SYS-05, and the AI assistant (SYS-09, assessed separately in P10).

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Agreement |
|---|---|---|---|
| IRS and state e-file systems (through SYS-01) | Bidirectional | Returns, extensions, acknowledgments | Tax software vendor terms; vendor is an Authorized IRS e-file Provider. Preparer-to-preparer disclosure under 26 CFR 301.7216-2(d)(1) |
| Clients (SYS-02 portal, SYS-03 email) | Bidirectional | Source documents, Forms 8879, returns | Engagement letters; **plain email attachments are a gap** (SC-8) |
| Client's lenders (on request) | Outbound | Copies of returns | Signed IRC 7216 consent before release |
| MSP remote management platform | Inbound administrative access | Device and suite management | MSP contract (**no security terms; no 7216 written notice**) |
| Backup service (MSP subcontractor) | Outbound | Copies of mailboxes and client folders | Through the MSP contract (not reviewed) |
| AI assistant (SYS-09) | Outbound prompts and uploads | Client notices and some source documents | Vendor business terms (**no IRC 7216 basis; see P10**) |
| Bookkeeping client's questionnaire | Outbound | Security answers (no client data) | None needed |

## 9. System Component Inventory
| Component | Type | Location or provider | Owner |
|---|---|---|---|
| Tax software tenant (SYS-01) | SaaS | Tax software vendor | Senior Tax Accountant |
| Client portal account (SYS-02) | SaaS | Portal vendor | Client Services Coordinator |
| Suite tenant, mailboxes, and client folders (SYS-03) | SaaS | Productivity suite vendor | Office Manager |
| Desktops (4), laptops (4), MFP (1) (SYS-06) | Endpoint | Office; laptops travel with the preparers | Office Manager (MSP operates) |
| Staff-owned phones with the suite app (7) (SYS-06) | Endpoint (personal) | With staff | Each employee (no device controls today) |
| Firewall, staff Wi-Fi, guest Wi-Fi (SYS-07) | Network | Office network closet | Office Manager (MSP operates) |
| Suite backup subscription (SYS-08) | SaaS | Backup vendor (MSP subcontractor) | Office Manager (MSP operates) |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 44 controls:
- Implemented: 9
- Partially implemented: 25
- Planned: 10
- Not applicable: 0

By responsibility: 18 system-specific (the firm), 23 hybrid (the firm with a vendor or the MSP), 3 common/inherited (fully provided by a SaaS vendor).

### 10.2 Inherited and MSP-provided controls
| Provider | What the firm relies on | Evidence | What the firm must still do |
|---|---|---|---|
| Tax software vendor | Platform security, encryption, backups (CP-9), session timeout (AC-12), audit records (AU-2, AU-11), MFA enforcement, e-file transmission | SOC 2 Type 2 report reviewed 2026-08-12 (P09) | Complementary user entity controls: user provisioning and removal, role assignment, review of user activity, protection of credentials, prompt notice of suspected account compromise |
| Portal vendor | Encryption in transit and at rest (SC-8, SC-28), session timeout, e-signature identity check (IA-8) | Vendor documentation only | Staff account management; require client MFA; deliver returns only through the portal |
| Productivity suite vendor | Platform security, encryption at rest and in transit, lockout, audit logging (AU-2) | Vendor documentation | Account management, MFA settings, forwarding and sharing settings, alerts, log review |
| MSP | Patching (SI-2), antivirus (SI-3), firewall (SC-7), laptop encryption (SC-28), backup operation (CP-9), screen lock (AC-11) | Monthly MSP reports; P07 evidence requests | Oversight: approve changes, review reports monthly, written 7216 notice to technicians, annual MSP review (P01 R-006) |
| Backup service (MSP subcontractor) | Storage of suite copies (CP-9) | None yet; full restore test due 2026-09-30 | Confirm retention, MFA, and subcontractor terms through the MSP |

**Inherited does not mean done.** Two of the tax software vendor's complementary user entity controls are open gaps at the firm: prompt removal of users (AC-2, PS-4) and review of user activity (AU-6).

### 10.3 Control assessment status
Assessed 2026-08-03 to 2026-08-05 by an independent consultant. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
Staff sign in to the tax software and the suite with a password and a second factor (a phone authenticator app). That fits access to customer information at the Moderate category and meets 314.4(c)(5) once number matching is on and the "scanner" mailbox stops using legacy authentication (P01 R-001, R-024). Clients sign in to the portal with their own accounts; MFA is optional today and will be required before the 2027 filing season (R-010). Forms 8879 are signed electronically with the portal's knowledge-based identity check, as Pub. 1345 requires.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness and tax software vendor report review (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **BEC:** business email compromise
- **CTP:** Client Tax Platform
- **EDR:** endpoint detection and response
- **EFIN / PTIN:** Electronic Filing Identification Number / Preparer Tax Identification Number
- **ERO:** Electronic Return Originator
- **MFA:** multi-factor authentication
- **MFP:** multifunction printer-scanner
- **MSP:** managed service provider
- **POA&M:** plan of action and milestones
- **WISP:** written information security plan (the IRS term for the Safeguards Rule's written information security program)

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan | Office Manager (Qualified Individual) |
