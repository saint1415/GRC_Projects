# System Security Plan: Group Data Platform (GDP)

**Organization:** Cris Santos Company Holdings, Inc. (corporate shared services, serving the Care Delivery, Health Plan, and Health-Tech SaaS divisions) | **Tier:** Multi-Sector | **Vertical:** Health Care and Social Assistance
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-10

> **Why this system.** At this tier the SSP can cover one system per division or a shared corporate system. The group chose the **Group Data Platform**, a shared corporate system, because it holds PHI from both covered-entity divisions and data derived from the SaaS, it inherits most of its controls from corporate (SYS-G1 to SYS-G3), and it carries the group's top risk (P01 GR-01). Each division's own primary system (for Care Delivery, the EHR and practice management system SYS-D1) keeps a division SSP that inherits from the same common control catalog.

## 1. System Name and Identifier
Group Data Platform (**GDP**), identifier CSCH-SYS-G3-DP. Part of SYS-G3 (group cloud platform and data platform); listed as SYS-G3-DP in the intake [asset inventory](../step-00_P00_intake/asset-inventory.csv).

## 2. System Overview
The GDP is the group's analytics and data science platform. It supports:
- **Care Delivery:** quality measurement, population health, and operational analytics for about 2.1 million active patients.
- **Health Plan:** claims analytics, care management targeting, quality reporting, and the data used to train and monitor the AI utilization-management model (P10).
- **Health-Tech SaaS:** product analytics on de-identified data sets (expert determination, 45 CFR 164.514(b)(1)).

About 1,900 workforce users (data engineers, analysts, data scientists, and privacy staff) and 34 service accounts use it.

**Major components** (all on the group cloud platform, provider A, with the disaster recovery replica and backup vault on provider B):
- **Ingestion pipelines:** managed integration and workflow services that pull from SYS-D1, SYS-D2, and SYS-D3 exports
- **Data lake:** object storage organized in zones (Care Delivery PHI, Health Plan PHI, de-identified, staging)
- **Data warehouse:** a managed analytical database
- **Data science workspace:** managed notebooks and model training compute
- **Catalog and policy engine:** dataset inventory, tags for covered entity and purpose, and access policies
- **Key management:** customer-managed keys per zone
- **Reporting service:** dashboards for division users

The platform is described by service category and is vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies to the GDP |
|---|---|---|---|
| N62-R01 | HIPAA Security Rule | 45 CFR Part 164, Subpart C | Corporate shared services is a business associate of both covered entities, so it must meet the Security Rule directly. Each covered entity also remains responsible for its ePHI |
| N62-R02 | HIPAA Privacy Rule | 45 CFR Part 164, Subpart E | Minimum necessary (164.502(b), 164.514(d)); TPO disclosures between the two covered entities (164.506(c)); business associate permitted uses (164.502(a)(3)); de-identification (164.514(b)) |
| N62-R03 | HIPAA Breach Notification Rule | 45 CFR 164.400-414 | As a business associate, corporate notifies each covered entity (164.410); each covered entity notifies its individuals, HHS, and media (P08) |
| N62-R04 | HIPAA Security Rule NPRM (proposed, not in force) | 90 FR 898 (2025-01-06) | Tracked only (asset inventory, encryption, restore within 72 hours) |
| N62-R07 | Section 1557 patient care decision support tools | 45 CFR 92.210 | Models trained on the GDP that support clinical decisions (P10) |
| MA | Medicare Advantage confidentiality of enrollee records | 42 CFR 422.118 | Health Plan enrollee data on the GDP must be used only for the purposes the MA organization's procedures specify (422.118(a)(1)) |
| N52-R01, N52-R07 | GLBA and state insurance data security laws | 15 U.S.C. 6801-6809; NAIC Model #668 where enacted | Health Plan member data; state insurance notice duties in adopting states (P08) |
| N52-R08 / N51-R08 | SEC cybersecurity disclosure | Reg S-K Item 106; Form 8-K Item 1.05 | A GDP incident may be material to the group (P08) |
| Contracts | Intercompany BAAs; SaaS customer BAAs | 45 CFR 164.504(e) | The Health Plan intercompany BAA (2019) predates the GDP (POAM-020); 97 SaaS customer BAAs do not permit de-identification for analytics (POAM-022) |
| Internal | Group policies POL-01 to POL-05 and division supplements | P06 | |

Not applicable: 42 CFR Part 2 (no division runs a Part 2 program); FTC Health Breach Notification Rule (all health data here is held by or for HIPAA covered entities). Applicability for each entity is decided in the intake [obligations register](../step-00_P00_intake/obligations-register.csv).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Group CISO and the group data platform director (system owner) on 2026-09-10, after the board risk committee review.

### 4.2 System Authorization Decision
The group is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- **Decision:** authorized to operate with conditions, 2026-09-10, by the Group CISO and the Group Chief Risk Officer (acceptance authority for High risks).
- **Conditions:** (1) complete zone separation and purpose-based access enforcement by 2027-03-31 (POAM-006); (2) no new cross-division data feed without a documented minimum-necessary protocol approved by both division privacy officers; (3) restrict and purge the staging area by 2026-10-31 (POAM-007).
- **Reauthorization:** annually, or at completion of the zone separation program.

### 4.3 System Operational Status
Operational. **Major modification planned:** zone separation by covered entity and purpose-based access enforcement (P01 GR-01), due 2027-03-31.

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Group data platform director | Accountable for the GDP and this SSP |
| Authorizing official equivalent | Group CISO with the Group Chief Risk Officer | Authorization decision; High risk acceptance |
| Data owner, Care Delivery zone | Care Delivery Privacy Officer | Approves access and feeds for Care Delivery PHI |
| Data owner, Health Plan zone | Health Plan Privacy Officer | Approves access and feeds for Health Plan PHI |
| Data owner, de-identified zone | SaaS data platform lead | De-identification method and customer BAA conformance |
| Privacy oversight | Group Chief Privacy Officer | Purpose catalog; minimum-necessary protocols |
| Common control providers | Group identity director (SYS-G1), Group SOC director (SYS-G2), Group cloud platform director (SYS-G3) | Operate inherited controls (common-control-catalog.csv) |
| Independent assessor | Group internal audit | Assesses common controls once and samples division controls (P07) |

Each covered entity keeps its own HIPAA Security Officer and Privacy Officer, as `../00_company-facts.md` requires.

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Health care delivery services (Care Delivery clinical data) | **High** | Moderate | Low | Provisional Moderate, raised to High for aggregation: a disclosure of about 2.1 million patients' records would have a severe effect (breach duties across 6 states, SEC materiality, patient harm). Analytics are not used for real-time care, so availability is Low |
| Health care administration (Health Plan claims, enrollment, UM data) | **High** | Moderate | Moderate | Aggregation of about 900,000 members' data. UM model monitoring and quality reporting have deadlines (P05 BP-G05) |
| Health care research and practitioner education (de-identified data sets) | Moderate | Moderate | Low | De-identified data can still be re-identified if linked; customer contract commitments apply |
| Information security (keys, access policies, logs) | High | High | Moderate | Compromise would expose every zone |
| **GDP category (high-water mark)** | **High** | **High** | **Moderate** | Overall **High** |

**Baseline:** the NIST SP 800-53B **High** baseline, tailored. The plan documents **123 controls** in `control-implementation.csv`:
- 117 from the High baseline;
- 4 from the privacy baseline (PM-9, PM-10, PT-2, PT-3), added because purpose-based access is the platform's main privacy risk;
- 2 program management controls not in any baseline (PM-1, PM-2).

Other High-baseline controls are either fully inherited from the cloud providers (for example, most PE controls, evidenced by their SOC 2 Type 2 reports) or tailored out with a reason in the group tailoring register (for example, PE controls for facilities the group does not operate).

## 7. Authorization Boundary Description
The boundary was drawn from the intake [asset inventory](../step-00_P00_intake/asset-inventory.csv) (SYS-G3-DP and the shared services it inherits from) and the platform exports EV-025 to EV-030.
- **Inside:** the GDP accounts in provider A (ingestion, lake, warehouse, workspace, catalog and policy engine, keys, reporting) and the DR replica and backup vault in provider B.
- **Outside, inherited (common control providers):** SYS-G1 identity platform, SYS-G2 SOC, SIEM, and EDR, and the SYS-G3 landing zone (network hub, logging account, guardrails).
- **Outside, interconnected:** SYS-D1 (Care Delivery EHR, LIS, PACS exports), SYS-D2 (Health Plan claims, enrollment, UM), and SYS-D3 (SaaS de-identified exports).

The diagram is in P04 `cloud-architecture.md` (the GDP subgraph).

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| SYS-D1 Care Delivery EHR, LIS, PACS | Inbound (nightly and near-real-time) | Clinical, billing, and lab data (PHI) | Care Delivery intercompany BAA (2024); feed approvals |
| SYS-D2 Health Plan claims, enrollment, UM | Inbound nightly | Claims, enrollment, UM decisions (PHI) | Health Plan intercompany BAA (2019, **predates the GDP**, POAM-020) |
| SYS-D2 AI UM model | Outbound (training data); inbound (monitoring results) | Features and outcomes (PHI) | Health Plan data owner approval |
| SYS-D3 Health-Tech SaaS | Inbound | De-identified data sets (expert determination). **Gap:** identifiable data can reach the staging area first (POAM-007) | Customer BAAs permitting de-identification (97 do not; POAM-022) |
| Care Delivery to Health Plan data share (via GDP) | Internal between covered entities | Quality and care management data for about 210,000 shared patients and members | 164.506(c)(4) health care operations disclosure; minimum-necessary protocol **not yet documented** (P03) |
| CMS and quality reporting vendors (via division systems) | Outbound | Quality measures | Division contracts; not a direct GDP interface |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| Ingestion and workflow services | PaaS | Provider A | Group data platform director |
| Data lake (4 zones) | Object storage | Provider A | Group data platform director |
| Data warehouse | Managed analytical database (PaaS) | Provider A | Group data platform director |
| Data science workspace | Managed notebooks and training compute | Provider A | Group data platform director |
| Catalog and policy engine | SaaS tool deployed in provider A | Provider A | Group Chief Privacy Officer (policy); platform director (operation) |
| Key management | PaaS (customer-managed keys per zone) | Provider A | Group cloud platform director |
| Reporting service | PaaS | Provider A | Group data platform director |
| DR replica and immutable backup vault | Object storage and backup service | Provider B | Group cloud platform director |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv` (123 controls) and `common-control-catalog.csv` (82 group common controls).

| Status | Controls |
|---|---|
| Implemented | 103 |
| Partially implemented | 20 |
| Planned | 0 |
| Not applicable | 0 |
| **Total** | **123** |

| Inheritance | Controls |
|---|---|
| Common/Inherited (from SYS-G1, SYS-G2, SYS-G3, group functions, or the cloud providers) | 77 |
| Hybrid (group provides the mechanism; the platform configures or operates part) | 24 |
| System-specific | 22 |

**The 20 partially implemented controls** cluster in three places:
- **Purpose-based access and minimum necessary** (group gap 1): AC-3, AC-4, AC-6, AC-21, AU-6, CM-8, PT-2, PT-3, AT-3, SI-12.
- **Account and key hygiene for service accounts:** AC-2, AC-2(12), IA-5, SI-4(4).
- **Governance across divisions** (gaps 5 and 6, and contracts): IR-3, IR-6, PL-2, PM-10, SA-4, CP-4.

### 10.2 Common control inheritance by division
The common control catalog lists 82 controls provided by corporate. Inheritance is **documented for Care Delivery** (2025 inheritance matrix), for the SaaS (its SOC 2 system description carves in the group services), and for the GDP (this plan). It is **not documented for the Health Plan** (group gap 6). Until POAM-015 closes, the Health Plan cannot show which of its HIPAA safeguards are met by group controls, and P07 found two CA-2 determination statements other than satisfied for this reason.

### 10.3 Control assessment status
Common controls were assessed once, and platform and division controls sampled, from 2026-07-01 to 2026-08-31 by group internal audit. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
- **Workforce users** authenticate through SYS-G1 federated sign-in with MFA (number matching); **administrators** use phishing-resistant hardware keys and just-in-time PAM elevation. This fits a High-confidentiality system with remote workforce access.
- **Service accounts** should use workload identity with short-lived tokens. Nine still use static keys older than 1 year (POAM-002).
- **No patients, members, or SaaS customers** access the GDP directly.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), intake evidence, inventories and obligations register ([step-00](../step-00_P00_intake/intake-report.md)), group and division risk registers (P01), gap analyses and regulation-by-division matrix (P03), cloud architecture and control map (P04), BIA (P05), group policies and division supplements (P06), assessment and POA&M (P07), incident response runbook and notification matrix (P08), SOC 2 readiness (P09), AI governance (P10).

## 13. Acronym List and Glossary
- **BAA:** business associate agreement
- **Common control:** a control provided once by corporate and inherited by several systems
- **GDP:** Group Data Platform
- **MA:** Medicare Advantage
- **PAM:** privileged access management
- **Purpose tag:** a label on a dataset naming its covered entity and the permitted purpose (treatment, payment, health care operations, or de-identified)
- **SIEM:** security information and event management
- **TPO:** treatment, payment, and health care operations
- **UM:** utilization management

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-08-31 | Draft after P07 fieldwork | Group data platform director |
| 1.0 | 2026-09-10 | Approved with authorization conditions | Group CISO |
