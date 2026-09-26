# System Security Plan: Project Delivery and Payment Platform (PDPP)

**Organization:** Cris Santos Company, LLC (commercial and institutional building general contractor) | **Tier:** Small | **Vertical:** Construction
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Project Delivery and Payment Platform (**PDPP**), identifier CSC-SYS-001.

## 2. System Overview
The PDPP supports how the company wins, builds, bills, and pays for work:
- estimating and bid submission
- drawings, RFIs, submittals, and daily logs for 8 active jobsites
- monthly progress payment applications (pay apps) to owners
- payments to about 120 subcontractors and suppliers

It serves 60 employees and about 400 external subcontractor and design-team users.

The PDPP is also the company's **FCI boundary**. It is the set of systems that process, store, or transmit Federal Contract Information under FAR 52.204-21, and the proposed CMMC Level 1 assessment scope under 32 CFR 170.19(b).

**Major components:**
- **SYS-01:** a SaaS construction project management platform (system of record for projects)
- **SYS-02:** a SaaS construction ERP (job cost, billing, accounts payable, vendor master with bank details)
- **SYS-04:** an identity provider for single sign-on and MFA
- **SYS-05:** a SaaS productivity suite (email, files, chat). Email carries pay apps and payment correspondence
- **SYS-06:** a public-cloud tenant hosting the BIM/CAD file server, the estimating database, an internet-facing file-transfer portal, and the backup vault
- **SYS-07:** the main office and yard network
- **SYS-08:** endpoints (laptops, desktops, smartphones, jobsite tablets, commissioning laptops)

The cloud tenant is described by service category and is vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| N23-R01 | FAR 52.204-21 Basic Safeguarding of Covered Contractor Information Systems | 48 CFR 52.204-21 (NOV 2021). In FC-1, FC-2, FC-3 |
| N23-R02 | FAR 52.204-25 Section 889 prohibition | 48 CFR 52.204-25 (NOV 2021). In FC-1, FC-2, FC-3 |
| N23-R03 | DFARS 252.204-7012 | In FC-3. Not triggered: no covered defense information on the PDPP (P03 G-032) |
| N23-R04 | CMMC Program (32 CFR Part 170) and DFARS 252.204-7021 | Level 1 (Self) expected in the next DoD award (P03) |
| Payment terms | FAR 52.232-5, 52.232-27, 52.232-33 | Progress payments; paying subcontractors within 7 days of receipt; EFT to the SAM bank account |
| Payroll | FAR 52.222-8 | Weekly certified payrolls; records kept 3 years after completion |
| State | Florida Information Protection Act (breach notification) | Fla. Stat. 501.171 |
| Internal | Security policies POL-01 to POL-05 | P06 |

Not applicable:
- NIST SP 800-171 and CMMC Level 2: the company holds no CUI and has decided not to pursue CUI work before 2028 (P03 section 1).
- HIPAA and PCI DSS: no PHI is held for clients and no card payments are accepted.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the CFO on 2026-08-31.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- The CFO accepted continued operation of the PDPP on 2026-08-31, with the conditions in the P07 POA&M.
- The President approved treatment plans for the Very High and High risks in P01 and did not accept any of them as they stand.
- The President, as CMMC Affirming Official, will **not** affirm Level 1 compliance in SPRS until every FAR 52.204-21 requirement is Met (P03 G-021 to G-023).
### 4.3 System Operational Status
Operational. Major modifications planned:
- phishing-resistant MFA for payment roles (P01 R-001), due 2026-11-30
- network separation of the file-transfer portal (P03 G-013), due 2026-10-31

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | CFO | Overall accountability; risk acceptance up to Moderate |
| Risk acceptor (authorizing official equivalent) | President (majority owner) | Acceptance of High and Very High risks; CMMC Affirming Official (32 CFR 170.22) |
| Security lead | IT Manager | Day-to-day security; SSP and CMMC self-assessment |
| Payment controls owner | Accounting Manager | Vendor master, billing, bank portal |
| Contract compliance | Contracts Administrator | Flowdowns, SAM representations, SPRS entries, Section 889 reports |
| Operations support | Managed service provider | Help desk, patching, antivirus console, backup monitoring |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1, plus one company-defined type. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Facilities, fleet, and equipment management (drawings, submittals, daily logs; FCI) | Moderate | Moderate | Moderate | Federal facility details must stay non-public; wrong drawings cause rework; jobsites can run 24 hours on printed sets (P05 MTD 24 h) |
| Payments; collections and receivables (pay apps, vendor bank details) | Moderate | **High** | Moderate | A single altered bank record can divert more than $1 million (P01 R-001, R-002); billing tolerates a 72-hour outage (P05) |
| Compensation management (payroll, certified payrolls) | Moderate | Moderate | Moderate | Social Security numbers and bank data; weekly payroll and certified payroll deadlines |
| Client facility security details (company-defined type: installed security system layouts and credentials) | Moderate | Moderate | Low | Disclosure could help an intruder at a client site |
| **PDPP category (high-water mark)** | **Moderate** | **High** | **Moderate** | |

**Baseline.** The integrity of payment data rates High, so a strict FIPS 200 reading would point to the High baseline. For a 60-person contractor, the company applies the **NIST SP 800-53B Moderate baseline**, tailored, and adds targeted controls for payment integrity instead of the full High baseline:
- separation of duties (AC-5)
- replay-resistant MFA for payment roles (IA-2(8))
- call-back verification of bank changes (POL-01)

The CFO approved this tailoring decision on 2026-08-31.

The plan documents 70 controls: those that implement the 15 FAR 52.204-21 requirements, the Section 889 duties, and core hygiene (see `control-implementation.csv`). Every other Moderate-baseline control is treated in one of two ways:
- **Inherited** from the SaaS and cloud providers, as evidenced by their SOC 2 reports (P09).
- **Out of scope for this tier**, recorded as a tailoring decision where the control's purpose applies only to federal systems.

## 7. Authorization Boundary Description
The boundary contains company-managed components and the company's configuration of vendor services. It is drawn to match where FCI lives (32 CFR 170.19(b)(1)).
- **Inside:**
  - the SYS-01 and SYS-02 tenant configurations and roles
  - the identity provider tenant and the productivity suite tenant
  - the cloud tenant (4 workloads)
  - the main office and yard network, including jobsite cellular routers
  - 44 laptops, 12 desktops, 48 smartphones, 20 rugged tablets, and 2 commissioning laptops
- **Outside (external services, interconnected):**
  - the vendors' platforms and the cloud provider's infrastructure
  - the payroll system (SYS-03) and the bank portal (SYS-09)
  - the AI bid assistant (SYS-12)
  - federal portals (SYS-13)
- **Out of the FCI scope:**
  - equipment telematics (SYS-10) and jobsite technology services (SYS-11): no FCI
  - client-installed security and building systems: client-owned
  - personal email accounts and personal devices: prohibited for FCI by POL-04

**Known exceptions to fix before the Level 1 affirmation.** FCI currently leaks outside the boundary through personal email and the AI bid assistant (P03 G-003, G-024). The boundary is valid for CMMC purposes only after those leaks are closed.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Owners (private, state/local, federal) | Outbound pay apps; inbound payments | Pay apps, lien waivers, remittance details | Prime contracts. **No agreed out-of-band method for remittance changes (gap)** |
| Subcontractors and suppliers | Bidirectional via SYS-01 and email | Drawings (FCI), invoices, bank details | Subcontracts. **FAR 52.204-21 and 52.204-25 substance not flowed down (gap)** |
| Payroll SaaS (SYS-03) | Outbound hours; inbound certified payroll reports | PII, payroll | Vendor contract; SOC 2 on file |
| Bank portal (SYS-09) | Outbound ACH files from SYS-02 | Payment instructions | Treasury agreement. **Single approver on ACH (gap)** |
| AI bid assistant (SYS-12) | Outbound bid documents; inbound estimates | FCI (federal bids), pricing | **Standard terms allow model training (gap)** |
| Federal portals (SYS-13) | Bidirectional | SAM registration and EFT data, SPRS, invoices | Government terms |
| Design teams (via file-transfer portal) | Bidirectional | Models and drawings | Project agreements |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| Project management platform tenant | SaaS | Vendor | VP Operations |
| ERP and accounting tenant | SaaS | Vendor | Accounting Manager |
| Identity provider tenant | SaaS | Identity vendor | IT Manager |
| Productivity suite tenant | SaaS | Productivity vendor | IT Manager |
| BIM/CAD file server and GPU virtual desktops | Cloud virtual machines and block storage | Cloud tenant | IT Manager |
| Estimating database | Cloud virtual machine | Cloud tenant | Director of Preconstruction |
| File-transfer portal | Cloud virtual machine, internet-facing | Cloud tenant (**same subnet as internal servers, gap**) | IT Manager |
| Backup vault | Cloud backup service | Cloud tenant (**same account and region, gap**) | IT Manager |
| Main office firewall, switches, Wi-Fi | Network | Main office | IT Manager |
| Jobsite cellular routers (8) | Network | Jobsite trailers | IT Manager |
| Laptops (44), desktops (12), smartphones (48) | Endpoint (managed) | Office and field | IT Manager |
| Rugged tablets (20), commissioning laptops (2) | Endpoint (**not managed, gap**) | Jobsites; security systems group | Superintendents; Systems Integration Manager |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 70 controls:
- Implemented: 10
- Partially implemented: 41
- Planned: 19
- Not applicable: 0

By inheritance: 52 system-specific, 11 hybrid, and 7 common or inherited from providers.

**Crosswalk to FAR 52.204-21.** The `regulatory_driver` column names the FAR paragraph that each control supports, so the SSP doubles as the CMMC Level 1 implementation description. Examples: AC-2 supports (b)(1)(i); SC-7 supports (x) and (xi); SI-3 supports (xiii) to (xv).

### 10.2 Control assessment status
Assessed 2026-08-03 to 2026-08-07. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
All workforce users authenticate through the identity provider with a password and a push-notification second factor. Administrators use security keys.

Push MFA is **not** adequate for the payment roles, because an adversary-in-the-middle phishing page can relay the push approval and steal the session (P01 R-001). The company will require phishing-resistant authenticators (security keys or device-bound passkeys) for Project Managers, accounting staff, and executives by 2026-11-30.

External subcontractor users of SYS-01 authenticate with the vendor's own sign-in and optional MFA. That is governed by the vendor and outside this boundary. SYS-01 permissions limit each external user to their own project.

## 12. Referenced Artifacts
Scenario facts (`../scenario-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness and vendor review (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **ACH:** Automated Clearing House (electronic bank payments)
- **CMMC:** Cybersecurity Maturity Model Certification
- **EFT:** electronic funds transfer
- **FCI:** Federal Contract Information (FAR 52.204-21(a))
- **MSP:** managed service provider
- **Pay app:** monthly progress payment application
- **PDPP:** Project Delivery and Payment Platform
- **POA&M:** plan of action and milestones
- **SAM:** System for Award Management
- **SPRS:** Supplier Performance Risk System

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan; also serves as the CMMC Level 1 scope document | IT Manager |
