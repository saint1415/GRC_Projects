# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Owner | Security Manager |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 incident response plan) |
| Review cycle | Annually (next review 2027-09-30), after each exercise, and after every severity 1 incident |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-7, IR-8, CP-2, SI-4 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| PCI DSS v4.0.1 (N71-R04) | 12.10.1 to 12.10.7; 10.7 |
| Law and rules | Fla. Stat. 501.171(3) to (6); each state's breach law; card brand rules applied through the acquirer (Visa *What To Do If Compromised* v10.0) |
| Supporting standards | STD-02 Logging and monitoring; STD-07 Contingency and event-day continuity |

## 1. Purpose
Make sure the company detects, contains, and recovers from security incidents quickly, protects attendees during event-day disruptions, and meets every legal, card brand, contractual, and insurance deadline.

## 2. Scope
All suspected or confirmed security incidents affecting company systems, card data, patron data, the website and payment pages, or the event-day systems at any venue, including incidents at service providers that affect company data or services.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Security Manager | Incident commander for security incidents; coordinates the MSSP and forensics |
| IT Director | Technical recovery lead; contingency plan owner |
| Chief Operating Officer | Chairs the crisis management team for major incidents; approves external statements |
| General Counsel | Breach determinations and notification decisions; keeps the decision log; engages outside breach counsel |
| Chief Financial Officer | Acquirer, card brand, insurer, and QSA contact for card incidents |
| Venue General Managers and Director of Safety and Security | Event-day decisions: holding doors, manual entry, evacuation; life safety first |
| Vice President of Marketing and Digital | Payment page containment; patron communications through counsel |
| MSSP | 24x7 detection, first containment, and escalation within 30 minutes for high severity |
| All workforce | Report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain an incident response plan and runbooks for its most likely and most harmful incidents. At minimum these are a ticketing platform breach exposing card and patron data, and an event-day outage of ticketing and scanning (P08). The plan must cover business recovery and continuity, data backup, legal requirements, and card brand procedures. (IR-8; RS.MA-01; PCI 12.10.1)
4.2 Workforce members must report any suspected incident **immediately**, and within 1 hour at most, to the service desk security line or their manager. Examples: phishing clicks, unexpected MFA prompts, lost devices, card numbers seen where they should not be, unknown scripts or prices on event pages, tampered payment devices. Good-faith reporting is never sanctioned. (IR-6; RS.MA-02)
4.3 Every incident must be logged, categorized by severity, and tracked to closure in the security incident queue. **The time of first suspicion and the time of any breach determination must be recorded**, because card brand clocks run from suspicion and Florida's clock runs from determination. (IR-5; IR-4)
4.4 A severity 1 incident (any suspected card data compromise, any confirmed patron data exfiltration, ransomware, or an event-day outage expected to exceed a High-criticality MTD in P05) must activate the crisis management team, chaired by the COO, within 1 hour. (IR-4; RC.RP-01)
4.5 **Card compromise.** The CFO must notify the acquirer within 24 hours of suspecting a card data compromise (merchant agreement) and make sure Visa is notified within 3 calendar days through the acquirer. Evidence must be preserved before changes are made, and the company must retain a PCI Forensic Investigator if a card brand requires one. (IR-6; RS.CO-02; PCI 12.10.1)
4.6 The General Counsel must decide whether an incident is a breach that requires notice under Fla. Stat. 501.171 and the law of each state where affected individuals reside, document the decision in the decision log, and retain it for at least 5 years. Notifications to individuals, regulators, consumer reporting agencies, the acquirer and card brands, the insurer, the County (from 2027-07-01), and law enforcement must meet the deadlines in the P08 notification matrix, and counsel must confirm each one. (IR-6; RS.AN-03; RS.CO-03)
4.7 The cyber insurer must be notified through its hotline before incident response vendors are engaged, as the policy requires. (IR-7)
4.8 No ransom or extortion payment may be made without approval from the CEO, counsel, and the insurer, a documented OFAC sanctions check, and a report to law enforcement. (IR-4)
4.9 **Event days.** During any incident that affects a show, the venue General Manager and the Director of Safety and Security decide whether to hold doors, switch to manual entry, or stop the show, following the venue emergency plan. Life safety decisions take priority over evidence preservation and revenue. (CP-2; RC.RP-01)
4.10 **Unexpected card data.** Card numbers found where they are not allowed (CRM, email, files, paper) must be treated as an incident: contain access, determine how the data got there, purge it securely, and fix the process. (IR-4; PCI 12.10.7)
4.11 Incident response must be exercised at least annually for each runbook, including at least one exercise a year with the crisis management team and outside counsel. Responders must be trained on their roles. (IR-2; IR-3; ID.IM-02; PCI 12.10.2; 12.10.4)
4.12 Alerts from the SIEM, the payment page monitoring service, EDR, and the identity provider must be triaged under STD-02; the MSSP must escalate high-severity alerts within 30 minutes. (SI-4; PCI 12.10.5; 10.7)
4.13 Lessons learned must be documented within 30 days of closing a major incident and fed into the risk register (P01), the POA&M (P07), and the runbooks. (IR-4; ID.IM)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.10. Compliance is checked through the annual independent assessment (P07), exercise reports, and the PCI DSS ROC.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. No exception may extend a legal, card brand, or contractual notification deadline.

## 7. Related documents
P08 `ir-runbook.md`, `ir-runbook-event-day-outage.md`, and `notification-matrix.csv`; POL-01; STD-02; STD-07; venue emergency plans; Fla. Stat. 501.171
