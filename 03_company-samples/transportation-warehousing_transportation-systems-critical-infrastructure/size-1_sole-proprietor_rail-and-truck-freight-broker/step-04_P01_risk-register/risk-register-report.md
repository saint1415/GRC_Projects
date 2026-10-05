# Risk Register Report: Cris Santos Company | Transportation Systems | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (freight broker arranging truck and rail shipments) |
| Size tier | Sole Proprietorship (owner only, 0 employees) |
| Vertical | Transportation Systems |
| Method | NIST SP 800-30 Rev. 1 (qualitative 5-level scales; Tables G-5 and I-2) |
| Also supports | The "reasonable measures" duty in Fla. Stat. 501.171(2), and the largest shipper's contract requirement for reasonable safeguards. This is the business's first risk assessment |
| Prepared | 2026-08-14 by the owner, with the on-call IT consultant |
| Risk owner and approver | Owner (owner, security lead, and risk acceptor for every risk) |
| Approved | 2026-09-08 |

## 1. Scope and risk framing
**Scope.** The whole business as one system: SYS-01 to SYS-09, the railroad portals (SYS-10) and FMCSA registration account (SYS-11) as interfaces, the outside services, and the five business functions in the BIA (P05).

**Risk tolerance.** The owner owns and accepts every risk. Because the same person proposes and approves, the owner applies three fixed rules:
- Low and Very Low: may be accepted, with the reason written in the register.
- Moderate: may be accepted only with a dated treatment plan or a written reason.
- High and Very High: must be treated with a dated plan. Never accepted as they are. A risk that could leave a carrier unpaid or a load unwatched is never accepted above Low.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the missing-controls list in `../00_company-facts.md` section 4, the SaaS mapping (P04), and a walk through the laptop, phone, and every SaaS account with the IT consultant on 2026-08-11 and 2026-08-12. Freight fraud (payment diversion, carrier impersonation, double brokering) is included because it is the cyber-enabled loss a broker is most likely to suffer.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (other sources), and likelihood of adverse impact, each on the 5-level scale. Combined with **Table G-5**.
3. **Rate impact.** Table H-3 levels, using the BIA impact categories (P05 section 3).
4. **Determine risk.** **Table I-2.** The `overall_likelihood` and `risk_level` columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.
5. **Close the loop.** R-014 was added on 2026-08-13 from the P07 test that found a forgotten administrator account.

## 3. Results
| Risk level | Count |
|---|---|
| High | 4 |
| Moderate | 8 |
| Low | 3 |
| **Total** | **15** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware on the laptop with theft of carrier packets | High | Offline export; stop syncing packets; separate network; training; runbook | Owner | 2026-12-31 |
| R-002 | Carrier payment diverted by a fake bank detail change | High | Call-back to the number on file; 5-day hold after a change; bank alerts | Owner | 2026-09-30 |
| R-003 | Business email takeover used to send fake invoices to shippers | High | Authenticator app and hardware key; port-out PIN; password manager | Owner | 2026-09-30 |
| R-004 | Carrier impersonation or double brokering leading to cargo theft | High | Identity check before the first load; tracking on every load; no-re-brokering terms | Owner | 2026-10-31 |
| R-009 | Owner unavailable (single point of failure) | Moderate | Backup broker agreement; sealed access sheet; attorney authorization | Owner | 2026-12-31 |
| R-012 | AI document capture misses POD exceptions; automatic carrier pay | Moderate | Automatic approval off; human review of every POD; training opt-out (P10) | Owner | 2026-09-30 |

The four High risks share one pattern: **the money and the freight both move on the strength of an email.** A carrier is booked because an email and an MC number look right; a bank detail changes because an email asks; a shipper pays an invoice because it came from the broker's address. Three free changes cut this sharply: a call-back rule for bank detail changes (R-002), an identity check before a carrier's first load (R-004), and phishing-resistant MFA with a port-out PIN on the email account (R-003).

## 4. Treatment summary
- **Free fixes first (by 2026-09-30):** call-back rule and bank alerts, MFA on the TMS, accounting, and load board, authenticator app on email, port-out PIN, FMCSA account recovery moved to the business email, automatic POD approval turned off, and the forgotten admin account deleted.
- **Budgeted (about $400 a year):** a password manager, two hardware security keys, and an encrypted offline drive for monthly exports.
- **Contract and process actions by 2026-12-31:** individual railroad portal user ID (R-007), backup broker agreement and attorney authorization (R-009), retention schedule and first disposal (R-011).
- **Accepted (Low):** R-015 (hurricane; all systems are SaaS and reachable over a hotspot). R-010 and R-011 are Low but still get their low-cost steps.

## 5. Approval
Owner, 2026-09-08: approved all treatment plans and the one acceptance. Next full review August 2027, or sooner after a new system, a new service line (for example, hazmat or quick pay), a hire, or an incident.
