# System Security Plan: Shared Corporate Services Platform (SCSP)

**Organization:** Cris Santos Company Holdings, Inc. (holding company and corporate shared services, serving the Insurance and Health Care Services divisions) | **Tier:** Multi-Sector | **Vertical:** Management of Companies and Enterprises
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-15

> **Why this system.** At this tier the SSP can cover one system per division or a shared corporate system. The group chose the **Shared Corporate Services Platform**, the holding company's own system, because every subsidiary depends on it (P05: identity has a 4-hour MTD for all three divisions), it moves about $65 million a day, it carries the group's financial reporting (SOX 404), and its identity component is the largest common control provider in the group. Division systems keep their own plans (for example, the Health Care Services EHR plan and the insurers' claims system plan) and inherit from the same common control catalog (`common-control-catalog.csv`).

## 1. System Name and Identifier
Shared Corporate Services Platform (**SCSP**), identifier CSCH-SCSP-01. It combines SYS-G1, SYS-G4, SYS-G5, and SYS-G6 in `../00_company-facts.md`.

## 2. System Overview
The SCSP is how the holding company delivers its shared services:
- **Identity (SYS-G1):** sign-in, MFA, PAM, identity governance, and the corporate directory for about 52,000 workforce identities, 1,240 service accounts, and about 900 federated applications in all three divisions.
- **ERP and consolidation (SYS-G4):** general ledger for 64 legal entities, payables, fixed assets, intercompany, consolidation, and the close. 3,100 users.
- **HCM and payroll (SYS-G5):** HR records, payroll, and benefits enrollment for 45,000 employees and about 60,000 former employees. It sends the eligibility feed to the group health plan's third-party administrator.
- **Treasury and payments hub (SYS-G6):** bank connectivity to 14 banks, wires, ACH, positive pay, claims disbursement files from Insurance, patient refund files from Health Care Services, and payroll funding. 260 users.
- **Integration services (provider A):** integration flows and managed file transfer that connect division systems, the four applications, and the banks.

**Who uses it:** shared services staff (finance, treasury, HR, payroll, IT), division finance and HR staff, and every workforce user for sign-in. No customers, patients, or policyholders sign in to the SCSP.

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies to the SCSP |
|---|---|---|---|
| N55-R03 | SOX section 404 | 15 U.S.C. 7262 | The ERP, HCM, and treasury are in scope for IT general controls (logical access, change management, computer operations). The group is a large accelerated filer, so the external auditor attests (7262(b)) |
| N55-R01 | Reg S-K Item 106 | 17 CFR 229.106 | The annual disclosure describes the processes that protect the SCSP, the use of third-party assessors, and oversight of third-party service providers (106(b)(1)(i)-(iii)) |
| N55-R02 | Form 8-K Item 1.05 | Release 33-11216 | An SCSP incident can be material to the group (P08) |
| N55-R06 | HIPAA, group health plan | 45 CFR 164.504(f); 164.314(b) | The holding company is plan sponsor. HCM benefits data and plan administration PHI must stay within the plan administration unit (164.504(f)(2)(iii)). The plan documents have not been amended with the security terms in 164.314(b)(2) (P03) |
| N62-R01 | HIPAA Security Rule (business associate) | 45 CFR Part 164, Subpart C | The holding company is a business associate of Health Care Services. The SCSP handles clinic patient refund files (ePHI) and controls access to the clinic EHR through SYS-G1 |
| N52-R07 | State insurance data security laws based on NAIC Model #668 | Enacted in Alabama and South Carolina, and in part in Tennessee | The holding company is a Third-Party Service Provider of the insurers (Model sec. 3P). The insurers must exercise due diligence and require it to protect their Nonpublic Information (sec. 4F) |
| Fla. Stat. 628.801 | Insurance holding company system | 628.801(1)-(3) | The holding company files the annual enterprise risk report; the Office of Insurance Regulation may examine the insurers' affiliates, including the SCSP |
| Fla. Stat. 501.171 | Florida Information Protection Act (worked example of state law) | 501.171(2) | Reasonable measures to protect personal information of employees, claimants, and patients in SCSP records |
| Internal | Group policies POL-01 to POL-05 and division supplements | P06 | |

Not applicable: Federal Reserve Regulation Y Subpart N and 12 CFR Part 225 Appendix F (the group owns no bank); the FTC Safeguards Rule (the insurers are under state insurance authorities, 15 U.S.C. 6805(a)(6), and no group entity is a non-bank lender).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Group CIO (system owner) and the Group CISO on 2026-09-15, after the board risk committee review.

### 4.2 System Authorization Decision
The group is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- **Decision:** authorized to operate with conditions, 2026-09-15, by the Group CIO and the Group CISO, with the Group Chief Risk Officer accepting the High risks under treatment.
- **Conditions:**
  1. Remove group-wide password and MFA reset rights from division help desks and require identity verification for MFA resets by 2026-11-30 (POAM-001).
  2. Close the directory trust from the acquired clinics' legacy directory, or approve it with monitoring, by 2026-12-31 (POAM-006).
  3. Stop the benefits export to the general HR collaboration site by 2026-10-31 (POAM-005).
  4. Bring all ERP superuser accounts under PAM by 2026-12-31 (POAM-003).
- **Reauthorization:** annually, or after the identity platform redesign.

### 4.3 System Operational Status
Operational. **Major modification planned:** division-scoped administration in SYS-G1 (tiered roles per division, help desk scoping), due 2027-03-31 (P01 GR-01).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Group CIO | Accountable for the SCSP and this plan |
| Authorizing official equivalent | Group CIO with the Group CISO | Authorization decision |
| Platform operations | SCSP platform director | Runs the integration services and coordinates the four applications |
| Component owners | Group identity director (SYS-G1); Group Controller (SYS-G4); Group Chief Human Resources Officer (SYS-G5); Group Treasurer (SYS-G6) | Application roles, access approvals, and configuration |
| Privacy | Group Chief Privacy Officer; group health plan privacy official (Group benefits director) | Purposes for HCM and benefits data; the plan sponsor firewall |
| Common control providers | Group SOC director (SYS-G2); Group infrastructure director (SYS-G3); Group HR; Group risk management; group security governance office | Operate inherited controls (`common-control-catalog.csv`) |
| Independent assessor | Group internal audit | Assesses common controls once and samples division controls (P07); tests SOX IT general controls |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Personnel management and payroll (HCM, payroll, benefits enrollment) | **High** | Moderate | Moderate | Raised from the provisional level for aggregation: SSNs and bank accounts of about 105,000 current and former employees, and plan PHI. Payroll RTO is 24 hours (P05 BP-G05) |
| Accounting and financial reporting (ERP, consolidation) | Moderate | **High** | Moderate | Errors or tampering would misstate SEC financial statements. Unreleased results are MNPI |
| Funds control and payments (treasury, integration) | Moderate | **High** | **High** | About $65 million a day; a fraudulent change could redirect payments. MTD 8 hours (P05 BP-G04, BP-G12) |
| Information security (identity, credentials, keys) | **High** | **High** | **High** | Compromise of SYS-G1 exposes all three divisions; identity MTD 4 hours (P05 BP-G01) |
| **SCSP category (high-water mark)** | **High** | **High** | **High** | Overall **High** |

**Baseline:** the NIST SP 800-53B **High** baseline, tailored. The plan documents **174 controls** in `control-implementation.csv`:
- 166 from the High baseline;
- 5 from the privacy baseline (PM-9, PM-10, PM-11, PT-2, PT-3), added because the SCSP holds employee PII and plan PHI;
- 3 program management controls not in any baseline (PM-1, PM-2, PM-30).

Other High-baseline controls are either fully inherited from the SaaS vendors and cloud providers (for example, most physical and environmental controls, evidenced by their SOC 2 Type 2 reports) or tailored out with a reason in the tailoring register (for example, controls for facilities the group does not operate).

## 7. Authorization Boundary Description
- **Inside:** the SYS-G1 identity tenant and directory servers, the SYS-G4 ERP tenant, the SYS-G5 HCM tenant, the SYS-G6 treasury tenant, and the SCSP integration services and managed file transfer in provider A (with the warm standby in provider B).
- **Outside, inherited (common control providers):** SYS-G2 (SOC, SIEM, EDR) and SYS-G3 (landing zones, network, colocation, backup vault); group HR, risk, governance, and internal audit functions.
- **Outside, interconnected:** banks; the health plan's third-party administrator; division systems SYS-I1, SYS-I2, SYS-I4, and SYS-H1; the productivity suite SYS-G7.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Agreement |
|---|---|---|---|
| 14 banks | Outbound payment files; inbound statements and confirmations | Payments, beneficiary bank details | Bank agreements; mutual TLS or private links |
| Health plan third-party administrator | Outbound eligibility feed | Plan enrollment (PHI) | Administrator BAA with the plan |
| SYS-I2 and SYS-I4 (Insurance) | Inbound claims disbursement files; outbound payment status | Claimant names, amounts, bank details (Nonpublic Information) | 2017 intercompany services agreement (**no security schedule**, scenario gap 2; POAM-016) |
| SYS-H1 (Health Care Services) | Inbound patient refund files; general ledger feeds | Patient names and refund amounts (ePHI) | 2021 business associate agreement |
| All division systems | Inbound general ledger feeds; outbound sign-in (SAML or OIDC) | Financial data; authentication | Integration route catalog |
| SYS-G7 HR collaboration site | Outbound scheduled benefits export | Benefits enrollment and case data (plan PHI) | **None; to be stopped** (POAM-005) |
| Acquired clinics' legacy directory | Two-way directory trust | Authentication | **No interconnection agreement** (POAM-006) |
| ERP vendor support | Inbound support sessions | Full ERP access | Vendor contract; **3 standing superusers** (POAM-003) |

## 9. System Component Inventory
| Component | Type | Location or provider | Owner |
|---|---|---|---|
| Identity tenant (SSO, MFA, identity governance) | SaaS | Identity SaaS vendor | Group identity director |
| PAM service and jump hosts | IaaS | Provider A | Group identity director |
| Corporate directory servers (6) | IaaS and colocation servers | Provider A; colocation | Group identity director |
| ERP tenant | SaaS | ERP SaaS vendor | Group Controller |
| HCM and payroll tenant | SaaS | HCM SaaS vendor | Group Chief Human Resources Officer |
| Treasury tenant | SaaS | Treasury SaaS vendor | Group Treasurer |
| Integration services and managed file transfer | PaaS | Provider A; warm standby in provider B | SCSP platform director |
| Integration storage and keys | Object storage; customer-managed keys | Provider A | Group infrastructure director |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv` (174 controls) and `common-control-catalog.csv` (94 group common controls).

| Status | Controls |
|---|---|
| Implemented | 154 |
| Partially implemented | 20 |
| Planned | 0 |
| Not applicable | 0 |
| **Total** | **174** |

| Inheritance | Controls |
|---|---|
| Common/Inherited (from SYS-G2, SYS-G3, group functions, or the cloud providers) | 89 |
| Hybrid (a group provider supplies the mechanism; the SCSP configures or operates part) | 17 |
| System-specific (including the identity controls the SCSP itself provides to the divisions) | 68 |

**The 20 partially implemented controls** cluster in four places:
- **Identity administration and reset** (scenario gap 1): AC-2, AC-2(12), AC-6, IA-5, IA-12, IA-12(2), AT-2(3), CA-3, SI-4.
- **ERP privileged access** (gap 4): AC-5, AC-6(5), AC-6(7), SA-9.
- **Plan sponsor separation** (gap 3): AC-4, PT-3.
- **Resilience and group coordination** (gaps 2 and 7): CP-4, CP-7, IR-3, IR-6, PM-30.

### 10.2 Common control inheritance by division
The common control catalog lists 94 controls provided once by the group. The SCSP is unusual: its identity component (SYS-G1) is itself the provider of 20 common controls, so for those controls the SCSP is the provider, not an inheritor.

| Division | Inheritance documentation | Status |
|---|---|---|
| Insurance | Insurance inheritance matrix (2025), used in the insurers' information security programs | Documented |
| Health Care Services | 2024 inheritance matrix for SYS-H1 to SYS-H3 | **Not documented for the 50 acquired clinics** (scenario gap 8; POAM-019) |
| SCSP | This plan | Documented |

### 10.3 Control assessment status
Common controls were assessed once, and SCSP and division controls sampled, from 2026-07-06 to 2026-08-28 by group internal audit. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
- **Workforce users** authenticate through SYS-G1 with number-matching MFA. **Administrators and high-risk business users** (treasury release, payroll changes, ERP privileged roles) use phishing-resistant hardware keys, and treasury requires step-up reauthentication to release payments (IA-11).
- **The weak point is recovery, not sign-in.** An attacker who persuades the help desk to reset MFA bypasses the strong authenticator entirely. The reset process must verify identity to the same strength as the authenticator it replaces (POAM-001; P08 scenario).
- **Service accounts** use workload identity where the platform supports it; 112 still lack a named owner (POAM-002).

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), group and division risk registers (P01), gap analyses and regulation-by-division matrix (P03), cloud architecture and control map (P04), BIA (P05), group policies and division supplements (P06), assessment and POA&M (P07), incident response runbook and notification matrix (P08), SOC 2 readiness (P09), AI governance (P10).

## 13. Acronym List and Glossary
- **Common control:** a control provided once by the group and inherited by several systems
- **HCM:** human capital management (HR and payroll system)
- **ITGC:** IT general controls tested for SOX 404
- **MNPI:** material non-public information
- **PAM:** privileged access management
- **SCSP:** Shared Corporate Services Platform
- **TPSP:** Third-Party Service Provider, as Model #668 sec. 3P defines it

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-08-28 | Draft after P07 fieldwork | SCSP platform director |
| 1.0 | 2026-09-15 | Approved with authorization conditions | Group CIO |
