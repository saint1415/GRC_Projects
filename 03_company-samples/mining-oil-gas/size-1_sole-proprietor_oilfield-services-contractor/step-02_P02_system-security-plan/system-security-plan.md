# System Security Plan (short form): Field Service Business Systems

**Organization:** Cris Santos Company (owner-operated oilfield services contractor) | **Tier:** Sole Proprietorship | **Vertical:** Mining, Quarrying, and Oil and Gas Extraction
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), all headings kept with short answers | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Field Service Business Systems (**FSBS**), identifier CSC-SYS-001.

## 2. System Overview
The FSBS is everything the owner-operator uses to run contract pumping rounds on 34 wells and automation service on about 60 customer field devices: the business email and file account (SYS-01), the accounting service (SYS-02), the rugged field laptop with configuration software (SYS-03), the smartphone (SYS-04), USB drives and programming cables (SYS-06), the home office network (SYS-07), the dynamometer analysis service (SYS-08), and the owner's credentials and client software for the customer remote access paths (SYS-05). Component details are in `../00_company-facts.md` section 3. There is no server and no IaaS. One person uses and runs it.

**Why this small system matters to critical infrastructure:** the laptop is both a business computer and an OT engineering workstation for two producers. It holds their control programs, network details, and passwords, and it connects to their controllers by cable and remotely. The customers' SCADA and field devices are outside this boundary, but the FSBS is a path into them.

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Applies? |
|---|---|---|
| N21-BM | NIST CSF 2.0 with NIST SP 800-82 Rev. 3 (voluntary benchmark, P03) | Chosen benchmark; not binding |
| MSA-A | Customer A MSA security schedule, items (1) to (8) | **Yes, by contract** (the main binding security duty) |
| Fla. Stat. 501.171 | Data security, breach notice, disposal (the statute names a sole proprietorship as a covered entity) | Yes, for 2 helpers' W-9 data |
| N21-R01 | USCG Marine Transportation System cyber rule, 33 CFR 101 Subpart F | No: no vessel, MTSA facility, or OCS facility (101.605) |
| N21-R02 | TSA SD Pipeline-2021-02G | No: the owner is not a TSA-notified pipeline owner or operator |
| N21-R03 | CIRCIA, proposed 6 CFR Part 226 | Proposed only; tracked in P03 |
| Internal | Information Security Policy | POL-01 (P06) |

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the owner-operator on 2026-08-31.
### 4.2 System Authorization Decision
No formal authorization applies to a private contractor. Equivalent decision: the owner-operator accepted continued operation on 2026-08-31, on condition that the four High risks in P01 (R-001, R-002, R-003, R-008) are treated by their due dates. Customer A's annual questionnaire (due 2026-09-30) is answered from this plan, P03, and P09.
### 4.3 System Operational Status
Operational. Planned changes: standard daily laptop account and password manager (2026-09-30); offline program backups (2026-10-31); new home router and separate network for the laptop (2026-11-30).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner, security lead, risk acceptor, incident commander | Owner-operator | Every role (designated in POL-01 4.2). The same person designs, runs, and checks the controls; P07 explains how that is offset |
| Technical support | On-call IT technician | Laptop, phone, and router help on request; attended sessions only |
| Service providers | Productivity suite provider, accounting service provider, dynamometer service provider | Operate inherited controls |
| Customer contacts | Customer A production superintendent and IT and SCADA contact; Customer B operations manager | Approve changes; issue and control remote access; receive incident notices |

## 6. System Information Types and System Categorization
| Information type (SP 800-60, adapted) | C | I | A | Rationale |
|---|---|---|---|---|
| Customer control programs, setpoints, network details, and credentials | Moderate | Moderate | Moderate | Disclosure or tampering gives a path into customer controllers; customers' hardwired shutdowns limit the physical worst case; a missing program stops a well (P05 BP-02 MTD 48 h) |
| Customer production data (gauges, run tickets, dynamometer cards) | Moderate | Moderate | Moderate | Confidential under the MSAs; customers book sales from the gauge sheets (P05 BP-01 and BP-03 MTD 24 h) |
| Business and personal information (invoices, helper W-9s) | Moderate | Low | Low | Social Security numbers are personal information under Fla. Stat. 501.171 |
| **FSBS category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** SP 800-53B Moderate, tailored to 29 controls that a one-person contractor can run and that answer Customer A's security schedule (`control-implementation.csv`). Other Moderate controls are inherited from the SaaS providers (evidence: the productivity suite SOC 2 report, P09) or tailored out because they assume staff, servers, or a federal program. AC-5, AU-9, CM-3, and CA-2(1) assume a second person but are kept with compensating controls (see `control-implementation.csv`).

## 7. Authorization Boundary Description
- **Inside:** the owner's SaaS accounts and their settings (SYS-01, SYS-02, SYS-08), the laptop and phone, USB drives and cables, the home office network, and the owner's credentials and client software for customer remote access.
- **Outside (external systems):** customers' SCADA, controllers, modems, and VPN gateways; the Customer B remote-desktop tool; the SaaS providers' platforms; the free AI chatbot (use stopped).

Diagram: P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Party | Data | Agreement |
|---|---|---|
| Customer A | Gauge sheets; programs and setpoints; remote sessions through its VPN | MSA with security schedule |
| Customer B | Programs and setpoints; remote sessions through a shared remote-desktop login | MSA confidentiality clause only; **no remote access terms (gap)** |
| Customers C and D | Gauge sheets; run tickets | MSA confidentiality clause |
| Dynamometer service | Dynamometer cards and run times for 14 wells | Provider terms; **no Customer A consent (gap)** |
| Productivity suite and accounting providers | Business records, program copies, invoices | Provider terms; SOC 2 report for the suite |

## 9. System Component Inventory
| Component | Type | Owner |
|---|---|---|
| Email and file account (SYS-01) | SaaS | Owner-operator |
| Accounting service (SYS-02) | SaaS | Owner-operator |
| Field laptop (SYS-03) | Endpoint and engineering workstation | Owner-operator |
| Smartphone (SYS-04) | Endpoint | Owner-operator |
| Customer remote access client software and credentials (SYS-05) | Access path | Owner-operator (paths owned by customers) |
| USB drives and programming cables (SYS-06) | Removable media | Owner-operator |
| Home office network (SYS-07) | Consumer router | Owner-operator |
| Dynamometer analysis service (SYS-08) | SaaS with AI | Owner-operator |

Customer field devices the owner programs are listed per customer in the planned device and credential register (CM-8 gap).

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 29 controls:
- Implemented: 6
- Partially implemented: 17
- Planned: 6

Inheritance: 1 fully inherited (SC-8), 11 hybrid (a provider or Customer A operates the mechanism and the owner configures or uses it correctly), and 17 the owner's alone (AC-5, AC-6(2), AC-11, AC-19, AT-2, CA-2(1), CA-3, CM-3, CM-8, CP-2, IA-5, IR-6, IR-8, MP-7, PL-4, RA-3, SA-9).

**Key safeguards per CSF Function:**
| Function | Key safeguards |
|---|---|
| Govern | POL-01; MSA terms as exchange agreements (CA-3); provider review (SA-9); owner holds all roles |
| Identify | Risk assessment (RA-3); BIA (P05); device and credential register (CM-8, gap) |
| Protect | MFA (IA-2(1), IA-2(2)); password manager (IA-5, planned); standard daily account (AC-6(2), planned); disk encryption (SC-28); dedicated scanned program drives (MP-7, planned); change approval and log (CM-3, planned) |
| Detect | Antivirus (SI-3); monthly review of SYS-01 and SYS-02 sign-ins (AU-6, planned; POL-01 7.7) |
| Respond | Ransomware runbook with the 24-hour Customer A notice (IR-8, IR-6) |
| Recover | Offline program backups (CP-9, gap); coverage agreement and recovery codes (CP-2) |

### 10.2 Control assessment status
Self-assessed 2026-07-20 to 2026-07-24 with the IT technician. See P07.

## 11. Digital Identity Acceptance Statement
Email and files use a password plus a text-message code, acceptable for now but weaker than an authenticator app, which is planned by 2026-09-30. The accounting service uses a password only until MFA is turned on (2026-09-15). Customer A's VPN uses Customer A's own MFA. The Customer B path uses a shared password with no MFA; it is outside the owner's control and is tracked as P01 R-003 until Customer B issues named accounts.

## 12. Referenced Artifacts
Scenario facts, P01 risk register, P03 gap analysis, P04 SaaS control map, P05 BIA, P06 POL-01, P07 assessment and POA&M, P08 runbook and notification matrix, P09 SOC 2 self-check and provider report review, P10 AI use assessment.

## 13. Acronym List and Glossary
- **FSBS:** Field Service Business Systems
- **MSA:** master service agreement
- **MFA:** multi-factor authentication
- **OT:** operational technology
- **PLC / RTU:** programmable logic controller / remote terminal unit
- **SCADA:** supervisory control and data acquisition

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial short-form plan | Owner-operator |
