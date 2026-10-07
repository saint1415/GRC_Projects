# Risk Register Report: Cris Santos Company | Emergency Services | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (licensed private ambulance service; PE-backed) |
| Size tier | Mid-Market (600 employees) |
| Vertical | Emergency Services (CISA sector; NAICS 621910 Ambulance Services) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2, I-3 values); enterprise roll-up per NIST IR 8286 Rev. 1 |
| Also satisfies | HIPAA risk analysis and risk management, 45 CFR 164.308(a)(1)(ii)(A)-(B) (C-EMERGENCY-R04); hazard input to the County A communications center continuity plan |
| Prepared | 2026-07-31 by the Security Manager and the vCISO; R-050 added 2026-08-14 from P07 testing |
| Approved | 2026-09-16: Chief Operating Officer (Moderate and below), Chief Executive Officer (High and Very High); presented to the board audit committee the same day |

## 1. Scope and risk framing
**Scope.** All business units (both communications centers, field operations, clinical services, the revenue cycle, billing services, and enterprise functions), the Dispatch and Patient Care Platform (DPCP; SSP in P02), the billing platform (SYS-03), the 58 vendors with PHI access, and the AI tools (SYS-14). Processes and impact values come from the BIA (P05); vulnerabilities come from the gap analysis (P03) and the control assessment (P07).

**What makes this business different.** A dispatch outage is a patient safety event, not only an IT event. Impact ratings therefore use the BIA safety category first. The company is also a business associate for 4 municipal clients, so a breach at the company or its billing vendor can create notice duties in two directions.

**Who can accept risk (tolerance).**
| Risk level | Who may accept | Conditions |
|---|---|---|
| Very Low and Low | The risk owner (director level or above) | Recorded in the register; reviewed annually |
| Moderate | Chief Operating Officer | Treatment plan or documented reason; reviewed every 6 months |
| High | Chief Executive Officer | Temporary only (up to 12 months) with a dated treatment plan; reported to the audit committee each quarter |
| Very High | Not acceptable | The CEO may approve a temporary exception of up to 90 days only after notifying the audit committee chair, while treatment is under way |

Risks that can delay an emergency response are never accepted above Low without a funded treatment plan.

### Risk appetite statements
Approved by the Chief Executive Officer and noted by the audit committee on 2026-09-16.

| Area | Appetite | Statement and measure |
|---|---|---|
| Emergency response and patient safety | **Very low** | No cyber or technology risk that could delay an emergency response is accepted above Low. Measure: risks of that kind above Low (8 today: R-001, R-003, R-008, R-009, R-010, R-016, R-017, R-050; target 0 by 2027-12-31) |
| Dispatch availability | **Very low** | Recovery capabilities must meet the BIA RTOs for BP-01 to BP-04 (P05). Measure: each High process has a passed recovery test or drill in the last 12 months (0 of 4 today) |
| Confidentiality of PHI | **Low** | No risk of a breach affecting 500 or more patients is accepted above Moderate. Measure: R-002, R-013, and R-041 at Moderate or lower by 2027-06-30 |
| Regulatory and contract compliance | **Low** | No HIPAA Security Rule Required implementation specification may stay Not met or Partially met beyond 2027-06-30. No county agreement default |
| Billing services client trust | **Low** | Client PHI is held to the same standard as company PHI, and client notices are never late. Measure: SOC 2 Type 2 report issued by 2027-11-30 (P09) |
| Third parties | **Moderate**, with conditions | Vendors are used widely, but no vendor receives PHI without a BAA, and every Tier 1 vendor is reassessed each year (P09) |
| Innovation and AI | **Moderate** | The company wants AI benefits in dispatch, documentation, and billing, but only through the AI governance gate in P10. No AI tool may lower a dispatch priority or submit a claim without human review |
| Financial loss from cyber events | **Moderate** | Single-event losses up to the $250,000 insurance retention are tolerable. Scenarios above $2 million need a treatment that reduces likelihood, not only insurance |

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, CISA's Emergency Services Sector context, the BIA, interviews with every process owner, the gap analysis (P03), and the control assessment (P07).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood of adverse impact were each rated, then combined with **Table G-5**.
3. **Rate impact.** Impact used **Table H-3**, anchored to the BIA impact categories (safety, operations, regulatory and contract, cost, reputation).
4. **Determine risk.** Risk level came from **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the two tables, not assigned by hand.
5. **Semi-quantitative view.** `semi_quant_score` gives each risk level its SP 800-30 Appendix I semi-quantitative value (Very High 10, High 8, Moderate 5, Low 2, Very Low 0). `exposure_estimate_usd` gives an order-of-magnitude single-event loss range from the BIA values, used for the enterprise roll-up (NIST IR 8286 Rev. 1). The ranges are estimates for prioritizing, not actuarial figures.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 8 |
| Moderate | 29 |
| Low | 12 |
| Very Low | 0 |
| **Total** | **50** |

Treatments: 45 Mitigate, 4 Accept (R-026, R-027, R-028, R-046), 1 Avoid (R-037). Status: 24 Open, 22 In progress, 4 Accepted.

Cyber insurance ($10 million limit, $250,000 retention) transfers part of the financial exposure for R-001, R-002, and R-013. It is not recorded as the treatment for any risk, because it does not lower the likelihood of harm to patients or operations.

### Top risks (Very High and High)
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware forces manual dispatch at both communications centers | Very High | Console EDR in block mode; monthly console patching; write-once backups for the integration engine and recordings; CAD rebuild test; drill at both centers; warm CAD standby | Director of IT (Security Officer) | 2027-06-30 |
| R-002 | PHI exfiltration for extortion | High | Egress alerting; restricted reporting extracts; CAD and integration engine logs to the SIEM | Security Manager | 2027-01-31 |
| R-003 | CAD rebuild exceeds the 1-hour RTO | High | Rebuild runbook with the CAD vendor; full rebuild test; quarterly restore tests | Director of IT (Security Officer) | 2026-12-31 |
| R-013 | Billing platform vendor breach exposes company and client PHI | High | Annual SOC 2 and CUEC review; vendor breach runbook; client notice templates; shorter notice term | Compliance and Privacy Officer | 2026-12-31 |
| R-015 | AI coding assistance causes Medicare and Medicaid overpayments | High | End straight-through coding; 100% coder review; monthly accuracy audit; look-back review | Director of Revenue Cycle | 2026-10-31 |
| R-016 | AI call triage misses or anchors a time-critical call | High | P10 go-live criteria; English-only advisory mode; monthly under-triage report | Medical Director | 2026-12-31 |
| R-021 | MSSP or CAD vendor remote access as a supply-chain entry point | High | Company-controlled access broker with session approval and recording; annual SOC 2 and CUEC review | vCISO | 2027-03-31 |
| R-022 | Cloud administrator takeover | High | Security keys for administrators; just-in-time elevation | Security Manager | 2027-03-31 |
| R-050 | Station alerting controllers with default passwords reachable from crew Wi-Fi (found in P07) | High | Isolate controllers; vendor access through the broker; password vault | Director of Field Operations | 2026-11-30 |

**Themes.**
- **Dispatch resilience (R-001, R-003, R-008, R-009, R-010, R-050).** The company can detect most attacks (EDR, MSSP, SIEM), and its CAD database backups are isolated. It has not proven it can rebuild CAD, and its second communications center shares the same CAD, so the center protects against hurricanes and fires but not ransomware.
- **Third parties in both directions (R-013, R-014, R-021, R-043, R-047).** The billing platform, the CAD vendor, and the MSSP are single points of failure. The billing services line adds duties the company owes to its clients.
- **AI adopted without governance (R-015 to R-020).** Four tools went live or were switched on without review. The two High risks are clinical (R-016) and financial-regulatory (R-015). P10 addresses all of them.
- **Visibility (R-002, R-036, R-038, R-041).** Logs that would prove what an attacker took are not collected, so a breach might have to be presumed for every patient in CAD.

R-050 was added on 2026-08-14 after the P07 assessors found station alerting controllers reachable from crew Wi-Fi on 2026-08-12, 4 of them with the manufacturer default password. The Director of Field Operations changed those passwords on 2026-08-14. The risk stays open until the controllers are isolated.

## 4. Treatment summary
**Funded in the FY2027 security plan (approved by the CEO 2026-09-16, $1.02 million one-time and $380,000 a year):**
- Warm CAD standby in the backup region and CAD rebuild testing ($260,000 one-time, $60,000 a year)
- Station network segmentation at 9 stations and central management for all vehicle routers ($210,000)
- Named MDC sign-in with MFA ($90,000)
- Vendor access broker with session recording and administrator security keys ($110,000 one-time, $45,000 a year)
- SIEM onboarding of CAD, integration engine, and ePCR audit logs, plus egress alerting ($95,000 a year through the MSSP)
- ePCR access analytics ($40,000 a year)
- SOC 2 readiness and Type 2 examination for billing services ($240,000 across 2027)
- AI coding look-back review and accuracy monitoring ($110,000 one-time)
- One GRC analyst position for vendor risk and evidence collection ($140,000 a year, already filled in 2026; counted in the yearly figure)

Smaller items (station closet locks, reporting cards, exercise facilitation, BAA work) are funded from the operating budget. Each funded item maps to a P07 POA&M entry.

**Accepted (4):** R-026 (Low; crews phone ECG findings), R-027 (Low; encrypted devices), R-028 (Low; vendor call filtering), R-046 (Low; radio and offline tablets).

**Avoided (1):** R-037. The company will not accept criminal justice information from County A unless a CJIS compliance program, an agreement, and a security addendum are in place first.

**Contract actions:** AI triage BAA amendment (R-019) by 2026-10-31; BAAs for 6 vendors (R-043) by 2026-12-31; billing vendor breach notice term and client workspace review (R-013, R-014) at the 2027 renewal; interconnection security terms with both counties (R-010, R-011) by 2027-03-31.

## 5. Enterprise and system-level registers
This file is the **enterprise register**. Following NIST IR 8286 Rev. 1, it rolls up to the company's enterprise risk register as one line, "Cybersecurity and dispatch resilience", owned by the COO and reported to the audit committee each quarter with the counts above and the top risks.

System-level registers are filtered views of this file, kept by each system owner, rather than separate spreadsheets. That keeps one set of ratings.

| System-level register | Owner | Risks in scope |
|---|---|---|
| Dispatch and Patient Care Platform (DPCP; SSP in P02) | Director of IT (Security Officer) | 34 risks whose affected assets include SYS-01, SYS-02, SYS-04, or SYS-06 to SYS-12 (filter the `affected_asset_or_process` column) |
| Billing platform and billing services (P09 scope) | Director of Revenue Cycle | R-012, R-013, R-014, R-015, R-044, R-047 |
| AI portfolio (P10) | Medical Director with the vCISO | R-015, R-016, R-017, R-018, R-019, R-020 |
| Communications center continuity (County A plan input) | Director of Communications | R-001, R-003, R-008, R-009, R-010, R-042, R-050 |

When a system-level review changes a rating, the owner updates this file, and the change flows to the enterprise roll-up.

## 6. Approval
- Chief Operating Officer: approved Moderate and Low treatments and the 4 acceptances, 2026-09-16.
- Chief Executive Officer: approved the High and Very High treatment plans, the risk appetite statements, the avoidance of R-037, and the FY2027 security budget, 2026-09-16.
- Board audit committee: received the results on 2026-09-16. Next report: December 2026 quarterly meeting.
- Next full risk analysis: July 2027, or sooner after a major change (for example the warm CAD standby, accepting County A data feeds, or expanding AI-001) or a significant incident.
