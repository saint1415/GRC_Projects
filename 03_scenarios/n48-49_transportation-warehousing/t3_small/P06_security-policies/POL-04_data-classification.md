# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Security and Safety Manager (FSO) |
| Approved by | General Manager |
| Effective date | 2026-09-04 |
| Review cycle | Annually (next review 2027-09-04), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-3, MP-6, AC-3, SC-8, SC-28, CM-8, CP-9, AU-9, AU-11, SI-12 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| USCG cyber rule (N48-49-R01) | 33 CFR 101.630(b), 101.650(b)(3), 101.650(c)(1)-(2), 101.650(g)(4) |

## 1. Purpose
Classify terminal information by sensitivity and set handling rules so that protection matches the harm a disclosure or alteration would cause.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, temporary staff and contractors), plus longshore labor and vendor technicians whenever they use company IT or OT. Covers every system and data set at the Florida terminal, including the cloud tenant, SaaS services, crane and yard equipment controllers (OT), and systems that vendors operate or support for the company.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Security and Safety Manager (FSO) | Owns classification; controls SSI storage and access |
| IT Manager (proposed CySO) | Implements encryption, backup, logging and disposal controls; keeps the system inventory |
| Operations Manager | Owner of TOS, cargo and customs data |
| All workforce | Label and handle information according to this policy |

## 4. Policy statements
4.1 Information must be classified in one of five levels:

| Level | Examples | Handling |
|---|---|---|
| **Sensitive security information (SSI)** | Facility Security Plan and Assessment, Cybersecurity Plan and its drafts, network maps, vulnerability and assessment reports, TWIC reader records (33 CFR 105.225(c)) | Marked as SSI; disclosed only to covered persons with a need to know; stored in the FSO's controlled repository (49 CFR part 1520) |
| **Restricted** | Personal information of employees and truck drivers (for example Social Security, driver license and account numbers), credentials | Encrypted at rest and in transit; approved systems only |
| **Confidential** | Cargo, customs release and hold status, bills of lading, bay plans, hazardous cargo location, TOS data, contracts | Encrypted in transit; need-to-know |
| **Internal** | Schedules, procedures | Workforce only |
| **Public** | Vessel schedule published by the port, website | No restriction |

(RA-2; MP-3; ID.AM-07; 101.630(b))
4.2 SSI must be marked, stored only in the FSO's repository or an SSI-restricted folder, and shared only with covered persons who need it. Documents that will become part of the Cybersecurity Plan, including P01 to P10, are handled as SSI now. (MP-3; AC-3; 101.630(b))
4.3 Restricted and Confidential data must be encrypted in transit. EDI and file transfers with partners must use AS2, SFTP or TLS; plain FTP is prohibited. Traffic to and from OT must be encrypted where technically feasible. Restricted data must be encrypted at rest on laptops, servers and cloud storage. (SC-8; SC-28; PR.DS-01; PR.DS-02; 101.650(c)(2))
4.4 Restricted, Confidential and SSI data may be stored only in approved systems: the TOS, the cloud tenant, the productivity suite and the FSO repository. It must never be kept on personal devices, personal cloud accounts or unapproved USB media. (AC-3)
4.5 The CySO must keep an inventory of network-connected systems, including which are critical IT or OT systems, and of where Restricted and SSI data is stored. (CM-8; ID.AM-07; 101.650(b)(3))
4.6 **Backups.** Critical IT and OT systems (the TOS database, gate server and OCR images, network device configurations, PLC programs and HMI settings) must be backed up, stored apart from production (a separate cloud account or offline), protected from alteration, and restore-tested at least quarterly. (CP-9; PR.DS-11; 101.650(g)(4))
4.7 Logs must be captured centrally, protected so that only privileged users can access them, and kept for at least 1 year. (AU-9; AU-11; 101.650(c)(1))
4.8 Media and devices that held Restricted, Confidential or SSI data must be wiped for reuse, or destroyed by a certified vendor that provides a certificate of destruction. (MP-6; ID.AM-08)
4.9 Restricted, Confidential and SSI data must not be entered into AI tools or other third-party services unless the tool is approved (P10 and POL-05). (AC-3)
4.10 Records are kept according to POL-01 4.10 and the FSP record rules. (SI-12)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement in POL-01 section 4.7. Sanctions range from retraining to termination of employment or of a contract, depending on intent and harm. For longshore labor, the company may refuse further access to its systems and refer the matter to the hiring hall. Compliance is checked through the annual control assessment (P07), the Cybersecurity Assessment (33 CFR 101.650(e)(1)) and the reviews in this policy set.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months. Where a Subpart F measure is not technically feasible, the compensating control must be documented for the Cybersecurity Plan.

## 7. Related documents
POL-01; POL-05; Facility Security Plan (SSI); 49 CFR part 1520; P10 approved AI tools list
