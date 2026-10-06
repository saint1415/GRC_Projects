# System Security Plan: Merchant Payments Platform (MPP)

**Organization:** Cris Santos Company, LLC (merchant services provider, an ISO) | **Tier:** Micro | **Vertical:** Financial Services
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Merchant Payments Platform (**MPP**), identifier CSC-SYS-001. The MPP is the set of SaaS services, devices, and settings the company uses to board, equip, and support its merchants. It includes the company's PCI DSS scope: the gateway administration and keyed-entry path.

## 2. System Overview
The MPP supports every function in the BIA (P05): the merchant help desk, backup keyed entry, gateway administration, onboarding, terminal swaps, chargeback support, merchant risk monitoring, and finance. It serves 7 employees, 6 outside sales agents, and about 850 merchants.

**The company does not run a payment processing platform.** The processor partner authorizes, clears, and settles every transaction on its own platform. The company's part of the payment environment is narrower but still sensitive:
- it **administers** about 420 merchants' gateway accounts, including the content of about 120 hosted payment pages;
- it **transmits** card data when support staff key a sale for a merchant (about 1,900 a year);
- it **holds** merchant owner information (Social Security numbers, bank accounts) for about 1,250 merchant files.

The company owns almost no infrastructure. This plan says, for each control, what the company does itself, what the MSP does for it, and what it inherits from a SaaS vendor or the processor partner.

**Major components:**
- **SYS-01:** gateway reseller console (processor partner SaaS)
- **SYS-02:** processor partner portal (SaaS)
- **SYS-03:** CRM and merchant document store (SaaS)
- **SYS-04:** productivity suite: email, files, chat (SaaS)
- **SYS-05:** cloud phone system with call recording (SaaS)
- **SYS-06:** 9 laptops (MSP-managed)
- **SYS-07:** office network: firewall, staff Wi-Fi, guest Wi-Fi, one internet line (MSP-managed)
- **SYS-08:** website and application intake (cloud web hosting and object storage)
- **SYS-09:** about 40 spare payment terminals
- **SYS-10:** suite backup (SaaS, operated by the MSP)

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| Primary (contract) | PCI DSS v4.0.1, as a service provider; Visa service provider Level 2 (annual SAQ D for Service Providers, quarterly ASV scan, AOC) | PCI SSC, June 2024; required by the ISO agreement and card brand rules |
| Federal | FTC Standards for Safeguarding Customer Information, with the small-institution exception (fewer than 5,000 consumers) | 16 CFR Part 314; 314.6 |
| Card brand | Visa Third Party Agent registration (as an ISO, through the sponsor bank); Visa What To Do If Compromised v10.0 (effective 2026-06-25) | Visa rules and supplements |
| State | Breach notification in each state where affected individuals reside; Florida as the worked example. Florida call recording consent | Fla. Stat. 501.171; Fla. Stat. 934.03(2)(d) |
| Contract | ISO agreement: annual validation, 24-hour compromise notice, indemnity | ISO agreement (renewed 2025-01-01) |
| Internal | Security policies POL-02, POL-03, POL-04 | P06 |

Not applicable (see P03 section 1):
- 12 CFR 53.4 bank service provider notice (C-FINANCIAL-R01): no covered services performed for the sponsor bank.
- Interagency Guidelines (C-FINANCIAL-R02): bind the sponsor bank; reach the company only through the ISO agreement.
- NCUA 12 CFR 748.1(c) (C-FINANCIAL-R03), SEC Regulation SCI (C-FINANCIAL-R04), NYDFS Part 500 (C-FINANCIAL-R05): not a credit union, SCI entity, or New York licensee.
- CIRCIA (C-FINANCIAL-R06): proposed only; tracked.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Owner on 2026-08-31.

### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization. The equivalent internal decisions:
- On 2026-08-31 the Owner accepted continued operation of the MPP, on the condition that the four High risks in P01 are treated by their due dates and the P07 POA&M is tracked monthly.
- External validation is the annual SAQ D for Service Providers and AOC, signed by the Owner and sent to the processor partner. The 2026 SAQ is due 2026-10-30 and will use the scope in section 7 of this plan, not the narrower 2025 scope.

### 4.3 System Operational Status
Operational. Planned changes:
- MFA required for every console account (R-001, R-002), by 2026-09-15
- Keyed-entry service stopped and replaced by merchant self-service in the gateway app (R-003), by 2026-10-15
- Secure application upload in the CRM replacing email and the website bucket (R-004, R-005), by 2026-10-31

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner and risk acceptor | Owner | Accountability; accepts Moderate risk; approves this plan and High-risk treatment plans; signs the SAQ and AOC; executive responsibility for PCI DSS (12.4.1) |
| Qualified Individual and security lead | Operations Manager | Day-to-day security and PCI DSS work (16 CFR 314.4(a)); maintains this plan, the risk register, and the service provider list |
| Payment page and filter changes | Terminal and Integration Technician | Hosted payment page content, integrations, terminal inventory |
| Fraud filter business owner | Onboarding and Risk Specialist | Fraud filter thresholds (P10) |
| IT operations | MSP | Laptops, patching, antivirus, firewall, Wi-Fi, suite administration, backup |
| Independent assessor | Security consultant | Control assessment (P07) |

**Where roles overlap.** The Operations Manager runs most controls and also prepares the SAQ that reports on them. The Owner signs the SAQ but does not operate controls. The compensating checks are the P07 assessment by an independent consultant, the ASV scans, and the planned penetration test.

## 6. System Information Types and System Categorization
Information types were matched to NIST SP 800-60 Vol. 2 Rev. 1 where a close type exists; card account data and merchant owner identity data are company-defined types. Impact levels follow FIPS 199 and were set by the company for its own context.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Card account data (keyed entry; masked reports) | Moderate | Moderate | Low | Small volumes (about 1,900 keyed sales a year), but disclosure triggers card brand and state duties. Keyed entry is a convenience (P05 MTD 24 h) |
| Gateway settings for merchants (hosted payment page content, users, filters) | Moderate | Moderate | Low | A malicious change could skim cards from about 120 merchants' customers, so integrity matters; merchants can wait a day for setting changes |
| Merchant owner information (SSNs, bank accounts, IDs) | Moderate | Moderate | Low | About 1,250 files; identity theft and deposit fraud risk; onboarding can wait days (P05 MTD 72 h) |
| Help desk and business operations | Low | Low | Moderate | Merchants need an answer within one business day (P05 BP-01 MTD 8 h) |
| **MPP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 7-person ISO. The plan documents 43 controls that carry the PCI DSS requirements in scope, the Safeguards Rule elements that apply, and basic cyber hygiene (see `control-implementation.csv`). Two are added by tailoring: CA-8 (penetration testing, a High-baseline control needed for PCI DSS 11.4) and PM-2. All other Moderate-baseline controls are handled one of two ways:
- **Inherited** from the processor partner and the SaaS vendors (platform, physical, and application controls), evidenced by the processor partner's PCI DSS AOC and the CRM vendor's SOC 2 report (P09).
- **Tailored out** for this tier, where the control addresses federal program management or organizations with dedicated IT staff (for example, configuration change boards and separate development environments). These are tailoring decisions, not gaps.

## 7. Authorization Boundary Description
The boundary contains what the company controls or pays someone to control on its behalf:
- **Inside:** the company's console accounts and the gateway settings it manages for merchants (SYS-01), its portal accounts (SYS-02), the CRM tenant (SYS-03), the suite tenant (SYS-04), the phone system account and its recordings (SYS-05), the 9 laptops (SYS-06), the office network (SYS-07), the website hosting account and storage bucket (SYS-08), the spare terminals (SYS-09), and the backup subscription (SYS-10).
- **Outside (external services, interconnected):** the processor partner's gateway, authorization, and settlement platform; the sponsor bank and card networks; the vendors' own platforms and data centers; the MSP's remote management platform; the outside agents' own devices (they reach only the CRM and the console sales view).

**PCI DSS scope inside the boundary.** The cardholder data environment is the keyed-entry path: the console's virtual terminal sessions (SYS-01), the phone system (SYS-05), the two support laptops (SYS-06), and, because there is no segmentation, the whole office network (SYS-07). The other laptops and the gateway console's administration functions are connected-to or security-impacting systems. The CRM, the website, and the suite are out of PCI DSS scope as long as no card data enters them. Stopping the keyed-entry service (R-003) would remove the support laptops, the phone system, and the office network from the cardholder data environment; the console administration would remain in scope because it can affect the security of merchants' card data.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Agreement |
|---|---|---|---|
| Processor partner gateway (SYS-01) | Bidirectional | Keyed sales, refunds, merchant user and page settings, masked reports | ISO agreement; gateway reseller terms |
| Processor partner portal (SYS-02) | Bidirectional | Applications, change requests, residuals, chargebacks | ISO agreement |
| Merchants | Bidirectional | Card details by phone (keyed entry), applications, support | Merchant processing agreement (processor partner and sponsor bank); company service terms |
| Outside sales agents | Inbound | Merchant applications (email today; **gap**) | Agent agreements (no security terms; **gap**) |
| CRM vendor, phone vendor, suite vendor, web hosting provider | Bidirectional | Merchant files, recordings, email, uploads | Vendor terms (no AOC from the phone vendor; **gap**) |
| MSP remote management platform | Inbound administrative access | Laptop management | MSP contract (no security terms; **gap**) |
| ASV | Inbound | External scans of the office IP | ASV service terms |

## 9. System Component Inventory
| Component | Type | Location or provider | Owner |
|---|---|---|---|
| Gateway console accounts and merchant settings (SYS-01) | SaaS | Processor partner | Operations Manager |
| Processor partner portal accounts (SYS-02) | SaaS | Processor partner | Operations Manager |
| CRM tenant (SYS-03) | SaaS | CRM vendor | Onboarding and Risk Specialist |
| Suite tenant (SYS-04) | SaaS | Suite vendor | Operations Manager (MSP administers) |
| Phone system account (SYS-05) | SaaS | Phone vendor | Merchant Support Lead |
| Laptops, 9 (SYS-06) | Endpoint | Office and homes | Operations Manager (MSP operates) |
| Firewall, staff Wi-Fi, guest Wi-Fi (SYS-07) | Network | Office | Operations Manager (MSP operates) |
| Web server and storage bucket (SYS-08) | Cloud workload | Web hosting and storage provider | Sales and Agent Manager (web developer administers) |
| Spare terminals, about 40 (SYS-09) | POI devices | Office, locked cabinet | Terminal and Integration Technician |
| Suite backup (SYS-10) | SaaS | Backup service (MSP) | Operations Manager (MSP operates) |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 43 controls:
- Implemented: 5
- Partially implemented: 31
- Planned: 7
- Not applicable: 0

By responsibility: 23 system-specific (the company), 18 hybrid (the company with a vendor or the MSP), 2 common or inherited (fully provided by vendors).

### 10.2 Inherited and MSP-provided controls
| Provider | What the company relies on | Evidence | What the company must still do |
|---|---|---|---|
| Processor partner (gateway and portal) | Platform security; role enforcement (AC-3); lockout (AC-7); console audit logs (AU-2, AU-11); TLS (SC-8); its own hosted payment page protections | PCI DSS AOC (Level 1 service provider), dated 2026-03 | Console user management, MFA enrollment, settings changes, log review, the content it adds to payment pages |
| CRM vendor | Encryption at rest (SC-28), backups (CP-9), lockout (AC-7) | SOC 2 Type 2 report reviewed 2026-08-21 (P09) | User management, sharing settings, MFA, retention |
| Suite vendor | Platform security, encryption, lockout, audit logging | Vendor documentation | Account settings, mail flow rules, log retention |
| Phone vendor | Recording storage and encryption; call encryption | Vendor documentation; deletion letter 2026-08-17. **No AOC** | Named admin accounts, recording settings, retention |
| MSP | Patching (SI-2), antivirus (SI-3), encryption (SC-28), firewall and Wi-Fi (SC-7, AC-18), backup operation (CP-9), screen lock (AC-11) | Monthly MSP reports; P07 evidence requests | Oversight: monthly report review, approval of exceptions, contract security terms |
| Web hosting and storage provider | Physical and platform security for SYS-08 | Provider documentation | Everything above the platform, including the bucket, keys, and plugins |

**Inherited does not mean done.** The processor partner's AOC protects the company only if the company runs its side: console MFA (IA-2(1)), account removal (AC-2, PS-4), and control over what it puts on hosted payment pages (SI-7, CM-3). All three are open gaps.

### 10.3 Control assessment status
Assessed 2026-08-03 to 2026-08-05 by an independent consultant. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
- **Employees** sign in to the suite, CRM, and processor partner portal with a password and a phone authenticator app. Number matching for push approvals is being enabled (R-004).
- **Gateway console users** today sign in with a password only, except the Owner and the Operations Manager. That does not meet PCI DSS 8.4.2 (MFA for all access into the cardholder data environment) or 16 CFR 314.4(c)(5). MFA will be required for every console account by 2026-09-15.
- **Outside agents** use named CRM accounts with MFA and a view-only console role.
- **Merchant users** of the gateway are the processor partner's users. The processor partner enforces their sign-in rules; the company only requests their creation.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness and CRM vendor report review (P09), AI assessment (P10), 2025 SAQ D and AOC, ASV scan reports.

## 13. Acronym List and Glossary
- **AOC:** Attestation of Compliance
- **ASV:** Approved Scanning Vendor
- **CRM:** customer relationship management system
- **ISO:** independent sales organization
- **MFA:** multi-factor authentication
- **MPP:** Merchant Payments Platform
- **MSP:** managed service provider
- **NPI:** nonpublic personal information
- **PAN:** primary account number (card number)
- **POA&M:** plan of action and milestones
- **POI:** point of interaction (payment terminal)
- **SAQ:** Self-Assessment Questionnaire

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan; PCI DSS scope redrawn to include the keyed-entry path | Operations Manager |
