# System Security Plan: Train Dispatch and Operations Back Office (TDOB)

**Organization:** Cris Santos Company, LLC (short line freight railroad, 16 route miles) | **Tier:** Micro | **Vertical:** Transportation Systems
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Train Dispatch and Operations Back Office (**TDOB**), identifier CSC-SYS-001.

## 2. System Overview
The TDOB supports every operating and business process of the railroad: issuing movement authority (track warrants and track-and-time), radio contact with crews, the daily interchange turn and local switching, car management and interchange EDI with the Class I, hazmat car handling, track inspection records, billing, and payroll records. It serves 7 employees, 6 customers, and the connecting Class I railroad.

The railroad owns almost no IT infrastructure. The operations system is vendor SaaS, a managed service provider (MSP) runs the office equipment, and the radio system is the only operations technology the company runs itself. This plan therefore says, for each control, what the railroad does itself, what the MSP does for it, and what it inherits from a SaaS vendor.

**Why the system is not called a "PTC back office".** The railroad has no positive train control (PTC) system. It has no installation duty (49 CFR 236.1005(b)(1)), and its 2.5-mile interchange move on the Class I's PTC line runs unequipped under the exception for Class II and III trains in 236.1006(b)(4). The system that carries movement authority is the dispatch back office described here.

**Major components:**
- **SYS-01:** short line operations system (vendor SaaS): authorities with conflict checking, train sheets, slow orders and bulletins, car inventory, waybills and EDI, hazmat car list, invoicing
- **SYS-02:** productivity suite (SaaS): email and the shared drive
- **SYS-03:** 3 desktops (dispatch desk, office, shop), 2 laptops, 3 rugged crew tablets (MSP-managed)
- **SYS-04:** office network: firewall, office and enginehouse Wi-Fi, one internet line (MSP-managed)
- **SYS-05:** cloud backup of the productivity suite (SaaS, operated by the MSP)
- **SYS-06:** radio dispatch system: base station and console at the desk, repeater at the mile 8 tower, locomotive and handheld radios
- **SYS-07:** locomotive telematics on the 2 road locomotives (vendor portal; monitoring only)

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| C-TRANSPORTATION-S01 | TSA Security Coordinator; reporting significant security concerns, including cyber attacks, within 24 hours | 49 CFR 1570.201; 1570.203 and Appendix A to part 1570 |
| C-TRANSPORTATION-S03 | Protection of Sensitive Security Information | 49 CFR 1520.9 |
| C-TRANSPORTATION-S05 | FRA accident/incident reporting | 49 CFR part 225 |
| C-TRANSPORTATION-S06 | Hazmat transportation security plan and security training (propane) | 49 CFR 172.800(b)(3); 172.802; 172.704(a)(4)-(5); 174.9 |
| C-TRANSPORTATION-S07 | Florida breach notification (employee personal information) | Fla. Stat. 501.171 |
| C-TRANSPORTATION-BM | NIST CSF 2.0 (voluntary benchmark) | CSF 2.0 |
| C-TRANSPORTATION-R06, R07 | TSA surface cyber NPRM and CIRCIA (proposed, not in force) | 89 FR 88488; 89 FR 23644. Tracked only |
| Internal | Security policies POL-02, POL-03, POL-04 | P06 |

Not applicable:
- TSA rail cyber directives SD 1580-21-01E and SD 1580/82-2022-01E (C-TRANSPORTATION-R01): the railroad is not in 49 CFR 1580.101 and has not been designated by TSA (P03 section 1).
- 49 CFR part 1580 subpart C (C-TRANSPORTATION-S02): no rail security-sensitive materials are carried.
- FRA PTC installation (C-TRANSPORTATION-S04): no duty; see section 2.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Owner and General Manager on 2026-08-31.

### 4.2 System Authorization Decision
The railroad is not a federal agency, so there is no formal authorization. The equivalent internal decision: on 2026-08-31 the Owner and General Manager accepted continued operation of the TDOB, on the condition that the POA&M items in P07 are completed by their dates and the High risks in P01 are treated by 2026-12-31.

### 4.3 System Operational Status
Operational. Planned changes, all due by 2026-12-31: replacement of the dispatch desktop with a supported operating system and the certified radio console version (P01 R-007), named crew logins with MFA in SYS-01 (R-003), EDR (R-001), backup upgrade and a weekly SYS-01 data export (R-005), and a cellular failover router (R-010).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner and risk acceptor | Owner and General Manager | Overall accountability; accepts Moderate and higher risk; approves this plan, policies, and spending. Primary TSA Security Coordinator and primary dispatcher |
| Security Lead | Office Manager | Day-to-day security; directs the MSP; maintains this plan, the risk register, and the inventory |
| Alternate Security Coordinator and relief dispatcher | Roadmaster | TSA contact when the General Manager is unavailable; relief dispatcher; AI pilot owner (P10) |
| Crew users | Locomotive Engineer, Conductor, Mechanic | Tablet and radio users; report incidents |
| IT operations | MSP | Devices, patching, antivirus, firewall, Wi-Fi, backup administration |
| Independent assessor | Cybersecurity consultant | Annual control assessment (P07) |

**Overlapping roles.** The General Manager approves the plan, accepts the risk, and also operates the main control (dispatch). The Office Manager writes the plan and runs most of the controls. The independent assessor (P07) and the operations SaaS vendor's SOC 2 report (P09) are the outside checks.

## 6. System Information Types and System Categorization
Information types follow the NIST SP 800-60 Vol. 2 Rev. 1 approach, with names adapted to a railroad. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Movement authority and train operations (warrants, track-and-time, train sheets, slow orders) | Low | Moderate | Moderate | A wrong or missing authority could lead to a collision or a roadway worker strike. It is rated Moderate, not High, because the operating rules require a radio repeat-back of every authority, the maximum speed is 10 mph, and only one train runs at a time on most days. Paper dispatch limits the availability impact to one shift (P05 MTD 8 h) |
| Hazmat shipment and security information (hazmat car list, shipping documents, security plan, SSI) | Moderate | Moderate | Low | Disclosure of the security plan or SSI could help an attacker target propane cars; cars can be held if data is unavailable (P05 MTD 24 h) |
| Car management and commercial data (waybills, EDI, invoices) | Low | Moderate | Low | Errors misroute cars or bill wrongly; the Class I's portal is a fallback |
| Employee information (HR, certifications, drug and alcohol testing records) | Moderate | Low | Low | Personal information covered by Fla. Stat. 501.171 |
| **TDOB category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 7-person railroad. The plan documents 42 controls that carry the TSA and hazmat security duties and basic cyber hygiene (see `control-implementation.csv`). All other Moderate-baseline controls are handled one of two ways:
- **Inherited** from the SaaS vendors (physical, platform, and application controls), with the operations SaaS vendor's SOC 2 report as the main evidence (P09).
- **Tailored out** for this tier, where the control addresses federal program management or organizations with dedicated IT staff (for example, configuration change boards and separate development environments). These are recorded as tailoring decisions, not gaps.

## 7. Authorization Boundary Description
The boundary contains what the railroad controls or pays someone to control on its behalf:
- **Inside:** the railroad's SYS-01 tenant configuration and user roles, the productivity suite tenant and shared drive (SYS-02), 8 devices (SYS-03), the office network (SYS-04), the backup subscription (SYS-05), the radio dispatch system (SYS-06), and the telematics portal account and onboard units (SYS-07).
- **Outside (external services, interconnected):** the vendors' own platforms and data centers; the Class I's EDI service and dispatcher; the accounting, payroll, and HR SaaS (SYS-08); the MSP's remote management platform; and the AI defect detection pilot (SYS-09, assessed separately in P10).
- **Not connected to anything:** the grade crossing warning systems (standalone circuits maintained by the contract signal maintainer).

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Agreement |
|---|---|---|---|
| Connecting Class I, interchange EDI (through SYS-01) | Bidirectional | Waybills, interchange reports, car hire data | Interchange agreement; SYS-01 vendor terms |
| Connecting Class I dispatcher | Bidirectional (radio and phone) | Authority for the 2.5-mile interchange move | Interchange agreement; Class I operating rules |
| Customers (email, SYS-01 customer notices) | Bidirectional | Car orders, switch requests, invoices | Customer contracts |
| Accounting, payroll, and HR SaaS (SYS-08) | Outbound from the Office Manager | Hours, payroll, employee records | Vendor terms |
| MSP remote management platform | Inbound administrative access | Device management | MSP service contract (**no security terms; gap**) |
| AI defect detection service (SYS-09) | Outbound video, inbound defect flags | Track imagery with location | Vendor pilot terms (**not reviewed; gap; P10**) |
| TSA (TSOC and Security Coordinator correspondence) | Bidirectional | Security reports; TSA bulletins, some marked SSI | 49 CFR 1570.201, 1570.203; 1520.9 |

## 9. System Component Inventory
| Component | Type | Location or provider | Owner |
|---|---|---|---|
| Operations system tenant (SYS-01) | SaaS | Operations SaaS vendor | Office Manager |
| Productivity suite tenant and shared drive (SYS-02) | SaaS | Productivity suite vendor | Office Manager |
| Desktops (3), laptops (2), crew tablets (3) (SYS-03) | Endpoint | Office and enginehouse; laptops with the General Manager and Office Manager; tablets with the crew and Roadmaster | Office Manager (MSP operates) |
| Firewall and Wi-Fi (SYS-04) | Network | Office network closet | Office Manager (MSP operates) |
| Suite backup subscription (SYS-05) | SaaS | Backup vendor (held by the MSP) | Office Manager (MSP operates) |
| Base station, console, repeater, mobile and handheld radios (SYS-06) | Operations technology | Dispatch desk; mile 8 tower; locomotives | Owner and General Manager (radio service vendor repairs) |
| Telematics units and portal (SYS-07) | Operations technology and SaaS | 2 road locomotives; telematics vendor | Mechanic |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 42 controls:
- Implemented: 11
- Partially implemented: 25
- Planned: 6
- Not applicable: 0

By responsibility: 20 system-specific (the railroad), 18 hybrid (the railroad with a vendor or the MSP), 4 common/inherited (fully provided by a SaaS vendor or the MSP).

### 10.2 Inherited and MSP-provided controls
| Provider | What the railroad relies on | Evidence | What the railroad must still do |
|---|---|---|---|
| Operations SaaS vendor | Platform security, encryption, backups and replication (CP-9), account lockout (AC-7), audit records (AU-2, AU-11), role enforcement (AC-3) | SOC 2 Type 2 report reviewed 2026-08-19 (P09) | Complementary user entity controls: named user accounts, timely removal, MFA enforcement, role assignment, review of user and audit reports |
| Productivity suite vendor | Platform security, encryption in transit and at rest (SC-8, SC-28), lockout (AC-7), audit logging (AU-2) | Vendor documentation | Account management, MFA settings, sharing settings, log review |
| MSP | Patching (SI-2), antivirus (SI-3), firewall and Wi-Fi (SC-7, AC-18), device encryption (SC-28), backup operation (CP-9), device lock (AC-11) | Monthly MSP reports; P07 evidence requests | Oversight: approve exceptions (such as the dispatch desktop), review reports monthly, annual MSP security review (P01 R-004) |
| Backup service (held by the MSP) | Storage of suite copies (CP-9) | None yet; restore test due 2026-09-30 | Confirm terms and access through the MSP |
| Radio service vendor | Repair of the base station and repeater | Service call agreement | Keep the spare base radio tested |

**Inherited does not mean done.** Two of the operations SaaS vendor's complementary user entity controls are open gaps at the railroad: named user accounts (the shared crew login, IA-2, AC-2) and review of user and audit reports (AU-6).

### 10.3 Control assessment status
Assessed 2026-08-04 to 2026-08-06 by an independent consultant. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
The General Manager and Office Manager sign in to SYS-01 and the suite with a password and a phone authenticator app. Number matching for push approvals is being enabled after the 2025 mailbox compromise (P01 R-009). The crew uses a shared password-only login on company tablets today. That is not acceptable for a system that records authority acknowledgments, and named crew accounts with MFA are planned by 2026-11-30 (R-003). Until then, the radio repeat-back and the dispatcher's paper log are the authoritative record of who acknowledged an authority.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness and vendor report review (P09), AI assessment (P10). Hazmat security plan (reviewed 2025-03-18; update due, P03).

## 13. Acronym List and Glossary
- **EDI:** electronic data interchange (waybills and interchange reports with the Class I)
- **EDR:** endpoint detection and response
- **MFA:** multi-factor authentication
- **MSP:** managed service provider
- **POA&M:** plan of action and milestones
- **PTC:** positive train control
- **SSI:** Sensitive Security Information (49 CFR part 1520)
- **TDOB:** Train Dispatch and Operations Back Office
- **Track warrant / track-and-time:** written movement authority for trains and for roadway workers on the main track
- **TSOC:** TSA Transportation Security Operations Center

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan | Office Manager (Security Lead) |
