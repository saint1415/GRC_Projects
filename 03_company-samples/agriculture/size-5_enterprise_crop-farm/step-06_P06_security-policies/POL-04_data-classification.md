# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Chief Privacy Officer |
| Approved by | Executive risk committee |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | RA-2, SC-8, SC-28, SI-7, AU-10, AU-9, MP-6, CP-9, SI-12 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-11 |
| Regulatory and guidance drivers | CSF 2.0 (benchmark); 21 CFR 112.161-112.166; 21 CFR 1.1455; 20 CFR 655.122(j); 40 CFR 170.311(b); Fla. Stat. 501.171(2) and (8) |

## 1. Purpose
Classify company, worker, grower, and customer information, protect it in proportion to its sensitivity, and keep regulatory records (Produce Safety, traceability, H-2A, and Worker Protection Standard) accurate, attributable, retained, and producible on time.

## 2. Scope
All Cris Santos Company workforce members (year-round employees, seasonal and H-2A workers, contractors, and integrator and vendor staff working on company systems) at the 48 farms, 17 packing sites, 6 irrigation control centers, offices, and both data center campuses in Florida, Georgia, South Carolina, and North Carolina, including acquired operations from their acquisition date. Covers all systems and data, including cloud, data centers, SaaS, operational technology (irrigation, fertigation and chemigation, packing, cold-chain, and drying controls), drones and equipment telematics, systems that vendors operate for the company, and the services offered to external growers (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Privacy Officer | Owns classification and personal information handling |
| Chief Compliance Officer | Owns STD-04.4 and the regulator records request procedure |
| Chief Food Safety and Quality Officer | Produce Safety and traceability records |
| Director of H-2A and Labor Compliance | H-2A earnings records and statements |
| Data owners | Classify data in their systems and approve access |
| Chief Information Officer | Backups and the records platforms |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested a mapped control in 2026 (P07).

4.1 Information must be classified as Restricted (Social Security, passport, visa, and bank account numbers, payroll files, credentials, and OT command and safety configurations), Confidential (grower data, yields, contracts, financial, legal, security, and material nonpublic information), Internal, or Public, and labeled where systems allow. (RA-2; ID.AM-07)
4.2 Restricted and Confidential data must be encrypted at rest and in transit using STD-04.1. Where a legacy OT protocol cannot be encrypted, it must run only on a private network segment under an approved exception. (SC-28; SC-8; PR.DS-01)
4.3 Regulatory records (Produce Safety, traceability, H-2A earnings, and Worker Protection Standard records) must be created at the time of the activity, attributable to the person who did the work, protected from undetected change, and kept with an audit trail of edits. (SI-7; AU-10; PR.DS-01)
4.4 Regulatory records must be producible within the legal time limits: 24 hours for offsite Produce Safety records and for Food Traceability Rule records (including the electronic sortable spreadsheet), and 72 hours for centrally kept H-2A records. (SI-12; CP-2; PR.DS-11)
4.5 Records must be kept per the records schedule: at least 2 years for Produce Safety and traceability records, 3 years after certification for H-2A records, 2 years after the restricted-entry interval for Worker Protection Standard information, and 6 years for security documentation. (SI-12; PR.DS-11)
4.6 Restricted data must not be stored on file shares or in the data warehouse unless the data owner has registered a need; worker identifiers in analytics must be masked. (AC-6; SI-12; PR.DS-01)
4.7 Media holding Restricted or Confidential data, including returned seasonal tablets, must be sanitized before reuse and destroyed by a certified vendor with a certificate before disposal; customer records must be disposed of so personal information is unreadable. (MP-6; PR.DS-01)
4.8 Backups of tier-1 systems, the PLC program library, and SCADA configurations must be encrypted, immutable or offline, stored in a separate account or location, and restore-tested at least annually; tier-1 restore tests must meet the BIA RPO. (CP-9; PR.DS-11)
4.9 Restricted or Confidential data must not be entered into any AI tool unless the AI governance committee has approved the use case and the provider's terms bar training on company data. (SA-9; PL-4; GV.SC-05)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-04.1 Encryption and Key Management Standard
- STD-04.2 Media Protection and Disposal Standard
- STD-04.3 Backup Standard
- STD-04.4 Regulatory Records Integrity and Retention Standard
- PRC-04.1 Regulator Records Request Procedure (FDA, DOL, EPA)

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), access certifications, and OT change and session reviews. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm. Vendor violations are handled under the contract and STD-01.9.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 FMICP SSP; P03 gap analysis; P05 BIA; P08 runbook and notification matrix; P10 AI governance.
