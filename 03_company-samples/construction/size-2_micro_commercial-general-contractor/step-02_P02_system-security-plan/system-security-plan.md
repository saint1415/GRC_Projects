# System Security Plan: Project and Payment System (PPS)

**Organization:** Cris Santos Company, LLC (commercial and institutional building general contractor) | **Tier:** Micro | **Vertical:** Construction
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Project and Payment System (**PPS**), identifier CSC-SYS-001.

## 2. System Overview
The PPS supports how the company wins, builds, bills, and pays for work:
- estimating and bid submission
- drawings, RFIs, submittals, daily logs, and photos for 4 active jobsites
- monthly progress payment applications (pay apps) to owners, about $92,000 a month
- payments to about 25 subcontractors and suppliers, about $55,000 a month
- payroll and weekly certified payrolls for the federal job

It serves 5 staff with system accounts and about 60 external subcontractor and design-team users of the project platform. The 2 Carpenters have no accounts.

The company owns almost no infrastructure. Most of the PPS is vendor SaaS, and a managed service provider (MSP) runs the laptops, the office network, and the backup. This plan therefore says, for each control, what the company does itself, what the MSP does for it, and what it inherits from a SaaS vendor.

The PPS is also the company's **FCI boundary**: the systems that process, store, or transmit Federal Contract Information under FAR 52.204-21, and the proposed CMMC Level 1 assessment scope under 32 CFR 170.19(b).

**Major components:**
- **SYS-01:** a SaaS construction project management and pay application platform (system of record for projects)
- **SYS-02:** a SaaS small-business accounting service with job costing (billing, accounts payable, vendor bank details)
- **SYS-03:** a SaaS payroll service with direct deposit
- **SYS-04:** a SaaS productivity suite (email, calendar, shared drive). Email carries pay apps and payment correspondence
- **SYS-05:** 4 laptops, 1 office desktop, 5 company smartphones, 2 jobsite tablets
- **SYS-06:** the office network: firewall and router, one Wi-Fi network, printer and plotter
- **SYS-07:** a cloud backup of email and files, run by the MSP

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| N23-R01 | FAR 52.204-21 Basic Safeguarding of Covered Contractor Information Systems | 48 CFR 52.204-21 (NOV 2021). In FC-1 |
| N23-R02 | FAR 52.204-25 Section 889 prohibition | 48 CFR 52.204-25 (NOV 2021). In FC-1 |
| N23-R04 | CMMC Program (32 CFR Part 170) and DFARS 252.204-7021 | Level 1 (Self) expected in the DoD solicitation due late 2026 (P03) |
| N23-R03 | DFARS 252.204-7012 | Not triggered: no DoD contract today and no covered defense information expected (P03 G-032) |
| Payment terms | FAR 52.232-27, 52.232-33 | Paying subcontractors within 7 days of receipt; EFT to the SAM bank account |
| Payroll | FAR 52.222-8 | Weekly certified payrolls; records kept 3 years after completion |
| State | Florida Information Protection Act (breach notification) | Fla. Stat. 501.171 |
| Internal | Security policies POL-02, POL-03, POL-04 | P06 |

Not applicable:
- NIST SP 800-171 and CMMC Level 2: the company holds no CUI and decided on 2026-08-31 not to bid work that needs it (P03 section 1).
- HIPAA and PCI DSS: the company holds no PHI for clients and accepts no card payments.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Owner and President on 2026-08-31.

### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- On 2026-08-31 the Owner accepted continued operation of the PPS, on the condition that the P07 POA&M items are completed by their dates.
- The Owner approved treatment plans for the Very High and High risks in P01 and did not accept any of them as they stand.
- The Owner, as CMMC Affirming Official, will **not** affirm Level 1 compliance in SPRS until every FAR 52.204-21 requirement is Met (P03 G-021 to G-023).

### 4.3 System Operational Status
Operational. Planned changes, all due by 2026-11-30:
- call-back verification and Owner approval of every bank change (P01 R-002), due 2026-09-30
- security keys for the payment roles (P01 R-001), due 2026-10-31
- device management for phones and tablets, and a separate guest Wi-Fi network (P03 G-001, G-012), due 2026-10-31

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner and risk acceptor | Owner and President | Overall accountability; approves this plan, policies, and spending; accepts Moderate risk; CMMC Affirming Official (32 CFR 170.22) |
| Security and compliance lead | Office Manager | Day-to-day security (part-time); maintains this plan, the risk register, the inventory, and the POA&M; MSP contact |
| Payment controls | Owner and President with the Office Manager | Office Manager prepares payments and bank changes; Owner verifies and releases |
| Project data and submittals | Project Manager and Estimator | SYS-01 users and permissions; submittal review, including Section 889 screening |
| Jobsite custodians | Superintendents | Tablets, storage containers, keys, and visitors |
| IT operations | MSP | Laptops, desktop, patching, antivirus, firewall and Wi-Fi, suite administration, backup |
| Independent assessor | Security consultant | Annual control assessment (P07) |

Because one part-time lead holds most security duties, the Owner reviews the POA&M with the Office Manager every month, and the annual assessment is done by someone outside the company.

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Facilities, fleet, and equipment management (drawings, submittals, daily logs; FCI) | Moderate | Moderate | Moderate | Federal and medical facility details must stay non-public; wrong drawings cause rework; jobsites can run a day on printed sets (P05 MTD 24 h) |
| Payments; collections and receivables (pay apps, vendor bank details) | Moderate | **High** | Moderate | One altered bank record can divert up to $78,000, close to a year of profit (P01 R-001, R-002); billing tolerates a 72-hour outage (P05) |
| Compensation management (payroll, certified payrolls) | Moderate | Moderate | Moderate | Social Security numbers and bank data; weekly payroll and certified payroll deadlines |
| **PPS category (high-water mark)** | **Moderate** | **High** | **Moderate** | |

**Baseline.** A strict FIPS 200 reading of the High integrity rating would point to the High baseline. For a 7-person contractor that is not workable. The company applies the **NIST SP 800-53B Moderate baseline**, tailored, and adds targeted payment-integrity controls instead:
- separation of duties for bank changes and payment release (AC-5)
- replay-resistant MFA for the three payment roles (IA-2(8))
- call-back verification of every bank change (POL-02 A.6)

The Owner approved this tailoring decision on 2026-08-31.

The plan documents 47 controls: those that implement the 15 FAR 52.204-21 requirements, the Section 889 duties, and the basic hygiene that the risk register depends on (see `control-implementation.csv`). Every other Moderate-baseline control is handled one of two ways:
- **Inherited** from the SaaS vendors (physical, platform, and application controls), with the SYS-01 vendor's SOC 2 report as the main evidence (P09).
- **Tailored out** for this tier, where the control addresses federal program management or organizations with in-house IT staff (for example, configuration change boards and separate development environments). These are recorded as tailoring decisions, not gaps.

## 7. Authorization Boundary Description
The boundary contains company-managed components and the company's configuration of vendor services. It is drawn to match where FCI lives (32 CFR 170.19(b)).
- **Inside:**
  - the SYS-01, SYS-02, and SYS-03 tenant configurations, users, and roles
  - the productivity suite tenant (SYS-04)
  - 4 laptops, 1 desktop, 5 phones, and 2 tablets (SYS-05)
  - the office network, printer, and plotter (SYS-06)
  - the backup subscription (SYS-07)
- **Outside (external services, interconnected):**
  - the vendors' platforms and data centers, and the MSP's remote management platform
  - the bank portal (SYS-08) and federal portals (SYS-10)
  - the AI estimating and bid assistant (SYS-09), a trial assessed separately in P10
- **Out of the FCI scope:**
  - the company website (vendor-hosted, public content only)
  - personal email accounts and personal devices: prohibited for FCI by POL-04

**Known exceptions to fix before the Level 1 affirmation.** FCI currently leaks outside the boundary through personal email and the AI tool (P03 G-003, G-024). The boundary is valid for CMMC purposes only after those leaks are closed.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Agreement |
|---|---|---|---|
| Owners (private, county, VA) | Outbound pay apps; inbound payments | Pay apps, lien waivers, remittance details | Prime contracts. **No agreed way to confirm remittance changes (gap)** |
| Subcontractors and suppliers | Bidirectional via SYS-01 and email | Drawings (FCI on FC-1), invoices, bank details, certified payrolls | Subcontracts. **FAR 52.204-21 and 52.204-25 substance not flowed down (gap)** |
| Bank portal (SYS-08) | Outbound ACH files from SYS-02 | Payment instructions | Treasury agreement; Owner releases every batch |
| AI estimating and bid assistant (SYS-09) | Outbound drawings; inbound quantities and prices | FCI (FC-1 change orders), owners' drawings, pricing | **Click-through terms allow model training (gap; P10)** |
| Federal portals (SYS-10) | Bidirectional | SAM registration and EFT data, invoices, certified payrolls | Government terms |
| MSP remote management platform | Inbound administrative access | Device management | MSP service contract. **No incident notice term (gap)** |

## 9. System Component Inventory
| Component | Type | Location or provider | Owner |
|---|---|---|---|
| Project management and pay application tenant (SYS-01) | SaaS | SYS-01 vendor | Project Manager and Estimator |
| Accounting tenant (SYS-02) | SaaS | Accounting vendor | Office Manager |
| Payroll account (SYS-03) | SaaS | Payroll service | Office Manager |
| Productivity suite tenant and shared drive (SYS-04) | SaaS | Productivity suite vendor | Office Manager (MSP administers) |
| Laptops (4) and office desktop (1) (SYS-05) | Endpoint, MSP-managed | Office and field | Office Manager |
| Smartphones (5) and jobsite tablets (2) (SYS-05) | Endpoint (**not managed, gap**) | Field | Superintendents; Project Manager |
| Firewall and router, Wi-Fi, printer and plotter (SYS-06) | Network and peripherals | Office (firewall in a locked closet) | Office Manager (MSP operates) |
| Backup subscription (SYS-07) | SaaS backup | Backup vendor (MSP subcontractor) | Office Manager (MSP operates) |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 47 controls:
- Implemented: 7
- Partially implemented: 28
- Planned: 12
- Not applicable: 0

By responsibility: 28 system-specific (the company), 16 hybrid (the company with a vendor or the MSP), and 3 common or inherited (fully provided by a SaaS vendor).

**Crosswalk to FAR 52.204-21.** The `regulatory_driver` column names the FAR paragraph that each control supports, so the SSP doubles as the CMMC Level 1 implementation description. Examples: AC-2 supports (b)(1)(i); AC-5 supports (b)(1)(ii); SC-7 supports (x) and (xi); SI-3 supports (xiii) to (xv). Controls that serve a business need rather than a FAR requirement (backup, training, contingency) say so.

### 10.2 Inherited and MSP-provided controls
| Provider | What the company relies on | Evidence | What the company must still do |
|---|---|---|---|
| SYS-01 vendor | Platform security, encryption (SC-8, SC-28), lockout (AC-7), backups (CP-9), audit records (AU-2) | SOC 2 Type 2 report reviewed 2026-08-24 (P09) | Complementary user entity controls: enforce MFA, add and remove users (including subcontractors), assign permissions, review activity, keep its own exports |
| Productivity suite vendor | Platform security, encryption, spam filtering (SI-8), lockout (AC-7), audit logging (AU-2) | Vendor documentation | Account management, MFA settings, forwarding rules, DMARC, log review |
| Accounting vendor and payroll service | Platform security and encryption | Vendor documentation only | User access, MFA, bank-change verification |
| MSP | Patching (SI-2), antivirus (SI-3), firewall and Wi-Fi (SC-7, AC-18), laptop encryption (SC-28), backup operation (CP-9), device lock (AC-11) | Monthly MSP reports; P07 evidence requests | Oversight: approve exceptions, read the monthly report, annual MSP security review (P01 R-014) |
| Backup service (MSP subcontractor) | Storage of email and file copies (CP-9) | None yet; restore test due 2026-09-30 | Confirm retention and administrator MFA through the MSP |

**Inherited does not mean done.** Two of the SYS-01 vendor's complementary user entity controls are open gaps at the company: MFA enforcement (IA-2(2)) and removal of users from closed projects (AC-2).

### 10.3 Control assessment status
Assessed 2026-08-17 to 2026-08-19 by an independent consultant. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
The 5 staff with accounts sign in to the productivity suite with a password and a push-notification second factor. The accounting service uses a text-message code.

Push MFA is **not** adequate for the payment roles. An adversary-in-the-middle phishing page can relay the push approval and steal the session (P01 R-001). The company will require phishing-resistant security keys for the Owner, Office Manager, and Project Manager by 2026-10-31, and will enforce MFA in SYS-01 for all company users by the same date.

External subcontractor users of SYS-01 sign in with the vendor's own sign-in and optional MFA. That is governed by the vendor and outside this boundary. SYS-01 permissions limit each external user to their own project.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness and vendor review (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **ACH:** Automated Clearing House (electronic bank payments)
- **CMMC:** Cybersecurity Maturity Model Certification
- **EFT:** electronic funds transfer
- **FCI:** Federal Contract Information (FAR 52.204-21(a))
- **MFA:** multi-factor authentication
- **MSP:** managed service provider
- **Pay app:** monthly progress payment application
- **POA&M:** plan of action and milestones
- **PPS:** Project and Payment System
- **SAM:** System for Award Management
- **SPRS:** Supplier Performance Risk System

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan; also serves as the CMMC Level 1 scope document | Office Manager (security and compliance lead) |
