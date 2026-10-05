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
| Regulatory drivers | C-WATER-R01 (300i-2(b)(2)); 40 CFR 141.202(b) and 141.31; N23-R03 (DFARS 252.204-7012(c)-(g)); SEC Form 8-K Item 1.05; state breach laws; OFAC ransomware advisory (2021-09-21) |
| Division supplements | Water Utility: process safety first, Tier 1 notice decisions. Construction: DFARS reporting. Environmental Services: client notices and hazmat incidents |

## 1. Purpose
Make sure the group detects, contains, and recovers from incidents consistently across divisions; that operators protect public health first; and that each division meets its own notice clocks.

## 2. Scope
All security incidents affecting any group IT or OT system or data, including incidents at suppliers, sister divisions acting as suppliers, and cloud providers.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Control room operators and shift supervisors | Take process safety actions immediately; put affected processes in local or manual control |
| Group SOC director | Incident commander for Severity 1 and 2 incidents in shared services |
| Group CISO | Declares Severity 1; briefs the board risk committee |
| Water Utility VP of Water Quality and Compliance | Decides Tier 1 public notices and primacy agency consultation for each affected system |
| Construction security and compliance lead | Makes DFARS 252.204-7012 reports |
| Environmental Services remote monitoring general manager | Makes client notices |
| Group General Counsel | Owns the notification matrix; approves legal notices |
| Disclosure committee | Decides materiality for Form 8-K Item 1.05 |

## 4. Policy statements
4.1 Every workforce member must report a suspected incident to the group SOC within 1 hour of noticing it. Operators must not wait for anyone before taking process safety actions. (IR-6; RS.MA-02)

4.2 The group SOC must handle incidents using one group severity scale and the group playbooks, including the OT playbook in P08. Division scales are not permitted. (IR-4; IR-8; RS.MA-01)

4.3 The incident log must record the time each regulated clock starts: when a water system learns of a situation that may need a Tier 1 notice (40 CFR 141.202(b)); when Construction discovers a cyber incident affecting covered defense information (252.204-7012(c)); and when the disclosure committee determines materiality. (IR-5; RS.AN-03)

4.4 Tier 1 public notice and primacy agency consultation decisions belong to the Water Utility VP of Water Quality and Compliance (or the named delegate for each system) and must be made in time to deliver notice no later than 24 hours after the system learns of the situation. **Public health notices never wait for legal review**; counsel is informed in parallel. (IR-6; RS.CO-02)

4.5 Construction must report cyber incidents affecting covered defense information to DoD within 72 hours of discovery, submit isolated malware to DC3, and preserve images and monitoring data for at least 90 days from the report. At least two staff must hold the DoD-approved medium assurance certificate needed to report. (IR-6; IR-4)

4.6 The Group General Counsel must maintain the multi-regulator notification matrix (P08) and review it every quarter. Every external legal notice other than a public health notice must be approved by counsel before it is sent. (IR-6; IR-8; RS.CO-02)

4.7 **SEC materiality.** Severity 1 incidents must be escalated to the disclosure committee within 24 hours of declaration. The committee must decide materiality without unreasonable delay. If material, the Form 8-K Item 1.05 filing must be made within 4 business days after the determination. (IR-6; RS.CO-03)

4.8 **Ransom payments** require board risk committee approval, counsel, the cyber insurer, and an OFAC sanctions check before any payment. (IR-4)

4.9 The group must run at least one cross-division exercise each year that includes an OT scenario, the notification matrix, and a materiality decision. (IR-3; ID.IM-02)

4.10 Evidence must be preserved with chain of custody, without delaying process safety actions. (IR-4; RS.AN-03)

4.11 A lessons-learned review must be completed within 30 days of recovery. The risk registers, POA&M, this policy, and the ERP of every affected water system must be updated where the incident shows a need. (IR-4; CP-2; ID.IM-02)

## 5. Compliance and enforcement
Checked through P07 (IR-3, IR-4, IR-6, IR-8) and exercise reports. Violations are handled under POL-01 4.7.

## 6. Exceptions
Exceptions follow POL-01 4.10. No exception may extend a legal or regulatory notice deadline.

## 7. Related documents
P08 runbook and notification matrix; POL-01; ERPs of the covered water systems; `division-supplements.md`; BIA recovery priorities (P05).
