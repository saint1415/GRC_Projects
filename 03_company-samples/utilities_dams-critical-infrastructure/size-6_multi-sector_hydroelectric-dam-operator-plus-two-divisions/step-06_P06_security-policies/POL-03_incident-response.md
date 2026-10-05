# Incident Response Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-03 |
| Owner | Group CISO, with the General Counsel for notifications |
| Approved by | Board safety, risk, and reliability committee, 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), after every Severity 1 incident, and after each cross-division exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8, CP-2 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| Regulatory drivers | C-DAMS-R02 (18 CFR 12.10(a)); C-DAMS-R03 (CIP-008-6 R1 to R4; CIP-003-9 Att. 1 Sec. 4); C-DAMS-R01 (Rev. 3A 3.2, 4.2, 7.4.1; Form 3 Q25 to Q28); NERC EOP-004-4; Form DOE-417; N23-R03 (252.204-7012(c) to (e)); Form 8-K Item 1.05; state breach laws |
| Division supplements | Hydro: safe-state first, EAP link, FERC and NERC reports. Constructors: DFARS reports and preservation. Engineering: DSMS client notices |

## 1. Purpose
Make sure the group detects, contains, and recovers from incidents consistently across divisions, keeps every dam under control while it does so, and meets every regulator's and client's clock on time.

## 2. Scope
All security incidents affecting any group system, OT or IT, or data, including incidents at vendors, affiliates, and cloud providers that affect group systems or data.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group SOC director | Runs detection and incident handling 24x7; incident commander for IT incidents in shared services |
| HOC shift supervisor | Incident commander on shift for any incident affecting Hydro OT, until the Senior Vice President, Hydro Operations or a delegate takes over. Authority to put any plant or gate into local control without further approval |
| Group CISO | Declares Severity 1; briefs the board committee |
| General Counsel | Owns the notification matrix; approves every external notice except safety reports |
| Chief Dam Safety Engineer | Decides EAP activation and makes 18 CFR 12.10 reports |
| NERC Compliance Director | Makes CIP-008 and CIP-003 Reportable Cyber Security Incident and attempt determinations with the OT security team, and EOP-004 and DOE-417 reports |
| Federal Programs Compliance Director | Makes DFARS 252.204-7012 reports |
| DSMS General Manager | Makes DSMS client notices |
| Disclosure committee | Decides materiality for Form 8-K Item 1.05 |

## 4. Policy statements
4.1 Every workforce member must report a suspected incident to the group SOC within 1 hour of noticing it. HOC and plant staff report OT events to the HOC shift supervisor at once. (IR-6; RS.MA-02)

4.2 **Safety first.** In any incident that could affect gates or units, operators must first put the affected equipment into a known safe state under local control. Evidence collection must never delay that step or an EAP action. (IR-4; CP-2; RS.MA-01)

4.3 The SOC must use one group severity scale and the group playbooks, including the P08 runbook. Any incident that touches more than one division is Severity 1 or 2 and has a single incident commander named at declaration. (IR-4; IR-8; RS.MA-01)

4.4 The incident log must record, for each regulator and client, when its clock starts: discovery (18 CFR 12.10; DFARS 252.204-7012), determination (CIP-008-6 R4; CIP-003-9 Att. 1 Sec. 4.2; Form 8-K Item 1.05; state breach laws), or recognition (EOP-004-4). (IR-5; RS.AN-03)

4.5 The General Counsel must maintain the multi-regulator notification matrix (P08), review it every quarter, and keep a printed copy in each HOC and command center. Counsel approves every external notice, except that safety reports to the FERC Regional Engineer, EAP notifications, and law enforcement calls must not wait for counsel. (IR-6; IR-8; RS.CO-02)

4.6 **SEC materiality.** Severity 1 incidents must be escalated to the disclosure committee within 24 hours of declaration. The committee must decide materiality without unreasonable delay. If material, the Form 8-K Item 1.05 filing must be made within 4 business days after the determination. (IR-6; RS.CO-03)

4.7 **Ransom payments** require board committee approval, counsel, the cyber insurer, and an OFAC sanctions check before any payment. (IR-4)

4.8 The group must run at least one cross-division exercise each year that includes OT, the notification matrix, and a materiality decision. The CIP-008 plan must be tested at least every 15 calendar months and the low impact plan at least every 36 calendar months. (IR-3; ID.IM-02; CIP-008-6 R2; CIP-003-9 Att. 1 Sec. 4.5)

4.9 Evidence must be preserved with chain of custody. Images and monitoring data for incidents involving covered defense information must be kept at least 90 days from the DoD report (252.204-7012(e)). OT evidence is BCSI or CEII and must be stored in the restricted library. (IR-4; RS.AN-03)

4.10 A lessons-learned review must be completed within 30 days of recovery, and the risk registers, POA&M, Security Plans, and this policy updated. CIP plans must be updated within the deadlines in CIP-008-6 R3 and CIP-009-6 R3. (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment (IR-3, IR-4, IR-6, IR-8), CIP evidence reviews, and exercise reports.

## 6. Exceptions
Exceptions follow POL-01 section 4.11. No exception may extend a legal or contractual notice deadline.

## 7. Related documents
P08 runbook and notification matrix; POL-01; `division-supplements.md`; BIA recovery priorities (P05); EAPs; CIP-008 and CIP-009 plans; FPE incident plan.
