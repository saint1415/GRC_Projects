# Risk Register Report: Cris Santos Company | Utilities | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Electric Cooperative, Inc. (member-owned electric distribution cooperative) |
| Size tier | Micro (7 employees) |
| Vertical | Utilities |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also serves as | The threat, criticality, and risk content of the cooperative's updated Vulnerability and Risk Assessment (VRA), 7 CFR 1730.27(c)(5)-(6) |
| Prepared | 2026-07-31 by the Office and Finance Manager (Security Coordinator) and the Line Superintendent with the MSP lead technician |
| Updated | 2026-08-12 (R-002 rewritten from P07 testing of the line recloser modems); 2026-08-25 (R-018 after the first month of forecast checks); 2026-08-31 (R-022 and R-023 accepted and closed) |
| Approved | 2026-08-31 by the General Manager; High-risk treatment plans approved by the Board of Trustees on 2026-09-17 |

## 1. Scope and risk framing
**Scope.** The whole cooperative and its key vendors: the DSOMS (P02), the business suite, email and the shared drive, the office network, and the backup vault (SYS-01 to SYS-07 in `../00_company-facts.md`). Vendors in scope: the hosted SCADA vendor, the AMI vendor, the business suite vendor, the MSP, the cellular carrier, and the card payment processor. The G&T is in scope as a dependency (power supply, delivery point protection), not as a system the cooperative controls.

**Why this is also the VRA update.** The cooperative's VRA dates from 2005 and covers physical security only. Since then it added AMI (2019), hosted SCADA (2021), load control (2022), and cellular line reclosers (2023). RUS expects an additional VRA when significant changes occur (7 CFR 1730.27(a)). This register supplies the threats and risk levels; the P03 rows for 1730.27(c)(1) to (c)(8) record the rest of the VRA content.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the Security Coordinator may accept.
- Moderate: only the General Manager may accept, with a treatment plan or a written reason.
- High and Very High: not accepted. The Board of Trustees approves a dated treatment plan instead. Risks to public or crew safety at High are never accepted.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA (P05), the P03 gap analysis, a walkthrough of Substation 1 and two line recloser sites (2026-07-23), and interviews with all 7 staff, the MSP lead technician, and the SCADA vendor's support lead (2026-07-20 to 2026-07-31). Public advisories on attacks against internet-exposed OT devices informed the adversarial ratings.
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories. For a cooperative with about $3,000 of revenue a day, 7 staff, and 26 members on the medical-needs list, an outage of every member for several hours or a $53,000 payment loss is rated High.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 3 |
| Moderate | 15 |
| Low | 5 |
| **Total** | **23** |

Status: 9 In progress, 12 Open, 2 Closed (R-022 and R-023 accepted).

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Attacker uses the shared SCADA password to open feeder reclosers and drop every member | High | Named SCADA accounts; MFA; sign-in limited to cooperative devices; login alerts | Line Superintendent | 2026-10-31 |
| R-002 | Attacker reaches a line recloser through an internet-exposed cellular modem | High | Move the 6 modems to the private network; OT inventory; firmware review | Line Superintendent | 2026-12-31 |
| R-004 | Business email compromise diverts the monthly power bill payment (about $53,000) | High | Written callback rule; training and phishing simulations; external-sender banner | Office and Finance Manager | 2026-10-31 |
| R-013 | RUS loan application delayed because the VRA and ERP cannot be certified | Moderate | VRA update by 2026-12-31; ERP update approved by the Board | General Manager | 2027-01-31 |
| R-014 | Cyber event that interrupts service not reported on DOE-417 within 1 hour | Moderate | DOE-417 steps in the runbook; filing arrangement with the G&T | Line Superintendent | 2026-10-31 |
| R-007 | Recloser or RTU settings cannot be restored | Moderate | Settings library in the vault after every change; quarterly restore test | Line Superintendent | 2026-11-30 |
| R-012 | Hurricane recovery without a plan for business systems | Moderate | ERP Business Continuity Section, cyber annex, current contacts | General Manager | 2027-01-31 |

**The common theme is remote control without accountability.** One password opens SCADA from anywhere (R-001), field modems were reachable from the internet (R-002), and the vendor and 4 AMI users can act without a second check (R-003, R-008). The cooperative's protection today is physical: every device can be operated by hand. That limits the length of an outage but not whether one happens.

**Risks that were fixed or found during the work:**
- R-001 and R-010: the shared SCADA password, unchanged since 2023, was changed on 2026-07-24, the day after the walkthrough. The SCADA vendor's 90-day login history showed no sign-ins from unknown locations. The structural gap (shared login, no MFA) remains open.
- R-002: P07 testing on 2026-08-11 found the LR-4 modem's web page open to the internet with the installer's default password. All 6 modem passwords were changed and the management ports closed on 2026-08-12. The likelihood of initiation stays High until the modems leave the public data plans.
- R-018: the first month of comparing forecasts with the G&T's peak hours (August 2026) showed the add-on picked the right day but an hour early twice. Human approval of every load-control event stays in place (P10).

## 4. Treatment summary
- **Funded (2026-2027 security budget, approved by the Board on 2026-09-17; about $9,400 one-time and $6,900 a year):**
  - Private cellular network plans for the 6 line recloser modems and a second-carrier SIM for the substation gateway: about $1,200 one-time and $1,400 a year
  - SCADA MFA and named-account licensing from the SCADA vendor: about $900 a year
  - MSP-managed EDR and device management for 6 computers and 3 tablets: about $1,700 a year
  - Security awareness training with phishing simulations for 7 people: about $500 a year
  - Immutable vault retention and MSP restore tests: about $600 a year
  - Restricted-key padlocks and key log for Substation 1 and the recloser sites, and a cabinet door switch alarmed to SCADA: about $1,900 one-time
  - Spare recloser control for restore tests: about $2,800 one-time
  - Independent assessment and policy work in 2026 (P07, P06): about $3,500 one-time
  - Annual MSP security review and remaining MSP project time: about $1,800 a year
- **Accepted:** R-022 (Low; card data never enters cooperative systems), R-023 (Low; comfort only, program terms cap events at 4 hours).
- **Contract actions:** security terms (24-hour incident notice, named support staff, access on request) in the SCADA vendor, AMI vendor, and MSP contracts at renewal, by 2026-12-31 (R-008, R-009); AMI data-use addendum by 2026-11-30 (R-017).
- **RUS actions:** VRA update complete by 2026-12-31 and ERP update approved by the Board by 2027-01-31, so the General Manager can sign the certifications for the 2027 loan application (R-013).

## 5. Approval
- General Manager: approved the register, all Moderate treatment plans, and the two acceptances on 2026-08-31.
- Board of Trustees: approved the three High-risk treatment plans and the 2026-2027 security budget on 2026-09-17.
- Next review: as part of the borrower analysis for the March 2027 RUS review, which must be done in the 90 days before it (7 CFR 1730.22(b)(1)); then every July, and sooner after a major change (for example, the AMI upgrade in the 2027 loan) or an incident.
