# System Security Plan: Core Brokerage SaaS Stack (CBSS)

**Organization:** Cris Santos Company, LLC (freight forwarding and customs brokerage office) | **Tier:** Micro | **Vertical:** Transportation and Warehousing
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Core Brokerage SaaS Stack (**CBSS**), identifier CSC-SYS-001.

## 2. System Overview
The CBSS supports every business process of the company's single Florida office: import entries and cargo release, Importer Security Filings (ISF), export EEI filings, ocean forwarding, duty and freight payments, client communication, and customs records management. It serves 7 employees and about 180 active clients (about 4,500 entries and 1,200 export shipments a year).

The company owns almost no infrastructure. Most of the CBSS is SaaS, and a managed service provider (MSP) runs the office computers, the network, and the suite backup. This plan therefore says, for each control, what the company does itself, what the MSP does for it, and what it inherits from a SaaS vendor.

**Major components:**
- **SYS-01:** customs brokerage and forwarding platform (vendor SaaS): entries, ISF, EEI, client and POA files, shipment documents, AI document capture and classification suggestions
- **SYS-02:** productivity suite (SaaS): email, calendar, chat, and the Client Records Archive in the shared drive
- **SYS-03:** accounting SaaS
- **SYS-04:** business online banking (ACH and wires)
- **SYS-06:** 6 desktops, 3 laptops, 1 multifunction printer-scanner (MSP-managed); personal phones used for MFA and email
- **SYS-07:** office network: firewall, staff Wi-Fi, separate guest Wi-Fi (MSP-managed)
- **SYS-08:** cloud backup of the productivity suite (SaaS, operated by the MSP)
- **SYS-10:** paper records in locked cabinets

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| CBP-111 | Customs broker duties: records, confidentiality, breach notice to CBP within 72 hours, supervision, employee lists, continuing education | 19 CFR Part 111, Subparts A, C, F (primary regulation for P03) |
| CBP-163 | Recordkeeping and alternative storage methods | 19 CFR 163.5 (brought in by 111.21(c) and 111.23(a)) |
| FMC | Ocean freight forwarder records, 5 years | 46 CFR 515.33 |
| EEI | Export records, 5 years | 15 CFR 30.10(a) |
| N48-49-R05 | CTPAT minimum security criteria (voluntary; reach the company through CTPAT importer clients' questionnaires) | CBP program |
| State | Florida Information Protection Act (reasonable security, disposal, breach notice) | Fla. Stat. 501.171 |
| Federal | FTC Act Section 5 (unfair or deceptive practices, including unreasonable data security) | 15 U.S.C. 45(a) |
| Internal | Security policies POL-02, POL-03, POL-04 | P06 |

Not applicable (reasons in P03): the USCG maritime cyber rule (N48-49-R01, 33 CFR Part 101 Subpart F), because the company has no facility or vessel security plan; TSA directives (N48-49-R02 to R04); the TSA indirect air carrier rule (49 CFR Part 1548), because the company tenders no air cargo; CMMC (N48-49-R07); SEC rules (N48-49-R08).

The `regulatory_driver` column in `control-implementation.csv` cites the 19 CFR and Florida sections directly, because the vertical requirement list has no customs broker entry (see `../00_company-facts.md` section 1).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the owner on 2026-08-31.

### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization. The equivalent internal decision: on 2026-08-31 the owner accepted continued operation of the CBSS, on the condition that the POA&M items in P07 are completed by their dates and the High risks in P01 are treated by 2026-12-31.

### 4.3 System Operational Status
Operational. Planned changes: payment call-back and dual approval (P01 R-001), removal of the shared entries@ account (R-003), first backup restore test (R-006), suite alerts and EDR (R-002), and a cellular failover router (R-008), all due by 2026-12-31.

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner and risk acceptor | Owner and President (licensed customs broker) | Overall accountability; accepts Moderate and higher risk; approves this plan, policies, and spending; responsible supervision and control (111.28(a)) |
| Security Coordinator and recordkeeping contact | Office and Compliance Manager | Day-to-day security; maintains this plan, the risk register, the inventory, and vendor records; brokerage-wide recordkeeping (111.21(d)) |
| Customs operations lead | Licensed Customs Broker (Entry Supervisor) | Entry review; business owner of AI-001 (P10) |
| Payments | Accounting Specialist | Wires, ACH, accounting SaaS |
| IT operations | MSP | Devices, patching, antivirus, firewall, Wi-Fi, suite administration on request, backup |
| Independent assessor | Information security consultant | Annual control assessment (P07) |

The Office and Compliance Manager both runs and checks most controls. The independent assessor and the MSP's monthly reports are the outside check.

## 6. System Information Types and System Categorization
Information types follow the NIST SP 800-60 Vol. 2 Rev. 1 approach, described in the company's own terms. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Client customs and trade records (importer identification numbers, including Social Security numbers for individual importers; entries; invoices; POAs) | Moderate | Moderate | Moderate | Disclosure breaks 111.24 confidentiality, triggers the 72-hour CBP notice and Florida breach duties; wrong data causes wrong duty payments; entries must flow within one business day (P05 MTD 8 h) |
| Payments and financial records (bank details, wires, duty payments) | Moderate | Moderate | Moderate | A changed bank detail diverts client money; payments must reach CBP and carriers on time (P05 MTD 24 h) |
| Human resources (employee data, including the Social Security numbers sent to CBP under 111.28(b)) | Moderate | Low | Low | Personal information under Fla. Stat. 501.171 |
| **CBSS category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 7-person office. The plan documents 45 controls that carry the customs broker duties and basic cyber hygiene (see `control-implementation.csv`). All other Moderate-baseline controls are handled one of two ways:
- **Inherited** from the SaaS vendors (physical, platform, and application controls), with the customs platform vendor's SOC 2 report as the main evidence (P09).
- **Tailored out** for this tier, where the control addresses federal program management or organizations with dedicated IT staff (for example, configuration change boards and separate development environments). These are recorded as tailoring decisions, not gaps.

## 7. Authorization Boundary Description
- **Inside:** the company's customs platform tenant configuration and user roles (SYS-01), the suite tenant and Client Records Archive (SYS-02), the accounting tenant (SYS-03), the company's bank portal users and limits (SYS-04), 9 computers and the printer (SYS-06), the office network (SYS-07), the backup subscription (SYS-08), and paper records (SYS-10).
- **Outside (interconnected):** the vendors' own platforms and data centers; CBP's ACE and eCBP portals (SYS-05); ocean carrier and terminal portals (SYS-09); the MSP's remote management platform; overseas agents' and clients' systems; staff personal phones (in scope only for the suite app rules in AC-19).

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Agreement |
|---|---|---|---|
| CBP (through SYS-01's Automated Broker Interface connection) | Bidirectional | Entries, ISF, release and hold messages | Platform vendor's CBP certification; company's filer code |
| CBP ACE and eCBP portals (SYS-05) | Bidirectional | Statements, broker submissions, employee lists | CBP terms of use |
| Export filing system (through SYS-01) | Outbound | EEI | Exporter authorizations on file |
| Overseas agents | Bidirectional | Shipment documents, ISF data, invoices for freight | Agency agreements (no security terms); **consumer messaging app in use (gap)** |
| Ocean carriers and terminals (SYS-09) | Bidirectional | Bookings, container status, freight invoices | Carrier web terms; **shared logins (gap)** |
| Clients | Bidirectional | POAs, invoices, CBP Form 5106 data, entry copies | Client terms and POA; **no written authorization to use service providers (gap, 111.24)** |
| Bank (SYS-04) | Outbound | Wires and ACH | Commercial account agreement |
| MSP remote management platform | Inbound administrative access | Device management | MSP service contract (no security terms) |
| CTPAT importer clients | Outbound | Questionnaire answers (no client data) | None needed |

## 9. System Component Inventory
| Component | Type | Location or provider | Owner |
|---|---|---|---|
| Customs platform tenant (SYS-01) | SaaS | Customs platform vendor (U.S. hosting per contract) | Entry Supervisor (business); Office and Compliance Manager (accounts) |
| Productivity suite tenant and Client Records Archive (SYS-02) | SaaS | Productivity suite vendor | Office and Compliance Manager |
| Accounting tenant (SYS-03) | SaaS | Accounting SaaS vendor | Accounting Specialist |
| Bank portal (SYS-04) | Bank service | Company's bank | Owner |
| Desktops (6), laptops (3), printer (SYS-06) | Endpoint | Office; laptops travel with the owner, the Entry Supervisor, and the Office and Compliance Manager | Office and Compliance Manager (MSP operates) |
| Firewall, staff Wi-Fi, guest Wi-Fi (SYS-07) | Network | Locked office closet | Office and Compliance Manager (MSP operates) |
| Suite backup subscription (SYS-08) | SaaS | Backup service (MSP subcontractor) | Office and Compliance Manager (MSP operates) |
| Paper records (SYS-10) | Physical | Locked cabinets | Office and Compliance Manager |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 45 controls:
- Implemented: 14
- Partially implemented: 23
- Planned: 8
- Not applicable: 0

By responsibility: 20 system-specific (the company), 20 hybrid (the company with a vendor or the MSP), 5 common/inherited (fully provided by a SaaS vendor, the bank, or the MSP).

### 10.2 Inherited and MSP-provided controls
| Provider | What the company relies on | Evidence | What the company must still do |
|---|---|---|---|
| Customs platform vendor | Platform security, encryption, backups (CP-9), session timeout (AC-12), lockout (AC-7), audit records (AU-2, AU-11) | SOC 2 Type 2 report reviewed 2026-08-25 (P09) | Complementary user entity controls: user provisioning and removal, role assignment, MFA enforcement, review of user access and audit reports, control of who receives exported data |
| Productivity suite vendor | Platform security, encryption at rest and in transit (SC-8, SC-28), lockout (AC-7), spam filtering (SI-8), audit logging (AU-2) | Vendor documentation | Account management, MFA settings, forwarding and sharing settings, impersonation protection, log review, retention |
| Bank | Portal MFA and lockout; wire limits | Account agreement | Dual approval and call-back for changed instructions (AC-5) |
| MSP | Patching (SI-2), antivirus (SI-3), firewall and Wi-Fi (SC-7, AC-18), encryption (SC-28), screen lock (AC-11), backup operation (CP-9) | Monthly MSP reports; P07 evidence requests | Oversight: approve exceptions, review reports monthly, annual MSP security review (P01 R-014) |
| Backup service (MSP subcontractor) | Storage of mail and file copies (CP-9) | None yet; restore test due 2026-09-30 | Confirm data region and subcontract terms through the MSP |

**Inherited does not mean done.** Two of the platform vendor's complementary user entity controls are open gaps at the company: account removal (AC-2, PS-4) and access and audit report review (AU-6).

### 10.3 Control assessment status
Assessed 2026-08-10 to 2026-08-12 by an independent consultant. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
Employees sign in to the customs platform, the suite, the accounting SaaS, and the bank with a password and a second factor (an authenticator app on their phone; bank codes for the bank portal). This is appropriate for the Moderate category. Two exceptions remain: the shared entries@ account (no MFA) and the shared carrier portal logins (no MFA offered by most carriers). Both are being replaced with named accounts (P01 R-003, R-009). CBP portal identities (SYS-05) are governed by CBP.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness and platform vendor report review (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **ACE:** Automated Commercial Environment (CBP)
- **BEC:** business email compromise
- **CBSS:** Core Brokerage SaaS Stack
- **EDR:** endpoint detection and response
- **EEI:** Electronic Export Information
- **ISF:** Importer Security Filing
- **MFA:** multi-factor authentication
- **MSP:** managed service provider
- **POA:** customs power of attorney
- **POA&M:** plan of action and milestones

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan | Office and Compliance Manager (Security Coordinator) |
