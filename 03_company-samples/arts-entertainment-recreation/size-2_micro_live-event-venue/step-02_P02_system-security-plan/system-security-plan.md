# System Security Plan: Ticketing and Venue Operations Platform (TVOP)

**Organization:** Cris Santos Company, LLC (live event venue operator with ticketing; one music club) | **Tier:** Micro | **Vertical:** Arts, Entertainment, and Recreation
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Ticketing and Venue Operations Platform (**TVOP**), identifier CSC-SYS-001.

## 2. System Overview
The TVOP supports selling tickets, admitting attendees, settling shows, and reaching patrons for the company's one Florida music club. It serves 7 employees, about 20 contractor workers per show, and about 47,000 patron accounts, and it carries about 16,400 ticket card transactions a year under the ticketing merchant account (MID-T).

The company owns almost no infrastructure. Most of the TVOP is vendor SaaS, and a managed service provider (MSP) runs the office computers, network, and productivity suite. This plan therefore says, for each control, what the company does itself, what the MSP does for it, and what it inherits from a SaaS vendor.

**Major components:**
- **SYS-01:** the company's configuration, users, price tiers, demand tools settings, and checkout widget settings in a white-label ticketing SaaS platform
- **SYS-02 and the door tablets:** the door sales channel: 2 tablets running the box office app with 2 Bluetooth P2PE card readers from the payment partner
- **SYS-04:** the back-office PC (where phone orders are typed today), the bar office PC, 3 laptops, and 3 scanners
- **SYS-05:** the productivity suite: 7 named mailboxes, 2 shared mailboxes, and shared files (settlement workbooks, contracts)
- **SYS-06:** the venue network: firewall, one staff Wi-Fi, separate patron guest Wi-Fi, one internet line
- **SYS-07:** the website on a website builder SaaS, whose event pages host the ticketing checkout widget
- **SYS-11:** the SaaS-to-SaaS suite backup, operated by the MSP

The bar POS (SYS-03) is a separate vendor system under its own merchant account (MID-F) with validated P2PE readers. It connects to the TVOP only through settlement reports.

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| N71-R04 | PCI DSS v4.0.1 (contractual, through the merchant agreements). Validation type for MID-T is open (P03 section 1.2) | PCI SSC standard; acquirer letter 2026-06-08 |
| N71-R05 | FTC Act Section 5 (patron data security, privacy and pricing claims) and the Rule on Unfair or Deceptive Fees for live-event tickets | 15 U.S.C. 45(a), (n); 16 CFR Part 464 |
| Federal | BOTS Act. The company is a protected ticket issuer; no compliance duty, but bot screening records are evidence (P10) | 15 U.S.C. 45c |
| Card brand | Visa compromise reporting rules, applied through the acquirer | Visa *What To Do If Compromised* v10.0 (2026-06-25) |
| State | Florida Information Protection Act (breach notification) | Fla. Stat. 501.171 |
| Internal | Security policies POL-02, POL-03, POL-04 | P06 |

Not applicable: the gaming rules in the vertical profile (N71-R01 to R03), because the club has no gaming, and COPPA (N71-R06), because the services are not directed to children.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Owner and General Manager on 2026-08-31.

### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization. The equivalent internal decision: on 2026-08-31 the Owner and General Manager accepted continued operation of the TVOP, on the condition that the POA&M items in P07 are completed by their dates and the four High risks in P01 are treated by their due dates (the last by 2026-12-15). The Owner also decides the PCI DSS scope option (P03 section 1.2) by 2026-09-30.

### 4.3 System Operational Status
Operational. Planned changes by 2026-09-30: card numbers no longer taken by phone or email, so no card number reaches the back-office PC or the mailbox (P03 Option B); MFA on every ticketing and website login. Later: a separate staff network for the door tablets and the back-office PC (2026-10-31) and a cellular failover router (2026-11-30).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner and risk acceptor | Owner and General Manager | Overall accountability; accepts Moderate risk; approves dated plans for High risk; approves this plan, policies, and spending; signs the SAQs and AOCs |
| Security and Privacy Lead | Venue Manager | Day-to-day security; PCI DSS contact; maintains this plan, the risk register, and the service provider list; MSP liaison |
| Ticketing business owner | Box Office and Ticketing Manager | Ticketing users and roles, price tiers, demand tools, door sales, shared box office mailbox |
| Website and patron communications | Marketing Coordinator | Website content and scripts (with the freelance web designer), email marketing |
| Payments and settlement records | Bookkeeper | Merchant statements, acquirer portal, settlement workbooks |
| IT operations | MSP | Office computers, firewall, Wi-Fi, suite administration and backup |
| Independent assessor | Security consultant | Annual control assessment (P07) |

**Where roles overlap and how that is compensated.** The Venue Manager runs event-night operations and also leads security, and the Owner is both a ticketing administrator and the risk acceptor. The company cannot separate those roles at 7 people. Independent checks come from outside: an independent consultant assesses the controls (P07), the MSP supplies evidence for the controls it runs, and the ticketing vendor's SOC 2 report and AOC cover the vendor side (P09).

## 6. System Information Types and System Categorization
Information types are the closest analogs in NIST SP 800-60 Vol. 2 Rev. 1 (written for federal missions). Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Payment collection (card data typed for phone orders and found in email; tokens and the last 4 digits elsewhere) | Moderate | Moderate | Moderate | Card data disclosure triggers acquirer, card brand, and state breach duties; wrong charges harm patrons; door sales can fall back to cash (P05 MTD 4 h) |
| Customer services (patron accounts, orders, marketing preferences) | Moderate | Moderate | Moderate | About 47,000 patron records; entry at the door depends on accurate order data, but a manual door procedure limits the effect of an outage (P05 BP-01) |
| Financial management (show settlements, artist payments) | Moderate | Moderate | Low | Wrong or redirected payments cause direct losses; settlements can be rebuilt from vendor reports (P05 MTD 24 h) |
| Personal identity and authentication (workforce and shared logins) | Moderate | Moderate | Low | Takeover of a shared login is a lead High risk (P01 R-001, R-002) |
| **TVOP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Why availability is not High.** An outage in the hour after doors could affect attendee safety (P05 BP-01). The plan relies on a manual door procedure and offline scanning, not on IT recovery, to keep that effect at Moderate. Until that procedure is written and drilled (P01 R-020, due 2026-10-31), this rating is an assumption the Venue Manager owns.

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 7-person club. The plan documents 42 controls that carry the PCI DSS and FTC obligations and basic cyber hygiene (see `control-implementation.csv`). All other Moderate-baseline controls are handled one of two ways:
- **Inherited** from the ticketing vendor, payment partner, POS vendor, and SaaS providers (platform, physical, and application controls), with their PCI DSS AOCs and SOC 2 reports as evidence (P09).
- **Tailored out** for this tier, where the control addresses federal program management or organizations with dedicated IT staff (for example, separate development environments and configuration change boards). These are recorded as tailoring decisions, not gaps.

## 7. Authorization Boundary Description
The boundary was drawn from the intake [asset inventory](../step-00_P00_intake/asset-inventory.csv). It contains what the company controls or pays someone to control on its behalf:
- **Inside:** the company's tenant configuration in the ticketing platform (9 venue users, price tiers, demand tools settings, checkout widget settings, API tokens); the 2 door tablets and 2 door readers plus the spare reader; the back-office PC, the bar office PC, 3 laptops, and 3 scanners; the productivity suite tenant; the venue network; the website builder account and its pages and scripts; and the MSP-operated suite backup.
- **Outside (external services, interconnected):** the ticketing vendor's platform and checkout widget code, the payment partner's gateway and P2PE solution, the acquirer, the bar POS and its P2PE solution (SYS-03), the email marketing service (SYS-08), finance and payroll (SYS-09), CCTV (SYS-10), and the MSP's remote management platform.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Agreement |
|---|---|---|---|
| Ticketing vendor platform (SYS-01) | Bidirectional (web, apps, API) | Orders, patron records, scan manifests, settlement reports | Ticketing services agreement; vendor PCI DSS AOC (2026-03-12); **no breach notice time in the contract (gap)** |
| Payment partner (SYS-02) | Outbound encrypted card data from the door readers; phone-order card data typed on the back-office PC; inbound authorizations | Card data (MID-T) | Merchant agreement; **partner AOC never requested until 2026-08-14 (gap)** |
| Acquirer | Settlement and chargeback data through the partner and the POS vendor | Transaction records | Merchant agreements (24-hour compromise notice term, fictional) |
| POS vendor (SYS-03) | Inbound sales reports | Bar sales totals by show | POS agreement; P2PE listing |
| Email marketing service (SYS-08) | Outbound subscriber lists uploaded by hand | Names, emails, preferences | Service terms |
| Former email marketing service | Outbound nightly patron sync through an old API token | Names, emails, order history | **None (lapsed). Found in P07 testing; token revoked 2026-08-12** |
| Freelance web designer | Administrator access to the website | Website content and scripts | **No written security terms (gap)** |
| Bank | Outbound artist payments | Payment instructions | Online banking agreement |
| MSP remote management platform | Inbound administrative access | Device management | MSP service contract (**no incident notice term**) |

## 9. System Component Inventory
| Component | Type | Location or provider | Owner |
|---|---|---|---|
| Ticketing tenant configuration and 9 venue users | SaaS configuration | Ticketing vendor | Box Office and Ticketing Manager |
| Checkout widget and demand tools settings | SaaS configuration | Ticketing vendor | Box Office and Ticketing Manager |
| Door tablets (2) and P2PE door readers (2, plus 1 spare) | Endpoint and payment device | Door box office; spare in the back office safe since 2026-07-22 | Box Office and Ticketing Manager |
| Back-office PC and bar office PC | Endpoint | Back office; bar office | Venue Manager (MSP operates) |
| Laptops (3) | Endpoint | Owner, Venue Manager, Marketing Coordinator | Venue Manager (MSP operates) |
| Ticket scanners (3) | Handheld device | Door (managed through SYS-01) | Venue Manager |
| Productivity suite tenant, mailboxes, shared files | SaaS | Productivity suite vendor | Venue Manager (MSP administers) |
| Firewall, staff Wi-Fi, guest Wi-Fi | Network | Back office network closet | Venue Manager (MSP operates) |
| Website builder account, pages, and 6 scripts | SaaS | Website builder vendor | Marketing Coordinator |
| Suite backup subscription | SaaS | Backup vendor (resold by the MSP) | Venue Manager (MSP operates) |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 42 controls:
- Implemented: 5
- Partially implemented: 23
- Planned: 14
- Not applicable: 0

By responsibility: 19 system-specific (the company), 19 hybrid (the company with a vendor or the MSP), 4 common/inherited (fully provided by a SaaS vendor).

### 10.2 Inherited and MSP-provided controls
| Provider | What the company relies on | Evidence | What the company must still do |
|---|---|---|---|
| Ticketing vendor | Platform security, checkout widget code, card data handling, encryption in transit (SC-8), lockout (AC-7), audit records (AU-2), backups (CP-9) | PCI DSS AOC 2026-03-12 and SOC 2 Type 2 report, reviewed 2026-08-19 (P09) | Complementary user entity controls: user management, MFA enforcement, API token control, audit log review, and protecting the pages where it embeds the widget |
| Payment partner | P2PE solution for the door readers; gateway and tokenization | PCI SSC listing checked 2026-07-15; AOC requested 2026-08-14 | Reader inventory and inspections per the P2PE instruction manual |
| POS vendor | P2PE solution for the bar readers | PCI SSC listing | Reader inventory and inspections; named clerk logins |
| Productivity suite vendor | Platform security, encryption (SC-8, SC-28), lockout (AC-7), logging (AU-2) | Vendor documentation | Account management, MFA, shared mailbox settings, log review |
| MSP | Patching (SI-2), anti-malware (SI-3), firewall and Wi-Fi (SC-7, AC-18), encryption (SC-28), suite backup (CP-9), screen lock (AC-11) | Monthly MSP report; P07 evidence requests | Oversight: approve exceptions, review reports monthly, yearly MSP security questions (P01 R-015) |

**Inherited does not mean done.** Four of the ticketing vendor's complementary user entity controls are open gaps at the company: MFA (IA-2(1)), user management (AC-2), API token control (found in P07), and audit log review (AU-6).

### 10.3 Control assessment status
Assessed 2026-08-10 to 2026-08-12 by an independent consultant. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
Staff sign in to the productivity suite with a password and a phone authenticator app. **Ticketing platform and website users do not have MFA.** They use local passwords, and two logins are shared. That falls short of what the Moderate category and PCI DSS 8.4 expect for administrator access. Enforcing the ticketing platform's MFA for every venue user, named door logins for contractor staff, and MFA on the website administrator account are due 2026-09-30 (P07 POAM-001, POAM-003). Patrons create accounts with the ticketing vendor's own sign-in controls, which are outside this boundary.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), intake evidence, inventories and obligations register ([step-00](../step-00_P00_intake/intake-report.md)), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness and vendor report review (P09), AI assessment (P10). The `evidence` column in `control-implementation.csv` cites the [evidence register](../step-00_P00_intake/evidence-register.csv) ID behind each statement.

## 13. Acronym List and Glossary
- **AOC:** attestation of compliance (PCI DSS)
- **ASV:** Approved Scanning Vendor
- **MFA:** multi-factor authentication
- **MID-T / MID-F:** the ticketing and the bar and merchandise merchant accounts
- **MSP:** managed service provider
- **P2PE:** point-to-point encryption (PCI SSC validated solutions)
- **POA&M:** plan of action and milestones
- **SAQ:** self-assessment questionnaire
- **TVOP:** Ticketing and Venue Operations Platform

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan | Venue Manager (Security and Privacy Lead) |
