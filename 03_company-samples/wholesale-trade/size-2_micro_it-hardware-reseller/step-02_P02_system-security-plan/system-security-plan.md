# System Security Plan: Reseller Operations Platform (ROP)

**Organization:** Cris Santos Company, LLC (IT hardware and software reseller) | **Tier:** Micro | **Vertical:** Wholesale Trade
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Reseller Operations Platform (**ROP**), identifier CSC-SYS-001.

## 2. System Overview
The ROP supports every business process of the company's single Florida office and stockroom: quoting, order entry, purchasing and drop-ship ordering, receiving and setup, shipping, the customer ordering portal, invoicing and supplier payments, and federal order administration. It serves 7 staff and about 85 commercial accounts, plus DoD end users ordering directly or through the Federal Prime.

The company owns almost no infrastructure. Most of the ROP is vendor SaaS, and a managed service provider (MSP) runs the computers and the network. This plan therefore says, for each control, what the company does itself, what the MSP does for it, and what it inherits from a SaaS vendor.

The ROP processes **Federal Contract Information (FCI)**: the equipment lists, asset tag numbers, user and room assignments, and delivery details that DoD customers send for setup orders. It holds **no Controlled Unclassified Information (CUI)** (`../00_company-facts.md` section 1).

**Major components:**
- **SYS-01:** ERP (vendor SaaS): quotes, orders, purchasing, inventory with serial tracking, accounting, and the customer ordering portal
- **SYS-02:** productivity suite (SaaS): email, shared files (including the Orders folder), chat
- **SYS-03:** 8 laptops, 1 setup bench desktop, 2 barcode scanners, 1 label printer (MSP-managed)
- **SYS-04:** office and stockroom network: firewall, staff Wi-Fi, separate guest Wi-Fi, one internet line (MSP-managed)
- **SYS-05:** SaaS-to-SaaS backup of the suite (operated by the MSP)
- **SYS-08:** MSP remote monitoring and management (RMM) tool (supporting component)
- **SYS-09:** stockroom security devices: alarm and 4 IP cameras with a recorder (supporting component; the recorder was replaced on 2026-08-20, see P07)

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies |
|---|---|---|---|
| N42-R04 | FAR Basic Safeguarding of Covered Contractor Information Systems | 48 CFR 52.204-21 | **Applies.** The 19 DoD setup orders carry the clause; the ROP is a covered contractor information system because it processes FCI |
| N42-R02 | CMMC Program | 32 CFR Part 170; DFARS 252.204-7021 | **Applies at Level 1 (Self)** for setup orders since 2026-02: annual self-assessment, results in SPRS, and an annual affirmation (32 CFR 170.15, 170.22) |
| N42-R05 | Section 889 prohibition | 48 CFR 52.204-25; representation 52.204-26 | **Applies** to all 34 DoD orders, and to the company's own use of equipment through its SAM representation |
| Contract clause | Sources of Electronic Parts | DFARS 252.246-7008 | **Applies** to DoD setup orders and Federal Prime orders (not in the N42 register; a DoD contract clause) |
| N42-R03 | DFARS safeguarding of covered defense information | 48 CFR 252.204-7012 | **In the setup orders but not triggered.** No covered defense information is processed, so the ROP is not a covered contractor information system as defined in 252.204-7012(a) |
| N42-R01 | FTC Act Section 5 | 15 U.S.C. 45(a) | Applies to any security claims the company makes to customers (for example in questionnaire answers, P09) |
| State | Florida Information Protection Act | Fla. Stat. 501.171 | Reasonable measures for personal information (employee records, customer contacts) and breach notice |
| Internal | Security policies POL-02, POL-03, POL-04 | P06 | |

Not applicable: SEC disclosure rules (N42-R07; private company), CCPA/CPRA (N42-R08; no California business), CTPAT (N42-R06; not an importer of record). See P03 section 1.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Owner on 2026-08-31.

### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization. The equivalent internal decision: on 2026-08-31 the Owner accepted continued operation of the ROP on two conditions. First, the POA&M items in P07 and the High risks in P01 are treated by their dates. Second, no new DoD setup order is accepted after 2026-10-31 unless a documented CMMC Level 1 self-assessment shows all 15 requirements MET, because no POA&M is allowed at Level 1 (32 CFR 170.21(a)(1)).

### 4.3 System Operational Status
Operational. Planned changes, all due by 2026-12-31: a separate network segment and rebuild for the setup bench (P01 R-011), a restricted FCI folder (R-012), endpoint detection and response (R-006), backup upgrade and restore tests (R-007), and replacement of the covered camera recorder (done 2026-08-20; R-024).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner, risk acceptor, and CMMC Affirming Official | Owner | Overall accountability; accepts risk; approves this plan, policies, and spending; signs SAM representations and the SPRS affirmation |
| Security and compliance lead | Operations Manager | Day-to-day security; maintains this plan, the risk register, and the POA&M; manages the MSP |
| Federal order administration | Federal Account Manager | Clause review and Section 889 checks on DoD orders |
| Supply chain lead | Purchasing and Inventory Coordinator | Supplier list, sourcing order, broker approvals (from 2026-11) |
| IT operations | MSP | Computers, patching, endpoint protection, firewall, Wi-Fi, backup administration |
| Independent assessor | Security consultant | Annual control assessment (P07) |

**Overlapping roles.** At 7 people the Owner approves the work, accepts risk, and affirms compliance, and the Operations Manager both runs and documents most controls. The compensating checks are the independent consultant's assessment (P07), the ERP vendor's SOC 2 report (P09), and government contracts counsel's review of anything filed in SAM or SPRS.

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Goods acquisition and logistics management (DoD equipment lists, delivery details: FCI) | Moderate | Moderate | Low | Disclosure of where and to whom equipment is delivered on an installation harms the customer and breaks FAR 52.204-21; wrong asset or configuration data reaches a DoD network; setup orders tolerate 48 hours (P05 BP-04) |
| Inventory control and customer services (orders, pricing, serials, customer contacts) | Moderate | Moderate | Moderate | Pricing and customer data are commercially sensitive; serial records support counterfeit tracing; order entry has a 24-hour MTD (P05 BP-01) |
| Accounting and payments (supplier bank details, invoices) | Moderate | Moderate | Low | A changed bank detail diverts payments (April 2026); payments tolerate 72 hours (P05 BP-06) |
| **ROP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 7-person reseller. The plan documents 45 controls that carry the FAR 52.204-21 requirements, the Section 889 and sourcing duties, and basic cyber hygiene (see `control-implementation.csv`). All other Moderate-baseline controls are handled one of two ways:
- **Inherited** from the SaaS vendors (physical, platform, and application controls), with the ERP vendor's SOC 2 report as the main evidence (P09).
- **Tailored out** for this tier, where the control addresses federal program management or organizations with dedicated IT staff (for example, configuration change boards and separate development environments). These are recorded as tailoring decisions, not gaps.

## 7. Authorization Boundary Description
- **Inside, and in the CMMC Level 1 assessment scope** (systems that process, store, or transmit FCI, 32 CFR 170.19(b)(1)): the company's ERP tenant and roles (SYS-01), the suite tenant and Orders folder (SYS-02), the 9 computers and scanners (SYS-03), the network (SYS-04), and the backup subscription (SYS-05).
- **Inside, as supporting components:** the MSP's RMM agents and the MSP's access to company systems (SYS-08), and the stockroom alarm and cameras (SYS-09). The cameras do not process FCI, but they sit on the company network and they matter for the Section 889 "use" representation (52.204-26(c)(2)).
- **Outside (external services, interconnected):** the vendors' own platforms, supplier portals (SYS-06), banking and the payment page (SYS-07), the carrier shipping service, the company website, and the ERP vendor's AI subprocessor used by the reorder feature (SYS-10, assessed in P10).

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Agreement |
|---|---|---|---|
| DoD contracting offices and the Federal Prime (email, SYS-02) | Bidirectional | Purchase orders, equipment lists, delivery details (FCI) | Purchase order clauses (52.204-21, 52.204-25, 252.246-7008, 252.204-7021) |
| National distributors and OEM programs (SYS-06) | Outbound orders; inbound pricing and status | Orders; drop-ship addresses limited to ship-to details | Distributor terms; **no flowdown of 52.204-25 or 252.246-7008 (gap)** |
| Brokers (email) | Bidirectional | Quotes, orders, invoices, bank details | None (gap) |
| Bank and payment processor (SYS-07) | Outbound payments | Supplier bank details | Bank agreement |
| MSP RMM platform (SYS-08) | Inbound administrative access | Device management | MSP service contract |
| ERP vendor's AI subprocessor (SYS-10) | Outbound | Order history, including DoD orders | ERP terms; **subprocessor terms not reviewed (gap; P10)** |
| SPRS and SAM | Outbound | Representations, CMMC Level 1 result and affirmation | Federal systems (no FCI sent) |

## 9. System Component Inventory
| Component | Type | Location or provider | Owner |
|---|---|---|---|
| ERP tenant and customer portal (SYS-01) | SaaS | ERP vendor | Operations Manager |
| Suite tenant and Orders folder (SYS-02) | SaaS | Productivity suite vendor | Operations Manager |
| 8 laptops, setup bench desktop, 2 scanners, label printer (SYS-03) | Endpoint | Office and stockroom; laptops travel | Operations Manager (MSP operates) |
| Firewall, staff Wi-Fi, guest Wi-Fi (SYS-04) | Network | Office network closet | Operations Manager (MSP operates) |
| Suite backup subscription (SYS-05) | SaaS | Backup vendor (resold by the MSP) | Operations Manager (MSP operates) |
| RMM agents (SYS-08) | Management agent | All 9 computers | MSP |
| Alarm, 4 cameras, recorder (SYS-09) | Physical security devices | Stockroom | Operations Manager |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 45 controls:
- Implemented: 7
- Partially implemented: 28
- Planned: 10
- Not applicable: 0

By responsibility: 26 system-specific (the company), 18 hybrid (the company with a vendor or the MSP), 1 common/inherited (fully provided by SaaS vendors: SC-8).

### 10.2 Inherited and MSP-provided controls
| Provider | What the company relies on | Evidence | What the company must still do |
|---|---|---|---|
| ERP vendor | Platform security, encryption, backups (CP-9), transport encryption (SC-8), audit records (AU-2) | SOC 2 Type 2 report reviewed 2026-08-20 (P09) | Complementary user entity controls: provisioning and removal, roles, MFA enforcement, review of user access and audit logs |
| Productivity suite vendor | Platform security, encryption at rest and in transit, audit logging | Vendor documentation | Account management, MFA settings, folder permissions, forwarding rules, log review |
| MSP | Patching (SI-2), endpoint protection (SI-3), firewall (SC-7), laptop encryption (SC-28), backup operation (CP-9), screen lock (AC-11) | Monthly MSP reports; P07 evidence requests | Oversight: approve exceptions, review reports monthly, annual MSP security review (P01 R-010) |
| Backup service (resold by the MSP) | Storage of suite copies (CP-9) | None yet; restore test due 2026-09-30 | Confirm terms and MFA through the MSP |

**Inherited does not mean done.** Two of the ERP vendor's complementary user entity controls are open gaps at the company: account removal (AC-2, PS-4) and log review (AU-6).

### 10.3 Control assessment status
Assessed 2026-08-10 to 2026-08-12 by an independent consultant. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
Staff sign in to the ERP and the suite with a password and a second factor (a phone authenticator app). This is appropriate for FCI at the Moderate category. The gaps are shared supplier portal and carrier logins and MSP-held administrator logins without MFA (P07 POAM-002, POAM-003). Customer portal users sign in with a password; MFA for customer users is optional in the ERP and is a planned improvement (P09).

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness and ERP vendor report review (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **C-SCRM:** cybersecurity supply chain risk management
- **CMMC:** Cybersecurity Maturity Model Certification
- **CUI:** Controlled Unclassified Information
- **FCI:** Federal Contract Information
- **MFA:** multi-factor authentication
- **MSP:** managed service provider
- **RMM:** remote monitoring and management
- **ROP:** Reseller Operations Platform
- **SPRS:** Supplier Performance Risk System
- **POA&M:** plan of action and milestones

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan | Operations Manager |
