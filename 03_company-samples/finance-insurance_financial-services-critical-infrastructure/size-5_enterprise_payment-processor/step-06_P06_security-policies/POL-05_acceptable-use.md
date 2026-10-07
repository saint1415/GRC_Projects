# Acceptable Use Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (and Cris Santos Payouts, LLC, under 23 NYCRR 500.2(d)) |
| Policy ID | POL-05 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Chief Human Resources Officer |
| Approved by | Executive risk committee |
| Approval date | 2026-09-08 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, new sponsor banks, or acquisitions |
| Implements (SP 800-53 Rev. 5) | PL-4, AT-2, AT-3, AC-20, SI-12, CM-11, IR-6, AC-3, AC-8 |
| CSF 2.0 | GV.PO-01, PR.AT-01, PR.AT-02, PR.AA-01, PR.DS-01, PR.PS-05, RS.MA-02, PR.AA-05 |
| Regulatory drivers | See `policy-control-map.csv` (one driver per statement) |

## 1. Purpose
Set the rules every workforce member follows when using company systems, data, and devices, including generative AI tools, and make sure people are trained to follow them.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary staff) in every location, and Cris Santos Payouts, LLC, which adopted this program under 23 NYCRR 500.2(d). Covers all systems and data, including Cloud A, Cloud B, DC-1, DC-2, SaaS, and systems that service providers operate for the company, and the services the company provides to merchants, ISV partners, and sponsor Banks A, B, and C.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Human Resources Officer | Policy owner; training and attestation records |
| Managers | Make sure staff complete training and follow the rules |
| CISO | Approved tools list and monitoring |
| All workforce | Follow this policy and report incidents |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Every workforce member must acknowledge this policy and the rules of behavior at hire and at least annually. (PL-4; GV.PO-01)
4.2 Every workforce member must complete security awareness training at hire and at least annually, including phishing and social engineering; developers, key custodians, settlement operators, and contact center agents must also complete role-based training. (AT-2; AT-3; PR.AT-01; PR.AT-02)
4.3 Only company-managed devices may access company systems; personal devices may never access the CDE. (AC-20; PR.AA-01)
4.4 Card numbers must never be requested or accepted by email, chat, or ticket; contact center agents must use the secure card capture tool, which pauses recording. (SI-12; PR.DS-01)
4.5 Only approved software may be installed, and nothing may be installed on CDE administration workstations outside endpoint management. (CM-11; PR.PS-05)
4.6 Generative AI tools may be used only from the approved tools list (STD-05.3); card, merchant, and customer data must never be entered into public AI tools. (AC-20; PL-4; PR.DS-01)
4.7 Lost devices and suspected incidents must be reported to the Cyber Fusion Center within 1 hour. (IR-6; RS.MA-02)
4.8 Merchant funding accounts and payout destinations may be changed only through the verified portal workflow; staff must never change them on a phone or email request. (AC-3; PR.AA-05)
4.9 Workforce members must be told that the company monitors use of its systems, through the sign-in notice and this policy. (AC-8; GV.PO-01)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-05.1 Security Awareness and Training Standard
- STD-05.2 External Systems and Personal Devices Standard
- STD-05.3 Approved AI Tools List
- PRC-05.1 Contact Center Card Data Handling Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the PCI DSS quarterly reviews (PCI DSS 12.4.2), access certifications, and the annual Internal Audit assessment (P07). Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 Core Payment Processing Platform SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
