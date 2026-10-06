# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Owner | Security Manager |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 plan's policy section) |
| Review cycle | Annually (next review 2027-09-30), and after every major incident or exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-7, IR-8, CP-2, CP-4 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, RC.CO-03, ID.IM-02 |
| CISA CPG 2.0 and other rules | CPG 1.C, 4.B, 5.A, 5.B, 6.A; Fla. Stat. 501.171(3)-(6); PCI DSS v4.0.1 Req. 12.10.1 |
| Supporting standards | STD-03 Logging and monitoring standard; STD-08 Contingency and recovery standard |

## 1. Purpose
Make sure the company detects, contains, reports, and recovers from security incidents in IT and building systems quickly, keeps occupants safe, and meets every legal and contractual notice deadline.

## 2. Scope
All security incidents and suspected incidents affecting company systems, building systems, or vendors that hold company, tenant, visitor, or employee data or that have access to building systems; and outages of the access control and video platform or other services that support High-criticality processes (P05).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Security Manager | Incident commander for security incidents; coordinates the MSSP and forensics |
| Vice President of Engineering (OT safety lead) | Decides on any action affecting building equipment; directs chief engineers |
| Director of Security Operations (physical security lead) | Doors, officers, SCC, and the access control platform during incidents |
| IT Director | Technical recovery lead; contingency plan owner |
| Chief Operating Officer | Chairs the crisis management team; approves external statements |
| General Counsel | Breach determinations; decision log; directs outside counsel |
| Outside breach counsel (insurer panel) | Directs the investigation under privilege where appropriate; confirms each notice |
| Director of Marketing and Communications | Tenant, media, and staff communications through counsel |
| MSSP | 24x7 detection, first containment on IT systems, escalation within 30 minutes for high severity |
| Everyone | Report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain an incident response plan and runbooks for its most likely and most harmful incidents. At minimum these are ransomware on building automation systems and a compromise or extended outage of the access control and video platform (P08). (IR-8; RS.MA-01; CPG 1.C)
4.2 Anyone must report a suspected incident **immediately**, and within 1 hour at most, to the IT service desk security line or the SCC. Examples: phishing clicks, unexpected setpoint or door schedule changes, ransom notes, unexplained remote sessions, lost devices, card data found where it should not be. Good-faith reporting is never sanctioned. (IR-6; RS.MA-02)
4.3 Every incident must be logged, categorized by severity, and tracked to closure in the security incident queue. **The date and time of discovery must be recorded when the incident is opened.** (IR-5; IR-4)
4.4 A severity 1 incident (any ransomware, confirmed access to personal information, loss of control of doors or building equipment at a property, or an outage expected to exceed a High-criticality MTD) must activate the crisis management team, chaired by the COO, within 2 hours. (IR-4; RC.RP-01)
4.5 **Occupant safety first.** Chief engineers may take local hand control of plant equipment at any time. Nobody may power off, reset, or reload field controllers, door controllers, or recorders during an incident without the OT safety lead's approval, because doing so can destroy evidence and the only copy of a program. (IR-4; CP-2)
4.6 The General Counsel, with outside counsel, must decide whether an incident is a breach under Fla. Stat. 501.171 and any other applicable law, record **the date of the determination** in the decision log, and keep the log and any written no-harm determination for at least 5 years. (IR-6; RS.AN-03)
4.7 Notices to individuals, the Florida Department of Legal Affairs, consumer reporting agencies, tenants under lease clauses, the JV partner, lenders, the acquirer, and the cyber insurer must meet the deadlines in the P08 notification matrix. Outside counsel must confirm each legal notice. (IR-6; RS.CO-02; RS.CO-03)
4.8 The cyber insurer must be notified through its hotline before incident response vendors are engaged, as the policy requires. (IR-7)
4.9 No ransom may be paid without approval from the CEO, outside counsel, and the insurer, a documented OFAC sanctions check, and a report to law enforcement. (IR-4)
4.10 Severity 1 ransomware and any other significant cyber incident must be reported voluntarily to CISA and the FBI within 24 hours of declaration, through counsel, unless counsel advises otherwise in writing. (IR-6; CPG 5.B)
4.11 Each runbook must be exercised at least annually, including at least one exercise a year with outside counsel and the executive team. Chief engineers and SCC shift leads must take part in the OT and access platform exercises. (IR-3; ID.IM-02)
4.12 **Contingency.** The BAACS must have a contingency plan and written degraded-mode procedures at every property, and backups of BAS servers and controller programs must be restore-tested at least quarterly (STD-08). (CP-2; CP-4; CPG 3.O, 6.A)
4.13 Lessons learned must be documented within 30 days of closing a severity 1 incident and fed into the risk register (P01) and the POA&M (P07). (IR-4; ID.IM)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.15. Compliance is checked through the annual independent assessment (P07) and exercise reports.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. No exception may extend a legal or contractual notice deadline.

## 7. Related documents
P08 `ir-runbook.md`, `ir-runbook-access-platform.md`, and `notification-matrix.csv`; POL-01; STD-03; STD-08; Fla. Stat. 501.171; OFAC ransomware advisory (2021-09-21)
