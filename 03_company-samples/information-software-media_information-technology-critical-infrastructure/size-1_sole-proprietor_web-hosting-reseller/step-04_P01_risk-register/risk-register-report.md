# Risk Register Report: Cris Santos Company | Information Technology | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (web hosting reseller) |
| Size tier | Sole Proprietorship (owner only, 0 employees) |
| Vertical | Information Technology |
| Method | NIST SP 800-30 Rev. 1 (qualitative 5-level scales; Tables G-5 and I-2) |
| Also supports | The "reasonable measures" duty of Fla. Stat. 501.171(2) and the FTC's reasonable-security expectations (P03). This is the company's first risk assessment |
| Prepared | 2026-08-21 by the owner, challenged by the contract security consultant |
| Risk owner and approver | Owner (risk owner and risk acceptor for every risk) |
| Approved | 2026-09-28 |

## 1. Scope and risk framing
**Scope.** The whole business as one system: the Hosting Control Plane and Customer Portal (SYS-01 to SYS-07), the consumer AI chat assistant (SYS-09), the freelance developer's access, and the upstream provider and SaaS vendors the business depends on. Processes come from the BIA (P05).

**What makes this business different.** A reseller's tools reach every customer at once. One stolen administrator login can change 120 websites or redirect 230 domains in minutes. Impact is therefore rated on the harm to customers and their shoppers, not only on the company's own revenue.

**Risk tolerance.** The owner owns and accepts every risk. Because the same person proposes and approves, three fixed rules apply:
- Low and Very Low: may be accepted, with the reason written in the register.
- Moderate: may be accepted only with a dated treatment plan or a written reason.
- High and Very High: must be treated with a dated plan. Not accepted as-is. A risk that could reach many customers' sites at once is never accepted above Moderate.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the missing-controls list in `../00_company-facts.md` section 4, the control map (P04), the 2025 and 2026 incidents, and a walk through every control plane tool with the consultant.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (other sources), and likelihood of adverse impact, each on the 5-level scale. Combined with **Table G-5**.
3. **Rate impact.** Table H-3 levels, using the BIA impact categories (P05 section 3).
4. **Determine risk.** **Table I-2.** The `overall_likelihood` and `risk_level` columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 3 |
| Moderate | 9 |
| Low | 2 |
| **Total** | **15** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Dashboard account takeover pushes malicious code to 120 customer sites | Very High | MFA on every dashboard account; freelancer limited to assigned sites; owner-only bulk pushes; weekly log review | Owner | 2026-10-15 |
| R-002 | Portal administrator takeover uses stored API credentials against every account and domain | High | Portal MFA now, security key later; restricted API key; independent backups | Owner | 2026-10-15 |
| R-004 | Mass exploitation of unpatched hosting-only sites; upstream suspends the whole reseller account | High | Monthly vulnerability notices; free automatic security updates; Terms of Service patching clause | Owner | 2026-12-31 |
| R-009 | Owner unavailable or phone lost; nobody can act for customers | High | Emergency access envelope; backup-operator arrangement; offline contact list | Owner | 2026-12-31 |
| R-007 | Missed 10-day Florida third-party agent notice to customers | Moderate | P08 runbook, contact list, documented determinations | Owner | 2026-10-31 |
| R-008 | AI triage dismisses a real compromise | Moderate | No auto-dismiss in protected categories; weekly review (P10) | Owner | 2026-10-15 |

The Very High and High risks share one cause: **the tools that reach every customer are protected less well than the owner's own email.** Two free settings (MFA on the portal administrator login and on the freelancer's dashboard account) cut R-001 and R-002 within two weeks of adoption. The other two High risks (R-004, R-009) are about who does what when the owner is not watching: hosting-only customers who never patch, and a business with no second operator.

**New risk from the control assessment (P07).** R-012 (forgotten contractor account) was added after P07 testing on 2026-08-19 found a former freelance designer's dashboard account still active nine months after the engagement ended. It was disabled the same day.

## 4. Treatment summary
- **Free fixes first (by 2026-10-15):** portal and dashboard MFA, freelancer role reduction, AI triage settings, correcting the website claims (R-006), and stopping customer data in the consumer AI tool (R-011, by 2026-09-30).
- **Budgeted (about $1,500 a year):** an independent backup service for all sites and mailboxes (R-005, R-010), a business password manager vault for customer credentials (R-003), and two security keys (R-002).
- **Contract actions:** security terms for the freelancer (R-001, R-012); Terms of Service clauses on patching, backups, and incident notice (R-004, R-007).
- **Insurance:** decide on the quoted technology errors and omissions policy with a cyber endorsement by 2026-12-31 (shares part of R-001 and R-002; does not replace any control).
- **Accepted (Low):** R-013 (device theft; encryption and MFA limit the harm) and R-014 (hurricane; everything is cloud-hosted).

## 5. Approval
Owner, 2026-09-28: approved all treatment plans and the two acceptances. Next full review August 2027, or sooner after a new tool, a new contractor, a change of upstream provider, or an incident.
