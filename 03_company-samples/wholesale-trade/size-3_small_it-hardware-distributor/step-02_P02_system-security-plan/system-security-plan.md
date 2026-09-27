# System Security Plan: Order-to-Fulfillment Platform (OFP)

**Organization:** Cris Santos Company, LLC (IT hardware and software wholesale distributor) | **Tier:** Small | **Vertical:** Wholesale Trade
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Order-to-Fulfillment Platform (**OFP**), identifier CSC-SYS-001.

## 2. System Overview
The OFP supports every step from order to shipment: order capture from resellers and DoD primes, purchasing, receiving, warehouse fulfillment, the reseller ordering portal, invoicing, and the configuration lab work done for Prime B. It serves 62 employees, about 1,100 reseller portal users, and an MSP.

The OFP is also the company's **CMMC Level 2 assessment scope** under 32 CFR 170.19(c). It holds the Controlled Unclassified Information (CUI) that Prime B provides (network drawings, IP addressing plans, and device configuration templates for DoD installations) and the Federal Contract Information (FCI) in DoD orders.

**Major components:**
- **SYS-01:** a SaaS ERP for order management, purchasing, inventory, and finance
- **SYS-02:** a warehouse management system (WMS) on company-managed servers in the cloud tenant, with 40 handheld scanners
- **SYS-03:** a SaaS reseller ordering portal
- **SYS-05:** an identity provider for single sign-on and MFA
- **SYS-07:** a public-cloud tenant (IaaS) hosting the WMS servers, the file server (including the CUI share), and the backup vault
- **SYS-08:** the office, warehouse, and lab network
- **SYS-09:** endpoints, including 6 lab workstations
- **SYS-10:** the configuration lab cage (badge-controlled)
- **SYS-13:** the MSP's remote monitoring and management (RMM) tool

The cloud tenant is described by service category and is vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| N42-R03 | DFARS Safeguarding Covered Defense Information and Cyber Incident Reporting | 48 CFR 252.204-7012 (Prime B subcontract) |
| N42-R02 | CMMC Program: Level 2 (C3PAO) required for the Prime B option period from 2027-04-01; Level 1 (Self) for Prime A and Prime C | 32 CFR Part 170; DFARS 252.204-7021 |
| N42-R04 | FAR Basic Safeguarding of Covered Contractor Information Systems (FCI) | 48 CFR 52.204-21 |
| N42-R05 | Section 889 covered telecommunications and video surveillance prohibition | 48 CFR 52.204-25 |
| DFARS | Sources of Electronic Parts (Prime B subcontract) | 48 CFR 252.246-7008 |
| DFARS | NIST SP 800-171 DoD Assessment requirements (SPRS) | 48 CFR 252.204-7019 and 252.204-7020 |
| CUI | CUI Basic is categorized at no less than moderate confidentiality | 32 CFR 2002.14(g) |
| N42-R01 | FTC Act Section 5 (reasonable security for personal information) | 15 U.S.C. 45(a) |
| State | Florida Information Protection Act (breach notification for employee and reseller-contact personal information) | Fla. Stat. 501.171 |
| Internal | Security policies POL-01 to POL-05 | P06 |

Not applicable:
- SEC cybersecurity disclosure (N42-R07): the company is privately held.
- CCPA/CPRA (N42-R08): no California customers, suppliers, or operations (counsel confirmed 2026-06).
- CTPAT (N42-R06): voluntary, and the company is not an importer of record.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Chief Operating Officer (system owner) on 2026-08-31.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- The Chief Operating Officer accepted operation of the OFP on 2026-08-31, with the conditions in the P07 POA&M.
- The Chief Executive Officer accepted the High risks in P01, with dated treatment plans, and approved the $118,000 budget.
- The Chief Executive Officer, as CMMC Affirming Official (32 CFR 170.22), will not affirm Level 2 compliance until the P03 gaps that cannot be placed on a CMMC POA&M are closed.
### 4.3 System Operational Status
Operational. Major modifications planned:
- **CUI enclave project** (restricted CUI share for 9 named users, lab VLAN with deny-by-default rules, hardened lab workstations with USB control), due 2026-12-15.
- **Backup redesign** (separate account, immutable retention), due 2026-12-31.
- **Handheld replacement** (supported operating system, named sign-in through the identity provider), due 2027-01-31.

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Chief Operating Officer | Overall accountability; risk acceptance up to Moderate; signs policies |
| Risk acceptor (authorizing official equivalent) and CMMC Affirming Official | Chief Executive Officer | Acceptance of High and Very High risks; SPRS and CMMC affirmations |
| Security lead | IT Manager | Maintains this SSP, the risk register, and the POA&M; runs the security program part-time |
| System administration | Systems Administrator | ERP, WMS, identity provider, file server, and endpoints |
| CUI custodian | Configuration Lab Lead | Day-to-day handling of CUI in the lab |
| Contract compliance | Government Contracts Manager | Flowdown clauses, SPRS entries, Section 889 reports, DIBNet reports |
| Supply chain risk lead | Purchasing and Supplier Manager | Approved supplier list, supplier vetting, C-SCRM plan |
| Operations support | Managed service provider (External Service Provider, 32 CFR 170.19(c)(2)) | After-hours help desk, server patching, backup monitoring |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| CUI configuration documents (Prime B network drawings, IP plans, configuration templates) | Moderate | Moderate | Low | 32 CFR 2002.14(g) sets confidentiality at no less than moderate; altered configurations could harm DoD networks; Prime B jobs tolerate days of delay (P05 MTD 72 h) |
| Goods acquisition, inventory control, and logistics (orders, purchase orders, inventory, shipments, FCI) | Moderate | Moderate | Moderate | Pricing and DoD order data are sensitive; wrong inventory or ship-to data sends the wrong product; one shipping day is the MTD (P05) |
| Financial management (invoices, supplier bank details) | Moderate | Moderate | Low | Bank-detail changes are a fraud target (near miss 2026-05-12); payments tolerate a few days (P05 MTD 72 h) |
| Human resources (workforce identities) | Moderate | Low | Low | Personal information of 62 employees |
| **OFP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 62-person distributor. The plan documents the 96 controls that implement the 110 NIST SP 800-171 Rev. 2 requirements, the 15 FAR 52.204-21 requirements, and supply chain risk management (SR family, applied with NIST SP 800-161 Rev. 1). See `control-implementation.csv`. Every other Moderate-baseline control is treated as follows:
- **Inherited** from the SaaS and cloud providers, as evidenced by their SOC 2 reports or FedRAMP authorization (P04, P09).
- **Out of scope for this tier**, recorded as a tailoring decision, where the control's purpose applies only to federal systems. Examples: PM-series program-level controls beyond PM-9 and PM-30.

**How the SR controls are applied.** SP 800-53 writes the SR controls for the components of an organization's own systems. The company applies them to OFP components and, as an author decision, also to the products it distributes to DoD customers, because those products become components of DoD systems.

## 7. Authorization Boundary Description
The boundary is the CMMC Level 2 assessment scope. Asset categories follow 32 CFR 170.19(c).

| Asset category | Assets |
|---|---|
| CUI Assets | SYS-01 ERP (CUI found in 14 order attachments, to be purged), SYS-07 file server CUI share, SYS-08 network, SYS-09 lab workstations and laptops |
| Security Protection Assets | SYS-05 identity provider, SYS-10 lab cage badge system, SYS-13 MSP RMM tool (External Service Provider) |
| Contractor Risk Managed Assets | SYS-02 WMS and handhelds (FCI only; prevented from holding CUI by policy and configuration) |
| Out of scope for CUI, in scope for this plan | SYS-03 reseller portal, if the ERP sync excludes DoD orders (to be confirmed by 2026-10-31) |

- **Inside:** the ERP tenant configuration and roles, the WMS servers and handhelds, the portal configuration, the identity provider tenant, the cloud tenant (WMS servers, file server, backup vault), the office, warehouse, and lab network, 58 laptops and desktops, 6 lab workstations, 12 label and shipping printers, the lab cage, and the RMM agents.
- **Outside (external services, interconnected):** the ERP, portal, and cloud providers' platforms; the EDI network (SYS-04); the productivity suite (SYS-06); the shipping label service (SYS-11); the forecasting add-on (SYS-12); primes, suppliers, and carriers.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Prime B | Inbound CUI documents by the prime's secure file share; outbound configured equipment | CUI configuration documents | Subcontract with DFARS 252.204-7012, 252.246-7008, FAR 52.204-25 |
| Prime A and Prime C (through SYS-04 EDI) | Bidirectional | Purchase orders, ship notices, invoices (FCI) | Subcontract purchase orders with FAR 52.204-21, 52.204-25, DFARS 252.204-7021 |
| 22 suppliers and 18 resellers (SYS-04 EDI) | Bidirectional | Purchase orders, ship notices, invoices | EDI trading partner agreements |
| Reseller portal (SYS-03) | Bidirectional sync with the ERP | Catalog, pricing, orders, invoices | Portal vendor contract; SOC 2 Type 2 (P09) |
| Forecasting add-on (SYS-12) | Outbound order history; inbound suggested purchase orders | Order history, **including DoD orders (FCI)** | Vendor terms only; **no FCI safeguarding terms (gap)** |
| Shipping label service (SYS-11) | Outbound | Ship-to addresses (FCI for DoD orders) | Vendor terms |
| MSP (SYS-13) | Bidirectional administrative access | Security Protection Data | MSP contract; **no customer responsibility matrix (gap)** |
| Bank | Outbound | Supplier payments | Bank agreement; call-back verification not yet required (gap) |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| ERP tenant | SaaS | ERP vendor (SOC 2 Type 2; no FedRAMP authorization) | Chief Operating Officer |
| WMS application and database servers (2) | Cloud virtual machines | Cloud tenant | Systems Administrator |
| File server with general shares and the CUI share | Cloud virtual machine and storage | Cloud tenant (FedRAMP Moderate authorized services) | IT Manager |
| Backup vault | Cloud backup service | Cloud tenant (same account, **gap**) | IT Manager |
| Reseller portal tenant | SaaS | Portal vendor | Sales Operations Manager |
| Identity provider tenant | SaaS | Identity vendor | IT Manager |
| Firewall and VPN, switches, wireless controller | Network | Headquarters building | IT Manager |
| Handheld scanners (40) | Endpoint (unsupported operating system, **gap**) | Distribution center | Warehouse and Logistics Manager |
| Laptops and desktops (58), lab workstations (6), label and shipping printers (12) | Endpoint | Headquarters, lab | Systems Administrator |
| Lab cage badge reader, cameras (24), network video recorder | Physical security | Headquarters building | Warehouse and Logistics Manager |
| RMM agents | Software agent | All Windows endpoints and servers | MSP (overseen by the IT Manager) |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 96 controls:
- Implemented: 25
- Partially implemented: 49
- Planned: 22
- Not applicable: 0

Inheritance: 75 system-specific, 18 hybrid, 3 common/inherited. The `regulatory_driver` column lists the SP 800-171 Rev. 2 requirements and contract clauses each control implements, taken from the P03 crosswalk. CSF 2.0 subcategories come from the official CSF 2.0 to SP 800-53 Rev. 5.2.0 reference; 17 controls with no entry in that reference are left blank.

**Relationship to SP 800-171 3.12.4.** SP 800-171 Rev. 2 requires a system security plan that describes how each requirement is implemented. This SSP, together with the requirement-level rows in P03 `gap-analysis.csv` (110 requirements, with current state and evidence), is that plan.

### 10.2 Control assessment status
Assessed 2026-08-03 to 2026-08-07 by a contracted independent assessor. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
All workforce users authenticate to email, the ERP, the VPN, and the cloud console through the identity provider with a password and a second factor (an authenticator app, or a hardware key for the IT Manager and Systems Administrator). This is appropriate for remote and privileged access to CUI given the Moderate categorization.

**Exceptions:** WMS handhelds use 6 shared zone accounts with no MFA, and the file server CUI share accepts domain passwords without MFA from the office network. Both are open gaps (P03 rows G-046 and G-111; P07 POAM-004 and POAM-005).

Reseller portal users authenticate with the portal vendor's sign-in, where MFA is optional. That is governed by the portal configuration and assessed in P09.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **C3PAO:** CMMC Third-Party Assessment Organization
- **C-SCRM:** cybersecurity supply chain risk management
- **CUI:** Controlled Unclassified Information
- **DIBNet:** the DoD portal for cyber incident reports
- **ERP:** enterprise resource planning
- **FCI:** Federal Contract Information
- **MSP:** managed service provider
- **OFP:** Order-to-Fulfillment Platform
- **POA&M:** plan of action and milestones
- **RMM:** remote monitoring and management
- **SPRS:** Supplier Performance Risk System
- **WMS:** warehouse management system

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan (replaces the uncompleted 2024 template) | IT Manager |
