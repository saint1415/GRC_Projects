# Risk Register Report: Cris Santos Company | Transportation and Warehousing | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (freight forwarder and customs broker) |
| Size tier | Sole Proprietorship (owner only, 0 employees) |
| Vertical | Transportation and Warehousing |
| Method | NIST SP 800-30 Rev. 1 (qualitative 5-level scales; Tables G-5 and I-2) |
| Also supports | Reasonable security measures under Fla. Stat. 501.171(2), and the owner's responsible supervision and control of the brokerage (19 CFR 111.28(a)). This is the business's first risk assessment |
| Prepared | 2026-08-21 by the owner, with the on-call IT consultant |
| Risk owner and approver | Owner (owner, security officer, and risk acceptor for every risk) |
| Approved | 2026-09-14 |

## 1. Scope and risk framing
**Scope.** The whole business as one system: SYS-01 to SYS-10, the paper records in the home office, and the contracted services (bookkeeper, IT consultant) and key vendors. Processes come from the BIA (P05).

**Risk tolerance.** The owner owns and accepts every risk. Because the same person proposes and approves, the owner applies three fixed rules:
- Low and Very Low: may be accepted, with the reason written in the register.
- Moderate: may be accepted only with a dated treatment plan or a written reason.
- High and Very High: must be treated with a dated plan. Not accepted as-is. Any risk that could put client money in a criminal's account or the broker license at risk is never accepted at High.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the missing-controls list in `../00_company-facts.md` section 4, the duties in 19 CFR Part 111 (P03), and a walk through the laptop, phone, router, and SaaS accounts with the IT consultant.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (other sources), and likelihood of adverse impact, each on the 5-level scale. Combined with **Table G-5**.
3. **Rate impact.** Table H-3 levels, using the BIA impact categories (P05).
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
| R-001 | Takeover of the business email account | High | Remove the MFA bypass; authenticator MFA; password manager; monthly sign-in review | Owner | 2026-09-30 |
| R-002 | Payment redirection to a criminal account | High | Call-back before any new or changed payee; wire alerts; client notice | Owner | 2026-09-30 |
| R-003 | Ransomware encrypts the records archive and steals client files | High | Independent versioned backup; folder protection; training; P08 runbook | Owner | 2026-10-31 |
| R-004 | Missed 72-hour CBP breach notice or Florida notices | Moderate | P08 runbook and notification matrix; walkthrough | Owner | 2026-10-31 |
| R-005 | Owner unavailable (single point of failure) | Moderate | Backup broker agreement; sealed recovery codes; records custodian | Owner | 2026-12-31 |
| R-007 | Client records shared without written client authorization | Moderate | Client authorization; vendor list; AI business plan (P10) | Owner | 2026-10-31 |

The three High risks share one cause: **the business moves client money and confidential client records through one email account, one laptop, and one person, with no second check.** Email takeover (R-001) is usually the first step of payment redirection (R-002), and both start with a phishing email. Removing the app password costs nothing and takes minutes. The call-back rule costs nothing and stops R-002 even if email is taken over.

**Loop from P07.** Testing on 2026-08-20 found the home router admin password still set to the factory default and showed that the former bookkeeper could still sign in to the accounting SaaS. Both were added to R-008 and R-006 before approval.

## 4. Treatment summary
- **Free fixes first (by 2026-09-30):** delete the email app password and block legacy sign-in (R-001); the call-back rule and client notice (R-002); named bookkeeper account and accounting MFA (R-006); wipe the 2019 laptop (R-012); unique passphrases in a password manager (R-015).
- **Budgeted (about $400 a year):** a password manager, an independent versioned backup for the records archive, and a business plan for the AI assistant or no AI use with client data.
- **Legal and contract actions (by 2026-11-30):** written client authorization for service providers (R-007) and the alternative storage notice to CBP Regulatory Audit (R-009), both confirmed with customs counsel first.
- **Accepted (Low):** R-013 (customs software outage; the vendor's 4-hour RTO meets the BIA) and R-014 (hurricane; the work can move with the laptop and phone).

## 5. Approval
Owner, 2026-09-14: approved all treatment plans and the two acceptances. Next full review August 2027, or sooner after a new system, a new vendor, a first employee, or an incident.
