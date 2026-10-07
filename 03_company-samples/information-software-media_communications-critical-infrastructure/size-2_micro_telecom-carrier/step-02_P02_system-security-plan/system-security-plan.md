# System Security Plan: Network Operations and Customer Billing Platform (OSS/BSS)

**Organization:** Cris Santos Company, LLC (rural fiber broadband and voice carrier) | **Tier:** Micro | **Vertical:** Communications
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Network Operations and Customer Billing Platform (**OSS/BSS**), identifier CSC-SYS-001.

## 2. System Overview
The OSS/BSS runs everything the company does for its about 1,420 accounts in one rural Florida town: customer accounts, orders, bills, and payments; the customer portal and its AI assistant; voice service for about 440 telephone numbers; and the fiber network that carries broadband for about 1,385 subscribers and 6 dedicated circuits. Its users are the 7 employees, the network engineering consultant, and the customers who use the portal.

At a carrier this size, "OSS" and "BSS" are not large platforms. The BSS is a vendor SaaS product. The voice side is a wholesale hosted voice platform that the company resells under its own brand. The OSS is a small stack in the network hut: the OLT element management system (EMS), DHCP, DNS, RADIUS, configuration backups, and a cloud monitoring service. The company runs the network itself; an MSP runs office IT. This plan says, for each control, what the company does, what the MSP or consultant does for it, and what it inherits from a SaaS vendor.

**Major components (inside the boundary):**
- **SYS-01:** billing and customer care system (BSS) with the customer portal (vendor SaaS)
- **SYS-02:** hosted voice platform: softswitch, numbers, voicemail, 911 routing, call detail records (CDRs) (wholesale provider SaaS; company admin portal)
- **SYS-03:** fiber access network: 2 OLTs, about 1,420 ONTs, aggregation switch
- **SYS-04:** network core and management: edge router with the remote-administration VPN; 2 hut servers (EMS, DHCP, DNS, RADIUS, configuration backups); provisioning link to SYS-01 through an API key
- **SYS-05:** network monitoring and alerting service (SaaS)
- **SYS-06:** productivity suite (email, shared drive)
- **SYS-07:** 4 desktops, 3 laptops, 3 technician tablets (MSP-managed)
- **SYS-08:** office network: firewall, staff Wi-Fi, guest Wi-Fi (MSP-managed)
- **SYS-09:** cloud backup of the productivity suite (MSP-operated)

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it touches this system |
|---|---|---|---|
| C-COMMUNICATIONS-R01 | FCC CPNI rules | 47 U.S.C. 222; 47 CFR 64.2001-64.2011 | Primary. The company is an interconnected VoIP provider, which the rules treat as a carrier (64.2003(o)). SYS-01, SYS-02, and SYS-10 hold or show CPNI: customer authentication (64.2010), training and certification (64.2009), breach notice (64.2011) |
| C-COMMUNICATIONS-R02 | FCC outage reporting | 47 CFR Part 4 (4.9, 4.18) | SYS-05 and SYS-04 detect outages; the Network Operations Lead files NORS notifications, notifies 911 outage contacts, and reports in DIRS when activated |
| C-COMMUNICATIONS-R03 | CALEA system security and integrity | 47 U.S.C. 1001-1010; 47 CFR 1.20000-1.20008 | Covered as a facilities-based broadband and interconnected VoIP provider (70 FR 59664). Intercepts run through SYS-02 and the TTP, outside this boundary; compromise reporting (1.20003(c)) is in the P08 runbook |
| C-COMMUNICATIONS-R05 | CIRCIA (pending rule) | 6 U.S.C. 681b; proposed 6 CFR Part 226 | Tracked only. No final rule in the Federal Register as of 2026-10-05 |
| State | Florida Information Protection Act (breach notification) | Fla. Stat. 501.171 | Driver license numbers and portal credentials in SYS-01 are Florida-defined personal information |
| Benchmark | NIST CSF 2.0 (voluntary) | P03 rows G-047 to G-054 | Used to define "reasonable measures" under 64.2010(a) |
| Internal | Security policies POL-02, POL-03, POL-04 | P06 | All components |

**Not applicable** (reasons in P03 section 1): SEC disclosure rules (C-COMMUNICATIONS-R06; privately held), submarine cable rules (C-COMMUNICATIONS-R04), CMRS-only CPNI rules (64.2010(h)), Emergency Alert System rules (no video or broadcast). Broadband usage data is not CPNI after *Ohio Telecom Ass'n v. FCC* (6th Cir. 2025), but POL-04 protects the whole customer account record at the CPNI level.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Owner and General Manager on 2026-08-31.

### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization. The equivalent internal decision: on 2026-08-31 the Owner and General Manager accepted continued operation of the OSS/BSS on these conditions:
- the edge router firmware is upgraded in the 2026-09-20 maintenance window (POAM-012);
- MFA is enabled on the voice platform admin portal and the router VPN by 2026-09-30 (POAM-003);
- the AI assistant's guest verification stays off (turned off 2026-08-14) until the P10 conditions are met;
- the High risks in P01 are treated by their dates.

### 4.3 System Operational Status
Operational. Planned changes: router and OLT firmware upgrades (by 2026-09-30), named network accounts through RADIUS or TACACS+ authentication with MFA (by 2026-12-31), an off-site configuration backup (by 2026-10-31), a customer authentication rebuild for the portal and phone support (by 2026-11-30), and security alerting (by 2026-12-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner and risk acceptor | Owner and General Manager | Overall accountability; signs the annual CPNI certification; CALEA senior officer; accepts Moderate and higher risks; approves this plan and spending |
| Security and compliance lead | Office Manager | Day-to-day security and CPNI compliance; maintains this plan, the risk register, and vendor records; BSS administrator |
| Network systems owner | Network Operations Lead | OLTs, edge router, hut servers, voice platform administration; outage reporting; CALEA technical contact |
| Network engineering support | Network engineering consultant (retainer) | Router and OLT configuration and upgrades |
| Office IT operations | MSP | Office computers, tablets, productivity suite, office firewall, cloud backup |
| Independent assessor | Contracted security consultant | Annual control assessment (P07) |

**Where roles overlap.** The Network Operations Lead both runs and checks the network, and the Office Manager both administers the BSS and reviews its logs. With 7 people this cannot be avoided. It is compensated by the General Manager's monthly review of the POA&M, the annual independent assessment (P07), and the rule that every shared or administrator login becomes a named account (POL-02 B.1).

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1 (closest matches). Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Customer account and CPNI records (accounts, call detail, voice plans, driver license numbers) | Moderate | Moderate | Low | Disclosure triggers CPNI and Florida breach duties and can expose a person's calling patterns to a stalker or fraudster; wrong data causes wrong bills; the BSS can be down a day (P05 MTD 24 h) |
| Network operations and configuration (device configurations, IP assignments, provisioning) | Moderate | Moderate | Moderate | Exposed configurations and credentials give an attacker the network; a bad change takes service down; every High process depends on it (P05 MTD 2 to 4 h) |
| Voice service and 911 routing records (registered locations, numbers) | Low | Moderate | Moderate | A wrong registered location misroutes a 911 call; voice and 911 have a 2-hour MTD (P05) |
| Billing and revenue collection | Moderate | Moderate | Low | Financial data; payments continue through the processor (P05 MTD 72 h) |
| **OSS/BSS category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 7-person carrier. The plan documents 45 controls that carry the CPNI safeguards, the network security outcomes most relevant to the P08 intrusion scenario, and basic office hygiene (see `control-implementation.csv`). All other Moderate-baseline controls are handled one of two ways:
- **Inherited** from the SaaS vendors (physical, platform, and application controls), with the BSS vendor's SOC 2 report as the main evidence (P09). The voice platform provider has not yet supplied equivalent evidence (POAM-011).
- **Tailored out** for this tier where the control addresses federal program management or organizations with dedicated IT staff (for example, configuration control boards and separate development environments). These are tailoring decisions, not gaps.

## 7. Authorization Boundary Description
- **Inside:** the company's BSS tenant and portal configuration (SYS-01), its voice platform account and numbers (SYS-02), the OLTs, ONTs, and aggregation switch (SYS-03), the edge router and hut servers (SYS-04), the monitoring service account (SYS-05), the productivity suite tenant (SYS-06), 10 endpoints (SYS-07), the office network (SYS-08), and the backup subscription (SYS-09).
- **Outside (external services, interconnected):** the vendors' own platforms and data centers; the middle-mile and transit provider; the voice platform's 911 routing network and the county 911 center; the CALEA TTP and any collection equipment it places; the AI assistant (SYS-10, assessed in P10); the answering service; the payment processor.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Agreement |
|---|---|---|---|
| Middle-mile and transit provider | Bidirectional | All subscriber internet traffic | Service contract (4-hour repair target) |
| Voice platform to county 911 center (through the provider's 911 network) | Outbound | 911 calls with registered location | Platform contract |
| Voice platform CDR export to SYS-01 | Inbound to the BSS (monthly file upload) | Rated toll and international calls (CPNI) | Platform contract; **no CPNI terms (gap)** |
| SYS-04 provisioning link to SYS-01 API | Bidirectional | Service orders, account details | BSS contract; **API key has full administrator rights (gap)** |
| SYS-10 AI assistant to SYS-01 | Bidirectional | Account and bill data for the signed-in customer | BSS contract add-on; assessed in P10 |
| Network engineering consultant | Inbound administrative access (VPN) | Router and OLT administration | Retainer letter; **shared login, no MFA (gap)** |
| MSP remote management platform | Inbound administrative access | Office device management | MSP service contract |
| CALEA TTP | Outbound, only under a lawful order | Intercepted broadband communications | TTP contract (CALEA terms) |
| Payment processor | Outbound (hosted page) | Card and bank payments (tokens only stored) | Processor agreement |
| Community bank branch | Outbound | Security questionnaire answers (no CPNI) | None needed |

## 9. System Component Inventory
| Component | Type | Location or provider | Owner |
|---|---|---|---|
| BSS tenant and portal (SYS-01) | SaaS | BSS vendor | Office Manager |
| Voice platform account (SYS-02) | SaaS | Hosted voice platform provider | Network Operations Lead |
| OLTs (2), aggregation switch, ONTs (about 1,420) (SYS-03) | Network | Hut; customer premises | Network Operations Lead |
| Edge router, hut servers (2) (SYS-04) | Network and server | Hut | Network Operations Lead |
| Monitoring service account (SYS-05) | SaaS | Monitoring vendor | Network Operations Lead |
| Productivity suite tenant (SYS-06) | SaaS | Productivity suite vendor | Office Manager (MSP operates) |
| Desktops (4), laptops (3), tablets (3) (SYS-07) | Endpoint | Office; field | Office Manager (MSP operates) |
| Office firewall and Wi-Fi (SYS-08) | Network | Office network closet | Office Manager (MSP operates) |
| Cloud backup subscription (SYS-09) | SaaS | Backup vendor (MSP resells) | Office Manager (MSP operates) |

A full inventory, including every place CPNI and customer PII are stored, is due 2026-10-31 (CM-8).

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 45 controls:
- Implemented: 10
- Partially implemented: 28
- Planned: 7
- Not applicable: 0

By responsibility: 24 system-specific (the company), 19 hybrid (the company with a vendor, the MSP, or the consultant), 2 common/inherited (fully provided by SaaS vendors).

### 10.2 Inherited, MSP-provided, and consultant-provided controls
| Provider | What the company relies on | Evidence | What the company must still do |
|---|---|---|---|
| BSS vendor | Platform security, encryption, backups (CP-9), lockout (AC-7), audit records (AU-2, AU-11), portal sign-in | SOC 2 Type 2 report reviewed 2026-08-25 (P09) | Complementary user entity controls: staff account management, role assignment, API key scoping, customer authentication settings (reset method, notices), access report review |
| Hosted voice platform provider | Softswitch security, 911 routing, CDR storage, encryption in transit (SC-8), backups (CP-9), voice intercept capability | Contract only; **no SOC report or questionnaire yet (POAM-011)** | MFA and named logins on the admin portal; export restrictions; CPNI and incident notice terms in the contract |
| Productivity suite vendor | Platform security, encryption, lockout, logging | Vendor documentation | Account management, MFA settings, sharing settings |
| MSP | Office patching (SI-2), antivirus (SI-3), firewall and Wi-Fi (SC-7, AC-18), laptop encryption (SC-28), suite backup (CP-9) | Monthly MSP reports; P07 evidence requests | Approve exceptions; review reports monthly; annual MSP review |
| Network engineering consultant | Router and OLT configuration and upgrades | Change emails only | Named VPN login with MFA; written change records; confidentiality and incident notice terms |
| Monitoring service vendor | Availability alerts and paging | Vendor documentation | Add security alerts (SI-4) |

**Inherited does not mean done.** Two of the BSS vendor's complementary user entity controls are open gaps at the company: customer authentication settings (IA-8) and the API key scope (AC-6).

### 10.3 Control assessment status
Assessed 2026-08-10 to 2026-08-12 by an independent consultant. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
- **Workforce:** staff sign in to the BSS and the productivity suite with a password and a phone authenticator app. That is appropriate for CPNI at the Moderate category. The same standard is required, and not yet met, for the voice platform portal, the router VPN, and network devices (IA-2(1)).
- **Customers:** the CPNI rules set the minimum for customer access to call detail: a password not prompted by readily available biographical or account information, set up without such information, with notices of changes to the telephone number or address of record (47 CFR 64.2010(b), (c), (e), (f)). The portal does not meet this today (IA-8; P03 G-021 to G-026). The planned design: password reset by a one-time code sent to the telephone number or email of record, a required account PIN for phone release of call detail, and change notices.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness and BSS vendor report review (P09), AI assessment (P10), CALEA SSI policies (filed 2017; under revision).

## 13. Acronym List and Glossary
- **BSS / OSS:** business support system / operations support system
- **CDR:** call detail record
- **CPNI:** customer proprietary network information (47 U.S.C. 222(h)(1))
- **DIRS / NORS:** Disaster Information Reporting System / Network Outage Reporting System
- **EMS:** element management system for the OLTs
- **MSP:** managed service provider
- **OLT / ONT:** optical line terminal (in the hut) / optical network terminal (at the customer)
- **SSI:** CALEA system security and integrity
- **TTP:** CALEA trusted third party

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan | Office Manager (security and compliance lead) |
