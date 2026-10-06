# System Security Plan: Motel Property Management and Point-of-Sale System (MPPS)

**Organization:** Cris Santos Company, LLC (independent 38-unit roadside motel) | **Tier:** Micro | **Vertical:** Accommodation and Food Services
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Motel Property Management and Point-of-Sale System (**MPPS**), identifier CSC-SYS-001.

## 2. System Overview
The MPPS supports every guest-facing and business process of the motel: reservations and OTA distribution, check-in and room keys, card payments, the lobby market, night audit and the guest register, housekeeping, crew billing, and guest Wi-Fi. It serves 7 employees and about 5,900 stays a year, with the front desk open 24 hours.

The motel owns almost no infrastructure. Most of the MPPS is vendor SaaS, and a managed service provider (MSP) runs the on-site network and PCs. This plan therefore says, for each control, what the motel does itself, what the MSP does for it, and what it inherits from a SaaS vendor or payment service provider.

**Major components:**
- **SYS-01:** all-in-one cloud PMS (vendor SaaS) with booking engine, channel manager, point-of-sale module for the lobby market, housekeeping module, and card vault
- **SYS-02:** payment gateway and 2 front desk terminals in a PCI-listed validated P2PE solution, semi-integrated with the PMS
- **SYS-03:** front desk PC, back office PC, Owner-Manager's laptop, 2 housekeeping tablets (PCs MSP-managed)
- **SYS-04:** motel network: firewall, office network, staff Wi-Fi, separate guest Wi-Fi, one internet line (MSP-managed)
- **SYS-05:** productivity suite (SaaS): email, the shared front desk mailbox, files
- **SYS-06:** door lock system: lock software and database on the back office PC, key card encoder, 41 locks
- **SYS-07:** CCTV: 10 cameras and an on-site recorder
- **SYS-09:** cloud backup of the back office PC and the suite (SaaS, operated by the MSP)

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| N72-R01 | PCI DSS v4.0.1 (contractual, through the merchant agreement) | PCI SSC standard. 2026 validation: SAQ P2PE plus SAQ A after the redesign (P03) |
| N72-R02 | FTC Act Section 5 (unfair or deceptive practices), with the FTC Rule on Unfair or Deceptive Fees | 15 U.S.C. 45(a), (n); 16 CFR Part 464 |
| N72-R03 | FTC Disposal Rule (background-check reports) | 16 CFR 682.3 |
| N72-R04 | State breach notification laws; Florida worked example | Fla. Stat. 501.171 |
| State | Florida guest register | Fla. Stat. 509.101(2) |
| State | Florida unconscionable prices in a declared emergency (SYS-10 interface) | Fla. Stat. 501.160 |
| Internal | Security policies POL-02, POL-03, POL-04 | P06 |

Not applicable:
- Illinois BIPA (N72-R05): no Illinois operations, and no biometric collection.
- CIRCIA (N72-R06): proposed only; the motel is far below the SBA size standard.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Owner-Manager on 2026-08-31.

### 4.2 System Authorization Decision
The motel is not a federal agency, so there is no formal authorization. The equivalent internal decision: on 2026-08-31 the Owner-Manager accepted continued operation of the MPPS, on the condition that the payment redesign is complete by 2026-11-30, the POA&M items in P07 are completed by their dates, and the four High risks in P01 are treated by 2026-12-31.

### 4.3 System Operational Status
Operational. Planned changes by 2026-12-31: the payment redesign that takes the front desk PC out of card data scope (P03), separate networks for payments, the lock system, and the office (P01 R-008), EDR (R-001, R-002), backup of the lock database (R-009), and a cellular failover router (R-011).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner and risk acceptor | Owner-Manager | Overall accountability; accepts Moderate risk; approves this plan, policies, spending, and the SAQ |
| Security and Privacy Lead | Assistant Manager | Day-to-day security, PCI DSS contact, account management, incident lead; maintains this plan and the risk register |
| Front office users | Front Desk Clerks, Night Auditor | Follow card handling and access rules; report incidents |
| IT operations | MSP | PCs, patching, antivirus, firewall, Wi-Fi, backup |
| Payment service provider | Payment gateway and P2PE solution provider | Card processing, P2PE terminals, tokens |
| Independent assessor | Security consultant | Yearly control assessment (P07) |

**Overlap.** The Assistant Manager operates and checks most controls. The Owner-Manager's monthly review, the MSP's monthly report, the independent assessor, and vendor attestations are the independent checks.

## 6. System Information Types and System Categorization
SP 800-60's information types describe federal missions and do not fit a motel closely, so the types are named in plain terms and rated with the FIPS 199 impact definitions.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Payment card data (keyed numbers, OTA virtual cards, card forms) | Moderate | Moderate | Low | Disclosure causes fraud, card brand costs, and breach notice; payments can wait for the gateway (P05 MTD 8 h) |
| Guest records (profiles, ID scans, stay history, guest register) | Moderate | Moderate | Moderate | ID numbers with names are personal information under Fla. Stat. 501.171(1)(g); wrong records cause overbooking; check-in MTD is 4 h |
| Room access data (lock system and room assignments) | Low | Moderate | Moderate | A wrong key to a wrong room is a guest safety issue; keys cannot be encoded without the lock system |
| Workforce and financial records | Moderate | Low | Low | Payroll and background-check reports; tolerate several days of delay |
| **MPPS category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 7-person motel. The plan documents 43 controls that carry the PCI DSS requirement groups and basic cyber hygiene (see `control-implementation.csv`). All other Moderate-baseline controls are handled one of two ways:
- **Inherited** from the SaaS vendors and the payment service provider (platform, physical, and application controls), with the PMS vendor's SOC 2 report and the AOCs as evidence (P09).
- **Tailored out** for this tier, where the control addresses federal program management or organizations with dedicated IT staff (for example, configuration change boards and separate development environments). These are recorded as tailoring decisions, not gaps.

## 7. Authorization Boundary Description
The boundary contains what the motel controls or pays someone to control on its behalf:
- **Inside:** the motel's PMS tenant configuration and users (SYS-01), the 2 P2PE terminals and the gateway merchant portal (SYS-02), 5 company devices (SYS-03), the motel network (SYS-04), the suite tenant (SYS-05), the lock system (SYS-06), CCTV (SYS-07), and the backup subscription (SYS-09).
- **Outside (external services, interconnected):** the vendors' own platforms and data centers, the gateway and P2PE provider's systems, the OTAs, the MSP's remote management platform, the lock vendor's remote support service, the accounting and payroll services (SYS-08), and the dynamic pricing tool (SYS-10, assessed in P10).
- **Personal device:** the Owner-Manager's phone runs the PMS, email, and CCTV apps. It is outside the boundary but must follow POL-02 (passcode, MFA apps, no card data).

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Agreement |
|---|---|---|---|
| Payment gateway and acquirer (from SYS-01 and SYS-02) | Bidirectional | Authorizations, settlements, tokens | Merchant agreement; gateway AOC (2026-01) |
| 3 OTAs (through the SYS-01 channel manager) | Bidirectional | Reservations, guest names, virtual card numbers, rates | OTA agreements |
| Dynamic pricing tool (SYS-10) | Inbound rates; outbound occupancy and pickup | Rates; aggregated occupancy data | Vendor subscription terms (P10) |
| Crew companies (SYS-05 email) | Inbound | Crew rosters; **card authorization forms (stops at the redesign)** | Crew account letters |
| Accounting SaaS and payroll service (SYS-08) | Outbound | Daily revenue and payroll data | Vendor terms |
| MSP remote management platform | Inbound administrative access | PC management | MSP service contract |
| Lock vendor remote support tool (SYS-06) | Inbound administrative access | Lock software support | **No written terms (gap)** |
| Background-check company | Bidirectional | Applicant data and reports | Service agreement |

## 9. System Component Inventory
| Component | Type | Location or provider | Owner |
|---|---|---|---|
| PMS tenant (SYS-01) | SaaS | PMS vendor | Assistant Manager |
| Gateway merchant portal and 2 P2PE terminals (SYS-02) | Service provider plus POI devices | Gateway; front desk counter | Assistant Manager |
| Front desk PC, back office PC, laptop, 2 tablets (SYS-03) | Endpoints | Front office and back office | Assistant Manager (MSP operates the PCs) |
| Firewall, office network, staff and guest Wi-Fi (SYS-04) | Network | Back office cabinet; 8 access points | Owner-Manager (MSP operates) |
| Suite tenant and shared front desk mailbox (SYS-05) | SaaS | Productivity suite vendor | Assistant Manager |
| Lock software, database, encoder, 41 locks (SYS-06) | On-premises application and devices | Back office PC; front desk; doors | Owner-Manager |
| CCTV recorder and 10 cameras (SYS-07) | On-premises devices | Back office | Owner-Manager |
| Backup subscription (SYS-09) | SaaS | Backup service (operated by the MSP) | Assistant Manager (MSP operates) |

A full inventory, including terminal serial numbers and every place card data and ID scans are stored, is due 2026-10-31 (CM-8).

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 43 controls:
- Implemented: 10
- Partially implemented: 25
- Planned: 8
- Not applicable: 0

By responsibility: 19 system-specific (the motel), 23 hybrid (the motel with a vendor or the MSP), 1 common/inherited (fully provided by SaaS vendors).

### 10.2 Inherited and MSP-provided controls
| Provider | What the motel relies on | Evidence | What the motel must still do |
|---|---|---|---|
| PMS vendor | Platform security, card vault encryption (SC-28), backups (CP-9), lockout (AC-7), activity logs (AU-2, AU-11) | SOC 2 Type 2 report reviewed 2026-08-20 (P09); PCI DSS service provider AOC (2026-02) | Complementary user entity controls: user provisioning and removal, least-privilege roles, MFA, activity report review, workstation protection |
| Payment gateway and P2PE provider | Encryption at the terminal, tokenization, processing (SC-8) | Gateway AOC (2026-01); P2PE solution listing confirmed 2026-07-15; P2PE Instruction Manual | Follow the Instruction Manual: device list, inspections, approved key entry only |
| Productivity suite vendor | Platform security, encryption, lockout, sign-in logs | Vendor documentation | Accounts, MFA, mailbox sharing, log review |
| MSP | Patching (SI-2), antivirus (SI-3), firewall and Wi-Fi (SC-7, AC-18), backup operation (CP-9), device lock (AC-11) | Monthly MSP reports; P07 evidence requests | Oversight: approve changes, review reports monthly, yearly MSP security review (P01 R-020) |
| Door lock vendor | Lock software support | None | Written remote access and incident notice terms (P01 R-001) |

**Inherited does not mean done.** Four of the PMS vendor's complementary user entity controls are open gaps at the motel: account removal (AC-2, PS-4), least privilege (AC-6), MFA for all users (IA-2(1)), and activity review (AU-6).

### 10.3 Control assessment status
Assessed 2026-08-03 to 2026-08-05 by an independent consultant. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
PMS administrators, the two manager mailboxes, and the backup console use a password and a phone authenticator app. Front office users sign in to the PMS with a password only, and the shared front desk mailbox and Windows login are shared. That is not acceptable for users who can display card numbers. Single sign-in with MFA for every PMS user and named accounts for every clerk are due 2026-10-31 (P01 R-002, R-005, R-007). Guests use the PMS vendor's booking engine; their identity is outside this boundary.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness and PMS vendor report review (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **AOC:** attestation of compliance (PCI DSS)
- **ASV:** approved scanning vendor
- **EDR:** endpoint detection and response
- **MFA:** multi-factor authentication
- **MPPS:** Motel Property Management and Point-of-Sale System
- **MSP:** managed service provider
- **OTA:** online travel agency
- **P2PE:** point-to-point encryption
- **PMS:** property management system
- **POA&M:** plan of action and milestones
- **SAQ:** self-assessment questionnaire (PCI DSS)

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan | Assistant Manager (Security and Privacy Lead) |
