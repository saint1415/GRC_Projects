# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (private career college) |
| Policy ID | POL-03 |
| Owner | IT Director (Qualified Individual) |
| Approved by | Campus President |
| Approved / effective | Approved 2026-08-21; effective 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), after every tabletop exercise, and after any security event (314.4(h)(7)) |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-03, ID.IM-04 |
| Regulatory basis | 16 CFR 314.4(h)(1)-(7) and 314.4(j) (N61-R02); SAIG Enrollment Agreement breach notice; FERPA 34 CFR 99.32 (N61-R01); Fla. Stat. 501.171 |

## 1. Purpose and goals of the plan (16 CFR 314.4(h)(1))
This policy and the incident response runbook (P08) together are the college's **written incident response plan** under 16 CFR 314.4(h). The plan has five goals:
1. Protect students and other consumers whose customer information or education records are at risk, and limit harm to them (for example, fraud or identity theft).
2. Contain a security event quickly and remove the attacker's access.
3. Restore student services within the recovery times in the BIA (P05), starting with registration, online instruction, and Title IV aid processing.
4. Meet every notification duty on time: FSA, the FTC, Florida, affected individuals, and the college's insurer.
5. Learn from each event and fix the weaknesses it exposed.

## 2. Scope
All Cris Santos Company workforce members: employees, full-time and adjunct faculty, contractors, and student workers. It also binds the financial aid servicer and other service providers through their contracts (POL-01 4.8). It covers any security event (16 CFR 314.2(q)) affecting college systems, customer information in any format, or education records.

## 3. Roles, responsibilities, and decision authority (16 CFR 314.4(h)(3))
| Role | Responsibility | Decides |
|---|---|---|
| IT Director (Qualified Individual) | Incident commander; directs containment, forensics, and recovery | Isolating systems, disabling accounts, engaging forensics through the insurer |
| Campus President | Executive lead; engages counsel and the cyber insurer; approves all external communications | Closing campus or moving classes online; notices to students, regulators, and the media, on counsel's advice |
| Board chair (majority owner) | Informed the same day for any declared incident | Any ransom payment decision (with counsel, the insurer, and an OFAC check); spending above the Campus President's authority |
| Director of Financial Aid | FSA point of contact; manages the servicer's response | Submitting the FSA breach report; pausing aid disbursements if data integrity is in doubt |
| Registrar (FERPA compliance officer) | Identifies affected education records; records unauthorized disclosures | Content of the FERPA disclosure record |
| Business Office Manager | Protects refunds and payments during an incident | Holding refund payment files |
| Outside breach counsel (insurer panel) | Legal advice; confirms each notification | Whether a notification event or Florida breach has occurred (advises the Campus President) |
| All workforce | Report suspected incidents immediately | None |

## 4. Policy statements
4.1 The college must maintain this policy and a runbook for its most likely severe incident, ransomware with student record exposure (P08). Both must describe the internal steps for detecting, analyzing, containing, eradicating, and recovering from a security event. (IR-8; IR-4; RS.MA-01; 314.4(h)(2))

4.2 **Reporting.** Workforce members must report any suspected incident **immediately**, and within 1 hour at most, to the IT Director's incident line or the IT help desk. Examples: a phishing click, a lost device, a misdirected spreadsheet, a ransom note, or unusual account activity. Service providers must report incidents affecting college data within 72 hours, as their contracts require (POL-01 4.8). Good-faith reporting is never sanctioned. (IR-6; RS.MA-02; 314.4(j)(2))

4.3 Every incident must be logged in the ticketing system under the Security category and tracked to closure. The log must record the discovery date, the actions taken with times and names, the evidence collected, and every notice sent. (IR-5; IR-6; RS.MA-02; 314.4(h)(6))

4.4 **Determinations.** For every incident that touches customer information or education records, the Qualified Individual, with counsel, must decide and document:
- whether a **notification event** occurred, meaning unencrypted customer information was acquired without authorization (16 CFR 314.2(m)). Unauthorized access is presumed to be acquisition unless there is reliable evidence it was not;
- how many consumers are affected;
- the **discovery date**: the first day the event was known to any employee, officer, or other agent of the college other than the person committing the breach (314.4(j)(2));
- whether a breach of personal information of Florida residents occurred (Fla. Stat. 501.171).

The Registrar must record any unauthorized disclosure of education records in the affected students' disclosure records (34 CFR 99.32). (IR-6; RS.AN-03)

4.5 **Notifications.** Notices must meet the deadlines in the P08 notification matrix, including:
- FSA: immediately on an actual or suspected breach (SAIG Enrollment Agreement);
- the FTC: as soon as possible and no later than 30 days after discovery, if 500 or more consumers are involved (314.4(j)(1));
- Florida residents and the Florida Department of Legal Affairs: no later than 30 days after determination (Fla. Stat. 501.171).

Counsel must confirm each notice before it is sent. (IR-6; RS.CO-02; RS.CO-03; 314.4(h)(4), (j))

4.6 No ransom may be paid without approval from the Board chair, counsel, and the cyber insurer, and an OFAC sanctions check. (IR-4)

4.7 The plan must be tested at least annually by a tabletop exercise that includes the financial aid office and the business office, and after any major incident. (IR-3; ID.IM-02)

4.8 **Lessons learned.** A lessons-learned review must be documented within 30 days of closing an incident. It must identify the weaknesses in systems and controls that the incident exposed, set remediation requirements with owners and dates in the POA&M (P07), and update this plan and the runbook as needed. The results go into the next Board report (314.4(i)(2)). (IR-4; ID.IM-03; ID.IM-04; 314.4(h)(5), (h)(7))

4.9 Printed copies of the runbook, contact list, and notification matrix must be kept in the incident binder in the IT office and the Campus President's office, because email may be unavailable during an incident. Electronic copies must be restricted to incident responders. (IR-8)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.10). Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07) and the annual tabletop exercise.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. They must be written, risk-rated, approved at the level in POL-01 4.4, and expire within 12 months.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; POL-01; BIA (P05); FTC Safeguards Rule 16 CFR 314.4(h)-(j); SAIG Enrollment Agreement; Fla. Stat. 501.171
