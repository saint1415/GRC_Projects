# Risk Register Report: Cris Santos Company | Construction | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (commercial and institutional building general contractor) |
| Size tier | Micro (7 employees) |
| Vertical | Construction |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also supports | Risk-based decisions for the CMMC Level 1 self-assessment (32 CFR 170.15) and the FAR 52.204-21 gap plan (P03) |
| Prepared | 2026-07-31 by the Office Manager (security and compliance lead) with the MSP lead technician |
| Updated | R-008 re-rated on 2026-07-28 during fieldwork, after the FC-1 submittal finding; R-021 accepted and closed on 2026-08-31 |
| Approved | 2026-08-31 by the Owner and President |

## 1. Scope and risk framing
**Scope.** The business and its key vendors. That covers every system in the Project and Payment System (SYS-01 to SYS-07 in `../00_company-facts.md`), the payment path from pay app to cash receipt and from invoice to subcontractor payment, the federal contract duties, and the vendors that hold company data or run its IT: the SYS-01, accounting, payroll, and productivity suite vendors, the MSP and its backup vendor, the bank, and the AI tool vendor.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the Office Manager may accept.
- Moderate: only the Owner may accept, with a treatment plan or a written reason.
- High and Very High: not accepted. The Owner approves a dated treatment plan instead.
- A risk that could make a federal representation or affirmation inaccurate is not accepted at any level; it must be fixed.

This is the company's first documented risk assessment.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA (P05), the gap analysis (P03), and interviews with all 5 staff who use systems and with the MSP lead technician (2026-07-20 to 2026-07-31). Business email compromise was weighted heavily: the FBI's IC3 reports it in all 50 states (PSA I-091124-PSA), and the company had a near miss in May 2026.
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories (P05). One misdirected owner payment of up to $78,000 is close to a year of the company's profit, so it rates Very High. Losing the DoD award (about 29% of a year's revenue) rates High.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 2 |
| Moderate | 16 |
| Low | 5 |
| **Total** | **24** |

Status: 11 In progress, 12 Open, 1 Closed (R-021 accepted).

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Project Manager mailbox takeover redirects an owner's progress payment | Very High | Security keys for payment roles; inbox-rule alerts; remittance-change notice to owners | Office Manager | 2026-10-31 |
| R-002 | Spoofed supplier or subcontractor bank change diverts a payment | High | Call-back to a known number; Owner approves each change; hold on first payment | Office Manager | 2026-09-30 |
| R-006 | Cannot reach Final Level 1 (Self) CMMC status before the DoD award | High | Close FAR 52.204-21 gaps; self-assess; SPRS entry and affirmation | Office Manager | 2026-12-15 |
| R-016 | Insurer denies a funds transfer fraud claim for lack of call-back records | Moderate | Call-back log; confirm the procedure with the broker | Owner and President | 2026-09-30 |
| R-013 | Email and files cannot be restored after ransomware or deletion | Moderate | Restore test; immutable retention; MFA on the backup console | Office Manager | 2026-10-31 |
| R-008 | Covered video surveillance equipment delivered on a federal job | Moderate | Section 889 check in submittal review; subcontract rider | Project Manager and Estimator | 2026-09-30 |
| R-009 | FCI and owners' drawings in personal email and the AI tool | Moderate | Block forwarding; approved-systems list; AI tool conditions (P10) | Project Manager and Estimator | 2026-10-15 |

**The common theme is that money moves on the strength of an email.** Owners pay the company, and the company pays subcontractors, based on instructions that nobody verifies out of band (R-001, R-002). The same fix, a call-back to a known number with a second person's approval, also makes the insurance coverage usable (R-016) and reduces R-003 and R-004. Security keys and mailbox alerts also reduce R-005 and R-017.

The second High risk (R-006) is a contract-eligibility risk. CMMC Level 1 allows no POA&Ms (32 CFR 170.21(a)(1)). Every FAR 52.204-21 requirement must be met before the Owner can affirm in SPRS, and the affirmation must be in SPRS before award (32 CFR 170.15(b)). Most of the work that closes R-006 is the same work in P03 and P07.

**Risks found or changed during the work:**
- R-008 was re-rated on 2026-07-28 after the gap analysis found a covered manufacturer's network video recorder in an approved FC-1 submittal. The likelihood of initiation moved to High because it had already happened once. The equipment was never delivered; the submittal was rejected and a compliant one approved on 2026-08-07.
- R-011: the departed Superintendent's SYS-01 and suite accounts were disabled on 2026-07-21, the day they were found. The sign-in logs showed no use after the termination date. The process gap remains open.

## 4. Treatment summary
- **Funded (2026 Q4, approved by the Owner; about $8,900 one-time and $1,630 a year):**
  - Security keys for the 3 payment-role users (2 each): about $300 one-time
  - MSP project time for DMARC, mailbox alerts, guest Wi-Fi, MFA on administrator logins, the restore test, and CMMC Level 1 evidence: about $3,600 one-time
  - Independent control assessment in 2026 (P07): $3,500 one-time
  - Counsel review of the SAM representations and the affirmation evidence binder: about $1,500 one-time
  - Device management for 5 phones and 2 tablets: about $420 a year
  - Security awareness training with phishing simulations for 5 users: about $400 a year
  - Backup upgrade to 90-day immutable retention: about $500 a year
  - Password manager for 5 users: about $250 a year
  - Two look-alike domain registrations: about $60 a year
- **Accepted:** R-021 (Low; accepted by the Office Manager because the SYS-01 vendor's recovery commitments meet the BIA).
- **Transferred in part:** the cyber policy's $25,000 social engineering sublimit covers part of R-001 and R-002, but only with call-back records (R-016). It is well below one pay app, so it does not replace the controls.
- **Contract actions:** AI tool enterprise terms or stop uploading FCI (R-009, R-023) by 2026-10-15; Section 889 and FAR 52.204-21 subcontract rider (P03) by 2026-09-30; MSP incident notice term (R-014) at renewal by 2026-12-31.

## 5. Approval
- Office Manager: accepted R-021 (Low), 2026-08-31.
- Owner and President: approved all treatment plans and the budget, 2026-08-31. The Owner did not accept any High or Very High risk; all three are being treated.
- Next full review: July 2027, or sooner after a major change (for example, a DoD award, a new SaaS that holds FCI, or wider use of the AI tool), an incident, or a near miss.
