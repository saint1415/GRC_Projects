# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | Plant Superintendent (incident commander and 18 CFR 12.10 reports) |
| Approved by | Owner and General Manager, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Every July with the risk register (next review 2027-07-31), and after any incident reported to FERC or any tabletop exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8, CP-2 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.MA-04, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| FERC and Part 12 | 18 CFR 12.10(a) and (b); 12.3(b)(4)(ii), (viii), (xi); 12.12(a)(1)(iii)(B); Security Program Rev. 3A 3.2, 3.3.3, 3.3.4, 4.2; Table 9.3a intrusion detection and response (voluntary benchmark) |

## 1. Purpose
Make sure the company keeps the dam under control, detects and contains physical and cyber security incidents, reports them to FERC and others on time, and recovers safely.

## 2. Scope
All workforce members of Cris Santos Company and outside parties with access (controls integrator, MSP, monitoring vendor). Covers the HPCDMS, the monitoring service, office IT and SaaS, cameras and locks, and the project works. A "security incident" includes any attempted or successful unauthorized access to or use of a system, any command, setpoint, or program change nobody can explain, tampering with the project works, instruments, or panels, lost keys or devices, and exposure of CEII-type documents or employee personal information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Operator-mechanic on duty or on call | First responder: puts affected gates and units in local control, confirms positions, calls the Plant Superintendent |
| Plant Superintendent | Incident commander; decides whether the event is a condition affecting safety (18 CFR 12.10) and makes the FERC reports; decides on EAP activation |
| Controls and Electrical Technician | OT technical lead: cuts remote paths, preserves logs, works with the integrator |
| Owner and General Manager | Backup incident commander; calls the cyber insurer; approves spending, outside statements, and any ransom decision; FERC primary security contact |
| Office and Compliance Administrator | Keeps the incident log and evidence folder; calls the MSP for office incidents; assesses any exposure of employee personal information with counsel |
| Controls integrator, MSP, insurer panel firms | Technical help under their contracts and the insurer's direction |
| All workforce | Report suspected incidents at once |

## 4. Policy statements
4.1 The company must keep an incident response runbook for its most likely serious incident, unauthorized access to spillway and turbine control systems (P08), with printed copies and the contact sheet in the control room, the office, and the Plant Superintendent's home. (IR-8; RS.MA-01)

4.2 **Safety first.** In any suspected OT incident, the first action is to put the affected gates and units in local control and confirm their physical positions by eye. No investigation step may delay that. (IR-4; CP-2)

4.3 Workforce members must report any suspected incident **at once**: within 15 minutes for anything touching gates, units, instruments, the tailrace warning devices, or the control room (unexpected gate movement, an HMI session nobody claims, strange readings, a forced lock, someone near the panels), and within 1 hour for anything else (a suspicious email, a lost phone, a document shared by mistake). Report by phone to the Plant Superintendent, or to the Owner if the Plant Superintendent cannot be reached. (IR-6; RS.MA-02)

4.4 **FERC report.** The Plant Superintendent must decide promptly whether an incident is a condition affecting the safety of the project. **Security incidents (physical and/or cyber) and any misoperation of a gate are such conditions** (18 CFR 12.3(b)(4)(ii), (xi)). They must be reported to the FERC Regional Engineer by email or telephone as soon as practicable after discovery, preferably within 72 hours, followed by a written report within the time the Regional Engineer specifies, verified under 12.13 (12.10(a)). Any rescue, serious injury, or death at the project is reported under 12.10(b). Safety reports never wait for counsel or the insurer. (IR-6; RS.CO-02)

4.5 Suspicious activity and security incidents must also be reported to the FERC Regional Office as soon as practical (usually within one working day), unless law enforcement restricts it, and should be entered in the HSIN Dams Sector suspicious activity tool once the company has an account (Rev. 3A 3.2, 4.2). The same call can cover 4.4. (IR-6; RS.CO-03)

4.6 If an incident could lead to a project emergency, the EAP must be activated under its own procedures. The sheriff and county emergency management must be called in parallel, and the county that operates the weir downstream must be told if flows could be affected (Rev. 3A 4.2). A security closure of the canoe launch or bank-fishing area for 30 days or less needs notice to the FERC Regional Office as soon as practical (usually within one working day); longer closures need prior coordination (Rev. 3A 3.3.4). (IR-4; CP-2; RS.MA-04)

4.7 Other notices (the cyber insurer, the cooperative, voluntary reports to the FBI and CISA, and Florida breach notices if employee personal information is breached) must follow the P08 notification matrix. Counsel reviews notices other than safety reports. (IR-6; RS.CO-02)

4.8 Every incident must be logged, including those that turn out to be harmless, with the discovery time, what happened, gate and unit positions, actions, and the outcome. Evidence (HMI event journal, remote session log export, firewall and camera records, PLC copies) must be preserved before it rolls over, with a record of who collected it and when. Evidence and incident records are Restricted (POL-04). (IR-5; RS.AN-03)

4.9 No ransom may be paid without the Owner's approval, advice from the insurer and counsel, and an OFAC sanctions check. Paying does not remove any reporting duty. (IR-4)

4.10 Vendors must report incidents that affect the company within 24 hours under their contract terms (POL-02 A.5). The Office and Compliance Administrator logs each report and the Plant Superintendent handles it under this policy. (IR-6; SA-9; GV.SC-08)

4.11 The runbook must be exercised every year in a tabletop with the integrator, and with the sheriff and county emergency management at least every other year, alternating physical and cyber scenarios. It may be combined with the annual EAP readiness test (18 CFR 12.25(b)). It is also exercised after any real incident that used it. (IR-3; ID.IM-02)

4.12 Lessons learned must be written up within 30 days of closing any incident that was reported to FERC or needed outside help, and fed into the risk register, the POA&M, this policy, and training. (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Breaking this policy is handled under POL-02 A.4. Failing to report a known incident is a serious violation; reporting in good faith is never punished. Compliance is checked through the annual tabletop and the independent assessment (P07).

## 6. Exceptions
Exceptions follow POL-02 A.9. No exception may delay local control of gates or a report under 18 CFR 12.10.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; Emergency Action Plan; Owner's Dam Safety Program (communication and reporting section); POL-02; POL-04
