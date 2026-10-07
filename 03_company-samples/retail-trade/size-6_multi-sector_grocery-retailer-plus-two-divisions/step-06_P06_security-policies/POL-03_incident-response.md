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
| Regulatory drivers | PCI DSS v4.0.1 Req. 12.10 (N44-45-R01); 16 CFR 314.4(h), (j) (N44-45-R03); 12 CFR 1026.12(b), 1026.13; Form 8-K Item 1.05; state breach laws (Florida worked example: Fla. Stat. 501.171) |
| Division supplements | Grocery Retail: acquirer notice and card brand forensics; EBT skimming. Grocery Wholesale: independent grocer notices; FDA record requests. Financial Services: FTC notice, card reissue, and Reg Z disputes |

## 1. Purpose
Make sure the group detects, contains, and recovers from incidents the same way in every division, and that each merchant account, the financial institution, and the public company meets its own notice duties on time.

## 2. Scope
All security incidents affecting any group system or data, including incidents at service providers and cloud providers that affect group data, and incidents on any payment page.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group SOC director | Runs detection and incident handling 24x7; incident commander for Severity 1 and 2 incidents in shared services |
| Group CISO | Declares Severity 1; briefs the board risk committee |
| Group General Counsel | Owns the notification matrix; approves every external notice |
| Grocery Retail CISO | Acquirer notice and card brand forensic process for the retail merchant |
| Financial Services CISO (Qualified Individual) | Decides whether a notification event occurred and owns the FTC notice |
| Grocery Wholesale security and compliance lead | Independent grocer notices; acquirer notice for the wholesale merchant account |
| Disclosure committee | Decides materiality for Form 8-K Item 1.05 |
| Division incident liaisons | Bring division facts, operational impact, and regulator contacts |

## 4. Policy statements
4.1 Every workforce member must report a suspected incident to the group SOC within 1 hour of noticing it. Store staff must report suspected PIN pad tampering immediately and take the device out of use. (IR-6; RS.MA-02)

4.2 The group SOC must handle incidents using one group severity scale and the group playbooks, including the P08 runbook. Division scales are not permitted. (IR-4; IR-8; RS.MA-01; PCI DSS 12.10.1)

4.3 The incident log must record, for each notice duty, the time its clock starts: suspicion of a card data compromise (merchant agreements), discovery of a notification event (16 CFR 314.4(j)(2): known to any employee, officer, or other agent), and determination of a breach under each state law. (IR-5; RS.AN-03)

4.4 Payment page alerts must reach the SOC and be triaged within 1 hour. A confirmed unauthorized change on a payment page is a Severity 1 incident. (IR-4; SI-4; PCI DSS 11.6.1, 12.10.5)

4.5 The Group General Counsel must maintain the multi-regulator notification matrix (P08) and review it every quarter. Every external notice must be approved by counsel before it is sent. (IR-6; IR-8; RS.CO-02)

4.6 **Financial Services notices.** The Qualified Individual must decide promptly whether a notification event occurred and, if at least 500 consumers are involved, the FTC must be notified as soon as possible and no later than 30 days after discovery. Compromised Rewards Cards must be blocked and reissued, and unauthorized charges handled as billing errors with cardholder liability no greater than the cardholder agreement allows. (IR-6; RS.CO-02; 16 CFR 314.4(j); 12 CFR 1026.12(b), 1026.13)

4.7 **SEC materiality.** Severity 1 incidents must be escalated to the disclosure committee within 24 hours of declaration. The committee must decide materiality without unreasonable delay. If material, the Form 8-K Item 1.05 filing must be made within 4 business days after the determination. (IR-6; RS.CO-03)

4.8 **Ransom and extortion payments** require board risk committee approval, counsel, the cyber insurer, and an OFAC sanctions check before any payment. (IR-4)

4.9 The group must run at least one cross-division exercise each year that includes the notification matrix and a materiality decision, and test the plan at least every 12 months. (IR-3; ID.IM-02; PCI DSS 12.10.2)

4.10 Evidence must be preserved with chain of custody. Logs relevant to an incident must be placed on legal hold. Where the acquirer or a card brand requires a PCI Forensic Investigator, the group must engage one. (IR-4; RS.AN-03)

4.11 A lessons-learned review must be completed within 30 days of recovery, and the risk registers, POA&M, and this policy updated. (IR-4; ID.IM-02; 16 CFR 314.4(h)(7))

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment (IR-3, IR-4, IR-6, IR-8), exercise reports, and the QSA ROC.

## 6. Exceptions
Exceptions follow POL-01 section 4.10. No exception may extend a legal or contractual notice deadline.

## 7. Related documents
P08 runbook and notification matrix; POL-01; `division-supplements.md`; BIA recovery priorities (P05); Financial Services written information security program.
