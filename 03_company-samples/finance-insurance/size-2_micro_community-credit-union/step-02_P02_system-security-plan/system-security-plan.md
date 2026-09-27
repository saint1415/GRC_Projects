# System Security Plan: Core and Digital Banking Platform (CDBP)

**Organization:** Cris Santos Community Federal Credit Union (member-owned federal credit union) | **Tier:** Micro | **Vertical:** Finance and Insurance
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Core and Digital Banking Platform (**CDBP**), identifier CSCFCU-SYS-001.

## 2. System Overview
The CDBP is how the credit union serves its members: teller and account services, online and mobile banking, outgoing wires, member email and documents, and the records behind them. It serves 7 employees and about 6,400 members, about 3,900 of whom use online or mobile banking.

The credit union owns almost no infrastructure. The core processor, the digital banking provider, and the corporate credit union run the platforms; the productivity suite is SaaS; and the managed service provider (MSP) runs the office computers, the network, and the document imaging server in a cloud tenant. This plan therefore says, for each control, what the credit union does itself, what the MSP does for it, and what it inherits from a vendor.

**Major components:**
- **SYS-01:** core processing system (vendor-hosted): the credit union's users, role profiles, and teller configuration
- **SYS-02:** online and mobile banking (vendor-hosted): the credit union's admin console settings and staff users
- **SYS-03:** wire transfer portal (corporate credit union web service): makers, approvers, and hardware tokens
- **SYS-04:** productivity suite (SaaS): email, the Member Services shared mailbox, and shared files
- **SYS-05:** 8 desktops, 3 laptops, 2 check scanners (MSP-managed)
- **SYS-06:** office network: firewall, staff and guest Wi-Fi, VoIP phones, one internet line (MSP-managed)
- **SYS-09:** document imaging server: one virtual server in a public cloud IaaS tenant (MSP-operated)

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| N52-R01 | Gramm-Leach-Bliley Act section 501(b), as implemented for federally insured credit unions by NCUA | 15 U.S.C. 6801(b); 12 CFR 748.0 (security program); Part 748 Appendix A (Guidelines for Safeguarding Member Information); Appendix B (response programs and member notice) |
| C-FINANCIAL-R03 | NCUA cyber incident notification (Financial Services critical infrastructure overlay) | 12 CFR 748.1(c): notice to NCUA no later than 72 hours after the credit union reasonably believes a reportable cyber incident occurred (in force since 2023-09-01, 88 FR 12811) |
| Rule | Suspicious activity reports | 12 CFR 748.1(d); 31 CFR 1020.320 |
| Rule | Disposal of consumer information (federal credit unions) | 12 CFR 748.0(c); 12 CFR 717.83 |
| Rule | Identity Theft Prevention Program (federal credit unions) | 12 CFR 717.90 |
| Rule | Vital records preservation program | 12 CFR Part 749 (rewritten effective 2026-07-16) |
| State | Funds-transfer liability and security procedures (UCC Article 4A) | Fla. Stat. 670.202 and 670.204 |
| State | Florida Information Protection Act (breach notification) | Fla. Stat. 501.171 |
| Internal | Security policies POL-02, POL-03, POL-04 | P06 |

**How the vertical's requirement IDs are used.** The Finance and Insurance requirement list has no separate row for NCUA Part 748. This plan cites Part 748 under N52-R01, because Appendix A states that it sets standards under GLBA section 501 (15 U.S.C. 6801), and cites 748.1(c) under C-FINANCIAL-R03 from the Financial Services critical infrastructure overlay.

Not applicable:
- **The OCC, Federal Reserve, and FDIC Interagency Guidelines (N52-R02) and the 36-hour notification rule (12 CFR Part 53 and parallels):** they apply to banks and bank holding companies. A federal credit union follows NCUA's Part 748 instead.
- **FTC Safeguards Rule (N52-R03):** it reaches non-federally insured credit unions, not this one.
- **NYDFS Part 500, SEC Regulation S-P and S-ID, NAIC Model #668, SEC cybersecurity disclosure (N52-R04 to N52-R08):** the reasons are in `../00_company-facts.md` section 1.

Consumer wires sent through Fedwire or a similar wire system are excluded from Regulation E's definition of electronic fund transfer (12 CFR 1005.3(c)(3)). Liability for an unauthorized wire therefore turns on UCC Article 4A as enacted in Florida, not on Regulation E.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the President and CEO on 2026-08-31. The board approved the information security program update and POL-02 to POL-04 on 2026-08-25.

### 4.2 System Authorization Decision
The credit union is not a federal agency, so there is no formal authorization. The equivalent internal decision: on 2026-08-31 the President and CEO accepted continued operation of the CDBP on condition that the P07 POA&M items are completed by their dates and the four High risks in P01 have treatment plans reported to the board each month until closed.

### 4.3 System Operational Status
Operational. Planned changes: required callbacks and BEC training (P01 R-001), member MFA and alerts (R-003), a copy of imaging backups outside the cloud account (R-010), desktop encryption (R-012), and a cellular failover router (R-013), all due by 2026-12-31.

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| Program approval and oversight | Board of Directors | Approves the written program (App. A III.A.1); receives the annual report (III.F); accepts High risks |
| System owner | President and CEO | Overall accountability; accepts Moderate risks; approves this plan |
| Information Security Officer and Privacy Officer | Operations Manager | Day-to-day security; maintains this plan, the risk register, and the vendor file; MSP contact |
| BSA Officer | Accounting and Compliance Officer | SAR decisions and filings (748.1(d)); backup wire approver |
| Wire maker | Senior Member Service Representative | Takes and keys wire requests |
| Lending system owner | Lending Manager | LOS users and the AI scoring pilot (P10) |
| IT operations | MSP | Devices, patching, antivirus, firewall, Wi-Fi, suite administration, imaging server |
| Independent assessor | IT audit consultant engaged by the Supervisory Committee | Annual control assessment (P07; App. A III.C.3) |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Payments and collections (wire instructions, ACH) | Moderate | Moderate | Moderate | A fraudulent or altered wire causes direct loss. Dual control, wire limits, and the fidelity bond keep a single loss serious rather than severe for a $60 million credit union. The alternate phone wire covers one business day (P05 MTD 8 h) |
| Member account and identity information (NPI, credentials, ID copies) | Moderate | Moderate | Moderate | Disclosure enables account takeover and identity theft and triggers the Appendix B member notice analysis; members need account access the same day (P05 BP-01 MTD 8 h) |
| Workforce identities | Moderate | Low | Low | Account data; limited harm if unavailable |
| **CDBP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 7-person credit union. The plan documents 47 controls that carry the Part 748 standards and basic cyber hygiene (see `control-implementation.csv`); two of them (PM-2, PM-9) are program controls outside the baseline, added because Appendix A III.A asks the board to assign responsibility and oversee the program. All other Moderate-baseline controls are handled one of two ways:
- **Inherited** from the core processor, the digital banking provider, the corporate credit union, and the SaaS vendors (physical, platform, and application controls), with their SOC reports as the main evidence (P09).
- **Tailored out** for this tier, where the control addresses federal program management or organizations with dedicated IT staff (for example, configuration change boards and separate development environments). These are recorded as tailoring decisions, not gaps.

## 7. Authorization Boundary Description
The boundary contains what the credit union controls or pays someone to control on its behalf:
- **Inside:** the credit union's users, role profiles, and settings in the core (SYS-01), the online banking admin console (SYS-02), and the wire portal (SYS-03); the productivity suite tenant (SYS-04); 8 desktops, 3 laptops, and 2 check scanners (SYS-05); the office network and phones (SYS-06); and the document imaging server and its snapshots (SYS-09).
- **Outside (external services, interconnected):** the vendors' own platforms and data centers; the card processor and lobby ATM (SYS-07); the loan origination system and its AI scoring add-on (SYS-08, assessed in P10); the Federal Reserve payment services reached through the corporate credit union; and the MSP's remote management platform.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Agreement |
|---|---|---|---|
| Core processor (SYS-01) | Bidirectional | Member accounts, transactions, the nightly offline-teller balance file | Core processing contract (renewal 2027-06-30; no incident notice time frame) |
| Digital banking provider (SYS-02) | Bidirectional | Member credentials, transactions, e-statements | Service agreement |
| Corporate credit union (SYS-03) | Outbound | Wire instructions; settlement | Wire service agreement with maker-checker and token terms |
| Card processor (SYS-07) | Bidirectional | Card authorizations, card fraud alerts | Card processing agreement |
| LOS vendor (SYS-08) | Bidirectional | Applications, credit reports, AI scores and reason codes | SaaS agreement (P10 reviews its data-use terms) |
| Members (SYS-04 email) | Bidirectional | Loan documents, ID copies, wire request forms | Membership agreement; **no written wire security procedure (gap; P03 G-025)** |
| MSP remote management platform | Inbound administrative access | Device and tenant management | MSP service contract |
| Cloud IaaS provider (SYS-09) | Hosted | Imaging server and snapshots | Provider terms, through the MSP's tenant |

## 9. System Component Inventory
| Component | Type | Location or provider | Owner |
|---|---|---|---|
| Core users and role profiles (SYS-01) | SaaS configuration | Core processor | Operations Manager |
| Online banking admin console (SYS-02) | SaaS configuration | Digital banking provider | Operations Manager |
| Wire portal users and tokens (SYS-03) | SaaS configuration | Corporate credit union | Operations Manager |
| Productivity suite tenant and shared mailbox (SYS-04) | SaaS | Productivity suite vendor | Operations Manager (MSP administers) |
| Desktops (8), laptops (3), check scanners (2) (SYS-05) | Endpoint | Office; laptops travel with the CEO, Operations Manager, and Lending Manager | Operations Manager (MSP operates) |
| Firewall, Wi-Fi, VoIP phones (SYS-06) | Network | Office network closet | Operations Manager (MSP operates) |
| Imaging server and snapshots (SYS-09) | IaaS workload | Cloud IaaS provider, MSP's tenant | Operations Manager (MSP operates) |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 47 controls:
- Implemented: 13
- Partially implemented: 27
- Planned: 7
- Not applicable: 0

By responsibility: 20 system-specific (the credit union), 23 hybrid (the credit union with a vendor or the MSP), 4 common/inherited (fully provided by a vendor).

### 10.2 Inherited and MSP-provided controls
| Provider | What the credit union relies on | Evidence | What the credit union must still do |
|---|---|---|---|
| Core processor | Platform security, replication and backup (CP-9), lockout (AC-7), session timeout (AC-12), audit records (AU-2) | SOC 1 Type 2 and SOC 2 Type 2 reports; SOC 2 reviewed 2026-08-18 (P09) | Complementary user entity controls: user setup and removal, role assignment, review of user and exception reports, office IP allowlist |
| Digital banking provider | Platform security, member sign-in service (IA-8), encryption (SC-8), audit logging | SOC 2 Type 2 report (review due 2026-11-30) | Admin console users and MFA, member authentication settings, alerts, log review |
| Corporate credit union | Wire portal security, maker-checker enforcement (AC-5), hardware tokens | Service agreement; audit summary requested | Maker and approver assignment, token custody, callback before keying |
| Productivity suite vendor | Platform security, encryption, lockout, audit logging | Vendor documentation | Account management, MFA, mailbox rules and forwarding settings, log review |
| MSP | Patching (SI-2), antivirus (SI-3), firewall and Wi-Fi (SC-7, AC-18), laptop encryption (SC-28), imaging server operation and snapshots (CP-9) | Monthly MSP reports; P07 evidence requests | Oversight: approve changes, review reports monthly, annual MSP security review (P01 R-014) |

**Inherited does not mean done.** Two of the core processor's complementary user entity controls are open gaps at the credit union: account removal (AC-2, PS-4) and review of user and exception reports (AU-6).

### 10.3 Control assessment status
Assessed 2026-08-04 to 2026-08-06 by an independent IT audit consultant. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
Staff sign in to the suite, the admin console, and the wire portal with a password and a second factor (authenticator app or hardware token). The core offers no MFA for teller users; access is limited to the office IP address as a compensating control. Members sign in to online banking with a password and a text code at new-device registration only. That is weak for accounts that can move money, and member MFA at sign-in and for sensitive changes is planned (P01 R-003). Member identity proofing at account opening follows the customer identification program (748.2(b)(2)) and is outside this plan.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness and core processor report review (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **BEC:** business email compromise
- **CDBP:** Core and Digital Banking Platform
- **CUEC:** complementary user entity control
- **ISO:** Information Security Officer
- **LOS:** loan origination system
- **MFA:** multi-factor authentication
- **MSP:** managed service provider
- **MSR:** Member Service Representative
- **NPI:** nonpublic personal information
- **POA&M:** plan of action and milestones

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan | Operations Manager (Information Security Officer) |
