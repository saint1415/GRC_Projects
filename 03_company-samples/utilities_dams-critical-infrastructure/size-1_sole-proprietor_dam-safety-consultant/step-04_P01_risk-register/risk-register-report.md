# Risk Register Report: Cris Santos Company | Dams | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent dam safety engineering consultant) |
| Size tier | Sole Proprietorship (owner-engineer only, 0 employees) |
| Vertical | Dams |
| Method | NIST SP 800-30 Rev. 1 (qualitative 5-level scales; Tables G-5 and I-2) |
| Also supports | The threat and resource assessment that Client A's agreement asks the consultant to share (Rev. 3A Form 3 Q23a-23b) and the CEII duty to keep CEII in a secure place (18 CFR 388.113(h)(2)). This is the business's first risk assessment |
| Prepared | 2026-07-24 by the owner-engineer, with the on-call IT technician (under NDA since 2026-07-14) |
| Risk owner and approver | Owner-engineer (owner and risk acceptor for every risk) |
| Approved | 2026-08-31 |

## 1. Scope and risk framing
**Scope.** The whole business as one system: SYS-01 to SYS-08, the USB backup drive, paper in the home office, the field assistant, and the owner's accounts on client-operated systems (`../00_company-facts.md` section 3). Processes come from the BIA (P05). Client A's own control systems are outside scope; the risk the consultant brings to them is in scope.

**Risk tolerance.** The owner-engineer owns and accepts every risk. Because the same person proposes and approves, the owner applies three fixed rules:
- Low and Very Low: may be accepted, with the reason written in the register.
- Moderate: may be accepted only with a dated treatment plan or a written reason.
- High and Very High: must be treated with a dated plan. Not accepted as is. Any risk that could give an outsider a path into a client's dam control systems is never accepted at High.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the missing-controls list in `../00_company-facts.md` section 4, the client agreements (CSCA-A, GRS-B), the CEII rules, and a walk through the laptop, phone, accounts, and home office with the IT technician on 2026-07-21 and 2026-07-22.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (other sources), and likelihood of adverse impact, each on the 5-level scale. Combined with **Table G-5**.
3. **Rate impact.** Table H-3 levels, using the BIA impact categories (P05 section 3). Harm to a client, or to people downstream of a client's dam, counts as well as harm to the business.
4. **Determine risk.** **Table I-2.** The `overall_likelihood` and `risk_level` columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results
| Risk level | Count |
|---|---|
| High | 2 |
| Moderate | 9 |
| Low | 4 |
| **Total** | **15** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Infostealer on the laptop takes the Client A gateway credentials and session | High | Standard account, password manager, hotspot for sessions, training, P08 runbook | Owner-engineer | 2026-09-30 |
| R-005 | Unencrypted USB backup with CEII lost or stolen | High | Encrypted drive; old one wiped; locked cabinet | Owner-engineer | 2026-09-30 |
| R-002 | Client A security-sensitive material kept outside the portal | Moderate | Portal-only rule; Client A view-only setting; monthly search | Owner-engineer | 2026-09-30 |
| R-009 | Missed 24-hour client notice or FERC CEII report | Moderate | P08 runbook, matrix, printed contacts, walkthrough | Owner-engineer | 2026-09-30 |
| R-012 | Owner unavailable; FERC approval and CEII access are personal | Moderate | Peer engineer; sealed emergency sheet; client call list | Owner-engineer | 2026-12-31 |
| R-013 | Signing certificate stolen; forged sealed report | Moderate | Hardware token with a PIN | Owner-engineer | 2026-12-31 |

**The two High risks share one cause: the business carries client keys and CEII on devices built for convenience.** The laptop runs every task in an administrator account and its browser remembers the gateway password; the backup drive copies everything, including CEII, with no encryption. Both fixes are cheap and take days. The deeper point for this vertical is that a consultant's laptop is part of the dam owner's attack surface. Client A's MFA and view-only role limit what an attacker can do, but they cannot tell a stolen session from the owner (P08).

## 4. Treatment summary
- **Free or low-cost fixes first (by 2026-09-30):** MFA on the accounting SaaS and Client B platform, standard daily account, password manager, photo sync off, encrypted backup drive with a restore test, portal-only rule for security-sensitive material, and the P08 runbook walkthrough.
- **Budgeted (about $700 in the first year):** password manager, encrypted backup drive, hardware token for the signing certificate, a business router for a separate network, and a short annual security course.
- **Contract and client actions by 2026-10-31:** field assistant agreement and Client A approval (R-011); certificate of destruction to the former client (R-010); keep the AI vendor's deletion confirmation for Client B (R-007).
- **Share:** a cyber insurance quote is part of the R-001 plan; the professional liability policy excludes cyber costs.
- **Accepted (Low):** R-014 (suite outage; provider commitments and phone fallback meet the BIA) and R-015 (hurricane; work moves with the owner).

## 5. Approval
Owner-engineer, 2026-08-31: approved all treatment plans and the two acceptances. Next full review July 2027, or sooner after a new client, a new system or vendor, a hire or subcontractor, or an incident.
