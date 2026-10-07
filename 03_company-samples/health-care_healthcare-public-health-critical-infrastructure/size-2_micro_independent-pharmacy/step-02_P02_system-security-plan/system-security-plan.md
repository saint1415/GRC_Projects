# System Security Plan: Pharmacy Core SaaS Stack (PCSS)

**Organization:** Cris Santos Company, LLC (independent community pharmacy) | **Tier:** Micro | **Vertical:** Healthcare and Public Health
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-28

## 1. System Name and Identifier
Pharmacy Core SaaS Stack (**PCSS**), identifier CSC-SYS-001.

## 2. System Overview
The PCSS supports every business process of the pharmacy's single Florida store: prescription intake and dispensing, controlled substance duties, claims to pharmacy benefit managers (PBMs), pickup, adherence packaging, delivery, refill requests, purchasing, and administration. It serves 7 workforce members and about 3,100 active patients (about 55 prescriptions a business day).

The pharmacy owns almost no infrastructure. Most of the PCSS is vendor SaaS, and a managed service provider (MSP) runs the on-site computers and network. This plan therefore says, for each control, what the pharmacy does itself, what the MSP does for it, and what it inherits from a SaaS vendor.

**Major components:**
- **SYS-01:** pharmacy management system (PMS, vendor SaaS): patient profiles, e-prescriptions including EPCS, DUR, labels, real-time claims, the PDMP file, the refill phone line and text reminders, pickup signature capture, and the order interface to SYS-05. It is the client and billing records system
- **SYS-02:** productivity suite (SaaS): email, calendar, and the shared drive
- **SYS-03:** 5 desktops, 2 laptops, and the store delivery phone (MSP-managed)
- **SYS-04:** store network: firewall, staff Wi-Fi, separate guest Wi-Fi, VoIP phones and camera recorder on the staff network (MSP-managed)
- **SYS-05:** adherence packaging system: strip packager and controller workstation (equipment vendor software)
- **SYS-06:** cloud fax (SaaS)
- **SYS-07:** cloud backup service (SaaS, operated by the MSP)
- **SYS-08:** proof-of-delivery app (SaaS, free tier) on the delivery phone

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| C-HPH-R01 | HIPAA Security Rule | 45 CFR Part 164, Subpart C |
| C-HPH-R02 | HIPAA Breach Notification Rule | 45 CFR 164.400-414 |
| C-HPH-R03 | HIPAA Security Rule NPRM (proposed, not in force) | 90 FR 898 (2025-01-06). Tracked only |
| DEA | Electronic prescriptions for controlled substances (pharmacy duties) and CSOS | 21 CFR 1311.200, 1311.205 (application requirements the pharmacy must rely on), 1311.210, 1311.215, 1311.305; 21 CFR 1311.30 |
| DEA | Corresponding responsibility of the dispensing pharmacist | 21 CFR 1306.04(a). Relevant to the SYS-09 risk score (P10) |
| Section 1557 | Patient care decision support tools | 45 CFR 92.210. Relevant to DUR alerts and the SYS-09 risk score (P10) |
| State | Florida Information Protection Act (breach notification) | Fla. Stat. 501.171 |
| State | Florida PDMP reporting and consultation; controlled substance records | Fla. Stat. 893.055(3)(a), (8); 893.07 |
| Internal | Security policies POL-02, POL-03, POL-04 | P06 |

Not applicable:
- 42 CFR Part 2 (C-HPH-R06): the pharmacy does not hold itself out as providing substance use disorder treatment, so it is not a program (42 CFR 2.11).
- FTC Health Breach Notification Rule (C-HPH-R05): 16 CFR 318.1 excludes HIPAA covered entities.
- CMS Emergency Preparedness (C-HPH-R07): pharmacies are not among the covered provider types.
- FDA sec. 524B (C-HPH-R04): duties fall on device manufacturers. The strip packager is not treated here as a cyber device; the store uses the equipment vendor contract instead.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the pharmacist-owner on 2026-08-28.

### 4.2 System Authorization Decision
The pharmacy is not a federal agency, so there is no formal authorization. The equivalent internal decision: on 2026-08-28 the pharmacist-owner accepted continued operation of the PCSS, on the condition that the POA&M items in P07 are completed by their dates and the High risks in P01 are treated by 2026-12-31.

### 4.3 System Operational Status
Operational. Planned changes, all due by 2026-12-31: EDR and backup upgrades (P01 R-001, R-005), desktop encryption (R-007), a separate network segment for the packaging workstation (R-008), and a cellular failover router (R-010).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner and risk acceptor | Pharmacist-owner | Overall accountability; accepts Moderate risk; approves this plan, policies, and spending; DEA registrant contact and CSOS certificate holder |
| Security Officer and Privacy Officer | Store Manager | Day-to-day security and privacy (45 CFR 164.308(a)(2)); maintains this plan, the risk register, and the BAA folder; PMS administrator |
| EPCS audit review | Pharmacist on duty (pharmacist-owner or Staff Pharmacist) | Reviews the daily EPCS audit report and decides on DEA reports (21 CFR 1311.215) |
| Clinical lead for the SYS-09 risk score | Staff Pharmacist | Use, monitoring, and output review (P10) |
| Adherence packaging | Lead Pharmacy Technician | SYS-05 operation and the ALF relationship |
| IT operations | MSP (business associate) | Computers, patching, antivirus, firewall, Wi-Fi, backup administration |
| Independent assessor | HIPAA security consultant | Annual control assessment (P07) |

**Overlapping roles.** One person, the Store Manager, both runs and checks most controls, and also holds PMS administrator rights. The compensating checks are the pharmacist-owner's monthly review of the POA&M and the PMS administrator log, the independent annual assessment (P07), and the vendors' SOC 2 reports (P09).

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Health care delivery services (patient profiles, prescriptions, ePHI) | Moderate | Moderate | Moderate | Disclosure harms patients and triggers breach duties; a wrong drug, dose, or allergy record could harm a patient; paper downtime limits the availability impact to one business day (P05 MTD 8 h) |
| Health care administration (claims, PBM billing) | Moderate | Moderate | Moderate | Financial and identity data; claims stop dispensing at the counter within a day (P05 MTD 24 h) |
| Controlled substance records (EPCS, PDMP, inventory) | Moderate | Moderate | Moderate | Integrity is a federal duty (21 CFR 1311.205(b)(13)-(16)); records must be readily retrievable for 2 years |
| Human resources management (workforce data) | Moderate | Low | Low | Payroll and HR files in the shared drive |
| **PCSS category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 7-person pharmacy. The plan documents 46 controls that carry the HIPAA Security Rule standards, the pharmacy's EPCS duties, and basic cyber hygiene (see `control-implementation.csv`). All other Moderate-baseline controls are handled one of two ways:
- **Inherited** from the SaaS vendors (physical, platform, and application controls), with the PMS vendor's SOC 2 report and EPCS audit report as the main evidence (P09).
- **Tailored out** for this tier, where the control addresses federal program management or organizations with IT staff (for example, configuration change boards and separate development environments). These are recorded as tailoring decisions, not gaps.

## 7. Authorization Boundary Description
The boundary contains what the pharmacy controls or pays someone to control on its behalf:
- **Inside:** the pharmacy's PMS tenant configuration, user roles, and EPCS settings (SYS-01), the productivity suite tenant and shared drive (SYS-02), 5 desktops, 2 laptops, and the delivery phone (SYS-03), the store network (SYS-04), the packaging system (SYS-05), the cloud fax account (SYS-06), the backup subscription (SYS-07), and the delivery app account (SYS-08).
- **Outside (external services, interconnected):** the vendors' own platforms and data centers; the e-prescribing network, claims switch, and PDMP connection (reached through the PMS vendor); PBMs; the Florida PDMP web portal; the wholesaler ordering portal and CSOS ordering; the MSP's remote management platform; the packaging vendor's remote-support service; and the SYS-09 risk score, which runs inside the PMS vendor's platform and is assessed separately in P10.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Agreement |
|---|---|---|---|
| E-prescribing network (through SYS-01) | Inbound | New prescriptions, including EPCS; renewal requests out | PMS vendor BAA with subcontractor flow-down |
| Claims switch and PBMs (through SYS-01) | Bidirectional | Real-time claims and responses | PMS vendor BAA; PBM network agreements |
| Florida PDMP (through SYS-01; web portal) | Outbound nightly file; pharmacist queries | Controlled substance dispensing data | Required by Fla. Stat. 893.055; state system |
| Prescriber offices (SYS-06 fax; phone) | Bidirectional | Prescriptions, refill authorizations | Treatment disclosures; fax vendor BAA |
| Two ALFs (SYS-02 email; SYS-06 fax) | Bidirectional | Orders, medication lists, delivery confirmations | Treatment disclosures; supply agreement with the ALF management company |
| Packaging equipment vendor remote support | Inbound administrative access | SYS-05 workstation and pack data | Service contract only; **no BAA (gap; P01 R-008)** |
| Proof-of-delivery app vendor (SYS-08) | Outbound | Patient names, addresses, prescription numbers, signature photos | Free-tier terms only; **no BAA (gap; P01 R-012)** |
| MSP remote management platform | Inbound administrative access | Device management | MSP BAA and service contract |
| Drug wholesaler (portal and CSOS) | Outbound | Orders, including Schedule II orders signed with CSOS | Supply agreement; no PHI |

## 9. System Component Inventory
| Component | Type | Location or provider | Owner |
|---|---|---|---|
| PMS tenant (SYS-01) | SaaS | PMS vendor | Store Manager |
| Productivity suite tenant and shared drive (SYS-02) | SaaS | Productivity suite vendor | Store Manager |
| Desktops (5), laptops (2), delivery phone (SYS-03) | Endpoint | Store; laptops travel with the pharmacist-owner and Store Manager; phone with the Delivery Driver | Store Manager (MSP operates) |
| Firewall, staff Wi-Fi, guest Wi-Fi, VoIP phones, camera recorder (SYS-04) | Network | Back office network shelf | Store Manager (MSP operates) |
| Strip packager and controller workstation (SYS-05) | Equipment and endpoint | Packaging room | Lead Pharmacy Technician (equipment vendor supports) |
| Cloud fax account (SYS-06) | SaaS | Cloud fax vendor | Store Manager |
| Cloud backup subscription (SYS-07) | SaaS | Backup vendor (MSP subcontractor) | Store Manager (MSP operates) |
| Proof-of-delivery app account (SYS-08) | SaaS | App vendor | Store Manager |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 46 controls:
- Implemented: 12
- Partially implemented: 28
- Planned: 6
- Not applicable: 0

By responsibility: 19 system-specific (the pharmacy), 23 hybrid (the pharmacy with a vendor or the MSP), 4 common/inherited (fully provided by a SaaS vendor).

### 10.2 Inherited and MSP-provided controls
| Provider | What the pharmacy relies on | Evidence | What the pharmacy must still do |
|---|---|---|---|
| PMS vendor | Platform security, encryption, backups including the daily backup of controlled substance records (CP-9), EPCS digital signature and archiving (SC-13), the EPCS audit trail and daily audit report (AU-2), lockout (AC-7) | SOC 2 Type 2 report and EPCS third-party audit report reviewed 2026-08-12 (P09) | Complementary user entity controls: user provisioning and removal, role assignment (including who may alter controlled substance records, 21 CFR 1311.200(e)), MFA settings, review of access reports and the daily EPCS report, and the one-business-day report of EPCS security incidents (1311.215(c)) |
| Productivity suite vendor | Platform security, encryption at rest and in transit (SC-8, SC-28), lockout (AC-7), audit logging (AU-2) | Vendor documentation; BAA accepted 2024 | Account management, MFA settings, sharing and forwarding settings, encryption rule, log review |
| Cloud fax vendor | Encrypted transmission and storage (SC-8) | Vendor documentation; BAA | Account management; recipient verification |
| MSP | Patching (SI-2), antivirus (SI-3), firewall and Wi-Fi (SC-7, AC-18), laptop encryption (SC-28), backup operation (CP-9), device lock (AC-11) | Monthly MSP reports; P07 evidence requests | Oversight: approve exceptions, review reports monthly, annual MSP security review (P01 R-013) |
| Backup service (MSP subcontractor) | Storage of backup copies (CP-9) | None yet; restore test due 2026-09-30 | Confirm the subcontractor BAA through the MSP |

**Inherited does not mean done.** Three of the PMS vendor's complementary user entity controls are open gaps at the pharmacy: account removal (AC-2, PS-4), review of access reports and the daily EPCS audit report (AU-6), and in-store MFA (IA-2(2)). The fourth, controlled substance permissions, was fixed on 2026-07-17 (AC-6).

### 10.3 Control assessment status
Assessed 2026-08-04 to 2026-08-06 by an independent consultant. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
Workforce users sign in to the productivity suite with a password and a phone authenticator app, and to the PMS from outside the store the same way. Inside the store, PMS sign-in uses a password only, because the vendor treats the store network as a trusted location. For access to ePHI at the Moderate category, that in-store gap is accepted only until the vendor's second-factor option is enabled (target 2026-12-31; IA-2(2)). EPCS prescriber authentication happens in the prescribers' own applications, outside this boundary. The CSOS certificate is a DEA-issued digital certificate held by the pharmacist-owner alone (21 CFR 1311.30(a)).

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness and PMS vendor report review (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **ALF:** assisted living facility
- **BAA:** business associate agreement
- **CSOS:** Controlled Substance Ordering System (DEA digital certificates for electronic Schedule II orders)
- **DUR:** drug utilization review
- **EDR:** endpoint detection and response
- **EPCS:** electronic prescriptions for controlled substances
- **ePHI:** electronic protected health information
- **MFA:** multi-factor authentication
- **MSP:** managed service provider
- **PBM:** pharmacy benefit manager
- **PCSS:** Pharmacy Core SaaS Stack
- **PDMP:** prescription drug monitoring program
- **PMS:** pharmacy management system
- **POA&M:** plan of action and milestones

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-28 | Initial plan | Store Manager (Security Officer) |
