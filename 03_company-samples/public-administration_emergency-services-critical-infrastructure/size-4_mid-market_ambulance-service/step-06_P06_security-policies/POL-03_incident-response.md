# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Owner | Security Manager |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-16 |
| Effective date | 2026-10-01 (replaces the 2023 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes, significant incidents, or exercises |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-7, IR-8, CP-2, CP-2(5), CP-4 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, RC.CO-03, ID.IM-02 |
| HIPAA Security Rule and other rules | 164.308(a)(6), (a)(7); 164.400-164.414; Fla. Stat. 501.171 |
| Supporting standards | STD-02 Logging and monitoring standard; STD-07 Contingency and recovery standard |

## 1. Purpose
Make sure the company keeps dispatching through any incident, detects and contains incidents quickly, meets every legal and contractual notification deadline in both its covered entity and business associate roles, and recovers safely.

## 2. Scope
All security incidents and suspected incidents affecting company systems, data, or vendors that hold company or client data, and major outages of systems or vendors that support High or Moderate criticality processes (P05). It applies at both communications centers, all stations, and all vehicles.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Security Manager | Incident commander for security incidents; coordinates the MSSP and forensics |
| Director of Communications | Dispatch continuity lead; decides when to enter and leave manual mode |
| Director of IT | Technical recovery lead; contingency plan owner |
| Chief Operating Officer | Chairs the crisis management team; approves external statements |
| Compliance and Privacy Officer | Breach risk assessment and notification decisions, including notices to billing services clients; keeps the decision log |
| Outside breach counsel (insurer panel) | Directs the investigation under privilege where appropriate; confirms each notification |
| Medical Director | Clinical safety decisions during manual mode; reviews affected calls afterward |
| Director of Government Contracts | County notices and liaison |
| MSSP | 24x7 detection, first containment, and a call within 30 minutes for high severity |
| All workforce | Report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain an incident response plan and runbooks for its most likely and most harmful incidents. At minimum these are ransomware that disables CAD at both communications centers, and a breach at the billing platform vendor affecting company and client PHI (P08). (IR-8; RS.MA-01; 164.308(a)(6))
4.2 **Dispatch never waits for IT.** When CAD, consoles, or the CAD-to-CAD links fail, the on-duty communications supervisor must switch to manual dispatch at once and notify the County A PSAP of any outage longer than 15 minutes. (CP-2(5); CP-2; RC.RP-01; 164.308(a)(7)(ii)(C))
4.3 Workforce members must report any suspected incident **immediately**, and within 1 hour at most, to the service desk security line or their supervisor. Examples: phishing clicks, lost tablets or MDCs, misdirected records, unusual CAD or MDC behavior, station alerting faults. Good-faith reporting is never sanctioned. (IR-6; RS.MA-02; 164.308(a)(6)(ii))
4.4 Every incident must be logged, categorized by severity, and tracked to closure in the security incident queue. **The date and time of discovery must be recorded when the incident is opened.** (IR-5; IR-4; RS.MA-02; 164.308(a)(6)(ii))
4.5 A severity 1 incident (any ransomware, confirmed PHI exfiltration, a CAD outage expected to exceed the 1-hour RTO, or a vendor breach affecting PHI) must activate the crisis management team, chaired by the COO, within 2 hours. (IR-4; RC.RP-01; 164.308(a)(6)(ii))
4.6 The Compliance and Privacy Officer must decide whether an incident is a reportable breach under 45 CFR 164.402, document the four-factor risk assessment in the decision log, identify which affected individuals belong to each billing services client, and retain the log for 6 years. (IR-6; RS.AN-03; 164.402; 164.414(b))
4.7 Notifications to individuals, HHS, the media, the Florida Department of Legal Affairs, consumer reporting agencies, billing services clients, the counties, the cyber insurer, and law enforcement must meet the deadlines in the P08 notification matrix. Outside counsel must confirm each notification. (IR-6; RS.CO-02; 164.404-164.410; Fla. Stat. 501.171)
4.8 The cyber insurer must be notified through its hotline before incident response vendors are engaged, as the policy requires. (IR-7; RS.CO-03; 164.308(a)(6)(ii))
4.9 No ransom may be paid without approval from the CEO, outside counsel, and the insurer, a documented OFAC sanctions check, and a report to law enforcement. (IR-4; RS.MA-01; 164.308(a)(6)(ii))
4.10 Each runbook must be exercised at least annually, including one exercise a year with the counties and one with outside counsel and the executive team. Manual dispatch must be drilled at both centers at least twice a year. (IR-3; CP-4; ID.IM-02; 164.308(a)(7)(ii)(D))
4.11 Lessons learned must be documented within 30 days of closing a major incident and fed into the risk register (P01) and the POA&M (P07). The Medical Director reviews every call handled in manual mode for patient impact. (IR-4; ID.IM-02; 164.308(a)(6)(ii))

## 5. Compliance and enforcement
Violations are handled under the HIPAA sanctions procedure (POL-01 section 4.8). Compliance is checked through the annual independent assessment (P07) and exercise reports.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. No exception may extend a legal or contractual notification deadline.

## 7. Related documents
P08 `ir-runbook.md`, `ir-runbook-billing-vendor-breach.md`, and `notification-matrix.csv`; POL-01; STD-02; STD-07; County A communications center continuity plan; HIPAA Breach Notification Rule; Fla. Stat. 501.171
