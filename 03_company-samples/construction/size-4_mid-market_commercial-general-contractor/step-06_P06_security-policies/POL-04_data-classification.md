# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Owner | Director of Contracts and Compliance (classification); IT Director (technical handling) |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after new CUI contracts, major changes, or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-4, AC-20, MP-1, MP-2, MP-3, MP-4, MP-5, MP-6, SC-8, SC-13, SC-28, SI-12, CP-9, SA-9 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| Federal contract requirements | FAR 52.204-21(b)(1)(iii), (vii), (b)(2) (N23-R01); DFARS 252.204-7012(b)(2) and SP 800-171 Rev. 2 families 3.1.3, 3.1.20, 3.8, 3.13.11 (N23-R03); DFARS 252.204-7021(d)(2) (N23-R04) |
| Supporting standards | STD-08 Encryption; STD-09 CUI handling |

## 1. Purpose
Classify company information by sensitivity and set handling rules, so that CUI stays in the CUI Project Enclave, FCI stays in systems that are assessed for it, and other sensitive data gets protection that matches the harm a disclosure would cause.

## 2. Scope
All workforce members, all company systems, paper records, and devices, in every location. Subcontractors that receive CUI or FCI are bound by their subcontracts (POL-01 4.12).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Contracts and Compliance | Owns classification; identifies FCI and CUI requirements in each contract; keeps the approved external systems list with the IT Director |
| FC-4 Project Executive | CUI custodian for FC-4: intake, distribution list, marking checks, printed CUI control |
| IT Director | Encryption, backup, data-movement controls, and disposal |
| Director of Technology and Security Systems | Custodian of client facility security details |
| All workforce | Handle information according to this policy |

## 4. Policy statements
4.1 Information must be classified in one of six levels:

| Level | Examples | Handling |
|---|---|---|
| **CUI** | Government-furnished CUI drawings and specifications; A&E CUI design packages; CUI RFIs and submittals on FC-4 | Only in the CPE (email, files, virtual desktops) or printed under 4.6; never in SYS-01, the corporate suite, personal accounts, or any AI tool |
| **Restricted** | Client facility security details; bank details; Social Security numbers and payroll; passwords and keys | Approved system only (credential vault, ERP, payroll system); encrypted; named need-to-know |
| **Federal (FCI)** | Non-CUI drawings, submittals, schedules, daily logs, pay apps, and certified payrolls for federal contracts | Only inside the PDPP; never in personal accounts or unapproved tools |
| **Confidential** | Bid and pricing data; private owners' drawings; contracts | Need-to-know; never shared with competitors |
| **Internal** | Procedures, schedules, safety plans | Workforce and project team only |
| **Public** | Approved website content, marketing | No restriction |

(RA-2; ID.AM-07)
4.2 **CUI intake.** CUI may be accepted only under a contract whose CUI requirements the Director of Contracts and Compliance has reviewed and only into the CPE. Anyone who receives a document marked CUI outside the CPE must stop, must not forward it, and must report it under POL-03 4.2. The CUI custodian must move it into the CPE and the Security Manager must treat the event as a possible incident (POL-03 4.5). (MP-3; AC-4; FAR 52.204-21(b)(2))
4.3 **CUI flow.** CUI must not leave the CPE except to people on the FC-4 distribution list, through CPE sharing to allow-listed domains or CPE guest accounts. Download, clipboard transfer, and drive mapping from enclave virtual desktops are blocked. CUI RFIs and submittals use the CPE workflow, not SYS-01. (AC-4; SP 800-171 Rev. 2 3.1.3)
4.4 **Approved external systems.** The approved external systems list names which systems may hold each level. For CUI: the CPE and subcontractor systems verified under POL-01 4.12. For FCI: SYS-01, SYS-02, SYS-03, SYS-05, owners' portals, and federal portals. Personal email, personal cloud storage, and personal devices are prohibited for CUI, FCI, Restricted, and Confidential data. Automatic forwarding to external addresses is blocked. (AC-20; FAR 52.204-21(b)(1)(iii); SP 800-171 Rev. 2 3.1.20; DFARS 252.204-7021(d)(2))
4.5 CUI must be protected with FIPS-validated cryptography at rest and in transit. Restricted and FCI data must be encrypted at rest on every device and encrypted in transit. (SC-8; SC-13; SC-28; SP 800-171 Rev. 2 3.13.11)
4.6 **Printed CUI.** Printing is allowed only to the FC-4 project office printer and the CUI room printer at the FC-4 trailer. Printed sets must be marked, numbered, signed out, kept in the badge-locked CUI room or a locked cabinet when not in use, carried in a sealed envelope or locked case between sites, and destroyed in a locked shred bin serviced by a certified shredding vendor with certificates. (MP-2; MP-3; MP-4; MP-5; MP-6; SP 800-171 Rev. 2 3.8.1 to 3.8.5)
4.7 **Marking.** The CUI custodian must check markings on every CUI design package received from the A&E firm before distribution; unmarked CUI is returned for marking. (MP-3; SP 800-171 Rev. 2 3.8.4)
4.8 Media and devices that held CUI, FCI, or Restricted data must be sanitized before disposal, return to a lessor, or reuse; disposal requires a certified vendor that provides a certificate of destruction. Every sanitization must be recorded. (MP-6; ID.AM-08; FAR 52.204-21(b)(1)(vii))
4.9 Backups must be encrypted, stored apart from production (a separate account and region, or a separate backup service for the CPE), protected from alteration, and restore-tested at least quarterly for High-criticality processes. (CP-9; PR.DS-11)
4.10 CUI must not be entered into any AI tool. FCI, Restricted, and Confidential data may be entered only into AI tools approved under P10 with terms that bar training on company data. (AC-20; SA-9)
4.11 Client facility security details must be kept in the credential vault under the client's project or MBSS site. They must be handed to the client at the end of warranty (unless an MBSS agreement continues) and then deleted from company systems. (AC-3)
4.12 Records must be retained under the retention schedule, including 6 years for security and SPRS evidence and 3 years after completion for certified payroll records (POL-01 4.16). (SI-12)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.18. Compliance is checked through the annual control assessment (P07), quarterly content searches of SYS-01 and the corporate suite for CUI markings, and CUI room inspections.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. No exception may allow CUI outside the CPE.

## 7. Related documents
POL-01; POL-03; POL-05; STD-08; STD-09; P02 boundary (section 7); P10 approved AI tools; records retention schedule; FC-4 CUI distribution list
