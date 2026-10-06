# Risk Register Report: Cris Santos Company | Accommodation and Food Services | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent 38-unit roadside motel) |
| Size tier | Micro (7 employees) |
| Vertical | Accommodation and Food Services |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Related requirement | PCI DSS v4.0.1 requirement group 12.3 (risks to the cardholder data environment). The targeted risk analyses that group calls for are separate documents, still to be written (P03 row for 12.3) |
| Prepared | 2026-07-24 by the Assistant Manager (Security and Privacy Lead) with the MSP lead technician |
| Updated | 2026-08-04 (R-006 added and R-009 raised from P07 testing); 2026-08-21 (R-014 updated from the P10 channel check); 2026-08-31 (R-021 and R-023 accepted and closed) |
| Approved | 2026-08-31 by the Owner-Manager |

## 1. Scope and risk framing
**Scope.** The whole motel and its key vendors. That covers every system that stores, processes, or transmits card data or guest personal information (SYS-01 to SYS-10 in `../00_company-facts.md`), the front office, and the vendors that handle that data or administer systems for the motel: the PMS vendor, the payment gateway and P2PE provider, the MSP, the lock vendor, the productivity suite vendor, the backup service, and the dynamic pricing tool vendor.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the Assistant Manager may accept.
- Moderate: only the Owner-Manager may accept, with a treatment plan or a written reason.
- High and Very High: not accepted. The Owner-Manager approves a dated treatment plan instead. Risks that could strand a guest or put a key in the wrong hands are never accepted at High.

This is the motel's first documented risk assessment. The 2025 SAQ was signed without one.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA (P05), the gap analysis (P03), the FTC's allegations in *FTC v. Wyndham Worldwide Corp.*, 799 F.3d 236 (3d Cir. 2015), and interviews with the Owner-Manager, the Assistant Manager, both Front Desk Clerks, the Night Auditor, the Head Housekeeper, and the MSP lead technician (2026-07-13 to 2026-07-24).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories. For a motel with about $3,000 of revenue a day, a card compromise that triggers card brand costs and breach notices, or a night when guests cannot get keys, is rated High.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 4 |
| Moderate | 15 |
| Low | 4 |
| **Total** | **23** |

Status: 9 In progress, 12 Open, 2 Closed (R-021 and R-023 accepted).

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Attacker uses the lock vendor's always-on remote tool to plant card-capture malware on the front desk PC | High | Lock tool off between sessions; separate networks; EDR; no keyed entry on PCs | Assistant Manager | 2026-11-30 |
| R-003 | Card forms in the shared mailbox (about 640, about 260 with security codes) are taken | High | Purge; no more card forms; named mailboxes with MFA | Assistant Manager | 2026-11-30 |
| R-009 | Loss of the back office PC destroys the lock database; no new keys can be made | High | Back up and restore-test the lock database; emergency key cards | Assistant Manager | 2026-10-31 |
| R-013 | Dynamic pricing raises rates on evacuees in a declared emergency | High | Ceiling, daily limits, and emergency mode with Owner-Manager approval (P10) | Owner-Manager | 2026-10-15 |
| R-008 | Flat office network lets malware reach terminals, locks, and CCTV | Moderate | Separate networks with deny-by-default rules | Assistant Manager | 2026-12-31 |
| R-015 | Acquirer non-compliance after the wrong 2025 SAQ | Moderate | Redesign by 2026-11-30; SAQ P2PE plus SAQ A by 2026-12-31 | Owner-Manager | 2026-12-31 |

**The common theme is the front desk PC.** It is where card numbers are keyed, where the shared mailbox is open, where the shared login never locks, and it shares a network with the PC that an outside vendor can reach at any time (R-001, R-002, R-003, R-007, R-008). The single most effective treatment is to stop card data from touching that PC at all, which is the P03 redesign. It also reduces R-005, R-015, and R-016.

**Risks found or changed during the work:**
- R-006: added on 2026-08-04 after P07 testing found 2 former employees' PMS accounts still active. Their activity logs showed no sign-ins after their last day. Both accounts were disabled that day; the process gap remains open.
- R-009: raised on 2026-08-04 when P07 testing found the lock database outside the backup job (likelihood of adverse impact from High to Very High). The MSP added it to the job on 2026-08-12. The rating stays High until a restore test with the lock vendor proves the copy works.
- R-001: on 2026-08-05 the MSP set the lock vendor's tool to start only when the motel accepts a session. One-time codes, written terms, and network separation remain, so the rating is unchanged.
- R-004: the crew billing binder was moved to a locked drawer in the back office on 2026-08-05.
- R-013: the 2025 hurricane evacuation is not hypothetical. The tool raised rates 61% above the 30-day average for 2 nights while the county was under a declared state of emergency. No complaint was received, but Fla. Stat. 501.160 treats a gross disparity from that average as prima facie evidence of an unconscionable price (see P10).

## 4. Treatment summary
- **Funded (2026 Q4, approved by the Owner-Manager; about $5,200 one-time and $2,260 a year):**
  - MSP-managed EDR with after-hours alerting on the 3 PCs: about $600 a year
  - Security awareness training for 7 people, with a front desk card-handling and caller module: about $400 a year
  - Cellular failover router: about $400 one-time and $360 a year
  - Separate networks for terminals, lock system and CCTV, and office PCs (managed switch and MSP labor): about $1,500 one-time
  - Quarterly ASV scans for as long as the office network stays in card data scope: about $300 a year
  - Immutable backup versions and lock database backup: about $300 a year
  - Yearly MSP security review and remaining MSP project time (accounts, encryption, restore tests): about $300 a year and $800 one-time
  - Independent assessment and policy work in 2026 (P07, P06): about $2,500 one-time
  - Pay-by-link for phone and crew payments: included in the gateway plan (no added fee)
- **Accepted:** R-021 (Low; a shredder is already used and few reports are obtained), R-023 (Low; the laptop is encrypted).
- **Contract actions:** written remote access and incident notice terms with the lock vendor (R-001) by 2026-10-31; dynamic pricing tool settings and terms (R-013) by 2026-10-15; MSP incident notice and recovery time terms at renewal by 2026-12-31 (R-020).

## 5. Approval
- Owner-Manager: approved all treatment plans, the two acceptances, and the budget on 2026-08-31.
- Next full review: July 2027, or sooner after a major change (for example, a decision to accept the franchise offer, a new payment design, or switching on the AI guest messaging add-on) or an incident.
