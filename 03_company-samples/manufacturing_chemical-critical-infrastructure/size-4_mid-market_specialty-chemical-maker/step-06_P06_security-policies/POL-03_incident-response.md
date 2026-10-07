# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Owner | Information Security Manager (CySO) |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-22 |
| Effective date | 2026-10-01 (replaces the 2024 IT-focused plan as the governing policy) |
| Review cycle | Annually (next review 2027-09-30) and after every significant incident or exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-7, IR-8, CP-2, CP-4, CP-10, AU-6, SI-4 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.CO-02, RS.CO-03, RS.AN-03, RC.RP-01, DE.AE-02, ID.IM-02 |
| Regulatory drivers | C-CHEMICAL-R02 (33 CFR 101.620(b)(6)-(7), 101.635, 101.650(g)); 33 CFR 6.16-1; 33 CFR 101.305; 40 CFR 302.6; 40 CFR 355.40-355.43; 40 CFR 68.81, 68.95-68.96; 29 CFR 1910.119(m); Fla. Stat. 501.171; C-CHEMICAL-R03 (proposed, tracked) |
| Supporting documents | P08 runbooks (OT intrusion; corporate ransomware) and notification matrix; STD-03; STD-05 |

## 1. Purpose
Make sure the company detects, contains, and recovers from cyber incidents without creating a process safety event, and meets every reporting duty on time.

## 2. Scope
All suspected or actual cyber incidents affecting IT, cloud, SaaS, TTRS, or OT at any site, and incidents at vendors that affect company systems or data.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Information Security Manager (CySO) | Incident manager for cyber incidents; owns this policy and the Cyber Incident Response Plan |
| Shift Supervisor (on duty) | First authority at the plant: puts units in a safe state; no IT action may override that decision |
| Port Plant Manager | Process incident commander; decides on unit restarts |
| COO | Chairs the crisis management team |
| General Counsel | Privilege, law enforcement, breach determinations, regulator contact strategy |
| Facility Security Officer | MTSA reports (6.16-1; 101.305) |
| VP EHS and Process Safety | Release reporting (302.6; 355.40-355.43); RMP and PSM incident investigations |
| MSSP | 24x7 detection and triage for IT and cloud (and OT from 2027-01-31) |

## 4. Policy statements
4.1 The company must keep a Cyber Incident Response Plan, made up of this policy, the P08 runbooks, and the notification matrix, and must execute and exercise it. (IR-8; 33 CFR 101.620(b)(6); 101.650(g)(2))
4.2 **Safety first.** In any incident touching OT, the Shift Supervisor's decision to put units in a safe state comes first. No containment step (isolating networks, shutting down servers) may be taken on OT without the Shift Supervisor's agreement, unless it is needed to stop an active manipulation. (IR-4; CP-12)
4.3 Everyone must report suspected incidents immediately to the control room or the CySO. (IR-6; 33 CFR 101.650(d)(1)(iv))
4.4 **Regulatory reporting.** The incident manager must make sure that: an actual or threatened cyber incident involving the Port plant is reported immediately to the FBI, CISA, and the Captain of the Port (33 CFR 6.16-1); breaches of security and suspicious activity are reported to the National Response Center without delay (101.305); and any release at or above a reportable quantity is reported immediately to the NRC, the LEPC, and the SERC (302.6; 355.40-355.43). Deadlines and contacts are in the P08 notification matrix. (IR-6; RS.CO-02)
4.5 Possible personal information breaches must go to the General Counsel the same day. Notices follow the law of each state where affected individuals reside (Florida: no later than 30 days after the breach is determined, Fla. Stat. 501.171). (IR-6; RS.CO-03)
4.6 Any incident that resulted in, or could reasonably have resulted in, a catastrophic release must also start an RMP and PSM incident investigation within 48 hours, with a cyber cause check. (IR-4; 40 CFR 68.81; 29 CFR 1910.119(m))
4.7 Incidents must be recorded in the incident register with timelines, evidence, decisions, and lessons learned. OT events from the OT sensor are incidents for recording purposes. (IR-5; 33 CFR 101.640)
4.8 The company must hold at least one cyber exercise each calendar year (no more than 18 months apart) and two cyber drills each calendar year at the Port plant, and must combine them with the RMP exercises where practical. Corrective actions must be tracked to closure. (IR-3; CP-4; 33 CFR 101.635(b)-(c); 40 CFR 68.96)
4.9 No ransom may be paid without the CEO's approval, legal advice, and a sanctions check against OFAC guidance. (IR-4)
4.10 Recovery must follow the BIA order (P05). An OT system may return to service only after its configuration is verified against the approved copy. (CP-10; RC.RP-01)
4.11 CIRCIA reporting is tracked as a proposed requirement and will be added when a final rule takes effect. (IR-6)

## 5. Compliance and enforcement
Checked through exercises, after-action reviews, the P07 assessment, and the annual Cybersecurity Plan audit.

## 6. Exceptions
Under POL-01 4.7. Statement 4.2 has no exceptions.

## 7. Related documents
POL-01; P08 `ir-runbook.md`, `ir-runbook-ransomware.md`, and `notification-matrix.csv`; emergency response plan (RMP 68.95); FSP; STD-03; STD-05
