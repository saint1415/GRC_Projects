# Incident Response Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all subsidiaries |
| Policy ID | POL-03 |
| Owner | Group CISO, with the Group General Counsel for notifications |
| Approved by | Board risk committee |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), after every Severity 1 incident, and after each cross-division exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-7, IR-8, CP-2 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.MA-04, RS.AN-03, RS.AN-08, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| Regulatory drivers | N55-R02 (Form 8-K Item 1.05); N52-R07 (Model #668 sec. 4H, 5, 6); N62-R01 (164.308(a)(6)-(7)); N62-R03 (164.400-164.414); state breach laws (Fla. Stat. 501.171 worked example) |
| Division supplements | Insurance: commissioner and producer of record notices. Health Care Services: clinical downtime and HIPAA breach decisions. Group health plan: plan breach decisions |

## 1. Purpose
Make sure the group detects, contains, and recovers from incidents consistently across divisions, and that each regulated entity (the public company, the insurers, the covered entity, and the group health plan) meets its own notice duties on time.

## 2. Scope
All security incidents affecting any group system or data, including incidents at vendors, at the holding company's shared services, and at cloud providers that affect group data.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group SOC director | Runs detection and incident handling 24x7; incident commander for Severity 1 and 2 incidents in shared services |
| Group CISO | Declares Severity 1; briefs the board risk committee |
| Group General Counsel | Owns the notification matrix; approves every external notice |
| Insurance chief compliance officer | Commissioner and producer of record notices for the insurers |
| Health Care Services HIPAA Privacy Officer | The covered entity's breach determination and notices |
| Group benefits director (plan privacy official) | The group health plan's breach determination and notices |
| Disclosure committee | Decides materiality for Form 8-K Item 1.05 |
| Division incident liaisons | Bring division facts, operational and patient-safety impact, and regulator contacts |

## 4. Policy statements
4.1 Every workforce member must report a suspected incident to the group SOC within 1 hour of noticing it. (IR-6; RS.MA-02; 164.308(a)(6)(ii))

4.2 The group SOC must handle incidents using one group severity scale and the group playbooks, including the P08 runbook. Division scales are not permitted. (IR-4; IR-8; RS.MA-01)

4.3 **Clocks start from the group's knowledge.** Because the group SOC is part of the holding company, the incident log must record the date the SOC knew of an incident as the discovery or determination date for every affected entity, unless counsel documents a later date with reasons. This applies to HIPAA discovery (164.404(a)(2) for covered entities; 164.410(a)(2) for business associates), the insurers' 72-hour clock for events at a Third-Party Service Provider (Model #668 sec. 6D(2)), and state breach determinations. (IR-5; RS.AN-03)

4.4 Each regulated entity's responsible official must document its own breach or notice determination: the four-factor assessment for Health Care Services and the group health plan (164.402), and the commissioner notice criteria for the insurers (Model #668 sec. 6A). The holding company must notify Health Care Services and the group health plan under their agreements and no later than 60 calendar days after discovery (164.410). (IR-6; RS.CO-02)

4.5 The Group General Counsel must maintain the multi-regulator notification matrix (P08), including commissioner contacts in each state that enacted Model #668 where the insurers are licensed, producer of record notices, and the group health plan, and review it every quarter. Every external notice must be approved by counsel. (IR-6; IR-8; RS.CO-02)

4.6 **Affected people by entity and state.** For every incident involving personal information, the SOC and data owners must produce counts of affected individuals by entity and by state of residence within 5 days, because commissioner, attorney general, HHS, and media notices depend on them. (IR-4; RS.AN-08)

4.7 **SEC materiality.** Severity 1 incidents must be escalated to the disclosure committee within 24 hours of declaration. The committee must decide materiality without unreasonable delay. If material, the Form 8-K Item 1.05 filing must be made within 4 business days after the determination. (IR-6; RS.MA-04)

4.8 **Ransom payments** require board risk committee approval, counsel, the cyber insurer, and an OFAC sanctions check before any payment. (IR-4)

4.9 The group must run at least one cross-division exercise each year that includes the notification matrix and a materiality decision. (IR-3; ID.IM-02)

4.10 Evidence must be preserved with chain of custody, and relevant logs placed on legal hold. Cybersecurity event records must be kept at least 5 years. (IR-4; IR-5; RS.AN-06)

4.11 A lessons-learned review must be completed within 30 days of recovery, and the risk registers, POA&M, and this policy updated. (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment (IR-3, IR-4, IR-6, IR-8) and exercise reports.

## 6. Exceptions
Exceptions follow POL-01 section 4.12. No exception may extend a legal notice deadline.

## 7. Related documents
P08 runbook and notification matrix; POL-01; `division-supplements.md`; BIA recovery priorities (P05).
