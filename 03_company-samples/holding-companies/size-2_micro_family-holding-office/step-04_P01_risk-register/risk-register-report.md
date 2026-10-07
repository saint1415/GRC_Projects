# Risk Register Report: Cris Santos Company | Management of Companies and Enterprises | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (family holding company and single-family office) |
| Size tier | Micro (7 employees) |
| Vertical | Management of Companies and Enterprises |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also satisfies | The written risk assessment the Safeguards Rule bases the program on (16 CFR 314.4(b)) and its periodic reassessment (314.4(b)(2)). The detailed content list in 314.4(b)(1) does not apply at this size (314.6), but this assessment meets it anyway |
| Prepared | 2026-08-14 by the Family Office Director (Qualified Individual) with the MSP lead technician |
| Updated | 2026-09-02 (R-023 added from P07 testing); 2026-09-18 (R-019, R-020, R-021 closed) |
| Approved | 2026-09-18 by the Principal; High-risk treatment plans approved by the Board of Managers the same day |

## 1. Scope and risk framing
**Scope.** The office and its key vendors: every system in the Family Office Shared Services Platform (SYS-01 to SYS-11 in `../00_company-facts.md`), the office suite, and the providers that hold or reach family information: the productivity suite, accounting, bill pay, payroll, investment platform, and vault vendors, the banks and custodians, the cloud provider, the MSP, and the outside CPA firm. The three subsidiaries' own systems are out of scope; the risks they bring to the office through guest access and payment approvals are in (R-018).

**What the office is protecting.** The office's own revenue is small ($1.1 million). What it protects is much larger: the family's money (about $310 million advised, plus daily payments), the family's privacy and physical safety (addresses, travel plans, minors' details), and the subsidiaries' ability to pay large bills. Impact ratings use the BIA categories in P05, scaled to that exposure.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the Family Office Director may accept.
- Moderate: only the Principal may accept, with a treatment plan or a written reason.
- High and Very High: not accepted. The Board of Managers approves a dated treatment plan instead. Risks to family members' personal safety at High are never accepted.

This is the office's first documented risk assessment.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA (P05), the gap analysis (P03), the March 2026 payment fraud attempt, and interviews with all 7 staff and the MSP lead technician (2026-08-03 to 2026-08-14).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories. Theft of every family member's identity documents is rated Very High because of the identity theft, extortion, and personal safety harm.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 4 |
| Moderate | 15 |
| Low | 4 |
| **Total** | **23** |

Status: 9 In progress, 11 Open, 3 Closed (R-021 treated; R-019 and R-020 accepted).

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Mailbox takeover by adversary-in-the-middle phishing redirects a family or subsidiary payment | High | Phishing-resistant security keys; managed-device sign-in; inbox rule and forwarding alerts; payment-fraud training | Family Office Director | 2026-12-31 |
| R-002 | Spoofed email gets staff to change payee bank details or send a wire | High | Written callback procedure and payment log; second-person check; training | Controller | 2026-10-31 |
| R-003 | Theft of family identity, tax, and estate records leads to identity theft, extortion, or physical risk | High | Need-to-know folders; move IDs and tax returns to the vault; data inventory; disposal | Family Office Director | 2026-12-31 |
| R-005 | MSP shared global admin account or MSP tools compromised | High | Named MSP admin accounts with security keys; contract security terms; annual MSP review | Family Office Director | 2026-12-31 |
| R-011 | A SaaS vendor holding family data is breached | Moderate | Service provider list; annual SOC 2 reviews; security terms at renewal | Family Office Director | 2026-12-31 |
| R-023 | One person can change a payee's bank details and pay it in the bill pay platform | Moderate | Turn on dual approval in the platform; weekly payee change report | Controller | 2026-10-15 |

**The common theme is email-driven payment fraud.** A small office that moves large sums by email is a prime target for business email compromise. The four High risks share three fixes: stronger sign-in (R-001, R-005), a written and recorded callback rule (R-002, R-015), and less data reachable from any one account (R-003, R-004). These fixes also reduce R-008, R-009, R-018, and R-023.

**Risks that changed during the work:**
- R-004: the AI assistant surfaced a trust distribution memo to the Executive Assistant on 2026-07-22. Florida law treats good-faith access by an employee as not a breach when the information is not misused (Fla. Stat. 501.171(1)(a)), and nothing left the office, so no notice was due. The access design gap remains.
- R-008: the former Marine Supply controller's guest account was removed on 2026-08-14. The sign-in log showed no use after February 2026. The process gap remains.
- R-009: the Principal's spouse got a separate vault account on 2026-08-20.
- R-021: the MSP updated the printer firmware and locked down the conference PC on 2026-08-21. Closed.
- R-023: added on 2026-09-02 after P07 testing found that the bill pay platform's dual approval setting was off.

## 4. Treatment summary
- **Funded (2026 Q4, approved by the Principal; about $7,900 one-time and $6,700 a year):**
  - Hardware security keys for 7 staff and 3 spares, and setup by the MSP: about $900 one-time
  - Productivity suite license upgrade (one-year audit logs, risky sign-in alerts, device-based access): about $1,700 a year
  - Independent SaaS backup of mail and files: about $900 a year
  - MSP-managed endpoint detection and response with after-hours alerting on 9 devices: about $1,600 a year
  - MSP vulnerability scanning (office and SYS-11), monthly: about $1,200 a year
  - Payment-fraud training with phishing simulations for 7 staff, plus a family briefing: about $600 a year
  - Annual MSP security review and contract amendment time: about $700 a year
  - SYS-11 operating system upgrade, firewall change, and snapshot copy by the MSP: about $2,000 one-time
  - Independent assessment (P07) and counsel review of the retention schedule and contracts: about $5,000 one-time
- **Accepted:** R-019 (Low; staff can work from home), R-020 (Low; storm checklist).
- **Contract actions:** MSP contract amendment (R-005, R-010) by 2026-12-31; minimum security terms in the three management agreements (R-018) by 2027-03-31; CPA firm and vendor security terms at renewal (R-011).

## 5. Approval
- Principal: approved all treatment plans, the two acceptances, and the budget on 2026-09-18.
- Board of Managers: approved the treatment plans for R-001, R-002, R-003, and R-005 on 2026-09-18.
- Next full review: August 2027, or sooner after a major change (for example, resuming the AI assistant pilot, replacing SYS-11, or adding a subsidiary) or an incident.
