# System Security Plan: CUI Engineering Enclave (CEE)

**Organization:** Cris Santos Company, LLC (aircraft parts manufacturer, DoD subcontractor) | **Tier:** Small | **Vertical:** Defense Industrial Base
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 2.0, 2026-08-31 (replaces v1.0 of 2024-08-30)
**Requirement set:** NIST SP 800-171 Rev. 2 (110 requirements), as required by DFARS 252.204-7012(b)(2) and CMMC Level 2 (32 CFR 170.14(c)(3))

## 1. System Name and Identifier
CUI Engineering Enclave (**CEE**), identifier CSC-SYS-CEE-01. This SSP satisfies SP 800-171 requirement 3.12.4 and is the SSP named in SPRS submissions under DFARS 252.204-7019 and 252.204-7020.

## 2. System Overview
The CEE is where the company receives, creates, stores, and uses controlled technical information (CTI) for its DoD subcontracts: controlled drawings, 3D models, specifications, NC programs, and the travelers and work instructions built from them. It supports engineering, manufacturing engineering, quality, and shop-floor production for Prime A and Prime B parts, some of which are ITAR defense articles. About 50 named users hold enclave accounts; about 40 machine operators see CUI through MES terminals and printed drawings.

**Major components** (IDs from `../scenario-facts.md` section 3):
- **SYS-01:** enclave identity provider (single sign-on, MFA, device compliance), government-community cloud
- **SYS-02:** enclave collaboration suite (CUI email, file storage, chat), government-community cloud
- **SYS-03:** enclave cloud subscription (PLM VMs, virtual desktops, SFTP gateway, log workspace, key vault, backup vault)
- **SYS-04:** CAD/PLM (CAD on engineering workstations, PLM on SYS-03)
- **SYS-05:** 24 CAD workstations and 16 enclave laptops
- **SYS-06:** MES and DNC servers and 14 shop-floor terminals
- **SYS-07:** 38 CNC machines and 4 coordinate measuring machines (Specialized Assets)
- **SYS-08:** plant enclave network (enclave firewall, engineering and shop-floor VLANs, site-to-site VPN, shop-floor printers)
- **SYS-12 (company side):** SFTP gateway, site-to-site VPN, and virtual desktop access to Prime A's supplier portal

The cloud services are described by service category and are vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it affects the CEE |
|---|---|---|---|
| C-DIB-R01 | DFARS 252.204-7012 (MAY 2024) | 48 CFR 252.204-7012 | SP 800-171 on covered contractor information systems; FedRAMP Moderate-equivalent cloud; 72-hour reporting; malware to DC3; 90-day image preservation; flowdown |
| C-DIB-R02 | CMMC Program and DFARS 252.204-7021 (NOV 2025) | 32 CFR Part 170; 48 CFR 252.204-7021 | Level 2 (C3PAO) status required for Prime A awards from Phase 2 (2026-11-10); scoping per 170.19(c); scoring per 170.24; POA&M limits per 170.21 |
| C-DIB-R03 | DFARS 252.204-7019 and 252.204-7020 (NOV 2023) | 48 CFR 252.204-7019, 252.204-7020 | Current SP 800-171 DoD Assessment score in SPRS; Government assessment access |
| C-DIB-R04 | FAR 52.204-21 (NOV 2021) | 48 CFR 52.204-21 | Basic safeguarding for FCI (also on corporate systems outside this boundary) |
| C-DIB-R05 | ITAR | 22 CFR Parts 120-130 | Release of technical data to foreign persons is an export (22 CFR 120.56); U.S.-person access control; encrypted-data carve-out conditions (22 CFR 120.54(a)(5)) |
| C-DIB-R06 | EAR | 15 CFR Parts 730-774 | Same principles for EAR-controlled technology on commercial parts (15 CFR 734.18(a)(5)) |
| CUI program | CUI Basic safeguarding | 32 CFR 2002.14 | CUI Basic is protected at no less than moderate confidentiality (2002.14(a)(3)); physical barrier outside controlled environments (2002.14(c)(3)) |
| Internal | Security policies POL-01 to POL-05 | P06 | Program rules |

Not applicable:
- **NISPOM (C-DIB-R07, 32 CFR Part 117):** the company holds no facility clearance and no classified information.
- **CIRCIA (6 U.S.C. 681b):** the final rule is not published; nothing is required yet.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Vice President of Operations on 2026-08-31. The President, as CMMC Affirming Official, reviewed it on the same date.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no authorization to operate. The equivalent internal decisions:
- The Vice President of Operations accepted continued operation of the CEE on 2026-08-31, subject to the POA&M in P07.
- The President approved the High-risk treatment plans in P01 and the remediation budget.
- External validation will come from the CMMC Level 2 certification assessment (target window 2027-02-15 to 2027-02-26).
### 4.3 System Operational Status
Operational. Planned major changes: MES authentication through SYS-01 with MFA (2026-11-30), FIPS mode on the SFTP gateway and plant VPN (2026-11-30), DNC connection for the 6 legacy CNC machines (2027-01-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Vice President of Operations | Accountability for the CEE; accepts Moderate risk |
| Risk acceptor and CMMC Affirming Official | President (majority owner) | High and Very High risk acceptance; SPRS affirmations (32 CFR 170.22) |
| CUI data owner | Director of Engineering | Decides what is CUI; approves access to engineering data |
| Security lead | IT Manager | SSP and POA&M owner; incident commander |
| System administrators | Systems Administrators (2) | Cloud tenant, identity provider, endpoints |
| OT owner | Manufacturing Systems Engineer | MES, DNC, CNC and CMM connectivity |
| Printed CUI owner | Quality Manager | Drawing distribution, travelers, shop-floor document control |
| Contracts and export compliance | Contracts Manager (ITAR Empowered Official) | Flowdowns, SPRS submissions, DIBNet reporting, prime notifications |

## 6. System Information Types and System Categorization
Information types are from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199. CUI Basic cannot be protected below moderate confidentiality (32 CFR 2002.14(a)(3)).

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Controlled technical information (drawings, models, NC programs) | Moderate | Moderate | Moderate | Disclosure harms national security programs and violates export controls; a wrong dimension or NC program produces nonconforming flight parts; outage stops production (P05 MTD 24 h for shop-floor release) |
| Production and quality records (travelers, inspection data) | Moderate | Moderate | Low | Records prove conformance to the prime; they can be recreated from paper in the short term |
| Identity and security data (accounts, logs) | Moderate | Moderate | Moderate | Protects the enclave itself |
| **CEE category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Requirement baseline.** The binding requirement set is the 110 SP 800-171 Rev. 2 requirements. Each requirement's implementation statement is in `sp800-171-requirement-statements.csv` (110 rows, linked to the gap analysis in P03). `control-implementation.csv` documents 100 SP 800-53 Rev. 5 controls (99 from the Moderate baseline, plus PM-9 by tailoring). They are the controls NIST's SP 800-171 Rev. 3 CUI overlay maps to those requirements, plus contingency, inventory, supply chain, and policy controls the company needs. Other Moderate-baseline controls are either inherited from the cloud provider (per its customer responsibility matrix) or outside this tier's scope.

## 7. Authorization Boundary Description
The boundary follows the CMMC Level 2 asset categories in 32 CFR 170.19(c)(1):

| Category | Assets in the CEE | Treatment |
|---|---|---|
| CUI Assets | SYS-02, SYS-03 (PLM, virtual desktops, SFTP gateway, backup vault), SYS-04, SYS-05, SYS-06 (MES, DNC, 14 terminals), printed drawings and travelers | Assessed against all 110 requirements |
| Security Protection Assets | SYS-01, enclave firewall and VLAN switches, EDR console, log workspace, key vault | Assessed against the requirements relevant to their function |
| Specialized Assets | SYS-07: 38 CNC machines and 4 CMMs (operational technology) | Inventoried, shown on the diagram, managed under risk-based practices (section 9); not assessed against other requirements |
| Contractor Risk Managed Assets | None designated | Not used |
| Out-of-Scope Assets | SYS-09 corporate network and endpoints, SYS-11 payroll and HR SaaS | Physically or logically separated by the enclave firewall. The MSP has no enclave access |
| Open scoping question | SYS-10 ERP (DoD purchase order data, FCI) | Position requested from Prime A under DFARS 252.204-7021(d)(2), due 2026-10-31 (P03 G-125) |

**External service provider.** The government-community cloud provider is a CSP that processes CUI, so it must meet the FedRAMP requirements in DFARS 252.204-7012 (32 CFR 170.19(c)(2), Table 4). Its offering is FedRAMP authorized at Moderate or higher. Its customer responsibility matrix (CRM) is referenced in this SSP, as 32 CFR 170.17(c)(5)(iii) requires. The plant network connecting to the CSP is inside the boundary.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Path | Agreement |
|---|---|---|---|---|
| Prime A supplier portal | Bidirectional | Drawings, models, quality data | Browser from enclave virtual desktops (prime-hosted) | Subcontract (DFARS 252.204-7012 flowed down) |
| Prime B | Bidirectional | Drawings, models, NC programs | SFTP gateway (SYS-12b). **FIPS mode not confirmed (gap)** | Subcontract (DFARS 252.204-7012 flowed down) |
| Outside processors (plating, heat treat, NDT) | Outbound | Drawings needed for the process | SFTP gateway; paper copies with parts. **No DFARS flowdown (gap)** | Purchase orders |
| Plant to cloud tenant | Bidirectional | All CEE traffic from the plant | Site-to-site VPN (SYS-12c). **FIPS mode not confirmed (gap)** | Internal |
| Corporate network (SYS-09) | None for CUI | Firewall allows only time sync and print release to corporate services | Enclave firewall | Internal |
| ERP (SYS-10) | Outbound from ERP to MES | Work order numbers, quantities, due dates (no drawings) | Scheduled file drop to MES | Internal (scoping question open) |
| Public generative AI services | **Blocked from 2026-10-31** | Engineers pasted CUI text before this plan (P10) | Web | None. Prohibited |

## 9. System Component Inventory
| Component | Type | Location or provider | CMMC category | Owner |
|---|---|---|---|---|
| Identity provider tenant (64 accounts) | SaaS | Government-community cloud | Security Protection Asset | IT Manager |
| Collaboration suite tenant | SaaS | Government-community cloud | CUI Asset | IT Manager |
| PLM application and database VMs (2) | IaaS VMs | Enclave subscription | CUI Asset | Director of Engineering |
| Virtual desktop pool (20 sessions) | PaaS | Enclave subscription | CUI Asset | Systems Administrators |
| SFTP gateway VM | IaaS VM (own subnet) | Enclave subscription | CUI Asset | Systems Administrators |
| Log workspace, key vault, backup vault | PaaS | Enclave subscription | Security Protection Assets | Systems Administrators |
| CAD workstations (24), enclave laptops (16) | Endpoints | Engineering wing; mobile | CUI Assets | Systems Administrators |
| MES server, DNC server, 14 terminals | On-premises servers and thin clients | Shop-floor VLAN | CUI Assets | Manufacturing Systems Engineer |
| CNC machines (38: 32 DNC-connected, 6 USB-loaded) and CMMs (4) | Operational technology | Shop floor | Specialized Assets | Manufacturing Systems Engineer |
| Enclave firewall, VLAN switches | Network | Server room | Security Protection Assets | Systems Administrators |
| Shop-floor printers (3) | Output devices | Open aisles (**gap**) | CUI Assets | Quality Manager |
| Printed drawings and travelers | Paper media | Cells, inspection, shipping | CUI (media) | Quality Manager |

**Specialized Asset treatment (SP 800-171 3.4.1; DFARS 252.204-7012(b)(3)).** CNC controllers run vendor-embedded operating systems that the company cannot patch or harden. Compensating measures: the machines sit on the shop-floor VLAN with no internet route; they accept programs only from the DNC server (32 machines) or, until 2027-01-31, from labeled and inventoried USB drives (6 machines); vendor remote support is supervised; the machines are listed in the asset inventory and the P04 diagram.

## 10. Control Implementation Details
### 10.1 Implementation status
**By requirement** (`sp800-171-requirement-statements.csv`, 110 rows):
- Implemented: 45
- Partially implemented: 46
- Planned: 18
- Not applicable: 1 (3.13.14, no VoIP in the boundary)

**By SP 800-53 control** (`control-implementation.csv`, 100 rows):
- Implemented: 29
- Partially implemented: 56
- Planned: 15

**Inheritance:** 70 system-specific, 27 hybrid, 3 common/inherited from the cloud provider. Inherited and hybrid statements rely on the provider's CRM and FedRAMP authorization package.

### 10.2 Assessment status and score
- Readiness assessment 2026-08-03 to 2026-08-07: see P07.
- Gap analysis: see P03. Recalculated score under 32 CFR 170.24: **-65** (the 2024 SPRS entry of 96 is withdrawn and will be corrected by 2026-09-30).
- Enduring exceptions: CNC controller patching and hardening (Specialized Assets, section 9).

## 11. Digital Identity Acceptance Statement
Enclave users authenticate to SYS-01 with a password and a phishing-resistant or app-based second factor. Administrators use hardware security keys. Access also requires an enrolled, compliant device. This meets SP 800-171 3.5.3 for enclave services and is appropriate for Moderate confidentiality.

**Exception until 2026-11-30:** MES terminals use shared local logins without MFA. The planned fix is MES sign-in through SYS-01 with badge plus PIN at the terminal (P07 POAM-003).

## 12. Referenced Artifacts
Scenario facts (`../scenario-facts.md`); requirement statements (`sp800-171-requirement-statements.csv`); risk register (P01); gap analysis and score (P03); cloud control map and diagram (P04); BIA (P05); policies (P06); assessment and POA&M (P07); incident response runbook (P08); SOC 2 readiness (P09); AI assessment (P10); cloud provider CRM and FedRAMP Marketplace record (kept by the IT Manager).

## 13. Acronym List and Glossary
- **C3PAO:** CMMC Third-Party Assessment Organization
- **CDI:** covered defense information
- **CMMC:** Cybersecurity Maturity Model Certification
- **CRM:** customer responsibility matrix
- **CTI:** controlled technical information
- **CUI:** Controlled Unclassified Information
- **DNC:** direct numerical control (NC program distribution)
- **FCI:** Federal contract information
- **MES:** manufacturing execution system
- **POA&M:** plan of action and milestones
- **SPRS:** Supplier Performance Risk System

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2024-08-30 | Initial plan (cloud enclave only) | IT Manager |
| 2.0 | 2026-08-31 | Full rewrite: added MES, DNC, Specialized Assets, printed CUI, SFTP gateway, virtual desktops, asset categories, 110 requirement statements | IT Manager |
