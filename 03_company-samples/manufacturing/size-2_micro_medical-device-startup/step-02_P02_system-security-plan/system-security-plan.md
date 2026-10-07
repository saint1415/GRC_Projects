# System Security Plan: Product Development and Release Platform (PDRP)

**Organization:** Cris Santos Company, LLC (medical device startup) | **Tier:** Micro | **Vertical:** Manufacturing (NAICS 334510)
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Product Development and Release Platform (**PDRP**), identifier CSC-SYS-001. This is the "device software development and manufacturing systems" system for this company: the platform that designs, builds, signs, tests, and distributes WM-1 software. The company has no MES of its own; manufacturing runs on the contract manufacturer's MES, which is an external interconnection (section 8).

## 2. System Overview
The PDRP supports every engineering and quality process of the startup: firmware and cloud development, firmware signing and release, design verification, the design history file, the 510(k) submission, and the handoff of released software to the contract manufacturer. It serves 7 employees, one contract firmware developer at a time, and the regulatory consultant.

The company owns almost no infrastructure. Most of the PDRP is SaaS, one workload runs in a public cloud tenant, and a managed service provider (MSP) runs the laptops and the office network. The MSP contract does not cover the engineering systems (repository, cloud tenant, lab workstations, signing key). This plan says, for each control, what the company does itself, what the MSP does for it, and what it inherits from a provider.

**Why this system matters.** Section 524B(b)(2) of the FD&C Act requires "processes and procedures to provide a reasonable assurance that the device and related systems are cybersecure." FDA's premarket guidance (issued 2026-02-03, section VII.C.2) counts software and firmware update servers as related systems. Whoever controls the PDRP controls what code runs on every WM-1 unit, now and after clearance.

**Major components:**
- **SYS-01:** source code repository and CI/CD service (SaaS), with hosted build runners
- **SYS-02:** eQMS and PLM (SaaS): design history file, risk management file, supplier records
- **SYS-03:** productivity suite (SaaS): email, files, chat, and the identity service for the suite and the eQMS
- **SYS-04:** WM-1 cloud service (pre-production) on a PaaS tenant: ingestion API, clinician dashboard, update service, managed database, key management service
- **SYS-05:** 7 MSP-managed laptops and 2 unmanaged lab workstations
- **SYS-06:** office and lab network (MSP-managed firewall; the lab bench network is flat with the office)
- **SYS-07:** firmware signing key (a file on the Head of Engineering's laptop) and release tooling

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| N31-33-R05 | FD&C Act section 524B, cyber devices: CVD and postmarket plan (b)(1), secure processes and patching (b)(2), SBOM (b)(3) | 21 U.S.C. 360n-2. Applies to the planned 510(k) (P03) |
| QMSR | Quality management system regulation, incorporating ISO 13485 by reference; design and development controls for class II devices | 21 CFR Part 820 (820.1(a), 820.3, 820.10(c)); in effect since 2026-02-02 (89 FR 7496) |
| Guidance | *Cybersecurity in Medical Devices: Quality Management System Considerations and Content of Premarket Submissions* (issued 2026-02-03; nonbinding) | FDA guidance; used to decide what the submission must show |
| After marketing | Medical device reporting; corrections and removals; complaint records | 21 CFR Part 803; Part 806; 820.35(a). Procedures drafted now, obligations start at commercial distribution |
| Before distribution | Establishment registration and device listing | 21 CFR Part 807 |
| Planned | HIPAA Security Rule and breach notice as a business associate, once hospitals send patient data to the cloud service | 45 CFR Part 164, Subpart C; 164.410. Not in force for the company today: it holds no PHI |
| State | Florida Information Protection Act, for workforce personal information | Fla. Stat. 501.171 |
| Internal | Security policies POL-02, POL-03, POL-04 | P06 |

Not applicable: DFARS 252.204-7012 and CMMC (N31-33-R01, R02) and ITAR (R03), because the company has no defense work; EAR (R04), because it sells only in the United States.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the CEO on 2026-08-31.

### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization. The equivalent internal decision: on 2026-08-31 the CEO accepted continued operation of the PDRP for pre-market development, on the conditions that (1) no firmware is released to anyone outside the company lab and the partner hospital's evaluation network until the signing key is in an HSM-backed service with two-person approval (P01 R-001), and (2) the POA&M items in P07 are completed by their dates.

### 4.3 System Operational Status
Operational, under active development. **Planned re-categorization:** before the first commercial release, the integrity rating in section 6 rises to High, because a compromised release could then reach patients. The plan will be revised at design freeze (target 2026-12-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner and risk acceptor | CEO | Overall accountability; accepts risk; approves this plan, policies, and spending |
| Product Security Lead | Head of Engineering (part-time) | Threat model, SBOM, vulnerability intake, signing key custodian; release approval |
| Information Security Coordinator | Operations Manager | Corporate IT with the MSP; account onboarding and removal; cyber insurance |
| Quality and regulatory owner | QA/RA Manager | QMS, design history file, supplier control, section 524B compliance, submission |
| Cloud and repository administrator | Cloud Software Engineer | Cloud tenant, repository organization, CI pipeline |
| IT operations | MSP | Laptops, EDR, patching, suite administration, office network |
| Independent assessor | Medical device cybersecurity consultant | Annual control assessment (P07) |

**Overlap and compensation.** The Head of Engineering designs the platform, holds the signing key, and leads product security. The Cloud Software Engineer administers the systems they build on. At 7 people this cannot be avoided. The compensating checks are the independent P07 assessment, the third-party penetration test planned for 2026-12, and two-person signing once the key moves to an HSM-backed service.

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1 (management and support information) and adapted to a device developer. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| System development (source code, firmware images, signing key) | Moderate | Moderate | Moderate | Theft exposes the company's core asset; tampering could put malicious code in pre-production units; the signing key cannot be replaced without re-keying every unit (P05 BP-01, RPO 0). Integrity rises to High before commercial release |
| Record retention (design history file, risk management file) | Moderate | Moderate | Low | Regulatory evidence for the 510(k); vendor-hosted with a 72-hour MTD (P05 BP-02) |
| Information security (vulnerability data, threat model, test reports) | Moderate | Moderate | Low | Unfixed vulnerability details would help an attacker; availability is not time-critical |
| Human resources and financial management | Moderate | Low | Low | Workforce personal information (Fla. Stat. 501.171); payroll through an outside service |
| **PDRP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 7-person startup. The plan documents 45 controls (see `control-implementation.csv`): 42 from the Moderate baseline and 3 added because FDA's premarket guidance expects them (CA-8 penetration testing, CM-14 signed components, SA-11(2) threat modeling). All other Moderate-baseline controls are handled one of two ways:
- **Inherited** from the SaaS vendors and the cloud provider (physical and environmental, platform, and infrastructure controls). The cloud provider's SOC 2 Type 2 report is the main evidence (P09).
- **Tailored out** for this tier where the control addresses federal program management or organizations with dedicated IT staff. These are recorded as tailoring decisions, not gaps.

## 7. Authorization Boundary Description
- **Inside:** the company's repository organization and CI configuration (SYS-01), eQMS tenant (SYS-02), productivity suite tenant (SYS-03), cloud tenant and everything deployed in it (SYS-04), 7 laptops and 2 lab workstations (SYS-05), the office and lab network (SYS-06), and the signing key with its release tooling (SYS-07).
- **Outside (external services, interconnected):** the providers' own platforms and data centers; the MSP's remote management platform; the contract manufacturer's MES and test stations (SYS-09); the pre-production units (SYS-08), which are the product rather than part of the platform; the partner hospital's simulation center network; the regulatory consultant's systems.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Agreement |
|---|---|---|---|
| Contract manufacturer MES and test stations (SYS-09) | Outbound | Signed firmware images; hub provisioning file (contains the hub API key) | Quality agreement (no security terms; gap); shared folder link from SYS-03 |
| Pre-production units in the lab and at the simulation center (SYS-08) | Bidirectional | Test telemetry in; signed firmware updates out | Development and evaluation agreement with the partner hospital system |
| Partner hospital simulation center network | Bidirectional (through the hubs) | Test telemetry only; no patient data | Same agreement; hospital security team monitors the test network |
| MSP remote management platform | Inbound administrative | Laptop management | MSP service contract |
| Regulatory consultant | Outbound | Submission drafts, design history extracts | Consulting agreement with confidentiality terms |
| Third-party penetration test lab (from 2026-12) | Bidirectional | Test units, firmware, test accounts | Statement of work with confidentiality terms (to be signed) |
| FDA (from the pre-submission onward) | Outbound | Q-Submission and 510(k) documents | FDA electronic submission portal |

## 9. System Component Inventory
| Component | Type | Location or provider | Owner |
|---|---|---|---|
| Repository organization and CI configuration (SYS-01) | SaaS | Source code and CI service vendor | Cloud Software Engineer |
| eQMS and PLM tenant (SYS-02) | SaaS | eQMS vendor | QA/RA Manager |
| Productivity suite tenant (SYS-03) | SaaS | Productivity suite vendor | Operations Manager (MSP administers) |
| WM-1 cloud service tenant (SYS-04) | PaaS | Cloud provider (vendor-agnostic) | Cloud Software Engineer |
| Laptops (7) (SYS-05) | Endpoint | Office and remote | Operations Manager (MSP operates) |
| Lab workstations (2) (SYS-05) | Endpoint | Engineering lab | Verification and Test Engineer |
| Firewall, Wi-Fi, lab bench network (SYS-06) | Network | Office network closet and lab | Operations Manager (MSP operates) |
| Signing key file and backup USB drive (SYS-07) | Cryptographic key | Head of Engineering's laptop; office safe | Head of Engineering |

A full inventory, including the pre-production units and third-party software components, is planned in the eQMS by 2026-10-31 (CM-8).

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 45 controls:
- Implemented: 4
- Partially implemented: 26
- Planned: 15
- Not applicable: 0

By responsibility: 25 system-specific (the company), 19 hybrid (the company with the MSP, a SaaS vendor, the cloud provider, or the contract manufacturer), 1 common/inherited (fully provided by the providers).

**What the numbers say.** The company has the device-side security features that engineers think about (secure boot, signed updates, TLS). It lacks the processes around them: who can sign, how credentials are issued, how vulnerabilities are found and handled, and how the contract manufacturer is controlled. Those processes are exactly what section 524B(b)(1)-(2) requires the submission to describe.

### 10.2 Inherited and MSP-provided controls
| Provider | What the company relies on | Evidence | What the company must still do |
|---|---|---|---|
| Cloud provider | Physical security, platform patching, encryption at rest by default (SC-28), activity logging (AU-2), snapshot mechanism (CP-9) | SOC 2 Type 2 report reviewed 2026-08-24 (P09) | Complementary user entity controls: identity and roles, MFA, key management, backup settings and restore tests, log retention and review |
| Source code and CI service vendor | Platform security, audit log (AU-2), MFA enforcement option (IA-2(1)), branch protection (AC-3) | Vendor documentation; SOC 2 report not yet requested | Organization settings, member removal, secrets handling in CI, permission review |
| eQMS vendor | Platform security, electronic signatures, backups (CP-9) | Contract; SOC 2 report not yet requested | Role assignment, periodic export, validation of the eQMS for its intended use (ISO 13485 cl. 4.1.6) |
| Productivity suite vendor | Platform security, sign-in lockout (AC-7), encryption in transit (SC-8) | Vendor documentation | Account management, MFA, sharing-link settings |
| MSP | Laptop EDR (SI-3), patching (SI-2), encryption (SC-28), firewall (SC-7), suite administration | Monthly MSP report; P07 evidence requests | Oversight; add the lab workstations to the contract (P01 R-016) |
| Contract manufacturer | Handling of firmware images and provisioning files at its test stations | Quality agreement; ISO 13485 certificate | Add security terms and review them at the supplier audit (SR-3, SR-6) |

**Inherited does not mean done.** The cloud provider's report lists complementary user entity controls. Three are open gaps at the company: the shared owner account (IA-2), restore testing (CP-4), and log review (AU-6).

### 10.3 Control assessment status
Assessed 2026-08-10 to 2026-08-12 by an independent consultant. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
Workforce users sign in to the suite, eQMS, repository, and cloud console with a password and a phone authenticator app. This is appropriate for the Moderate category. Two exceptions are tracked: the shared cloud owner account (MFA codes held on the CEO's phone) and the shared lab workstation login. Device identity (hub to cloud) is a separate product requirement: unique per-device certificates are planned before design freeze (IA-3).

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness and cloud provider report review (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **BLE:** Bluetooth Low Energy
- **CI/CD:** continuous integration and continuous delivery
- **CVD:** coordinated vulnerability disclosure
- **eQMS:** electronic quality management system
- **HSM:** hardware security module
- **MES:** manufacturing execution system
- **MSP:** managed service provider
- **PDRP:** Product Development and Release Platform
- **PLM:** product lifecycle management
- **QMSR:** Quality Management System Regulation (21 CFR Part 820)
- **SBOM:** software bill of materials

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan | Operations Manager with the Head of Engineering |
