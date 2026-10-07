# System Security Plan: Group Workforce Platform (GWP)

**Organization:** Cris Santos Company Holdings, Inc. (corporate shared services, serving the Staffing, Consulting, and Home Health divisions) | **Tier:** Multi-Sector | **Vertical:** Administrative and Support and Waste Management and Remediation Services
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-10

> **Why this system.** At this tier the SSP can cover one system per division or a shared corporate system. The group chose the **Group Workforce Platform**, the shared payroll and applicant tracking platform, because every division hires, credentials, and pays its workers on it, it holds the group's most sensitive personal data (SSNs, bank accounts, Form I-9 records, consumer reports, clinician medical screening files), it inherits most of its controls from corporate (SYS-G1 to SYS-G3), and it carries the group's top risk (P01 GR-01). Division systems (SYS-D1 to SYS-D3) keep division SSPs that inherit from the same common control catalog (`common-control-catalog.csv`).

## 1. System Name and Identifier
Group Workforce Platform (**GWP**), identifier CSCH-SYS-G4. SYS-G4 in `../00_company-facts.md`.

## 2. System Overview
The GWP runs the worker lifecycle for the whole group:
- **Staffing:** recruiting and onboarding about 610,000 associates a year, credentialing Healthcare Staffing clinicians, and the weekly associate payroll (about $190 million a week).
- **Consulting:** hiring and paying about 9,000 consultants, including Federal Solutions staff whose federal contracts require E-Verify (48 CFR 52.222-54).
- **Home Health:** hiring, credentialing, and paying about 18,000 employees, including per-visit pay for field clinicians.
- **Corporate:** hiring and paying corporate staff.

About 9,600 staff users (recruiters about 6,100; onboarding and compliance about 1,400; payroll about 640; credentialing about 380; HR and associate service about 900; administrators about 180) work in it. About 1.1 million associates and employees have self-service accounts, and about 7.2 million candidate profiles sit in the ATS.

**Major components:**
- **ATS and career sites:** a staffing-industry enterprise ATS (vendor SaaS), with an AI ranking add-on from a third-party AI vendor (P10 AI-001) and a conversational recruiting assistant (AI-002)
- **Onboarding and electronic Form I-9 service** (vendor SaaS): tax and direct deposit forms, Form I-9 with document images, background check ordering through two screening providers; E-Verify cases are created by named users on the DHS E-Verify website
- **Credentialing service** (vendor SaaS): licenses, certifications, immunization and tuberculosis records, drug screens, and post-offer physicals for about 96,000 clinicians
- **Payroll and pay delivery engine:** commercial payroll software, customer-managed on cloud provider A, with a tokenization service for SSNs and bank account numbers, an associate self-service app, and bank and paycard file delivery
- **Integration platform:** containers on provider A, built by the group workforce technology team; receives approved time from SYS-D1, visit records from SYS-D3, and consultant timesheets from SYS-D2
- **Workforce data hub:** a managed analytical database on provider A for workforce reporting and AI monitoring
- **I-9 archive:** object storage on provider A holding about 0.9 million scanned paper Forms I-9 (2009-2016)
- **DR replica and immutable backup vault** on provider B

The platform is described by service category and is vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies to the GWP |
|---|---|---|---|
| N56-BM | NIST CSF 2.0 (voluntary benchmark) | NIST CSWP 29 | Group program benchmark; Target Profile in P03 |
| N56-R03 | Form I-9 retention and electronic I-9 standards | 8 CFR 274a.2(b)(2), (e)-(i) | Every division's Forms I-9 are completed and kept in the onboarding service and the I-9 archive. Paragraph (g)(1) sets the records security program: authorized access only, backup and recovery, trained staff, and a permanent audit record |
| E-Verify MOU | MOU for Employers (each employing entity); Federal contractor terms for Consulting (MOU Art. II.B; FAR 52.222-54) | MOU Art. II.A.3, II.A.5, II.A.15, II.A.16 | User access, tutorial, safeguarding of case data and passwords, and **immediate notice to DHS** of a breach of E-Verify personal data |
| N56-R02 | FCRA employment background checks | 15 U.S.C. 1681b(b) | Disclosure and authorization forms and consumer reports stored in onboarding |
| N56-R01 | FTC/FACTA Disposal Rule | 16 CFR 682.3 | Disposal of consumer report information |
| ADA | Confidential medical files | 29 CFR 1630.14(b)(1) | Post-offer physicals and medical screening results in credentialing must be kept on separate forms in separate, confidential medical files |
| N62-R01, N62-R02, N62-R03 | HIPAA Security, Privacy, and Breach Notification Rules | 45 CFR Part 164 | Workers' own employment records are not PHI (45 CFR 160.103 excludes employment records held by a covered entity as employer). But the Home Health visit-pay feed puts **patient** names and addresses in the GWP, so corporate acts as Home Health's business associate for that data (scenario gap 1) |
| State law | State breach and data security laws | Each state where affected individuals reside; Florida worked example Fla. Stat. 501.171 | The GWP holds personal information (SSNs, driver license and passport numbers) for workers in every state the group operates in |
| CCPA | California Consumer Privacy Act | Cal. Civ. Code 1798.100 et seq. | Employee and applicant data of California residents is in scope; CPPA ADMT rules apply to the AI ranking add-on from 2027-01-01 (P10) |
| N56-R08 | NYC Local Law 144 | NYC Admin. Code 20-870 et seq. | The AI ranking add-on is used for NYC requisitions |
| SEC | Reg S-K Item 106; Form 8-K Item 1.05 | 17 CFR 229.106 | A GWP incident may be material to the group (P08); payroll is in SOX scope |
| Internal | Group policies POL-01 to POL-05 and division supplements | P06 | |

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Group CISO and the group workforce platform director (system owner) on 2026-09-10, after the board risk committee review.

### 4.2 System Authorization Decision
The group is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- **Decision:** authorized to operate with conditions, 2026-09-10, by the Group CISO and the Group Chief Risk Officer (acceptance authority for High risks).
- **Conditions:** (1) the visit-pay interface stops carrying patient names and addresses by 2026-12-31, and existing records are purged or restricted by 2027-03-31 (POAM-006); (2) bank-account changes in associate self-service require phishing-resistant or out-of-band confirmation by 2027-03-31 (POAM-008); (3) no new GWP interface or AI feature goes live without a privacy impact assessment (RA-8).
- **Reauthorization:** annually, or when the visit-pay redesign and self-service authentication changes are complete.

### 4.3 System Operational Status
Operational. **Major modifications planned:** visit-pay interface redesign (anonymous visit IDs), associate self-service authentication upgrade, and E-Verify user management through identity governance.

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Group workforce platform director | Accountable for the GWP and this SSP |
| Authorizing official equivalent | Group CISO with the Group Chief Risk Officer | Authorization decision; High risk acceptance |
| Business owners | Group payroll director; group talent acquisition technology director; group credentialing director | Payroll, ATS and onboarding, and credentialing components |
| Employment compliance owner | Staffing Vice President, Employment Compliance | Form I-9, E-Verify, and FCRA procedures for all divisions |
| Privacy oversight | Group Chief Privacy Officer | Processing register, purposes, privacy impact assessments |
| Home Health data owner | Home Health HIPAA Privacy Officer | Approves any use of Home Health patient data in the GWP |
| Common control providers | Group identity director (SYS-G1), Group SOC director (SYS-G2), Group cloud platform director (SYS-G3) | Operate inherited controls (`common-control-catalog.csv`) |
| Independent assessor | Group internal audit | Assesses common controls once and samples division controls (P07) |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1 (human resource management types) and adjusted for aggregation. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Payroll management and pay delivery | **High** | **High** | Moderate | SSNs and bank accounts for about 3.4 million current and former workers; altered bank data diverts pay at scale (scenario gap 2); repeat-payroll workaround holds about 48 hours (P05 BP-G04) |
| Staff recruitment and employment (candidates, onboarding, Form I-9, consumer reports) | **High** | Moderate | Moderate | Identity documents and consumer reports for millions of people; Form I-9 deadlines (P05 BP-G05) |
| Personnel medical screening (clinician credentialing) | **High** | Moderate | Moderate | Confidential medical files (29 CFR 1630.14(b)(1)); clinicians cannot work without verified credentials |
| Health care delivery services (Home Health visit records in visit-pay data) | Moderate | Low | Low | Patient names, addresses, dates, and visit type; should not be in the GWP at all (gap 1) |
| Information security (keys, tokenization vault, logs) | High | High | Moderate | Compromise would expose every data store |
| **GWP category (high-water mark)** | **High** | **High** | **Moderate** | Overall **High** |

**Baseline:** the NIST SP 800-53B **High** baseline, tailored. The plan documents **120 controls** in `control-implementation.csv`:
- 113 from the High baseline;
- 5 from the privacy baseline (PM-9, PM-10, PT-2, PT-3, RA-8), added because purpose and minimum-necessary failures are the platform's main privacy risk;
- 2 program management controls not in any baseline (PM-1, PM-2).

Other High-baseline controls are either fully inherited from the cloud providers and SaaS vendors (for example, most PE controls, evidenced by their SOC 2 Type 2 reports) or tailored out with a reason in the group tailoring register.

## 7. Authorization Boundary Description
- **Inside:** the group's tenants and configuration of the ATS, onboarding and I-9, and credentialing services; the payroll engine, integration platform, data hub, and I-9 archive accounts in provider A; the DR replica and backup vault in provider B.
- **Outside, inherited (common control providers):** SYS-G1 identity platform, SYS-G2 SOC, SIEM, and EDR, and the SYS-G3 landing zone (network hub, logging account, guardrails).
- **Outside, interconnected:** SYS-D1 (Staffing time capture and VMS feeds), SYS-D2 (Consulting timesheets), SYS-D3 (Home Health visit records), the two background screening providers, DHS E-Verify (used by named users through its own website), two ACH originating banks, and the paycard program manager.

The diagram is in P04 `cloud-architecture.md` (the GWP subgraph).

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| SYS-D1 Staffing time capture and client VMS feeds | Inbound (hourly) | Approved time, assignments, pay and bill rates | Internal interface specification |
| SYS-D2 Consulting engagement systems | Inbound (weekly) | Consultant timesheets | Internal interface specification |
| SYS-D3 Home Health scheduling and EVV | Inbound (daily) | Visit records for per-visit pay. **Gap:** includes patient name, address, visit date, and visit type (about 214,000 patients since 2024-04) | Intercompany BAA (2023-10) covers IT hosting, identity, SOC, and EHR integration, **not payroll** (POAM-024) |
| Background screening providers (2) | Outbound orders; inbound reports | Candidate identity data; consumer reports | Provider agreements with FCRA certifications (15 U.S.C. 1681b(b)(1)(A)) |
| DHS E-Verify | Manual entry by named users | Form I-9 data; case results | MOU for Employers per employing entity |
| ACH originating banks (2); paycard program manager | Outbound | Pay files with bank account numbers | Bank agreements; file encryption |
| AI ranking add-on vendor | Outbound | Resumes and application answers | Vendor agreement (allows model training on candidate data; POAM-009, POAM-012) |
| Tax filing service | Outbound | Wage and tax data | Service agreement |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| ATS, career sites, AI ranking add-on | SaaS | ATS vendor; AI vendor | Group talent acquisition technology director |
| Onboarding and electronic Form I-9 service | SaaS | Onboarding vendor | Group talent acquisition technology director |
| Credentialing service | SaaS | Credentialing vendor | Group credentialing director |
| Payroll and pay delivery engine, self-service app, tokenization service | Customer-managed software on IaaS and PaaS | Provider A | Group payroll director |
| Integration platform | Managed containers (PaaS) | Provider A | Group workforce platform director |
| Workforce data hub | Managed analytical database (PaaS) | Provider A | Group workforce data director |
| I-9 archive | Object storage | Provider A | Staffing Vice President, Employment Compliance |
| DR replica and immutable backup vault | Database replica; backup service | Provider B | Group cloud platform director |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv` (120 controls) and `common-control-catalog.csv` (102 group common and hybrid controls).

| Status | Controls |
|---|---|
| Implemented | 102 |
| Partially implemented | 18 |
| Planned | 0 |
| Not applicable | 0 |
| **Total** | **120** |

| Inheritance | Controls |
|---|---|
| Common/Inherited (from SYS-G1, SYS-G2, SYS-G3, group functions, or the cloud providers) | 75 |
| Hybrid (group provides the mechanism; the platform configures or operates part) | 27 |
| System-specific | 18 |

**The 18 partially implemented controls** cluster in four places:
- **Home Health patient data and purpose** (scenario gap 1): AC-4, AC-6, CM-12, PT-2, PT-3, RA-8, SI-12.
- **Associate self-service and bank changes** (gap 2): IA-2(2), AU-6.
- **Accounts, secrets, and the I-9 archive** (gap 8): AC-2, IA-5, AU-12.
- **Governance across divisions and vendors** (gaps 4, 5, and 6): CA-2, PL-2, IR-3, IR-8, CP-4, SA-9.

### 10.2 Common control inheritance by division
The common control catalog lists 102 controls provided wholly or partly by corporate. Inheritance is **documented for Staffing** (2025 inheritance matrix), for **Consulting** (2026 matrix, including the Federal Solutions enclave), and for the GWP (this plan). It is **not documented for Home Health** (scenario gap 6). Until POAM-021 closes, Home Health cannot show which HIPAA safeguards are met by group controls, and P07 found CA-2 statements other than satisfied for this reason.

### 10.3 Control assessment status
Common controls were assessed once, and GWP and division controls sampled, from 2026-07-01 to 2026-08-31 by group internal audit. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
- **Staff users** authenticate through SYS-G1 federated sign-in with number-matching MFA; **administrators** use phishing-resistant hardware keys and just-in-time PAM elevation. This fits a High-confidentiality system.
- **Associates and employees** use the self-service app with an SMS one-time code. SMS is a restricted authenticator, and the same code approves bank-account changes, which is how 690 diversions happened in 2025. The target is a passkey or app-based authenticator with out-of-band confirmation of bank changes (POAM-008).
- **Candidates** use email-verified career-site accounts; they see only their own applications.
- **E-Verify** users authenticate to the DHS website with credentials that DHS issues; the group controls who has an account but not the authenticator (POAM-001, POAM-002).
- **Service accounts** should use workload identity with short-lived tokens; 41 still use static secrets (POAM-002).

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), group and division risk registers (P01), gap analyses and regulation-by-division matrix (P03), cloud architecture and control map (P04), BIA (P05), group policies and division supplements (P06), assessment and POA&M (P07), incident response runbook and notification matrix (P08), SOC 2 readiness (P09), AI governance (P10).

## 13. Acronym List and Glossary
- **ATS:** applicant tracking system
- **BAA:** business associate agreement
- **Common control:** a control provided once by corporate and inherited by several systems
- **EVV:** electronic visit verification
- **GWP:** Group Workforce Platform
- **PAM:** privileged access management
- **SIEM:** security information and event management
- **Tokenization:** replacing an SSN or bank account number with a token; the real value is kept in a separate vault
- **VMS:** vendor management system

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-08-31 | Draft after P07 fieldwork | Group workforce platform director |
| 1.0 | 2026-09-10 | Approved with authorization conditions | Group CISO |
