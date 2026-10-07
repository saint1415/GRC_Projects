# Incident Response Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-03 |
| Owner | Group CISO, with the Group General Counsel for notifications |
| Approved by | Board audit and risk committee |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), after every Severity 1 incident, and after each cross-division exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8, CP-2, SR-8 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| Regulatory drivers | N42-R03 (252.204-7012(c)-(g); SP 800-171 R2 3.6.1 to 3.6.3); N42-R05 (52.204-25(d)); DFARS 252.246-7008(b)(3)(ii); N42-R07 (Form 8-K Item 1.05); N44-45-R01 (PCI DSS v4.0.1 Req. 12.10); state breach notification laws |
| Division supplements | IT Distribution: DIBNet reports, prime notices, contracting officer notices. Logistics: product quarantine, 3PL client notices, OT safety. Online Retail: acquirer and card brand notices, consumer notices, marketplace takedowns |

## 1. Purpose
Make sure the group detects, contains, and recovers from cyber and product-integrity incidents consistently across divisions, and that every division and the public company meet their own notice duties on time.

## 2. Scope
All security incidents affecting any group system, data, or product in group custody, including incidents at suppliers, service providers, and cloud providers that affect group data or products.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group SOC director | Runs detection and incident handling 24x7; incident commander for Severity 1 and 2 incidents in shared services |
| Group CISO | Declares Severity 1; briefs the board audit and risk committee |
| Group General Counsel | Owns the notification matrix; approves every external notice |
| Federal Solutions vice president | DIBNet reports, prime and contracting officer notices |
| Group supply chain risk director | Product-integrity decisions: quarantine, release, disposition |
| Online Retail PCI compliance manager | Acquirer and card brand notices |
| Disclosure committee | Decides materiality for Form 8-K Item 1.05 |
| Division incident liaisons | Bring division facts and division contacts |

## 4. Policy statements
4.1 Every workforce member must report a suspected incident, including a suspected tampered, counterfeit, or covered product, to the group SOC within 1 hour of noticing it. (IR-6; RS.MA-02; 3.6.2)

4.2 The group SOC must handle incidents using one group severity scale and the group playbooks, including the P08 runbook. Division scales are not permitted. (IR-4; IR-8; RS.MA-01; 3.6.1)

4.3 The incident record must capture, for each notice clock, the time it starts: discovery of a cyber incident (DFARS 252.204-7012), identification of covered equipment (FAR 52.204-25), determination of a breach (state laws), and determination of materiality (Form 8-K Item 1.05). (IR-5; RS.AN-03)

4.4 At least four people in at least two locations must hold DoD-approved medium assurance certificates and tested DIBNet access at all times. (IR-6; 252.204-7012(c)(3))

4.5 The Group General Counsel must maintain the multi-regulator notification matrix (P08) and review it every quarter. Every external notice must be approved by counsel before it is sent. (IR-6; IR-8; RS.CO-02)

4.6 **SEC materiality.** Severity 1 incidents must be escalated to the disclosure committee within 24 hours of declaration. The committee must decide materiality without unreasonable delay. If material, the Form 8-K Item 1.05 filing must be made within 4 business days after the determination. (IR-6; RS.CO-03)

4.7 **Suspect products** must be quarantined and kept, not returned or destroyed, until the Group supply chain risk director and counsel approve disposition, and any prime or contracting officer instructions are received. (SR-8; IR-4)

4.8 **Ransom payments** require board audit and risk committee approval, counsel, the cyber insurer, and an OFAC sanctions check before any payment. (IR-4)

4.9 The group must run at least one cross-division exercise each year that includes the notification matrix and a materiality decision. (IR-3; ID.IM-02; 3.6.3)

4.10 Evidence must be preserved with chain of custody. For incidents reported under DFARS 252.204-7012, images and monitoring data must be kept at least 90 days from the report. (IR-4; RS.AN-03; 252.204-7012(e))

4.11 A lessons-learned review must be completed within 30 days of recovery, and the risk registers, POA&M, and this policy updated. (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 5. Compliance is checked through the P07 assessment (IR-3, IR-4, IR-6, IR-8), exercise reports, and the PCI DSS ROC.

## 6. Exceptions
Exceptions follow POL-01 section 4.14. No exception may extend a legal or contractual notice deadline.

## 7. Related documents
P08 runbook and notification matrix; POL-01; `division-supplements.md`; BIA recovery priorities (P05).
