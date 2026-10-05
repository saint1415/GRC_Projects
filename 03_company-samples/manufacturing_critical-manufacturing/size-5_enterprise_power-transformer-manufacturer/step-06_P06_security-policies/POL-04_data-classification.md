# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Chief Compliance Officer |
| Approved by | Executive risk committee |
| Approval date | 2026-09-08 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-6, SC-8, SC-28, SI-7, SI-12, CP-9, AU-10 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-11 |
| Binding requirements served | FAR 52.204-21(b)(1)(i), (vii); 10 CFR 429.71; 15 CFR 762.6(a); state breach laws (Fla. Stat. 501.171(8) worked example) |

## 1. Purpose
Make sure every piece of company, customer, and supplier information is classified and handled according to its sensitivity, that test and certification records stay trustworthy, and that records are kept as long as the law and contracts require.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, temporary workers, and interns) at all 7 plants, 9 service centers, 3 spare yards, and offices in Florida, Georgia, Tennessee, Texas, North Carolina, and Ohio, including the acquired Ohio plant (AQ-01) from its acquisition date. Covers all systems and data, including cloud, colocation, SaaS, plant control systems (OT), test systems, and systems that suppliers operate for the company, and the products and services the company supplies to utilities (TMU firmware and configuration software, the Fleet Monitoring Service, and the Spare Transformer Reserve Service).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Compliance Officer | Owns classification and the records schedule |
| Data owners (system owners) | Classify their data; approve access |
| CISO | Encryption, backup, and disposal standards |
| Corporate Director of Quality | Test data and DOE certification record integrity |
| Director of Trade Compliance | Export records |
| All workforce | Handle information according to its class |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Information must be classified as Restricted (transformer designs and winding specifications, customer substation drawings, firmware source and signing keys, FCI, employee Social Security and bank data, credentials, material nonpublic information), Confidential (supplier pricing, bills of materials, test reports, utility asset health data, STRS member data), Internal, or Public, and labeled where systems allow. (RA-2; ID.AM-07)
4.2 Restricted data must be encrypted at rest and in transit using STD-04.1. (SC-28; SC-8; PR.DS-01)
4.3 FCI must be stored only in the ERP and labeled federal project sites, and must not be entered into unapproved systems or public AI tools. (AC-3; PR.DS-01)
4.4 Test data must be protected from unauthorized or undetected change from capture to certified report, locked at Quality sign-off, and DOE certification records must be indexed and kept for 2 years after a model is discontinued. (SI-7; AU-10; SI-12; PR.DS-01)
4.5 Export records must be kept at least 5 years, and no export may be released without a screening record, including during system downtime. (SI-12; AC-3; GV.OC-03)
4.6 Customer drawings must be exchanged only through the PLM customer portal or another approved encrypted channel. (SC-8; PR.DS-02)
4.7 Media holding Restricted or Confidential data must be sanitized before reuse and destroyed by a certified vendor with a certificate before disposal. (MP-6; PR.DS-01)
4.8 Backups of tier-1 data must be encrypted, immutable, stored in a separate account, and restore-tested at least quarterly; OT controller programs must be backed up automatically and copied offline weekly. (CP-9; PR.DS-11)
4.9 Restricted or Confidential data must not be entered into any AI tool unless the AI governance committee has approved the use case and the contract bars training on company data. (SA-9; PL-4; GV.SC-05)
4.10 Records must be kept per the records schedule, including 7 years for financial and security records. (SI-12; PR.DS-11)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-04.1 Encryption Standard
- STD-04.2 Media Protection and Disposal Standard
- STD-04.3 Backup Standard (including OT program backups)
- STD-04.4 Test Data and Certification Records Integrity Standard
- PRC-04.1 FCI Handling Procedure
- PRC-04.2 Export Screening Downtime Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 EPSP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
