# Acceptable Use Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-05 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Chief Human Resources Officer, with the CISO |
| Approved by | Executive risk committee |
| Approval date | 2026-09-08 (version 2026.1) |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30) |
| Implements (SP 800-53 Rev. 5) | PL-4, PL-4(1), AT-2, AT-3, MP-7, CM-11, AC-8 |
| CSF 2.0 | GV.PO-01, PR.AT-01, PR.AT-02, PR.PS-05 |
| Regulatory drivers | SD Pipeline-2021-02G Sections III.D.1.d and V.A.2 (C-ENERGY-R03); 49 CFR 192.631(h) (C-ENERGY-R04); SEC insider trading rules (disclosure controls) |

## 1. Purpose
Set the rules every worker follows when using company systems, including the stricter rules for control rooms and OT devices, and the company's rules for AI tools.

## 2. Scope
All employees, contractors, and supplier personnel who use company IT or OT systems, in any location.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Human Resources Officer | Acknowledgments, training records, and HR sanctions |
| CISO | Training content, phishing exercises, approved AI tools list (with the AI governance committee) |
| Vice President, Gas Control | Controller cyber training in the simulator |
| Managers | Make sure their staff complete training and follow this policy |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Company systems are for company business; limited personal use of business IT is allowed if it creates no risk. No personal use of any kind is allowed on SCADA consoles, station HMIs, or engineering workstations. (PL-4; GV.PO-01)
4.2 Every worker must acknowledge this policy before receiving access and every year after. (PL-4(1); PR.AT-01)
4.3 Security awareness training is required at hire and every year, with at least quarterly phishing exercises. Role-based training is required for controllers (cyber-caused abnormal operating conditions in the simulator, every year), OT engineers and administrators (ICS security, every two years), and disclosure committee members (every year). (AT-2; AT-3; PR.AT-01; PR.AT-02)
4.4 Only company-owned transient devices that have been scanned at an OT media kiosk the same day may connect to OT. Personal devices and supplier laptops must never be connected to OT networks. (MP-7; PR.PS-05)
4.5 Workers must not install software, browser extensions, or remote access tools unless IT or OT engineering approves them. (CM-11; PR.PS-05)
4.6 Workers must report suspicious messages with the report button and report lost devices and unexpected system behavior at once (POL-03 statement 4.2). (AT-2; PR.AT-01)
4.7 Only AI tools on the approved list (STD-05.3) may be used for company work, and every new AI use case, including AI features switched on inside existing products, must be registered with the AI governance committee before use. The leak-detection model is an advisory tool for controllers and is governed by P10. (PL-4; GV.PO-01)
4.8 Workers with knowledge of a potential material cybersecurity incident must keep it confidential and must not trade in company securities until it is public or the General Counsel lifts the restriction. (PL-4; GV.PO-01)
4.9 System use notices shown at sign-in apply to everyone. Use of company systems may be monitored. (AC-8; GV.PO-01)

## 5. Standards and procedures under this policy
- STD-05.1 Security Awareness and Training Standard
- STD-05.2 Transient Device and Removable Media Standard
- STD-05.3 AI Use Standard (approved AI tools list and intake)

## 6. Compliance and enforcement
Compliance is monitored through acknowledgment and training reports, phishing results, kiosk logs, web proxy blocks of unapproved AI domains, and the annual Internal Audit assessment (P07). Violations are handled under PRC-01.1 (POL-01 statement 4.16).

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2. Statement 4.1's ban on personal use of OT devices and statement 4.4 cannot be excepted.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P10 AI governance and inventory.
