# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Owner | Security Operations Manager |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2025 plan's policy section) |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8, AT-2, AU-11 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| Agency requirements | CJISSECPOL v6.1 IR-6 and AT-2; Pub. 1075 sec. 1.8 (through the AG-01 contract); Fla. Stat. 501.171(6); Fla. Stat. 282.318, 282.3185, 282.3186 (agency duties the company supports); the law of each other state where agencies sit or affected individuals reside |
| Supporting documents | P08 runbooks (ransomware; insider misuse) and notification matrix; STD-02 Logging and monitoring |

## 1. Purpose
Make sure the company detects, contains, reports, and recovers from security incidents quickly, and gives each agency what it needs in time to meet its own legal reporting clocks.

## 2. Scope
All workforce members, wherever they work. Covers every incident that affects the ACMC, agency data, agency systems the company administers, company systems, or vendors that hold agency data or access.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Security Operations Manager | Incident commander; works with the MDR provider and the forensic firm |
| Chief Operating Officer | Chairs the crisis management team; engages the insurer |
| General Counsel | Legal lead; engages outside breach counsel; privilege |
| Director of Contracts and Compliance | Agency notices and the notification matrix; breach determinations with counsel |
| Chief Executive Officer | Ransom decisions (4.7); informs the audit committee chair and the PE sponsor |
| Director of Cloud Operations and Director of Managed Services | Containment and recovery in the cloud and in agency systems |
| All workforce | Report suspected incidents within 1 hour |

## 4. Policy statements
4.1 The company must maintain an incident response plan and runbooks for its most likely and most harmful incidents, starting with ransomware (including through managed services) and insider misuse of regulated data (P08). The plan defines reportable incidents in terms of CJI, FTI, motor vehicle records, benefits data, and agency personal information, and sets metrics for the capability. (IR-8; RS.MA-01)
4.2 Workforce members must report any suspected incident **immediately, and no more than 1 hour after discovery**, to the incident line or the Security Operations Manager. Examples: a phishing click, a lost laptop, agency data in the wrong place, unusual access, an alert in an agency system, or a vendor notice. Good-faith reporting is never sanctioned. (IR-6; RS.MA-02; CJISSECPOL IR-6)
4.3 Every incident is logged, categorized, and tracked to closure in the security case system, with no regulated data in the case record. (IR-5)
4.4 **Agency notice comes first.** For any suspected incident that may involve an agency's data or systems, the Director of Contracts and Compliance notifies that agency's named security contact on the clock in the P08 notification matrix: within 1 hour for suspected CJI incidents (AG-02, AG-39); within 1 hour for suspected FTI incidents so AG-01 can report to TIGTA and the IRS Office of Safeguards within 24 hours; and in time for any Florida agency to report a ransomware incident within 12 hours. The company does not wait for its own investigation to finish. (IR-6; RS.CO-02)
4.5 Breach notices under Fla. Stat. 501.171(6)(a) must reach each affected Florida agency no later than 10 days after the breach is determined, with all information the agency needs for its own notices, including counts of affected individuals by state of residence. Notices for agencies in other states follow each state's law as mapped by counsel. Counsel confirms every external notice. (IR-6; RS.CO-03)
4.6 Evidence (logs, images, timelines) is preserved from the first hour under counsel's direction and kept for 7 years. (IR-4; AU-11)
4.7 **Ransom.** No ransom may be paid without approval from the Chief Executive Officer, counsel, and the cyber insurer, an OFAC sanctions check, and consultation with every affected agency. Florida state agencies, counties, and municipalities may not pay or comply with a ransom demand (Fla. Stat. 282.3186); the company will not make a payment any agency customer objects to. (IR-4)
4.8 The plan is tested at least annually by a tabletop exercise that includes the AG-01, AG-02, and AG-03 security contacts, and the insider misuse runbook is exercised at least annually with HR and counsel. (IR-3)
4.9 Staff involved in a security incident complete refresher training within 30 days, as the CJIS Security Policy requires. (AT-2; IR-2)
4.10 Lessons learned are documented within 30 days of closing an incident and added to the risk register, the runbooks, and training. (IR-4; ID.IM-02)
4.11 Incidents found in agency-hosted systems are handled under this policy and the agency's own procedures, with the agency's incident lead in command of its systems. (IR-4)
4.12 Any severity 1 incident (ransomware, confirmed data theft, or misuse of regulated data) activates the crisis management team. (IR-4; RC.RP-01)

## 5. Compliance and enforcement
Violations are handled under POL-01 statement 4.8. Compliance is checked through the annual tabletops, the incident metrics, and the control assessment (P07).

## 6. Exceptions
Exceptions follow POL-01 statement 4.7. The reporting clocks in 4.2, 4.4, and 4.5 cannot be waived.

## 7. Related documents
P08 runbooks and notification matrix; POL-01; POL-04; CJIS Security Policy v6.1; IRS Publication 1075 section 1.8; Fla. Stat. 501.171
