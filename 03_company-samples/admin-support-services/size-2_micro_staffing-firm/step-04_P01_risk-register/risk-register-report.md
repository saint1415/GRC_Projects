# Risk Register Report: Cris Santos Company | Administrative and Support and Waste Management and Remediation Services | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (temporary staffing firm) |
| Size tier | Micro (7 internal staff; about 22 associates on assignment in an average week) |
| Vertical | Administrative and Support and Waste Management and Remediation Services |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Why it matters legally | No sector rule requires a risk assessment. The assessment is how the firm shows "reasonable measures to protect and secure data in electronic form containing personal information" (Fla. Stat. 501.171(2)) and meets its cyber insurer's application questions |
| Prepared | 2026-07-31 by the Operations Manager (Security and Privacy Lead) with the MSP lead technician |
| Updated | 2026-08-12 (R-022 added and closed from P07 testing); 2026-08-31 (R-012 and R-019 accepted) |
| Approved | 2026-08-31 by the Owner |

## 1. Scope and risk framing
**Scope.** The whole firm and its key vendors: the PATS (SSP, P02), the paper Form I-9 files, the accounting SaaS (all in the intake [asset inventory](../step-00_P00_intake/asset-inventory.csv)), and the vendors that hold worker data or run systems for the firm: the payroll service vendor, the ATS vendor and its AI subprocessor, the productivity suite vendor, the background screening provider, the MSP, and the backup service ([vendor register](../step-00_P00_intake/vendor-register.csv)).

**Risk tolerance and who can accept risk:**
- Low and Very Low: the Operations Manager may accept.
- Moderate: only the Owner may accept, with a treatment plan or a written reason.
- High and Very High: not accepted. The Owner approves a dated treatment plan instead. A risk that could divert associates' pay or expose every worker's SSN is never accepted at High.

This is the firm's first documented risk assessment. Before 2026, security decisions were made one at a time, mostly when the cyber insurer asked a question.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA (P05), the intake evidence, the gap analysis (P03), and interviews with all 7 staff and the MSP lead technician (2026-07-20 to 2026-07-31, EV-040), plus an office walkthrough on 2026-07-22 (EV-046). The gap analysis ran in the same fieldwork window, and the two shared findings.
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**. Each rating rests on evidence named in the `likelihood_basis` column: the vendor console and MSP exports, the payroll reports, the contracts and HR files, the walk-throughs, the account comparison of 2026-07-21 (EV-041), the records search of 2026-07-22 (EV-045), the compliance samples (EV-047, EV-048) and the interviews. A rating with no evidence behind it would be a guess, so none was made.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories. For a firm with about $19,400 of weekly billings and records on several hundred workers and about 9,800 candidates, theft of every worker's SSN or a diverted payroll is rated High.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 3 |
| Moderate | 14 |
| Low | 5 |
| **Total** | **22** |

Status: 6 In progress, 13 Open, 3 Closed (R-022 treated; R-012 and R-019 accepted).

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Phishing relays a payroll administrator's SMS code; SSNs exported and pay diverted | High | Authenticator-app MFA; bank-change and export alerts; Owner's monthly bank-change review; payroll phishing training | Operations Manager | 2026-10-31 |
| R-009 | AI match feature hides qualified applicants with a disparate effect | High | P10 conditions: sort-only mode, human review, bias testing, notice and accommodation | Senior Recruiter | 2026-11-30 |
| R-013 | MSP or its remote tool compromised; reaches every laptop and the backup | High | MFA on MSP-held logins; annual MSP review; contract amendment with 24-hour notice | Owner | 2026-12-31 |
| R-004 | Onboarding folder with Form I-9 images and consumer reports open to all staff | Moderate | Restrict to two people; move consumer reports out | Operations Manager | 2026-09-30 |
| R-002 | Pay redirected by an impersonated bank-change request | Moderate | Call-back rule; hold the first payroll after a change; vendor second factor | Operations Manager | 2026-10-31 |
| R-006 | Former staff keep access (ATS, email, payroll, E-Verify) | Moderate | Last-day checklist; monthly reconciliation | Operations Manager | 2026-09-30 |

**The common theme is the payroll and onboarding data.** The firm's most damaging plausible event is not ransomware: it is someone quietly taking every worker's SSN and bank details and redirecting pay. Three weaknesses line up behind that path: a phishable second factor on the payroll service (R-001), no call-back on bank changes (R-002), and no one watching exports or bank changes. Fixing those three also lowers R-003 and R-016.

**Risks that were fixed or found during the work:**
- R-006: the former recruiter's ATS and email accounts were disabled on 2026-07-21, the day the account comparison found them (EV-041). The ATS and suite sign-in logs showed no use after her last day (2026-05-15), so the Operations Manager documented that no breach occurred. The process gap remains open.
- R-009: the AI feature's smart filter was turned off on 2026-07-24, during this assessment (EV-042). The P10 conditions are still open.
- R-022: added on 2026-08-12 after P07 testing found a former Coordinator's E-Verify account still active (EV-AC-2). It was deactivated on 2026-08-11; the E-Verify user report showed no sign-in after 2025-12-10. Closed; the process gap stays in R-006.

**Two passes.** Pass 1 was completed on 2026-07-31 from intake and fieldwork evidence. Pass 2 followed the control assessment (P07): R-022 was added on 2026-08-12 from P07 testing. The `assessment_pass` column shows which pass produced each risk.

## 4. Treatment summary
- **Funded (2026 Q4, approved by the Owner; about $1,900 one-time and $2,900 a year):**
  - Payroll service authenticator-app MFA and alerts: no extra cost (vendor features)
  - Security awareness training with phishing simulations for 7 people: about $500 a year
  - Backup upgrade to 90-day immutable versions with MFA: about $500 a year
  - Productivity suite plan upgrade for 1-year log retention and alerting: about $900 a year
  - MSP project time (folder permissions, restore tests, wiping, account clean-up): about $1,200 one-time
  - Annual MSP security review and vendor follow-ups: about $1,000 a year
  - Independent statistician review of the AI bias test (P10): about $700 one-time
- **Independent assessment (P07) and policy work (P06) in 2026:** about $2,800 one-time, already spent.
- **Accepted:** R-012 (Low; hotspots and working from home cover a one-day internet outage) and R-019 (Low; kiosk mode on guest Wi-Fi).
- **Contract actions:** MSP contract amendment (R-013) at renewal by 2026-12-31; AI data use addendum (R-010) by 2026-10-31; 72-hour breach notice terms with the ATS vendor and the screening provider at renewal (R-017).

## 5. Approval
- Owner: approved all treatment plans, the two acceptances, and the budget on 2026-08-31.
- Next full review: July 2027, or sooner after a major change (for example a new payroll service, turning any AI feature back on, or adding job orders outside Florida) or an incident.
