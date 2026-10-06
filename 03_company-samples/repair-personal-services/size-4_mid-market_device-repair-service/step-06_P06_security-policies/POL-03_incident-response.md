# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Owner | Security Manager |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after every major incident or exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-7, IR-8, AU-2, AU-6, AU-9, AU-11, CP-2 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, RC.CO-03, ID.IM-02 |
| Legal and contractual basis | Fla. Stat. 501.171(3) to (6); other states' breach laws; PCI DSS v4.0.1 12.10.1; merchant agreement (acquirer notice); Manufacturer A agreement (24-hour notice); Partner agreements (48-hour notice) |
| Supporting standards | STD-02 Logging and monitoring standard; STD-07 Contingency and recovery standard |

## 1. Purpose
Make sure the company detects, contains, reports, and recovers from security incidents quickly, protects customers whose devices and data it holds, and meets every legal and contractual notification deadline.

## 2. Scope
All security incidents and suspected incidents affecting company systems, customer devices or recovered data in custody, partner claim data, payment channels, or vendors that hold company data. It applies at all stores, the Depot, the contact center, and the corporate office.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Security Manager | Incident commander for security incidents; coordinates the MSSP and forensics |
| IT Director | Technical recovery lead; contingency plan owner |
| Chief Operating Officer | Chairs the crisis management team for major incidents; approves external statements |
| General Counsel with outside breach counsel (insurer panel) | Directs investigations under privilege where appropriate; confirms each notification |
| Privacy and Compliance Manager | Breach determinations with counsel; keeps the decision log |
| Chief Financial Officer | Insurer and acquirer notices; card brand cases through the acquirer |
| Director of Partner Programs | Manufacturer and partner notices |
| HR Director | Workforce matters when an employee is involved |
| Director of Customer Experience | Customer, media, and staff communications through counsel |
| MSSP | 24x7 detection, first containment, and escalation within 30 minutes for high severity |
| All workforce | Report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain an incident response plan and runbooks for its most likely and most harmful incidents. At minimum these are customer device data exposure and point-of-sale compromise (P08), and ransomware (2024 plan, to be merged into the P08 format by 2027-03-31). (IR-8; RS.MA-01)
4.2 Workforce members must report any suspected incident **immediately**, and within 1 hour at most, to the service desk security line, their manager, or the anonymous reporting line. Examples: a colleague browsing customer content, a tampered terminal, a lost mail-in parcel, a suspicious login, a card number written down. Good-faith reporting is never sanctioned. Managers must log every report they receive. (IR-6; RS.MA-02)
4.3 Every incident must be logged, categorized by severity, and tracked to closure in the security incident queue. **The date and time the company first had reason to believe a breach occurred must be recorded when the incident is opened**, because Florida's 30-day clocks and the contract clocks start from it. (IR-5; IR-4)
4.4 A severity 1 incident (any confirmed exposure of customer data outside the company, any checkout page or terminal compromise, or ransomware) must activate the crisis management team, chaired by the COO, within 2 hours. (IR-4; RC.RP-01)
4.5 **Evidence first.** Bench workstations, customer devices, terminals, and storage involved in an incident must not be wiped, reimaged, returned, or repaired until the incident commander releases them. Every item must carry a chain-of-custody record. (IR-4; AU-9)
4.6 The Privacy and Compliance Manager, with counsel, must decide whether an incident is a breach under Fla. Stat. 501.171 and each other affected state's law, and must document the decision in the decision log. Written no-notice determinations must be kept for at least 5 years and sent to the Department of Legal Affairs within 30 days (501.171(4)(c)). (IR-6; RS.AN-03)
4.7 **Contract clocks start at suspicion.** The CFO must notify the acquirer within 24 hours of suspecting a card data compromise; the Director of Partner Programs must notify Manufacturer A within 24 hours of a suspected incident involving its program customers or devices, and the affected partner within 48 hours of discovering a breach of claim data. These notices must not wait for the investigation to finish. (IR-6; PCI DSS 12.10.1; contracts)
4.8 Notifications to individuals, the Florida Department of Legal Affairs, other states' regulators, consumer reporting agencies, the cyber insurer, and law enforcement must meet the deadlines in the P08 notification matrix. Counsel must confirm each notification. (IR-6; RS.CO-02; RS.CO-03)
4.9 The cyber insurer must be notified through its hotline before incident response vendors are engaged, as the policy requires. (IR-7)
4.10 No ransom or extortion payment may be made without approval from the CEO, counsel, and the insurer, a documented OFAC sanctions check, and a report to law enforcement. (IR-4)
4.11 Security logs needed to investigate incidents (identity provider, EDR, SYS-01 audit events, bench session records, lab storage, application logs) must be collected and kept for at least 1 year searchable and 3 years archived (STD-02). (AU-2; AU-6; AU-11)
4.12 Incident response must be exercised at least annually for each runbook, including one exercise a year with counsel and the executive team. (IR-3; ID.IM-02)
4.13 Lessons learned must be documented within 30 days of closing a severity 1 or 2 incident and fed into the risk register (P01) and the POA&M (P07). (IR-4; ID.IM-03)

## 5. Compliance and enforcement
Violations are handled under the sanctions rule in POL-01 section 4.8. Compliance is checked through the annual independent assessment (P07) and exercise reports.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. No exception may extend a legal or contractual notification deadline.

## 7. Related documents
P08 `ir-runbook.md`, `ir-runbook-pos-compromise.md`, and `notification-matrix.csv`; POL-01; STD-02; STD-07; Fla. Stat. 501.171; merchant agreement; Manufacturer A agreement; Partner agreements
