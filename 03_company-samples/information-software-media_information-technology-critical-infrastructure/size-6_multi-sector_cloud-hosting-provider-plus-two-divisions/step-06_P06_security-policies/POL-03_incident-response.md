# Incident Response Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-03 |
| Owner | Group CISO, with the Group General Counsel for notifications |
| Approved by | Board risk committee, 2026-09-17 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), after every Severity 1 incident, and after each cross-division exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8, AU-11, SI-4 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| Regulatory references | FedRAMP IEC rules (G1); 48 CFR 252.204-7012(c) to (g) and (m); 12 CFR 53.4; 45 CFR 164.410; 16 CFR 314.4(h) and (j); PCI DSS v4.0.1 Requirement 12.10; sponsor bank and card network terms; Form 8-K Item 1.05; state breach laws |
| Division supplements | Cloud Hosting: FedRAMP federal incident response coordinator and PAIN rating. Managed IT: DIBNet reporting and DIB client notices. Payment Processing: sponsor bank, card network, and FTC notices |

## 1. Purpose
Make sure the group detects, contains, and recovers from incidents consistently across divisions, and that every division meets its own notice duties on time.

## 2. Scope
All security incidents affecting any group system or data, including incidents at vendors and in services one division provides to another.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group SOC director | Runs detection and incident handling 24x7; incident commander for Severity 1 and 2 incidents in shared services |
| Group CISO | Declares Severity 1; briefs the board risk committee |
| Group General Counsel | Owns the notification matrix; reviews external notices |
| Government Cloud compliance director (federal incident response coordinator) | FedRAMP reportability evaluation and IEC reports for G1 |
| Managed IT federal contracts compliance officer | DIBNet reports and notices to primes |
| Payment Processing chief compliance officer | Sponsor bank, card network, FTC, and state licensing notices |
| Division customer and client notice owners | Bank notices, BAA notices, and contractual notices for their division |
| Disclosure committee | Decides materiality for Form 8-K Item 1.05 |

## 4. Policy statements
4.1 Every workforce member must report a suspected incident to the group SOC within 1 hour of noticing it. (IR-6; RS.MA-02)

4.2 The group SOC must handle incidents using one group severity scale and the group playbooks, including the P08 runbook. Division severity scales are not permitted. (IR-4; IR-8; RS.MA-01)

4.3 The incident record must capture, for each notifying entity, the time of discovery and the time of each determination that starts a clock: the FedRAMP reportability evaluation, the bank 4-hour disruption determination, the breach determination under each law, the sponsor bank determination, and the materiality determination. (IR-5; RS.AN-03)

4.4 Each notifying entity owns its notices: the Cloud Hosting division for FedRAMP reports, bank notices, BAA notices, and customer notices; the Managed IT division for DIBNet reports, prime notices, DIB client notices, bank notices, and BAA notices; the Payment Processing division for sponsor bank, card network, FTC, and state licensing notices. (IR-6; RS.CO-02)

4.5 The Group General Counsel must maintain the multi-regulator notification matrix (P08), review it every quarter, and review external notices. **No legal review may delay a regulatory clock:** the FedRAMP Initial Incident Report and the DIBNet report are sent by their designated officials on time, with counsel reviewing in parallel. (IR-6; IR-8; RS.CO-02)

4.6 **SEC materiality.** Severity 1 incidents must be escalated to the disclosure committee within 24 hours of declaration. The committee must decide materiality without unreasonable delay. If material, the Form 8-K Item 1.05 filing must be made within 4 business days after the determination. (IR-6; RS.CO-03)

4.7 **Ransom payments** require board risk committee approval, counsel, the cyber insurer, and an OFAC sanctions check before any payment. (IR-4)

4.8 The group must run at least one cross-division exercise each year that includes the notification matrix, a FedRAMP PAIN rating, and a materiality decision. (IR-3; ID.IM-02)

4.9 Evidence must be preserved with chain of custody, and relevant logs placed on legal hold. For incidents involving covered defense information, images of affected systems and relevant monitoring data must be kept at least 90 days after the DIBNet report (48 CFR 252.204-7012(e)). (IR-4; AU-11; RS.AN-03)

4.10 A lessons-learned review must be completed within 30 days of recovery, and the risk registers, POA&M, and this policy updated. (IR-4; ID.IM-02)

4.11 **Automated containment.** The AI triage service and SOAR may run a containment action without analyst approval only for action classes the owning division has approved in writing. In G1, the CDE, and the CUI enclave, every containment action needs analyst approval until the division approves otherwise under POL-01 4.13. (IR-4; SI-4)

4.12 **Emergency stop.** The incident commander may suspend RMM jobs and technician sessions, HCP run-command, partner-operator access, and fleet automation for the whole group without further approval when they may be the path of an attack. (IR-4)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment (IR-3, IR-4, IR-6, IR-8) and exercise reports.

## 6. Exceptions
Exceptions follow POL-01 section 4.11. No exception may extend a legal or contractual notice deadline.

## 7. Related documents
P08 runbook and notification matrix; POL-01; `division-supplements.md`; BIA recovery priorities (P05).
