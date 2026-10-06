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
| Regulatory anchors | State breach laws (Fla. Stat. 501.171(3)-(6) worked example); E-Verify MOU Art. II.A.16; HIPAA 164.308(a)(6) and 164.400-414; Form 8-K Item 1.05; client contracts and BAAs |
| Division supplements | Staffing: pay disruption communications to associates; MSP client notices. Consulting: client notices under BAAs; federal contracting officer contacts. Home Health: patient-safety escalation; HIPAA breach decisions; emergency preparedness link |

## 1. Purpose
Make sure the group detects, contains, and recovers from incidents consistently across divisions, and that every employing entity, business associate, covered entity, and the public company meets its own notice duties on time.

## 2. Scope
All security incidents affecting any group system or data, including incidents at vendors, subcontractors, cloud providers, and client systems that involve group workforce accounts.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group SOC director | Runs detection and incident handling 24x7; incident commander for Severity 1 and 2 incidents in shared services |
| Group CISO | Declares Severity 1; briefs the board risk committee |
| Group General Counsel | Owns the notification matrix; approves every external notice |
| Staffing Vice President, Employment Compliance | Makes the E-Verify breach notice to DHS for each employing entity |
| Home Health HIPAA Privacy Officer | Makes Home Health's breach determination and notices |
| Consulting HIPAA compliance officer | Makes Consulting's business associate notices to clients |
| Disclosure committee | Decides materiality for Form 8-K Item 1.05 |
| Division incident liaisons | Bring division facts, client and patient impact, and division contacts |

## 4. Policy statements
4.1 Every workforce member must report a suspected incident to the group SOC within 1 hour of noticing it. (IR-6; RS.MA-02; 164.308(a)(6)(ii))

4.2 The group SOC must handle incidents using one group severity scale and the group playbooks, including the P08 runbook. Division scales are not permitted. **Severity 1:** confirmed exfiltration or encryption in a shared service, data of more than one division involved, or a payroll that may not run on time. (IR-4; IR-8; RS.MA-01)

4.3 The incident log must record the date each entity discovered or determined the incident, as each law defines it: for HIPAA, the first day known or that should reasonably have been known to any workforce member (covered entity, 164.404(a)(2)) or employee or agent (business associate, 164.410(a)(2)); for state laws, the date of determination of the breach or reason to believe one occurred (Fla. Stat. 501.171(3)-(4) worked example). For incidents in corporate shared services, the SOC's date is used for every division unless counsel documents otherwise. (IR-5; RS.AN-03)

4.4 **E-Verify.** Any suspected or confirmed breach of personal information from E-Verify, or of the means of access to it, must be reported to DHS immediately as the MOU requires (Art. II.A.16), by each affected employing entity. (IR-6; RS.CO-02)

4.5 Home Health's HIPAA Privacy Officer must document its own four-factor breach risk assessment (164.402) and decide its notices. Consulting must notify each affected client as its BAA requires and no later than 60 calendar days after discovery (164.410). Corporate must notify Home Health the same way for Home Health data it holds. (IR-6; RS.CO-02)

4.6 The Group General Counsel must maintain the multi-regulator notification matrix (P08), including the state law table, client contract terms, and BAA terms, and review it every quarter. Every external notice must be approved by counsel before it is sent. (IR-6; IR-8; RS.CO-02)

4.7 **SEC materiality.** Severity 1 incidents must be escalated to the disclosure committee within 24 hours of declaration. The committee must decide materiality without unreasonable delay. If material, the Form 8-K Item 1.05 filing must be made within 4 business days after the determination. (IR-6; RS.CO-03)

4.8 **Ransom payments** require board risk committee approval, counsel, the cyber insurer, and an OFAC sanctions check before any payment. (IR-4)

4.9 **Workers come first in a pay incident.** If a payroll may be late or diverted, the Group payroll director must decide by Wednesday 18:00 whether to run the repeat-payroll procedure, and Staffing must tell associates by text and branch scripts what will happen to their pay. (IR-4; RC.CO-03)

4.10 The group must run at least one cross-division exercise each year that includes the notification matrix, the E-Verify notice, and a materiality decision. (IR-3; ID.IM-02)

4.11 Evidence must be preserved with chain of custody. Logs relevant to an incident must be placed on legal hold. (IR-4; RS.AN-03)

4.12 A lessons-learned review must be completed within 30 days of recovery, and the risk registers, POA&M, and this policy updated. (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment (IR-3, IR-4, IR-6, IR-8) and exercise reports.

## 6. Exceptions
Exceptions follow POL-01 section 4.11. No exception may extend a legal notice deadline.

## 7. Related documents
P08 runbook and notification matrix; POL-01; `division-supplements.md`; BIA recovery priorities (P05).
