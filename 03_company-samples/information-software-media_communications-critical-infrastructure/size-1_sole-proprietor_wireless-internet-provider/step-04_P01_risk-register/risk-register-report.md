# Risk Register Report: Cris Santos Company | Communications | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (owner-operated wireless internet service provider) |
| Size tier | Sole Proprietorship (owner-operator only, 0 employees) |
| Vertical | Communications |
| Method | NIST SP 800-30 Rev. 1 (qualitative 5-level scales; Tables G-5 and I-2) |
| Also supports | The CPNI duty to "take reasonable measures to discover and protect against attempts to gain unauthorized access to CPNI" (47 CFR 64.2010(a)). This is the company's first risk assessment |
| Prepared | 2026-07-24 by the owner-operator, with the on-call network consultant (under confidentiality and security terms since 2026-07-17) |
| Risk owner and approver | Owner-operator (owner, security lead, and risk acceptor for every risk) |
| Approved | 2026-08-31 |

## 1. Scope and risk framing
**Scope.** The whole business as one system: SYS-01 to SYS-08, the four tower sites, paper sign-up forms in the home office, and the contracted services (upstream fiber provider, wholesale VoIP provider, billing vendor, network consultant, tower contractor, bookkeeper). Processes come from the BIA (P05).

**Risk tolerance.** The owner-operator owns and accepts every risk. Because the same person proposes and approves, the owner applies three fixed rules:
- Low and Very Low: may be accepted, with the reason written in the register.
- Moderate: may be accepted only with a dated treatment plan or a written reason.
- High and Very High: must be treated with a dated plan. Not accepted as-is. A High risk to 911 calling or to CPNI is never accepted.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the missing-controls list in `../00_company-facts.md` section 4, the gap analysis (P03), an external port check of the network's public addresses, and a walk through the SaaS accounts, laptop, router, and SITE-1 and SITE-3 with the network consultant.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (other sources), and likelihood of adverse impact, each on the 5-level scale. Combined with **Table G-5**.
3. **Rate impact.** Table H-3 levels, using the BIA impact categories (P05 section 3).
4. **Determine risk.** **Table I-2.** The `overall_likelihood` and `risk_level` columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results
| Risk level | Count |
|---|---|
| High | 3 |
| Moderate | 10 |
| Low | 2 |
| **Total** | **15** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Edge router takeover through its management interface or an unpatched flaw | High | Firmware update, management filters, named accounts, remote logging, advisory tracking | Owner-operator | 2026-09-15 |
| R-002 | VoIP reseller portal takeover and export of all call detail | High | Portal MFA; password manager; monthly activity review | Owner-operator | 2026-09-15 |
| R-009 | Upstream fiber cut or power loss takes down all service and 911 calling | High | Automatic generator transfer; price a second upstream | Owner-operator | 2027-06-30 |
| R-003 | Call history disclosed through the AI support assistant | Moderate | CPNI only inside a signed-in portal session; change notices | Owner-operator | 2026-10-31 |
| R-005 | FCC enforcement for missed CPNI certifications and unfiled CALEA policies | Moderate | File with counsel; accurate 2026 certification | Owner-operator | 2027-03-01 |
| R-006 | CPNI breach notice sequence missed | Moderate | P08 runbook; reporting facility and contacts | Owner-operator | 2026-09-30 |

Two of the three High risks share one cause: **the two places CPNI can be reached from outside (the router and the VoIP portal) were protected by a password alone.** Both fixes cost little: a firmware update and filter change in one maintenance window, and turning on MFA the vendor already offers. The third High risk (R-009) is about availability, not security. It costs real money, so its due date is set for after the next budget year, and the generator's automatic transfer switch comes first.

**New risk from the control assessment.** R-015 (vendor-default credentials) came from the P07 test on 2026-07-23, which found a SITE-3 access point with the default password and SNMP community string. The owner changed them the same day; the remaining work is checking every device.

## 4. Treatment summary
- **Free or low-cost fixes first (by 2026-09-30):** VoIP portal MFA, router firmware and filters, deleting old CDR exports, adopting the P08 runbook and locating the FCC reporting facility.
- **Budgeted (about $1,500 the first year):** password manager, a small log server at SITE-1, generator automatic transfer switch, and counsel time for the CPNI and CALEA filings.
- **Filings with counsel:** CALEA policies through CEFS by 2026-11-30; CPNI certification for calendar year 2026 by 2027-03-01 (R-005).
- **Larger decision (2027):** a second upstream for R-009.
- **Accepted (Low):** R-013 (vendor breach). The billing vendor's SOC 2 report supports acceptance; the VoIP provider is asked for breach notice terms at renewal.

## 5. Approval
Owner-operator, 2026-08-31: approved all treatment plans and the one acceptance. Next full review July 2027, or sooner after a new service, a new vendor, a hire, a new tower site, or an incident.
