# System Security Plan: ERP and Production Scheduling Platform (EPSP)

**Organization:** Cris Santos Company, LLC (power and distribution transformer manufacturer, Florida) | **Tier:** Small | **Vertical:** Critical Manufacturing
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-04

## 1. System Name and Identifier
ERP and Production Scheduling Platform (**EPSP**), identifier CSC-SYS-001.

## 2. System Overview
The EPSP runs the company's order-to-shipment flow for distribution and power transformers: customer orders, bills of materials, purchasing, inventory, the finite-capacity production schedule, work order release to the plant floor, labor and material confirmations, test data collection, shipping, export screening, and finance. About 118 office users work in the ERP, and about 160 production workers, supervisors, and test technicians use the MES through 25 shop-floor kiosks.

**Major components:**
- **SYS-01:** commercial ERP software with an advanced planning and scheduling (APS) module, installed on virtual machines in a public cloud tenant with a managed database
- **SYS-02:** a SaaS identity provider for single sign-on and MFA, synchronized from 2 on-premises directory servers
- **SYS-03:** an integration service on a cloud virtual machine that moves work orders to the MES and confirmations back, and exchanges EDI messages
- **SYS-05:** the manufacturing execution system (MES) server in the plant server room and 25 shop-floor kiosks
- **SYS-09 (part):** about 45 planning, purchasing, sales, quality, and finance endpoints; the internet-edge firewall; the internal IT/OT firewall; and the site-to-site VPN to the cloud tenant
- ERP backups (managed database backups and VM snapshots)

The cloud tenant is described by service category and is vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
No federal or state law regulates the security of this system directly. Its obligations come from contracts, plus one narrow records rule. Applicability is analyzed in P03 section 1.

| ID | Requirement | Citation | Relevance to the EPSP |
|---|---|---|---|
| FAR clause | Basic Safeguarding of Covered Contractor Information Systems | FAR 52.204-21 (in the federal contract) | The ERP and email hold FCI (agency specifications, delivery schedules, test reports), so the EPSP is a covered contractor information system |
| FAR clause | Prohibition on covered telecommunications and video surveillance equipment | FAR 52.204-25 | Applies to the whole company; 4 covered cameras were found outside this boundary (P03 G-080) |
| Contract | Utility Supplier Cyber Security Addenda (12 utilities) | Flow-down of NERC CIP-013-2 R1 Part 1.2 topics | Incident notice, access-revocation notice, and vulnerability disclosure depend on EPSP data and on the IR process |
| C-CRITICAL-MFG-R03 | EAR recordkeeping | 15 CFR 762.6 | Export screening and shipping records are kept in the ERP (5-year minimum) |
| C-CRITICAL-MFG-R01 | CIRCIA (proposed, not in force) | Proposed 6 CFR Part 226 (89 FR 23644) | Tracked only. If finalized as proposed, an incident affecting the EPSP could be reportable (P03 G-089) |
| State | Florida Information Protection Act (breach notice) | Fla. Stat. 501.171 | Employee personal information in the ERP payroll and HR modules |
| Benchmark | NIST CSF 2.0 with SP 800-82 Rev. 3 | Voluntary | The company's chosen benchmark (P03) |
| Internal | Security policies POL-01 to POL-05 | P06 | Approved 2026-09-04 |

**Not applicable:** NERC CIP-013-2 as a direct obligation (the company is not a registered entity; P03 G-088), DFARS 252.204-7012 (C-CRITICAL-MFG-R04; no DoD work), and the ICTS connected vehicles rule (C-CRITICAL-MFG-R02).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the VP Operations (system owner) on 2026-09-04.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization to operate. The equivalent internal decision:
- The VP Operations accepted continued operation of the EPSP on 2026-09-04, with the conditions in the P07 POA&M.
- The President approved dated treatment plans for the High and Very High risks in P01 on 2026-09-04 and accepted none of them.
- Condition: the MES dual-homing must be removed and the IT/OT firewall rules restricted (POAM-001) before the EPSP is extended to any new plant system.
### 4.3 System Operational Status
Operational. Major modifications planned:
- Move the MES and historian into an OT DMZ and remove MES dual-homing (P01 R-001), due 2027-03-31.
- Move ERP backups to a separate account and region with immutable retention (P01 R-002), due 2026-12-31.

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | VP Operations | Overall accountability; risk acceptance up to Moderate |
| Risk acceptor (authorizing official equivalent) | President | Acceptance of High and Very High risks |
| Security lead | IT Manager | Day-to-day security of the EPSP; identity provider and cloud tenant administration |
| OT security lead | Controls Engineer | The MES interface to plant systems; IT/OT firewall rules on the plant side |
| Business owners | Production Planning Manager (schedule, MES users); Controller (ERP finance); Supply Chain Manager (purchasing, EDI) | Access approvals and data quality for their modules |
| Contract obligations | Contracts and Compliance Manager | FAR clauses, utility addenda notices |
| Operations support | Managed service provider | After-hours help desk, patching, firewall management, backup monitoring |

## 6. System Information Types and System Categorization
Information types were chosen with reference to NIST SP 800-60. Types that SP 800-60 does not describe (production control and proprietary design data) are organization-defined. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Supply chain management (goods acquisition, inventory control, logistics) | Moderate | Moderate | Moderate | Supplier pricing and bills of materials are sensitive; wrong quantities or shipments hurt customers; plant runs short in about 2 weeks (P05 BP-07, BP-08) |
| Production planning and control (organization-defined) | Low | Moderate | Moderate | A wrong work order or recipe reference yields a nonconforming transformer; the MES holds about 2 shifts of work (P05 BP-01 MTD 48 h) |
| Product test records (organization-defined) | Low | Moderate | Moderate | Certified test reports are product integrity evidence for utilities (P05 BP-05 RPO 1 h) |
| Proprietary design data referenced by the ERP and MES (organization-defined) | Moderate | Moderate | Low | Bills of materials and winding specifications are trade secrets |
| Federal contract information (organization-defined) | Low | Low | Low | FCI requires basic safeguarding under FAR 52.204-21 |
| Financial management (accounting, payments, collections) | Moderate | Moderate | Low | Payment fraud risk; invoices can wait a few days (P05 BP-10) |
| Human resources management (payroll and employee records) | Moderate | Low | Low | Employee personal information subject to Fla. Stat. 501.171 |
| **EPSP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

Availability was held at Moderate, not High. A 2-day outage would be serious, with lost shipments and slipped storm orders, but manual scheduling and paper travelers can keep work moving (P05).

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 200-person manufacturer. The plan documents 74 controls (see `control-implementation.csv`): those that implement FAR 52.204-21, support the utility addendum duties, or address the CSF 2.0 gaps in P03 for this boundary. Every other Moderate-baseline control is treated as follows:
- **Inherited** from the cloud provider, identity provider, and MSP, with evidence from their SOC 2 reports (P09 reviewed the MSP report; the other providers' reports are being requested, see SA-9).
- **Out of scope for this tier**, recorded as a tailoring decision, where the control's purpose applies only to federal systems.

## 7. Authorization Boundary Description
- **Inside:** the ERP and APS virtual machines, managed database, and backups in the cloud tenant; the integration service VM; the identity provider tenant and the 2 directory servers that feed it; the MES server and its database; the 25 kiosks; about 45 planning, purchasing, sales, quality, and finance endpoints; the internet-edge firewall, the IT/OT firewall, and the site-to-site VPN.
- **Outside (interconnected systems):** the PLM vault (SYS-04), plant control systems (SYS-06), test bay (SYS-07), historian (SYS-08), EDI network provider (SYS-10), productivity suite (SYS-11), AI services (SYS-14), and the cloud provider's infrastructure.
- **Boundary weakness:** the MES server has a network interface on the plant network as well as the office network. Until POAM-001 closes, the plant network is reachable through a component inside this boundary.

The cloud architecture diagram is in P04 `cloud-architecture.md`. The IT/OT data flow diagram is being drawn (P03 G-020, due 2026-11-30).

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| EDI network provider (SYS-10) | Bidirectional (through SYS-03) | Purchase orders, advance ship notices, invoices | EDI provider contract; trading partner agreements |
| PLM vault (SYS-04) | Inbound | Released bills of materials and drawing references | Internal; interface not documented (gap, P03 G-020) |
| Plant control systems (SYS-06) | MES to HMIs | Work order and recipe identifiers | Internal; **no documented flow (gap)** |
| High-voltage test bay (SYS-07) | Inbound to MES | Test results for certified test reports | Internal; **no integrity check (gap)** |
| AI-001 forecasting service (SYS-14) | Outbound from ERP | Order history and backlog | Internal; covered in P10 |
| Utilities and developers | Via EDI and email | Orders, ship notices, invoices | Supply agreements; 12 with security addenda |
| ERP software vendor | Inbound support sessions | Support access on request | Support agreement; per-ticket VPN account |
| MSP | Inbound management | RMM agent on IT servers and endpoints | MSP contract (SOC 2 Type 2, Security) |
| Bank and payroll provider | Outbound | Payment files, payroll data | Service agreements |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| ERP application servers (2) and APS server (1) | Cloud virtual machines | Cloud tenant, one region | IT Manager |
| ERP database | Managed database service | Cloud tenant | IT Manager |
| Integration service | Cloud virtual machine | Cloud tenant | IT Manager |
| ERP backups | Database backups and VM snapshots | Same account and region as production (**gap**) | IT Manager |
| Site-to-site VPN gateway | Cloud network service and campus firewall | Cloud tenant and HQ | IT Manager (MSP managed) |
| Identity provider tenant | SaaS | Identity vendor | IT Manager |
| Directory servers (2) | Windows servers | HQ server room | IT Manager |
| MES server and database | Physical server, dual-homed (**gap**) | Plant server room | Production Planning Manager (business); IT Manager (technical) |
| Shop-floor kiosks (25) | Industrial PCs | Bays A and B, tank shop, test bay | Production Planning Manager |
| Planning, purchasing, sales, quality, finance endpoints (about 45) | Laptops and desktops with EDR | HQ and plant offices | IT Manager |
| Internet-edge firewall (HA pair) and IT/OT firewall | Next-generation firewalls | HQ and plant server rooms | IT Manager (MSP managed); Controls Engineer (plant rules) |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 74 controls:
- Implemented: 18
- Partially implemented: 41
- Planned: 15
- Not applicable: 0

### 10.2 Control assessment status
22 of these controls were assessed 2026-08-10 to 2026-08-15, including OT tests on 2026-08-15. See P07 `assessment-results.csv` and `poam.csv` (19 POA&M items).

## 11. Digital Identity Acceptance Statement
Authentication assurance levels (AAL) follow the definitions in NIST SP 800-63B.
- **ERP, email, VPN, and cloud console:** a password plus a phone authenticator app through the identity provider (AAL2). This fits a Moderate system that holds FCI, supplier pricing, and payment data.
- **Administrators:** hardware security keys (phishing-resistant, AAL2 or higher) for the 3 IT administrators.
- **MES kiosks:** badge number and PIN (single-factor, AAL1). This is accepted for now because the kiosks are inside the badge-controlled plant and can only confirm work, not change orders or recipes. The acceptance is conditional:
  - removing the shared supervisor override accounts (POAM-013);
  - revisiting badge-tap MFA when the MES is rebuilt in the OT DMZ.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`); risk register (P01); gap analysis (P03); cloud control map and diagram (P04); BIA (P05); policies POL-01 to POL-05 (P06); assessment and POA&M (P07); ransomware runbook and notification matrix (P08); security self-benchmark and MSP SOC 2 review (P09); AI risk assessment (P10).

## 13. Acronym List and Glossary
- **APS:** advanced planning and scheduling
- **DMZ:** demilitarized zone (a buffer network between IT and OT)
- **EDI:** electronic data interchange
- **EDR:** endpoint detection and response
- **EPSP:** ERP and Production Scheduling Platform
- **ERP:** enterprise resource planning
- **FCI:** federal contract information
- **HMI:** human-machine interface
- **MES:** manufacturing execution system
- **MSP:** managed service provider
- **OT:** operational technology
- **POA&M:** plan of action and milestones
- **TMU:** transformer monitoring unit

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.1 | 2026-08-07 | Draft for the control assessment | IT Manager |
| 1.0 | 2026-09-04 | Updated with P07 results and approved | IT Manager |
