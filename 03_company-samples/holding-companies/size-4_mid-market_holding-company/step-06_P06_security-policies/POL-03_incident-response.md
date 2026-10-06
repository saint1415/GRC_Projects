# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. and its subsidiaries |
| Policy ID | POL-03 |
| Owner | Security Manager |
| Approved by | CEO |
| Approval date | 2026-09-22 |
| Effective date | 2026-10-01 (replaces the 2024 incident response plan) |
| Review cycle | Annually (next review 2027-09-30), and after every severity 1 incident or exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-7, IR-8, AU-2, AU-6, AU-11, CP-2, CP-10 |
| CSF 2.0 | ID.IM-04, DE.AE-08, RS.MA-01, RS.MA-04, RS.AN-06, RS.CO-02, RC.RP-01, RC.CO-03 |
| FTC Safeguards Rule (Finance) | 16 CFR 314.4(h)(1)-(7), (j) |
| HIPAA (group health plan) | 45 CFR 164.308(a)(6), (a)(7); 164.314(b)(2)(iv); 164.402-164.410 |
| Supporting standards | STD-02 Logging and monitoring; STD-07 Contingency and recovery; runbooks in P08 |

## 1. Purpose
Make sure the group detects, contains, and recovers from security incidents quickly, meets every notice deadline, and learns from each event. For Finance, this policy and the P08 runbooks are the written incident response plan required by 16 CFR 314.4(h). For the group health plan, they are the sponsor's security incident procedures.

## 2. Scope
Every suspected or confirmed security incident affecting any group company, its systems, its data, or data that service providers hold for it, including incidents at acquired companies and plant systems.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Crisis management team (chair: CFO; CEO, General Counsel, vCISO, VP of Information Technology, VP of Human Resources, affected subsidiary Presidents) | Business decisions, external statements, extortion decisions, resources |
| Incident commander (Security Manager; backup: VP of Information Technology) | Runs the technical response |
| General Counsel | Privilege, notification decisions, regulators, law enforcement, contracts |
| Finance President | Decides with counsel whether a Safeguards Rule notification event occurred |
| VP of Human Resources (plan Privacy Official) | Decides with counsel whether a breach of plan PHI occurred; reports to the Benefits Committee |
| Subsidiary Presidents | Local escalation, workarounds, and customer communication for their company |
| MSSP | 24x7 detection, host isolation, and escalation |
| All workforce | Report suspected incidents immediately |

## 4. Policy statements
4.1 Every workforce member must report a suspected incident immediately to the service desk or the incident line. Reporting in good faith is never sanctioned. (IR-6; DE.AE-08)
4.2 The incident commander must classify each incident by severity (1 to 4) using the P08 criteria and escalate severity 1 and 2 incidents to the crisis management team and the affected subsidiary Presidents within 1 hour. (IR-4; RS.MA-04)
4.3 **Record discovery and determination dates.** The incident log must record when the incident was first known to any workforce member or agent, and when a breach was determined. These dates start the FTC 30-day clock (16 CFR 314.4(j)(2)), the HIPAA 60-day clock (164.404(a)(2)), and Florida's 30-day clock (Fla. Stat. 501.171). (IR-5; RS.AN-06)
4.4 For any incident that may involve personal information, Finance customer information, or plan PHI, the General Counsel must be told the same day, and outside counsel engaged through the cyber insurer before forensics begins. (IR-4; RS.MA-01)
4.5 The General Counsel must keep a **decision log** for each severity 1 or 2 incident: the data and people involved by company and state of residence, the Safeguards Rule notification event decision, the HIPAA four-factor assessment (164.402), each notice and its deadline, and any law enforcement delay request. (IR-6; RS.CO-02; 314.4(h)(6))
4.6 Notices must follow the P08 notification matrix. The holding company, acting for a subsidiary under the intercompany services agreement, must tell the affected subsidiary's President the same day it has reason to believe the subsidiary's data was involved; the legal outer limit for an agent under Florida law is 10 days after determination. Security incidents involving plan ePHI must be reported to the Benefits Committee (164.314(b)(2)(iv)). (IR-6; RS.CO-02; 314.4(j))
4.7 Evidence must be preserved with a chain-of-custody record, and logs must be exported before they expire. (AU-11; RS.AN-07)
4.8 **Extortion payments** require the CEO, the board chair, the General Counsel, the cyber insurer, and an OFAC sanctions check. The default position is not to pay while clean backups exist. Paying never removes notice duties. (IR-4)
4.9 **Payment fraud.** Any suspected fraudulent payment must be reported to the bank fraud line by the Treasurer or CFO immediately, before any other step, and handled under the payment fraud runbook. (IR-4; RS.MI-01)
4.10 Recovery must follow the BIA recovery order (P05) and the validation steps in P08. (CP-10; RC.RP-01)
4.11 A lessons-learned review must be held within 14 days after recovery and documented within 30 days; the runbooks, risk register, and POA&M must be updated (314.4(h)(5), (h)(7)). (IR-4; ID.IM-03)
4.12 The plan and runbooks must be exercised at least twice a year, including the subsidiaries, a key vendor, and a walkthrough of the FTC and plan breach notices. (IR-3; ID.IM-02)
4.13 Incident team members, subsidiary leads, and benefits staff must be trained on their roles each year. (IR-2; PR.AT-02)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.8). Compliance is checked through exercises, the annual independent assessment (P07), and post-incident reviews.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. No exception may remove or delay a legal notice.

## 7. Related documents
POL-01; P08 `ir-runbook.md`, `ir-runbook-payment-fraud.md`, and `notification-matrix.csv`; BIA (P05); STD-02; STD-07; cyber insurance and crime policies
