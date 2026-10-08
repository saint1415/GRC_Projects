# System Security Plan (short form): Practice Systems Profile

**Organization:** Cris Santos Company (solo primary care physician practice) | **Tier:** Sole Proprietorship | **Vertical:** Health Care and Social Assistance
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), all headings kept with short answers | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Practice Systems Profile (**PSP**), identifier CSC-SYS-001.

## 2. System Overview
The PSP is everything the practice uses to see about 900 active patients: scheduling, charting, e-prescribing, the patient portal, faxing, billing, and patient communication. One person, the physician-owner, uses and runs it. Components are SYS-01 to SYS-07 in `../00_company-facts.md` section 3: the EHR/PM (SaaS), a consumer email and file account, a laptop and tablet, a personal phone, a cloud fax service, the shared building Wi-Fi, and a consumer AI scribe app (trial paused; see P10). There is no server and no IaaS. Most safeguards are **inherited from the SaaS vendors**; the owner is responsible for identities, data handling, devices, and vendor contracts (P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| N62-R01 | HIPAA Security Rule | 45 CFR Part 164, Subpart C |
| N62-R02 | HIPAA Privacy Rule | 45 CFR Part 164, Subpart E |
| N62-R03 | HIPAA Breach Notification Rule | 45 CFR 164.400-414 |
| N62-R04 | HIPAA Security Rule NPRM (proposed, not in force) | 90 FR 898 (2025-01-06). Tracked only |
| N62-R07 | Section 1557 patient care decision support tools | 45 CFR 92.210 (EHR reminders; P10) |
| State | Breach notification; recording consent | Fla. Stat. 501.171; Fla. Stat. 934.03 |
| Internal | Information Security Policy | POL-01 (P06) |

Not applicable: 42 CFR Part 2 (no federally assisted SUD program) and the CMS emergency preparedness rule (N62-R08), which does not cover physician offices.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the physician-owner on 2026-08-31.
### 4.2 System Authorization Decision
No formal authorization applies to a private practice. Equivalent decision: the physician-owner accepted continued operation on 2026-08-31, on condition that the High risks in P01 (R-001, R-002, R-004) are treated by their due dates.
### 4.3 System Operational Status
Operational. Planned changes: move email and files to a business plan with a BAA (2026-10-31); practice-owned router (2026-12-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner, Security Officer, Privacy Officer, risk acceptor | Physician-owner | Every role (45 CFR 164.308(a)(2) designation in POL-01) |
| Technical support | On-call IT consultant (BA since 2026-07-17) | Laptop and Wi-Fi help on request; no standing access |
| Service providers | EHR vendor, billing company, cloud fax vendor (all BAs) | Operate inherited controls |

## 6. System Information Types and System Categorization
| Information type (SP 800-60) | C | I | A | Rationale |
|---|---|---|---|---|
| Health care delivery services (patient records, ePHI) | Moderate | Moderate | Moderate | Disclosure triggers breach duties; wrong data can harm care; loss beyond one clinic day affects patient safety (P05 MTD 24 h) |
| Health care administration (claims) | Moderate | Moderate | Low | Financial and identity data; payers accept late claims (P05 MTD 120 h) |
| **PSP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** SP 800-53B Moderate, tailored to 26 controls that carry the HIPAA safeguards for a one-person practice (`control-implementation.csv`). Other Moderate controls are either inherited from the SaaS vendors (evidence: the EHR vendor's SOC 2 report, P09) or tailored out because they assume staff, servers, or a federal program. AC-5, AU-9, CM-3, and CA-2(1) are kept with compensating controls (see `control-implementation.csv`).

## 7. Authorization Boundary Description
- **Inside:** the owner's EHR/PM account settings and user roles, the email and file account, the cloud fax account, the laptop, tablet, and phone, the suite's use of the building Wi-Fi, and paper records in the suite.
- **Outside (external services):** the EHR vendor's platform, the billing company, the answering service, the cloud fax platform, the e-prescribing network, the AI scribe app vendor, and the building network equipment.

Diagram: P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Party | Data | Agreement |
|---|---|---|
| Billing company | Charges, claims, remittances (it submits standard transactions for the practice) | BAA |
| E-prescribing network (through the EHR) | Prescriptions | Via EHR vendor BAA |
| Cloud fax | Referrals, records requests | BAA |
| Answering service | After-hours messages | **No BAA (gap)** |
| Email and file provider | Incidental PHI in email and documents | **No BAA (gap)** |
| AI scribe app | Visit audio, draft notes | **No BAA; trial paused (gap)** |

## 9. System Component Inventory
| Component | Type | Owner |
|---|---|---|
| EHR/PM tenant (SYS-01) | SaaS | Physician-owner |
| Email and file account (SYS-02) | Consumer SaaS | Physician-owner |
| Laptop and tablet (SYS-03) | Endpoints | Physician-owner |
| Mobile phone (SYS-04) | Personal endpoint | Physician-owner |
| Cloud fax (SYS-05) | SaaS | Physician-owner |
| Building Wi-Fi (SYS-06) | Shared network | Landlord |
| AI scribe app (SYS-07) | Consumer app | Physician-owner |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 26 controls:
- Implemented: 11
- Partially implemented: 13
- Planned: 2

Inheritance: 4 fully inherited from the vendors (AC-3, AU-2, AU-9, SC-5), 13 hybrid (vendor operates the mechanism, the owner configures or uses it correctly), and 9 the owner's alone (AC-11, AT-2, AU-6, CA-2(1), CM-3, CP-2, IR-8, RA-3, SA-9).

**Key safeguards per CSF Function:**
| Function | Key safeguards |
|---|---|
| Govern | POL-01; BAAs (SA-9); owner holds all roles |
| Identify | Risk analysis (RA-3); BIA (P05) |
| Protect | EHR MFA (IA-2(1)); disk encryption (SC-28, gap); device lock (AC-11) |
| Detect | EHR audit logging (AU-2, inherited); monthly log review (AU-6, planned) |
| Respond | Ransomware runbook (IR-8) |
| Recover | EHR vendor backups (CP-9, inherited); coverage arrangement (CP-2) |

### 10.2 Control assessment status
Self-assessed 2026-07-20 to 2026-07-24 with the IT consultant. See P07.

## 11. Digital Identity Acceptance Statement
The EHR requires a password and a second factor on the owner's phone, which is appropriate for remote access to ePHI at a Moderate categorization. The email account and cloud fax portal use a password only until MFA is turned on (2026-09-15). Patients use the EHR vendor's portal and its identity controls, outside this boundary.

## 12. Referenced Artifacts
Scenario facts, P01 risk register, P03 gap analysis, P04 SaaS control map, P05 BIA, P06 POL-01, P07 assessment and POA&M, P08 runbook, P09 SOC 2 self-check and vendor review, P10 AI use assessment.

## 13. Acronym List and Glossary
- **BA / BAA:** business associate / business associate agreement
- **EHR/PM:** electronic health record and practice management
- **ePHI:** electronic protected health information
- **MFA:** multi-factor authentication
- **PSP:** Practice Systems Profile

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial short-form plan | Physician-owner |
