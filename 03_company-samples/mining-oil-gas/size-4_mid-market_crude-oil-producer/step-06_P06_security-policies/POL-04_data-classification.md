# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Owner | General Counsel, with the Security Manager |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-16 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-3, AC-6, MP-6, SC-8, SC-12, SC-28, CP-6, CP-9, CM-8, SA-9, SI-12 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| Benchmark (N21-BM) | SP 800-82 Rev. 3 sections 6.1.1 (asset management), 6.2.3 (data security), 6.2.4 (backups), 6.2.7 (media) |
| Binding rules referenced | Fla. Stat. 501.171(2) (reasonable security measures); 49 CFR 195.11(d) (record retention) |
| Supporting standards | STD-01 Secure configuration, network, and encryption standard; STD-07 Backup and recovery standard; STD-05 AI use standard |

## 1. Purpose
Classify company information by sensitivity and set handling rules, so that protection matches the harm a disclosure, alteration, or loss would cause.

## 2. Scope
All information the company creates, receives, maintains, or transmits, in any form and in every system, including data held by vendors, controller programs and SCADA configurations, and data on field devices.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| General Counsel | Owns this policy; decides classification disputes; approves new external sharing of Restricted data |
| Security Manager | Keeps the Restricted data inventory; runs data discovery scans |
| Data owners | Production Accounting Director (royalty owner, production, and revenue data); HR Director (employee data); Measurement Supervisor (LACT tickets and shipper data); Reservoir Engineering Manager (seismic and reservoir data); SCADA and Automation Manager (controller programs, SCADA configuration); Pipeline Compliance Manager (pipeline safety records) |
| VP IT | Encryption, backup, and disposal controls for IT and cloud |
| SCADA and Automation Manager | Backup and disposal controls for OT |
| All workforce | Label and handle information according to this policy |

## 4. Policy statements
4.1 Information must be classified in one of four levels. (RA-2; ID.AM-07)

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Royalty owner and employee personal information (Social Security and taxpayer numbers, bank account details, driver license and health plan numbers); credentials; SCADA configurations, controller programs, shutdown logic, MOP settings, and segment identification records; seismic and reservoir data (trade secret) | Encrypted at rest and in transit; access by named role with data owner approval; approved systems only |
| **Confidential** | Shipper volumes and crude quality data; LACT and run tickets; production and revenue data; partner billing; contracts; security documents; vehicle location history | Encrypted in transit; need-to-know |
| **Internal** | Procedures, schedules, internal announcements | Workforce and authorized contractors only |
| **Public** | Website, published reports | No restriction |

4.2 Restricted data must be encrypted at rest and in transit. Restricted data must leave the company only through an approved secure transfer service; password-protected email attachments are not an approved method. Where OT equipment cannot encrypt (older RTUs and the licensed radio network), the exception must be documented with compensating controls under POL-01 4.10. (SC-28; SC-8; PR.DS-01; PR.DS-02)
4.3 **Data minimization.** Social Security and taxpayer numbers may be stored only in production accounting, HR and payroll, and the backup account. Analytics and engineering copies must use de-identified extracts. The full owner deck copy in the data platform must be replaced by a de-identified extract by 2026-11-30. (AC-3; AC-6; PR.DS-01)
4.4 The Security Manager must keep an inventory of where Restricted data is stored and which vendors receive it, reconciled each quarter with a data discovery scan for Social Security numbers. The OT Security Engineer must keep the OT asset inventory, including controller and flow computer configurations, and complete it for South Florida and Alabama by 2027-06-30. (CM-8; ID.AM-07)
4.5 **Disposal.** Media and devices holding Restricted or Confidential data must be sanitized (for reuse) or destroyed by a vendor that provides a certificate (for disposal). This includes retired RTUs, PLCs, HMIs, flow computers, modems, and gateways, which must have configurations and passwords wiped before they leave company control. Paper records with personal information must be shredded. The company applies these rules to all records containing personal information, consistent with the disposal standard in Fla. Stat. 501.171(8), although that subsection reaches customer records and the company has no consumer customers. (MP-6; ID.AM-08)
4.6 **Backups.** Cloud workloads must be backed up to the separate backup account in a second region with write-once retention. SCADA server images and controller programs must be kept offline in two locations, at least one with no network path, and restore-tested each quarter (STD-07). (CP-9; CP-6; PR.DS-11)
4.7 Encryption keys for cloud workloads and backups must be managed in the company's key management service, with separate keys for the backup account and annual rotation. (SC-12)
4.8 **Shipper data.** Each shipper may see only its own volumes, quality, and statements. Shipper data must not be shared with another shipper or used for any purpose outside the gathering agreement. (AC-3; PR.DS-01)
4.9 Restricted and Confidential data must not be entered into AI tools unless the tool is approved under STD-05 for that data level, and the vendor's terms prohibit training on company data (P10). (SA-9; PR.DS-01)
4.10 Records are retained according to the records retention schedule. Security documentation is retained under POL-01 4.14, and gathering system records under 49 CFR 195.11(d). (SI-12)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.8). Compliance is checked through the annual independent control assessment (P07), the quarterly data discovery scans, and destruction certificates.

## 6. Exceptions
Exceptions follow POL-01 section 4.10.

## 7. Related documents
POL-01; POL-02; POL-05; STD-01; STD-05; STD-07; P04 cloud architecture; P10 approved-tools list; records retention schedule
