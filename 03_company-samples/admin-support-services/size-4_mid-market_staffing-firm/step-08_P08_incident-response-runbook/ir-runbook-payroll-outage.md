# Incident Response Runbook: Payroll Platform Outage Before Payday

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed staffing and temporary help firm) |
| Tier / Vertical | Mid-Market / Administrative and Support and Waste Management and Remediation Services |
| Incident type | Extended outage of the payroll, billing, and back-office platform (SYS-02) in payroll week, caused by a cyberattack on the payroll vendor (for example ransomware) or a vendor failure. Variants: ATS outage that blocks time approval (section 7), and loss of the Thursday credit line draw (section 8) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); CSF GV.SC-08 (suppliers included in incident planning); NIST SP 800-34 Rev. 1 for the recovery steps |
| Policy basis | POL-03 Incident Response and Contingency Policy (4.1, 4.6, 4.7, 4.11); STD-07 Contingency and recovery; STD-03 Vendor risk management |
| Companion documents | `ir-runbook.md` (payroll and HR system breach); `notification-matrix.csv`; BIA (P05 BP-01, BP-02, BP-11, BP-12); risk register (P01 R-005, R-043) |
| Runbook owner | Director of Payroll and Billing (business lead) with the Security Manager (security lead) |
| Approved | 2026-09-22 by the Chief Operating Officer |
| Last tested | Not yet. Payroll outage tabletop scheduled 2027-02-17; first live test of the off-cycle manual payroll by 2026-12-31 (POAM-011) |

## 0. Why this runbook exists
About 3,600 associates expect about $1.45 million in pay every Friday. The payroll vendor's stated RTO is 8 hours, which meets the BIA, but a ransomware event at a payroll vendor can last days, and the firm has no tested way to pay people without the platform (P05 finding 3; P01 R-005, High). Overtime earned in a workweek must be paid on the regular payday for that period (29 CFR 778.106). A missed payday is a business crisis first: temporary workers leave within days, clients lose fill rates, and the lender and PE sponsor must be told. If the vendor was attacked, it may also be a **breach of firm data held by a third-party agent** (Fla. Stat. 501.171(6)), so the breach runbook may run in parallel.

## 1. Roles (Govern)
| Role | Primary | Backup | Responsibility |
|---|---|---|---|
| Business lead | Director of Payroll and Billing | Controller | Payroll decisions, manual payroll, associate pay continuity |
| Security lead | Security Manager | IT Director | Cut and later re-establish connections safely; assess exposure of firm data |
| CMT chair (severity 1) | Chief Operating Officer | CEO | Declares the outage severity 1; approves spending and communications |
| Finance and treasury | Chief Financial Officer | Controller | Funding the manual payroll, bank coordination, lender and sponsor updates |
| Vendor management and legal | General Counsel | Director of Compliance and Privacy | Contract rights, vendor breach notice, notices to clients and the lender |
| Business units | VP Light Industrial; VP Office and Professional; VP Healthcare Staffing; VP Managed Workforce Solutions | Branch and on-site managers | Associate and client messages; MSP supplier payments |
| Communications | Director of Marketing | Contact Center Manager | Associate texts, scripts, branch talking points |

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Payroll platform unavailable or erroring for more than 1 hour on Monday to Thursday | Payroll staff; vendor status page | Business lead opens a vendor incident; confirm with the vendor's support line |
| Vendor reports a cyberattack or suspected compromise | Vendor notice (Fla. Stat. 501.171(6) requires notice within 10 days of determination; the contract asks for 72 hours) | **Immediately** pause integration jobs and revoke the integration's payroll API credentials (step 3.1); notify the General Counsel |
| Vendor cannot confirm it will release Friday's deposits by Thursday 12:00 | Vendor account manager | Declare severity 1; start the manual payroll decision clock (section 4) |
| Pay files released but the bank rejects or delays them | Bank; payroll vendor | Controller works with the bank; treat as severity 2 |

**Severity levels:**
- **Severity 3:** outage under 4 hours on Monday or Tuesday, no data concern. The business lead manages it.
- **Severity 2:** outage expected to exceed 8 hours, any outage on Wednesday or Thursday, or any vendor cyber incident. Security lead engaged; COO informed.
- **Severity 1:** Friday payroll at risk (no vendor commitment by Thursday 12:00), or confirmed exposure of firm data at the vendor. CMT convened.

## 3. First hours (RS.MA, RS.MI)
1. **Cut connections if the vendor was attacked.** Pause integration jobs to and from the payroll platform; revoke the integration's API credentials; block the vendor's remote access, if any; confirm that no firm accounts are federated in a way the attacker could use.
2. **Secure the last good data.** Export from the data warehouse and the integration platform the prior week's payroll register, current pay rates, and bank details (masked copy plus the payroll team's secured full copy under dual control), and the approved time for the current week from the ATS client portal, the VMS, and the timekeeping platform.
3. **Insurance and counsel.** Call the cyber insurer hotline; counsel reviews the vendor contract (service credits, notice duties, data return).
4. **Status rhythm.** Business lead and vendor account manager on a call every 4 hours; written status to the CMT after each call.
5. **Tell associates early.** If payday is at risk, text associates by Thursday 15:00 what is happening, when they will be paid, and that the firm will never ask for bank details by text.

## 4. Manual payroll decision and execution (RC.RP-04)
**Decision point (Thursday 12:00, or earlier if the vendor gives no recovery time):** the CFO and the Director of Payroll and Billing decide whether to run the **off-cycle manual payroll** (procedure in STD-07, POAM-011). The default is to run it if the vendor cannot commit to releasing deposits by Thursday 18:00.

| Step | What | Who |
|---|---|---|
| 1 | Build the gross pay file from the prior week's register, adjusted with this week's approved hours (exports from step 3.2); flag associates with no approved time | Payroll specialists |
| 2 | Calculate net pay with the prior week's effective withholding rates; record every estimate for later true-up | Payroll specialists; Controller reviews |
| 3 | Fund through the bank's direct ACH origination (set up in advance under POAM-011) or load pay cards through the pay card provider; dual approval by the CFO and Controller; credit line draw by phone if needed (section 8) | CFO; Controller |
| 4 | Reconcile: count of associates paid against the approved-time list; exceptions paid by pay card on Monday | Director of Payroll and Billing |
| 5 | When the platform returns, true up taxes, deductions, and differences in the next regular payroll; record overtime paid so no worker is short for the workweek | Payroll specialists |

**Bank details are a fraud target during an outage.** Pay only to accounts on file in the last good register; no bank changes are accepted until the platform returns and call-back verification resumes.

## 5. Vendor cyber incident: data exposure assessment (RS.AN)
1. Ask the vendor, through counsel, which firm data was in scope (associate register, bank data, tax data) and when the attacker had access.
2. If firm personal information may have been accessed, start the decision log in `ir-runbook.md` section 6. The firm, as the covered entity, owns the Florida notices once the vendor notifies it (Fla. Stat. 501.171(6)(a)), and the clocks run from the firm's determination.
3. Check whether payrolled MSP workers or MSP client data were in scope; if so, the 48-hour MSP client notice applies.
4. Do not reconnect integrations until the vendor provides a written statement of eradication and clean recovery, and the Security Manager approves.

## 6. Communications (RS.CO, RC.CO)
| Audience | Message | When | Owner |
|---|---|---|---|
| Associates | What happened, when pay will arrive, how (direct deposit or pay card), and how to reach the payroll hotline | By Thursday 15:00 if payday is at risk; again when paid | Director of Marketing; contact center |
| Branch and on-site staff | Scripts and FAQ; no speculation about cause | Same day as declaration | VPs of the business units |
| Clients | Associates will be paid; no impact on service expected (or the impact) | Severity 1 only, or if billing is delayed | Account executives |
| MSP clients | Status of supplier timesheets and consolidated invoices; 48-hour notice if program data is involved | Severity 1, or as contracts require | VP Managed Workforce Solutions |
| Lender and PE sponsor | Missed or delayed payroll and the funding plan | Within 24 hours of severity 1 (credit agreement and internal rule) | CFO; CEO |
| Audit committee chair | Severity 1 summary | Within 24 hours | CEO |

## 7. Variant: ATS outage blocks time approval
If the ATS client portal is down on Monday, clients cannot approve time. Use the paper timesheets signed by client supervisors and the on-site sign-in sheets; branch office administrators scan them to the payroll team. The VMS and timekeeping platform imports continue if available. If time cannot be approved by Tuesday 17:00, pay the prior week's hours for associates still on assignment and true up the next week (BIA BP-02 workaround). The ATS vendor's RTO of 12 hours does not meet the dispatch RTO (P05 finding 1), so dispatch also moves to the daily assignment export.

## 8. Variant: credit line draw unavailable
If the bank portal or the borrowing base report is unavailable on Thursday, the CFO requests the draw by phone from the relationship manager with a manual borrowing base built from the last approved certificate and the week's billing estimate, with CFO and Controller dual approval (BIA BP-12). If the draw is refused, the CFO escalates to the CEO and the PE sponsor for a bridge.

## 9. Recovery and close (RC.RP)
1. Vendor confirms restoration, integrity of firm data, and (if attacked) eradication.
2. Re-establish integration connections with new credentials; run reconciliation of new hires, rates, and time for the outage period.
3. Run the true-up payroll; confirm no associate was underpaid for any workweek.
4. Business lead declares recovery complete when the next regular payroll runs on schedule (RC.RP-06).

## 10. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days; written report within 30 days (POL-03 4.10).
- Update P01 (R-005, R-043), P05 (vendor recovery assumptions), the POA&M, STD-07, and the vendor's Tier 1 review in P09.
- Consider a secondary payroll path (for example a standing ACH origination arrangement with the firm's bank) if the outage exceeded the vendor's stated RTO.
