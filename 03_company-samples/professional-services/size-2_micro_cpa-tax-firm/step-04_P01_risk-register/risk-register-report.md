# Risk Register Report: Cris Santos Company | Professional, Scientific, and Technical Services | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (CPA and tax preparation firm) |
| Size tier | Micro (7 employees) |
| Vertical | Professional, Scientific, and Technical Services |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also satisfies | The risk assessment the FTC Safeguards Rule requires the program to be based on (16 CFR 314.4(b)) and the periodic reassessment (314.4(b)(2)). The written criteria in 314.4(b)(1) are not required at this size (314.6) but are met anyway (section 2) |
| Prepared | 2026-07-17 by the Office Manager (Qualified Individual) with the MSP lead technician |
| Updated | 2026-08-05 (R-024 added from P07 testing); 2026-08-31 (R-016 and R-023 accepted) |
| Approved | 2026-08-31 by the Owner CPA |

## 1. Scope and risk framing
**Scope.** The whole firm and its key vendors: every system that holds client tax return information or customer information (SYS-01 to SYS-09 in `../00_company-facts.md`), the office suite, and the vendors that handle that information for the firm: the tax software vendor, the portal vendor, the productivity suite vendor, the payroll platform vendor, the MSP and its backup subcontractor, the MFP lessor, and the AI assistant vendor.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the Office Manager may accept.
- Moderate: only the Owner CPA may accept, with a treatment plan or a written reason.
- High and Very High: not accepted. The Owner CPA approves a dated treatment plan instead, due before the next filing season.

This is the firm's first risk assessment. The 2024 WISP listed threats from the IRS Pub. 5708 template but did not rate likelihood or impact, so it is not relied on.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the threats IRS Pub. 4557 describes for tax professionals (phishing, account takeover, refund fraud), the BIA (P05), the gap analysis (P03), and interviews with all 7 employees and the MSP lead technician (2026-07-06 to 2026-07-17).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories. For a firm with about $10,500 billed per business day in season and records on about 3,300 consumers, theft of most client files or a week-long outage in a deadline week is rated High or Very High.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

These scales and rules are the "criteria for the evaluation and categorization of identified security risks" and the "requirements describing how identified risks will be mitigated or accepted" that a larger firm would need under 314.4(b)(1)(i) and (iii).

## 3. Results

| Risk level | Count |
|---|---|
| High | 3 |
| Moderate | 18 |
| Low | 4 |
| **Total** | **25** |

Status: 16 Open, 7 In progress, 2 Closed (R-016 and R-023 accepted).

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Business email compromise steals client tax documents and sends refund and payment change requests | High | Number matching; block external forwarding (done 2026-07-20); suite alerts; one year of logs; training and phishing simulations | Office Manager | 2026-10-31 |
| R-005 | Ransomware encrypts computers and the synced client folders in the filing season | High | MSP-managed EDR; narrower sync; immutable backup; quarterly restore tests | Office Manager | 2026-12-31 |
| R-006 | MSP remote tool compromise reaches every computer and the MSP-held logins | High | Contract security and breach notice terms; annual MSP review; MFA on MSP-held logins | Owner CPA | 2026-12-31 |
| R-002 | Refund direct deposit changed through a hijacked email thread | Moderate | Call-back rule before transmission | Owner CPA | 2026-09-30 |
| R-007 | Former or seasonal worker still has access | Moderate | Last-day checklist; end dates on seasonal accounts; monthly reconciliation | Office Manager | 2026-09-30 |
| R-013 | Tax return information uploaded to the AI assistant without an IRC 7216 basis | Moderate | No client-identifying content until counsel confirms a basis; deletion request; approved-tools rule (P10) | Senior Tax Accountant | 2026-09-30 |

**The common theme is email.** Clients send their tax documents by email, the firm sends returns back the same way, and the suite has the weakest sign-in of any system that holds them. A BEC attacker needs no access to the tax software to steal what a refund fraudster wants (R-001), and the same mailbox lets the attacker ask for bank account changes (R-002, R-003). The treatments for R-001 also reduce R-008, R-009, and R-024.

**Risks that were fixed or found during the work:**
- R-001: the MSP blocked automatic forwarding to external addresses for every mailbox on 2026-07-20, at the Office Manager's request.
- R-007: the seasonal assistant's accounts were disabled on 2026-07-08, the day they were found. Tax software and suite sign-in logs showed no use after the assistant's last day (2026-04-17), so the Office Manager documented that no unauthorized access occurred. The process gap remains open.
- R-024: added on 2026-08-05 after P07 testing found the MFP's legacy-authentication mailbox and default administration password. The password was changed on 2026-08-05.

## 4. Treatment summary
- **Funded (2026 Q4, approved by the Owner CPA; about $6,900 one-time and $2,930 a year):**
  - MSP-managed EDR with alert monitoring on 8 computers: about $1,400 a year
  - Security awareness training with phishing simulations for 8 people, including the seasonal assistant: about $450 a year
  - Suite plan upgrade for one year of audit logs and alert policies: about $720 a year
  - Cellular failover router: about $400 one-time and $360 a year
  - MSP project time for desktop encryption, administrator accounts, MFA on MSP-held logins, the MFP fix, and restore tests: about $1,500 one-time
  - Independent assessment in 2026 (P07): about $3,500 one-time
  - Counsel review of the IRC 7216 basis for AI use and of the consent template: about $1,500 one-time
- **Accepted:** R-016 (Moderate, by the Owner CPA: the tax software vendor meets the BIA and extensions are the fallback) and R-023 (Low, by the Office Manager: laptops are encrypted).
- **Contract actions:** MSP contract amendment with security terms, a 72-hour breach notice, and a technician list (R-006) by 2026-12-31; written IRC 6713 and 7216 notice to MSP technicians (R-025) by 2026-10-31; breach notice terms with the portal and payroll vendors at renewal (R-019).

## 5. Approval
- Owner CPA: approved all treatment plans, the two acceptances, and the budget on 2026-08-31.
- Next full review: July 2027, or sooner after a material change (for example, buying another preparer's client list, which could bring the firm near the 5,000-consumer line in 314.6) or an incident.
