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
| Implements (SP 800-53 Rev. 5) | RA-2, PT-2, PT-4, PT-5, MP-6, SC-8, SC-28, SI-12, CP-9, AC-3 |
| CSF 2.0 | ID.AM-07, GV.OC-03, PR.DS-01, PR.DS-02, PR.DS-11 |
| Regulatory basis | 47 U.S.C. 222; 47 CFR 64.2005-64.2009; 47 CFR 1.20003-1.20004; Fla. Stat. 501.171(2), (8) |

## 1. Purpose
Classify the company's information by the harm its disclosure, alteration, or loss would cause, and set handling rules that match, including the rules for using CPNI, the whole-account protection rule, and the separation of lawful-intercept data.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary staff) and the agents of care vendors and other third parties who use company systems, in all four states, including acquired carriers from their closing date. Covers all systems and data, including the carrier network and its management plane, the lawful-intercept platform, cloud, data centers, SaaS, and systems that vendors operate for the company, and the services offered to business customers (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Privacy Officer | Owns classification; approves new uses of Restricted data |
| Vice President, Marketing | CPNI approvals, notices, and the campaign register |
| Data owners (system owners) | Classify their data; approve access |
| CISO | Encryption, backup, and disposal standards |
| Director, Lawful Intercept Compliance | Handling of lawful-intercept data and court orders |
| All workforce | Handle information according to its class |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Information must be classified as Restricted (CPNI including call detail, the whole customer account record, lawful-intercept data and court orders, customer credentials, SSNs, payment data), Confidential (network topology and configurations, outage filings, security data, material nonpublic information), Internal, or Public, and labeled where systems allow. (RA-2; ID.AM-07)
4.2 The whole customer account record, including broadband usage and configuration data, must be protected to the CPNI standard, even where the data is not CPNI under 47 U.S.C. 222(h)(1). (RA-2; AC-3; PR.DS-01)
4.3 CPNI may be used, disclosed, or accessed only as 47 U.S.C. 222 and 64.2005 allow, or with customer approval checked at the time of use. Every sales or marketing campaign that uses CPNI must be registered, approved by a supervisor, and its records kept at least 1 year. (PT-2; PT-4; GV.OC-03)
4.4 Customers must receive a CPNI notice that meets 64.2008(c) before any solicitation for approval, and opt-out notices must be sent every two years, including to customers of acquired carriers within 90 days of closing. (PT-5; GV.OC-03)
4.5 Restricted data must be encrypted at rest and in transit using STD-04.1, including on management networks and in transfers from network elements. (SC-28; SC-8; PR.DS-01)
4.6 Lawful-intercept data and court orders must stay in the lawful-intercept enclave and its approved records system. They must never be placed in tickets, email, chat, or AI tools. (AC-3; SC-7; PR.DS-01)
4.7 Restricted data extracts must be registered, minimized, and deleted within 90 days unless renewed. (SI-12; AC-6; PR.DS-01)
4.8 Call detail records must be kept 36 months and then deleted. Media and records holding Restricted or Confidential data must be sanitized or destroyed so the data is unreadable, with a certificate. (SI-12; MP-6; PR.DS-01)
4.9 Backups of Restricted data must be encrypted, immutable, stored in a separate account or location, and restore-tested at least quarterly for tier-1 systems. (CP-9; PR.DS-11)
4.10 Restricted data must not be entered into any AI tool unless the AI council has approved the use case and the contract bars training on and secondary use of company data. (SA-9; PL-4; GV.SC-05)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-04.1 Encryption Standard
- STD-04.2 Media Protection and Disposal Standard
- STD-04.3 Backup Standard
- STD-04.4 CPNI Use and Approval Standard
- PRC-04.1 Data Extract Registration Procedure
- PRC-04.2 Campaign Registration and Supervisory Approval Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), access certifications, and the CPNI certification evidence package. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or of a vendor agent's access, in proportion to intent and harm. Misuse of CPNI is always a sanctionable violation.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 OSS/BSS SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
