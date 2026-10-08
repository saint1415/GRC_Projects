# System Security Plan (short form): Field Service Business Systems

**Organization:** Cris Santos Company (owner-operated industrial equipment repair service) | **Tier:** Sole Proprietorship | **Vertical:** Critical Manufacturing
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), all headings kept with short answers | **Version:** 1.0, 2026-09-11

## 1. System Name and Identifier
Field Service Business Systems (**FSBS**), identifier CSC-SYS-001.

## 2. System Overview
The FSBS is everything the owner-technician uses to run a one-person repair business for about 10 manufacturing customers: the core SaaS stack for email, files, client and billing records, plus the tools that hold and move the **Customer Machine Library** (control programs for about 70 customer machines). Components are SYS-01 to SYS-06, SYS-08, and SYS-09 in `../00_company-facts.md` section 3: a business productivity suite, an accounting SaaS, the service laptop (with one legacy engineering virtual machine), the phone, the field connection kit, the cellular remote access router the owner installed at Customer B, the AI vibration analytics trial, and the home network.

The FSBS is unusual for a small business in one way: **it connects to other companies' operational technology.** The laptop and USB sticks are plugged into PLCs, HMIs, drives, and CNC controllers at plants that build distribution transformers, power transformers, and switchgear, and into monitoring cabinets at utility substations. The customers' machines are outside the boundary, but what the FSBS carries into them is the owner's responsibility. NIST SP 800-82 Rev. 3 is used as the OT guide (P03).

There is no server and no IaaS. The SaaS providers operate the platforms; the owner is responsible for identities, data, the laptop, phone, and field kit, and what they connect to (P04).

## 3. Laws, Regulations, and Policies Affecting the System
No federal or state cybersecurity regulation binds this business (P03 section 1). Its binding duties are contract terms.

| ID | Requirement | Status for the FSBS |
|---|---|---|
| Customer A exhibit S1 to S8 | Contractor Cyber Security Exhibit (signed 2025-09-30). S4, S5, and S6 flow down NERC CIP-013-2 R1.2 topics from Customer A's utility contracts | **Binding by contract** (P03 G-036 to G-043) |
| Customer B and C NDAs | Reasonable care, use only for the services, prompt notice of unauthorized disclosure | **Binding by contract** (P03 G-044, G-045) |
| CSF 2.0 with SP 800-82 Rev. 3 | NIST CSWP 29; NIST SP 800-82 Rev. 3 | Voluntary benchmark (P03 G-001 to G-035) |
| C-CRITICAL-MFG-R01 | CIRCIA, proposed 6 CFR Part 226 | Proposed only; as proposed would not reach this business (P03 G-047) |
| C-CRITICAL-MFG-R02 to R04 | ICTS connected vehicles rule; EAR; DFARS 252.204-7012 | Not applicable (P03 G-048 to G-050) |
| Other | NERC CIP-013-2 (direct); FAR 52.204-21, -23, -25 | Not applicable: not NERC-registered; no federal work (P03 G-046, G-051) |
| Internal | Information Security Policy | POL-01 (P06) |

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the owner-technician on 2026-09-11.
### 4.2 System Authorization Decision
No formal authorization applies to a private sole proprietorship. Equivalent decision: the owner-technician accepted continued operation on 2026-09-11, on condition that the High risks in P01 (R-001, R-002, R-003) are treated by their due dates and that the router at Customer B stays powered off except for sessions Customer B approves (in place since 2026-09-03).
### 4.3 System Operational Status
Operational. Planned changes: MFA on the accounting SaaS and router portal (2026-09-30); offline backup drives, standard daily laptop account, host-only virtual machine, encrypted USB sticks, password manager, separate business Wi-Fi (2026-10-31); router at Customer B replaced by a Customer B owned gateway or removed (2026-12-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner, security lead, contract compliance, incident lead, risk acceptor | Owner-technician | Every role (designated in POL-01 section 3) |
| Technical support | On-call IT consultant (NDA since 2026-08-20) | Laptop, virtual machine, and home router help on request, in sessions the owner starts and watches; no standing access |
| Bookkeeping | Outside bookkeeper (CPA firm) | Own named accountant-role login to the accounting SaaS, with MFA |
| Service providers | Productivity suite provider, accounting SaaS provider, router maker (cloud portal), vibration analytics vendor | Operate inherited controls |
| Customer contacts | Customer A plant controls engineer; Customer B maintenance supervisor | Approve remote sessions; run media scanning (Customer A); receive incident notices |

## 6. System Information Types and System Categorization
| Information type | C | I | A | Rationale |
|---|---|---|---|---|
| Customer machine programs and configuration (PLC logic, HMI projects, drive parameters, CNC programs, winding recipes, monitoring unit firmware) | Moderate | Moderate | Moderate | Customer trade secrets (exhibit S1; NDAs). A wrong or altered program can damage equipment or a transformer coil and stop a grid-equipment line (serious adverse effect); the customers' own machine safety systems are outside this boundary. A stopped line needs a reload within 4 hours (P05 RTO) |
| Customer machine credentials and network details | Moderate | Low | Low | Disclosure gives access to 10 customer sites |
| Business records (quotes, invoices, remittance details, tax records) | Moderate | Moderate | Low | Payment fraud and financial loss; can wait 72 hours (P05 BP-04) |
| **FSBS category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** SP 800-53B Moderate, tailored to 28 controls that carry the customer contract duties and the High risks for a one-person business (`control-implementation.csv`). Other Moderate controls are either inherited from the SaaS providers (evidence: the productivity suite provider's SOC 2 report, P09) or tailored out because they assume staff, servers, or a federal program. AC-5, AU-9, CM-3, and CA-2(1) are kept with compensating controls (see `control-implementation.csv`). The integrity rating would rise to High if the owner ever became responsible for a machine's safety functions; that would be a new contract and a new assessment.

## 7. Authorization Boundary Description
- **Inside:** the owner's tenant settings and accounts in the productivity suite, accounting SaaS, router cloud portal, and vibration analytics SaaS; the service laptop and its virtual machine; the phone; the field connection kit (cables, adapters, 8 USB sticks, a small switch); the router at Customer B (owner property); the home office network as the owner uses it; the paper file cabinet.
- **Outside:** Customer A's remote access gateway (SYS-07) and media scanning station; every customer machine, plant network, and substation system; the SaaS platforms themselves; the IT consultant's and bookkeeper's own systems; OEM support desks.
- **Where the boundary touches OT:** each time the laptop or a USB stick connects to a customer controller (POL-01 section 7). Those connections are the highest-risk points in the plan (P01 R-002).

Diagram: P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Party | Data | Agreement |
|---|---|---|
| Customer A (plants and substation work) | Programs, drawings, firmware and hash values, remote sessions through its gateway | Service agreement with exhibit S1 to S8 |
| Customers B and C | Programs, drawings, machine passwords | Mutual NDAs |
| Seven local plants | Programs and passwords | **No written security terms** |
| OEM support desks | Program files sent for diagnosis | **No terms; customer consent not recorded (gap, P03 G-036)** |
| Vibration analytics vendor (AI-001) | Vibration data, machine and plant names | **Click-through terms; no Customer A consent (gap, P10)** |
| Bookkeeper | Invoices, payments, bank feed | Engagement letter |
| IT consultant | Watched remote sessions on the laptop | NDA (2026-08-20) |

## 9. System Component Inventory
| Component | Type | Owner |
|---|---|---|
| Productivity suite tenant (SYS-01) | SaaS | Owner-technician |
| Accounting SaaS (SYS-02) | SaaS | Owner-technician |
| Service laptop and legacy virtual machine (SYS-03) | Endpoint | Owner-technician |
| Phone (SYS-04) | Personal endpoint used for business | Owner-technician |
| Field connection kit (SYS-05) | Removable media and cables | Owner-technician |
| Cellular remote access router at Customer B (SYS-06) and its cloud portal | Owner device on a customer panel | Owner-technician |
| Vibration analytics SaaS and sensors (SYS-08) | SaaS trial | Owner-technician |
| Home office network (SYS-09) | Shared household network | Owner-technician |
| Old laptop (replaced 2025; not wiped) | Retired endpoint | Owner-technician |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 28 controls:
- Implemented: 4 (AU-9, IA-2, MA-4, RA-3)
- Partially implemented: 20
- Planned: 4 (AC-6, AT-2, MP-6, SI-7)

Inheritance: none fully inherited at the control level; 10 hybrid (a provider or Customer A operates the mechanism and the owner configures or uses it correctly: AC-2, AC-5, AC-17, AU-9, CP-9, IA-2, IA-2(1), SC-28, SI-2, SI-3) and 18 the owner's alone.

**Key safeguards per CSF Function:**
| Function | Key safeguards |
|---|---|
| Govern | POL-01 with the contract obligations list (Appendix B); supplier terms (SA-9); owner holds all roles |
| Identify | Risk assessment (RA-3); BIA (P05); asset and software list (CM-8, gap) |
| Protect | Suite MFA (IA-2(1), gaps on two services); disk encryption (SC-28); standard account (AC-6, planned); removable media rules (MP-7); Customer A gateway only (AC-17) |
| Detect | Built-in antivirus (SI-3); media scanning at Customer A (exhibit S3, partial); hash checks (SI-7, planned) |
| Respond | Ransomware runbook and notification matrix (IR-8, IR-6) |
| Recover | Version history (CP-9, inherited part); offline backups and customer-held copies (planned); referral arrangement (CP-2, planned) |

### 10.2 Control assessment status
Self-assessed 2026-08-24 to 2026-08-28 with the IT consultant (tests 2026-08-26 at the home office and 2026-08-27 at Customer B). See P07.

## 11. Digital Identity Acceptance Statement
The productivity suite requires a password and an authenticator app code, which is appropriate for the account that holds the Customer Machine Library. The accounting SaaS owner account and the router cloud portal use a password only until MFA is turned on (2026-09-30); the router stays powered off except for approved sessions until then. Customer A's gateway enforces its own MFA and per-session approval, outside this boundary. Customer machine passwords are the customers' authenticators; the owner protects them (IA-5) but cannot change how the customers' controllers authenticate.

## 12. Referenced Artifacts
Scenario facts, P01 risk register, P03 gap analysis, P04 SaaS control map, P05 BIA, P06 POL-01, P07 assessment and POA&M, P08 runbook and notification matrix, P09 SOC 2 self-check and vendor review, P10 AI use assessment.

## 13. Acronym List and Glossary
- **FSBS:** Field Service Business Systems
- **HMI:** human-machine interface
- **MFA:** multi-factor authentication
- **NDA:** nondisclosure agreement
- **OEM:** original equipment manufacturer
- **OT:** operational technology
- **PLC:** programmable logic controller
- **Customer Machine Library:** the owner's copies of customer machine programs, synced to cloud storage

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-09-11 | Initial short-form plan | Owner-technician |
