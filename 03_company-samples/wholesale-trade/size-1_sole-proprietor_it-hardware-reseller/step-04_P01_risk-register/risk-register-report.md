# Risk Register Report: Cris Santos Company | Wholesale Trade | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (IT hardware reseller) |
| Size tier | Sole Proprietorship (owner only, 0 employees) |
| Vertical | Wholesale Trade |
| Method | NIST SP 800-30 Rev. 1 (qualitative 5-level scales; Tables G-5 and I-2) |
| Also supports | The CMMC Level 1 self-assessment (P03) and the supply chain benchmark from NIST SP 800-161 Rev. 1 |
| Prepared | 2026-08-07 by the owner, with the on-call IT consultant. R-008 added from P07 testing on 2026-08-06 |
| Risk owner and approver | Owner (risk acceptor for every risk) |
| Approved | 2026-08-31 |

## 1. Scope and risk framing
**Scope.** The whole business as one system: SYS-01 to SYS-10, the garage stock and staging bench, paper tag sheets, and the suppliers and contractors around them (distributors, marketplace and brokers, IT consultant, bookkeeper, prime contractor). Processes come from the BIA (P05).

**Risk tolerance.** The owner owns and accepts every risk. Because the same person proposes and approves, the owner applies three fixed rules:
- Low and Very Low: may be accepted, with the reason written in the register.
- Moderate: may be accepted only with a dated treatment plan or a written reason.
- High and Very High: must be treated with a dated plan. Not accepted as-is. Any risk that could put counterfeit or covered equipment on a DoD delivery is never accepted.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the missing-controls list in `../00_company-facts.md` section 4, the FAR 52.204-21 gap analysis (P03), the supply chain practices in SP 800-161 Rev. 1, and a walk through the accounts, laptop, router, and garage with the IT consultant.
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
| R-001 | Counterfeit or tampered products from a marketplace seller or broker reach customers or a DoD delivery | High | Written sourcing rule; OEM serial, seal, and firmware checks on receipt; quarantine | Owner | 2026-10-15 |
| R-002 | Wire payment redirected through a compromised supplier mailbox (already cost $2,340) | High | Call-back before any new payment details; pay marketplace sellers through the marketplace | Owner | 2026-09-15 |
| R-004 | CMMC Level 1 (Self) not achieved and affirmed by 2026-10-30, or affirmed without meeting all 15 requirements | High | Close every FAR gap by 2026-10-15; affirm only when all are met | Owner | 2026-10-30 |
| R-003 | Takeover of the accounting SaaS administrator account (no MFA, reused password) | Moderate | MFA; password manager; monthly sign-in review | Owner | 2026-09-15 |
| R-010 | Covered (Section 889) equipment on a DoD order, or a missed 1-business-day report | Moderate | Covered-manufacturer check on every DoD quote; reporting steps in P08 | Owner | 2026-10-15 |
| R-011 | Owner unavailable (single point of failure) | Moderate | Emergency sheet; sealed recovery codes; agreement with the prime | Owner | 2026-12-31 |

The three High risks share one cause: **the business trusts what arrives by email and from suppliers without checking it.** Counterfeit stock, redirected payments, and an unsupported compliance affirmation all come from accepting something at face value. Each fix is a habit plus a free setting: a call-back, a serial lookup, and a self-assessment done before signing.

A wrong affirmation is also a legal risk. The Affirming Official attests that every Level 1 requirement is implemented (32 CFR 170.22(a)(2)), so R-004 is treated by meeting all 15 requirements first, not by affirming on time.

## 4. Treatment summary
- **Free fixes first (by 2026-09-30):** MFA with an authenticator app on SYS-01 and email; call-back rule for payments; remove open file links; AI assistant training off and chats deleted; standard (non-administrator) laptop account; customer device passwords into a vault.
- **Budgeted (about $450 a year):** password manager, laptop and file backup service, a second Wi-Fi access point or router for a business-only network, and a key lockbox.
- **Before the CMMC Level 1 affirmation (by 2026-10-15):** sourcing rule and receiving checks (R-001), Section 889 screening (R-010), router firmware and network separation (R-008), media sanitization method (R-012), and garage access (R-013).
- **Accepted (Low):** R-015 (hurricane; SaaS is reachable from anywhere and distributors drop-ship commercial orders).

## 5. Approval
Owner, 2026-08-31: approved all treatment plans and the one acceptance. Next full review in August 2027 with the annual CMMC Level 1 self-assessment, or sooner after a new system, a new supplier type, a hire, a CUI request from the prime, or an incident.
