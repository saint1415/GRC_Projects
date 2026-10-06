# Incident Response Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-03 |
| Owner | Group CISO, with the Group General Counsel for notifications |
| Approved by | Board risk committee, 2026-09-15 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), after every Severity 1 incident, and after each cross-division exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8, CP-2 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| PCI DSS and other | PCI DSS 12.10; card brand compromise procedures (Visa What To Do If Compromised v10.0); state breach laws; Form 8-K Item 1.05 |
| Division supplements | Live Venues: event-day escalation and crowd safety. Hotels and Restaurants: guest safety and door locks. Ticketing and Streaming: client notices and the client notice register |

## 1. Purpose
Make sure the group detects, contains, and recovers from incidents consistently across divisions, and that each merchant, the service provider, and the public company meet their own notice duties on time.

## 2. Scope
All security incidents affecting any group system or data, including incidents at service providers and on payment pages that affect group or client data.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group SOC director | Runs detection and incident handling 24x7; incident commander for Severity 1 and 2 incidents in shared services and the ticketing platform |
| Group CISO | Declares Severity 1; briefs the board risk committee |
| Group General Counsel | Owns the notification matrix; approves every external notice |
| Group PCI program director | Coordinates acquirer and card brand notices for each merchant role and the service provider |
| General Manager Ticketing | Issues client notices under client agreements and state third-party agent laws |
| Disclosure committee | Decides materiality for Form 8-K Item 1.05 |
| Division incident liaisons | Bring division facts, event-day or guest impact, and division contacts |

## 4. Policy statements
4.1 Every workforce member must report a suspected incident to the group SOC within 1 hour of noticing it. (IR-6; RS.MA-02)

4.2 The group SOC must handle incidents using one group severity scale and the group playbooks, including the P08 runbook. Division scales are not permitted. (IR-4; IR-8; RS.MA-01; PCI DSS 12.10.1)

4.3 The incident log must record the time of first suspicion of a card data compromise and the time of determination of a breach, because card brand clocks run from suspicion and state clocks from determination. (IR-5; RS.AN-03)

4.4 **Notice ownership by role.** For each affected merchant role (Live Venues, Hotels and Restaurants, streaming), the Group PCI program director notifies that merchant's acquirer as its merchant agreement requires. For clients of the ticketing platform, the General Manager Ticketing notifies each affected client within its contract term and within any state third-party agent deadline. (IR-6; RS.CO-02; PCI DSS 12.10.1)

4.5 The Group General Counsel must maintain the notification matrix (P08) and a client notice register, review both every quarter, and approve every external notice. (IR-6; IR-8; RS.CO-02)

4.6 **SEC materiality.** Severity 1 incidents must be escalated to the disclosure committee within 24 hours of declaration. The committee must decide materiality without unreasonable delay. If material, the Form 8-K Item 1.05 filing must be made within 4 business days after the determination. (IR-6; RS.CO-03)

4.7 **Ransom and extortion payments** require board risk committee approval, counsel, the cyber insurer, and an OFAC sanctions check before any payment. (IR-4)

4.8 The group must run at least one cross-division exercise each year that includes the notification matrix, client notices, card brand notices, and a materiality decision. (IR-3; ID.IM-02; PCI DSS 12.10.2)

4.9 Evidence must be preserved with chain of custody. Logs and payment page captures relevant to an incident must be placed on legal hold. (IR-4; RS.AN-03)

4.10 A lessons-learned review must be completed within 30 days of recovery, and the risk registers, POA&M, and this policy updated. Incident records are kept at least 5 years. (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment (IR-3, IR-4, IR-6, IR-8) and exercise reports.

## 6. Exceptions
Exceptions follow POL-01 section 4.11. No exception may extend a legal, card brand, or contractual notice deadline.

## 7. Related documents
P08 runbook and notification matrix; POL-01; `division-supplements.md`; BIA recovery priorities (P05).
