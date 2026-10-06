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
| Implements (SP 800-53 Rev. 5) | PL-4, AT-2, AT-3, AC-20, MP-7, SC-7, SR-9 |
| CSF 2.0 | PR.AT-01, PR.AT-02, PR.IR-01, PR.DS-10, DE.CM-02 |
| Other requirements | PCI DSS v4.0.1 9.5.1.3, 12.2, 12.6; HIPAA 164.308(a)(5), 164.310(b) for SL-2 |

## 1. Purpose
Set the rules every workforce member follows when using company technology and handling customers' devices.

## 2. Scope
All workforce members and contractors, on company systems and wherever they handle customer devices.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Human Resources Officer | Policy owner; training and acknowledgments |
| Store and depot managers | Enforce the rules on the floor |
| CISO | Approved tools lists |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Every workforce member must acknowledge this policy at hire and every year. (PL-4; PR.AT-01)
4.2 Every workforce member must complete annual security awareness training and take part in phishing simulations; technicians, agents, developers, and administrators must complete role-based training. (AT-2; AT-3; PR.AT-01)
4.3 Customer devices may be connected only to bench workstations on the customer device network, never to office PCs, counter tablets, or personal devices. (AC-20; SC-7; PR.IR-01)
4.4 Personal phones must not be used to photograph customer device content, and removable media may be used only at registered data transfer stations. (MP-7; PR.DS-10)
4.5 Only approved AI tools on STD-05.3 may be used for company work, and any new AI feature must be registered in the AI inventory before use. (SA-9; PL-4; GV.PO-01)
4.6 Company data may be stored or processed only in approved systems listed in STD-05.2. (AC-20; PR.AA-05)
4.7 Store staff must inspect PIN pads weekly, report signs of tampering at once, and verify the identity of anyone who asks to service a payment device. (SR-9; PE-3; DE.CM-02)
4.8 Contact center agents must use the consent prompt at the start of recorded calls and pause recording for any payment taken outside the DTMF masking service. (PL-4; GV.OC-03)
4.9 Lost or stolen company devices and suspected incidents must be reported immediately. (IR-6; RS.MA-02)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-05.1 Security Awareness and Training Standard
- STD-05.2 External Systems and Personal Devices Standard
- STD-05.3 Approved AI Tools List
- PRC-05.1 Bench Workstation Use Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, access certifications, the annual Internal Audit assessment (P07), and the annual PCI DSS ROC. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions to this policy follow the process in POL-01 section 7 and `policy-hierarchy.md` section 5: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, limited to 12 months, and recorded in the exception register with compensating controls.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 STPP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
