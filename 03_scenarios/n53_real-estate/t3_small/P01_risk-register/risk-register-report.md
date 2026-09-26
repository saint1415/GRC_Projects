# Risk Register Report: Cris Santos Company | Real Estate and Rental and Leasing | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (residential real estate brokerage with property management and an in-house Closing Services division) |
| Size tier | Small (60 employees, plus about 140 contractor sales associates) |
| Vertical | Real Estate and Rental and Leasing |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also satisfies | Written risk assessment, FTC Safeguards Rule 16 CFR 314.4(b)(1) (criteria for rating risks, criteria for assessing confidentiality, integrity, and availability, and how risks are mitigated or accepted) |
| Prepared | 2026-08-14 by the IT Manager (Qualified Individual); R-032 added 2026-08-28 |
| Approved | 2026-09-21 by the COO (Moderate and below) and the majority owner and Broker of Record (High) |

## 1. Scope and risk framing
**Scope.** The Transaction Management and Closing Communications System (TMCC, P02), the property management platform, the CRM, and the business processes in the BIA (P05). That covers every system that holds customer information or other nonpublic personal information, the three escrow accounts, and the service providers that handle that data (`../scenario-facts.md` section 3).

**Why this register matters more than usual.** In this business, the most likely serious loss is not stolen data. It is **stolen money**: closing funds and escrow disbursements sent to a criminal's account after an email is compromised or spoofed. The register therefore rates harm to clients' funds and to the escrow accounts alongside data exposure.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the IT Manager may accept.
- Moderate: the COO may accept, with a treatment plan or a documented reason.
- High and Very High: only the majority owner may accept, and only temporarily with a dated treatment plan. A High risk to clients' closing funds or to escrowed funds may not be accepted without a plan due within 90 days.

This is the company's first written risk assessment. The previous review was an informal IT checklist in 2022.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA, the March 2026 near miss, interviews with the Closing Services Manager, Controller, Director of Property Management, Transaction Coordination Manager, and both Sales Managers, and the gap analysis (P03).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories. A single diverted closing wire (typically $150,000 to $450,000) is rated High.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 3 |
| Moderate | 23 |
| Low | 8 |
| **Total** | **34** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Contractor agent mailbox takeover leads to altered wire instructions and a diverted buyer wire | High | MFA for all contractor accounts; wire instructions only through the portal; forwarding alerts | IT Manager | 2026-11-30 |
| R-002 | Spoofed payoff letter diverts a disbursement from the title escrow trust account | High | Written payoff and disbursement verification procedure with independent callback | Closing Services Manager | 2026-10-31 |
| R-006 | Backups and SaaS data lost along with production | High | Immutable separate-account backups; SaaS backup; quarterly restore tests | IT Manager | 2026-12-31 |
| R-033 | Unauthorized wire from the sales or property management escrow account | Moderate | Dual approval on all escrow wires | Controller | 2026-10-15 |
| R-034 | Seller impersonation of a vacant lot or rental owner | Moderate | Enhanced identity verification for remote sellers | Closing Services Manager | 2026-12-31 |
| R-023 | Tenant screening produces unjustified disparate denials | Moderate | Written criteria, individualized review, disparity testing (P10) | Director of Property Management | 2026-12-31 |

Two of the three High risks share one theme: **the company's money-movement steps trust email.** Contractor agents have no MFA and pass wire instructions by email (R-001), and payoff letters are accepted by email without an independent callback (R-002). Closing those two gaps also reduces five related Moderate risks (R-003, R-004, R-018, R-027, R-031) and supports the escrow duties in Fla. Stat. 475.25(1)(k) and 626.8473. The third High risk (R-006) is the recovery gap that would turn a ransomware attack into a closing shutdown.

R-032 was added on 2026-08-28 after control assessment testing (P07) found five contractor mailboxes auto-forwarding to personal webmail.

## 4. Treatment summary
- **Funded (2026 Q4 budget, $41,000):**
  - MFA licenses and mobile application management for 140 contractor agents
  - MSP-managed EDR with 24x7 alerting
  - Backup redesign and SaaS backup
  - Penetration test of the Closing Communications Portal and the external network
  - Monthly vulnerability scanning
- **Procedure changes (staff time):** written disbursement verification procedure (R-002, R-031), dual approval on all escrow wires (R-033), owner payout change procedure (R-027), same-day contractor offboarding (R-007).
- **Accepted:**
  - R-021: Low, hotspot workaround
  - R-028: Low, monthly reconciliation meets r. 61J2-14.012(2)
- **Contract actions:** service provider inventory and security terms (R-013, R-014), due 2027-03-31.

## 5. Approval
- COO: approved Moderate and Low treatments and acceptances, 2026-09-21.
- Majority owner and Broker of Record: approved the High-risk treatment plans and the budget, 2026-09-21.
- Next full review: August 2027 (16 CFR 314.4(b)(2) periodic reassessment), or sooner after a major change or incident.
