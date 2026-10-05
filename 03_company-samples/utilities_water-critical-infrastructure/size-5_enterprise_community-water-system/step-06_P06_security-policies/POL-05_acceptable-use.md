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
| Implements (SP 800-53 Rev. 5) | PL-4, PL-4(1), AC-8, AC-20, AT-2, AT-3, CM-11, MP-7 |
| CSF 2.0 | PR.AT-01, PR.AT-02, GV.PO-01, PR.PS-02 |
| Regulations | SDWA section 1433 (42 U.S.C. 300i-2(b)(1)) |

## 1. Purpose
Set clear, plain-language rules for how the workforce uses company systems, devices, data, and AI tools, with extra rules for anyone who works on or near OT.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary staff) in all four regulated subsidiaries in Florida, Georgia, North Carolina, and Tennessee and in the two service lines, including acquired systems from their acquisition date. Covers all IT and OT systems and data: SCADA, PLCs, RTUs, telemetry, and HMIs at the 126 community water systems and 5 ROCCs; cloud, colocation, and SaaS; and systems that vendors and integrators operate or support for the company, including the services offered to municipal clients (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Human Resources Officer | Owns this policy; runs training and acknowledgments |
| CISO | Sets the approved AI tools list and technical restrictions |
| Managers and plant superintendents | Make sure their staff complete training and follow the rules |
| All workforce | Follow this policy and acknowledge it each year |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether the 2026 independent assessment tested it (P07).

4.1 Workforce members must use company systems only for authorized business purposes and must acknowledge this policy at hire and each year. (PL-4; GV.PO-01)
4.2 All workforce members must complete security awareness training at hire and each year; operators, SCADA technicians, and OT engineers must also complete role-based OT security training each year. (AT-2; AT-3; PR.AT-01; PR.AT-02)
4.3 Only company-managed devices may connect to OT networks. Personal devices and vendor laptops must never be connected to OT networks. (AC-20; PR.AA-05)
4.4 Removable media may be used on OT hosts only after scanning at a company media kiosk; USB storage is blocked on OT hosts. (MP-7; PR.DS-01)
4.5 Workforce members must not post photos, videos, or descriptions of control rooms, HMI screens, network diagrams, chemical storage, or security measures on social media or public sites. (PL-4(1); PR.AT-01)
4.6 Only AI tools on the approved list (STD-05.3) may be used for company work, and Restricted or Confidential information must never be entered into any other AI tool. (AC-20; PL-4; PR.DS-01)
4.7 Workforce members must not install software on company devices; only IT and OT engineering may install approved software. (CM-11; PR.PS-02)
4.8 Phishing emails and suspicious calls or visits, including requests for information about plant operations, remote access, or schedules, must be reported to the SOC. (AT-2; PR.AT-01)
4.9 Company systems display a use notice, and use may be monitored; workforce members have no expectation of privacy on company systems. (AC-8; GV.PO-01)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-05.1 Security Awareness and Training Standard
- STD-05.2 External Systems, Personal Devices, and Removable Media Standard
- STD-05.3 Approved AI Tools List

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, quarterly access certifications, the annual independent assessment by Internal Audit and the co-sourced OT assessment firm (P07), and plant drills. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 GCR-WTSS SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance; each covered system's RRA and ERP.
