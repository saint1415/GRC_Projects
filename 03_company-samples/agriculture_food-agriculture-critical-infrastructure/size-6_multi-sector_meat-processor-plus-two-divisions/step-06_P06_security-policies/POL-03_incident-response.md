# Incident Response Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-03 |
| Owner | Group CISO, with the Group General Counsel for notifications and the Group Chief Food Safety and Quality Officer for food safety decisions |
| Approved by | Board risk committee |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), after every Severity 1 incident, and after each cross-division exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8, CP-2, CP-10 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| Regulatory drivers | 9 CFR 417.3(b), 418.2; 21 U.S.C. 350f(d); 21 CFR 117.206(a)(3), 1.908(a)(6), 121.145, 121.157(b)(3); state breach laws; PCI DSS Req. 12.10; Form 8-K Item 1.05 |
| Division supplements | Meat Processing: product hold and FSIS steps; Food Distribution: DC and in-transit temperature decisions, 3PL customer notices; Grocery Retail: payment card incident steps |

## 1. Purpose
Make sure the group detects, contains, and recovers from incidents consistently across divisions, that food safety decisions come first when an incident touches production, storage, or transport, and that every division meets its own notice duties on time.

## 2. Scope
All security incidents affecting any group IT or OT system or data, including incidents at integrators, contractors, cloud and SaaS providers, and payment service providers that affect group systems, product, or data.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group SOC director | Runs detection and incident handling 24x7; incident commander for Severity 1 and 2 incidents in shared services |
| Group CISO | Declares Severity 1; briefs the board risk committee |
| Group Chief Food Safety and Quality Officer | Leads product decisions across divisions; with plant FSQA managers, decides FSIS and FDA notices |
| Group General Counsel | Owns the notification matrix; approves every external notice |
| Division incident liaisons | Bring plant, DC, or store facts and division regulator and customer contacts |
| Grocery Retail payments security manager | Runs payment card incident steps with the acquirer |
| Disclosure committee | Decides materiality for Form 8-K Item 1.05 |

## 4. Policy statements
4.1 Every workforce member must report a suspected incident to the group SOC within 1 hour of noticing it. Plant, DC, and store staff may report through their supervisor or the plant control room. (IR-6; RS.MA-02)

4.2 The group SOC must handle incidents using one group severity scale and the group playbooks, including the P08 runbook. Division severity scales are not permitted. (IR-4; IR-8; RS.MA-01)

4.3 **Food safety first.** When an incident affects a control system, recipe system, temperature monitoring, or food safety records, the SOC must bring in the plant or DC FSQA lead at once. Affected product must be held until FSQA evaluates it (9 CFR 417.3(b); 21 CFR 117.206(a)(3); 21 CFR 1.908(a)(6)). Product decisions do not wait for IT recovery. (IR-4; RS.MA-01)

4.4 The incident log must record the time of discovery, the last trusted monitoring record for each affected site, and the date each food safety or breach determination was made, because the FSIS, FDA, and state clocks run from determination. (IR-5; RS.AN-03)

4.5 The Group General Counsel must maintain the multi-regulator notification matrix (P08) and review it every quarter. Every external notice must be approved by counsel before it is sent; FSIS and FDA notices are made by FSQA with counsel informed. (IR-6; IR-8; RS.CO-02)

4.6 **SEC materiality.** Severity 1 incidents must be escalated to the disclosure committee within 24 hours of declaration. The committee must decide materiality without unreasonable delay. If material, the Form 8-K Item 1.05 filing must be made within 4 business days after the determination. (IR-6; RS.CO-03)

4.7 **Ransom payments** require board risk committee approval, counsel, the cyber insurer, and an OFAC sanctions check before any payment. Payment never releases held product or removes any notice duty. (IR-4)

4.8 The group must run at least one cross-division exercise each year that includes a product hold decision, an FSIS notice decision, a payment card decision, and a materiality decision. (IR-3; ID.IM-02)

4.9 Evidence must be preserved with chain of custody. Logs relevant to an incident must be placed on legal hold. (IR-4; RS.AN-03)

4.10 A lessons-learned review must be completed within 30 days of recovery, and the risk registers, POA&M, HACCP plans (if a deviation was unforeseen), the Plant 6 food defense plan (if tampering was found or suspected), and this policy updated. (IR-4; ID.IM-02; 21 CFR 121.157(b)(3))

4.11 **Restart validation.** No line restarts after an OT incident until PLC programs and formulations are verified against the repository and signed masters, FSQA signs a restart checklist, and the first batch is verified against critical limits. (CP-10; RC.RP-01)

4.12 **Payment card incidents** must follow the Grocery Retail supplement, including immediate containment of the CDE, preservation of evidence for a forensic investigator if the acquirer requires one, and notice to the acquirer as the contract requires. (IR-4; PCI DSS Req. 12.10)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment (IR-3, IR-4, IR-6, IR-8) and exercise reports.

## 6. Exceptions
Exceptions follow POL-01 section 4.10. No exception may extend a legal notice deadline or allow held product to ship.

## 7. Related documents
P08 runbook and notification matrix; POL-01; `division-supplements.md`; BIA recovery priorities (P05); plant HACCP plans and recall procedures.
