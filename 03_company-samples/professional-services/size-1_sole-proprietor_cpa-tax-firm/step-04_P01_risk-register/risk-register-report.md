# Risk Register Report: Cris Santos Company | Professional, Scientific, and Technical Services | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (CPA and tax preparation practice) |
| Size tier | Sole Proprietorship (CPA-owner only, 0 employees) |
| Vertical | Professional, Scientific, and Technical Services |
| Method | NIST SP 800-30 Rev. 1 (qualitative 5-level scales; Tables G-5 and I-2) |
| Also satisfies | The risk assessment the FTC Safeguards Rule requires the program to be based on (16 CFR 314.4(b)). The *written* form in 314.4(b)(1) is not mandatory under the 314.6 exception (about 1,450 consumers), but the owner keeps it in writing. This is the practice's first one |
| Prepared | 2026-07-31 by the CPA-owner, with the on-call IT consultant (services agreement and IRC 7216 notice since 2026-07-23) |
| Risk owner and approver | CPA-owner (owner, Qualified Individual, and risk acceptor for every risk) |
| Approved | 2026-08-31 |

## 1. Scope and risk framing
**Scope.** The whole business as one system: SYS-01 to SYS-09, paper files in the home office, and the outside parties that touch client data (tax software vendor, IT consultant, SaaS vendors, AI assistant vendor). Processes and impact levels come from the BIA (P05).

**Risk tolerance.** The CPA-owner owns and accepts every risk. Because the same person proposes and approves, the owner applies three fixed rules (POL-01 4.4):
- Low and Very Low: may be accepted, with the reason written in the register.
- Moderate: may be accepted only with a dated treatment plan or a written reason.
- High and Very High: must be treated with a dated plan and are never accepted as they are. Every High and Moderate treatment is due before the 2027 filing season (2027-01-15), except the first file purge, which waits until after the season.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the missing-controls list in `../00_company-facts.md` section 4, the two 2026 near misses (section 7 of the facts), IRS Pub. 4557's warning signs of data theft, and a walk through the laptop, phone, router, and SaaS accounts with the IT consultant.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (other sources), and likelihood of adverse impact, each on the 5-level scale, combined with **Table G-5**.
3. **Rate impact.** Table H-3 levels, using the BIA impact categories (P05 section 3).
4. **Determine risk.** **Table I-2.** The `overall_likelihood` and `risk_level` columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results
| Risk level | Count |
|---|---|
| High | 2 |
| Moderate | 9 |
| Low | 4 |
| **Total** | **15** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Business email compromise of the owner's mailbox and theft of client tax documents | High | Scan-to-folder, then mailbox MFA; password manager; monthly sign-in and rule review; training; P08 runbook | CPA-owner | 2026-09-15 |
| R-009 | CPA-owner unavailable or phone lost in filing season (single point of failure) | High | Sealed recovery codes; continuation agreement with another CPA; second authenticator | CPA-owner | 2026-12-31 |
| R-002 | Refund diversion through a hijacked client mailbox | Moderate | Call-back rule for every bank, address, or email change | CPA-owner | 2026-12-15 |
| R-006 | Client tax return information disclosed to the AI assistant vendor without an IRC 7216 basis | Moderate | No client data in the tool; counsel review (P10) | CPA-owner | 2026-10-31 |
| R-005 | Forgotten 2025 contract preparer account in the tax software (P07 finding) | Moderate | Disabled 2026-07-29; quarterly user review; weekly EFIN and PTIN counts in season | CPA-owner | 2026-10-31 |
| R-004 | Client documents by plain email and text photos synced to a personal photo backup | Moderate | Portal-only exchange; required client portal MFA; photo cleanup | CPA-owner | 2027-01-15 |

**One setting drives the top risk.** R-001 is High because the mailbox that holds years of client W-2s, 1099s, and prior returns is protected only by a password that is reused elsewhere, and MFA was switched off so the printer-scanner could email scans. Moving the scanner to scan-to-folder costs nothing and lets MFA go back on. R-002 and R-005 show the other half of the tax preparer threat: the attacker's goal is a fraudulent refund, so the firm's controls must also stop bank account changes and misuse of its accounts, not only data theft.

**R-009 is High because of the calendar.** The chance that the owner is suddenly out of action is low, but in March the impact is Very High: about 380 individual clients would miss the April deadline with nobody able to file extensions under the firm's EFIN.

## 4. Treatment summary
- **Free fixes first (by 2026-09-15, before the extension deadline):** scan-to-folder and mailbox MFA, practice management MFA, password manager, printed P08 contacts.
- **Budgeted (about $400 a year):** password manager, backup service for the email and file suite, and a security course for the owner.
- **Contract and counsel actions by 2026-12-31:** counsel's IRC 7216 advice on the AI uploads and on sharing client data with a backup CPA (R-006, R-009); continuation agreement (R-009); vendor list and the IT consultant's MFA confirmation (R-008).
- **Before the 2027 filing season (2027-01-15):** portal-only exchange with required client MFA (R-004); call-back rule announced to clients (R-002); runbook walkthrough (R-013).
- **Accepted (Low):** R-014 (lost or stolen device; both devices are encrypted) and R-015 (hurricane; the SaaS tools work from anywhere and extensions are available).
- **New from the control assessment (P07):** R-005, the forgotten contract preparer account, was added after the account test on 2026-07-29.

## 5. Approval
CPA-owner, 2026-08-31: approved all treatment plans and the two acceptances. Next full review July 2027, or sooner after a new system or vendor, any engagement of a helper or contract preparer, a move above 5,000 consumers (which ends the 314.6 exceptions), or an incident.
