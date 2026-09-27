# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Owner | Security Manager |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2023 policy) |
| Review cycle | Annually (next review 2027-09-30), and after every major incident or exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-7, IR-8, CP-2 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, RC.CO-03, ID.IM-02 |
| HIPAA and other rules | 164.308(a)(6); 164.400-164.414; Fla. Stat. 501.171; 42 CFR 416.54 (ASC) |
| Supporting standards | STD-02 Logging and monitoring standard; STD-07 Contingency and recovery standard |

## 1. Purpose
Make sure the company detects, contains, reports, and recovers from security incidents and major vendor outages quickly, keeps patients safe, and meets every legal and contractual notification deadline.

## 2. Scope
All security incidents and suspected incidents affecting company systems, data, or vendors that hold company data, and major outages of third-party services that support High or Moderate criticality processes (P05). It applies at all sites, including the ASC.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Security Manager | Incident commander for security incidents; coordinates the MSSP and forensics |
| IT Director | Technical recovery lead; contingency plan owner |
| Chief Operating Officer | Chairs the crisis management team for major incidents; approves external statements |
| Compliance and Privacy Officer | Breach risk assessment and notification decisions; maintains the decision log |
| Outside breach counsel (insurer panel) | Directs the investigation under privilege where appropriate; confirms each notification |
| Chief Medical Officer and ASC Administrator | Clinical downtime decisions; ASC emergency plan activation |
| Director of Marketing and Communications | Media, patient, and staff communications through counsel |
| MSSP | 24x7 detection, first containment, and escalation within 30 minutes for high severity |
| All workforce | Report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain an incident response plan and runbooks for its most likely and most harmful incidents. At minimum these are ransomware with PHI exfiltration and a major vendor or clearinghouse outage (P08). (IR-8; RS.MA-01)
4.2 Workforce members must report any suspected incident **immediately**, and within 1 hour at most, to the IT service desk security line or their manager. Examples: phishing clicks, lost devices, misdirected PHI, unusual device or system behavior. Good-faith reporting is never sanctioned. (IR-6; RS.MA-02; 164.308(a)(6)(ii))
4.3 Every incident must be logged, categorized by severity, and tracked to closure in the security incident queue. **The date and time of discovery must be recorded when the incident is opened.** (IR-5; IR-4)
4.4 A major incident (severity 1: any ransomware, confirmed PHI exfiltration, or an outage expected to exceed a High-criticality MTD) must activate the crisis management team, chaired by the COO, within 2 hours. (IR-4; RC.RP-01)
4.5 The Compliance and Privacy Officer must decide whether an incident is a reportable breach under 45 CFR 164.402, document the four-factor risk assessment in the decision log, and retain it for 6 years. (IR-6; RS.AN-03; 164.414(b))
4.6 Notifications to individuals, HHS, the media, the Florida Department of Legal Affairs, consumer reporting agencies, the cyber insurer, contract partners, and law enforcement must meet the deadlines in the P08 notification matrix. Outside counsel must confirm each notification. (IR-6; RS.CO-02; RS.CO-03)
4.7 The cyber insurer must be notified through its hotline before incident response vendors are engaged, as the policy requires. (IR-7)
4.8 No ransom may be paid without approval from the CEO, outside counsel, and the insurer, a documented OFAC sanctions check, and a report to law enforcement. (IR-4)
4.9 During any incident that affects the ASC, the ASC Administrator must decide whether to activate the ASC emergency plan, and must document the decision. (CP-2; 42 CFR 416.54)
4.10 Incident response must be exercised at least annually for each runbook, including at least one exercise a year with outside counsel and the executive team. The ASC must include a cyber scenario in its emergency preparedness exercises. (IR-3; ID.IM-02)
4.11 Lessons learned must be documented within 30 days of closing a major incident and fed into the risk register (P01) and the POA&M (P07). (IR-4; ID.IM)

## 5. Compliance and enforcement
Violations are handled under the HIPAA sanctions procedure (POL-01 section 4.8). Compliance is checked through the annual independent assessment (P07) and exercise reports.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. No exception may extend a legal notification deadline.

## 7. Related documents
P08 `ir-runbook.md`, `ir-runbook-vendor-outage.md`, and `notification-matrix.csv`; POL-01; STD-02; STD-07; ASC emergency preparedness plan; HIPAA Breach Notification Rule; Fla. Stat. 501.171
