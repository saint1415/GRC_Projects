# Risk Register Report: Cris Santos Company | Health Care and Social Assistance | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (solo primary care physician practice) |
| Size tier | Sole Proprietorship (physician-owner only, 0 employees) |
| Vertical | Health Care and Social Assistance |
| Method | NIST SP 800-30 Rev. 1 (qualitative 5-level scales; Tables G-5 and I-2) |
| Also satisfies | HIPAA risk analysis, 45 CFR 164.308(a)(1)(ii)(A). This is the practice's first one |
| Prepared | 2026-07-24 by the physician-owner, with the on-call IT consultant (under BAA since 2026-07-17) |
| Risk owner and approver | Physician-owner (owner, Privacy Officer, Security Officer, and risk acceptor for every risk) |
| Approved | 2026-08-31 |

## 1. Scope and risk framing
**Scope.** The whole business as one system: SYS-01 to SYS-07, paper records in the exam suite, and the four contracted services (billing company, answering service, IT consultant, cloud fax). Processes come from the BIA (P05).

**Risk tolerance.** The physician-owner owns and accepts every risk. Because the same person proposes and approves, the owner applies three fixed rules:
- Low and Very Low: may be accepted, with the reason written in the register.
- Moderate: may be accepted only with a dated treatment plan or a written reason.
- High and Very High: must be treated with a dated plan. Not accepted as-is. Any risk to patient safety rated High is never accepted.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the missing-controls list in `../scenario-facts.md` section 4, the gap analysis (P03), and a walk through the laptop, phone, and SaaS accounts with the IT consultant.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (other sources), and likelihood of adverse impact, each on the 5-level scale. Combined with **Table G-5**.
3. **Rate impact.** Table H-3 levels, using the BIA impact categories.
4. **Determine risk.** **Table I-2.** The `overall_likelihood` and `risk_level` columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results
| Risk level | Count |
|---|---|
| High | 3 |
| Moderate | 9 |
| Low | 3 |
| **Total** | **15** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware on the laptop with theft of downloads and email | High | Email MFA, disk encryption, business file plan with backups, training | Physician-owner | 2026-10-31 |
| R-002 | Takeover of the personal email account | High | MFA now; then a business plan with a BAA | Physician-owner | 2026-09-15 |
| R-004 | Theft or loss of the unencrypted laptop | High | Built-in full-disk encryption | Physician-owner | 2026-09-15 |
| R-003 | PHI in a consumer email account with no BAA | Moderate | Business plan with a BAA; migrate and delete | Physician-owner | 2026-10-31 |
| R-009 | AI scribe app used with no BAA or consent | Moderate | Avoid: do not resume; deletion request; breach risk assessment (P10) | Physician-owner | 2026-09-30 |
| R-010 | Physician-owner unavailable (single point of failure) | Moderate | Coverage arrangement; sealed recovery codes | Physician-owner | 2026-12-31 |

The three High risks share one cause: **patient information sits on an unencrypted laptop and in a consumer email account protected only by a password.** Two built-in settings (email MFA and disk encryption) cost nothing and reduce R-001, R-002, and R-004 within two weeks of adoption. Moving email and files to a business plan with a BAA then closes R-003 and most of R-012.

## 4. Treatment summary
- **Free or low-cost fixes first (by 2026-09-30):** email MFA, disk encryption, confirming the IT consultant's remote-access safeguards, stopping the AI scribe, and adopting the P08 runbook.
- **Budgeted (about $600 a year):** a business-grade email and file plan with a BAA, a password manager, and a practice-owned router for the suite.
- **Contract actions by 2026-10-31:** BAA with the answering service (R-007); vendor deletion request and breach risk assessment for the AI scribe trial (R-009).
- **Accepted (Low):** R-011 (EHR outage; vendor commitments meet the BIA) and R-015 (hurricane; the EHR is reachable from home).

## 5. Approval
Physician-owner, 2026-08-31: approved all treatment plans and the two acceptances. Next full review July 2027, or sooner after a new system, a new vendor, a hire, or an incident.
