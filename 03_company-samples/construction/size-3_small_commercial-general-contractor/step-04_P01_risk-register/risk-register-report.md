# Risk Register Report: Cris Santos Company | Construction | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (commercial and institutional building general contractor) |
| Size tier | Small (60 employees) |
| Vertical | Construction |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also supports | Risk-based decisions for the CMMC Level 1 self-assessment (32 CFR 170.15) and the FAR 52.204-21 gap plan (P03) |
| Prepared | 2026-07-24 by the IT Manager, updated 2026-08-07 after control assessment testing |
| Approved | 2026-08-31 by the CFO (Moderate and below) and the President (High and Very High) |

## 1. Scope and risk framing
**Scope.** The Project Delivery and Payment Platform (PDPP) and the business processes in the BIA (P05). That covers every system that holds Federal Contract Information (FCI), the payment path from pay app to cash receipt and from invoice to subcontractor payment, and the vendors that support them (`../00_company-facts.md` section 3). Client-installed security systems are in scope only for the risks the company creates while installing and commissioning them.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the IT Manager may accept.
- Moderate: the CFO may accept, with a treatment plan or a documented reason.
- High and Very High: only the President may accept, and only temporarily with a dated treatment plan. Any risk that could put a false statement in a federal representation or affirmation is not acceptable at any level; it must be fixed.

This is the company's first documented risk assessment.

## 2. Method
1. **Identify.** Threat sources and events were identified from SP 800-30 Appendices D and E, the BIA, interviews with the CFO, Accounting Manager, Project Managers, Contracts Administrator, and Systems Integration Manager, and the gap analysis (P03). Business email compromise was weighted heavily: the FBI's IC3 reports it in all 50 states (PSA I-091124-PSA), and the company had a near miss in March 2026.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories (P05). One misdirected owner payment of about $1 million is close to a year of the company's net profit, so it rates Very High.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 3 |
| Moderate | 20 |
| Low | 10 |
| **Total** | **34** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Project Manager mailbox takeover redirects an owner's progress payment | Very High | Phishing-resistant MFA for payment roles; inbox-rule alerts; remittance-change notice to owners | IT Manager | 2026-11-30 |
| R-002 | Fraudulent subcontractor bank-change request diverts a payment | High | Call-back verification; second approver in the vendor master; dual ACH approval | Accounting Manager | 2026-09-30 |
| R-006 | Ransomware encrypts cloud workloads and deletes backups | High | Immutable, separate-account backups; quarterly restore tests | IT Manager | 2026-12-31 |
| R-007 | Cannot reach Final Level 1 (Self) CMMC status before the next DoD award | High | Close FAR 52.204-21 gaps; self-assess; SPRS entry and affirmation | IT Manager | 2026-12-15 |
| R-009 | Covered video surveillance equipment delivered on a federal project | Moderate | Section 889 screening in submittal review; replace FC-1 equipment | Systems Integration Manager | 2026-10-31 |
| R-010 | Client facility security details leak from the file share | Moderate | Password vault; restricted folders; managed commissioning laptops | Systems Integration Manager | 2026-10-31 |
| R-020 | Internet-facing file-transfer portal used to reach internal servers | Moderate | Separate public subnet; vulnerability scanning | IT Manager | 2026-10-31 |

The Very High and two of the three High risks share one theme: **money moves on the strength of an email.** Owners pay the company, and the company pays subcontractors, based on instructions that nobody verifies out of band (R-001, R-002). Fixing payment verification and phishing-resistant MFA also reduces five related Moderate risks (R-003, R-004, R-005, R-017, R-034) and one Low risk (R-024).

The third High risk (R-007) is a contract-eligibility risk. CMMC Level 1 allows no POA&Ms (32 CFR 170.21(a)(1)): every one of the 15 FAR requirements must be met before the President can affirm in SPRS. Most of the work that closes R-007 is the same work in P03 and P07.

R-009 was re-rated on 2026-08-07 after control assessment testing (P07) found covered video surveillance equipment at the FC-1 VA clinic. The likelihood of initiation moved to High because the event had already happened once.

## 4. Treatment summary
- **Funded (2026 Q4 budget, $41,000):**
  - Security keys for 30 payment-role and executive users, and conditional access
  - Lookalike-domain registration and monitoring
  - Immutable backup redesign
  - Device management for 20 tablets and 2 commissioning laptops
  - Password vault for client system credentials
  - Monthly vulnerability scanning by the MSP
  - Phishing and payment-fraud training
  - MSP labor for the CMMC Level 1 readiness work
- **Separately funded:** replacement of the FC-1 covered video surveillance equipment ($38,000, project cost).
- **Accepted:** R-030 (Low; telematics shared login, accepted by the IT Manager; revisit at the 2027 contract renewal).
- **Transferred in part:** the cyber policy's $250,000 social engineering sublimit covers part of R-001 and R-002. It is far below a single owner payment, so it does not replace the controls.
- **Contract actions:** AI vendor enterprise terms (R-011, R-014) by 2026-10-15; subcontract template flowdowns (P03) by 2026-10-31.

## 5. Approval
- IT Manager: accepted R-030 (Low), 2026-08-31.
- CFO: approved Moderate and Low treatments, 2026-08-31.
- President: approved the Very High and High treatment plans and the budget, 2026-08-31. The President did not accept any High or Very High risk; all four are being treated.
- Next full review: July 2027, or sooner after a major change, an incident, or a new DoD contract.
