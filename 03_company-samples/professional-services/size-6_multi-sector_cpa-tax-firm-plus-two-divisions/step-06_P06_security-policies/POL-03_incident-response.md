# Incident Response Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions; adopted by CPA Partners |
| Policy ID | POL-03 |
| Owner | Group CISO, with the Group General Counsel for notifications |
| Approved by | Board risk committee |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), after every Severity 1 incident, and after each cross-division exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8, CP-2 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| Regulatory basis | 16 CFR 314.4(h) and (j); IRS Pub. 1345 security incident reporting; 17 CFR 248.30(a)(3)-(5); 45 CFR 164.410; Form 8-K Item 1.05; state breach laws (Florida worked example: Fla. Stat. 501.171) |
| Division supplements | Tax and Advisory: IRS Stakeholder Liaison and state tax agency reports, refund holds. Wealth: Regulation S-P notices and money-movement holds. Practice Cloud: customer notice register. CPA Partners: business associate notices |

## 1. Purpose
Make sure the group detects, contains, and recovers from incidents consistently across divisions, and that each regulated entity meets its own notice duties on time. With the P08 runbook, this policy is Tax and Advisory's written incident response plan under 16 CFR 314.4(h) and part of Wealth's response program under 17 CFR 248.30(a)(3).

## 2. Scope
All security incidents affecting any group system or data, including incidents at service providers, affiliates, and cloud providers that affect group data.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group SOC director | Runs detection and incident handling 24x7; incident commander for Severity 1 and 2 incidents in shared services |
| Group CISO (Qualified Individual) | Declares Severity 1; briefs the board risk committee and the Tax and Advisory board of managers |
| Group General Counsel | Owns the combined notification matrix; approves every external notice |
| Chief Tax Officer | Makes the IRS and state tax agency reports for Tax and Advisory |
| Wealth Chief Compliance Officer | Makes Wealth's Regulation S-P notice determinations |
| Practice Cloud trust and assurance director | Makes customer notices under contracts and state third-party agent laws |
| CPA Partners risk and quality partner | Makes business associate notices to health care clients |
| Disclosure committee | Decides materiality for Form 8-K Item 1.05 |
| Division incident liaisons | Bring division facts and regulator contacts |

## 4. Policy statements
4.1 Every workforce member must report a suspected incident to the group SOC within 1 hour of noticing it, including any MFA prompt they did not start and any request to change refund, payroll, or transfer bank details that they cannot verify. (IR-6; RS.MA-02; 314.4(h)(2))

4.2 The group SOC must handle incidents using one group severity scale and the group playbooks, including the P08 runbook. Division scales are not permitted. (IR-4; IR-8; RS.MA-01)

4.3 **Record the dates that start each clock.** The incident log must record, for each regulated entity: the **discovery** date (first day the event is known to any employee, officer, or other agent other than the attacker, 16 CFR 314.4(j)(2)); the **confirmation** date (IRS Pub. 1345 next-business-day report); the date Wealth **becomes aware** of unauthorized access (248.30(a)(4)(iii)); the **determination** date under state law (Fla. Stat. 501.171); and, for CPA Partners, the HIPAA discovery date (164.410(a)(2)). Because the group SOC serves every division, the date the SOC knows is treated as the date each affected entity knows, unless counsel documents otherwise. (IR-5; RS.AN-03)

4.4 Each regulated entity makes its own notice decision: Tax and Advisory (FTC, IRS, state tax agencies, states), Wealth (Regulation S-P), Practice Cloud (customers), CPA Partners (covered entities). A determination that notice is not required must be documented with its basis. (IR-6; RS.CO-02; 248.30(a)(4)(i); 275.204-2(a)(25))

4.5 The Group General Counsel must maintain the combined notification matrix (P08) and review it every quarter. Every external notice must be approved by counsel before it is sent. (IR-6; IR-8; RS.CO-02; 314.4(h)(4))

4.6 **Affiliate notices.** A group entity that holds or processes another entity's regulated data must notify that entity on the incident bridge as soon as it is aware, and in any case within the shortest contract or regulatory period: 72 hours for Wealth customer information systems (248.30(a)(5)(i)(B)); 24 or 72 hours for Practice Cloud customers by contract. (IR-6; RS.CO-02)

4.7 **SEC materiality.** Severity 1 incidents must be escalated to the disclosure committee within 24 hours of declaration. The committee must decide materiality without unreasonable delay. If material, the Form 8-K Item 1.05 filing must be made within 4 business days after the determination. (IR-6; RS.CO-03)

4.8 **Money holds.** When an incident may affect refunds, payroll, or client transfers, the affected division must hold pending bank-detail changes, return releases, and transfers until they are verified by call-back to a number of record. (IR-4; RS.MI-01)

4.9 **Extortion payments** require board risk committee approval, counsel, the cyber insurer, and an OFAC sanctions check before any payment. (IR-4)

4.10 The group must run at least one cross-division exercise each year that includes the combined notification matrix and a materiality decision, before the filing season. (IR-3; ID.IM-02; 314.4(h)(7))

4.11 Evidence must be preserved with chain of custody. Logs relevant to an incident must be placed on legal hold. (IR-4; RS.AN-03)

4.12 A lessons-learned review must be completed within 30 days of recovery, and the risk registers, POA&M, and this policy updated. The Qualified Individual's next report to the Tax and Advisory board of managers must cover each Severity 1 or 2 incident affecting Tax and Advisory. (IR-4; ID.IM-02; 314.4(h)(5), (h)(7), (i)(2))

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.8. Compliance is checked through the P07 assessment (IR-3, IR-4, IR-6, IR-8) and exercise reports.

## 6. Exceptions
Exceptions follow POL-01 section 4.11. No exception may extend a legal or contractual notice deadline.

## 7. Related documents
P08 runbook and notification matrix; POL-01; `division-supplements.md`; BIA recovery priorities (P05).
