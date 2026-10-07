# Risk Register Report: Cris Santos Company | Emergency Services | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (unarmed private security patrol, licensed Class "B" agency) |
| Size tier | Sole Proprietorship (owner only, 0 employees) |
| Vertical | Emergency Services |
| Method | NIST SP 800-30 Rev. 1 (qualitative 5-level scales; Tables G-5 and I-2) |
| Also supports | "Reasonable measures" to protect personal information, Fla. Stat. 501.171(2). No statute requires a written risk assessment for this business; this is its first one |
| Prepared | 2026-08-14 by the owner, with the on-call IT technician (confidentiality agreement since 2026-08-07) |
| Risk owner and approver | Owner (risk owner and risk acceptor for every risk) |
| Approved | 2026-08-31 |

## 1. Scope and risk framing
**Scope.** The whole business as one system: SYS-01 to SYS-07, client keys, cards, and codes held in trust, paper records at the home office, and the outside parties (patrol app vendor and its AI model provider, email and accounting providers, IT technician, backup patrol agency). Processes come from the BIA (P05).

**What makes this business different.** Its most sensitive data is not about the owner's customers as consumers. It is the **means to enter client property**: alarm codes, gate codes, keys, and post orders. A leak of that data can lead straight to a burglary, a lost contract, and discipline under Fla. Stat. 493.6118(1)(e), which treats "any unauthorized release of information acquired as a result of activities regulated under this chapter" as grounds for action against the license.

**Risk tolerance.** The owner owns and accepts every risk. Because the same person proposes and approves, the owner applies three fixed rules:
- Low and Very Low: may be accepted, with the reason written in the register.
- Moderate: may be accepted only with a dated treatment plan or a written reason.
- High and Very High: must be treated with a dated plan. Not accepted as-is. Any risk to people's safety at a client site rated High is never accepted.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the missing-controls list in `../00_company-facts.md` section 4, the gap analysis (P03), and a walk through the laptop, phone, patrol app, vehicle, and SaaS accounts with the IT technician on 2026-08-12.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (other sources), and likelihood of adverse impact, each on the 5-level scale. Combined with **Table G-5**.
3. **Rate impact.** Table H-3 levels, using the BIA impact categories (cost, operations, regulatory, safety, reputation).
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
| R-001 | Ransomware on the shared laptop encrypts the synced drive, including the code spreadsheet | High | Separate accounts; versioned backup; codes out of the spreadsheet; training | Owner | 2026-10-31 |
| R-002 | Takeover of the patrol app admin account (reused password, no MFA) | High | App-based MFA; password manager; monthly sign-in review | Owner | 2026-09-15 |
| R-003 | Client codes exposed and used to enter a client site | High | Codes into an encrypted vault plus one sealed paper copy; delete spreadsheet, note, and texts | Owner | 2026-09-15 |
| R-008 | AI assistant labels an urgent event as routine (near miss 2026-07-19) | Moderate | Owner sets every priority; phone call for urgent events | Owner | 2026-08-31 |
| R-007 | Owner unavailable (single point of failure) | Moderate | Written backup agency agreement; sealed code book | Owner | 2026-12-31 |
| R-004 | Client keys lost or stolen from the vehicle | Moderate | Coded tags; vehicle lockbox; monthly count | Owner | 2026-10-31 |

The three High risks share one cause: **the codes that open client sites are stored in ordinary files and accounts that are protected only by passwords.** The spreadsheet sits in a consumer drive synced to a shared laptop (R-001), the patrol app post orders sit behind a reused password (R-002), and the same codes sit in a phone note and text threads (R-003). Moving every code into one encrypted vault, turning on app-based MFA, and deleting the copies cost almost nothing and reduce all three within two weeks of adoption.

## 4. Treatment summary
- **Free or low-cost fixes first (by 2026-09-30):** MFA on the patrol app admin account and email, password manager, codes into the vault and the sealed paper copy, longer phone passcode with hidden previews, separate laptop accounts, owner-set priorities in the AI assistant, and the P08 runbook.
- **Budgeted (about $250 a year plus a one-time $150):** password manager (about $40 a year), a versioned backup service (about $100 a year), a business email and file plan to replace the consumer account (about $110 a year), and a bolted vehicle lockbox (about $150). The home safe was bought 2026-08-20.
- **Contract and client actions by 2026-10-31:** remove stale portal accounts and require MFA for client users (R-009); tell clients to stop texting codes and how bank changes are announced (R-003, R-010); expire public video links (R-006). Written backup agency agreement by 2026-12-31 (R-007).
- **Avoided:** R-013 (criminal justice information): POL-01 9.6 forbids accepting it, which keeps the business outside the CJIS Security Policy.
- **Accepted (Low):** R-014 (hurricane; contracts suspend patrols during declared storm emergencies) and R-015 (patrol app outage; offline mode and the paper log cover a shift).

## 5. Approval
Owner, 2026-08-31: approved all treatment plans and the two acceptances. Next full review August 2027, or sooner after a new system, a new client type, a hire, or an incident.
