# Risk Register Report: Cris Santos Company | Health Care and Social Assistance | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (primary care office, two physicians) |
| Size tier | Micro (7 employees) |
| Vertical | Health Care and Social Assistance |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also satisfies | HIPAA risk analysis, 45 CFR 164.308(a)(1)(ii)(A), and risk management, 164.308(a)(1)(ii)(B) |
| Prepared | 2026-07-31 by the Office Manager (Privacy and Security Officer) with the MSP lead technician |
| Updated | 2026-08-12 (R-023 added from P07 testing); 2026-08-31 (R-006, R-020, R-021 closed) |
| Approved | 2026-08-31 by the owner physician |

## 1. Scope and risk framing
**Scope.** The whole practice and its key vendors. That covers every system that creates, receives, maintains, or transmits ePHI (SYS-01 to SYS-08 in `../00_company-facts.md`), the office suite, and the vendors that handle ePHI for the practice: the EHR vendor, the MSP, the productivity suite vendor, the cloud fax vendor, the backup service, and the AI scribe vendor.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the Office Manager may accept.
- Moderate: only the owner physician may accept, with a treatment plan or a written reason.
- High and Very High: not accepted. The owner physician approves a dated treatment plan instead. Patient-safety risks at High are never accepted.

This is the practice's first documented risk analysis since a 2019 consultant checklist. The 2019 checklist did not rate likelihood or impact and is not relied on.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA (P05), the gap analysis (P03), and interviews with both physicians, the Office Manager, the Billing Specialist, the Front Desk Coordinator, and the MSP lead technician (2026-07-20 to 2026-07-31).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories. For a practice with about $4,400 of revenue per clinic day and about 3,500 patients, a breach of every patient record or a week-long closure is rated High or Very High.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 3 |
| Moderate | 14 |
| Low | 6 |
| **Total** | **23** |

Status: 9 In progress, 11 Open, 3 Closed (R-006 treated; R-020 and R-021 accepted).

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware via phishing encrypts workstations and the synced shared drive | High | Training and phishing simulations; MSP-managed EDR; immutable backup versions; restore tests | Office Manager | 2026-12-31 |
| R-002 | PHI stolen during ransomware (breach of up to about 3,500 patients) | High | ePHI inventory; move scanned records into the EHR; mailbox and download alerts | Office Manager | 2026-12-31 |
| R-013 | MSP remote tool compromise reaches every endpoint | High | Annual MSP security review; 24-hour incident notice in the MSP contract | Owner Physician | 2026-12-31 |
| R-005 | Shared-drive data cannot be restored | Moderate | First restore test; 90-day immutable versions; quarterly tests | Office Manager | 2026-10-31 |
| R-004 | Former workforce member still has access | Moderate | Last-day termination checklist; monthly account reconciliation | Office Manager | 2026-09-30 |
| R-011 | AI scribe processes PHI without a BAA | Moderate | Pause recording until the BAA is signed | Associate Physician | 2026-09-30 |

**The common theme is ransomware.** The practice cannot yet detect an intrusion quickly (R-001), does not know every place PHI sits (R-002), and gives one outside party administrator access to every device (R-013). The treatments for these three also reduce R-003, R-005, R-007, and R-015.

**Risks that were fixed or found during the work:**
- R-006: the productivity suite BAA was accepted in the admin console on 2026-08-14. The risk is closed.
- R-004: the former MA's account was disabled on 2026-07-21, the day it was found. The EHR and email sign-in logs showed no use after the termination date, so the Office Manager (Privacy Officer) documented that no breach occurred. The process gap remains open.
- R-023: added on 2026-08-12 after P07 testing found that the MSP had excluded the procedure-room workstation from patching since April 2026.

## 4. Treatment summary
- **Funded (2026 Q4, approved by the owner physician; about $4,800 one-time and $4,300 a year):**
  - MSP-managed EDR with alert monitoring on 10 computers: about $1,800 a year
  - Security awareness training with phishing simulations for 7 people: about $500 a year
  - Backup upgrade to 90-day immutable versions: about $600 a year
  - Cellular failover router: about $400 one-time and $360 a year
  - Desktop encryption, restore tests, and account clean-up by the MSP: about $1,400 of MSP time
  - Independent assessment and policy work in 2026 (P07, P06): about $3,000 one-time
  - Annual MSP security review and remaining MSP project time: about $1,040 a year
- **Accepted:** R-020 (Low; payers accept late claims), R-021 (Low; devices encrypted).
- **Contract actions:** AI scribe BAA (R-011) by 2026-09-30; MSP contract amendment for incident notice and subcontractor list (R-013) at renewal by 2026-12-31.

## 5. Approval
- Owner physician: approved all treatment plans, the two acceptances, and the budget on 2026-08-31.
- Next full review: July 2027, or sooner after a major change (for example, expanding the AI scribe to the second physician) or an incident.
