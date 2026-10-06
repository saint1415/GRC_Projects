# Risk Register Report: Cris Santos Company | Real Estate and Rental and Leasing | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (residential real estate brokerage) |
| Size tier | Sole Proprietorship (broker-owner only, 0 employees) |
| Vertical | Real Estate and Rental and Leasing |
| Method | NIST SP 800-30 Rev. 1 (qualitative 5-level scales; Tables G-5 and I-2) |
| Also supports | The "reasonable measures" duty in Fla. Stat. 501.171(2), and the written risk assessment element of the FTC Safeguards Rule used as a benchmark (16 CFR 314.4(b); not binding here, P03 section 1) |
| Prepared | 2026-08-21 by the broker-owner, with the on-call IT technician (confidentiality agreement since 2026-08-14) |
| Risk owner and approver | Broker-owner (owner, broker, security lead, and risk acceptor for every risk) |
| Approved | 2026-09-15 |

## 1. Scope and risk framing
**Scope.** The whole business as one system: SYS-01 to SYS-11, the sales escrow account, paper files in the home office, and the three contracted services (transaction coordinator, bookkeeper, IT technician). Processes come from the BIA (P05).

**What makes this business different.** Most of the harm in a brokerage does not come from losing data. It comes from **someone believing a false instruction to move money**. A buyer's closing wire can be larger than the brokerage's yearly income, and once the receiving bank accepts it the money is usually gone within hours. The register is built around that fact.

**Risk tolerance.** The broker-owner owns and accepts every risk. Because the same person proposes and approves, the owner applies three fixed rules:
- Low and Very Low: may be accepted, with the reason written in the register.
- Moderate: may be accepted only with a dated treatment plan or a written reason.
- High and Very High: must be treated with a dated plan. Not accepted as they are. Any risk to client funds rated High is never accepted.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the missing-controls list in `../00_company-facts.md` section 4, the May 2026 near miss, the gap analysis (P03), and a walk through the mailbox, phone, laptop, router, and SaaS accounts with the IT technician on 2026-08-19 and 2026-08-20.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (other sources), and likelihood of adverse impact, each on the 5-level scale. Combined with **Table G-5**.
3. **Rate impact.** Table H-3 levels, using the BIA impact categories (P05 section 3).
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
| R-001 | Mailbox takeover; buyer sent altered closing wire instructions | High | Phishing-resistant MFA, forwarding blocks and alerts, wire procedure, training | Broker-owner | 2026-10-31 |
| R-002 | Look-alike domain sends fake wire instructions | High | DMARC, signed wire safety notice, pre-closing call | Broker-owner | 2026-10-31 |
| R-004 | Coordinator uses the owner's password and text codes | High | Separate login with its own MFA; written terms | Broker-owner | 2026-09-30 |
| R-003 | Earnest money deposit diverted on spoofed escrow instructions | Moderate | Secure sharing and phone confirmation of escrow instructions | Broker-owner | 2026-10-31 |
| R-011 | Screening recommendation used as the decision | Moderate | Written criteria, owner review, adverse action notices (P10) | Broker-owner | 2026-11-30 |
| R-010 | Broker-owner unavailable (single point of failure) | Moderate | Backup broker, sealed recovery codes, bank answer | Broker-owner | 2026-12-31 |

The three High risks share one cause: **the brokerage trusts email as if it were a verified channel for money instructions**, and its mailbox is protected by a text code that two people use. Two changes do most of the work: one identity per person with phishing-resistant MFA (R-001, R-004), and a rule that no money moves until someone calls a number they did not get from an email (R-001, R-002, R-003). Both cost almost nothing.

## 4. Treatment summary
- **No-cost fixes first (by 2026-09-30):** separate coordinator login, authenticator app or security key on email, platform, and banking, password manager, separate family laptop account, no client data in the AI writing assistant.
- **Budgeted (about $400 a year):** two security keys, a password manager, a SaaS backup for mail and files, and a short security course for the owner and the coordinator.
- **Procedure and contract actions by 2026-10-31:** written wire procedure and client wire safety notice (R-001 to R-003), written terms with the coordinator and bookkeeper (R-004, R-007), runbook and confirmed contacts (R-013), DMARC (R-002).
- **Accepted (Low):** R-015 (hurricane; every core system is reachable over the phone's cellular connection).

## 5. Approval
Broker-owner, 2026-09-15: approved all treatment plans and the one acceptance. Next full review August 2027, or sooner after a new system, a new contractor, a first hire or affiliated sales associate, a change in services (for example, acting as closing agent, which would bring the FTC Safeguards Rule into force), or an incident.
