# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (and Cris Santos Assurance, LLP) |
| Policy ID | POL-03 |
| Owner | Director of Information Security |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-22 |
| Effective date | 2026-10-01 (replaces the 2024 plan) |
| Review cycle | Annually (next review 2027-09-30), and after every major incident or exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-7, IR-8, AU-1, CP-1, CP-2 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RS.MI-01, RC.RP-01, ID.IM-04 |
| FTC Safeguards Rule | 16 CFR 314.4(h)(1)-(7) and (j) |
| Other | IRS Pub. 1345 (security incident reporting); 45 CFR 164.308(a)(6), 164.410; Fla. Stat. 501.171 and other state breach laws |
| Supporting standards | STD-02 Logging and monitoring standard; STD-07 Contingency and recovery standard |

## 1. Purpose
Make sure the Company detects, contains, reports, and recovers from security incidents and major vendor outages quickly, protects clients from refund and payment fraud, and meets every legal, IRS, and contractual notification deadline. With the P08 runbooks, this policy is the written incident response plan required by 16 CFR 314.4(h).

**Goals of the plan (314.4(h)(1)):** protect clients and their tax return information; stop refund diversion and payment fraud quickly; keep filing deadlines and client payrolls; meet every notice deadline; and learn from every event.

## 2. Scope
All security incidents and suspected incidents affecting Company systems, data, or service providers that hold Company data, and outages of third-party services that support High-criticality processes in the BIA (P05). It covers the offshore program, the CAS platform, and the Attest Firm's engagement platform.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Information Security | Incident commander for security incidents; coordinates the MSSP and forensics |
| Chief Information Officer | Technical recovery lead; contingency plan owner |
| Chief Operating Officer | Chairs the crisis management team for major incidents; approves external statements |
| General Counsel | Engages outside breach counsel; legal decisions on notices |
| Privacy Officer | Keeps the decision log; breach analysis for IRC 7216, FTC, state, and business associate duties |
| Director of Tax Operations | IRS e-file Responsible Official; IRS Stakeholder Liaison report; refund holds |
| CAS Practice Leader | CAS payment and payroll holds; client notices for CAS clients |
| Director of Marketing and Communications | Client, staff, and media communications through counsel |
| MSSP | 24x7 detection, first containment, and escalation within 30 minutes for high severity |
| All workforce | Report suspected incidents immediately |

## 4. Policy statements
4.1 The Company must maintain an incident response plan and runbooks for its most likely and most harmful incidents. At minimum these are business email compromise with taxpayer data theft, and ransomware with data extortion (with a tax software vendor outage variant) (P08). (IR-8; RS.MA-01; 314.4(h))

4.2 Workforce members, seasonal staff, interns, and offshore vendor staff must report any suspected incident **immediately**, and within 1 hour at most, to the security line or their manager. Examples: an MFA prompt they did not start, a client asking about an email "from the Company," a request to change bank details, a misdirected return, a lost device. Good-faith reporting is never sanctioned. (IR-6; RS.MA-02; 314.4(h)(4); 164.308(a)(6)(ii))

4.3 Every incident must be logged and tracked to closure in the security incident queue. The log must record three dates when they occur: **discovery** (first day known to any employee, officer, or other agent other than the attacker; starts the FTC clock under 314.4(j)(2) and the business associate clock under 164.410(a)(2)), **confirmation** (starts the IRS next-business-day clock under Pub. 1345), and **determination** (starts the Florida 30-day clock under Fla. Stat. 501.171). (IR-5; IR-4; 314.4(h)(6))

4.4 A severity 1 incident (any confirmed mailbox takeover with client data, ransomware, confirmed data theft, diverted refund or client payment, or an outage expected to exceed a High-criticality MTD) must activate the crisis management team, chaired by the Chief Operating Officer, within 2 hours. (IR-4; RC.RP-01; 314.4(h)(3))

4.5 The Privacy Officer, with the General Counsel and outside counsel, must decide whether an incident is a notification event under 16 CFR 314.4(j), a breach under state law, a breach of unsecured PHI for a covered entity client, or an unauthorized disclosure under IRC 7216, and must record the reasoning in the decision log. (IR-6; RS.AN-03)

4.6 Notices to the IRS, state tax agencies, the FTC, affected individuals, state regulators, consumer reporting agencies, covered entity clients, CAS clients, the cyber insurer, and law enforcement must meet the deadlines in the P08 notification matrix, including any shorter deadlines in client BAAs and contracts. Outside counsel must confirm each notice. (IR-6; RS.CO-02; RS.CO-03; 314.4(j); 164.410)

4.7 During a suspected mailbox or account compromise, every refund bank account, address, or email change entered in the tax software in the last 30 days, and every CAS bank change and pending payment, must be frozen until the client confirms it by call-back on the number on file. (IR-4; RS.MI-01)

4.8 The cyber insurer must be notified through its hotline before incident response vendors are engaged, as the policy requires. (IR-7)

4.9 No ransom or extortion payment may be made without approval from the Chief Executive Officer, outside counsel, and the insurer, a documented OFAC sanctions check, and a report to law enforcement. The default position is not to pay while backups are intact. (IR-4)

4.10 Incident response must be exercised at least annually for each runbook, including at least one exercise a year with outside counsel and the executive team, and before each filing season. (IR-3; ID.IM-02; 314.4(h)(7))

4.11 Lessons learned must be documented within 30 days of closing a major incident and fed into the risk register (P01), the POA&M (P07), training, and this plan. (IR-4; ID.IM-04; 314.4(h)(5), (h)(7))

4.12 Service providers must notify the Company of security events within their contract terms. The receipt of such a notice is itself a trigger to open an incident. (IR-6; SA-9; Fla. Stat. 501.171(6))

## 5. Compliance and enforcement
Violations are handled under POL-01 4.14. Compliance is checked through the annual independent assessment (P07) and exercise reports.

## 6. Exceptions
Exceptions follow POL-01 4.8. No exception may extend a legal notification deadline.

## 7. Related documents
P08 `ir-runbook.md`, `ir-runbook-ransomware.md`, and `notification-matrix.csv`; POL-01; STD-02; STD-07; 16 CFR 314.4(h) and (j); IRS Pub. 1345; 45 CFR 164.410; Fla. Stat. 501.171
