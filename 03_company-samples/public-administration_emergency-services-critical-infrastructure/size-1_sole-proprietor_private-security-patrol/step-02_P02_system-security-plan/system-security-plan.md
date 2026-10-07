# System Security Plan (short form): Patrol Business SaaS Stack

**Organization:** Cris Santos Company (unarmed private security patrol, licensed Class "B" agency) | **Tier:** Sole Proprietorship | **Vertical:** Emergency Services
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), all headings kept with short answers | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Patrol Business SaaS Stack (**PBS**), identifier CSC-SYS-001.

## 2. System Overview
The PBS is everything the business uses to patrol 7 client properties, answer alarm calls, report to clients, and bill them. One person, the owner, uses and runs it. Components are SYS-01 to SYS-07 in `../00_company-facts.md` section 3: the patrol management app (SaaS, the system of record, with an AI report assistant), a consumer email and file account, an accounting SaaS, a home office laptop, the owner's phone, a body-worn camera, and the home router. There is no server and no IaaS. The boundary also covers what the owner holds outside any system: 23 client keys, 6 access cards, the alarm and gate codes, and the paper key log. Most platform safeguards are **inherited from the SaaS vendors**; the owner is responsible for identities, devices, client access data, and vendor terms (P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| State | Private security licensing: agency and officer licenses, unauthorized release of information, false reports, records on request | Fla. Stat. Chapter 493 (493.6301; 493.6118(1)(e); 493.6119(4); 493.6121(2)) |
| State | Reasonable measures for personal information, breach notice, disposal | Fla. Stat. 501.171(2)-(6), (8) |
| State | Consent to record oral communications (body-camera audio) | Fla. Stat. 934.03(2)(d) |
| Contract | Client patrol agreements: confidentiality, 2-hour and 24-hour incident notice, 45-minute alarm response, return of keys and information | P03 rows G-019 to G-021 |
| Internal | Information Security Policy | POL-01 (P06) |

The vertical's registry requirements do not apply to this business: the HIPAA Security Rule (C-EMERGENCY-R04; not a covered entity), the FBI CJIS Security Policy and 28 CFR Parts 20 and 23 (C-EMERGENCY-R01 to R03; no criminal justice information), FCC EAS rules (C-EMERGENCY-R06), and CIRCIA (C-EMERGENCY-R05; proposed only). Reasons are in P03 section 1.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the owner on 2026-08-31.
### 4.2 System Authorization Decision
No formal authorization applies to a private business. Equivalent decision: the owner accepted continued operation on 2026-08-31, on condition that the High risks in P01 (R-001, R-002, R-003) are treated by their due dates.
### 4.3 System Operational Status
Operational. Planned changes: password manager and app-based MFA (2026-09-15); access codes moved out of the spreadsheet into the password manager vault with a sealed paper copy in the home safe (2026-09-15); a separate backup of files (2026-10-31); a written agreement with the backup patrol agency (2026-12-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner, information security lead, records custodian, incident commander, risk acceptor | Owner (Class "D" licensee and designated agency manager) | Every role (designated in POL-01 4.2) |
| Technical support | On-call IT technician (confidentiality agreement since 2026-08-07) | Laptop, phone, and router help on request; no standing access |
| Service providers | Patrol app vendor (and its AI model provider), email and file provider, accounting SaaS vendor | Operate inherited controls |
| Continuity partner | Backup patrol agency (licensed Class "B"; verbal arrangement) | Covers patrols if the owner cannot; no system access today |

## 6. System Information Types and System Categorization
| Information type (SP 800-60) | C | I | A | Rationale |
|---|---|---|---|---|
| Client site access information (alarm and gate codes, key and keyholder lists, post orders) | Moderate | Moderate | Moderate | Disclosure enables entry to a client site; a wrong code delays response; loss stops alarm response (P05 BP-02 MTD 4 h) |
| Incident and patrol records (reports with personal information, GPS tracks, video) | Moderate | Moderate | Moderate | Personal information under Fla. Stat. 501.171; reports are evidence and must be accurate (493.6119(4)); records must be produced on request (493.6121(2)) |
| Business administration (contracts, invoices) | Low | Moderate | Low | Wrong bank details on an invoice cause loss; billing can wait days (P05 BP-04) |
| **PBS category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** SP 800-53B Moderate, tailored to 24 controls that a one-person patrol can run (`control-implementation.csv`). Other Moderate controls are either inherited from the SaaS vendors (evidence: the patrol app vendor's SOC 2 report, P09) or tailored out because they assume staff, servers, or a federal program. PE-3 is applied to the physical access devices the owner holds for clients (keys, cards, and codes), which is where this business's highest-consequence data lives.

## 7. Authorization Boundary Description
- **Inside:** the owner's patrol app admin account, its settings and client portal accounts; the email and file account; the accounting SaaS account; the laptop, phone, and body camera; the home router; client keys, cards, and codes; the paper key log and paper records at the home office.
- **Outside (external services):** the patrol app vendor's platform and its AI model provider, the email and accounting platforms, the mobile carrier, clients' alarm monitoring companies and alarm panels, the backup patrol agency, and client sites themselves.

Diagram: P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Party | Data | Agreement |
|---|---|---|
| Clients (portal, email, phone) | Daily and incident reports, post orders, codes | Patrol agreements with confidentiality clauses |
| Patrol app vendor and its AI model provider | Reports, voice notes, GPS, photos | Vendor terms; AI addendum (training opt-out set 2026-08-12) |
| Alarm monitoring companies | Alarm calls, keyholder status | Client's own contract; owner listed as responder |
| Police and fire (911) | Calls; incident reports or video on request | None (lawful request or client consent) |
| Email and file provider | Contracts, code spreadsheet, video clips | Consumer terms only |
| Backup patrol agency | Nothing today | **Verbal only (gap)** |

## 9. System Component Inventory
| Component | Type | Owner |
|---|---|---|
| Patrol app tenant (SYS-01) | SaaS | Owner |
| Email and file account (SYS-02) | Consumer SaaS | Owner |
| Accounting SaaS (SYS-03) | SaaS | Owner |
| Laptop (SYS-04) | Endpoint (shared with a family member) | Owner |
| Mobile phone (SYS-05) | Endpoint | Owner |
| Body-worn camera (SYS-06) | Recording device | Owner |
| Home router (SYS-07) | ISP-provided network device | ISP; owner configures |
| Client keys, access cards, codes, key log | Physical access devices and paper | Owner (in custody for clients) |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 24 controls:
- Implemented: 5
- Partially implemented: 15
- Planned: 4

Inheritance: 2 fully inherited from the patrol app vendor (AC-3, AU-2), 9 hybrid (a vendor operates the mechanism and the owner configures or uses it correctly), and 13 the owner's alone (AC-11, AC-19, AT-2, AU-6, CP-2, IA-5, IR-6, IR-8, MP-6, PE-3, RA-3, SA-9, SI-12).

**Key safeguards per CSF Function:**
| Function | Key safeguards |
|---|---|
| Govern | POL-01; vendor review (SA-9); owner holds all roles |
| Identify | Risk assessment (RA-3); BIA (P05); retention schedule (SI-12, planned) |
| Protect | MFA (IA-2(1), gap on the patrol app); key and code custody (PE-3); encryption (SC-28, gaps on the code list and camera card) |
| Detect | Patrol app audit trail (AU-2, inherited); monthly sign-in review (AU-6, planned) |
| Respond | Ransomware runbook (IR-8); notification matrix with client and Florida deadlines (IR-6) |
| Recover | Patrol app vendor backups (CP-9, inherited); sealed code book and backup agency (CP-2) |

### 10.2 Control assessment status
Self-assessed 2026-08-10 to 2026-08-14 with the IT technician. See P07.

## 11. Digital Identity Acceptance Statement
The accounting SaaS requires a password and an app-based second factor. Email uses a password and a text-message code, which is weaker because a phone number can be moved to another SIM; it moves to an authenticator app by 2026-09-15. The patrol app admin account, which can read every client's codes in the post orders, used a password only until MFA is turned on (2026-09-15). Client portal users sign in with a password only until MFA is required for them (2026-10-31).

## 12. Referenced Artifacts
Scenario facts, P01 risk register, P03 gap analysis, P04 SaaS control map, P05 BIA, P06 POL-01, P07 assessment and POA&M, P08 runbook, P09 SOC 2 self-check and vendor review, P10 AI use assessment.

## 13. Acronym List and Glossary
- **Class "B" / Class "D":** Florida security agency license / security officer license (Fla. Stat. 493.6301)
- **DAR:** daily activity report
- **MFA:** multi-factor authentication
- **PBS:** Patrol Business SaaS Stack
- **Post orders:** a client's written instructions for its site, including access codes

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial short-form plan | Owner |
