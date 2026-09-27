# Incident Response Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-03 |
| Owner | Group CISO, with the Group General Counsel for notifications |
| Approved by | Holding company board risk committee; adopted by the bank board risk committee (2026-09-10) |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), after every Severity 1 incident, and after each cross-division exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8, CP-2 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| Regulatory basis | 12 CFR 30 App. B III.C.1.g and Supplement A; 12 CFR 225 App. F III.C.1.g; 12 CFR 53.3, 53.4, 225.302, 225.303, 304.24; 12 CFR 21.11 and 225.4(f); Form 8-K Item 1.05; state breach notification laws |
| Division supplements | Banking: wire recall and fraud operations. Financial Software: client bank notices and the 4-hour determination. Commercial Real Estate: loan funding fraud and guarantor notices |

## 1. Purpose
Make sure the group detects, contains, and recovers from incidents consistently across divisions, and that the bank, the holding company, the Financial Software division as a bank service provider, and the public company each meet their own notice duties on time.

## 2. Scope
All security incidents and payment frauds affecting any group system, data, or customer, including incidents at service providers and affiliates that affect group data or services.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group SOC director | Runs detection and incident handling 24x7; incident commander for Severity 1 and 2 incidents in shared services |
| Group CISO | Declares Severity 1; briefs both board risk committees |
| Group General Counsel | Owns the notification matrix; approves every external notice |
| Bank determination officials (Group CISO with the bank's chief operations officer) | Decide whether an incident is a bank notification incident (12 CFR 53.2(b)(7)) |
| Holding company determination officials (Group General Counsel with the Group Chief Risk Officer) | Decide whether an incident is a holding company notification incident (225.301(b)(7)) |
| Client risk and assurance director (Financial Software) | Makes the 4-hour determination and bank service provider notices to client banks |
| BSA/AML Officers | SARs (bank: 12 CFR 21.11; nonbank subsidiaries: 12 CFR 225.4(f)) |
| Disclosure committee | Decides materiality for Form 8-K Item 1.05 |
| Division incident liaisons | Bring division facts, customer impact, and division regulator contacts |

## 4. Policy statements
4.1 Every workforce member must report a suspected payment fraud **within 15 minutes** and any other suspected incident **within 1 hour** to the group SOC. (IR-6; RS.MA-02)

4.2 The group SOC must handle incidents using one group severity scale and the group playbooks, including the P08 runbook. Division scales are not permitted. (IR-4; IR-8; RS.MA-01)

4.3 **Containment decisions that affect customers or clients.** A decision to suspend a customer-facing function (for example, business wire initiation on the platform) must be made by the incident commander with the Group CISO, and the time must be recorded, because it can start notice clocks for the bank (53.3), the holding company (225.302), and client banks (53.4). (IR-4; RS.MI-01)

4.4 **Bank and holding company determinations.** As soon as possible after a computer-security incident is identified, the bank determination officials must decide whether it is a notification incident, and the holding company determination officials must decide separately for the holding company, each using the P08 criteria, including incidents that start in an affiliate. Each decision and its time is recorded. If yes, the OCC must receive notice no later than 36 hours after the bank's determination (53.3), and the Federal Reserve no later than 36 hours after the holding company's (225.302). (IR-6; RS.CO-02)

4.5 **Bank service provider notices.** The Financial Software division must decide, at the 4-hour mark of any disruption or degradation of covered services, whether 12 CFR 53.4, 225.303, or 304.24 applies, and if so notify each affected client bank's designated point of contact (or its CEO and CIO) as soon as possible. The division must hold a designated contact for every client bank. Contract notice terms that are shorter apply as well. (IR-6; RS.CO-02)

4.6 **Customer information.** When unauthorized access to sensitive customer information is suspected, the bank must notify the OCC as soon as possible and investigate misuse; the Group Chief Privacy Officer decides customer notices under Supplement A and each state's breach law, using the P08 matrix. Counsel confirms each notice. (IR-6; RS.CO-03)

4.7 **SEC materiality.** Severity 1 incidents must be escalated to the disclosure committee within 24 hours of declaration. The committee must decide materiality without unreasonable delay. If material, the Form 8-K Item 1.05 filing must be made within 4 business days after the determination. (IR-6; RS.CO-03)

4.8 **Fraudulent payments.** For a suspected fraudulent wire or ACH payment in any division, bank payments operations must request a recall immediately, place holds where possible, and report to the FBI through IC3. The responsible BSA/AML Officer must file any SAR within the regulatory time limits. SAR information is confidential. (IR-4; RS.MI-01)

4.9 **Ransom payments** require holding company board risk committee approval, counsel, the cyber insurer, and an OFAC sanctions check before any payment. (IR-4)

4.10 The group must run at least one cross-division exercise each year that includes the notification matrix, the bank and holding company determinations, a bank service provider notice decision, and a materiality decision. (IR-3; ID.IM-02)

4.11 Evidence must be preserved with chain of custody, and relevant logs placed on legal hold. (IR-4; RS.AN-03)

4.12 A lessons-learned review must be completed within 30 days of recovery, and the risk registers, POA&M, and this policy updated. (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.15. Compliance is checked through the P07 assessment (IR-3, IR-4, IR-6, IR-8) and exercise reports.

## 6. Exceptions
Exceptions follow POL-01 section 4.11. No exception may extend a legal notice deadline.

## 7. Related documents
P08 runbook and notification matrix; POL-01; POL-02 4.13; `division-supplements.md`; BIA recovery priorities (P05).
