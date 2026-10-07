# System Security Plan: Transaction Management and Closing Communications System (TMCC)

**Organization:** Cris Santos Company, Inc. and its subsidiary Cris Santos Title and Closing, LLC (PE-backed residential real estate brokerage with property management and title and closing services) | **Tier:** Mid-Market | **Vertical:** Real Estate and Rental and Leasing
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-29

## 1. System Name and Identifier
Transaction Management and Closing Communications System (**TMCC**), identifier CSC-TMCC-01. The TMCC is the company's major system. It comprises SYS-01 to SYS-08 in `../00_company-facts.md`, with their interfaces to SYS-09 (banking) and SYS-12 (e-signature).

## 2. System Overview
The TMCC carries every step of a residential sale from signed contract to disbursed funds:
- contract management, compliance review, and document storage for about 12,600 transaction sides a year;
- communications with buyers, sellers, lenders, and other title agents, including the delivery of **wire instructions** through the Closing Communications Portal;
- title production, settlement statements, the disbursement ledger, and about 35,000 outgoing wires a year (about $3.6 billion) from Title and Closing's trust accounts.

Users: 600 employees (including 112 Title and Closing staff, 88 transaction coordinators, and 44 finance and escrow accounting staff), about 1,650 contractor sales associates who use company email and the transaction platform from their own devices, and about 28,000 buyer and seller portal accounts.

**Why this system.** The BIA (P05) rates closing and disbursement (BP-01) and wire instruction delivery (BP-02) as the most time-critical processes, and the risk register (P01) rates diverted closing funds as the top risk (R-001 and R-002). Every component an attacker would touch in a business email compromise scheme is inside this boundary.

**Major components:**
| ID | Component | Hosting and service model |
|---|---|---|
| SYS-01 | Transaction management platform (agent and client portal) | Vendor SaaS; vendor SOC 2 Type 2 |
| SYS-02 | Title production and closing software (settlement statements, disbursement ledger, positive pay files) | Vendor SaaS; vendor SOC 2 Type 2 |
| SYS-03 | Identity provider with SSO, MFA, and conditional access | SaaS |
| SYS-04 | Productivity suite (email, files, chat) | SaaS |
| SYS-05 | Cloud landing zone: identity, shared services, workloads, and backup accounts; Closing Communications Portal, integration service, data warehouse | Public cloud IaaS/PaaS, vendor-agnostic (P04) |
| SYS-06 | Networks at headquarters and 22 sales offices on SD-WAN, including the headquarters file server | On-premises; SD-WAN managed service |
| SYS-07 | 660 company laptops and desktops and 80 company phones; contractor personal devices when they access SYS-01 or SYS-04 | Company-managed; personal devices unmanaged |
| SYS-08 | SIEM operated by the MSSP | SaaS |

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it affects the TMCC |
|---|---|---|---|
| N53-R01 | FTC Standards for Safeguarding Customer Information (Safeguards Rule). Binds Title and Closing, a settlement services provider; the parent handles its customer information as affiliate and service provider (P03 section 1.1) | 16 CFR Part 314 | Primary control requirement; mapped in `control-implementation.csv` |
| N53-R02 | FTC Act Section 5 (unfair or deceptive practices, including unreasonable data security) | 15 U.S.C. 45(a) | Applies to the whole company, including brokerage-only data |
| State | Broker escrow duties | Fla. Stat. 475.25(1)(d)1. and (1)(k); Fla. Admin. Code ch. 61J2-14; r. 61J2-10.032 | Sales escrow deposits and refunds that the TMCC records |
| State | Title agency trust funds | Fla. Stat. 626.8473 | Disbursements must follow closing instructions; drives the High integrity rating |
| State | Florida Information Protection Act | Fla. Stat. 501.171(2), (4), (8) | Reasonable security, breach notice, and disposal (P08) |
| Federal | RESPA affiliated business arrangements | 12 CFR 1024.15 | Referral data shared with the mortgage joint venture (section 8); compliance owned by General Counsel |
| Contract | Lender clients and the national homebuilder | Closing services agreements | SOC 2 Type 2 report on Title and Closing's services (P09) |
| Internal | Security policies POL-01 to POL-05 and standards STD-01 to STD-11 | P06 | Policy basis for every control |

Not applicable to this system (reasoning in P03 section 1):
- **CCPA/CPRA (N53-R03):** not doing business in California under General Counsel's 2025 position; settlement data is GLBA data in any case.
- **PCI DSS (N53-R04):** card payments run only on the property management platform's hosted payment page, outside this boundary.
- **SEC cybersecurity disclosure (N53-R05):** privately held.
- **FinCEN residential real estate reporting (31 CFR 1031.320):** vacated on 2026-03-19, appeal pending. If restored, reports would be prepared from SYS-02 data (P03 G-064).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Chief Operating Officer (system owner) on 2026-09-29, after the control assessment (P07), and presented the same day to the audit committee and to Title and Closing's board of managers.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization to operate. The equivalent internal decision:
- **Decision:** operation of the TMCC accepted with conditions, 2026-09-29.
- **Authorizing official equivalent:** Chief Executive Officer for High and Very High risks; Chief Operating Officer for Moderate and below (P01 acceptance authorities). For Title and Closing, the President of Title and Closing co-signs as the senior member who oversees the Qualified Individual (16 CFR 314.4(a)(2)).
- **Conditions:**
  - MFA enforced for every contractor agent by 2026-11-15 (POAM-001). If it slips, agents without MFA lose access to email and SYS-01 on that date.
  - Out-of-band verification of every payee and bank account change in all three account types by 2026-11-30 (POAM-002).
  - SaaS application logs in the SIEM by 2027-01-31 (POAM-005).
  - Quarterly POA&M status to the audit committee; re-decision by 2027-09-30 or after a major change.
### 4.3 System Operational Status
Operational. Major modifications planned:
- transaction-level visibility in SYS-01, replacing office-wide visibility (2027-03-31);
- SaaS application log integration with the SIEM (2027-01-31);
- independent backup of email, files, and SYS-01 data (2027-03-31);
- secure development pipeline for the Closing Communications Portal (2027-01-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Chief Operating Officer | Accountable for the TMCC; accepts Moderate risk; executive sponsor of the security program |
| Authorizing official equivalent (High risk) | Chief Executive Officer | Accepts High risk; approves the risk appetite |
| Oversight | Board audit committee; Title and Closing board of managers | Quarterly cyber risk reporting; annual Qualified Individual report (314.4(i)) |
| Qualified Individual and system security officer | Security Manager (parent company employee) | Runs the program (16 CFR 314.4(a)); maintains this plan |
| Senior overseer of the Qualified Individual for Title and Closing | President, Title and Closing | Directs and oversees the Qualified Individual for the financial institution (314.4(a)(2)); owns disbursement procedures |
| Program strategy | vCISO (part-time contractor) | Strategy, board reporting support, plan review |
| Infrastructure and recovery | IT Director | Landing zone, networks, endpoints, backup and recovery |
| Data and process owner, escrow and trust records | Controller; Title Escrow Accounting Manager | Reconciliations; banking entitlements with the CFO |
| Data and process owner, transactions | Director of Transaction Services | SYS-01 workflows and contract-to-close communications |
| Contractor oversight | Director of Agent Services; managing brokers | Agent onboarding and offboarding |
| Legal and notification | General Counsel | Contracts, notices, RESPA |
| Independent assessment | Co-sourced internal audit firm | Annual IT audit; P07 assessment |
| Monitoring | MSSP (service provider under 314.4(f)) | 24x7 EDR and SIEM monitoring |

## 6. System Information Types and System Categorization
Information types come from NIST SP 800-60 Vol. 2 Rev. 1, rated for this company. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Payments and funds disbursement (wire instructions, disbursement ledger, trust balances, payee bank data) | Moderate | **High** | Moderate | One altered instruction can send $60,000 to $400,000 of a client's funds to a criminal (P05); losses are often unrecoverable and breach trust fund duties (Fla. Stat. 626.8473(4)). Closings can slip one day (P05 MTD 8 h) |
| Customer personal and financial information (IDs, Social Security numbers, bank and loan data in closing files for about 98,000 consumers) | Moderate | Moderate | Moderate | Disclosure triggers FTC and Florida notice duties and identity theft risk; serious but not catastrophic to the company |
| Contract and transaction records | Moderate | Moderate | Moderate | Contract deadlines run in days (P05 BP-04 MTD 24 h) |
| Workforce and contractor identities | Moderate | Moderate | Low | Credentials are the entry point for BEC; limited harm if briefly unavailable |
| System and network monitoring (security logs) | Moderate | Moderate | Low | Needed to prove what customer information was acquired (P08) |
| **TMCC category (high-water mark)** | **Moderate** | **High** | **Moderate** | |

**Why integrity is High.** The P01 top risks are integrity failures: a changed payee, a spoofed payoff letter, a portal that shows the wrong account. Integrity was not lowered with compensating arguments, as it can be in other sectors, because the harm falls on clients and is often permanent.

## 7. Authorization Boundary Description
**Inside the boundary:**
- the company's tenant configuration, users, roles, and workflows in SYS-01, SYS-02, SYS-03, and SYS-04;
- all 4 cloud accounts and their workloads (Closing Communications Portal, integration service, data warehouse, backups);
- networks at all 23 sites, including firewalls, switches, staff and guest Wi-Fi, and the headquarters file server;
- 740 company endpoints, and contractor personal devices when they access SYS-01 or SYS-04;
- the company's SIEM tenant and its use cases.

**Outside the boundary (interconnected external services):**
- SYS-09 banking platforms at 3 banks;
- SYS-12 e-signature service;
- the SaaS vendors' own platforms and the cloud provider's infrastructure;
- the MSSP's platform;
- lenders' payoff portals and the title insurance underwriter's agent portal;
- the mortgage joint venture's systems (operated by the partner lender).

**Neighbors outside the boundary:** SYS-10 property management platform, SYS-11 CRM, and SYS-13 accounting system. They share the identity provider, email, and integration service, so their connections are documented here, but their own controls are covered by the risk register, P09, and P10, not by this plan.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| SYS-09 banking platforms (2 trust account banks, 1 escrow and operating bank) | Outbound wires, ACH, and positive pay files; inbound confirmations | Payee, account, amount | Treasury services agreements (security procedure: hardware tokens; dual approval on trust accounts only, **gap**) |
| SYS-12 e-signature service | Bidirectional (API from SYS-01 and SYS-02) | Contracts, addenda, closing documents | Vendor terms; security terms negotiated in 2025 |
| Integration service to SYS-01, SYS-02, SYS-10, SYS-11, SYS-13 | Bidirectional (API over TLS) | Transaction status, parties, closing dates, commission data | Vendor API terms; 7 non-expiring service secrets (**gap**, IA-5) |
| Closing Communications Portal to buyers and sellers | Outbound | Closing documents, wire instructions | Portal terms of use; notice at contract |
| Lenders and loan servicers | Inbound closing packages and payoff statements; outbound funding confirmations | Loan and payoff data | Lender closing instructions; payoffs must come from the lender portal or be verified by callback |
| Title insurance underwriter | Outbound policy and premium data | Policy data | Agency agreement |
| Mortgage joint venture (partner lender's systems) | Outbound leads by API from SYS-11, after buyer consent | Name, contact data, price range, pre-approval status | Joint venture data-sharing agreement with security terms; Affiliated Business Arrangement Disclosure Statement at referral (12 CFR 1024.15(b)(1)) |
| Title and Closing (subsidiary) | Shared systems run by the parent | All Title and Closing customer information | 2022 intercompany services agreement with **no security terms** (gap 4; 314.4(a)(3)) |
| MSSP | Inbound logs; remote response actions | Security logs, which may include email metadata | MSSP contract with security terms; SOC 2 Type 2 |
| Contract development firm | Remote access to the portal pipeline | Portal code, test data | Development contract without secure development terms (**gap** 10) |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| Transaction platform tenant (SYS-01) | SaaS | Transaction platform vendor | Director of Transaction Services |
| Title production tenant (SYS-02) | SaaS | Title production vendor | President, Title and Closing |
| Identity provider tenant (SYS-03) | SaaS | Identity vendor | IT Director |
| Productivity suite tenant (SYS-04) | SaaS | Productivity suite provider | IT Director |
| Closing Communications Portal | Managed web application service, managed database, web application firewall | Workloads account (SYS-05) | President, Title and Closing (business); IT Director (technical); contract development firm maintains code |
| Integration service | Virtual machines | Workloads account | IT Director |
| Data warehouse | Managed database service | Workloads account | Chief Financial Officer |
| Backup vault | Backup service with write-once retention | Backup account (second region) | IT Director |
| Network hub, cloud firewall, privileged access service, log pipeline and locked log bucket | Network and management services | Shared services account | IT Director |
| Cloud identity federation, organization guardrails, posture service | Identity and policy services | Identity account | Security Manager |
| SD-WAN edges, firewalls, switches, Wi-Fi (23 sites) | Network | Headquarters and 22 offices | IT Director |
| Headquarters file server (scanned closing files 2012 to 2018) | On-premises server | Headquarters | President, Title and Closing |
| Company laptops and desktops (660) and phones (80) | Endpoint | All sites and remote | IT Director |
| Contractor personal devices (about 3,000) | Endpoint (unmanaged) | Agents' homes and the field | Each agent, under the agent agreement |
| SIEM tenant | SaaS | MSSP | Security Manager |

## 10. Control Implementation Details
### 10.1 Control implementation status
**Baseline and tailoring.** The company is not bound by FIPS 200. It uses the NIST SP 800-53B **Moderate** baseline (287 controls and enhancements) as its starting point, because confidentiality and availability are Moderate, and tailors it for the High integrity rating:
- **Documented here: 116 controls** in `control-implementation.csv`. They cover every SP 800-53 control mapped to a Safeguards Rule element in P03 (an author mapping), the controls that address the High and Moderate risks in P01 (payee verification, agent identity, logging, recovery, vendor oversight), and core network hygiene.
- **Added by tailoring (5):** CA-8 Penetration Testing (High baseline), which 16 CFR 314.4(d)(2)(i) also requires absent effective continuous monitoring; and PM-1, PM-2, PM-9, and PM-14, which have no baseline allocation but carry the program elements of 314.3(a), 314.4(a), (b)(1)(iii), and (d)-(e).
- **Integrity tailoring:** the AC-5, SI-7, SI-10, and AT-3 statements set funds-specific requirements beyond the baseline wording: dual control on every escrow and trust account payment and payee change, independent callback to a number from the file, and a portal check that displayed instructions match the ledger.
- **Inherited without separate statements:** the remaining Moderate-baseline physical and environmental controls for cloud and SaaS data centers (for example PE-9 to PE-17) and platform-level SA and SC controls. They are inherited from the SaaS vendors, the identity vendor, the cloud provider, and the MSSP, evidenced by their SOC 2 Type 2 reports, which are reviewed each year (P09 `vendor-soc2-review.csv`).
- **Deferred:** the other Moderate controls with no Safeguards Rule mapping and no Moderate-or-higher risk in P01 (for example PL-8 security architectures and SA-5 system documentation, which the SaaS vendors' own documentation covers). The PT privacy family belongs to the privacy baseline, not the Moderate security baseline, and is handled by General Counsel's privacy notice program. They are recorded as tailoring decisions and reviewed yearly.

**Status of the 116 documented controls:**
| Status | Count |
|---|---|
| Implemented | 39 |
| Partially implemented | 73 |
| Planned | 4 |
| Not applicable | 0 |

**Inheritance of the 116 documented controls:**
| Inheritance | Count | Main providers |
|---|---|---|
| System-specific | 67 | Company |
| Hybrid | 36 | SaaS vendors, identity vendor, cloud provider, MSSP, banks |
| Common/Inherited | 13 | Identity vendor (for example AC-7, IA-2(1)), cloud provider (CP-6, SC-5), MSSP and insurer panel (IR-7), email security vendor (SI-8) |

By baseline: 111 of the documented controls are in the Moderate baseline, 1 comes from the High baseline (CA-8), and 4 are program management controls added by tailoring.

The Partially implemented statements trace to the 11 known gaps in `../00_company-facts.md` section 4 and to the P07 findings.

**The gaps that matter most** (all tracked in the P07 POA&M):
- IA-2(2): about 310 contractor agents without MFA.
- AC-5 and SI-7: payee and bank account changes outside Title and Closing are not independently verified.
- AU-2, AU-6, and SI-4: SaaS application events (payee changes, exports) are not monitored.
- CP-2, CP-4, and CP-9: no SaaS downtime plan, no independent backup of email and SYS-01 data.
- SA-4, SA-11, and SA-15: the portal that delivers wire instructions has no secure development standard.

### 10.2 Control assessment status
The co-sourced internal audit firm assessed 32 controls from 2026-08-17 to 2026-09-04 (P07 `assessment-plan.md`, `assessment-results.csv`, and `poam.csv`). Weaknesses are tracked in the POA&M and reported quarterly to the audit committee and to Title and Closing's board of managers.

## 11. Digital Identity Acceptance Statement
- **Employees:** all employees authenticate through the identity provider with a password and push MFA with number matching, under conditional access that checks device compliance. That is acceptable for Moderate confidentiality.
- **Wire release staff and administrators:** because integrity is High and relay phishing kits defeat push and code-based MFA, the 46 staff who release or approve wires and all administrators use phishing-resistant security keys (in place since 2025).
- **Contractor agents:** about 1,340 use MFA; about 310 use a password only. A password alone is **not acceptable** for a system whose integrity rating is High. MFA is required for every agent by 2026-11-15 (16 CFR 314.4(c)(5)). The Qualified Individual will not approve an equivalent control in writing.
- **Buyers and sellers:** the portal uses a one-time code sent to a phone number verified at contract. This is acceptable only together with the rule that wire instructions are never changed by email and with the callback for any phone number change (planned 2027-01-31, IA-8).

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`); risk register (P01); gap analysis and roadmap (P03); cloud architecture and control map (P04); BIA (P05); policies and standards index (P06); assessment and POA&M (P07); incident runbooks (P08); SOC 2 readiness and vendor reviews (P09); AI governance assessment (P10).

## 13. Acronym List and Glossary
- **BEC:** business email compromise
- **EDR:** endpoint detection and response
- **FIPS:** Federal Information Processing Standards
- **MSSP:** managed security service provider
- **MTD, RTO, RPO:** maximum tolerable downtime, recovery time objective, recovery point objective
- **POA&M:** plan of action and milestones
- **Qualified Individual:** the person designated under 16 CFR 314.4(a) to oversee, implement, and enforce the information security program
- **SD-WAN:** software-defined wide area network
- **TMCC:** Transaction Management and Closing Communications System
- **WAF:** web application firewall

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-08-07 | Draft from the BIA, risk assessment, and gap analysis | Security Manager |
| 1.0 | 2026-09-29 | Updated with P07 results; approved by the Chief Operating Officer | Security Manager (Qualified Individual) |
