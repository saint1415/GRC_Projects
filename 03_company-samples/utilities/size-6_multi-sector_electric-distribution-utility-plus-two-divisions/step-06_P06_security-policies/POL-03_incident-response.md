# Incident Response Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-03 |
| Owner | Group CISO, with the Group General Counsel for notifications |
| Approved by | Board risk committee |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), after every Severity 1 incident, and after each cross-division exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8, CP-2, CP-10 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RS.MI-01, RC.RP-01, ID.IM-02 |
| Regulatory links | NERC CIP-008-6 (TCC) and CIP-003-9 Attachment 1 Section 4 (low impact); CIP-009-6; EOP-004-4; Form DOE-417; client contract notice terms; FAR 52.204-25(d) and 52.204-23(c); state breach laws; SEC Form 8-K Item 1.05; OFAC ransomware advisory (2021-09-21) |
| Division supplements | Electric Utility: TCC and DCC reporting checklists, operational incident command. Gas Production: field SCADA isolation and local control. Engineering Services: client notice register |

## 1. Purpose
Make sure the group detects, contains, and recovers from incidents consistently across divisions, keeps the grid and field operations safe while it does, and meets every reporting duty on time.

## 2. Scope
All security incidents affecting any group IT or OT system or data, including incidents at vendors, cloud providers, and affiliates that affect group or client data or systems.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group SOC director | Runs detection and incident handling 24x7; technical incident commander for Severity 1 and 2 |
| Control center shift supervisors (TCC, DCC, POC) | Operational incident commander for any incident affecting grid or field operations; decides every isolation step that affects operations |
| Group CISO | Declares Severity 1; briefs the board risk committee |
| Group General Counsel | Owns the notification matrix; approves every external notice except time-critical operational reports |
| Electric Utility NERC compliance director | Determines Reportable Cyber Security Incidents and attempts with the CIP Senior Manager; files CIP-008-6, DOE-417, and EOP-004-4 reports |
| Engineering Services contracts director | Sends client notices under the client notice register |
| Disclosure committee | Decides materiality for Form 8-K Item 1.05 |

## 4. Policy statements
4.1 Every workforce member must report a suspected incident immediately to the group SOC. In an OT environment, the person must also tell the control center shift supervisor. (IR-6; RS.MA-01)

4.2 **One severity scale.** Severity 1: any incident with an effect on grid or field operations, any suspected compromise of an OT environment or of SYS-G4, or any incident affecting more than one division. The SOC must declare severity within 30 minutes of triage. (IR-4; RS.MA-03)

4.3 **Safety first.** No containment step that changes grid or field operations may be taken without the shift supervisor's decision. Crews working under clearances are protected before anything else. (IR-4; CP-2)

4.4 **Record the clock times.** The incident commander must record when an incident occurred, when it was identified, when it was determined to be a Cyber Security Incident, and when it was determined to be Reportable or an attempt to compromise. Each reporting duty runs from a different one of these times. (IR-5; IR-6)

4.5 **Reporting duties** follow the notification matrix (P08):
- Electric Utility: CIP-008-6 R4 notices to the E-ISAC and CISA within 1 hour of determining a Reportable Cyber Security Incident and by the end of the next calendar day for an attempt to compromise; DOE-417 within the form's clocks (1 hour, 6 hours, end of next calendar day, 72 hours); EOP-004-4 event reports; E-ISAC notice for Reportable incidents at low impact assets (CIP-003-9 Attachment 1 Section 4).
- Engineering Services: client notices within each contract's window; FAR 52.204-25(d) reports within 1 business day and FAR 52.204-23(c) reports within 3 business days of identification.
- All divisions: state breach notices for affected individuals in each state where they reside.
(IR-6; RS.CO-02; RS.CO-03)

4.6 **SEC materiality.** The Group General Counsel must convene the disclosure committee within 24 hours of a Severity 1 declaration. Materiality must be decided without unreasonable delay; a Form 8-K Item 1.05 filing is due within 4 business days of a materiality determination. (IR-6; GV.OV-01)

4.7 **Ransom and extortion.** No payment may be made without approval of the board risk committee, counsel, and the insurer, and an OFAC sanctions check. Reporting to law enforcement or CISA must be made in any case. (IR-4; IR-6)

4.8 **Testing.** Each division plan must be tested at least once a year. The Electric Utility's CIP-008-6 plan must be tested at least once every 15 calendar months, its CIP-009-6 recovery plans every 15 calendar months, and its low impact plan at least once every 36 calendar months. A cross-division tabletop including the disclosure committee and client notices must be held every year. (IR-3; ID.IM-02)

4.9 **Evidence.** Preserve logs, images, and records with chain of custody before rebuilding, without delaying recovery of grid or field operations. (IR-4; CIP-009-6 R1 Part 1.5)

4.10 **Lessons learned** within 30 days of closure, with plan updates; for CIP plans, within the time CIP-008-6 R3 and CIP-009-6 R3 set. (IR-4; ID.IM-03)

4.11 Recovery must follow the BIA recovery order (P05), with OT remote access restored only after the attacker's path is closed. (CP-2; CP-10; RC.RP-01)

## 5. Compliance and enforcement
Compliance is checked through exercises, P07, and CIP evidence reviews.

## 6. Exceptions
None for statements 4.3 to 4.6. Others follow POL-01 section 4.10.

## 7. Related documents
P08 runbook and notification matrix; the Electric Utility CIP-008-6 plan, low impact plan, CIP-009-6 recovery plans, and EOP-004-4 Operating Plan; `division-supplements.md`.
