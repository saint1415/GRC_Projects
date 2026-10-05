# Incident Response Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-03 |
| Owner | Group CISO, with the Group General Counsel for notifications |
| Approved by | Board safety, security, and risk committee |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), after every Severity 1 incident, and after each cross-division exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8, CP-2 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RS.MI-01, RC.RP-01, ID.IM-02 |
| TSA and other | SD 1580-21-01E II.C, II.D; SD 1580/82-2022-01E III.D.4; 49 CFR 1570.203; 49 CFR 1520.9(c); 49 CFR 236.1033(f); FAR 52.204-25(d) and 52.204-23(c); Form 8-K Item 1.05; state breach laws |
| Division supplements | Freight Railroad: CISA and TSOC reports, manual dispatch, PTC failure procedures, RSSM location fallback. Transload and Wholesale: FAR reports, hazmat loading stop. Real Estate: tenant notices and building life safety |

## 1. Purpose
Make sure the group detects, contains, and recovers from incidents consistently across divisions, keeps trains, terminals, and buildings safe while it does, and meets every notice duty on time.

## 2. Scope
All security incidents affecting any group IT or OT system or data, including incidents at vendors and cloud providers that affect group operations or data.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group SOC Director | Runs detection and incident handling 24x7; incident commander for Severity 1 and 2 incidents in shared services |
| Group CISO | Declares Severity 1; primary TSA Cybersecurity Coordinator; briefs the board committee |
| Director, Network Operations Center | Decides on manual dispatch and IT/OT isolation for rail operations |
| Vice President, Rail Security | TSOC reports under 1570.203; RSSM location requests; SSI disclosure reports |
| Group General Counsel | Owns the notification matrix; approves every external notice |
| Disclosure committee | Decides materiality for Form 8-K Item 1.05 |
| Division incident liaisons | Bring division facts and division regulator and customer contacts |

## 4. Policy statements
4.1 Every workforce member must report a suspected incident to the group SOC within 1 hour of noticing it. NOC and terminal staff report through their supervisors and the SOC duty line. (IR-6; RS.MA-02)

4.2 The group SOC must handle incidents using one group severity scale and the group playbooks, including the P08 runbook. Division scales are not permitted. (IR-4; IR-8; RS.MA-01)

4.3 **Safety first.** The Director, NOC may order manual dispatch and isolation of the NOC operations zone from the corporate network at any time an IT incident could affect train movement, without waiting for the investigation (SD 1580/82-2022-01E III.D.4; SD 1580-21-01E II.D.1.c). Terminal managers stop hazmat loading when rack controls or shipping paper data may be affected. (IR-4; RS.MI-01)

4.4 **TSA and CISA.** For a Covered Railroad, report to CISA within 24 hours of identification by default, and never later than the 72 hours the directive allows, stating that the report is made under SD 1580-21-01E, so it also satisfies 49 CFR 1570.203. For any of the 72 railroads, a cyber attack is reportable to TSA within 24 hours (1570.203; Appendix A). The group also follows TSA's recommendation to call the TSOC within 12 hours of discovering a significant cybersecurity incident (IC Surface-2025-01). (IR-6; RS.CO-02)

4.5 The Group General Counsel must maintain the multi-regulator notification matrix (P08) and review it every quarter. Every external notice must be approved by counsel; TSA-facing reports are treated as SSI. (IR-6; IR-8; RS.CO-02)

4.6 **SEC materiality.** Severity 1 incidents must be escalated to the disclosure committee within 24 hours of declaration. The committee must decide materiality without unreasonable delay. If material, the Form 8-K Item 1.05 filing must be made within 4 business days after the determination. (IR-6; RS.CO-03)

4.7 **Ransom payments** require approval of the board safety, security, and risk committee, counsel, the cyber insurer, and an OFAC sanctions check before any payment. (IR-4)

4.8 The group must run at least one cross-division exercise each year that includes the notification matrix and a materiality decision. Each Covered Railroad's incident response plan must be exercised at least annually, testing at least two of its objectives with the named positions taking part (SD 1580-21-01E II.D.3). (IR-3; ID.IM-02)

4.9 Evidence must be preserved with chain of custody. Logs relevant to an incident must be placed on legal hold. (IR-4; RS.AN-03)

4.10 A lessons-learned review must be completed within 30 days of recovery, and the risk registers, POA&M, CIP (by amendment request if needed), and this policy updated. (IR-4; ID.IM-02)

4.11 When SSI is found to have been released to unauthorized persons, the Vice President, Rail Security must promptly inform TSA (49 CFR 1520.9(c)). (IR-6; RS.CO-02)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment (IR-3, IR-6, IR-8) and exercise reports.

## 6. Exceptions
Exceptions follow POL-01 section 4.12. No exception may extend a legal or directive deadline.

## 7. Related documents
P08 runbook and notification matrix; POL-01; `division-supplements.md`; BIA recovery priorities (P05); the Covered Railroads' Cybersecurity Incident Response Plan (SSI).
