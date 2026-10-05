# System Security Plan: Project Delivery and Payment Platform (PDPP)

**Organization:** Cris Santos Company Holdings, Inc. (corporate shared services, serving the Construction, Property, and A&E divisions) | **Tier:** Multi-Sector | **Vertical:** Construction
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-15

> **Why this system.** At this tier the SSP can cover one system per division or a shared corporate system. The group chose the **PDPP**, a shared corporate system, because all three divisions use it (A&E issues design-build revisions in it, Construction runs projects and pay applications in it, and Property approves tenant improvement work and intercompany pay applications in it), it moves about $1.18 billion of billings a month, it is the group's CMMC Level 1 assessment scope, and it carries two of the group's top risks: payment fraud (P01 GR-02) and CUI landing where it must not be (P01 GR-01). The CUI enclave (SYS-G6) keeps its own SSP, as NIST SP 800-171 R2 requirement 3.12.4 and 32 CFR 170.19(c) require; it is assessed in P03 and P07.

## 1. System Name and Identifier
Project Delivery and Payment Platform (**PDPP**), identifier CSCH-PDPP-01. A shared corporate system owned by corporate shared services. See `../00_company-facts.md` section 3.

## 2. System Overview
The PDPP is the system of record for project delivery and the front end of the billing cycle. It supports:
- **Construction:** drawings, RFIs, submittals, change events, daily logs, subcontractor bid packages, and monthly pay applications with schedules of values and lien waivers for about 1,350 active projects.
- **A&E:** design-build design revisions and responses to RFIs on commercial work. Federal CUI design work stays in the enclave.
- **Property:** owner-side approvals of tenant improvement and capital projects, including intercompany pay applications from Construction.

About 21,000 workforce users and 46,000 external users (owners, subcontractors, design consultants) use it.

**Major components:**
- **Project management SaaS tenant** (commercial vendor service; not FedRAMP authorized): documents, workflows, pay application module, subcontractor and owner portals
- **Integration services** on the group cloud platform (provider A): an integration hub that moves pay application and change data to SYS-G4, a document conversion service, and an API gateway
- **Payment-instruction service**: publishes the group's verified remittance details from SYS-G4 to pay application cover sheets (partly built; see SI-10)
- **Nightly independent export** of all project records to group cloud storage, with backups in the provider B vault
- **E-signature service** for pay applications and lien waivers (SaaS)

The platform is described by service category and is vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies to the PDPP |
|---|---|---|---|
| N23-R01 | FAR Basic Safeguarding | 48 CFR 52.204-21 | The PDPP processes FCI for 212 federal contracts. All 15 requirements apply |
| N23-R04 | CMMC Program and DFARS CMMC clause | 32 CFR Part 170; DFARS 252.204-7021 | The PDPP is the CMMC Level 1 (Self) assessment scope (Final status date 2026-01-20; annual affirmation due 2027-01-20). Under 252.204-7021(d)(2), FCI may be processed only on systems with the required status |
| N23-R03 | DFARS Safeguarding Covered Defense Information | 48 CFR 252.204-7012 | **The PDPP must not hold CUI.** It is not FedRAMP Moderate authorized or equivalent (252.204-7012(b)(2)(ii)(D)). The 2026-07-14 scan found 1,140 CUI-marked files in it (scenario gap 1) |
| N23-R02 | Section 889 | 48 CFR 52.204-25 | Not a direct PDPP requirement; submittal screening for installed equipment runs in the PDPP workflow (P03) |
| FAR 52.232-33 | Payment by EFT, System for Award Management | 48 CFR 52.232-33 | Remittance details on federal pay applications must match SAM; the PDPP must not let anyone redirect payments |
| N53-R05 | SEC cybersecurity disclosure | Reg S-K Item 106; Form 8-K Item 1.05 | A PDPP incident (for example a large payment diversion) goes to the disclosure committee (P08) |
| State law | State breach notification laws | Each state where affected individuals reside (Florida: Fla. Stat. 501.171) | The PDPP holds little personal information, but subcontractor certified payrolls sometimes get uploaded (P08) |
| Contracts | Owner prime contracts; subcontracts; SaaS vendor contract | Contract terms | Owner confidentiality and notice terms; flowdowns of FAR 52.204-21(c) and DFARS 252.204-7012(m) |
| Internal | Group policies POL-01 to POL-05 and division supplements | P06 | |

Not applicable: HIPAA (no PHI); PCI DSS (no card data in the PDPP; parking card payments are in SYS-D4); FedRAMP (the group does not operate a federal information system for an agency).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Group CISO and the Group project delivery platform director (system owner) on 2026-09-15, after the board risk committee review.

### 4.2 System Authorization Decision
The group is not a federal agency, so there is no federal authorization. The internal decision:
- **Decision:** authorized to operate with conditions, 2026-09-15, by the Group CISO and the Group Chief Risk Officer (acceptance authority for High risks).
- **Conditions:** (1) block uploads of files carrying CUI markings and purge the 1,140 files found, with each removal recorded, by 2026-11-30 (POAM-006); (2) route all design-build CUI drawings to the field through the enclave gateway, with no workaround (POAM-011); (3) validate the pay application remittance block against verified SYS-G4 bank data by 2026-12-31 (POAM-009 and P01 GR-02); (4) MFA mandatory for owner approvers and subcontractor administrators by 2027-03-31 (POAM-008).
- **Reauthorization:** annually, aligned with the CMMC Level 1 annual affirmation.

### 4.3 System Operational Status
Operational. **Major modification planned:** CUI upload blocking and the payment-instruction service (validated remittance block), both due by 2026-12-31.

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Group project delivery platform director | Accountable for the PDPP and this SSP |
| Authorizing official equivalent | Group CISO with the Group Chief Risk Officer | Authorization decision; High risk acceptance |
| Business owner, Construction | Construction VP of project controls | Project roles, pay application workflow |
| Business owner, Property | Property VP of development and construction | Owner-side approvals |
| Business owner, A&E | A&E chief operating officer | Design-build design collaboration |
| Payment-instruction owner | Group Treasurer | Verified remittance data from SYS-G4 |
| CMMC Level 1 scope owner | Director of Federal Contracts Compliance | Level 1 self-assessment and SPRS entries; supports the Construction division president as Affirming Official |
| Common control providers | Group identity director (SYS-G1), Group SOC director (SYS-G2), Group cloud and network director (SYS-G3), Group Treasurer (SYS-G4), Group IT operations director (SYS-G5) | Operate inherited controls (`common-control-catalog.csv`) |
| Independent assessor | Group internal audit | Assesses common controls once and samples system and division controls (P07) |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Project documents and federal contract information | Moderate | Moderate | Moderate | FCI under FAR 52.204-21; owners' facility details; disclosure would cause serious but not severe harm. Availability Moderate per the 8-hour MTD for document control (P05 BP-C01), met by offline field copies |
| Payments (pay applications, remittance details) | Moderate | **Moderate** | Moderate | A corrupted remittance instruction can divert a payment of up to about $6 million. Serious for the group, not severe for an $18 billion company. Integrity controls are set at the top of Moderate (SI-10, AC-5, SI-7) |
| Contract and acquisition information (subcontract packages, bids) | Moderate | Moderate | Low | Subcontractor pricing is confidential; bids can be resubmitted |
| Information security (keys, access policies, logs) | Moderate | Moderate | Moderate | Compromise would expose all projects |
| **PDPP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | Overall **Moderate** |

**CUI is not an information type of this system.** CUI requires the NIST SP 800-171 R2 environment of SYS-G6. Its presence in the PDPP is treated as a spill (section 10.1), not as a reason to raise the PDPP's categorization.

**Baseline:** the NIST SP 800-53B **Moderate** baseline, tailored. The plan documents **166 controls** in `control-implementation.csv`:
- 163 from the Moderate baseline;
- 1 from the privacy baseline (PM-9), for the group risk management strategy;
- 2 program management controls not in any baseline (PM-1, PM-2).

The other Moderate-baseline controls are either fully inherited from the cloud providers and the SaaS vendor (for example most PE and MP controls, evidenced by their SOC 2 Type 2 reports) or tailored out with a reason in the group tailoring register (for example, wireless and media controls for a system with no group-owned wireless or media). Where NIST's CSF 2.0 to SP 800-53 crosswalk lists no CSF subcategory for a control (for example AC-8, AC-21, PS-3, MA-4), the `csf2_subcategories` value is an author mapping.

## 7. Authorization Boundary Description
- **Inside:** the project management SaaS tenant (configuration, roles, and data the group controls), the integration and payment-instruction services and the API gateway in the PDPP accounts on provider A, the nightly export and its backups in the provider B vault, and the e-signature service account.
- **Outside, inherited (common control providers):** SYS-G1 identity, SYS-G2 SOC, SYS-G3 landing zone and network, SYS-G4 ERP and payment factory, SYS-G5 email.
- **Outside, interconnected:** SYS-G4 (billing and payments), the estimating database, SYS-D6 (AI estimating assistant, read-only connector to cost history only), and the CUI enclave gateway (one-way notices only; no CUI may flow into the PDPP).
- **Outside, used by external users:** owners', subcontractors', and design consultants' own devices and identity providers.

The diagram is in P04 `cloud-architecture.md` (section 2.2).

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| SYS-G4 ERP and payment factory | Bidirectional (hourly) | Pay application totals, change orders, cost codes; verified remittance details (outbound from SYS-G4) | Interface catalog; group data owner approval |
| Owners (external) | Bidirectional | Pay applications, lien waivers, approvals | Prime contracts; terms of use. **Gap:** many owners have not been told the group's remittance verification procedure (scenario gap 3) |
| Subcontractors and suppliers (external) | Bidirectional | Bid packages, submittals, pay requests, lien waivers | Subcontracts with FAR 52.204-21(c) flowdown on federal work |
| A&E design teams | Bidirectional | Design revisions and RFI responses on commercial and non-CUI work | Intercompany agreement |
| Property (owner role) | Bidirectional | Tenant improvement and capital project approvals; intercompany pay applications | Intercompany agreement |
| SYS-G6 CUI enclave | **None permitted for CUI.** Gateway sends notices only | Notice that a drawing revision exists in the enclave | Enclave SSP. **Gap:** field teams copy CUI drawings out of the enclave into the PDPP (POAM-011) |
| Estimating database and SYS-D6 | Outbound (cost history, read-only) | Historical costs | P10 conditions |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| Project management SaaS tenant | SaaS | Vendor (multi-region, US) | Group project delivery platform director |
| Integration hub and document conversion | PaaS (managed containers and functions) | Provider A | Group project delivery platform director |
| Payment-instruction service | PaaS | Provider A | Group Treasurer (data); platform director (operation) |
| API gateway | PaaS | Provider A | Group cloud and network director |
| Nightly export store | Object storage | Provider A, backups in provider B vault | Group project delivery platform director |
| E-signature service account | SaaS | Vendor | Construction VP of project controls |
| Key management | PaaS (customer-managed keys) | Provider A | Group cloud and network director |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv` (166 controls) and `common-control-catalog.csv` (142 group common controls).

| Status | Controls |
|---|---|
| Implemented | 148 |
| Partially implemented | 18 |
| Planned | 0 |
| Not applicable | 0 |
| **Total** | **166** |

| Inheritance | Controls |
|---|---|
| Common/Inherited (from SYS-G1 to SYS-G5, group functions, the cloud providers, or the SaaS vendor) | 113 |
| Hybrid (group provides the mechanism; the PDPP configures or operates part) | 31 |
| System-specific | 22 |

**The 18 partially implemented controls** cluster in four places:
- **CUI in the wrong system** (scenario gap 1): AC-4, AC-21, CM-8, CM-12, SI-4, AT-3.
- **External user lifecycle and authentication:** AC-2, AC-2(3), IA-8, PS-7, SA-9 (the SaaS vendor's complementary user entity controls).
- **Payment-instruction integrity** (scenario gap 3): AC-5, SI-10, AU-6.
- **Cross-division incident handling and recovery** (scenario gap 7): IR-3, IR-6, IR-8, CP-4.

**The CUI spill, in short.** The scan on 2026-07-14 found 1,140 CUI-marked files from 9 DoD projects. The group treated the spill as a cyber incident under DFARS 252.204-7012 and reported it on 2026-07-16 (within 72 hours of discovery). The files were restricted to project administrators the same day and are being purged under POAM-006. Until then the PDPP is a CUI asset in fact, which affects the CMMC Level 2 scope for the enclave (P03).

### 10.2 Common control inheritance by division
The common control catalog lists 142 controls provided by corporate. Inheritance is **documented for Construction** (2025 inheritance matrix, used for the CMMC Level 1 scope), **for A&E** (2026 inheritance matrix), and **for the PDPP** (this plan). The CUI enclave inherits governance, HR, and SOC monitoring only; it provides its own identity, network, and email inside its FedRAMP Moderate authorized boundary. Inheritance is **not documented for Property** (scenario gap 4). Until POAM-021 closes, Property cannot show which group controls protect its building systems and property accounting, and P07 found 4 CA-2 determination statements other than satisfied for this reason. Property also does not inherit the payment factory's bank-change controls, because its accounts payable runs on SYS-D3 (scenario gap 3).

### 10.3 Control assessment status
Common controls were assessed once, and PDPP, enclave, and division controls sampled, from 2026-07-06 to 2026-08-28 by group internal audit. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
- **Workforce users** authenticate through SYS-G1 single sign-on with MFA. Project executives, project accountants, finance staff, and administrators use phishing-resistant authenticators because they can change or approve payment data. Others use number-matching MFA.
- **External users** authenticate with PDPP-local accounts or federation from their own company. MFA is optional today; 61% of external users have not enrolled (IA-8). Owner approvers and subcontractor administrators will be required to use MFA by 2027-03-31 (POAM-008).
- **Changing remittance details** requires step-up re-authentication (IA-11) and, once POAM-009 closes, can only select a bank account already verified in SYS-G4.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), group and division risk registers (P01), gap analyses and regulation-by-division matrix (P03), cloud architecture and control map (P04), BIA (P05), group policies and division supplements (P06), assessment and POA&M (P07), incident response runbook and notification matrix (P08), SOC 2 readiness (P09), AI governance (P10). The CUI enclave SSP (v2.3, under revision; POAM-016) is a separate document.

## 13. Acronym List and Glossary
- **CUI:** controlled unclassified information
- **Common control:** a control provided once by corporate and inherited by several systems
- **FCI:** federal contract information (FAR 52.204-21(a))
- **Pay application:** a contractor's monthly request for payment, with a schedule of values and lien waivers
- **PDPP:** Project Delivery and Payment Platform
- **Remittance block:** the bank details printed on a pay application or invoice that tell the payer where to send money
- **SPRS:** Supplier Performance Risk System
- **TSSI:** Technology and Security Systems Integration unit (Construction)

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-08-28 | Draft after P07 fieldwork | Group project delivery platform director |
| 1.0 | 2026-09-15 | Approved with authorization conditions | Group CISO |
