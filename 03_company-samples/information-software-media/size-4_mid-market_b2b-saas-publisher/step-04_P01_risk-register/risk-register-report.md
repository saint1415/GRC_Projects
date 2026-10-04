# Risk Register Report: Cris Santos Company | Information | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed B2B SaaS publisher of a multi-tenant customer service platform) |
| Size tier | Mid-Market (600 employees) |
| Vertical | Information |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2, I-3 values); enterprise roll-up per NIST IR 8286 Rev. 1 |
| Also satisfies | HIPAA risk analysis and risk management for the healthcare cell, as a business associate (45 CFR 164.308(a)(1)(ii)(A)-(B)); the FTC's expectation that a company assess risks to the personal information it holds (Start with Security, lesson 1) |
| Prepared | 2026-08-07 by the GRC Manager and the Director of Security; R-050 added 2026-09-02 from P07 testing |
| Approved | 2026-09-29: Chief Technology Officer (Moderate and below), Chief Executive Officer (High and Very High); presented to the board audit committee the same day |

## 1. Scope and risk framing
**Scope.** All business units, the Customer Engagement Platform (CEP, SYS-01 to SYS-08), the external services it depends on (SYS-09 to SYS-11), corporate systems (SYS-12), the 14 sub-processors, the engineering services contractor, and the 5 AI uses in P10. Processes and impact values come from the BIA (P05); vulnerabilities come from the gap analysis (P03) and the control assessment (P07).

**Who can accept risk (tolerance).**
| Risk level | Who may accept | Conditions |
|---|---|---|
| Very Low and Low | The risk owner (director level or above) | Recorded in the register; reviewed annually |
| Moderate | Chief Technology Officer | Treatment plan or documented reason; reviewed every 6 months |
| High | Chief Executive Officer | Temporary only (up to 12 months) with a dated treatment plan; reported to the audit committee each quarter |
| Very High | Not acceptable | The CEO may approve a temporary exception of up to 90 days only after notifying the audit committee chair, while treatment is under way |

**Overlap and compensation.** The CTO is the CEP system owner and also accepts Moderate risks for it. To keep that honest, the Director of Security can take any risk directly to the audit committee chair, and the co-sourced internal audit firm reviews the acceptance log each year.

### Risk appetite statements
Approved by the Chief Executive Officer and noted by the audit committee on 2026-09-29.

| Area | Appetite | Statement and measure |
|---|---|---|
| Confidentiality of customer data | **Low** | No risk of bulk or cross-tenant exposure of customer data is accepted above Moderate. Measure: R-001, R-002, and R-003 at Moderate or lower by 2027-03-31 |
| Regulated data (PHI in the healthcare cell) | **Very low** | PHI must stay inside the healthcare cell and sub-processors under BAAs. Any flow outside that boundary is stopped first and analyzed second. Measure: R-004 and R-005 closed by 2026-11-30 |
| Availability of the service | **Low** | Recovery capability must meet the BIA RTOs for all High-criticality processes (P05). Measure: a passed regional failover exercise within 4 hours by 2027-06-30 |
| Truthful statements | **Very low** | Public, contractual, and questionnaire statements must match practice. Measure: 0 known inaccurate statements after 2026-10-15; quarterly statement review |
| Third parties | **Moderate**, with conditions | Sub-processors are essential to the product, but each has a DPA, a current SOC 2 review, and a BAA where it touches healthcare data (P09) |
| Innovation and AI | **Moderate** | The company competes on AI features, but customer-facing AI ships only after the P10 assessment, with evaluation thresholds met and a human handoff path |
| Financial loss from cyber events | **Moderate** | Single-event losses up to the $500,000 insurance retention are tolerable. Scenarios above $2 million need a treatment that reduces likelihood, not only insurance |

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the Information vertical overlay (cloud credential compromise, multi-tenant exposure, supply chain), the FTC's Start with Security cases, the BIA, interviews with every process owner, the gap analysis (P03), and the control assessment (P07).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood of adverse impact were each rated, then combined with **Table G-5**.
3. **Rate impact.** Impact used **Table H-3**, anchored to the BIA impact categories (credits and cost, operations, regulatory and contractual, safety, reputation).
4. **Determine risk.** Risk level came from **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the two tables, not assigned by hand.
5. **Semi-quantitative view.** `semi_quant_score` gives each risk level its SP 800-30 Appendix I semi-quantitative value (Very High 10, High 8, Moderate 5, Low 2, Very Low 0). `exposure_estimate_usd` gives an order-of-magnitude single-event loss range from the BIA values, used for the enterprise risk roll-up (NIST IR 8286 Rev. 1). The ranges are estimates for prioritizing, not actuarial figures.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 8 |
| Moderate | 29 |
| Low | 14 |
| Very Low | 0 |
| **Total** | **52** |

Treatments: 48 Mitigate, 4 Accept (R-030, R-038, R-039, R-051). Status: 29 Open, 19 In progress, 4 Accepted.

Cyber insurance ($15 million limit, $500,000 retention) transfers part of the financial exposure for R-001, R-002, R-006, and R-007. It is not recorded as the treatment for any risk, because it does not lower the likelihood of harm to customers.

### Top risks (Very High and High)
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Leaked long-lived cloud key used to download attachments and query the warehouse | Very High | Replace the 9 keys with federated short-lived credentials; bulk-read alerts; tabletop | VP Platform Engineering | 2026-10-31 |
| R-002 | Data copied without detection, so affected tenants cannot be identified | High | Object-level and database audit logs; MDR on cloud workloads | Director of Security | 2026-12-31 |
| R-003 | Cross-tenant exposure through an authorization flaw or shared search credentials | High | Database row-level security; per-tenant search credentials; cross-tenant tests | VP Engineering | 2027-03-31 |
| R-004 | Healthcare subject lines in the warehouse used or viewed outside the BAA | High | Stop the export; purge; counsel breach assessment | Associate General Counsel, Privacy | 2026-10-31 |
| R-006 | Primary region loss keeps the platform down beyond the 4-hour MTD | High | Warm standby; search snapshots; DR plan; failover exercise | VP Platform Engineering | 2027-06-30 |
| R-007 | Destructive attack deletes production and backups | High | Write-once backup vault with separate administrators; remove standing roles | VP Platform Engineering | 2026-12-31 |
| R-009 | Public and contractual statements shown to be inaccurate | High | Correct 3 statements; quarterly statement review | General Counsel | 2026-10-15 |
| R-013 | Webhook server-side request forgery reaches internal services | High | Egress proxy with private address blocking; retest | VP Engineering | 2026-10-31 |
| R-024 | Identity provider takeover or failure blocks recovery | High | Quarterly break-glass test; 2-person admin changes | Director of IT | 2026-12-31 |

**Themes.**
- **Credentials and data-level visibility (R-001, R-002, R-012, R-025, R-026, R-050).** The company has strong workforce authentication, but machine credentials and data-level logging lag behind. A single leaked key could expose most customers' attachments, and the company could not prove which.
- **Multi-tenancy (R-003, R-008, R-011, R-017, R-034).** One layer of tenant isolation, broad support access on the Standard plan, and data kept after termination.
- **Healthcare cell boundary (R-004, R-005, R-045).** The cell's design is strong; the leaks are a data export and two missing subcontractor BAAs.
- **Recovery (R-006, R-007, R-031, R-042).** Recovery from a region loss or a destructive attack is not proven, and the SLA credit cap is reached at 7.2 hours.
- **Truthfulness (R-009, R-019, R-044).** Three public statements describe controls that do not fully operate, which turns security gaps into deception risk under FTC Act Section 5.
- **AI (R-019 to R-023, R-045, R-046).** The AI features shipped ahead of governance; P10 assesses them.

## 4. Treatment summary
**Funded in the FY2027 security plan (approved by the CEO 2026-09-29, $850,000 one-time and $1.3 million a year):**
- Warm standby DR region and search replication ($250,000 one-time; $380,000 a year)
- MDR extension to cloud workloads, object-level and database audit logging ($260,000 a year)
- Second layer of tenant isolation and cross-tenant test suite ($300,000 one-time, engineering time)
- Workload identity federation, retirement of the 9 long-lived keys, and a write-once backup vault ($120,000 one-time)
- 2 security engineers and 1 GRC analyst ($560,000 a year)
- SOC 2 scope expansion and AI evaluation tooling ($180,000 one-time; $60,000 a year)
- Second email delivery provider ($40,000 a year)

Smaller items (statement corrections, deletion job changes, contract amendments) are funded from operating budgets. Each funded item maps to a P07 POA&M entry.

**Accepted (4):** R-030 (Low, VP Platform Engineering; provider volumetric protection), R-038 (Low, VP Product; AI features are outside the SLA and fail cleanly), R-039 (Low, Director of IT; full-disk encryption), R-051 (Low, Associate General Counsel, Privacy; customers that disable card redaction are contractually responsible).

**Contract actions:** subcontractor BAAs for the SMS provider and the error-tracking SaaS (R-005), zero-retention terms for all AI traffic (R-019), and Data Security Program attestations from the engineering contractor (R-033), all due by 2026-12-31.

## 5. Enterprise and system-level registers
This file is the **enterprise register**. Following NIST IR 8286 Rev. 1, it rolls up to the company's enterprise risk register as one line, "Cybersecurity, privacy, and service resilience", owned by the CTO and reported to the audit committee each quarter with the counts above and the top risks.

System-level registers are filtered views of this file, kept by each system owner, rather than separate spreadsheets. That keeps one set of ratings.

| System-level register | Owner | Risks in scope |
|---|---|---|
| Customer Engagement Platform (CEP; SSP in P02) | Chief Technology Officer, with the Director of Security | 34 risks whose affected assets include SYS-01 to SYS-08 (filter the `affected_asset_or_process` column) |
| Healthcare cell (the HIPAA risk analysis for ePHI held as a business associate) | Director of Security (HIPAA Security Official) | R-002, R-004, R-005, R-006, R-007, R-010, R-018, R-027, R-045 |
| AI portfolio (P10) | VP Product | R-019, R-020, R-021, R-022, R-023, R-045, R-046 |

When a system-level review changes a rating, the owner updates this file, and the change flows to the enterprise roll-up.

## 6. Approval
- Chief Technology Officer: approved Moderate and Low treatments, 2026-09-29.
- Chief Executive Officer: approved the High and Very High treatment plans, the risk appetite statements, and the FY2027 security budget, 2026-09-29.
- Board audit committee: received the results on 2026-09-29. Next report: 2026-12 quarterly meeting.
- Next full risk assessment: July 2027, or sooner after a major change (for example an acquisition, R-048) or a significant incident.
