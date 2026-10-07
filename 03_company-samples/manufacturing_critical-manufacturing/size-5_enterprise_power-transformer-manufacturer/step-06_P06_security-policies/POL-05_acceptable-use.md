# Acceptable Use Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-05 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Chief Human Resources Officer |
| Approved by | Executive risk committee |
| Approval date | 2026-09-08 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | PL-4, AT-2, AT-3, AC-20, MP-7, CM-11 |
| CSF 2.0 | GV.PO-01, PR.AT-01, PR.AT-02, PR.PS-05 |
| Binding requirements served | FAR 52.204-21(b)(1)(iii), (iv) |

## 1. Purpose
Set clear rules for how workforce members use company systems, plant equipment, removable media, personal devices, and AI tools.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, temporary workers, and interns) at all 7 plants, 9 service centers, 3 spare yards, and offices in Florida, Georgia, Tennessee, Texas, North Carolina, and Ohio, including the acquired Ohio plant (AQ-01) from its acquisition date. Covers all systems and data, including cloud, colocation, SaaS, plant control systems (OT), test systems, and systems that suppliers operate for the company, and the products and services the company supplies to utilities (TMU firmware and configuration software, the Fleet Monitoring Service, and the Spare Transformer Reserve Service).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Human Resources Officer | Owns this policy and training records |
| Managers and plant supervisors | Make sure their teams follow it |
| CISO | Approved tools lists and technical enforcement |
| All workforce | Follow it and report problems |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Workforce members must use company systems only for authorized purposes and must acknowledge this policy at hire and annually. (PL-4; GV.PO-01)
4.2 All workforce members must complete security awareness training annually (shift briefings for production workers), and staff in OT, administrator, and field roles must complete role-based training before access and annually. (AT-2; AT-3; PR.AT-02)
4.3 Personal devices may reach only company email and files through managed apps and must never connect to plant networks. (AC-20; PR.AA-05)
4.4 USB storage must not be used on HMIs, engineering workstations, or kiosks; OEM media must be scanned at a plant media kiosk before use. (MP-7; PR.PS-05)
4.5 Workforce members must not install software; only software from the approved catalog may be installed by IT or controls engineering. (CM-11; PR.PS-05)
4.6 Only AI tools on the approved list (STD-05.3) may be used; any new AI use, including AI features in existing products, must be registered before use; AI output must be reviewed by a person, and must not be used to change maintenance intervals, safety settings, or employment decisions without AI governance committee approval. (PL-4; SA-9; GV.PO-01)
4.7 Workforce members must report phishing and suspicious events through the report button or the SOC hotline. (IR-6; RS.MA-02)
4.8 Workforce members must not post company, customer, or federal contract information on public websites or social media. (AC-22; PR.DS-01)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-05.1 Security Awareness and Training Standard
- STD-05.2 External Systems and Personal Devices Standard
- STD-05.3 Approved AI Tools List
- STD-05.4 Removable Media and Plant Floor Devices Standard

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 EPSP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
