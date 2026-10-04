# System Security Plan: Order-to-Fulfillment Platform (OFP)

**Organization:** Cris Santos Company Holdings, Inc. (corporate shared services, serving the IT Distribution, Logistics and Warehousing, and Online Retail divisions) | **Tier:** Multi-Sector | **Vertical:** Wholesale Trade
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-15

> **Why this system.** At this tier the SSP can cover one system per division or a shared corporate system. The group chose the **Order-to-Fulfillment Platform**, the registry's primary system (order management, warehouse, and reseller portal), because all three divisions run on the same ERP and WMS, it inherits most of its controls from corporate (SYS-G1 to SYS-G3), and it carries the DoD order stream, including the Federal Fulfillment Enclave (FFE) that holds CUI. Division systems outside the OFP (the Online Retail storefront and contact center, DC automation, the Lifecycle Services platform) keep their own security plans that inherit from the same common control catalog (`common-control-catalog.csv`).

## 1. System Name and Identifier
Order-to-Fulfillment Platform (**OFP**), identifier CSCH-OFP-01. Components SYS-G4, SYS-G5, SYS-D1, SYS-D2, and SYS-D5 in `../00_company-facts.md` section 3.

## 2. System Overview
The OFP takes an order from any channel and turns it into a shipment:
- **IT Distribution:** reseller orders, quotes, and EDI purchase orders (about 85,000 order lines per shipping day), purchasing from about 2,400 suppliers, and the federal order stream with integration work for DoD installations.
- **Logistics:** wave release, picking, packing, and shipping at 9 DCs, and inventory and order services for about 140 3PL clients.
- **Online Retail:** consumer orders flow from the storefront (outside this boundary) into the ERP and the WMS for fulfillment.

About 31,000 workforce users, 41,000 reseller users, and 1,900 3PL client users use it.

**Major components:**
- **SYS-G4 group ERP** (commercial SaaS): order-to-cash, procure-to-pay, inventory, finance, and the item master with the Section 889 screening flags. Holds FCI. **No CUI by policy** (gap: CUI attachments found, section 10).
- **SYS-G5 EDI and integration hub:** value-added network, B2B APIs, and the supplier portal for about 1,150 trading partners.
- **SYS-D5 WMS:** multi-client warehouse management on cloud provider A, with about 6,800 handhelds at 9 DCs and a web console for 3PL clients.
- **SYS-D1 reseller portal and quoting** (vendor SaaS); card payments go to a payment service provider's hosted page, outside the boundary.
- **SYS-D2 Federal Fulfillment Enclave:** federal order management, the CUI document store, imaging and configuration servers in the provider B government-community landing zone, and the lab networks and workstations at integration centers IC-1 (inside DC-1) and IC-2 (inside DC-6).

The platform is described by service category and is vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies to the OFP |
|---|---|---|---|
| N42-R03 | DFARS Safeguarding Covered Defense Information and Cyber Incident Reporting | 48 CFR 252.204-7012 | The FFE and any OFP component that stores CUI is a covered contractor information system: SP 800-171 Rev. 2, 72-hour reporting, 90-day preservation, and FedRAMP Moderate equivalency for cloud services that hold CDI ((b)(2)(ii)(D)) |
| N42-R02 | CMMC Program, Level 2 (C3PAO) from Phase 2 awards | 32 CFR Part 170; DFARS 252.204-7021 | The FFE plus the security protection assets it relies on (SYS-G1, SYS-G2, DC badge systems) form the Level 2 assessment scope (32 CFR 170.19(c)) |
| N42-R04 | FAR Basic Safeguarding (FCI) | 48 CFR 52.204-21 | The ERP, EDI hub, and WMS hold FCI from DoD orders and shipments |
| N42-R05 | Section 889 prohibition | 48 CFR 52.204-25 | The item master screening flags and the federal order block |
| DFARS | Sources of electronic parts; SP 800-171 DoD Assessments | 48 CFR 252.246-7008; 252.204-7019 and -7020 | Sourcing order for integration jobs; SPRS score for the CUI environment |
| CUI | CUI Basic at no less than moderate confidentiality | 32 CFR 2002.14(g) | Sets the FFE confidentiality floor |
| N42-R07 | SEC cybersecurity disclosure | 17 CFR 229.106; Form 8-K Item 1.05 | An OFP incident can be material to the group (P08) |
| N42-R08 | CCPA/CPRA and CPPA regulations | Cal. Civ. Code 1798.100 et seq.; Cal. Code Regs. tit. 11, 7120-7124 | Consumer order and shipping data for Online Retail customers in California pass through the ERP and WMS; reasonable security and the 2028 cybersecurity audit cover them |
| N42-R01 | FTC Act Section 5 | 15 U.S.C. 45(a) | Reasonable security for reseller, consumer, and employee data |
| Contracts | 3PL client agreements; payment brand rules through the acquirer | Contracts | 3PL service levels and SOC reports (P09); the reseller portal keeps card data outside the boundary by using a hosted payment page |
| Internal | Group policies POL-01 to POL-05 and division supplements | P06 | |

Not applicable to the OFP: CTPAT (voluntary program, applied to import processes outside the boundary); PCI DSS cardholder data environment (no card data is stored, processed, or transmitted inside the boundary); USCG and TSA cyber rules (no regulated vessel, facility, or operator).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Group CISO and the Group ERP and platforms director (system owner) on 2026-09-15, after the board audit and risk committee review.

### 4.2 System Authorization Decision
The group is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- **Decision:** authorized to operate with conditions, 2026-09-15, by the Group CISO and the Group Chief Risk Officer (acceptance authority for High risks).
- **Conditions:** (1) purge CUI from the commercial ERP and collaboration tenant and block attachments on DoD orders by 2026-11-30 (POAM-007); (2) close the IC-2 lab network route by 2026-10-31 (POAM-006); (3) no new integration job for a Phase 2 award until the CMMC readiness check passes (POAM-010).
- **CMMC affirmation:** the IT Distribution president, as Affirming Official (32 CFR 170.22), will not affirm Level 2 compliance until the C3PAO assessment closes with a Final or Conditional status.
- **Reauthorization:** annually, or after the C3PAO assessment (2027-01).

### 4.3 System Operational Status
Operational. **Major modifications planned:** CUI containment (data loss prevention on CUI markings, attachment block, migration of prime file exchange to the government-community tenant), due 2026-12-15; handheld replacement and named sign-in at DC-8 and DC-9, due 2027-03-31; MFA for 3PL client users, due 2026-12-31.

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Group ERP and platforms director | Accountable for the OFP and this SSP |
| Authorizing official equivalent | Group CISO with the Group Chief Risk Officer | Authorization decision; High risk acceptance |
| CMMC Affirming Official | IT Distribution president | Affirmations in SPRS for the Federal Solutions CAGE code |
| CMMC scope owner | Group CMMC program director | Level 2 assessment scope, SPRS submissions, C3PAO coordination |
| CUI custodians | Integration center managers (IC-1, IC-2) | Day-to-day CUI handling in the FFE |
| Federal contract compliance | Federal Solutions vice president | Flowdown, Section 889 representations, DIBNet reports |
| WMS business owner | Logistics vice president of operations | WMS and DC physical security, including the buildings around the integration centers |
| Supply chain risk | Group supply chain risk director | Item master screening flags, approved supplier list, SR controls |
| Common control providers | Group identity director (SYS-G1), Group SOC director (SYS-G2), Group cloud platform director (SYS-G3), Group HR director, Logistics DC operations | Operate inherited controls (`common-control-catalog.csv`) |
| Independent assessor | Group internal audit | Assesses common controls once and samples division controls (P07) |

**Overlap and compensation.** Logistics both operates DC physical security and is a user of the OFP. Group internal audit, which is independent of both, tests the DC controls that the CUI environment depends on (P07 PE-3).

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| CUI configuration documents (FFE) | Moderate | Moderate | Low | 32 CFR 2002.14(g) sets the confidentiality floor; altered configurations could harm DoD networks; integration jobs tolerate 48 hours (P05 BP-ID03) |
| Goods acquisition, inventory control, and logistics (orders, purchase orders, inventory, shipments, FCI) | Moderate | Moderate | Moderate | Pricing and DoD order data are sensitive; a wrong manufacturer of record or ship-to sends the wrong product; the ERP and WMS have 8- to 12-hour MTDs (P05) |
| Supply chain integrity data (item master manufacturer of record, Section 889 flags, approved supplier list) | Low | **Moderate** | Moderate | Tampering could release covered or counterfeit products to federal customers |
| Consumer and reseller contact and shipping data | Moderate | Moderate | Moderate | Personal information of millions of consumers; state breach laws and CCPA |
| **OFP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | Overall **Moderate** |

**Why availability is Moderate, not High.** A one-day ERP or WMS outage would cost the group heavily, but most reseller and 3PL revenue is delayed rather than lost, and documented workarounds exist (P05). The board audit and risk committee accepted Moderate on 2026-09-15, with the condition that a ransomware test of the WMS replica is completed (POAM-016).

**Baseline:** the NIST SP 800-53B **Moderate** baseline, tailored, with SP 800-171 Rev. 2 as an overlay for the FFE. The plan documents **113 controls** in `control-implementation.csv`:
- 109 from the Moderate baseline;
- 4 not in any baseline but needed here: PM-1, PM-9, PM-30 (group program, risk strategy, and supply chain strategy) and SR-4 (provenance for federal integration jobs).

Other Moderate-baseline controls are either fully inherited from the cloud and SaaS providers (evidenced by their SOC 2 reports and, for provider B, FedRAMP authorizations) or tailored out with a reason in the group tailoring register.

**How the SR controls are applied.** SP 800-53 writes the SR controls for the components of an organization's own systems. As an author decision, the group also applies them to the products it distributes to DoD customers, because those products become components of DoD systems.

## 7. Authorization Boundary Description
- **Inside:** the ERP tenant configuration and roles, the EDI hub, the WMS application, database, and handhelds, the reseller portal configuration, and the FFE (provider B accounts, CUI store, imaging and configuration servers, IC-1 and IC-2 lab networks, workstations, and lab cages).
- **Outside, inherited (common control providers):** SYS-G1 identity platform, SYS-G2 SOC, SIEM, and EDR, the SYS-G3 landing zones, and the DC buildings and badge systems run by Logistics.
- **Outside, interconnected:** the storefront (SYS-D8), the TMS (SYS-D6), DC automation (SYS-D7), the forecasting service (SYS-D4), the data platform (SYS-G6), primes, suppliers, carriers, and payment service providers.

**CMMC Level 2 asset categories (32 CFR 170.19(c))**
| Category | Assets |
|---|---|
| CUI Assets | FFE (SYS-D2) servers, CUI store, IC-1 and IC-2 lab networks and workstations. The commercial ERP and collaboration tenant hold CUI today and are CUI Assets until the purge closes (POAM-007) |
| Security Protection Assets | SYS-G1 (government-community tenant and PAM), SYS-G2 SIEM and EDR, the DC-1 and DC-6 badge and camera systems |
| Contractor Risk Managed Assets | WMS (SYS-D5) and EDI hub (SYS-G5): FCI only, kept free of CUI by policy and configuration |
| Out of scope for CUI | Reseller portal (SYS-D1), storefront, contact center, DC automation |

The diagrams are in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Primes A to F | Inbound CUI through the prime secure file exchange into the FFE; outbound configured equipment | CUI configuration documents; FCI | Subcontracts with DFARS 252.204-7012, -7019, -7020, -7021, 252.246-7008, FAR 52.204-21 and 52.204-25. **Gap:** two primes also exchanged CUI through the commercial collaboration tenant (POAM-007) |
| Suppliers and resellers (SYS-G5) | Bidirectional | Purchase orders, advance ship notices, invoices, catalogs | EDI trading partner agreements |
| Storefront (SYS-D8) | Inbound orders; outbound status | Consumer orders and shipping addresses | Internal interface standard |
| Forecasting service (SYS-D4) and data platform (SYS-G6) | Outbound order history; inbound purchase orders (automatic release) | Order history including FCI | Group AI Standard (P10). **Gap:** the feed includes DoD orders |
| TMS (SYS-D6) and carriers | Outbound | Shipment and address data | Carrier agreements |
| 3PL clients | Bidirectional (console and file transfer) | Client inventory and orders | 3PL agreements; SOC 1 report; SOC 2 planned (P09) |
| Commercial ERP vendor | Hosting | Orders, FCI; **CUI attachments found** | SaaS contract; no FedRAMP Moderate equivalency evidence (POAM-008) |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| Group ERP tenant | SaaS | ERP vendor (SOC 2 Type 2) | Group ERP and platforms director |
| EDI and integration hub | PaaS and value-added network | Provider A; network provider | Group integration director |
| WMS application and database | Containers and managed database | Provider A, two regions | Logistics vice president of operations |
| Handhelds (about 6,800) and DC wireless | Endpoint and network | 9 DCs | Logistics vice president of operations |
| Reseller portal tenant | SaaS | Portal vendor | IT Distribution chief operating officer |
| FFE accounts: CUI store, federal order management, imaging and configuration servers | IaaS and PaaS | Provider B government-community region (FedRAMP Moderate or higher) | Federal Solutions vice president |
| IC-1 and IC-2 lab networks, about 120 lab workstations, lab cages | Network, endpoint, physical | Inside DC-1 and DC-6 | Integration center managers |
| Immutable backup vault | Backup service | Separate provider B account | Group cloud platform director |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv` (113 controls) and `common-control-catalog.csv` (102 controls provided by corporate functions, the Logistics DC operation, or Lifecycle Services media sanitization).

| Status | Controls |
|---|---|
| Implemented | 88 |
| Partially implemented | 23 |
| Planned | 2 |
| Not applicable | 0 |
| **Total** | **113** |

| Inheritance | Controls |
|---|---|
| Common/Inherited (from SYS-G1, SYS-G2, SYS-G3, group functions, or Logistics DC operations) | 75 |
| Hybrid (a group provider supplies the mechanism; the OFP configures or operates part) | 27 |
| System-specific | 11 |

The `regulatory_driver` column lists the SP 800-171 Rev. 2 requirements and contract clauses each control implements (from the P03 crosswalk). CSF 2.0 subcategories come from the official CSF 2.0 to SP 800-53 Rev. 5.2.0 reference; enhancements without their own entry use their base control's entry, and 18 controls with no entry are left blank.

**The 23 partially implemented controls** cluster in four places:
- **CUI outside the enclave** (scenario gap 1): AC-3, AC-4, AC-20, SA-9, CA-2, PL-2, SC-7, RA-5.
- **Supply chain at scale** (gaps 2 and 3): SR-3, SR-4, SR-5, SR-6, SR-10, SR-11, SR-11(1), AT-3, CM-8.
- **Acquired DCs and physical controls** (gap 7): AC-2, IA-2, PE-3.
- **Cross-division response and recovery** (gap 10): IR-3, IR-6, CP-4.

The two **planned** controls are IA-8 (MFA for 3PL client users) and SI-7 (firmware integrity checks at DC receiving).

### 10.2 Common control inheritance by division
The common control catalog lists 102 controls. Inheritance is **documented for IT Distribution** (the FFE SSP draft and this plan) and for **Online Retail** (the PCI DSS responsibility matrix maps group controls to its cardholder data environment). It is **not documented for Logistics** (scenario gap 8). Until POAM-022 closes, Logistics cannot show which controls for the WMS, TMS, and DC automation are met by group controls, which also blocks the 3PL SOC 2 system description (P09).

### 10.3 Relationship to SP 800-171 3.12.4
SP 800-171 Rev. 2 requires a system security plan that describes how each requirement is implemented. For the CMMC scope, this SSP together with the requirement-level rows in P03 `gap-analysis.csv` (110 requirements with current state and evidence) is that plan.

### 10.4 Control assessment status
Common controls were assessed once, and OFP and division controls sampled, from 2026-07-06 to 2026-08-28 by group internal audit. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
- **Workforce users** authenticate through SYS-G1 with MFA. FFE users sign in through the government-community tenant with phishing-resistant authenticators; administrators use hardware keys and just-in-time PAM elevation. This fits a Moderate system holding CUI.
- **Exception:** 22 shared handheld logins at DC-8 and DC-9 (POAM-001).
- **Reseller users** sign in to the portal with the portal vendor's identity service; MFA is required for reseller administrators and optional for buyers.
- **3PL client users** sign in to the WMS console with passwords only; MFA is planned (IA-8, POAM-027).

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud architecture and control map (P04), group and division risk registers (P01), gap analyses and regulation-by-division matrix (P03), group policies and division supplements (P06), assessment and POA&M (P07), incident runbook and notification matrix (P08), SOC 2 readiness (P09), AI governance (P10).

## 13. Acronym List and Glossary
- **C3PAO:** CMMC Third-Party Assessment Organization
- **Common control:** a control provided once by corporate (or by the Logistics DC operation) and inherited by several systems
- **CUI / FCI:** Controlled Unclassified Information / Federal Contract Information
- **DC:** distribution center
- **FFE:** Federal Fulfillment Enclave
- **IC-1, IC-2:** federal integration centers inside DC-1 and DC-6
- **OFP:** Order-to-Fulfillment Platform
- **PAM:** privileged access management
- **SPRS:** Supplier Performance Risk System
- **WMS:** warehouse management system

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-08-31 | Draft after P07 fieldwork; FFE section expanded to the integration center lab networks | Group ERP and platforms director |
| 1.0 | 2026-09-15 | Approved with authorization conditions | Group CISO |
