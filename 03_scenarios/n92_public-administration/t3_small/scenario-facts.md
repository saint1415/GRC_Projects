# Scenario facts: Cris Santos Company | Public Administration | Small

All 10 deliverables in this folder use the facts below. The company is fictitious, and so are its agency customers. Where a fact comes from a regulation, policy, or standard, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (a privately held GovTech systems integrator; not a government entity) |
| Business | GovTech systems integrator (NAICS 541512, Computer Systems Design Services). It builds, hosts, and supports a configurable case management platform for state and local agencies (about 70% of receipts) and sells implementation, data migration, and integration services (about 30%) |
| Location | Florida. One **headquarters office** (engineering, operations, corporate staff) and remote staff who work from home in Florida, Georgia, and Alabama. All work, including all support and administration of agency data, is performed in the United States |
| Workforce | 60 employees: 5 executives and directors, 20 software engineers and quality analysts, 5 cloud operations engineers (including the Cloud Operations Lead), 15 implementation consultants, business analysts, and trainers, 7 customer support staff, and 8 corporate staff (IT, contracts and compliance, HR, finance, business development) |
| Revenue | $20.4 million a year (fictional), about $78,000 per business day. Under the SBA standard of $34.0 million for NAICS 541512 (13 CFR 121.201), so SBA-small |
| Customers | 11 agency customers, all in Florida (see the customer table below). About 455,000 individuals have records in the platform |
| Regulatory status | The company is a **private contractor**. The federal data-owner rules below bind the agencies directly and reach the company **through its contracts**: IRS Publication 1075 through Exhibit 7 contract language, the FBI CJIS Security Policy through the CJIS Security Addendum (28 CFR 20.33(a)(7)), and Florida Rule 60GG-2, F.A.C. through the security terms state agencies must put in IT contracts (Fla. Stat. 282.318(4)(h); Rule 60GG-2.001(3)(b)). Every agency contract requires the NIST SP 800-53 Rev. 5 Moderate baseline for the hosted platform |
| Florida data security duty | The company is a "third-party agent" of its agency customers under Fla. Stat. 501.171(1)(h): it must take reasonable measures to protect personal information (501.171(2)) and must notify the agency of a breach no later than 10 days after determining it (501.171(6)(a)) |
| Not in scope | HIPAA: no customer has designated the company a business associate. The human services customer (AC-03) confirmed in writing that its eligibility case functions sit outside its HIPAA health care component under its hybrid-entity designation (45 CFR 164.105). Driver's Privacy Protection Act: no motor vehicle agency customers. Election systems: none. Federal contracts (FAR 52.204-21, FAR 52.204-25): none. SLCGP: no grant funds pay for the platform. CIRCIA: proposed rule only |
| State law approach | Florida law is cited where a Florida duty is unavoidable (Rule 60GG-2 and Fla. Stat. 282.318 for state agency contracts, Fla. Stat. 282.3185 and 282.3186 for local government customers, and Fla. Stat. 501.171). Individuals whose records are affected may live in other states; those are handled generically ("each state where affected individuals reside") |

**Agency customers (fictional)**

| ID | Customer | Use of the platform | Regulated data | How requirements reach the company |
|---|---|---|---|---|
| AC-01 | A state revenue agency (Florida state agency) | Tax compliance casework: audit follow-up, collections cases, taxpayer correspondence. In production since 2024 | **Federal tax information (FTI)** received by the agency from the IRS under IRC 6103(d), plus state tax data. About 210,000 taxpayer case records | Contract with Pub. 1075 Exhibit 7 language; the agency's 2024 IRS 45-day notification names the company and its cloud provider (Pub. 1075 Exhibit 6; 26 CFR 301.6103(n)-1); SP 800-53 Moderate; Rule 60GG-2 contract terms |
| AC-02 | A county sheriff's office (pretrial services and probation units) | Supervision case management. Criminal history summaries are imported through the sheriff's interface. In production since 2023 | **Criminal justice information (CJI)**, including criminal history record information (CHRI). About 31,000 supervision case records | Contract with the CJIS Security Addendum (28 CFR 20.33(a)(7)); CJIS Security Policy v6.1 (06/25/2026); SP 800-53 Moderate |
| AC-03 | A state human services agency (Florida state agency) | Pilot since January 2026 in 2 regions: application intake and verification task workflow for SNAP, TANF, and Medicaid, plus the AI eligibility assistant pilot (SYS-11) | Applicant and household data, Social Security numbers, income documents. About 64,000 applicant households. **FTI is prohibited** in this tenant (see below) | Contract confidentiality terms reflecting 7 CFR 272.1(c) (SNAP) and 42 CFR 431.300-431.307 (Medicaid); SP 800-53 Moderate; Rule 60GG-2 contract terms |
| AC-04 to AC-11 | 8 Florida counties and cities | Code enforcement, constituent requests, permit complaints | Names, addresses, phone numbers, some driver license numbers in complaint files. About 150,000 constituent records | Contract security terms (SP 800-53 Moderate by reference) |

**Why FTI is prohibited in the AC-03 tenant.** Human services agencies that receive FTI under IRC 6103(l)(7) "may not contract for services that involve the disclosure of FTI to contractors or sub-contractors" (Pub. 1075 section 2.C.11.2; Exhibit 6). The AC-03 contract therefore forbids FTI in the platform. The agency keeps IRS income match results in its own eligibility system.

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Chief Executive Officer (majority owner, Cris Santos) | Accepts High and Very High risks; signs security attestations to agencies; approves budget |
| Chief Operating Officer | Executive owner of the security program and **system owner** of the platform; approves policies; accepts Moderate risks |
| IT Manager (Information Security Officer) | Runs the security program part time alongside corporate IT; the security point of contact named in agency contracts; maintains the risk register and SSP |
| Contracts and Compliance Manager | Privacy and contract compliance lead. Tracks every agency security term (Exhibit 7, CJIS Security Addendum, Rule 60GG-2 terms); owns breach notices to agencies |
| Director of Engineering | Owns the platform code, the software development life cycle, and change management |
| Cloud Operations Lead | Operates the production cloud tenant: infrastructure, backups, logging, patching, on-call rotation |
| Customer Support Manager | Tier 2 support; the support team has read access to customer tenants for troubleshooting |
| Director of Customer Delivery | Implementations, data migrations, and agency user training |
| HR Manager | Screening, onboarding, and terminations; coordinates fingerprint-based checks through agency customers |
| Data and AI Lead | Owns the AI eligibility assistant feature (P10) |
| Agency security contacts (customer roles) | AC-01 disclosure officer; AC-02 local agency security officer; AC-03 information security manager |

## 3. Systems

| ID | System | Hosting | Holds agency data? | Notes |
|---|---|---|---|---|
| SYS-01 | Agency Case Management Platform (ACMP), production | Company cloud tenant (IaaS/PaaS) | Yes (FTI, CJI, benefits applicant data, constituent data) | Multi-tenant web application on a managed container service, a managed relational database, object storage for documents, and a message queue. AC-01 runs in a dedicated database instance with a customer-managed encryption key; other tenants share a database cluster with row-level tenant separation |
| SYS-02 | Integration gateway | Company cloud tenant | Yes (in transit) | Secure file transfer from AC-01's tax system, an API link to AC-02's message switch, and an API link to AC-03's eligibility system |
| SYS-03 | Workforce identity provider (single sign-on and MFA) | SaaS | No (identities only) | Protects the cloud console, the platform's admin functions, SYS-05, SYS-06, and SYS-07 |
| SYS-04 | Agency user sign-in | Part of SYS-01 | No (identities only) | AC-01, AC-02, and AC-03 federate with their own identity providers (agency-enforced MFA). Municipal customers use platform-local accounts |
| SYS-05 | Productivity suite (email, files, chat) | SaaS | Incidental | Staff sometimes receive agency data in email during implementations |
| SYS-06 | Source code repository and CI/CD pipeline | SaaS | No (code and secrets) | Builds and deploys SYS-01 and SYS-02 through infrastructure as code |
| SYS-07 | Support ticketing system | SaaS | Yes (in attachments) | Agency users attach screenshots to tickets. Not an IRS-approved subcontractor (see gaps) |
| SYS-08 | Endpoints | Company-managed | Cached | 64 laptops with full-disk encryption, endpoint detection and response (EDR), and mobile device management |
| SYS-09 | Headquarters office network | On-premises | No (in transit only) | Firewall and Wi-Fi. No production systems on-premises |
| SYS-10 | Non-production environments (development, test, staging) | Company cloud tenant, separate accounts | Should hold synthetic data only | A staging copy of AC-01 data was made in 2025 (see gaps) |
| SYS-11 | AI eligibility assistant (pilot feature of SYS-01) | Company cloud tenant plus the cloud provider's managed large language model service | Yes (AC-03 applicant data) | Pilot since May 2026 for 40 AC-03 caseworkers in one region (see P10) |
| SYS-12 | Backups | Company cloud tenant | Yes | Point-in-time database recovery (5-minute granularity) and daily snapshots kept 35 days, in the same account and region as production |
| SYS-13 | Logging and monitoring | Company cloud tenant | Yes (log content) | Cloud audit logs, application audit logs, and performance alerts. Kept 90 days |

The cloud provider is described by service category only (vendor-agnostic). The services the company uses are FedRAMP Moderate authorized and run in U.S. regions (checked on the FedRAMP Marketplace in June 2026), as Pub. 1075 section 3.3.1 requires for FTI.

**SSP system (P02):** the *Agency Case Management Platform (ACMP)*: SYS-01, SYS-02, SYS-04, SYS-10, SYS-11, SYS-12, and SYS-13, with the supporting services that administer them (SYS-03, SYS-06, and the administrator endpoints in SYS-08).

## 4. Current security posture: partially compliant

**In place today:**
- Single sign-on with MFA (authenticator app with number matching) for all workforce accounts; hardware security keys for the 5 cloud administrators
- Federated sign-in with agency-enforced MFA for AC-01, AC-02, and AC-03 users
- Company-managed laptops with full-disk encryption, EDR, and mobile device management
- Encryption in transit (TLS 1.2 or higher) and at rest (provider-managed AES-256); a dedicated database instance and customer-managed key for the AC-01 FTI tenant
- Infrastructure as code; pull requests need two approvals; static code analysis and dependency scanning run in the pipeline
- FedRAMP Moderate authorized cloud services in U.S. regions only
- Point-in-time database recovery and daily snapshots (SYS-12)
- Annual security awareness training for all staff through an online learning system
- Commercial background checks at hire for all staff; FBI fingerprint-based checks, arranged through agency customers, for 9 staff
- CJIS Security Addendum certification pages signed by 9 staff and held by AC-02
- An external application penetration test in October 2025
- A written incident response plan (2024) and an on-call rotation for production outages
- A cyber insurance policy with a breach hotline and panel vendors

**Missing or weak, found in the 2026 assessments:**
1. No risk assessment of the platform since its 2023 launch, and the only "SSP" is a 2023 proposal document that was never maintained.
2. Staff access to regulated data runs ahead of screening: 13 staff can reach CJI but only 9 have fingerprint-based checks and signed CJIS Security Addendum certifications; 11 staff can reach FTI but only 9 have Pub. 1075 background investigations, and 3 are overdue for annual FTI disclosure awareness recertification. The 4 unscreened staff include the 2 cloud engineers hired in 2026, who hold standing administrator access to every tenant.
3. Logs are kept 90 days, with no central review and no after-hours alerting. CJIS requires at least 1 year (AU-11) and Pub. 1075 requires 7 years for FTI systems (AU-11).
4. Backups share the production account and region, are not immutable, and have never been restore-tested end to end. The 8-hour recovery time in agency contracts is unproven.
5. The 2024 incident response plan has never been tested and lacks the customer clocks: 1 hour for suspected CJI incidents (CJIS IR-6), the revenue agency's 24-hour reporting to TIGTA and the IRS Office of Safeguards (Pub. 1075 section 1.8), 12-hour ransomware reporting by Florida agencies (Fla. Stat. 282.318, 282.3185), and 10 days under Fla. Stat. 501.171(6).
6. TLS termination at the container ingress and the integration gateway uses cryptographic libraries not running in a FIPS-validated mode, and there is no inventory of cryptographic modules. CJIS requires FIPS 140-3 certified modules for CJI in transit and will not accept FIPS 140-2 certificates after 2026-09-21 (SC-13).
7. Four municipal tenants allow platform-local agency accounts without MFA.
8. In 2025 an unmasked copy of AC-01 production data (with FTI) was loaded into staging to troubleshoot a defect. No IRS Data Testing Request was made (Pub. 1075 section 2.E.6.4), and 14 engineers had access. The copy was deleted in March 2026, with no deletion record.
9. No authenticated vulnerability scanning of running containers and hosts; 2 medium findings from the 2025 penetration test are still open.
10. Emergency production changes are sometimes made directly in the cloud console without a ticket (3 in the last 6 months).
11. Data of a municipal customer whose contract ended in 2025 has not been deleted, and there is no process to certify deletion at contract end.
12. Agency users attach screenshots with FTI and CJI to support tickets (SYS-07). The ticketing vendor is not an IRS-approved subcontractor (Pub. 1075 Exhibit 7, I(8)) and has no CJIS Security Addendum.
13. Vendor reviews cover only the cloud provider. The managed large language model service (added May 2026) and the ticketing vendor were never reviewed, and the FedRAMP status of the model service was not checked.
14. The AI eligibility assistant pilot started without an AI risk assessment, bias testing, a documented human-review rule, or notice to applicants (see P10).
15. The API key for the AC-02 message-switch interface is stored in plain text in a CI/CD pipeline variable visible to all 20 engineers (found during P07 testing).

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 regulation | NIST SP 800-53 Rev. 5 (Release 5.2.0) Moderate baseline, required by every agency contract, with the CJIS Security Policy v6.1 and IRS Pub. 1075 (Rev. 11-2021) contractor requirements as the secondary overlays |
| P08 incident | Ransomware in the production cloud tenant that encrypts platform databases holding CJI (AC-02) and FTI (AC-01), with data theft, starting from a stolen cloud engineer session token |
| P09 SOC 2 | The company **is** a service organization: agencies rely on its controls over their data. AC-01's 2027 contract renewal requires an independent SOC 2 Type 2 report or an equivalent. Two prospective out-of-state agencies ask for GovRAMP verification. Readiness self-assessment against Security, Availability, and Confidentiality |
| P10 AI | The AI eligibility assistant (SYS-11) that recommends SNAP, TANF, and Medicaid eligibility outcomes to AC-03 caseworkers |
| Cloud | Vendor-agnostic. Services are described by category, with AWS, Azure, and Google Cloud equivalents noted only where needed for shared responsibility |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-07-13 to 2026-07-24 | Risk assessment and gap analysis fieldwork |
| 2026-08-03 to 2026-08-07 | Control assessment fieldwork |
| 2026-08-31 | Deliverables approved by the Chief Operating Officer (and by the CEO for High risks) |
