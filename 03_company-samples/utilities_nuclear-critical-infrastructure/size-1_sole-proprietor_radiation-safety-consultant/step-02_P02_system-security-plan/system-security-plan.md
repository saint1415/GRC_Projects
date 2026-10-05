# System Security Plan (short form): Core Business SaaS Stack

**Organization:** Cris Santos Company (independent radiation safety consultant) | **Tier:** Sole Proprietorship | **Vertical:** Nuclear Reactors, Materials, and Waste
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), all headings kept with short answers | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Core Business SaaS Stack (**CBSS**), identifier CSC-SYS-001. The name keeps the registry default ("Core business SaaS stack: email, files, client and billing records").

## 2. System Overview
The CBSS is everything the consultancy uses to plan and support outage work, analyze survey and dose data, write client reports, exchange documents with clients, track instrument calibration, and bill. One person, the owner-consultant, uses and runs it. Components are SYS-01 to SYS-08 in `../00_company-facts.md` section 3: a business email and file suite, a main laptop, a phone, an older field laptop with six survey instruments, an accounting SaaS, the owner's access to two client portals, the home network, and two AI features (see P10), plus one USB drive and paper records. There is no server and no IaaS. Most platform safeguards are **inherited from the SaaS providers and the clients**; the owner is responsible for identities, devices, media, data placement, and keeping the clients' contract terms (P04).

What makes this small system sensitive is what the clients put into it: Client A's outage work packages and survey maps, and Client B's Part 37 security information (its security plan, approved-individuals list, and security review reports). The business holds no radioactive material, no license, and no Safeguards Information.

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| C-NUCLEAR-S01 | Client A Contractor Security Requirements (from Client A's 73.54 and 73.56 programs) | CSR-A (1)-(10), signed 2026-02-16 |
| C-NUCLEAR-R01 | NRC cyber security rule for power reactors (Client A's duty; reaches the owner through CSR-A; 73.54(d)(1) names contractors) | 10 CFR 73.54 |
| C-NUCLEAR-R03 | NRC cyber security event notifications (Client A's duty; CSR-A (5) feeds it) | 10 CFR 73.77 |
| C-NUCLEAR-S02 | Duties of an individual with unescorted access | 10 CFR 73.56(f), (g) |
| C-NUCLEAR-S03 | Safeguards Information (conditional; none held) | 10 CFR 73.21, 73.22 |
| C-NUCLEAR-S04 | Part 37 protection of information, through Client B's Florida license condition and CSIA-B | 10 CFR 37.43(d), 37.55; CSIA-B (1)-(6) |
| C-NUCLEAR-S05 | Florida data security and breach notice (one W-9) | Fla. Stat. 501.171 |
| Internal | Information Security Policy | POL-01 (P06) |

Not applicable: 10 CFR 73.110, NERC CIP, and CIRCIA (proposed only). See P03 section 1.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the owner-consultant on 2026-08-31.
### 4.2 System Authorization Decision
No formal authorization applies to a private consultancy. Equivalent decision: the owner accepted continued operation on 2026-08-31, on condition that the High risks in P01 (R-001, R-002) are treated by their due dates, and that the Client A items (encrypted Client A-only media, standard daily account, MFA changes, runbook walkthrough) are done before the fall outage starts on 2026-10-19.
### 4.3 System Operational Status
Operational. Planned changes: standard daily account and authenticator-app MFA (2026-09-15); Client A-only encrypted USB drive (2026-10-09); separate business wireless network (2026-10-31); replacement of the field laptop operating system or an isolated, offline field laptop (2026-12-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner, security and compliance lead, incident commander, risk acceptor | Owner-consultant | Every role. Independence is limited; P07 explains how outside checks compensate |
| Technical support | On-call IT technician (NDA since 2026-07-14) | Laptop, phone, and network help on request; no standing access; no access to client folders |
| Field support | Per-diem health physics technician | Client A surveys only; no access to the CBSS |
| Service providers | Email and file suite provider, accounting SaaS vendor, calibration-tracking SaaS vendor | Operate inherited controls |
| Client-operated services | Client A (contractor portal), Client B (secure share) | Operate their portals and MFA |

## 6. System Information Types and System Categorization
Ratings follow the SP 800-60 method (confidentiality, integrity, availability) using the BIA (P05) impact levels.

| Information type | C | I | A | Rationale |
|---|---|---|---|---|
| Client security information (Client B Part 37 security plan, approved-individuals list, review reports; Client A security-related documents) | Moderate | Moderate | Low | Disclosure could help an adversary plan theft or sabotage and would break CSIA-B and CSR-A; the client keeps the original |
| Radiological survey, dose, and shielding data | Low | Moderate | Moderate | Altered or lost data could lead to unplanned worker dose (P05 BP-01 MTD 24 h during outages) |
| Business records (billing, W-9) | Moderate | Low | Low | One Social Security number (Fla. Stat. 501.171) |
| **CBSS category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** SP 800-53B Moderate, tailored to 26 controls that carry the client contract terms and basic hygiene for a one-person consultancy (`control-implementation.csv`). Other Moderate controls are inherited from the SaaS providers (evidence: the suite provider's SOC 2 report, P09) or the clients' portals, or are tailored out because they assume staff, servers, or a federal system.

## 7. Authorization Boundary Description
- **Inside:** the owner's suite account and its settings, the main laptop, the phone, the field laptop and survey instruments, the USB drive, the accounting and calibration-tracking SaaS accounts, the owner's credentials for the client portals, the home network as used for business, and paper in the home office.
- **Outside (external or interconnected):** the SaaS providers' platforms, Client A's contractor portal and plant networks, Client B's secure share, the calibration laboratory, and the AI chat service. Client A's plant digital assets are never connected to anything inside the boundary (CSR-A (1)); the only path is portable media through Client A's kiosk (CSR-A (2)).

Diagram: P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Party | Data | Agreement |
|---|---|---|
| Client A contractor portal | Work packages, survey maps, dose reports | CSR-A |
| Client A radiation protection workstations (on site) | Survey data files, by kiosk-scanned USB drive | CSR-A (2) |
| Client B secure share | Security plan, approved-individuals list, review reports | CSIA-B |
| Calibration laboratory and calibration-tracking SaaS | Instrument serial numbers, calibration results, readings with site tags | Vendor terms (**not reviewed; gap**) |
| Accounting SaaS | Invoices, W-9 copy | Vendor terms (**not reviewed; gap**) |
| Consumer AI chat assistant | One paragraph of a Client B report draft (2026-06-09) | **None; use stopped (gap)** |

## 9. System Component Inventory
| Component | Type | Owner |
|---|---|---|
| Email and file suite (SYS-01) | SaaS, business plan | Owner-consultant |
| Main laptop (SYS-02) | Endpoint, encrypted | Owner-consultant |
| Mobile phone (SYS-03) | Personal endpoint | Owner-consultant |
| Field laptop and six survey instruments (SYS-04) | Endpoint (unsupported OS) and instruments | Owner-consultant |
| Accounting SaaS (SYS-05) | SaaS | Owner-consultant |
| Client portal accounts (SYS-06) | Client-operated | Client A; Client B |
| Home network (SYS-07) | ISP router and Wi-Fi | Owner-consultant |
| AI features (SYS-08) | SaaS feature; consumer app | Owner-consultant |
| USB drive | Removable media, unencrypted | Owner-consultant |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 26 controls:
- Implemented: 5
- Partially implemented: 20
- Planned: 1

Inheritance: 1 fully inherited from the suite provider (AU-2), 11 hybrid (a provider or client operates the mechanism, the owner configures or uses it correctly), and 14 the owner's alone.

**Key safeguards per CSF Function:**
| Function | Key safeguards |
|---|---|
| Govern | POL-01; client agreements as rules of behavior (PL-4); vendor oversight (SA-9, gap) |
| Identify | Risk assessment (RA-3); BIA (P05); register of client information (planned, MP-6) |
| Protect | MFA (IA-2(1), IA-2(2)); laptop encryption (SC-28); kiosk-scanned media (MP-7); access enforcement on shares (AC-3) |
| Detect | Suite sign-in and sharing logs (AU-2, inherited); monthly review of sign-ins and sharing (POL-01 7.7) |
| Respond | Runbook and contract notice clocks (IR-8, IR-6) |
| Recover | Suite version history (CP-9); peer coverage (CP-2, planned) |

### 10.2 Control assessment status
Self-assessed 2026-07-20 to 2026-07-24 with the IT technician. See P07.

## 11. Digital Identity Acceptance Statement
Client A and Client B enforce MFA on their own portals, which is their decision. The email suite uses a password and a text message code; because the suite holds client report drafts, the owner moves it to an authenticator app by 2026-09-15. The accounting and calibration-tracking SaaS use a password only until MFA is turned on (2026-09-15). No customer or public users sign in to anything in the boundary.

## 12. Referenced Artifacts
Scenario facts, P01 risk register, P03 gap analysis, P04 SaaS control map, P05 BIA, P06 POL-01, P07 assessment and POA&M, P08 runbook and notification matrix, P09 SOC 2 self-check and vendor review, P10 AI use assessment. Client agreements CSR-A and CSIA-B are held in the owner's contract folder (not reproduced here).

## 13. Acronym List and Glossary
- **CBSS:** Core Business SaaS Stack
- **CSIA-B:** Client B Confidentiality and Security Information Agreement
- **CSR-A:** Client A Contractor Security Requirements
- **MFA:** multi-factor authentication
- **RSO:** Radiation Safety Officer
- **SGI:** Safeguards Information (10 CFR 73.21)

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial short-form plan | Owner-consultant |
