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
| Regulatory drivers | PCI DSS Requirement 12.10 (N72-R01, N71-R04, N53-R04); 16 CFR 314.4(h) and (j) (N53-R01); state breach laws (N72-R04; Fla. Stat. 501.171 worked example); Form 8-K Item 1.05 (N53-R05) |
| Division supplements | Hotels: owner notices for managed hotels; lock and guest-safety escalation. Attractions: ride safety escalation; kids' club and biometric data. Vacation Ownership: FTC Safeguards Rule notice; owners' associations |

## 1. Purpose
Make sure the group detects, contains, and recovers from incidents consistently across divisions, and that every legal entity, every acquirer relationship, and the public company meets its own notice duties on time.

## 2. Scope
All security incidents affecting any group system or data, including incidents at managed hotels, at service providers (including the legacy POS vendor, the PMS vendor, and the gate vendor), and at cloud providers that affect group data or card data.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group SOC director | Runs detection and incident handling 24x7; incident commander for Severity 1 and 2 incidents in shared services |
| Group CISO | Declares Severity 1; briefs the board risk committee |
| Group General Counsel | Owns the notification matrix; approves every external notice; chairs the disclosure committee |
| Group Director of Payments and PCI Compliance | Notifies acquirers under each merchant agreement; coordinates the PCI Forensic Investigator |
| Hotels senior vice president of owner relations | Notifies owners of managed hotels under their agreements |
| Qualified Individual | Decides, with counsel, whether a Safeguards Rule notification event occurred; files the FTC notice |
| Group Chief Privacy Officer | Breach determinations with counsel; state notices |
| Disclosure committee | Decides materiality for Form 8-K Item 1.05 |
| Division incident liaisons | Bring division facts, safety and operational impact, and division contacts |

## 4. Policy statements
4.1 Every workforce member must report a suspected incident to the group SOC within 1 hour of noticing it. Front desk, outlet, and park staff must report a suspected skimmer or tampered terminal immediately and stop using the device. (IR-6; RS.MA-02; Req 12.10.1, 9.5.1)

4.2 The group SOC must handle incidents using one group severity scale and the group playbooks, including the P08 runbook. Division severity scales are not permitted. (IR-4; IR-8; RS.MA-01)

4.3 **Discovery and determination dates.** The incident log must record, for each regime, the date its clock starts: for the FTC Safeguards Rule, the first day the event is known to any employee, officer, or other agent of the finance subsidiary, which includes the group SOC (314.4(j)(2)); for state laws, the trigger each statute uses (in Florida, the determination of a breach); and for acquirers, the trigger in each merchant agreement. (IR-5; RS.AN-03)

4.4 **Card compromise.** A suspected compromise of card data must be reported to the affected acquirers as each merchant agreement requires, and a PCI Forensic Investigator engaged when an acquirer or card brand requires one. For managed hotels, the owner is the merchant of record and must be notified under its management agreement so it can notify its acquirer. (IR-6; RS.CO-02; Req 12.10.1)

4.5 The Group General Counsel must maintain the multi-regulator notification matrix (P08) and review it every quarter. Every external notice must be approved by counsel before it is sent. (IR-6; IR-8; RS.CO-02)

4.6 **FTC Safeguards Rule.** If a notification event involves the information of 500 or more consumers, the Qualified Individual must file the FTC notice as soon as possible and no later than 30 days after discovery. (IR-6; RS.CO-02; 314.4(j))

4.7 **SEC materiality.** Severity 1 incidents, and any incident that starts at a managed hotel owner, a shared vendor, or a service provider and could affect more than one division, must be escalated to the disclosure committee within 24 hours of declaration. The committee must decide materiality without unreasonable delay. If material, the Form 8-K Item 1.05 filing must be made within 4 business days after the determination. (IR-6; RS.CO-03)

4.8 **Safety first.** Any incident that may affect ride and show control or door locks must be escalated to ride engineering or hotel engineering at once. Rides stay closed until engineers verify their controls; affected rooms are re-keyed. (IR-4; RS.MA-01)

4.9 **Ransom payments** require board risk committee approval, counsel, the cyber insurer, and an OFAC sanctions check before any payment. (IR-4)

4.10 The group must run at least one cross-division exercise each year that includes the notification matrix, an acquirer and owner notice, an FTC notice decision, and a materiality decision. (IR-3; ID.IM-02; Req 12.10.2)

4.11 Evidence must be preserved with chain of custody. Logs relevant to an incident must be placed on legal hold. (IR-4; RS.AN-03)

4.12 A lessons-learned review must be completed within 30 days of recovery, and the risk registers, POA&M, and this policy updated. (IR-4; ID.IM-02; 314.4(h)(7))

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment (IR-3, IR-4, IR-6, IR-8) and exercise reports.

## 6. Exceptions
Exceptions follow POL-01 section 4.11. No exception may extend a legal or contractual notice deadline.

## 7. Related documents
P08 runbook and notification matrix; POL-01; `division-supplements.md`; BIA recovery priorities (P05).
