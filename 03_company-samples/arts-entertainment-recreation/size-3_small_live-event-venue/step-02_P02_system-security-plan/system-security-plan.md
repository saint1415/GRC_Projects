# System Security Plan: Ticketing and Venue Operations Platform (TVOP)

**Organization:** Cris Santos Company, LLC (live event venue operator with ticketing) | **Tier:** Small | **Vertical:** Arts, Entertainment, and Recreation
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Ticketing and Venue Operations Platform (**TVOP**), identifier CSC-SYS-001.

## 2. System Overview
The TVOP supports selling tickets, admitting attendees, settling shows, and reaching patrons for the company's one Florida venue building (the Hall and the Lounge). It serves 60 employees, about 220 event-day workers from staffing contractors, and about 260,000 patron accounts, and it carries about 171,000 ticket card transactions a year under the ticketing merchant account (MID-T).

**Major components:**
- **SYS-01:** the company's configuration, users, pricing rules, bot mitigation settings, and checkout settings in a white-label ticketing SaaS platform
- **SYS-02 and SYS-04:** the box office channel: 6 box office PCs and 4 USB card readers from the payment partner
- **SYS-05:** a public-cloud tenant hosting the patron marketing database, the show settlement app, the nightly export function, and the backup vault
- **SYS-06:** an identity provider for single sign-on and MFA
- **SYS-08:** the venue network
- **SYS-09:** administrator endpoints and the 24 ticket scanners

The cloud tenant is described by service category and is vendor-agnostic (see P04). The food, beverage, and merchandise POS (SYS-03) is a separate vendor system under its own merchant account (MID-F) and connects to the TVOP only through settlement reports.

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| N71-R04 | PCI DSS v4.0.1 (contractual, through the merchant agreement). MID-T validates with SAQ D for Merchants in 2026 | PCI SSC standard; acquirer letter 2026-05-18 |
| N71-R05 | FTC Act Section 5 (patron data security, privacy and pricing claims) and the Rule on Unfair or Deceptive Fees for live-event tickets | 15 U.S.C. 45(a), (n); 16 CFR Part 464 |
| Federal | BOTS Act. The company is a protected ticket issuer; no compliance duty, but bot block records are evidence (P10) | 15 U.S.C. 45c |
| Card brand | Visa compromise reporting rules, applied through the acquirer | Visa *What To Do If Compromised* v10.0 (2026-06-25) |
| State | Florida Information Protection Act (breach notification and reasonable measures) | Fla. Stat. 501.171 |
| Internal | Security policies POL-01 to POL-05 | P06 |

Not applicable, as decided in the intake [obligations register](../step-00_P00_intake/obligations-register.csv): the gaming rules in the vertical profile (N71-R01 to R03, no gaming), and COPPA (N71-R06, services not directed to children).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the General Manager on 2026-08-31.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization. The equivalent internal decisions:
- The General Manager accepted continued operation of the TVOP on 2026-08-31, with the conditions in the P07 POA&M.
- The majority owner accepted the High risks in P01, with dated treatment plans, and will decide the PCI DSS scope option (P03 section 1.2) by 2026-09-30.
### 4.3 System Operational Status
Operational. Major modification planned: moving box office window sales and phone orders to the payment partner's validated P2PE devices by 2026-11-15. That change removes card data from the box office PCs and the corporate segment (P01 R-003, R-005).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | General Manager | Overall accountability; risk acceptance up to Moderate |
| Risk acceptor (authorizing official equivalent) | Majority owner | Acceptance of High and Very High risks; signs the AOCs |
| Information Security Lead | IT Manager | Day-to-day security; PCI DSS contact |
| Business owner, ticketing | Director of Ticketing | Ticketing users, pricing rules, bot mitigation, box office |
| PCI DSS validation and payments | Controller | Merchant agreement, SAQs, vendor AOCs |
| Checkout content and patron data | Marketing Director | Marketing settings, website, patron database |
| Operations support | Network and security integrator; ticketing vendor support | Firewall and Wi-Fi; platform support |

## 6. System Information Types and System Categorization
Information types are the closest analogs in NIST SP 800-60 Vol. 2 Rev. 1 (written for federal missions). Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Payment collection (card data in the box office channel; tokens and truncated numbers elsewhere) | Moderate | Moderate | Moderate | Card data disclosure triggers card brand, acquirer, and state breach duties; wrong charges harm patrons; box office can fall back to online sales (P05 MTD 8 h) |
| Customer services (patron accounts, orders, marketing preferences) | Moderate | Moderate | Moderate | About 260,000 patron records; entry at the doors depends on accurate order data, but a manual entry procedure limits the effect of an outage (P05 BP-01) |
| Financial management (show settlements, artist payments) | Moderate | Moderate | Low | Wrong or redirected payments cause direct losses; settlement can be rebuilt from reports (P05 MTD 24 h) |
| Personal identity and authentication (workforce identities) | Moderate | Moderate | Low | Account takeover is the lead High risk (P01 R-001) |
| **TVOP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Why availability is not High.** An outage during doors has a severe effect on operations and could affect attendee safety (P05 BP-01). The plan relies on a **manual entry procedure** and offline scanning, not on IT recovery, to keep that effect at the Moderate level. Until that procedure is written and drilled (P01 R-034, due 2026-11-30), this rating is an assumption the Operations Director owns.

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 60-person venue operator, with CA-8 added from the High baseline because PCI DSS 11.4 requires penetration testing. The plan documents the 71 controls that carry the PCI DSS and FTC obligations (see `control-implementation.csv`). Every other Moderate-baseline control is treated as follows:
- **Inherited** from the ticketing vendor, payment partner, cloud provider, and SaaS providers, as evidenced by their PCI DSS AOCs and SOC 2 reports (P09).
- **Out of scope for this tier**, recorded as a tailoring decision, where the control's purpose applies only to federal systems.

## 7. Authorization Boundary Description
The boundary was drawn from the intake [asset inventory](../step-00_P00_intake/asset-inventory.csv). It contains company-managed components and the company's configuration of vendor services:
- **Inside:** the company's tenant configuration in the ticketing platform (34 venue users, pricing and bot mitigation settings, marketing and checkout settings, API keys); the 6 box office PCs and 4 box office card readers; the cloud tenant (patron database, settlement app, export function, backup vault); the identity provider tenant; the venue network (firewall, switches, Wi-Fi); 42 other PCs and laptops that share the corporate segment; and the 24 ticket scanners.
- **Outside (external services, interconnected):** the ticketing vendor's platform and hosted checkout, the payment partner's gateway, the acquirer, the POS and its P2PE solution (SYS-03), the productivity suite (SYS-07), CCTV and door access (SYS-10), the website and email service (SYS-11), and finance and payroll (SYS-12).

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Ticketing vendor platform (SYS-01) | Bidirectional (web and API) | Orders, patron records, scan manifests, settlement reports | Ticketing services agreement; vendor PCI DSS AOC 2026-02-20; **no breach notice time in the contract (gap)** |
| Payment partner (SYS-02) | Outbound card data from box office readers and PCs; inbound authorizations | Card data (MID-T) | Merchant agreement; partner AOC **dated 2024 (gap)** |
| Acquirer | Settlement and chargeback data through the partner | Transaction records | Merchant agreement (24-hour compromise notice term, fictional) |
| POS vendor (SYS-03) | Inbound daily sales reports | Sales totals by show | POS agreement; P2PE listing |
| Website and email service (SYS-11) | Outbound weekly subscriber list from SYS-05 | Names, emails, preferences | Service terms |
| Marketing agency | Accounts on SYS-01; receives campaign lists | Patron segments | **Agency contract has no security or data-use terms (gap)** |
| Bank | Outbound payment files from settlement | Artist and vendor payments | Online banking agreement |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| Ticketing tenant configuration and 34 venue users | SaaS configuration | Ticketing vendor | Director of Ticketing |
| Checkout and marketing settings (including 9 company-added scripts, to be removed) | SaaS configuration | Ticketing vendor | Marketing Director |
| Box office PCs (6) and USB card readers (4) | Endpoint and payment device | Box office | Director of Ticketing |
| Patron marketing database | Managed database | Cloud tenant | Marketing Director |
| Settlement app | Cloud application service | Cloud tenant | Controller |
| Nightly export function and ticketing API key | Serverless function | Cloud tenant | IT Manager |
| Backup vault | Cloud backup service | Cloud tenant (same account, **gap**) | IT Manager |
| Identity provider tenant | SaaS | Identity vendor | IT Manager |
| Firewall, switches, Wi-Fi controller | Network | Venue building | IT Manager |
| Other PCs and laptops (42) | Endpoint | Offices | IT Manager |
| Ticket scanners (24) | Handheld device | Doors (managed through SYS-01) | Operations Director |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 71 controls:
- Implemented: 10
- Partially implemented: 33
- Planned: 27
- Not applicable: 1 (AC-4, enforced through SC-7 firewall rules at this tier)

### 10.2 Control assessment status
Assessed 2026-08-03 to 2026-08-07. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
Workforce users of email, the cloud console, and accounting authenticate through the identity provider with a password and a phone authenticator app. **Ticketing platform users do not use the identity provider.** They sign in with local passwords, and MFA is available but not enforced. That falls short of what the Moderate categorization and PCI DSS 8.4 require for administrative and CDE access. Enforcing the platform's MFA for all 34 venue users is due 2026-09-30 (POAM-003). Federating the platform to the identity provider will be evaluated at contract renewal.

Patrons create accounts on the ticketing vendor's platform with the vendor's own sign-in controls. That is governed by the vendor and outside this boundary.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), intake evidence, inventories and obligations register ([step-00](../step-00_P00_intake/intake-report.md)), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness and vendor reviews (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **AOC:** attestation of compliance (PCI DSS)
- **ASV:** Approved Scanning Vendor
- **CDE:** cardholder data environment
- **MID-T / MID-F:** the ticketing and the food, beverage, and merchandise merchant accounts
- **MFA:** multi-factor authentication
- **P2PE:** point-to-point encryption (PCI SSC validated solutions)
- **POA&M:** plan of action and milestones
- **SAQ:** self-assessment questionnaire
- **TVOP:** Ticketing and Venue Operations Platform

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan | IT Manager |
