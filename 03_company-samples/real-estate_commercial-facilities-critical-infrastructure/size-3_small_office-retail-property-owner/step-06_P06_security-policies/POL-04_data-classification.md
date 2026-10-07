# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Chief Operating Officer |
| Approved by | Chief Operating Officer |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-4, MP-6, SC-8, SC-28, SI-12, CP-9, CP-4, CM-8 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| CISA CPG 2.0 (voluntary) | 2.A, 3.K, 3.O |
| Other drivers | Fla. Stat. 501.171(2) and (8); PCI DSS v4.0.1 Req. 3.2.1, 3.3.1.2, 9.4 (SAQ P2PE) |

## 1. Purpose
Classify company information by sensitivity and set handling rules, so protection matches the harm that disclosure, tampering, or loss would cause to tenants, visitors, employees, and building operations.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, and contractors) and vendors who handle company information. Covers information in every form: electronic, paper, video, and building system configurations.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Operating Officer | Owns classification; approves new uses of Restricted data |
| Data owners (Security Manager, Director of Engineering, Controller, HR Manager) | Classify their data; set and enforce retention |
| IT Manager | Implements encryption, backup, and disposal controls |
| All workforce | Label and handle information according to this policy |

## 4. Policy statements
4.1 Information must be classified in one of four levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Visitor driver license and ID scans; employee Social Security numbers; tenant and employee bank details; credentials and OT passwords; any face template or other biometric data (none collected today) | Encrypted at rest and in transit; need-to-know; approved systems only; retention limits in 4.6 |
| **Confidential** | Tenant employee badge records, photos, and access history; video recordings; BAS programs, network diagrams, and security system layouts; leases; security documents | Encrypted in transit; need-to-know; shared outside the company only with named accounts |
| **Internal** | Building schedules, work orders, procedures | Workforce and approved contractors only |
| **Public** | Leasing brochures, website | No restriction |

(RA-2; ID.AM-07)
4.2 Restricted data must be encrypted at rest on every device and service, including laptops, tablets, and NVR disks where the device supports it, and encrypted in transit. (SC-28; SC-8; PR.DS-01; PR.DS-02; CPG 3.K)
4.3 **Card data.** Card numbers and security codes may be entered only into the company's P2PE payment terminals. They must never be written on paper, typed into any computer, emailed, or recorded. Card data received by email must be deleted from the mailbox and deleted items, and the sender told to use the terminal or an invoice link from the processor. (PCI DSS 3.2.1, 3.3.1.2, 9.4; SAQ P2PE eligibility)
4.4 The IT Manager must keep an inventory of where Restricted and Confidential data is stored and which vendors receive it, and an OT asset inventory of every BAS, access control, and video device, updated at least quarterly. (CM-8; ID.AM-07; CPG 2.A)
4.5 Media and devices holding Restricted or Confidential data (including NVR drives and retired controllers) must be wiped for reuse or destroyed by a vendor that provides a certificate of destruction. Paper records with personal information must be cross-cut shredded. (MP-6; ID.AM-08; Fla. Stat. 501.171(8))
4.6 **Retention.** Data owners must keep data only as long as needed:

| Data | Retention |
|---|---|
| Visitor ID images and photos | 30 days after the visit |
| Visitor logs (name, host, time) | 1 year |
| Video recordings | 30 days, unless preserved for an incident, claim, or law enforcement request |
| Access control event history | 1 year |
| Tenant employee badge records | Deleted within 30 days after the badge is deleted (POL-02 4.6) |
| Security logs | At least 1 year (POL-03 4.9) |

(SI-12; Fla. Stat. 501.171(8))
4.7 **Backups.** Backups of the BAS server, BAS field controller programs and graphics, the historian, and file storage must be encrypted, kept in a separate account with immutable retention, and restore-tested each quarter. The integrator must deliver current controller programs and graphics to the company after every change. (CP-9; CP-4; PR.DS-11; CPG 3.O)
4.8 Restricted and Confidential data must not be entered into AI tools or enabled for new analytics features unless the use is on the approved AI list (POL-05 4.8, P10). (SA-9)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.7). Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07) and the quarterly retention checks by data owners.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months.

## 7. Related documents
POL-01; POL-05; P10 approved AI list; the P2PE Instruction Manual; Fla. Stat. 501.171
