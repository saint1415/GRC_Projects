# System Security Plan: Device Cloud Service (DCS)

**Organization:** Cris Santos Company, LLC (connected medical device manufacturer) | **Tier:** Small | **Vertical:** Manufacturing (NAICS 334510)
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-04

## 1. System Name and Identifier
Device Cloud Service (**DCS**), identifier CSC-SYS-001.

## 2. System Overview
The DCS is the companion cloud service for the company's wireless patient monitors. For 40 hospital customers it:
- receives vital-sign telemetry and alarm events from about 6,800 PM-2 and 2,100 PM-1 monitors;
- gives clinicians remote viewing of their own patients in a web portal;
- sends results and secondary alarm notifications to each hospital's EHR and clinical communication system;
- distributes signed PM-2 firmware updates.

Primary alarms always sound at the bedside monitor. The DCS adds remote visibility and does not replace the bedside alarm.

The DCS holds PHI for about 380,000 patients on behalf of the hospitals, so the company is a HIPAA business associate for this service. Under FD&C Act section 524B, the DCS is also a **related system** of the PM-2 cyber device: its update service and device connections must be covered by the processes that give a reasonable assurance that "the device and related systems are cybersecure" (21 U.S.C. 360n-2(b)(2)).

**Major components:**
- device ingestion gateway (mutual TLS)
- container platform running the ingestion, processing, portal, HL7 interface, and update services
- managed relational database and object storage
- key management service holding data keys and the device certificate authority
- cloud audit logging, plus the external log analytics service (SYS-10)
- the workforce identity provider tenant (SYS-02) and the support and DevOps endpoints that administer the service

The public cloud tenant is described by service category and is vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies |
|---|---|---|---|
| N31-33-R05 | FD&C Act section 524B, ensuring cybersecurity of devices | 21 U.S.C. 360n-2 | The DCS is a related system of the PM-2 cyber device and will be part of the AI-001 submission |
| QMSR | Quality Management System Regulation | 21 CFR Part 820 (ISO 13485 incorporated by reference) | Design and development controls (820.10(c)) cover DCS software that performs device functions |
| FDA reporting | Medical device reporting; corrections and removals | 21 CFR Part 803; 21 CFR Part 806 | Apply when a DCS or device vulnerability leads to a reportable event or a correction |
| N62-R01 | HIPAA Security Rule | 45 CFR Part 164, Subpart C | Applies to the DCS as a business associate (164.302) |
| N62-R03 | HIPAA Breach Notification Rule | 45 CFR 164.410 | Notice to hospital customers after discovery of a breach |
| Contract | Business associate agreements with 40 hospitals | BAAs | Notice terms, permitted uses, 24-month retention |
| State | Florida Information Protection Act | Fla. Stat. 501.171(2) and (6) | Reasonable security measures; third-party agent notice to the hospital |
| Internal | Security policies POL-01 to POL-05 | P06 | |

Not applicable: DFARS 252.204-7012, CMMC, and ITAR (no defense work); SEC cybersecurity disclosure rules (privately held).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the COO on 2026-09-04.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- The COO accepted continued operation of the DCS on 2026-09-04, with the conditions in the P07 POA&M.
- The CEO accepted the High risks in P01 on the same date, with dated treatment plans.
### 4.3 System Operational Status
Operational since 2019. Planned major modifications:
- just-in-time production access (due 2026-11-30)
- log redesign that masks patient identifiers (due 2026-10-31)
- the AI-001 image analysis service, planned for the 2027 Q3 marketing submission (see P10)

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | COO | Overall accountability; accepts risk up to Moderate |
| Risk acceptor (authorizing official equivalent) | CEO | Accepts High and Very High risks |
| HIPAA security official | IT Manager | Security program for the DCS (45 CFR 164.308(a)(2)) |
| System operator | Cloud Operations Lead | Production operations, backups, monitoring |
| Engineering owner | VP Engineering | DCS software, secure development, SBOM |
| Product security | Product Security Lead | Threat modeling, vulnerability monitoring, CVD intake |
| Regulatory owner | VP QA/RA | Section 524B, MDR, and correction reporting decisions |
| Privacy | Compliance Manager (Privacy Officer) | BAAs, breach risk assessments, notices to hospitals |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Health care delivery services (vital-sign trends, alarm history, patient identifiers) | Moderate | Moderate | Moderate | Disclosure is a reportable breach for the hospitals. Altered remote data could delay a clinical response, but primary alarms stay at the bedside, which limits the harm. P05 sets the MTD for remote monitoring at 4 hours |
| System maintenance (firmware update distribution) | Low | Moderate | Low | Images are public-facing binaries, but a tampered image could cause harm. PM-2 rejects unsigned images, which bounds the integrity impact at Moderate for this boundary |
| Information security (audit logs, device certificates, access records) | Moderate | Moderate | Low | Needed for investigations and for breach determinations |
| **DCS category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 250-person company running one multi-tenant cloud service. The plan documents 73 controls: those that carry the HIPAA Security Rule for the DCS, the section 524B expectations for related systems, and core cloud hygiene (see `control-implementation.csv`). Every other Moderate-baseline control is treated as follows:
- **Inherited** from the cloud provider (physical, environmental, and hypervisor controls), evidenced by its SOC 2 Type 2 report (P09 Part B).
- **Out of scope for this tier**, recorded as a tailoring decision, where the control's purpose applies only to federal systems. Examples: PM-series program-level controls beyond PM-9.

## 7. Authorization Boundary Description
The boundary contains the company-managed parts of the DCS and the company's configuration of provider services:
- **Inside:** the cloud tenant (ingestion gateway, container platform and its services, database, object storage, key management, secrets manager, bastion, audit logging), the identity provider tenant configuration for DCS roles, the log analytics service configuration (SYS-10), and 22 support and DevOps laptops.
- **Outside (interconnected):**
  - the cloud provider's infrastructure (inherited controls)
  - fielded monitors (SYS-11), which are operated by the hospitals on hospital networks
  - hospital EHRs, interface engines, clinical communication systems, and identity providers
  - the source code repository and build and signing pipeline (SYS-04), which produces the firmware the update service distributes
  - the support ticketing vendor (SYS-12)

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement / protection |
|---|---|---|---|
| PM-2 monitors (SYS-11) | Inbound telemetry; outbound settings and firmware | Vitals, alarms, device status; signed firmware | Mutual TLS with per-device certificates |
| PM-1 monitors (SYS-11) | Inbound telemetry | Vitals, alarms | TLS with a per-hospital shared API key (**gap**) |
| Hospital EHRs and clinical communication systems | Outbound | Results, secondary alarm notifications | BAA; HL7 over site-to-site VPN (12 hospitals) or TLS (28 hospitals); no interconnection security terms (**gap**) |
| Hospital identity providers | Inbound assertions | Clinician identities | Federation (28 hospitals) |
| Build and signing pipeline (SYS-04) | Inbound | Signed PM-2 firmware images | Upload by pipeline service account; signing key on the build server without HSM (**gap**, P01 R-002) |
| Log analytics service (SYS-10) | Outbound | Application logs with patient names and MRNs | **No subcontractor BAA (gap)** |
| Support ticketing (SYS-12) | Bidirectional | Case notes, occasional patient identifiers | Subcontractor BAA |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| Device ingestion gateway | Managed load balancer plus containers | Cloud tenant | Cloud Operations Lead |
| Container platform (ingestion, processing, portal, HL7, update services) | Managed container orchestration | Cloud tenant | Cloud Operations Lead |
| Clinical data store | Managed relational database with point-in-time recovery | Cloud tenant, second-region backup copy | Cloud Operations Lead |
| Reports and firmware images | Object storage | Cloud tenant | Cloud Operations Lead |
| Key management and device certificate authority | Managed key management service | Cloud tenant | Product Security Lead |
| Secrets manager | Managed service | Cloud tenant | Cloud Operations Lead |
| Web application firewall and denial-of-service protection | Managed edge service | Cloud tenant | Cloud Operations Lead |
| Site-to-site VPN gateway (12 hospitals) | Managed network service | Cloud tenant | Cloud Operations Lead |
| Bastion for administrative sessions | Managed access service | Cloud tenant | Cloud Operations Lead |
| Cloud audit logging | Provider service | Cloud tenant | IT Manager |
| Log analytics workspace | SaaS | Log analytics vendor | Cloud Operations Lead |
| Identity provider tenant (DCS roles) | SaaS | Identity vendor | IT Manager |
| Support and DevOps laptops (22) | Endpoint | Company facility and remote | IT Manager |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 73 controls:
- Implemented: 33
- Partially implemented: 31
- Planned: 9

By inheritance: 53 system-specific, 14 hybrid, 6 common/inherited.

### 10.2 Control assessment status
Assessed 2026-08-10 to 2026-08-14. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
- **Workforce:** users authenticate through the identity provider with a password and a second factor. Privileged cloud and production roles require phishing-resistant hardware keys. This fits the Moderate categorization and the all-tenant scope of administrative access.
- **Clinicians:** they authenticate through their hospital's identity provider, or with local portal accounts that require MFA. Identity proofing of clinicians is the hospital's responsibility under the BAA.
- **Devices:** PM-2 authenticates with unique certificates. PM-1's shared per-hospital key does not meet this statement and is tracked in P01 R-014 and the P07 POA&M.

## 12. Referenced Artifacts
- Scenario facts (`../00_company-facts.md`)
- BIA (P05)
- Cloud control map (P04)
- Risk register (P01)
- Gap analysis (P03)
- Policies (P06)
- Assessment and POA&M (P07)
- Incident response runbook (P08)
- SOC 2 readiness (P09)
- AI assessment (P10)
- PM-2 design history file (PLM)

## 13. Acronym List and Glossary
- **BAA:** business associate agreement
- **CVD:** coordinated vulnerability disclosure
- **DCS:** Device Cloud Service
- **HSM:** hardware security module
- **MDR:** medical device report (21 CFR Part 803)
- **MFA:** multi-factor authentication
- **PHI:** protected health information
- **POA&M:** plan of action and milestones
- **QMSR:** Quality Management System Regulation (21 CFR Part 820)
- **SBOM:** software bill of materials

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-09-04 | Initial plan | IT Manager with the Cloud Operations Lead |
