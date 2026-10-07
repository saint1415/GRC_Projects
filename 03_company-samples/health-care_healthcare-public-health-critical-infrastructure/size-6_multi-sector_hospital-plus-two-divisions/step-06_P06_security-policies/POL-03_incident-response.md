# Incident Response Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-03 |
| Owner | Group CISO, with the Group General Counsel for notifications |
| Approved by | Board risk committee, 2026-09-15 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), after every Severity 1 incident, and after each cross-division exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8, CP-2, CP-2(1) |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| HIPAA and other | 164.308(a)(6), (a)(7); Breach Notification Rule 164.400-164.414; 42 CFR 482.15 and 489.24 (emergency preparedness and EMTALA); 16 CFR 314.4(h), (j); FSA breach reporting; NAIC Model #668 sec. 6 where enacted; Form 8-K Item 1.05; state breach laws |
| Division supplements | Hospital System: clinical downtime, hospital incident command, diversion, and notices to 64 practices. Health Plan: state insurance commissioner notices and ASO plan notices. College: FSA and FTC notices |

## 1. Purpose
Make sure the group detects, contains, and recovers from incidents consistently across divisions, keeps patients safe while clinical systems are down, and meets every covered entity's, business associate's, financial institution's, and public company's notice duties on time.

## 2. Scope
All security incidents affecting any group system or data, including incidents at business associates, subcontractors, service providers, cloud providers, and device manufacturers that affect group data or patient care.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group SOC director | Runs detection and incident handling 24x7; incident commander for Severity 1 and 2 incidents in shared services |
| Group CISO | Declares Severity 1; briefs the board risk committee |
| Group General Counsel | Owns the notification matrix; approves every external notice |
| Hospital System and Health Plan Privacy Officers | Each makes its own covered entity's breach determination and notices |
| College IT director (Qualified Individual) with the financial aid director | College notices to Federal Student Aid and the FTC |
| Hospital incident command (each hospital's chief executive or delegate) | Clinical operations, downtime, and diversion decisions with the ED medical lead |
| System emergency management director | Activates the unified emergency plan; coordinates with county EMS and emergency management |
| Disclosure committee | Decides materiality for Form 8-K Item 1.05 |
| Division incident liaisons | Bring division facts and division regulator contacts |

## 4. Policy statements
4.1 Every workforce member must report a suspected incident to the group SOC within 1 hour of noticing it. (IR-6; RS.MA-02; 164.308(a)(6)(ii))

4.2 The group SOC must handle incidents using one group severity scale and the group playbooks, including the P08 runbook. Division scales are not permitted, and the College's 2022 plan is replaced by this policy and the group plan by 2026-12-31. (IR-4; IR-8; RS.MA-01; 16 CFR 314.4(h))

4.3 The incident log must record the discovery date for each entity: for a covered entity, the first day the breach is known, or by reasonable diligence would have been known, to any workforce member (164.404(a)(2)); for a business associate, to any employee or agent (164.410(a)(2)); for the College, the first day a notification event is known to any employee, officer, or other agent other than the person committing it (16 CFR 314.4(j)(2)). (IR-5; RS.AN-03)

4.4 Each covered entity's Privacy Officer must document its own four-factor breach risk assessment (164.402) and decide its own notices. A business associate division must notify each affected covered entity as its BAA requires and no later than 60 calendar days after discovery (164.410); corporate must notify each affected covered-entity division the same way. (IR-6; RS.CO-02)

4.5 The Group General Counsel must maintain the multi-regulator notification matrix (P08), including state attorney general, state insurance commissioner, Federal Student Aid, and FTC Safeguards Rule contacts and clocks, and review it every quarter. Every external notice must be approved by counsel before it is sent. (IR-6; IR-8; RS.CO-02)

4.6 **Patient safety first.** When a Severity 1 or 2 incident affects clinical systems, each affected hospital must start downtime procedures and activate its incident command under the unified emergency plan. Ambulance diversion is decided by hospital incident command with the ED medical lead, using the P08 criteria; every person who comes to the ED must still be screened and stabilized as EMTALA requires (42 CFR 489.24). (CP-2(1); IR-4; RC.RP-01; 482.15(a)(2))

4.7 **SEC materiality.** Severity 1 incidents must be escalated to the disclosure committee within 24 hours of declaration. The committee must decide materiality without unreasonable delay. If material, the Form 8-K Item 1.05 filing must be made within 4 business days after the determination. (IR-6; RS.CO-03)

4.8 **Ransom payments** require board risk committee approval, counsel, the cyber insurer, and an OFAC sanctions check before any payment. (IR-4)

4.9 The group must run at least one cross-division exercise each year that includes clinical downtime, the notification matrix, and a materiality decision. When it uses a clinically relevant scenario, the hospitals record it as their additional annual exercise under 482.15(d)(2)(ii) and file the after-action report in the emergency program records. (IR-3; ID.IM-02)

4.10 Evidence must be preserved with chain of custody. Logs relevant to an incident must be placed on legal hold. (IR-4; RS.AN-03)

4.11 A lessons-learned review must be completed within 30 days of recovery, and the risk registers, the POA&M, the emergency plan, and this policy updated. (IR-4; ID.IM-02; 482.15(d)(2)(iii))

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment (IR-3, IR-4, IR-6, IR-8) and exercise reports.

## 6. Exceptions
Exceptions follow POL-01 section 4.10. No exception may extend a legal notice deadline or an EMTALA duty.

## 7. Related documents
P08 runbook and notification matrix; POL-01; `division-supplements.md`; BIA recovery priorities and MTDs (P05); unified emergency preparedness plan.
