# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Office Manager (Security Coordinator), with the Owner for formulations |
| Approved by | Owner and President, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes |
| Implements (SP 800-53 Rev. 5) | RA-2, CM-8, MP-6, SC-8, SC-28, CP-9, CP-4, SA-9, SI-12, AC-3 |
| CSF 2.0 | ID.AM-01, ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| Benchmarks and rules | C-CHEMICAL-R01 (6 CFR 27.400 CVI, legacy; 27.230(a)(8), voluntary benchmark); 49 CFR 172.201(e); 172.704(d); Fla. Stat. 501.171 |

## 1. Purpose
Sort company information by how much harm its loss, change, or disclosure would cause, and set simple handling rules for each level.

## 2. Scope
Everyone who works for the company and all company information in any form: in SaaS services, on the HMI PC and PLC, on computers and USB sticks, on paper, and in any vendor's system.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Owner and President | Owns formulations and the CVI file; approves sharing of Restricted information outside the company |
| Office Manager | Owns this policy; keeps the inventory; approves new tools |
| Operations Manager | Keeps recipe and HMI backups; owns the offline backup drive |
| MSP | Encryption, office backup, restore tests, and device wiping, as directed |
| Everyone | Handle information according to its level |

## 4. Policy statements
4.1 Company information has three levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Formulations and HMI recipes; the PLC program and HMI project; network diagrams and OT passwords; the legacy CFATS Top-Screen file (CVI); employee personal information | Only in approved places (4.3); encrypted at rest and in transit where the system allows; shared outside the company only with the Owner's approval and a named recipient; never in personal accounts or public AI tools |
| **Internal** | Customer lists and prices, contracts, shipping records, SDS drafts, security documents other than those above | Employees and approved vendors only; encrypted in transit |
| **Public** | Published SDSs, product sheets, the website | No restriction |

Published SDSs are Public by design: customers and responders must have them. A formulation behind an SDS is Restricted. When unsure, treat information as Restricted. (RA-2; ID.AM-07)

4.2 Restricted information is encrypted wherever it is stored on a laptop or desktop and whenever it leaves company systems. The HMI PC is protected by its location, named logins, and the network segment until its replacement in 2027. (SC-28; SC-8; PR.DS-01; PR.DS-02)

4.3 Restricted information may be kept only in: named folders in the shared drive; the HMI PC and PLC; the offline backup drive in the Owner's safe; the cloud backup; and the payroll service (employee data). **The CVI file stays on paper in the locked cabinet and is never scanned.** (AC-3; 27.400(d))

4.4 The Office Manager keeps a one-page inventory of every device (including the PLC, HMI PC, and gateway), every SaaS service, every connection, and every place Restricted information is stored, and updates it when anything changes. (CM-8; CA-9; ID.AM-01)

4.5 Restricted information shared with a customer or vendor goes through a named guest account or an encrypted file, under a confidentiality agreement. "Anyone with the link" sharing is not allowed for Restricted or Internal information. (AC-3; GV.SC-05)

4.6 **AI tools.** Company information may be entered only into AI tools on the approved list, which the Office Manager keeps:
- **AI-001**, the integrator's batch-optimization feature, may receive T-1 process data under the P10 conditions. Write-back to the PLC stays off.
- **AI-002**, the SDS service's drafting assistant, is not approved until its assessment is done.
- **Public AI chatbots** must never receive Restricted or Internal information.

(SA-9; PL-4)

4.7 **Backups.**
- The productivity suite is backed up daily, with versions kept at least 90 days in storage that cannot be changed or deleted in that period. The MSP restores a sample every quarter and gives the Office Manager a written result.
- The Operations Manager exports the recipes and HMI project weekly and after every approved change to the offline drive in the Owner's safe and to the cloud backup.
- The integrator delivers a current copy of the PLC program, with checksums, after every change.
- The OT backup is restored to the spare panel PC and a bench PLC once a year.

(CP-9; CP-4; PR.DS-11)

4.8 **Disposal.** Devices, drives, and USB sticks that held Restricted information are wiped before reuse or destroyed by a vendor that provides a certificate. Paper with Restricted information goes in the locked shred bin. The Office Manager keeps each record. (MP-6; ID.AM-08)

4.9 **Retention.**
- Hazmat shipping papers: 2 years after acceptance by the initial carrier (49 CFR 172.201(e)).
- DOT hazmat training records: the preceding 3 years, and 90 days after the employee leaves (172.704(d)). A scanned copy of the training binder is kept in the shared drive.
- Security documents: 3 years (POL-02 A.7).
- Incident records: 5 years.
- The legacy CVI file: kept while CFATS remains lapsed.

(SI-12; GV.PO-02)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Compliance is checked through the monthly MSP report, the quarterly restore results, the backup log, and the yearly assessment (P07).

## 6. Exceptions
Exceptions follow POL-02 A.9.

## 7. Related documents
POL-02; POL-03; inventory; P04 cloud control map; P10 AI risk assessment
