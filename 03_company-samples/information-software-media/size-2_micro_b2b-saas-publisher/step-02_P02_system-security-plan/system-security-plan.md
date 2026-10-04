# System Security Plan: Vendor Compliance Platform (VCP)

**Organization:** Cris Santos Company, LLC (B2B SaaS software publisher) | **Tier:** Micro | **Vertical:** Information
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-15

## 1. System Name and Identifier
Vendor Compliance Platform (**VCP**), identifier CSC-VCP-001. The VCP is the multi-tenant SaaS production platform the company sells to customers.

## 2. System Overview
The VCP lets 45 mid-size property management companies and general contractors collect and track their subcontractors' and suppliers' compliance documents. Vendors upload certificates of insurance, W-9 tax forms, and licenses through upload links; the AI extraction feature fills in fields such as policy dates, coverage limits, and taxpayer identification numbers; customer reviewers confirm the result; and nightly jobs remind vendors before documents expire. About 900 customer users track about 41,000 vendors and about 165,000 documents.

The company has 7 employees and no dedicated security staff. The CTO runs the cloud account and is the part-time security and compliance lead. A managed service provider (MSP) runs the laptops and the productivity suite. This plan therefore says, for each control, what the company does itself, what the MSP does for it, and what it inherits from the cloud provider or a SaaS vendor.

**Major components:**
- **SYS-01:** the production environment in one public-cloud account and region: web application, API, and background workers on a managed container service; a managed relational database; an object storage bucket for uploaded documents; provider-managed encryption keys; and the internal admin console
- **SYS-02:** the SaaS source repository and CI/CD pipeline that build and deploy the VCP
- **SYS-03 (identity service):** the productivity suite's identity service, used for staff single sign-on to the repository, support desk, and CRM (MSP-administered)
- **SYS-05:** error tracking and log management (SaaS)
- **SYS-08:** the 7 company laptops used to administer the VCP (MSP-managed)

The cloud account is described by service category and is vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it affects the VCP |
|---|---|---|---|
| N51-R01 | FTC Act Section 5 | 15 U.S.C. 45(a); unfairness test 45(n) | Reasonable security for vendor data (including Social Security numbers on W-9s), and accuracy of the company's security, data-use, and AI accuracy statements. Gap analysis in P03 |
| N51-R03 | CCPA/CPRA and CPPA regulations | Cal. Civ. Code 1798.140(d) | Applicability check only: the company is not a CCPA "business" (P03 section 1.3) |
| N51-R04 | DOJ Data Security Program | 28 CFR Part 202 | Applicability check only: below the bulk thresholds and no covered data transactions (P03 section 1.4) |
| Contract | Customer MSA, DPA, and security exhibit | Contract | 72-hour incident notice, 30-day sub-processor notice, 60-day deletion, annual penetration test, 30-day backup retention, 99.5% uptime target |
| Assurance | SOC 2 Trust Services Criteria | AICPA 2017 TSC (2022 points of focus) | Type 1 readiness for Security and Confidentiality in P09 |
| State | Florida Information Protection Act (reasonable measures; third-party agent notice) | Fla. Stat. 501.171(2), (6) | Applies to the company as a third-party agent for customers. Notice duties in P08; other states handled generically |
| Internal | Security policies POL-02, POL-03, POL-04 | P06 | |

Not applicable (see `../00_company-facts.md` section 1): COPPA (N51-R02), PADFA (N51-R05, the company is not a data broker), FCC CPNI (N51-R06), FedRAMP (N51-R07), SEC disclosure (N51-R08), HIPAA, and PCI DSS.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Chief Executive Officer on 2026-09-15.

### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization. The equivalent internal decision: on 2026-09-15 the Chief Executive Officer accepted continued operation of the VCP on the condition that the Very High and High risks in P01 are treated by their dates (the CI key by 2026-10-15, the latest by 2026-11-30) and the POA&M items in P07 are worked on schedule.

### 4.3 System Operational Status
Operational. Major changes planned: replacing the static CI key with short-lived federated credentials (P01 R-001, due 2026-10-15), separate cloud roles for routine work (R-002), a separate backup account (R-007), and security logging and alerts (POAM-005), all by 2026-12-31.

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| Risk acceptor (authorizing official equivalent) | Founder and Chief Executive Officer | Approves this plan and the budget; accepts Moderate risk; approves treatment plans for High and Very High risk |
| System owner and security and compliance lead | CTO | Overall technical accountability; maintains this plan, the risk register, and the policies; accepts Low risk |
| Privacy lead | Operations and Finance Manager | DPAs, sub-processor list, offboarding checklist, training records |
| Technical operations (backup) | Senior Software Engineer | Backups, logging, deployments; backup technical lead for incidents |
| Customer access to tenants | Customer Success Manager | Uses the admin console for support; customer communications |
| Endpoint and suite operations | MSP | Laptops, productivity suite, help desk |
| Independent assessor | Security consultant | Control assessment (P07) |

**Where roles overlap and how that is compensated.** The CTO designs, operates, and self-assesses most controls and also did the risk and gap analysis. Three checks offset that: the Chief Executive Officer approves every risk decision and public statement, the independent consultant tested 14 controls in P07, and the cloud provider's SOC 2 report covers the inherited layer. A SOC 2 auditor will add a fourth check in 2027.

## 6. System Information Types and System Categorization
Information types were chosen with reference to NIST SP 800-60 Vol. 2 Rev. 1 (closest matching types). Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Customer vendor records and documents (contacts, W-9s with taxpayer identification numbers, certificates, licenses) | Moderate | Moderate | Low | Social Security numbers for about 9,800 individuals make disclosure harmful (identity theft) and trigger breach notice duties. Not High: no financial account, health, or bulk data. A wrong status could let an uninsured vendor on site. Customers can work from exports for a day (P05 MTD 24 h) |
| Compliance status and audit reports | Low | Moderate | Moderate | Customers rely on status before site work; the uptime target makes availability Moderate |
| System development and operations (source code, secrets, configuration) | Moderate | Moderate | Low | Secrets such as the CI key give access to all customer data (R-001) |
| **VCP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 7-person SaaS company. `control-implementation.csv` documents 47 controls: 45 Moderate-baseline controls that matter most for a multi-tenant SaaS platform and SOC 2 Security and Confidentiality, plus 2 selected by tailoring (CA-8 because the security exhibit promises penetration testing, and SA-3(2) because engineers use production data outside production). All other Moderate-baseline controls are handled one of two ways:
- **Inherited** from the cloud provider and SaaS vendors (physical and environmental controls, maintenance, and their platform controls), with the cloud provider's SOC 2 report as the main evidence (P09 V-01).
- **Not selected at this tier**, recorded as a tailoring decision, where the control serves federal program management or organizations with dedicated security staff (for example, separate configuration control boards).

## 7. Authorization Boundary Description
- **Inside:** the production cloud account and everything in it (SYS-01), the repository and CI/CD configuration (SYS-02), the suite identity service as it controls staff access (SYS-03), the error tracking and log management configuration (SYS-05), and the 7 company laptops used to administer the VCP (SYS-08).
- **Outside but in scope as a gap:** the contract developer's personal laptop. It holds a copy of the CI key and database extracts, but the company does not manage it (PS-7, SA-3(2)). It must be brought under control or stop holding company data (POAM-011, POAM-014).
- **Outside (external services, interconnected):** the cloud provider's infrastructure, the email delivery service (SYS-04), the AI model provider (SYS-06), the support desk and other business SaaS (SYS-07), and the MSP's remote management platform.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Agreement |
|---|---|---|---|
| Customer users (web) | Bidirectional | Vendor records, documents, statuses, reports | MSA and DPA |
| Vendors (upload links) | Inbound | Certificates, W-9s, licenses | Customer instructions under the DPA; upload page terms |
| Customer single sign-on (3 customers) | Inbound | Authentication assertions | MSA (customer configuration) |
| Email delivery service (SYS-04) | Outbound | Vendor contact names, emails, document names, upload links | DPA (sub-processor) |
| AI model provider (SYS-06) | Outbound document text and images; inbound extracted fields and summaries | Full document content, including Social Security numbers on W-9s | **Click-through API terms only; not on the sub-processor list (gap; P10)** |
| Error tracking and log management (SYS-05) | Outbound | Error payloads, sometimes with extracted W-9 text | DPA (sub-processor) |
| Support desk SaaS (SYS-07) | Bidirectional | Tickets and screenshots from customers | DPA (sub-processor) |
| Contract developer's personal laptop | Outbound (copies) | Database extracts; the CI key | Contractor agreement (confidentiality only; **gap**) |

## 9. System Component Inventory
| Component | Type | Location or provider | Owner |
|---|---|---|---|
| Web application, API, workers, admin console | Containers on a managed container service | Production cloud account | CTO |
| Load balancer and network rules | Managed network service | Production cloud account | Senior Software Engineer |
| Relational database (multi-tenant) | Managed database service | Production cloud account | Senior Software Engineer |
| Document bucket (about 165,000 files) | Object storage | Production cloud account | Senior Software Engineer |
| Snapshots and point-in-time recovery | Backup feature of the database service | Production cloud account (same account, **gap**) | Senior Software Engineer |
| Encryption keys and TLS certificates | Managed key and certificate services | Production cloud account | Senior Software Engineer |
| Repository and CI/CD pipeline | SaaS | Source hosting vendor | CTO |
| Suite identity service | SaaS | Productivity suite vendor | Operations and Finance Manager (MSP operates) |
| Error tracking and log management | SaaS | Observability vendor | Senior Software Engineer |
| Uptime monitor and status page | SaaS | Monitoring vendor | CTO |
| Company laptops (7) | Endpoint | Staff homes and office | Operations and Finance Manager (MSP operates) |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 47 controls:
- Implemented: 10
- Partially implemented: 27
- Planned: 10
- Not applicable: 0

By responsibility: 22 system-specific (the company), 23 hybrid (the company with the cloud provider, a SaaS vendor, or the MSP), 2 common/inherited (fully provided by the cloud provider: PE-3 and SC-12).

### 10.2 Inherited and MSP-provided controls
| Provider | What the company relies on | Evidence | What the company must still do |
|---|---|---|---|
| Cloud provider | Data center security (PE-3), key management (SC-12), storage encryption (SC-28), backup features (CP-9), management event logging (AU-2), network services (SC-7) | SOC 2 Type 2 report reviewed 2026-09-02 (P09 V-01) | Complementary user entity controls: protect access keys and administrator accounts, configure logging, backups, and network rules, manage its own users (AC-2, AC-6, IA-5, AU-2, CP-9) |
| Productivity suite vendor (through the MSP) | Staff sign-in, MFA, lockout (IA-2, IA-2(1), AC-7) | Vendor documentation; MSP configuration report | Tell the MSP about joiners and leavers on time; review the MSP's administrator accounts |
| MSP | Laptop encryption, antivirus, patching, screen lock, wiping (SC-28, SI-3, SI-2, AC-11, MP-6) | Monthly MSP report; P07 evidence requests | Oversight: review reports monthly; add security terms to the contract (PS-7) |
| Error tracking and log management SaaS | Log storage and access control (AU-11) | Vendor documentation; assurance report reviewed in P09 (V-03) | Stop sending tax IDs in error payloads (R-005) |
| Repository host | Branch protection, dependency alerts (CM-3, RA-5) | Vendor documentation | Enforce protection for administrators; act on alerts |

**Inherited does not mean done.** The cloud provider's controls protect customer data only if the company runs its side. Today the company's own gaps (the static administrator key, five full administrators, no data-level logging, backups in the same account) are exactly the controls the provider's report says the customer must operate.

### 10.3 Control assessment status
Assessed 2026-08-24 to 2026-08-26 by an independent security consultant (14 controls). See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
Staff sign in to the suite with a password and an authenticator app; the suite's single sign-on then grants the repository, support desk, and CRM. Cloud console accounts use a password and an authenticator app. This fits the Moderate categorization, with three exceptions being fixed: the admin console accepts a password only (POAM-003), the cloud root account depends on one person's phone and a shared vault entry (R-025), and the CI pipeline uses a static key that no person signs in with (R-001, POAM-004). Phishing-resistant hardware keys for the CTO, both engineers, and the root account are planned with POAM-003.

Customer users sign in with platform accounts (MFA optional) or their own single sign-on (3 customers). Customer administrators can see every vendor's W-9 in their tenant, so MFA will be required for customer administrators from 2026-12-31 (R-014).

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness and vendor reviews (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **CI/CD:** continuous integration and continuous delivery
- **DPA:** data processing agreement
- **MFA:** multi-factor authentication
- **MSA:** master subscription agreement
- **MSP:** managed service provider
- **POA&M:** plan of action and milestones
- **Sub-processor:** a vendor that processes customer data on the company's behalf
- **TIN:** taxpayer identification number (a Social Security number or an employer identification number)
- **VCP:** Vendor Compliance Platform

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-09-15 | Initial plan | CTO (security and compliance lead) |
