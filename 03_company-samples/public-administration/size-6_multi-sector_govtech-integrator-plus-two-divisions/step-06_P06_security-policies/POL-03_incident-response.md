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
| Agency and federal drivers | CJISSECPOL v6.1 IR-6 (1 hour); Pub. 1075 sec. 1.8 (24 hours, through the agencies); DFARS 252.204-7012(c), (e) (72 hours; 90-day preservation); 45 CFR 164.410; state third-party agent and agency reporting laws (Florida worked example: Fla. Stat. 501.171(6)(a); 282.318; 282.3185; 282.3186); Form 8-K Item 1.05; OFAC advisory (2021-09-21) |
| Division supplements | GovTech: agency fact sheets and CSA, LASO, and disclosure officer contacts. IT Consulting: DoD reports and medium assurance certificates. Software: RMS agency notices, FedRAMP and GovRAMP incident communications |

## 1. Purpose
Make sure the group detects, contains, and recovers from incidents the same way in every division, and that every agency, federal customer, customer, and regulator receives what it needs in time to meet its own deadlines.

## 2. Scope
All security incidents affecting any group system or data, including incidents at service providers, subcontractors, and cloud providers, and incidents in agency-owned systems that group staff use.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group SOC director | Runs detection and incident handling 24x7; incident commander for Severity 1 and 2 incidents in shared services |
| Group CISO | Declares Severity 1; briefs the board risk committee |
| Group General Counsel | Owns the group notification matrix; approves every external notice |
| Group public sector compliance director | Runs the agency notice desk (BP-G05): CJIS, IRS, and state agency contacts |
| Division incident liaisons | Bring division facts, agency and customer contacts, and operational impact |
| IT Consulting federal contracts compliance officer | DoD reports through DIBNet |
| Disclosure committee | Decides materiality for Form 8-K Item 1.05 |

## 4. Policy statements
4.1 Every workforce member must report a suspected incident to the group SOC immediately and no more than 1 hour after noticing it. (IR-6; RS.MA-02; CJISSECPOL v6.1 IR-6)

4.2 The group SOC must handle incidents using one group severity scale and the group playbooks, including the P08 runbook. Division escalation steps are annexes to the group procedure, not separate procedures. (IR-4; IR-8; RS.MA-01)

4.3 Incident records, tickets, and email must not contain CJI, FTI, CUI, or PHI. Use record counts and identifiers only. (IR-5; RS.AN-03)

4.4 **Agency and customer notice.** When an incident may involve an agency's or customer's data, the notice desk must tell the agency's designated contact **within 1 hour of discovery**, without waiting for the investigation, and then send written facts in time for the agency's own deadlines (for example, 24 hours for FTI reporting to TIGTA and the IRS, and 12 hours for Florida agency ransomware reports). Business associate, DFARS, FedRAMP, GovRAMP, and contract clocks in the matrix must also be met. (IR-6; RS.CO-02)

4.5 **The group's own legal clocks.** Third-party agent notices under state law (Florida: no later than 10 days after determination, Fla. Stat. 501.171(6)(a)), DoD reports within 72 hours of discovery (DFARS 252.204-7012(c)), and business associate notices to covered entities (45 CFR 164.410 and the BAA) must be tracked from the recorded discovery or determination time. (IR-6; RS.CO-02)

4.6 The Group General Counsel must maintain the group notification matrix (P08), with every agency, CSA, BAA, DoD, FedRAMP, GovRAMP, and state clock, check contacts every quarter, and approve every external notice. (IR-6; IR-8; RS.CO-02)

4.7 **SEC materiality.** Severity 1 incidents must be escalated to the disclosure committee within 24 hours of declaration. The committee must decide materiality without unreasonable delay. If material, the Form 8-K Item 1.05 filing must be made within 4 business days after the determination. (IR-6; RS.CO-03)

4.8 **Ransom.** No ransom may be paid over agency data without each affected agency's agreement. Florida state agencies, counties, and municipalities may not pay or otherwise comply with a ransom demand (Fla. Stat. 282.3186), and the group must not pay in a way any agency customer objects to. Any group payment requires board risk committee approval, counsel, the cyber insurer, and an OFAC sanctions check. (IR-4)

4.9 Evidence must be preserved with chain of custody. For DoD-related incidents, images and monitoring data must be kept at least 90 days from the report (DFARS 252.204-7012(e)). (IR-4; RS.AN-03)

4.10 The group must run at least one cross-division exercise each year that includes agency security contacts, the notification matrix, and a materiality decision. (IR-3; ID.IM-02)

4.11 A lessons-learned review must be completed within 30 days of recovery; staff involved in an incident must complete refresher training within 30 days (CJISSECPOL v6.1 AT-2); and the risk registers, POA&M, and this policy must be updated. (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.8. Compliance is checked through the P07 assessment (IR-3, IR-4, IR-6, IR-8) and exercise reports.

## 6. Exceptions
Exceptions follow POL-01 section 4.11. No exception may extend a legal or contract notice deadline.

## 7. Related documents
P08 runbook and notification matrix; POL-01; `division-supplements.md`; BIA recovery priorities (P05).
