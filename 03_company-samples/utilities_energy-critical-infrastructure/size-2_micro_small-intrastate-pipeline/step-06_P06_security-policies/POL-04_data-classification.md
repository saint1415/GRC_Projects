# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Office Manager (security program coordinator), with the Operations Manager for SCADA information |
| Approved by | Owner, 2026-09-15 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-15), and after major changes or a TSA designation |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-3, CM-8, CP-9, CP-4, SC-8, SC-28, SA-9, MP-3, MP-6, SI-12 |
| CSF 2.0 | ID.AM-01, ID.AM-02, ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-11 |
| Pipeline safety link | 49 CFR 192.605(b)(3) (maps and records available to operating personnel); 192.631(j) (records) |

## 1. Purpose
Sort company information by the harm its disclosure, change, or loss could cause, and set simple handling rules for each level. For a pipeline, the information that would help someone send a false command or hide a leak is the most sensitive.

## 2. Scope
All employees, contractors, and vendors, and all company information in any form: in SCADA, the productivity suite, accounting, on laptops and tablets, on paper, on removable media, and in any vendor's system.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Office Manager | Owns this policy; keeps the list of SaaS services and where Restricted information lives; approves new tools |
| Operations Manager | Protects SCADA configurations, credentials, and field device information; keeps the PSGCS inventory and configuration copies |
| MSP | Encryption, backup, restore tests, and device wiping, as directed |
| All staff | Handle information according to its level |

## 4. Policy statements
4.1 Company information has three levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | SCADA credentials and MFA recovery codes; SCADA configuration exports and RTU programs; gateway and device passwords; SIM lists; network diagrams; security assessments and this program's gap and risk details; employee Social Security and bank numbers | Approved locations only (4.2); encrypted at rest and in transit; named access; never in email to outside parties unless encrypted; never in any AI tool |
| **Internal** | Pipeline maps and alignment sheets, O&M manual, emergency plan, customer contracts, volumes, nominations, payroll summaries | Staff and approved contractors only, by named access; encrypted in transit |
| **Public** | Website, public awareness brochures, emergency contact number | No restriction |

When unsure, treat information as Restricted. (RA-2; ID.AM-07)

4.2 Restricted information may be kept only in: the SCADA tenant; a restricted folder in the productivity suite with named access; encrypted removable media in the office safe; and, for RTU programs, the Operations Manager's encrypted laptop. (AC-3; PR.DS-01)

4.3 Restricted information must be encrypted wherever it is stored and whenever it leaves the company's systems. Every laptop and tablet must use full-disk encryption. (SC-28; SC-8; PR.DS-01; PR.DS-02)

4.4 **Inventory.** The Operations Manager keeps a one-page PSGCS inventory (every field device with its firmware version, every gateway with its SIM number and private-network status). The Office Manager keeps the list of SaaS services and where Restricted information is stored. Both are updated when anything changes. (CM-8; ID.AM-01; ID.AM-02)

4.5 **Backups.** The Operations Manager must export the SCADA configuration and copy the RTU programs to encrypted media in the office safe every quarter and after any significant change. The productivity suite must be backed up nightly with versions kept at least 90 days in storage that cannot be changed or deleted in that period. The MSP restores a sample each quarter and gives the Office Manager a written result. (CP-9; CP-4; PR.DS-11)

4.6 **Sharing.** Internal and Restricted information is shared with contractors only through named access to a specific folder, never by open link, and the access is removed when the job ends. (AC-3; PR.DS-01)

4.7 **AI tools.** Restricted information must never be entered into any AI tool. Internal information may be used only in AI tools on the approved list. Today the list has one entry: the SCADA vendor's leak-detection module, as an advisory tool under the P10 conditions. Public AI chatbots must not receive Restricted or Internal information. (SA-9; PL-4)

4.8 **Disposal.** Devices and media that held Restricted information must be wiped before reuse or destroyed by a vendor that gives a certificate. Field devices are reset to clear configurations and passwords before they leave company control. (MP-6)

4.9 **If TSA designates the pipeline.** Plans, assessments, and reports required by a TSA Security Directive become Sensitive Security Information under 49 CFR Part 1520. On designation they must be marked and handled under Part 1520, in the restricted folder, and shared only with people who have a need to know. (MP-3; AC-3)

4.10 **Retention.** O&M, control room management, and incident records follow 49 CFR Parts 191 and 192 and FPSC rules. Security records follow POL-02 A.7. (SI-12)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.10. Compliance is checked through the quarterly backup and restore records, the monthly MSP report, and the annual assessment (P07).

## 6. Exceptions
Exceptions follow POL-02 A.9.

## 7. Related documents
POL-02; POL-03; PSGCS inventory; P04 cloud control map; P10 AI risk assessment; O&M manual
