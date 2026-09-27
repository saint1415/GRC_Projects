# System Security Plan: Office Clinical Platform (OCP)

**Organization:** Cris Santos Company, LLC (primary care office, two physicians) | **Tier:** Micro | **Vertical:** Health Care and Social Assistance
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Office Clinical Platform (**OCP**), identifier CSC-SYS-001.

## 2. System Overview
The OCP supports every clinical and business process of the practice's single Florida office: scheduling, check-in, visit documentation, e-prescribing, in-office ECG and spirometry, referrals and faxes, claims, and patient communication. It serves 7 workforce members and about 3,500 active patients (about 40 visits per clinic day).

The practice owns almost no infrastructure. Most of the OCP is vendor SaaS, and a managed service provider (MSP) runs the on-site equipment. This plan therefore says, for each control, what the practice does itself, what the MSP does for it, and what it inherits from a SaaS vendor.

**Major components:**
- **SYS-01:** EHR/PM (vendor SaaS) with patient portal, e-prescribing, lab interface, and the clearinghouse connection
- **SYS-02:** productivity suite (SaaS): email and the shared drive
- **SYS-03:** 6 desktops, 4 laptops, 2 tablets (MSP-managed)
- **SYS-04:** office network: firewall, staff Wi-Fi, separate guest Wi-Fi (MSP-managed)
- **SYS-05:** cloud file-sync backup of the shared drive (SaaS, operated by the MSP)
- **SYS-06:** cloud fax (SaaS)
- **SYS-07:** ECG machine and spirometer, connected by USB to the procedure-room workstation

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| N62-R01 | HIPAA Security Rule | 45 CFR Part 164, Subpart C |
| N62-R02 | HIPAA Privacy Rule | 45 CFR Part 164, Subpart E |
| N62-R03 | HIPAA Breach Notification Rule | 45 CFR 164.400-414 |
| N62-R04 | HIPAA Security Rule NPRM (proposed, not in force) | 90 FR 898 (2025-01-06). Tracked only |
| N62-R07 | Section 1557 patient care decision support tools | 45 CFR 92.210. Relevant to EHR decision support alerts and to the AI scribe if suggestion features are enabled (P10) |
| State | Florida Information Protection Act (breach notification) | Fla. Stat. 501.171 |
| Internal | Security policies POL-02, POL-03, POL-04 | P06 |

Not applicable:
- 42 CFR Part 2 (N62-R05): the practice runs no federally assisted SUD program.
- FTC Health Breach Notification Rule (N62-R06): the practice is a HIPAA covered entity, not a vendor of personal health records.
- CMS Emergency Preparedness (N62-R08): the conditions cover hospitals and 16 other provider types, not physician offices.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the owner physician on 2026-08-31.

### 4.2 System Authorization Decision
The practice is not a federal agency, so there is no formal authorization. The equivalent internal decision: on 2026-08-31 the owner physician accepted continued operation of the OCP, on the condition that the POA&M items in P07 are completed by their dates and the three High risks in P01 are treated by 2026-12-31.

### 4.3 System Operational Status
Operational. Planned changes: EDR and backup upgrades (P01 R-001, R-005), desktop encryption (R-007), and a cellular failover router (R-010), all due by 2026-12-31.

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner and risk acceptor | Owner physician | Overall accountability; accepts Moderate risk; approves this plan, policies, and spending |
| Security Officer and Privacy Officer | Office Manager | Day-to-day security and privacy (45 CFR 164.308(a)(2)); maintains this plan, the risk register, and the BAA folder |
| Clinical lead for AI scribe pilot | Associate physician | Pilot decisions and output review (P10) |
| Revenue cycle | Billing Specialist | Clearinghouse and payer access |
| IT operations | MSP (business associate) | Devices, patching, antivirus, firewall, Wi-Fi, backup administration |
| Independent assessor | HIPAA security consultant | Annual control assessment (P07) |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Health care delivery services (patient records, ePHI) | Moderate | Moderate | Moderate | Disclosure harms patients and triggers breach duties; wrong data could harm care; paper downtime limits the availability impact to one clinic day (P05 MTD 8 h) |
| Health care administration (claims, eligibility) | Moderate | Moderate | Low | Financial and identity data; payers accept late claims (P05 MTD 72 h) |
| Human resources management (workforce data) | Moderate | Low | Low | Payroll and HR files in the shared drive |
| **OCP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 7-person office. The plan documents 42 controls that carry the HIPAA Security Rule standards and basic cyber hygiene (see `control-implementation.csv`). All other Moderate-baseline controls are handled one of two ways:
- **Inherited** from the SaaS vendors (physical, platform, and application controls), with the EHR vendor's SOC 2 report as the main evidence (P09).
- **Tailored out** for this tier, where the control addresses federal program management or organizations with dedicated IT staff (for example, configuration change boards and separate development environments). These are recorded as tailoring decisions, not gaps.

## 7. Authorization Boundary Description
The boundary contains what the practice controls or pays someone to control on its behalf:
- **Inside:** the practice's EHR tenant configuration and user roles (SYS-01), the productivity suite tenant and shared drive (SYS-02), 12 devices (SYS-03), the office network (SYS-04), the practice's backup subscription (SYS-05), the cloud fax account (SYS-06), and the ECG machine, spirometer, and their workstation (SYS-07).
- **Outside (external services, interconnected):** the vendors' own platforms and data centers, the clearinghouse and e-prescribing network (reached through the EHR vendor), the reference laboratory, the MSP's remote management platform, and the AI scribe service (SYS-08, a pilot assessed separately in P10).

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Agreement |
|---|---|---|---|
| Clearinghouse (through SYS-01) | Bidirectional | Claims, eligibility, remittance | EHR vendor BAA with subcontractor flow-down |
| E-prescribing network (through SYS-01) | Outbound | Prescriptions | EHR vendor BAA |
| Reference laboratory (through SYS-01 lab interface) | Bidirectional | Orders, results | Treatment disclosure between providers; EHR vendor contract |
| Referring providers and specialists (SYS-06 fax, SYS-02 email) | Bidirectional | Referrals, records | Treatment disclosures; fax vendor BAA on file; suite BAA accepted 2026-08-14 |
| MSP remote management platform | Inbound administrative access | Device management | MSP BAA and service contract |
| AI scribe (SYS-08) | Outbound audio, inbound draft notes | Visit audio and notes (ePHI) | **BAA under review (gap; P10)** |
| Local hospital referral network | Outbound | Security questionnaire answers (no PHI) | None needed |

## 9. System Component Inventory
| Component | Type | Location or provider | Owner |
|---|---|---|---|
| EHR/PM tenant (SYS-01) | SaaS | EHR vendor | Office Manager |
| Productivity suite tenant and shared drive (SYS-02) | SaaS | Productivity suite vendor | Office Manager |
| Desktops (6), laptops (4), tablets (2) (SYS-03) | Endpoint | Office; laptops travel with physicians and the Office Manager | Office Manager (MSP operates) |
| Firewall, staff Wi-Fi, guest Wi-Fi (SYS-04) | Network | Office network closet | Office Manager (MSP operates) |
| File-sync backup subscription (SYS-05) | SaaS | Backup vendor (MSP subcontractor) | Office Manager (MSP operates) |
| Cloud fax account (SYS-06) | SaaS | Cloud fax vendor | Office Manager |
| ECG machine, spirometer, procedure-room workstation (SYS-07) | Medical device and endpoint | Procedure room | Owner physician |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 42 controls:
- Implemented: 13
- Partially implemented: 22
- Planned: 7
- Not applicable: 0

By responsibility: 19 system-specific (the practice), 19 hybrid (the practice with a vendor or the MSP), 4 common/inherited (fully provided by a SaaS vendor).

### 10.2 Inherited and MSP-provided controls
| Provider | What the practice relies on | Evidence | What the practice must still do |
|---|---|---|---|
| EHR vendor | Platform security, encryption, backups (CP-9), session timeout (AC-12), audit records (AU-2, AU-11), account lockout (AC-7) | SOC 2 Type 2 report reviewed 2026-08-20 (P09) | Complementary user entity controls: user provisioning and removal, role assignment, MFA enforcement, access report review |
| Productivity suite vendor | Platform security, encryption at rest and in transit (SC-8, SC-28), lockout (AC-7), audit logging (AU-2) | Vendor documentation; BAA accepted 2026-08-14 | Account management, MFA settings, forwarding and sharing settings, log review |
| Cloud fax vendor | Encrypted transmission and storage (SC-8) | Vendor documentation; BAA | Account management; recipient verification |
| MSP | Patching (SI-2), antivirus (SI-3), firewall and Wi-Fi (SC-7, AC-18), device encryption (SC-28), backup operation (CP-9), device lock (AC-11) | Monthly MSP reports; P07 evidence requests | Oversight: approve exceptions, review reports monthly, annual MSP security review (P01 R-013) |
| Backup service (MSP subcontractor) | Storage of shared-drive copies (CP-9) | None yet; restore test due 2026-09-30 | Confirm subcontractor BAA through the MSP |

**Inherited does not mean done.** Two of the EHR vendor's complementary user entity controls are open gaps at the practice: account removal (AC-2, PS-4) and access report review (AU-6).

### 10.3 Control assessment status
Assessed 2026-08-10 to 2026-08-12 by an independent consultant. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
Workforce users sign in to the EHR and the productivity suite with a password and a second factor (a phone authenticator app). This is appropriate for access to ePHI at the Moderate category. Number matching for push approvals is being enabled (P01 R-003). Patients use the EHR vendor's portal with its own identity proofing; that is governed by the vendor and outside this boundary.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness and EHR vendor report review (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **BAA:** business associate agreement
- **EDR:** endpoint detection and response
- **EHR/PM:** electronic health record and practice management
- **ePHI:** electronic protected health information
- **MFA:** multi-factor authentication
- **MSP:** managed service provider
- **OCP:** Office Clinical Platform
- **POA&M:** plan of action and milestones

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan | Office Manager (Security Officer) |
