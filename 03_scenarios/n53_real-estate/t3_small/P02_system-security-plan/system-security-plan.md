# System Security Plan: Transaction Management and Closing Communications System (TMCC)

**Organization:** Cris Santos Company, LLC (residential real estate brokerage with property management and an in-house Closing Services division) | **Tier:** Small | **Vertical:** Real Estate and Rental and Leasing
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-21

## 1. System Name and Identifier
Transaction Management and Closing Communications System (**TMCC**), identifier CSC-SYS-001.

## 2. System Overview
The TMCC carries every step of a residential sale from signed contract to disbursed funds:
- contract management, compliance review, and document storage for about 1,150 transaction sides a year;
- communications with buyers, sellers, lenders, and title and escrow parties, including the delivery of **wire instructions**;
- settlement statements, the disbursement ledger, and about 2,800 outgoing wires a year (about $260 million) from the title escrow trust account.

Users: 60 employees (Closing Services, transaction coordination, finance and escrow accounting, sales management, IT) and about 140 contractor sales associates who use company email and the transaction platform from their own devices. Buyers and sellers use the client portals.

**Why this system.** The most likely serious loss for the company is diverted closing funds after an email account is compromised or spoofed (P01 R-001 and R-002, both High). Every component that an attacker would touch in that scheme is inside this boundary.

**Major components:**
- **SYS-01:** transaction management platform (vendor SaaS; agent and client portal)
- **SYS-02:** closing and escrow software (vendor SaaS; settlement statements, disbursement ledger, positive pay file)
- **SYS-03:** identity provider (single sign-on and MFA for employees)
- **SYS-04:** productivity suite (email, files, chat) for employees and contractor agents
- **SYS-05:** public cloud tenant hosting the **Closing Communications Portal**, the integration service, and the backup vault
- **SYS-06:** office networks at the Main Office and Branch Office, including the Main Office network storage device (scanned closing files, 2016 to 2022)
- **SYS-07:** 64 company laptops and desktops; contractor personal devices that access SYS-01 and SYS-04

The cloud tenant is described by service category and is vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| N53-R01 | FTC Standards for Safeguarding Customer Information (Safeguards Rule). Applies because the Closing Services division provides real estate settlement services (P03 section 1.1) | 16 CFR Part 314 |
| N53-R02 | FTC Act Section 5 (unfair or deceptive practices, including unreasonable data security) | 15 U.S.C. 45(a), (n) |
| State | Broker escrow duties | Fla. Stat. 475.25(1)(d)1. and (1)(k); Fla. Admin. Code ch. 61J2-14 |
| State | Title agency trust funds | Fla. Stat. 626.8473 |
| State | Florida Information Protection Act (breach notice and disposal) | Fla. Stat. 501.171 |
| Internal | Security policies POL-01 to POL-05 | P06 |

Not applicable to this system (reasoning in P03 section 1):
- CCPA/CPRA (N53-R03): no California business, and receipts are far below the threshold.
- PCI DSS (N53-R04): rent card payments run on the property management platform's hosted payment page, outside this boundary.
- SEC cybersecurity disclosure (N53-R05): the company is privately held.
- FinCEN residential real estate reporting (31 CFR 1031.320): vacated on 2026-03-19; appeal pending. If restored, reports would be prepared from SYS-02 data (P03 G-059).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the COO on 2026-09-21.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- The COO accepted continued operation of the TMCC on 2026-09-21, with the conditions in the P07 POA&M.
- The majority owner and Broker of Record approved the treatment plans for the three High risks in P01 (R-001, R-002, R-006) on 2026-09-21. **Condition:** the written disbursement verification procedure (POAM-002) must be in use by 2026-10-31, and contractor MFA (POAM-001) must be enforced by 2026-11-30. If either date slips, the majority owner decides whether Closing Services may keep accepting changed wire instructions by any channel other than the portal.
### 4.3 System Operational Status
Operational. Major modifications planned:
- contractor MFA and legacy protocol blocking (2026-11-30);
- backup redesign with a separate immutable account and SaaS backup (2026-12-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | COO | Overall accountability; accepts Moderate risks |
| Risk acceptor (authorizing official equivalent) | Majority owner and Broker of Record | Accepts High and Very High risks; governing body for the Qualified Individual's annual report |
| Qualified Individual and system security officer | IT Manager | Runs the security program (16 CFR 314.4(a)); maintains this plan |
| Data and process owner, closing funds | Closing Services Manager | Disbursement, wire release, payoff verification; title escrow trust account |
| Data and process owner, escrow records | Controller | Sales and property management escrow accounts; reconciliations |
| Data and process owner, transactions | Transaction Coordination Manager | SYS-01 workflows and contract-to-close communications |
| Contractor oversight | Sales Managers (2) | Onboard and offboard contractor agents |
| Operations support | Managed service provider (service provider under 314.4(f)) | After-hours help desk, patching, firewall management |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1 and rated for this company. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Payments and funds disbursement (wire instructions, disbursement ledger, escrow balances) | Moderate | **High** | Moderate | One altered wire instruction can send $150,000 to $450,000 of a client's funds to a criminal (P05); losses are often unrecoverable and breach trust fund duties (Fla. Stat. 626.8473(4)). Closings can slip one day (P05 MTD 8 h) |
| Customer personal and financial information (IDs, Social Security numbers, bank and loan data in closing files) | Moderate | Moderate | Moderate | Disclosure triggers FTC and Florida notice duties and identity theft risk |
| Contract and transaction records | Moderate | Moderate | Moderate | Contract deadlines run in days (P05 BP-03 MTD 24 h) |
| Workforce and contractor identities | Moderate | Moderate | Low | Credentials are the entry point for BEC; limited harm if unavailable |
| **TMCC category (high-water mark)** | **Moderate** | **High** | **Moderate** | |

**Baseline and tailoring.** The company is not bound by FIPS 200. It uses the NIST SP 800-53B **Moderate** baseline as the starting point and adds controls where the High integrity rating demands them:
- **CA-8** Penetration Testing (High baseline), which the Safeguards Rule also requires (314.4(d)(2)(i));
- money-movement controls that go beyond the baseline wording: dual approval on every escrow wire (AC-5) and independent callback verification of every payee change (written procedure, POAM-002).

The plan documents **73 controls** (see `control-implementation.csv`): the controls that implement the Safeguards Rule elements and the BEC defenses, plus core network hygiene. Every other Moderate-baseline control is treated as follows:
- **Inherited** from the SaaS and cloud providers, as evidenced by their SOC 2 reports (P09 reviews the transaction platform's report; the others are due under POAM-013).
- **Out of scope for this tier**, recorded as a tailoring decision, where the control's purpose applies only to federal systems (for example, PM-series controls beyond PM-1, PM-2, and PM-9).

## 7. Authorization Boundary Description
The boundary contains company-managed components and the company's configuration of vendor services:
- **Inside:** the SYS-01, SYS-02, SYS-03, and SYS-04 tenant configurations, users, and roles; the cloud tenant (portal, integration service, backup vault); both office networks, including firewalls, switches, staff and guest Wi-Fi, and the network storage device; 64 company endpoints; contractor personal devices when they access SYS-01 or SYS-04.
- **Outside (interconnected external services):**
  - SYS-08 commercial online banking (bank-hosted);
  - SYS-11 e-signature service;
  - the SaaS vendors' own platforms and the cloud provider's infrastructure;
  - lenders' payoff portals;
  - the title insurance underwriter's agent portal.
- **Neighbors outside the boundary:** SYS-09 CRM and SYS-10 property management platform. They share the identity provider and email but are covered by the risk register and P10, not by this plan.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| SYS-08 online banking (three escrow banks) | Outbound wire and positive pay files; inbound confirmations | Payee, account, amount | Bank treasury services agreements (security procedure: hardware tokens and dual approval on the trust account) |
| SYS-11 e-signature service | Bidirectional (API from SYS-01 and SYS-02) | Contracts, addenda, closing documents | Vendor terms of service; no negotiated security terms (**gap**, P03 G-030) |
| Integration service to SYS-01 and SYS-02 | Bidirectional (API over TLS) | Transaction status, parties, closing dates | Vendor API terms |
| Closing Communications Portal to buyers and sellers | Outbound | Closing documents, wire instructions | Portal terms of use; client notice at contract |
| Lenders | Inbound payoff statements and closing packages; outbound funding confirmations | Loan and payoff data | Lender closing instructions; payoff letters must come from the lender portal or be verified by callback (procedure due 2026-10-31) |
| Title insurance underwriter | Outbound policy data | Policy and premium data | Agency agreement |
| MSP | Remote administration | Endpoint and firewall management | MSP contract with no security terms (**gap**, P03 G-030) |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| Transaction management platform tenant (SYS-01) | SaaS | Transaction platform vendor | Transaction Coordination Manager |
| Closing and escrow software tenant (SYS-02) | SaaS | Closing software vendor | Closing Services Manager |
| Identity provider tenant (SYS-03) | SaaS | Identity vendor | IT Manager |
| Productivity suite tenant (SYS-04) | SaaS | Productivity suite provider | IT Manager |
| Closing Communications Portal | Cloud managed web application service (PaaS) and database | Cloud tenant (SYS-05) | IT Manager (contract developer maintains code) |
| Integration service | Cloud virtual machine | Cloud tenant (SYS-05) | IT Manager |
| Backup vault | Cloud backup service | Cloud tenant (SYS-05), same account as production (**gap**) | IT Manager |
| Firewalls (2), switches, Wi-Fi | Network | Main Office and Branch Office | IT Manager (MSP manages firewalls) |
| Network storage device | On-premises storage (unencrypted, **gap**) | Main Office | Closing Services Manager |
| Company laptops and desktops (64) | Endpoint | Both offices and remote | IT Manager |
| Contractor personal laptops and phones (about 140 agents) | Endpoint (unmanaged) | Agents' homes and the field | Each agent, under the agent agreement |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 73 controls:
- Implemented: 14
- Partially implemented: 41
- Planned: 18
- Not applicable: 0

Inheritance: 48 system-specific, 21 hybrid, 4 common or inherited from providers.

**The gaps that matter most** (all tracked in the P07 POA&M):
- IA-2(2): no MFA for contractor agents, who are about 70% of users.
- AU-6 and SI-4: no log review or alerting, so a mailbox takeover would go unseen.
- AC-5 and AT-3: single approver on two escrow accounts; no written verification procedure for payoffs and changed instructions.
- CP-9 and CP-4: backups share the production account and have never been restored.
- SA-8, SA-11, and CA-8: the portal that delivers wire instructions has never been tested.

### 10.2 Control assessment status
Assessed 2026-08-24 to 2026-08-28 by an independent assessor (22 controls). See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
- **Employees:** every employee authenticates through the identity provider with a password and an authenticator app (authenticator assurance level 2 in NIST SP 800-63B terms). This is acceptable for the Moderate confidentiality rating. Because the integrity rating is High and relay phishing kits can defeat app-based MFA, **Closing Services staff, the Controller, and administrators move to phishing-resistant authenticators by 2026-12-31** (P01 R-003).
- **Contractor agents:** today they use a password only, which is **not acceptable** for a system whose integrity rating is High. MFA is required by 2026-11-30 (16 CFR 314.4(c)(5)). No written approval of an equivalent control will be issued.
- **Buyers and sellers:** the Closing Communications Portal sends a one-time code by email. That code goes to the same mailbox a BEC attacker may control. The penetration test (2026-11-15) will assess the portal's sign-in, and an SMS or authenticator option is planned. The transaction platform's client portal is governed by its vendor and outside this boundary.
- **Online banking:** bank-issued hardware tokens, governed by the bank's security procedure.

## 12. Referenced Artifacts
Scenario facts (`../scenario-facts.md`), risk register (P01), gap analysis (P03), cloud control map (P04), BIA (P05), policies POL-01 to POL-05 (P06), assessment and POA&M (P07), BEC incident response runbook (P08), SOC 2 readiness and vendor report review (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **BEC:** business email compromise
- **DMARC:** Domain-based Message Authentication, Reporting, and Conformance
- **EDR:** endpoint detection and response
- **MFA:** multi-factor authentication
- **MSP:** managed service provider
- **Payoff letter:** a lender's statement of the amount needed to pay off a loan at closing, with wiring details
- **POA&M:** plan of action and milestones
- **Qualified Individual:** the person designated under 16 CFR 314.4(a) to oversee the information security program
- **TMCC:** Transaction Management and Closing Communications System
- **Title escrow trust account:** the Closing Services division's account for closing funds (Fla. Stat. 626.8473)

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-08-31 | Draft after control assessment fieldwork | IT Manager |
| 1.0 | 2026-09-21 | Approved by the COO | IT Manager |
