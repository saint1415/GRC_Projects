# Risk Register Report: Cris Santos Company | Accommodation and Food Services | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (six-room bed-and-breakfast inn) |
| Size tier | Sole Proprietorship (owner-innkeeper only, 0 employees) |
| Vertical | Accommodation and Food Services |
| Method | NIST SP 800-30 Rev. 1 (qualitative 5-level scales; Tables G-5 and I-2) |
| Also satisfies | Input to the risk management that PCI DSS v4.0.1 Requirement 12.3 covers, including its targeted risk analyses (N72-R01), and evidence of "reasonable measures" under Fla. Stat. 501.171(2) (N72-R04). This is the inn's first one |
| Prepared | 2026-07-24 by the owner-innkeeper, with the on-call IT consultant (under a confidentiality agreement since 2026-07-17) |
| Risk owner and approver | Owner-innkeeper (owner, security and privacy lead, and risk acceptor for every risk) |
| Approved | 2026-08-31 |

## 1. Scope and risk framing
**Scope.** The whole business as one system: SYS-01 to SYS-11, the paper reservation pad and binder, the house and its door locks, and the contracted services (cleaning service, bookkeeper, IT consultant) and key vendors. Processes come from the BIA (P05).

**Risk tolerance.** The owner owns and accepts every risk. Because the same person proposes and approves, the owner applies three fixed rules:
- Low and Very Low: may be accepted, with the reason written in the register.
- Moderate: may be accepted only with a dated treatment plan or a written reason.
- High and Very High: must be treated with a dated plan. Not accepted as they are. Any risk to guest safety (room access) rated High is never accepted.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the missing-controls list in `../00_company-facts.md` section 4, the gap analysis (P03), current attacks on lodging (fake OTA messages and payment links), and a walk through the house, the laptop, the phone, and each SaaS account with the IT consultant on 2026-07-21.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (other sources), and likelihood of adverse impact, each on the 5-level scale. Combined with **Table G-5**.
3. **Rate impact.** Table H-3 levels, using the BIA impact categories (P05 section 3).
4. **Determine risk.** **Table I-2.** The `overall_likelihood` and `risk_level` columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results
| Risk level | Count |
|---|---|
| High | 3 |
| Moderate | 9 |
| Low | 3 |
| **Total** | **15** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Information stealer on the shared laptop leads to takeover of the innkeeping software, OTA-2, and email | High | MFA, password manager, no family use, disk encryption, training | Owner-innkeeper | 2026-10-31 |
| R-002 | Card numbers and security codes on the paper pad and in email are stolen | High | Shred and purge; pay-by-link; never record security codes | Owner-innkeeper | 2026-10-31 |
| R-004 | Phished innkeeping or OTA password used to send guests fake payment links | High | MFA on both accounts; named relief account; monthly sign-in review | Owner-innkeeper | 2026-09-15 |
| R-003 | Payment facilitator penalties for never validating PCI DSS | Moderate | Redesign to SAQ A plus SAQ P2PE; submit by 2026-12-31 | Owner-innkeeper | 2026-12-31 |
| R-005 | Room entry through an old master code, shared login, or forgotten lock account | Moderate | New master code, quarterly changes, named accounts | Owner-innkeeper | 2026-10-31 |
| R-008 | About 1,900 guest ID photos exposed | Moderate | Stop photographing IDs; delete photos; MFA on the backup | Owner-innkeeper | 2026-09-30 |

The three High risks share one cause: **the inn's most valuable accounts are protected only by passwords saved in a family laptop's browser, and card data sits outside the vendors' vaults.** Turning on MFA in three accounts costs nothing and reduces R-001 and R-004 within two weeks of adoption. Taking phone payments by pay-by-link and destroying the pad and email forms removes the data behind R-002 and most of the PCI DSS scope behind R-003.

## 4. Treatment summary
- **Free fixes first (by 2026-09-15):** MFA on the innkeeping software, email, and OTA-2; password manager; disk encryption; new house master code; shred the pad pages and purge the email forms.
- **Small budget (about $150 a year):** a password manager (about $40), a business-grade email and file plan with version history (about $100), and the pay-by-link feature (included in the facilitator's fees).
- **Design and contract actions by 2026-12-31:** SAQ A plus SAQ P2PE validation (R-003), relief innkeeper account and sealed recovery codes (R-010), AI add-on conditions (R-013, by 2026-10-15).
- **Accepted (Low):** R-011 (innkeeping outage; vendor recovery objectives meet the BIA) and R-012 (hurricane; the SaaS systems are reachable from anywhere).

**Loop from the control assessment (P07).** Testing on 2026-07-23 found two things the walkthrough had missed: the lock installer's administrator account was still active in the lock app (disabled the same day; added to R-005), and the router's internet-side remote management was on (turned off the same day; added to R-006).

## 5. Approval
Owner-innkeeper, 2026-08-31: approved all treatment plans and the two acceptances. Next full review July 2027, or sooner after a new system or vendor, a change in how payments are taken, or an incident.
