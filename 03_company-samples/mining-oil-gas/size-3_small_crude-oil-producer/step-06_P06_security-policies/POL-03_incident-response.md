# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | IT Manager |
| Approved by | CFO and VP Operations |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.MI-01, RS.AN-07, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02, ID.IM-03 |
| Benchmark (N21-BM) | SP 800-82 Rev. 3 sections 3.3.8 (incident response capability), 6.4 (Respond), 6.5 (Recover) |

## 1. Purpose
Make sure the company detects, contains, reports, and recovers from security incidents quickly, safely, and lawfully, including incidents that threaten the SCADA system and field operations.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, contractors, and temporary workers) at headquarters, both field offices, the OCC, and every well site and facility. Covers all business IT and OT systems, including systems that vendors operate for the company.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| IT Manager | Incident commander for security incidents; coordinates the MDR service and forensic firm |
| SCADA and Automation Supervisor | Leads OT analysis and containment; coordinates the SCADA integrator |
| VP Operations | Decides on operational changes (manual operations, shut-ins) with the Field Superintendents |
| CFO | Engages counsel and the cyber insurer; approves external communications and notifications |
| HSE and Regulatory Manager | Environmental and safety reporting if an incident causes a release |
| All workforce | Report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain an incident response plan and runbooks for its most likely incidents, starting with ransomware spreading from business IT toward SCADA (P08). The plan must be linked to the field manual-operations procedure in the emergency response plan. (IR-8; RS.MA-01)
4.2 Workforce members must report any suspected incident **immediately**, and within 1 hour at most, to the IT help line or, in the field, to their supervisor. Production Controllers must report unexplained HMI behavior (setpoints changing, commands they did not issue, unfamiliar screens) to the OCC shift lead and the SCADA and Automation Supervisor at once. Good-faith reporting is never sanctioned. (IR-6; RS.MA-02)
4.3 Every incident must be logged, categorized, and tracked to closure in the help desk under the Security category. (IR-5)
4.4 **Authority to isolate.** The IT Manager, with the VP Operations, may disconnect the SCADA network from the corporate network and the cloud at any time to contain an incident. If neither can be reached within 15 minutes and ransomware is spreading, the OCC shift lead may do so. Shut-in decisions remain with the Field Superintendents under the emergency response plan. (IR-4; RS.MI-01)
4.5 Evidence must be preserved before systems are rebuilt, where doing so does not delay safety actions: logs, disk images, HMI screenshots, and copies of controller programs. (IR-4; RS.AN-07)
4.6 Notifications to regulators, individuals, law enforcement, the insurer, and business partners must meet the deadlines in the P08 notification matrix, including Fla. Stat. 501.171 and oil discharge reporting to the National Response Center. Counsel must confirm each legal notification. (IR-6; RS.CO-02)
4.7 No ransom may be paid without approval from the majority owner, legal counsel, and the cyber insurer, and an OFAC sanctions check. (IR-4)
4.8 The incident response plan must be tested at least annually by a tabletop exercise that includes IT, the OCC, field operations, and the SCADA integrator, and after any major incident. (IR-3; ID.IM-02)
4.9 Lessons learned must be documented within 30 days of closing an incident and added to the risk register. (IR-4; ID.IM-03)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.8). Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07) and the access reviews in this policy set.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; POL-01; Emergency Response Plan; Fla. Stat. 501.171; 40 CFR 110.6
