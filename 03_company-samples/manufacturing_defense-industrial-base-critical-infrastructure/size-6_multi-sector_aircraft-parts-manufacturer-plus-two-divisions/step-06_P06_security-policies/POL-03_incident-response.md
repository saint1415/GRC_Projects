# Incident Response Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-03 |
| Owner | Group CISO, with the Group General Counsel for notifications |
| Approved by | Board audit and risk committee |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), after every Severity 1 incident, and after each cross-division exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8, IR-9, AU-11, CP-2 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| SP 800-171 and other | 3.6.1 to 3.6.3; DFARS 252.204-7012(c) to (g) and (m)(2)(ii); DFARS 252.239-7010(d) to (h), (k); 32 CFR 117.8; Form 8-K Item 1.05; state breach laws |
| Division supplements | Aircraft Parts: production and product-integrity escalation; prime notices. Engineering Services: FSO reports and customer-site incidents. Defense Software: DoD edition reporting, CSP duties to SYS-D4 tenants, customer notices |

## 1. Purpose
Make sure the group detects, contains, and recovers from incidents consistently across divisions, and that every division meets its own DoD, customer, export, NISPOM, and SEC duties on time, even when one incident touches several divisions.

## 2. Scope
All security incidents affecting any group system or data, including incidents at suppliers, cloud providers, and sister-division services that affect group or customer data, and incidents involving CUI on customer systems or GFE used by group staff.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group SOC director | Runs detection and incident handling 24x7; incident commander for Severity 1 and 2 incidents in shared services |
| Group CISO | Declares Severity 1; briefs the board audit and risk committee |
| Group General Counsel | Owns the notification matrix; approves every external notice except that a DoD report is never delayed for review |
| Division DoD reporters (certificate holders) | File DIBNet reports under their division's contracts |
| Division Empowered Officials | Decide on ITAR and EAR voluntary disclosures |
| Facility security officers | NISPOM reports at the cleared centers |
| Disclosure committee | Decides materiality for Form 8-K Item 1.05 |
| Division incident liaisons | Bring division facts, program and contract data, and customer contacts |

## 4. Policy statements
4.1 Every workforce member must report a suspected incident to the group SOC within 1 hour of noticing it, including incidents on customer systems or GFE that involve group work. (IR-6; RS.MA-02; 3.6.2)

4.2 The group SOC must handle incidents using one group severity scale and the group playbooks, including the P08 runbook. Division scales are not permitted. (IR-4; IR-8; RS.MA-01; 3.6.1)

4.3 The incident log must record the **time of discovery** for each division and each contract affected. Suspected unauthorized access to a system holding CDI starts the clock; proof of exfiltration is not required. (IR-5; RS.AN-03; 252.204-7012(a), (c))

4.4 **DoD reporting.** Each division with affected contracts must report on DIBNet within 72 hours of discovery, using a DoD-approved medium assurance certificate, and update the report as facts develop. Each division must keep at least two certificate holders at different locations. Subcontracts must also receive the DoD incident report number as soon as practicable. (IR-6; RS.CO-02; 252.204-7012(c)(1)(ii), (c)(3), (m)(2)(ii); 252.239-7010(d))

4.5 **Cloud service provider duties.** When a group platform holds a customer's CDI, the providing division must support that customer's reporting and meet the clause duties for reporting, malware, preservation, and forensic access, as its customer contracts and DFARS 252.204-7012(b)(2)(ii)(D) require. (IR-6; RS.CO-02)

4.6 **Evidence.** Images of affected systems and relevant monitoring and packet capture data must be preserved for at least 90 days from the DoD report, and longer if DoD asks. Malicious software must go to DC3 (or as the Contracting Officer instructs for the DoD edition), never to the Contracting Officer. (IR-4; AU-11; RS.AN-03; 252.204-7012(d), (e); 252.239-7010(e), (f))

4.7 **SEC materiality.** Severity 1 incidents must be escalated to the disclosure committee within 24 hours of declaration. The committee must decide materiality without unreasonable delay. If material, the Form 8-K Item 1.05 filing must be made within 4 business days after the determination. (IR-6; RS.CO-03)

4.8 **Export and NISPOM decisions.** For any incident involving export-controlled data, the Empowered Official must record a decision on voluntary disclosure (22 CFR 127.12; 15 CFR 764.5). At cleared centers, facility security officers must make the reports 32 CFR 117.8 requires, including prompt FBI reports of possible espionage with a copy to DCSA. (IR-6; RS.CO-02)

4.9 **Extortion and ransom payments** require board audit and risk committee approval, counsel, the cyber insurer, and an OFAC sanctions check before any payment. A payment never removes a reporting duty. (IR-4)

4.10 The Group General Counsel must maintain the multi-regulator notification matrix (P08) and review it every quarter. The group must run at least one cross-division exercise each year that includes DIBNet reporting by every division and a materiality decision. (IR-3; IR-8; ID.IM-02; 3.6.3)

4.11 **Spillage.** Classified information found on an unclassified system must be handled under the FSO's spillage procedure and, for the DoD edition, with the Contracting Officer. (IR-9; RS.MA-01; 252.239-7010(k))

4.12 A lessons-learned review must be completed within 14 days of containment and documented within 30 days, and the risk registers, POA&M, SSPs, and this policy updated. (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment (IR-3, IR-4, IR-6, IR-8) and exercise reports.

## 6. Exceptions
Exceptions follow POL-01 section 4.12. No exception may extend a contractual or legal reporting deadline.

## 7. Related documents
P08 runbook and notification matrix; POL-01; `division-supplements.md`; BIA recovery priorities (P05).
