# System Security Plan (short form): Pharmacy Core SaaS Stack

**Organization:** Cris Santos Company (independent community pharmacy) | **Tier:** Sole Proprietorship | **Vertical:** Healthcare and Public Health
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), all headings kept with short answers | **Version:** 1.0, 2026-09-04

## 1. System Name and Identifier
Pharmacy Core SaaS Stack (**PCSS**), identifier CSC-SYS-001. It is the registry's "core business SaaS stack (email, files, client and billing records)". In a pharmacy, the client and billing records system is the pharmacy management system (PMS).

## 2. System Overview
The PCSS is everything the pharmacy uses to fill about 3,500 prescriptions a year for about 650 active patients: prescription intake (including electronic prescriptions for controlled substances, EPCS), drug utilization review, labels, claims to PBMs, PDMP reporting, refill reminders, compounding records, faxes, email, and Schedule II ordering. One pharmacist runs it; a relief pharmacist uses it about 2 days a month. Components are SYS-01 to SYS-08 in `../00_company-facts.md` section 3: the vendor-hosted PMS, an email and file suite, a counter desktop, a laptop, a phone, a cloud fax service, the store network, and a consumer AI chatbot (use restricted; see P10). There is no server and no IaaS. Most safeguards for the PMS are **inherited from the PMS vendor**; the owner is responsible for accounts, devices, the store network, data placement, and vendor contracts (P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| C-HPH-R01 | HIPAA Security Rule | 45 CFR Part 164, Subpart C |
| C-HPH-R02 | HIPAA Breach Notification Rule | 45 CFR 164.400-414 |
| C-HPH-R03 | HIPAA Security Rule NPRM (proposed, not in force) | 90 FR 898 (2025-01-06). Tracked only |
| C-HPH-R08, C-HPH-R09 | HPH Cybersecurity Performance Goals; 405(d) HICP (voluntary) | Used to choose practical safeguards |
| C-HPH-R10 | HITECH recognized security practices | 42 U.S.C. 17941 (mitigating factor in OCR enforcement) |
| DEA | EPCS pharmacy duties and recordkeeping; CSOS private key rules | 21 CFR 1311.200-1311.215, 1311.305; 21 CFR 1311.30 |
| N62-R07 (parent vertical ID) | Section 1557 patient care decision support tools | 45 CFR 92.210 (PMS DUR alerts; P10) |
| State | Breach notification; PDMP reporting; controlled substance records | Fla. Stat. 501.171; 893.055; 893.07 |
| Internal | Information Security Policy | POL-01 (P06) |

Not applicable: 42 CFR Part 2 (C-HPH-R06; not a Part 2 program), the FTC Health Breach Notification Rule (C-HPH-R05; excludes covered entities), the CMS emergency preparedness rule (C-HPH-R07; pharmacies are not a covered provider type), FDA section 524B (C-HPH-R04; manufacturer duty), and CIRCIA (C-HPH-R11; proposed only).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the pharmacist-owner on 2026-09-04.
### 4.2 System Authorization Decision
No formal authorization applies to a private pharmacy. Equivalent decision: the pharmacist-owner accepted continued operation on 2026-09-04, on condition that the three High risks in P01 (R-001, R-002, R-005) are treated by their due dates and that the relief pharmacist has an own PMS account by 2026-09-30, before any further relief shift.
### 4.3 System Operational Status
Operational. Planned changes: own accounts for each pharmacist and MFA for the administrator role at every location (2026-09-30); a separate guest Wi-Fi network (2026-10-31); accept the email and file suite BAA (2026-09-15).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner, Security Officer, Privacy Officer, risk acceptor | Pharmacist-owner | Every role (45 CFR 164.308(a)(2) designation in POL-01); also DEA registrant contact and CSOS certificate holder |
| User (workforce member) | Relief pharmacist (independent contractor) | Dispensing on relief days; follows POL-01 |
| Technical support | On-call IT consultant (BA since 2026-07-31) | Store network and device help on request; no standing access |
| Service providers | PMS vendor, cloud fax vendor (BAs); email and file suite vendor (BA terms not yet accepted) | Operate inherited controls |

## 6. System Information Types and System Categorization
| Information type (SP 800-60) | C | I | A | Rationale |
|---|---|---|---|---|
| Health care delivery services (prescriptions, patient profiles, ePHI) | Moderate | Moderate | Moderate | Disclosure triggers breach duties; a wrong drug, dose, or allergy record can harm a patient; outage beyond one business day affects patient safety (P05 MTD 24 h) |
| Controlled substance records (EPCS records, dispensing records, CSOS orders) | Moderate | Moderate | Moderate | DEA requires intact, retrievable records (21 CFR 1311.305); altered records hide diversion |
| Health care administration (claims and payments) | Moderate | Moderate | Low | Financial and identity data; claims can be submitted after recovery (P05 MTD 72 h) |
| **PCSS category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** SP 800-53B Moderate, tailored to 30 controls that carry the HIPAA safeguards and the pharmacy's EPCS and CSOS duties for a one-person pharmacy (`control-implementation.csv`). Other Moderate controls are inherited from the PMS vendor (evidence: its SOC 2 and EPCS certification reports, P09) or tailored out because they assume staff, servers, or a federal program. AC-5, AU-9, CM-3, and CA-2(1) are kept with compensating controls (see `control-implementation.csv`).

## 7. Authorization Boundary Description
- **Inside:** the pharmacy's PMS account settings and roles, the email and file suite, the cloud fax account, the counter desktop, laptop, and phone, the store network, the CSOS certificate, the AI chatbot account, and paper prescriptions and logs in the store.
- **Outside (external services):** the PMS vendor's platform and its e-prescribing network and claims switch, the cloud fax platform, the email and file suite platform, the Florida PDMP, the drug wholesaler, the card processor's terminal, and the AI chatbot vendor.

Diagram: P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Party | Data | Agreement |
|---|---|---|
| Prescribers, through the e-prescribing network (via the PMS) | New prescriptions, EPCS, refill requests and responses | PMS vendor BAA (vendor holds the network agreement) |
| PBMs, through the claims switch (via the PMS) | Real-time claims and responses (standard transactions) | PMS vendor BAA; PBM network agreements |
| Florida PDMP | Nightly controlled substance dispensing report | Required by Fla. Stat. 893.055(3)(a) |
| Cloud fax | Faxed prescriptions and refill requests | BAA |
| Email and file suite | Fax copies, compounding records, correspondence | **BAA offered but not accepted (gap)** |
| Drug wholesaler | Orders, including CSOS-signed Schedule II orders | Supply agreement (no PHI) |
| AI chatbot vendor | Patient details pasted in 6 conversations | **No BAA; PHI use stopped (gap)** |

## 9. System Component Inventory
| Component | Type | Owner |
|---|---|---|
| PMS tenant (SYS-01) | SaaS | Pharmacist-owner |
| Email and file suite (SYS-02) | SaaS | Pharmacist-owner |
| Counter desktop (SYS-03), with label printer, scanner, CSOS certificate | Endpoint | Pharmacist-owner |
| Laptop (SYS-04) | Endpoint | Pharmacist-owner |
| Mobile phone (SYS-05) | Personal endpoint | Pharmacist-owner |
| Cloud fax (SYS-06) | SaaS | Pharmacist-owner |
| Store network (SYS-07) | ISP router with Wi-Fi | Pharmacist-owner (router supplied by the ISP) |
| AI chatbot account (SYS-08) | Consumer SaaS | Pharmacist-owner |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 30 controls:
- Implemented: 8
- Partially implemented: 19
- Planned: 3

Inheritance: 3 fully inherited from the PMS vendor (AC-3, AU-2, AU-9), 13 hybrid (a vendor operates the mechanism and the owner configures or uses it correctly), and 14 the owner's alone (AC-11, AT-2, AU-6, CA-2(1), CM-3, CP-2, IA-5, IR-6, IR-8, MP-6, PE-3, RA-3, SA-9, SC-12).

**Key safeguards per CSF Function:**
| Function | Key safeguards |
|---|---|
| Govern | POL-01; BAAs and vendor report reviews (SA-9); owner holds all roles |
| Identify | Risk analysis (RA-3); BIA (P05) |
| Protect | Own accounts and MFA (IA-2, IA-2(1), gaps); desktop encryption (SC-28, gap); CSOS key protection (SC-12, gap); separate guest network (SC-7, gap) |
| Detect | PMS and EPCS audit trail (AU-2, AU-9, inherited); daily EPCS audit report review (AU-6, planned) |
| Respond | PMS vendor ransomware runbook (IR-8); DEA one-business-day report (IR-6) |
| Recover | PMS vendor backups (CP-9, inherited); paper downtime kit and coverage arrangement (CP-2) |

### 10.2 Control assessment status
Self-assessed 2026-08-03 to 2026-08-07 with the IT consultant. See P07.

## 11. Digital Identity Acceptance Statement
PMS web sign-in from outside the store requires a password and a second factor on the owner's phone, which is appropriate for remote access to ePHI at a Moderate categorization. Inside the store, the PMS accepts a password alone, and one account is shared, which is **not acceptable** for an administrator account or for controlled substance records that must name the person who dispensed (21 CFR 1311.205(b)(10)(iii)). Own accounts and MFA for the administrator role at every location are due 2026-09-30. Patients do not sign in to any pharmacy system; the refill phone line uses the prescription number only.

## 12. Referenced Artifacts
Scenario facts, P01 risk register, P03 gap analysis, P04 SaaS control map, P05 BIA, P06 POL-01, P07 assessment and POA&M, P08 runbook and notification matrix, P09 SOC 2 self-check and vendor review, P10 AI use assessment.

## 13. Acronym List and Glossary
- **BA / BAA:** business associate / business associate agreement
- **CSOS:** Controlled Substance Ordering System (DEA digital certificates for electronic Schedule II orders)
- **DUR:** drug utilization review
- **EPCS:** electronic prescriptions for controlled substances
- **ePHI:** electronic protected health information
- **MFA:** multi-factor authentication
- **PBM:** pharmacy benefit manager
- **PCSS:** Pharmacy Core SaaS Stack
- **PDMP:** prescription drug monitoring program
- **PMS:** pharmacy management system

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-09-04 | Initial short-form plan | Pharmacist-owner |
