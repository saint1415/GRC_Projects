# Incident Response Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-03 |
| Owner | Group CISO, with the Group General Counsel for notifications |
| Approved by | Board risk committee, 2026-09-22 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), after every Severity 1 incident, and after each cross-division exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-7, IR-8, CP-2, CP-10 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.MA-03, RS.AN-03, RS.CO-02, RS.CO-03, RS.MI-01, RC.RP-01, ID.IM-02 |
| Regulatory drivers | C-ENERGY-R02 (SD 01G II.C); C-ENERGY-R03 (SD 02G III.D.4, III.F); PHMSA 191.5 and 192.615; FERC 260.9; SSI 1520.9(c); N55-R02 (Form 8-K Item 1.05); state breach laws |
| Division supplements | Gas Transmission: operate-or-shut-down decision and TSA Cybersecurity Incident Response Plan. Gathering and Production: field shut-in and Part 191 notices. Integrity Services: client notice register and SSI disclosure reports |

## 1. Purpose
Make sure the group detects, contains, and recovers from incidents consistently across divisions, keeps pipelines and field operations safe while it does, and meets every division's notice duties on time.

## 2. Scope
All cybersecurity incidents affecting any group IT or OT system or data, including incidents at service providers that affect group systems or data, and incidents that affect SSI or client data the group holds.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group SOC director | Runs detection and incident handling 24x7; incident commander for Severity 1 and 2 incidents in shared services |
| Group CISO | Declares Severity 1; briefs the board risk committee |
| Group OT Security Director | Leads OT analysis; advises on OT integrity |
| Vice President of Gas Control | Recommends whether to operate, operate manually, or shut down a segment (Gas Transmission) |
| Gas Transmission president | Decides a precautionary shutdown of a segment |
| Controllers and field supervisors | Act at once under the emergency plan when safety requires it (192.615) |
| Director of Pipeline Cybersecurity | TSA Cybersecurity Coordinator; files the CISA report under SD 01G |
| Group General Counsel | Owns the notification matrix; approves every external notice |
| Disclosure committee | Decides materiality for Form 8-K Item 1.05 |
| Division incident liaisons | Bring division facts, operational impact, and regulator contacts |

## 4. Policy statements
4.1 Every workforce member must report a suspected incident to the group SOC within 1 hour of noticing it. A controller who sees anything abnormal on SCADA must follow the control room and emergency procedures first, then report. (IR-6; RS.MA-02)

4.2 The group SOC must handle incidents using one group severity scale and the group playbooks, including the P08 runbook. Severity 1 includes any incident in which OT is affected or cannot be shown to be unaffected. Division scales are not permitted. (IR-4; IR-8; RS.MA-01; RS.MA-03)

4.3 **Safety first.** Nothing in this policy delays an action that a controller or field supervisor must take under the emergency plan, including emergency shutdown, valve shut-off, or pressure reduction. (CP-2; 192.615(a)(6), (a)(11))

4.4 **IT/OT isolation.** The Director of Gas Control (Gas Transmission) and the Vice President of Field Operations Technology (Gathering and Production) each have authority to close all connections between their OT and corporate IT, including the OT remote access gateway, without waiting for proof that OT is affected. (SC-7; RS.MI-01; SD 02G III.D.4, III.F.1.d)

4.5 **Precautionary shutdown.** A decision to shut down a pipeline segment because OT cannot be trusted or seen, or because safe manual operation cannot be staffed, is made by the division president on the recommendation of the Vice President of Gas Control, using the criteria in the P08 runbook, and recorded with its reasons. (IR-4; CP-2)

4.6 **Notifications.** The Group General Counsel must maintain the multi-regulator notification matrix (P08) and review it every quarter. Every external notice must be approved by counsel. The group reporting procedure must name an owner for each clock on every shift, including CISA under SD 01G (no later than 72 hours after identification, with a 24-hour internal target), PHMSA (one hour after confirmed discovery of an incident), FERC service interruption reports, SSI disclosure reports to TSA, client notices, and state breach notices. (IR-6; RS.CO-02; SD 01G II.C.3; 191.5; 260.9; 1520.9(c))

4.7 **SEC materiality.** Severity 1 incidents must be escalated to the disclosure committee within 24 hours of declaration. The committee must decide materiality without unreasonable delay. If material, the Form 8-K Item 1.05 filing must be made within 4 business days after the determination. (IR-6; RS.CO-03)

4.8 **Ransom payments** require board risk committee approval, counsel, the cyber insurer, and an OFAC sanctions check before any payment. (IR-4)

4.9 **Exercises.** Each TSA-designated division must exercise its Cybersecurity Incident Response Plan at least annually, testing at least two of its objectives, with the named positions taking part. The group must also run at least one cross-division exercise each year that includes the notification matrix, a shutdown decision, and a materiality decision. (IR-3; ID.IM-02; SD 02G III.F.1.e)

4.10 Evidence must be preserved with chain of custody, including forensic memory images before devices are powered off or moved where practicable. Logs relevant to an incident must be placed on legal hold. (IR-4; RS.AN-03; SD 02G III.F.1.b)

4.11 Restores must use backups verified free of known malicious code. (CP-10; RC.RP-03; SD 02G III.F.1.c)

4.12 A lessons-learned review must be completed within 30 days of recovery, and the risk registers, POA&M, TSA plans (with an amendment request where required), and this policy updated. (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.12. Compliance is checked through the P07 assessment (IR-3, IR-4, IR-6, IR-8), exercise reports, and the TSA Cybersecurity Assessment Plan.

## 6. Exceptions
Exceptions follow POL-01 section 4.11. No exception may extend a legal or contractual notice deadline.

## 7. Related documents
P08 runbook and notification matrix; POL-01; `division-supplements.md`; BIA recovery priorities (P05); emergency plans (192.615); TSA Cybersecurity Incident Response Plan (SSI).
