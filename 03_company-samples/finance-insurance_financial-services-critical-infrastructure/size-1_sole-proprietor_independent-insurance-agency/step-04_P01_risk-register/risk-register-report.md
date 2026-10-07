# Risk Register Report: Cris Santos Company | Financial Services | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent insurance agency) |
| Size tier | Sole Proprietorship (owner-agent only, 0 employees) |
| Vertical | Financial Services |
| Method | NIST SP 800-30 Rev. 1 (qualitative 5-level scales; Tables G-5 and I-2) |
| Also supports | The "reasonable measures" duty in Fla. Stat. 501.171(2), the risk assessment the insurers' data security addenda ask about, and the 16 CFR 314.4(b) benchmark. This is the agency's first risk assessment |
| Prepared | 2026-08-07 by the owner-agent, with the on-call IT consultant (services agreement since 2026-07-27) |
| Risk owner and approver | Owner-agent (owner, information security coordinator, and risk acceptor for every risk) |
| Approved | 2026-09-14 |

## 1. Scope and risk framing
**Scope.** The whole business as one system: SYS-01 to SYS-08, paper in the office and the garage, the premium trust account, and the contracted services (bookkeeper, IT consultant, insurers, wholesale broker, premium finance company). Processes come from the BIA (P05).

**Risk tolerance.** The owner-agent owns and accepts every risk. Because the same person proposes and approves, the owner applies three fixed rules:
- Low and Very Low: may be accepted, with the reason written in the register.
- Moderate: may be accepted only with a dated treatment plan or a written reason.
- High and Very High: must be treated with a dated plan. Not accepted as-is. Any risk that can move client premium (trust funds) to the wrong account is treated, whatever its rating.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the missing-controls list in `../00_company-facts.md` section 4, the 2026-07-08 near miss, the lead insurer's questionnaire, the gap analysis (P03), and a walk through the laptop, phone, router, and SaaS accounts with the IT consultant.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (other sources), and likelihood of adverse impact, each on the 5-level scale. Combined with **Table G-5**.
3. **Rate impact.** Table H-3 levels, using the BIA impact categories (cost, operations, regulatory, reputation).
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
| R-001 | Business email compromise of the agency mailbox | High | Authenticator app or security key; block outside forwarding; monthly review; training | Owner-agent | 2026-09-30 |
| R-002 | Clients pay premiums to a criminal's account after a fake invoice | High | Fixed trust account details on the invoice template; letter to clients; callback rule | Owner-agent | 2026-09-30 |
| R-005 | Fraudulent transfer through the shared banking identity | High | View-only sub-user for the bookkeeper; owner-only payment rights; transfer alerts | Owner-agent | 2026-09-30 |
| R-015 | Insurer or regulator action because no written program existed | Moderate | Questionnaire answered with this program and the POA&M | Owner-agent | 2026-09-30 |
| R-004 | Client information in a consumer AI chatbot | Moderate | Avoid: do not resume; delete; counsel review (P10) | Owner-agent | 2026-09-30 |
| R-009 | Owner unavailable (single point of failure) | Moderate | Emergency servicing arrangement; sealed recovery codes | Owner-agent | 2026-12-31 |

The three High risks share one cause: **the agency's money and mail move on trust, not on checks.** The mailbox that sends invoices is protected by a text code an attacker can relay, clients have no way to tell a real invoice from a fake one, and the bank sees the bookkeeper as the owner. Each fix is free or nearly free and is due before the questionnaire goes back to the lead insurer on 2026-09-30.

## 4. Treatment summary
- **Free fixes first (by 2026-09-30):** authenticator app or security key on email and banking, blocked outside forwarding, the invoice template and client letter, the bank sub-user, rater MFA, a password manager, and stopping the consumer AI chatbot.
- **Budgeted (about $400 a year):** a password manager, an email and file backup service with 1-year retention, and a security awareness course.
- **Contract actions by 2026-10-31:** confidentiality and security terms with the bookkeeper; review of the e-signature and rater vendors (R-005, R-006).
- **Accepted as-is:** none. All three Low risks (R-008, R-013, R-014) have cheap fixes, so the owner chose to treat them.

## 5. Approval
Owner-agent, 2026-09-14: approved all treatment plans. Next full review August 2027, or sooner after a new system, a new vendor, a hire, a new insurer addendum, or an incident.
