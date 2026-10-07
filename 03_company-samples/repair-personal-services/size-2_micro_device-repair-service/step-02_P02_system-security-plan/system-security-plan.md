# System Security Plan: Service Ticketing and Point-of-Sale System (STPS)

**Organization:** Cris Santos Company, LLC (independent electronics and device repair shop) | **Tier:** Micro | **Vertical:** Other Services (except Public Administration)
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Service Ticketing and Point-of-Sale System (**STPS**), identifier CSC-SYS-001.

## 2. System Overview
The STPS supports every step of a repair at the shop's single Florida storefront: intake and consent at the counter, diagnostics and repair at the bench, data transfer and basic data recovery, payment, and release. It serves 7 workforce members, about 22 tickets a business day, and about 15,500 customer records.

The shop owns very little infrastructure. Its records live in vendor SaaS, card data stays inside the payment processor's P2PE terminals, and a managed service provider (MSP) runs the office endpoints, network, and backup. The bench workstations and bench storage are the exception: the Senior Technician runs them, outside the MSP contract. This plan says, for each control, what the shop does itself, what the MSP does for it, and what it inherits from a SaaS vendor or the processor.

**Major components:**
- **SYS-01:** SaaS repair-shop ticketing and point-of-sale platform (tickets, customer records, inventory, invoicing, text and email updates)
- **SYS-02:** the payment processor's P2PE solution: 2 counter PIN pads, 1 spare, and the merchant portal
- **SYS-03:** productivity suite (email, the shared repairs mailbox, files), administered by the MSP
- **SYS-04:** 2 counter PCs and 2 laptops (MSP-managed)
- **SYS-05:** 3 bench PCs and 1 data transfer station (not MSP-managed)
- **SYS-06:** bench storage (8 TB network storage device) for transfers and recovery images
- **SYS-07:** shop network: firewall, staff Wi-Fi, separate guest Wi-Fi, one internet line (MSP-managed)
- **SYS-08:** cloud backup of the productivity suite and bench storage (SaaS, operated by the MSP)

**What the system protects beyond its own data.** Customer devices under repair connect to the bench PCs for diagnostics and data transfer, and join the staff Wi-Fi. Their contents (photos, messages, health and location data, saved passwords) are not stored in the STPS by design, but they pass through it, and copies land on the bench storage. The plan therefore treats bench handling of customer devices as part of the system.

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| N81-R01 | FTC Act Section 5: unfair or deceptive practices | 15 U.S.C. 45(a)(1), 45(n) |
| N81-R02 | State breach and data security laws; Florida as the worked example | Fla. Stat. 501.171(2)-(6), (8) |
| N81-R03 | PCI DSS v4.0.1 (contractual), validated on SAQ P2PE | Merchant agreement; SAQ P2PE v4.0.1 (October 2024) |
| N81-R04 | FTC Disposal Rule, for the 2 background check reports only | 16 CFR 682.3 |
| N81-BM | NIST CSF 2.0 (voluntary benchmark); NIST SP 800-88 Rev. 2 for sanitization | NIST CSWP 29; SP 800-88r2 (September 2025) |
| Internal | Security policies POL-02, POL-03, POL-04 | P06 |

Not applicable: the FTC Safeguards Rule (no credit extended), COPPA (N81-R05; not directed to children), and HIPAA (N81-R06; not a covered entity or business associate). Reasons are in P03 section 1.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Owner on 2026-08-31.

### 4.2 System Authorization Decision
The shop is not a federal agency, so there is no formal authorization. The equivalent internal decision: on 2026-08-31 the Owner accepted continued operation of the STPS, on the condition that the POA&M items in P07 are completed by their dates and the treatment plans for the High risks in P01 are carried out by their due dates. None of the High risks was accepted without treatment.

### 4.3 System Operational Status
Operational. Planned changes: SYS-01 restricted passcode field and purge of passcode notes (due 2026-10-31), named counter accounts with MFA (2026-09-30), a separate network for customer devices and bench equipment (2026-12-31), bench workstation management by the MSP with EDR (2026-12-31), and a cellular failover router (2026-11-30).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner and risk acceptor | Owner | Overall accountability; accepts Moderate risk; approves treatment plans for High risks, this plan, policies, and spending |
| Security and Privacy Lead | Shop Manager | Day-to-day security and privacy; maintains this plan, the risk register, the vendor list, and the SAQ; designated in writing 2026-07-15 |
| Bench systems custodian | Senior Technician | Bench workstations, bench storage, data transfer and recovery, sanitization of recycled devices; business owner of the AI assistant's diagnostic suggestions (P10) |
| IT operations | MSP | Office endpoints, firewall and Wi-Fi, productivity suite administration, cloud backup |
| Independent assessor | Independent security consultant | Annual control assessment (P07) |

**Role overlap and how it is compensated.** In a 7-person shop the Shop Manager both runs security and does daily counter work, and the Senior Technician both administers the bench systems and uses them. Neither can review their own work alone. The compensations are: the Owner reviews the monthly account and log checks with the Shop Manager; the MSP takes over bench workstation management (P01 R-020); and an independent consultant assesses the controls each year (P07).

## 6. System Information Types and System Categorization
Information types were chosen as the closest matches in NIST SP 800-60 Vol. 2 Rev. 1 (customer services, collections and receivables, and personal identity and authentication), adapted to a private business. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Customer records and repair tickets (names, contact details, device identifiers, passcodes until purged) | Moderate | Moderate | Moderate | Passcodes and account passwords enable account takeover, and an email with a password is personal information under Fla. Stat. 501.171(1)(g); a wrong record can mean a device released to the wrong person; intake and release stop within one business day (P05 MTD 8 h) |
| Customer device content in custody (photos, messages, health, location, saved credentials) | Moderate | Moderate | Low | Serious harm to an individual if exposed; the shop is not the system of record and jobs can wait (P05 BP-04 MTD 72 h) |
| Payment and invoicing (truncated card numbers, business account bank details) | Moderate | Moderate | Moderate | Card data stays inside the P2PE terminals; bank details enable payment fraud; payment and release share BP-03 |
| Workforce records and background reports | Moderate | Low | Low | Consumer report information under the Disposal Rule; limited harm if briefly unavailable |
| **STPS category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 7-person shop. The plan documents 45 controls that carry the shop's legal and contractual duties and basic cyber hygiene (see `control-implementation.csv`). All other Moderate-baseline controls are handled one of two ways:
- **Inherited** from the SaaS vendors and the payment processor (physical, platform, and application controls, and card data encryption), with the ticketing vendor's SOC 2 report and the processor's P2PE listing as evidence (P09).
- **Tailored out** for this tier, where the control addresses federal program management or organizations with IT staff (for example, configuration change boards and separate development environments). These are recorded as tailoring decisions, not gaps.

**Added for a repair shop.** Three controls govern handling of customer devices and get extra weight here: AC-6 (what a technician may open), MP-6 (sanitization of recycled devices), and MP-7 (no customer data on removable drives except company-issued ones). PS-6 (signed confidentiality agreements) supports them.

## 7. Authorization Boundary Description
- **Inside:** the SYS-01 tenant configuration, roles, and fields; the merchant portal account and the 3 terminals' physical custody (SYS-02, customer side); the productivity suite tenant (SYS-03); 4 office endpoints (SYS-04); 4 bench workstations (SYS-05); the bench storage (SYS-06); the shop network (SYS-07); the shop's backup subscription (SYS-08).
- **Outside (external services, interconnected):** the vendors' platforms and data centers; the processor's P2PE decryption environment; the MSP's remote management platform; the security cameras' cloud service (SYS-09); the AI assistant's model provider (SYS-10, assessed in P10); the outside data recovery lab, courier, and recycler.
- **Customer devices** are outside the boundary but connect to bench PCs and Wi-Fi inside it. The rules for handling them are part of this plan (AC-6, MP-6, MP-7, SC-7).

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Agreement |
|---|---|---|---|
| Payment processor (SYS-02) | Bidirectional | Amount out; approval and truncated card number back. Card data only inside the terminals | Merchant agreement; P2PE Instruction Manual |
| AI assistant model provider (through SYS-01) | Outbound | Chat and text messages; ticket symptoms and notes | SYS-01 terms only; **no data-use terms with the shop (gap; P10)** |
| Customers (SYS-01 texts and email; SYS-10 chat) | Bidirectional | Status, quotes, invoices | Intake form terms |
| MSP remote management platform | Inbound administrative access | Endpoint management | MSP service contract (no incident notice term; gap) |
| Outside data recovery lab (courier) | Outbound and return | Customer drives and recovered data | **None (gap)** |
| E-waste recycler | Outbound | Wiped devices and retired equipment | Pickup agreement; certificate per pickup |
| Outside bookkeeper and payroll service | Outbound | Invoices, payroll data | Service agreement |
| Property management business account | Outbound | Security questionnaire answers (no customer data) | None needed |

## 9. System Component Inventory
| Component | Type | Location or provider | Owner |
|---|---|---|---|
| Ticketing and POS tenant (SYS-01) | SaaS | Ticketing and POS vendor | Shop Manager |
| P2PE terminals (2 plus 1 spare) and merchant portal (SYS-02) | Payment terminal; service | Front counter; payment processor | Shop Manager |
| Productivity suite tenant (SYS-03) | SaaS | Productivity suite vendor | Shop Manager (MSP operates) |
| 2 counter PCs, 2 laptops (SYS-04) | Endpoint | Counter; laptops travel with the Owner and Shop Manager | Shop Manager (MSP operates) |
| 3 bench PCs, 1 data transfer station (SYS-05) | Endpoint | Back repair room | Senior Technician |
| Bench storage, 8 TB (SYS-06) | Storage device | Back repair room | Senior Technician |
| Firewall, staff Wi-Fi, guest Wi-Fi (SYS-07) | Network | Back room wall cabinet | Shop Manager (MSP operates) |
| Cloud backup subscription (SYS-08) | SaaS | Backup provider (MSP's) | Shop Manager (MSP operates) |

A full device and data inventory, including terminal serial numbers, is due 2026-10-31 (CM-8).

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 45 controls:
- Implemented: 5
- Partially implemented: 22
- Planned: 18
- Not applicable: 0

By responsibility: 26 system-specific (the shop), 16 hybrid (the shop with a vendor, the processor, or the MSP), 3 common/inherited (fully provided by a SaaS vendor or the processor).

### 10.2 Inherited and MSP-provided controls
| Provider | What the shop relies on | Evidence | What the shop must still do |
|---|---|---|---|
| Ticketing and POS vendor | Platform security, encryption, backups (CP-9), lockout (AC-7), audit records (AU-2, AU-11) | SOC 2 Type 2 report (Security) reviewed 2026-08-18 (P09) | Complementary user entity controls: named users, role assignment, MFA, removing leavers, reviewing exports and audit logs |
| Payment processor | Card data encryption in the terminals (SC-8); decryption and key management; terminal supply | P2PE listing; processor PCI DSS attestation; P2PE Instruction Manual | The PIM controls: terminal list, inspections, staff training, no card data anywhere else (SAQ P2PE eligibility) |
| Productivity suite vendor | Platform security, encryption, lockout (AC-7), logging (AU-2) | Vendor documentation | Account management, MFA, forwarding and sharing settings, log review |
| MSP | Patching (SI-2), antivirus (SI-3), firewall and Wi-Fi (SC-7, AC-18), laptop encryption (SC-28), screen lock (AC-11), backup operation (CP-9) | Monthly MSP reports; P07 evidence requests | Oversight: monthly report review, approve exceptions, extend the contract to the bench equipment, add an incident notice term (P01 R-013) |
| Cloud backup service (MSP's provider) | Storage of backup copies (CP-9) | None yet; restore test due 2026-09-30 | Restore tests; immutable retention; shorter retention for customer data |

**Inherited does not mean done.** Two of the ticketing vendor's complementary user entity controls are open gaps at the shop: named users (the shared Counter login, AC-2, IA-2) and review of exports and audit logs (AU-6). The P2PE solution protects card data only while staff keep card numbers out of ticket notes and off paper.

### 10.3 Control assessment status
Assessed 2026-08-10 to 2026-08-12 by an independent consultant. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
Named users sign in to SYS-01, the productivity suite, and the merchant portal with a password and a phone authenticator app. This is appropriate for customer personal information at the Moderate category. The shared Counter login does not meet this statement and is being replaced by named accounts with MFA by 2026-09-30 (P01 R-002, R-003). Customers do not have accounts; they receive status by text and email, and the AI assistant returns ticket status only when the customer gives the ticket number and the phone number on file.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness and ticketing vendor report review (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **EDR:** endpoint detection and response
- **MFA:** multi-factor authentication
- **MSP:** managed service provider
- **P2PE:** point-to-point encryption (a PCI-listed solution that encrypts card data inside the terminal)
- **PIM:** P2PE Instruction Manual
- **POA&M:** plan of action and milestones
- **SAQ:** PCI DSS self-assessment questionnaire
- **STPS:** Service Ticketing and Point-of-Sale System

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan | Shop Manager (Security and Privacy Lead) |
