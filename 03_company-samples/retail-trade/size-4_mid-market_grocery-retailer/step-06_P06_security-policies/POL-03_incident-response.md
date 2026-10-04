# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Owner | Security Manager |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 plan) |
| Review cycle | Annually (next review 2027-09-30), and after every major incident or exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-7, IR-8, CP-2, SI-4 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, RC.CO-03, ID.IM-02 |
| PCI DSS v4.0.1 | Requirement 12.10; 10.4, 10.7 (N44-45-R01) |
| Other rules | Fla. Stat. 501.171(3)-(6); state breach notification laws; merchant agreement notice term |
| Supporting standards | STD-02 Logging and monitoring standard; STD-07 Contingency and recovery standard |

## 1. Purpose
Make sure the company detects, contains, reports, and recovers from security incidents quickly, protects customers and their card data, keeps stores and the DC running, and meets every legal and contractual notice deadline.

## 2. Scope
All security incidents and suspected incidents affecting company systems, card data, customer or supplier data, or vendors that hold company data, and outages of systems that support High or Moderate criticality processes (P05). It applies at all stores, the DC, and the support center.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Security Manager | Incident commander for security incidents; coordinates the MSSP and forensics |
| IT Director | Technical recovery lead; contingency plan owner |
| Chief Operating Officer | Chairs the crisis management team for major incidents; approves external statements |
| Chief Financial Officer | Notifies the acquirer and manages card brand instructions; cyber insurance claim |
| General Counsel | Breach determinations and notices with outside counsel; keeps the decision log with the Privacy and Compliance Manager |
| Outside breach counsel (insurer panel) | Directs the investigation under privilege where appropriate; confirms each notification |
| Director of Store Operations and Distribution Center Director | Store and DC downtime decisions; store staff communication |
| Director of E-commerce and Marketing | Checkout page containment; online channel decisions |
| MSSP | 24x7 detection, first containment, and escalation within 30 minutes for high severity |
| All workforce | Report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain an incident response plan and runbooks for its most likely and most harmful incidents. At minimum these are payment card data compromise through e-commerce skimming and ransomware across stores and the DC (P08). (IR-8; RS.MA-01; PCI DSS 12.10.1)
4.2 Workforce members must report any suspected incident **immediately**, and within 1 hour at most, to the service desk security line or their manager. Examples: phishing clicks, lost devices, signs of PIN pad tampering, unknown devices in a store, customer reports of card fraud after shopping online, and card numbers received by email. Good-faith reporting is never sanctioned. (IR-6; RS.MA-02)
4.3 Every incident must be logged, categorized by severity, and tracked to closure in the security incident queue. **The time of first suspicion and the time of any breach determination must be recorded**, because contract and legal clocks run from them. (IR-5; IR-4)
4.4 A major incident (severity 1: any suspected card data compromise, ransomware, confirmed customer data exfiltration, or an outage expected to exceed a High-criticality MTD) must activate the crisis management team, chaired by the COO, within 2 hours. (IR-4; RC.RP-01)
4.5 **Acquirer notice.** The Chief Financial Officer must notify the acquirer within 24 hours of suspecting a compromise of card data, as the merchant agreement requires, and must follow the acquirer's and card brands' instructions, including any requirement to engage a PCI Forensic Investigator. (IR-6; RS.CO-02; PCI DSS 12.10.1)
4.6 The General Counsel must decide whether an incident is a breach that requires notice under Fla. Stat. 501.171 or another state's law, document the decision and its basis in the decision log, and keep it for at least 5 years. Notifications to individuals, the Florida Department of Legal Affairs, consumer reporting agencies, other states, the cyber insurer, suppliers, and law enforcement must meet the deadlines in the P08 notification matrix. Outside counsel must confirm each notification. (IR-6; RS.AN-03; RS.CO-02; RS.CO-03)
4.7 The cyber insurer must be notified through its hotline before incident response vendors are engaged, as the policy requires. (IR-7)
4.8 No ransom or extortion payment may be made without approval from the CEO, outside counsel, and the insurer, a documented OFAC sanctions check, and a report to law enforcement. (IR-4)
4.9 After a suspected card data compromise, online card payments, or the affected store lanes, must not resume until the containment is verified and the forensic firm and the acquirer have no objection. (IR-4; RC.RP-01)
4.10 Incident response must be exercised at least annually for each runbook, including at least one exercise a year with outside counsel, the executive team, and the acquirer contact. (IR-3; ID.IM-02; PCI DSS 12.10.2)
4.11 Alerts from CDE security controls (EDR, anti-malware, payment page tamper detection, log source failures) must be monitored 24x7 and handled under this policy. (SI-4; IR-4; PCI DSS 10.7)
4.12 Lessons learned must be documented within 30 days of closing a major incident and fed into the risk register (P01) and the POA&M (P07). (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 4.8). Compliance is checked through the annual independent assessment (P07), the QSA's PCI DSS assessment, and exercise reports.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. No exception may extend a legal or contractual notification deadline.

## 7. Related documents
P08 `ir-runbook.md`, `ir-runbook-ransomware.md`, and `notification-matrix.csv`; POL-01; STD-02; STD-07; store downtime procedures; Fla. Stat. 501.171
