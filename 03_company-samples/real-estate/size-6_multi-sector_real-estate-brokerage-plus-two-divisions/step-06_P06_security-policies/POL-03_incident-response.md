# Incident Response Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-03 |
| Owner | Group CISO, with the Group General Counsel for notifications |
| Approved by | Board risk committee; adopted by the boards of Home Loans and Title as part of their written incident response plans |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), after every Severity 1 incident, and after each cross-division exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8, CP-2 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02, ID.IM-04 |
| FTC Safeguards Rule and other | 16 CFR 314.4(h), (j); state breach notification laws; state insurance data security laws where enacted; Form 8-K Item 1.05 |
| Division supplements | Brokerage: escrow dispute notices and agent mailbox takeover. Mortgage and Title: wire recall, lender and underwriter notices, SAR routing, insurance commissioner notices. Homebuilding: trade partner payment fraud and smart-home incidents |

## 1. Purpose
Make sure the group detects, contains, and recovers from incidents consistently across divisions, recovers diverted funds where possible, and that each financial institution, each division, and the public company meets its own notice duties on time.

## 2. Scope
All security events affecting any group system or data, including events at service providers that affect group data, and all attempted or completed payment fraud.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group SOC director | Runs detection and incident handling 24x7; incident commander for Severity 1 and 2 incidents |
| Group CISO (Qualified Individual) | Declares Severity 1; briefs the board risk committee and the institution presidents |
| Group General Counsel | Owns the notification matrix; approves every external notice |
| President, Mortgage; President, Title | Decide their institution's notices with counsel |
| Group Treasurer | Leads funds recovery (recalls, bank holds) |
| Division incident liaisons | Bring division facts and division regulator and contract contacts |
| Disclosure committee | Decides materiality for Form 8-K Item 1.05 |

## 4. Policy statements
4.1 Every workforce member and contractor agent must report a suspected incident, including a suspicious payment change request, to the group SOC within 1 hour of noticing it. (IR-6; RS.MA-02)

4.2 The group SOC must handle incidents using one group severity scale and the group playbooks, including the P08 runbook. Division scales are not permitted. (IR-4; IR-8; RS.MA-01; 314.4(h)(2))

4.3 **Discovery dates.** The incident record must state, for each financial institution and each affected division, the first day the event was known to any employee, officer, or other agent, counting, conservatively, knowledge by contractor agents handling the institution's customer files and by the parent's SOC staff (16 CFR 314.4(j)(2)), and the date each state law clock started. (IR-5; RS.AN-03; 314.4(h)(6))

4.4 **FTC notice per institution.** Affected consumers must be counted separately for Home Loans and for Title. Each institution with a notification event involving at least 500 of its consumers must notify the FTC as soon as possible and no later than 30 days after discovery. (IR-6; RS.CO-02; 314.4(j))

4.5 The Group General Counsel must maintain the multi-regulator notification matrix (P08), including the states where Title is subject to an insurance data security law, and review it every quarter. Every external notice must be approved by counsel. (IR-6; IR-8; RS.CO-02; 314.4(h)(4))

4.6 **SEC materiality.** Severity 1 incidents must be escalated to the disclosure committee within 24 hours of declaration. The committee must decide materiality without unreasonable delay. If material, the Form 8-K Item 1.05 filing must be made within 4 business days after the determination. (IR-6; RS.CO-03)

4.7 **Funds recovery.** When a payment may have been diverted, Treasury must ask the sending bank to recall it immediately and file a complaint with the FBI Internet Crime Complaint Center the same day. Loan-related fraud must be routed to the Home Loans BSA officer within 1 business day. (IR-4; RS.MI-01)

4.8 **Ransom payments** require board risk committee approval, counsel, the cyber insurer, and an OFAC sanctions check before any payment. (IR-4)

4.9 The group must run at least one cross-division exercise each year that includes the notification matrix, per-institution FTC counting, and a materiality decision. (IR-3; ID.IM-02)

4.10 A lessons-learned review must be completed within 30 days of recovery, and the risk registers, POA&M, and this policy updated. (IR-4; ID.IM-04; 314.4(h)(7))

4.11 Evidence must be preserved with chain of custody, and relevant logs placed on legal hold. (IR-4; RS.AN-03)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment (IR-3, IR-4, IR-6, IR-8) and exercise reports.

## 6. Exceptions
Exceptions follow POL-01 section 4.12. No exception may extend a legal notice deadline.

## 7. Related documents
P08 runbook and notification matrix; POL-01; `division-supplements.md`; BIA recovery priorities (P05).
