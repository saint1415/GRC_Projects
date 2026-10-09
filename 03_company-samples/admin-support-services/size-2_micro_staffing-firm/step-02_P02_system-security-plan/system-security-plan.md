# System Security Plan: Payroll and Applicant Tracking System (PATS)

**Organization:** Cris Santos Company, LLC (temporary staffing firm) | **Tier:** Micro | **Vertical:** Administrative and Support and Waste Management and Remediation Services
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Payroll and Applicant Tracking System (**PATS**), identifier CSC-SYS-001.

## 2. System Overview
The PATS supports the firm's whole staffing cycle from one Central Florida office: taking client orders, recruiting and screening applicants, onboarding new associates (Form I-9, E-Verify, background checks), capturing and approving time, and paying about 22 associates on assignment and 7 staff every Friday. It holds the most sensitive records the firm keeps: SSNs, dates of birth, bank account numbers, identity document images, and consumer reports for about 9,800 candidates and several hundred current and former workers.

The firm owns almost no infrastructure. The PATS is mostly vendor SaaS, and a managed service provider (MSP) runs the laptops, the office network, and the suite backup. This plan therefore says, for each control, what the firm does itself, what the MSP does for it, and what it inherits from a SaaS vendor.

**Major components:**
- **SYS-01:** staffing ATS (vendor SaaS): career site, applicants, job orders, onboarding packets, screening orders
- **SYS-02:** payroll and timekeeping service (vendor SaaS): payroll, tax filing, direct deposit, associate self-service, clock-in, client approvals
- **SYS-03:** productivity suite (SaaS): email, calendar, chat, shared drive with the Onboarding folder
- **SYS-04:** 8 laptops, 1 applicant tablet, 1 multifunction scanner (MSP-managed); 7 personal smartphones used for work
- **SYS-05:** office network: firewall, staff Wi-Fi, guest Wi-Fi, one internet line (MSP-managed)
- **SYS-08:** SaaS-to-SaaS backup of the productivity suite (operated by the MSP)

**Interconnected services inside the plan's scope of review:** SYS-06 background screening portal (integrated with the ATS), SYS-07 E-Verify, and SYS-09 the ATS AI match feature (assessed in P10).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it touches the PATS |
|---|---|---|---|
| N56-BM | NIST CSF 2.0 (voluntary benchmark) | NIST CSWP 29 | Benchmark for the gap analysis (P03); not a legal duty |
| N56-R03 | Form I-9 retention and electronic retention standards | 8 CFR 274a.2(b)(2)-(4), (e)-(i) | Paper Forms I-9 and their scans in the shared drive; the scans of document images bring in the electronic standards (274a.2(b)(3)) |
| Contract | E-Verify MOU for Employers | MOU Art. II.A (revision 06/01/13) | E-Verify user access, safeguarding of E-Verify information and passwords, immediate breach notice to DHS |
| State | Florida employment eligibility | Fla. Stat. 448.095(2) | Verification within 3 business days; outage documentation; 3-year retention of verification documentation |
| N56-R02 | FCRA employment background checks | 15 U.S.C. 1681b(b) | Disclosure, authorization, and adverse action steps run through SYS-06 |
| N56-R01 | FACTA Disposal Rule | 16 CFR 682.3 | Disposal of consumer report information in the shared drive, laptops, and paper |
| State | Florida Information Protection Act | Fla. Stat. 501.171 | Reasonable security measures (2), breach notices (3)-(6), disposal of customer records (8) |
| Federal | Title VII, ADEA, ADA (employment agency and employer) | 42 U.S.C. 2000e-2; 29 U.S.C. 623; 42 U.S.C. 12112 | Use of the AI match feature in referrals (P10) |
| Internal | Security policies POL-02, POL-03, POL-04 | P06 | |

Not applicable (decided in the intake [obligations register](../step-00_P00_intake/obligations-register.csv); reasons restated in P03): HIPAA as a business associate (N56-R04), TCPA and the Telemarketing Sales Rule (N56-R05), PCI DSS (N56-R06), FAR 52.204-21 (N56-R07), NYC Local Law 144 (N56-R08), PHMSA security plans (N56-R09).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Owner on 2026-08-31.

### 4.2 System Authorization Decision
The firm is not a federal agency, so there is no formal authorization. The equivalent internal decision: on 2026-08-31 the Owner accepted continued operation of the PATS on the condition that the POA&M items in P07 are completed by their dates and the three High risks in P01 (R-001 payroll account takeover, R-009 AI screening bias, R-013 MSP compromise) are treated by 2026-12-31.

### 4.3 System Operational Status
Operational. Planned changes by 2026-12-31: authenticator-app MFA and bank-change alerts in the payroll service (R-001), folder permissions and a purge of the Onboarding folder (R-004, R-015), backup MFA and restore tests (R-005), and MSP contract terms (R-013).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner and risk acceptor | Owner (President) | Overall accountability; accepts Moderate and higher risk; approves this plan, policies, and spending |
| Security and Privacy Lead | Operations Manager | Day-to-day security and privacy; maintains this plan, the risk register, and the vendor file; E-Verify program administrator; payroll approver |
| Onboarding and payroll operations | Onboarding and Payroll Coordinator | Form I-9, E-Verify cases, screening orders and FCRA notices, payroll entry, bank-change requests |
| ATS administrator | Senior Recruiter | ATS users and settings, including the AI match feature (P10) |
| IT operations | MSP (contractor) | Laptops, patching, antivirus, firewall, Wi-Fi, suite administration on request, backup administration |
| Independent assessor | Security consultant | Annual control assessment (P07) |

**Where roles overlap.** The Operations Manager approves payroll, administers E-Verify, runs security, and reviews the logs of the systems she uses. In a 7-person firm that cannot be avoided. It is offset by the Owner's monthly review of the payroll bank-change report (planned under R-001), the MSP and payroll vendor evidence, and the independent assessment in P07.

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Personnel identification and payroll (SSNs, bank accounts, pay) | Moderate | Moderate | Moderate | Disclosure enables identity theft and triggers Florida breach notice; altered bank data diverts pay; payroll has a one-day MTD (P05 BP-02) |
| Employment eligibility records (Form I-9 images, E-Verify data) | Moderate | Moderate | Low | Use limited by law (8 CFR 274a.2(b)(4)); paper originals are the record of retention, so loss of scans is recoverable |
| Applicant and consumer report data | Moderate | Low | Low | Consumer reports and resumes; recruiting can pause 2 to 3 days (P05 BP-05) |
| Client orders and time records | Low | Moderate | Moderate | Wrong hours mean wrong pay and invoices; orders have the shortest MTD (P05 BP-01) |
| **PATS category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 7-person firm. The plan documents 42 controls that carry the firm's legal duties and basic cyber hygiene (see `control-implementation.csv`). All other Moderate-baseline controls are handled one of two ways:
- **Inherited** from the SaaS vendors (physical, platform, and application controls), with the payroll vendor's SOC 2 report as the main evidence (P09).
- **Tailored out** for this tier, where the control addresses federal program management or organizations with their own IT staff (for example, configuration change boards and separate development environments). These are recorded as tailoring decisions, not gaps.

Two controls outside the Moderate baseline were added by tailoring: PM-2 (the designated lead) and PT-5 (privacy notice, because applicants must be told about AI scoring). SI-12 is in the baseline and is called out because Form I-9 and consumer report retention is the firm's largest data problem.

## 7. Authorization Boundary Description
The boundary was drawn from the intake [asset inventory](../step-00_P00_intake/asset-inventory.csv). It contains what the firm controls, or pays someone to control on its behalf:
- **Inside:** the firm's ATS tenant, users, and settings (SYS-01); its payroll service account, administrators, and settings (SYS-02); the suite tenant and shared drive (SYS-03); 8 laptops, the applicant tablet, the scanner, and the work use of 7 personal phones (SYS-04); the office network (SYS-05); the firm's backup subscription (SYS-08).
- **Outside but interconnected (reviewed in this plan):** the screening provider's platform (SYS-06), E-Verify (SYS-07), and the ATS vendor's AI subprocessor (SYS-09).
- **Outside:** the vendors' own platforms and data centers, the firm's bank, job boards, the MSP's remote management platform, and the accounting SaaS (SYS-10), which holds no worker PII beyond client contacts.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Agreement |
|---|---|---|---|
| Background screening provider (SYS-06, through the ATS) | Bidirectional | Candidate identifiers out; consumer reports and status in | Screening services agreement with the FCRA end-user certification; **no breach notice term** |
| E-Verify (SYS-07) | Outbound by staff entry | Form I-9 data; case results | E-Verify MOU (2024-03-04) |
| ATS AI subprocessor (SYS-09) | Outbound | Resumes and application answers; scores back | ATS click-through AI terms; **no data use or no-training term** (P10) |
| Payroll service to the firm's bank and associates' banks | Outbound | Direct deposit files; tax payments | Payroll services agreement |
| Client supervisors (approver portal) | Inbound | Time approvals | Client service agreements |
| Job boards | Inbound | Applications | Job board terms |
| MSP remote management platform | Inbound administrative access | Laptop management | MSP service contract (**no security terms**) |
| Largest client's security questionnaire | Outbound | Answers and this plan's summary (no worker data) | Client master services agreement |

## 9. System Component Inventory
| Component | Type | Location or provider | Owner |
|---|---|---|---|
| ATS tenant (SYS-01) | SaaS | ATS vendor | Senior Recruiter |
| Payroll service account (SYS-02) | SaaS | Payroll service vendor | Operations Manager |
| Suite tenant and shared drive (SYS-03) | SaaS | Productivity suite vendor | Operations Manager (MSP administers on request) |
| Laptops (8), applicant tablet (1), multifunction scanner (1) (SYS-04) | Endpoint | Office; laptops also used from home | Operations Manager (MSP operates) |
| Personal smartphones used for work (7) (SYS-04) | Endpoint (personal) | Staff | Each staff member; rules in POL-02 Part C |
| Firewall, staff Wi-Fi, guest Wi-Fi, internet line (SYS-05) | Network | Office network closet | Operations Manager (MSP operates) |
| Suite backup subscription (SYS-08) | SaaS | Backup service (MSP-operated) | Operations Manager (MSP operates) |
| Paper Form I-9 cabinet | Physical records | Locked records room | Operations Manager |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 42 controls:
- Implemented: 12
- Partially implemented: 18
- Planned: 12
- Not applicable: 0

By responsibility: 21 system-specific (the firm), 17 hybrid (the firm with a vendor or the MSP), 4 common/inherited (fully provided by a SaaS vendor).

### 10.2 Inherited and MSP-provided controls
| Provider | What the firm relies on | Evidence | What the firm must still do |
|---|---|---|---|
| Payroll service vendor | Platform security, encryption, backups (CP-9), audit records (AU-2, AU-11), lockout (AC-7) | SOC 2 Type 2 report (EV-049) reviewed 2026-08-20 (P09) | Complementary user entity controls: administrator provisioning and removal, MFA settings, review of bank changes and exports |
| ATS vendor | Platform security, encryption, backups, role enforcement (AC-3), audit records (AU-2) | Trust page only (EV-009); SOC 2 report requested, not received | Users and roles, MFA enforcement, export review, AI settings |
| Productivity suite vendor | Platform security, encryption in transit and at rest (SC-8, SC-28), lockout (AC-7), audit logging (AU-2) | Vendor documentation (EV-038) | Account management, MFA settings, folder permissions, forwarding rules, log review |
| MSP | Patching (SI-2), antivirus (SI-3), firewall and Wi-Fi (SC-7, AC-18), laptop encryption (SC-28), backup operation (CP-9), screen lock (AC-11) | MSP reports (EV-019 to EV-021); MSP contract (EV-018); P07 evidence requests | Oversight: approve exceptions, review reports monthly, annual MSP security review (P01 R-013) |
| Backup service (MSP-operated) | Storage of suite copies (CP-9) | None yet; restore test due 2026-09-30 | Require MFA on the console; receive restore results |

**Inherited does not mean done.** The payroll vendor's report lists controls the firm must run for the vendor's controls to work. Two are open gaps: MFA strong enough to resist phishing on administrator accounts (IA-2(1)) and review of bank changes and exports (AU-6, SI-4). Those two gaps are exactly the path of the P08 scenario.

### 10.3 Control assessment status
Assessed 2026-08-10 to 2026-08-12 by an independent consultant. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
Staff sign in to the ATS and the suite with a password and a second factor from a phone app. The payroll service uses a password and an SMS code, which is weaker than the other two because a phishing page can relay the code in real time. Given that the payroll service can change where money goes, the firm will move its administrators to authenticator-app MFA by 2026-10-31 (R-001) and add a call-back rule for every bank change. Associates use the payroll vendor's self-service with a password only; adding a verification step for bank changes is requested from the vendor (R-002). Applicants use the ATS career site without an account.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), intake evidence, inventories and obligations register ([step-00](../step-00_P00_intake/intake-report.md)), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness and payroll vendor report review (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **AiTM:** adversary-in-the-middle (a phishing page that relays the sign-in, including MFA codes)
- **ATS:** applicant tracking system
- **CRA:** consumer reporting agency
- **MFA:** multi-factor authentication
- **MOU:** E-Verify Memorandum of Understanding for Employers
- **MSP:** managed service provider
- **PATS:** Payroll and Applicant Tracking System
- **POA&M:** plan of action and milestones

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan | Operations Manager (Security and Privacy Lead) |
