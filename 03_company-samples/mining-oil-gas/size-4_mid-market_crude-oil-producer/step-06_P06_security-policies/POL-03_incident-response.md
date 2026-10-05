# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Owner | Security Manager, with the SCADA and Automation Manager for OT response |
| Approved by | Chief Operating Officer, with the VP Operations agreeing to the OT and field statements |
| Approval date | 2026-09-16 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after every major incident or exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-7, IR-8, CP-2 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RS.MI-01, RC.RP-01, ID.IM-02, ID.IM-03 |
| Benchmark (N21-BM) | SP 800-82 Rev. 3 sections 3.3.8 (incident response planning), 6.4 (respond), 6.5 (recover) |
| Binding rules referenced | 49 CFR 195.52 and 195.54 (gathering system accident notice and report); 40 CFR 110.6 (oil discharge notice); Fla. Stat. 501.171(3)-(6) and other states' breach laws |
| Supporting standards | STD-08 Logging and monitoring standard; STD-07 Backup and recovery standard |

## 1. Purpose
Make sure the company detects, contains, reports, and recovers from security incidents in business IT and OT quickly, keeps people and the environment safe, protects the gathering system, and meets every legal and contractual notification deadline.

## 2. Scope
All security incidents and suspected incidents affecting company systems, SCADA, field devices, data, or vendors that hold company data or connect to company systems, at every site. It applies with the emergency response plan and the pipeline emergency procedures, which keep authority over safety and pipeline decisions.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Security Manager | Incident commander for security incidents; coordinates the MDR provider and forensics |
| SCADA and Automation Manager and OT Security Engineer | OT lead: SCADA isolation, controller integrity checks, OT rebuild |
| Chief Operating Officer | Chairs the crisis management team (CMT) for major incidents; approves external statements with the General Counsel |
| VP Operations and Field Superintendents | Manual operations and shut-in decisions; safety comes first |
| Control Room Manager and OCC shift lead | First report from the control room; manual operations from the OCC or BCC |
| Pipeline Compliance Manager | Decides on and makes the gathering system accident notices (49 CFR 195.52) |
| HSE Director | Oil discharge and spill notices; emergency response plan |
| General Counsel, with outside breach counsel | Legal privilege, breach determinations, notices, the decision log |
| MDR provider | 24x7 IT detection, IT host isolation, escalation within 30 minutes for high severity |
| All workforce | Report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain an incident response plan with an OT annex and runbooks for its most likely and most harmful incidents. At minimum these are ransomware spreading from business IT toward SCADA, and unauthorized remote command of field equipment through a third-party access path (P08). (IR-8; RS.MA-01)
4.2 Workforce members must report any suspected incident **immediately**, and within 1 hour at most. **Production Controllers and field staff must report unexplained HMI behavior, setpoint or valve changes nobody ordered, controller faults with no known cause, and unknown devices in cabinets to the OCC shift lead, who calls the Security Manager and the OT Security Engineer.** Good-faith reporting is never sanctioned. (IR-6; RS.MA-02)
4.3 Every incident must be logged, given a severity, and tracked to closure in the security incident queue. The date and time of discovery must be recorded when the incident is opened. (IR-5; IR-4)
4.4 **Authority to isolate.** The OT Security Engineer or the SCADA and Automation Manager, with the VP Operations, may open the IT/OT connections (the OT DMZ at the OCC and the site firewalls at the BCC and the South Florida office) at any time. If neither can be reached within 15 minutes, the OCC shift lead may do so. The MDR provider may isolate IT hosts but must not act on OT devices. Isolation must never disable a safety function; if site safety is in doubt, the Field Superintendent shuts the site in under the emergency response plan. (IR-4; RS.MI-01)
4.5 A severity 1 incident (any ransomware, any intrusion into the SCADA network, an unauthorized command to field equipment, or confirmed exfiltration of personal information) must activate the CMT, chaired by the COO, within 2 hours. (IR-4; RC.RP-01)
4.6 **Gathering system link.** Any cyber event that affects monitoring or control of the gathering system must trigger the pipeline emergency procedures at once. The Pipeline Compliance Manager must be called and must decide on the National Response Center telephone notice under 49 CFR 195.52, which is due at the earliest practicable moment and no later than 1 hour after confirmed discovery. The cyber investigation must never delay this notice. (IR-6; RS.CO-03)
4.7 General Counsel, with outside breach counsel, must decide whether an incident is a breach of personal information under the law of each affected state, document the decision and the facts in the decision log, and retain it with the incident record. A Florida determination that notice is not required must be in writing, kept for at least 5 years, and sent to the Department of Legal Affairs within 30 days (Fla. Stat. 501.171(4)). (IR-6; RS.AN-03)
4.8 Notifications to individuals, regulators, the National Response Center, the cyber insurer, shippers, partners, lenders, and law enforcement must meet the deadlines in the P08 notification matrix. Outside counsel must confirm each legal notice before it is sent. The HSE Director makes oil discharge notices immediately under 40 CFR 110.6 without waiting for the cyber investigation. (IR-6; RS.CO-02)
4.9 The cyber insurer must be notified through its hotline before incident response vendors are engaged, as the policy requires. (IR-7)
4.10 No ransom may be paid without approval from the CEO, General Counsel, and the insurer, a documented OFAC sanctions check, and a report to law enforcement. A decryptor must never be run on SCADA servers, HMIs, or engineering workstations; they are rebuilt from verified images. (IR-4)
4.11 Incident response must be exercised at least annually for each runbook. Each operating area must hold an OT tabletop each year with its Field Superintendent, and the CMT must hold one exercise a year with the CEO and General Counsel. At least one exercise a year must be held jointly with a pipeline emergency drill. (IR-3; ID.IM-02)
4.12 Lessons learned must be documented within 30 days of closing a major incident or exercise and fed into the risk register (P01), the POA&M (P07), and the contingency plan. (IR-4; ID.IM-03)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.8). Compliance is checked through the annual independent control assessment (P07), exercise reports, and the incident log.

## 6. Exceptions
Exceptions follow POL-01 section 4.10. No exception may extend a legal notification deadline or delay a safety or pipeline notice.

## 7. Related documents
P08 `ir-runbook.md`, `ir-runbook-ot-remote-access.md`, and `notification-matrix.csv`; POL-01; STD-07; STD-08; emergency response plan; pipeline emergency procedures; 49 CFR 195.52; Fla. Stat. 501.171
