# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC and its subsidiaries |
| Policy ID | POL-03 |
| Owner | IT Manager |
| Approved by | CEO |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after an acquisition, a major change, or an incident |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.MA-04, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-04 |
| FTC Safeguards Rule (Finance) | 16 CFR 314.4(h)(1)-(7), (j) |

## 1. Purpose
Make sure the group detects, contains, reports, and recovers from security incidents quickly and lawfully, handles them the same way at every subsidiary, and meets notice deadlines. For Finance, this policy and the P08 runbook form the written incident response plan required by 16 CFR 314.4(h).

## 2. Scope
All workforce members (owners, managers, employees, contractors, and temporary staff) of Cris Santos Company, LLC and each subsidiary, at every site and when working remotely. Covers all systems and data the group owns or uses, including the Shared Corporate Services Platform, each subsidiary's own systems, and systems that service providers run for the group.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| IT Manager | Incident commander for security incidents; coordinates the MSP, forensic firm, and managed detection provider |
| CFO | Engages counsel and the cyber insurer; approves external communications; decides on payments holds with the bank |
| Finance President | Decides with counsel whether an event is a notification event under 16 CFR 314.2(m); oversees borrower notices |
| HR Director | Decides with counsel on employee notices |
| Subsidiary Presidents | Report incidents at their site to the group line; run local workarounds from the BIA |
| All workforce | Report suspected incidents immediately |

## 4. Policy statements
4.1 **Goal.** The goal of incident response is to protect people and customer information first, keep critical services running, meet every legal deadline, and learn from each event. (IR-8; 314.4(h)(1))
4.2 The group must maintain one incident response plan and runbooks for its most likely incidents, starting with compromise of the shared platform (P08). Subsidiaries must use the group plan; they may not run separate incident processes. (IR-8; RS.MA-01; 314.4(h)(2))
4.3 Workforce members must report any suspected incident **immediately**, and within 1 hour at most, to the group incident line. Examples: phishing clicks, unexpected MFA prompts, lost devices, misdirected customer or employee data, requests to change bank details, unusual system behavior. Good-faith reporting is never sanctioned. (IR-6; RS.MA-02)
4.4 **Decision authority.** The IT Manager may isolate devices, disable accounts, and revoke sessions at any subsidiary without prior approval. The CFO may ask the bank to hold payments. The CEO decides on shutting down shared services. (IR-4; 314.4(h)(3))
4.5 Every incident must be logged, categorized, and tracked to closure in the ticketing system under the Security category, including the time of discovery. (IR-5; 314.4(h)(6))
4.6 Notifications to regulators, individuals, the lender, the insurer, and other parties must meet the deadlines in the P08 notification matrix. Counsel must confirm each notification. A notification event affecting 500 or more consumers must be reported to the FTC no later than 30 days after discovery. (IR-6; RS.CO-02; 314.4(h)(4), (j))
4.7 No ransom may be paid without approval from the CEO, the Board chair, counsel, and the cyber insurer, and an OFAC sanctions check. (IR-4)
4.8 The incident response plan must be tested at least annually by a tabletop exercise that includes the subsidiary Presidents and the MSP, and after any major incident. (IR-3; GV.SC-08)
4.9 Weaknesses found during an incident must be added to the POA&M with an owner and date. Lessons learned must be documented within 30 days of closing an incident, and the plan must be revised as needed. (IR-4; ID.IM; 314.4(h)(5), (h)(7))

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.8). Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07) and the access reviews in this policy set.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. They must be written, risk-rated, approved by the right level under POL-01 4.5, and expire within 12 months.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; POL-01; FTC Safeguards Rule 16 CFR 314.4(h), (j); Fla. Stat. 501.171
