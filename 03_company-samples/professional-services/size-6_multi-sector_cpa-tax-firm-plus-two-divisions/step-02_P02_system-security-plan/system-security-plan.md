# System Security Plan: Tax Preparation and Client Portal Platform (TPCP)

**Organization:** Cris Santos Company Holdings, Inc. (Tax and Advisory, the focus business of the CPA and Tax Services division) | **Tier:** Multi-Sector | **Vertical:** Professional, Scientific, and Technical Services
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-10

> **Why this system.** At this tier the SSP can cover one system per division or a shared corporate system. The group chose the focus division's primary system, the **TPCP**, because it holds tax return information for about 9 million people a year, it is where the three divisions meet (its client portal is a tenant of the group's own Practice Cloud product, and its referral interface feeds the Wealth CRM), and it carries two of the group's High risks (P01 GR-01 and GR-02). It inherits most controls from corporate (SYS-G1 to SYS-G4). Wealth (SYS-W1) and Practice Cloud (SYS-S1) keep their own plans, which inherit from the same common control catalog. Practice Cloud's plan is the basis of its SOC 2 system description.

## 1. System Name and Identifier
Tax Preparation and Client Portal Platform (**TPCP**), identifier CSCH-TAX-TPCP. It covers SYS-T1 and the Tax and Advisory tenant of SYS-S1 in `../00_company-facts.md`.

## 2. System Overview
The TPCP is how Tax and Advisory prepares and files about 5.6 million individual returns and 380,000 business, trust, and exempt organization returns a year. It supports:
- **Preparation and review:** preparers in about 1,150 tax offices enter or extract source data, prepare returns in the tax engine, and send them to reviewers.
- **Client document exchange and signature:** clients upload documents, sign Forms 8879 and engagement letters, and receive returns through the Tax and Advisory tenant of Practice Cloud.
- **Electronic filing:** approved and signed returns are released through the e-file gateway to the tax engine vendor's transmitter, an Authorized IRS e-file Provider. Tax and Advisory acts as the ERO.
- **Integrated planning referrals:** for clients who consent, the referral interface sends selected tax return information to the Wealth CRM.

About 27,000 permanent and 11,000 seasonal workforce users and 41 service accounts use it in season.

**Major components** (vendor-agnostic; see P04):
- **Tax engine:** a licensed professional tax calculation and forms engine, deployed as containers in the Tax division's provider A accounts
- **Preparer workflow and review tools:** in-house web application (queues, review checklists, office assignment)
- **Return data store:** managed relational database and object storage for returns and scanned documents
- **AI document extraction service:** in-house service that calls a hosted model from a third-party model provider (AI-001, P10)
- **E-file gateway:** service that sends signed returns to the transmitter and receives acknowledgments
- **Referral interface:** batch API from SYS-T1 to the SYS-W1 integration hub
- **Client portal tenant:** Tax and Advisory's tenant of SYS-S1 Practice Cloud (provider B), operated by the Practice Cloud division as an internal service provider
- **Office endpoints:** managed workstations and scanners in tax offices

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies to the TPCP |
|---|---|---|---|
| N54-R01 | FTC Safeguards Rule | 16 CFR Part 314 | Tax and Advisory is a financial institution (314.2(h)(2)(viii)); the TPCP holds most of its customer information. The full rule applies; 314.6 does not (P03) |
| N54-R02 | IRC 7216 | 26 U.S.C. 7216; 26 CFR 301.7216-1 to -3 | Every disclosure or use of tax return information must fit a permission in 301.7216-2 or a written consent under 301.7216-3. Governs the referral interface, the AI service, and contractors |
| N54-R03 | IRS e-file and WISP guidance | IRS Pubs. 1345, 4557, 5708 | ERO duties: next-business-day security incident report (Pub. 1345), Form 8879 signature and retention rules |
| N52-R05 | SEC Regulation S-P | 17 CFR 248.30 | Integrated planning data that Wealth sends to Tax and Advisory is handled on Wealth's behalf; Tax and Advisory is Wealth's service provider for it (248.30(a)(5), (d)(10)) |
| N52-R08 / N51-R08 | SEC cybersecurity disclosure | Reg S-K Item 106; Form 8-K Item 1.05 | A TPCP incident may be material to the group (P08) |
| State law | Breach notification and data security | Each state where affected individuals reside (Florida worked example: Fla. Stat. 501.171) | Notices and reasonable security duties (P08) |
| Professional | Circular 230 due diligence | 31 CFR 10.22 | Practitioners remain responsible for returns prepared with AI assistance (P10) |
| Internal | Group policies POL-01 to POL-05 and the Tax division supplement | P06 | |

Not applicable: HIPAA (the TPCP holds no PHI; CPA Partners' business associate work runs on SYS-T3), FAR and DFARS (no federal contracts).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Group CISO (Qualified Individual) and the Tax division technology director (system owner) on 2026-09-10, after the board risk committee review.

### 4.2 System Authorization Decision
The group is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- **Decision:** authorized to operate with conditions, 2026-09-10, by the Group CISO and the Tax division president (the senior member who oversees the Qualified Individual under 314.4(a)(2)), with the Group Chief Risk Officer concurring for the High risks.
- **Conditions:** (1) the referral interface must check for a recorded, compliant IRC 7216 consent before every transfer by 2026-12-31 (POAM-009); (2) legacy authentication on office intake mailboxes must be blocked before the 2027 filing season, by 2027-01-04 (POAM-002); (3) no seasonal account may be activated before training and the background check are complete for the 2027 season (POAM-001, POAM-003).
- **Reauthorization:** annually before the filing season, or after a major change.

### 4.3 System Operational Status
Operational. **Major modifications planned:** consent enforcement in the referral interface (2026-12-31), and AI accuracy monitoring for the extraction service before the 2027 season (POAM-011).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Tax division technology director | Accountable for the TPCP and this SSP |
| Authorizing official equivalent | Group CISO (Qualified Individual) with the Tax division president | Authorization decision |
| Business owner | Chief Tax Officer | Tax practice, e-file program (Responsible Official), IRC 7216 consent process |
| Privacy oversight | Group Chief Privacy Officer | Purpose register; consent design; referral data fields |
| Common control providers | Group identity director (SYS-G1), Group SOC director (SYS-G2), Group cloud platform director and Group network director (SYS-G3), Group collaboration services director (SYS-G4) | Operate inherited controls (`common-control-catalog.csv`) |
| Internal service provider | Practice Cloud CISO | Operates the portal tenant's platform controls |
| Independent assessor | Group internal audit | Assesses common controls once and samples division controls (P07) |

## 6. System Information Types and System Categorization
Information types were chosen with NIST SP 800-60 Vol. 2 Rev. 1 as a guide; impact levels were set by the group under FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Taxpayer tax return information (about 9 million people a year; 24 million in retention) | **High** | **High** | Moderate | Disclosure at this scale would be severe (FTC and state notices, identity theft and refund fraud, SEC materiality). Integrity is High because a changed refund account or amount causes direct financial loss. Availability is Moderate: extensions are a workaround (P05) |
| Client authentication and e-signature records (Form 8879) | Moderate | **High** | Moderate | The ERO may not transmit without a valid signature; records prove authorization |
| Integrated planning data (referral interface; Wealth data held for Wealth) | **High** | Moderate | Low | Combines tax and account data for 210,000 households |
| Security information (keys, logs, interface credentials) | High | High | Moderate | Compromise would expose every component |
| **TPCP category (high-water mark)** | **High** | **High** | **Moderate** | Overall **High** |

**Baseline:** the NIST SP 800-53B **High** baseline, tailored. The plan documents **145 controls** in `control-implementation.csv`:
- 136 from the High baseline;
- 7 from the privacy baseline (PM-9, PM-10, PM-14, PT-2, PT-3, PT-4, PT-5), added because IRC 7216 consent and permitted purpose are the platform's main privacy duties;
- 2 program management controls not in any baseline (PM-1, PM-2), because they carry the written program and the Qualified Individual.

Other High-baseline controls are either fully inherited from the cloud providers (for example, most PE controls, evidenced by their SOC 2 Type 2 reports) or tailored out with a reason in the group tailoring register (for example, PE controls for facilities the group does not operate).

## 7. Authorization Boundary Description
- **Inside:** SYS-T1 in the Tax division's provider A accounts (tax engine, workflow and review tools, return data store, AI extraction service, e-file gateway, referral interface), Tax and Advisory's tenant configuration and data in SYS-S1, and office endpoints and scanners.
- **Outside, inherited (common control providers):** SYS-G1 identity, SYS-G2 SOC, SIEM, EDR, and email gateway, SYS-G3 landing zones and SD-WAN, and SYS-G4 email (including office intake mailboxes).
- **Outside, internal service provider:** the SYS-S1 Practice Cloud platform (multi-tenant service, provider B), evidenced by its SOC 2 Type 2 report.
- **Outside, interconnected:** the tax engine vendor's transmitter (IRS and state e-file), the third-party model provider (AI-001), and SYS-W1 (referral interface).

The diagram is in P04 `cloud-architecture.md` (section 2.2).

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Tax engine vendor's transmitter (Authorized IRS e-file Provider) | Outbound returns; inbound acknowledgments | Signed returns; IRS and state acknowledgments | License and transmission agreement; disclosure permitted by 301.7216-2(d)(1) |
| Third-party model provider (AI-001) | Outbound documents; inbound extracted fields | Scanned source documents (SSNs, wages, bank details) | 2025 contract: U.S.-only processing, no training, no human review of content, deletion within 30 days |
| SYS-S1 Practice Cloud (internal service provider) | Both | Client documents, signatures, delivered returns | 2024 master agreement; 72-hour incident notice |
| SYS-W1 Wealth CRM (referral interface) | Outbound nightly batch | Selected tax return information for consenting clients. **Gap:** no consent check in the interface (POAM-009) | IRC 7216 consent (2022 template, **not specific enough**, POAM-022); integrated planning agreement (2022) |
| SYS-W1 (integrated planning data) | Inbound | Custodial statements and planning data for 210,000 households, held for Wealth | Integrated planning agreement (2022; **no Regulation S-P 72-hour term**, POAM-018) |
| SYS-G4 office intake mailboxes | Inbound | Client documents emailed to offices; moved to SYS-T1 by intake staff | Group email; **legacy authentication still allowed** (POAM-002) |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| Tax engine (licensed) | Containers on managed Kubernetes (PaaS) | Provider A | Tax division technology director |
| Workflow and review tools | Containers (in-house) | Provider A | Tax division technology director |
| Return data store | Managed relational database and object storage | Provider A | Tax division technology director |
| AI document extraction service | Containers calling a hosted model API | Provider A; model provider (U.S.) | Chief Tax Officer (business); system owner (operation) |
| E-file gateway | Containers with private egress | Provider A | Tax division technology director |
| Referral interface | Managed integration service | Provider A | Tax division technology director |
| Client portal tenant | SaaS tenant of SYS-S1 | Provider B | Tax division operations director (tenant); Practice Cloud CISO (platform) |
| Office workstations and scanners | Managed endpoints | About 1,150 tax offices | Group endpoint team |
| Backups | Immutable vault | Provider B | Group cloud platform director |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv` (145 controls) and `common-control-catalog.csv` (111 group common controls).

| Status | Controls |
|---|---|
| Implemented | 126 |
| Partially implemented | 19 |
| Planned | 0 |
| Not applicable | 0 |
| **Total** | **145** |

| Inheritance | Controls |
|---|---|
| Common/Inherited (85 from SYS-G1 to SYS-G3, group functions, or the cloud providers; 2 from Practice Cloud) | 87 |
| Hybrid (group provides the mechanism; the TPCP configures or operates part) | 25 |
| System-specific | 33 |

**The 19 partially implemented controls** cluster in four places:
- **IRC 7216 consent and permitted purpose** (scenario gap 1): AC-4, AC-6, AC-21, PT-2, PT-3, PT-4.
- **Seasonal workforce identity** (gap 2): AC-2, AT-2, PS-3, PS-4.
- **Email and refund-diversion detection** (gap 3): IA-2, SI-4, AU-6.
- **AI, vendors, and cross-division response** (gaps 4 and 6): CM-4, SA-11, SA-9, CP-4, IR-3, IR-6.

### 10.2 Common control inheritance by division
The catalog lists 111 controls provided by corporate (110 that the TPCP inherits in full or in part, plus the SYS-G4 mail-flow control, AC-4, that reaches the TPCP only through its email settings). Inheritance is **documented for Tax and Advisory** (2025 inheritance matrix, now replaced for the TPCP by this plan), **for Wealth** (its 2025 Regulation S-P program maps its safeguards to group controls), and **for Practice Cloud** (its SOC 2 system description carves in the group services). It is **not documented for CPA Partners** (scenario gap 7). Until POAM-016 closes, CPA Partners cannot show which safeguards for its engagement files and HIPAA business associate work are met by group controls under the administrative services agreement.

### 10.3 Control assessment status
Common controls were assessed once, and TPCP and division controls sampled, from 2026-07-06 to 2026-08-28 by group internal audit. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
- **Workforce users** authenticate through SYS-G1 single sign-on with number-matching MFA; **administrators** use phishing-resistant hardware keys and just-in-time PAM elevation.
- **Seasonal users** use the same MFA, have no remote access, and work only from office devices. Their account lifecycle is the main identity weakness (POAM-001).
- **Clients** use portal accounts with mandatory MFA (since 2025-12). New clients are identity-proofed in the office or remotely. Form 8879 e-signature uses the identity verification that IRS Pub. 1345 requires for electronic signatures.
- **Office intake mailboxes** are the exception: legacy authentication without MFA is still allowed for them until POAM-002 closes.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), group and division risk registers (P01), gap analyses and regulation-by-division matrix (P03), cloud architecture and control map (P04), BIA (P05), group policies and division supplements (P06), assessment and POA&M (P07), incident response runbook and notification matrix (P08), SOC 2 readiness (P09), AI governance (P10).

## 13. Acronym List and Glossary
- **EFIN / PTIN:** Electronic Filing Identification Number / Preparer Tax Identification Number
- **ERO:** Electronic Return Originator
- **Integrated planning client:** a Wealth household whose returns Tax and Advisory prepares
- **Qualified Individual:** the person responsible for the information security program under 16 CFR 314.4(a)
- **Referral interface:** the batch interface that sends selected tax return information to the Wealth CRM for consenting clients
- **Tax return information:** any information furnished for or in connection with preparing a return, including information derived from it and statistical compilations (26 CFR 301.7216-1(b)(3))
- **TPCP:** Tax Preparation and Client Portal Platform

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-08-28 | Draft after P07 fieldwork | Tax division technology director |
| 1.0 | 2026-09-10 | Approved with authorization conditions | Group CISO |
