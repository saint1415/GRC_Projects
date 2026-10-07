# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc., adopted by Cris Santos Title and Escrow, LLC and Cris Santos Relocation, LLC |
| Policy ID | POL-04 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Chief Privacy Officer |
| Approved by | Executive risk committee |
| Approval date | 2026-09-08 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | RA-2, SC-28, SC-8, AC-21, SI-12, AC-6, MP-6, SI-7, SI-10, AU-10, AT-2, AU-6 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-11, PR.DS-10 |
| Regulatory drivers | See `policy-control-map.csv` (N53-R01 Safeguards Rule citations for each statement) |

## 1. Purpose
Classify the company's information by the harm its disclosure, alteration, or loss would cause, and set handling rules that match, including the integrity rules for wire instructions and payee bank details.

## 2. Scope
All Cris Santos Company, Inc. employees, the about 38,000 contractor sales associates who use company systems, contractors, and temporary staff, in all 9 states, and the employees of Cris Santos Title and Escrow, LLC and Cris Santos Relocation, LLC, which adopted this hierarchy by resolution. Acquired firms are covered from their acquisition date. Covers all systems and data, including cloud, colocation, SaaS, contractor agents' own devices when they access company systems, and systems that vendors operate for the company, and the services offered to business clients (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Privacy Officer | Owns classification and the retention schedule |
| Data owners (system owners) | Classify their data; approve access |
| President, Title and Escrow | Funds instruction integrity rules (STD-04.4) and payee verification (PRC-04.3) |
| Each state's broker of record | Earnest money deposit handling (PRC-04.2) |
| All employees and contractor agents | Handle information according to its class |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Information must be classified as Restricted (customer information, Social Security and account numbers, identity documents, wire instructions and payee bank details, consumer reports, credentials), Confidential (financial, legal, security, material nonpublic information), Internal, or Public. (RA-2; ID.AM-07)
4.2 Restricted data must be encrypted at rest and in transit under STD-04.1. Where the Qualified Individual finds encryption infeasible, compensating controls must be approved in writing and reviewed at least annually. (SC-28; SC-8; PR.DS-01)
4.3 Restricted data must be shared with outside parties only through approved channels (the Closing Communications Hub, SYS-01, or SYS-02), not as email attachments. (AC-21; SC-8; PR.DS-02)
4.4 Restricted data extracts must be registered, minimized, and deleted within 90 days unless renewed. (SI-12; AC-6; PR.DS-01)
4.5 Records must be kept per STD-04.2 and disposed of no later than two years after last use unless a business or legal need is documented, and the schedule must be reviewed at least annually, including data inherited through acquisitions. (SI-12; PR.DS-11)
4.6 Media and paper holding Restricted or Confidential data must be sanitized or destroyed by a certified vendor with a certificate. (MP-6; PR.DS-01)
4.7 Payee bank details must be verified under PRC-04.3 before first use and after any change, and approved instructions must be protected so later changes are detected. (SI-7; SI-10; PR.DS-01)
4.8 Every payee change and disbursement approval must be attributable to a named approver through a signed approval record. (AU-10; PR.DS-01)
4.9 Wire instructions must be delivered only inside the Closing Communications Hub or the brokerage escrow page. No employee or contractor agent may send, forward, or confirm wire instructions by email, text message, or phone, and any request to change instructions must be treated as a suspected incident. (SI-7; AT-2; PR.DS-02)
4.10 Earnest money deposits must be placed in escrow within each state's deadline and reconciled monthly under PRC-04.2. (AU-6; PR.DS-10)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-04.1 Encryption and Key Management Standard
- STD-04.2 Records Retention and Disposal Standard
- STD-04.3 Backup Standard
- STD-04.4 Funds Instruction Integrity Standard
- PRC-04.1 Data Extract Registration Procedure
- PRC-04.2 Earnest Money Deposit Handling Procedure
- PRC-04.3 Payee Verification and Callback Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or of the agent agreement, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 TMCC SSP; P03 gap analysis; P08 BEC runbook and notification matrix; P10 AI governance.
