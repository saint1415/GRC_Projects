# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Chief Compliance Officer |
| Approved by | Executive risk committee |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | MP-1, RA-2, AC-4, SC-7, MP-2, MP-4, MP-6, SC-28, SC-8, SI-10, AC-3, CP-9, SA-9, PL-4, SI-12 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-11, GV.SC-05 |
| Regulatory drivers | N23-R01 (52.204-21(a), (b)(1)(vii)); N23-R03 (252.204-7012(a), (b)(2); SP 800-171 R2 3.8, 3.13); N23-R04 (252.204-7021(d)(2)); FAR 52.232-33(b); Fla. Stat. 501.171(2) (worked example); client contract security terms |

## 1. Purpose
Classify company information by sensitivity and set handling rules so that protection matches risk and legal duties: CUI stays in the FPCE and the plan rooms, bank details are never trusted on the strength of a message, and personal information and client facility security details are kept where they belong.

## 2. Scope
All Cris Santos Company workforce members (employees, craft workers, contractors, and interns) at headquarters (HQ-1), the nine regional offices, about 140 jobsites, the two yards, and the two colocation data centers in eight states, including acquired businesses (AQ-1 and AQ-2) from their acquisition date. Covers all company systems and data, including cloud, colocation, SaaS, the Federal Programs CUI Enclave (FPCE), jobsite technology, client building systems that BTS administers, systems that vendors and subcontractors operate for the company, and the services the company offers to external clients (SL-1 and SL-2). Subcontractor and design-team users of company systems are bound by the security terms in their subcontracts and access agreements.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Compliance Officer | Owns classification; approves new uses of Restricted data |
| Director, CMMC Program Office | CUI handling standard; CUI marking and plan room rules with the federal project security managers |
| Data owners (system owners) | Classify their data; approve access |
| CISO | Encryption, backup, and disposal standards |
| Vice President, Treasury | Payment data integrity rules |
| All workforce | Handle information according to its class |

Role overlaps are limited by design: Internal Audit (third line) never operates the controls it tests, and the people who maintain payees never release payments (POL-02 4.3).

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in the 2026 PDPP assessment (P07).

4.1 Information must be classified as CUI; Restricted (FCI, bank and payment data, Social Security numbers, client facility security details, credentials); Confidential (bid and pricing data, financials, material nonpublic information); Internal; or Public. (RA-2; ID.AM-07)
4.2 CUI may be stored, processed, or sent only in the FPCE and controlled plan rooms. CUI must never be placed in the commercial project management platform, commercial email, or any AI tool. (AC-4; SC-7; PR.DS-01)
4.3 Printed CUI must carry CUI markings, be stored in locked cabinets when not in use, be checked out and returned through the plan room log, and be shredded by a certified vendor with a certificate. (MP-2; MP-4; MP-6; PR.DS-01)
4.4 Restricted and CUI data must be encrypted at rest and in transit using STD-04.1; CUI with FIPS-validated cryptography. (SC-28; SC-8; PR.DS-01)
4.5 Bank account details must never be accepted, changed, or confirmed on the strength of an email, text, or inbound phone call alone. (SI-10; PR.DS-01)
4.6 Social Security numbers on certified payrolls must be truncated where the contracting officer allows, and certified payrolls must be sent through owner or government portals rather than email. (AC-3; PR.DS-01)
4.7 Client facility security details (layouts, camera locations, credentials) must be kept only in the BTS vault and in project folders restricted to the BTS team. (AC-3; PR.DS-01)
4.8 Media holding Restricted, Confidential, or CUI data must be sanitized before reuse and destroyed by a certified vendor with a certificate before disposal. (MP-6; PR.DS-01)
4.9 Backups of Restricted data must be encrypted, immutable, stored in a separate account or location, and restore-tested at least quarterly for tier-1 systems. (CP-9; PR.DS-11)
4.10 FCI, Restricted, and Confidential data must not be entered into any AI tool unless the AI governance committee has approved the use case and enterprise terms bar training on company data. No AI tool is approved for CUI. (SA-9; PL-4; GV.SC-05)
4.11 Records must be kept per the records schedule, including 6 years for security and CMMC records and the retention periods in federal contracts. (SI-12; PR.DS-11)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot weaken it.
- STD-04.1 Encryption Standard
- STD-04.2 Media Protection and Disposal Standard
- STD-04.3 Backup Standard
- STD-04.4 Payment Data Integrity Standard
- STD-04.5 CUI Handling Standard
- PRC-04.1 Controlled Plan Room Procedure (Federal Group)
- PRC-04.2 Certified Payroll Handling Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, quarterly access certifications, monthly payment-control exception reports, the annual Internal Audit assessment (P07), and the CMMC self-assessments (P03). Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm. Subcontractor and vendor violations are handled under their contracts and can lead to removal of access or the subcontract.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. No exception can change how a CMMC requirement is scored.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 enterprise risk register; P02 PDPP SSP; P03 regulatory gap analysis (including the FPCE readiness check); P07 assessment and POA&M; P08 runbook and notification matrix; P10 AI governance; FPCE SSP (separate, CMMC Level 2).
