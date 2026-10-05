# Incident Response Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions (Crude Oil Production, Power Generation, Crude Logistics) and corporate shared services |
| Policy ID | POL-03 |
| Owner | Group CISO, with the Group General Counsel for notifications |
| Approved by | Board risk committee (2026-09-17) |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, or incidents |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8, CP-2 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| Regulatory and benchmark drivers | NERC CIP-003-9 R2 Attachment 1 Section 4 and EOP-004-4; PHMSA 195.52 and 195.402(e); 40 CFR 110.6; 49 CFR 171.15; Form 8-K Item 1.05; state breach laws |
| Division supplements | Production: manual operations and SPCC alarm-loss duties. Power Generation: Reportable Cyber Security Incident determination and E-ISAC notice; EOP-004 Operating Plan. Crude Logistics: PHMSA and hazmat notices; controller response to SCADA loss |

## 1. Purpose
Make sure the group detects, contains, and recovers from incidents consistently across divisions, protects people and the environment first, and meets every regulator's notice duty on time.

## 2. Scope
All security incidents affecting any group system or data, including OT, and incidents at suppliers and cloud providers that affect group operations or data.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group SOC director | Runs detection and incident handling 24x7; incident commander for Severity 1 and 2 incidents in shared services |
| Group OT Security Director | Leads the OT desk and OT technical response |
| Control room shift leads (IOC, GCC, PCC) | Decide isolation, manual operation, and shutdowns for their operations |
| Group CISO | Declares Severity 1; briefs the board risk committee |
| Group General Counsel | Owns the notification matrix; approves every external notice |
| Regulator notice owners | Production HSE director (EPA); Power Generation CIP Senior Manager (E-ISAC determination) and NERC Compliance Manager (EOP-004); Pipeline Compliance Manager (PHMSA); Fleet Safety Director (hazmat incidents) |
| Disclosure committee | Decides materiality for Form 8-K Item 1.05 |

## 4. Policy statements
4.1 Every workforce member must report a suspected incident to the group SOC within 1 hour of noticing it. Control room staff report to their shift lead, who calls the SOC OT desk. (IR-6; RS.MA-02)

4.2 The SOC must handle incidents using one group severity scale and the group playbooks, including the P08 runbook. Division severity scales are not permitted. (IR-4; IR-8; RS.MA-01)

4.3 **Operations decide on operations.** Only the control room shift lead may isolate a control room from corporate networks, switch to manual operation, or shut in or shut down. The SOC advises; it does not direct controllers. Safety and environmental protection come before evidence collection. (IR-4; RS.MI-01)

4.4 The incident log must record the time each clock starts: confirmed discovery (PHMSA), knowledge of a discharge (EPA), determination of a Reportable Cyber Security Incident (NERC), the materiality determination (SEC), and determination of a breach (state laws). (IR-5; RS.AN-03)

4.5 The Group General Counsel must maintain the multi-regulator notification matrix (P08) and review it every quarter. Each regulator notice has a named owner. Counsel approves every notice except safety and environmental notices that a rule requires within hours, which the named owner makes first and reports to counsel. (IR-6; IR-8; RS.CO-02)

4.6 Printed copies of the notification matrix, contacts, and forms must be kept at the IOC, BCC, GCC, PCC, and backup PCC, so notices can be made when corporate email and phones are unavailable. (IR-8; CP-2; RS.CO-02)

4.7 **SEC materiality.** Severity 1 incidents must be escalated to the disclosure committee within 24 hours of declaration. The committee must decide materiality without unreasonable delay. If material, the Form 8-K Item 1.05 filing must be made within 4 business days after the determination. (IR-6; RS.CO-03)

4.8 **Ransom payments** require board risk committee approval, counsel, the cyber insurer, and an OFAC sanctions check before any payment. (IR-4; RS.MA-04)

4.9 The group must run at least one cross-division exercise each year that includes OT isolation, the notification matrix, and a materiality decision. Power Generation must also test its CIP-003-9 incident response plan at least once every 36 calendar months and update it within 180 days after a test or reportable incident. (IR-3; ID.IM-02)

4.10 **Reconnection.** A control room isolated during an incident may be reconnected to corporate networks only after the incident commander and the Group OT Security Director confirm that the paths it uses are clean and the shift lead agrees. (IR-4; CP-10; RC.RP-05)

4.11 Evidence must be preserved with chain of custody, including controller logic and HMI state where it can be captured safely. Logs relevant to an incident must be placed on legal hold. (IR-4; RS.AN-07)

4.12 A lessons-learned review must be completed within 30 days of recovery, and the risk registers, POA&M, and this policy updated. (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.14. Compliance is checked through the P07 assessment of common controls and division samples, the annual supplement attestations, and division access reviews.

## 6. Exceptions
Exceptions follow POL-01 section 4.11. No exception may weaken a safety function or extend a legal notice deadline.

## 7. Related documents
P08 runbook and notification matrix; POL-01; `division-supplements.md`; BIA recovery priorities (P05).
