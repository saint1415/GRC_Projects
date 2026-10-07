# System Security Plan (short form): Engineering Office Systems

**Organization:** Cris Santos Company (engineering subcontractor handling CUI drawings) | **Tier:** Sole Proprietorship | **Vertical:** Defense Industrial Base
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), all headings kept with short answers | **Version:** 1.0, 2026-08-31 (replaces the 2025-05 template)

This plan is also the system security plan that NIST SP 800-171 Rev. 2 requirement 3.12.4 and the CMMC Level 2 self-assessment require (32 CFR 170.24(c)(2)(i)(B)(5)). At this size the requirement-by-requirement statements are kept in one place: the `current_state` column of the P03 gap analysis (`../step-05_P03_regulatory-gap-analysis/gap-analysis.csv`, rows G-001 to G-110). This document and that table together form the SSP.

## 1. System Name and Identifier
Engineering Office Systems (**EOS**), identifier CSC-SYS-001. CAGE code on file in SAM.gov.

## 2. System Overview
The EOS is everything the owner uses to deliver engineering work: desktop CAD on one laptop, email and synced project files, client and billing records, and the Prime A portal. One person, the owner, uses and runs it. Components are SYS-01 to SYS-08 and the planned SYS-10 in `../00_company-facts.md` section 3. There is no server and no IaaS. About 320 CUI files (Prime A drawings, models, and the owner's derived work) are held on the laptop and in the commercial productivity suite (SYS-01). Most service-side safeguards are inherited from SaaS providers; the owner is responsible for identities, data placement, devices, the home network, and the home office (P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | Applies? |
|---|---|---|---|
| C-DIB-R01 | DFARS Safeguarding Covered Defense Information and Cyber Incident Reporting | 48 CFR 252.204-7012 (MAY 2024) | Yes, in the Prime A subcontract. SP 800-171 Rev. 2 on every covered contractor information system; FedRAMP Moderate-equivalent cloud; 72-hour DoD reporting |
| C-DIB-R02 | CMMC Program and DFARS 252.204-7021 | 32 CFR Part 170; 48 CFR 252.204-7021 (NOV 2025) | From the follow-on subcontract: CMMC Level 2 (Self) before award (32 CFR 170.16(b); 170.23(a)(2)) |
| C-DIB-R03 | NIST SP 800-171 DoD Assessment (SPRS) | 48 CFR 252.204-7019 and 252.204-7020 (NOV 2023) | Yes. Basic Assessment not more than 3 years old in SPRS |
| C-DIB-R04 | Basic Safeguarding of Covered Contractor Information Systems | 48 CFR 52.204-21 (NOV 2021) | Yes, for FCI (including SYS-05) |
| C-DIB-R05 | ITAR | 22 CFR Parts 120-130 | Yes for the ITAR-marked drawings: no release to foreign persons (120.50, 120.56). Registration not required (122.1(b)(2)) |
| C-DIB-R06 | EAR | 15 CFR Parts 730-774 | Possibly, for some commercial aerospace data (734.18(a)(5) for encrypted storage) |
| C-DIB-R07 | NISPOM | 32 CFR Part 117 | No. No facility clearance and no classified information |
| Internal | Information Security Policy | POL-01 (P06) | Yes |

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the owner on 2026-08-31.
### 4.2 System Authorization Decision
No Government authorization applies to a contractor system. The equivalent decisions are (a) the owner's acceptance of continued operation on 2026-08-31, on condition that the High and Very High risks in P01 are treated by their due dates, and (b) the CMMC affirmation (32 CFR 170.22), which the owner will **not** submit until a self-assessment with evidence supports it (target 2027-01-15).
### 4.3 System Operational Status
Operational. Planned changes: SYS-10 go-live and CUI migration out of SYS-01 (2026-11-30); separate business network (2026-10-31); standard user account for daily work (2026-09-30).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner, security lead, CUI and export compliance lead, risk acceptor, Affirming Official | Owner | Every role. Designated in POL-01 section 3 |
| Technical support | On-call IT consultant | Hands-on help on site with the owner present; no standing or remote access |
| Outside reviewer | Independent CMMC consultant | Reviews the self-assessment from screenshots and documents; sees no CUI |
| Service providers | SYS-01 provider (until migration), SYS-10 provider, accounting SaaS vendor, internet service provider | Operate inherited controls |

## 6. System Information Types and System Categorization
| Information type | C | I | A | Rationale |
|---|---|---|---|---|
| Controlled technical information (CUI Basic; some ITAR technical data) | Moderate | Moderate | Low | 32 CFR 2002.14(a)(3) treats Moderate as the confidentiality level for CUI Basic; altered drawings could reach parts but Prime A checks every release; P05 MTD 72 to 120 h |
| Federal contract information (task orders, invoices) | Low | Low | Low | Basic safeguarding only (FAR 52.204-21); P05 MTD 240 h |
| Commercial customer proprietary data | Moderate | Moderate | Low | Nondisclosure agreements; possible EAR-controlled technology |
| **EOS category (high-water mark)** | **Moderate** | **Moderate** | **Low** | |

**Baseline:** the 110 security requirements of NIST SP 800-171 Rev. 2 (all apply; four have no in-scope component today and are scored as Met under 32 CFR 170.24(b)(3), see P03). For P07 and the risk register, those requirements are traced to a tailored set of 30 SP 800-53 Rev. 5 Moderate controls in `control-implementation.csv`.

## 7. Authorization Boundary Description
- **Inside (CMMC Level 2 assessment scope, 32 CFR 170.19(c)):** CUI Assets: SYS-02 laptop, SYS-07 USB backup drive, SYS-08 printer and scanner, SYS-01 (until CUI leaves it on 2026-11-30), SYS-03 phone (until CUI is removed from it), SYS-10 (after go-live). Security Protection Assets: SYS-04 home router and Wi-Fi; SYS-03 phone as the MFA device; the password manager (planned). Also inside: the owner, the home office room, and printed CUI.
- **FCI only:** SYS-05 accounting SaaS. Its CMMC scoping position is open under DFARS 252.204-7021(d)(2), so it is kept inside this boundary and protected to FAR 52.204-21 and MFA (P03 G-125).
- **Outside:** SYS-06 Prime A portal (Prime A's system), SYS-09 commercial AI chatbot (prohibited for CUI), household devices on the home network (to be separated), and the commercial customers' systems.
- **After migration:** SYS-01 becomes a Contractor Risk Managed Asset (it can, but by policy must not, hold CUI) and SYS-03 becomes a Security Protection Asset only.

Diagram: P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Party | Data | Path | Agreement |
|---|---|---|---|
| Prime A | CUI drawings, models, markups; task orders (FCI) | SYS-06 portal (MFA, TLS); some email to SYS-01 | Subcontract with DFARS 252.204-7012 |
| Commercial customers | Proprietary drawings | Email and file links | Nondisclosure agreements |
| SYS-01 provider | All CUI files and email today | Commercial SaaS | Standard commercial terms. **Not FedRAMP Moderate (gap)** |
| SYS-10 provider (planned) | CUI files and email | Government-community cloud SaaS | Reseller agreement; FedRAMP package and CRM |
| SYS-09 AI chatbot provider | CUI excerpts pasted 2026 (stopped) | Commercial SaaS | Consumer terms. **Prohibited for CUI** |
| DoD (DIBNet) | Cyber incident reports | Web portal | Requires a medium assurance certificate (planned) |

## 9. System Component Inventory
| Component | Type | CMMC asset category | Owner |
|---|---|---|---|
| SYS-01 productivity suite | Commercial SaaS | CUI Asset today; Contractor Risk Managed Asset after migration | Owner |
| SYS-02 engineering laptop | Endpoint | CUI Asset | Owner |
| SYS-03 mobile phone | Personal endpoint | CUI Asset today; Security Protection Asset after migration | Owner |
| SYS-04 router and Wi-Fi | Network device | Security Protection Asset | Owner (internet service provider equipment) |
| SYS-05 accounting SaaS | Commercial SaaS | FCI only (scoping open) | Owner |
| SYS-07 USB backup drive | Removable media | CUI Asset | Owner |
| SYS-08 printer and scanner | Network device | CUI Asset | Owner |
| SYS-10 government-community cloud suite | SaaS (FedRAMP Moderate or higher) | CUI Asset (planned) | Owner |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 30 controls:
- Implemented: 5
- Partially implemented: 19
- Planned: 6

Inheritance: 12 hybrid (a provider runs the mechanism and the owner configures or uses it) and 18 the owner's alone. No control is fully inherited, because SYS-01 is not an acceptable home for CUI and SYS-10 is not live yet. Once SYS-10 is live, its customer responsibility matrix will be referenced here (32 CFR 170.16(c)(2)(iii)).

**Key safeguards per CSF Function:**
| Function | Key safeguards |
|---|---|
| Govern | POL-01; this SSP (PL-2); approved external services only (SA-9, AC-20); owner holds all roles |
| Identify | Risk assessment (RA-3); BIA (P05); asset inventory with CMMC categories (section 9) |
| Protect | MFA (IA-2(1), IA-2(2)); password manager (IA-5, planned); standard user account (AC-6(2), planned); disk encryption with FIPS mode (SC-28(1), SC-13); separate business network (SC-7); locked office and visitor log (PE-3, PE-8) |
| Detect | SaaS audit logs (AU-2); monthly review (AU-6, planned); vulnerability scans (RA-5, planned) |
| Respond | CUI exfiltration runbook (IR-8); DoD reporting with a medium assurance certificate (IR-6, planned) |
| Recover | Version history and encrypted weekly backup (CP-9); continuity arrangement with Prime A (P05) |

### 10.2 Control assessment status
Self-assessed 2026-07-13 to 2026-08-07, with outside review by the CMMC consultant. Recalculated SPRS score: see P03 section 3. Control tests: P07.

## 11. Digital Identity Acceptance Statement
SYS-01 and the Prime A portal require a password and an authenticator app code, which meets SP 800-171 3.5.3 for network access but is not phishing resistant (P01 R-001). Local administrator sign-in on the laptop uses a password only (gap). SYS-10 will require a hardware security key for the owner's accounts, with a spare key in the home safe. SYS-05 moves from password only to MFA by 2026-09-15.

## 12. Referenced Artifacts
Scenario facts, P01 risk register, P03 gap analysis (requirement statements and score), P04 SaaS control map and diagram, P05 BIA, P06 POL-01, P07 assessment and POA&M, P08 runbook and notification matrix, P09 readiness self-check and SYS-10 evidence review, P10 AI use assessment.

## 13. Acronym List and Glossary
- **CAGE:** Commercial and Government Entity code
- **CDI / CTI:** covered defense information / controlled technical information
- **CRM:** customer responsibility matrix
- **CUI / FCI:** controlled unclassified information / federal contract information
- **EOS:** Engineering Office Systems
- **SPRS:** Supplier Performance Risk System

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.1 | 2025-05-20 | Generic template (did not describe the system) | Owner |
| 1.0 | 2026-08-31 | Short-form plan written from the 2026 self-assessment | Owner |
