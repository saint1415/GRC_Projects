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
| Regulatory drivers | N81-R02 (Fla. Stat. 501.171(3)-(6)) and other states' laws; N81-R03 and N44-45-R01 (PCI DSS v4.0.1 Req. 12.10); N54-R06 (45 CFR 164.308(a)(6); 164.410); N52-R08 (Form 8-K Item 1.05); merchant agreements; Manufacturer A and B agreements; TPA agreement; enterprise and managed services contracts |
| Division supplements | Device Repair: manufacturer, TPA, and enterprise notices; device custody during incidents. Electronics Retail: acquirer and card brand procedures. IT Support: business associate and managed customer notices; RMM kill switch |

## 1. Purpose
Make sure the group detects, contains, and recovers from incidents consistently across divisions, and that each division meets its own notice duties to acquirers, manufacturers, the TPA, customers, covered entities, regulators, and investors on time.

## 2. Scope
All security incidents affecting any group system, customer device in custody, or customer data, including incidents at vendors, tool suppliers, and cloud providers that affect group data or systems, and incidents the group causes on managed customers' systems.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group SOC director | Runs detection and incident handling 24x7; incident commander for Severity 1 and 2 incidents in shared services |
| Group CISO | Declares Severity 1; briefs the board risk committee |
| Group General Counsel | Owns the notification matrix; approves every external notice |
| Division security and compliance leads | Bring division facts; make their division's contractual and regulatory notices with counsel |
| IT Support Privacy Official | Business associate notices to covered entities (164.410) |
| Disclosure committee | Decides materiality for Form 8-K Item 1.05 |

## 4. Policy statements
4.1 Every workforce member must report a suspected incident to the group SOC within 1 hour of noticing it, including a suspected misuse of a customer's device. (IR-6; RS.MA-02; 164.308(a)(6)(ii))

4.2 The group SOC must handle incidents using one group severity scale and the group playbooks, including the P08 runbook. Division scales are not permitted. (IR-4; IR-8; RS.MA-01; PCI DSS 12.10.1)

4.3 The incident log must record, for each division, the time it first suspected a card data compromise, the date it determined a breach or had reason to believe one occurred, and, for IT Support, the date of discovery (the first day known, or by reasonable diligence would have been known, to any employee or agent, 164.410(a)(2)). Notice clocks are planned from the earliest of these. (IR-5; RS.AN-03)

4.4 **Contract clocks are legal duties for this policy.** The matrix must list, with an owner, each contract notice term: both merchant agreements (24 hours from suspicion), Manufacturers A and B (24 hours), the TPA (48 hours), enterprise depot contracts (72 hours after confirmation), managed services contracts, and business associate agreements (10 calendar days standard; 5 business days for 47 practices). (IR-6; RS.CO-02; PCI DSS 12.10.1)

4.5 The Group General Counsel must maintain the notification matrix (P08) and review it every quarter. Every external notice must be approved by counsel before it is sent. When a division holds personal information for another business (as a third-party agent), it must notify that business no later than the state-law deadline (10 days in Florida, 501.171(6)(a)) or the contract term, whichever is shorter. (IR-6; IR-8; RS.CO-02)

4.6 **SEC materiality.** Severity 1 incidents must be escalated to the disclosure committee within 24 hours of declaration. The committee must decide materiality without unreasonable delay. If material, the Form 8-K Item 1.05 filing must be made within 4 business days after the determination. (IR-6; RS.CO-03)

4.7 **Ransom and extortion payments** require board risk committee approval, counsel, the cyber insurer, and an OFAC sanctions check before any payment. (IR-4)

4.8 The group must run at least one cross-division exercise each year that includes both merchants, IT Support's customer notices, the notification matrix, and a materiality decision. (IR-3; ID.IM-02; PCI DSS 12.10.2)

4.9 Evidence must be preserved with chain of custody. Customer devices involved in an incident must be quarantined in the evidence cage and not returned or wiped until counsel releases them. (IR-4; RS.AN-07)

4.10 A lessons-learned review must be completed within 30 days of recovery, and the risk registers, POA&M, and this policy updated. (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment (IR-3, IR-4, IR-6, IR-8), exercise reports, and the QSA ROCs.

## 6. Exceptions
Exceptions follow POL-01 section 4.10. No exception may extend a legal or contractual notice deadline.

## 7. Related documents
P08 runbook and notification matrix; POL-01; `division-supplements.md`; BIA recovery priorities (P05).
