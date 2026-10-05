# Risk Register Report: Cris Santos Company | Energy | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (pipeline integrity engineering consultant) |
| Size tier | Sole Proprietorship (engineer-owner only, 0 employees) |
| Vertical | Energy |
| Method | NIST SP 800-30 Rev. 1 (qualitative 5-level scales; Tables G-5 and I-2) |
| Also supports | Client A supplier questionnaire (addendum s.11); "reasonable measures" under Fla. Stat. 501.171(2); "reasonable steps" to safeguard SSI under 49 CFR 1520.9(a)(1) |
| Prepared | 2026-08-14 by the engineer-owner, with the on-call IT support contractor (under NDA since 2026-08-07) |
| Risk owner and approver | Engineer-owner (owner, security lead, SSI custodian, and risk acceptor for every risk) |
| Approved | 2026-09-11 |

## 1. Scope and risk framing
**Scope.** The whole business as one system: SYS-01 to SYS-08, paper client files in the home office, the two subcontractors, and the client relationships that set security terms. Processes come from the BIA (P05).

**What makes this business different from other one-person firms.** The data is not the owner's. It belongs to three pipeline operators, and part of it is Client A's Sensitive Security Information. A disclosure can hurt a client's security, end the client relationship that brings half of revenue, and lead to a TSA civil penalty under 49 CFR 1520.17. Impact ratings reflect that.

**Risk tolerance.** The engineer-owner owns and accepts every risk. Because the same person proposes and approves, the owner applies three fixed rules:
- Low and Very Low: may be accepted, with the reason written in the register.
- Moderate: may be accepted only with a dated treatment plan or a written reason.
- High and Very High: must be treated with a dated plan. Never accepted as they are. Any risk involving SSI or a client safety decision rated High is never accepted.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the missing-controls list in `../00_company-facts.md` section 4, the gap analysis (P03), and a walk through the laptop, phone, SaaS accounts, sharing settings, and home office with the IT support contractor on 2026-08-13.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (other sources), and likelihood of adverse impact, each on the 5-level scale. Combined with **Table G-5**.
3. **Rate impact.** Table H-3 levels, using the BIA impact categories (P05 section 3).
4. **Determine risk.** **Table I-2.** The `overall_likelihood` and `risk_level` columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

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
| R-001 | Ransomware on the laptop with theft of client data, SSI, and W-9s | High | Standard daily account, password manager, encrypted offline backup, training, P08 runbook | Engineer-owner | 2026-10-30 |
| R-003 | Client A SSI disclosed through the shared folder or the unlocked paper copy | High | Separate SSI folder shared with no one; locked storage; marking; POL-01 SSI rules | Engineer-owner | 2026-09-30 |
| R-004 | Unencrypted USB backup drive lost or stolen | High | Hardware-encrypted drive; destroy the old one with a record | Engineer-owner | 2026-09-15 |
| R-005 | Accounting SaaS takeover (SSNs, fake bank details) | High | MFA and a unique passphrase | Engineer-owner | 2026-09-15 |
| R-008 | Late notice to Client A or TSA after an incident | Moderate | P08 runbook, printed contacts, walkthrough | Engineer-owner | 2026-09-30 |
| R-006 | Client A data in an unapproved AI service | Moderate | Avoid: no further use; deletion request; approval rule (P10) | Engineer-owner | 2026-09-30 |
| R-010 | Engineer-owner unavailable (single point of failure) | Moderate | Peer engineer arrangement; sealed recovery codes; second MFA key | Engineer-owner | 2026-12-31 |

The four High risks share two causes: **client data and SSI sit in places the owner never chose deliberately** (a shared project folder, an unlocked drawer, an unencrypted drive), and **two accounts that hold sensitive data have weak sign-in** (the accounting SaaS with a reused password, and a laptop used daily as administrator). Most fixes cost little: an encrypted drive, a password manager, a locked cabinet, and changed settings.

R-012 (an AI output error reaching a client recommendation) is Moderate only because the owner never used trial outputs in a deliverable. Its impact is Very High, because a missed leak signature or a misranked anomaly could delay a pipeline operator's safety decision. P10 sets the conditions for any future use.

## 4. Treatment summary
- **Free or low-cost fixes first (by 2026-09-30):** accounting MFA, password manager, encrypted backup drive, SSI folder and locked storage, anonymous links off, router password, AI deletion request, P08 printed and walked through.
- **Budgeted (about $400 a year plus a one-time $250):** password manager, hardware security keys, encrypted drive, cross-cut shredder, and a locking file cabinet.
- **Contract actions by 2026-10-30:** subcontractor security terms and Client A written approval of each subcontractor (R-007); return-or-destroy certificates for old projects (R-009); 2026 questionnaire answered from these deliverables (R-013).
- **By 2026-12-31:** peer engineer arrangement and sealed recovery codes (R-010); AI validation rules before any future tool (R-012).
- **Accepted (Low):** R-014 (hurricane; cloud files reachable from anywhere) and R-015 (suite outage; client portals hold the source data). R-011 is Low and still treated because the fix is free.

## 5. Approval
Engineer-owner, 2026-09-11: approved all treatment plans and the two acceptances. Next full review August 2027, or sooner after a new client, a new service, a subcontractor change, or an incident.
