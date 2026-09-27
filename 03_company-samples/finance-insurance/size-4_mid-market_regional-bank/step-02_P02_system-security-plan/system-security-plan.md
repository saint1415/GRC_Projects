# System Security Plan: Core and Online Banking Platform (COBP)

**Organization:** Cris Santos Bank, N.A. (regional commercial bank; subsidiary of Cris Santos Company, Inc., a privately held bank holding company) | **Tier:** Mid-Market | **Vertical:** Finance and Insurance
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-18

## 1. System Name and Identifier
Core and Online Banking Platform (**COBP**), identifier CSB-COBP-01. The COBP is the bank's major system. It is built from SYS-01, SYS-02, SYS-03, SYS-05, SYS-06, SYS-07 (part), SYS-10 (hosting only), and SYS-12 in `../00_company-facts.md`.

## 2. System Overview
The COBP is how the bank keeps its books and how customers, respondent institutions, and staff move money. It supports every High-criticality process in the BIA (P05): wires for bank customers (BP-01) and for 18 respondent institutions (BP-02), branch services (BP-03), online and mobile banking (BP-04), and ACH (BP-05). It serves about 107,500 deposit customers, 77,000 online banking users, 600 workforce members, and handles about 380 outgoing wires (about $165 million) a day.

**Major components:**
| ID | Component | Hosting and service model |
|---|---|---|
| SYS-01 | Core banking system: deposits, loans, customer information file, general ledger; the bank administers its users in the core security module | Hosted by the core processor (bank service provider); SOC 1 and SOC 2 Type 2 |
| SYS-02 | Online and mobile banking, consumer and business, with the bank's admin console (entitlements, limits, security settings) | Vendor-hosted SaaS (digital banking provider) |
| SYS-03 | Payments hub (wire and ACH) and correspondent portal; 4 payments workstations for the Federal Reserve payment services | Licensed software run by the bank in the production account (IaaS and PaaS) |
| SYS-05 | Identity provider: workforce SSO and MFA; customer identity service for respondent users | SaaS |
| SYS-06 | Landing zone accounts that host and protect SYS-03 and SYS-10: management, security and log archive, shared network, production, backup | Public cloud, vendor-agnostic (P04) |
| SYS-07 (part) | Operations center, both wire rooms, and branch endpoints and networks used to access the platform | On-premises; SD-WAN |
| SYS-12 | SIEM operated by the MSSP, and EDR | SaaS; managed service |

The AI credit decisioning service (SYS-10) runs in the production account. The COBP provides its hosting controls; the model itself is governed in P10.

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it affects the COBP |
|---|---|---|---|
| N52-R01 | Gramm-Leach-Bliley Act, section 501(b) safeguards | 15 U.S.C. 6801(b) | Basis for the safeguards standards below |
| N52-R02 | Interagency Guidelines Establishing Information Security Standards (OCC) | 12 CFR Part 30, Appendix B, with Supplement A | Primary control requirement; mapped in `control-implementation.csv` |
| Rule | Computer-Security Incident Notification | 12 CFR Part 53 (bank); 12 CFR 225 Subpart N (holding company) | 36-hour regulator notice; inbound notices from bank service providers; outbound notices to bank respondents (P08) |
| Rule | Identity Theft Red Flags | 12 CFR 41.90 | Account opening and contact-information changes on covered accounts (gap 2) |
| Rule | Suspicious activity reports | 12 CFR 21.11; 31 CFR 1020.320 | Fraud cases through the platform (P08) |
| Guidance | FFIEC Authentication and Access to Financial Institution Services and Systems (August 2021; Federal Reserve SR 21-14) | Supervisory guidance, not regulation | Examiners expect MFA or controls of equivalent strength for high-risk activities such as adding beneficiaries and sending wires (section 11) |
| Guidance | FFIEC Information Technology Examination Handbook | Supervisory guidance, not regulation | How examiners assess the Guidelines |
| State | Funds-transfer liability and security procedures (UCC Article 4A) | Fla. Stat. 670.202 and 670.204 | The callback is part of the agreed security procedure in funds transfer agreements |
| State | Breach notification | Fla. Stat. 501.171 (worked example); the law of each state where affected individuals reside | Customer notices (P08) |
| Contract | Respondent institution agreements | Contract | Correspondent service commitments (gap 12; P09) |
| Internal | Security policies POL-01 to POL-05 and the standards index | P06 | Policy basis for every control |

Not applicable (reasons in `../00_company-facts.md` section 1): the OCC heightened standards (12 CFR Part 30, Appendix D), the FTC Safeguards Rule (N52-R03), NYDFS Part 500 (N52-R04), SEC Regulation S-P and S-ID (N52-R05, N52-R06), NAIC Model #668 (N52-R07), and SEC cybersecurity disclosure (N52-R08). Consumer wire transfers sent through Fedwire are excluded from Regulation E's definition of electronic fund transfer (12 CFR 1005.3(c)(3)); Regulation E error resolution governs consumer ACH and bill payments, which are outside this plan's security scope.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Chief Operating Officer (system owner) on 2026-09-18, after the control assessment (P07) and the Board Risk Committee review on 2026-09-15.
### 4.2 System Authorization Decision
The bank is not a federal agency, so there is no formal authorization to operate. The equivalent internal decision:
- **Decision:** continued operation of the COBP accepted with conditions, 2026-09-18.
- **Authorizing official equivalent:** President and CEO for High risks, with the CRO's concurrence; COO for Moderate and below (P01 acceptance authorities).
- **Conditions:** the High-risk POA&M items in P07 must meet their milestones; the Audit Committee receives POA&M status each quarter; re-decision by 2027-09-30 or after a major change (for example, a new core processor or a new payments channel).
### 4.3 System Operational Status
Operational. Major modifications planned:
- Phishing-resistant customer authentication and out-of-band beneficiary confirmation (due 2027-03-31; P01 R-002)
- Out-of-band verification and customer alerts for contact-information changes (due 2026-12-31; R-001)
- Payments hub, correspondent portal, and core security logs onboarded to the SIEM, with change-anomaly use cases (due 2027-01-31; R-013)
- PAM extended to core security administrators and payments hub administrators (due 2027-03-31; R-007)
- Payments hub failover redesign and retest to meet the 4-hour RTO (due 2027-03-31; R-004)

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Chief Operating Officer | Accountable for the COBP; accepts Moderate risk |
| Authorizing official equivalent (High risk) | President and CEO, with the CRO's concurrence | Accepts High risk; reports each acceptance to the Board Risk Committee |
| Oversight | Board Risk Committee; Board Audit Committee | Program oversight and annual report (III.F); assessment and POA&M oversight |
| Information Security Officer | ISO (reports to the CRO) | Day-to-day security; SSP maintenance; MSSP oversight; designated by the board |
| IT operations | Chief Information Officer; Cloud Platform Manager; Infrastructure Manager | Operate the platform, the landing zone, networks, and endpoints |
| GRC | IT Risk and Compliance Manager | Risk register, policies, standards, POA&M tracking |
| Business process owners | Director of Payments Operations; Correspondent Services Director; Treasury Management Director; Retail Banking Director | Callback standard, limits, customer and respondent agreements, account maintenance |
| Fraud and SAR decisions | BSA/AML Officer | SARs; law enforcement liaison |
| Independent assessment | Chief Audit Executive with the co-sourced IT audit firm | Annual assessment (P07) |
| Operations support | Core processor; digital banking provider; payments hub vendor; MSSP | Hosting, application support, 24x7 monitoring |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Payments and collections (wire and ACH instructions, including for respondents) | Moderate | Moderate | Moderate | A fraudulent or altered wire causes direct financial loss. Per-wire limits, maker-checker, and the financial institution bond keep the worst single loss well below a level that would threaten the bank's capital, so the effect is serious rather than severe. Wires can be sent by the alternate procedure for one business day (P05 MTD 8 h) |
| Customer account and identity information (NPI, credentials) | Moderate | Moderate | Low | Disclosure enables account takeover and triggers customer notice analysis under Supplement A |
| General ledger and liquidity (financial management) | Low | Moderate | Moderate | Wrong balances could release wires against insufficient funds; the position can be estimated from Federal Reserve statements for a day |
| Workforce identities | Moderate | Low | Low | Account data; limited harm if unavailable |
| System and network monitoring (security logs) | Moderate | Moderate | Low | Needed for investigations and the notification incident determination |
| **COBP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Integrity was considered for High.** The COBP moves about $165 million a day. The team kept integrity at Moderate because maker-checker, per-wire limits, sanctions screening, and daily reconciliation to the Federal Reserve account limit any single loss, and the bond transfers part of it. To compensate, the tailoring below adds integrity-focused statements for CM-3 (payments hub business configuration), SI-10 (wire field validation), and AC-5 (limit changes).

**Baseline:** the NIST SP 800-53B **Moderate** baseline, tailored for a $2.5 billion bank as described in section 10.1.

## 7. Authorization Boundary Description
**Inside the boundary:**
- the bank's configuration of the core (users, roles, parameters it controls) and of online banking (admin console entitlements, limits, security settings);
- the payments hub and correspondent portal application stack in the production account, and the landing zone accounts that host and protect it;
- the identity provider tenant and its customer identity service for respondent users;
- the 4 payments workstations, both wire rooms, the operations center endpoints, and the branch endpoints used to take and key payment requests and account maintenance;
- the SIEM tenant and its use cases, and the EDR agents.

**Outside the boundary (external services, interconnected):**
- the core processor's platform and data centers;
- the digital banking provider's platform;
- the cloud provider's infrastructure;
- the Federal Reserve payment services;
- the MSSP's platform;
- the respondent institutions' own systems and users' devices;
- the card processor, the LOS provider, and the AML monitoring provider.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Core processor (SYS-01) | Bidirectional (private circuits; API from the payments hub) | Balances, holds, postings, customer profile | Core processor contract (no incident notice time frame or recovery terms; **gap**, renewal 2027) |
| Digital banking provider (SYS-02) | Bidirectional | Customer sessions, transfers, wire and ACH requests to the payments hub | Provider contract; 53.4 contact sent 2026-03 |
| Federal Reserve payment services | Outbound and inbound | Wire messages; ACH files | Federal Reserve operating circulars and the bank's access agreement |
| Respondent institutions (18) | Inbound payment orders; outbound settlement statements | Wire and ACH orders for respondents' customers | Respondent agreements (2019 template; **no security or notice terms**, gap 12) |
| Business customers | Inbound | Wire and ACH requests through online banking or relationship managers | Treasury management and funds transfer agreements (callback and dual approval as the security procedure) |
| AML monitoring provider (SYS-13) | Outbound nightly | Transactions from the core and the payments hub | Provider contract (**no 53.4 contact yet**) |
| MSSP | Outbound | Security logs and alerts | MSSP contract |
| Payments hub vendor | Inbound support sessions | Remote support | Support agreement; standing vendor VPN (**gap**, R-048) |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| Core security module configuration and bank parameters | SaaS configuration | Core processor | Chief Information Officer |
| Online banking admin console configuration | SaaS configuration | Digital banking provider | Treasury Management Director |
| Payments hub and correspondent portal (application servers, database) | Virtual machines and managed database | Production account | Director of Payments Operations (business); Cloud Platform Manager (technical) |
| Network hub, cloud firewall, VPN gateways | Network services | Shared network account | Cloud Platform Manager |
| Organization guardrails, posture management, log archive | Security services | Management and security accounts | Information Security Officer |
| Backup vault (write-once, 35 days) | Backup service | Backup account, second region | Cloud Platform Manager |
| Identity provider tenant and customer identity service | SaaS | Identity vendor | Chief Information Officer |
| Payments workstations (4) and hardware tokens | Endpoint | Primary and secondary wire rooms | Director of Payments Operations |
| Operations center and wire room endpoints (about 110) | Endpoint | Headquarters campus; Georgia regional office | Infrastructure Manager |
| Branch endpoints used for payments and maintenance (about 280) | Endpoint | 28 branches | Retail Banking Director |
| SD-WAN edges and firewalls | Network | 28 branches and 2 operations sites | Infrastructure Manager |
| SIEM tenant and EDR console | SaaS | MSSP; EDR vendor | Information Security Officer |

## 10. Control Implementation Details
### 10.1 Control implementation status
**Baseline and tailoring.** The COBP uses the NIST SP 800-53B **Moderate** baseline, tailored as follows:
- **Documented here: 115 controls** in `control-implementation.csv`. They cover every SP 800-53 control the author mapped to a provision of the Interagency Guidelines, Supplement A, 12 CFR Part 53, or 12 CFR 41.90 in P03 (an author mapping; no official NIST mapping of these rules exists), plus the Moderate controls that address the risks in P01 (payments integrity, privileged access, third parties, monitoring, recovery).
- **Selected by tailoring (added, not in the Moderate baseline): 4 controls.** PM-1, PM-2, and PM-9 support the board's role under III.A. CA-8 records the annual penetration tests the bank runs to meet III.C.3.
- **Integrity tailoring:** CM-3, SI-10, and AC-5 statements address payments hub configuration, wire validation, and limit changes (section 6).
- **Inherited without separate statements:** the remaining Moderate-baseline physical and environmental controls for provider data centers (for example PE-9 to PE-17), and platform-level SA and SC controls, inherited from the core processor, the digital banking provider, the cloud provider, the identity vendor, and the MSSP, and evidenced by their SOC reports, reviewed each year (P09 `vendor-soc2-review.csv`).
- **Deferred:** other Moderate controls with no mapping to the bank's rules and no Moderate-or-higher risk in P01 (for example SA-11 developer testing and SA-15 development process; the bank configures vendor software but does not develop it). They are recorded as tailoring decisions and reviewed each year.

**Status of the 115 documented controls:**
| Status | Count |
|---|---|
| Implemented | 57 |
| Partially implemented | 58 |
| Planned | 0 |
| Not applicable | 0 |

**Inheritance of the 115 documented controls:**
| Inheritance | Count | Main providers |
|---|---|---|
| System-specific | 71 | Bank |
| Hybrid | 36 | Core processor, digital banking provider, cloud provider, identity vendor, MSSP, payments hub vendor |
| Common/Inherited | 8 | Identity vendor (AC-7, IA-2(1), IA-2(2), IA-2(8)), providers (AC-12, SC-5, SC-13), MSSP and insurer panel (IR-7) |

The Partially implemented statements trace to the 12 gaps in `../00_company-facts.md` section 4 and to the P07 findings.

### 10.2 Control assessment status
The co-sourced IT audit firm assessed 35 controls (244 determination statements) from 2026-08-03 to 2026-08-21 (P07 `assessment-plan.md`, `assessment-results.csv`, and `poam.csv`). Weaknesses are tracked in the POA&M and reported quarterly to the Audit Committee.

## 11. Digital Identity Acceptance Statement
- **Workforce.** All workforce users authenticate through the identity provider with a password and app-based MFA with number matching, under conditional access that requires a managed device. Payments workstation users also present a hardware token to the Federal Reserve payment services. This is appropriate for the Moderate categorization.
- **Administrators.** Directory, identity provider, and cloud administrators use phishing-resistant hardware keys through PAM. Core security administrators and payments hub administrators do not yet, which is **not acceptable** for accounts that can create users or change wire limits (R-007; due 2027-03-31).
- **Business customers.** MFA is required, but 12% of business users still receive SMS codes and one-time codes can be relayed by a real-time phishing site. The FFIEC 2021 authentication guidance (supervisory guidance) expects MFA or controls of equivalent strength for high-risk transactions. The bank will move business users to app-based push or passkeys, and confirm every new wire beneficiary out of band, by 2027-03-31 (R-002). From 2026-10-01 until then, the Treasury Management Director's team reviews new-beneficiary reports each business day.
- **Consumers.** An SMS code is required only for sign-in from a new device. Step-up for adding external transfer recipients is planned with the business user change (R-016).
- **Respondent institutions.** Respondent users sign in to the correspondent portal through the customer identity service with app-based MFA. The 2 vendor-created generic administrator accounts found in P07 were disabled on 2026-08-14 (R-049).

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`); BIA (P05); cloud architecture and control map (P04); risk register (P01); gap analysis and roadmap (P03); policies and standards index (P06); assessment and POA&M (P07); incident runbooks (P08); SOC 2 readiness and vendor reviews (P09); AI governance assessment (P10).

## 13. Acronym List and Glossary
- **ACH:** Automated Clearing House
- **BEC:** business email compromise
- **COBP:** Core and Online Banking Platform
- **CUEC:** complementary user entity control (in a SOC report)
- **EDR:** endpoint detection and response
- **ISO:** Information Security Officer
- **MFA:** multi-factor authentication
- **MSSP:** managed security service provider
- **NPI:** nonpublic personal information (GLBA)
- **PAM:** privileged access management
- **POA&M:** plan of action and milestones
- **Respondent:** a smaller bank or credit union that uses the bank's correspondent payment services

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-07-24 | Draft from the BIA, risk assessment, and gap analysis | IT Risk and Compliance Manager |
| 1.0 | 2026-09-18 | Updated with P07 results; approved by the Chief Operating Officer | Information Security Officer |
