# Incident Response Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-03 |
| Owner | Group CISO, with the Group General Counsel for notifications |
| Approved by | Board risk committee, 2026-09-15 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), after every Severity 1 incident, and after each cross-division exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-7, IR-8, CP-2 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| Regulatory drivers | Customer contract notice terms; GSA BTTRG v3.0 section 1.6.1; N23-R03 (DFARS 252.204-7012(c)-(e)); FAR 52.204-25(d), 52.204-23(c), 52.204-30(c); state breach laws (Florida worked example: Fla. Stat. 501.171); SEC Form 8-K Item 1.05 |
| Division supplements | Facilities Support: building safety first and customer security staff. Construction: DoD reporting. Janitorial and Security: monitoring customers and police dispatch |

## 1. Purpose
Make sure the group detects, contains, and recovers from incidents consistently across divisions, keeps people in customer buildings safe while it does so, and meets every customer, agency, state, and SEC notice duty on time.

## 2. Scope
All security incidents affecting any group system, the IBOP and the customer building systems it administers, or group-held information, including incidents at vendors, integrators, and subcontractors that affect group or customer information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group SOC director | Runs detection and incident handling 24x7; incident commander for Severity 1 and 2 incidents in shared services |
| Group CISO | Declares Severity 1; briefs the board risk committee |
| Group General Counsel | Owns the notification matrix; approves every external notice |
| Division security and compliance leads | Bring division facts and customer contacts; send customer notices for their division's contracts |
| Construction CUI program manager | Makes DoD reports for covered defense information |
| Facilities Support site managers and ROC directors | Coordinate building safety with customer security staff |
| Disclosure committee | Decides materiality for Form 8-K Item 1.05 |

## 4. Policy statements
4.1 Every workforce member must report a suspected incident to the group SOC or the nearest ROC within 1 hour of noticing it. (IR-6; RS.MA-02)

4.2 The group SOC must handle incidents using one group severity scale and the group playbooks, including the P08 runbook. **Building safety comes first:** before any containment step that could change door states or building equipment, the site manager must agree the door and equipment posture with the customer's security staff. (IR-4; IR-8; RS.MA-01)

4.3 The incident log must record when the incident was first known to any employee. Contract and legal notice clocks are planned from that time unless counsel documents a later start. (IR-5; RS.AN-03)

4.4 **Customer notices.** The division that holds the affected contract must notify the customer within the contract's notice term (most state and county contracts: 24 hours of discovery; 9 county contracts: 12 hours; commercial monitoring contracts: 72 hours), with the facts the customer needs for its own legal reports. (IR-6; RS.CO-02)

4.5 The Group General Counsel must maintain the notification matrix (P08) with every contract's notice term and review it every quarter. Every external notice must be approved by counsel before it is sent, except a first notice under 4.4 that would otherwise be late. (IR-6; IR-8; RS.CO-02)

4.6 **DoD reporting.** A cyber incident affecting a covered contractor information system or covered defense information must be reported to DoD at https://dibnet.dod.mil within 72 hours of discovery (DFARS 252.204-7012(c)). Images and monitoring data must be preserved for at least 90 days from the report (7012(e)), and malicious software submitted to the DoD Cyber Crime Center (7012(d)). At least three people must hold the medium assurance certificate needed to report. (IR-6; IR-4; RS.CO-02)

4.7 **Federal buildings.** Incidents that may involve agency systems, agency data, or credentials of staff with agency access must be reported to the agency as its contract and policies require; for GSA buildings, immediately (BTTRG v3.0 section 1.6.1). (IR-6; RS.CO-02)

4.8 **Supply chain reports.** If an incident identifies covered telecommunications or video surveillance equipment, the contracting officer must be notified within 1 business day (FAR 52.204-25(d)); Kaspersky covered articles and FASCSA-covered articles within 3 business days (52.204-23(c), 52.204-30(c)). (IR-6; SR-3)

4.9 **SEC materiality.** Severity 1 incidents must be escalated to the disclosure committee within 24 hours of declaration. The committee must decide materiality without unreasonable delay. If material, the Form 8-K Item 1.05 filing must be made within 4 business days after the determination. (IR-6; RS.CO-03)

4.10 **Ransom.** The group does not pay ransoms on behalf of public customers, several of which may not pay (Florida worked example: Fla. Stat. 282.3186). Any payment for the group's own systems requires board risk committee approval, counsel, the cyber insurer, and an OFAC sanctions check first. (IR-4)

4.11 The group must run at least one cross-division exercise each year that includes the notification matrix, a customer participant, a DoD reporting decision, and a materiality decision. (IR-3; ID.IM-02)

4.12 Evidence must be preserved with chain of custody. Logs relevant to an incident must be placed on legal hold. (IR-4; RS.AN-03)

4.13 A lessons-learned review must be completed within 30 days of recovery, and the risk registers, POA&M, and this policy updated. (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment (IR-4, IR-6, IR-8) and exercise reports.

## 6. Exceptions
Exceptions follow POL-01 section 4.11. No exception may extend a legal or contract notice deadline.

## 7. Related documents
P08 runbook and notification matrix; POL-01; `division-supplements.md`; BIA recovery priorities (P05).
