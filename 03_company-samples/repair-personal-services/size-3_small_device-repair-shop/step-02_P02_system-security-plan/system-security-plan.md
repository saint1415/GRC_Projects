# System Security Plan: Service Ticketing and Point-of-Sale Platform (STPP)

**Organization:** Cris Santos Company, LLC (electronics and device repair service) | **Tier:** Small | **Vertical:** Other Services (except Public Administration)
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-04

## 1. System Name and Identifier
Service Ticketing and Point-of-Sale Platform (**STPP**), identifier CSC-SYS-001.

## 2. System Overview
The STPP runs every step of a repair: intake and consent at the counter, diagnostics and repair at the bench, data recovery and transfer at the Depot lab, payment, and release. It serves 60 workforce members at four Florida stores and the Depot, about 200 tickets a business day, and about 72,000 customer records.

**Major components:**
- **SYS-01:** a SaaS repair-shop ticketing and point-of-sale system (tickets, customer records, inventory, invoicing, status portal, text and email updates)
- **SYS-03:** an identity provider for single sign-on and MFA
- **SYS-05:** a public-cloud tenant for recovered-data delivery, the chatbot connector function, and the backup vault
- **SYS-06:** the Depot data recovery lab (storage array and 3 imaging workstations)
- **SYS-07:** 30 bench PCs and 6 bench laptops at the stores and Depot
- **SYS-09:** the store and Depot networks
- **SYS-10:** 22 office PCs and laptops and 10 counter tablets

**What the system protects beyond its own data.** Customer devices under repair connect to bench PCs for diagnostics and data transfer. The data on those devices (photos, messages, health and location data, saved credentials) is not stored in the STPP by design, but it passes through it. The plan therefore treats bench PCs, the lab, and the handling of devices as part of the system.

The cloud tenant is described by service category and is vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| N81-R01 | FTC Act Section 5: unfair or deceptive practices | 15 U.S.C. 45(a)(1), 45(n) |
| N81-R02 | State breach and data security laws; Florida as the worked example | Fla. Stat. 501.171(2)-(6), (8) |
| N81-R03 | PCI DSS v4.0.1 (contractual), validated on SAQ P2PE | Merchant agreement; SAQ P2PE v4.0.1 (October 2024) |
| N81-R04 | FTC Disposal Rule, for background check reports only | 16 CFR 682.3 |
| N81-BM | NIST CSF 2.0 (voluntary benchmark); NIST SP 800-88 Rev. 2 for sanitization | NIST CSWP 29; SP 800-88r2 (September 2025) |
| Contract | Manufacturer A and B authorized service provider agreements | Program agreements (fictional terms) |
| Internal | Security policies POL-01 to POL-05 | P06 |

Not applicable: the FTC Safeguards Rule (no credit extended), COPPA (not directed to children), and HIPAA (not a covered entity or business associate). Reasons are in P03 section 1.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the General Manager on 2026-09-04.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- The General Manager accepted operation of the STPP on 2026-09-04, with the conditions in the P07 POA&M.
- The majority owner approved the treatment plans for the four High risks in P01 on the same date. None of them was accepted without treatment.
### 4.3 System Operational Status
Operational. Major modifications planned: SYS-01 role redesign and passcode purge (due 2026-11-15), bench VLAN and EDR (due 2027-01-31), and backup account separation (due 2026-12-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | General Manager | Overall accountability; risk acceptance up to Moderate |
| Risk acceptor (authorizing official equivalent) | Majority owner | Acceptance of High and Very High risks |
| Information Security Lead | IT Manager | Day-to-day security; maintains this SSP and the risk register |
| Process owner (repair and devices) | Operations Manager | Technician access rules, sanitization, manufacturer program terms |
| Data custodian (recovered data) | Data Recovery Lead | Lab storage, retention, and deletion of recovered data |
| PCI DSS and contracts | Controller | Merchant agreement, SAQ P2PE, vendor contracts |
| Site custodians | Store Managers | Device custody, PIN pad inspections, counter access |

## 6. System Information Types and System Categorization
Information types were chosen as the closest matches in NIST SP 800-60 Vol. 2 Rev. 1 (customer services, collections and receivables, and personal identity and authentication), adapted to a private business. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Customer records and repair tickets (names, contact details, device identifiers, passcodes until purged) | Moderate | Moderate | Moderate | Disclosure of passcodes and account credentials enables account takeover and is a Florida breach; wrong records mean devices released to the wrong person; intake and release stop within one business day (P05 MTD 8 h) |
| Customer device content in custody (photos, messages, health, location, credentials) | Moderate | Moderate | Low | Serious, not catastrophic, harm to individuals if exposed; the company is not the system of record for it; recovery work can pause (P05 BP-05 MTD 72 h) |
| Payment and invoicing (truncated card data, business account ACH details) | Moderate | Moderate | Moderate | Card data stays inside P2PE terminals; ACH details enable payment fraud; payment and release share BP-03 |
| Workforce identities and background reports | Moderate | Low | Low | Consumer report information under the Disposal Rule; limited harm if briefly unavailable |
| **STPP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Why not High confidentiality.** Exposure of a customer's device content can be very personal, but for an individual customer it is serious rather than severe or catastrophic in FIPS 199 terms, and the company processes no data whose loss would threaten life or national interests. A bulk exposure of many customers is handled through the Moderate baseline plus the extra controls on technician access (AC-6, MP-7, PS-6) that this plan adds.

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 60-person repair company. This plan documents 61 controls: those that carry the company's legal and contractual duties and core security hygiene (see `control-implementation.csv`). Every other Moderate-baseline control is treated as follows:
- **Inherited** from the SaaS, cloud, and payment providers, as evidenced by their SOC 2 reports and the P2PE listing (P09).
- **Out of scope for this tier**, recorded as a tailoring decision, where the control's purpose applies mainly to federal systems. Examples: PM-series program controls beyond PM-2 and PM-9.

## 7. Authorization Boundary Description
- **Inside:** the SYS-01 tenant configuration, roles, and fields; the identity provider tenant; the cloud tenant (delivery storage, connector function, backup vault); the lab storage array and imaging workstations; 36 bench PCs and laptops; 22 office PCs and laptops; 10 counter tablets; the five site networks.
- **Outside (external services, interconnected):** the SYS-01 vendor's platform; the cloud provider's infrastructure; the payment processor's P2PE solution and terminals (SYS-02); the Manufacturer A and B portals and tools (SYS-08); the chatbot and diagnostics services (SYS-11); the recycler and courier.
- **Customer devices** are outside the boundary but connect to bench PCs inside it. The rules for handling them are part of this plan (AC-6, MP-6, MP-7).

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Payment processor (SYS-02) | Terminal to processor (encrypted in the device) | Card data; the STPP receives only approval and truncated number | Merchant agreement; P2PE Instruction Manual |
| Manufacturer A and B portals (SYS-08) | Bidirectional | Device serials, repair details, customer name for warranty claims | Program agreements |
| Chatbot service (SYS-11, AI-001) | Bidirectional through the connector function | Customer questions, ticket status, first name | **No data-use terms (gap)** |
| Diagnostics service (SYS-11, AI-002) | Outbound logs and photos, inbound suggestions | Device diagnostic logs, damage photos | **No data-use terms (gap)** |
| Business accounts | Outbound | Recovered data, invoices | Service contracts |
| Courier | Physical | Mail-in devices | Shipping account terms only (**gap**) |
| Certified electronics recycler | Physical | Recycling lots and retired equipment | Service contract with lot-level certificates (**gap**: no serial-level record) |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| SYS-01 ticketing and POS tenant | SaaS | Ticketing and POS vendor | General Manager |
| Identity provider tenant | SaaS | Identity vendor | IT Manager |
| Recovered-data delivery storage | Cloud object storage | Cloud tenant | Data Recovery Lead |
| Chatbot connector | Cloud serverless function | Cloud tenant | IT Manager |
| Backup vault | Cloud backup service | Cloud tenant (same account, **gap**) | IT Manager |
| Lab storage array and 3 imaging workstations | On-premises | Depot lab | Data Recovery Lead |
| Bench PCs (30) and bench laptops (6) | Endpoint | Stores and Depot | Operations Manager |
| Office PCs and laptops (22), counter tablets (10) | Endpoint | Stores and Depot | IT Manager |
| Firewalls (5), switches, Wi-Fi | Network | Each site | IT Manager |
| P2PE terminals (12) | Payment device (processor-owned solution) | Counters; 2 spares | Store Managers |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 61 controls:
- Implemented: 15
- Partially implemented: 35
- Planned: 11

### 10.2 Control assessment status
Assessed 2026-08-10 to 2026-08-14. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
Workforce users with named accounts authenticate through the identity provider with a password and an authenticator app. Cloud and identity administrators use number-matching MFA. **Shared counter logins at Stores C and D do not meet this statement** and are being replaced by named accounts with badge-plus-PIN sign-in and MFA (POAM-007).

Customers use the status portal with a ticket number and a one-time code sent to the phone on file. At device release, customers must show photo ID or give a one-time code (planned; P01 R-010).

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **AOC:** attestation of compliance (PCI DSS)
- **EDR:** endpoint detection and response
- **MFA:** multi-factor authentication
- **P2PE:** point-to-point encryption
- **PIM:** P2PE Instruction Manual
- **POA&M:** plan of action and milestones
- **SAQ:** self-assessment questionnaire
- **STPP:** Service Ticketing and Point-of-Sale Platform

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-09-04 | Initial plan | IT Manager |
