# Acceptable Use Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-05 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Chief Human Resources Officer |
| Approved by | Executive risk committee |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | PL-4, AT-2, AT-3, AC-20, IA-2, MP-2, CM-8 |
| CSF 2.0 | PR.AT-01, PR.AT-02, PR.AA-01, ID.AM-02 |
| Key regulatory drivers | SP 800-171 R2 3.2 (FSCE); FAR 52.204-21(b)(1)(iii) |

## 1. Purpose
Set the rules every workforce member follows when using company systems, data, and AI tools, and the training each role needs to follow them.

## 2. Scope
All Cris Santos Company workforce members (employees, temporary workers supplied by staffing agencies, contractors, and interns) at headquarters, the 6 distribution centers, the 15 sales offices, and remote locations, including AQ-1 and any future acquisition from its closing date. Covers all systems and data, including cloud, colocation, SaaS, distribution-center OT, the FSCE, and systems that vendors, carriers, 3PLs, and drop-ship partners operate for the company, and the services offered to external customers (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Human Resources Officer | Owns this policy, attestations, and training records |
| Managers | Make sure staff complete training before access |
| Staffing agencies | Make sure temporary workers complete the short module before receiving a handheld |
| All workforce | Follow these rules |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Company systems are for business use. Activity on them is logged and may be monitored. (PL-4; PR.AT-01)
4.2 Every workforce member must complete security awareness training and attest to this policy at hire and annually; temporary workers must complete the short module before receiving a handheld. (AT-2; PL-4; PR.AT-01)
4.3 Staff in high-risk roles must complete role-based training each year: receiving and returns staff (counterfeit indicators), sales desk (order and ship-to fraud), accounts payable (bank-change fraud), enclave users (CUI handling), and administrators. (AT-3; PR.AT-02)
4.4 Personal devices may reach email and chat only through managed apps; personal cloud storage and personal email must not be used for company data. (AC-20; PR.AA-05)
4.5 Suspected phishing, suspicious supplier requests, and unexpected product substitutions must be reported to the SOC at once. (IR-6; AT-2; RS.MA-02)
4.6 Only AI tools on the approved list (STD-05.3) may be used for company work, and any new AI use, including AI features switched on in existing products, must be registered with the AI governance committee before use. (SA-9; CM-8; ID.AM-02)
4.7 Bank-detail changes and ship-to changes must never be made on the strength of an email alone; they must be verified by a call to the number already on file. (AT-2; PR.AT-01)
4.8 Credentials, badges, and security keys must never be shared, and nobody may sign in for another person on a kiosk or handheld. (IA-2; PR.AA-01)
4.9 CUI printouts and media must stay in the configuration lab, in locked storage when not in use. (MP-2; PR.DS-01)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-05.1 Security Awareness and Training Standard
- STD-05.2 External Systems and Personal Devices Standard
- STD-05.3 Approved AI Tools List

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), access certifications, and the CMMC Program Office's internal assessments for the FSCE. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 OCFP SSP; FSCE CMMC SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
