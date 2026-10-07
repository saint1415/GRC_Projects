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
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions. CIP-003-9 R1 content is also approved by the CIP Senior Manager at least once every 15 calendar months |
| Implements (SP 800-53 Rev. 5) | PL-4, AT-2, AT-3, CM-7, MP-7, SI-3, AC-19, AC-20, PS-3, SA-9 |
| CSF 2.0 | PR.AT-01, PR.AT-02, PR.PS-01, GV.RR-04 |
| Regulatory basis | CIP-004-7 R1 to R3; CIP-010-4 R4; CIP-003-9 Attachment 1 Sections 1 and 5; FERC Security Program 4.2, Table 9.3a, Form 3 Q17 |

## 1. Purpose
Set the rules every workforce member follows when using company systems, OT consoles, removable media, and AI tools, and the training and screening needed before access.

## 2. Scope
All Cris Santos Company workforce members (employees, seasonal staff, contractors, and interns) at the headquarters, 14 offices, two Hydro Operations Centers, the Contract Operations Center, and all 46 developments in Georgia, Alabama, North Carolina, South Carolina, Tennessee, and Virginia, including the Piedmont developments from their acquisition date. Covers all systems and data: IT, OT (fleet SCADA, plant control, spillway and gate control, dam safety instrumentation and warning), cloud, colocation, SaaS, and systems that vendors operate for the company, and the services the company offers to external clients (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Human Resources Officer | Owns this policy; training and personnel risk assessments |
| Director, OT Security | Removable media and Transient Cyber Asset rules |
| Chief Risk Officer | Chairs the AI council intake process |
| Managers | Make sure staff complete training and follow the rules |
| All workforce | Acknowledge and follow the rules |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategories. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Rules of behavior must be acknowledged at hire and annually. (PL-4; GV.PO-01)
4.2 Annual security awareness is required for all staff; staff with CIP access must receive security awareness each calendar quarter and complete role-based CIP training before access and at least every 15 calendar months. (AT-2; AT-3; PR.AT-01; PR.AT-02)
4.3 OT consoles, servers, and engineering workstations must be used only for control functions: no email, web browsing, personal media, or unapproved software. (CM-7; PL-4; PR.PS-01; GV.PO-01)
4.4 Removable media and laptops, including contractor devices, must be scanned at a company kiosk before connecting to any OT asset, and the scan must be logged. (MP-7; SI-3; PR.DS-01; PR.DS-02)
4.5 Personal devices must not connect to OT networks; company phones are used for out-of-band coordination only. (AC-19; AC-20; PR.AA-05; ID.AM-02; ID.AM-04)
4.6 Only AI tools on the approved list (STD-05.3) may be used for company work, and every new AI use must be registered with the AI council before use. (PL-4; SA-9; GV.PO-01; GV.SC-04; GV.SC-05)
4.7 Staff must report suspicious activity at projects, including drones, photography of security features, and unknown devices, to security dispatch at once. (IR-6; PE-6; RS.MA-01; RS.MA-02; PR.AA-06)
4.8 A personnel risk assessment, including identity confirmation and a seven-year criminal history check, must be completed before CIP access and repeated at least every 7 years. (PS-3; GV.RR-04)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-05.1 Awareness and Training Standard
- STD-05.2 Removable Media, Transient Cyber Asset, and Personal Device Standard
- STD-05.3 Approved AI Tools and AI Intake Standard
- PRC-05.1 Personnel Risk Assessment Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the NERC internal controls program, the annual Internal Audit assessment (P07), and access verifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. An exception cannot excuse a NERC CIP requirement.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 HFCDMS SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
