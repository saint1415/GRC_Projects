# System Security Plan (short form): Farm Management and Irrigation Control Platform

**Organization:** Cris Santos Company (precision-agriculture crop farm) | **Tier:** Sole Proprietorship | **Vertical:** Agriculture, Forestry, Fishing and Hunting
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), all headings kept with short answers | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Farm Management and Irrigation Control Platform (**FMICP**), identifier CSC-SYS-001.

## 2. System Overview
The FMICP is everything the farm uses to grow, protect, record, and sell its crops: the farm management and irrigation software (SYS-01), the pump controller, pivot panel, probes, and freeze sensor it controls (SYS-06), the laptop, phone, and tablet, the home network, the drone, the AI yield trial, the accounting and banking SaaS, and the booking and payment systems. Components are SYS-01 to SYS-10 in the intake [asset inventory](../step-00_P00_intake/asset-inventory.csv). One person, the owner-operator, uses and runs all of it. There is no server and no IaaS. Most application safeguards are **inherited from the SaaS vendors**; the owner is responsible for accounts, data, devices, the home network, and the field devices (P04).

The part that matters most is the path from SYS-01 to the pump and pivot: anyone who controls the SYS-01 administrator or technician account can start or stop irrigation and silence the freeze alarm (P05 BP-01).

## 3. Laws, Regulations, and Policies Affecting the System
| Source | Requirement | Citation |
|---|---|---|
| Benchmark (voluntary) | NIST Cybersecurity Framework 2.0 | NIST CSWP 29 (2024-02-26) |
| OT guide (voluntary) | Guide to Operational Technology Security | NIST SP 800-82 Rev. 3 (2023) |
| Federal (binding) | Produce Safety Rule qualified exemption: point-of-purchase and Internet notice; eligibility records; record retention and availability | 21 CFR 112.6, 112.7, 112.164, 112.166 |
| Federal (binding) | Small UAS rules (safety, not cybersecurity): remote pilot certificate, registration, safety event reports | 14 CFR 107.12, 107.13, 107.9 |
| State (binding) | Data security, disposal, and breach notice (a sole proprietorship is a covered entity) | Fla. Stat. 501.171 |
| Contract | Card processor merchant terms; FMIS, booking, and AI vendor terms; irrigation dealer service agreement | Contracts |
| Internal | Information Security Policy | POL-01 (P06) |

Not applicable: 21 CFR Part 121 (N11-R01), because farms do not register as food facilities (21 CFR 1.226(b), 121.1); H-2A rules, because the farm has no employees. Applicability was decided in the intake [obligations register](../step-00_P00_intake/obligations-register.csv); see also P03 section 1.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the owner-operator on 2026-08-31.
### 4.2 System Authorization Decision
No formal authorization applies to a private farm. Equivalent decision: the owner-operator accepted continued operation on 2026-08-31, on condition that the High risks in P01 (R-001, R-002, R-005) are treated by their due dates and that every irrigation and freeze-alarm action is done before freeze season starts (2026-11-30).
### 4.3 System Operational Status
Operational. Planned changes: MFA on SYS-01 and the booking platform (2026-09-15); separate networks for customer Wi-Fi and the pump house (2026-11-15); standalone freeze alarm (2026-11-15); end of the AI yield trial terms review (2026-10-31, P10).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner, security lead, risk acceptor, incident lead | Owner-operator | Every role (designated in writing in POL-01) |
| Technical support | On-call IT technician (local computer repair shop) | Laptop, phone, and router help on request; no standing access |
| OT support | Irrigation dealer | Pump controller and pivot panel service; technician account in SYS-01 |
| Service providers | FMIS vendor, booking platform vendor, card processor, accounting SaaS vendor, AI yield vendor | Operate inherited controls |

## 6. System Information Types and System Categorization
SP 800-60's information type catalog is built for federal missions and has no farm operations type. The types below are author-defined following the SP 800-60 method; impact levels follow FIPS 199.

| Information type | C | I | A | Rationale |
|---|---|---|---|---|
| Irrigation and freeze-protection control (schedules, setpoints, alarm thresholds) | Low | Moderate | Moderate | A wrong command can drown or burn a crop or over-apply fertilizer; on a freeze night a lost alarm can cost the strawberry crop. Manual operation at the pump house keeps availability impact at Moderate (P05 BP-01) |
| Field, exemption, and program records | Low | Moderate | Low | Records must be accurate to show the qualified exemption (21 CFR 112.7) and support crop insurance; a few days of downtime is tolerable (P05 BP-03) |
| Personal information (W-9 data; booking accounts held by the vendor) | Moderate | Low | Low | Names with Social Security numbers, and account credentials, trigger Fla. Stat. 501.171 notice if accessed |
| Farm operational and yield data; customer contact lists | Moderate | Low | Low | Commercially sensitive; little harm if briefly unavailable |
| **FMICP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** SP 800-53B Moderate, tailored to 27 controls that matter for a one-person farm (`control-implementation.csv`), with the SP 800-82 Rev. 3 OT guidance applied to SYS-06. Other Moderate controls are either inherited from the SaaS vendors (evidence: the FMIS vendor's SOC 2 report, P09) or tailored out because they assume staff, servers, software development, or a federal program. AC-5, AU-9, CM-3, and CA-2(1) are kept with compensating controls (see `control-implementation.csv`).

## 7. Authorization Boundary Description
The boundary was drawn from the intake [asset inventory](../step-00_P00_intake/asset-inventory.csv): SYS-01 to SYS-10 (with the SYS-01 scheduling module, AI-002) and the paper files (OTH-01) are inside; the tractor guidance display (OTH-02) and the public chatbot (AI-003, governed in P10) are outside.
- **Inside:** the owner's account settings and users in SYS-01, SYS-08, SYS-09, and SYS-10; the email and file account; the laptop, phone, and tablet; the home router, access point, and customer Wi-Fi; the pump controller, pivot panel, probes, and freeze sensor; the drone; paper program documents in the home office.
- **Outside (external services):** the SaaS platforms themselves, the card processor, the pivot panel's cellular connectivity service (run by the FMIS vendor and its carrier), the internet provider, the bank, and the tractor's guidance display (offline; its files enter by USB stick).

Diagram: P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Party | Data | Agreement |
|---|---|---|
| FMIS vendor (SYS-01) | Field records; irrigation commands and alarms | Subscription terms; SOC 2 report reviewed (P09) |
| Irrigation dealer | Remote control and settings of the pump and pivot through SYS-01 | Service agreement **with no security terms (gap)** |
| Booking platform vendor (SYS-10) | Customer accounts, reservations, payments | Subscription terms; third-party agent under Fla. Stat. 501.171(1)(h) |
| Card processor | Card transactions (encrypted at the reader) | Merchant terms |
| AI yield vendor (SYS-08) | Drone imagery; block yields | **Click-through terms allow model training on farm data (gap, P10)** |
| Accounting SaaS vendor (SYS-09) and tax preparer | Books; W-9 data | Subscription terms; engagement letter |
| Crop insurance agent; buying point | Acreage, production, settlement sheets | Policy; buying point contract |

## 9. System Component Inventory
| Component | Type | Owner |
|---|---|---|
| FMIS and irrigation module tenant (SYS-01) | SaaS | Owner-operator |
| Email and file account (SYS-02) | Consumer SaaS | Owner-operator |
| Laptop (SYS-03) | Endpoint | Owner-operator |
| Phone and tablet (SYS-04) | Endpoints | Owner-operator |
| Router, outdoor access point, customer Wi-Fi (SYS-05) | Network | Owner-operator (router supplied by the internet provider) |
| Pump controller, pivot panel and cellular modem, 12 soil probes, freeze sensor (SYS-06) | OT (about 16 devices) | Owner-operator; serviced by the irrigation dealer |
| Camera drone and ground station (SYS-07) | Drone | Owner-operator |
| AI yield prediction tenant (SYS-08) | SaaS (trial) | Owner-operator |
| Accounting SaaS and online banking (SYS-09) | SaaS | Owner-operator |
| Booking platform, card reader, email marketing service (SYS-10) | SaaS and processor service | Owner-operator |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 27 controls:
- Implemented: 8
- Partially implemented: 16
- Planned: 3

Inheritance: 2 fully inherited from the vendors (AC-3, AU-9), 11 hybrid (a vendor operates the mechanism and the owner configures or uses it correctly), and 14 the owner's alone (AC-6, AC-18, AT-2, AU-6, CA-2(1), CM-3, CM-8, CP-2, IA-5, IR-8, PE-3, RA-3, SA-9, SI-12).

**Key safeguards per CSF Function:**
| Function | Key safeguards |
|---|---|
| Govern | POL-01; owner holds every role; vendor and dealer terms (SA-9, gap) |
| Identify | Risk assessment (RA-3); BIA (P05); device list (CM-8) |
| Protect | MFA (IA-2(1), gap on SYS-01); unique passwords and no defaults (IA-5, gap); separate networks (SC-7, gap); laptop encryption (SC-28) |
| Detect | SYS-01 activity log (vendor records it); monthly review (AU-6, planned); freeze and pressure alarms |
| Respond | Ransomware and account takeover runbook (IR-8); local/remote selector to cut off remote commands |
| Recover | Manual irrigation; vendor backups (CP-9); farm-held exports (gap); mutual-aid neighbor (CP-2) |

### 10.2 Control assessment status
Self-assessed 2026-07-13 to 2026-07-17 with the on-call IT technician. See P07.

## 11. Digital Identity Acceptance Statement
Email, online banking, and the accounting SaaS require a password and a second factor. The SYS-01 administrator account, which can start and stop irrigation, and the booking platform admin account use a password only until MFA is turned on (2026-09-15); for an account that can affect a crop in one night this is not acceptable, and it is POAM-001. Text-message codes on email are accepted for now and will move to an authenticator app with the password manager. Customers use the booking platform's own sign-in, outside this boundary.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), intake evidence, inventories and obligations register ([step-00](../step-00_P00_intake/intake-report.md)), P01 risk register, P03 gap analysis, P04 SaaS control map, P05 BIA, P06 POL-01, P07 assessment and POA&M, P08 runbook, P09 SOC 2 self-check and vendor review, P10 AI use assessment.

## 13. Acronym List and Glossary
- **FMIS:** farm management information system (SYS-01)
- **FMICP:** Farm Management and Irrigation Control Platform
- **Hand-Off-Auto:** a panel switch that lets the owner run a pump by hand, stop it, or hand control to the controller
- **MFA:** multi-factor authentication
- **OT:** operational technology (the pump controller, pivot panel, probes, and sensor)
- **Qualified exemption:** the Produce Safety Rule exemption in 21 CFR 112.5

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial short-form plan | Owner-operator |
