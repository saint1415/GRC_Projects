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
| Implements (SP 800-53 Rev. 5) | RA-2, MP-1, MP-6, SC-8, SC-28, SI-7, SI-12, CP-9, AC-16 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-11 |
| HIPAA Security Rule | 164.310(d); 164.312(a)(2)(iv), (c), (e); 164.308(a)(7)(ii)(A) |

## 1. Purpose
Classify the group's information by the harm its disclosure, alteration, or loss would cause, and set handling rules that match, including the integrity rules for clinical results.

## 2. Scope
All Cris Santos Company workforce members (employees, providers, contractors, students, and volunteers) at all 159 sites in Florida, Georgia, Alabama, and South Carolina, including acquired practices from their acquisition date. Covers all systems and data, including cloud, colocation, SaaS, medical devices, and systems that business associates and other vendors operate for the group, and the services the group offers to external clients (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Privacy Officer | Owns classification; approves new uses of Restricted data |
| Data owners (system owners) | Classify their data; approve access |
| CISO | Encryption, backup, and disposal standards |
| Laboratory Director | Result integrity rules for lab data |
| All workforce | Handle information according to its class |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Information must be classified as Restricted (PHI, Part 2 records, genetic and lab results, SSNs, payment card data, credentials), Confidential (financial, legal, security, material nonpublic information), Internal, or Public, and labeled where systems allow. (RA-2; ID.AM-07)
4.2 Restricted data must be encrypted at rest and in transit using STD-04.1, including on endpoints and inside data center segments. (SC-28; SC-8; PR.DS-01)
4.3 Clinical results must be protected from unauthorized or undetected change from entry to final report, and every result change must be attributable to a person or an approved rule version. (SI-7; AU-10; PR.DS-01)
4.4 Records received from Part 2 programs must be flagged and handled under the Part 2 procedure. (AC-16; PR.DS-01)
4.5 Restricted data extracts must be registered, minimized, and deleted within 90 days unless renewed. (SI-12; AC-6; PR.DS-01)
4.6 Media holding Restricted or Confidential data must be sanitized before reuse and destroyed by a certified vendor with a certificate before disposal. (MP-6; PR.DS-01)
4.7 Backups of Restricted data must be encrypted, immutable, stored in a separate account or location, and restore-tested at least quarterly for tier-1 systems. (CP-9; PR.DS-11)
4.8 Restricted data must not be entered into any AI tool unless the AI council has approved the use case and a BAA with no-training terms is in place. (SA-9; PL-4; GV.SC-05)
4.9 Records must be kept per the records schedule, including 6 years for security documentation and CLIA retention periods for lab records. (SI-12; PR.DS-11)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-04.1 Encryption Standard
- STD-04.2 Media Protection and Disposal Standard
- STD-04.3 Backup Standard
- STD-04.4 Clinical Data Integrity Standard
- PRC-04.1 Data Extract Registration Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), and access certifications. Violations are handled under the HIPAA sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 LIS SSP; P08 runbook and notification matrix; P10 AI governance; applicable regulations listed in P03.
