# System Security Plan: Practice Business Platform (PBP)

**Organization:** Cris Santos Company, LLC (radiation safety consulting practice) | **Tier:** Micro | **Vertical:** Nuclear Reactors, Materials, and Waste
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-15

## 1. System Name and Identifier
Practice Business Platform (**PBP**), identifier CSC-SYS-001.

## 2. System Overview
The PBP supports every business process of the practice: consulting RSO work and audits, Part 37 security program services for 6 category 2 clients, shielding and survey projects, the calibration laboratory and leak test service, reactor outage support, client communications, and office administration. It serves 7 staff, about 140 consulting clients, and about 300 calibration and leak test customers.

The practice owns almost no infrastructure. Most of the PBP is SaaS, and a managed service provider (MSP) runs the laptops, the office network, and the suite backup. For each control, this plan says what the practice does itself, what the MSP does for it, and what it inherits from a SaaS vendor.

**What makes this system different from other small offices:** it holds copies of 6 clients' Part 37 security plans, implementing procedures, and lists of individuals approved for unescorted access to category 2 material. The clients must protect that information under 10 CFR 37.43(d), and their contracts pass that duty to the practice. Confidentiality of that information is the main design driver.

**Major components:**
- **SYS-01:** productivity suite (SaaS): email, calendar, the client file library, chat
- **SYS-02:** calibration and leak test management system (vendor SaaS)
- **SYS-03:** accounting, invoicing, and payroll service (SaaS)
- **SYS-04:** 7 laptops and 2 calibration laboratory workstations (MSP-managed), plus USB drives used at client sites
- **SYS-05:** office network: firewall, staff Wi-Fi, separate guest Wi-Fi (MSP-managed)
- **SYS-06:** SaaS-to-SaaS backup of the suite (operated by the MSP)
- **SYS-07:** calibration laboratory instruments (beam calibrator controller, reference electrometer, gamma spectroscopy system), connected to the lab workstations

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| C-NUCLEAR-S01 | Protection of client Part 37 security information and background investigation information (client contract flow-down) | 10 CFR 37.43(d), 37.31; imposed on the clients by their Florida license condition |
| C-NUCLEAR-S03 | Reactor client contract terms (portable media and devices, 4-hour incident notice, no Safeguards Information) | Client contracts, derived from the plants' 10 CFR 73.54 and 73.56 programs |
| C-NUCLEAR-S04 | NIST CSF 2.0 benchmark | Voluntary; adopted by the owner |
| C-NUCLEAR-S05 | Florida data security and breach notification | Fla. Stat. 501.171 |
| C-NUCLEAR-S06 | FTC Act Section 5 | 15 U.S.C. 45(a) |
| C-NUCLEAR-S02 | Florida radiation control rules (own license; records of the calibration source) | Chapter 64E-5, F.A.C. Radiation safety rule; relevant to SYS-02 source inventory records |
| Internal | Security policies POL-02, POL-03, POL-04 | P06 |

Not applicable, with reasons in P03 section 1:
- 10 CFR 73.54, 73.77, 73.110 (C-NUCLEAR-R01 to R03): the practice is not a power reactor licensee.
- NERC CIP (C-NUCLEAR-R04): not a registered entity.
- CIRCIA (C-NUCLEAR-R05): proposed only; as proposed, the practice is below the SBA size standard and meets no sector criterion.
- Safeguards Information (10 CFR 73.21): the practice does not produce, receive, or acquire SGI.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Principal Health Physicist (owner) on 2026-09-15.

### 4.2 System Authorization Decision
The practice is not a federal agency, so there is no formal authorization. The equivalent internal decision: on 2026-09-15 the owner accepted continued operation of the PBP, on the condition that the POA&M items in P07 are completed by their dates and the three High risks in P01 are treated by 2026-12-31. The restricted client library (POAM-002) must be in place by 2026-10-15, before the next Part 37 review season.

### 4.3 System Operational Status
Operational. Planned changes: restricted client library (P01 R-001, R-004), company-issued encrypted USB drives (R-003), MFA on the MSP-held firewall login (R-013), lab workstation encryption and replacement plan (R-009, R-011), and backup upgrade with restore tests (R-010), all due by 2026-12-31.

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner and risk acceptor | Principal Health Physicist (owner) | Overall accountability; accepts Moderate risk; approves this plan, policies, and spending |
| Security Officer | Office Manager | Day-to-day security; maintains this plan, the risk register, and the account lists; MSP contact |
| Client security information custodian | Senior Health Physicist (Part 37 services lead) | Keeps the client approval list (which staff each client approved); controls the restricted client library |
| Field devices and media | Senior Health Physicist (field services lead) | Company USB drives, scanning before site trips, reactor media rules |
| SYS-02 administrator | Calibration Laboratory Technician | SYS-02 accounts and settings; lab workstations; AI pilot (P10) |
| IT operations | MSP | Laptops, patching, antivirus, firewall, Wi-Fi, encryption, backup |
| Independent assessor | Outside cybersecurity consultant | Annual control assessment (P07) |

## 6. System Information Types and System Categorization
Information types follow NIST SP 800-60 Vol. 2 Rev. 1 where a close type exists. Client security information is an organization-defined type. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Client security information (Part 37 security plans, implementing procedures, approved-individual lists, review reports) | Moderate | Moderate | Low | Disclosure could help someone defeat one client's protection of category 2 material and would breach the client contract: a serious adverse effect. Availability is Low because the clients hold the originals (P05 MTD 72 h) |
| Calibration and leak test records | Low | Moderate | Moderate | A wrong certificate could leave a client using a faulty survey meter; calibration has a 48-hour MTD (P05) |
| Client communications and reports | Moderate | Moderate | Moderate | Client business information; BP-07 MTD 24 h |
| Personnel, payroll, and dose records | Moderate | Low | Low | Personal information under Fla. Stat. 501.171 |
| **PBP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

The practice rated client security information Moderate, not High, because one disclosure affects one client's program rather than causing catastrophic harm. The rating is revisited if the practice ever receives Safeguards Information or category 1 client information.

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 7-person practice. The plan documents 42 controls (41 from the Moderate baseline and PM-2, added by tailoring) that carry the client contract duties and basic cyber hygiene (see `control-implementation.csv`). All other Moderate-baseline controls are handled one of two ways:
- **Inherited** from the SaaS vendors (physical, platform, and application controls), with the SYS-02 vendor's SOC 2 report as the main evidence (P09).
- **Tailored out** for this tier, where the control addresses federal program management or organizations with dedicated IT staff (for example, configuration change boards and separate development environments). These are tailoring decisions, not gaps.

## 7. Authorization Boundary Description
The boundary contains what the practice controls or pays someone to control on its behalf:
- **Inside:** the suite tenant and its client library (SYS-01), the practice's SYS-02 tenant configuration and users, the SYS-03 account, 9 computers and the USB drives used at client sites (SYS-04), the office network (SYS-05), the backup subscription (SYS-06), and the lab instruments (SYS-07).
- **Outside (external services, interconnected):** the vendors' own platforms, the MSP's remote management platform, the dosimetry processor's portal (SYS-08), client systems the practice reaches only by email or on site, and the reactor plants' networks, which practice devices never join.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Agreement |
|---|---|---|---|
| 6 Part 37 clients (email, named-recipient sharing links) | Bidirectional | Security plans, implementing procedures, approved-individual lists, review reports | Consulting contracts with information protection terms (37.43(d) flow-down) |
| 2 reactor clients (on site only) | Outbound people, inbound plant rules | Outage work on plant systems; no practice devices on plant networks; media scanned at the plant kiosk | Outage support contracts |
| Other consulting clients (email, sharing links) | Bidirectional | Audit reports, survey and shielding reports | Consulting contracts |
| Calibration customers (SYS-02 customer portal, parcel shipments) | Bidirectional | Instrument lists, certificates, leak test results | Service terms |
| MSP remote management platform | Inbound administrative access | Device management | MSP service contract (no security terms; gap) |
| Dosimetry processor portal (SYS-08) | Inbound | Staff dose reports | Processor service terms |
| Suite backup service | Outbound | Copies of mail and files | Through the MSP |

## 9. System Component Inventory
| Component | Type | Location or provider | Owner |
|---|---|---|---|
| Suite tenant, client library, mailboxes (SYS-01) | SaaS | Productivity suite vendor | Office Manager |
| SYS-02 tenant | SaaS | Calibration system vendor | Calibration Laboratory Technician |
| SYS-03 account | SaaS | Accounting and payroll service | Office Manager |
| 7 laptops (SYS-04) | Endpoint | Travel with staff | Office Manager (MSP operates) |
| Lab workstations 1 and 2 (SYS-04) | Endpoint | Calibration laboratory | Calibration Laboratory Technician (MSP operates) |
| USB drives used at client sites (SYS-04) | Removable media | Field kits; 4 personal drives in use today | Senior Health Physicist (field services lead) |
| Firewall, staff Wi-Fi, guest Wi-Fi (SYS-05) | Network | Locked network closet | Office Manager (MSP operates) |
| Suite backup subscription (SYS-06) | SaaS | Backup vendor (MSP subcontractor) | Office Manager (MSP operates) |
| Beam calibrator controller, electrometer, gamma spectroscopy system (SYS-07) | Laboratory instrument | Calibration laboratory | Principal Health Physicist (RSO) |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 42 controls:
- Implemented: 10
- Partially implemented: 22
- Planned: 10
- Not applicable: 0

By responsibility: 19 system-specific (the practice), 20 hybrid (the practice with a vendor or the MSP), 3 common/inherited (fully provided by a SaaS vendor).

### 10.2 Inherited and MSP-provided controls
| Provider | What the practice relies on | Evidence | What the practice must still do |
|---|---|---|---|
| Productivity suite vendor | Platform security, encryption at rest and in transit (SC-8, SC-28), lockout (AC-7), audit logging (AU-2, AU-11) | Vendor documentation | Library permissions, sharing settings, MFA settings, log review, encrypted delivery of client security information |
| Calibration system vendor (SYS-02) | Platform security, backups (CP-9), audit trail (AU-2), encryption (SC-28) | SOC 2 Type 2 report reviewed 2026-08-20 (P09) | Complementary user entity controls: user provisioning and removal, MFA enforcement for all users, review of user access, export of the practice's records |
| Accounting and payroll service | Platform security; payroll processing | Vendor documentation | Account management |
| MSP | Patching (SI-2), antivirus (SI-3), firewall and Wi-Fi (SC-7, AC-18), laptop encryption (SC-28), backup operation (CP-9), screen lock (AC-11) | Monthly MSP reports; P07 evidence requests | Oversight: approve exceptions, review reports monthly, annual MSP security review (SR-6) |
| Part 37 clients' reviewing officials | Trustworthiness and reliability decisions on practice staff (PS-3) | Client approval letters (4 of 6 on file) | Keep the approval list current; tell clients within 2 working days when someone leaves |

**Inherited does not mean done.** Two of the SYS-02 vendor's complementary user entity controls are open gaps at the practice: account removal (AC-2, PS-4) and MFA for all users (IA-2(1)).

### 10.3 Control assessment status
Assessed 2026-08-24 to 2026-08-26 by an independent cybersecurity consultant. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
Staff sign in to the suite and SYS-03 with a password and a second factor (a phone authenticator app with push approval). This is appropriate for the Moderate category, including access to client security information, once number matching is enabled (P01 R-001). In SYS-02, only the 2 administrators use MFA today; the other 5 users must be enrolled by 2026-10-15 (POAM-005). Part 37 clients rely on 37.43(d)(7), which requires that information "stored in nonremovable electronic form must be password protected." The practice treats MFA plus folder restrictions as its way of meeting the clients' expectation.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness and SYS-02 vendor report review (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **Category 2 quantity:** an amount of radioactive material at or above the category 2 threshold in 10 CFR Part 37, Appendix A, and below category 1
- **MFA:** multi-factor authentication
- **MSP:** managed service provider
- **PBP:** Practice Business Platform
- **POA&M:** plan of action and milestones
- **RSO:** Radiation Safety Officer
- **T&R:** trustworthiness and reliability (the determination a Part 37 client's reviewing official makes before giving a person access to its security information, 37.43(d)(3))

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-09-15 | Initial plan | Office Manager (Security Officer) |
