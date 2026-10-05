# Incident Response Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-03 |
| Owner | Group CISO, with the Group General Counsel for notifications |
| Approved by | Board risk committee, 2026-09-17 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), after every Severity 1 incident, and after each cross-division exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8, CP-2 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| Regulatory drivers | C-COMMUNICATIONS-R01 (47 CFR 64.2011); C-COMMUNICATIONS-R02 (47 CFR 4.9); C-COMMUNICATIONS-R03 (47 CFR 1.20003(c)); C-COMMUNICATIONS-R06 (Form 8-K Item 1.05); 47 CFR 17.48; FAR 52.204-25(d) and 52.204-23(c); state breach laws; MNO customer contracts |
| Division supplements | Carrier: CPNI breach procedure; NOC outage and PSAP procedures; lawful-intercept compromise procedure. Engineering: customer notice register. Tower: FAA lighting outage procedure |

## 1. Purpose
Make sure the group detects, contains, and recovers from incidents consistently across divisions, protects 911 and aviation safety while it does so, and meets every regulator, customer, and investor notice on time.

## 2. Scope
All security incidents affecting any group system, network, device fleet, or data, including incidents at vendors and cloud providers that affect group data or services, and incidents in customer networks reached through Engineering's managed services.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group SOC director | Runs detection and incident handling 24x7; incident commander for Severity 1 and 2 incidents in shared services |
| Group CISO | Declares Severity 1; briefs the board risk committee |
| Group General Counsel | Owns the notification matrix; approves every external notice |
| Carrier CPNI compliance officer | Makes the reasonable determination of a CPNI breach with counsel and files the law enforcement notice |
| Carrier NOC director | Service-impact decisions; Part 4 and PSAP notices |
| CALEA senior officer | Lawful-intercept compromise decisions and reports |
| Engineering MNO general manager | Customer outage and incident notices |
| Tower site operations director | FAA lighting outage reports and the daily observation fallback |
| Disclosure committee | Decides materiality for Form 8-K Item 1.05 |

## 4. Policy statements
4.1 Every workforce member must report a suspected incident to the group SOC within 1 hour of noticing it. (IR-6; RS.MA-02)

4.2 The group SOC must handle incidents using one group severity scale and the group playbooks, including the P08 runbook. Division scales are not permitted. (IR-4; IR-8; RS.MA-01)

4.3 **Service-impact gate.** Before any containment action that could affect calling, 911, broadband, managed customer networks, or tower lighting monitoring (for example, isolating an SBC, a gateway, or the service assurance platform), the incident commander must consult the Carrier NOC and, for the platform, the Tower Alarm Monitoring Center. If the action causes or may cause a reportable outage or loss of lighting alarms, the Part 4, PSAP, and FAA steps in the matrix start at once. (IR-4; CP-2; RS.MI-01; 47 CFR 4.9; 17.47(a); 17.48)

4.4 The incident log must record the discovery time and, for CPNI, the date and basis of the reasonable determination of a breach. The determination must not wait for forensics to finish. (IR-5; RS.AN-03; 47 CFR 64.2011(b))

4.5 **CPNI breaches.** The Carrier must notify the USSS and FBI through the FCC reporting facility as soon as practicable and within 7 business days after reasonable determination. No division may notify Carrier customers or disclose the breach publicly until 7 full business days have passed after that notice, unless the investigating agency agrees or directs otherwise. (IR-6; RS.CO-02; 47 CFR 64.2011(a)-(c))

4.6 The Group General Counsel must maintain the multi-regulator notification matrix (P08) and review it every quarter. Every external notice must be approved by counsel before it is sent. (IR-6; IR-8; RS.CO-02)

4.7 **SEC materiality.** Severity 1 incidents must be escalated to the disclosure committee within 24 hours of declaration. The committee must decide materiality without unreasonable delay. If material, the Form 8-K Item 1.05 filing must be made within 4 business days after the determination, or within the delay that Item 1.05(d) allows during the CPNI hold, with the required correspondence to the SEC. (IR-6; RS.CO-03)

4.8 **Lawful intercept.** Any suspected compromise of SYS-C8, of an interception, or of call-identifying information must be escalated to the CALEA senior officer at once and reported to the affected law enforcement agencies within a reasonable time after discovery. Forensic staff must not view intercept content. (IR-6; 47 CFR 1.20003(c))

4.9 **Engineering customers.** Engineering must notify each affected MNO customer within its contract term (30 minutes for a possibly reportable outage; 24 or 72 hours for a security incident), using the customer notice register. (IR-6; RS.CO-02)

4.10 **Ransom payments** require board risk committee approval, counsel, the cyber insurer, and an OFAC sanctions check before any payment. (IR-4)

4.11 The group must run at least one cross-division exercise each year that includes the notification matrix, the service-impact gate, and a materiality decision. (IR-3; ID.IM-02)

4.12 Evidence must be preserved with chain of custody, and logs placed on legal hold. A lessons-learned review must be completed within 30 days of recovery, and the risk registers, POA&M, and this policy updated. (IR-4; RS.AN-03; ID.IM-02)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment (IR-4, IR-6, IR-8) and exercise reports.

## 6. Exceptions
Exceptions follow POL-01 section 4.10. No exception may extend a legal or contractual notice deadline.

## 7. Related documents
P08 runbook and notification matrix; POL-01; `division-supplements.md`; BIA recovery priorities (P05).
