# System Security Plan (short form): Core Business Systems

**Organization:** Cris Santos Company (independent utility engineering consultant) | **Tier:** Sole Proprietorship | **Vertical:** Utilities
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), all headings kept with short answers | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Core Business Systems (**CBS**), identifier CSC-SYS-001. The name follows the scenario registry's "core business SaaS stack (email, files, client and billing records)", with the laptop, phone, and USB drives added because they carry client security information.

## 2. System Overview
The CBS is everything the owner-engineer uses to deliver protection and control engineering, field support, and planning studies to four utility clients: email and files, the engineering laptop and its settings and analysis software, the phone, USB drives for settings files, the accounting SaaS, the home office network, two AI tools, and the owner's named accounts on the Client A portal and the Client B remote access gateway. Components are SYS-01 to SYS-08 in `../00_company-facts.md` section 3. There is no server, no IaaS, and no operational technology owned by the business. The business **touches client OT** in two ways: its laptop connects to Client B relays as a Transient Cyber Asset managed by a party other than the Responsible Entity, and the owner has vendor electronic remote access to Client B through Client B's gateway.

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | How it reaches the business |
|---|---|---|
| N22-R01 | NERC CIP Reliability Standards | **By contract only.** Client A (medium impact) passes down CIP-004-7 R6, CIP-011-3 R1, and CIP-013-2 R1.2 items through SSA-A (1) to (8). Client B (low impact) passes down CIP-003-9 Attachment 1 Sections 5 and 6 through VAA-B (1) to (5). See P03 |
| CEII NDA | 18 CFR 388.113(g)(5) and (h)(2) | Signed with FERC for the Client D study (2026-02-10) |
| State | Breach notification | Fla. Stat. 501.171 (narrow: one subcontractor W-9) |
| Contract | Client C confidentiality clause | No sharing of Client C data without written consent (P10) |
| Internal | Information Security Policy | POL-01 (P06) |

Not applicable: N22-R02 (TSA pipeline directive), N22-R03 (NRC 10 CFR 73.54), N22-R04 (SDWA section 1433), NERC EOP-004-4, and Form DOE-417. The business is not a registered entity, a pipeline, a reactor licensee, a water system, or an electric utility (P03 G-001 to G-005).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the owner-engineer on 2026-08-31.
### 4.2 System Authorization Decision
No formal authorization applies to a private consultancy. Equivalent decision: the owner accepted continued operation on 2026-08-31, on condition that the High risks in P01 (R-001, R-002, R-003) are treated by their due dates, and that no Client A BCSI is shared with anyone until Client A authorizes that person in writing.
### 4.3 System Operational Status
Operational. Planned changes: password manager and app-based MFA (2026-09-15); standard daily laptop account, dedicated USB drives, and the drafter access agreement (2026-09-30); separate business network and client information register (2026-10-31); a dedicated field laptop for client relay connections (2026-12-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner, security lead, incident commander, risk acceptor | Owner-engineer | Every role. Independence is limited; see P07 |
| Technical support | On-call IT technician (NDA since 2026-07-17) | Laptop, phone, and network help on request; no access to client folders |
| Subcontractor | CAD drafting subcontractor | Drawing updates from markups; no client security information without written client approval (POL-01 6.3) |
| Service providers | Email and file suite provider; accounting SaaS provider | Operate inherited controls (P04) |
| Client operators | Client A (portal); Client B (gateway) | Operate the access controls on their own systems |

## 6. System Information Types and System Categorization
| Information type (SP 800-60) | C | I | A | Rationale |
|---|---|---|---|---|
| Client critical infrastructure information (Client A BCSI, Client B settings and event records, CEII) | Moderate | Moderate | Low | Disclosure could help an attacker plan against a client's protection systems and breaches the client terms; a tampered setting could cause a misoperation, but each client reviews and tests settings before use; work can wait a day or more (P05) |
| Client communications and incident notices | Low | Moderate | Moderate | Mostly routine; a missed 24-hour notice breaks SSA-A (5) and VAA-B (5) (P05 MTD 24 h) |
| Business administration (billing, contracts) | Low | Moderate | Low | A changed bank detail on an invoice diverts payments (P01 R-008) |
| **CBS category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** SP 800-53B Moderate, tailored to 30 controls that carry the clients' flow-down terms for a one-person business (`control-implementation.csv`). Other Moderate controls are either inherited from the SaaS providers (evidence: the email suite provider's SOC 2 report, P09) or tailored out because they assume staff, servers, or a network the business does not run. AC-5, AU-9, CM-3, and CA-2(1) assume a second person but are kept with compensating controls (see `control-implementation.csv`).

## 7. Authorization Boundary Description
- **Inside:** the email and file suite tenant and its sharing settings, the accounting SaaS account, the laptop, the phone, the USB drives, the home office network as used for business, the owner's accounts and credentials for the Client A portal and the Client B gateway, the two AI tool accounts, and paper in the home office.
- **Outside (external services):** the SaaS providers' platforms, Client A's portal and BES Cyber Systems, Client B's gateway, network, and relays, the drafting subcontractor's computer, the personal consumer photo cloud, and FERC.

Diagram: P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Party | Data | Agreement |
|---|---|---|
| Client A | Relay settings, drawings, studies (BCSI) | MSA with SSA-A; transfer only through the Client A portal |
| Client B | Settings files, relay event records | VAA-B; gateway sessions enabled by Client B; files through Client B's file exchange |
| Client C | Feeder load data; planning study | Confidentiality clause; **data uploaded to the AI forecasting SaaS without consent (gap, P10)** |
| Client D and FERC | Transmission planning models (CEII); study | FERC CEII NDA; subcontract with Client D |
| Drafting subcontractor | Drawing markups | General subcontract; **no access agreement (gap)**; Client A BCSI was exposed through the shared folder until 2026-07-21 |
| Personal consumer photo cloud | Photos of client control houses | **No business terms (gap)** |

## 9. System Component Inventory
| Component | Type | Owner |
|---|---|---|
| Email and file suite tenant (SYS-01) | SaaS | Owner-engineer |
| Engineering laptop (SYS-02) | Endpoint; also a Transient Cyber Asset at Client B | Owner-engineer |
| Mobile phone (SYS-03) | Personal endpoint | Owner-engineer |
| Accounting SaaS (SYS-04) | SaaS | Owner-engineer |
| USB drives, 3 (SYS-05) | Removable media | Owner-engineer |
| Client A portal and Client B gateway accounts (SYS-06) | Client-operated | Clients (accounts named to the owner) |
| Home office network (SYS-07) | ISP router and Wi-Fi | Owner-engineer |
| AI forecasting SaaS and consumer chatbot (SYS-08) | SaaS | Owner-engineer |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 30 controls:
- Implemented: 8
- Partially implemented: 17
- Planned: 5

Inheritance: 13 hybrid (a provider or client operates the mechanism and the owner configures or uses it correctly) and 17 the owner's alone. None is fully inherited: even where a provider or client runs the control, the owner still holds the credentials and decides where client data goes.

**Key safeguards per CSF Function:**
| Function | Key safeguards |
|---|---|
| Govern | POL-01; client terms tracked (SA-9, AC-20); drafter access agreement (PS-6, planned) |
| Identify | Risk assessment (RA-3); BIA (P05); client information register (CM-8, planned) |
| Protect | Laptop encryption (SC-28); MFA (IA-2(1), IA-2(2), partial); least privilege (AC-6, planned); USB control (MP-7) |
| Detect | Monthly sign-in and sharing review (AU-6, planned); antivirus (SI-3) |
| Respond | Client notice procedure (IR-6, planned); runbook (IR-8) |
| Recover | File version history (CP-9, partial); standby engineer and sealed codes (CP-2) |

### 10.2 Control assessment status
Self-assessed 2026-07-20 to 2026-07-24 with the IT technician. See P07.

## 11. Digital Identity Acceptance Statement
Client A and Client B enforce MFA on their own systems. The email suite uses SMS codes, which do not resist phishing relays; given the BCSI and CEII it holds, the owner moves it to an authenticator app or security key by 2026-09-15 (POL-01 7.2). The accounting SaaS uses a password only until the same date.

## 12. Referenced Artifacts
Scenario facts, P01 risk register, P03 gap analysis, P04 SaaS control map, P05 BIA, P06 POL-01, P07 assessment and POA&M, P08 runbook and notification matrix, P09 SOC 2 self-check and vendor review, P10 AI use assessment.

## 13. Acronym List and Glossary
- **BCSI:** BES Cyber System Information (NERC Glossary; protected under CIP-011)
- **BES:** Bulk Electric System
- **CEII:** Critical Energy/Electric Infrastructure Information (18 CFR 388.113)
- **MFA:** multi-factor authentication
- **SSA-A / VAA-B:** Client A Supplier Security Addendum / Client B Vendor Access Agreement
- **Transient Cyber Asset:** a portable device connected to a client's BES Cyber System for a short time (NERC Glossary)

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial short-form plan | Owner-engineer |
