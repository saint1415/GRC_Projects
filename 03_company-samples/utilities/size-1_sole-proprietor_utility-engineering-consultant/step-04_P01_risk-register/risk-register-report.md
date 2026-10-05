# Risk Register Report: Cris Santos Company | Utilities | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent utility engineering consultant) |
| Size tier | Sole Proprietorship (owner-engineer only, 0 employees) |
| Vertical | Utilities |
| Method | NIST SP 800-30 Rev. 1 (qualitative 5-level scales; Tables G-5 and I-2) |
| Also supports | Client A's annual security questionnaire and the client terms in SSA-A and VAA-B (P03). This is the business's first risk assessment |
| Prepared | 2026-07-24 by the owner-engineer, with the on-call IT technician (under NDA since 2026-07-17) |
| Risk owner and approver | Owner-engineer (owner, security lead, and risk acceptor for every risk) |
| Approved | 2026-08-31 |

## 1. Scope and risk framing
**Scope.** The whole business as one system: SYS-01 to SYS-08, paper in the home office, and the outside parties that touch client information (drafting subcontractor, IT technician, SaaS providers). Processes come from the BIA (P05).

**What makes this business different.** It owns no operational technology, but it carries two kinds of client risk: **client security information** (Client A BCSI, Client B settings and event records, FERC CEII) and **a path into client OT** (the laptop that connects to Client B relays and the Client B gateway account). A failure at the consultant can become a client's NERC CIP problem. Impact ratings therefore count harm to the clients, not only to the business.

**Risk tolerance.** The owner owns and accepts every risk. Because the same person proposes and approves, the owner applies three fixed rules:
- Low and Very Low: may be accepted, with the reason written in the register.
- Moderate: may be accepted only with a dated treatment plan or a written reason.
- High and Very High: must be treated with a dated plan. Not accepted as-is. Any risk that could put a client's protection system or BCSI at risk is never accepted at High.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the missing-controls list in `../00_company-facts.md` section 4, the client terms (SSA-A, VAA-B, the CEII NDA), the SaaS mapping (P04), and a walk through the laptop, phone, USB drives, and SaaS settings with the IT technician.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (other sources), and likelihood of adverse impact, each on the 5-level scale. Combined with **Table G-5**.
3. **Rate impact.** Table H-3 levels, using the BIA impact categories (P05), including harm to clients.
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
| R-001 | Phished email credentials expose BCSI, CEII, and gateway details | High | App-based MFA; password manager; BCSI only in the Client A portal; sign-in review; training | Owner-engineer | 2026-09-30 |
| R-002 | Malware on the multi-purpose laptop carried into Client B relays | High | Standard daily account; dedicated field laptop | Owner-engineer | 2026-12-31 |
| R-003 | MFA push fatigue opens a session into Client B's OT network | High | Password manager; reject and report unexpected pushes; number matching | Owner-engineer | 2026-09-30 |
| R-004 | Client A BCSI reached an unauthorized person (drafter share) | Moderate | Owner-only client folders; drafter access agreement; share review | Owner-engineer | 2026-09-30 |
| R-009 | Client C data in an AI SaaS without consent | Moderate | Consent or rebuild; deletion request; P10 rules | Owner-engineer | 2026-09-30 |
| R-013 | Incident missed or 24-hour client notice late | Moderate | P08 runbook, matrix, and contact sheet | Owner-engineer | 2026-09-30 |

The three High risks share one cause: **the owner's identity and laptop are the doorway to client systems, and both are protected like a home user's.** SMS codes, saved browser passwords, and an everyday administrator account would be ordinary at a home office, but here they guard BCSI, CEII, and a path into a utility's OT network. The fixes are mostly free (app-based MFA, a standard account, a rule never to approve an unexpected push) and one is budgeted (a dedicated field laptop, about $1,200).

R-004 is rated Moderate even though it already happened: the drafter is a known party who signed a confidentiality clause and a deletion statement, which keeps the likelihood of adverse impact Moderate. The harm that remains is to the Client A relationship and to Client A's own CIP-004-7 R6 record, which is Client A's decision.

## 4. Treatment summary
- **Free fixes first (by 2026-09-30):** app-based MFA, password manager, standard laptop account, photo sync off, dedicated USB drives, owner-only client folders, the P08 runbook and contact sheet, and stopping AI tools until clients consent.
- **Budgeted (about $1,500 the first year):** dedicated field laptop (about $1,200), password manager (about $40 a year), and an online security course (about $200).
- **Contract actions:** drafter access agreement (2026-09-30); Client C consent or rebuild of the forecast (2026-09-30); certification of the two 2025 Client A projects (2026-10-31); standby engineer and Client A pre-authorization request (2026-12-31).
- **Accepted (Low):** R-006 (device theft; both devices encrypted) and R-015 (hurricane; data is in SaaS and the laptop travels).

High and Moderate gaps found in the gap analysis (P03) are linked to these risks in the `regulatory_driver` column, and each High and Moderate control weakness has a POA&M item in P07.

## 5. Approval
Owner-engineer, 2026-08-31: approved all treatment plans and the two acceptances. Next full review July 2027, or sooner after a new client, a new tool, a new subcontractor, or an incident.
