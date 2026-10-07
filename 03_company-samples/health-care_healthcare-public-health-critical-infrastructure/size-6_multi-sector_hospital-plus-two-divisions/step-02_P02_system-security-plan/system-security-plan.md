# System Security Plan: Hospital Clinical Information System (HCIS)

**Organization:** Cris Santos Company Holdings, Inc., Hospital System division (9 acute-care hospitals), with common controls from corporate shared services | **Tier:** Multi-Sector | **Vertical:** Healthcare and Public Health
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-15

> **Why this system.** At this tier the SSP can cover one system per division or a shared corporate system. The group chose the focus division's primary system, the **Hospital Clinical Information System (HCIS)**, because the BIA (P05) ranks its processes highest (2- to 4-hour MTDs for ED care, inpatient care, pharmacy, and laboratory), it carries the group's top risk (P01 GR-01, ransomware in the shared data centers), and it inherits most of its infrastructure controls from corporate. The plan comes with a **common control catalog** (`common-control-catalog.csv`, 99 controls) that the Health Plan and the College also inherit from.

## 1. System Name and Identifier
Hospital Clinical Information System (**HCIS**), identifier CSCH-HS-HCIS. It is SYS-H1 plus the parts of SYS-H2 that exchange data with it, as defined in `../00_company-facts.md` section 3.

## 2. System Overview
The HCIS is the clinical and revenue backbone of the 9 hospitals. It supports:
- ED care in 9 emergency departments (about 610,000 visits a year), inpatient care for about 3,000 patients a day, perioperative care, pharmacy, laboratory and blood bank, and imaging;
- 46 hospital outpatient sites and the patient portal;
- 64 independent physician practices on the community-connect service (about 1,100 users), for which the Hospital System is a business associate;
- the EHR vendor's sepsis prediction model, which scores adult ED and inpatient encounters (P10).

About 34,000 workforce users (employees, employed physicians, contractors, and agency staff) and about 4,500 students and trainees a year use it, plus the community-connect users. The EHR holds records for about 3.4 million patients with an encounter in the last 3 years.

**Major components:**
- **Enterprise EHR (SYS-H1):** web, application, and database tiers in DC1, replicated to DC2; patient portal module; sepsis prediction module
- **Downtime business continuity workstations:** one or more on every nursing unit and in every ED, refreshing census, medication, and results reports every 2 hours
- **Clinical interface engine:** active-passive pair across DC1 and DC2; routes HL7 and FHIR messages to the laboratory, imaging, pharmacy automation, the health information exchange, public health agencies, and the Health Plan
- **Laboratory information system and blood bank system** (SYS-H2)
- **PACS and vendor-neutral archive** (SYS-H2); the long-term archive tier is at cloud provider A
- **Pharmacy automation servers** for dispensing cabinets and carousels (SYS-H2)

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies to the HCIS |
|---|---|---|---|
| C-HPH-R01 | HIPAA Security Rule | 45 CFR Part 164, Subpart C | The Hospital System is a covered entity; corporate is its business associate for the data center, identity, and SOC services |
| C-HPH-R02 | HIPAA Breach Notification Rule | 45 CFR 164.400-164.414 | Breach notices to patients, HHS, and media; corporate notifies the Hospital System as business associate (164.410); the Hospital System notifies the 64 community-connect practices as their business associate (P08) |
| C-HPH-R07 | CMS emergency preparedness condition of participation | 42 CFR 482.15 | The HCIS is the "system of medical documentation" each hospital must preserve and keep available in an emergency (482.15(b)(5)). The 9 hospitals use a unified and integrated program (482.15(f)) |
| (vertical overlay) | Section 1557, patient care decision support tools | 45 CFR 92.210 | The sepsis prediction model (P10) |
| (vertical overlay) | EMTALA | 42 CFR 489.24 | Governs ambulance diversion and screening when the HCIS is down (P08) |
| C-HPH-R03 | HIPAA Security Rule NPRM | 90 FR 898 (2025-01-06) | **Proposed only**, tracked: asset inventory, MFA, 72-hour restoration |
| C-HPH-R08, C-HPH-R09, C-HPH-R10 | HPH CPGs; 405(d) HICP; HITECH recognized security practices | Voluntary; 42 U.S.C. 17941 | The program follows HICP practices for large organizations and the CPGs; documenting 12 months of recognized practices supports HHS's consideration under 42 U.S.C. 17941 |
| C-HPH-R11 | CIRCIA | Proposed 6 CFR Part 226 | **Proposed only**. All 9 hospitals have 100 or more beds and would be covered if the rule is finalized as proposed |
| N52-R08 | SEC cybersecurity disclosure | Form 8-K Item 1.05; Reg S-K Item 106 | An HCIS outage or breach may be material to the group (P08) |
| Contracts | Intercompany BAA (2021); community-connect BAAs; EHR vendor BAA | 45 CFR 164.504(e); 164.314(a) | |
| Internal | Group policies POL-01 to POL-05 and the Hospital System supplement | P06 | |

Screened out: 42 CFR Part 2 (no hospital is a Part 2 program; records received from outside programs are flagged and handled case by case); FTC Health Breach Notification Rule (16 CFR 318.1 excludes HIPAA covered entities); FERPA (student health clearance records are held by the College, not in the HCIS).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the HCIS system owner (Hospital System clinical applications director) and the Hospital System security and compliance lead on 2026-09-15, after the board risk committee review.

### 4.2 System Authorization Decision
The group is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- **Decision:** authorized to operate with conditions, 2026-09-15, by the Group CISO and the Group Chief Risk Officer.
- **Conditions:** (1) build a clean recovery environment and complete a full EHR restore test from the immutable vault by 2027-03-31 (POAM-012); (2) move student and trainee accounts into identity governance with end dates and MFA by 2026-12-31 (POAM-001); (3) separate the HCIS server zones and directory tier from other divisions' workloads in both data centers by 2027-06-30 (POAM-007); (4) add a system-wide IT outage scenario, with diversion criteria, to the unified emergency plan by 2026-12-31 (POAM-023).
- **Reauthorization:** annually, or after the clean recovery environment is in service.

### 4.3 System Operational Status
Operational. **Major modifications planned:** a clean recovery environment at cloud provider B (2027-03-31) and the EHR vendor's annual upgrade (2027-05).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Hospital System clinical applications director | Accountable for the HCIS and this plan |
| Authorizing official equivalent | Group CISO with the Group Chief Risk Officer | Authorization decision; High risk acceptance |
| Security Official (45 CFR 164.308(a)(2)) | Hospital System security and compliance lead | Security of ePHI in the HCIS |
| Privacy Official | Hospital System Privacy Officer | Access monitoring, minimum necessary, breach determinations |
| Clinical leads | System CMIO; System CNO | Clinical safety of changes; downtime procedures |
| Emergency preparedness | System emergency management director | Unified emergency plan (482.15(f)) |
| Common control providers | Group identity director (SYS-G1); Group SOC director (SYS-G2); Group infrastructure and network directors (SYS-G3) | Operate inherited controls (`common-control-catalog.csv`) |
| Independent assessor | Group internal audit | Assesses common controls once and samples HCIS controls (P07) |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Health care delivery services (clinical records, orders, results, medication administration) | **High** | **High** | **High** | Aggregation of about 3.4 million patients' records (breach duties in 3 states, SEC materiality). Wrong orders, results, or drug data can kill. ED, inpatient, pharmacy, and laboratory MTDs are 2 to 4 hours (P05) |
| Health care administration (registration, scheduling, billing) | Moderate | Moderate | Moderate | Revenue cycle can wait 72 hours (P05 BP-H11) |
| Information security (credentials, keys, audit logs) | High | High | Moderate | Compromise would expose every hospital |
| **HCIS category (high-water mark)** | **High** | **High** | **High** | Overall **High** |

**Baseline:** the NIST SP 800-53B **High** baseline, tailored. The plan documents **123 controls** in `control-implementation.csv`:
- 118 from the High baseline;
- 3 from the privacy baseline (PM-9, PT-2, PT-3), added because minimum necessary between the two covered entities is a scenario gap;
- 2 program management controls not in any baseline (PM-1, PM-2).

Other High-baseline controls are inherited in full from corporate without HCIS-specific content (for example, most PE controls for the data centers) or tailored out with a reason in the group tailoring register (for example, PE controls for facilities the Hospital System does not run). The `csf2_subcategories` column comes from NIST's CSF 2.0 to SP 800-53 crosswalk (`00_universal-framework/crosswalks/`); for 12 controls the crosswalk lists no subcategory, and those cells are an author mapping (AC-11, CA-6, CP-3, IR-2, MA-4, MP-6, PL-4, PS-3, PS-4, PS-8, PT-2, PT-3).

## 7. Authorization Boundary Description
- **Inside:** the EHR web, application, and database tiers in DC1 and DC2; downtime business continuity workstations; the clinical interface engine; the laboratory and blood bank systems; PACS and the archive (including its tier at provider A); pharmacy automation servers.
- **Outside, inherited (common control providers):** SYS-G1 identity and the group directory, SYS-G2 SOC, SIEM, and EDR, and SYS-G3 data center facilities, network, file service, cloud platform, and backup vault.
- **Outside, interconnected:** SYS-H3 medical devices and clinical OT (device integration through the interface engine), the Health Plan (admission notices and eligibility, SYS-P1), the health information exchange, the reference laboratory, public health agencies, the clearinghouse, and the community-connect practices.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| SYS-H3 medical devices (monitors, pumps, analyzers) | Inbound | Vital signs, device data, results | Clinical engineering device integration standard |
| Health Plan (SYS-P1) | Outbound admission notices; inbound eligibility | ADT messages for about 140,000 shared members; eligibility | Intercompany data sharing addendum (2023). **Minimum-necessary protocol not written** (POAM-016) |
| Health information exchange | Both | Clinical documents | HIE participation agreement and BAA |
| Reference laboratory | Both | Orders and results | BAA; interface agreement |
| State and county public health agencies | Outbound | Reportable laboratory results, syndromic surveillance, immunizations | Public health reporting (permitted disclosure) |
| Clearinghouse | Outbound | Claims and eligibility transactions | BAA |
| 64 community-connect practices | Both (shared instance) | Practice patients' records | Community-connect agreements and BAAs (Hospital System as business associate) |
| College (SYS-E1) | Inbound | Student rotation rosters (by email today) | Affiliation agreement; student FERPA consent (34 CFR 99.30) |

## 9. System Component Inventory
| Component | Type | Location | Owner |
|---|---|---|---|
| EHR web and application tiers | Virtual servers | DC1 (production), DC2 (replica) | HCIS system owner |
| EHR database | Database cluster with storage replication | DC1, DC2 | HCIS system owner |
| Downtime workstations (about 640) | Encrypted workstations with local printers | 9 hospitals | HCIS system owner |
| Clinical interface engine | Active-passive pair | DC1, DC2 | HCIS system owner |
| Laboratory information and blood bank systems | Virtual servers | DC1, DC2 | System laboratory director (application); infrastructure inherited |
| PACS and vendor-neutral archive | Servers and storage; archive tier at provider A | DC1, DC2, provider A | System imaging director |
| Pharmacy automation servers | Virtual servers | DC1 | System chief pharmacy officer |

The full inventory is in the configuration management database. Interfaced devices are not yet linked to their interfaces (CM-8, POAM-011).

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv` (123 controls) and `common-control-catalog.csv` (99 group common and hybrid controls).

| Status | Controls |
|---|---|
| Implemented | 103 |
| Partially implemented | 20 |
| Planned | 0 |
| Not applicable | 0 |
| **Total** | **123** |

| Inheritance | Controls |
|---|---|
| Common/Inherited (from SYS-G1, SYS-G2, SYS-G3, or group functions) | 71 |
| Hybrid (corporate provides the mechanism; the Hospital System configures or operates part) | 28 |
| System-specific | 24 |

**The 20 partially implemented controls** cluster in six places:
- **Student and trainee access** (scenario gap 4): AC-2, AC-2(3), IA-2(2), AT-2, PS-7.
- **Recovery from a ransomware attack that reaches both data centers, and its link to emergency preparedness** (gaps 1 and 2): CP-2, CP-2(1), CP-4, CP-10.
- **Shared data center architecture** (gap 1): SC-7.
- **Clinical system hygiene:** SI-2, SA-22, CM-8, IA-5.
- **Minimum necessary between the two covered entities** (gap 7): AC-4, CA-3, PT-3.
- **Cross-division incident notification** (gap 8): IR-3, IR-6, IR-8.

### 10.2 Common control inheritance by division
The catalog lists 99 controls provided fully or partly by corporate. Inheritance is **documented** for the Hospital System (2024 inheritance matrix) and the Health Plan (2025 matrix). The **College inherits only part** of the catalog: 29 controls are inherited (mostly data center and backup controls for its file shares in DC1, plus group internal audit), 44 partly (SOC monitoring, policy, HR, and risk), and 26 not at all (identity and third-party risk), because it still runs its own directory (scenario gap 5). Until the College moves to SYS-G1 (due 2027-06-30), it must meet the Safeguards Rule access and MFA elements itself (P03).

### 10.3 Control assessment status
Group internal audit assessed the common controls once, and sampled HCIS and division controls, from 2026-07-06 to 2026-08-28. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
- **Workforce users** unlock clinical workstations with a badge tap and PIN and use SYS-G1 MFA for remote access and email. **Administrators** use phishing-resistant authenticators and just-in-time PAM elevation. This fits a High system used on shared clinical workstations, where speed of access is a patient safety factor.
- **Students and trainees** use local EHR accounts with a password only. This does not meet the plan's assurance level and is a condition of the authorization (POAM-001).
- **Community-connect practice users** authenticate through their practices' identity providers with MFA required by contract (IA-8). **Patients** use the portal's own identity service and are outside the workforce assurance level.
- **Service and interface accounts** should use managed credentials with rotation; 63 still have static passwords older than 1 year (POAM-002).

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), group and division risk registers (P01), gap analyses and regulation-by-division matrix (P03), cloud architecture and control map (P04), BIA (P05), group policies and division supplements (P06), assessment and POA&M (P07), incident response runbook and notification matrix (P08), SOC 2 readiness for the community-connect service (P09), AI governance (P10).

## 13. Acronym List and Glossary
- **ADT:** admission, discharge, and transfer messages
- **BAA:** business associate agreement
- **Common control:** a control provided once by corporate and inherited by several systems
- **Community connect:** the Hospital System's EHR instance extended to independent practices
- **DC1, DC2:** the group's primary and secondary data centers
- **HCIS:** Hospital Clinical Information System
- **PAM:** privileged access management
- **SIEM:** security information and event management

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-08-31 | Draft after P07 fieldwork | HCIS system owner |
| 1.0 | 2026-09-15 | Approved with authorization conditions | Group CISO |
