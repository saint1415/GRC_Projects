# System Security Plan: Group CUI Engineering Enclave (GCEE)

**Organization:** Cris Santos Company Holdings, Inc. (corporate shared services, serving the Aircraft Parts and Engineering Services divisions) | **Tier:** Multi-Sector | **Vertical:** Defense Industrial Base
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 3.0, 2026-09-15
**Requirement set:** NIST SP 800-171 Rev. 2 (110 requirements), as required by DFARS 252.204-7012(b)(2) and CMMC Level 2 (32 CFR 170.14(c)(3)); SP 800-53 Rev. 5 Moderate baseline for control implementation detail

> **Why this system.** At this tier the SSP can cover one system per division or a shared corporate system. The group chose the **GCEE**, a shared corporate system, because both CUI divisions keep their drawings, models, specifications, and test reports in one PLM environment; it inherits most of its controls from corporate (SYS-G1, SYS-G2, SYS-G3, SYS-G5); and it carries the group's top risk (P01 GR-01). Each plant keeps a plant enclave SSP for its MES, DNC, and machines (SYS-D1), and Defense Software keeps its own plans for SYS-D3 (DoD authorization package) and SYS-D4. All of them inherit from the same common control catalog (`common-control-catalog.csv`).

## 1. System Name and Identifier
Group CUI Engineering Enclave (**GCEE**), identifier CSCH-SYS-G3-CEE. It is the core of the **Enterprise CUI Environment**, the planned CMMC Level 2 assessment scope that also includes plants 1 to 8 and the Engineering Services centers (`../00_company-facts.md` section 6). This SSP satisfies SP 800-171 requirement 3.12.4 for the GCEE and is named in SPRS submissions under DFARS 252.204-7019 and 252.204-7020.

## 2. System Overview
The GCEE is where the group receives, creates, stores, and releases controlled technical information (CTI) for its DoD contracts and subcontracts: drawings, 3D models, specifications, NC programs and additive build files, stress and test reports, and the inspection plans built from them. It supports:
- **Aircraft Parts:** design, change control, and release to 9 plants (Plant 9 is not yet connected; scenario gap 1).
- **Engineering Services:** design, analysis, and test reporting for DoD program offices and primes.
- **Program H:** a separate project enclave inside the GCEE with tighter access and monitoring, the intended Level 3 (DIBCAC) scope (32 CFR 170.19(e)).

About 12,600 named users (6,900 Aircraft Parts, 5,200 Engineering Services, 120 Defense Software support and integration staff, 380 corporate platform and security staff) and 140 service accounts use it. The PLM vault holds about 4.8 million controlled documents.

**Major components** (all in the SYS-G3 government-community landing zone on provider A, with the backup vault in a second provider A region):
- **PLM application and database:** application servers (IaaS virtual machines) and a managed database
- **PLM vault:** object storage for controlled documents, with customer-managed keys
- **CAD virtual workstation pool:** GPU virtual desktops for about 2,400 concurrent sessions
- **Thick CAD workstations:** about 1,100 managed workstations at plants and centers for very large assemblies (CUI Assets)
- **Engineering data exchange gateway:** managed file transfer and secure web transfer for primes, DoD, and suppliers, in its own DMZ subnet
- **Program H project enclave:** a separate account with its own vault, keys, and access group
- **Key management and immutable backup vault**

Engineering laptops that reach CAD only through the virtual desktop service are configured so that nothing beyond keyboard, video, and mouse reaches the endpoint; they are Out-of-Scope Assets under 32 CFR 170.19(c)(1). The services are described by category and are vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies to the GCEE |
|---|---|---|---|
| C-DIB-R01 | DFARS 252.204-7012 (MAY 2024) | 48 CFR 252.204-7012 | SP 800-171 on covered contractor information systems; external cloud providers holding CDI must meet security requirements equivalent to the FedRAMP Moderate baseline and paragraphs (c) to (g) ((b)(2)(ii)(D)); 72-hour reporting; malware to DC3; 90-day image preservation; flowdown ((m)) |
| C-DIB-R02 | CMMC Program and DFARS 252.204-7021 (NOV 2025) | 32 CFR Part 170; 48 CFR 252.204-7021 | Phase 2 (planned for 2026-11-10) suspended by the 2026-07-13 CIO memorandum; 252.204-7021 only where a program office requires a specific level (DoD Class Deviation 2026-O0025, Revision 3, DFARS 240.371-5); voluntary Level 2 (C3PAO) assessment planned; scoping per 170.19(c); scoring per 170.24; POA&M limits per 170.21; Program H Level 3 expectation suspended, readiness continues, with Final Level 2 (C3PAO) for the Level 3 scope as a prerequisite (170.18(a)(1)) |
| C-DIB-R03 | DFARS 252.204-7019 and 252.204-7020 (NOV 2023) | 48 CFR 252.204-7019, 252.204-7020 | Current SP 800-171 DoD Assessment in SPRS (DIBCAC High Assessment, 2024); subcontractor assessment checks before award ((g)) |
| C-DIB-R04 | FAR 52.204-21 (NOV 2021) | 48 CFR 52.204-21 | Basic safeguarding for FCI; met inside the GCEE and on corporate systems |
| C-DIB-R05 | ITAR | 22 CFR Parts 120-130 | Release of technical data to a foreign person is an export (22 CFR 120.56); U.S.-person gating; the encrypted-data carve-out in 22 CFR 120.54(a)(5) is relied on only where its conditions are met |
| C-DIB-R06 | EAR | 15 CFR Parts 730-774 | Same principles for EAR technology on commercial parts (15 CFR 734.18(a)(5)) |
| CUI program | CUI Basic safeguarding | 32 CFR 2002.14 | CUI Basic is protected at no less than moderate confidentiality (2002.14(a)(3)) |
| N51-R08 | SEC cybersecurity disclosure | Reg S-K Item 106; Form 8-K Item 1.05 | A GCEE incident may be material to the group (P08) |
| Internal | Group policies POL-01 to POL-05 and division supplements | P06 | Program rules |

Not applicable to the GCEE: NISPOM (C-DIB-R07, 32 CFR Part 117) governs only the classified systems at the two cleared Engineering Services centers, which are outside this boundary (their reporting and insider threat duties are in P03 and P08); CIRCIA (final rule not published).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Group CISO and the Group data and engineering platforms director (system owner) on 2026-09-15, after the board audit and risk committee review. The Aircraft Parts and Engineering Services presidents, as CMMC Affirming Officials for their CAGE codes (32 CFR 170.22), reviewed it the same day.

### 4.2 System Authorization Decision
The group is not a federal agency, so there is no authorization to operate. The equivalent internal decision:
- **Decision:** authorized to operate with conditions, 2026-09-15, by the Group CISO and the Group Chief Risk Officer.
- **Conditions:** (1) stop exporting Aircraft Parts CUI to SYS-D4 and move that data into the GCEE by 2026-11-30, unless SYS-D4 shows FedRAMP Moderate equivalency first (POAM-006); (2) close every requirement that 32 CFR 170.21 does not allow on a POA&M before the C3PAO assessment window (2026-12-07); (3) no new interconnection without an interconnection agreement (CA-3).
- **External validation:** a voluntary CMMC Level 2 certification assessment by a C3PAO (target window 2026-12-07 to 2026-12-18), then a Level 3 certification assessment by DCMA DIBCAC for the Program H scope after Final Level 2 (C3PAO) status, if Program H requires it.
- **Review:** annually, after the C3PAO assessment, and when Plant 9 or the HPC cluster joins.

### 4.3 System Operational Status
Operational. Planned major changes: Plant 9 connection after its migration (2027-03-31); device certificates for thick workstations (2027-03-31); Program H Level 3 controls (2027 Q3).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Group data and engineering platforms director | Accountable for the GCEE and this SSP |
| Authorizing official equivalent | Group CISO with the Group Chief Risk Officer | Authorization decision; High risk acceptance |
| CMMC Affirming Officials | Aircraft Parts president; Engineering Services president | SPRS affirmations for their CAGE codes (32 CFR 170.22) |
| CUI data owners | Aircraft Parts VP of engineering; Engineering Services VP of engineering; Program H chief engineer | Approve project access and data flows |
| Export control | Division Empowered Officials; Group export compliance director | Export tags, foreign-person sharing under agreements |
| Common control providers | Group identity director (SYS-G1), Group SOC director (SYS-G2), Group cloud platform director (SYS-G3), Group HR director, Group supply chain risk director | Operate inherited controls (`common-control-catalog.csv`) |
| Platform operation | GCEE platform engineering lead; PLM administrators | Day-to-day operation |
| CMMC program | Group CMMC program director | Scope, SPRS, C3PAO and DIBCAC coordination |
| Independent assessor | Group internal audit | Assesses common controls once and samples division controls (P07) |

## 6. System Information Types and System Categorization
Information types are from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Controlled technical information (drawings, models, NC programs, build files) | Moderate | Moderate | Moderate | Disclosure harms DoD programs and violates export controls; a wrong revision produces nonconforming flight parts; a PLM outage idles two divisions (P05 BP-AP03: MTD 24 hours) |
| Test and analysis data | Moderate | Moderate | Moderate | Lost test data means repeating scheduled tests (P05 BP-ES02) |
| Identity and security data (keys, logs, access policies) | Moderate | Moderate | Moderate | Protects the enclave itself |
| **GCEE category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Why not High.** The group considered raising confidentiality to High for the aggregation of many programs' data. It kept Moderate because the binding standard for CUI Basic is moderate confidentiality (32 CFR 2002.14(a)(3)) and the contracts require SP 800-171, and it addressed aggregation risk with the Program H enclave and the Level 3 requirements selected from SP 800-172 instead.

**Baseline.** The binding requirement set is the 110 SP 800-171 Rev. 2 requirements; each one's GCEE implementation is in `sp800-171-requirement-statements.csv` (110 rows, linked to the P03 gap rows). `control-implementation.csv` documents **137 SP 800-53 Rev. 5 controls**: 136 from the Moderate baseline plus PM-9 (tailored in). Other Moderate controls are either fully inherited from cloud provider A under its customer responsibility matrix (most PE controls for data centers) or tailored out in the group tailoring register.

## 7. Authorization Boundary Description
The boundary follows the CMMC Level 2 asset categories in 32 CFR 170.19(c)(1):

| Category | Assets | Treatment |
|---|---|---|
| CUI Assets | PLM application and database, PLM vault, virtual workstation pool, thick CAD workstations (about 1,100), exchange gateway, Program H enclave, backup vault, printed CUI at engineering centers | Assessed against all 110 requirements |
| Security Protection Assets | SYS-G1 government-community tenant, SYS-G2 SIEM and EDR, SYS-G3 hub, guardrails, and key management | Assessed against the requirements relevant to their function |
| Specialized Assets | None in the GCEE (plant machines are in the plant enclave SSPs; HPC test equipment in the Engineering Services plan) | n/a |
| Contractor Risk Managed Assets | None designated | Not used |
| Out-of-Scope Assets | Engineering laptops that reach CAD only through the virtual desktop service in keyboard-video-mouse mode | Configuration evidence kept to justify the category |

**External service providers (32 CFR 170.19(c)(2)).**
- **Cloud provider A** (government-community offering, FedRAMP authorized at High) and the **collaboration suite** (FedRAMP authorized at Moderate or higher) are CSPs that hold CUI and meet the FedRAMP requirements in DFARS 252.204-7012. Their CRMs are referenced here, as 32 CFR 170.17(c)(5)(iii) requires.
- **SYS-D4 industry edition** (Defense Software division) receives Aircraft Parts sustainment CUI from the GCEE. For the GCEE it is an external CSP. It has not yet shown security equivalent to the FedRAMP Moderate baseline, so this flow is a gap (AC-20, SA-9; P03 G-020 and G-111; condition 1 in section 4.2).

The diagram is in P04 `cloud-architecture.md` (section 2.2).

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Path | Agreement |
|---|---|---|---|---|
| SYS-D1 plant MES and DNC (plants 1 to 8) | Outbound (release push) | Released drawings, NC programs, build files, inspection plans | Plant VPNs (FIPS-validated) | Plant enclave SSPs |
| SYS-D2 HPC cluster | Bidirectional | Simulation inputs and results | Private link | **No interconnection agreement (gap)** |
| SYS-D2 test systems | Inbound | Test data | Private link after local buffering | Engineering Services plan |
| SYS-D4 industry edition | Outbound daily | Aircraft Parts sustainment data (CUI) | Platform API | **Gap: no equivalency evidence; stop or prove by 2026-11-30** |
| Prime portals (Primes A to D) | Bidirectional | Drawings, models, quality data | Browser from virtual workstations | Subcontracts (DFARS 252.204-7012 flowed down) |
| Suppliers and outside processors (about 1,450) | Outbound | Drawings needed for each order | Exchange gateway | Purchase orders with DFARS flowdown (92% confirmed) |
| DoD program offices | Bidirectional | Deliverables and data packages | Exchange gateway; DoD portals | Prime contracts |
| SYS-G5 CUI suite | Bidirectional | Links and attachments | Tenant integration | Internal |
| SYS-G4 ERP | Inbound | Part numbers and order data only (no CUI) | Scheduled interface | Internal |
| Public generative AI services | **Blocked** | None | Web category block | Prohibited (POL-05) |

## 9. System Component Inventory
| Component | Type | Location or provider | CMMC category | Owner |
|---|---|---|---|---|
| PLM application servers and database | IaaS and PaaS | Provider A government-community region | CUI Asset | Group data and engineering platforms director |
| PLM vault | Object storage | Provider A | CUI Asset | Same |
| Virtual workstation pool (2,400 sessions) | PaaS | Provider A | CUI Asset | GCEE platform engineering lead |
| Thick CAD workstations (about 1,100) | Endpoints | Plants 1 to 8 and engineering centers | CUI Asset (**plants 4 and 7 not yet inventoried**) | GCEE platform engineering lead |
| Exchange gateway | Managed file transfer (PaaS) | Provider A DMZ subnet | CUI Asset | GCEE platform engineering lead |
| Program H enclave (vault, keys, access group) | Separate account | Provider A | CUI Asset | Program H chief engineer |
| Key management; backup vault | PaaS | Provider A (two regions) | Security Protection Asset; CUI Asset | Group cloud platform director |
| Printed CUI at engineering centers | Paper media | Engineering centers | CUI (media) | Division security and compliance leads |

## 10. Control Implementation Details
### 10.1 Implementation status
**By SP 800-171 requirement** (`sp800-171-requirement-statements.csv`, 110 rows): 105 Implemented and 5 Partially implemented (3.1.3, 3.1.20, 3.4.1, 3.4.9, 3.12.4). Requirements whose open gaps sit only in plant systems or at Plant 9 (for example 3.3.1, 3.8.7, 3.13.11) are Implemented for the GCEE itself; their gaps are tracked in the plant enclave SSPs and in P03.

**By SP 800-53 control** (`control-implementation.csv`, 137 rows):

| Status | Controls |
|---|---|
| Implemented | 120 |
| Partially implemented | 15 |
| Planned | 2 |
| Not applicable | 0 |
| **Total** | **137** |

| Inheritance | Controls |
|---|---|
| Common/Inherited (from SYS-G1, SYS-G2, SYS-G3, group functions, or cloud provider A) | 88 |
| Hybrid (group provides the mechanism; the GCEE configures or operates part) | 38 |
| System-specific | 11 |

**The 15 partially implemented controls** cluster in four places:
- **The SYS-D4 dependency and other external flows** (scenario gap 4): AC-4, AC-20, CA-3, SA-9.
- **Inventory, software, and service accounts:** AC-2, CM-8, CM-11, IA-5.
- **Plans and sharing:** PL-2 (HPC and Engineering Services inheritance, gap 6), AC-21 (foreign-person sharing tags).
- **Group functions inherited by the GCEE:** IR-3 and IR-6 (cross-division exercise and Defense Software reporters, gap 8), SI-4(4) (Program H egress baseline), SR-3 and SR-6 (supplier CMMC verification, gap 3).

The 2 planned controls (IA-3 device authentication and SR-11 component authenticity) also prepare for Level 3.

### 10.2 Common control inheritance by division
`common-control-catalog.csv` lists 123 controls provided by corporate: SYS-G1 (31), SYS-G2 (27), SYS-G3 (22), the group security governance office (18), group HR (10), the group supply chain risk office (7), group facilities security (5), and the group CMMC program office (3). Inheritance is **documented for Aircraft Parts** (2025 inheritance matrix and plant enclave SSPs), for **Defense Software** (DoD edition SSP and the industry edition SOC 2 system description), and for the **GCEE** (this plan). For **Engineering Services** it is documented for the engineering centers but **not for the HPC cluster and test systems** that joined the CUI environment in 2026 (scenario gap 6, POAM-009). Until that closes, a C3PAO cannot trace which requirements those systems inherit, and P07 found CA-2 statements other than satisfied for this reason.

### 10.3 Assessment status and score
- Common controls were assessed once, and GCEE and division controls sampled, from 2026-07-06 to 2026-08-28 by group internal audit (P07).
- Gap analysis: P03. Recalculated score under 32 CFR 170.24: **87** for the Aircraft Parts portion of the planned assessment scope and **79** for the Enterprise CUI Environment as a whole (Engineering Services adds four NOT MET requirements). The SPRS record (DIBCAC High Assessment, 98, 2024) predates Plant 9 and the HPC cluster.
- Enduring exceptions: none in the GCEE. Plant machine exceptions are in the plant enclave SSPs.

## 11. Digital Identity Acceptance Statement
- **Workforce users** authenticate to the SYS-G1 government-community tenant with MFA (64% phishing-resistant, the rest number-matching push) from a compliant device; **administrators** use hardware security keys and just-in-time PAM elevation. This fits a Moderate system holding CUI and export-controlled data.
- **Service accounts** should use workload identity. 19 still use static keys older than 1 year (IA-5; POAM-002).
- **Partner users** of the exchange gateway authenticate through their own organization's federation or gateway accounts with MFA.
- **Level 3 preparation:** bidirectional, certificate-based device authentication for thick workstations is planned by 2027-03-31 (IA-3; SP 800-172 3.5.1e).

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`); requirement statements (`sp800-171-requirement-statements.csv`); common control catalog (`common-control-catalog.csv`); group and division risk registers (P01); gap analyses and regulation-by-division matrix (P03); cloud architecture and control map (P04); BIA (P05); group policies and division supplements (P06); assessment and POA&M (P07); incident response runbook and notification matrix (P08); SOC 2 readiness (P09); AI governance (P10); cloud provider CRMs and FedRAMP Marketplace records (kept by the Group CMMC program director).

## 13. Acronym List and Glossary
- **C3PAO:** CMMC Third-Party Assessment Organization
- **CDI:** covered defense information
- **Common control:** a control provided once by corporate and inherited by several systems
- **CRM:** customer responsibility matrix
- **CTI:** controlled technical information
- **DIBCAC:** DCMA's Defense Industrial Base Cybersecurity Assessment Center
- **Enterprise CUI Environment:** the planned Level 2 assessment scope (GCEE, plants 1 to 8, Engineering Services centers)
- **GCEE:** Group CUI Engineering Enclave
- **PAM:** privileged access management
- **PLM:** product lifecycle management
- **SPRS:** Supplier Performance Risk System

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 2.0 | 2024-04-30 | Plan used for the DIBCAC High Assessment | Group data and engineering platforms director |
| 2.9 | 2026-08-28 | Draft after P07 fieldwork: Program H enclave, Engineering Services users, SYS-D4 dependency | GCEE platform engineering lead |
| 3.0 | 2026-09-15 | Approved with authorization conditions | Group CISO |
