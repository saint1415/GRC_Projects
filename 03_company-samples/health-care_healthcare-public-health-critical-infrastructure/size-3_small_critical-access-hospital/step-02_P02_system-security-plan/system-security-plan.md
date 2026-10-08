# System Security Plan: Hospital Clinical Information System (HCIS)

**Organization:** Cris Santos Company, LLC (rural critical access hospital) | **Tier:** Small | **Vertical:** Healthcare and Public Health
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Hospital Clinical Information System (**HCIS**), identifier CSC-SYS-001.

## 2. System Overview
The HCIS supports every clinical and business process at the hospital's single Florida campus: emergency department care, inpatient and swing-bed nursing, medication administration, pharmacy, laboratory, CT and X-ray imaging with teleradiology reads, registration and transfers, claims, and public health reporting. It serves 60 employees, about 40 contracted clinicians and agency nurses, and patients whose records number about 38,000.

**Major components:**
- **SYS-01:** a vendor-hosted EHR (ED, inpatient, eMAR with barcode scanning, pharmacy, laboratory module, patient accounting, portal), including the vendor's sepsis prediction model (**SYS-13**)
- **SYS-02:** an identity provider for single sign-on and MFA, synchronized with the on-premises directory
- **SYS-04:** a public-cloud tenant hosting the imaging archive and viewer, the interface engine, and the backup vault
- **SYS-05:** the hospital network, phones, and server room (virtualization host with the directory, file, print, analyzer middleware, dispensing cabinet, and infusion pump drug-library servers)
- **SYS-06:** endpoints, including two EHR downtime PCs
- **SYS-07:** medical devices (CT, X-ray, infusion pumps, monitors, analyzers, dispensing cabinets)

The cloud tenant is described by service category and is vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| C-HPH-R01 | HIPAA Security Rule | 45 CFR Part 164, Subpart C |
| C-HPH-R02 | HIPAA Breach Notification Rule | 45 CFR 164.400-414 |
| C-HPH-R03 | HIPAA Security Rule NPRM (proposed, not in force) | 90 FR 898 (2025-01-06). Tracked only |
| C-HPH-R07 | CMS emergency preparedness | 42 CFR 485.625 (the CAH counterpart of 482.15). Governs the plan, medical documentation during emergencies, communications, and exercises |
| C-HPH-R08 | HHS HPH Cybersecurity Performance Goals (voluntary) | Self-benchmark in P03 `cpg-benchmark.csv` |
| C-HPH-R09 | HHS 405(d) HICP (voluntary) | 2023 edition, Technical Volume 1 (small organizations) |
| C-HPH-R10 | HITECH recognized security practices | 42 U.S.C. 17941 |
| N62-R07 (parent vertical) | Section 1557 patient care decision support tools | 45 CFR 92.210. Applies to the sepsis prediction model (P10) |
| Other federal | EMTALA | 42 CFR 489.24. Screening and stabilization continue during any IT outage; ambulance diversion rules |
| Other federal | Medicare Promoting Interoperability Program | 42 CFR 495.24 (annual security risk analysis attestation) |
| State | Florida Information Protection Act (breach notification) | Fla. Stat. 501.171 |
| Internal | Security policies POL-01 to POL-05 | P06 |

Not applicable:
- 42 CFR Part 2 (C-HPH-R06): the hospital is not a Part 2 program (scoping decision, screened in the intake [obligations register](../step-00_P00_intake/obligations-register.csv) from the license and service list, EV-024).
- FTC Health Breach Notification Rule (C-HPH-R05): covered entities are excluded (16 CFR 318.1).
- FDA sec. 524B (C-HPH-R04): applies to device manufacturers; the hospital uses it in purchasing.
- CIRCIA (C-HPH-R11): proposed only. If finalized as proposed, it would cover critical access hospitals regardless of size.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the CEO on 2026-08-31.
### 4.2 System Authorization Decision
The hospital is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- The CEO accepted continued operation of the HCIS on 2026-08-31, with the conditions in the P07 POA&M.
- The governing body accepted the Very High and High risks in P01 temporarily, with dated treatment plans, and receives a monthly status report until R-001 falls below Very High.
### 4.3 System Operational Status
Operational. Major modifications planned: network segmentation (P01 R-001), backup redesign (R-003, due 2026-11-30), and named vendor remote access with MFA (due 2026-10-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | CEO | Overall accountability; risk acceptance up to Moderate |
| Risk acceptor (authorizing official equivalent) | Governing body | Acceptance of High and Very High risks |
| Security Officer | IT Manager | Day-to-day security; 45 CFR 164.308(a)(2) designee |
| Privacy Officer and Section 1557 Coordinator | Quality and Compliance Manager | Privacy Rule, breach determinations, 45 CFR 92.7 and 92.210 |
| Clinical downtime lead | Director of Nursing | Downtime procedures; diversion decision with the CEO and ED physician |
| Emergency Preparedness Coordinator | Facilities Manager | 42 CFR 485.625 program; building OT |
| Medical device owners | Imaging Manager, Laboratory Manager, Facilities Manager (biomed contract) | Device inventory, patching with manufacturers |
| Operations support | Managed service provider (business associate) | Network and server administration, patching, EDR console |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199 and reflect this hospital's use, not the provisional values alone.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Health care delivery services (patient records, orders, medication administration) | Moderate | **High** | Moderate | Disclosure harms patients and triggers breach duties (serious, not catastrophic). Altered orders, doses, allergies, or drug-library limits could cause death (catastrophic), so integrity is High. Downtime procedures and transfer agreements keep care going, so loss of availability is serious rather than catastrophic (P05 MTD 4 h for ED and inpatient support) |
| Health care administration (claims, eligibility) | Moderate | Moderate | Low | Financial and identity data; payers accept late claims (P05 MTD 72 h) |
| Public health monitoring (reportable results) | Moderate | Moderate | Low | Late reporting has limited direct harm; results can be phoned |
| Human resources management (workforce identities) | Moderate | Low | Low | Account data; limited harm if unavailable |
| **HCIS category (high-water mark)** | **Moderate** | **High** | **Moderate** | Overall: **High** |

**Baseline:** the NIST SP 800-53B **High** baseline, tailored for a 60-person critical access hospital. The plan documents 80 controls that implement the HIPAA Security Rule, the information aspects of the CMS emergency preparedness condition, and the HHS CPGs (see `control-implementation.csv`). Every other High-baseline control and enhancement is handled in one of three ways:
- **Inherited** from the EHR vendor, the identity provider, and the cloud provider, as evidenced by their SOC 2 reports (P09).
- **Deferred**, with a tailoring decision recorded here and revisited at the 2027 review. The High baseline enhancements for account management, audit, and contingency planning (for example, automated account actions and alternate processing sites) are largely deferred because the hospital first needs the base controls that are Partially implemented today.
- **Out of scope for this tier**, where the control's purpose applies only to federal systems. Examples: PM-series program controls beyond PM-2 and PM-9.

The CSF 2.0 column in `control-implementation.csv` lists up to three subcategories from NIST's official CSF 2.0 to SP 800-53 crosswalk (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`). Where NIST lists none for a control, the column gives an author mapping labeled as such.

## 7. Authorization Boundary Description
The boundary was drawn from the intake [asset inventory](../step-00_P00_intake/asset-inventory.csv). It contains hospital-managed components and the hospital's configuration of vendor services:
- **Inside:** the EHR tenant configuration, user roles, and sepsis model settings; the identity provider tenant; the cloud tenant (3 workloads); the hospital network, phones, and server room; 88 desktops and workstations on wheels, 12 laptops, 16 barcode scanners, and 2 downtime PCs; and the medical devices listed in section 9.
- **Outside (external services, interconnected):** the EHR vendor's platform, the cloud provider's infrastructure, the clearinghouse, teleradiology group, telepharmacy service, reference laboratory, HIE, state health department, and cloud fax service.
- **Outside, same network (separate system):** building and clinical OT (SYS-08), owned by the Facilities Manager. It shares the flat network today, which is why segmentation is the first major modification. It is covered in P01 and P04.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| EHR vendor (SYS-01) | Bidirectional (VPN and TLS) | All clinical and billing data | BAA; contract; SOC 2 Type 2 |
| Clearinghouse (SYS-09) | Bidirectional | Claims, eligibility, remittance | BAA; contract |
| Teleradiology group (SYS-10) | Outbound images, inbound reports | CT and X-ray studies, reads | BAA. **Support VPN uses a shared account without MFA (gap)** |
| Telepharmacy service (SYS-11) | Remote access into the EHR | Medication orders | BAA; named accounts with MFA |
| Reference laboratory (SYS-12) | Bidirectional (HL7 via interface engine) | Send-out orders and results | BAA |
| HIE (SYS-12) | Bidirectional | Care summaries | BAA; participation agreement |
| State health department (SYS-12) | Outbound | Electronic laboratory reports, immunizations, syndromic surveillance | Public health reporting (permitted disclosure); state onboarding agreement |
| Cloud fax service (SYS-14) | Bidirectional | Records requests, transfer documents | **No BAA (gap)** |
| Biomedical service contractor | Physical access to devices | Device data at rest | **No BAA (gap)** |
| MSP | Remote administration | All hospital-managed systems | BAA. Shared technician admin account (gap) |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| EHR tenant and sepsis model settings | SaaS | EHR vendor | CEO (system owner); Chief of Medical Staff (model) |
| Identity provider tenant and directory sync | SaaS and on-premises server | Identity vendor; server room | IT Manager |
| Imaging archive and viewer | Cloud virtual machines and object storage | Cloud tenant | Imaging Manager |
| Interface engine | Cloud virtual machine | Cloud tenant | IT Manager |
| Backup vault | Cloud backup service | Cloud tenant (production account, **gap**) | IT Manager |
| Local backup appliance | On-premises appliance | Server room (joined to directory, **gap**) | IT Manager |
| Firewall, core switch, Wi-Fi, VoIP phone system | Network | Server room and hospital | IT Manager |
| Virtualization host (directory, file, print, analyzer middleware, dispensing cabinet server, pump drug-library server) | On-premises server | Server room | IT Manager |
| Desktops and workstations on wheels (88), laptops (12), barcode scanners (16), downtime PCs (2) | Endpoint | Hospital | IT Manager |
| CT scanner and acquisition workstation; digital X-ray | Medical device | Imaging | Imaging Manager |
| Infusion pumps (14), patient monitors and central station | Medical device | ED and inpatient unit | Facilities Manager (biomed contract) |
| Chemistry and hematology analyzers; point-of-care glucose meters | Medical device | Laboratory | Laboratory Manager |
| Automated dispensing cabinets (2) | Medical device | ED and inpatient unit | Director of Nursing |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 80 controls:
- Implemented: 17
- Partially implemented: 51
- Planned: 12
- Not applicable: 0

By inheritance: 60 system-specific, 16 hybrid, 4 common/inherited.

### 10.2 Control assessment status
22 of these controls were assessed 2026-08-03 to 2026-08-07. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
- **Employees and contracted clinicians off site:** password plus a phone authenticator app through the identity provider, for email, remote access, the EHR from outside the hospital, and the cloud console.
- **Administrators:** hardware security keys (phishing-resistant).
- **On-site EHR sign-in:** password only today. This is below what the High integrity categorization calls for, because a shared or stolen password could be used to enter orders. Badge-tap plus PIN is being evaluated as a second factor that works at the bedside without slowing care (POAM-011).
- **Vendors:** named accounts with MFA through the identity provider are required by POL-02; the teleradiology support account does not yet comply (POAM-008).

Patients use the EHR vendor's portal with its own identity proofing and MFA. That is governed by the vendor and outside this boundary.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), intake evidence, inventories and obligations register ([step-00](../step-00_P00_intake/intake-report.md)), risk register (P01), gap analysis and CPG benchmark (P03), cloud control map (P04), BIA (P05), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 self-benchmark and vendor report review (P09), AI assessment (P10), and the hospital's emergency preparedness plan (42 CFR 485.625).

## 13. Acronym List and Glossary
- **BAA:** business associate agreement
- **CAH:** critical access hospital
- **CPG:** Cybersecurity Performance Goal (HHS, voluntary)
- **EDR:** endpoint detection and response
- **eMAR:** electronic medication administration record
- **EMTALA:** Emergency Medical Treatment and Labor Act
- **HCIS:** Hospital Clinical Information System
- **MDS2:** Manufacturer Disclosure Statement for Medical Device Security
- **MSP:** managed service provider
- **OT:** operational technology (building and clinical systems)
- **POA&M:** plan of action and milestones

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan | IT Manager |
