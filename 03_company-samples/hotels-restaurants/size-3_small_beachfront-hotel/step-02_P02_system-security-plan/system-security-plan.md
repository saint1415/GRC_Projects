# System Security Plan: Property Management and Point-of-Sale Platform (PMPS)

**Organization:** Cris Santos Company, LLC (independent 140-room beachfront hotel) | **Tier:** Small | **Vertical:** Accommodation and Food Services
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Property Management and Point-of-Sale Platform (**PMPS**), identifier CSC-SYS-001.

## 2. System Overview
The PMPS supports every guest-facing and payment process at the hotel: reservations, arrival and check-in, key card issuance, folios and payments, restaurant and bar service, night audit, and card settlement. It serves 60 employees and about 15,700 stays a year, and carries about 97,000 card transactions a year under two merchant accounts (MID-1 Rooms and MID-2 Food and beverage).

**Major components:**
- **SYS-01:** a SaaS property management system (PMS) with the vendor's card vault
- **SYS-02:** a payment gateway and 4 front desk chip terminals (not P2PE)
- **SYS-05:** the restaurant and bar POS with 14 devices in a validated P2PE solution
- **SYS-06:** the hotel staff network (flat today) and internet connection
- **SYS-07:** endpoints (34 PCs and laptops, 12 tablets)
- **SYS-08:** the door lock system (on-premises lock server, 3 encoders, 160 locks)
- **SYS-09:** the identity provider
- **SYS-10:** a public-cloud tenant (reporting database, guest-marketing hub, chatbot integration, backup vault)

The cloud tenant is described by service category and is vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| N72-R01 | PCI DSS v4.0.1 (contractual). MID-1 validates on SAQ D for Merchants; MID-2 on SAQ P2PE for 2026 | PCI SSC standard; merchant agreements |
| N72-R02 | FTC Act Section 5 (security and privacy claims; unfair security practices) and the FTC Rule on Unfair or Deceptive Fees | 15 U.S.C. 45(a), (n); 16 CFR Part 464 |
| N72-R03 | FTC Disposal Rule (background-check reports) | 16 CFR 682.3 |
| N72-R04 | State breach notification; Florida Information Protection Act | Fla. Stat. 501.171 |
| State | Florida guest register | Fla. Stat. 509.101(2) |
| Internal | Security policies POL-01 to POL-05 | P06 |

Not applicable:
- CIRCIA (N72-R06), which is proposed only and would not reach a business below the SBA size standard.
- Illinois BIPA (N72-R05), because the hotel has no Illinois operations.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the General Manager on 2026-08-31.
### 4.2 System Authorization Decision
The hotel is not a federal agency, so there is no formal authorization. The equivalent internal decisions:
- The General Manager accepted continued operation of the PMPS on 2026-08-31, with the conditions in the P07 POA&M.
- The majority owner accepted the five High risks in P01 with dated treatment plans.
- The Controller will sign the 2026 SAQ D and SAQ P2PE attestations only with evidence for every answer (P03 section 4).
### 4.3 System Operational Status
Operational. Major modifications planned:
- network segmentation (payment, lock, CCTV, and office VLANs), due 2026-12-31;
- validated P2PE terminals at the front desk with keypad entry for phone payments, due 2027-01-31;
- lock server upgrade and relocation above flood level, due 2027-03-31.

Each of these changes PCI scope and triggers a scope review (PCI DSS 12.5.2).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | General Manager | Overall accountability; risk acceptance up to Moderate |
| Risk acceptor (authorizing official equivalent) | Majority owner | Acceptance of High and Very High risks |
| Information Security Lead | IT Manager | Day-to-day security; PCI DSS technical contact |
| PCI compliance owner | Controller | Merchant agreements; SAQs and attestations; service provider files |
| Front office data owner | Front Office Manager | PMS roles, card handling, night audit, guest register |
| Physical and lock system owner | Chief Engineer | Lock system, server room, hurricane preparation |
| Operations support | Managed service provider | Help desk, firewall, patching, anti-malware |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1 where a close match exists. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Payment card data (account data under PCI DSS) | Moderate | Moderate | Moderate | Disclosure causes card fraud, acquirer and card brand costs, and notice duties; not catastrophic to the business |
| Guest records (profiles, ID scans, stay history, guest register) | Moderate | Moderate | Moderate | Passport and license numbers are personal information under Fla. Stat. 501.171; wrong room or folio data harms guests; P05 MTD 4 h for check-in |
| Room access (lock system data) | Low | Moderate | Moderate | Integrity and availability affect guest safety; P05 MTD 2 h with emergency key cards as fallback |
| Financial management (folios, settlement) | Moderate | Moderate | Low | Night audit can run late (P05 MTD 24 h) |
| **PMPS category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 60-person hotel. The plan documents the 65 controls that implement PCI DSS v4.0.1 for SAQ D and core network hygiene (see `control-implementation.csv`). Two controls outside the Moderate baseline were **added** because PCI DSS requires them: CA-8 (penetration testing, Requirement 11.4) and SR-9 (tamper protection of payment devices, Requirement 9.5). PM-9 is a program-level control with no baseline. Every other Moderate-baseline control is treated as follows:
- **Inherited** from the SaaS, payment, and cloud providers, as evidenced by their AOCs and SOC 2 reports (P09).
- **Out of scope for this tier**, recorded as a tailoring decision, where the control's purpose applies only to federal systems.

## 7. Authorization Boundary Description
The boundary contains hotel-managed components and the hotel's configuration of vendor services:
- **Inside:** PMS tenant configuration, users, and roles; the front desk terminals; the restaurant POS stations and P2PE devices (physical custody and inspection); the staff network, firewall, and staff Wi-Fi; 34 PCs and laptops and 12 tablets; the lock server and encoders; the identity provider tenant; the cloud tenant (4 workloads and the backup vault).
- **Outside (external services, interconnected):** the PMS vendor's platform and card vault, the payment gateway, the P2PE solution provider, the booking engine, the channel manager, the productivity suite, the revenue-management system, the chatbot, the guest Wi-Fi and TV networks, and the cloud provider's infrastructure.

**PCI scope note.** Because the staff network is flat, every system on it is in PCI scope for MID-1 today. After segmentation, only the payment VLAN and the systems that can affect it stay in scope. The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Payment gateway (SYS-02) | Bidirectional | Authorizations, tokens, settlement | Merchant agreement MID-1; gateway AOC dated 2025-02, **more than 12 months old (gap)** |
| P2PE solution provider (SYS-05) | Outbound encrypted card data | Restaurant payments | Merchant agreement MID-2; P2PE Instruction Manual |
| Booking engine (SYS-03) | Inbound reservations and tokens | Direct bookings | Contract; AOC 2026-01 |
| Channel manager (SYS-04) | Inbound reservations and virtual card numbers | Online travel agency bookings | Contract; **no AOC (gap)** |
| Revenue-management system (SYS-12) | Outbound bookings; inbound rates | Aggregated stay data; rates | Contract; **pooled benchmarking clause (gap)** |
| Guest chatbot (SYS-13) | Bidirectional through the cloud integration | Availability, rates, guest questions | Contract; **no retention or masking terms (gap)** |
| Productivity suite (SYS-11) | Inbound email | Card authorization forms (**to be stopped**) | Service terms |
| Lock vendor and MSP remote support | Inbound remote sessions | Administrative access | Service contracts; **no MFA (gap)** |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| PMS tenant | SaaS | PMS vendor | Front Office Manager |
| Front desk chip terminals (4) | Payment device | Front desk | Controller |
| Restaurant POS stations (5) and P2PE devices (14) | POS and payment devices | Restaurant and bars | Food and Beverage Director |
| Firewall, switches, staff Wi-Fi | Network | Ground-floor server room | IT Manager |
| Front desk PCs (6), reservations PCs (2), back office PCs and laptops (26), tablets (12) | Endpoint | Hotel | IT Manager |
| Lock server and encoders (3) | On-premises server and devices | Server room; front desk | Chief Engineer |
| Identity provider tenant | SaaS | Identity vendor | IT Manager |
| Reporting database, guest-marketing hub, chatbot integration, backup vault | Managed database, serverless function, object storage, backup service | Cloud tenant | IT Manager |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 65 controls:
- Implemented: 6
- Partially implemented: 39
- Planned: 20
- Not applicable: 0

Inheritance: 45 system-specific, 18 hybrid, 2 common (inherited from providers).

### 10.2 Control assessment status
Assessed 2026-08-03 to 2026-08-07. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
Staff sign in to email and the cloud console through the identity provider with a password and a phone authenticator app. PMS administrators use the same. **Non-administrator PMS users sign in with a PMS password only**, which is not adequate for users who can reach card data; single sign-on with MFA for all PMS users is due 2026-10-31 (POAM-003).

Guests use the booking engine's own accounts, which are governed by the vendor and outside this boundary.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis and SAQ decision (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 benchmark and PMS vendor report review (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **AOC:** attestation of compliance (PCI DSS)
- **ASV:** approved scanning vendor
- **EDR:** endpoint detection and response
- **MID:** merchant identification (merchant account)
- **MSP:** managed service provider
- **P2PE:** point-to-point encryption (PCI SSC validated solution)
- **PMPS:** Property Management and Point-of-Sale Platform
- **PMS:** property management system
- **POA&M:** plan of action and milestones
- **SAQ:** self-assessment questionnaire

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan | IT Manager |
