# Risk Register Report: Cris Santos Company | Emergency Services | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (licensed BLS ambulance service, non-emergency transport only) |
| Size tier | Micro (7 employees) |
| Vertical | Emergency Services (CISA sector; NAICS 621910 Ambulance Services) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also satisfies | HIPAA risk analysis, 45 CFR 164.308(a)(1)(ii)(A), and risk management, 164.308(a)(1)(ii)(B) (C-EMERGENCY-R04) |
| Prepared | 2026-08-07 by the Office Manager (Privacy and Security Officer) with the MSP lead technician |
| Updated | 2026-08-19 (R-023 added from P07 testing); 2026-09-04 (R-004 and R-010 closed) |
| Approved | 2026-09-04 by the Owner |

## 1. Scope and risk framing
**Scope.** The whole company and its key vendors. That covers every system that creates, receives, maintains, or transmits ePHI (SYS-01 to SYS-09 in `../00_company-facts.md`), the office and garage, both ambulances, and the vendors that handle ePHI or run systems for the company: the operations platform vendor, the MSP and its backup subcontractor, the productivity suite vendor, the hosted phone vendor, and the billing company.

**What makes this business different.** The company does not answer 911 calls, so a dispatch outage does not delay an emergency response. It can still hurt patients: about 18 dialysis patients depend on scheduled pickups that start at 5:00 a.m., and callers sometimes describe an emergency on the request line. Impact ratings therefore use the BIA safety category (P05) first, then regulatory and cost.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the Office Manager may accept.
- Moderate: only the Owner may accept, with a treatment plan or a written reason.
- High and Very High: not accepted. The Owner approves a dated treatment plan instead. A risk that could cause a missed dialysis session or a missed 911 redirect is never accepted at Moderate or above without treatment.

**Who does the work.** The Office Manager is both the Security Officer who runs the controls and the person who rates the risks. The MSP lead technician took part in every session as a second view, and the independent assessor (P07) tested the main controls.

This is the company's first documented security risk analysis.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA (P05), the gap analysis (P03), CISA's Emergency Services Sector context, and interviews with the Owner, the Office Manager, the Scheduler-Dispatcher, two EMTs, the Medical Director, and the MSP lead technician (2026-07-27 to 2026-08-07).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories. For a company with about $3,000 of revenue a day and about 5,200 patients in its platform, a breach of every patient record or a multi-day dispatch failure is rated High or Very High.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 3 |
| Moderate | 17 |
| Low | 4 |
| **Total** | **24** |

Status: 11 In progress, 11 Open, 2 Closed (R-004 treated; R-010 accepted).

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware via phishing encrypts the office desktops, including the dispatch desk, and the synced shared drive | High | Training and phishing simulations; MSP-managed EDR with after-hours monitoring; immutable backups; nightly run sheet and manual dispatch drills | Office Manager | 2026-12-31 |
| R-002 | Stolen password used to sign in to the operations platform and export about 5,200 patients' records | High | Shared password changed 2026-09-08; MFA for every platform user and named dispatch accounts; export log review | Office Manager | 2026-10-31 |
| R-003 | MSP remote management tool compromise reaches every office computer | High | Annual MSP security review; 24-hour incident notice and after-hours line at contract renewal | Owner | 2026-12-31 |
| R-008 | Platform outage longer than the 2-hour dispatch RTO, with manual dispatch never practiced | Moderate | Nightly printed run sheet; quarterly manual dispatch drill | Scheduler-Dispatcher | 2026-10-31 |
| R-014 | AI intake assistant misses an emergency described by a caller | Moderate | Prompt-only design; the 911 redirect card decides; monthly call review (P10) | Medical Director | 2026-10-31 |
| R-023 | Unmanaged remote desktop tool on the dispatch desktop (found in testing) | Moderate | Removed 2026-08-19; approved software list; EDR | Office Manager | 2026-10-31 |

**The common theme is sign-in and recovery.** The company's most valuable system accepts a password alone (R-002), the office computers can be reached by an outside tool nobody watches (R-003, R-023), and no one has practiced dispatching without the board (R-001, R-008). The treatments for the three High risks also reduce R-005, R-006, R-007, R-016, and R-022.

**Risks that were fixed or found during the work:**
- R-004: the Owner signed the hosted phone and fax vendor's BAA on 2026-08-21, and the Office Manager set a 2-year recording retention on 2026-08-28. The risk is closed.
- R-006: the two former EMT accounts were disabled on 2026-07-29, the day they were found. The platform access report showed no sign-ins after their last shifts, so the Office Manager (Privacy Officer) documented that no breach occurred. The process gap remains open.
- R-023: added on 2026-08-19 after P07 testing found a free remote desktop tool on the dispatch desktop. The MSP removed it the next day. The tool's own connection log showed no unknown sessions in its 90-day history, which is all it kept.

## 4. Treatment summary
- **Funded (2026 Q4, approved by the Owner; about $3,600 one-time and $4,700 a year):**
  - MSP-managed EDR with after-hours alert monitoring on the 3 computers: about $900 a year
  - After-hours emergency line added to the MSP contract: about $1,800 a year
  - Security awareness training with phishing simulations for 7 people: about $500 a year
  - Backup upgrade to 90-day immutable versions with MFA on the console: about $400 a year
  - Cellular failover router at the office: about $400 one-time and $360 a year
  - Separate staff and guest Wi-Fi, desktop encryption, hotspot onboarding, and restore tests by the MSP: about $1,200 of MSP time
  - Independent assessment and policy work in 2026 (P07, P06): about $2,000 one-time
  - Yearly MSP and billing company reviews: about $740 a year of staff and MSP time
  - MFA and named dispatch accounts on the platform: no added cost (included in the subscription)
- **Accepted:** R-010 (Low; tablets and phones are encrypted and can be wiped).
- **Contract actions:** written confirmation that the AI feature is covered by the platform BAA with no-training terms (R-013) by 2026-10-15; MSP contract amendment for incident notice and an after-hours line (R-003, R-016) at renewal by 2026-12-31; billing company breach notice terms (R-020) by 2026-12-31.

## 5. Approval
- Owner: approved all treatment plans, the acceptance of R-010, and the budget on 2026-09-04.
- Next full review: August 2027, or sooner after a major change (for example, a new platform, a 911 zone from the county, or moving the AI intake assistant beyond the pilot) or an incident.
