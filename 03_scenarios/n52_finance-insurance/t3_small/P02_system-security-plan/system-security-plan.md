# System Security Plan: Wire and Digital Banking Platform (WDBP)

**Organization:** Cris Santos Bank, N.A. (community commercial bank) | **Tier:** Small | **Vertical:** Finance and Insurance
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Wire and Digital Banking Platform (**WDBP**), identifier CSB-SYS-002.

## 2. System Overview
The WDBP is how customers and staff move money. It supports consumer and business online and mobile banking, business wire and ACH initiation, branch-originated wire requests, and wire-room processing to the Federal Reserve payment services. It handles about 35 outgoing wires per business day (about $4 million per day on average) and ACH files for 140 business customers. About 9,000 consumer and 1,400 business users are enrolled.

**Major components:**
- **SYS-02:** online and mobile banking, hosted by a digital banking provider. The bank manages user entitlements, limits, and security settings in the provider's admin console.
- **SYS-03:** the wire transfer and ACH origination platform, hosted by a payments service provider. The bank manages roles, approval thresholds, beneficiary templates, and two dedicated payments workstations in the wire room.
- **SYS-05:** the identity provider, which gives workforce users single sign-on and MFA to the admin console and the wire platform.
- **SYS-07 (part):** 5 wire-room PCs, the 2 payments workstations, and the branch endpoints used to take wire requests.

The system is a mix of **bank-managed configuration** and **vendor-hosted services**. Section 7 draws the line.

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| N52-R01 | Gramm-Leach-Bliley Act, section 501(b) safeguards | 15 U.S.C. 6801(b) |
| N52-R02 | Interagency Guidelines Establishing Information Security Standards (OCC) | 12 CFR Part 30, Appendix B, and Supplement A (response programs and customer notice) |
| Rule | Computer-Security Incident Notification | 12 CFR Part 53 (bank); 12 CFR 225 Subpart N (holding company) |
| Rule | Suspicious activity reports | 12 CFR 21.11; 31 CFR 1020.320 |
| State | Funds-transfer liability and security procedures (UCC Article 4A) | Fla. Stat. 670.202 |
| State | Florida Information Protection Act (breach notification) | Fla. Stat. 501.171 |
| Internal | Security policies POL-01 to POL-05 | P06 |

Not applicable: the FTC Safeguards Rule (N52-R03), NYDFS Part 500 (N52-R04), SEC Regulation S-P and S-ID (N52-R05, N52-R06), NAIC Model #668 (N52-R07), and SEC cybersecurity disclosure (N52-R08). The reasons are in `../scenario-facts.md` section 1. Consumer wire transfers sent through Fedwire are excluded from Regulation E's definition of electronic fund transfer (12 CFR 1005.3(c)(3)), so Regulation E error resolution does not govern the wire part of this system. It does govern consumer ACH and online bill payments, which are outside this plan's security scope.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the President and CEO on 2026-08-31, after review by the Audit and Risk Committee on 2026-08-27.
### 4.2 System Authorization Decision
The bank is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- The COO accepted continued operation of the WDBP on 2026-08-31, with the conditions in the P07 POA&M.
- The President and CEO accepted the High risks R-001 and R-002 (P01) until their treatment dates, and reported the acceptance to the Audit and Risk Committee.
### 4.3 System Operational Status
Operational. Major modification planned: required customer MFA and out-of-band confirmation of new wire beneficiaries (P01 R-002), due 2026-12-31 for business users and 2027-03-31 for consumer users.

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Chief Operating Officer | Overall accountability; risk acceptance up to Moderate |
| Risk acceptor (authorizing official equivalent) | President and CEO | Acceptance of High risks, reported to the Audit and Risk Committee |
| Information Security Officer | IT Manager | Day-to-day security; designated by the board |
| Business process owners | Deposit Operations Manager (wires); Treasury Management Officer (business online banking) | Callback standard, limits, customer agreements |
| Fraud and SAR decisions | BSA/AML Officer | SARs, law enforcement liaison |
| Operations support | Digital banking provider; payments service provider; MSSP | Hosting, application security, 24x7 alert monitoring |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Payments and collections (wire and ACH instructions) | Moderate | Moderate | Moderate | A fraudulent or altered wire causes direct financial loss. Per-wire limits, dual control, and the financial institution bond keep the worst single loss well under 5% of capital, so the effect is serious rather than severe. Wires can be sent by the alternate procedure for one business day (P05 MTD 8 h) |
| Customer account and identity information (NPI, credentials) | Moderate | Moderate | Low | Disclosure enables account takeover and triggers customer notice analysis under Supplement A |
| Workforce identities | Moderate | Low | Low | Account data; limited harm if unavailable |
| **WDBP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 120-person community bank. The plan documents the 62 controls that implement the Interagency Guidelines for this system (see `control-implementation.csv`). Every other Moderate-baseline control is treated as follows:
- **Inherited** from the digital banking provider, the payments service provider, and the identity provider, as evidenced by their SOC reports (P09).
- **Out of scope for this tier**, recorded as a tailoring decision, where the control's purpose applies only to federal systems. Examples: PM-series program-level controls beyond PM-1, PM-2, and PM-9.

## 7. Authorization Boundary Description
The boundary contains bank-managed components and the bank's configuration of vendor services:
- **Inside:** the admin console configuration (user entitlements, limits, security settings), the wire platform configuration (roles, approval thresholds, beneficiary templates, callback fields), the identity provider tenant as it protects both, the 2 payments workstations and 5 wire-room PCs, the branch endpoints used to take and key wire requests, and the isolated payments network segment.
- **Outside (external services, interconnected):** the digital banking provider's platform, the payments service provider's platform, the core banking system (SYS-01) at the core processor, the Federal Reserve payment services, and the MSSP.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Core banking system (SYS-01) at the core processor | Bidirectional | Balances, holds, postings, customer profile | Core processor contract (no incident notice time frame; **gap**) |
| Federal Reserve payment services | Outbound and inbound | Wire messages; ACH files | Federal Reserve operating circulars and the bank's access agreement |
| Business customers (online banking) | Inbound | Wire and ACH requests | Treasury management agreement with the agreed security procedure (callback and dual approval) |
| Branches (email, phone, in person) | Inbound | Wire requests | Funds transfer agreement; callback standard (**inconsistently applied; gap**) |
| MSSP | Outbound | Endpoint and firewall alerts | MSSP contract |
| Digital banking provider to core | Bidirectional | Account data, transfers | Provider and core processor interface agreement |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| Online banking admin console configuration | SaaS configuration | Digital banking provider | Treasury Management Officer |
| Wire and ACH platform configuration | SaaS configuration | Payments service provider | Deposit Operations Manager |
| Identity provider tenant | SaaS | Identity vendor | IT Manager |
| Payments workstations (2) and hardware tokens | Endpoint | Wire room, main office | Deposit Operations Manager |
| Wire-room PCs (5) | Endpoint | Wire room, main office | IT Manager |
| Branch endpoints used for wire requests (about 24) | Endpoint | Six branches | Branch Managers |
| Payments network segment and branch firewalls | Network | Main office and branches | IT Manager |
| Spare pre-built payments workstation | Endpoint (standby) | Branch 4 | IT Manager |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 62 controls:
- Implemented: 27
- Partially implemented: 30
- Planned: 5
- Not applicable: 0

By inheritance: 42 system-specific, 12 hybrid, 8 common (inherited from a provider).

### 10.2 Control assessment status
Assessed 2026-08-03 to 2026-08-07. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
**Workforce.** All workforce users authenticate through the identity provider with a password and a second factor (an authenticator app, or a hardware key for administrators). Payments workstation users also present a hardware token to the Federal Reserve payment services. This is appropriate for the Moderate categorization. Number matching for push approvals is being enforced by 2026-11-30 (R-013).

**Customers.** Customers use the digital banking provider's logon with device recognition. MFA is optional today, which is **not acceptable** for business users who can add beneficiaries and send wires. The bank will require MFA for all business users by 2026-12-31 and all consumer users by 2027-03-31, and will require out-of-band confirmation of every new wire beneficiary (R-002). Until then, the Treasury Management Officer reviews new-beneficiary reports daily.

## 12. Referenced Artifacts
Scenario facts (`../scenario-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC report review (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **ACH:** Automated Clearing House
- **BEC:** business email compromise
- **CUEC:** complementary user entity control
- **ISO:** Information Security Officer
- **MFA:** multi-factor authentication
- **MSSP:** managed security service provider
- **NPI:** nonpublic personal information (GLBA)
- **POA&M:** plan of action and milestones
- **WDBP:** Wire and Digital Banking Platform

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan | IT Manager (ISO) |
