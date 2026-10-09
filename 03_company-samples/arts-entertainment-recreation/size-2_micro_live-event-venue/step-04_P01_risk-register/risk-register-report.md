# Risk Register Report: Cris Santos Company | Arts, Entertainment, and Recreation | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (live event venue operator with ticketing; one music club) |
| Size tier | Micro (7 employees) |
| Vertical | Arts, Entertainment, and Recreation |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also supports | PCI DSS v4.0.1 Requirement 12.3 (risk identification) and FTC Act Section 5 reasonable security (N71-R04, N71-R05) |
| Prepared | 2026-07-24 by the Venue Manager (Security and Privacy Lead) with the MSP account technician |
| Updated | 2026-08-12 (R-023 added from P07 testing) |
| Approved | 2026-08-31 by the Owner and General Manager |

## 1. Scope and risk framing
**Scope.** The business and its key vendors: the Ticketing and Venue Operations Platform (TVOP) defined in the SSP (P02), both merchant accounts (MID-T and MID-F), the business functions in the BIA (P05), and the vendors that hold patron or card data or run systems for the company: the ticketing vendor, the payment partner, the POS vendor, the MSP, the website builder and the freelance web designer, the email marketing service, and the staffing contractors (SYS-01 to SYS-12 in the intake [asset inventory](../step-00_P00_intake/asset-inventory.csv) and the [vendor register](../step-00_P00_intake/vendor-register.csv)).

**Risk tolerance and who can accept risk:**
- Low and Very Low: the Venue Manager may accept.
- Moderate: only the Owner and General Manager may accept, with a treatment plan or a written reason.
- High and Very High: not accepted. The Owner approves a dated treatment plan instead. Risks to attendee safety at High are never accepted.

This is the company's first documented risk assessment.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA (P05), the intake evidence, the gap analysis (P03), interviews with all 7 employees and the MSP account technician (2026-07-13 to 2026-07-24, EV-045), and observation of two show nights (2026-07-17 and 2026-07-18, EV-052 and EV-053) and an on-sale (2026-07-21, EV-047). The gap analysis ran in the same fieldwork window, and the two shared findings.
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**. Each rating rests on evidence named in the `likelihood_basis` column: the vendor console and MSP exports, the acquirer records, the contracts folder, the walk-throughs and show-night observations, the account comparison of 2026-07-21 (EV-046) and the interviews. A rating with no evidence behind it would be a guess, so none was made.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories (cost, operations, contractual and regulatory, attendee safety, reputation). For a club with about $7,300 of revenue per show and about 47,000 patron records, a card skimming event across the online channel or the loss of the ticketing merchant account is rated High.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 4 |
| Moderate | 14 |
| Low | 5 |
| **Total** | **23** |

Status: 9 In progress, 13 Open, 1 Closed (R-018 accepted). Treatments: 19 Mitigate, 2 Avoid, 1 Share/Transfer, 1 Accept.

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Fake payment form placed over the checkout widget on the website event pages | High | Named website logins with MFA; remove scripts; weekly page check; ASV scans | Marketing Coordinator | 2026-09-30 |
| R-002 | Takeover of a ticketing account, then patron export or fraudulent refunds | High | Enforce MFA; named door logins; no export right for marketing; weekly check | Box Office and Ticketing Manager | 2026-09-30 |
| R-014 | Advertised ticket prices omit the mandatory fees (16 CFR 464.2) | High | Total price in every display; pre-publication checklist | Marketing Coordinator | 2026-09-30 |
| R-005 | 2026 PCI DSS validation fails or is filed wrongly | High | Scope decision (P03 Option B); evidence file; ASV scans | Owner and General Manager | 2026-12-15 |
| R-003 | Malware on the back-office PC captures phone-order card numbers | Moderate | Avoid: stop taking card numbers by phone | Box Office and Ticketing Manager | 2026-09-30 |
| R-004 | Card numbers in the shared box office mailbox exposed | Moderate | Avoid: purge (done 2026-08-03) and never accept card numbers by email | Box Office and Ticketing Manager | 2026-09-15 |

**The theme of the High risks: the company's own logins and pages are the weak point, not the vendors.** The ticketing vendor's widget, the P2PE readers, and the vendors' PCI DSS controls are sound. A shared website login lets an attacker change the page around the widget (R-001), unprotected ticketing logins let an attacker export patrons (R-002), and the company's own advertising breaks the FTC fee rule (R-014). R-001 and R-002 together are the P08 incident scenario. Their treatments also reduce R-004, R-006, R-007, and R-023.

R-005 is a business risk rather than a security event, but it is rated High because MID-T carries about $610,000 a year in ticket revenue. The cheapest treatment, which is to stop taking card numbers by phone or email, **avoids** R-003 and R-004 rather than mitigating them, and it is what makes a reduced SAQ possible (P03 section 1.2).

**Risks that were fixed or found during the work:**
- R-006: the former Marketing Coordinator's ticketing account was disabled on 2026-07-21, the day the account comparison found it (EV-046). The ticketing audit log showed no sign-ins after the departure date. The process gap remains open.
- R-004: the MSP purged the 23 emails with card numbers on 2026-08-03 (EV-059). The process change is still open.
- R-011: the spare door reader was locked in the back office safe on 2026-07-22 (EV-057).
- R-023: added on 2026-08-12 after P07 testing found a 2024 API token still sending patron records every night to a lapsed email marketing account (EV-SA-9). The token was revoked on 2026-08-12.

**Two passes.** Pass 1 was completed on 2026-07-24 from intake and fieldwork evidence. Pass 2 followed the control assessment (P07): R-023 was added on 2026-08-12 from P07 testing. The `assessment_pass` column shows which pass produced each risk.

## 4. Treatment summary
- **Funded (2026 Q4, approved by the Owner; about $5,700 one-time and $2,160 a year, fictional):**
  - MSP-managed EDR with after-hours alerting on the 5 office computers: about $900 a year
  - Security awareness training with phishing simulations for 7 employees: about $500 a year
  - Quarterly ASV scans of the website: about $400 a year
  - Cellular failover router: about $400 one-time and $360 a year
  - MSP project time (separate staff network, encryption of the Owner's laptop, MFA on MSP-held consoles, shared mailboxes added to the backup, restore tests): about $1,800
  - Independent assessment and policy work in 2026 (P07, P06): about $3,500 one-time
- **No-cost actions due by 2026-09-30:** MFA in the ticketing platform and on the website, named door logins, script removal, total-price displays, stopping card numbers by phone and email, and a reader inventory.
- **Offset:** a PCI DSS validation on file ends the acquirer's non-validation fees on both accounts (about $960 a year, fictional).
- **Accepted:** R-018 (Low; the vendor's bot screening and queue are the control at about 6 high-demand on-sales a year).
- **Shared or transferred:** R-022 through the vendor contracts (AOC and SOC 2 review, a 72-hour breach notice term at renewal) and cyber insurance. The Owner must confirm whether the policy covers card brand assessments.

## 5. Approval
- Owner and General Manager: approved all treatment plans, the acceptance of R-018, and the budget on 2026-08-31, and will decide the P03 scope option by 2026-09-30.
- Next full review: July 2027, or sooner after a major change (for example a new payment channel or ticketing platform) or an incident.
