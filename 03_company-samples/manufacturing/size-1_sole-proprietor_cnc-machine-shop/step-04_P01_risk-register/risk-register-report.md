# Risk Register Report: Cris Santos Company | Manufacturing | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (owner-operated CNC machine shop) |
| Size tier | Sole Proprietorship (owner-machinist only, 0 employees) |
| Vertical | Manufacturing (NAICS 332710) |
| Method | NIST SP 800-30 Rev. 1 (qualitative 5-level scales; Tables G-5 and I-2) |
| Why it matters here | The shop's first risk assessment. No regulation requires one from the shop, but it is the starting point for the CMMC Level 1 self-assessment and for answering OEM supplier questionnaires |
| Prepared | 2026-08-14 by the owner-machinist, with the on-call IT technician (under NDA since 2026-08-07) |
| Risk owner and approver | Owner-machinist (owner, security lead, and risk acceptor for every risk) |
| Approved | 2026-09-04 |

## 1. Scope and risk framing
**Scope.** The whole business as one system: the Shop Business Systems (SYS-01 to SYS-06 and SYS-09), the CNC controllers, paper travelers and records in the bay, the external services the owner uses (customer portals, the AI assistant), and the contracted services (IT technician, bookkeeper, outside processors, machine service technician). Business functions come from the BIA (P05).

**Risk tolerance.** The owner-machinist owns and accepts every risk. Because the same person proposes and approves, the owner applies three fixed rules (POL-01 4.4):
- Low and Very Low: may be accepted, with the reason written in the register.
- Moderate: may be accepted only with a dated treatment plan or a written reason.
- High and Very High: must be treated with a dated plan and are never accepted as they are. Any risk that could put a nonconforming part into a medical device, or cost the shop a main customer, is treated.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the missing-controls list in `../00_company-facts.md` section 4, the FAR 52.204-21 requirements (P03), and a walk through the laptop, router, machines, and SaaS accounts with the IT technician.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (other sources), and likelihood of adverse impact, each on the 5-level scale. Combined with **Table G-5**.
3. **Rate impact.** Table H-3 levels, using the BIA impact categories (cost, operations, contract, safety, reputation).
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
| R-001 | Ransomware on the shop laptop with theft of customer drawings | High | Separate backup with test restore; standard user account; network separation; training | Owner-machinist | 2026-10-31 |
| R-003 | Loss of the aerospace award (FAR 52.204-21 and CMMC Level 1 not met) | High | Close every FAR gap; self-assess; CAGE code; SPRS entry and affirmation | Owner-machinist | 2026-11-30 |
| R-006 | Unapproved change to a released OEM program ships nonconforming parts | High | Read-only released folder with hashes; compare before each run | Owner-machinist | 2026-12-31 |
| R-002 | Payment fraud through email or the accounting SaaS | Moderate | App-based MFA; phone verification of bank changes | Owner-machinist | 2026-09-30 |
| R-005 | VMC controller reached through the flat network or a service laptop | Moderate | Separate segment; guest Wi-Fi; share password; media check | Owner-machinist | 2026-10-31 |
| R-008 | Customer drawing content in a consumer AI assistant | Moderate | Stop for customer content; opt out; delete; G-code review rule (P10) | Owner-machinist | 2026-09-30 |

The three High risks have different causes but one lesson: **the shop's value is in customer drawings and programs, and today one laptop on one flat network holds all of it with no copy it cannot overwrite and no check that a program is the approved one.** R-003 is different in kind: it is certain to happen unless the owner acts, because Level 1 allows no plan of action. Each FAR 52.204-21 gap in P03 must be closed, not just scheduled, before the owner affirms in SPRS.

## 4. Treatment summary
- **Free fixes first (by 2026-09-30):** app-based MFA on accounting and email, the remote-support rule, the visitor log, the website review rule, the drawing intake screen, and stopping customer content in the AI assistant.
- **Budgeted (about $900 once and $250 a year):** a small business router with a guest network and a separate wired segment, an external backup drive kept disconnected plus a second cloud backup service, and a password manager.
- **Before the CMMC affirmation (by 2026-11-30):** every FAR 52.204-21 requirement met (P03), self-assessment run with SP 800-171A objectives, CAGE code and SPRS access obtained, results and affirmation entered.
- **Contract actions by 2026-10-31:** flowdown and NDA for any outside processor that must see an aerospace drawing (R-004); written notice to customers that bank details never change by email (R-002).
- **Accepted (Low):** R-015 (suite outage or lockout; the machines keep running and customer portals hold the drawings).

## 5. Approval
Owner-machinist, 2026-09-04: approved all treatment plans and the one acceptance. Next full review August 2027, or sooner after a new system, a new customer contract with security terms, a hire, or an incident.
