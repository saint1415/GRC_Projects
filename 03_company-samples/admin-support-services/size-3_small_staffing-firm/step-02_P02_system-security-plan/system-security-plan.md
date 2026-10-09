# System Security Plan: Associate Payroll and Applicant Tracking Platform (APATP)

**Organization:** Cris Santos Company, LLC (temporary staffing firm) | **Tier:** Small | **Vertical:** Administrative and Support and Waste Management and Remediation Services
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Associate Payroll and Applicant Tracking Platform (**APATP**), identifier CSC-SYS-001.

## 2. System Overview
The APATP supports the firm's core cycle from applicant to paycheck: recruiting and applicant screening, onboarding (tax forms, direct deposit, Form I-9, background checks, E-Verify), time capture and client approval, weekly associate payroll, and client invoicing. It is used by the 60 internal staff at headquarters and 3 other Florida branches, by about 450 associates on assignment in an average week (self-service and timekeeping), and by client supervisors who approve time.

**Major components:**
- **SYS-01:** a SaaS staffing ATS and onboarding platform with the electronic Form I-9 module and client portal
- **SYS-02:** a SaaS payroll and billing platform
- **SYS-03:** an identity provider for single sign-on and MFA
- **SYS-04:** a public-cloud tenant hosting the integration service, reporting database, document archive, and backup vault
- **SYS-06:** a SaaS mobile timekeeping app with GPS clock-in
- **SYS-10 and SYS-11:** office networks and endpoints, including 8 lobby applicant kiosks

The cloud tenant is described by service category and is vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| N56-R03 | Form I-9 retention, inspection, and electronic I-9 standards | 8 CFR 274a.2(b)(2), (b)(3), (e)-(i) |
| E-Verify | E-Verify Memorandum of Understanding (employer) | MOU Art. II.A (access, tutorial, use limits, safeguarding, breach notice to DHS) |
| State | Florida E-Verify statute | Fla. Stat. 448.095(2) (25 or more employees; 3-year retention of documentation and verifications) |
| N56-R02 | FCRA employment background checks | 15 U.S.C. 1681b(b)(1)-(3); 1681m(a) |
| N56-R01 | FACTA Disposal Rule | 16 CFR 682.3 |
| State | Florida Information Protection Act (data security, breach notice, disposal) | Fla. Stat. 501.171 |
| Federal | Title VII disparate impact (applies to the AI screening add-on) | 42 U.S.C. 2000e-2(b), (k) |
| Benchmark | NIST CSF 2.0 (voluntary; label N56-BM) | P03 |
| Internal | Security policies POL-01 to POL-05 | P06 |

Not applicable: HIPAA (N56-R04), PCI DSS (N56-R06), FAR 52.204-21 (N56-R07), NYC Local Law 144 (N56-R08), TCPA/TSR (N56-R05), and PHMSA security plans (N56-R09). Reasons are in the intake [obligations register](../step-00_P00_intake/obligations-register.csv) and P03 section 1.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the COO on 2026-08-31.
### 4.2 System Authorization Decision
The firm is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- The COO accepted operation of the APATP on 2026-08-31, with the conditions in the P07 POA&M.
- The President accepted the High risks listed in P01, with dated treatment plans.
### 4.3 System Operational Status
Operational. Major modifications planned: payroll platform SSO (P01 R-001, due 2026-11-30), reporting database minimization (R-005, due 2026-11-30), and backup redesign (R-004, due 2026-12-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | COO | Overall accountability; risk acceptance up to Moderate |
| Risk acceptor (authorizing official equivalent) | President (majority owner) | Acceptance of High and Very High risks |
| Information Security Lead | IT Manager | Day-to-day security; maintains this plan |
| Records and screening compliance | HR and Compliance Manager | Form I-9, E-Verify, FCRA, retention, breach notices with counsel |
| Payroll process owner | Payroll Manager | Payroll platform users, bank-change controls, payroll continuity |
| Recruiting process owner | Director of Recruiting | ATS recruiting workflow and the AI screening add-on |
| Operations support | Managed IT provider | After-hours EDR monitoring; branch network changes |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Personnel records and employment eligibility (applicant, associate, I-9, consumer report data) | Moderate | Moderate | Low | SSNs and identity documents of about 31,000 people: disclosure causes identity theft and breach duties; altered I-9 records are a violation of INA 274A(b)(3) (8 CFR 274a.2(g)(2)); onboarding can fall back to paper for days (P05) |
| Payroll management and expense reimbursement (associate pay, bank accounts, tax) | Moderate | Moderate | Moderate | Diverted or wrong pay harms associates directly; payroll must run weekly (P05 MTD 48 h) |
| Customer services (client job orders, timesheet approvals, invoices) | Low | Moderate | Moderate | Limited sensitivity; wrong time or invoices cause disputes; clients need approvals weekly |
| **APATP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 60-person staffing firm. The plan documents 70 controls that carry the firm's legal duties (I-9, E-Verify, FCRA, Florida) and core security hygiene (see `control-implementation.csv`). Every other Moderate-baseline control is treated as follows:
- **Inherited** from the SaaS and cloud providers, as evidenced by their SOC 2 reports (P09 Part B) or service documentation.
- **Out of scope for this tier**, recorded as a tailoring decision, where the control's purpose applies only to federal systems. Examples: PM-series program-level controls beyond PM-1, PM-2, and PM-9.

Five controls outside the Moderate baseline were added by tailoring: three program-level controls that a small firm needs because the security program and this system share one owner, PM-1, PM-2, and PM-9; and two privacy controls that carry legal duties, PT-5 (FCRA disclosure and applicant notice) and SI-12(1) (remove SSNs from the reporting copy). The other 65 controls are in the Moderate baseline.

## 7. Authorization Boundary Description
The boundary was drawn from the intake [asset inventory](../step-00_P00_intake/asset-inventory.csv). It contains firm-managed components and the firm's configuration of vendor services:
- **Inside:** the ATS tenant configuration, roles, and I-9 module settings; the payroll platform users and settings; the identity provider tenant; the timekeeping app admin settings; the cloud tenant (4 workloads); the 4 office networks; 62 laptops, 8 kiosks, 4 scanners, and 34 smartphones.
- **Outside (external services, interconnected):** the ATS, payroll, and timekeeping vendors' platforms; the cloud provider's infrastructure; the background screening provider; E-Verify (DHS); the AI screening vendor; the payroll vendor's bank.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Background screening provider (SYS-07) | Bidirectional (ATS integration) | Candidate identifiers, SSN, authorization; consumer reports; adverse action letter triggers | Screening services agreement and FCRA end-user certification. **No security terms (gap)** |
| E-Verify (SYS-08) | Outbound case data, inbound results (manual entry on the DHS website) | Form I-9 data, photos for photo matching | E-Verify MOU |
| AI screening vendor (SYS-09) | Outbound resumes and applications; inbound scores | Candidate work history and application answers | Click-through marketplace terms. **No data use or security terms (gap)** |
| Payroll platform (SYS-02) via integration service | Outbound new hires and rates; inbound pay confirmations | SSN, bank, pay, time | Payroll services agreement with security and breach notice terms |
| Timekeeping app (SYS-06) via integration service | Inbound punches | Time and GPS location at clock-in | Subscription terms. **No retention or breach terms (gap)** |
| Client supervisors (client portal in SYS-01) | Bidirectional | Timesheets, associate names | Client master services agreements |
| Payroll vendor's bank | Outbound (within SYS-02) | ACH direct deposit and pay card funding | Payroll services agreement |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| ATS and onboarding tenant (with I-9 module and client portal) | SaaS | ATS vendor | Director of Recruiting (recruiting); HR and Compliance Manager (onboarding) |
| Payroll and billing tenant | SaaS | Payroll vendor | Payroll Manager |
| Identity provider tenant | SaaS | Identity vendor | IT Manager |
| Timekeeping app tenant | SaaS | Timekeeping vendor | Payroll Manager |
| Integration service | Cloud container service | Cloud tenant | IT Manager |
| Reporting database | Managed database | Cloud tenant | IT Manager |
| Document archive (scanned Forms I-9 2014-2022, exported consumer reports) | Object storage | Cloud tenant | HR and Compliance Manager |
| Backup vault | Cloud backup service | Cloud tenant (same account and region, **gap**) | IT Manager |
| Office firewalls (4), switches, Wi-Fi | Network | HQ and Branches 2-4 | IT Manager |
| Laptops (62), kiosks (8), scanners (4), smartphones (34) | Endpoint | All offices | IT Manager |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 70 controls:
- Implemented: 20
- Partially implemented: 40
- Planned: 10
- Not applicable: 0

### 10.2 Control assessment status
Assessed 2026-08-03 to 2026-08-07. See P07 `assessment-results.csv` and `poam.csv`.

### 10.3 Electronic Form I-9 system description
8 CFR 274a.2(e)(5) requires a complete description of each electronic generation or storage system and its indexing system, available on request. This SSP gives the system-level description: the ATS I-9 module (generation and storage since 2022, indexed by associate ID, name, and hire date) and the document archive (storage of scanned 2014-2022 forms, indexed by a spreadsheet of object names). The step-by-step business process documentation required by 274a.2(f)(1) (how forms are created, modified, and kept, and how audit trails establish integrity) is due 2026-12-31 (POAM-006).

## 11. Digital Identity Acceptance Statement
Internal staff authenticate through the identity provider with a password and number-matching push MFA. That is appropriate for the Moderate categorization. It is not phishing-resistant, so administrators move to hardware security keys in 2027 (P01 R-029). The payroll platform's SMS codes do **not** meet this standard and are being replaced (R-001).

Associates use the ATS self-service portal and the timekeeping app with vendor-managed sign-in and MFA. Their identity is proofed at hire through Form I-9 document examination and E-Verify (IA-12).

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), intake evidence, inventories and obligations register ([step-00](../step-00_P00_intake/intake-report.md)), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **APATP:** Associate Payroll and Applicant Tracking Platform
- **ATS:** applicant tracking system
- **CRA:** consumer reporting agency (the background screening provider)
- **EDR:** endpoint detection and response
- **FCRA:** Fair Credit Reporting Act
- **MFA:** multi-factor authentication
- **MOU:** memorandum of understanding (E-Verify)
- **POA&M:** plan of action and milestones

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan | IT Manager |
