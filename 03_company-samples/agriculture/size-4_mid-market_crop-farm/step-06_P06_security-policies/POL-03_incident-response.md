# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Owner | Security Manager |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after every major incident or exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-7, IR-8, CP-2 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.MA-04, RS.AN-03, RS.CO-02, RS.CO-03, RS.MI-01, RC.RP-01, RC.CO-03, ID.IM-02 |
| Other requirements | Fla. Stat. 501.171(3)-(6); 20 CFR 655.122(k); 21 CFR 112.166(a); 40 CFR 170.311(b)(5); retail supplier agreements (24-hour notice); cyber insurance policy; NIST SP 800-82 Rev. 3 section 6.4 |
| Languages | Issued in English; reporting cards in English and Spanish for all field staff |
| Supporting standards | STD-02 Logging and monitoring standard; STD-07 Contingency and recovery standard |

## 1. Purpose
Make sure the company detects, contains, reports, and recovers from security incidents quickly, keeps crops, food, and workers safe while it does, and meets every legal and contractual notice deadline.

## 2. Scope
All security incidents and suspected incidents affecting company systems, OT, data, or vendors that hold company data, at every site. It includes OT integrity events (unexplained changes to irrigation, fertigation, ripening, or cold storage settings) and major outages of services that support High or Moderate criticality processes (P05).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Security Manager | Incident commander for security incidents; coordinates the MSSP and forensics |
| IT Director | Technical recovery lead for IT and cloud; contingency plan owner |
| Director of Irrigation and Water Resources; Packinghouse Manager | OT leads: manual operation, OT containment, and safe restart |
| Director of Food Safety and Quality | Product hold and recall decisions with the CEO; retail customer food safety contact |
| Chief Operating Officer | Chairs the crisis management team for major incidents; approves external statements |
| HR Director | Worker notices and H-2A payroll continuity |
| Vice President of Grower Services | Grower communications and settlement continuity |
| Outside breach counsel (insurer panel) | Directs the investigation under privilege where appropriate; confirms each notice |
| Communications Manager | Staff, grower, customer, and media messages through counsel |
| MSSP | 24x7 detection, first containment of IT endpoints, and a call within 30 minutes on high severity |
| All workforce | Report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain an incident response plan and runbooks for its most harmful incidents. At minimum these are ransomware on the farm-management and irrigation control systems with data theft, and an OT integrity incident with possible product safety impact (P08). (IR-8; RS.MA-01)
4.2 Workforce members must report any suspected incident **immediately**, and within 1 hour at most, to the service desk security line or their supervisor. Examples: phishing clicks, lost tablets, strange messages, and any pump, valve, pivot, injection, ripening room, or cooler behavior that nobody scheduled. Good-faith reporting is never sanctioned. (IR-6; RS.MA-02)
4.3 Every incident must be logged, categorized by severity, and tracked to closure in the security incident queue. **The date and time of discovery, and later the date the company determined that a breach occurred, must be recorded.** (IR-5; IR-4)
4.4 A severity 1 incident (any ransomware, confirmed theft of worker or grower personal data, an OT integrity event that could affect product or worker safety, or an outage expected to exceed a High-criticality MTD) must activate the crisis management team, chaired by the COO, within 2 hours. (IR-4; RS.MA-04; RC.RP-01)
4.5 **Safety first in OT.** Before an OT segment is isolated, its control owner must hand the affected pumps, injection skids, pivots, or rooms over to manual operation. Fertigation injection must be stopped at the skid whenever an unauthorized change is suspected. Product that may have been affected by an OT integrity event must be placed on hold until the Director of Food Safety and Quality releases it. (IR-4; RS.MI-01; SP 800-82 Rev. 3 section 6.4)
4.6 Outside counsel and the HR Director (for workers) or the Vice President of Grower Services (for growers) must decide whether an incident is a breach of personal information under Fla. Stat. 501.171 and the law of each state where affected individuals reside, and record the decision in the decision log. (IR-6; RS.AN-03)
4.7 Notices to individuals, the Florida Department of Legal Affairs, other states' regulators, consumer reporting agencies, retail customers (within 24 hours of an event affecting product safety, traceability, or committed volumes), contract growers, the cyber insurer, and law enforcement must meet the deadlines in the P08 notification matrix. Outside counsel must confirm each notice. (IR-6; RS.CO-02; RS.CO-03)
4.8 The cyber insurer must be notified through its hotline before incident response vendors are engaged, as the policy requires. (IR-7)
4.9 No ransom may be paid without approval from the CEO, outside counsel, and the insurer, a documented OFAC sanctions check, and a report to law enforcement. (IR-4)
4.10 **Continuity duties during an incident.** H-2A earnings statements must still be issued on or before each payday, pesticide application information must still be displayed within 24 hours, and Produce Safety records must still be retrievable for FDA, using the paper procedures in STD-07. (CP-2; 20 CFR 655.122(k); 40 CFR 170.311(b)(5); 21 CFR 112.166(a))
4.11 Incident response must be exercised at least annually for each runbook, including at least one exercise a year with outside counsel, the executive team, the SCADA integrator, and the FMIS vendor. (IR-3; ID.IM-02)
4.12 Lessons learned must be documented within 30 days of closing a severity 1 or 2 incident and fed into the risk register (P01) and the POA&M (P07). (IR-4; ID.IM-03)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.8. Compliance is checked through the annual independent assessment (P07) and exercise reports.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. No exception may extend a legal or contractual notice deadline.

## 7. Related documents
P08 `ir-runbook.md`, `ir-runbook-ot-integrity.md`, and `notification-matrix.csv`; POL-01; STD-02; STD-07; food safety recall plan; food defense plan; Fla. Stat. 501.171
