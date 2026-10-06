# System Security Plan: Family Office Shared Services Platform (FOSSP)

**Organization:** Cris Santos Company, LLC (family holding company and single-family office) | **Tier:** Micro | **Vertical:** Management of Companies and Enterprises
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-18

## 1. System Name and Identifier
Family Office Shared Services Platform (**FOSSP**), identifier CSC-SYS-001.

## 2. System Overview
The FOSSP is the set of services the office uses to do its three jobs: oversee the three operating subsidiaries, manage the family's investments, and run the family's administration (payments, payroll, accounting, records). It serves 7 staff, 9 subsidiary guest users, and 11 family members (through the document vault), and it reaches about $310 million (fictional) of family assets at two custodians through bank and custodian portals.

The office owns almost no infrastructure. Most of the FOSSP is vendor SaaS, the banks and custodians host their own portals, and a managed service provider (MSP) runs the laptops, the network, and the one cloud workload. This plan therefore says, for each control, what the office does itself, what the MSP does for it, and what it inherits from a vendor.

This is the registry's "shared corporate services platform (ERP and identity)" at Micro size: the accounting system (SYS-01) plays the ERP role, and the productivity suite (SYS-02) is the identity provider for everything else.

**Major components:**
- **SYS-01:** multi-entity cloud accounting and consolidation system (SaaS)
- **SYS-02:** productivity suite with identity: email, files (Family, Subsidiaries, and Office sites), chat, single sign-on, MFA (SaaS)
- **SYS-03:** bill pay platform (SaaS)
- **SYS-04:** payroll and HR service for office and household employees (SaaS)
- **SYS-05:** bank and custodian portals (hosted by the banks and custodians)
- **SYS-06:** investment reporting and aggregation platform with read-only custodian data feeds (SaaS)
- **SYS-07:** family document vault and client portal (SaaS)
- **SYS-08:** 8 laptops, 1 conference-room PC, 1 multifunction printer (MSP-managed); staff personal phones for email and MFA
- **SYS-09:** office network: firewall, staff Wi-Fi, separate guest Wi-Fi (MSP-managed)
- **SYS-10:** generative AI assistant add-on in SYS-02 (4-user pilot; P10)
- **SYS-11:** legacy partnership accounting server, one virtual machine in a public cloud provider's IaaS (MSP-administered)

## 3. Laws, Regulations, and Policies Affecting the System
| Requirement | Citation | How it applies |
|---|---|---|
| FTC Safeguards Rule | 16 CFR Part 314 | The office is treated as a financial institution (investment advisory services to family members for a fee). With fewer than 5,000 consumers, 314.4(b)(1), (d)(2), (h), and (i) do not apply (314.6). All other elements apply. See P03 |
| Florida Information Protection Act | Fla. Stat. 501.171 | Reasonable security measures (501.171(2)), disposal (501.171(8)), and breach notice (P08) |
| Advisers Act family office exclusion | 17 CFR 275.202(a)(11)(G)-1 | Not a security rule, but it limits who the office may serve; the FOSSP must not be used to advise non-family persons (P03 rows G-001 to G-003) |
| NIST CSF 2.0 Organizational Profile | NIST CSWP 29 | Voluntary benchmark (P03) |
| Internal | POL-02, POL-03, POL-04 | P06 |

Not applicable (P03 section 1): SEC Regulation S-K Item 106 (N55-R01), Form 8-K Item 1.05 (N55-R02), and SOX section 404 (N55-R03), because the office is not a registrant or issuer; Federal Reserve Regulation Y Subpart N (N55-R04) and 12 CFR Part 225 Appendix F (N55-R05), because it owns no bank; HIPAA plan sponsor duties (N55-R06), because the insured plan gets 164.530(k) relief; CIRCIA (N55-R07), still proposed.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Principal on 2026-09-18.

### 4.2 System Authorization Decision
The office is not a federal agency, so there is no formal authorization. The equivalent internal decision: on 2026-09-18 the Principal accepted continued operation of the FOSSP, and the Board of Managers approved treatment plans for the four High risks in P01 (R-001, R-002, R-003, R-005), on the condition that the P07 POA&M items are completed by their dates.

### 4.3 System Operational Status
Operational. Planned changes by 2026-12-31: phishing-resistant MFA (R-001), an independent SYS-02 backup (R-006), closing SYS-11's remote desktop port and upgrading its operating system (R-007), MSP-managed endpoint detection with after-hours alerting (SI-4), and named MSP administrator accounts (R-005). The AI assistant pilot (SYS-10) is paused until the P10 conditions are met.

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| Authorizing official and risk acceptor | Principal (with the Board of Managers for High risks) | Approves this plan, policies, and spending |
| System owner, security lead, and Qualified Individual | Family Office Director | Day-to-day security; maintains this plan, the risk register, and the vendor list; accepts Moderate risks |
| Administrator of SYS-02 and onboarding | Office Manager | Accounts, guests, sharing settings; coordinates the MSP |
| Payments and accounting | Controller | SYS-01, payment approvals, SYS-11 business owner |
| Investment systems | Investment Director; Investment Analyst | SYS-06 and custodian access |
| Bill pay and payroll | Senior Accountant | SYS-03, SYS-04 |
| Family records | Executive Assistant to the Principal | SYS-07 uploads and family user support |
| IT operations | MSP | Laptops, network, patching, antivirus, SYS-11 administration |
| Independent assessor | Outside security consultant | Annual control assessment (P07) |

**Where roles overlap.** The Family Office Director designs, runs, and reports on the program, and owns most risks. Two things compensate: an independent consultant assesses the controls each year (P07), and the Board of Managers receives a written annual report from the Family Office Director even though 314.4(i) does not apply at this size.

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Financial management: payments | Moderate | **High** | Moderate | A changed payee account or a forged approval moves money irreversibly (one wire can exceed $50,000); P05 MTD 24 h |
| Personal identity and authentication (family members' SSNs, passports, tax returns) | **High** | Moderate | Low | Exposure enables identity theft and extortion and can reveal family members' homes and travel; personal safety impact (P05) |
| Financial management: asset and liability management (investment positions, private deal documents) | Moderate | Moderate | Moderate | Custodians hold the official record; P05 MTD 48 h |
| Human resources management (office and household payroll) | Moderate | Moderate | Moderate | SSNs and bank accounts of 12 employees; biweekly payroll |
| **FOSSP category (high-water mark)** | **High** | **High** | **Moderate** | |

**Baseline.** The high-water mark is High for confidentiality and integrity. For a 7-person office, the plan starts from the NIST SP 800-53B **Moderate** baseline and adds the High-impact protections that matter most for these two information types: phishing-resistant MFA, separation of duties on payments, and a second-person check on payee changes. That is a documented tailoring decision, not a gap. The plan documents 44 controls (see `control-implementation.csv`). Other Moderate-baseline controls are either **inherited** from the SaaS vendors, banks, and custodians (physical, platform, and application controls) or **tailored out** for this tier because they address federal program management or organizations with in-house development and IT staff.

## 7. Authorization Boundary Description
- **Inside:** the office's tenant configuration, users, and data in SYS-01 to SYS-04, SYS-06, SYS-07, and SYS-10; the office's users, tokens, and entitlements in SYS-05; the devices in SYS-08; the network in SYS-09; and the SYS-11 virtual machine, its snapshots, and its cloud firewall rules.
- **Outside (external services, interconnected):** the vendors' platforms and data centers; the banks' and custodians' systems; each subsidiary's own accounting, point-of-sale, and IT systems and their IT providers; the outside CPA firm and counsel; the MSP's remote management platform.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Agreement |
|---|---|---|---|
| Custodians (SYS-06 data feeds) | Inbound | Positions and transactions | Custodian data feed authorizations signed by each family client |
| Banks and custodians (SYS-05) | Bidirectional | Payment and trade instructions | Account agreements; delegated-access forms |
| Subsidiaries (guest accounts in the Subsidiaries site; bank approver roles) | Bidirectional | Monthly financial packages, board packs, payment approvals | Management agreements (no security terms yet; R-018) |
| Outside CPA firm (SYS-07 share links) | Outbound | Tax documents with SSNs | Engagement letter (no security terms yet; R-011) |
| Outside counsel (SYS-07 share links) | Bidirectional | Estate and trust documents | Engagement letter |
| MSP remote management platform | Inbound administrative access | Device management | MSP service contract (no security terms; R-010) |
| AI assistant (SYS-10) | Internal to the SYS-02 tenant | Whatever the user can open | Productivity suite terms; pilot paused (P10) |

## 9. System Component Inventory
| Component | Type | Location or provider | Owner |
|---|---|---|---|
| Accounting tenant (SYS-01) | SaaS | Accounting system vendor | Controller |
| Productivity and identity tenant (SYS-02, SYS-10) | SaaS | Productivity suite vendor | Office Manager |
| Bill pay account (SYS-03) | SaaS | Bill pay vendor | Senior Accountant |
| Payroll account (SYS-04) | SaaS | Payroll service | Senior Accountant |
| Bank and custodian entitlements and tokens (SYS-05) | Hosted portals | Two banks, two custodians | Controller |
| Investment platform tenant (SYS-06) | SaaS | Investment platform vendor | Investment Director |
| Document vault (SYS-07) | SaaS | Vault vendor | Family Office Director |
| 8 laptops, conference PC, printer (SYS-08) | Endpoints | Office; laptops travel with staff | Office Manager (MSP operates) |
| Firewall and Wi-Fi (SYS-09) | Network | Office network closet | Office Manager (MSP operates) |
| Partnership accounting virtual machine and snapshots (SYS-11) | IaaS workload | Public cloud provider, one account | Controller (MSP operates) |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 44 controls:
- Implemented: 10
- Partially implemented: 20
- Planned: 14
- Not applicable: 0

By responsibility: 22 system-specific (the office), 19 hybrid (the office with a vendor, bank, or the MSP), 3 common/inherited (fully provided by vendors).

### 10.2 Inherited and MSP-provided controls
| Provider | What the office relies on | Evidence | What the office must still do |
|---|---|---|---|
| Productivity suite vendor | Platform security, sign-in and MFA service, encryption (SC-8, SC-28), lockout (AC-7), audit records (AU-2) | Vendor documentation | Accounts and guests, MFA strength, sharing settings, log review, backup |
| Banks and custodians | Dual approval (AC-5), hardware tokens, payment records, fraud monitoring | Account agreements; entitlement reports | Decide who approves; verify payees by callback; remove leavers' tokens |
| Accounting system and investment platform vendors | Platform security and backups (CP-9) | SOC 2 Type 2 reports (investment platform reviewed in P09) | Complementary user entity controls: user access, MFA, access review |
| Bill pay, payroll, and vault vendors | Platform security and backups | Vendor documentation | Roles (the bill pay approval gap, AC-5), family user MFA |
| MSP | Patching (SI-2), antivirus (SI-3), firewall (SC-7), screen lock (AC-11), laptop encryption (SC-28), SYS-11 administration | Monthly MSP report; P07 evidence | Direct the work, receive evidence, approve exceptions, annual review (R-010) |
| Cloud provider (SYS-11) | Physical and hypervisor security, default disk encryption | Provider shared responsibility documentation | Everything inside the virtual machine, its firewall rules, and its snapshots (P04) |

**Inherited does not mean done.** The vendors' reports assume the customer manages its own users and MFA. Those are the office's weakest areas today (AC-2, AC-6, IA-2(1)).

### 10.3 Control assessment status
Assessed 2026-08-31 to 2026-09-02 by an independent consultant. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
Staff and subsidiary guests sign in to SYS-02 with a password and authenticator app push, and SYS-02 provides single sign-on to SYS-01, SYS-03, SYS-04, and SYS-06. Push approval can be relayed by an adversary-in-the-middle phishing page, which is the office's top risk (R-001). Because the confidentiality and integrity impact is High, the office will require **phishing-resistant authenticators** (hardware security keys) for all staff by 2026-12-31 and for administrators first. Bank and custodian portals use bank-issued hardware tokens. Family members use the vault's own sign-in; SMS codes are being replaced by an authenticator app (R-009).

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness and vendor report review (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **FOSSP:** Family Office Shared Services Platform
- **IaaS:** infrastructure as a service
- **MFA:** multi-factor authentication
- **MSP:** managed service provider
- **POA&M:** plan of action and milestones
- **Qualified Individual:** the person who oversees the information security program under 16 CFR 314.4(a)
- **SaaS:** software as a service

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-09-18 | Initial plan | Family Office Director |
