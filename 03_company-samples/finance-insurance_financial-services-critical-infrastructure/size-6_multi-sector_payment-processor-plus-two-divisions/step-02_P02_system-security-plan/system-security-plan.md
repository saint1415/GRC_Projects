# System Security Plan: Payment Processing Platform (PPP)

**Organization:** Cris Santos Company Holdings, Inc. (Payment Processing division, Cris Santos Payments, LLC; common controls from corporate shared services) | **Tier:** Multi-Sector | **Vertical:** Financial Services
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-10

> **Why this system.** At this tier the SSP can cover one system per division or a shared corporate system. The group chose the **Payment Processing Platform**, the focus division's cardholder data environment, because it is the system the BIA ranks highest (P05: authorization and the token vault have 2-hour MTDs), it carries the group's top risks (P01 GR-01 and GR-02), and it is where the group's common controls meet a division's own regulators: the card brands and the four sponsor banks. The Software division describes its systems in its SOC 2 system description and gateway ROC, which inherit from the same common control catalog (`common-control-catalog.csv`). Merchant Consulting has no system of its own in the CDE; its users work inside this one.

## 1. System Name and Identifier
Payment Processing Platform (**PPP**), identifier CSCH-PP-CDE-01. It is made up of SYS-P1 to SYS-P6 in `../00_company-facts.md` section 3, with SYS-P7 as a connected-to system.

## 2. System Overview
The PPP authorizes, clears, and settles card payments for about 920,000 merchants: about 80 million authorizations a day, about $1.4 trillion a year, and about $3.8 billion in merchant funding files a day to four sponsor banks.

**Major components:**
- **Authorization and switching (SYS-P1):** terminal and API gateways and the card network interfaces, active-active in both group data centers
- **Token vault and payment HSM clusters (SYS-P2):** about 640 million unique PANs encrypted at rest; PIN translation; key hierarchy under dual control
- **Clearing, settlement, and merchant funding engine (SYS-P3):** daily clearing files and ACH funding files to Banks A to D
- **E-commerce payment API and hosted payment fields (SYS-P4):** provider A, two regions; embedded by merchants and by Software division storefronts
- **Merchant portal and virtual terminal (SYS-P5):** about 2.1 million merchant user accounts
- **Chargeback and dispute platform (SYS-P6):** provider A; used by the division's chargeback operations and by about 2,400 Merchant Consulting dispute analysts
- **Connected-to:** the fraud-detection scoring service (SYS-P7), which receives tokens and transaction features on the authorization path

About 8,900 workforce users reach the PPP (including the 2,400 consulting dispute analysts), with 410 privileged administrators and about 860 service identities.

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies to the PPP |
|---|---|---|---|
| PCI DSS | PCI DSS v4.0.1 as a service provider (contract, through the card brands and sponsor banks) | PCI SSC, June 2024 | The PPP is the division's assessed CDE. Level 1 service provider: annual ROC by a QSA, AOC, quarterly ASV scans |
| C-FINANCIAL-R01 | Bank service provider notification | 12 CFR 53.4 (Banks A and B); 225.303 (Bank C); 304.24 (Bank D) | Clearing, settlement, reconciliation, and funding file services are covered services under 12 U.S.C. 1867(c); a computer-security incident that disrupts them for 4 or more hours requires notice to the affected bank |
| FTC Safeguards | GLBA Safeguards Rule | 16 CFR Part 314 | The division is a financial institution (12 CFR 225.28(b)(14)); the PPP holds customer information of other institutions' customers (314.1(b)); FTC notice under 314.4(j) |
| Card brand rules | Visa What To Do If Compromised (and each brand's rules through the sponsor banks) | Brand rules (contract) | Compromise reporting clocks (P08) |
| C-FINANCIAL-R02 | Interagency Guidelines | 12 CFR 30 App. B and parallels | Apply to the sponsor banks; reach the PPP through the sponsor agreements' service provider terms (III.D) |
| N51-R08 | SEC cybersecurity disclosure | Reg S-K Item 106; Form 8-K Item 1.05 | A PPP incident may be material to the group (P08) |
| State law | Breach notification laws | Each state where affected individuals reside (Fla. Stat. 501.171 worked example) | For cardholder data the division is usually its merchants' third-party agent (501.171(6)) |
| Internal | Group policies POL-01 to POL-05 and the Payment Processing supplement | P06 | |

Not applicable: NYDFS Part 500, SEC Regulation SCI, NCUA 12 CFR 748.1(c) (see `../00_company-facts.md` section 1). CIRCIA (C-FINANCIAL-R06) is a proposed rule only and is tracked, not applied.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Payment Processing division CISO, the system owner (Payment Processing chief technology officer), and the Group CISO on 2026-09-10, after the board risk committee review.

### 4.2 System Authorization Decision
The group is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- **Decision:** authorized to operate with conditions, 2026-09-10, by the Group CISO and the Group Chief Risk Officer, with the division president as the PCI DSS accountable executive (PCI DSS 12.4.1).
- **Conditions:** (1) remove the bulk "case export" permission from dispute analysts by 2026-10-31 (POAM-003); (2) move Merchant Consulting users of SYS-P6 to SYS-G1 with phishing-resistant MFA by 2027-03-31, with SMS codes blocked for CDE access by 2026-12-31 (POAM-001, POAM-002); (3) record designated contacts for all four sponsor banks and extend the 4-hour determination procedure before the 2026 ROC fieldwork starts on 2026-11-02 (POAM-005).
- **Reauthorization:** annually, timed with the ROC, or after a significant change (PCI DSS 12.5.2.1).

### 4.3 System Operational Status
Operational. **Major modification planned:** the Merchant Consulting identity migration (2027-03-31) and PAN masking for dispute documents (2027-01-31). Both require a PCI DSS scope review under 12.5.2.1 and 12.5.3.

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Payment Processing chief technology officer | Accountable for the PPP and this SSP |
| Authorizing official equivalent | Group CISO with the Group Chief Risk Officer | Authorization decision; High risk acceptance |
| PCI DSS accountable executive | Payment Processing division president | Executive responsibility for the PCI DSS program (12.4.1) |
| Security lead | Payment Processing division CISO | Day-to-day PCI DSS program; quarterly reviews (12.4.2) |
| Qualified Individual | Group CISO (employed by the holding company, an affiliate) | 16 CFR 314.4(a); the division president is the senior member overseeing the Qualified Individual (314.4(a)(2)) |
| Data owner, settlement and funding | Head of settlement operations | Funding file integrity; retention |
| Sponsor bank and card brand liaison | Head of bank and network relationships | Notices under 53.4, 225.303, 304.24 and brand rules |
| Common control providers | Group identity director (SYS-G1), Group SOC director (SYS-G2), Group cloud platform director and Group Chief Information Officer (SYS-G3) | Operate inherited controls (`common-control-catalog.csv`) |
| Independent assessors | Group internal audit; external QSA firm | P07; annual ROC |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Payment and transaction data (cardholder data, authorization messages) | **High** | **High** | **High** | Disclosure of the vault's 640 million PANs would have a severe effect on cardholders, merchants, and the group (card brand, bank, FTC, state, and SEC consequences). Altered authorizations move money. Authorization is real time (P05 MTD 2 hours) |
| Settlement and funding (clearing files, ACH funding files) | Moderate | **High** | **High** | A wrong or late funding file harms merchants of a sponsor bank and triggers bank notices (P05 BP-PP04) |
| Merchant information (merchant owner and bank account data) | Moderate | Moderate | Moderate | Personal information of merchant owners; fraud risk if changed |
| Information security (keys, access policies, logs) | High | High | Moderate | Compromise would expose every segment |
| **PPP category (high-water mark)** | **High** | **High** | **High** | Overall **High** |

**Baseline:** the NIST SP 800-53B **High** baseline, tailored. The plan documents **170 controls** in `control-implementation.csv`:
- 166 from the High baseline;
- 2 from the privacy baseline that are program management controls (PM-9, PM-14);
- 2 program management controls not in any baseline (PM-1, PM-2), added because the PCI DSS accountable executive and the Qualified Individual are named there.

Other High-baseline controls are tailored out in the division tailoring register with a reason (for example, PE controls for buildings the division does not operate are inherited in full from the group data center facilities and cloud provider A).

## 7. Authorization Boundary Description
- **Inside:** SYS-P1 to SYS-P3 in the CDE segments of both group data centers; SYS-P4 to SYS-P6 in the division's provider A accounts; the PAM jump hosts that administer them.
- **Connected-to (in PCI DSS scope, outside the CDE):** SYS-P7 scoring service; the SYS-G1 identity platform; SYS-G2 logging and EDR; the administrative access path.
- **Outside, inherited (common control providers):** SYS-G1, SYS-G2, and SYS-G3 data centers, landing zone, and backup vault.
- **Outside, interconnected:** card networks, sponsor banks, the Software division gateway (SYS-S2), six unaffiliated processors (through SYS-S2 only), the group data platform (SYS-G4, tokens only), and the Merchant Consulting tenant (SYS-M1, federated identity).

The diagrams are in P04 `cloud-architecture.md` (the PPP subgraph).

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Card networks | Both | Authorization, clearing, and settlement messages | Network rules through the sponsor banks' memberships; dedicated encrypted links |
| Sponsor banks A to D | Outbound | Clearing reports and ACH funding files | Sponsor agreements (covered services under 12 U.S.C. 1867(c)) |
| Software division gateway (SYS-S2) | Inbound | Authorization requests (PAN) for about 70% of gateway traffic | Intercompany services agreement (2023). **No responsibility matrix** (POAM-009) |
| Software division storefronts (SYS-S1) | Inbound (browser) | Card data entered in the hosted payment fields | Hosted fields terms; storefront page security is the Software division's (P04) |
| Merchant Consulting (SYS-M1) | Identity federation; inbound documents | Dispute analyst sign-in; dispute evidence. **Gap:** evidence with PAN sits in consulting mailboxes first (POAM-007) | Intercompany services agreement (2025) naming consulting a service provider (16 CFR 314.2(r)) |
| Group data platform (SYS-G4) | Outbound | Tokens and transaction features only | Data platform standard; weekly PAN discovery |
| Fraud scoring (SYS-P7) | Both | Tokens and features; scores | Internal |
| Merchants and ISVs | Both | API calls, portal sessions, tokens | Merchant agreements |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| Authorization switch, terminal and API gateways | Software on group servers | Data centers 1 and 2 | Payment Processing chief technology officer |
| Card network interface processors | Network appliances and software | Data centers 1 and 2 | Group Chief Information Officer (links); division (software) |
| Token vault database | Clustered relational database | Data centers 1 and 2 | Payment Processing division CISO |
| Payment HSM clusters | FIPS 140-3 Level 3 hardware | Data centers 1 and 2 | Payment Processing division CISO (key custodians) |
| Settlement and funding engine | Software and database | Data centers 1 and 2 | Head of settlement operations |
| E-commerce API and hosted fields | Containers, API gateway, content delivery | Provider A (two regions) | Payment Processing chief technology officer |
| Merchant portal and virtual terminal | Web application | Provider A | Payment Processing chief technology officer |
| Dispute platform | Web application and document storage | Provider A | Head of settlement operations |
| PAM jump hosts | Hardened virtual machines | Data centers 1 and 2 | Group identity director |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv` (170 controls) and `common-control-catalog.csv` (130 group common and hybrid controls).

| Status | Controls |
|---|---|
| Implemented | 153 |
| Partially implemented | 17 |
| Planned | 0 |
| Not applicable | 0 |
| **Total** | **170** |

| Inheritance | Controls |
|---|---|
| Common/Inherited (from SYS-G1, SYS-G2, SYS-G3, group functions, or the facility providers) | 101 |
| Hybrid (group provides the mechanism; the division configures or operates part) | 29 |
| System-specific | 40 |

**The 17 partially implemented controls** cluster in three places:
- **Merchant Consulting users inside the CDE** (scenario gaps 1 and 2): AC-2, AC-2(12), AC-4, AC-6, AT-3, CM-8, IA-2(2), PL-2, PS-4, SI-4, SI-12.
- **Notification and cross-division response** (gaps 4 and 7): IR-3, IR-6, IR-8, CP-2.
- **Oversight of affiliates and models** (gap 6): SA-9, CA-7.

The PPP's own technical core (tokenization, keys, segmentation, active-active recovery, logging) is fully implemented. The gaps arrive with the people and services of other divisions.

### 10.2 Common control inheritance by division
The common control catalog lists 130 controls that corporate provides in full (101) or in part (29). Inheritance is **documented for the Payment Processing division** (PCI DSS responsibility matrix, 2025, and this plan) and **for the Software division** (its SOC 2 system description carves in the group services). It is **not documented for Merchant Consulting** (scenario gap 2). Until POAM-010 closes, the group cannot show which consulting safeguards are met by group controls and which still depend on SYS-M1. The P07 assessment found CA-2 and PL-2 statements other than satisfied for this reason.

### 10.3 Control assessment status
Common controls were assessed once, and PPP and division controls sampled, from 2026-07-01 to 2026-08-31 by group internal audit (P07 `assessment-results.csv` and `poam.csv`). The QSA's 2026 ROC fieldwork runs 2026-11-02 to 2026-12-11.

## 11. Digital Identity Acceptance Statement
- **Workforce users** authenticate through SYS-G1 with number-matching MFA; **administrators** use phishing-resistant hardware keys and just-in-time PAM elevation. This fits a High system reached by a large remote workforce.
- **Merchant Consulting users** authenticate through SYS-M1 with SMS one-time codes. This does not meet the group standard for CDE access and is accepted only until 2026-12-31 under the authorization conditions (POAM-002).
- **Merchant portal users** must use MFA for refund, funding account, and virtual terminal roles; other roles get risk-based sign-in analysis (PCI DSS 8.3.10.1).
- **Service identities** use workload identity or secrets held in the secret store, rotated at least every 90 days.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud architecture and control map (P04), group and division risk registers (P01), gap analyses and regulation-by-division matrix (P03), group policies and division supplements (P06), assessment and POA&M (P07), incident response runbook and notification matrix (P08), SOC readiness (P09), AI governance (P10), the 2025 ROC and AOC, and the PCI DSS responsibility matrix.

## 13. Acronym List and Glossary
- **AOC / ROC:** Attestation of Compliance / Report on Compliance (PCI DSS)
- **CDE:** cardholder data environment
- **Common control:** a control provided once by corporate and inherited by several systems
- **Covered services:** services subject to the Bank Service Company Act, 12 U.S.C. 1867(c), whose disruption can trigger a bank service provider notice
- **HSM:** hardware security module
- **ISV:** independent software vendor
- **PAN:** primary account number
- **PAM:** privileged access management
- **QSA:** Qualified Security Assessor

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-08-31 | Draft after P07 fieldwork | Payment Processing division CISO |
| 1.0 | 2026-09-10 | Approved with authorization conditions | Group CISO |
