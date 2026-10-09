# Risk Register Report: Cris Santos Company | Arts, Entertainment, and Recreation | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (live event venue operator with ticketing) |
| Size tier | Small (60 employees) |
| Vertical | Arts, Entertainment, and Recreation |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also supports | PCI DSS v4.0.1 Requirement 12.3 (risk identification) and FTC Act Section 5 reasonable security (N71-R04, N71-R05) |
| Prepared | 2026-07-24 by the IT Manager (Information Security Lead); R-019 added 2026-08-07 |
| Approved | 2026-08-31 by the General Manager (Moderate and below) and the majority owner (High) |

## 1. Scope and risk framing
**Scope.** The Ticketing and Venue Operations Platform (TVOP) defined in the SSP (P02), both merchant accounts (MID-T and MID-F), the business processes in the BIA (P05), and the vendors that hold patron or card data for the company ([asset inventory](../step-00_P00_intake/asset-inventory.csv) and [vendor register](../step-00_P00_intake/vendor-register.csv)).

**Risk tolerance and who can accept risk:**
- Low and Very Low: the IT Manager may accept.
- Moderate: the General Manager may accept, with a treatment plan or a documented reason.
- High and Very High: only the majority owner may accept, and only temporarily with a dated treatment plan. Risks to attendee safety at High are not acceptable.

This is the company's first documented risk assessment.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA, the intake evidence, interviews with the Director of Ticketing, Controller, Marketing Director, and Operations Director (EV-050), and observation of an on-sale (2026-07-17, EV-052) and a show night (2026-07-18, EV-053). The gap analysis (P03) ran in the same fieldwork window, and the two shared findings.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**. Each rating rests on evidence named in the `likelihood_basis` column: configuration exports, module settings, the document request, contracts, observations and interviews. A rating with no evidence behind it would be a guess, so none was made.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories (cost, operations, contractual and regulatory, attendee safety, reputation).
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 5 |
| Moderate | 21 |
| Low | 8 |
| **Total** | **34** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Takeover of a venue administrator account on the ticketing platform, then patron export and checkout changes | High | Enforce MFA; cut admins to 3; alerts on admin and checkout changes | IT Manager | 2026-09-30 |
| R-002 | Skimming script on the checkout page | High | Remove company-added scripts; restrict marketing settings; vendor change alerts | Marketing Director | 2026-09-30 |
| R-005 | 2026 PCI DSS validation fails and the ticketing merchant account is at risk | High | Scope reduction decision (P03 Option B); evidence file per SAQ answer | Controller | 2026-12-15 |
| R-015 | Advertised ticket prices omit mandatory fees (16 CFR 464.2) | High | Total price in every price display; pre-publication check | Marketing Director | 2026-09-30 |
| R-021 | Business email compromise redirects an artist settlement payment | High | Callback verification; phishing training for finance and booking | Controller | 2026-10-31 |
| R-003 | Malware on a box office PC captures phone-order card numbers | Moderate | Avoid: validated P2PE devices so no card number reaches a PC | IT Manager | 2026-11-15 |
| R-004 | Paper slips with card numbers and security codes | Moderate | Avoid: stop writing card data; shred all slips | Director of Ticketing | 2026-09-15 |

**The theme of the High risks: the ticketing platform is only as safe as the company's own accounts and settings on it.** The vendor's PCI DSS and SOC 2 controls do not stop a venue administrator from being phished (R-001), an agency from adding a skimming script (R-002), or marketing from advertising a price without fees (R-015). R-001 and R-002 together are the P08 incident scenario. Fixing them also reduces five related Moderate risks (R-006, R-007, R-008, R-026, R-030).

R-005 is a business risk rather than a security event, but it is rated High because MID-T carries about $13.9 million a year in ticket revenue. The cheapest treatment (validated P2PE at the box office, about $6,500) also **avoids** R-003 and R-004 rather than mitigating them.

R-021 is not a card data risk. It is included because a venue pays artists and promoters large settlements after each show, and those payment instructions arrive by email.

**Two passes.** Pass 1 was completed on 2026-07-24 from intake and fieldwork evidence. Pass 2 followed the control assessment (P07): R-019 was added on 2026-08-07 after testing found the integrator's default passwords on the CCTV recorder and the door access controller (EV-IA-5). The `assessment_pass` column shows which pass produced each risk.

## 4. Treatment summary
- **Funded (2026 Q4 budget, $41,000, fictional):**
  - Validated P2PE devices for the box office and phone desk (about $6,500)
  - EDR on all PCs with alerting to the IT on-call (about $11,000 a year)
  - Log service for ticketing, identity provider, firewall, and PC logs (about $7,500 a year)
  - ASV and internal vulnerability scanning (about $3,000 a year)
  - Separate-account immutable backups (about $2,000 a year)
  - Cellular failover for the box office and a spare firewall (about $4,000)
  - Penetration test after the scope change (about $7,000, 2027 Q1)
- **No-cost actions due by 2026-09-30:** MFA enforcement on the ticketing platform, account cleanup, script removal, total-price displays, shredding the slips, and changing default passwords.
- **Accepted:**
  - R-025: Low; the Controller reviews every settlement sheet.
  - R-028: Low; named POS clerk logins at the next POS contract renewal.
- **Shared or transferred:** R-011 and R-033 through the ticketing vendor contract (recovery commitments and a 72-hour breach notice clause), and R-029 through the vendor's fraud screening. Cyber insurance covers part of the cost of R-001, R-002, and R-021, but not PCI assessments by the card brands unless the policy says so (Controller to confirm).

## 5. Approval
- General Manager: approved Moderate and Low treatments and acceptances, 2026-08-31.
- Majority owner: approved the High-risk treatment plans and the budget, 2026-08-31, and will decide the P03 scope option by 2026-09-30.
- Next full review: July 2027, or sooner after a major change (for example the P2PE migration) or an incident.
