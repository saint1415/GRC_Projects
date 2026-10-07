# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Owner | Director of Security |
| Approved by | Chief Technology Officer |
| Approval date | 2026-09-29 |
| Effective date | 2026-10-01 (replaces the 2023 policy) |
| Review cycle | Annually (next review 2027-09-30), and after every major incident or exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-7, IR-8, CP-2, AU-2, AU-6 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, RC.CO-03, ID.IM-02 |
| Regulatory and contract drivers | N51-R01 (FTC Data Breach Response guide); 45 CFR 164.308(a)(6), 164.402, 164.410, 164.412, 164.414(b); 12 CFR 53.4 (bank customers); Fla. Stat. 501.171; DPA, BAA, and MSA notice terms |
| Supporting standards | STD-02 Logging and monitoring standard; STD-07 Contingency and recovery standard |

## 1. Purpose
Make sure the company detects, contains, and recovers from security incidents and major outages quickly, and meets every legal and contractual notice deadline to customers, covered entities, bank customers, and regulators.

## 2. Scope
All security incidents and suspected incidents affecting company systems, customer data, or sub-processors that hold customer data, and platform outages that threaten the BIA MTDs (P05).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Security | Incident commander for security incidents; coordinates the MDR provider and forensics |
| VP Platform Engineering | Technical recovery lead; incident commander for outages |
| Chief Technology Officer | Chairs the crisis management team for severity 1 incidents |
| General Counsel | Breach determinations, the decision log, and approval of every external notice and statement |
| Associate General Counsel, Privacy | Business associate notices to covered entities; DPA notices with the VP Customer Support |
| VP Customer Support | Sends approved customer notices and status updates; owns the customer security contact list |
| Chief Financial Officer | Insurance claim, service credits, finance impacts |
| Outside breach counsel (insurer panel) | Directs investigations under privilege where appropriate; confirms each legal notice |
| MDR provider | 24x7 detection and first containment for endpoints and identity; escalation within 30 minutes for high severity |
| All workforce | Report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain an incident response plan and runbooks for its most likely and most harmful incidents. At minimum these are cloud credential compromise exposing customer data and extended platform outage (P08). (IR-8; RS.MA-01)
4.2 Workforce members must report any suspected incident **immediately**, and within 1 hour at most, through the security channel or the on-call page. Examples: exposed credentials, unexpected access to customer data, a customer report of data from another tenant, a lost laptop. Good-faith reporting is never sanctioned. (IR-6; RS.MA-02; 164.308(a)(6)(ii))
4.3 Every incident must be logged, categorized by severity, and tracked to closure. **The time of discovery and the time of confirmation must both be recorded when the incident is opened.** Discovery starts the business associate clock (45 CFR 164.410(a)(2)); confirmation starts the DPA clocks. (IR-5; IR-4)
4.4 A severity 1 incident (confirmed unauthorized access to customer data, any destructive attack, or an outage expected to exceed a High-criticality MTD) must activate the crisis management team, chaired by the CTO, within 1 hour. (IR-4; RC.RP-01)
4.5 The General Counsel must decide whether an incident involving PHI is a breach of unsecured PHI, documenting the four-factor risk assessment (45 CFR 164.402) in the decision log. Decisions and notices must be retained for 6 years. (IR-6; RS.AN-03; 164.414(b))
4.6 Notices must meet the deadlines in the P08 notification matrix. **Plan to the shortest clock:** 24 hours for Enterprise customers with negotiated terms; 48 hours for other DPA customers; notice to bank customers when a disruption reaches or is likely to reach 4 hours; 10 business days to covered entities under the BAAs; 10 days for the Florida third-party agent notice. Outside counsel must confirm each legal notice. (IR-6; RS.CO-02; RS.CO-03)
4.7 The cyber insurer must be notified through its hotline before incident response vendors are engaged, as the policy requires. (IR-7)
4.8 No extortion or ransom payment may be made without approval from the CEO, outside counsel, and the insurer, a documented OFAC sanctions check, and a report to law enforcement. Paying does not remove any notice duty. (IR-4)
4.9 Evidence must be preserved before eradication: cloud audit logs, identity logs, and affected resources are exported to the evidence location with hashes recorded. (IR-4; AU-9)
4.10 Incident response must be exercised at least annually for each runbook, including one exercise a year with outside counsel and the executive team. The regional failover exercise counts for the outage runbook. (IR-3; ID.IM-02)
4.11 Lessons learned must be documented within 30 days of closing a severity 1 or 2 incident and fed into the risk register (P01), the POA&M (P07), and the SOC 2 incident log. Public and contractual statements affected by the incident must be reviewed under POL-01 4.11. (IR-4; ID.IM-03)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.8. Compliance is checked through the annual independent assessment (P07), exercise reports, and the SOC 2 examination.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. No exception may extend a legal or contractual notification deadline.

## 7. Related documents
P08 `ir-runbook.md`, `ir-runbook-platform-outage.md`, and `notification-matrix.csv`; POL-01; STD-02; STD-07; customer DPA, BAA, and MSA templates
