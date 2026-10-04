# System Security Plan: Field SCADA and Production Accounting System (FSPA)

**Organization:** Cris Santos Company, LLC (independent crude oil producer, one field) | **Tier:** Micro | **Vertical:** Mining, Quarrying, and Oil and Gas Extraction
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Field SCADA and Production Accounting System (**FSPA**), identifier CSC-SYS-001.

## 2. System Overview
The FSPA lets 7 people watch and control one Florida Panhandle oil field and turn what it produces into sales and royalty payments. It covers 22 wells (16 producing), one tank battery, and one SWD facility, plus the office tools used to account for production and pay about 140 royalty owners.

The company owns very little IT. The SCADA host and field equipment are its own; almost everything else is SaaS, a managed service provider (MSP) runs office IT, and a SCADA integrator supports the SCADA host remotely. This plan says, for each control, what the company does itself, what the MSP or a vendor does for it, and what it inherits.

**Major components:**
- **SYS-01:** SCADA host at the field office: polling master, HMI, alarm engine, local historian
- **SYS-02:** 16 pump-off controllers, 1 tank battery PLC, 1 SWD facility PLC, a licensed 900 MHz radio network, 3 cellular modems
- **SYS-03:** the company's tenant in the production accounting SaaS
- **SYS-04:** productivity suite (email, shared drive), MSP-administered
- **SYS-05:** 7 computers and 5 company smartphones
- **SYS-06:** main-office network (MSP-managed) and field office network (router and Wi-Fi)
- **SYS-07:** MSP-operated cloud backup
- **SYS-08:** the SCADA vendor's cloud alarm call-out and mobile viewer, including the predictive maintenance add-on in pilot (P10)
- **SYS-09:** the SCADA integrator's remote access path

**What the system does not do:** it does not perform safety functions. H2S detection, tank high-level shutdown, and SWD pump high-pressure shutdown are hardwired at each site and work without SCADA. This design choice limits how much harm a SCADA compromise can cause and is the basis for the Moderate integrity rating in section 6.

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | Status for the FSPA |
|---|---|---|---|
| N21-BM | NIST CSF 2.0 with NIST SP 800-82 Rev. 3, including the SP 800-82 Rev. 3 OT overlay (Appendix F) | NIST CSWP 29; SP 800-82 Rev. 3 | Voluntary benchmark adopted by the company (P03) |
| State | Florida Information Protection Act | Fla. Stat. 501.171(2), (4), (6) | Applies to royalty owner and employee personal information in production accounting, email, and laptops |
| Federal | Oil discharge notice | 40 CFR 110.6; 33 CFR 153.203 | Applies if a SCADA failure or attack leads to an oil discharge that reaches water; drives the P08 notification matrix |
| Contract | Seismic data license; cyber insurance policy | License and policy terms | Access limited to named users (license); MFA on remote access and offline backups (insurance application) |
| Internal | Security policies POL-02, POL-03, POL-04 | P06 | Approved 2026-08-31 |

**Not applicable** (see P03 section 1):
- N21-R01, the USCG Marine Transportation System cyber rule (33 CFR 101.605): no vessel, waterfront facility, or OCS facility.
- N21-R02, TSA Security Directive Pipeline-2021-02G: not a TSA-notified pipeline owner or operator.
- N21-R03, CIRCIA: proposed only; as proposed, the company is far below the SBA size standard and meets no sector criterion.
- PHMSA pipeline safety (49 CFR Parts 192 and 195): the company operates only production facilities and flow lines, and no gas gathering line.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Owner on 2026-08-31, with the Field Superintendent's agreement for the field controls.

### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization. The equivalent internal decision: on 2026-08-31 the Owner accepted continued operation of the FSPA on these conditions:
- the four High risks in P01 are treated by their due dates (the remote desktop exposure, R-025, was closed on 2026-08-11);
- the POA&M items in P07 are completed by their dates;
- the SCADA connector to the vendor cloud stays send-only (no write-back) unless a new P10 assessment approves a change.

### 4.3 System Operational Status
Operational. Planned changes, all due by 2026-12-31:
- vendor remote access through an MFA-protected, owner-enabled session tool (P01 R-002), due 2026-10-31
- a small firewall separating the SCADA host and radio base from the field office PCs and Wi-Fi (R-001), due 2026-11-30
- an offline, rotated SCADA backup and a copy of controller programs (R-003)
- a replacement SCADA host on a supported operating system (R-006)

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner and risk acceptor | Owner | Overall accountability; accepts Moderate risk; approves this plan, the policies, and spending |
| Security Coordinator | Office Manager | Day-to-day security program; directs the MSP; keeps this plan, the risk register, and vendor records |
| OT lead | Field Superintendent | Business owner of SCADA and field operations; approves OT changes and vendor sessions |
| SCADA operations | Field Technician | Operates and maintains the SCADA host, controllers, and radios |
| Data owner (production and royalty data) | Production Accountant | Production accounting configuration, owner data, run ticket entry |
| IT operations | MSP | Office computers, phones, suite, main-office firewall, cloud backup |
| OT support | SCADA integrator | SCADA host configuration and remote support |
| Independent assessor | Consultant with OT experience | Annual control assessment (P07) |

**Overlap and compensation.** At 7 people, the Office Manager both runs and reviews the IT controls, and the Field Technician both operates and changes SCADA. The Owner reviews progress monthly, the Field Superintendent approves OT changes, and an independent assessor tests the controls each year.

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1, which gives provisional impact levels for federal systems. The company adjusted them for its own operations, as the publication allows. Impact levels follow FIPS 199.

| Information type (SP 800-60 Vol. 2 Rev. 1) | Provisional (C, I, A) | Company rating (C, I, A) | Rationale |
|---|---|---|---|
| Energy Production (D.7.4): process data, setpoints, controller logic | Low, Low, Low | Low, **Moderate**, **Moderate** | A changed SWD pressure setpoint or pump-off logic could damage equipment, cause a spill, or break an injection permit limit; hardwired shutdowns keep the worst case below High. Loss of SCADA forces manual operations and, for water disposal, shut-ins after 12 hours (P05) |
| Energy Supply (D.7.1): run tickets, sales volumes | Low, Moderate, Moderate | Low, Moderate, Low | Wrong volumes misstate sales and royalties; paper run tickets and 3 weeks of tank storage limit the availability impact (P05 MTD 120 h) |
| Payments (C.3.2.5): royalty and partner distributions | Low, Moderate, Low | **Moderate**, Moderate, Low | Owner records include Social Security and bank account numbers covered by Fla. Stat. 501.171 |
| **FSPA category (high-water mark)** | | **Moderate, Moderate, Moderate** | |

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 7-person company with the SP 800-82 Rev. 3 OT overlay (Appendix F). The overlay was applied where OT limits a control, for example the HMI screen lock (AC-11), the shared HMI login (IA-2), and unencrypted radio polling (SC-8). The plan documents **43 controls** that address the P01 risks and the benchmark gaps (see `control-implementation.csv`). All other Moderate-baseline controls are handled one of two ways:
- **Inherited** from the SaaS providers (physical, platform, and application controls), with the production accounting vendor's SOC 2 report as the main evidence (P09).
- **Tailored out** for this tier, where the control addresses federal program management or organizations with dedicated IT staff (for example, configuration control boards and separate development environments). These are tailoring decisions, not gaps.

## 7. Authorization Boundary Description
The boundary contains what the company controls or pays someone to control for it:
- **Inside:** the SCADA host and field office network, all field controllers, radios, and modems, the 7 computers and 5 phones, the main-office network, the company's tenants and settings in production accounting, the productivity suite, the cloud backup, and the SCADA vendor's cloud service, and the integrator's remote access path.
- **Outside (external services, interconnected):** the SaaS vendors' own platforms and data centers, the cellular carrier's network, the bank portal (SYS-10), the crude purchaser's systems, the payroll service, the MSP's remote management platform, and the integrator's own network and laptops.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Agreement |
|---|---|---|---|
| SCADA vendor cloud service (SYS-08) | Outbound from the SCADA host connector; write-back disabled 2026-08-26 | Alarms, well status, pump-off controller data | Subscription terms; **no security or data-use terms (gap)** |
| SCADA integrator (SYS-09) | Inbound remote access | Full SCADA host administration | Service agreement; **no security terms, shared account, no MFA (gap)** |
| Production accounting SaaS (SYS-03) | Outbound (manual entry and file upload) | Run tickets, volumes, owner records | SaaS agreement; SOC 2 Type 2 reviewed (P09) |
| Bank portal (SYS-10) | Outbound | Royalty and payables ACH files | Bank agreement; dual approval |
| Non-operating partners | Bidirectional (email) | Joint interest bills, well data, seismic interpretations | Joint operating agreements; seismic license limits who may see licensed data |
| Crude purchaser | Inbound | Run ticket copies, sales statements | Crude purchase contract |
| MSP remote management platform | Inbound administrative access | Office device management | MSP service contract |
| Cellular carrier | Transport | Polling of 3 well sites on the carrier's private network | Carrier contract |

## 9. System Component Inventory
| Component | Type | Location or provider | Owner |
|---|---|---|---|
| SCADA host (SYS-01) and its USB backup drive | Workstation (unsupported OS, **gap**) | Field office | Field Superintendent (Field Technician operates) |
| Pump-off controllers (16), tank battery PLC, SWD PLC (SYS-02) | Field controllers | Well sites, tank battery, SWD facility | Field Superintendent |
| 900 MHz base radio and 15 remote radios; 3 cellular modems (SYS-02) | Communications | Field office tower; well sites | Field Superintendent |
| Field office router and Wi-Fi (SYS-06) | Network | Field office (flat network, **gap**) | Field Superintendent |
| Main-office firewall and Wi-Fi (SYS-06) | Network | Main office | Office Manager (MSP operates) |
| Laptops (5), desktops (2) (SYS-05) | Endpoints | Both offices | Office Manager (MSP operates all except the engineering laptop) |
| Smartphones (5) (SYS-05) | Mobile endpoints | Owner, Field Superintendent, Lease Operators, Field Technician | Office Manager (MSP operates) |
| Production accounting tenant (SYS-03) | SaaS | Production accounting vendor | Production Accountant |
| Suite tenant and shared drive (SYS-04) | SaaS | Productivity suite vendor | Office Manager (MSP administers) |
| Cloud backup subscription (SYS-07) | SaaS | Backup vendor through the MSP | Office Manager (MSP operates) |
| SCADA cloud service account (SYS-08) | SaaS | SCADA vendor | Field Superintendent |
| Integrator remote access tool (SYS-09) | Third-party software | Installed on the SCADA host (**gap**) | Field Superintendent |

The field controllers, radios, and modems are not yet listed by model and firmware (gap 1; POAM-010).

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 43 controls:
- Implemented: 6
- Partially implemented: 28
- Planned: 9
- Not applicable: 0

By responsibility: 26 system-specific (the company), 16 hybrid (the company with a vendor or the MSP), 1 common/inherited (fully provided by SaaS vendors).

### 10.2 Inherited and MSP-provided controls
| Provider | What the company relies on | Evidence | What the company must still do |
|---|---|---|---|
| Production accounting vendor | Platform security, encryption, backups, MFA enforcement, audit records | SOC 2 Type 2 report reviewed 2026-08-20 (P09) | Complementary user entity controls: user removal, role assignment, review of owner bank detail changes |
| Productivity suite vendor | Platform security, encryption at rest and in transit, MFA enforcement, audit logging | Vendor documentation | Account management, sharing settings (Geology folder), log review |
| SCADA vendor (SYS-08) | Alarm delivery, mobile viewer, connector software | Security whitepaper only | Account removal, MFA settings, keep the connector send-only, contract terms |
| MSP | Office patching (SI-2), antivirus (SI-3), firewall (SC-7), laptop encryption (SC-28), phone management (AC-19), cloud backup (CP-9) | Monthly MSP report; P07 evidence requests | Oversight: review the monthly report, approve exceptions, extend scope to the SCADA host |
| SCADA integrator | SCADA host configuration and rebuild knowledge | None | Named accounts, MFA, session approval, a written rebuild procedure |

**Inherited does not mean done.** Two of the production accounting vendor's complementary user entity controls are open gaps at the company: account removal (AC-2, PS-4) and verification of owner bank detail changes (P01 R-004).

### 10.3 Control assessment status
Assessed 2026-08-10 to 2026-08-12 by an independent consultant. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
- **SaaS users** (suite, production accounting, bank portal) sign in with a password and a phone authenticator app. This is appropriate for the Moderate categorization.
- **SCADA users** sign in to the HMI with local SCADA accounts. Today all field staff share one operator login. The target, consistent with the SP 800-82 Rev. 3 overlay discussion of IA-2: named accounts for the Field Technician and the integrator; for Lease Operators, either named accounts or a documented compensating control (locked field office, a sign-in sheet at the HMI, and a monthly review of the operator log); and for all remote access, individual identification with MFA before any shared account is used.
- **Mobile viewer users** have individual accounts; MFA, which the vendor supports, will be turned on by 2026-09-30.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness and vendor report review (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **FSPA:** Field SCADA and Production Accounting System
- **H2S:** hydrogen sulfide
- **HMI:** human-machine interface
- **MFA:** multi-factor authentication
- **MSP:** managed service provider
- **OT:** operational technology
- **PLC:** programmable logic controller
- **POA&M:** plan of action and milestones
- **SCADA:** supervisory control and data acquisition
- **SWD:** saltwater disposal

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan | Office Manager (Security Coordinator) with the Field Superintendent |
