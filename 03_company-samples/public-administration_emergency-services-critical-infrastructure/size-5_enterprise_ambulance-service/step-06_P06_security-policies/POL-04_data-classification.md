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
| Implements (SP 800-53 Rev. 5) | RA-2, SC-8, SC-28, AU-2, AC-4, SI-10, SI-12, AU-11, MP-6, CP-9, SA-9, PL-4 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-11, GV.SC-05 |
| HIPAA Security Rule | 164.310(d); 164.312(a)(2)(iv), (c), (e); 164.316(b)(2) |

## 1. Purpose
Make sure every kind of company information is identified, protected in proportion to its sensitivity, kept as long as the law requires, and disposed of safely, and that dispatch and patient care records stay accurate and attributable.

## 2. Scope
All Cris Santos Company workforce members at all 231 sites and in every ambulance, including acquired operations from their acquisition date. Covers all company information in any form: CAD incidents, call recordings, patient care records, member trip data, claims, workforce data, and security records, wherever held, including by vendors and clients' systems the company operates for them (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Privacy Officer | Owns classification and the records schedule |
| Data owners (system owners) | Classify their data and approve access |
| Director of Cloud Platform Engineering | Encryption, backup, and key services |
| All workforce | Handle data as labeled |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Information must be classified as Restricted (PHI, call recordings, member data, SSNs, credentials), Confidential (financial, legal, security, county contract terms, material nonpublic information), Internal, or Public, and labeled where systems allow. (RA-2; ID.AM-07)
4.2 Restricted data must be encrypted at rest and in transit using STD-04.1, including on tablets, MDCs, and laptops and across county PSAP links. (SC-28; SC-8; PR.DS-01)
4.3 Changes to dispatch times, unit status history, and signed patient care records must be logged with the user, time, and reason, and signed patient care records may change only through an addendum. (AU-2; SI-7; PR.DS-01)
4.4 Criminal justice information must not be received or stored in company systems. CAD-to-CAD interfaces must drop law enforcement fields, and any proposal to receive such data requires a CJIS applicability review first. (AC-4; SI-10; PR.DS-01)
4.5 Restricted data extracts must be registered, minimized, and deleted within 90 days unless renewed. (SI-12; AC-6; PR.DS-01)
4.6 Media holding Restricted or Confidential data, including retired tablets, MDCs, and console drives, must be sanitized before reuse and destroyed by a certified vendor with a certificate before disposal. (MP-6; PR.DS-01)
4.7 Backups of Restricted data must be encrypted, immutable, stored in a separate account or location, and restore-tested at least quarterly for tier-1 systems. (CP-9; PR.DS-11)
4.8 Restricted data must not be entered into any AI tool unless the AI governance committee has approved the use case and a BAA with no-training terms is in place. (SA-9; PL-4; GV.SC-05)
4.9 Records must be kept per the records schedule (STD-04.4): each state's EMS records rules (Florida worked example: at least 5 years, Rule 64J-1.014, F.A.C.), 7 years for Medicare documentation (42 CFR 424.516(f)), and 6 years for security documentation and audit logs. (SI-12; AU-11; PR.DS-11)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-04.1 Encryption Standard
- STD-04.2 Media Protection and Disposal Standard
- STD-04.3 Backup Standard
- STD-04.4 Records Retention Schedule
- PRC-04.1 Data Extract Registration Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), and access certifications. Violations are handled under the HIPAA sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 EDPCP SSP; P08 runbook and notification matrix; P10 AI governance; applicable regulations listed in P03.
