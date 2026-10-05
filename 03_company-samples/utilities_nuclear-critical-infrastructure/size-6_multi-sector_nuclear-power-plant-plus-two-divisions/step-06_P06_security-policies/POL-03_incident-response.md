# Incident Response Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (all divisions and corporate shared services) |
| Policy ID | POL-03 |
| Owner | Group CISO (notifications: Group General Counsel) |
| Approved by | Board risk committee |
| Effective date | 2026-10-01 |
| Review cycle | Annually, after every Severity 1 incident, and after a change in any notification rule |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-7, IR-8 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| Regulatory drivers | C-NUCLEAR-R03 (73.77); C-NUCLEAR-R04 (CIP-008-6); C-NUCLEAR-S05 (50.72); C-NUCLEAR-S06 (37.57, 37.81); C-NUCLEAR-S10 (Form 8-K Item 1.05); C-NUCLEAR-S11 |

## 1. Purpose
Detect, contain, and recover from incidents quickly, and make every required notice on time, across three divisions and many regulators.

## 2. Scope
All security incidents affecting group business systems or information, and any business-side event that could affect a CDA, an SGI program, the NERC CIP environment, or a Part 37 security system. Each station CSP's incident response measures (73.54(e)(2)) govern response on CDAs; this policy governs everything else and the handoffs.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group SOC director | Incident commander for business-system incidents |
| Station CST lead | Incident commander for anything inside a CSP boundary; decides with the fleet security director whether a 73.77 notice is needed |
| Fleet security director | Decides and makes 73.77 notices; the only route for external reports about station systems |
| CIP Senior Manager | Decides CIP-008-6 reportability for the fleet operations center |
| Radiation Safety Officer (Florida facility) | Decides Part 37 reportability |
| Group General Counsel | Runs the notification matrix; approves every external notice except regulator notices that must be made within hours by the licensee |
| Disclosure committee | SEC materiality |

## 4. Policy statements
4.1 Every suspected incident must be reported to the group SOC at once. Station staff also report to the station shift manager. (IR-6; RS.MA-01)

4.2 One severity scale applies across the group. Severity 1 includes any incident that touches a CSP-adjacent asset (kiosk update server, plant data replicas, one-way device receive side), SGI, access authorization information, the fleet operations center, or the Florida vault security systems. (IR-4; RS.MA-03)

4.3 **The SOC must bring in the station CST within 30 minutes** of seeing activity on a CSP-adjacent asset or activity aimed at CDA information, so the station can decide 73.77 clocks (1 hour, 4 hours, 8 hours from discovery). (IR-4; IR-6; 73.77(a))

4.4 **No one may report an event about station systems to the FBI, CISA, or any other agency except through the fleet security director**, because a notice to another agency about an event related to the cyber security program for 73.54 systems starts a 4-hour NRC clock (73.77(a)(2)(iii)). The same rule applies to the Florida vault (Part 37 reports to the Bureau of Radiation Control) and the fleet operations center (CIP-008-6 R4). (IR-6; RS.CO-02)

4.5 The Group General Counsel must keep a notification matrix covering every regulator and contract clock in the group (P08), review it at least annually, and exercise it across divisions at least annually. (IR-6; IR-8; RS.CO-03)

4.6 The disclosure committee must be convened within 24 hours of declaring a Severity 1 incident and must decide materiality without unreasonable delay. (IR-6; Form 8-K Item 1.05)

4.7 No ransom may be paid without a decision by the board risk committee, legal advice, an OFAC sanctions check, and a report to law enforcement made under 4.4. (IR-4; RS.MA-01)

4.8 Evidence must be preserved before systems are rebuilt. Nothing may be copied out of a CSP-protected network, an SGI system, or the vault security systems for forensics except under that program's procedure. (IR-4; AU-9)

4.9 Incident response plans must be tested at least annually. At least one test each year must be a joint group SOC and station CST exercise that starts on the business network. (IR-3; ID.IM-02)

4.10 Lessons learned must be held within 14 days of recovery and documented within 30 days. Weaknesses in a CSP are entered in the station CAP within 24 hours of discovery (73.77(b)(1)). (IR-4; ID.IM-03)

## 5. Compliance and enforcement
Checked by P07 testing, exercise reports, and Nuclear Oversight reviews of the CSP incident response program.

## 6. Exceptions
None for 4.3, 4.4, and 4.10. Others under POL-01 4.12.

## 7. Related documents
P08 runbook and notification matrix; station CSP incident response procedures; CIP-008-6 plan; Florida facility Part 37 event procedure; POL-01; POL-04.
