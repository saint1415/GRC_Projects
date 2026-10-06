# Incident Response Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-03 |
| Owner | Group CISO, with the Group General Counsel for notifications |
| Approved by | Board risk committee, 2026-09-15 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), after every Severity 1 incident, and after each cross-division exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8, CP-2, AU-11 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| Regulatory drivers | CISA CPG 2.0 goals 1.C, 4.B, 5.A, 5.B, 6.A (voluntary, adopted); Form 8-K Item 1.05; state breach laws; DFARS 252.204-7012(c)-(e); PCI DSS v4.0.1 Req. 12.10; lease and property management agreement notice clauses |
| Division supplements | Commercial Property: tenant and owner notices; building safety escalation. Construction: DoD reporting and CUI incidents. Hotels: guest safety, card compromise, acquirer notice |

## 1. Purpose
Make sure the group detects, contains, and recovers from incidents consistently across divisions, keeps people safe in buildings and hotels during an OT incident, and meets every notice duty on time.

## 2. Scope
All security incidents affecting any group system, building system, or data, including incidents at suppliers (internal and external) and cloud providers that affect group systems or data.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group SOC director | Runs detection and incident handling 24x7; incident commander for Severity 1 and 2 incidents in shared services |
| Group building technology director | Building operations lead in any OT incident; decides with chief engineers when to move sites to manual operation |
| Group CISO | Declares Severity 1; briefs the board risk committee |
| Group General Counsel | Owns the notification matrix; approves every external notice |
| Construction director of federal contracts compliance | Makes DoD reports under DFARS 252.204-7012 |
| Hotels payment security lead | Card compromise response and acquirer notice |
| Disclosure committee | Decides materiality for Form 8-K Item 1.05 |
| Division incident liaisons | Bring division facts, safety and operational impact, and division contacts |

## 4. Policy statements
4.1 Every workforce member, and every engineer, RBOC operator, and BTI technician who sees a building system behave unexpectedly, must report a suspected incident to the group SOC within 1 hour of noticing it. (IR-6; RS.MA-02)

4.2 The group SOC must handle incidents using one group severity scale and the group playbooks, including the P08 runbook. **Safety first in OT incidents:** chief engineers and hotel engineers may move a site to manual operation at any time to keep people safe, and no response action may disable life-safety systems. (IR-4; IR-8; RS.MA-01)

4.3 The incident log must record, for each notice duty, the date and time its clock starts: discovery, determination of a breach, or determination of materiality, as each law or contract defines it. (IR-5; RS.AN-03)

4.4 The Group General Counsel must maintain the multi-regulator notification matrix (P08), including state breach laws, lease and property management agreement clauses, DoD reporting, the acquirers, and SEC disclosure, and review it every quarter. Every external notice must be approved by counsel before it is sent. (IR-6; IR-8; RS.CO-02)

4.5 **SEC materiality.** Severity 1 incidents must be escalated to the disclosure committee within 24 hours of declaration. The committee must decide materiality without unreasonable delay. If material, the Form 8-K Item 1.05 filing must be made within 4 business days after the determination. (IR-6; RS.CO-03)

4.6 **Suppliers in incidents.** Internal suppliers (POL-01 4.8) must report incidents affecting group systems to the SOC within 24 hours and must join the incident team on request. External suppliers report under their security addendum. (IR-6; SA-9)

4.7 **Ransom payments** require board risk committee approval, counsel, the cyber insurer, and an OFAC sanctions check before any payment. (IR-4)

4.8 The group must run at least one cross-division exercise each year that includes the notification matrix and a materiality decision, and each region must run an OT manual-operation drill each year. (IR-3; ID.IM-02)

4.9 Evidence must be preserved with chain of custody, and relevant logs placed on legal hold. For incidents involving CUI, images and monitoring data must be kept for at least 90 days from the DoD report (DFARS 252.204-7012(e)). (IR-4; AU-11; RS.AN-03)

4.10 A lessons-learned review must be completed within 30 days of recovery, and the risk registers, POA&M, and this policy updated. (IR-4; ID.IM-02)

4.11 **Suspected card compromise** must be reported to the Hotels payment security lead or the Commercial Property controller immediately, and the acquirer notified as the merchant agreement requires. (IR-6; RS.CO-02)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment (IR-4, IR-6, IR-8), exercise reports, and drill records.

## 6. Exceptions
Exceptions follow POL-01 section 4.11. No exception may extend a legal or contractual notice deadline.

## 7. Related documents
P08 runbook and notification matrix; POL-01; `division-supplements.md`; BIA recovery priorities (P05); BAACS contingency plan.
