# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Owner | Security Manager |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2024 incident response plan) |
| Review cycle | Annually (next review 2027-09-30), after every significant incident or exercise, and after any FCC rule change on breach or outage notice |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-7, IR-8, AU-6, CP-2, SI-4 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, DE.AE-02, ID.IM-01 |
| FCC, CALEA, and state rules | 47 CFR 64.2011; 64.2009(f); 1.20003(c); 4.9; 4.18; 64.6305(a)(2); Fla. Stat. 501.171 |
| Supporting standards | STD-02 Logging and monitoring standard; STD-07 Contingency and recovery standard |

## 1. Purpose
Make sure the company detects, contains, and recovers from security incidents, meets every notification clock (CPNI, CALEA, outage and PSAP, state breach law), and protects 911 calling while it responds.

## 2. Scope
All security incidents affecting company systems, networks, customer data, or lawful-intercept systems, including incidents at vendors that hold company data, and any outage caused or worsened by a security incident or by containment actions.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Crisis management team (chair: COO) | Business, legal, and communications decisions for severity 1 incidents |
| Incident commander (Security Manager; backup IT Director) | Runs the response; keeps the incident log |
| NOC Director | Service impact, PSAP notice, NORS, and DIRS |
| Vice President of Regulatory Affairs | CPNI breach determination with counsel; law enforcement notice through the FCC reporting facility; RMD and opt-out failure notices |
| Vice President of Network Operations | CALEA compromise reports |
| General Counsel | Privilege, breach counsel, forensics engagement, state law notices |
| MDR provider | 24x7 detection, triage, and endpoint and cloud containment |
| All workforce and vendor agents | Report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain an incident response plan and runbooks for its most likely high-impact incidents: a network intrusion exposing CPNI and ransomware that disrupts operations (P08), plus the NOC outage and storm plan. (IR-8; RS.MA-01)
4.2 Workforce members and vendor agents must report any suspected incident **immediately**, and within 1 hour at most, to the NOC (24x7) or the security team. Examples: unexpected configuration changes or reboots on network elements, unknown accounts, pretext calls asking for call detail, phishing clicks, lost devices, CPNI sent to the wrong person, and chatbot answers about another customer's account. Good-faith reporting is never sanctioned. (IR-6; RS.MA-02)
4.3 Every incident must be logged, categorized, and tracked to closure in the ticketing system under the Security category, recording the time of **discovery** and, for CPNI, the time of **reasonable determination**. This register is also the CPNI breach record (47 CFR 64.2011(d)), kept at least 2 years. (IR-5)
4.4 **Severity 1** (crisis management team convened): confirmed intruder on a network element, voice core, management plane, or SYS-10; confirmed CPNI exfiltration; ransomware; any incident affecting 911 calling. (IR-4)
4.5 **Service first.** Before any containment action that could affect service (isolating an SBC, a router, or a central office), the NOC Director must assess the effect on voice and 911 and start the PSAP and NORS clocks if they apply. (IR-4; CP-2; 4.9(h))
4.6 The Vice President of Regulatory Affairs, with counsel, must decide whether an incident is a CPNI breach under 64.2011(e) and record the date and basis of the reasonable determination. The determination must not wait for forensics to finish. (IR-6)
4.7 **Notification deadlines.** Notices must follow the P08 notification matrix. Counsel confirms each notice. The current 47 CFR 64.2011 applies until the FCC publishes an effective date for the 2023 amendments; the matrix is rechecked at the start of every incident. (IR-6; RS.CO-02; RS.CO-03)
- **CPNI breach:** USSS and FBI through the FCC reporting facility as soon as practicable and no later than 7 business days after reasonable determination; no customer or public notice until 7 full business days after that notice, unless the investigating agency agrees or directs otherwise. (64.2011(a)-(c))
- **CALEA:** any compromise of a lawful interception or of call-identifying information, and any unlawful electronic surveillance on company premises, to the affected law enforcement agencies within a reasonable time after discovery. (1.20003(c))
- **Outages:** PSAP notice within 30 minutes; NORS notification within 120 minutes (wireline) or 240 minutes (VoIP with a PSAP affected), whatever the cause. (4.9)
- **Opt-out failure:** written notice to the FCC within 5 business days. (64.2009(f))
- **State breach laws:** Florida (Fla. Stat. 501.171) and the law of each state where affected individuals reside.
4.8 **Ransom.** No ransom may be paid without approval from the CEO, counsel, and the cyber insurer, an OFAC sanctions check, and a report to law enforcement. The default position, approved by the CEO, is not to pay while clean backups exist. (IR-4)
4.9 **Evidence.** Network element logs, TACACS+ accounting, cloud logs, and SBC logs must be preserved to write-once storage on day 0 of any network intrusion, before local retention rolls over. Forensics on SYS-10 may be done only by or under the supervision of the CALEA-authorized employees, and no one may view intercept content. (AU-9; IR-4)
4.10 The incident response plan must be tested at least annually by tabletop, including the NOC, regulatory affairs, customer operations, counsel, and the MDR, and after any major incident. (IR-3)
4.11 Lessons learned must be documented within 30 days of closing a severity 1 or 2 incident and added to the risk register, the POA&M, CPNI training, and, where relevant, the next CPNI certification statement. (IR-4; ID.IM-01)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.8. Compliance is checked through the annual assessment (P07), the annual tabletop, and review of the incident log by the vCISO each quarter.

## 6. Exceptions
Exceptions follow POL-01 section 6. No exception may delay a regulatory notice.

## 7. Related documents
POL-01; POL-04; P08 runbooks and notification matrix; NOC outage and storm plan; CALEA SSI policies; cyber insurance policy
