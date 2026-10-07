# Incident Response Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-03 |
| Owner | Group CISO, with the Group General Counsel for notifications |
| Approved by | Board risk committee |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), after every Severity 1 incident, and after each cross-division exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8, CP-2, CP-4, CP-9, CP-10 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, RC.RP-03, ID.IM-02 |
| Regulatory basis | 40 CFR 302.6; 40 CFR 355.40 to 355.43; 40 CFR 68.81, 68.95, 68.96; 33 CFR 6.16-1, 101.305, 101.635, 101.650(g); 49 CFR 171.15, 171.16; Form 8-K Item 1.05; state breach laws |
| Division supplements | Specialty Chemicals: safe state first and RMP incident investigation. Distribution: Terminal T1 Coast Guard reporting and drills. Hazmat Transport: en route incidents, DOT reports, and ELD outages |

## 1. Purpose
Make sure the group detects, contains, and recovers from cyber incidents consistently across divisions, keeps people and the community safe while it does, and meets every release, Coast Guard, DOT, SEC, and breach notice on time.

## 2. Scope
All security incidents affecting any group IT or OT system or data, including incidents at integrators, vendors, and cloud providers that affect group systems.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group SOC director | Runs detection and incident handling 24x7; incident commander for cyber incidents in shared services |
| Plant manager (or shift superintendent until the plant manager arrives) | Incident commander for any process emergency; decides on shutdown and safe state |
| Terminal T1 Terminal Manager with the CySO and FSO | Terminal incident command and Coast Guard reporting |
| Hazmat Transport dispatch director | En route incidents and DOT incident reports |
| Specialty Chemicals EHS director | Release notices and RMP incident investigation |
| Group General Counsel | Owns the notification matrix; approves non-emergency external notices |
| Disclosure committee | Decides materiality for Form 8-K Item 1.05 |
| Group CISO | Declares Severity 1; briefs the board risk committee |

## 4. Policy statements
4.1 Every workforce member must report a suspected incident, or any process behavior they cannot explain (setpoints, alarm limits, or recipes changing without a known cause), to the SOC or the control room immediately. (IR-6; RS.MA-02)

4.2 The SOC must handle incidents using one group severity scale and the group playbooks, including the OT annex and the P08 runbook. Division severity scales are not permitted. **Severity 1** includes any confirmed unauthorized change to OT, ransomware on any system that produces shipping papers, and any incident touching more than one division. (IR-4; IR-8; RS.MA-01)

4.3 **Safe state first.** In any incident touching OT, the plant or terminal incident commander decides first how to keep the process safe, using field instruments and the SIS rather than possibly manipulated HMI values. Cyber containment steps that could upset a process (for example powering off controllers) need the incident commander's approval. (IR-4; CP-12)

4.4 **Release notices never wait for the cyber investigation.** A release at or above a reportable quantity is reported to the National Response Center immediately and to the LEPC and SERC under EPCRA, by the shift superintendent or EHS, using the printed call list and phones that do not depend on the business network. (IR-6; RS.CO-02; 40 CFR 302.6; 40 CFR 355.43)

4.5 The Group General Counsel must keep the multi-regulator notification matrix (P08), review it every quarter, and name an owner for every row. Coast Guard reports for Terminal T1 (33 CFR 6.16-1, immediately) and DOT telephone reports (49 CFR 171.15, within 12 hours) are made by the facility or carrier owner and confirmed to counsel afterward. Other external notices are approved by counsel first. (IR-6; IR-8; RS.CO-02)

4.6 **SEC materiality.** Severity 1 incidents must be escalated to the disclosure committee within 24 hours of declaration. The committee decides materiality without unreasonable delay, considering OT and safety consequences (release, plant or terminal outage, water utility supply) as well as data and cost. If material, the Form 8-K Item 1.05 filing is made within 4 business days after the determination. (IR-6; RS.CO-03)

4.7 **Ransom payments** require board risk committee approval, counsel, the cyber insurer, and an OFAC sanctions check before any payment. Control systems are restored from verified copies, never by decrypting them. (IR-4)

4.8 **Evidence.** DCS event journals, SIS logs, gateway recordings, and firewall logs must be exported and placed on legal hold before they roll over. Chain of custody applies. (IR-4; AU-9; RS.AN-03)

4.9 **Exercises.** The group runs at least one cross-division exercise each year that includes the notification matrix and a materiality decision. Where possible it is combined with the RMP tabletop and notification exercises (40 CFR 68.96) and the Terminal T1 annual cyber exercise (33 CFR 101.635(c)). Terminal T1 also runs cyber drills at least twice each calendar year (101.635(b)). (IR-3; CP-4; ID.IM-02)

4.10 **Restore safely.** Control system configurations, SIS programs, and recipes are restored only from verified offline copies taken before the first sign of intrusion. A plant or terminal restarts only after a pre-startup safety review confirms setpoints, alarm limits, interlocks, and recipes against the process safety information, with an MOC record (40 CFR 68.77; 68.75). (CP-9; CP-10; RC.RP-03)

4.11 **Investigation and lessons learned.** Any cyber incident that changed, or could have changed, an RMP-covered process is also investigated under 40 CFR 68.81 (start within 48 hours). A lessons-learned review is completed within 14 days of recovery and documented within 30 days, and the risk registers, POA&M, and this policy are updated. (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment (IR-3, IR-4, IR-6, IR-8, CP-4) and exercise reports.

## 6. Exceptions
Exceptions follow POL-01 section 4.10. No exception may delay a release notice or any other legal notice deadline.

## 7. Related documents
P08 runbook and notification matrix; group OT annex; RMP emergency response plans; Terminal T1 Facility Security Plan; hazmat security plans; OFAC Updated Advisory on Potential Sanctions Risks for Facilitating Ransomware Payments (2021-09-21).
