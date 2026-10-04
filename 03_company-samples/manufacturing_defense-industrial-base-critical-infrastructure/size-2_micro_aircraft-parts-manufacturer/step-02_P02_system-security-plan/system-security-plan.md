# System Security Plan: CUI Machining Enclave (CME)

**Organization:** Cris Santos Company, LLC (aircraft parts machine shop, DoD subcontractor) | **Tier:** Micro | **Vertical:** Defense Industrial Base
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-31 (first SSP)
**Requirement set:** NIST SP 800-171 Rev. 2 (110 requirements), as required by DFARS 252.204-7012(b)(2) and assessed for CMMC Level 2 (32 CFR 170.14(c)(3))

## 1. System Name and Identifier
CUI Machining Enclave (**CME**), identifier CSC-SYS-CME-01. This is the company's first system security plan. It satisfies SP 800-171 requirement 3.12.4 and is the SSP named in the corrected SPRS submission under DFARS 252.204-7019 and 252.204-7020.

**Why the name differs from the registry default.** The registry suggests a "CUI engineering enclave (CAD/PLM)". A 7-person build-to-print shop has no PLM system: the controlled job folders in the CUI suite (SYS-01) and the CAM workstation (SYS-03) do that job.

## 2. System Overview
The CME is where the shop receives, stores, and uses controlled technical information (CTI) for its DoD subcontracts: drawings, 3D models, and specifications from Prime A and Supplier B, and the CAM files, NC programs, setup sheets, and CMM inspection programs made from them. About 25 of the 60 CUI part numbers are ITAR defense articles. Four people hold CUI suite accounts; the Lead Machinist and 2 machinists see CUI on printed drawings and at the machine controls.

The company owns almost no IT infrastructure and has no IT staff. The CUI suite is a government-community cloud SaaS, and a managed service provider (MSP) runs the computers, firewall, and backups. This plan therefore says, for each control, what the company does itself, what the MSP does for it, and what it inherits from the cloud provider.

**Major components** (IDs from `../00_company-facts.md` section 3):
- **SYS-01:** CUI suite: email, controlled job folders, identity and MFA (government-community cloud, FedRAMP authorized at Moderate or higher)
- **SYS-03:** CAD/CAM programming workstation, with the DNC software that sends programs to 3 machines
- **SYS-04:** quality PC with CMM software, and the CMM
- **SYS-05:** 2 laptops (President, Office Manager)
- **SYS-06:** 5 CNC machines (3 networked, 2 loaded by USB)
- **SYS-07:** shop network: firewall, switch, Wi-Fi, shop-floor printer, VoIP desk phones
- **SYS-08 (services protecting the enclave):** MSP remote monitoring and management (RMM), antivirus console, cloud backup

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it affects the CME |
|---|---|---|---|
| C-DIB-R01 | DFARS 252.204-7012 (MAY 2024) | 48 CFR 252.204-7012 | SP 800-171 on every covered contractor information system; cloud services holding CDI must meet FedRAMP Moderate-equivalent requirements ((b)(2)(ii)(D)); 72-hour reporting; malware to DC3; 90-day image preservation; flowdown |
| C-DIB-R02 | CMMC Program and DFARS 252.204-7021 (NOV 2025) | 32 CFR Part 170; 48 CFR 252.204-7021 | Level 2 (Self) status and affirmation needed before Prime A purchase orders issued from 2027-04-01; scoping per 170.19(c); scoring per 170.24; POA&M limits per 170.21 |
| C-DIB-R03 | DFARS 252.204-7019 and 252.204-7020 (NOV 2023) | 48 CFR 252.204-7019, 252.204-7020 | A current SP 800-171 DoD Assessment score in SPRS; the 2025 score of 110 is inaccurate and must be corrected |
| C-DIB-R04 | FAR 52.204-21 (NOV 2021) | 48 CFR 52.204-21 | Basic safeguarding for FCI, including the ERP and commercial suite outside this boundary |
| C-DIB-R05 | ITAR | 22 CFR Parts 120-130 | Release of technical data to a foreign person is an export (22 CFR 120.56); U.S.-person access; encrypted-data carve-out conditions (22 CFR 120.54(a)(5)) |
| C-DIB-R06 | EAR | 15 CFR Parts 730-774 | Same principles for EAR-controlled technology on commercial parts (15 CFR 734.18(a)(5)) |
| CUI program | CUI Basic safeguarding | 32 CFR 2002.14 | CUI Basic is protected at no less than moderate confidentiality (2002.14(a)(3)) |
| Internal | Security policies POL-02, POL-03, POL-04 | P06 | Program rules |

Not applicable:
- **NISPOM (C-DIB-R07, 32 CFR Part 117):** no facility clearance and no classified information.
- **CIRCIA (6 U.S.C. 681b):** the final rule is not published; nothing is required yet.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the President on 2026-08-31. The President is also the CMMC Affirming Official (32 CFR 170.22).

### 4.2 System Authorization Decision
The company is not a federal agency, so there is no authorization to operate. The equivalent internal decision: on 2026-08-31 the President accepted continued operation of the CME on three conditions: (1) the corrected SPRS score is posted by 2026-09-30, (2) CUI stops flowing into the commercial suite, the ERP, and the commercial backup by 2026-10-31, and (3) the POA&M in P07 is worked to the dates shown. External validation will come from the Level 2 self-assessment (target 2027-03-15) and, if a later Prime A program requires it, a C3PAO assessment.

### 4.3 System Operational Status
Operational. Planned changes: compliant backup and retirement of the commercial backup (2026-09-15 to 2026-09-30), enclave VLAN (2026-11-30), desktop encryption and removal of local administrator rights (2026-10-31), DoD reporting certificates (2026-10-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner, risk acceptor, Affirming Official | President | Accountability; accepts Moderate and higher risks; SPRS submissions and affirmations; ITAR Empowered Official |
| Security and Compliance Coordinator | Office Manager | Maintains this plan, the risk register, the inventory, and the POA&M; accounts; visitor log; training records |
| CUI data custodian | CNC Programmer | Job folders, CAM and NC programs, program transfer to machines |
| Printed CUI on the floor | Lead Machinist | Drawing custody, USB transfers to the 2 older machines |
| Quality records | Quality Inspector | CMM programs and inspection data |
| IT operations (External Service Provider) | MSP | Endpoints, patching, antivirus, firewall, Wi-Fi, backup, tenant administration |
| Independent assessor | Consultant (SP 800-171A) | Readiness assessment (P07) |

**Role overlap.** One person (the Office Manager) runs the program and also reviews accounts and logs; the President approves and accepts risk. The independent consultant (P07) and the monthly MSP report are the outside checks on work the company does and reviews itself.

## 6. System Information Types and System Categorization
Information types are from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199. CUI Basic cannot be protected below moderate confidentiality (32 CFR 2002.14(a)(3)).

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Controlled technical information (drawings, models, NC and CMM programs) | Moderate | Moderate | Moderate | Disclosure harms defense programs and can be an unauthorized export; a wrong dimension or program produces a nonconforming flight part; an outage stops new work (P05 MTD 48 to 72 h) |
| Production and quality records (travelers, inspection reports, certificates) | Moderate | Moderate | Low | Records prove conformance; short outages are covered by paper |
| Identity and security data (accounts, MSP credentials, logs) | Moderate | Moderate | Moderate | Protects the enclave itself |
| **CME category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Requirement baseline.** The binding set is the 110 SP 800-171 Rev. 2 requirements. Their implementation statements are in P03 `gap-analysis.csv` (current_state column, rows G-001 to G-110) and are part of this plan by reference. `control-implementation.csv` documents 55 SP 800-53 Rev. 5 controls from the Moderate baseline that carry those requirements, plus contingency, inventory, and supplier controls the shop needs. The CSF 2.0 column uses the NIST CSF 2.0 to SP 800-53 crosswalk in `00_universal-framework/crosswalks/`; for 9 controls with no entry there (AC-11, MA-4, MA-5, MP-2, MP-6, MP-7, PL-4, PS-3, PS-4) the mapping is the author's. Other Moderate-baseline controls are inherited from the cloud provider through its FedRAMP authorization or are outside what a 7-person shop needs (for example, separate development environments and configuration change boards); these are tailoring decisions, not gaps.

## 7. Authorization Boundary Description
The boundary follows the CMMC Level 2 asset categories in 32 CFR 170.19(c)(1):

| Category | Assets | Treatment |
|---|---|---|
| CUI Assets | SYS-01, SYS-03, SYS-04 (quality PC), SYS-05, shop-floor printer, printed drawings and setup sheets, USB drives for the older machines | Assessed against all 110 requirements |
| Security Protection Assets | SYS-01 identity and MFA, firewall, MSP RMM and antivirus consoles, backup service | Assessed against the requirements relevant to their function |
| Specialized Assets | SYS-06 (5 CNC machines) and the CMM (test equipment) | Inventoried, on the diagram, managed under risk-based practices (section 9); not assessed against other requirements |
| Contractor Risk Managed Assets | None designated | Not used |
| Out-of-Scope Assets (intended) | SYS-11 payroll and accounting; guest Wi-Fi | Cannot process CUI and provide no security protection |
| **Holding CUI today, outside the intended boundary** | SYS-02 commercial suite (Supplier B emails and old job folders); SYS-09 ERP (drawing PDFs on 31 job records); the MSP's commercial backup cloud (images of SYS-03 and SYS-04) | Not Out-of-Scope while they hold CUI. Each must be cleaned and blocked by 2026-10-31 (P03 G-111, G-125), or it stays in scope and fails 3.13.11 and the FedRAMP condition |

**External service providers (32 CFR 170.19(c)(2), Table 4).**
- **Cloud provider (CSP holding CUI):** the CUI suite offering is FedRAMP authorized at Moderate or higher, which meets DFARS 252.204-7012(b)(2)(ii)(D). Its customer responsibility matrix (CRM) must be on file and referenced here; it is not yet (due 2026-09-30).
- **MSP (ESP that is not a CSP, handling Security Protection Data):** its services are in the assessment scope as Security Protection Assets. Its relationship and services must be documented here and in a CRM-style responsibility matrix (170.19(c)(2)(ii)). That matrix is due 2026-10-31 (P07 POAM-009). The MSP does not need its own CMMC certification, but its technicians, tools, and accounts will be looked at in the company's assessment.
- **Commercial backup cloud (MSP subcontractor):** it stores CUI and is not FedRAMP authorized. It is being retired (section 4.3).

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Path | Agreement |
|---|---|---|---|---|
| Prime A supplier portal | Bidirectional | Drawings, models, quality data | Browser from SYS-05 or SYS-03 (prime-hosted, prime's MFA) | Purchase order terms (DFARS 252.204-7012 flowed down) |
| Supplier B | Inbound drawings; outbound quotes and data | Drawing packages | **Commercial orders mailbox (SYS-02) today (gap)**; SYS-01 email from 2026-10-31 | Purchase order terms (DFARS 252.204-7012 flowed down) |
| CNC machines (3 networked) | Outbound | NC programs | DNC software on SYS-03 over the flat network (unencrypted; to move to the enclave VLAN) | Internal |
| CNC machines (2 older) | Outbound | NC programs | USB drives (to be company-owned, labeled, and logged) | Internal |
| ERP (SYS-09) | Internal | Order data (FCI); **drawing PDFs on 31 records (gap)** | Web | ERP vendor terms |
| MSP RMM platform | Inbound administrative access | Device management | RMM agent on every computer | MSP contract (no CMMC terms yet) |
| Public generative AI services | **Prohibited** | CUI text pasted once (P10) | Web | None |
| Customer C | Bidirectional | Commercial drawings (EAR-controlled for some parts) | Commercial suite | Customer agreement |

## 9. System Component Inventory
| Component | Type | Location or provider | CMMC category | Owner |
|---|---|---|---|---|
| CUI suite tenant: 4 users, 1 MSP admin, 1 break-glass (SYS-01) | SaaS | Government-community cloud | CUI Asset; identity as Security Protection Asset | Office Manager |
| CAD/CAM workstation with DNC software (SYS-03) | Desktop | Office | CUI Asset | CNC Programmer |
| Quality PC (SYS-04) | Desktop | Inspection room | CUI Asset | Quality Inspector |
| CMM | Test equipment | Inspection room | Specialized Asset | Quality Inspector |
| Laptops (2) (SYS-05) | Endpoint | Office; travel with the President and Office Manager | CUI Assets | Office Manager |
| CNC machines (5) (SYS-06) | Operational technology | Shop floor | Specialized Assets | Lead Machinist |
| Firewall, switch, staff and guest Wi-Fi (SYS-07) | Network | Office closet | Security Protection Assets | Office Manager (MSP operates) |
| Shop-floor printer | Output device | Shop floor | CUI Asset | Lead Machinist |
| VoIP desk phones (4) | Hosted VoIP | Office | Out of scope once on the office VLAN (G-101) | Office Manager |
| RMM agent and console, antivirus console (SYS-08) | MSP SaaS | MSP | Security Protection Assets | MSP |
| USB drives (2 company-owned, planned) | Portable media | Locked drawer at the older machines | CUI Assets | Lead Machinist |

**Specialized Asset treatment (SP 800-171 3.4.1; DFARS 252.204-7012(b)(3)).** The CNC controllers run builder-embedded software that the company cannot patch or harden; the 2 older controllers are no longer supported (SA-22). The CMM is driven by the quality PC. Compensating measures:
- the 3 networked machines will sit on the enclave VLAN with no internet route and accept programs only from SYS-03 (2026-11-30);
- the 2 older machines accept only the 2 company-owned USB drives, which are scanned on SYS-03 and wiped after use (2026-10-31);
- builder service engineers are escorted and may not connect their own media without a scan (POL-02);
- all machines are in the inventory and on the P04 diagram.

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 55 controls:
- Implemented: 3 (PL-2, RA-3, SI-3)
- Partially implemented: 37
- Planned: 15
- Not applicable: 0

By responsibility: 28 system-specific (the company, often performed by the MSP under direction) and 27 hybrid (the company with the cloud provider or the MSP). No control is fully inherited.

### 10.2 Inherited and MSP-provided controls
| Provider | What the company relies on | Evidence | What the company must still do |
|---|---|---|---|
| Government-community cloud provider (SYS-01) | Data center and platform security, encryption at rest and in transit (SC-8, SC-28), account lockout (AC-7), audit record generation (AU-2), incident duties under 252.204-7012(c) to (g) | FedRAMP Marketplace listing (Moderate or higher). CRM due 2026-09-30 | Users and roles, MFA settings, external sharing settings, audit retention and review, device rules |
| MSP (External Service Provider) | Patching (SI-2), antivirus (SI-3), firewall and Wi-Fi (SC-7, AC-18), backup operation (CP-9), remote maintenance (MA-4), tenant administration | Monthly MSP report; MSP SOC 2 Type 2 report (P09); P07 evidence | Direct and check the work: approve exceptions, review the monthly report, named MSP admin accounts with MFA, written responsibility matrix, U.S.-person confirmation for technicians |
| Commercial backup vendor (MSP subcontractor) | Image backups of SYS-03 and SYS-04 (CP-9) | Backup job report | **Retire it.** It stores CUI outside a FedRAMP-authorized cloud |

**Inherited does not mean done.** The cloud provider's controls protect the job folders only when the company's side is in place: today external sharing is at the default, audit logs are never reviewed, and one phone reads CUI email with no device controls.

### 10.3 Assessment status and score
- Gap analysis, fieldwork 2026-07-13 to 2026-07-24: see P03. Recalculated score under 32 CFR 170.24: **-161**. The 2025 SPRS entry of 110 will be corrected by 2026-09-30.
- Readiness assessment 2026-08-10 to 2026-08-12: see P07 `assessment-results.csv` and `poam.csv`.
- Enduring exception: patching and hardening of CNC controllers (Specialized Assets, section 9).

## 11. Digital Identity Acceptance Statement
CUI suite users sign in with a password and an authenticator app; the MSP administrator account and the break-glass account also require MFA. This meets SP 800-171 3.5.3 for network access to SYS-01 and is appropriate for Moderate confidentiality. **Exceptions until 2026-10-31:** local sign-in to SYS-03 and SYS-04 (including local administrator) has no MFA, and the quality PC uses a shared login (P07 POAM-002). Planned fix: named accounts that sign in with the suite identity and MFA on both PCs, and removal of the shared login.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`); BIA (P05); cloud control map and diagram (P04); risk register (P01); gap analysis, requirement statements, and score (P03); policies (P06); assessment and POA&M (P07); incident response runbook (P08); SOC 2 readiness and MSP report review (P09); AI assessment (P10); cloud provider FedRAMP listing and CRM, and MSP contract (kept by the Office Manager).

## 13. Acronym List and Glossary
- **C3PAO:** CMMC Third-Party Assessment Organization
- **CDI:** covered defense information
- **CMM:** coordinate measuring machine
- **CMMC:** Cybersecurity Maturity Model Certification
- **CRM:** customer responsibility matrix
- **CTI:** controlled technical information
- **CUI:** Controlled Unclassified Information
- **DNC:** direct numerical control (sending NC programs to machines)
- **ESP:** External Service Provider
- **MSP:** managed service provider
- **POA&M:** plan of action and milestones
- **RMM:** remote monitoring and management
- **SPRS:** Supplier Performance Risk System

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | First plan | Office Manager (Security and Compliance Coordinator) with the MSP lead technician |
