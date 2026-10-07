# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (community water system, 2,850 population served) |
| Policy ID | POL-03 |
| Owner | Office Manager (security and compliance coordinator), with the Chief Operator for all plant decisions |
| Approved by | Owner and General Manager, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Every August (next review 2027-08-31), and after any incident that needed outside help or a notice |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8, CP-2, CP-4 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.MI-01, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| Regulatory basis | Tier 1 public notice and primacy agency consultation, 40 CFR 141.202(b); report of a violation within 48 hours, 141.31(b); public notice certification, 141.31(d)(1); Ground Water Rule fallback monitoring and reporting, 141.403(b)(3)(i)(A) and 141.405(a)(1); customer data breach notice, Fla. Stat. 501.171. Readiness for the SDWA section 1433 emergency response plan, 42 U.S.C. 300i-2(b) |

## 1. Purpose
Make sure the company keeps delivering safe water during a cybersecurity incident, then contains it, reports it on time, and recovers, and meets every public notice and breach notice deadline.

## 2. Scope
All 7 employees and the contractors and vendors who support company systems (SCADA integrator, MSP, remote monitoring vendor, billing vendor). It covers the WTSS, the office network, company phones, and the SaaS systems. A "security incident" includes any attempted or successful unauthorized access, use, change, or destruction of information or of a control system, unexplained control actions, malware, lost or stolen devices, and a vendor's security incident that affects company systems or data.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Licensed operator on duty or on call | First actions for safe water (4.3): hand operation, grab samples, disconnecting remote access |
| Chief Operator | Incident lead for any incident that touches the WTSS; leads the Tier 1 decision and primacy agency consultation; directs the integrator |
| Office Manager | Incident lead for office and SaaS incidents; keeps the incident log; directs the MSP; handles customer data breach notices with breach counsel |
| Owner and General Manager | Calls the cyber insurer; approves spending, outside communications, and any public notice; decides with the Chief Operator on a Tier 1 notice |
| MSP and SCADA integrator | Technical response under their contracts and the P08 runbook |
| Cyber insurer and panel vendors | Breach counsel and forensics, engaged through the insurer's 24x7 hotline |
| All staff | Report suspected incidents at once |

## 4. Policy statements
4.1 **Runbook.** The company must keep an incident response runbook for its most likely serious incident, a remote-access compromise of the HMI (P08), as the cyber annex of the emergency plan. A printed copy with the contact sheet and notification matrix must be kept in the plant control room binder and at the Owner's and Chief Operator's homes. (IR-8; RS.MA-01)

4.2 **Report at once.** Staff must report any suspected incident **at once, and within 1 hour at most**, by phone. Operators report to the Chief Operator (or the Owner if the Chief Operator cannot be reached): an HMI cursor or screen moving when no one is using it, a setpoint, pump mode, or alarm limit that no one on shift changed, an unknown remote session, or an alarm with no process cause. Office staff report to the Office Manager: a clicked phishing link, a strange pop-up or locked files, a lost phone or laptop, or a request to change bank details. (IR-6; RS.MA-02)

4.3 **Safe water first.** If there is any doubt about the integrity of SCADA control, the licensed operator on site must, before anything else: put the hypochlorite feed and any affected well or pump in hand at the panel, return the feed to the normal rate, take a chlorine grab sample, and end the remote desktop session or unplug the HMI computer's network cable without turning it off. No one needs permission to take these actions. (CP-2; IR-4; RS.MI-01)

4.4 **Residual record fallback.** If the continuous chlorine residual record is lost or cannot be trusted, grab samples must be taken every 4 hours and logged on paper until the analyzer and its record are verified, and continuous monitoring must resume within 14 days (40 CFR 141.403(b)(3)(i)(A)). If the state-determined minimum residual is not restored within 4 hours, the Chief Operator must notify the state by the end of the next business day (141.405(a)(1)). (CP-2; DE.CM-01)

4.5 **Tier 1 decision.** The Chief Operator and the Owner must decide as soon as practical whether the incident caused a failure or significant interruption in key treatment processes, or another Tier 1 situation (40 CFR 141.202(a) Table 1). If so, the notice must reach persons served, and primacy agency consultation must start, no later than 24 hours after the company learns of the situation (141.202(b)). The time the company learned of the situation must be written in the incident log. (IR-6; RS.CO-02)

4.6 **Other reports.** A violation of a drinking water regulation, including missed monitoring, must be reported to the state within 48 hours (141.31(b)). A public notice certification must be sent within 10 days of completing the notice (141.31(d)(1)). All other notices follow the P08 notification matrix. (IR-6; RS.CO-03)

4.7 **Outside help.** For any suspected compromise of the WTSS or any data theft, the Owner must call the cyber insurer's breach hotline before hiring any outside firm. The Chief Operator calls the integrator, and the Office Manager calls the MSP. The company reports any confirmed unauthorized control action to the FBI and, voluntarily, to CISA, within 24 hours of declaring the incident (company rule). (IR-4; IR-6; RS.MA-02)

4.8 **Customer data.** If customer personal information may be involved, the Office Manager and breach counsel decide whether there was a breach of security under Fla. Stat. 501.171 and send any required notices within the deadlines in the P08 matrix. Vendors that hold customer data must report their own breaches to the company within the 10 days allowed by 501.171(6), and contracts must say so. (IR-6; RS.AN-03)

4.9 **Ransom.** No ransom may be paid without the Owner's approval, advice from breach counsel and the insurer, and an OFAC sanctions check. (IR-4)

4.10 **Evidence.** Evidence must be preserved before the HMI computer is rebuilt, where this does not delay 4.3. Keep the HMI computer powered on and disconnected, photograph screens and panel states, and export the remote desktop connection history. (IR-4; RS.AN-03)

4.11 **Log.** The Office Manager must log every incident, including those that turn out to be harmless: when it was found, when the company learned of any Tier 1 situation, what was done, and the outcome. (IR-5)

4.12 **Exercise.** The runbook must be exercised every year with a tabletop that includes the integrator and the MSP, together with a hand-operation drill, and after any real incident that used it. The first exercise is due by 2026-11-30. (IR-3; CP-4; ID.IM-02)

4.13 **Lessons learned.** Lessons learned must be written within 30 days of closing any incident that needed outside help or a notice, and fed into the risk register, the emergency plan, and training. (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Failing to report is a violation; reporting a mistake in good faith is never sanctioned. Compliance is checked through the annual exercise and the independent assessment (P07).

## 6. Exceptions
Exceptions follow POL-02 A.9. No exception may delay a safe-water action under 4.3 or a legally required notice.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; 2023 emergency plan (to be revised with the cyber annex by 2026-10-31); POL-02; POL-04; 40 CFR Part 141 Subpart Q; Fla. Stat. 501.171
