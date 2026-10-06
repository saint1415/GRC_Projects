# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLP |
| Policy ID | POL-04 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Chief Privacy Officer |
| Approved by | Executive risk committee |
| Approval date | 2026-09-08 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | RA-2, SC-8, SC-28, MP-6, SI-12, AC-21, PT-4, CM-12 |
| CSF 2.0 | ID.AM-05, ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02 |
| Regulations | 16 CFR 314.4(c)(2), (c)(3), (c)(6); 26 CFR 301.7216-2, -3; 45 CFR 164.312(a)(2)(iv), (e)(2)(ii); 164.502(a)(3); FAR 52.204-21(b)(1)(vii); Fla. Stat. 501.171(8) |

## 1. Purpose
Classify the firm's information by sensitivity and legal restrictions, and set handling rules for storage, transmission, sharing, AI use, retention, and disposal.

## 2. Scope
All Cris Santos Company partners, employees, seasonal staff, contractors, and interns in all 64 offices and the 12 processing hubs, and staff of acquired firms from their acquisition date. Covers all systems and data, including cloud, colocation, SaaS, the offshore provider workspace, and systems that service providers operate for the firm, and the services the firm offers to clients (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Privacy Officer | Owns the classification scheme, data map, and records schedule |
| National Tax Leader | Owns the IRC 7216 consent program |
| Engagement partners | Classify engagement data and enforce handling rules |
| Director of Tax Technology and system owners | Implement technical handling rules |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Information must be classified as Restricted (tax return information, customer information, PHI, SSNs, bank and identity documents, Federal Contract Information), Confidential (other client and firm non-public information), Internal, or Public, and labeled in the DMS where the system supports it. (RA-2; ID.AM-05)
4.2 A data map must record where Restricted information is stored, including AI services and offshore workspaces, and be updated at least annually. (CM-12; ID.AM-07)
4.3 Restricted information must be encrypted at rest and in transit over external networks. Any exception requires compensating controls approved in writing by the Qualified Individual. (SC-8; SC-28; PR.DS-01)
4.4 Returns and source documents must be exchanged with clients through the client portal or another approved encrypted channel, never as plain email attachments. (SC-8; PR.DS-02)
4.5 Tax return information may leave the firm only under a documented IRC 7216 permission or with the taxpayer's prior written consent, obtained before the disclosure and never as a condition of service. (AC-21; PT-4; PR.DS-01)
4.6 Form 1040 series filers' SSNs must not be released to any preparer outside the United States; packages for the offshore provider must pass automated consent and SSN-masking checks before release. (AC-21; SA-9; PR.DS-01)
4.7 PHI held as a business associate may be used and disclosed only as the business associate agreement permits, and PHI repositories must be tagged. (AC-21; PT-2; PR.DS-01)
4.8 Restricted information may be used in an AI tool only if the tool is on the approved list (STD-05.3), the IRC 7216 basis is documented, processing stays in the United States, and the vendor may not train on firm data. (SA-9; PT-4; GV.SC-05)
4.9 Records must be kept according to the records schedule (tax files 7 years; Forms 8878 and 8879 at least 3 years under Pub. 1345) and then disposed of, unless a legal hold applies. Disposal runs must be logged and verified. (SI-12; MP-6; ID.AM-08)
4.10 Paper and media containing Restricted information must be shredded or sanitized before disposal or reuse, with certificates of destruction. (MP-6; PR.DS-01)
4.11 The records schedule must be reviewed annually to minimize unnecessary retention. (SI-12; ID.AM-08)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-04.1 Encryption Standard
- STD-04.2 Media Protection and Disposal Standard
- STD-04.3 Records Retention Schedule
- STD-04.4 IRC 7216 Disclosure and Consent Standard
- PRC-04.1 Offshore Release Procedure
- PRC-04.2 Disposal Run Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment, partnership, or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 Tax Engagement Platform SSP; P08 runbook and notification matrix; P10 AI governance; applicable regulations listed in P03.
