# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | IT Manager |
| Approved by | General Manager |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| Regulatory basis | 10 CFR 37.57 and 37.81 through the Florida license condition; Chapter 64E-5, F.A.C. (64E-5.343, 64E-5.344); Fla. Stat. 501.171; OFAC ransomware advisory (2021-09-21) |

## 1. Purpose
Make sure the company detects, contains, reports, and recovers from security incidents quickly and lawfully. That includes incidents that start in IT and threaten the OT network or the physical protection of radioactive material.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, contractors, and temporary staff) at the Plant, in company vehicles, and at customer sites. Covers all company systems and data, including systems that vendors operate for the company, the plant OT network, and the physical security systems. It applies to Part 37 security-related information and all other company information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| IT Manager | Incident commander for cyber incidents; coordinates the MSP, forensic firm, and controls integrator |
| Radiation Safety Officer | Decides whether an event is reportable under Part 37 or Chapter 64E-5; contacts the LLEA and the Florida Bureau of Radiation Control |
| Operations Manager | Places processing in a safe state; runs OT contingency steps |
| General Manager | Engages counsel and the cyber insurer; approves external communications |
| All workforce | Report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain an incident response plan and runbooks for its most likely incidents. The first covers a cyber attack on the business network with an attempted pivot to OT and the security systems (P08). (IR-8; RS.MA-01)

4.2 **Reporting.** Workforce members must report any suspected incident immediately, and within 1 hour at most, to the IT incident line or their supervisor. Examples: phishing clicks, lost devices, unusual system behavior. Good-faith reporting is never sanctioned. (IR-6; RS.MA-02)

4.3 **Security system events.** Any suspected cyber activity affecting the PACS, cameras, NVR, IDS communicator, or Part 37 security-related information must be reported to the RSO at once, as well as to IT. Examples: a camera going offline unexpectedly, unknown badges, access to the restricted library by someone not on the list. (IR-6; 10 CFR 37.57(b))

4.4 The RSO must decide without delay whether the event is suspicious activity related to possible theft, sabotage, or diversion. If it is, the RSO must notify the LLEA as appropriate and the Florida Bureau of Radiation Control no later than 4 hours after notifying the LLEA. Actual or attempted theft, sabotage, or diversion requires immediate LLEA notice and State notice within 4 hours of discovery. (IR-6; RS.CO-02; 37.57(a)-(b))

4.5 Every incident must be logged, categorized, and tracked to closure in the ticketing system under the Security category, which the RSO can see. (IR-5)

4.6 Notifications to regulators, law enforcement, customers, and affected individuals must meet the deadlines in the P08 notification matrix. Legal counsel must confirm breach notices under Fla. Stat. 501.171. (IR-6; RS.CO-03)

4.7 No ransom may be paid without approval from the President, legal counsel, and the cyber insurer, and an OFAC sanctions check. (IR-4)

4.8 The incident response plan must be tested at least annually by a tabletop exercise that includes the RSO, the controls integrator, and the alarm monitoring company. It must also be tested after any major incident. (IR-3; ID.IM-02)

4.9 Lessons learned must be documented within 30 days of closing an incident, added to the risk register, and fed into the Part 37 security program review. (IR-4; ID.IM)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.8). Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07), the Part 37 program reviews, and the access reviews in this policy set.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. They must be written, risk-rated, approved by the policy owner (or by the President for High risk), and expire within 12 months.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; POL-01; Part 37 procedures SEC-05 and SEC-09 (restricted); transportation procedure TR-06
