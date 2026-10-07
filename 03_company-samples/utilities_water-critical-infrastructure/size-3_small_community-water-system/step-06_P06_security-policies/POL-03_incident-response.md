# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | IT Manager |
| Approved by | General Manager |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8, CP-2 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| Regulatory basis | ERP plans and procedures, 42 U.S.C. 300i-2(b)(2)-(4); Tier 1 public notice, 40 CFR 141.202; customer data breach notice, Fla. Stat. 501.171 |

## 1. Purpose
Make sure the company detects, contains, reports, and recovers from cybersecurity incidents quickly and safely, keeps delivering safe water while it does, and meets public notification and breach notification deadlines.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, contractors, and interns) at WTP-1, WTP-2, the administration office, and remote sites. Covers all systems and data, including operational technology (the Water Treatment SCADA System, PLCs, RTUs, and telemetry) and systems that service providers operate for the company.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| IT Manager | Incident commander for cybersecurity incidents; coordinates the integrator, insurer, and forensic support |
| Operations Manager | Treatment decisions, including switching to manual operation; OT recovery |
| Chief Plant Operator on duty | Immediate process safety actions at the plant |
| Water Quality Supervisor | Decides with the General Manager whether a Tier 1 notice is needed; leads primacy agency consultation |
| General Manager | Engages counsel and the cyber insurer; approves external communications |
| All workforce | Report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain an incident response plan and runbooks for its most likely incidents, starting with remote-access compromise of an HMI (P08). The plan and runbooks are part of the ERP. (IR-8; RS.MA-01; 300i-2(b)(2))
4.2 Workforce members must report any suspected incident **immediately**, and within 1 hour at most. Operators must report unexpected setpoint changes, HMI cursor movement they did not cause, unknown remote sessions, or unexplained alarms to the Chief Plant Operator and the incident line at once. Good-faith reporting is never sanctioned. (IR-6; RS.MA-02)
4.3 **Process safety comes first.** If there is any doubt about the integrity of SCADA control, the Chief Plant Operator must move affected processes to manual (local) control and verify chemical feed rates and water quality by grab sample before doing anything else. (CP-2; IR-4)
4.4 Every incident must be logged, categorized, and tracked to closure. (IR-5)
4.5 The Water Quality Supervisor and General Manager must decide as soon as practical whether the incident caused a failure or significant interruption in key treatment processes that requires a Tier 1 public notice. If so, the notice must go out and primacy agency consultation must start no later than 24 hours after the company learns of the situation (40 CFR 141.202(b)). (IR-6; RS.CO-02)
4.6 Other notifications (customers under Fla. Stat. 501.171 if personal information is involved, the cyber insurer, and voluntary reports to CISA and the FBI) must follow the P08 notification matrix. Legal counsel must confirm each legally required notice. (IR-6; RS.CO-03)
4.7 No ransom may be paid without approval from the majority owner, legal counsel, and the cyber insurer, and an OFAC sanctions check. (IR-4)
4.8 Evidence must be preserved before systems are rebuilt, where this does not delay process safety actions. (IR-4)
4.9 The incident response plan must be exercised at least annually by an OT cyber tabletop that includes the SCADA integrator, and after any major incident. (IR-3; ID.IM-02)
4.10 Lessons learned must be documented within 30 days of closing an incident and fed into the risk register, the RRA, and the ERP. (IR-4)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07) and the reviews in this policy set.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; ERP; POL-01; 40 CFR 141 Subpart Q; Fla. Stat. 501.171
