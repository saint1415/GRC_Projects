# Risk Register Report: Cris Santos Company | Finance and Insurance | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Community Federal Credit Union (member-owned federal credit union) |
| Size tier | Micro (7 employees; $60.0 million in total assets) |
| Vertical | Finance and Insurance |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also satisfies | Risk assessment steps of 12 CFR Part 748, Appendix A, III.B.1 to III.B.3 (N52-R01): identify threats, assess likelihood and potential damage, and assess the sufficiency of controls |
| Prepared | 2026-07-24 by the Operations Manager (Information Security Officer) with the MSP lead technician |
| Updated | 2026-08-06 (R-004 and R-010 updated with P07 test results); 2026-08-12 (R-001 and R-002 updated after the shared mailbox conversion); 2026-08-21 (R-011 updated with the P10 notice review); 2026-08-31 (R-022 and R-023 accepted and closed) |
| Approved | President and CEO, 2026-08-31; presented to the board with the annual report on 2026-08-25 |

## 1. Scope and risk framing
**Scope.** The whole credit union and its key vendors: every member information system in `../00_company-facts.md` section 3 (SYS-01 to SYS-09), the office, and the vendors that hold or reach member information: the core processor, the digital banking provider, the corporate credit union, the card processor, the LOS vendor, the productivity suite vendor, the cloud IaaS provider, and the MSP.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the Operations Manager (ISO) may accept.
- Moderate: only the President and CEO may accept, with a treatment plan or a written reason.
- High and Very High: not accepted by management. The board approves a dated treatment plan and hears progress each month until the risk is reduced.

This is the credit union's first documented risk assessment since a 2019 template questionnaire, which did not rate likelihood or impact and is not relied on. The 2025 NCUA examination recommended an update.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA (P05), the gap analysis (P03), the 2025 account takeover, and interviews with all 7 employees and the MSP lead technician (2026-07-13 to 2026-07-24).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories. For a credit union with about $4,400 of net revenue per business day and about 6,400 members, a fraudulent wire, a breach of member documents, or a multi-day closure is rated High or Very High.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 4 |
| Moderate | 14 |
| Low | 5 |
| **Total** | **23** |

Status: 10 In progress, 11 Open, 2 Closed (R-022 and R-023 accepted).

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Business email compromise leads to a fraudulent member wire | High | Written callback procedure for every wire not requested in person; no emailed instructions alone; BEC training; shared mailbox MFA (done) | Operations Manager | 2026-10-31 |
| R-002 | Member NPI stolen from the shared Member Services mailbox | High | Delegated mailbox with MFA (done); move documents out of email; secure upload link; mailbox alerts | Operations Manager | 2026-11-30 |
| R-006 | Core processor incident exposes member data and the credit union learns late | High | Side letter and renewal terms for prompt incident notice with the facts needed for the NCUA report; annual SOC review | President and CEO | 2027-06-30 |
| R-014 | MSP tool or cloud login compromise reaches every computer and the imaging server | High | Annual MSP security review; 24-hour incident notice and recovery commitment in the contract; tenant in the credit union's name | President and CEO | 2026-12-31 |
| R-011 | AI credit scoring gives unlawful adverse action reasons or biased results | Moderate | P10 conditions: corrected notices, reason-code mapping, second review, fairness testing | Lending Manager | 2026-10-31 |
| R-007 | Missed 72-hour NCUA report or Appendix B member notice | Moderate | POL-03 and the P08 runbook; tabletop exercise | Operations Manager | 2026-11-30 |

**The common theme is trust in email and in vendors.** The credit union moves member money on emailed instructions without an independent check (R-001), keeps member documents in a shared mailbox (R-002), and depends on a core processor and an MSP whose contracts do not say how fast they must tell it about an incident (R-006, R-014). The treatments for R-001 and R-002 also reduce R-004, R-018, and R-019.

**Risks that changed during the work:**
- R-002 and R-001: the MSP converted the Member Services mailbox to a delegated shared mailbox on 2026-08-12, so each MSR now reaches it through their own account with MFA. The stored documents remain, so R-002 stays High until they are moved.
- R-004: P07 testing on 2026-08-05 found the former MSR's core account still enabled. It was disabled the same day. Core sign-in logs showed no use after her last day, so the ISO documented that no member information was accessed. The process gap remains open.
- R-010: P07 testing confirmed the MSP's cloud console login accepts a password alone.

## 4. Treatment summary
- **Funded (2026 Q4, approved by the President and CEO and reported to the board; about $7,900 one-time and $5,660 a year):**
  - MSP-managed EDR with alert monitoring on 11 computers and the imaging server: about $2,100 a year
  - Security awareness training with BEC content and phishing exercises for 7 people: about $500 a year
  - Member MFA and alert features from the digital banking provider: about $1,200 a year
  - Immutable copy of imaging server backups in a separate account: about $600 a year
  - Secure document upload and encrypted email for members: about $900 a year
  - Cellular failover router: about $400 one-time and $360 a year
  - Desktop encryption, MFA setup, mailbox conversion, and restore tests by the MSP: about $1,500 of MSP time
  - Independent control assessment (P07): about $4,500 one-time
  - Counsel review of vendor contract terms (core side letter, MSP amendment): about $1,500 one-time
- **Accepted:** R-022 (Low; card processor and network rules carry the response), R-023 (Low; laptops encrypted).
- **Contract actions:** core processor side letter on incident notice by 2026-10-31 and full terms at renewal on 2027-06-30 (R-006); MSP amendment for incident notice, a recovery time commitment, and tenant ownership by 2026-12-31 (R-014); LOS vendor data-use and model documentation terms (R-011, P10).

## 5. Approval
- Board of Directors: received the register summary and approved the High-risk treatment plans on 2026-08-25.
- President and CEO: approved all treatment plans, the two acceptances, and the budget on 2026-08-31.
- Next full review: July 2027, or sooner after a major change (for example, expanding the AI scoring pilot or changing core processors) or an incident.
