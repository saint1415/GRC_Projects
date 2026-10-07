# System Security Plan: Core and Digital Banking Platform (CDBP)

**Organization:** Cris Santos Company Holdings, Inc. (Banking division and Financial Software and Data Services division, with corporate shared services) | **Tier:** Multi-Sector | **Vertical:** Finance and Insurance
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-10

> **Why this system.** At this tier the SSP can cover one system per division or a shared system. The group chose the **Core and Digital Banking Platform**, a system shared by two divisions: the bank's core banking system (SYS-B1) and the multi-tenant digital banking platform (SYS-S1) that the Financial Software division runs for the bank and 310 client institutions. It is the scenario's primary system ("core banking and online banking platform"), it carries the group's top risks (P01 GR-01, GR-02, GR-04), and it shows the multi-sector problem in one boundary: the same components answer to the OCC as the bank's system and to 310 client institutions as a bank service provider's product. Other division systems keep their own plans and inherit from the same common control catalog (`common-control-catalog.csv`).

## 1. System Name and Identifier
Core and Digital Banking Platform (**CDBP**), identifier CSCH-CDBP-01. It covers SYS-B1 and SYS-S1 in `../00_company-facts.md`, joined by the payment initiation gateway to SYS-B2.

## 2. System Overview
The CDBP is how the bank's customers, and the customers of 310 client institutions, see and move their money. It supports:
- **The bank:** deposit and loan account processing, the customer information file, and general ledger posting on the core (SYS-B1) for about 6.2 million consumer and 540,000 business customers; online and mobile banking for 4.1 million consumer and 310,000 business users on the platform (SYS-S1).
- **Client institutions:** online and mobile banking and business payment initiation for 212 community banks and 98 credit unions (about 15 million end users). Each client runs its own core elsewhere; the platform reads balances and posts payment requests through each client's interfaces.
- **Business payments:** business users of the bank and of client institutions create wires and ACH files on the platform. For the bank tenant, requests pass through the payment initiation gateway to the payments hub (SYS-B2); for client tenants, requests go to each client's own payment system.

About 9,000 bank workforce users (branch, operations, treasury management) use the core; about 1,100 Financial Software staff (engineering, operations, and 460 client support staff) operate the platform; about 2,300 client administrators manage their own tenants.

**Major components:**
- **Core banking system (SYS-B1):** licensed core application and database cluster in the primary group data center, with synchronous replication to the hot secondary data center
- **Digital banking platform (SYS-S1):** container platform, API gateway, mobile and web back end, and managed databases in cloud provider A (primary region plus warm standby region); one database schema and encryption key per tenant; the bank tenant has a dedicated database cluster
- **Customer identity service:** end-user authentication with device binding, MFA, and risk scoring (part of SYS-S1)
- **Tenant administration consoles** (client administrators and the bank's treasury management team) and the **support console** (Financial Software support staff)
- **Payment initiation gateway:** message service in the primary data center that signs payment requests and passes them to SYS-B2 (cold standby in the secondary data center)
- **Key management:** cloud key management for platform tenants; hardware security modules for core data and payment message signing

Services are described by category and are vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies to the CDBP |
|---|---|---|---|
| N52-R02 | Interagency Guidelines Establishing Information Security Standards (OCC) | 12 CFR 30 App. B and Supplement A | The core and the bank tenant hold the bank's customer information. The CDBP must meet the bank's program objectives (II.B) and the III.C measures. The Financial Software division is the bank's service provider for SYS-S1 (III.D) |
| N52-R02 | Guidelines as issued by the Federal Reserve | 12 CFR 225 App. F | The Financial Software division is a nonbank subsidiary of the holding company. The holding company must make sure it is subject to a comprehensive program (App. F II.A); it is included in the group program |
| (not an N52 ID) | OCC heightened standards | 12 CFR 30 App. D | The bank is a covered bank. The platform's technology services to the bank are a front line unit activity (App. D I.E.6(a)(iii)), subject to independent risk management and internal audit |
| N52-R01 | Gramm-Leach-Bliley Act | 15 U.S.C. 6801-6809 | Customer information of the bank; client institutions' customer information is protected under each client's own duties and contracts (12 CFR 1016.3(e)(2)(v)) |
| (incident rule) | Computer-Security Incident Notification | 12 CFR 53.3, 53.4; 225.302, 225.303; 304.24 | The bank notifies the OCC of a notification incident (53.3); the holding company notifies the Federal Reserve (225.302); the division, as bank service provider, notifies each affected client bank when covered services are disrupted for 4 or more hours (53.4, 225.303, 304.24 by the client's regulator) |
| (statute) | Bank Service Company Act | 12 U.S.C. 1867(c) | Services the division performs for client banks are subject to examination by each client bank's federal banking agency; each client bank notifies its agency of the service relationship within 30 days |
| Contracts | Client master agreements; SOC 1 and SOC 2 commitments; the 2021 intercompany services agreement with the bank | P09 | 88 client contracts require notice within 24 hours of a security incident affecting the client; the intercompany agreement sets no notice time (POAM-012) |
| N52-R08 | SEC cybersecurity disclosure | Form 8-K Item 1.05; Reg S-K Item 106 | A CDBP incident can be material to the group (P08) |
| Internal | Group policies POL-01 to POL-05 and division supplements | P06 | |

Not applicable: FTC Safeguards Rule (16 CFR Part 314), because the bank is under the OCC and the division is under the Federal Reserve (15 U.S.C. 6805(a)(1)); NYDFS Part 500 (no New York-licensed entity); PCI DSS for the CDBP (card data stays at the card processor; the platform shows masked card numbers only).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Group CISO, the CDBP system owner (Head of Digital Banking Platform, Financial Software division), and the bank's digital banking executive (business owner for the bank tenant) on 2026-09-10, after the board risk committees' review.

### 4.2 System Authorization Decision
The group is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- **Decision:** authorized to operate with conditions, 2026-09-10, by the Group CISO and the Group Chief Risk Officer (acceptance authority for High risks), with the Head of Technology and Cyber Risk giving second-line concurrence.
- **Conditions:** (1) remove standing all-tenant access from the support console by 2026-12-31 (POAM-008); (2) bind workforce console sessions to managed devices and shorten them to 8 hours by 2026-11-30 (POAM-003); (3) complete bank-designated notice contacts for all 212 client banks by 2026-10-31 (POAM-005); (4) test the payment initiation gateway failover by 2027-03-31 (POAM-011).
- **Reauthorization:** annually, or after a major change to the tenant model or the payment path.

### 4.3 System Operational Status
Operational. **Planned changes:** support console redesign with tenant-scoped, ticket-linked access (POAM-008); a hot standby for the payment initiation gateway (P01 BR-004).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Head of Digital Banking Platform (Financial Software division) | Accountable for the CDBP and this SSP |
| Business owner, bank tenant and core | Bank digital banking executive; bank chief operations officer (core) | Approve bank access, limits, and changes affecting bank customers |
| Authorizing official equivalent | Group CISO with the Group Chief Risk Officer | Authorization decision; High risk acceptance |
| Second-line challenge | Head of Technology and Cyber Risk | Independent review of the authorization and risk acceptances |
| Client assurance | Client risk and assurance director (Financial Software) | SOC reports, client due diligence, bank service provider notices |
| Common control providers | Group identity director (SYS-G1), Group SOC director (SYS-G2), Group cloud platform director and Group CIO (SYS-G3, SYS-G4), Group Property Management director (data center buildings) | Operate inherited controls (`common-control-catalog.csv`) |
| Independent assessor | Group internal audit | Assesses common controls once and samples CDBP and division controls (P07) |

## 6. System Information Types and System Categorization
Information types are organization-defined, informed by NIST SP 800-60. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Customer account and personal financial information (bank and client tenants) | **High** | Moderate | Moderate | Aggregation: about 19 million end users across 311 tenants. A disclosure would trigger notices in every state, 311 institutions' customer notices, and SEC materiality |
| Payment instructions (wire and ACH) | Moderate | **High** | **High** | A changed beneficiary or amount causes direct, often unrecoverable loss. Wires have a 4-hour MTD (P05 BP-B01) |
| Core ledger and posting data | High | **High** | **High** | System of record for the bank; RPO of 15 minutes (P05 BP-B03) |
| Authentication data (credentials, device bindings, session tokens) | High | High | High | Compromise allows account takeover and payment fraud |
| Security and audit information | High | High | Moderate | Needed to establish facts for every notice clock |
| **CDBP category (high-water mark)** | **High** | **High** | **High** | Overall **High** |

**Baseline:** the NIST SP 800-53B **High** baseline, tailored. The plan documents **128 controls** in `control-implementation.csv`:
- 123 from the High baseline;
- 2 from the privacy baseline (PM-9, PM-10);
- 3 program management controls not in any baseline (PM-1, PM-2, PM-30), added because the plan relies on group governance and third-party strategy.

Other High-baseline controls are either fully inherited from the cloud providers or the data center buildings (for example, most PE controls) or tailored out with a reason in the group tailoring register (for example, PE controls for facilities the platform does not use).

## 7. Authorization Boundary Description
- **Inside:** SYS-B1 core application and database cluster (both data centers); SYS-S1 accounts in provider A (primary and warm standby regions), including the customer identity service and all consoles; the payment initiation gateway; platform backups in the provider B vault.
- **Outside, inherited (common control providers):** SYS-G1 identity, SYS-G2 SOC, SIEM, EDR and email gateway, SYS-G3 data center and landing-zone infrastructure, SYS-G4 email and collaboration, and the data center buildings run by Group Property Management.
- **Outside, interconnected:** SYS-B2 payments hub (and through it the Federal Reserve payment services), the card processor (masked card data and card controls), credit bureaus (for SYS-B3, not the CDBP itself), and the 310 client institutions' cores and payment systems.

The diagram is in P04 `cloud-architecture.md` (the CDBP subgraph).

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| SYS-B2 payments hub | Outbound (signed payment requests); inbound (status) | Bank-tenant wires and ACH | Internal interconnection record; mutual TLS on private links |
| Client institutions' cores (310) | Both | Balances, transactions, payment requests for each client's tenant | Client master agreements; client security schedules |
| Card processor | Both | Masked card data; card lock and limit changes | Bank processor contract (bank service provider) |
| SYS-B3 loan origination | Outbound | Account relationship data for pre-filled applications | Internal interconnection record |
| Enterprise data platform | Outbound nightly | Bank-tenant analytics extracts only; no client-tenant data | Data sharing approval by the Group Chief Privacy Officer |
| Bank to Financial Software (intercompany) | Service | The whole platform service for the bank tenant | 2021 intercompany services agreement (**no incident notice time or audit rights**, POAM-012) |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| Core application and database cluster | Licensed software on group servers | Primary and secondary group data centers | Bank chief operations officer (business); Group CIO (infrastructure) |
| Platform container clusters and API gateway | PaaS | Provider A (2 regions) | Head of Digital Banking Platform |
| Tenant databases | Managed database (PaaS), schema and key per tenant | Provider A | Head of Digital Banking Platform |
| Customer identity service | Platform component on PaaS | Provider A | Head of Digital Banking Platform |
| Tenant and support consoles | Web applications on the platform | Provider A | Head of Digital Banking Platform |
| Payment initiation gateway | Message service on group servers | Primary data center (cold standby in secondary) | Head of Commercial Payments Operations (business); Group CIO (infrastructure) |
| Hardware security modules | Appliances | Both data centers | Group cloud platform director |
| Backups | Immutable vault | Provider B and secondary data center | Group cloud platform director |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv` (128 controls) and `common-control-catalog.csv` (100 group common controls).

| Status | Controls |
|---|---|
| Implemented | 110 |
| Partially implemented | 18 |
| Planned | 0 |
| Not applicable | 0 |
| **Total** | **128** |

| Inheritance | Controls |
|---|---|
| Common/Inherited (from SYS-G1 to SYS-G4, group functions, the data center buildings, or the cloud providers) | 86 |
| Hybrid (group provides the mechanism; the CDBP configures or operates part) | 14 |
| System-specific | 28 |

**The 18 partially implemented controls** cluster in five places:
- **Workforce sessions and identity hygiene** (the root of the P08 scenario): AC-2, AC-2(12), AC-12, IA-5, IA-11, SI-4.
- **Tenant and support console access:** AC-6, AU-6, IA-8 (scenario gap 6), AT-3. (AC-3 itself is implemented: tenant isolation holds; the problem is how broad the support role is.)
- **Resilience of the payment path:** CP-2, CP-4.
- **Cross-division incident handling and bank service provider notices** (gaps 3 and 5): IR-3, IR-4, IR-6, IR-8.
- **Oversight of the affiliate service provider** (gap 3): SA-4, SA-9.

### 10.2 Common control inheritance by division
The common control catalog lists 100 controls provided by corporate. Inheritance is **documented for the bank** (2025 inheritance matrix), for the **Financial Software division** (its SOC 1 and SOC 2 system descriptions carve in group services), and for the CDBP (this plan). It is **not documented for Commercial Real Estate** (scenario gap 2). Until POAM-018 closes, Commercial Real Estate cannot show which of its safeguards are met by group controls, and P07 found CA-2 determination statements other than satisfied for this reason.

### 10.3 What client institutions must do (complementary user entity controls)
The division's SOC reports list the controls each client must operate: approve and remove its own administrators; set business user entitlements and limits; **require MFA for business payment users** (41 client tenants have not); review the tenant audit reports; and give the division a bank-designated point of contact for incident notices. The platform can enforce only some of these; POAM-009 changes the default so that business payment MFA can no longer be switched off.

### 10.4 Control assessment status
Common controls were assessed once, and CDBP and division controls sampled, from 2026-07-01 to 2026-08-31 by group internal audit. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
- **Workforce users** authenticate through SYS-G1 federated sign-in with number-matching MFA; **administrators** use phishing-resistant hardware keys and just-in-time PAM elevation. Console sessions are not yet bound to managed devices (POAM-003).
- **End users** (consumers and business users) authenticate to the customer identity service with a password, device binding, and risk-based MFA; business payment users must use MFA in the bank tenant and in 269 of 310 client tenants.
- **Client administrators** must use MFA in every tenant.
- **Service accounts** should use workload identity with short-lived credentials; 21 still use static keys older than 1 year (POAM-002).

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), group and division risk registers (P01), gap analyses and regulation-by-division matrix (P03), cloud architecture and control map (P04), BIA (P05), group policies and division supplements (P06), assessment and POA&M (P07), incident response runbook and notification matrix (P08), SOC 2 readiness (P09), AI governance (P10).

## 13. Acronym List and Glossary
- **CDBP:** Core and Digital Banking Platform
- **Bank service provider:** a person that performs services subject to the Bank Service Company Act for a banking organization (12 CFR 53.2(b)(2))
- **Common control:** a control provided once by corporate and inherited by several systems
- **CUEC:** complementary user entity control (a control a client must operate for the service organization's controls to work)
- **Notification incident:** a computer-security incident that has materially disrupted or degraded, or is reasonably likely to, the bank's operations or a material business line (12 CFR 53.2(b)(7))
- **PAM:** privileged access management
- **Tenant:** one institution's isolated part of the multi-tenant platform

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-08-31 | Draft combining the former core and platform plans, after P07 fieldwork | CDBP system owner |
| 1.0 | 2026-09-10 | Approved with authorization conditions | Group CISO |
