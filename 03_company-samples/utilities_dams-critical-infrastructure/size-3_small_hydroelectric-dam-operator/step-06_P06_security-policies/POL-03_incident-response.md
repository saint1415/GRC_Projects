# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | Chief Dam Safety Engineer (reporting) and Plant Manager (OT response) |
| Approved by | Vice President of Operations |
| Effective date | 2026-09-01 |
| Review cycle | Annually each November (next review 2027-11-15), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8, CP-2 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.MA-04, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| FERC and Part 12 | 18 CFR 12.10(a) and 12.3(b)(4)(xi); Security Program Rev. 3A 3.2, 4.2, 7.4.1, Table 9.3a (intrusion detection and response), Form 3 Q25-28 |

## 1. Purpose
Make sure the company detects, contains, reports, and recovers from physical and cyber security incidents quickly and lawfully, keeps the dam under control throughout, and meets its FERC reporting duties.

## 2. Scope
All Cris Santos Company workforce members (employees, seasonal staff, contractors, and vendors with access). Covers the PCDMS (OT), the corporate network, SaaS and cloud services, the project works, and company information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Operations Supervisor on shift | Incident commander for OT and physical incidents until the Plant Manager takes over; puts gates and units in local control |
| Plant Manager | OT incident commander; decides on isolating the control network |
| Chief Dam Safety Engineer | Decides whether the event is a condition affecting safety (18 CFR 12.10); EAP activation; FERC reports |
| Compliance and Security Coordinator | Law enforcement contact; suspicious activity reports; FERC security contact |
| IT Manager | Incident commander for IT-only incidents; evidence from IT and cloud systems |
| Vice President of Operations | Engages counsel and the cyber insurer; approves external statements |
| All workforce | Report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain an incident response plan and runbooks for its most serious incidents, starting with unauthorized access to spillway and turbine control systems (P08). (IR-8; RS.MA-01)
4.2 **Safety first.** In any suspected OT incident, the first action is to place affected gates and units under local control and confirm their physical positions. No investigation step may delay that. (IR-4; CP-2)
4.3 Workforce members must report any suspected incident **immediately**, and within 15 minutes at most for anything touching gates, units, instruments, or the control room: unexpected gate movement, unknown sign-ins, strange HMI behavior, lost badges or keys, suspicious people, drones, or questions about the dam. Good-faith reports are never punished. (IR-6; RS.MA-02)
4.4 The Chief Dam Safety Engineer must decide promptly whether an incident is a condition affecting the safety of the project. **Security incidents (physical and/or cyber) and any misoperation of a gate are such conditions** (18 CFR 12.3(b)(4)(ii), (xi)) and must be reported to the FERC Regional Engineer by email or telephone as soon as practicable, preferably within 72 hours, followed by a written report when the Regional Engineer directs (12.10(a)). (IR-6; RS.CO-02)
4.5 Suspicious activity and security incidents must also be reported to the FERC Regional Office as soon as practical (usually within one working day), unless law enforcement restricts it, and should be entered in the HSIN suspicious activity tool (Rev. 3A 3.2, 4.2). (IR-6; RS.CO-03)
4.6 If an incident could lead to a project emergency, the EAP must be activated under its own procedures. Law enforcement (the sheriff) and county emergency management must be called in parallel, as the Internal Emergency Response sub-element describes (Rev. 3A 7.4.1). (IR-4; CP-2; RS.MA-04)
4.7 Other notices (FBI, CISA, the offtaker, the cyber insurer, affected dam owners in the basin, and any breach notices for personal information) must follow the P08 notification matrix. Counsel must confirm notices other than safety reports, which must never wait for counsel. (IR-6; RS.CO-02)
4.8 Every incident must be logged, categorized, and tracked to closure, and evidence (logs, HMI event journals, PLC logic copies) must be preserved with chain of custody. (IR-5; RS.AN-07)
4.9 No ransom may be paid without approval from the President, counsel, and the cyber insurer, and an OFAC sanctions check. (IR-4)
4.10 The incident response plan must be exercised at least once a year with law enforcement and county emergency management, alternating physical and cyber scenarios, and after any major incident. (IR-3; ID.IM-02; Rev. 3A Form 3 Q26)
4.11 Lessons learned must be documented within 30 days of closing an incident and fed into the risk register, the Security Plan, and the POA&M. (IR-4; ID.IM-03; Rev. 3A Form 3 Q27-28)

## 5. Compliance and enforcement
Violations are handled under the company's disciplinary procedure (POL-01 section 5). Failing to report a known incident is a serious violation. Compliance is checked through the annual exercise and control assessment (P07).

## 6. Exceptions
Exceptions follow POL-01 section 4.8. No exception may delay local control of gates or a report under 18 CFR 12.10.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; Emergency Action Plan; FERC Security Plan (Internal Emergency Response sub-element); Owner's Dam Safety Program; POL-01
