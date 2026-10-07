# Risk Register Report: Cris Santos Company | Finance and Insurance | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (state-registered investment adviser) |
| Size tier | Sole Proprietorship (owner-adviser only, 0 employees) |
| Vertical | Finance and Insurance |
| Method | NIST SP 800-30 Rev. 1 (qualitative 5-level scales; Tables G-5 and I-2) |
| Also supports | FTC Safeguards Rule risk assessment, 16 CFR 314.4(b). A **written** assessment with the criteria in 314.4(b)(1) is not required at this size (314.6: fewer than 5,000 consumers), but the program must still be based on a risk assessment. This is the adviser's first one |
| Prepared | 2026-07-17 by the owner-adviser, with the on-call IT consultant (services agreement since 2026-07-10) |
| Risk owner and approver | Owner-adviser (owner, Qualified Individual, and risk acceptor for every risk) |
| Approved | 2026-08-31 |

## 1. Scope and risk framing
**Scope.** The whole business as one system: SYS-01 to SYS-10, the paper files in the locked cabinet, and the contracted services (custodian, SaaS vendors, IT consultant, compliance consultant). Processes come from the BIA (P05).

**Risk tolerance.** The owner-adviser owns and accepts every risk. Because the same person proposes and approves, the owner applies three fixed rules:
- Low and Very Low: may be accepted, with the reason written in the register.
- Moderate: may be accepted only with a dated treatment plan or a written reason.
- High and Very High: must be treated with a dated plan. Not accepted as-is. Any risk that can move client money without the client's authority is never accepted at High.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the missing-controls list in `../00_company-facts.md` section 4, the gap analysis (P03), the 2026-06-18 near miss, and a walk through the laptop, phone, and SaaS accounts with the IT consultant on 2026-07-15.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (other sources), and likelihood of adverse impact, each on the 5-level scale. Combined with **Table G-5**.
3. **Rate impact.** Table H-3 levels, using the BIA impact categories (including client financial harm).
4. **Determine risk.** **Table I-2.** The `overall_likelihood` and `risk_level` columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results
| Risk level | Count |
|---|---|
| High | 3 |
| Moderate | 7 |
| Low | 5 |
| **Total** | **15** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Fraudulent wire requested from a client's compromised email | High | Callback to the number on file before any money movement request; client letter; training | Owner-adviser | 2026-09-30 |
| R-002 | Takeover of the owner's email account | High | MFA, unique passphrase, monthly sign-in and forwarding-rule review | Owner-adviser | 2026-09-15 |
| R-003 | Takeover of the CRM, portfolio platform, or e-signature account | High | MFA on every SaaS account; password manager | Owner-adviser | 2026-09-15 |
| R-004 | Loss of the unencrypted USB backup drive | Moderate | Encrypted drive in the home safe; wipe the old one | Owner-adviser | 2026-09-30 |
| R-006 | Client statements in a consumer AI assistant | Moderate | Avoid: do not resume; delete history; business plan only (P10) | Owner-adviser | 2026-09-30 |
| R-005 | Owner-adviser unavailable (single point of failure) | Moderate | Successor adviser arrangement; sealed recovery codes; hardware key | Owner-adviser | 2026-12-31 |

The three High risks share one cause: **the adviser trusts email.** Money movement requests are accepted by email, and the email account and the other SaaS accounts that hold client data are protected only by a reused password. Two free changes reduce all three within two weeks of adoption: turn on MFA everywhere, and call the client at the number on file before acting on any request to move money. The 2026-06-18 near miss was stopped by the custodian, not by the adviser; the callback rule makes the adviser the first line of defense.

## 4. Treatment summary
- **Free fixes first (by 2026-09-30):** MFA on five services, password manager (about $40 a year), callback rule and client letter, encrypted USB drive (about $100), stopping the consumer AI assistant, and adopting the P08 runbook.
- **Budgeted (about $300 a year):** an encrypted cloud backup of mail and files (R-008, R-011) and a separate router for the business network (R-009).
- **Contract actions by 2026-10-31:** security and confidentiality terms with the compliance consultant; vendor list and review (R-007).
- **By 2026-12-31:** successor adviser arrangement and sealed recovery codes (R-005); records index confirmed against the Florida rule (R-011).
- **Accepted (Low):** R-013 (custodian or platform outage; the custodian takes phone orders) and R-014 (hurricane; all systems are SaaS).

## 5. Approval
Owner-adviser, 2026-08-31: approved all treatment plans and the two acceptances. Next full review July 2027, or sooner after a new system, a new vendor, a hire, a move to SEC registration, or an incident.
