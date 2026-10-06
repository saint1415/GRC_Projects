# System Security Plan: Transaction Management and Closing Communications System (TMCC)

**Organization:** Cris Santos Company Holdings, Inc. (shared system of the Residential Brokerage and Mortgage and Title divisions, on corporate shared services) | **Tier:** Multi-Sector | **Vertical:** Real Estate and Rental and Leasing
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-17

> **Why this system.** At this tier the SSP can cover one system per division or a shared system. The group chose the **TMCC** because it is where the group's top risk lives (P01 GR-01, business email compromise targeting closing funds): it carries a sale from signed contract to disbursed funds across two divisions, it holds customer information of Title (a financial institution under the FTC Safeguards Rule) and brokerage client files in one place, and it inherits most of its controls from corporate (SYS-G1 to SYS-G5). Each division's other systems (for example, Home Loans' loan origination system SYS-M1 and the Homebuilding ERP SYS-H1) keep their own plans that inherit from the same common control catalog (`common-control-catalog.csv`).

## 1. System Name and Identifier
Transaction Management and Closing Communications System (**TMCC**), identifier CSCH-TMCC-01. Components SYS-B1 and SYS-B2 in `../00_company-facts.md` section 3, plus the TMCC integration service.

## 2. System Overview
The TMCC supports about 170,000 brokerage transaction sides and about 128,000 Title closings a year. It does four jobs:
- **Contract to close (SYS-B1):** contracts, compliance review, deadlines, and document storage for brokerage transactions, used by about 52,000 contractor agents and 4,600 brokerage employees.
- **Closing communications (SYS-B2):** the Closing Communications Portal, the only channel for title wire instructions since 2022. About 340,000 buyers and sellers a year sign in to see closing documents and, after an identity check, wire instructions.
- **Integration:** the company-built TMCC integration service syncs SYS-B1, SYS-B2, SYS-M2 (title production), and SYS-G5 (payee records and wire release).
- **Payee verification hand-off:** every instruction displayed in SYS-B2 is checked against the payee record in SYS-G5 before display and again before release.

**Major components:**
- **SYS-B1 tenant:** vendor SaaS (the group configures roles, visibility, retention, and integrations). The vendor provides a SOC 2 Type 2 report (P09 vendor review).
- **SYS-B2 Closing Communications Portal:** company-built web application on managed containers, an API gateway, and a managed database in cloud provider A.
- **TMCC integration service:** company-built message and workflow service in provider A.
- **Warm standby:** SYS-B2 and the integration service in provider B.
- **Identity verification service:** a third-party SaaS that proofs consumers before wire instructions are shown (AI-006 in P10).
- **E-signature service:** a third-party SaaS integrated with SYS-B1 and SYS-M2.

Cloud services are described by category and are vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies to the TMCC |
|---|---|---|---|
| N53-R01 | FTC Safeguards Rule | 16 CFR Part 314 | Title and Home Loans are financial institutions. Title's customer information sits in the TMCC, and an information system includes one "connected to a system containing customer information" (314.2(j)). Customer information includes records handled "by or on behalf of you or your affiliates" (314.2(d)). The brokerage is not a financial institution itself (P03 section 1), but the TMCC is part of Title's information system, so the full rule applies to it |
| N53-R02 | FTC Act Section 5 | 15 U.S.C. 45(a) | Reasonable security for brokerage client data and accurate representations about it |
| N53-R05 | SEC cybersecurity disclosure | Reg S-K Item 106; Form 8-K Item 1.05 | A TMCC incident may be material to the group (P08) |
| State law | Breach notice and data security | Each state where affected individuals reside; Fla. Stat. 501.171(2), (4), (6), (8) as the worked example | Reasonable measures, notices, third-party agent duties, and disposal for personal information in the TMCC |
| State law | Trust funds and escrow | Fla. Stat. 626.8473(3)-(5) (Title, worked example); Fla. Stat. 475.25(1)(k) and Fla. Admin. Code ch. 61J2-14 (brokerage escrow, worked example) | Wire instructions and escrow records in the TMCC drive how trust and escrow funds move |
| RESPA | Affiliated business arrangements | 12 CFR 1024.15 | Referrals between the brokerage, Home Loans, and Title require the affiliated business disclosure; the TMCC records when it was given |
| Contracts | Intercompany services agreement (2021); vendor contracts | 16 CFR 314.4(a)(3), (f)(2) | The intercompany agreement has no security, audit, or incident notice terms (POAM-013) |
| Internal | Group policies POL-01 to POL-05 and division supplements | P06 | |

Not applicable to the TMCC: PCI DSS (N53-R04), because no card data is stored, processed, or transmitted in the TMCC; CCPA/CPRA (N53-R03), because the group has no California operations (reviewed each year by the Group General Counsel).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Group CISO (Qualified Individual), the TMCC system owner, and the President, Title (co-data owner) on 2026-09-17, after the board risk committee review.

### 4.2 System Authorization Decision
The group is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- **Decision:** authorized to operate with conditions, 2026-09-17, by the Group CISO and the Group Chief Risk Officer (acceptance authority for High risks).
- **Conditions:**
  1. MFA for all contractor agent accounts by 2026-12-31; accounts without MFA after that date are disabled (POAM-001).
  2. No email delivery of any wire instruction for brokerage escrow deposits or refunds; out-of-band verification for every escrow refund wire by 2026-11-30 (POAM-003).
  3. SYS-B1 audit logs in the SIEM with alerts on payee and bank account changes by 2027-01-31 (POAM-004).
  4. No new affiliate data feed from the TMCC without a documented purpose approved by the Group Chief Privacy Officer and the Title co-data owner (POAM-006).
- **Reauthorization:** annually, or after a major change to wire instruction delivery.

### 4.3 System Operational Status
Operational. **Planned changes:** the contractor agent identity tier moves to phishing-resistant or app-based MFA (2026 Q4); SYS-B1 visibility moves from office level to transaction team level (2027 Q1, POAM-009).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Residential Brokerage chief product officer | Accountable for the TMCC and this SSP |
| Co-data owner (Title customer information and wire instructions) | President, Title | Approves access to Title data and any change to instruction publishing |
| Authorizing official equivalent | Group CISO (Qualified Individual for Home Loans and Title) with the Group Chief Risk Officer | Authorization decision; High risk acceptance |
| Senior officer overseeing the Qualified Individual for Title | President, Title | 16 CFR 314.4(a)(2) |
| Escrow account owner (brokerage) | Florida Broker of Record (each state's Broker of Record for its accounts) | Escrow deposit and refund procedures |
| Privacy oversight | Group Chief Privacy Officer | Affiliate data sharing, purposes, retention |
| Common control providers | Group identity director (SYS-G1), Group SOC director (SYS-G2), Group cloud platform director (SYS-G3), Group collaboration services director (SYS-G4), Group Treasurer (SYS-G5) | Operate inherited controls (`common-control-catalog.csv`) |
| Independent assessor | Group internal audit | Assesses common controls once and samples TMCC and division controls (P07) |

## 6. System Information Types and System Categorization
Information types were chosen with NIST SP 800-60 Vol. 2 Rev. 1 as a guide and adjusted for this business. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Closing and settlement records (Title customer information; brokerage client files) | **High** | Moderate | Moderate | Aggregation: SYS-B1 holds files on about 3.1 million consumers back to 2011. A disclosure would trigger FTC notices for Title, breach notices in 8 states, and an SEC materiality decision |
| Wire and payee instructions | Moderate | **High** | Moderate | An altered instruction diverts funds directly. Title disburses about $208 million per business day; a single diverted closing can exceed $500,000 |
| Personal identity and authentication (consumer identity checks; agent identities) | Moderate | High | Moderate | Identity checks gate access to wire instructions |
| Information security (keys, access policies, audit trails) | High | High | Moderate | Compromise would expose every transaction |
| **TMCC category (high-water mark)** | **High** | **High** | **Moderate** | Overall **High**. Availability is Moderate: the BIA sets an RTO of 4 hours with a phone-based fallback (P05 BP-BR02) |

**Baseline:** the NIST SP 800-53B **High** baseline, tailored. The plan documents **147 controls** in `control-implementation.csv`:
- 140 from the High baseline;
- 3 from the privacy baseline (PM-9, PT-2, PT-3), added because affiliate data use is the TMCC's main privacy risk;
- 2 program management controls not in any baseline (PM-1, PM-2), because the Qualified Individual and program duties of 16 CFR 314.4(a) attach here;
- 2 controls tailored in from outside the baselines: **AC-3(2) Dual Authorization** and **SC-37 Out-of-band Channels**, because dual approval and callback verification are the core defenses against diverted closing funds.

Other High-baseline controls are either fully inherited from the cloud providers and SaaS vendors (for example, most PE controls, evidenced by their SOC 2 Type 2 reports) or tailored out with a reason in the group tailoring register (for example, PE controls for facilities the group does not operate, and wireless controls with no TMCC wireless component).

## 7. Authorization Boundary Description
- **Inside:** the SYS-B1 tenant configuration and data; SYS-B2 (containers, API gateway, database, and document storage in provider A); the TMCC integration service; the warm standby in provider B.
- **Outside, inherited (common control providers):** SYS-G1 identity, SYS-G2 SOC and SIEM, SYS-G3 landing zones and backup vault, SYS-G4 email (notifications), and SYS-G5 payee verification and wire release.
- **Outside, interconnected:** SYS-M2 title production (vendor-hosted), the identity verification service, the e-signature service, and the Group Data Platform (nightly feed, under review).

Diagram: P04 `cloud-architecture.md` (the TMCC subgraph).

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| SYS-M2 title production (vendor-hosted) | Inbound | Settlement statements; wire instructions; closing documents | Title vendor contract with security and incident terms |
| SYS-G5 treasury and payments hub | Both | Payee records out; verification result and release status in | Group common control; intercompany services agreement (no security terms, POAM-013) |
| SYS-G4 email | Outbound | Notification that a document is ready (no content, no instructions) | Group common control |
| Identity verification service | Both | Consumer identity document and selfie out; match result in | Vendor contract with no-training and 30-day deletion terms |
| E-signature service | Both | Contracts and closing documents | Vendor contract |
| SYS-B3 brokerage CRM and SYS-M1 loan origination | Outbound | Buyer contact and transaction status for affiliate referrals | Affiliated business disclosure given at referral (12 CFR 1024.15(b)(1)); **purpose and consent records not documented** (POAM-006) |
| Group Data Platform | Outbound nightly | Closing data for analytics, including Title customer information | **No documented purpose or data owner approval** (scenario gap 4; POAM-006) |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| SYS-B1 transaction platform tenant | SaaS | Vendor | TMCC system owner |
| SYS-B2 portal application | Managed containers and API gateway (PaaS) | Provider A | TMCC system owner |
| SYS-B2 database and document storage | Managed database and object storage | Provider A | TMCC system owner |
| TMCC integration service | Managed workflow and messaging (PaaS) | Provider A | TMCC system owner |
| Warm standby | Containers, database replica | Provider B | Group cloud platform director |
| Secrets and keys | Key management and secret store | Provider A | Group cloud platform director |
| Identity verification service | SaaS | Vendor | President, Title (business owner) |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv` (147 controls) and `common-control-catalog.csv` (117 group common controls).

| Status | Controls |
|---|---|
| Implemented | 124 |
| Partially implemented | 23 |
| Planned | 0 |
| Not applicable | 0 |
| **Total** | **147** |

| Inheritance | Controls |
|---|---|
| Common/Inherited (from SYS-G1 to SYS-G5, group functions, or the cloud providers) | 94 |
| Hybrid (group provides the mechanism; the TMCC configures or operates part) | 24 |
| System-specific | 29 |

**The 23 partially implemented controls** cluster in five places:
- **Contractor agent identities** (scenario gap 1): AC-2, AC-2(12), AC-20, AT-2, IA-2(2), PS-7.
- **Payee verification and monitoring of payment changes** (gaps 2 and 3): SC-37, AU-2, AU-6, AU-12, SI-4.
- **Affiliate data flows, least privilege, and retention** (gaps 4 and 9): AC-4, AC-6, AC-21, PT-2, PT-3, SI-12.
- **Notification across regulators** (gap 7): IR-3, IR-6, IR-8.
- **Third parties and secrets:** SA-9, CP-2, IA-5.

**What is strong:** the single channel for title wire instructions (PL-8, SI-7, AU-10), dual approval and hardware-key release (AC-3(2), IA-2(1)), identity proofing before instructions are shown (IA-12, IA-11), and the portal's secure development and testing (SA-11, SA-15, CA-8).

### 10.2 Common control inheritance by division
The common control catalog lists 117 controls provided by corporate. Inheritance is **documented for the Residential Brokerage** and **for Home Loans and Title** (2025 inheritance matrices) and for the TMCC (this plan). It is **not documented for Homebuilding** (scenario gap 5): about 3,800 Homebuilding field and sales users are still on a legacy directory and email tenant, so some SYS-G1 and SYS-G4 controls do not reach them at all. Until POAM-014 and POAM-015 close, Homebuilding cannot show which controls it inherits, and P07 found the CA-2 statements for Homebuilding other than satisfied for this reason.

### 10.3 Control assessment status
Common controls were assessed once, and TMCC and division controls sampled, from 2026-07-06 to 2026-08-28 by group internal audit. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
- **Employees** authenticate through SYS-G1 with app-based MFA (number matching). **Administrators and Title staff who publish instructions or release wires** use phishing-resistant hardware keys.
- **Contractor agents** authenticate through the SYS-G1 contractor tier. 81% use app-based MFA; about 9,900 still use a password only under an expired exception (POAM-001). This is not acceptable for a High-integrity system and is condition 1 of the authorization.
- **Buyers and sellers** sign in to SYS-B2 with a one-time code sent to the email address Title verified at order opening, and must complete identity proofing (document and selfie match) before wire instructions are first shown (IA-12). A failed check routes to a Title closer, who verifies by phone at a number from the title file, never from an email.
- **Service accounts** for the integration service should use workload identity; two still use static API keys (POAM-008).

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), group and division risk registers (P01), gap analyses and regulation-by-division matrix (P03), cloud architecture and control map (P04), BIA (P05), group policies and division supplements (P06), assessment and POA&M (P07), incident response runbook and notification matrix (P08), SOC 2 readiness and vendor reviews (P09), AI governance (P10).

## 13. Acronym List and Glossary
- **Callback verification:** confirming a payee or bank account change by calling a number already on file, never one supplied in the request
- **Common control:** a control provided once by corporate and inherited by several systems
- **Contractor agent:** a licensed sales associate who is an independent contractor, not an employee
- **NPI:** nonpublic personal information
- **PAM:** privileged access management
- **Positive pay:** a bank service that matches presented items against the issuer's file
- **Qualified Individual:** the person who oversees a financial institution's information security program (16 CFR 314.4(a))
- **SIEM:** security information and event management
- **TMCC:** Transaction Management and Closing Communications System

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-08-28 | Draft after P07 fieldwork | TMCC system owner |
| 1.0 | 2026-09-17 | Approved with authorization conditions | Group CISO |
