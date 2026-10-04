# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Owner | Information Security Manager |
| Approved by | Chief Information Officer |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2023 plan) |
| Review cycle | Annually (next review 2027-09-30), and after every major incident or exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-7, IR-8, CP-2, AU-6 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, RC.CO-03, ID.IM-02 |
| Safeguards Rule and other rules | 16 CFR 314.4(h)(1)-(7), (j); SAIG Enrollment Agreement; 34 CFR 668.16(g); 34 CFR 99.32; 34 CFR 668.46(g); state breach laws (Florida worked example: Fla. Stat. 501.171) |
| Supporting standards | STD-02 Logging and monitoring standard; STD-07 Contingency and recovery standard |

## 1. Purpose
Make sure the college detects, contains, reports, and recovers from security incidents and identity fraud quickly, protects students' records and money, keeps campuses safe, and meets every legal and contractual deadline. This policy and the P08 runbooks are the written incident response plan required by 16 CFR 314.4(h). **Goals of the plan (314.4(h)(1)):** protect people first, preserve teaching and aid processing within the BIA RTOs, limit exposure of customer information and education records, meet every notice deadline, and learn from each event.

## 2. Scope
All security incidents and suspected incidents affecting college systems or data, including data held by vendors and the third-party servicer, student account takeovers and refund fraud, fraudulent applicants, and outages of services that support High or Moderate criticality processes (P05). It applies at all campuses and online.

## 3. Roles and responsibilities (314.4(h)(3))
| Role | Responsibility |
|---|---|
| Information Security Manager | Incident commander for security incidents; coordinates the MSSP and forensics |
| Chief Information Officer | Technical recovery lead; IT DR plan owner; chairs the crisis management team for major incidents |
| President and Chief Executive Officer | Ransom decisions; campus closure decisions; informs the board and the PE sponsor |
| Chief Compliance Officer | Breach and notification decisions; FTC, FSA, and OIG filings; maintains the decision log |
| General Counsel and outside breach counsel (insurer panel) | Directs the investigation under privilege where appropriate; confirms each notification |
| vCISO (Qualified Individual) | Advises the crisis team; reports events to the board (314.4(i)(2)) |
| Director of Financial Aid and Bursar | Aid and refund continuity; fraud holds; FSA coordination |
| Director of Campus Safety | Emergency notification and campus safety during incidents |
| Director of Marketing and Communications | Student, staff, media, and partner communications through counsel |
| MSSP | 24x7 detection, first containment, and escalation within 30 minutes for high severity |
| All employees | Report suspected incidents immediately |

## 4. Policy statements
4.1 The college must maintain incident runbooks for its most likely and most harmful incidents. At minimum these are ransomware with student record exposure and student identity fraud (account takeover, refund diversion, and fraudulent applicants) (P08). (IR-8; RS.MA-01; 314.4(h)(2))
4.2 Employees must report any suspected incident **immediately**, and within 1 hour at most, to the IT service desk security line or their manager. Examples: phishing clicks, lost devices, misdirected records, a student reporting a missing refund, suspicious applications, unusual system behavior. Good-faith reporting is never sanctioned. (IR-6; RS.MA-02)
4.3 Every incident must be logged, categorized by severity, and tracked to closure in the security incident queue. **The date and time of discovery must be recorded when the incident is opened.** Knowledge of any employee, officer, or agent (other than the person committing the breach) counts as the college's knowledge for the FTC notice (314.4(j)(2)). (IR-5; IR-4; 314.4(h)(6))
4.4 A major incident (severity 1: any ransomware, confirmed exfiltration of customer information or education records, fraud affecting 10 or more students, or an outage expected to exceed a High-criticality MTD) must activate the crisis management team, chaired by the CIO, within 2 hours. (IR-4; RC.RP-01)
4.5 The Chief Compliance Officer must decide with counsel whether an event is a notification event under 16 CFR 314.2(m), a breach under each affected state's law, and a suspected breach to report to FSA, and must document each decision and the affected-consumer count in the decision log, kept for 6 years. (IR-6; RS.AN-03)
4.6 Notifications to the FTC, FSA, the Office of Inspector General, affected students and parents, state regulators and consumer reporting agencies, the cyber insurer, employer partners, and law enforcement must meet the deadlines in the P08 notification matrix. Outside counsel must confirm each notification. (IR-6; RS.CO-02; RS.CO-03; 314.4(h)(4); 314.4(j))
4.7 The cyber insurer must be notified through its hotline before incident response vendors are engaged, as the policy requires. (IR-7)
4.8 No ransom may be paid without approval from the President and CEO, outside counsel, and the insurer, a documented OFAC sanctions check, and a report to law enforcement. (IR-4)
4.9 Any incident that could affect the emergency notification service or campus security systems must be reported at once to the Director of Campus Safety, who confirms that Clery emergency notification remains available through the break-glass path. (CP-2; 34 CFR 668.46(g))
4.10 Any unauthorized disclosure of PII from education records must be recorded in the affected students' disclosure records under 34 CFR 99.32. (AU-6; RS.MA-02)
4.11 Incident response must be exercised at least annually for each runbook, including at least one exercise a year with outside counsel and the executive team. (IR-3; ID.IM-02)
4.12 Lessons learned must be documented within 30 days of closing a major incident, including the remediation of identified weaknesses, and fed into the risk register (P01) and the POA&M (P07). The plan is revised as needed after each event. (IR-4; ID.IM-04; 314.4(h)(5), (h)(7))

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.8. Compliance is checked through the annual independent assessment (P07), exercise reports, and the Qualified Individual's annual report.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. No exception may extend a legal or contractual notification deadline.

## 7. Related documents
P08 `ir-runbook.md`, `ir-runbook-identity-fraud.md`, and `notification-matrix.csv`; POL-01; STD-02; STD-07; Clery annual security report; 16 CFR 314.4(h) and (j)
