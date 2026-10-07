# System Security Plan (short form): Core Business SaaS Stack

**Organization:** Cris Santos Company (independent dam safety engineering consultant) | **Tier:** Sole Proprietorship | **Vertical:** Dams
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), all headings kept with short answers | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Core Business SaaS Stack (**CBSS**), identifier CSC-SYS-001.

## 2. System Overview
The CBSS is everything the business uses to inspect dams and deliver sealed safety reports for three clients: email and files, the engineering laptop, the phone and field tablet, accounting, the home office network, two AI tools, a USB backup drive, and paper in the home office. One person, the owner-engineer, uses and runs it. Components are SYS-01 to SYS-08 in `../00_company-facts.md` section 3. There is no server and no IaaS.

The CBSS also holds the **keys to client systems**: the owner's named accounts on Client A's document portal and vendor remote access gateway (view-only access to the HMI screens and historian for Client A's spillway gates and units) and on Client B's instrumentation data platform. The client systems are outside the boundary. The owner's credentials, devices, and network are inside it, and that is where most of the risk sits (P01 R-001).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | How it reaches the business |
|---|---|---|
| C-DAMS-R01 | FERC Security Program for Hydropower Projects, Rev. 3A | Not directly (it binds licensees). Passed down by Client A's agreement, CSCA-A (1) to (9) |
| CEII | 18 CFR 388.113(g)(1), (g)(5), and (h)(2) | Directly: Client A's written authorization and the owner's own non-disclosure agreement with FERC |
| Part 12D | 18 CFR 12.31(a), 12.34, 12.35(a), 12.36(g) and (h) | Shapes the Client A engagement: independence, the personal FERC approval, and a signed and sealed report |
| C-DAMS-R02 | 18 CFR 12.10 incident reporting | Not directly. Client A and Client B report; the consultant must tell them quickly (CSCA-A (7), GRS-B (3)) |
| Contract | Client B agreement GRS-B (1) to (3) | Confidentiality, MFA, 24-hour notice |
| State | Breach notification | Fla. Stat. 501.171 (only the field assistant's W-9) |
| Internal | Information Security Policy | POL-01 (P06) |

Not applicable: NERC CIP (C-DAMS-R03), because the business is not registered and neither client project is a BES generating resource; CIRCIA, which is proposed only.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the owner-engineer on 2026-08-31.
### 4.2 System Authorization Decision
No formal authorization applies to a private consultancy. Equivalent decision: the owner-engineer accepted continued operation on 2026-08-31, on condition that the High risks in P01 (R-001, R-005) are treated by their due dates and that no Client A gateway session runs from the administrator account after 2026-09-30.
### 4.3 System Operational Status
Operational. Planned changes: password manager and MFA everywhere (2026-09-15); standard daily account on the laptop (2026-09-30); encrypted backup drive (2026-09-30); separate business network (2026-10-31); hardware token for the signing certificate (2026-12-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner, security lead, incident commander, risk acceptor | Owner-engineer | Every role (POL-01 section 3) |
| Technical support | On-call IT technician (NDA since 2026-07-14) | Laptop, phone, and network help on request; no standing access; no access to client folders |
| Field support | Field assistant (1099) | Field days only; no system access; agreement pending (P01 R-011) |
| Service providers | Email and file suite provider; accounting SaaS provider | Operate inherited controls |
| Client system operators | Client A (portal and gateway); Client B (instrumentation platform) | Create, enable, monitor, and remove the owner's client accounts |

## 6. System Information Types and System Categorization
| Information type | C | I | A | Rationale |
|---|---|---|---|---|
| CEII and client engineering records (design drawings, inundation maps, prior Part 12D reports, instrument data) | Moderate | Moderate | Low | Disclosure could help someone plan an attack on a dam, which FERC protects against (388.113(c)(2)); wrong data could lead to a wrong safety finding; work can wait days (P05) |
| Client system access credentials and sessions (Client A gateway, portal; Client B platform) | Moderate | Moderate | Moderate | Misuse gives a view of gate and unit status at a high hazard dam; client must hear within 24 hours (P05 BP-01 MTD 24 h) |
| Sealed engineering reports and the signing certificate | Low | Moderate | Moderate | Reports become public filings once redacted; a forged or altered seal would undermine the report (18 CFR 12.36(h)) |
| **CBSS category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Security-sensitive material is kept out of the boundary on purpose.** Client A's Security Plan and Form 3 answers would be a High confidentiality information type: they describe how a high hazard dam is protected. A one-person business cannot run the High baseline. The design answer is that this material is **never stored in the CBSS**; it is read only inside Client A's portal or on site (CSCA-A (2); Rev. 3A 7.3). The June 2026 download (`00_company-facts.md` section 4, item 2) showed that the rule needs a technical backstop, so the owner asked Client A on 2026-07-22 to set the portal folder to view-only.

**Baseline:** SP 800-53B Moderate, tailored to 25 controls that carry the client and CEII duties for a one-person business (`control-implementation.csv`). Other Moderate controls are inherited from the SaaS providers (evidence: the suite provider's SOC 2 report, P09) or tailored out because they assume staff, servers, or a federal program.

## 7. Authorization Boundary Description
- **Inside:** the email and file suite tenant, the accounting SaaS account, the laptop, phone, and tablet, the home office network, the AI tool accounts, the USB backup drive, paper records, and the owner's credentials for the client-operated systems.
- **Outside (external services and client systems):** the SaaS providers' platforms, Client A's portal, gateway, HMI, and historian, Client B's instrumentation platform, the personal consumer photo cloud (to be removed from use), and the field assistant's phone.

Diagram: P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Party | Data | Agreement |
|---|---|---|
| Client A | Security-sensitive material (view only), CEII, gate and unit status (view only), draft and final reports | CSCA-A; FERC CEII authorization letter (2026-06-03) |
| Client B | Instrument readings, gate test records, drawings | GRS-B |
| FERC CEII Coordinator | Upstream project CEII (Client B study) | Non-disclosure agreement (granted 2026-03-10) |
| Client C | Inspection photos and report | Contract with a confidentiality clause |
| AI anomaly detection SaaS | Three years of Client B piezometer and seepage weir readings (uploaded 2026-05-19) | **Click-through terms only; no client consent (gap)** |
| Personal consumer photo cloud | Field photos, including security features | **No agreement; personal account (gap)** |
| Field assistant | Photos taken on a personal phone at Client B | **No agreement (gap)** |

## 9. System Component Inventory
| Component | Type | Owner |
|---|---|---|
| Email and file suite (SYS-01) | SaaS | Owner-engineer |
| Engineering laptop (SYS-02) | Endpoint | Owner-engineer |
| Mobile phone (SYS-03) | Personal endpoint | Owner-engineer |
| Field tablet (SYS-04) | Endpoint | Owner-engineer |
| Accounting SaaS (SYS-05) | SaaS | Owner-engineer |
| Client-operated accounts (SYS-06) | Credentials for client systems | Owner-engineer (accounts); clients (systems) |
| Home office network (SYS-07) | Shared home network | Owner-engineer |
| AI tools (SYS-08) | SaaS | Owner-engineer |
| USB backup drive | Removable media | Owner-engineer |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 25 controls:
- Implemented: 7
- Partially implemented: 15
- Planned: 3

Inheritance: 1 fully inherited (SC-8, TLS on every service), 11 hybrid (a provider or client runs the mechanism and the owner configures or uses it correctly), and 13 the owner's alone (AC-6(2), AC-11, AC-19, CP-2, IA-5, IA-5(2), IR-6, IR-8, MP-4, MP-6, PE-3, RA-3, SA-9).

**Key safeguards per CSF Function:**
| Function | Key safeguards |
|---|---|
| Govern | POL-01; client agreements and vendor list (SA-9); owner holds all roles |
| Identify | Risk assessment (RA-3); BIA (P05); client information register (MP-6, planned) |
| Protect | MFA (IA-2(1), IA-2(2) gaps); password manager (IA-5); standard daily account (AC-6(2)); encryption (SC-28, USB gap) |
| Detect | Own gateway session log and monthly sign-in review (AU-6, planned); Client A's weekly review |
| Respond | Gateway account compromise runbook (IR-8); 24-hour client notices (IR-6) |
| Recover | Suite version history (CP-9); peer engineer and sealed emergency sheet (CP-2) |

### 10.2 Control assessment status
Self-assessed 2026-07-20 to 2026-07-24 with the on-call IT technician. See P07.

## 11. Digital Identity Acceptance Statement
The email and file suite requires a password and an authenticator app code. Client A's portal and gateway require MFA that Client A enforces. The accounting SaaS and the Client B platform use a password only until MFA is turned on (2026-09-15). The signing certificate is protected only by the laptop login until it moves to a hardware token (2026-12-31). The owner accepts this level for a Moderate system on those dates.

## 12. Referenced Artifacts
Scenario facts, P01 risk register, P03 gap analysis, P04 SaaS control map, P05 BIA, P06 POL-01, P07 assessment and POA&M, P08 runbook and notification matrix, P09 SOC 2 self-check and vendor review, P10 AI use assessment.

## 13. Acronym List and Glossary
- **CBSS:** Core Business SaaS Stack
- **CEII:** Critical Energy/Electric Infrastructure Information (18 CFR 388.113)
- **CSCA-A:** Client A's Consultant Security and Confidentiality Agreement
- **GRS-B:** Client B's Gate Reliability Study Agreement
- **HMI:** human-machine interface (operator screens)
- **MFA:** multi-factor authentication
- **Part 12D:** 18 CFR Part 12 Subpart D, inspections by an independent consultant

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial short-form plan | Owner-engineer |
