# Risk Register Report: Cris Santos Company | Government Services and Facilities | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (facilities support contractor operating government buildings, NAICS 561210) |
| Size tier | Sole Proprietorship (owner only, 0 employees) |
| Vertical | Government Services and Facilities |
| Method | NIST SP 800-30 Rev. 1 (qualitative 5-level scales; Tables G-5 and I-2) |
| Also satisfies | RA-3 of the SP 800-53 Rev. 5 Moderate baseline required by the city security exhibit (CT-C). This is the business's first risk assessment |
| Prepared | 2026-08-14 by the owner, with the on-call IT technician (under NDA since 2026-08-03). Status and existing-control columns updated 2026-08-21 after the P07 tests; ratings were not re-scored |
| Risk owner and approver | Owner (owner, security officer, and risk acceptor for every risk) |
| Approved | 2026-09-04 |

## 1. Scope and risk framing
**Scope.** The whole business as one system: the Building Systems Support Environment (SYS-01 to SYS-07, P02), the owner's accounts and access paths into the city's building systems (SYS-08), the CUI and FCI the owner holds for the federal subcontract, paper drawings, and the on-call IT technician. The city's and GSA's systems are not assessed here, but harm to them through the owner's access is. Processes and impact levels come from the BIA (P05).

**What makes this business different from most one-person businesses:** the owner holds administrator access to public buildings. A mistake or an intrusion through the owner's accounts can unlock doors, lock people in, or make an occupied library unsafe in the summer. Impact ratings use the BIA's safety and contract categories, not only the cost to the business.

**Risk tolerance.** The owner owns and accepts every risk. Because the same person proposes and approves, the owner applies three fixed rules (POL-01 4.4):
- Low and Very Low: may be accepted, with the reason written in the register.
- Moderate: may be accepted only with a dated treatment plan or a written reason.
- High and Very High: must be treated with a dated plan and are never accepted as they are. Any risk that could affect the safety of building occupants is told to the city facilities manager.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the missing-controls list in `../00_company-facts.md` section 4, the SaaS mapping (P04), and a walk through the laptop, phone, router, and accounts with the IT technician on 2026-08-11 and 2026-08-12.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (other sources), and likelihood of adverse impact, each on the 5-level scale, combined with **Table G-5**.
3. **Rate impact.** Table H-3 levels, using the BIA impact categories (cost, operations, contract, safety, reputation).
4. **Determine risk.** **Table I-2.** The `overall_likelihood` and `risk_level` columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results
| Risk level | Count |
|---|---|
| High | 3 |
| Moderate | 10 |
| Low | 2 |
| **Total** | **15** |

### Top risks
| Risk ID | Risk | Level | Treatment | Due |
|---|---|---|---|---|
| R-001 | Intrusion into the city BAS through the remote-desktop agent | High | Remove the agent; city VPN only | 2026-09-30 |
| R-002 | Misuse of the shared BAS supervisory administrator password (unchanged since 2023) | High | Password manager now; city changes it and issues a named account | 2026-10-31 |
| R-006 | Owner unavailable, nobody else can run the city buildings | High | Backup controls firm approved by the city; manual operation sheets; sealed emergency access | 2026-12-31 |
| R-005 | Only copies of controller programs on the laptop | Moderate | Cloud and drive backups; quarterly comparison | 2026-10-31 |
| R-008 | CUI drawings disclosed | Moderate | Restricted CUI folder; marking; training | 2026-10-31 |
| R-010 | Missed notice deadline after an incident | Moderate | P08 runbook and printed contact sheet | 2026-09-30 |
| R-011 | Unscreened part in the federal building | Moderate | Confirm or replace the switch; parts check | 2026-09-30 |

Two of the three High risks are **access paths into the city's BAS** that the owner set up or inherited and never told the city IT manager about in detail. Both can be closed cheaply: removing the agent costs nothing and ends a subscription, and the BAS password change needs only the city's agreement. The third High risk, the single-person dependency, cannot be removed by a one-person business. It can be reduced to Moderate with a backup firm and written manual steps, and the residual is recorded as Moderate in the register.

## 4. Treatment summary
- **Free fixes first (by 2026-09-30):** remove the remote-desktop agent (R-001), standard laptop account (R-004), keep only the two latest cardholder exports (R-009), adopt and print the P08 runbook (R-010), confirm or replace the switch (R-011), stop customer data going into the chatbot (R-013).
- **Budgeted (about $1,500 a year):** password manager, an owner-owned router, an encrypted external drive, more cloud storage for nightly backups of the engineering folder, and cyber insurance quotes (about $1,000 a year expected, to be confirmed).
- **Needs the city (by 2026-10-31 to 2026-12-31):** named BAS supervisory account and password change (R-002), approval of a backup controls firm (R-006), a written decision on the face verification add-on (R-014).
- **Avoided:** R-014. The owner will not configure the face verification add-on unless the P10 conditions are met.
- **Accepted (Low):** R-015 (hurricane). Controllers keep running, SaaS is reachable over the hotspot, and the city runs its own storm plan for its buildings.

## 5. Approval
Owner, 2026-09-04: approved all treatment plans, the avoidance of R-014, and the acceptance of R-015. The three High risks go to the city IT manager and the city facilities manager in writing with the owner's account list by 2026-09-30 (POL-01 7.8). Next full review August 2027, or sooner after a new contract, a new system or service, a hire or subcontractor, or an incident.
