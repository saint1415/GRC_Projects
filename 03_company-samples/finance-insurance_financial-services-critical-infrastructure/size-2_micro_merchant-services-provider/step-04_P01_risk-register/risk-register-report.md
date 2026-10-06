# Risk Register Report: Cris Santos Company | Financial Services | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (merchant services provider, an ISO) |
| Size tier | Micro (7 employees) |
| Vertical | Financial Services |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also satisfies | Input to PCI DSS 12.3.1 targeted risk analyses (the analyses themselves are a P03 gap). The FTC Safeguards Rule written risk assessment (16 CFR 314.4(b)(1)) does not apply at this size (314.6 exception), but this register meets it anyway |
| Prepared | 2026-07-24 by the Operations Manager (Qualified Individual) with the MSP lead technician |
| Updated | 2026-08-05 (R-022 added from P07 testing); 2026-08-31 (R-016 and R-021 accepted and closed) |
| Approved | 2026-08-31 by the Owner |

## 1. Scope and risk framing
**Scope.** The whole business and its key vendors: every system in `../00_company-facts.md` section 3 (SYS-01 to SYS-10), every process in the BIA (P05), the processor partner, the MSP, the CRM and phone vendors, the web developer, and the 6 outside sales agents.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the Operations Manager may accept.
- Moderate: only the Owner may accept, with a treatment plan or a written reason.
- High and Very High: not accepted. The Owner approves a dated treatment plan instead.
- **A risk that would leave a PCI DSS requirement "not in place" cannot be accepted.** The ISO agreement depends on an honest SAQ and AOC, so those risks are treated or avoided.

This is the company's first written risk assessment. The 2022 policy template mentioned an annual risk assessment, but none was ever recorded.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA (P05), the gap analysis (P03), the March 2026 deposit change attempt, and interviews with the Owner, all staff, and the MSP lead technician (2026-07-13 to 2026-07-24).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories. For a company with about $1.1 million in receipts, anything that could end the ISO agreement (a card data compromise traced to a company account, or a false SAQ) is rated Very High: it would end the business.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 4 |
| Moderate | 12 |
| Low | 6 |
| **Total** | **22** |

Status: 10 In progress, 10 Open, 2 Closed (R-016 and R-021 accepted).

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Phished console password used to insert a skimming script into merchants' hosted payment pages | High | MFA on every console account; payment page script inventory; weekly console log review | Operations Manager | 2026-10-31 |
| R-007 | Caller posing as a merchant gets the deposit bank account changed | High | Call-back rule to the number on file; two-person approval; drills | Merchant Support Lead | 2026-09-30 |
| R-008 | Notice clocks missed after a compromise (24-hour contract notice, Visa's 3 calendar days, state law) | High | P08 runbook; recorded contacts; tabletop | Operations Manager | 2026-11-30 |
| R-009 | PCI DSS validation fails or is found inaccurate | High | Accurate 2026 SAQ with an action plan; scope confirmation; smaller scope | Owner | 2026-10-30 |
| R-003 | Card data in call recordings and on general-purpose laptops | Moderate | Recordings deleted; stop the keyed-entry service | Merchant Support Lead | 2026-10-15 |
| R-005 | Website application bucket exposed | Moderate | Move to the CRM upload link; delete bucket contents; take back the hosting login | Sales and Agent Manager | 2026-10-31 |

**The common theme is the gateway console and the people who use it.** The console is where the company touches the payment environment, and it has the weakest sign-in of any company system (R-001, R-002). People are the other path: a convincing caller (R-007) or a phishing email (R-001, R-004, R-010). The treatments for R-001 and R-007 also reduce R-002, R-006, and R-022.

**One decision shrinks several risks at once.** Stopping the keyed-entry service (R-003, treatment "Avoid") removes card data from the phone system and laptops. It also takes the office network out of the cardholder data environment and makes the 2026 SAQ smaller and more accurate (R-009). Merchants lose little: they can key their own sales in the gateway's mobile app (P05 BP-02).

**Risks that were fixed or found during the work:**
- R-006: the former agent's console and CRM accounts were disabled on 2026-07-15, the day they were found. Sign-in logs showed no use after the contract ended. The process gap remains open.
- R-003: card data was found in call recordings on 2026-07-21. Recording of the support queue was paused on 2026-07-22, and the recordings with card data were deleted on 2026-08-14 after counsel's review (P08 section 6.5).
- R-009: the Owner told the processor partner on 2026-08-20 that the 2025 SAQ left out the keyed-entry path.
- R-022: added on 2026-08-05 after P07 testing found unapproved analytics scripts on 2 merchants' hosted payment pages. Both were removed on 2026-08-12 with the merchants' agreement.

## 4. Treatment summary
- **Funded (2026 Q4, approved by the Owner; about $3,900 one-time and $5,700 a year):**
  - MSP-managed EDR on 9 laptops: about $1,600 a year
  - Security awareness training with phishing simulations for 7 employees and 6 agents: about $700 a year
  - Business password manager: about $400 a year
  - Approved business AI assistant for 7 users (no training on company data): about $1,500 a year
  - Internal vulnerability scanning added to the ASV service: about $1,500 a year
  - Website rebuild to remove the application form and move the hosting account: about $1,200 one-time
  - MSP project time (restore tests, EDR rollout, Wi-Fi change): about $1,200 one-time
  - Independent assessment in 2026 (P07): about $1,500 one-time
- **Planned for 2027 Q1:** first penetration test of the remaining PCI DSS scope (about $4,000; scope is smaller once keyed entry stops).
- **Accepted:** R-016 (Low; home working covers the office) and R-021 (Low; laptops encrypted and hold no local data).
- **Shared:** R-018 (processor partner failure), through contract terms requested at the 2027-01-01 renewal.
- **Contract actions:** MSP security terms (R-011) by 2026-12-31; agent agreement addendum (R-017) by 2026-12-31; hosting account transfer (R-020) by 2026-09-30.

## 5. Approval
- Owner: approved all treatment plans, the two acceptances, and the budget on 2026-08-31.
- Next full review: July 2027, or sooner after a major change (for example, a second processor partner, a new keyed or phone payment service, or a new AI tool) or an incident. The six-month PCI DSS scope confirmation (12.5.2.1) triggers a review of R-001 to R-003, R-009, and R-022 each time.
