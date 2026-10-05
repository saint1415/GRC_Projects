# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | Operations Manager (incident commander), with the Office Manager (Security Coordinator) |
| Approved by | Owner and President, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after any incident that needed outside help or notification |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| Benchmarks and rules | C-CHEMICAL-R01 (6 CFR 27.230(a)(8), (a)(15), (a)(16), voluntary benchmark); 40 CFR 302.6; 40 CFR 355.40-355.43; 49 CFR 172.604; Fla. Stat. 501.171 (employee personal information) |

## 1. Purpose
Make sure the company keeps people safe, reports releases on time, and contains, reports, and recovers from security incidents, including any incident that touches the batch control system.

## 2. Scope
Everyone who works for the company and every system and copy of company information, including systems the MSP, the integrator, and SaaS vendors run for the company. A "security incident" includes any attempted or successful unauthorized access, use, change, or destruction of information or of a system; any unexplained change to a recipe, setpoint, or alarm limit; malware; lost or stolen devices; and suspicious attempts to buy or take hydrogen peroxide.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Operations Manager | Incident commander; decides the safe state of the blend room; leads release reporting |
| Office Manager | Cyber incident coordinator: calls the MSP and the insurer hotline; keeps the incident log |
| Owner and President | Decision maker for money, ransom, closing the site, and outside communications; backup incident commander |
| MSP | Technical response on office systems: isolate, investigate, rebuild, restore |
| Control system integrator | Technical response on the PLC, HMI, and gateway, on site, under the Operations Manager's direction |
| Cyber insurer and its panel vendors | Breach counsel and forensics, through the insurer's hotline |
| Everyone | Report suspected incidents at once |

## 4. Policy statements
4.1 The company keeps an incident response runbook for its most serious likely incident, an intrusion into the batch control system (P08), with printed copies in the blend room, at the loading dock, and in the office. (IR-8; RS.MA-01)

4.2 Report any suspected incident to the Operations Manager or the Office Manager **at once, and within 1 hour at most**, in person or by phone. If neither can be reached, report to the Owner. Examples: an HMI value or recipe that changed with no one at the screen, a mouse moving on its own, a strange pop-up or locked files, a phishing click, a lost laptop, or someone asking to buy hydrogen peroxide for cash. (IR-6; RS.MA-02; 27.230(a)(16))

4.3 The Office Manager logs every incident and suspicious activity, including those that turn out to be harmless, with the date found, what happened, what was done, and the outcome. (IR-5; 27.230(a)(16))

4.4 **Safety first.** Anyone who suspects the HMI or PLC cannot be trusted must stop the batch with the emergency stop and call the Operations Manager. The Operations Manager may stop all dosing, close tote valves, and hold any batch without asking anyone. Automatic dosing restarts only after the checks in the P08 runbook. (IR-4; RS.MI-01)

4.5 **Release reporting comes first.** For any fire or release, call 911 first. If a release reaches or may exceed a reportable quantity (sodium hypochlorite 100 lb, sodium hydroxide 1,000 lb, phosphoric acid 5,000 lb), the Operations Manager notifies the National Response Center immediately and, if people outside the site could be exposed, the LEPC and SERC immediately, whatever the cause (40 CFR 302.6; 355.40-355.43). A transport incident is also reported to the ERI provider. All other notices follow the P08 notification matrix. (IR-6; RS.CO-02)

4.6 For any suspected intrusion, ransomware, data theft, or account takeover, the Office Manager calls the cyber insurer's hotline before hiring any outside firm. If people were hurt or property was damaged, the Owner also notifies the general liability and pollution liability carriers, because the cyber policy excludes bodily injury and property damage. (IR-4; RS.MA-02)

4.7 No ransom may be paid without the Owner's approval, advice from breach counsel and the insurer, and an OFAC sanctions check. Recovery of the batch control system must never depend on paying. (IR-4)

4.8 The Office Manager reports any intrusion into the batch control system voluntarily to CISA and the FBI, with a target of 24 hours, after telling counsel. (IR-6; RS.CO-03; 27.230(a)(15))

4.9 If employee personal information may have been taken, the Office Manager, with counsel, decides whether notice is required under Fla. Stat. 501.171 and meets its deadlines. (IR-6; RS.CO-02)

4.10 The MSP, the integrator, and SaaS vendors must report security incidents affecting the company as their contracts require (POL-02 A.5). The Office Manager logs each report and handles it under this policy. (IR-6; SA-9)

4.11 The runbook is tested every year with a tabletop exercise that includes the MSP and the integrator, and after any real incident that used it. (IR-3; ID.IM-02)

4.12 Lessons learned are written up within 30 days of closing any incident that needed outside help or notification, and fed into the risk register, training, and the emergency action plan. (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Failing to report is a violation; reporting a mistake in good faith is never sanctioned. Compliance is checked in the yearly assessment (P07) and the yearly tabletop.

## 6. Exceptions
Exceptions follow POL-02 A.9. No exception may delay a safety action or a legally required notification.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; emergency action plan; POL-02; POL-04; Fla. Stat. 501.171
