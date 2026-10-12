# Risk Register Report: Cris Santos Company | Construction | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (commercial and institutional building general contractor) |
| Size tier | Sole Proprietorship (owner only, 0 employees) |
| Vertical | Construction |
| Method | NIST SP 800-30 Rev. 1 (qualitative 5-level scales; Tables G-5 and I-2) |
| Prepared | 2026-07-17 by the owner, with the on-call IT technician; R-006 updated 2026-07-22 after the P07 router finding |
| Risk owner and approver | Owner (risk owner, risk acceptor, and CMMC Affirming Official for every risk) |
| Approved | 2026-08-31 |

## 1. Scope and risk framing
**Scope.** The whole business as one system: SYS-01 to SYS-09, paper plan sets and files, the home office and storage unit, and the outside parties that touch money or FCI (bookkeeper, subcontractors, clients, the VA paying office), as listed in the intake [asset inventory](../step-00_P00_intake/asset-inventory.csv) and [vendor register](../step-00_P00_intake/vendor-register.csv). Processes come from the BIA (P05).

**Risk tolerance.** The owner owns and accepts every risk. Because the same person proposes and approves, the owner applies three fixed rules (POL-01 4.4):
- Low and Very Low: may be accepted, with the reason written in the register.
- Moderate: may be accepted only with a dated treatment plan or a written reason.
- High and Very High: must be treated with a dated plan. Not accepted as they are. Any risk that could send a payment to the wrong account is treated, never accepted.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the intake evidence, the BIA, the gap analysis (P03), the March 2026 near miss (EV-010), and a walk through the accounts, devices, and home network with the IT technician on 2026-07-16 (EV-033). The gap analysis ran in the same self-assessment week, and the two shared findings.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (other sources), and likelihood of adverse impact, each on the 5-level scale. Combined with **Table G-5**. Each rating rests on evidence named in the `likelihood_basis` column: the account, device and router reviews (EV-004, EV-007, EV-018 to EV-020), the payment correspondence (EV-009, EV-010), the contract forms and the prime's requirement (EV-011, EV-013), the document search (EV-029), and the owner's self-reviews (EV-032, EV-034). A one-person contractor keeps no ticket or incident log to count, so a rating with no evidence behind it would be a guess, and none was made.
3. **Rate impact.** Table H-3 levels, using the BIA impact categories (P05 section 3).
4. **Determine risk.** **Table I-2.** The `overall_likelihood` and `risk_level` columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 3 |
| Moderate | 9 |
| Low | 2 |
| **Total** | **15** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Mailbox takeover used to send a client false remittance instructions | Very High | Security key on email; sign-in and forwarding-rule checks; DMARC; remittance-change notice to clients; cyber insurance quote | Owner | 2026-10-31 |
| R-002 | Spoofed subcontractor bank-change request | High | Call-back to the number in the subcontract; wait and test deposit before paying a changed account | Owner | 2026-09-15 |
| R-008 | No Final Level 1 (Self) before the DoD subcontract award | High | Close the FAR 52.204-21 gaps; self-assess; SPRS affirmation | Owner | 2026-11-30 |
| R-010 | Owner unavailable or phone lost (single point of failure) | High | Standby supervision agreement; sealed recovery codes; security key backup | Owner | 2026-12-31 |
| R-007 | Covered hotspot in use; unsupported SAM representation | Moderate | Device retired; purchase check; documented inquiry before each SAM renewal | Owner | 2026-10-31 |
| R-009 | FCI in the AI tool, the personal photo cloud, and file-transfer links | Moderate | Approved locations for FCI; no FCI in the AI tool without no-training terms | Owner | 2026-09-30 |

**The pattern.** Three of the four top risks are about **money moving on the strength of an email**. A $24,000 pay app sent to the wrong account would be more than a month and a half of the company's receipts, and the company has no insurance for it. The cheapest controls are procedural, not technical: never change bank details on the strength of an email, and tell every client the same in writing. The technical controls (security key, DMARC, sign-in checks) cost less than $100 a year.

**The deadline.** R-008 has a hard date. The prime contractor cannot award the DoD subcontract until the owner holds Final Level 1 (Self) and has affirmed in SPRS (32 CFR 170.15(b); DFARS 252.204-7021(d)(4)). Most Level 1 gaps are also the controls that reduce R-001 to R-006, so one plan serves both.

## 4. Treatment summary
- **Free fixes first (by 2026-09-15):** call-back rule for bank changes, MFA on SYS-01 and SYS-02, separate family and bookkeeper accounts, password manager.
- **Two passes.** Pass 1 was completed on 2026-07-17 from intake and self-assessment evidence. R-007 (covered hotspot) came from the Section 889 inquiry on 2026-07-16 (EV-039), inside that week, so it is in pass 1. Pass 2 followed the control assessment (P07): R-006 (router default password) came from P07 testing on 2026-07-21 (EV-IA-5, EV-SC-7), and the register was updated on 2026-07-22; the password and remote administration were fixed the same day as the test. The `assessment_pass` column records the pass for each risk.
- **Budgeted (about $400 a year):** two security keys, a password manager, a replacement router, and file sync with version history. A cyber insurance quote with social engineering coverage is requested by 2026-10-31 (R-001).
- **Accepted (Low):** R-015 (hurricane; records are in SaaS and reachable from the phone).

## 5. Approval
Owner, 2026-08-31: approved all treatment plans and the one acceptance. Next full review July 2027, or sooner after a new federal contract, a new system or vendor, a hire, or an incident (POL-01 4.3).
