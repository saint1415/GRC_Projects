# Incident Response Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-03 |
| Version | v2026.1 |
| Owner | Group CISO, with the Group General Counsel for notifications |
| Approved by | Board risk committee, 2026-09-15 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), after every Severity 1 incident, and after each cross-division exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-6(3), IR-8, CP-2, SR-8 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RS.MI-01, RC.RP-01, ID.IM-02, GV.SC-08 |
| Regulatory and contract drivers | Utility addendum secs. 1 and 2 (CIP-013-2 R1 Parts 1.2.1 and 1.2.2 flow-down); client CIP-013-2 terms (Grid Engineering); N22-R01 CIP-008-6, EOP-004-4, Form DOE-417 (Electric Utility); FAR 52.204-25(d), 52.204-23(c), 52.204-30; SEC Form 8-K Item 1.05; state breach laws (Fla. Stat. 501.171 worked example); OFAC ransomware advisory (2021-09-21); C-CRITICAL-MFG-R01 CIRCIA (proposed; readiness only) |
| Division supplements | Manufacturing: plant safe-state and isolation, PSIRT notices to utilities. Electric Utility: CIP-008-6 plan, EOP-004-4 Operating Plan, DOE-417 desk. Grid Engineering: client notices and commissioning laptop incidents |

## 1. Purpose
Make sure the group detects, contains, and recovers from incidents consistently across divisions, keeps people and the grid safe while it does, and meets every notice duty on time: to utilities and clients, to the Electric Utility's reliability regulators, to federal contracting officers, to affected individuals, and to investors.

## 2. Scope
All security incidents affecting any group system or data, including plant OT, the TMU product and FMS, the Electric Utility's BES Cyber Systems, and incidents at suppliers and cloud providers that affect group systems, data, or products.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group SOC director | Runs detection and incident handling 24x7; incident commander for Severity 1 and 2 incidents in shared services |
| Group CISO | Declares Severity 1; briefs the board risk committee |
| Group General Counsel | Owns the notification matrix; approves external notices except the time-critical reliability reports in 4.5 |
| Group OT security director | Leads OT containment support for plants and the utility |
| Plant managers | Decide to put processes into a safe state and to stop production |
| Chief product security officer | Runs the PSIRT; sends utility addendum notices |
| Grid Engineering contracts director | Sends client notices under client contract terms |
| Electric Utility NERC compliance director | Makes CIP-008-6, EOP-004-4, and DOE-417 determinations and reports |
| Group Chief Privacy Officer | Makes state breach determinations |
| Director of federal contracts; Grid Engineering federal programs manager | Make FAR reports to contracting officers |
| Disclosure committee | Decides materiality for Form 8-K Item 1.05 |

## 4. Policy statements
4.1 Every workforce member must report a suspected incident to the group SOC within 1 hour of noticing it. Plant and control center staff report to their supervisor and the SOC at the same time. (IR-6; RS.MA-02)

4.2 The group SOC must handle incidents with one group severity scale and the group playbooks, including the P08 runbook. Division plans (the Electric Utility's CIP-008-6 plan, the Manufacturing PSIRT procedure) must use the group scale and must say when an incident moves between the group plan and the division plan. (IR-4; IR-8; RS.MA-01)

4.3 The Group General Counsel must maintain the multi-party notification matrix (P08) and review it every quarter. Every notice in the matrix must have a named sender, a backup, a template, and an out-of-band contact list. (IR-6; IR-8; RS.CO-02)

4.4 **Customer and client notices.** The SOC must tell the PSIRT and the Grid Engineering contracts director within 4 hours whenever an incident touches a supplied product, a service, client data, or a commissioning laptop. They must then send each notice within the shortest applicable contract deadline from confirmation (24 or 48 hours under the utility addenda; 24 to 72 hours under client terms) and coordinate the response with each customer. (IR-6; IR-6(3); SR-8; GV.SC-08)

4.5 **Reliability reports.** The Electric Utility's reporting desk must make CIP-008-6 R4, EOP-004-4, and Form DOE-417 reports within their own deadlines (for example, a DOE-417 Emergency Alert within 1 hour) **without waiting** for group legal review. The group SOC must give the desk the facts it needs at once and must treat any activity aimed at a TCC Electronic Access Point as a potential CIP reportable event. (IR-6; RS.CO-02)

4.6 **SEC materiality.** Severity 1 incidents must be escalated to the disclosure committee within 24 hours of declaration. The committee must decide materiality without unreasonable delay. If the incident is material, the Form 8-K Item 1.05 filing must be made within 4 business days after the determination. (IR-6; RS.CO-03)

4.7 **Ransom payments** require board risk committee approval, counsel, the cyber insurer, an OFAC sanctions check before any payment, and a report to law enforcement or CISA. (IR-4)

4.8 **OT containment.** Plant managers may stop production and put processes into a safe state at any time. The SOC may operate the pre-approved IT/OT isolation points (P08) for a plant or for the GEPS integration hub without further approval. Restart must use verified controller programs and plant engineering sign-off. (IR-4; CP-2; RS.MI-01)

4.9 **FAR reports.** Covered telecommunications equipment found during contract performance must be reported to the contracting officer within 1 business day (52.204-25(d)); Kaspersky covered articles and FASCSA covered articles within 3 business days (52.204-23(c); 52.204-30). (IR-6)

4.10 The group must run at least one cross-division exercise each year that includes a plant outage, the notification matrix, the reliability reporting desk, and a materiality decision. (IR-3; ID.IM-02)

4.11 Evidence must be preserved with chain of custody, and logs relevant to an incident placed on legal hold. OT evidence must be collected without disturbing safe operation. (IR-4; RS.AN-03)

4.12 A lessons-learned review must be completed within 30 days of recovery, and the registers, POA&M, and this policy updated. (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment (IR-3, IR-4, IR-6, IR-6(3), IR-8), exercise reports, and the Electric Utility's CIP-008-6 test records.

## 6. Exceptions
Exceptions follow POL-01 section 4.10. No exception may extend a legal, regulatory, or contract notice deadline.

## 7. Related documents
P08 runbook and notification matrix; POL-01; `division-supplements.md`; BIA recovery priorities (P05); Electric Utility CIP-008-6 plan and EOP-004-4 Operating Plan; Manufacturing PSIRT procedure.
