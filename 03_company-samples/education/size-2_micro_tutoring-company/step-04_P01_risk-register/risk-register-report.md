# Risk Register Report: Cris Santos Company | Educational Services | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (K-12 tutoring and learning center) |
| Size tier | Micro (7 employees, plus 14 contractor tutors) |
| Vertical | Educational Services |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also satisfies | The risk assessment in the COPPA Rule's written information security program, 16 CFR 312.8(b)(2): internal and external risks to the confidentiality, security, and integrity of children's personal information and the sufficiency of the safeguards |
| Prepared | 2026-07-24 by the Center Director (Information Security Coordinator) with the MSP lead technician |
| Updated | 2026-08-06 (R-024 added from P07 testing and closed); 2026-08-28 (R-020 and R-023 accepted) |
| Approved | 2026-08-28 by the Owner |

## 1. Scope and risk framing
**Scope.** The whole company and its key vendors. That covers every system that collects, stores, or sends students' and families' information (SYS-01 to SYS-08 in `../00_company-facts.md`), the learning center, the district program sites as far as the company's own work goes, and the parties that handle children's information for the company: the tutoring platform vendor, the scheduling platform vendor, the productivity suite vendor, the MSP and its backup subcontractor, and the 14 contractor tutors.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the Center Director may accept.
- Moderate: only the Owner may accept, with a treatment plan or a written reason.
- High and Very High: not accepted. The Owner approves a dated treatment plan instead. Risks to a child's safety are never accepted above Low.

This is the company's first risk assessment. It is also the first of the annual assessments that 16 CFR 312.8(b)(2) requires, which the company should have had in place by the April 22, 2026 compliance date.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA (P05), the gap analysis (P03), and interviews with the Owner, the Center Director, the Director of Tutoring, the Enrollment and Billing Coordinator, 2 Lead Tutors, 3 contractor tutors, and the MSP lead technician (2026-07-13 to 2026-07-24).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories. For a company with about $3,700 of billing per operating day, about 250 children under 13, and a district contract worth about 16 percent of revenue, theft of evaluation reports or loss of the district contract is rated High, and harm to a child is rated Very High.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 3 |
| Moderate | 16 |
| Low | 5 |
| **Total** | **24** |

Status: 10 In progress, 11 Open, 3 Closed (R-024 treated; R-020 and R-023 accepted).

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware via phishing encrypts center computers and the synced shared drive | High | Training and phishing simulations; MSP-managed EDR; immutable backup versions; restore tests | Center Director | 2026-12-31 |
| R-002 | Theft of the "Student files" folder (evaluation reports, district rosters) | High | Shrink and lock down the folder; inventory; mass-download alerts | Center Director | 2026-12-31 |
| R-003 | Takeover of a tutor or administrator account in the tutoring platform | High | Enforce MFA; 2 administrators only; contractor device rules | Director of Tutoring | 2026-10-31 |
| R-005 | District rosters on contractor tutors' personal computers | Moderate | Stop roster emails; platform-only access; new contractor agreement | Director of Tutoring | 2026-09-30 |
| R-006 | Collecting children's information without compliant notice and consent | Moderate | New online and direct notices; consent before any account; written security program | Center Director | 2026-10-31 |
| R-018 | A tutor misuses online contact with a child | Moderate | Monthly spot review of messages and recordings; no contact outside the platform | Owner | 2026-10-31 |

**The common theme is that children's information is spread wider than the company knew.** It sits in the platform behind single-factor logins (R-003), in a shared folder anyone on staff can open (R-002), on contractors' personal computers (R-005), and in records nobody ever deletes (R-007). The treatments for these four also reduce R-001, R-004, R-015, and R-022, and they shrink what a breach would expose.

**Risks found or fixed during the work:**
- R-004: three former contractor tutors' platform accounts were disabled on 2026-07-15, the day they were found. The platform log showed no sign-ins after each tutor's last session, so the Center Director documented that no unauthorized access occurred. The process gap remains open.
- R-008: the Owner had the vendor turn off the AI progress insights module on 2026-08-28 until the P10 conditions are met.
- R-024: added on 2026-08-06 after P07 testing found the firewall management page open to the internet. The MSP turned it off the same week; the risk is closed.

## 4. Treatment summary
- **Funded (2026 Q4, approved by the Owner; about $3,900 one-time and $3,600 a year):**
  - MSP-managed EDR with after-hours alert monitoring on 8 computers: about $1,450 a year
  - Security awareness training with phishing simulations for 7 staff and 14 contractor tutors: about $650 a year
  - Backup upgrade to 90-day immutable versions: about $500 a year
  - Wi-Fi segmentation and new access point settings by the MSP: about $600 one-time
  - Desktop encryption, MFA set-up, account clean-up, and the first restore test by the MSP: about $900 of MSP time
  - Notice and consent rewrite reviewed by outside privacy counsel: about $1,200 one-time
  - Independent assessment in 2026 (P07): about $1,200 one-time
  - Annual MSP security review and remaining MSP project time: about $1,000 a year
- **Accepted:** R-020 (Low; weekly schedule export), R-023 (Low; laptops encrypted).
- **Contract actions:** tutoring platform data processing addendum with written security assurances and no model training (R-008) by 2026-10-31; new contractor tutor agreement (R-005) by 2026-09-30; MSP contract amendment for incident notice and a recovery commitment (R-013) by 2026-12-31.

## 5. Approval
- Owner: approved all treatment plans, the two acceptances, and the budget on 2026-08-28.
- Next full review: July 2027 (the annual assessment under 312.8(b)(2)), or sooner after a material change such as a new platform, a second district contract, or turning the AI module back on.
