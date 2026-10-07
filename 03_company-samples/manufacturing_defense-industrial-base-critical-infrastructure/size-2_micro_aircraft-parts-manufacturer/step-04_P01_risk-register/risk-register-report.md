# Risk Register Report: Cris Santos Company | Defense Industrial Base | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (aircraft parts machine shop, DoD subcontractor) |
| Size tier | Micro (7 employees) |
| Vertical | Defense Industrial Base |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also satisfies | SP 800-171 Rev. 2 requirement 3.11.1 (periodic risk assessment) |
| Prepared | 2026-07-24 by the Office Manager (Security and Compliance Coordinator) with the MSP lead technician |
| Updated | 2026-08-12 (R-023 added from P07 testing); 2026-08-31 (R-015 accepted and closed) |
| Approved | 2026-08-31 by the President |

## 1. Scope and risk framing
**Scope.** The whole business and its key vendors: every system that holds CUI, whether it should or not (SYS-01 to SYS-10 in `../00_company-facts.md`), printed drawings, the shop floor, and the vendors that handle CUI or protect it: the government-community cloud provider, the MSP and its backup subcontractor, the commercial suite and ERP vendors, Prime A's portal, and the 2 outside processors.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the Office Manager may accept.
- Moderate: only the President may accept, with a written reason.
- High and Very High: not accepted. The President approves a dated treatment plan instead.
- A risk whose treatment is an SP 800-171 requirement is never accepted, whatever its level, because CMMC Level 2 requires every requirement to be met (32 CFR 170.24). It may only be scheduled.

This is the company's first documented risk assessment.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA (P05), the SSP and cloud mapping (P02, P04), and interviews with all 7 employees and the MSP lead technician (2026-07-13 to 2026-07-24).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories. For a shop with about $4,400 of shipments per production day, losing Prime A (about 40% of revenue) or all DoD work is Very High.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 5 |
| Moderate | 16 |
| Low | 3 |
| **Total** | **25** |

Status: 14 Open, 10 In progress, 1 Closed (R-015 accepted). Treatment: 23 Mitigate, 1 Accept, 1 Share/Transfer.

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-004 | SPRS score of 110 does not reflect implementation | Very High | Post the recalculated score and a plan to 110; counsel engaged | President | 2026-09-30 |
| R-001 | CUI exfiltrated through the shared commercial orders mailbox (no MFA) | High | Move Supplier B to SYS-01; purge CUI from SYS-02; MFA or remove the shared mailbox | Office Manager | 2026-10-31 |
| R-003 | CUI in the MSP's commercial backup cloud (not FedRAMP authorized) | High | Compliant backup first, then stop and delete the commercial backup | President | 2026-09-30 |
| R-006 | Cannot report a cyber incident to DoD within 72 hours | High | Medium assurance certificates; P08 runbook; tabletop with a DIBNet drill | President | 2026-11-30 |
| R-016 | CUI pasted into a public generative AI chatbot | High | AI rule in POL-04; web block; training; disclosure decision (P10) | CNC Programmer | 2026-10-31 |
| R-005 | No CMMC Level 2 (Self) status by 2027-04-01; Prime A work lost | High | P03 roadmap; self-assessment and SPRS posting by 2027-03-15 | President | 2027-03-15 |

**The common theme is that CUI lives in more places than the enclave.** The job folders in the CUI suite are well protected by the provider. The exposure is everywhere else: the commercial mailbox (R-001), the commercial backup (R-003), the ERP (R-020), paper (R-011), USB drives (R-012), a personal phone (R-014), and a public chatbot (R-016). Shrinking CUI back into the enclave treats seven risks at once and makes the CMMC scope smaller.

**The second theme is that the company cannot see or report an incident.** No alerts, no log review, and no DoD certificate (R-006, R-022) mean an exfiltration like the P08 scenario would be found by a customer, not by the shop.

**Risks found or changed during the work:**
- R-013: the former part-time programmer's commercial suite account and Prime A portal access were disabled on 2026-07-15, the day they were found. Sign-in logs showed no use after his last day. The offboarding gap remains open.
- R-023: added on 2026-08-12 after P07 testing found one MSP technician's RMM console login without MFA. The MSP enabled MFA the same day; evidence is pending.
- R-004: counsel advised on 2026-07-28 that the 110 score must be corrected promptly.

## 4. Treatment summary
- **Funded (approved by the President on 2026-08-31; about $36,000 one-time and $13,000 a year):**
  - Compliant backup setup, migration of CUI out of the commercial suite and ERP, and retirement of the commercial backup (MSP project): about $3,500
  - Enclave VLAN with a managed switch and firewall rules: about $4,000
  - Desktop encryption, named accounts with MFA, removal of local administrator rights: about $1,500
  - Medium assurance certificates (2), phishing-resistant keys, and 2 encrypted USB drives: about $900
  - Shred bin, cross-cut shredder, and a locked drawing cabinet: about $900
  - Baselines and vulnerability scanning setup: about $2,500
  - Independent readiness assessment (P07), SSP and policy support: about $9,000
  - Level 2 self-assessment support before 2027-03-15: about $6,000
  - Tabletop exercise: about $1,500
  - Counsel for the SPRS correction and export control reviews: about $6,000
  - Recurring: SYS-01 audit retention and backup licensing (about $3,000), MSP managed detection and scanning (about $6,000), training with phishing simulations (about $600), contract programmer standby (about $1,500), annual self-assessment support (about $2,000)
- **Accepted:** R-015 (Low; machining continues offline during an internet outage).
- **Shared:** R-024 (hurricane) through property and business interruption insurance, plus a checklist.
- **Contract actions:** MSP contract amendment (named accounts, responsibility matrix, U.S.-person technicians, 24-hour incident notice, recovery time) by 2026-10-31 (R-007, R-010); DFARS flowdown or no-drawing process sheets for outside processors by 2026-10-31 (R-025).

## 5. Approval
- President: approved all treatment plans, the one acceptance, and the budget on 2026-08-31.
- Next full review: July 2027, or sooner after a major change (for example, enabling the CUI suite AI assistant, adding a DNC link to the older machines, or a new prime requiring Level 2 (C3PAO)) or an incident.
