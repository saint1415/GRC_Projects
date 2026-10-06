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
| Implements (SP 800-53 Rev. 5) | RA-2, SC-8, SC-28, SI-12, MP-6, CP-9, RA-8, SA-9 |
| CSF 2.0 | ID.AM-05, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| Regulatory drivers | CPG 2.0 goals 3.K, 3.O (R05); Cal. Civ. Code 1798.100(a)(3) and 11 CCR 7150 (R03); PCI DSS Req. 3 and 9.4 (R01); state disposal laws |

## 1. Purpose
Classify company, tenant, visitor, employee, and client information and set the handling rules for each level, so that sensitive data is protected, kept only as long as needed, and disposed of properly.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and TRS staff) at all 140 operated properties in Florida, Texas, Georgia, North Carolina, Arizona, and California, including acquired properties from their acquisition date. Covers all systems and data: IT, OT (building automation, access control, video), cloud, colocation, SaaS, systems that integrators and other vendors operate for the company, and the services the TRS offers to external clients (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Privacy Officer | Owns classification, the retention schedule, and CPPA risk assessments |
| Data owners (system owners) | Classify data in their systems and apply handling rules |
| Director of Cloud Platform Engineering | Encryption and backup services |
| Chief Accounting Officer | Card handling rules (PCI DSS) |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Data owners must classify information as Restricted (face templates, government ID numbers, Social Security numbers, bank details, authentication secrets), Confidential (credential records and access history, video, building drawings, lease terms, client data), Internal, or Public, and label systems accordingly. (RA-2; ID.AM-05)
4.2 Restricted and Confidential data must be encrypted in transit and at rest. Where an OT protocol cannot be encrypted, the exception must be documented with zone isolation as the compensating control. (SC-8; SC-28; PR.DS-01; PR.DS-02)
4.3 Data must not be kept longer than the retention schedule in STD-04.4: visitor ID images 30 days, visit logs 1 year, access history 2 years, video 30 days unless held for a case, and face templates deleted within 24 hours of opt-out or the end of the holder's credential. (SI-12; PR.DS-01)
4.4 Media and records with Restricted or Confidential data must be disposed of using NIST SP 800-88 Rev. 2 methods, with a certificate of destruction for each batch. (MP-6; ID.AM-08)
4.5 Card data must be taken only on validated P2PE terminals and must never be written on paper, typed into any company system, or sent by email or chat. (SI-12; MP-6; PR.DS-01)
4.6 No new processing of California consumers' sensitive personal information, no systematic observation of employees to infer performance or behavior, and no use of ADMT for a significant decision may start until the Chief Privacy Officer has completed the CPPA risk assessment or ADMT review (PRC-04.1). (RA-8; GV.OC-03)
4.7 Backups of tier-1 systems, including OT controller programs and configurations, must be immutable, kept in accounts separate from production, held by the company (not only by integrators), and restore-tested on the schedule in STD-04.3. (CP-9; PR.DS-11)
4.8 Video exports and bulk exports of credential or visitor data must have a case number or approved business purpose, supervisor approval, and a log entry. (AU-6; AC-6; DE.CM-03)
4.9 Vendors that process Restricted or Confidential data must have contracts that limit use to company purposes, prohibit using company data to train their models, and require deletion at contract end. (SA-9; GV.SC-05)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-04.1 Encryption Standard
- STD-04.2 Media Protection and Disposal Standard
- STD-04.3 Backup Standard
- STD-04.4 Retention Schedule
- STD-04.5 Card Handling Standard
- PRC-04.1 CPPA Risk Assessment Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 BAACS SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
