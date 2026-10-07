# System Security Plan: ERP and Production Scheduling Platform (EPSP)

**Organization:** Cris Santos Company, Inc. (PE-backed power and distribution transformer manufacturer, Florida) | **Tier:** Mid-Market | **Vertical:** Critical Manufacturing
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-15

## 1. System Name and Identifier
ERP and Production Scheduling Platform (**EPSP**), identifier CSC-EPSP-01. The EPSP is the company's major system: it carries every order from quote to shipment and releases all work to both plants.

## 2. System Overview
The EPSP runs the order-to-shipment flow for distribution transformers (Plant 1) and power transformers (Plant 2): customer orders, bills of materials, purchasing, inventory, the finite-capacity schedule for both plants, work order release, labor and material confirmations, test data collection, shipping, export screening, and finance. About 300 office users work in the ERP, and about 420 production workers, supervisors, and test technicians use the MES through 62 kiosks.

**Major components:**
| ID | Component | Hosting and service model |
|---|---|---|
| SYS-01 | Commercial ERP with an advanced planning and scheduling (APS) module | Virtual machines and a managed database in the ERP production account of the cloud landing zone (IaaS/PaaS, vendor-agnostic) |
| SYS-02 | Identity provider for single sign-on and MFA, synchronized from the corporate directory | SaaS; 2 domain controllers at HQ |
| SYS-03 | Integration platform (ERP to MES at both plants; EDI) | Virtual machines in the ERP production account |
| SYS-05 | MES and kiosks: Plant 1 MES in the Plant 1 OT DMZ with 40 kiosks; Plant 2 legacy MES with 22 kiosks | On premises |
| SYS-09 (part) | About 180 planning, purchasing, quality, and finance endpoints; SD-WAN; the IT/OT boundary firewalls at both plants | Company-managed |
| SYS-14 (part) | EPSP use cases in the MSSP-operated SIEM | SaaS |
| Landing zone (part) | Management and security, shared services, ERP production, and backup accounts | Public cloud (P04) |

The PLM vault (SYS-04), plant control systems (SYS-06), test systems (SYS-07), historians (SYS-08), the EDI provider (SYS-10), the FMS (SYS-13), and the HR and payroll SaaS (SYS-16) connect to the EPSP as interconnected systems (section 8).

## 3. Laws, Regulations, and Policies Affecting the System
No federal or state law regulates the security of this system directly. Its obligations come from contracts, plus one records rule. Applicability is analyzed in P03 section 1.

| ID | Requirement | Citation | How it affects the EPSP |
|---|---|---|---|
| FAR clause | Basic Safeguarding of Covered Contractor Information Systems | FAR 52.204-21 (in 3 federal contracts) | The ERP, email, and labeled project sites hold FCI (agency specifications, delivery schedules, test reports), so the EPSP is a covered contractor information system. Its 15 safeguards are mapped in `control-implementation.csv` |
| FAR clauses | Covered telecommunications and video surveillance equipment; Kaspersky covered articles; FASCSA orders | FAR 52.204-25, 52.204-23, 52.204-30 | Apply company-wide. The EPSP holds the purchasing records used for the inquiries and the reports (P03 G-124 to G-126) |
| Contract | Utility Supplier Cyber Security Addenda (31 utilities) | Flow-down of NERC CIP-013-2 R1 Part 1.2 topics | Incident notice (24 or 48 hours), access-revocation notice (1 business day), and vulnerability disclosure depend on EPSP data and on the incident response process |
| C-CRITICAL-MFG-R03 | EAR recordkeeping | 15 CFR 762.6(a) | Export screening and shipping records are kept in the ERP (5-year minimum; kept 7) |
| C-CRITICAL-MFG-R01 | CIRCIA (proposed, not in force) | Proposed 6 CFR Part 226 (89 FR 23644) | Tracked only. If finalized as proposed, an incident affecting the EPSP could be reportable to CISA (P03 G-134) |
| State | Florida Information Protection Act | Fla. Stat. 501.171 | Employee personal information in the ERP payroll interface and HR exports |
| Benchmark | NIST CSF 2.0 with SP 800-82 Rev. 3 | Voluntary | The company's chosen benchmark; full profile in P03 |
| Internal | Security policies POL-01 to POL-05 and standards STD-01 to STD-10 | P06 | Policy basis for every control |

**Not applicable:** NERC CIP-013-2 as a direct obligation (the company is not a registered entity; P03 G-133), DFARS 252.204-7012 and CMMC (C-CRITICAL-MFG-R04; no DoD work; P03 G-137), and the ICTS connected vehicles rule (C-CRITICAL-MFG-R02; P03 G-135).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Chief Operating Officer (system owner) on 2026-09-15, after the control assessment (P07) and before the audit committee meeting the same day.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization to operate. The equivalent internal decision:
- **Decision:** continued operation of the EPSP accepted with conditions, 2026-09-15.
- **Authorizing official equivalent:** Chief Executive Officer for High and Very High risks; Chief Operating Officer for Moderate and below (P01 acceptance authorities).
- **Conditions:**
  - the Plant 2 MES service account must be removed from the corporate Domain Admins group and the two-way domain trust reduced to a one-way trust by 2026-10-31 (POAM-002);
  - the Plant 2 MES dual-homing must be removed before any new Plant 2 system is connected to the EPSP (POAM-001);
  - High-risk POA&M items must meet their milestones, with status reported to the audit committee each quarter;
  - re-decision by 2027-09-30 or after a major change (the 2027 Plant 2 MES migration counts as one).
### 4.3 System Operational Status
Operational. Major modifications planned:
- Plant 2 OT DMZ, removal of MES dual-homing, and the move of Plant 2 to the Plant 1 MES (P01 R-001), due 2027-06-30
- Retirement of the Plant 2 legacy directory domain (P01 R-051), due 2027-03-31
- Onboarding of both MES instances and the integration platform to the SIEM (P01 R-005), due 2027-01-31

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Chief Operating Officer | Accountable for the EPSP; accepts Moderate risk; executive sponsor of the security program |
| Authorizing official equivalent (High risk) | Chief Executive Officer | Accepts High risk; approved the risk appetite |
| Oversight | Board audit committee | Quarterly cyber risk reporting |
| Program strategy | vCISO (part-time contractor) | Program strategy, board reporting, annual SSP review |
| Security lead | Security Manager | Day-to-day security of the EPSP; MSSP oversight; incident commander |
| Technical owner | IT Director | ERP, integration platform, landing zone, SD-WAN, endpoints, backups; recovery lead |
| OT security lead | OT Security Engineer | IT/OT boundary firewalls, OT DMZ, remote access gateway, MES security at both plants |
| Plant systems owner | Director of Manufacturing Engineering | Approves plant-side changes to the MES and OT interfaces |
| Business owners | Production Planning Manager (schedule, MES users); Controller (ERP finance); Director of Supply Chain (purchasing, EDI); Plant Managers (kiosks, supervisors) | Access approvals and data quality for their modules |
| Contract obligations | General Counsel; Contracts and Trade Compliance Manager | FAR clauses, utility addenda notices, export records |
| Independent assessment | Co-sourced internal audit firm with an OT specialist subcontractor | Annual IT audit; the P07 assessment |
| Monitoring | MSSP | 24x7 monitoring of EDR, SIEM, identity, cloud, and the Plant 1 OT sensor |

## 6. System Information Types and System Categorization
Information types were chosen with reference to NIST SP 800-60. Types that SP 800-60 does not describe (production control, product test records, and proprietary design data) are organization-defined. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Supply chain management (goods acquisition, inventory control, logistics) | Moderate | Moderate | Moderate | Supplier pricing and bills of materials are sensitive; wrong quantities or shipments hurt customers; key stock lasts about 2 weeks (P05 BP-11, BP-12) |
| Production planning and control (organization-defined) | Low | Moderate | Moderate | A wrong work order or recipe reference yields a nonconforming transformer; the MES holds about 2 shifts of work (P05 BP-01 MTD 48 h) |
| Product test records (organization-defined) | Low | Moderate | Moderate | Certified test reports are product integrity evidence for utilities and federal customers (P05 BP-04 and BP-07, RPO 1 h) |
| Proprietary design data referenced by the ERP and MES (organization-defined) | Moderate | Moderate | Low | Bills of materials and winding specifications are trade secrets |
| Federal contract information (organization-defined) | Low | Low | Low | FCI requires basic safeguarding under FAR 52.204-21 |
| Financial management (accounting, payments, collections) | Moderate | Moderate | Low | Payment fraud risk; invoices can wait a few days (P05 BP-16) |
| Human resources management (payroll interface, employee records) | Moderate | Low | Low | Employee personal information subject to Fla. Stat. 501.171 |
| System and network monitoring (security logs) | Moderate | Moderate | Low | Needed for investigations and for utility and FAR notices |
| **EPSP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Availability was considered for High.** A 5-day outage of both plants would defer about $6.8 million of shipments and slip storm-restoration orders (P05). The team kept availability at Moderate for three reasons: work can continue for about 2 shifts from MES buffers and then on paper travelers, drying ovens run stored recipes from local PLCs, and the backlog means most lost output is deferred rather than lost. To compensate, the plan adds recovery-focused tailoring (section 10.1). **Integrity was considered for High** because of certified test reports; it stays Moderate because Quality signs every report against raw test data.

## 7. Authorization Boundary Description
**Inside the boundary:**
- the ERP and APS virtual machines, managed database, and integration platform in the ERP production account;
- the management and security, shared services, and backup accounts as they serve the EPSP (guardrails, network hub, log archive, ERP backups);
- the identity provider tenant and the 2 corporate domain controllers that feed it;
- the Plant 1 MES and its OT DMZ servers, and the Plant 2 MES server and database;
- the 62 kiosks;
- about 180 planning, purchasing, quality, and finance endpoints;
- the SD-WAN edges, the site firewalls, and the IT/OT boundary firewalls at both plants;
- the EPSP use cases in the SIEM tenant.

**Outside the boundary (interconnected systems):** the PLM vault (SYS-04), plant control systems (SYS-06), test systems (SYS-07), historians (SYS-08), EDI provider (SYS-10), productivity suite (SYS-11), FMS (SYS-13), HR and payroll SaaS (SYS-16), AI services (SYS-17), the Plant 2 legacy directory domain, and the cloud provider's and MSSP's infrastructure.

**Boundary weaknesses:**
- The Plant 2 MES server has an interface on the Plant 2 plant network as well as the office network. Until POAM-001 closes, the Plant 2 plant network is reachable through a component inside this boundary.
- The Plant 2 legacy domain trusts the corporate domain both ways, and the P07 test found the Plant 2 MES service account in the corporate Domain Admins group. Until POAM-002 closes, a compromise of the Plant 2 domain can reach the corporate domain.

The cloud architecture diagram is in P04 `cloud-architecture.md`. The Plant 1 IT/OT data flow diagram is part of the 2025 OT DMZ design; the Plant 2 diagram is in draft (P03 G-034).

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| EDI network provider (SYS-10) | Bidirectional (through SYS-03) | Purchase orders, advance ship notices, invoices | EDI provider contract; trading partner agreements |
| PLM vault (SYS-04) | Inbound | Released bills of materials and drawing references | Internal; documented for Plant 1 only |
| Plant 1 control systems (SYS-06) | MES to HMIs through the OT DMZ | Work order and recipe identifiers | Internal; documented in the OT DMZ design |
| Plant 2 control systems (SYS-06) | MES to HMIs on the flat network | Work order and recipe identifiers | Internal; **no documented flow (gap, CA-3)** |
| Test systems (SYS-07) | Inbound to the MES | Test results for certified test reports | Internal; checksummed at Plant 1, **no integrity check at Plant 2 (gap, SI-7)** |
| Plant 2 legacy domain | Two-way trust | Authentication | **No written terms (gap, CA-3; POAM-002)** |
| AI-001 forecasting service | Outbound nightly extract | Order history and backlog | Internal; covered in P10 |
| HR and payroll SaaS (SYS-16) | Outbound | Labor hours | Service agreement |
| Utilities and developers | Via EDI and email | Orders, ship notices, invoices | Supply agreements; 31 with security addenda |
| ERP software vendor | Inbound support sessions | Named guest accounts with MFA, enabled per ticket | Support agreement |
| MSSP | Inbound logs; response actions | Security logs; EDR isolation | MSSP contract (SOC 2 Type 2, Security) |
| Bank | Outbound | Payment files | Banking agreement with call-back verification |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| ERP application servers (4) and APS server (1) | Cloud virtual machines | ERP production account | IT Director |
| ERP database | Managed database service | ERP production account | IT Director |
| Integration platform servers (2) | Cloud virtual machines | ERP production account | IT Director |
| ERP backups | Database copies with 35-day write-once retention | Backup account, second region | IT Director |
| Network hub, cloud firewall, SD-WAN termination, log archive | Network and logging services | Shared services account | IT Director |
| Organization guardrails, posture and threat detection | Policy and security services | Management and security account | Security Manager |
| Identity provider tenant | SaaS | Identity vendor | IT Director |
| Corporate domain controllers (2) | Windows servers | HQ server room | IT Director |
| Plant 1 MES application and database servers; OT backup server | Virtual servers | Plant 1 OT DMZ | Production Planning Manager (business); OT Security Engineer (technical) |
| Plant 2 MES server and database | Physical server, dual-homed (**gap**) | Plant 2 server room | Production Planning Manager (business); IT Director (technical) |
| Kiosks (62) | Industrial PCs | Plant 1 (40), Plant 2 (22) | Plant Managers |
| Planning, purchasing, quality, and finance endpoints (about 180) | Laptops and desktops with EDR | HQ, Plant 1 and Plant 2 offices | IT Director |
| SD-WAN edges and site firewalls; IT/OT firewalls | Network | HQ and Plant 1; Plant 2 | IT Director; OT Security Engineer (IT/OT rules) |
| SIEM tenant use cases | SaaS | MSSP | Security Manager |

## 10. Control Implementation Details
### 10.1 Control implementation status
**Baseline and tailoring.** The EPSP uses the NIST SP 800-53B **Moderate** baseline (287 controls and enhancements), tailored as follows:
- **Documented here: 130 controls** in `control-implementation.csv`. They cover every control that implements one of the 15 FAR 52.204-21 safeguards, the controls that support the utility addendum duties, the controls behind the CSF 2.0 gaps in P03 for this boundary, and the Moderate controls that address the P01 risks (segmentation, privileged access, remote access, monitoring, recovery).
- **Selected by tailoring (added):** PM-1, PM-2, and PM-9. They are not in the Moderate baseline but are needed to govern a program that spans IT and two plants.
- **Recovery tailoring:** CP-2, CP-4, CP-9, and CP-10 statements explicitly include the MES and plant-side dependencies, not only the ERP, because the BIA shows the plants stop when the MES does.
- **Inherited without separate statements:** the remaining Moderate-baseline physical and environmental controls for cloud and SaaS data centers (for example PE-9 to PE-17), and platform-level SA and SC controls. These are inherited from the cloud provider, the identity vendor, and the MSSP, and are evidenced by their SOC 2 Type 2 reports, which are reviewed each year (P09 `vendor-soc2-review.csv`).
- **Deferred:** the other Moderate controls with no FAR mapping and no Moderate-or-higher risk in P01 (for example SA-11 developer testing, because the EPSP is commercial software that the company configures but does not develop). They are recorded as tailoring decisions and reviewed yearly. Secure development for the company's own product software is handled outside this boundary (P03 G-070; POAM-017).

**Status of the 130 documented controls:**
| Status | Count |
|---|---|
| Implemented | 44 |
| Partially implemented | 84 |
| Planned | 2 |
| Not applicable | 0 |

**Inheritance of the 130 documented controls:**
| Inheritance | Count | Main providers |
|---|---|---|
| System-specific | 88 | Company |
| Hybrid | 32 | Identity vendor, cloud provider, MSSP, SD-WAN provider, ERP software vendor |
| Common/Inherited | 10 | Identity vendor (for example AC-7, IA-2(2)), cloud provider (CP-6, SC-12, SC-5), MSSP (AU-6(1)), insurer panel and MSSP (IR-7) |

Most Partially implemented statements describe a control that works at HQ, in the cloud, and at Plant 1 but not yet at Plant 2. They trace to gaps 1 to 6 in `../00_company-facts.md` section 4 and to the P07 findings.

### 10.2 Control assessment status
The co-sourced internal audit firm, with an OT specialist subcontractor, assessed 33 of these controls from 2026-08-03 to 2026-08-21, with OT tests in the Saturday maintenance windows on 2026-08-08 (Plant 1) and 2026-08-15 (Plant 2). See P07 `assessment-plan.md`, `assessment-results.csv`, and `poam.csv`. Weaknesses are tracked in the POA&M and reported quarterly to the audit committee.

## 11. Digital Identity Acceptance Statement
Authentication assurance levels (AAL) follow the definitions in NIST SP 800-63B.
- **Office users (ERP, email, VPN):** password plus push MFA with number matching through the identity provider, under conditional access that checks device compliance (AAL2). This fits a Moderate system that holds FCI, supplier pricing, and payment data.
- **Administrators:** FIDO2 security keys for the 18 cloud, identity, and domain administrators (phishing-resistant, AAL2 or higher); push MFA through the privileged access broker for the other 23 privileged accounts. MES administrator accounts and OT engineering workstations will move to the broker with MFA by 2027-03-31 (POAM-016).
- **MES kiosks:** badge number and PIN (single-factor, AAL1). This is accepted because kiosks sit inside badge-controlled plants and can only confirm work, not change orders. The acceptance is conditional:
  - removing the 3 shared Plant 2 supervisor override accounts (POAM-004);
  - stopping badge number reuse at Plant 2;
  - revisiting badge-tap MFA when Plant 2 moves to the Plant 1 MES in 2027.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`); risk register (P01); gap analysis and roadmap (P03); cloud architecture and control map (P04); BIA (P05); policies and standards index (P06); assessment and POA&M (P07); incident runbooks and notification matrix (P08); SOC 2 readiness and vendor reviews (P09); AI governance assessment (P10).

## 13. Acronym List and Glossary
- **APS:** advanced planning and scheduling
- **DMZ:** demilitarized zone (a buffer network between IT and OT)
- **EDI:** electronic data interchange
- **EDR:** endpoint detection and response
- **EPSP:** ERP and Production Scheduling Platform
- **ERP:** enterprise resource planning
- **FCI:** federal contract information
- **FMS:** Fleet Monitoring Service
- **HMI:** human-machine interface
- **MES:** manufacturing execution system
- **MSSP:** managed security service provider
- **OT:** operational technology
- **POA&M:** plan of action and milestones
- **SD-WAN:** software-defined wide area network
- **TMU:** transformer monitoring unit

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-07-31 | Draft from the risk assessment and gap analysis | Security Manager |
| 1.0 | 2026-09-15 | Updated with P07 results (including the Plant 2 domain trust finding); approved by the Chief Operating Officer | Security Manager with the IT Director |
