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
| Regulatory basis | PCI DSS 12.10; 16 CFR 314.4(h), (j); 12 CFR 53.4, 225.303, 304.24 (C-FINANCIAL-R01); card brand rules; Form 8-K Item 1.05 (N51-R08); state breach laws |
| Division supplements | Payment Processing: card brand and sponsor bank procedures; PFI engagement. Software: ISV and merchant notices; gateway and storefront playbooks. Merchant Consulting: client notices under engagement letters |

## 1. Purpose
Make sure the group detects, contains, and recovers from incidents consistently across divisions, and that every division meets its own card brand, bank, regulator, contract, and public company notice duties on time, wherever the incident starts.

## 2. Scope
All security incidents affecting any group system or data, including incidents at service providers, affiliates, and cloud providers that affect group data, and incidents that start in one division and reach another.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group SOC director | Runs detection and incident handling 24x7; incident commander for Severity 1 and 2 incidents in shared services |
| Group CISO | Declares Severity 1; briefs the board risk committee |
| Group General Counsel | Owns the notification matrix; approves every external notice |
| Head of bank and network relationships | Card brand and sponsor bank notices; the 4-hour determination for covered services |
| Software division client trust and assurance director | ISV and merchant notices for the Software division |
| Merchant Consulting division president | Client notices under engagement letters |
| Disclosure committee | Decides materiality for Form 8-K Item 1.05 |
| Division incident liaisons | Bring division facts, operational impact, and division contacts |

## 4. Policy statements
4.1 Every workforce member must report a suspected incident to the group SOC within 1 hour of noticing it. (IR-6; RS.MA-02; PCI DSS 12.10.1)

4.2 The group SOC must handle incidents using one group severity scale and the group playbooks, including the P08 runbook. Division scales are not permitted. (IR-4; IR-8; RS.MA-01)

4.3 The incident log must record, for each notice clock, the time it starts: reasonable suspicion of an account data compromise (card brands), discovery by any employee or agent (16 CFR 314.4(j)), determination of a covered-services disruption (bank rules), determination of a breach (state laws), and the materiality determination (SEC). (IR-5; RS.AN-03)

4.4 **Account data compromise anywhere in the group.** Any suspected compromise of cardholder data, in any division, must be escalated to the head of bank and network relationships within 1 hour of suspicion, so the card brand and sponsor bank clocks are met. (IR-6; RS.CO-02; PCI DSS 12.10.1)

4.5 **Covered services.** For any incident, whatever its origin, that may disrupt clearing, settlement, reconciliation, or merchant funding files, the incident commander and the head of bank and network relationships must decide whether covered services have been, or are reasonably likely to be, materially disrupted or degraded for 4 or more hours, record the decision, and notify each affected sponsor bank's designated contact as soon as possible under the rule of that bank's regulator. (IR-6; RS.CO-02; 12 CFR 53.4; 225.303; 304.24)

4.6 The Group General Counsel must maintain the multi-regulator notification matrix (P08), review it every quarter, and confirm every sponsor bank, ISV, and enterprise merchant contact every quarter. Every external notice must be approved by counsel before it is sent. (IR-6; IR-8; RS.CO-02)

4.7 **SEC materiality.** Severity 1 incidents must be escalated to the disclosure committee within 24 hours of declaration. The committee must decide materiality without unreasonable delay. If material, the Form 8-K Item 1.05 filing must be made within 4 business days after the determination. (IR-6; RS.CO-03)

4.8 **FTC notice.** For a notification event involving the information of at least 500 consumers, the financial-institution division must notify the FTC as soon as possible and no later than 30 days after discovery. (IR-6; 314.4(j))

4.9 **Ransom payments** require board risk committee approval, counsel, the cyber insurer, and an OFAC sanctions check before any payment. (IR-4)

4.10 The group must run at least one cross-division exercise each year that includes the notification matrix, a covered-services determination, and a materiality decision. (IR-3; ID.IM-02; PCI DSS 12.10.2)

4.11 Evidence must be preserved with chain of custody, and a PCI Forensic Investigator engaged when a card brand requires one. Logs relevant to an incident must be placed on legal hold. (IR-4; RS.AN-03)

4.12 **PAN found where not expected** (email, tickets, logs, analytics) must be handled as an incident: contain, purge with a record, find the root cause, and decide whether any notice applies. (IR-4; PCI DSS 12.10.7)

4.13 A lessons-learned review must be completed within 30 days of recovery, and the risk registers, POA&M, and this policy updated. (IR-4; ID.IM-02; 314.4(h)(7))

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment (IR-3, IR-4, IR-6, IR-8), exercise reports, and the ROCs.

## 6. Exceptions
Exceptions follow POL-01 section 4.10. No exception may extend a legal, card brand, or contract notice deadline.

## 7. Related documents
P08 runbook and notification matrix; POL-01; POL-04; `division-supplements.md`; BIA recovery priorities (P05).
