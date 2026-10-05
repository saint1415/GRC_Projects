# Acceptable Use Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-05 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Chief Human Resources Officer (with the CISO) |
| Approved by | Executive risk committee |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | PL-4, AT-2, AT-3, AC-20, CM-11, SI-3 |
| CSF 2.0 | PR.AT-01, PR.AT-02, GV.RR-04, PR.PS-05 |
| Regulatory drivers | MTSA 33 CFR 101.650(d), (i)(2); DOT 49 CFR 172.704(a)(4)-(5) |

## 1. Purpose
Set the rules every workforce member and integrator follows when using company IT and OT, including approved AI tools, so that everyday behavior does not open a path into the plants.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, integrators, and temporary staff) at all 14 plants, 9 distribution centers, 2 R&D centers, and offices, including acquired plants from their acquisition date. Covers all information technology (IT) and operational technology (OT): process control systems, safety instrumented systems, PLCs, terminal and loading rack automation, cloud, colocation, SaaS, and systems that vendors and integrators operate for the company, and the services the company offers to external customers (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Human Resources Officer | Policy owner; acknowledgments and training records |
| CISO | Technical rules and the approved AI tools list |
| Chief Data and Analytics Officer | AI governance committee chair (P10) |
| Managers | Make sure their staff complete training and acknowledgments |
| All workforce and integrators | Follow the rules; report incidents |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 All workforce members and integrators must acknowledge this policy and the rules of behavior at hire or onboarding and annually. (PL-4; GV.RR-04)
4.2 All personnel with IT or OT access, including contractors, must complete security awareness training at onboarding and annually. At MTSA facilities, the training must cover the topics in 33 CFR 101.650(d)(1) and be completed within 5 days of system access and no later than 30 days after hire; anyone not yet trained must be escorted or monitored. (AT-2; PR.AT-01)
4.3 Operators, controls engineers, I&E technicians, and integrators must complete role-based OT security training annually; hazmat employees must complete security awareness and in-depth security training. (AT-3; PR.AT-02)
4.4 Personal devices, personal storage, and non-company laptops must never be connected to OT networks or devices. (AC-20; MP-7; PR.PS-05)
4.5 Users must not install software on company devices; OT software is installed only by administrators from the OT patch and media staging service. (CM-11; PR.PS-05)
4.6 Company information may be used with AI tools only if the tool is on the approved AI tools list (STD-05.3). Restricted information, including formulations, recipes, and SSI, must never be entered into a tool not approved for Restricted data. (AC-20; PL-4; GV.PO-01)
4.7 No AI system may write setpoints or commands to a control or safety system without approval by the AI governance committee and MOC, including a PHA of the change. (CM-3; AC-4; GV.RM-01)
4.8 Phishing and suspicious messages must be reported with the report button; users must never approve an MFA prompt they did not start. (AT-2; IR-6; PR.AT-01)
4.9 Email, chat, and file sharing must not be used to send Restricted data outside the company except through approved encrypted channels. (SC-8; AC-21; PR.DS-02)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-05.1 Acceptable Use of IT and OT Standard (rules of behavior)
- STD-05.2 External Systems and Personal Devices Standard
- STD-05.3 Approved AI Tools List

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring (including OT metrics), the annual Internal Audit assessment (P07), access certifications, and MTSA Cybersecurity Plan audits at PLT-01. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 GC-PCBMS SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
