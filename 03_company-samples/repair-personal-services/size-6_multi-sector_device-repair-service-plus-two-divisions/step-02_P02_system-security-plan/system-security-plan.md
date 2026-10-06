# System Security Plan: Service Ticketing and Point-of-Sale Platform (STPP)

**Organization:** Cris Santos Company Holdings, Inc. (Device Repair division, Cris Santos Repair, LLC; used also by the Electronics Retail and IT Support Services divisions) | **Tier:** Multi-Sector | **Vertical:** Other Services (except Public Administration)
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-10

> **Why this system.** At this tier the SSP can cover one system per division or a shared corporate system. The group chose the **STPP**, the focus division's system of record, because it holds the customer and device data behind the group's top risks (P01 GR-01, GR-05), it is used by all three divisions (Device Repair stores and depots, the 260 in-store repair counters inside retail stores, and IT Support in-home technicians), and it inherits most of its infrastructure controls from corporate (SYS-G1 to SYS-G4). The retail cardholder data environment is covered by the retail PCI DSS program and ROC, and IT Support's platform by its SOC 2 system description. Both draw on the same common control catalog (`common-control-catalog.csv`).

## 1. System Name and Identifier
Service Ticketing and Point-of-Sale Platform (**STPP**), identifier CSCH-SYS-D1. It covers SYS-D1 and the repair bench environment of SYS-D2 that connects customer devices to it (`../00_company-facts.md` section 3).

## 2. System Overview
The STPP runs every step of a repair: intake and consent at the counter, passcode capture, diagnostics and repair at the bench, parts, manufacturer warranty and TPA claims, payment, and release of the device to its owner.

| Measure | Value |
|---|---|
| Sites | 1,120 repair stores, 260 in-store repair counters (inside retail stores), 5 regional depots (2 with data recovery labs) |
| Workforce users | About 16,800 Device Repair users, about 1,400 IT Support in-home technicians, and about 520 retail store managers and supervisors with read-only ticket lookup |
| Volume | About 9.4 million repair tickets a year (about 30,000 a day); 38% are protection plan claims for the TPA, 11% manufacturer warranty, 6% enterprise accounts |
| Data | About 16.8 million customer records (customers since 2018): names, phone numbers, email and postal addresses, device make, model, serial number or IMEI, repair history, signed consents, and device passcodes (in the passcode vault at 680 stores; in free-text notes elsewhere) |

**Major components:**
- **STPP application:** containers and a managed relational database in group cloud provider A, with a warm standby in provider B
- **Store clients:** counter tablets and office PCs (browser), receipt and label printers
- **Payment integration:** semi-integrated with the processor's **validated P2PE** terminals (about 2,600 at repair stores and depots). The STPP sends the amount and receives an approval, a token, and a truncated card number. It never receives card data. In-store counter tickets are paid at retail POS lanes, which look up the ticket by barcode
- **Online booking page:** appointment booking with an optional deposit through the processor's hosted payment fields
- **Interfaces:** TPA claims, Manufacturer A and B service portals, the AI-assisted diagnostics service (AI-002), SYS-G4 customer accounts and status pages, SMS and email notifications
- **Repair bench environment (SYS-D2 part in scope):** about 6,900 bench workstations with about 40 third-party diagnostic, flashing, and data transfer tools, and the data recovery lab imaging workstations and storage

**What the system protects beyond its own data.** Customer devices under repair connect to bench workstations. The data on them (photos, messages, health and location data, saved credentials) is not stored in the STPP by design, but it passes through the bench environment. This plan therefore treats bench workstations, labs, and device handling as part of the system.

All cloud services are described by category and are vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies to the STPP |
|---|---|---|---|
| N81-R01 | FTC Act Section 5 | 15 U.S.C. 45(a)(1), 45(n) | Deception covers the intake privacy notice and AI marketing claims; unfairness covers unreasonable handling of customer devices and data |
| N81-R02 | State breach, data security, and disposal laws (Florida worked example) | Fla. Stat. 501.171(2)-(6), (8) | Reasonable security for personal information, including account email and password pairs held in notes (501.171(1)(g)1.b.); breach notices; disposal of customer records |
| N81-R03 | PCI DSS v4.0.1 (contractual) | Repair merchant agreement; Level 1 annual ROC | The STPP is connected to the P2PE environment and hosts the booking page that embeds the processor's payment fields (P03) |
| N81-R04 | FTC Disposal Rule | 16 CFR 682.3 | Background check reports for technicians only (SYS-G5); listed here because PS-3 depends on them |
| N81-BM | NIST CSF 2.0 (voluntary benchmark); NIST SP 800-88 Rev. 2 for sanitization | NIST CSWP 29; SP 800-88r2 (September 2025) | The division's benchmark (P03) |
| N52-R08 | SEC cybersecurity disclosure | Reg S-K Item 106; Form 8-K Item 1.05 | A material STPP incident would be disclosed by the group (P08) |
| Contracts | Manufacturer A and B program agreements; TPA repair network agreement; enterprise depot contracts | Fictional terms | Named MFA accounts on manufacturer portals, 24-hour incident notice, data use limited to the repair, annual program audit |
| Internal | Group policies POL-01 to POL-05 and the Device Repair supplement | P06 | |

Not applicable to the STPP: HIPAA (Device Repair is not a covered entity or business associate; the data recovery service is not offered to health care accounts), the FTC Safeguards Rule (the division extends no credit), and COPPA (not directed to children). Reasons are in P03 section 1.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Device Repair CISO and the STPP product owner (system owner) on 2026-09-10, after the board risk committee review.

### 4.2 System Authorization Decision
The group is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- **Decision:** authorized to operate with conditions, 2026-09-10, by the Group CISO and the Group Chief Risk Officer (acceptance authority for High risks).
- **Conditions:** (1) passcode vault at all stores and purge of passcodes and account passwords from notes by 2027-01-31 (POAM-002); (2) named bench accounts at all 260 in-store counters by 2026-12-31 (POAM-001); (3) bench network separated from retail POS lanes at the 112 failing stores before the retail QSA fieldwork closes, 2026-11-15 (POAM-009); (4) no new bench tool added until the tool review gate is live (POAM-008).
- **Reauthorization:** annually, or when the passcode and bench programs complete.

### 4.3 System Operational Status
Operational. **Major modifications planned:** passcode vault rollout and notes purge, named bench accounts with session logging, the bench image redesign with tool allow-listing, and in-store counter network separation.

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | STPP product owner (Device Repair engineering director) | Accountable for the STPP and this SSP |
| Authorizing official equivalent | Group CISO with the Group Chief Risk Officer | Authorization decision; High risk acceptance |
| Division security lead | Device Repair CISO | Security of the STPP and bench estate; repair merchant PCI DSS program |
| Process owner (devices and benches) | Device Repair chief operating officer | Technician access standard, bench handling, sanitization, depots |
| Data custodian (recovered data) | Device Repair data recovery director | Lab storage, retention, and deletion |
| Privacy oversight | Group Chief Privacy Officer | Purposes for passcodes and credentials; retention; data sharing with partners |
| Common control providers | Group identity director (SYS-G1), Group SOC director (SYS-G2), Group cloud platform director (SYS-G3), Group chief digital officer (SYS-G4) | Operate inherited controls (`common-control-catalog.csv`) |
| Independent assessor | Group internal audit | Assesses common controls once and samples division controls (P07) |

## 6. System Information Types and System Categorization
Information types were chosen as the closest matches in NIST SP 800-60 Vol. 2 Rev. 1 (customer services, collections and receivables, and personal identity and authentication), adapted to a private business. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Customer records and repair tickets (contact details, device identifiers, consents, passcodes until purged) | Moderate | Moderate | Moderate | Disclosure of passcodes and account credentials enables account takeover and is a breach under state law; wrong records mean devices released to the wrong person; intake and release stop the business within 8 hours (P05 BP-DR01) |
| Customer device content in custody (photos, messages, health and location data, saved credentials) | Moderate | Moderate | Low | Serious harm to individuals if exposed; the STPP is not the system of record for it; bench work can pause (P05 BP-DR03 RTO 8 hours) |
| Payment and invoicing (approvals, tokens, truncated card numbers, enterprise account billing) | Moderate | Moderate | Moderate | Card data stays in P2PE terminals and the processor's payment fields; payment and release share BP-DR02 |
| Partner claims and warranty data (TPA, Manufacturers A and B) | Moderate | Moderate | Moderate | Contract duties and 38% of volume (BP-DR04) |
| Security information (keys, credentials, logs) | Moderate | Moderate | Moderate | Compromise would expose the passcode vault and interfaces |
| **STPP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | Overall **Moderate** |

**Aggregation was considered.** 16.8 million customer records in one system could justify High confidentiality if passcodes and account passwords stayed in readable notes. The group's answer is to remove them (the passcode vault and notes purge, POAM-002) rather than to treat the whole platform as High. Until that work closes, P01 carries the exposure as a High risk (DR-001, GR-05), and this plan adds the privacy controls PT-2 and PT-3 and field-level encryption for the vault (SC-28(1)).

**Baseline:** the NIST SP 800-53B **Moderate** baseline, tailored. The plan documents **130 controls** in `control-implementation.csv`:
- 125 from the Moderate baseline;
- 3 from the privacy baseline (PM-9, PT-2, PT-3), added because the purpose and retention of passcodes and credentials is the platform's main privacy risk;
- 2 program management controls not in any baseline (PM-1, PM-2).

Other Moderate-baseline controls are either fully inherited from the cloud providers, the colocation provider, and the processor (for example, most PE controls for data centers and the P2PE terminal controls, evidenced by their assurance reports and the P2PE listing) or tailored out with a reason in the group tailoring register (for example, controls for federal-only functions).

**CSF 2.0 mapping.** The `csf2_subcategories` column comes from NIST's CSF 2.0 informative references to SP 800-53 Rev. 5.2.0 (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`). For 20 controls NIST lists no reference (for example AC-8, MP-6, PS-6, PT-2); for those the column is an author mapping.

## 7. Authorization Boundary Description
- **Inside:** the STPP accounts in provider A (application, database, booking page, interfaces, passcode vault keys) and the standby and backup vault in provider B; counter tablets and office PCs at repair stores and depots; about 6,900 bench workstations (repair stores, in-store counters, depots) and their gold images; the data recovery lab imaging workstations and storage.
- **Outside, inherited (common control providers):** SYS-G1 identity platform, SYS-G2 SOC, SIEM, and EDR, SYS-G3 landing zone and network, and SYS-G4 customer accounts.
- **Outside, interconnected:** the processor's P2PE solution and terminals; retail POS lanes (ticket lookup for in-store counter payments); the TPA claims platform; Manufacturer A and B portals; the AI-assisted diagnostics service; the courier and the certified electronics recycler.
- **Customer devices** are outside the boundary but connect to bench workstations inside it. The rules for handling them are part of this plan (AC-6, AC-20, MP-6, MP-7).
- **In-store counter networks** are retail store infrastructure (SYS-D4) outside the boundary. The bench workstations on them are inside it. That split is why SC-7 and AC-20 are only partially implemented.

The diagram is in P04 `cloud-architecture.md` (section 2.2).

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Processor P2PE solution | Terminal to processor (encrypted in the device); approval to the STPP | Card data stays in the solution; the STPP gets approval, token, and truncated number | Repair merchant agreement; P2PE Instruction Manual |
| Retail POS lanes (SYS-D3) | Lane reads ticket by barcode; STPP receives payment confirmation | Ticket number, amount, payment status | Intercompany service agreement (2023) |
| TPA claims platform | Bidirectional | Plan holder name, contact, device, claim and repair details | TPA repair network agreement |
| Manufacturer A and B portals | Bidirectional | Device serials, repair details, customer name for warranty claims | Program agreements |
| AI-assisted diagnostics service (AI-002) | Outbound diagnostic logs, photos, and ticket notes; inbound suggestions | **Notes can contain passcodes (gap; POAM-018)** | Vendor terms without data-use limits (**gap**) |
| SYS-G4 customer accounts, chatbot, and status pages | Bidirectional | Ticket status, first name, store | Group service |
| Enterprise depot customers | Outbound | Repair reports, recovered data, invoices | Enterprise contracts (72-hour incident notice) |
| Courier; certified electronics recycler | Physical | Mail-in devices; recycling lots | Service contracts (lot-level certificates only for recycling, **gap**) |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| STPP application (containers) and API gateway | PaaS | Provider A | STPP product owner |
| STPP database with point-in-time recovery | Managed relational database (PaaS) | Provider A | STPP product owner |
| Passcode vault key and field encryption | Key management (PaaS) | Provider A | Group cloud platform director |
| Booking page with hosted payment fields | Web front end (PaaS) | Provider A | STPP product owner |
| Warm standby and immutable backup vault | PaaS and backup service | Provider B | Group cloud platform director |
| Counter tablets and office PCs | Managed endpoints | Repair stores and depots | Device Repair chief operating officer |
| Bench workstations (about 6,900) and gold images | Endpoints | Repair stores, in-store counters, depots | Device Repair chief operating officer |
| Data recovery lab imaging workstations and storage | On-premises | 2 depots | Device Repair data recovery director |
| P2PE terminals (about 2,600) | Payment devices (processor's validated solution; outside the boundary) | Repair stores and depots | Store managers |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv` (130 controls) and `common-control-catalog.csv` (77 group common controls).

| Status | Controls |
|---|---|
| Implemented | 86 |
| Partially implemented | 42 |
| Planned | 2 |
| Not applicable | 0 |
| **Total** | **130** |

| Inheritance | Controls |
|---|---|
| Common/Inherited (from SYS-G1 to SYS-G4 or group functions) | 56 |
| Hybrid (group provides the mechanism; the STPP team configures or operates part) | 16 |
| System-specific | 58 |

**The 42 partially implemented controls** cluster in six places:
- **Passcodes, credentials, and purpose** (scenario gap 1): AC-3, AC-4, AC-21, AU-6, CM-12, PT-2, PT-3, SI-12.
- **Technician access and shared bench logins** (gap 2): AC-2, AC-6, AC-11, AT-3, AU-12, IA-2, MP-7, PS-6.
- **In-store counter networks and bench hardening** (gap 3): AC-20, CA-7, CM-6, CM-8, CM-11, RA-5, SA-22, SC-7, SI-2, SI-4.
- **Bench tool supply chain** (gap 5): CM-7, SA-4, SA-9, SI-7, SR-2, SR-3, SR-5.
- **Sanitization and media** (gap 4): MP-4, MP-6.
- **Governance, notification, and contingency** (gaps 8 and 10): CP-2, CP-4, CP-10, IA-5, IR-3, IR-6, PL-1.

The 2 planned controls are CM-7(5) (tool allow-listing) and SR-6 (bench tool vendor assessments).

### 10.2 Common control inheritance by division
The common control catalog lists 77 controls provided by corporate. Inheritance is **documented for Electronics Retail** (the PCI responsibility matrix in the 2025 retail ROC), for **IT Support** (its SOC 2 system description carves in the group services), and now for the **STPP** (this plan). It is **not documented for the depots and data recovery labs** (scenario gap 9). Until POAM-013 closes, the division cannot show which controls at the labs come from corporate, and the repair QSA will ask the same question in January 2027.

### 10.3 Control assessment status
Common controls were assessed once, and STPP and division controls sampled, from 2026-07-01 to 2026-08-31 by group internal audit. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
- **Workforce users** authenticate through SYS-G1 federated sign-in with MFA (number matching); **administrators** use phishing-resistant authenticators and just-in-time PAM elevation. Passcode vault reads and refunds require re-authentication (IA-11).
- **Shared bench logins at the 260 in-store counters do not meet this statement.** They are being replaced by named accounts with badge tap and PIN on the bench and MFA at shift start (POAM-001).
- **Interfaces** use workload identities; 6 legacy partner interface secrets are being rotated and moved to the secret store (IA-5).
- **Customers** check repair status through SYS-G4 customer sign-in or a one-time code sent to the phone on the ticket (IA-8). They have no other access to the STPP.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud architecture and control map (P04), group and division risk registers (P01), gap analyses and regulation-by-division matrix (P03), group policies and division supplements (P06), assessment and POA&M (P07), incident response runbook and notification matrix (P08), SOC 2 readiness (P09), AI governance (P10).

## 13. Acronym List and Glossary
- **Bench workstation:** the technician PC that connects to customer devices for diagnostics, flashing, and data transfer
- **In-store repair counter:** a Device Repair counter inside a group electronics store
- **P2PE:** point-to-point encryption; a validated P2PE solution is listed by the PCI Security Standards Council
- **Passcode vault:** the restricted STPP field that holds a device passcode, visible only to the assigned technician and purged 7 days after release
- **PAM:** privileged access management
- **ROC:** Report on Compliance (PCI DSS)
- **TPA:** the third-party administrator of the device protection plans that Electronics Retail sells

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-08-31 | Draft after P07 fieldwork | STPP product owner |
| 1.0 | 2026-09-10 | Approved with authorization conditions | Device Repair CISO |
