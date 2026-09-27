# Acceptable Use Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-05 |
| Owner | Chief Operating Officer |
| Approved by | Chief Operating Officer |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | PL-4, AT-2, AT-3, CM-7, CM-11, MP-7, AC-11 |
| CSF 2.0 | PR.AT-01, PR.AT-02, GV.PO-01 |
| CISA CPG 2.0 (voluntary) | 3.J, 3.M, 3.P, 3.R |
| Other drivers | PCI DSS v4.0.1 Req. 9.5.1.3, 12.1.3, 12.6 (SAQ P2PE) |

## 1. Purpose
Set clear, plain-language rules for how the workforce and contractors use company systems, building systems, devices, and data.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, and contractors), integrators, the MSP, and the guard contractor when they use company systems, devices, or networks, including engineering workstations, tablets, and security console PCs.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| HR Manager | Collects signed acknowledgments at hire and each year; tracks training |
| IT Manager | Awareness content, monthly reminders, phishing exercises; the approved software and AI lists |
| Director of Engineering and Security Manager | Role training for engineers and console operators |
| All workforce | Follow these rules |

## 4. Policy statements
4.1 Company systems are for company business. Limited personal use (for example, checking personal email on a break) is allowed on office laptops if it does not create risk. **No personal use of engineering workstations, BAS servers, or security console PCs.** (PL-4)
4.2 Every workforce member and contractor with system access must sign this policy before receiving access and again each year. (PL-4; PCI DSS 12.1.3)
4.3 **Training.** Security awareness training is required at hire and every year. The IT Manager sends monthly reminders and runs at least quarterly phishing exercises. Engineers and security console operators also complete annual OT security training: spotting unusual BAS behavior, safe manual operation, and remote access rules. Management office staff who take card payments complete terminal handling and tampering training each year. (AT-2; AT-3; PR.AT-01; PR.AT-02; CPG 3.J; PCI DSS 9.5.1.3; 12.6)
4.4 Lock your screen when you step away (security console PCs follow POL-02 4.10). Keep engineering rooms and the console room closed. (AC-11)
4.5 Do not install software, browser extensions, or firmware, and do not connect new devices to OT networks, unless IT (for corporate systems) or the Director of Engineering (for BAS) approves it. (CM-11; CM-7; CPG 3.P)
4.6 **USB and contractor laptops.** Do not connect USB drives to engineering workstations or the BAS server except company-issued drives that have been scanned. Contractor laptops must be scanned by IT before they connect to an OT network. Autorun is disabled on all company computers. (MP-7; CM-7; CPG 3.M; 3.R)
4.7 Do not open unexpected attachments or links. Report suspicious messages with the Report Phishing button. Call back any vendor that asks to change bank details, using a number from the contract file, never the number in the message. (AT-2)
4.8 **AI tools and analytics.** Use only AI tools and analytics features on the approved AI list kept by the IT Manager. Never paste Restricted or Confidential data into a tool that is not approved. Vendors may not turn on new analytics or biometric features without COO approval (POL-01 4.10, P10). (PL-4)
4.9 Report lost or stolen devices and badges, and anything suspicious, to the incident line immediately (POL-03 4.2). Inspect the payment terminals for tampering as the weekly checklist requires, and report any sign of tampering at once. (IR-6; PCI DSS 9.5.1.2)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.7). Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07), training records, and phishing exercise results.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months.

## 7. Related documents
POL-01; POL-03; POL-04; P10 approved AI list; training records; the P2PE Instruction Manual
