# Risk Register Report: Cris Santos Company | Arts, Entertainment, and Recreation | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent event promoter with one leased room) |
| Size tier | Sole Proprietorship (owner only, 0 employees) |
| Vertical | Arts, Entertainment, and Recreation |
| Method | NIST SP 800-30 Rev. 1 (qualitative 5-level scales; Tables G-5 and I-2) |
| Also supports | PCI DSS v4.0.1 risk assessment duties (Requirement 12.3) and "reasonable measures" under Fla. Stat. 501.171(2). This is the business's first risk assessment |
| Prepared | 2026-07-31 by the owner, with the on-call IT consultant |
| Risk owner and approver | Owner (owner, security and privacy lead, PCI DSS contact, and risk acceptor for every risk) |
| Approved | 2026-08-31 |

## 1. Scope and risk framing
**Scope.** The whole business as one system: SYS-01 to SYS-08, the Room, and the contractors (marketing assistant, door and security contractor, sound engineer, bookkeeper, IT consultant), as listed in the intake [asset inventory](../step-00_P00_intake/asset-inventory.csv) and [vendor register](../step-00_P00_intake/vendor-register.csv). Processes come from the BIA (P05).

**Risk tolerance.** The owner owns and accepts every risk. Because the same person proposes and approves, the owner applies three fixed rules:
- Low and Very Low: may be accepted, with the reason written in the register.
- Moderate: may be accepted only with a dated treatment plan or a written reason.
- High and Very High: must be treated with a dated plan. Not accepted as-is. Any risk to card data is never accepted above Low.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the intake evidence, the BIA, and a walk through every SaaS account, the laptop, the phones, and the Room's network with the IT consultant (2026-07-27 to 2026-07-31, EV-035). The gap analysis (P03) ran in the same self-assessment week, and the two shared findings.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (other sources), and likelihood of adverse impact, each on the 5-level scale. Combined with **Table G-5**. Each rating rests on evidence named in the `likelihood_basis` column: the account, device and network settings (EV-001, EV-002, EV-011, EV-017 to EV-020), the PCI portal and merchant agreement (EV-009, EV-010, EV-047), the owner's intake account (EV-028), and the searches and reviews run during the self-assessment (EV-040, EV-042, EV-046). A one-person business keeps no ticket or incident log to count, so a rating with no evidence behind it would be a guess, and none was made.
3. **Rate impact.** Table H-3 levels, using the BIA impact categories.
4. **Determine risk.** **Table I-2.** The `overall_likelihood` and `risk_level` columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results
| Risk level | Count |
|---|---|
| High | 3 |
| Moderate | 8 |
| Low | 4 |
| **Total** | **15** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Takeover of the ticketing platform administrator account | High | MFA, unique passwords, named sub-users, log review | Owner | 2026-09-15 |
| R-002 | Card-skimming script on the website pages that embed the checkout | High | Website MFA, remove non-essential scripts, monthly page check | Owner | 2026-09-30 |
| R-003 | Card numbers keyed on the laptop or received by email and text | High | Payment links; never accept card details; delete on receipt | Owner | 2026-09-30 |
| R-004 | Untrue SAQ A attestation | Moderate | Scope description; close eligibility gaps before signing | Owner | 2026-10-31 |
| R-010 | Compromise missed or deadlines missed | Moderate | P08 runbook, contacts, walkthrough | Owner | 2026-09-30 |
| R-011 | Advertised prices leave out fees (16 CFR 464.2) | Moderate | Total price in every post, email, and flyer | Owner | 2026-09-30 |

The three High risks share one cause: **the owner's card security depends on two accounts and one web page that the owner controls, and all three are weaker than the vendor systems behind them.** A shared password with no MFA protects both the ticketing platform and the website, and card numbers still reach the owner by phone, email, and text. Two free settings (MFA on SYS-01 and the website) and two habit changes (payment links, never accepting card details) reduce all three within a month and make the 2026 SAQ A attestation true.

## 4. Treatment summary
- **Free fixes first (by 2026-09-15):** MFA on SYS-01 and the website, unique passphrases, named sub-users for the assistant and door staff, and payment links for phone orders.
- **Budgeted (about $400 a year):** a password manager, a security course for the owner, and a second router for a guest network in the Room.
- **Process changes by 2026-09-30:** remove non-essential scripts from event pages, export retention rule, total-price posting checklist, smart pricing in suggest-only mode (P10), call-back check for payment instructions, and the P08 runbook walkthrough.
- **Before signing the 2026 SAQ A (due 2026-10-31):** PCI scope description and evidence folder (R-004), vendor responsibility list (R-013).
- **Accepted (Low):** R-008 (ticketing platform outage; the offline door list meets the BIA) and R-015 (hurricane; refunds and rescheduling run from the platform).

**Loop from the control assessment (P07).** Testing on 2026-07-29 found a former freelance assistant still listed as a website administrator (EV-SA-9). The owner removed the account the same day. It is recorded under R-002, because a website administrator can add scripts to the pages that embed the checkout.

**One pass.** The register was completed on 2026-07-31 from intake and self-assessment evidence. The control tests ran on 2026-07-29, inside the same week, so this pass already reflects them: R-002 cites the former website administrator (EV-SA-9) and R-007 the router's default password (EV-IA-5). No risk was added after P07 testing. The `assessment_pass` column records the pass for each risk.

## 5. Approval
Owner, 2026-08-31: approved all treatment plans and the two acceptances. Next full review July 2027, or sooner after a new system, a new contractor with access, a change in how cards are taken, or an incident.
