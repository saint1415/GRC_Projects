# System Security Plan: Transport Operations Platform (TOP)

**Organization:** Cris Santos Company, LLC (licensed BLS ambulance service, non-emergency transport only) | **Tier:** Micro | **Vertical:** Emergency Services
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-04

## 1. System Name and Identifier
Transport Operations Platform (**TOP**), identifier CSC-SYS-001.

## 2. System Overview
The TOP supports every step of a non-emergency ambulance trip: the request from a hospital, dialysis center, or family; scheduling; dispatch of one of 2 BLS ambulances; the patient care report; delivery of that report to the receiving hospital; and the hand-off of trip data to the billing company. It serves 7 workforce members and about 3,000 transports a year from one Florida office and garage.

The company owns almost no infrastructure. Most of the TOP is vendor SaaS, and a managed service provider (MSP) runs the office computers, network, and backup. This plan therefore says, for each control, what the company does itself, what the MSP does for it, and what it inherits from a SaaS vendor.

**Major components:**
- **SYS-01:** ambulance operations platform (vendor SaaS): CAD board, trip scheduling, facility request portal, and ePCR with hospital record delivery and state data export
- **SYS-02:** productivity suite (SaaS): email, shared drive, shared fax mailbox
- **SYS-04:** hosted phone system (SaaS): request lines, call recording, on-call forwarding, fax-to-email
- **SYS-05:** 2 desktops, 1 laptop, 3 rugged ePCR tablets, 4 company phones (MSP-managed)
- **SYS-06:** office network: firewall, Wi-Fi, one internet line (MSP-managed)
- **SYS-07:** vehicle hotspots and GPS trackers
- **SYS-08:** cloud backup of suite mailboxes and the shared drive (SaaS, administered by the MSP)

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| C-EMERGENCY-R04 | HIPAA Security Rule | 45 CFR Part 164, Subpart C. The company is a covered entity (45 CFR 160.103) |
| Related | HIPAA Privacy Rule and Breach Notification Rule | 45 CFR Part 164, Subparts E and D (164.400-414) |
| Related | HIPAA Security Rule NPRM (proposed, not in force) | 90 FR 898 (2025-01-06). Tracked only |
| C-EMERGENCY-R05 | CIRCIA (proposed, not in force) | Proposed 6 CFR 226 (89 FR 23644). Tracked only. See P03 section 1 |
| Medicare | Ambulance coverage and documentation | 42 CFR 410.40(e) (certification statements); 410.41 (vehicle, staff, billing); 424.516(f) (keep documentation 7 years) |
| State | EMS records and patient care records | Fla. Stat. 401.30; Rule 64J-1.014, F.A.C. (5-year retention; record available to the receiving hospital on request within 48 hours of dispatch) |
| State | Recording of telephone calls | Fla. Stat. 934.03 (all-party consent, 934.03(2)(d)) |
| State | Florida Information Protection Act (breach notification) | Fla. Stat. 501.171 |
| Federal | Section 1557 patient care decision support tools | 45 CFR 92.210. Relevant to the AI intake assistant (P10) |
| Contract | Regional hospital transport agreement | Security questionnaire and cyber insurance requirement (P09) |
| Internal | Security policies POL-02, POL-03, POL-04 | P06 |

Not applicable:
- FBI CJIS Security Policy (C-EMERGENCY-R01) and 28 CFR 20.21 and Part 23 (C-EMERGENCY-R02, R03): the TOP does not store, process, or view criminal justice information. The company has no link to the county 911 center or to law enforcement systems.
- FCC EAS rules (C-EMERGENCY-R06): the company is not an EAS participant.
- 42 CFR Part 2: the company runs no federally assisted substance use disorder program.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Owner on 2026-09-04.

### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization. The equivalent internal decision: on 2026-09-04 the Owner accepted continued operation of the TOP, on the condition that the POA&M items in P07 are completed by their dates and the three High risks in P01 are treated by 2026-12-31.

### 4.3 System Operational Status
Operational. Planned changes: MFA and named dispatch accounts on the platform (P01 R-002, R-007), EDR and backup upgrades (R-001, R-005), desktop encryption (R-011), and a separate staff Wi-Fi network (R-018), all due by 2026-12-31.

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner and risk acceptor | Owner (managing member) | Overall accountability; accepts Moderate risk; approves this plan, policies, and spending |
| Security Officer and Privacy Officer | Office Manager | Day-to-day security and privacy (45 CFR 164.308(a)(2)); maintains this plan, the risk register, and the BAA folder |
| Dispatch operations | Scheduler-Dispatcher | Dispatch board use, the nightly run sheet, manual dispatch; AI intake pilot user |
| Clinical oversight | Medical Director (contracted) | Patient care protocols, 911 redirect rules, AI intake review (P10) |
| IT operations | MSP (business associate) | Office computers, mobile device management, patching, antivirus, firewall, Wi-Fi, backup administration |
| Independent assessor | HIPAA security consultant | Annual control assessment (P07) |

**Where roles overlap.** The Office Manager writes the risk analysis, runs most controls, and is also the Security Officer who checks them. The Owner, who approves, also works crew shifts. To make up for this, an independent consultant assesses the controls each year (P07), and the MSP's monthly report gives a second view of the technical controls.

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Health care delivery services (trip, patient care, and certification records; ePHI) | Moderate | Moderate | Moderate | Disclosure harms patients and triggers breach duties; a wrong pickup address or level of service could delay care; manual dispatch limits the availability impact (P05 MTD 4 h for dispatch) |
| Health care administration (claims, payer data) | Moderate | Moderate | Low | Financial and identity data; payers accept late claims (P05 MTD 72 h) |
| Human resources management (workforce data, certifications) | Moderate | Low | Low | Payroll and HR files in the shared drive |
| **TOP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Why availability is Moderate and not High.** The company does not answer 911 calls. A dispatch outage delays scheduled transports; it does not delay an emergency response. The worst credible harm is a missed dialysis session, which the manual dispatch procedure is meant to prevent. If the company ever takes a 911 zone, availability must be re-rated.

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 7-person company. The plan documents 46 controls that carry the HIPAA Security Rule standards, dispatch continuity, and basic cyber hygiene (see `control-implementation.csv`). All other Moderate-baseline controls are handled one of two ways:
- **Inherited** from the SaaS vendors (physical, platform, and application controls), with the platform vendor's SOC 2 report as the main evidence (P09).
- **Tailored out** for this tier, where the control addresses federal program management or organizations with their own IT staff (for example, configuration change boards and separate development environments). These are recorded as tailoring decisions, not gaps.

## 7. Authorization Boundary Description
The boundary contains what the company controls or pays someone to control on its behalf:
- **Inside:** the company's platform tenant configuration, users, and roles, including facility portal accounts (SYS-01); the suite tenant and shared drive (SYS-02); the hosted phone account, recordings, and fax settings (SYS-04); 10 devices (SYS-05); the office network (SYS-06); the vehicle hotspots and trackers (SYS-07); and the backup subscription (SYS-08).
- **Outside (external services, interconnected):** the vendors' own platforms and data centers; the billing company and its clearinghouse (SYS-03); receiving hospitals; the state EMS data system; the MSP's remote management platform; the fleet tracking service; and the AI intake assistant (SYS-09), a pilot assessed separately in P10.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Agreement |
|---|---|---|---|
| Billing company and clearinghouse (SYS-03) | Outbound trip data and PCS; inbound remittances | Demographics, insurance, level of service, mileage, certification statements | BAA and billing contract |
| Receiving hospitals (SYS-01 hospital portal) | Outbound | Patient care records | Treatment disclosure; Fla. Stat. 401.30(2) |
| State EMS data system (EMSTARS) | Outbound | Incident-level ePCR data in the state format | Rule 64J-1.014, F.A.C. |
| Facilities using the request portal (SYS-01) | Inbound requests and PCS uploads | Patient name, date of birth, pickup and destination, condition, PCS | Portal terms; facility accounts created by the Office Manager |
| Facilities by fax (SYS-04 to SYS-02) | Bidirectional | Face sheets, PCS, trip confirmations | **Phone and fax vendor BAA signed 2026-08-21 (gap until then)** |
| MSP remote management platform | Inbound administrative access | Device management | MSP BAA and service contract |
| AI intake assistant (SYS-09) | Outbound call audio; inbound suggestions | Recorded request calls, transcripts, suggested level of service, emergency flag | **Data-use terms not reviewed (gap; P10)** |
| Regional hospital | Outbound | Security questionnaire answers (no PHI) | Transport agreement |

## 9. System Component Inventory
| Component | Type | Location or provider | Owner |
|---|---|---|---|
| Operations platform tenant (SYS-01) | SaaS | Platform vendor | Office Manager |
| Productivity suite tenant and shared drive (SYS-02) | SaaS | Productivity suite vendor | Office Manager |
| Hosted phone account and recordings (SYS-04) | SaaS | Hosted phone vendor | Office Manager |
| Desktops (2), laptop (1) (SYS-05) | Endpoint | Office; the laptop travels with the Owner | Office Manager (MSP operates) |
| Rugged tablets (3), company phones (4) (SYS-05) | Mobile endpoint | Ambulances, on-call staff, Owner | Office Manager (MSP operates MDM) |
| Firewall and Wi-Fi (SYS-06) | Network | Office supply room | Office Manager (MSP operates) |
| Vehicle hotspots (2) and GPS trackers (2) (SYS-07) | Network and telematics | Ambulances | Owner |
| Backup subscription (SYS-08) | SaaS | Backup vendor (MSP subcontractor) | Office Manager (MSP operates) |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 46 controls:
- Implemented: 11
- Partially implemented: 28
- Planned: 7
- Not applicable: 0

By responsibility: 19 system-specific (the company), 24 hybrid (the company with a vendor or the MSP), 3 common/inherited (fully provided by a SaaS vendor).

### 10.2 Inherited and MSP-provided controls
| Provider | What the company relies on | Evidence | What the company must still do |
|---|---|---|---|
| Operations platform vendor | Platform security, encryption, backups and replication (CP-9), lockout (AC-7), session timeout (AC-12), audit records (AU-2, AU-11) | SOC 2 Type 2 report reviewed 2026-08-26 (P09) | Complementary user entity controls: user provisioning and removal, MFA enablement, role assignment, review of access reports and exports |
| Productivity suite vendor | Platform security, encryption at rest and in transit (SC-8, SC-28), lockout (AC-7), audit logging (AU-2) | Vendor documentation; BAA | Account management, MFA settings, sharing and forwarding settings, log review |
| Hosted phone vendor | Encrypted storage of recordings and faxes (SC-28); forwarding (CP-8) | Vendor documentation; BAA signed 2026-08-21 | Account management; recording announcement; retention settings |
| MSP | Patching (SI-2), antivirus (SI-3), firewall and Wi-Fi (SC-7, AC-18), device encryption and lock through MDM (SC-28, AC-11), backup operation (CP-9) | Monthly MSP report; P07 evidence requests | Oversight: approve exceptions, review reports monthly, annual MSP security review (P01 R-003) |
| Backup service (MSP subcontractor) | Storage of suite copies (CP-9) | None yet; restore test due 2026-09-30 | Confirm subcontractor BAA through the MSP |

**Inherited does not mean done.** Two of the platform vendor's complementary user entity controls are open gaps at the company: MFA enablement (IA-2(1)) and account removal and review (AC-2, AU-6).

### 10.3 Control assessment status
Assessed 2026-08-17 to 2026-08-19 by an independent consultant. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
Office users sign in to the suite and the billing portal with a password and a second factor (a phone authenticator app). That is appropriate for access to ePHI at the Moderate category. **The platform is the exception:** today it accepts a password alone, and the dispatch board uses a shared account. The company accepts this only until 2026-10-31, when MFA is enabled for every platform user and the dispatch board moves to named accounts with a quick sign-in on the dispatch desktop (POAM-002, POAM-003). Until then the compensating measures are a changed shared password (2026-09-08) and a weekly review of the platform's export log by the Office Manager. Facility portal users are external; they sign in with the vendor's own password rules and see only their facility's trips.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness and platform vendor report review (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **BAA:** business associate agreement
- **BLS:** basic life support
- **CAD:** computer-aided dispatch
- **EDR:** endpoint detection and response
- **EMSTARS:** Emergency Medical Services Tracking and Reporting System (Florida)
- **ePCR:** electronic patient care report
- **MDM:** mobile device management
- **MFA:** multi-factor authentication
- **MSP:** managed service provider
- **PCS:** physician certification statement
- **POA&M:** plan of action and milestones
- **TOP:** Transport Operations Platform

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-09-04 | Initial plan | Office Manager (Security Officer) |
