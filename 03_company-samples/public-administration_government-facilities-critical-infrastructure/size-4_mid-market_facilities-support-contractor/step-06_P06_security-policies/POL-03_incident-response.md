# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Owner | Security Manager |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 plan) |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-7, IR-8 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| Contract and legal drivers | County A addendum (6 hours for suspected ransomware, 24 hours otherwise); state, County B, and City contracts (24 hours); school district (48 hours); GSA contract (immediate report to GSA IT, BTTRG section 1.6.1; FAR 52.204-25(d) 1 business day; 52.204-23(c) and 52.204-30(c) 3 business days); Fla. Stat. 501.171(6)(a) (third-party agent notice within 10 days); Fla. Stat. 282.3186 |

## 1. Purpose
Make sure the company detects, contains, reports, and recovers from security incidents quickly, meets every customer and legal notice deadline, and never leaves a customer building unsafe or unsecured while doing so.

## 2. Scope
All workforce members and subcontractors. Covers incidents affecting company systems, the IFOP, customer building systems the company operates or maintains, customer data held by the company, and company staff conduct on GSA systems.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Crisis management team (CMT), chaired by the COO | Business decisions, customer and public communications, ransom recommendation to the CEO |
| Security Manager | Incident commander for security incidents |
| VP Operations | Operations lead: building safety, manual-mode procedures, technician dispatch, ROC |
| Director of Building Technology | OT technical lead (BAS and access control) |
| General Counsel | Breach determinations, legal privilege, regulator and contract notices, the notice log |
| Program managers | Customer notices within contract deadlines; coordination with customer security staff |
| Contracts Director | FAR clause reports and subcontractor notices |
| MSSP | 24x7 detection, first containment for IT, escalation within 30 minutes |
| All workforce | Report suspected incidents immediately |

## 4. Policy statements
4.1 The company must keep an incident response plan and runbooks for its most likely and most harmful incidents, starting with intrusion into building access control and automation systems and with ransomware (P08). (IR-8; RS.MA-01)
4.2 Workforce members and subcontractors must report any suspected incident **immediately, and within 1 hour at most**, to the ROC line. Examples: unexpected door unlocks or schedule changes, unknown remote sessions, setpoint changes nobody made, unknown devices or modems in panels, lost laptops or PIV cards, misdirected drawings, phishing clicks. Good-faith reporting is never sanctioned. (IR-6; RS.MA-02)
4.3 **Safety first.** If an incident affects doors, critical facilities, life-safety-related building functions, or environmental conditions, the operations lead must put the affected building into a safe state (manual mode, doors secured, customer security staff informed) before technical investigation continues. (IR-4)
4.4 Every incident must be logged, categorized, and tracked to closure in the incident log. (IR-5)
4.5 Incidents rated severity 1 (a confirmed intrusion into customer OT, ransomware, or a breach of customer personal information or CUI) must be escalated to the CMT within 1 hour of declaration. (IR-4; RS.MA-02)
4.6 **Customer notice.** The program manager, with General Counsel, must notify the affected customer within the contract deadline: County A within 6 hours of discovering suspected ransomware and 24 hours for other incidents; the state, County B, and the City within 24 hours; the school district within 48 hours; and GSA immediately for anything touching GSA systems, GSA data, or company staff with GSA access. Notice must come early enough for state and local customers to meet their own 12-hour (ransomware) and 48-hour reports to the state (Fla. Stat. 282.3185(5); 282.318(3)(c)9.c.). (IR-6; RS.CO-02)
4.7 Legal notices (for example Fla. Stat. 501.171 notices, other states' breach notices, and FAR clause reports) must follow the P08 notification matrix. General Counsel must decide each breach determination and keep the decision log with the times of discovery and determination. (IR-6; RS.CO-03)
4.8 No ransom may be paid without approval from the CEO, General Counsel, and the cyber insurer, and an OFAC sanctions check. The company must never pay on a customer's behalf; Florida state agencies, counties, and municipalities may not pay or otherwise comply with a ransom demand (Fla. Stat. 282.3186). (IR-4)
4.9 The plan must be tested at least annually by a tabletop exercise that includes at least one customer, and after any major incident. Each runbook must be exercised at least every 2 years. (IR-3)
4.10 Incident responders, ROC operators, program managers, and Building Technology staff must receive incident response training within 30 days of assignment and annually. (IR-2)
4.11 Lessons learned must be documented within 30 days of closing a severity 1 or 2 incident and fed into the risk register and POA&M. (IR-4; ID.IM-02)
4.12 Evidence must be preserved with chain of custody. For incidents that may lead to claims or notices, General Counsel engages forensic firms so their work is done at counsel's direction. (IR-4; RS.AN-03)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.8). Compliance is checked through the annual control assessment (P07), each exercise, and the notice log.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. No exception may extend a contract or legal notice deadline.

## 7. Related documents
P08 runbooks and notification matrix; POL-01; POL-02; customer contracts; GSA BTTRG section 1.6
