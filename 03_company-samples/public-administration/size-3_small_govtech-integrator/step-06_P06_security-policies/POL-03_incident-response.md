# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | IT Manager |
| Approved by | Chief Operating Officer |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8, AT-2 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| Agency requirements | CJISSECPOL v6.1 IR-6 and AT-2; Pub. 1075 section 1.8 (through the AC-01 contract); Fla. Stat. 501.171(6); Fla. Stat. 282.318 and 282.3185 (agency duties the company supports) |

## 1. Purpose
Make sure the company detects, contains, reports, and recovers from security incidents quickly, and gives each agency what it needs in time to meet its own legal reporting clocks.

## 2. Scope
All Cris Santos Company workforce members, wherever they work. Covers every incident that affects the ACMP, agency data, or the systems that administer them, including incidents at vendors.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| IT Manager | Incident commander; coordinates the Cloud Operations Lead, the managed detection service, and the forensic firm |
| Contracts and Compliance Manager | Agency notices and the notification matrix; breach determinations with counsel |
| Chief Operating Officer | Engages counsel and the cyber insurer; approves external statements |
| Chief Executive Officer | Ransom decisions (4.7) |
| Cloud Operations Lead | Containment and recovery in the cloud tenant |
| All workforce | Report suspected incidents within 1 hour |

## 4. Policy statements
4.1 The company must maintain an incident response plan and runbooks for its most likely incidents, starting with ransomware in the production tenant (P08). The plan must define reportable incidents in terms of CJI, FTI, and agency personal information. (IR-8; RS.MA-01)
4.2 Workforce members must report any suspected incident **immediately, and no more than 1 hour after discovery**, to the incident line or the IT Manager. Examples: a phishing click, a lost laptop, agency data in the wrong place (including tickets or email), unusual access, or a vendor notice. Good-faith reporting is never sanctioned. (IR-6; RS.MA-02; CJISSECPOL IR-6)
4.3 Every incident is logged, categorized, and tracked to closure in the ticketing system under the Security category, with no regulated data in the ticket. (IR-5)
4.4 **Agency notice comes first.** For any suspected incident that may involve an agency's data, the Contracts and Compliance Manager notifies that agency's named security contact on the clock in the P08 notification matrix: within 1 hour for suspected CJI incidents (AC-02), immediately for suspected FTI incidents so AC-01 can report to TIGTA and the IRS Office of Safeguards within 24 hours, and in time for any Florida agency to report a ransomware incident within 12 hours. The company does not wait for its own investigation to finish. (IR-6; RS.CO-02)
4.5 Breach notices under Fla. Stat. 501.171(6) must reach the affected agency no later than 10 days after the breach is determined, together with all information the agency needs for its own notices. Counsel confirms every external notice. (IR-6; RS.CO-03)
4.6 Evidence (logs, images, timelines) is preserved from the first hour and kept for 7 years (POL-01 4.11). (IR-4)
4.7 **Ransom.** No ransom may be paid without approval from the Chief Executive Officer, counsel, and the cyber insurer, an OFAC sanctions check, and consultation with every affected agency. Florida state agencies, counties, and municipalities may not pay or comply with a ransom demand (Fla. Stat. 282.3186); the company will not make a payment an agency customer objects to. (IR-4)
4.8 The incident response plan is tested at least annually by tabletop exercise that includes the AC-01 and AC-02 security contacts, and after any major incident. (IR-3)
4.9 Staff involved in a security incident complete refresher training within 30 days, as the CJIS Security Policy requires. (AT-2; IR-2)
4.10 Lessons learned are documented within 30 days of closing an incident and added to the risk register and training. (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.8. Compliance is checked through the annual tabletop and the control assessment (P07).

## 6. Exceptions
Exceptions follow POL-01 section 4.7. The reporting clocks in 4.2, 4.4, and 4.5 cannot be waived.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; POL-01; CJIS Security Policy v6.1; IRS Publication 1075 section 1.8; Fla. Stat. 501.171
