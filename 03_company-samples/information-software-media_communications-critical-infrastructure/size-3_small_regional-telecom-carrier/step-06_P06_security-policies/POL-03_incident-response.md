# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | IT Manager |
| Approved by | COO |
| Effective date | 2026-09-04 |
| Review cycle | Annually (next review 2027-09-04), and after major changes, incidents, or FCC rule changes |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-01 |
| FCC and CALEA rules | 64.2011; 1.20003(c); 4.9; 4.18 |

## 1. Purpose
Make sure the company detects, contains, reports, and recovers from security incidents quickly and lawfully, and meets the CPNI breach, CALEA compromise, and outage reporting deadlines, which keep running during a cyber incident.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary staff) at CO-1, CO-2, the warehouse and fleet yard, remote cabinets, and remote work locations, and the agents of vendors who access company systems, including the overflow call center. Covers all systems and data, including systems that vendors operate for the company. It applies to customer proprietary network information (CPNI), lawful-intercept information, subscriber personal information, network configuration and outage information, and all other company information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| IT Manager | Incident commander for security incidents; coordinates the managed detection provider and forensic firm |
| NOC Manager | Outage response, PSAP notifications, and NORS and DIRS filings during any incident that affects service |
| Regulatory Affairs Manager (privacy lead) | CPNI breach determination with counsel; law enforcement notice through the FCC reporting facility; breach records |
| Vice President of Network Operations | CALEA compromise reports to law enforcement; approves network isolation that affects service |
| COO | Engages counsel and the cyber insurer; approves external communications |
| All workforce and vendor agents | Report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain an incident response plan and runbooks for its most likely incidents, starting with a network intrusion exposing CPNI (P08). (IR-8; RS.MA-01)
4.2 Workforce members and vendor agents must report any suspected incident **immediately**, and within 1 hour at most, to the NOC (24x7) or the IT Manager. Examples: unexpected configuration changes, unknown accounts on network elements, pretext calls asking for call detail, phishing clicks, lost devices, and CPNI sent to the wrong person. Good-faith reporting is never sanctioned. (IR-6; RS.MA-02)
4.3 Every incident must be logged, categorized, and tracked to closure in the ticketing system under the Security category. This register also serves as the CPNI breach record required by 47 CFR 64.2011(d). (IR-5)
4.4 The Regulatory Affairs Manager, with counsel, must decide whether an incident is a CPNI breach under 64.2011(e) and must record the date and basis of the "reasonable determination." (IR-6)
4.5 **Notification deadlines.** Notices must meet the P08 notification matrix. Counsel confirms each notice. (IR-6; RS.CO-02; RS.CO-03)
- **CPNI breach:** notify the USSS and FBI through the FCC reporting facility as soon as practicable and no later than 7 business days after reasonable determination. Do not notify customers or the public until 7 full business days after that notice, unless the investigating agency agrees to earlier notice or directs a delay. (64.2011(a)-(c))
- **CALEA:** report any compromise of a lawful interception or of call-identifying information, and any unlawful electronic surveillance on company premises, to the affected law enforcement agencies within a reasonable time after discovery. (1.20003(c))
- **Outages:** PSAP notice within 30 minutes and NORS notification within 120 minutes (wireline) for qualifying outages, whatever the cause. (4.9)
- **State breach laws:** Florida (Fla. Stat. 501.171) and the law of each state where affected individuals reside, when personal information as those laws define it is involved.
4.6 No ransom may be paid without approval from the Chief Executive Officer, counsel, and the cyber insurer, and an OFAC sanctions check. (IR-4)
4.7 The incident response plan must be tested at least annually by tabletop exercise, including the NOC and the Regulatory Affairs Manager, and after any major incident. (IR-3)
4.8 Lessons learned must be documented within 30 days of closing an incident and added to the risk register and, where relevant, to CPNI training. (IR-4; ID.IM-01)

## 5. Compliance and enforcement
Violations are handled under the sanctions procedure (POL-01 section 4.8), which expressly covers misuse of CPNI (47 CFR 64.2009(b)). Sanctions range from retraining to termination, and for vendor agents, removal from company work. Compliance is checked through the annual control assessment (P07), the access reviews in POL-02, and the evidence gathered for the annual CPNI certification.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. They must be written, risk-rated, approved by the policy owner (or by the Chief Executive Officer for High risk), and expire within 12 months. No exception may permit a practice the CPNI, CALEA, or outage rules prohibit.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; POL-01; NOC outage escalation procedure; CALEA SSI policies; 47 CFR 64.2011; 47 CFR Part 4
