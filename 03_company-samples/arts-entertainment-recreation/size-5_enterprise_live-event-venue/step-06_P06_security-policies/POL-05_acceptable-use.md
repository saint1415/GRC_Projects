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
| Implements (SP 800-53 Rev. 5) | PL-4, PL-4(1), AC-8, AC-11, AC-20, AT-2, AT-3, IR-6 |
| CSF 2.0 | PR.AT-01, PR.AT-02, GV.PO-01 |
| Regulatory basis | PCI DSS v4.0.1 Requirements 12.2, 12.6, and 9.5 (N71-R04) |

## 1. Purpose
Set clear, plain-language rules for how the workforce, including seasonal event staff, uses the company's systems, devices, data, card readers, and AI tools.

## 2. Scope
All Cris Santos Company workforce members (employees, part-time and seasonal event staff, contractors, and interns) at headquarters, all 36 venues in 8 states, the 3 festivals, and the two contact centers, including acquired venues from their acquisition date. Covers all systems and data, including cloud, colocation, SaaS, venue operational technology, and systems that service providers and other vendors operate for the company, and the services the company offers to business clients (SL-1 white-label ticketing and SL-2 venue management).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Human Resources Officer | Policy owner; acknowledgments and training records |
| Managers and venue supervisors | Make sure staff complete training before their first shift |
| All workforce | Follow this policy |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Every workforce member must acknowledge this policy at hire and annually, and seasonal event staff at the start of each season. (PL-4; GV.PO-01)
4.2 Every workforce member must complete security awareness training at hire and annually, and take part in phishing simulations; event staff must complete the card handling and tamper awareness module before their first shift. (AT-2; PR.AT-01)
4.3 Role-based training is required each year for developers (secure coding), payment operations and contact center agents (card handling), and incident response roles. (AT-3; PR.AT-02)
4.4 Never write down, type into notes, or read aloud for a recording any card number or security code; report any card data you find to the SOC. (MP-6; IR-6; PR.AT-01)
4.5 Box office and stand staff must inspect card devices before each event as trained and report any sign of tampering or substitution immediately. (AT-3; PR.AT-02)
4.6 Only AI tools on the approved AI tools list (STD-05.3) may be used with company data, and any new AI feature must be registered in the AI inventory before use. (PL-4; AC-20; GV.PO-01)
4.7 Personal devices may reach company data only through managed apps and may never be used to reach the cardholder data environment. (AC-20; PR.AA-05)
4.8 Lock your screen when you step away and never share your login, including POS clerk and box office logins. (AC-11; IA-2; PR.AA-01)
4.9 Report suspected incidents, lost devices, and phishing to the SOC immediately. (IR-6; RS.MA-02)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-05.1 Security Awareness and Training Standard
- STD-05.2 External Systems and Personal Devices Standard
- STD-05.3 Approved AI Tools List
- PRC-05.1 Card Device Inspection Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), the QSA's Reports on Compliance, and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 TVOP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
