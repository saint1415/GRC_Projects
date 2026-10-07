# System Security Plan (short form): Shop Business Systems

**Organization:** Cris Santos Company (owner-operated CNC machine shop) | **Tier:** Sole Proprietorship | **Vertical:** Manufacturing
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), all headings kept with short answers | **Version:** 1.0, 2026-09-04

## 1. System Name and Identifier
Shop Business Systems (**SBS**), identifier CSC-SYS-001.

## 2. System Overview
The SBS is everything the shop uses to quote, program, machine, inspect, ship, and bill small lots of precision parts for about 12 business customers. One person, the owner-machinist, uses and runs it. Components are SYS-01 to SYS-06 and SYS-09 in `../00_company-facts.md` section 3: a business email and file plan (SaaS), an accounting SaaS, one laptop with CAD/CAM software, a phone, two CNC machine controllers, the shop network, and the shop website. There is no server and no IaaS. Most back-end safeguards are **inherited from the SaaS providers**; the owner is responsible for identities, data handling, devices, the shop network, and contracts (P04).

The SBS is also the shop's **covered contractor information system** under FAR 52.204-21, because aerospace drawings (FCI) are received by email, stored in the file plan, opened on the laptop, and turned into programs for the VMC. For CMMC Level 1 scoping, the CNC controllers are **specialized assets** (operational technology): they are not assessed at Level 1 (32 CFR 170.19(b)(2)(ii)), but the shop still protects them because they hold programs made from customer drawings.

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it reaches the shop |
|---|---|---|---|
| N31-33-R02 | CMMC Level 1 (Self) | 32 CFR 170.14(c), 170.15, 170.22; DFARS 252.204-7021 | Flowdown from the aerospace customer (supplier letter 2026-06-15) |
| C-DIB-R04 | FAR 52.204-21 Basic Safeguarding | 48 CFR 52.204-21(b)(1)(i)-(xv), (c) | Flowdown on aerospace POs since 2025-03 |
| Contract | FAR 52.204-25 (Section 889) | 48 CFR 52.204-25(d)-(e) | Flowdown on aerospace POs; reporting only |
| Contract | OEM supplier quality agreements and NDAs | QMSR purchasing controls, flowed by contract (21 CFR 820.10; ISO 13485 clause 7.4) | Direct contract terms |
| N31-33-R03, N31-33-R04 | ITAR and EAR | 22 CFR 122.1; 15 CFR Parts 730-774 | Not triggered today; intake screening rule in POL-01 8.3 |
| Benchmark | NIST CSF 2.0 and Small Business Quick-Start Guide | NIST CSWP 29; NIST SP 1300 | Voluntary benchmark for the whole business |
| Internal | Information Security Policy | POL-01 (P06) | |

Not applicable: FD&C Act section 524B (N31-33-R05; the shop makes no devices and submits nothing to FDA), the QMSR directly (21 CFR 820.1(a)(2) excludes component manufacturers), DFARS 252.204-7012 and CMMC Level 2 (no CUI), and HIPAA (no PHI). Reasons are in P03.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the owner-machinist on 2026-09-04.
### 4.2 System Authorization Decision
No formal authorization applies to a private business. Equivalent decision: the owner accepted continued operation on 2026-09-04, on condition that the High risks in P01 (R-001, R-003, R-006) are treated by their due dates and that every FAR 52.204-21 requirement is met before the CMMC Level 1 affirmation (target 2026-11-30), because Level 1 allows no POA&M (32 CFR 170.15(a)(1)).
### 4.3 System Operational Status
Operational. Planned changes: separate network for the VMC and laptop (2026-10-31); separate backup (2026-10-31); read-only released-program folder (2026-12-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner, security lead, risk acceptor, CMMC affirming official | Owner-machinist | Every role. POL-01 section 3 designates it in writing |
| Technical support | On-call IT technician (NDA since 2026-08-07) | Laptop, router, and machine network help on request; no standing access |
| Service providers | Productivity suite provider, accounting SaaS provider | Operate inherited controls |

## 6. System Information Types and System Categorization
| Information type | C | I | A | Rationale |
|---|---|---|---|---|
| Customer technical data (drawings, models; OEM confidential and aerospace FCI) | Moderate | Moderate | Low | Disclosure breaks NDAs and FAR 52.204-21; a wrong drawing revision makes wrong parts; drawings can be resent by customers |
| Production data (CAM files and NC programs) | Moderate | Moderate | Moderate | Derived from customer drawings; an altered program can make nonconforming OEM parts or crash a machine; loss beyond three days misses ship dates (P05 MTD 72 h) |
| Quality records (inspection reports, certificates, traceability) | Low | Moderate | Moderate | OEMs rely on them; SQAs require 10-year retention (P05 BP-02) |
| Financial (invoices, payments) | Low | Moderate | Low | Payment redirection is the main risk; invoicing can wait a week (P05 MTD 168 h) |
| **SBS category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** SP 800-53B Moderate, tailored to 24 controls (`control-implementation.csv`) that carry the 15 FAR 52.204-21 requirements, the OEM contract terms, and the CSF 2.0 benchmark for a one-person shop. Other Moderate controls are inherited from the SaaS providers (evidence: the productivity suite provider's SOC 2 report, P09) or tailored out because they assume staff, servers, or a federal system.

## 7. Authorization Boundary Description
- **Inside:** the productivity suite account and its settings, the accounting SaaS account settings and users, the laptop, the phone, the router and shop Wi-Fi, the website account, the VMC and turning center controllers (as specialized assets), USB sticks, and paper travelers and records in the bay.
- **Outside (external services):** the SaaS providers' platforms, customer portals (customer-owned), the AI assistant (consumer service), outside processors, the calibration lab, and the machine service technician's laptop.

Diagram: P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Party | Data | Agreement |
|---|---|---|
| Medical OEMs (3) | Drawings, models, POs; first article reports and certificates back | NDAs; SQAs (2) or PO quality clauses (1) |
| Aerospace customer | Drawings (FCI) through its portal and by email; POs | PO terms with FAR 52.204-21, FAR 52.204-25, and (from the next award) DFARS 252.204-7021 Level 1 (Self) |
| Outside processors | POs, spec callouts, and sometimes full drawings | **PO only; no confidentiality or FAR 52.204-21 flowdown (gap)** |
| Bookkeeper | Invoices, payments (no drawings) | Engagement letter |
| IT technician | Laptop and network access on request | NDA (2026-08-07) |
| AI assistant | Pasted drawing notes, one OEM drawing, G-code | **Consumer terms only (gap; P10)** |

## 9. System Component Inventory
| Component | Type | Owner |
|---|---|---|
| Productivity suite account (SYS-01) | SaaS | Owner-machinist |
| Accounting SaaS account (SYS-02) | SaaS | Owner-machinist |
| Shop laptop with CAD/CAM (SYS-03) | Endpoint | Owner-machinist |
| Mobile phone (SYS-04) | Personal endpoint | Owner-machinist |
| VMC and turning center controllers (SYS-05) | Operational technology (specialized assets) | Owner-machinist |
| Router and shop Wi-Fi (SYS-06) | Network | Owner-machinist (router supplied by the internet provider) |
| Website account (SYS-09) | SaaS | Owner-machinist |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 24 controls:
- Implemented: 4
- Partially implemented: 15
- Planned: 5

Inheritance: 12 hybrid (a provider operates the mechanism and the owner configures or uses it) and 12 the owner's alone. None is fully inherited, because at the SaaS layer the customer always keeps identities, data, and devices (P04).

**Key safeguards per CSF Function:**
| Function | Key safeguards |
|---|---|
| Govern | POL-01; NDAs and contract terms (SA-9); owner holds all roles |
| Identify | Risk assessment (RA-3); BIA (P05); drawing intake screening (POL-01 8.3) |
| Protect | Unique accounts (IA-2); MFA (IA-2(1), gap on accounting); disk encryption (SC-28); network separation (SC-7, gap); released-program integrity (SI-7, planned) |
| Detect | Provider sign-in logs; monthly review (AU-6, planned); antivirus alerts (SI-3) |
| Respond | Ransomware runbook with customer notice terms (IR-8) |
| Recover | File versions (CP-9, partial); separate backup (planned); emergency access sheet (CP-2) |

### 10.2 Control assessment status
Self-assessed 2026-08-10 to 2026-08-14 with the IT technician; tests on 2026-08-12. See P07.

## 11. Digital Identity Acceptance Statement
The productivity suite requires a password and a text-message code, which is acceptable today for a Moderate system but weaker than an authenticator app; the owner moves to app-based codes with the accounting change (2026-09-30). The accounting SaaS uses a password only until then. The aerospace portal's identity controls belong to the customer and sit outside this boundary. The laptop uses a local password; a separate standard user account for daily work is planned (POL-01 7.2).

## 12. Referenced Artifacts
Scenario facts, P01 risk register, P03 gap analysis, P04 SaaS control map, P05 BIA, P06 POL-01, P07 assessment and POA&M, P08 runbook, P09 SOC 2 self-check and vendor review, P10 AI use assessment.

## 13. Acronym List and Glossary
- **CAM:** computer-aided manufacturing (software that turns a model into a CNC program)
- **CMMC:** Cybersecurity Maturity Model Certification
- **FCI:** Federal contract information (FAR 52.204-21(a))
- **NC program:** the numerical control program (G-code) a CNC machine runs
- **OEM:** original equipment manufacturer (here, the medical device makers)
- **SPRS:** Supplier Performance Risk System
- **SQA:** supplier quality agreement
- **VMC:** vertical machining center

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-09-04 | Initial short-form plan | Owner-machinist |
