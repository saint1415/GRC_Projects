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
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, acquisitions or Cybersecurity Plan amendments |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-1, MP-3, MP-6, SC-8, SC-28, SI-7, AU-9, AU-10, CP-9, SI-12 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-11, PR.PS-04 |
| 33 CFR Part 101 Subpart F | 101.630(b); 101.650(c); 101.650(g)(4) |

## 1. Purpose
Classify the company's information by the harm its disclosure, alteration or loss would cause, and set handling rules that match, including the rules for sensitive security information and for the integrity of customs holds and hazardous cargo data.

## 2. Scope
All Cris Santos Company employees, contractors, temporary staff and interns at headquarters, the enterprise planning center and the 8 terminals (T-01 to T-08) in Florida, Georgia, South Carolina and Texas, including acquired terminals from their acquisition date. Longshore workers ordered through the hiring halls and OEM and vendor technicians are covered when they use company IT or OT, through the hiring hall arrangements and their contracts. Covers all IT and OT systems and data, including cloud, colocation, SaaS, cranes and automation, gate systems, and the services the company provides to outside customers (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Compliance Officer | Owns classification; approves new uses of Restricted data |
| Director of Maritime Cybersecurity (CySO) | SSI handling for the Cybersecurity Plans and Assessment |
| Data owners (system owners) | Classify their data; approve access |
| CISO | Encryption, logging, backup and disposal standards |
| All workers | Handle information according to its class |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Information must be classified as Restricted (SSI, personal information such as driver license numbers and TWIC card identifiers, credentials), Confidential (customs and cargo data, bills of lading, customer and financial data, material nonpublic information), Internal or Public, and labeled where systems allow. (RA-2; ID.AM-07)
4.2 SSI, including the Cybersecurity Plans, FSPs, FSAs, network maps and MARSEC Directive materials, must be marked and protected under 49 CFR part 1520, stored only in the SSI repository and shared only with covered persons who need to know. (AC-3; MP-3; PR.DS-01)
4.3 Restricted and Confidential data must be encrypted in transit and at rest under STD-04.1. OT traffic must be encrypted where technically feasible, and the feasibility decision must be documented. (SC-8; SC-28; PR.DS-02)
4.4 Changes to customs holds, releases and hazardous cargo data must be attributable to a named person or an approved rule version, tested before release, and reconciled daily with the source. (SI-7; AU-10; PR.DS-01)
4.5 Logs must be captured centrally, protected so that only privileged users can read them, and kept 1 year online and 3 years in the archive. (AU-9; AU-11; PR.PS-04)
4.6 Media holding Restricted or Confidential data must be sanitized before reuse and destroyed by a certified vendor with a certificate before disposal. (MP-6; PR.DS-01)
4.7 Backups of critical IT and OT systems, including approved controller programs, must be immutable, stored in a separate account or location, and restore-tested at least quarterly for tier-1 systems. (CP-9; PR.DS-11)
4.8 Restricted, Confidential or SSI data must not be entered into any AI tool unless the AI governance committee has approved the use case and the contract bars training on company data. (SA-9; PL-4; GV.SC-05)
4.9 Driver license numbers must not be copied into analytic datasets or sent to AI vendors, and must be tokenized in SL-1 by 2027-06-30. (SI-12; AC-6; PR.DS-01)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-04.1 Encryption Standard
- STD-04.2 Media Protection and Disposal Standard
- STD-04.3 Backup Standard
- STD-04.4 SSI Handling Standard
- STD-04.5 Cargo Data Integrity Standard
- PRC-04.1 Data Extract Registration Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), access certifications and, once the Cybersecurity Plans are approved, the annual Plan audits. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 ETOP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance; the Cybersecurity Plans and FSPs (SSI).
