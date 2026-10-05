# System Security Plan: Group ERP and Production Scheduling Platform (GEPS)

**Organization:** Cris Santos Company Holdings, Inc. (corporate shared services, serving the Transformer Manufacturing, Electric Utility, and Grid Engineering divisions) | **Tier:** Multi-Sector | **Vertical:** Critical Manufacturing
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-15

> **Why this system.** At this tier the SSP can cover one system per division or a shared corporate system. The group chose the **GEPS**, a shared corporate system, because it is the registry's primary system for this vertical (ERP and production scheduling), it serves all three divisions from one instance, it inherits most of its controls from corporate (SYS-G1 to SYS-G3), and it carries two of the group's High risks (P01 GR-01 and GR-02). Plant OT (SYS-M1, SYS-M2) and the Electric Utility's TCC (SYS-U1) keep their own plans: the plants under the group OT standard, the TCC under the NERC CIP program. Both draw on the same common control catalog where it applies.

## 1. System Name and Identifier
Group ERP and Production Scheduling Platform (**GEPS**), identifier CSCH-SYS-G4. SYS-G4 in `../00_company-facts.md`.

## 2. System Overview
The GEPS is one ERP instance with a company code for each division. It supports:
- **Transformer Manufacturing:** configure-to-order quoting, bills of materials and routings, the APS finite-capacity schedule for 8 plants, work order release through the integration hub, purchasing and supplier EDI, inventory and spare units, shipping, and export screening.
- **Electric Utility:** storm stock and materials, purchasing, and finance. The utility's operational systems (TCC, DCC, AMI, CIS) are not part of the GEPS, and group policy prohibits BES Cyber System Information in it.
- **Grid Engineering:** project accounting, time, and purchasing.
- **Corporate:** general ledger, consolidation, and payments for SEC reporting.

About 16,500 named users (about 11,000 in Manufacturing), 1,900 supplier portal users, and 20 service accounts (6 for the integration hub, 14 for batch jobs).

**Major components** (Cloud provider A, with the disaster recovery copy and backup vault in Cloud provider B):
- **Web and application tier:** ERP application servers on virtual machines behind a web application firewall
- **Database tier:** managed database cluster with replication to provider B (RPO about 15 minutes)
- **APS module:** finite-capacity scheduling engine and planner workbench
- **Integration hub:** message broker and interface servers that send work orders, bills of materials, and routings to each plant MES and receive confirmations; also EDI with customers, suppliers, and the EDI network provider
- **Supplier portal:** purchase order collaboration for suppliers, behind the group customer identity service
- **Reporting copy:** read-only replica in provider B refreshed every 4 hours

The platform is described by service category and is vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies to the GEPS |
|---|---|---|---|
| C-CRITICAL-MFG-R03 | EAR | 15 CFR Parts 730-774; recordkeeping 15 CFR 762.6(a) | Export orders are screened against restricted-party lists in the GEPS before release; export records are kept 7 years (5 required) |
| C-CRITICAL-MFG-R01 | CIRCIA (proposed only) | 6 U.S.C. 681-681g; proposed 6 CFR 226.2(b)(3)(iii) and (b)(6) | Not in effect. If finalized as proposed, a GEPS ransomware incident would be reportable to CISA within 72 hours (readiness only; P08) |
| C-CRITICAL-MFG-R02 | ICTS connected vehicles rule | 15 CFR Part 791, Subpart D | Not applicable: no vehicles or vehicle systems |
| C-CRITICAL-MFG-R04 | DFARS 252.204-7012 | 48 CFR 252.204-7012 | Not applicable: no DoD contracts; the bid review gate keeps CUI out |
| FAR | Basic safeguarding; covered telecommunications; Kaspersky; FASCSA | 48 CFR 52.204-21, -25, -23, -30 | Federal contract delivery schedules, order data, and references to agency specifications are FCI held in the GEPS, so it is a covered contractor information system for Manufacturing's 14 and Grid Engineering's federal contracts |
| SEC | Cybersecurity disclosure | Form 8-K Item 1.05; 17 CFR 229.106 | A GEPS outage that stops the plants is a likely material incident (P08); the GEPS general ledger supports SEC reporting |
| Contracts | Utility Supplier Cyber Security Addenda (140 utilities) | Contract terms flowing down CIP-013-2 R1 Part 1.2 | Indirect: the addenda cover products and services, not the GEPS. A GEPS incident triggers addendum notice only if it relates to supplied products or services (P08) |
| NERC CIP | Electric Utility obligations | CIP-002-5.1a to CIP-013-2 | Not applicable to the GEPS: it is not a BES Cyber System, EACMS, or PACS, and the utility's BCSI is prohibited in it |
| State law | Breach notification | Each state where affected individuals reside (Florida worked example: Fla. Stat. 501.171) | Limited: the GEPS holds names and business contact details of employees and supplier contacts, not Social Security or account numbers (those are in SYS-G5) |
| Internal | Group policies POL-01 to POL-05 and division supplements | P06 | |

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Group CISO and the Group ERP platform director (system owner) on 2026-09-15, after the board risk committee review.

### 4.2 System Authorization Decision
The group is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- **Decision:** authorized to operate with conditions, 2026-09-15, by the Group CISO and the Group Chief Risk Officer (acceptance authority for High risks), with the VP manufacturing operations as the business owner of the scheduling module.
- **Conditions:** (1) one integration hub service account per plant, with keys in the secret store and rotated every 90 days, by 2026-12-31 (POAM-002); (2) a full restore test of APS and the integration hub in provider B by 2027-03-31 (POAM-004); (3) no new plant connection except through an OT DMZ, and the P8 path moved behind a DMZ by 2027-03-31 (POAM-007).
- **Reauthorization:** annually, or when the P8 MES migration or a major ERP upgrade completes.

### 4.3 System Operational Status
Operational. **Major modification planned:** migration of the P8 legacy MES to the standard MES behind an OT DMZ (2027-06-30).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Group ERP platform director | Accountable for the GEPS and this SSP |
| Authorizing official equivalent | Group CISO with the Group Chief Risk Officer | Authorization decision; High risk acceptance |
| Business owner, scheduling and manufacturing modules | VP manufacturing operations | Approves Manufacturing roles, plant interfaces, and schedule changes |
| Data owners, other company codes | Electric Utility director of supply chain; Grid Engineering chief operating officer; group controller | Approve access to their company codes |
| Common control providers | Group identity director (SYS-G1), Group SOC director (SYS-G2), Group cloud platform director (SYS-G3), Group HR director, Group procurement director | Operate inherited controls (`common-control-catalog.csv`) |
| Plant interface owners | Director of OT engineering; plant managers | Own the MES side of each interface and the OT DMZ rules |
| Independent assessor | Group internal audit | Assesses common controls once and samples GEPS and division controls (P07) |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1 where a type fits; two company-defined types cover contract and export data. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Logistics management (APS schedule, work order release, shipping) | Low | **High** | **High** | A wrong or altered bill of materials or routing released to 8 plants could put a defective transformer on the grid. Loss of scheduling stops all plants within about 48 hours (P05 BP-MF02) |
| Inventory control (spare units, storm stock, materials) | Low | High | **High** | Spare transformers and storm stock for utilities, including the affiliate, during hurricane season (P05 BP-MF07, BP-EU03) |
| Goods acquisition (purchasing and supplier EDI) | Moderate | Moderate | Moderate | Supplier pricing; long-lead core steel and bushings |
| Accounting and payments (general ledger, consolidation) | Moderate | High | Moderate | SEC reporting and internal control over financial reporting |
| Customer and federal contract information (company-defined) | Moderate | Moderate | Low | Customer specifications references, FCI, and NDA terms |
| Export control records (company-defined) | Low | Moderate | Low | Screening results and records kept under 15 CFR 762.6 |
| Information security (roles, keys, logs) | Moderate | High | Moderate | Compromise would expose every company code |
| **GEPS category (high-water mark)** | **Moderate** | **High** | **High** | Overall **High** |

**Baseline:** the NIST SP 800-53B **High** baseline, tailored. The plan documents **142 controls** in `control-implementation.csv`:
- 141 from the High baseline;
- 1 program management control not in any baseline (PM-9), added because risk acceptance for the GEPS sits at group level.

Other High-baseline controls are fully inherited from the cloud providers (most PE and MP controls, evidenced by their SOC 2 Type 2 reports) or tailored out with a reason in the group tailoring register (for example, PE controls for facilities the group does not run for this system). CSF 2.0 subcategories in the CSV come from NIST's official CSF 2.0 to SP 800-53 mapping (control enhancements take their base control's entries); for 17 controls neither the control nor its base control has an entry, and the author mapped them (for example AU-8 to PR.PS-04 and MA-4 to PR.AA-03).

## 7. Authorization Boundary Description
- **Inside:** the GEPS accounts in provider A (web, application, database, APS, integration hub, supplier portal) and the disaster recovery copy, reporting copy, and backups in provider B.
- **Outside, inherited (common control providers):** SYS-G1 identity, SYS-G2 SOC, SIEM, and EDR, SYS-G3 landing zones (hub network, log archive, guardrails, keys, backup vault).
- **Outside, interconnected:** plant MES at P1 to P7 (through each OT DMZ) and the P8 legacy MES (direct, a gap); PLM (SYS-M3); TDMS (SYS-M4); EDI network provider and two direct supplier EDI links; the Electric Utility EAM (SYS-U5); SYS-G5 HR (cost centers only).

The diagram is in P04 `cloud-architecture.md` (section 2.2).

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Plant MES P1 to P7 (SYS-M1) | Outbound work orders, BOMs, routings; inbound confirmations | Production data | Interface agreements per plant (2024); traffic terminates in each OT DMZ |
| P8 legacy MES (SYS-M1) | Both | Production data | **None** (CA-3 gap); direct connection to a dual-homed server (POAM-007) |
| PLM (SYS-M3) | Inbound design release | Engineering BOMs and drawing references | Internal interface specification |
| TDMS (SYS-M4) | Inbound | Test release status (no test data) | Internal interface specification |
| EDI network provider | Both | Orders, ship notices, invoices with utilities and suppliers | Provider contract with 24-hour incident notice |
| Direct supplier EDI (2 core steel suppliers) | Both | Orders and ship notices | **No interconnection agreement** (CA-3 gap) |
| Electric Utility EAM (SYS-U5) | Both | Materials reservations and storm stock issues | Intercompany data agreement (2023) |
| Banks | Outbound | Payment files | Bank agreements |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| ERP web and application servers | IaaS virtual machines | Provider A | Group ERP platform director |
| ERP database cluster | Managed database (PaaS) | Provider A, replica in provider B | Group ERP platform director |
| APS engine and planner workbench | IaaS virtual machines | Provider A | Group ERP platform director (VP manufacturing operations as business owner) |
| Integration hub | Managed message broker plus interface servers | Provider A | Group ERP platform director |
| Supplier portal | Web application behind the group customer identity service | Provider A | Group procurement director |
| Reporting copy | Read-only replica | Provider B | Group ERP platform director |
| Disaster recovery environment and immutable backups | IaaS and backup service | Provider B | Group cloud platform director |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv` (142 controls) and `common-control-catalog.csv` (104 group common controls).

| Status | Controls |
|---|---|
| Implemented | 120 |
| Partially implemented | 22 |
| Planned | 0 |
| Not applicable | 0 |
| **Total** | **142** |

| Inheritance | Controls |
|---|---|
| Common/Inherited (from SYS-G1, SYS-G2, SYS-G3, group functions, or the cloud providers) | 92 |
| Hybrid (group provides the mechanism; the GEPS team configures or operates part) | 12 |
| System-specific | 38 |

**The 22 partially implemented controls** cluster in four places:
- **The plant interface** (scenario gaps 1 and 2): AC-4, AC-6, CA-3, CM-4, CM-8, SC-7, SI-4(4).
- **Service accounts and logging:** AC-2, IA-5, AU-6, SI-4, AT-3, CA-8.
- **Recovery of scheduling** (gap 1): CP-2, CP-2(3), CP-4, CP-9(1), CP-10.
- **Cross-division incident handling** (gap 7) and duties: IR-3, IR-6, IR-8, AC-5.

### 10.2 Common control inheritance by division
The common control catalog lists 104 controls provided by corporate. Inheritance is **documented for Transformer Manufacturing** (2025 matrix, IT systems; plant OT follows the group OT standard instead), for the **Electric Utility** (2025 matrix, IT systems only, used as CIP evidence; the TCC and substations use separate CIP-004 and CIP-005 accounts and networks), and for the **GEPS** (this plan). It is **not documented for Grid Engineering** (scenario gap 6). Until POAM-014 closes, Grid Engineering cannot show which of its client contract and SOC 2 commitments rest on group controls. 18 of the catalog controls were assessed once in 2026 (P07); the rest are on the 2027 cycle.

### 10.3 Control assessment status
Common controls were assessed once, and GEPS and division controls sampled, from 2026-07-06 to 2026-08-28 by group internal audit. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
- **Workforce users** authenticate through SYS-G1 federated sign-in with MFA (number matching); **administrators** use phishing-resistant hardware keys and just-in-time PAM elevation. This fits a system rated High for integrity and availability, used remotely by planners and buyers.
- **Supplier portal users** authenticate through the group customer identity service with MFA.
- **Service accounts** should use workload identity with short-lived tokens. The 6 integration hub accounts still use static keys older than 1 year (POAM-002).
- **Plant shop-floor users** do not sign in to the GEPS; they use the MES, which is outside this boundary.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), group and division risk registers (P01), gap analyses and regulation-by-division matrix (P03), cloud architecture and control map (P04), BIA (P05), group policies and division supplements (P06), assessment and POA&M (P07), incident response runbook and notification matrix (P08), SOC 2 readiness (P09), AI governance (P10).

## 13. Acronym List and Glossary
- **APS:** advanced planning and scheduling
- **BCSI:** BES Cyber System Information (NERC)
- **Common control:** a control provided once by corporate and inherited by several systems
- **EDI:** electronic data interchange
- **FCI:** federal contract information
- **GEPS:** Group ERP and Production Scheduling Platform
- **MES:** manufacturing execution system
- **OT DMZ:** a network zone between the office network and plant control systems
- **PAM:** privileged access management
- **SIEM:** security information and event management

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-08-31 | Draft after P07 fieldwork | Group ERP platform director |
| 1.0 | 2026-09-15 | Approved with authorization conditions | Group CISO |
