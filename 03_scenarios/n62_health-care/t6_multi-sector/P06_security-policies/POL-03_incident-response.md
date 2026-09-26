# Incident Response Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-03 |
| Owner | Group CISO, with the Group General Counsel for notifications |
| Approved by | Board risk committee |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), after every Severity 1 incident, and after each cross-division exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8, CP-2 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| HIPAA and other | 164.308(a)(6), (a)(7); Breach Notification Rule 164.400-414; Form 8-K Item 1.05; state breach and insurance notice laws |
| Division supplements | Care Delivery: clinical downtime and patient-safety escalation; notices to 38 white-label practices. Health Plan: state insurance regulator notices. SaaS: customer notices per BAA |

## 1. Purpose
Make sure the group detects, contains, and recovers from incidents consistently across divisions, and that every covered entity, business associate, and the public company meets its own notice duties on time.

## 2. Scope
All security incidents affecting any group system or data, including incidents at business associates, subcontractors, and cloud providers that affect group data.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group SOC director | Runs detection and incident handling 24x7; is incident commander for Severity 1 and 2 incidents in shared services |
| Group CISO | Declares Severity 1; briefs the board risk committee |
| Group General Counsel | Owns the notification matrix; approves every external notice |
| Care Delivery and Health Plan Privacy Officers | Each makes its own covered entity's breach determination and notices |
| SaaS security and compliance lead | Makes the SaaS's business associate notices to customers |
| Disclosure committee | Decides materiality for Form 8-K Item 1.05 |
| Division incident liaisons | Bring division facts, clinical and operational impact, and division regulator contacts |

## 4. Policy statements
4.1 Every workforce member must report a suspected incident to the group SOC within 1 hour of noticing it. (IR-6; RS.MA-02; 164.308(a)(6)(ii))

4.2 The group SOC must handle incidents using one group severity scale and the group playbooks, including the P08 runbook. Division scales are not permitted. (IR-4; IR-8; RS.MA-01)

4.3 The incident log must record the date each entity discovered a breach: the first day it was known, or by reasonable diligence would have been known, to any workforce member (covered entity, 164.404(a)(2)) or any employee or agent (business associate, 164.410(a)(2)). (IR-5; RS.AN-03)

4.4 Each covered entity's Privacy Officer must document its own four-factor breach risk assessment (164.402) and decide its own notices. A business associate division must notify each affected customer as its BAA requires and no later than 60 calendar days after discovery (164.410), and corporate must notify each affected covered-entity division the same way. (IR-6; RS.CO-02)

4.5 The Group General Counsel must maintain the multi-regulator notification matrix (P08) and review it every quarter. Every external notice must be approved by counsel before it is sent. (IR-6; IR-8; RS.CO-02)

4.6 **SEC materiality.** Severity 1 incidents must be escalated to the disclosure committee within 24 hours of declaration. The committee must decide materiality without unreasonable delay. If material, the Form 8-K Item 1.05 filing must be made within 4 business days after the determination. (IR-6; RS.CO-03)

4.7 **Ransom payments** require board risk committee approval, counsel, the cyber insurer, and an OFAC sanctions check before any payment. (IR-4)

4.8 The group must run at least one cross-division exercise each year that includes the notification matrix and a materiality decision. (IR-3; ID.IM-02)

4.9 Evidence must be preserved with chain of custody. Logs relevant to an incident must be placed on legal hold. (IR-4; RS.AN-03)

4.10 A lessons-learned review must be completed within 30 days of recovery, and the risk registers, POA&M, and this policy updated. (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment (IR-3, IR-4, IR-6, IR-8) and exercise reports.

## 6. Exceptions
Exceptions follow POL-01 section 4.10. No exception may extend a legal notice deadline.

## 7. Related documents
P08 runbook and notification matrix; POL-01; `division-supplements.md`; BIA recovery priorities (P05).
