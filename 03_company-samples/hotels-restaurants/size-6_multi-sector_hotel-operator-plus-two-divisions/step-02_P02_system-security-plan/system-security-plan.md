# System Security Plan: Hotel Property Management and Point-of-Sale Platform (PMPS)

**Organization:** Cris Santos Company Holdings, Inc. (Hotels division, Cris Santos Hotels, LLC; inherits group common controls) | **Tier:** Multi-Sector | **Vertical:** Accommodation and Food Services
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-10

> **Why this system.** At this tier the SSP can cover one system per division or a shared corporate system. The group chose the **Hotels division's PMPS** because Hotels is the focus division, the PMPS carries most of the group's card transactions on the hotel side and every hotel's guest register, and it is where the shared legacy POS vendor (scenario gap 1) and the guest profile hub link (gap 2) meet. The PMPS inherits most of its controls from the group common control catalog (`common-control-catalog.csv`). The Attractions ticketing and gate platform (SYS-A1 and SYS-A2) and the Vacation Ownership loan platform (SYS-V2) keep division SSPs that inherit from the same catalog.

## 1. System Name and Identifier
Hotel Property Management and Point-of-Sale Platform (**PMPS**), identifier CSCH-HTL-PMPS. It covers SYS-H1, SYS-H3, and the property payment network segments of SYS-H4 in `../00_company-facts.md`.

## 2. System Overview
The PMPS runs hotel operations and card acceptance at **88 hotels**: 30 owned or leased and 58 managed for third-party owners. It supports:
- **Front office:** arrivals, room assignment, folios, night audit, and the guest register in the cloud PMS (about 9.8 million room nights a year).
- **Food and beverage:** 214 restaurant, bar, and in-room dining outlets that post room charges to the PMS.
- **Card acceptance:** front desk terminals (validated P2PE at 71 hotels; semi-integrated chip terminals at 17) and outlet POS (validated P2PE at 142 outlets; legacy integrated POS at 72 outlets in 23 hotels). About 13.9 million card transactions a year flow through the PMPS.

About 14,800 PMS users (front office, reservations, accounting, and managers at owned and managed hotels), about 6,100 POS users, and 46 service accounts use it.

**Major components:**
- **Cloud PMS tenant** (vendor SaaS; the Hotels division administers the multi-property tenant, roles, and interfaces)
- **Cloud POS** (vendor SaaS back office) with validated P2PE devices
- **Legacy integrated POS** (on-property POS servers and workstations at 23 hotels, managed and remotely supported by the legacy POS vendor)
- **Property payment segments** (SD-WAN edge firewalls and payment VLANs at each hotel, built from group templates)
- **Interface layer** (PMS interfaces to door lock servers, the CRS, SYS-G4 tokenization, and SYS-G5 loyalty lookups)

The design is described by service category and is vendor-agnostic (P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies to the PMPS |
|---|---|---|---|
| N72-R01 | PCI DSS v4.0.1 (contractual) | PCI SSC standard | The PMPS is in the Hotels merchant ROC (Acquirer A) and, for the 58 managed hotels whose owners are the merchants of record, in the Hotels service provider ROC. The division gives each owner its service provider AOC and a responsibility matrix (Requirement 12.9) |
| N72-R02 | FTC Act Section 5 | 15 U.S.C. 45(a), (n) | Reasonable security for guest and card data. *FTC v. Wyndham Worldwide Corp.*, 799 F.3d 236 (3d Cir. 2015), concerned a hotel company that managed hotels' PMS systems; the PMPS is the system the group manages for owners |
| N72-R03 | FTC Disposal Rule | 16 CFR 682.3 | Background-check reports for front office and outlet managers (PS-3; MP-6) |
| N72-R04 | State breach notification laws | Florida worked example: Fla. Stat. 501.171 | PMS guest data (names with ID document numbers) and card data captured at the PMPS are personal information in most states; Florida notice duties are in P08 |
| Florida guest register | Fla. Stat. 509.101(2) | Florida Statutes 2026 | The PMS is the guest register for the 26 Florida hotels: chronological, with dates of occupancy and rates, available for inspection, and may be electronic. Registers more than 2 years old need not be made available, so 2 years is the retention floor, not a reason to keep everything |
| N53-R03 | CCPA and CPPA regulations | Cal. Civ. Code 1798.100 et seq.; 11 CCR 7120-7124 | The group is a CCPA "business" (5 California hotels; revenue above $26,625,000). Guest data in the PMPS is in scope of the group's privacy program and its first cybersecurity audit (report due 2028-04-01) |
| N53-R05 | SEC cybersecurity disclosure | Reg S-K Item 106; Form 8-K Item 1.05 | A PMPS incident may be material to the group (P08) |
| N72-R06 | CIRCIA (proposed) | Proposed 6 CFR Part 226 | Tracked only. Not in effect; the group exceeds the SBA size standard, so it would be covered by the proposed size-based criterion if the rule is finalized as proposed |
| Contracts | Management agreements; merchant agreement with Acquirer A | Fictional terms | 31 of 58 management agreements predate 2020 and assign no security responsibilities or incident notice duties (gap 6; POAM-026) |
| Internal | Group policies POL-01 to POL-05 and the Hotels supplement | P06 | |

Not applicable: Illinois BIPA (N72-R05; no Illinois hotels); HIPAA; gaming rules.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Group CISO and the Hotels division payments and systems director (system owner) on 2026-09-10, after the board risk committee review.

### 4.2 System Authorization Decision
The group is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- **Decision:** authorized to operate with conditions, 2026-09-10, by the Group CISO and the Group Chief Risk Officer (acceptance authority for High risks).
- **Conditions:**
  1. Remove the legacy POS vendor's always-on remote tool and route all vendor support through group PAM by 2026-12-31 (POAM-001).
  2. Restrict the CRS integration service account to the loyalty fields the PMS and POS need by 2026-11-30 (POAM-013).
  3. Complete the P2PE replacement of the 72 legacy POS outlets and 17 non-P2PE front desks by 2027-06-30.
- **Reauthorization:** annually, after each QSA ROC, or when the legacy POS is retired.

### 4.3 System Operational Status
Operational. **Major modifications planned:** legacy POS replacement (61% of the group-wide program complete; due 2027-06-30) and front desk P2PE at the remaining 17 hotels.

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Hotels division payments and systems director | Accountable for the PMPS and this SSP |
| Authorizing official equivalent | Group CISO with the Group Chief Risk Officer | Authorization decision; High risk acceptance |
| Business owner | Hotels chief operating officer | Front office and food and beverage operations |
| PCI DSS program manager | Group Director of Payments and PCI Compliance | Merchant and service provider ROCs; responsibility matrices for owners |
| Division security lead | Hotels security and compliance lead | Hotels supplement; division register; Low risk acceptance |
| Common control providers | Group identity director (SYS-G1), Group SOC director (SYS-G2), Group cloud platform and network directors (SYS-G3), Group Director of Payments and PCI Compliance (SYS-G4) | Operate inherited controls |
| Owner liaison | Hotels senior vice president of owner relations | Responsibility matrices and incident notices to 41 ownership groups |
| Independent assessors | Group internal audit; the QSA | P07 assessment; ROCs |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1 and adjusted for this business. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Payment card data (collections and receivables) | **High** | Moderate | Moderate | Provisional Moderate, raised to High for aggregation: card data from about 13.9 million transactions a year passes through the PMPS, a compromise triggers card brand investigations across 88 hotels and 41 owners, and it could be material to the group (P08) |
| Guest reservation and identity data (customer services) | Moderate | Moderate | Moderate | Names, contact details, stay history, and identity document numbers captured at check-in. The full profile store is SYS-G5 (outside the boundary, rated High there) |
| Hotel operations (folios, room status, key encoding interface, guest register) | Low | Moderate | Moderate | Errors affect billing and guest access; front desks can run on downtime procedures for about 8 hours (P05 BP-H01) |
| Information security (keys, access policies, logs) | High | High | Moderate | Compromise would expose every property payment segment |
| **PMPS category (high-water mark)** | **High** | **High** | **Moderate** | Overall **High** |

**Baseline:** the NIST SP 800-53B **High** baseline, tailored. The plan documents **114 controls** in `control-implementation.csv`:
- 111 from the High baseline;
- PM-9 (risk management strategy), which is in the privacy baseline and is the basis for PCI DSS targeted risk analyses;
- 2 program management controls not in any baseline (PM-1, PM-2).

Other High-baseline controls are either fully inherited from the cloud providers and SaaS vendors (for example, most PE controls, evidenced by their SOC 2 Type 2 reports and AOCs) or tailored out with a reason in the group tailoring register (for example, controls for facilities the group does not operate). Where the CSF 2.0 to SP 800-53 crosswalk has no entry for a control (AC-8, AC-11, AU-8, IR-2, MA-4, MP-4, MP-6, PL-4, PS-3, PS-4, SR-9), the CSF subcategory in the CSV is an **author mapping**.

## 7. Authorization Boundary Description
- **Inside:** the cloud PMS tenant configuration, roles, and interfaces; cloud POS back office configuration and P2PE devices; legacy POS servers and workstations at 23 hotels; property payment segments (edge firewalls, payment VLANs, front desk and outlet workstations) at 88 hotels.
- **Outside, inherited (common control providers):** SYS-G1 identity, SYS-G2 SOC, SIEM, and EDR, SYS-G3 cloud platform and network hubs, and SYS-G4 group payment services (tokenization, vault, gateway).
- **Outside, interconnected:** SYS-H2 CRS and contact center, SYS-G5 guest profile hub, SYS-H4 door lock servers, SYS-H5 revenue management, and owners' corporate networks at 9 managed hotels.

The diagram is in P04 `cloud-architecture.md` (section 2.2).

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| SYS-H2 CRS | Two-way | Reservations, rates, guest profiles, card tokens | Internal interface specification |
| SYS-G4 group payment services | Two-way | Card authorizations; tokens back to the PMS | Internal service agreement; in all three PCI DSS validations |
| SYS-G5 guest profile hub | Inbound lookups | Loyalty status and profile fields. **Gap:** the CRS integration service account can read every hub table, including owners' bank data (POAM-013) | Internal interface specification |
| SYS-H4 door lock servers | Outbound | Room number, guest name, stay dates for key encoding | Lock vendor interface |
| Payment gateway and Acquirer A | Outbound | Authorizations and settlement | Merchant agreement; gateway AOC |
| Legacy POS vendor | Inbound remote support | Full administrative access to legacy POS servers. **Gap:** always-on tool outside PAM (POAM-001) | Support contract; vendor AOC covers software only |
| Owners' networks (9 managed hotels) | Two-way | Owner accounting extracts | Interconnection terms missing for older agreements (POAM-026) |
| Florida Division of Hotels and Restaurants | On request | Guest register (Fla. Stat. 509.101(2)) | Statute |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| Cloud PMS tenant | SaaS (vendor) | PMS vendor | Hotels division payments and systems director |
| Cloud POS back office and P2PE devices | SaaS plus devices | Cloud POS vendor; 142 outlets | Hotels vice president of food and beverage |
| Legacy POS servers and workstations | On-premises, vendor-managed | 23 hotels | Hotels vice president of food and beverage (vendor operates) |
| Front desk terminals | P2PE devices (71 hotels); semi-integrated chip terminals (17 hotels) | 88 hotels | Hotels division payments and systems director |
| Property payment segments | Edge firewalls and VLANs | 88 hotels | Group network director (template); hotel IT (local) |
| Front desk and outlet workstations | Managed endpoints with EDR | 88 hotels | Group endpoint engineering lead |
| Interface services | PaaS integration services | Cloud provider A | Hotels division payments and systems director |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv` (114 controls) and `common-control-catalog.csv` (91 group common or hybrid controls).

| Status | Controls |
|---|---|
| Implemented | 92 |
| Partially implemented | 22 |
| Planned | 0 |
| Not applicable | 0 |
| **Total** | **114** |

| Inheritance | Controls |
|---|---|
| Common/Inherited (from SYS-G1 to SYS-G5, group functions, or the cloud providers) | 71 |
| Hybrid (the group provides the mechanism; the Hotels division configures or operates part) | 20 |
| System-specific | 23 |

**The 22 partially implemented controls** cluster in four places:
- **The legacy POS and its vendor** (gap 1): AC-17, MA-4, PS-7, SA-9, SA-22, SC-8(1), SI-2, SI-3, IR-4, AU-6, SR-9, AT-3.
- **Accounts and access** (gap 2): AC-2, AC-2(12), AC-6, IA-5, IA-8.
- **Owners and notification** (gaps 6 and 8): CA-3, IR-3, IR-6.
- **Inventory and retention** (gap 12): CM-8, SI-12.

### 10.2 Common control inheritance by division
The common control catalog lists 91 controls provided or partly provided by corporate. Inheritance is **documented for Hotels** (2025 inheritance matrix and the ROC responsibility matrices) and **for Attractions** (2026-02 matrix), except ride and show control networks, which the catalog does not cover. It is **not documented for Vacation Ownership** (scenario gap 7). Vacation Ownership does not inherit SYS-G1 controls at all until its directory migration on 2027-03-31, so its Safeguards Rule access and MFA controls are division-operated today (P03; POAM-020, POAM-027).

### 10.3 Control assessment status
Common controls were assessed once, and PMPS and division controls sampled, from 2026-07-06 to 2026-08-28 by group internal audit. See P07 `assessment-results.csv` and `poam.csv`. The QSA assesses the PMPS for the 2026 merchant ROC from 2026-10-19.

## 11. Digital Identity Acceptance Statement
- **Workforce users** authenticate through SYS-G1 with MFA for all PMS access (PCI DSS 8.4.2); administrators use phishing-resistant authenticators and just-in-time PAM elevation.
- **Legacy POS local accounts** (112 at 23 hotels) use 6-digit PINs at outlet workstations inside the payment segment. They are accepted only until the legacy POS is retired, with compensating monitoring at the segment boundary (POAM-002, POAM-003).
- **Service accounts** use secrets from the group secret store; the CRS integration service account's key must rotate every 90 days (POAM-003).
- **Guests** do not access the PMPS directly; they sign in to SYS-G5, outside the boundary.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), group and division risk registers (P01), gap analyses and regulation-by-division matrix (P03), cloud architecture and control map (P04), BIA (P05), group policies and division supplements (P06), assessment and POA&M (P07), incident response runbook and notification matrix (P08), SOC 2 readiness (P09), AI governance (P10), 2025 merchant ROC and 2026 service provider ROC (QSA).

## 13. Acronym List and Glossary
- **AOC:** attestation of compliance
- **CDE:** cardholder data environment
- **Common control:** a control provided once by corporate and inherited by several systems
- **CRS:** central reservation system
- **P2PE:** point-to-point encryption (a PCI-listed validated solution)
- **PAM:** privileged access management
- **PMPS:** Hotel Property Management and Point-of-Sale Platform
- **POI:** point of interaction (payment terminal)
- **QSA:** Qualified Security Assessor
- **ROC:** Report on Compliance

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-08-28 | Draft after P07 fieldwork | Hotels division payments and systems director |
| 1.0 | 2026-09-10 | Approved with authorization conditions | Group CISO |
