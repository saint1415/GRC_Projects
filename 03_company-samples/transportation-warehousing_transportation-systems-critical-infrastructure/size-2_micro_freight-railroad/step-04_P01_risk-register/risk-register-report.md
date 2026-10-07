# Risk Register Report: Cris Santos Company | Transportation Systems | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (short line freight railroad, 16 route miles) |
| Size tier | Micro (7 employees) |
| Vertical | Transportation Systems |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Prepared | 2026-07-24 by the Office Manager (Security Lead) with the Owner and General Manager and the MSP lead technician |
| Updated | 2026-08-05 (R-017 added from P07 testing); 2026-08-31 (R-011 and R-021 accepted and closed) |
| Approved | 2026-08-31 by the Owner and General Manager |

## 1. Scope and risk framing
**Scope.** The whole railroad and its key vendors. That covers every system in `../00_company-facts.md` section 3 (SYS-01 to SYS-09), the Junction office and enginehouse, the radio system, and the vendors that hold company data or run company systems: the operations SaaS vendor, the MSP, the productivity suite vendor, the backup service, the telematics vendor, the payroll vendor, and the AI pilot vendor.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the Office Manager may accept.
- Moderate: only the Owner and General Manager may accept, with a treatment plan or a written reason.
- High and Very High: not accepted. The Owner and General Manager approves a dated treatment plan instead. Risks to train or roadway worker safety at High are never accepted.

This is the railroad's first documented risk assessment. Because the General Manager both accepts risk and runs dispatch, the independent assessor (P07) reviews the register each year.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA (P05), the gap analysis (P03), and interviews with the General Manager, Office Manager, Roadmaster, Conductor, Mechanic, and the MSP lead technician (2026-07-13 to 2026-07-24).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories. For a railroad with about $4,400 of revenue per operating day, a multi-day stoppage is High; anything that can lead to a collision, a roadway worker strike, or a propane release is Very High.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 3 |
| Moderate | 14 |
| Low | 5 |
| **Total** | **22** |

Status: 9 In progress, 11 Open, 2 Closed (R-011 and R-021 accepted).

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware via phishing encrypts the office computers, the dispatch desktop, and the synced shared drive | High | Training and phishing simulations; MSP-managed EDR; dispatch desktop on its own segment; immutable backups | Office Manager | 2026-12-31 |
| R-002 | Conflicting or lost movement authority during an unplanned switch to paper dispatch | High | Written paper dispatch procedure with a radio roll call; drill twice a year | Owner and General Manager | 2026-11-30 |
| R-004 | MSP remote tool compromise reaches every computer, including the dispatch desktop | High | Annual MSP security review; incident notice, recovery time, and remote-work approval in the contract | Owner and General Manager | 2026-12-31 |
| R-006 | A cyber attack is not reported to TSA within 24 hours | Moderate | TSA report step in POL-03 and P08; contact card; staff briefing | Owner and General Manager | 2026-10-15 |
| R-003 | Shared crew login misused by a former employee or outsider | Moderate | Named crew accounts with MFA; termination checklist | Office Manager | 2026-11-30 |
| R-005 | Shared drive or operations data cannot be restored | Moderate | First restore test; immutable versions; weekly operations data export | Office Manager | 2026-10-31 |
| R-007 | Unsupported operating system on the dispatch desktop | Moderate | Replace the desktop with the certified console version | Office Manager | 2026-12-31 |

**The common theme is the dispatch desk.** One computer on a flat office network, running an unsupported operating system, carries the radio console that every movement authority depends on (R-001, R-007, R-012). When it fails, the railroad falls back to paper dispatch, which works only if the dispatcher knows every active authority at that moment (R-002). The treatments for these risks also reduce R-010 and R-013.

**The one binding cyber duty was missed.** 49 CFR 1570.203 makes a cyber attack reportable to TSA within 24 hours of discovery. The 2025 mailbox compromise (R-009) was not reported because nobody knew the duty covered cyber events (R-006).

**Risks that were fixed or found during the work:**
- R-003: the shared crew password, unchanged since 2023-05 and known to a conductor who left on 2026-02-27, was changed on 2026-07-16. The vendor's 90-day sign-in history showed use only from the 3 company tablets. The process gap remains open.
- R-017: added on 2026-08-05 after P07 testing found that the telematics portal uses a shared administrator login with its installation password and no MFA.

## 4. Treatment summary
- **Funded (2026 Q4, approved by the Owner and General Manager; about $7,300 one-time and $4,040 a year):**
  - MSP-managed EDR with alert monitoring on 5 computers: about $1,000 a year
  - Security awareness training with phishing simulations for 7 people: about $500 a year
  - Backup upgrade to 90-day immutable versions: about $600 a year
  - Named crew accounts with MFA in the operations system (3 more licenses): about $1,080 a year
  - Cellular failover router: about $400 one-time and $360 a year
  - Replacement dispatch desktop with the certified radio console version: about $2,200 one-time
  - Desktop encryption, a separate dispatch segment, restore tests, and account clean-up by the MSP: about $1,200 of MSP time
  - Independent assessment and policy work in 2026 (P07, P06): about $3,500 one-time
  - Annual MSP security review: about $500 a year
- **Accepted:** R-011 (Low; the operations SaaS vendor's recovery commitments meet the BIA and paper dispatch covers one shift), R-021 (Low; tablets are encrypted and can be wiped).
- **Contract actions:** MSP contract amendment at renewal by 2026-12-31 (R-004); AI pilot terms by 2026-10-31 (R-020).

## 5. Approval
- Owner and General Manager: approved all treatment plans, the two acceptances, and the budget on 2026-08-31.
- Next full review: July 2027, or sooner after a major change (for example, a new customer shipping RSSM, a new operations system, or expanding the AI pilot) or an incident.
