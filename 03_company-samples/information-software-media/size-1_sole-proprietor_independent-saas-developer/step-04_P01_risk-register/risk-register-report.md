# Risk Register Report: Cris Santos Company | Information | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent B2B SaaS software publisher) |
| Size tier | Sole Proprietorship (owner-developer only, 0 employees) |
| Vertical | Information |
| Method | NIST SP 800-30 Rev. 1 (qualitative 5-level scales; Tables G-5 and I-2) |
| Also supports | Reasonable security under FTC Act Section 5 (N51-R01): the FTC's guidance starts with knowing your risks. Also the SOC 2 risk assessment criteria (P09, CC3.2) |
| Prepared | 2026-08-28 by the owner-developer, after the 2026-08-27 tests with the contract security consultant |
| Risk owner and approver | Owner-developer (owner, security and privacy lead, and risk acceptor for every risk) |
| Approved | 2026-09-25 |

## 1. Scope and risk framing
**Scope.** The whole business as one system: the Multi-tenant Booking Platform (SYS-01 to SYS-09), the support contractor's access, and the sub-processors that receive subscriber data. Processes come from the BIA (P05).

**Risk tolerance.** The owner-developer owns and accepts every risk. Because the same person proposes and approves, the owner applies fixed rules (POL-01 4.4):
- Low and Very Low: may be accepted, with the reason written in the register.
- Moderate: may be accepted only with a dated treatment plan or a written reason.
- High and Very High: must be treated with a dated plan. Never accepted as they are.
- Any risk that would break a promise made to subscribers in the Terms of Service, DPA, or website is treated, whatever its level.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the missing-controls list in `../00_company-facts.md` section 4, the cloud mapping (P04), and the consultant's secret scan and configuration review on 2026-08-27.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (other sources), and likelihood of adverse impact, each on the 5-level scale, combined with **Table G-5**.
3. **Rate impact.** Table H-3 levels, using the BIA impact categories. Very High means an event that could end the business: losing most subscribers or their data at once.
4. **Determine risk.** **Table I-2.** The `overall_likelihood` and `risk_level` columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 2 |
| Moderate | 10 |
| Low | 2 |
| **Total** | **15** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Production secrets stolen from the laptop and used to copy the database | Very High | Secrets out of the `.env` file, rotation, scoped token, database allow list, log review | Owner-developer | 2026-10-31 |
| R-002 | Takeover of the hosting or repository account | High | Security keys, shorter sessions, sign-in alerts | Owner-developer | 2026-11-30 |
| R-006 | Owner-developer unavailable or locked out (single point of failure) | High | Sealed emergency kit; standby developer | Owner-developer | 2026-12-31 |
| R-003 | Shared super-admin login used by the support contractor | Moderate | Named support role with MFA; admin action log | Owner-developer | 2026-11-30 |
| R-007 | Data loss with a restore slower than the BIA allows | Moderate | Backups outside the account; photo versioning; restore tests | Owner-developer | 2026-12-31 |
| R-011 | Public statements that do not match practice (FTC deception) | Moderate | Correct the website and release note now | Owner-developer | 2026-10-15 |

The three highest risks share one cause: **everything depends on one person and a handful of secrets that person carries on one laptop and one phone.** The cheapest fixes come first: rotating secrets, deleting the `.env` file and the local data copy, and turning on registrar MFA cost nothing and cut R-001 and R-012 within weeks.

## 4. Treatment summary
- **Free fixes by 2026-10-31:** correct public statements (R-011); registrar MFA and lock (R-012); secrets moved and rotated, database allow list (R-001); high-severity library fixes (R-005); Smart Replies auto-send off and model provider DPA (R-009, R-010); P08 runbook and contact list (R-013).
- **Owner time by 2026-11-30 and 2026-12-31:** support role and admin action log (R-003); data deletion (R-014); backups outside the account and restore steps (R-007); emergency kit and standby developer (R-006).
- **Budgeted (about $900 a year):** two hardware security keys, a secrets feature in the password manager plan, an outside storage account for backup copies, a security course, and a few hours of consultant time each year.
- **Larger work by 2027-03-31:** automated tenant isolation tests and a second isolation layer (R-004).
- **Accepted (Low):** R-008 (provider regional outage) and R-015 (hurricane at the home office).

R-001, R-002, and R-006 keep a target residual risk of Moderate even after treatment, because a one-person business cannot remove its dependence on one administrator. Cyber insurance (quoted, not bought) is the remaining transfer option; the owner decides on it by 2026-12-31 (P08).

## 5. Approval
Owner-developer, 2026-09-25: approved all treatment plans and the two acceptances. Next full review August 2027, or sooner after a new sub-processor, a new AI feature, a contractor change, or an incident.
