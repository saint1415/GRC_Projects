# System Security Plan: ERP and Job Scheduling Platform (EJSP)

**Organization:** Cris Santos Company, LLC (transformer repair and remanufacturing shop, Florida) | **Tier:** Micro | **Vertical:** Critical Manufacturing
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
ERP and Job Scheduling Platform (**EJSP**), identifier CSC-SYS-001.

## 2. System Overview
The EJSP runs the business side of the shop: quotes, repair and rewind work orders, the job scheduling board, inventory and purchasing, test reports, shipping, invoicing, and email with customers. It serves 7 employees and about 25 active customers, including 6 utilities that buy rebuilt transformers to restore power after storms. It is the registry's "ERP and production scheduling system" at micro scale: a SaaS job-shop ERP with a scheduling board, plus the test PC that produces the test report every shipment needs.

The shop owns very little infrastructure. Most of the EJSP is vendor SaaS, a managed service provider (MSP) runs the computers and network, and the test PC is supported by the test set vendor. For each control, this plan says what the shop does itself, what the MSP does for it, and what it inherits from a SaaS vendor.

**Major components:**
- **SYS-01:** cloud ERP for job shops (vendor SaaS): jobs, scheduling board, inventory, purchasing, invoicing, accounting, customer portal
- **SYS-02:** productivity suite (SaaS): email, shared drive (rewind data sheet library, test report copies, customer drawings, FCI, HR files)
- **SYS-03:** 3 office desktops, 2 laptops, 1 shop-floor PC, 2 shop tablets (MSP-managed)
- **SYS-04:** office and shop network: firewall and router, one Wi-Fi network, one internet line (MSP-managed)
- **SYS-05 (test PC only):** the test bay computer that runs the test set software, holds the local test database, and produces test reports
- **SYS-08:** SaaS-to-SaaS backup of the productivity suite (operated by the MSP) and the ERP vendor's platform backups

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it touches the EJSP |
|---|---|---|---|
| Contract | FAR 52.204-21 Basic Safeguarding of Covered Contractor Information Systems | 48 CFR 52.204-21 (in the federal purchase order) | FCI (agency drawings, delivery schedule, test reports) sits in the suite, the ERP, and the test PC, so these are covered contractor information systems. 15 basic safeguards, (b)(1)(i)-(xv) |
| Contract | FAR 52.204-25 and 52.204-23 | 48 CFR 52.204-25(b)(2), (d); 52.204-23(b), (c) | Reasonable inquiry for covered telecommunications and video surveillance equipment (the camera recorder shares this network); Kaspersky covered articles |
| Contract | G&T cooperative Vendor Cyber Security Exhibit | Master service agreement exhibit; flows down CIP-013-2 R1 Parts 1.2.1 to 1.2.3 | 72-hour incident notice; response coordination; 1-business-day access-revocation notice for badge holders |
| State | Florida Information Protection Act | Fla. Stat. 501.171(2), (4), (8) | Reasonable measures for employee personal information in the suite; 30-day breach notice; disposal |
| Benchmark | NIST CSF 2.0 with NIST SP 800-82 Rev. 3 | NIST CSWP 29; SP 800-82r3 | Voluntary benchmark used for the gap analysis (P03) |
| C-CRITICAL-MFG-R01 | CIRCIA (proposed 6 CFR Part 226) | 89 FR 23644 | Not in effect. If finalized as proposed, the sector criterion in proposed 226.2(b)(3) would cover the shop regardless of size; tracked for readiness only |
| Internal | Security policies POL-02, POL-03, POL-04 | P06 | Access, incident response, and data handling rules |

Not applicable: NERC CIP-013-2 as a direct obligation (the shop is not a registered entity); DFARS 252.204-7012 (C-CRITICAL-MFG-R04; no DoD work); the ICTS connected vehicles rule (C-CRITICAL-MFG-R02); EAR export controls (C-CRITICAL-MFG-R03; no exports).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Owner on 2026-08-31.

### 4.2 System Authorization Decision
The shop is not a federal agency, so there is no formal authorization. The equivalent internal decision: on 2026-08-31 the Owner accepted continued operation of the EJSP, on condition that the POA&M items in P07 are completed by their dates and the four High risks in P01 (R-001, R-003, R-006, R-024) are treated by their due dates.

### 4.3 System Operational Status
Operational. Planned changes by 2026-12-31: ERP MFA and separate administrator accounts, a separate shop network for the test PC and oven HMI, a backup for the test PC and a scheduled ERP export, MSP-managed EDR, and a cellular failover router.

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner and risk acceptor | Owner | Overall accountability; accepts Moderate and higher risk; approves this plan, policies, and spending |
| Security Coordinator | Office Manager | Day-to-day security (designated 2026-07-01); ERP and suite administrator; maintains this plan, the risk register, the inventory, and the obligations list; manages the MSP |
| Shop equipment owner | Shop Manager | Test PC, oven controls, and winding machine; approves any change or vendor session on shop equipment |
| Test PC operator | Field Service and Test Technician | Runs tests; keeps test report copies; operates the AI-001 portal (outside this boundary) |
| IT operations | MSP | Managed computers, patching, antivirus, firewall, Wi-Fi, suite backup |
| Independent assessor | Independent consultant | Annual control assessment (P07) |

**Where roles overlap.** The Office Manager both administers the ERP and suite and is the Security Coordinator, so nobody independent checks her own administrator actions. Compensating steps: the Owner reviews the monthly account and log review checklist and signs it; the ERP administrator account is used only for administration once separate accounts exist (POAM-002); and the annual independent assessment (P07) covers account management.

## 6. System Information Types and System Categorization
Information types were chosen with reference to NIST SP 800-60. Types that SP 800-60 does not describe (repair production control, test records, and rewind design data) are organization-defined. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Supply chain management (goods acquisition, inventory control, logistics) | Low | Moderate | Moderate | Wrong stock or shipment data hurts storm deliveries; ERP down more than a day stops quoting and shipping (P05 BP-05 MTD 24 h) |
| Repair production control (organization-defined) | Low | Moderate | Moderate | A wrong work order or traveler produces a nonconforming rebuild; paper travelers cover a day (P05 BP-01) |
| Test records (organization-defined) | Low | Moderate | Moderate | Every unit ships with a test report; a falsified or lost result is a product integrity problem for utilities (P05 BP-04) |
| Rewind design data (organization-defined) | Moderate | Moderate | Low | The rewind data sheet library is the shop's main trade secret |
| Federal contract information (organization-defined) | Low | Low | Low | FCI requires basic safeguarding under FAR 52.204-21 |
| Financial management (accounting, payments, collections) | Moderate | Moderate | Low | Supplier bank detail fraud risk; invoices can wait a few days (P05 BP-08) |
| Human resources management (payroll and employee records) | Moderate | Low | Low | Employee personal information subject to Fla. Stat. 501.171 |
| **EJSP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 7-person shop. The plan documents 42 controls (see `control-implementation.csv`) that carry the FAR 52.204-21 safeguards, the cooperative exhibit duties, and the basic hygiene behind the P03 gaps. All other Moderate-baseline controls are handled one of two ways:
- **Inherited** from the SaaS vendors (physical, platform, and application controls), with the ERP vendor's SOC 2 report as the main evidence (P09).
- **Tailored out** for this tier, where the control addresses federal program management or organizations with IT staff (for example, change control boards, separate development environments, and alternate processing sites). These are recorded as tailoring decisions, not gaps.

## 7. Authorization Boundary Description
The boundary contains what the shop controls or pays someone to control on its behalf:
- **Inside:** the shop's ERP tenant configuration and user roles (SYS-01), the suite tenant and shared drive (SYS-02), 8 devices (SYS-03), the firewall, Wi-Fi, and internet line (SYS-04), the test PC (SYS-05), and the backup subscriptions (SYS-08).
- **Outside, interconnected over the same network:** the drying oven PLC and HMI with the OEM cellular modem (SYS-06), the winding machine (SYS-07, connected only by USB stick), and the camera recorder (SYS-09). They are outside because the EJSP does not depend on them to run, but they share its network today, which is the main boundary weakness (SC-7; P01 R-001, R-003).
- **Outside, external services:** the vendors' own platforms, the MSP's RMM platform, the oil laboratory's AI portal (SYS-10; assessed in P10), and the payroll service.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Agreement |
|---|---|---|---|
| Customers (suite email, shared links, ERP portal) | Bidirectional | Quotes, test reports, drawings, job status | Customer purchase orders; cooperative master service agreement and exhibit |
| Federal agency (suite email) | Bidirectional | Agency drawings, delivery schedule, test reports (FCI) | Federal purchase order with FAR 52.204-21 |
| Test set (USB and serial to the test PC) | Inbound | Test measurements | None needed |
| MSP RMM platform | Inbound administrative access | Device management | MSP contract (no security terms; gap) |
| Test set vendor support | Inbound remote access (ad hoc) | Software support | None (the 2024 firewall rule was removed 2026-08-11; POAM-005) |
| Oil laboratory AI portal (SYS-10) | Outbound | DGA results and nameplate data for customer transformers | Vendor standard terms (gap; P10) |
| Payroll service | Outbound | Payroll data | Service agreement |
| Banks and suppliers | Bidirectional | Purchase orders, payments | Bank agreement; call-back rule for bank detail changes (POL-02 C.7) |

## 9. System Component Inventory
| Component | Type | Location or provider | Owner |
|---|---|---|---|
| ERP tenant (SYS-01) | SaaS | ERP vendor | Office Manager |
| Suite tenant and shared drive (SYS-02) | SaaS | Productivity suite vendor | Office Manager |
| 3 desktops, 2 laptops, shop-floor PC, 2 tablets (SYS-03) | Endpoint | Office and repair bay; laptops travel | Office Manager (MSP operates) |
| Firewall and router, Wi-Fi access point, cable modem (SYS-04) | Network | Office network shelf | Office Manager (MSP operates) |
| Test PC (SYS-05) | Endpoint (unsupported operating system) | Test bay | Shop Manager |
| Suite backup subscription (SYS-08) | SaaS | Backup service (MSP account) | Office Manager (MSP operates) |

A full inventory, including OT equipment and where sensitive data is stored, is due 2026-10-31 (CM-8; POAM-004).

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 42 controls:
- Implemented: 6
- Partially implemented: 23
- Planned: 13
- Not applicable: 0

By responsibility: 16 system-specific (the shop), 24 hybrid (the shop with a vendor or the MSP), 2 common/inherited (fully provided by SaaS vendors).

### 10.2 Inherited and MSP-provided controls
| Provider | What the shop relies on | Evidence | What the shop must still do |
|---|---|---|---|
| ERP vendor | Platform security, encryption, backups (CP-9), lockout (AC-7), audit trail (AU-2), TLS (SC-8) | SOC 2 Type 2 report reviewed 2026-08-20 (P09) | Complementary user entity controls: user provisioning and removal, role assignment, MFA enforcement, review of user access and audit reports, and protecting its own export of data |
| Productivity suite vendor | Platform security, encryption at rest and in transit (SC-8, SC-28), lockout (AC-7), audit logging (AU-2) | Vendor documentation | Account management, MFA settings, sharing settings, log review |
| MSP | Patching (SI-2), antivirus (SI-3), firewall and Wi-Fi (SC-7, AC-18), laptop encryption (SC-28), suite backup (CP-9), screen lock (AC-11) | Monthly MSP reports; P07 evidence requests | Direct the work, approve exceptions, review reports monthly, add security terms to the contract (P01 R-009) |
| Backup service (MSP account) | Storage of suite backups (CP-9) | MSP backup job report | Restore test due 2026-09-30; separate MFA-protected login for deletion |
| Test set vendor | Test software support and calibration | Calibration certificate | Locate media and license key; attended support sessions only |

**Inherited does not mean done.** Two of the ERP vendor's complementary user entity controls are open gaps at the shop: MFA enforcement (IA-2(1)) and account removal (AC-2, PS-4).

### 10.3 Control assessment status
Assessed 2026-08-10 to 2026-08-12 by an independent consultant. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
Authentication assurance levels (AAL) follow the definitions in NIST SP 800-63B.
- **Productivity suite:** password plus a phone authenticator app (AAL2) for every user. Appropriate for a Moderate system holding FCI, the design library, and employee data.
- **ERP:** password only (AAL1) today. Not acceptable for administrator accounts or for a system that holds supplier bank details and customer pricing. ERP MFA for all users is due 2026-09-30 (POAM-002).
- **Shared logins:** the shop-floor PC "shop" login and the test PC administrator account identify no individual. Accepted only until named accounts replace them (shop-floor PC by 2026-10-31; test PC when it is replaced or rebuilt, by 2026-12-31).

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness and ERP vendor report review (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **DGA:** dissolved gas analysis (oil test that shows transformer condition)
- **EDR:** endpoint detection and response
- **EJSP:** ERP and Job Scheduling Platform
- **FCI:** federal contract information
- **HMI:** human-machine interface (operator touch panel)
- **MFA:** multi-factor authentication
- **MSP:** managed service provider
- **OEM:** original equipment manufacturer
- **PLC:** programmable logic controller
- **POA&M:** plan of action and milestones
- **RMM:** remote monitoring and management

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan | Office Manager (Security Coordinator) |
