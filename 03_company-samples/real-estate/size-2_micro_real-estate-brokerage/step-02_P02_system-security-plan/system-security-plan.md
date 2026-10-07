# System Security Plan: Transaction Management and Closing Communications System (TMCC)

**Organization:** Cris Santos Company, LLC (residential real estate brokerage with property management) | **Tier:** Micro | **Vertical:** Real Estate and Rental and Leasing
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-14

## 1. System Name and Identifier
Transaction Management and Closing Communications System (**TMCC**), identifier CSC-SYS-001.

## 2. System Overview
The TMCC carries a residential sale from signed contract to closing day:
- contract management, disclosures, deadlines, and document storage for about 190 transaction sides a year;
- communication with buyers, sellers, title companies, closing attorneys, and lenders, including **deposit instructions and wire fraud warnings**;
- handling of earnest money held in the brokerage's sales escrow account and its transfer to the title company before closing.

Users: 7 employees and about 22 contractor sales associates who use company email and the transaction platform from their own devices. Buyers and sellers use the transaction platform's client document sharing.

**Why this system.** The most likely serious loss is diverted closing funds after a mailbox is taken over or spoofed (P01 R-001 and R-002, both High). Every component an attacker would use in that scheme is in this boundary or connects to it.

The brokerage owns almost no infrastructure. Most of the TMCC is vendor SaaS, and a managed service provider (MSP) runs the office equipment and the email backup. For each control this plan says what the brokerage does itself, what the MSP does for it, and what it inherits from a SaaS vendor.

**Major components:**
- **SYS-01:** transaction management platform (vendor SaaS; client document sharing)
- **SYS-02:** productivity suite: 29 mailboxes and shared files, including the sales escrow ledger spreadsheet
- **SYS-03:** e-signature service (vendor SaaS)
- **SYS-07:** 7 laptops and 2 desktops (MSP-managed); contractor agents' personal devices reach SYS-01 and SYS-02
- **SYS-08:** office network: firewall, staff Wi-Fi, separate guest Wi-Fi, multifunction printer and scanner (MSP-managed)
- **SYS-09:** SaaS-to-SaaS backup of employee mailboxes and shared files (cloud workload, MSP-operated)

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| N53-R02 | FTC Act Section 5 (unfair or deceptive practices, including unreasonable data security and the brokerage's own security statements) | 15 U.S.C. 45(a), (n) |
| N53-R01 | FTC Safeguards Rule. **Does not apply** (the brokerage is not a financial institution; P03 section 1). Used as the benchmark for the security program, so control rows cite it as "N53-R01 benchmark" | 16 CFR Part 314 |
| State | Florida Information Protection Act: reasonable measures, breach notice, third-party agents, disposal | Fla. Stat. 501.171(2)-(6), (8) |
| State | Broker escrow duties and escrow disputes | Fla. Stat. 475.25(1)(d)1. and (1)(k); Fla. Admin. Code ch. 61J2-14; r. 61J2-10.032 |
| State | Broker records retention (5 years) | Fla. Stat. 475.5015 |
| Federal | FCRA disposal rule (screening reports reach this system only by email) | 16 CFR 682.3 |
| Internal | Security policies POL-02, POL-03, POL-04 | P06 |

Not applicable (reasoning in P03 section 1): CCPA/CPRA (N53-R03), PCI DSS (N53-R04; rent card payments run on the property management platform's hosted page, outside this boundary), SEC disclosure (N53-R05), FinCEN residential real estate rule (vacated; brokers are not reporting persons).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Broker-owner on 2026-09-14.

### 4.2 System Authorization Decision
The brokerage is not a federal agency, so there is no formal authorization. The equivalent internal decision: on 2026-09-14 the Broker-owner accepted continued operation of the TMCC on the condition that the POA&M items in P07 are completed by their dates and the three High risks in P01 (R-001, R-002, R-006) are treated by 2026-12-31.

### 4.3 System Operational Status
Operational. Planned changes by 2026-12-31: MFA for every account and legacy protocols blocked (R-001, R-005), separate named administrator accounts (R-006), mailbox alerts (R-025), backup of agent mailboxes and a first restore test (R-008), and desktop encryption (R-011).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner and risk acceptor | Broker-owner | Overall accountability; accepts Moderate risk; approves High-risk treatment plans, this plan, policies, and spending; approves every escrow payment |
| Security and compliance lead | Office Manager | Day-to-day security (benchmark Qualified Individual, 314.4(a)); maintains this plan, the risk register, and the vendor list; manages accounts; incident lead |
| Escrow records | Bookkeeper | Escrow ledgers and monthly reconciliations; initiates ACH batches |
| Transaction workflow | Transaction Coordinators (2) | Deposit instructions, deposit verification, file compliance in SYS-01 |
| Users | Contractor sales associates (about 22) | Follow POL-02 Part C; report suspicious email within 1 hour |
| IT operations | MSP | Devices, patching, antivirus, firewall, Wi-Fi, backup administration |
| Independent assessor | Security consultant | Control assessment (P07) |

**Overlap and how it is compensated.** The Office Manager both runs most controls and keeps this plan, and also initiates escrow wires. Two checks offset this: online banking requires the Broker-owner to approve every escrow payment (AC-5), and an outside consultant who operates no control assessed the controls in August 2026 (P07).

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Client transaction records (contracts, ID images, proof of funds, pre-approval letters) | Moderate | Moderate | Moderate | Disclosure enables identity theft and triggers Florida breach notice; altered documents can derail a closing; P05 MTD 24 h for BP-03 |
| Payment instructions and escrow records | Moderate | **Moderate** | Moderate | Altered instructions divert client funds; the loss falls mostly on one client, which keeps integrity at Moderate rather than High for the system as a whole; P05 MTD 24 h for BP-01 |
| Agent and employee records | Moderate | Low | Low | License, agreement, and payroll data |
| **TMCC category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 7-person brokerage. The plan documents 44 controls that carry the benchmark Safeguards Rule elements, the Florida duties, and basic hygiene (see `control-implementation.csv`). Other Moderate-baseline controls are:
- **inherited** from the SaaS vendors (physical, platform, and application controls), with the transaction platform vendor's SOC 2 report as the main evidence (P09); or
- **tailored out** for this tier where they address federal program management or organizations with their own IT staff (for example, configuration control boards and separate development environments). These are tailoring decisions, not gaps.

## 7. Authorization Boundary Description
- **Inside:** the brokerage's configuration, accounts, and data in SYS-01, SYS-02, and SYS-03; the 9 company devices (SYS-07); the office network (SYS-08); and the backup subscription (SYS-09).
- **Inside but not company-owned:** contractor agents' personal devices while they reach SYS-01 and SYS-02. The brokerage cannot manage them today; it sets rules for them (POL-02 C.3) and protects the accounts (MFA).
- **Outside (interconnected):** online banking (SYS-04, bank-hosted), the property management platform (SYS-05, covered in P04 and P10), the accounting SaaS (SYS-06), the MLS and lockbox apps (association-provided), the vendors' own platforms and data centers, the MSP's remote management platform, and the generative AI tools (SYS-10, P10).

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Agreement |
|---|---|---|---|
| Escrow bank (SYS-04) | Outbound payment orders; inbound statements | Wire and ACH details; balances | Treasury services agreement; dual control set at the bank |
| Title companies and closing attorneys | Bidirectional (email; SYS-01 sharing) | Contracts, deposit verification, closing figures | None. **Wire instructions from them arrive by email today (gap; IA-8)** |
| Buyers and sellers | Bidirectional | Contracts, IDs, proof of funds, deposit instructions | Brokerage agreements; wire fraud warning in the contract packet |
| Property management platform (SYS-05) | Bidirectional (users and email) | Owner and tenant records; screening reports forwarded by email | Platform terms of service (no security addendum) |
| MSP remote management platform | Inbound administrative access | Device management | MSP service contract (no security or incident notice terms; R-013) |
| Generative AI tools (SYS-10) | Outbound text | Listing text; sometimes client details (gap; P10) | Consumer terms only |

## 9. System Component Inventory
| Component | Type | Location or provider | Owner |
|---|---|---|---|
| Transaction platform tenant (SYS-01) | SaaS | Transaction platform vendor | Office Manager |
| Productivity suite tenant: 29 mailboxes and shared files (SYS-02) | SaaS | Productivity suite vendor | Office Manager |
| E-signature account (SYS-03) | SaaS | E-signature vendor | Office Manager |
| 7 laptops, 2 desktops (SYS-07) | Endpoint | Office; laptops travel with staff | Office Manager (MSP operates) |
| Contractor agents' personal laptops and phones | Endpoint (not managed) | Agents' homes and vehicles | Each agent, under POL-02 C.3 |
| Firewall, staff and guest Wi-Fi, printer and scanner (SYS-08) | Network | Office network closet | Office Manager (MSP operates) |
| SaaS-to-SaaS backup subscription (SYS-09) | Cloud workload | Backup vendor (MSP-operated) | Office Manager (MSP operates) |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 44 controls:
- Implemented: 8
- Partially implemented: 27
- Planned: 9
- Not applicable: 0

By responsibility: 19 system-specific (the brokerage), 19 hybrid (the brokerage with a vendor, the bank, or the MSP), 6 common/inherited (provided by a SaaS vendor or the MSP).

### 10.2 Inherited and MSP-provided controls
| Provider | What the brokerage relies on | Evidence | What the brokerage must still do |
|---|---|---|---|
| Transaction platform vendor | Platform security, encryption, backups, lockout (AC-7), activity records (AU-2) | SOC 2 Type 2 report reviewed 2026-08-19 (P09) | Complementary user entity controls: user provisioning and removal, MFA enforcement, file visibility settings, activity review |
| Productivity suite vendor | Platform security, encryption in transit and at rest, spam filtering (SI-8), lockout (AC-7), audit logging (AU-2) | Vendor documentation | Account management, MFA for every account, blocking legacy protocols and external forwarding, DMARC, log review |
| Escrow bank | Dual control and approval limits (AC-5) | Entitlement report | Keep the approver list current; call the fraud desk on any doubt |
| MSP | Patching (SI-2), antivirus (SI-3), firewall and Wi-Fi (SC-7, AC-18), laptop encryption (SC-28), backup operation (CP-9) | Monthly MSP report; P07 evidence requests | Oversight: approve exceptions, read the monthly report, annual MSP security review, contract terms (R-013) |
| Backup vendor (through the MSP) | Storage of mailbox and file copies (CP-9) | None yet; first restore test due 2026-09-30 | Extend scope to agent mailboxes; test restores |

**Inherited does not mean done.** Two of the transaction platform vendor's complementary user entity controls are open gaps at the brokerage: account removal for departing agents (AC-2, PS-4) and MFA for agents (IA-2(2)).

### 10.3 Control assessment status
Assessed 2026-08-17 to 2026-08-19 by an independent consultant. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
Employees sign in to SYS-01 and SYS-02 with a password and an authenticator app. That is appropriate for client financial and identity data at the Moderate category. Contractor agents use a password alone, which is **not** acceptable for accounts that send deposit and closing communications; MFA for every account is due 2026-10-31 (POAM-003). Buyers and sellers reach shared documents through the transaction platform's client sign-in, which the vendor governs.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness and vendor report review (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **ACH:** automated clearing house (bank transfer)
- **BEC:** business email compromise
- **DMARC:** an email domain policy that tells receivers what to do with mail that fails sender checks
- **MFA:** multi-factor authentication
- **MSP:** managed service provider
- **POA&M:** plan of action and milestones
- **TMCC:** Transaction Management and Closing Communications System

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-09-14 | Initial plan | Office Manager (security and compliance lead) |
