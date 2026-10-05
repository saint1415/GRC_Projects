# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Owner | IT Security Manager |
| Approved by | Site Vice President |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2022 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes or significant incidents |
| Implements (SP 800-53 Rev. 5) | IR-8, IR-6, IR-5, IR-4, CP-2, CP-4, CP-10, IR-3, AU-2, SI-4 |
| CSF 2.0 | DE.CM-01, ID.IM-04, RC.RP-01, RS.AN-03, RS.CO-02, RS.CO-03, RS.MA-01, RS.MA-02, RS.MA-03 |
| Regulatory drivers | C-NUCLEAR-R01, C-NUCLEAR-S06, C-NUCLEAR-R03, C-NUCLEAR-S04, C-NUCLEAR-R04 |
| Supporting standards | STD-02 Logging and monitoring; STD-07 Contingency and recovery (see `standards-index.md`) |

## 1. Purpose
Make sure business network and cloud incidents are detected, contained, escalated to the CST and the Shift Manager when they could touch 73.54 scope, reported on time to every regulator, and recovered in the order the BIA sets.

## 2. Scope
All security incidents and suspected incidents affecting business systems, cloud services, business data, or vendors that hold company data. It works with the CSP incident response procedures, which govern CDAs, and the NERC low-impact Cyber Security Incident response plan for the dispatch network.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| IT Security Manager | Incident commander for business network incidents; coordinates the MSSP and forensics |
| Cyber Security Program Manager and CST | Assess any link to 73.54 scope; lead CDA response under the CSP |
| Shift Manager | Decides NRC reportability under 50.72 and 73.77 and makes ENS notifications |
| Site Vice President | Chairs the crisis management team (CMT) |
| General Counsel | Breach and notification decisions with outside counsel; decision log |
| Compliance and GRC Lead | NERC E-ISAC determination with the CIP Senior Manager |
| Regulatory Affairs Manager | Written reports and CAP entries |
| MSSP | 24x7 detection, first containment, escalation within 30 minutes for high severity |
| All workforce | Report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain integrated runbooks for its most likely and most harmful incidents: a business network attack with an attempted pivot toward CDAs, and insider compromise of SRI or SGI (P08). They replace the separate 2023 IT plan. (IR-8; RS.MA-01; C-NUCLEAR-R01 (73.54(e)(2)))
4.2 Workforce members must report suspected incidents immediately (within 1 hour at most) to the service desk security line or the MSSP. Good-faith reporting is never sanctioned. (IR-6; RS.MA-02; C-NUCLEAR-S06)
4.3 Every incident must be logged with the **date and time of discovery** and tracked to closure. (IR-5; RS.MA-02; C-NUCLEAR-R03 (73.77(a)))
4.4 **Escalation to the CST and the Shift Manager.** The incident commander must call the Cyber Security Program Manager (or the CST on-call) and the Shift Manager immediately when an incident involves: activity aimed at boundary addresses or the receive server; vendor paths or portable media used with CDAs; an insider with electronic access in 73.56 scope; EP support systems; or reconnaissance aimed at the Station. The Shift Manager makes the 73.77 reportability decision. (IR-4; IR-6; RS.CO-02; RS.AN-03; C-NUCLEAR-R03 (73.77(a)(1)-(3)))
4.5 **No outside report without the decision point.** No one may report a cyber event to law enforcement, CISA, the E-ISAC, or any other agency until the Shift Manager has been told, because a report to another agency can start a 4-hour NRC notification clock (73.77(a)(2)(iii)). (IR-6; RS.CO-03; C-NUCLEAR-R03 (73.77(a)(2)(iii)))
4.6 If the corrective action program is unavailable, 73.77(b) entries are recorded on numbered paper CAP intake forms within 24 hours and entered when CAP is restored. (IR-5; CP-2; RS.MA-02; C-NUCLEAR-R03 (73.77(b)))
4.7 A severity 1 incident must activate the crisis management team within 2 hours. (IR-4; RS.MA-01; C-NUCLEAR-S06)
4.8 General Counsel keeps the notification decision log: Florida breach determination and 30-day clock, NRC, NERC, contract, and insurer notices. (IR-6; RS.CO-02; C-NUCLEAR-S04 (501.171(3)-(4)))
4.9 Any ransom payment needs the CEO, counsel, the insurer, an OFAC sanctions check, and a report to law enforcement. The default position is not to pay while backups are intact. (IR-4; RS.MA-03; C-NUCLEAR-S06)
4.10 Business systems are restored in the order set by the BIA (P05), and recovery of the WMS and CAP/EDMS must be tested at least annually and before each refueling outage. (CP-2; CP-4; CP-10; RC.RP-01; C-NUCLEAR-S06)
4.11 The incident response plans must be exercised at least annually with IT, the CST, the Shift Manager, and the MSSP together; the NERC low-impact plan at least every 36 calendar months. (IR-3; ID.IM-04; C-NUCLEAR-R01 (RG 5.71 C.8.3); C-NUCLEAR-R04 (CIP-003-9 Att. 1 Sec. 4.5))
4.12 Logs needed to investigate incidents must be collected from all PBN-WMS components, including WMS, EDMS, CAP, and the receive server (STD-02). (AU-2; SI-4; DE.CM-01; C-NUCLEAR-R01 (73.54(e)(2)(i)))

## 5. Compliance and enforcement
Compliance is checked through the annual independent assessment (P07), quarterly access reviews, the metrics reported to the audit committee, and, for anything in 73.54 scope, the 73.55(m) program review. Violations are handled under POL-01 4.13.

## 6. Exceptions
Exceptions follow POL-01 4.8: written, risk-rated, approved by the right authority under POL-01 4.5, recorded in the risk register, and limited to 12 months. No exception may permit a known regulatory noncompliance.

## 7. Related documents
POL-01; P08 runbooks and notification matrix; STD-02 Logging and monitoring standard; STD-07 Contingency and recovery standard; CSP incident response procedures; NERC low-impact Cyber Security Incident response plan
