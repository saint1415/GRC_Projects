# Risk Register Report: Cris Santos Company | Real Estate and Rental and Leasing | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. and Cris Santos Title and Closing, LLC (PE-backed residential real estate brokerage with property management and title and closing services) |
| Size tier | Mid-Market (600 employees; about 1,650 contractor agents) |
| Vertical | Real Estate and Rental and Leasing |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2, I-3 values); enterprise roll-up per NIST IR 8286 Rev. 1 |
| Also satisfies | The written risk assessment required by the FTC Safeguards Rule, 16 CFR 314.4(b) and (b)(1)(i)-(iii), for Title and Closing; the periodic reassessment in 314.4(b)(2) |
| Prepared | 2026-08-07 by the Security Manager (Qualified Individual) and the vCISO; R-052 added 2026-09-04 from P07 testing |
| Approved | 2026-09-29: Chief Operating Officer (Moderate and below), Chief Executive Officer (High), President of Title and Closing (co-signs every risk that affects Title and Closing's customer information); presented to the audit committee and to Title and Closing's board of managers the same day |

## 1. Scope and risk framing
**Scope.** All business units (22 sales offices, transaction services, Title and Closing, property management and leasing, inside sales, agent services, finance, and enterprise functions), the TMCC (SYS-01 to SYS-08), the neighboring systems (SYS-09 to SYS-13), about 85 vendors (SYS-14), and the AI tools (SYS-15). Processes and impact values come from the BIA (P05); vulnerabilities come from the gap analysis (P03) and the control assessment (P07).

**Criteria (314.4(b)(1)(i)-(ii)).** Threats and risks are categorized with the SP 800-30 scales below. Confidentiality, integrity, and availability are assessed per system in the SSP (P02 section 6), and the adequacy of existing controls is recorded for each risk in `existing_controls`.

**Who can accept risk (314.4(b)(1)(iii)).**
| Risk level | Who may accept | Conditions |
|---|---|---|
| Very Low and Low | The risk owner (director level or above) | Recorded in the register; reviewed annually |
| Moderate | Chief Operating Officer | Treatment plan or documented reason; reviewed every 6 months |
| High | Chief Executive Officer | Temporary only (up to 12 months) with a dated treatment plan; reported to the audit committee each quarter. For risks to Title and Closing's customer information, the President of Title and Closing must co-sign |
| Very High | Not acceptable | The CEO may approve a temporary exception of up to 90 days only after notifying the audit committee chair, while treatment is under way |

### Risk appetite statements
Approved by the Chief Executive Officer and noted by the audit committee on 2026-09-29.

| Area | Appetite | Statement and measure |
|---|---|---|
| Client funds (payment integrity) | **Very low** | The company will not accept any risk of diverting client funds above Moderate. Every such risk rated High must have a funded treatment that lowers likelihood within 90 days. Measure: funds-diversion risks above Moderate (6 today: R-001, R-002, R-003, R-008, R-021, R-052; target 0 by 2027-03-31) |
| Confidentiality of customer information | **Low** | No risk of a breach affecting 500 or more consumers (the FTC notification threshold) may stay above Moderate. Measure: R-004 and R-031 at Moderate or lower by 2027-06-30 |
| Availability of closings | **Low** | Recovery must meet the BIA RTOs for every High-criticality process (P05). Measure: every High process has a passed recovery test or drill in the last 12 months |
| Regulatory compliance | **Low** | No Safeguards Rule element may stay Not met after 2027-06-30. Zero unresolved trust or escrow reconciliation differences at month-end (Fla. Stat. 626.8473; r. 61J2-14.012) |
| Fair housing and consumer protection | **Very low** | No AI or automated tool may be used in housing decisions or access to brokerage services without the P10 review, and no unexplained disparity flag may persist beyond 2 quarters |
| Third parties | **Moderate**, with conditions | Vendors are used widely, but no service provider receives customer information without security and notice terms in its contract, and every Tier 1 service provider is reassessed each year (P09) |
| Financial loss from cyber events | **Moderate** | Single-event losses up to the $250,000 insurance retention are tolerable. Scenarios above $1 million (the funds transfer fraud sublimit) need a treatment that reduces likelihood, not only insurance |

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the FBI IC3 BEC themes for real estate, the company's own fraud log (37 stopped payee changes and 1 loss in 12 months), the BIA, interviews with every process owner, the gap analysis (P03), and the control assessment (P07).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood of adverse impact were each rated, then combined with **Table G-5**.
3. **Rate impact.** Impact used **Table H-3**, anchored to the BIA impact categories (cost, operations, regulatory, safety, reputation) and to funds at risk.
4. **Determine risk.** Risk level came from **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the two tables, not assigned by hand.
5. **Semi-quantitative view.** `semi_quant_score` gives each risk level its SP 800-30 Appendix I semi-quantitative value (Very High 10, High 8, Moderate 5, Low 2, Very Low 0). `exposure_estimate_usd` gives an order-of-magnitude single-event loss range from the BIA values, used for the enterprise risk roll-up (NIST IR 8286 Rev. 1). The ranges are estimates for prioritizing, not actuarial figures.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 0 |
| High | 9 |
| Moderate | 31 |
| Low | 12 |
| Very Low | 0 |
| **Total** | **52** |

Treatments: 48 Mitigate, 4 Accept (R-012, R-038, R-046, R-049). Status: 24 Open, 24 In progress, 4 Accepted.

Cyber insurance ($10 million limit, $250,000 retention, $1 million funds transfer fraud sublimit) and the underwriter's closing protection letters transfer part of the financial exposure for R-001 to R-004 and R-021. Insurance is not recorded as the treatment for any risk, because it does not stop a client's money from being diverted.

### Top risks (High)
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Agent mailbox takeover; buyer sent altered wire instructions | High | MFA for every agent; agent phishing simulations; SaaS log alerting | Security Manager (Qualified Individual) | 2026-11-30 |
| R-002 | Spoofed payoff or edited payee bank details divert a trust disbursement | High | Two-person rule for every payee edit; portal or callback payoffs | President, Title and Closing | 2026-11-30 |
| R-003 | Owner payout, agent commission, or escrow refund diverted by a bank account change | High | Out-of-band callback and dual approval for all account types | Chief Financial Officer | 2026-11-30 |
| R-004 | Ransomware with theft of closing files | High | Restrict and migrate the file server; vault secrets; restore tests | IT Director | 2027-03-31 |
| R-008 | Portal displays altered wire instructions after a code or pipeline compromise | High | Pipeline controls, scanning, display integrity check | Security Manager (Qualified Individual) | 2027-01-31 |
| R-021 | Seller impersonation; proceeds paid to an impostor | High | Enhanced remote seller verification; tune AI-005 | President, Title and Closing | 2026-12-31 |
| R-031 | Standing SaaS global administrator compromised | High | Just-in-time admin roles; separate admin accounts | Security Manager (Qualified Individual) | 2026-12-31 |
| R-039 | Tenant screening produces disparate outcomes | High | P10 conditions and quarterly disparity testing | Director of Property Management | 2027-01-31 |
| R-052 | External auto-forwarding rules in 6 agent mailboxes (found in P07) | High | Rules removed; block external forwarding; incident investigation | Security Manager (Qualified Individual) | 2026-10-31 |

**Themes.**
- **Money moves on trust (R-001 to R-003, R-008, R-021, R-022, R-052).** Title and Closing's own wires are well defended (portal, callbacks, dual approval, security keys). The weak points are the edges: agents without MFA, payee edits, owner and agent payouts, the portal's own code, and impostor sellers.
- **Contractor agents are the largest user population and the least controlled (R-001, R-006, R-007, R-019, R-027, R-052).** They are about 72% of identities, use personal devices, and are not trained or phished like employees.
- **SaaS is where the evidence lives, and it is not watched (R-005, R-013, R-031, R-032).** Most customer information sits in vendor platforms whose logs are not collected and whose data has no independent copy.
- **Automated decisions about housing (R-039 to R-044).** Five AI tools went live without review. P10 addresses them.

## 4. Treatment summary
**Funded in the FY2027 security plan (approved by the CEO 2026-09-29, $565,000 one-time and $255,000 a year):**
- Agent MFA rollout support and an agent help line through enforcement ($60,000)
- Payee verification workflow in SYS-10 and SYS-13 and a callback logging tool ($90,000)
- SaaS application log integration and alert use cases through the MSSP ($110,000 a year)
- Independent SaaS backup for email, files, and SYS-01 ($45,000 a year)
- Just-in-time SaaS administration ($40,000 a year)
- Portal secure development pipeline, code scanning, and an expanded penetration test ($120,000)
- Vendor risk tooling ($60,000 a year)
- File server migration and the first retention purge ($70,000)
- SOC 2 readiness and Type 2 examination for Title and Closing ($180,000 across 2027)
- Badge readers for 9 office network closets ($45,000)

Each funded item maps to a P07 POA&M entry.

**Accepted (4):** R-012 (Moderate, COO; vendor availability and break-glass accounts), R-038 (Low, COO; provider DoS protection and phone fallback), R-046 (Low, President of Title and Closing; FinCEN rule vacated), R-049 (Low, President of Title and Closing; kiosks reach no customer information).

**Contract actions:** security and notice terms for 24 service providers and the intercompany services agreement (R-016, R-017), due 2026-12-31 to 2027-03-31; title production vendor recovery terms at the 2027 renewal (R-010); secure development terms for the contract development firm (R-008); security duties in the agent agreement (R-001, R-006, R-019), effective 2027-01-01.

## 5. Enterprise and system-level registers
This file is the **enterprise register**. Following NIST IR 8286 Rev. 1, it rolls up to the company's enterprise risk register as one line, "Cybersecurity, payment fraud, and technology resilience", owned by the COO and reported to the audit committee each quarter with the counts above and the top risks.

System-level registers are filtered views of this file, kept by each owner, rather than separate spreadsheets. That keeps one set of ratings.

| System-level register | Owner | Risks in scope |
|---|---|---|
| TMCC (SSP in P02) | Security Manager (Qualified Individual) | 31 risks whose `affected_asset_or_process` names SYS-01 to SYS-08 |
| Title and Closing (the financial institution under 16 CFR 314) | President, Title and Closing | R-001, R-002, R-005, R-010, R-017, R-019, R-021, R-024, R-035, R-044, R-046, R-047 |
| Property management | Director of Property Management | R-003, R-039, R-040, R-045 |
| AI portfolio (P10) | Chief Operating Officer | R-039, R-040, R-041, R-042, R-043, R-044 |

When a system-level review changes a rating, the owner updates this file, and the change flows to the enterprise roll-up.

## 6. Approval
- Chief Operating Officer: approved Moderate and Low treatments and the acceptance of R-012 and R-038, 2026-09-29.
- Chief Executive Officer: approved the High treatment plans, the risk appetite statements, and the FY2027 security budget, 2026-09-29.
- President, Title and Closing: co-signed the Title and Closing register and accepted R-046 and R-049, 2026-09-29.
- Board audit committee and Title and Closing's board of managers: received the results on 2026-09-29. Next report: 2026-12 quarterly meeting.
- Next full risk assessment: July 2027, or sooner after a major change (for example an acquisition, R-050) or a significant incident (314.4(b)(2)).
