# System Security Plan: Ticketing and Venue Operations Platform (TVOP)

**Organization:** Cris Santos Company Holdings, Inc. (operated by the Ticketing and Streaming Technology division for the Live Venues and Hotels and Restaurants divisions and about 1,150 client venues) | **Tier:** Multi-Sector | **Vertical:** Arts, Entertainment, and Recreation
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-15

> **Why this system.** At this tier the SSP can cover one system per division or a shared corporate system. The group chose the **Ticketing and Venue Operations Platform**, because it is the one system all three divisions depend on (P05), it carries card data and patron data for the group and its clients, it inherits most of its controls from corporate (SYS-G1 to SYS-G3), and it carries the group's top risk (P01 GR-01). The other division systems (SYS-D1 venue estate, SYS-D2 hotel systems, SYS-D4 streaming) keep division plans that inherit from the same common control catalog (`common-control-catalog.csv`).

## 1. System Name and Identifier
Ticketing and Venue Operations Platform (**TVOP**), identifier CSCH-SYS-D3-TVOP. It is SYS-D3 in `../00_company-facts.md`, plus the venue edge components at the 30 integrated group venues.

## 2. System Overview
The TVOP sells and delivers tickets and admits patrons. It supports:
- **Live Venues:** event setup, pricing, on-sales, box office sales, and entry for about 22 million tickets a year at 30 integrated venues (the 8 acquired theaters are not yet on it).
- **Hotels and Restaurants:** event-and-stay packages sold on a hotels tenant (about 180,000 a year).
- **Ticketing and Streaming:** the same platform sold as a service to about 1,150 client venues (about 74 million tickets a year), and payment processing for streaming purchases.
- **About 68 million patron accounts** and about 41 million stored card-on-file tokens.

**Users:** about 2,300 workforce users with console access (engineers, client support, group ticketing staff), about 3,200 seasonal box office users at group venues, about 41,000 client tenant users (managed by clients), and patrons.

**Major components** (provider A primary in two regions; disaster recovery in provider B):
- **Event and inventory services:** event setup, seat maps, holds, price levels
- **Hosted checkout:** event pages, cart, and hosted payment fields; a tag manager lets tenants add marketing tags
- **Payment orchestration and token vault:** authorization routing to 3 acquirers and gateways; card numbers encrypted with keys held in hardware security modules (HSMs). This is the **cardholder data environment (CDE)**
- **Patron accounts and customer identity service**
- **Mobile tickets and access control service:** rotating barcodes; scan validation
- **Dynamic pricing module and bot detection with virtual queue** (P10)
- **Box office app** on managed stations with validated P2PE devices (venue edge)
- **Access control scanners** (venue edge, managed devices)
- **Data services:** order database, reporting, exports, and feeds to the patron data platform (SYS-G4)

The platform is described by service category and is vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies to the TVOP |
|---|---|---|---|
| N71-R04 | PCI DSS v4.0.1 | PCI SSC standard (contractual, not law) | **Primary.** The TVOP stores, processes, and transmits card data. The Ticketing and Streaming division validates it as a **service provider** with an annual ROC by a QSA (AOC 2026-03-31). Live Venues and Hotels and Restaurants rely on it as **merchants**, and their own ROC and SAQ list it as a third-party service provider (Requirement 12.8). The same standard is N72-R01 for the hotels division |
| N71-R05 / N51-R01 | FTC Act Section 5 | 15 U.S.C. 45(a), (n) | Reasonable security for patron data; security and privacy statements to patrons and clients must be true |
| N71-R05 | FTC Rule on Unfair or Deceptive Fees | 16 CFR Part 464 (live-event tickets and short-term lodging are covered goods, 464.1) | Event pages and checkout must show total prices (464.2) and must not misrepresent fees (464.3). The platform renders prices for every tenant |
| None (statute) | BOTS Act | 15 U.S.C. 45c | Protects ticket issuers; the TVOP's bot detection records are evidence for enforcement (P10) |
| None (regulation) | ADA Title III ticketing | 28 CFR 36.302(f) | Accessible seating pricing and sale methods; the pricing module and the bot challenge must not break them (P10) |
| N51-R03 | CCPA and CPPA regulations | Cal. Civ. Code 1798.100 et seq.; Cal. Code Regs. tit. 11, 7120-7124 | The group does business in California and exceeds the revenue threshold. For client patron data the division acts for its clients; first cybersecurity audit report due 2028-04-01 (P03) |
| N51-R04 | DOJ Data Security Program | 28 CFR Part 202 | Covered personal identifiers of more than 100,000 people; vendor access screened (P03) |
| N51-R08 | SEC cybersecurity disclosure | Reg S-K Item 106; Form 8-K Item 1.05 | A TVOP incident may be material to the group (P08) |
| N72-R04 and state law | State breach notification laws | Each state where affected individuals reside (Florida worked example: Fla. Stat. 501.171) | Card numbers with security codes, and email with password, are personal information (501.171(1)(g)). The division is a third-party agent of its client venues (501.171(6)) |
| Contracts | Client agreements; SOC 2 commitments; card brand rules | 2024 client agreement; SOC 2 (Security, Availability, Confidentiality); Visa What To Do If Compromised v10.0 | Client notice terms (24 or 72 hours); 99.95% availability; card brand compromise clocks |
| Internal | Group policies POL-01 to POL-05 and division supplements | P06 | |

Not applicable: Nevada Reg. 5.260, NIGC MICS, and casino BSA/AML (N71-R01 to R03), because no division conducts gaming; COPPA (N71-R06, N51-R02), because the platform is general audience and accounts require age 18 or older; FedRAMP (N51-R07), because there are no federal customers.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Group CISO and the General Manager Ticketing (system owner) on 2026-09-15, after the board risk committee review.

### 4.2 System Authorization Decision
The group is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- **Decision:** authorized to operate with conditions, 2026-09-15, by the Group CISO and the Group Chief Risk Officer (acceptance authority for High risks).
- **Conditions:** (1) tenant-added tags removed from all checkout pages or brought under the script inventory, authorization, and change-and-tamper detection by 2026-11-30 (POAM-006, POAM-007); (2) no new tenant feature that adds content to payment pages without a payment page security review; (3) MFA required for all client tenant administrators by 2027-01-31 (POAM-010).
- **Reauthorization:** annually, aligned with the service provider ROC, or after a major change.

### 4.3 System Operational Status
Operational. **Major modification planned:** checkout tag isolation (tags allowed on event pages only, never in the payment step) and onboarding of the 8 acquired theaters by 2027-03-31.

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | General Manager Ticketing | Accountable for the TVOP and this SSP |
| Authorizing official equivalent | Group CISO with the Group Chief Risk Officer | Authorization decision; High risk acceptance |
| Technical owner | Chief Technology Officer (Ticketing and Streaming) | Architecture, releases, and system-specific controls |
| CDE owner | Director of Payments Engineering | Payment orchestration, token vault, and key custodians |
| PCI DSS program | Group PCI program director | Scope documents, QSA relationship, provider list |
| Data owners | VP Ticketing and Box Office (group venue tenants); VP Revenue Management (hotels tenant); each client for its own tenant data | Approve access and data uses for their tenant |
| Privacy oversight | Group Chief Privacy Officer | Purposes, feeds to the patron data platform, client data terms |
| Common control providers | Group identity director (SYS-G1), Group SOC director (SYS-G2), Group cloud platform director (SYS-G3) | Operate inherited controls (`common-control-catalog.csv`) |
| Independent assessors | Group internal audit; the external QSA | Common controls and samples (P07); annual ROC |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1 where a close match exists. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Customer payment data (card numbers in the CDE; tokens elsewhere) | **High** | High | High | Aggregation of about 41 million stored card tokens and live card entry for about 96 million tickets a year. A compromise would trigger card brand investigations for three merchant roles and 1,150 clients |
| Patron identity and order data | **High** | Moderate | High | About 68 million accounts with email and password; state breach duties; client contract notices |
| Ticket inventory, pricing, and access credentials | Moderate | **High** | **High** | Oversold or counterfeit tickets and wrong prices harm patrons and clients; event entry depends on the access control service (P05 MTD 1 to 2 hours) |
| Information security (keys, HSMs, access policies, logs) | High | High | Moderate | Compromise would expose the CDE |
| **TVOP category (high-water mark)** | **High** | **High** | **High** | Overall **High** |

**Baseline:** the NIST SP 800-53B **High** baseline, tailored. The plan documents **171 controls** in `control-implementation.csv`:
- 167 from the High baseline;
- 2 from the privacy baseline (PT-2, PT-3), added because purpose limits on patron and client data are a main risk (gap 3);
- 2 program management controls not in any baseline (PM-1, PM-2).

Other High-baseline controls are fully inherited from the cloud providers (for example, most PE and MP controls, evidenced by their SOC 2 reports) or tailored out with a reason in the group tailoring register.

## 7. Authorization Boundary Description
- **Inside:** the TVOP accounts in provider A (event and inventory services, hosted checkout and tag manager, payment orchestration and token vault in a separate CDE account, patron accounts, access control service, pricing and bot modules, data services), the disaster recovery accounts in provider B, and the venue edge at the 30 integrated venues (box office stations, P2PE devices, scanners, venue operations consoles).
- **Outside, inherited (common control providers):** SYS-G1 identity platform, SYS-G2 SOC, SIEM, and EDR, and the SYS-G3 landing zones and WAN.
- **Outside, interconnected:** acquirers and gateways; the P2PE solution provider; client systems through ticketing APIs; the hotel PMS (package room releases); the patron data platform (SYS-G4); the streaming service (SYS-D4) for purchases; the tag management vendor and other script vendors whose code runs in patrons' browsers on checkout pages.

The diagram is in P04 `cloud-architecture.md` (the TVOP subgraph).

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Acquirers and gateways (3) | Outbound and inbound | Authorization requests and responses (card data) | Processing agreements; each holds a current PCI DSS AOC |
| P2PE solution provider | Inbound from venue devices | Encrypted card data from box office devices | P2PE solution agreement and instruction manual |
| Client venue systems (APIs) | Both | Orders, patron contact data, attendance (no card numbers) | 2024 client agreement (212 clients still on pre-2024 terms) |
| Hotel PMS (SYS-D2) | Both | Package room releases and reservations | Intercompany service terms |
| Patron data platform (SYS-G4) | Outbound nightly | Group tenant orders and patrons; **all tenants' purchaser data for pricing model training** (gap 3, POAM-012) | Group data use register; client agreements |
| Streaming (SYS-D4) | Inbound | Purchase requests; returns tokens | Intercompany service terms |
| Tag management vendor and script vendors | Code delivered to patrons' browsers | Can read anything on the page, including payment fields if not isolated | **No security assessment or contract terms** (POAM-009) |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| Event, inventory, and pricing services | Containers (PaaS) | Provider A, two regions | Chief Technology Officer |
| Hosted checkout and tag manager | Containers and CDN | Provider A; CDN | Chief Technology Officer |
| Payment orchestration and token vault | Containers in a separate CDE account; managed HSMs | Provider A, two regions | Director of Payments Engineering |
| Order and patron databases | Managed relational databases (PaaS) | Provider A; replica in provider B | Chief Technology Officer |
| Customer identity service | SaaS | Identity vendor | General Manager Ticketing |
| Access control service and scanners | Containers; managed handheld devices | Provider A; 30 venues | General Manager Ticketing; VP Venue Operations |
| Box office stations and P2PE devices | Managed workstations; P2PE devices | 30 venues | VP Ticketing and Box Office |
| Disaster recovery region and backup vault | Database replicas; immutable vault | Provider B | Group cloud platform director |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv` (171 controls) and `common-control-catalog.csv` (127 group common and hybrid controls).

| Status | Controls |
|---|---|
| Implemented | 152 |
| Partially implemented | 19 |
| Planned | 0 |
| Not applicable | 0 |
| **Total** | **171** |

| Inheritance | Controls |
|---|---|
| Common/Inherited (from SYS-G1, SYS-G2, SYS-G3, group functions, or the cloud providers) | 106 |
| Hybrid (group or a provider supplies the mechanism; the TVOP configures or operates part) | 22 |
| System-specific | 43 |

**The 19 partially implemented controls** cluster in four places:
- **Checkout scripts added by tenants** (scenario gap 1): AC-22, CM-3, CM-7, CM-8, SA-9, SC-18, SI-7, SR-6, AU-6.
- **Access for people outside the core team:** AC-2 (seasonal box office accounts), AC-6 (support impersonation role), IA-8 (client administrators without MFA).
- **Data purpose** (gap 3): PT-2, PT-3.
- **Cross-division response and AI** (gaps 4 and 5): IR-3, IR-6, IR-8, AT-3, SA-11.

### 10.2 Common control inheritance by division
The common control catalog lists 127 controls that corporate provides (or passes through from the cloud providers) fully (106) or in part (21). Inheritance is **documented for Live Venues** (2025 inheritance matrix, which does not cover the 8 acquired theaters), for **Ticketing and Streaming** (its service provider ROC and SOC 2 system description carve in the group services), and for the TVOP (this plan). It is **not documented for Hotels and Restaurants** (scenario gap 6). Until POAM-014 closes, the hotels division cannot show its acquirer which PCI DSS requirements group controls meet, and its PMS sits outside SYS-G1 and the SIEM.

### 10.3 Control assessment status
Common controls were assessed once, and TVOP and division controls sampled, from 2026-07-01 to 2026-08-31 by group internal audit. See P07 `assessment-results.csv` and `poam.csv`. The QSA's 2026 service provider ROC (AOC 2026-03-31) is separate evidence for the CDE.

## 11. Digital Identity Acceptance Statement
- **Workforce users** authenticate through SYS-G1 federated sign-in with MFA (number matching); **administrators and key custodians** use phishing-resistant hardware keys and just-in-time PAM elevation. Box office staff use named sign-in with MFA on managed stations. This fits a High system with card data.
- **Client tenant users** authenticate to the customer identity service. MFA is offered to all and **should be required for administrators** (POAM-010), because a client administrator can change checkout content for that client's patrons.
- **Patrons** use email and password with breached-password screening and optional MFA, plus step-up checks for account changes. An email and password together are personal information under Fla. Stat. 501.171(1)(g)1.b, which shapes the incident runbook (P08).

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), group and division risk registers (P01), gap analyses and regulation-by-division matrix (P03), cloud architecture and control map (P04), BIA (P05), group policies and division supplements (P06), assessment and POA&M (P07), incident response runbook and notification matrix (P08), SOC 2 readiness (P09), AI governance (P10).

## 13. Acronym List and Glossary
- **AOC:** attestation of compliance (PCI DSS)
- **CDE:** cardholder data environment
- **Common control:** a control provided once by corporate and inherited by several systems
- **HSM:** hardware security module
- **P2PE:** point-to-point encryption (a PCI-listed validated solution)
- **QSA:** Qualified Security Assessor
- **ROC:** Report on Compliance (PCI DSS)
- **Tag:** a script a tenant adds to its pages through the tag manager (for example analytics or advertising)
- **Tenant:** a venue organization's partition of the multi-tenant platform (group venues, the hotels tenant, or a client)
- **TVOP:** Ticketing and Venue Operations Platform

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-08-31 | Draft after P07 fieldwork | General Manager Ticketing |
| 1.0 | 2026-09-15 | Approved with authorization conditions | Group CISO |
