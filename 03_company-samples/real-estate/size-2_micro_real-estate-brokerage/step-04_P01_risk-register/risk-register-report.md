# Risk Register Report: Cris Santos Company | Real Estate and Rental and Leasing | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (residential real estate brokerage with property management) |
| Size tier | Micro (7 employees; about 22 contractor sales associates) |
| Vertical | Real Estate and Rental and Leasing |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also serves as | The written risk assessment in the benchmark Safeguards Rule element 16 CFR 314.4(b) (not binding on this brokerage; P03 section 1), and documentation of "reasonable measures" under Fla. Stat. 501.171(2) |
| Prepared | 2026-08-07 by the Office Manager (security and compliance lead) with the MSP lead technician |
| Updated | 2026-08-18 (R-025 added from P07 testing); 2026-09-14 (R-020 and R-021 accepted and closed) |
| Approved | 2026-09-14 by the Broker-owner |

## 1. Scope and risk framing
**Scope.** The whole business and its key vendors: every system in `../00_company-facts.md` section 3 (SYS-01 to SYS-10), paper files, the office, and the vendors that hold client data or run systems for the brokerage: the productivity suite, transaction platform, e-signature, property management platform (with its screening provider), and backup vendors, the MSP, and the escrow bank.

**Who can accept risk:**
- Very Low and Low: the Office Manager may accept.
- Moderate: only the Broker-owner may accept, with a treatment plan or a written reason.
- High and Very High: not accepted. The Broker-owner approves a dated treatment plan instead. Any risk to escrowed or client funds rated High is never accepted.

This is the brokerage's first documented risk assessment.

**Overlap of roles.** The Office Manager who wrote this register also runs most of the controls it rates. The independent assessment in August 2026 (P07) is the check on this work, and it added R-025.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA (P05), the gap analysis (P03), the May 2026 near miss, and interviews with the Broker-owner, the Office Manager, the Bookkeeper, both Transaction Coordinators, the Property Manager, three contractor agents, and the MSP lead technician (2026-07-27 to 2026-08-07).
2. **Rate likelihood.** For each event, the likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood that it causes adverse impact were rated, then combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories (P05 section 3). A diverted closing wire ($60,000 to $250,000) or control of every mailbox is rated High.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results
| Risk level | Count |
|---|---|
| High | 3 |
| Moderate | 14 |
| Low | 8 |
| **Total** | **25** |

Status: 8 In progress, 15 Open, 2 Closed (R-020 and R-021 accepted). Treatment: 23 Mitigate, 2 Accept.

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Agent mailbox takeover; buyer sent altered closing wire instructions | High | MFA for every account; block legacy protocols; forwarding and sign-in alerts; instructions only through client document sharing; buyer call-first warnings; agent training | Office Manager | 2026-10-31 |
| R-002 | Brokerage wires a held deposit on spoofed title company instructions | High | Written verification rule with callback to a known number; approver checks the callback record | Broker-owner | 2026-09-30 |
| R-006 | Shared global administrator without MFA controls the whole email tenant | High | Named administrator accounts with MFA; shared account disabled; sealed break-glass account | Office Manager | 2026-09-30 |
| R-013 | MSP tool or backup login compromise | Moderate | Annual MSP review; contract terms for MFA, 24-hour notice, recovery time | Broker-owner | 2026-12-31 |
| R-008 | Mail and files cannot be restored | Moderate | Back up all 29 mailboxes; monthly SYS-01 export; quarterly restore tests | Office Manager | 2026-12-31 |
| R-016 | Tenant screening produces unjustified disparate denials | Moderate | P10 conditions: written criteria, human review, individualized record review | Property Manager | 2026-11-30 |

**The common theme is the email channel.** All three High risks end in money or control moving because someone trusted an email: an agent's unprotected mailbox (R-001), an unverified title company message (R-002), or a single unprotected administrator password (R-006). Their treatments are mostly free settings and one written rule, and they also reduce R-003, R-004, R-005, and R-025.

**Found or fixed during the work:**
- On 2026-07-30 an agent who had left on 2026-07-17 was found with active email and transaction platform accounts. They were disabled the same day; the two sign-ins after departure touched only the agent's own files. The process gap remains open (R-009).
- R-025 was added on 2026-08-18 after P07 testing found 3 agent mailboxes forwarding all mail to personal webmail. The rules were removed on 2026-08-19.
- The May 2026 near miss (a spoofed title company email) is now recorded as the first entry in the incident log (P08).

## 4. Treatment summary
- **Funded (2026 Q4, approved by the Broker-owner; about $6,000 one-time and $3,500 a year):**
  - MFA for agents, legacy protocol blocking, named administrator accounts, forwarding block, and alert set-up: settings in existing services, about 6 hours of MSP time ($900)
  - Backup extended to all 29 mailboxes: about $700 a year
  - Security training with a wire fraud module and quarterly phishing simulations for 7 employees and 22 agents: about $900 a year
  - Desktop encryption, first restore test, and device clean-up by the MSP: about $600 of MSP time
  - Hardware token for the second approval device (R-023): about $100
  - Counsel review of screening criteria and the adverse action template (R-016, R-017): about $1,500 one-time
  - Independent assessment (P07): about $2,900 one-time
  - MSP behavior-based detection at contract renewal (R-007): about $1,900 a year, from 2027
- **Accepted:** R-020 (Low; vendor recovery commitments meet the BIA) by the Broker-owner, and R-021 (Low; all services reachable without the office line) by the Office Manager.
- **Contract actions:** MSP amendment (R-013) and SaaS vendor breach notice terms (R-014) at renewal; agent agreement security addendum (R-009) by 2026-12-31.

## 5. Approval
- Broker-owner: approved all treatment plans, the acceptance of R-020, and the budget on 2026-09-14.
- Next full review: July 2027, or sooner after a major change (for example, a new transaction platform or adding closing services, which would bring the Safeguards Rule into force) or an incident.
