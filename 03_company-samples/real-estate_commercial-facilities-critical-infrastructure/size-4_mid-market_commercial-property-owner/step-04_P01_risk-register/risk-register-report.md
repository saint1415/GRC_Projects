# Risk Register Report: Cris Santos Company | Commercial Facilities | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed commercial office and retail property owner-operator) |
| Size tier | Mid-Market (600 employees) |
| Vertical | Commercial Facilities |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2, I-3 values); enterprise roll-up per NIST IR 8286 Rev. 1 |
| Also supports | CISA CPG 2.0 goals 1.B (oversight) and 2.B (track vulnerabilities in a risk register); the "reasonable measures" duty in Fla. Stat. 501.171(2) |
| Prepared | 2026-07-31 by the GRC Analyst and the vCISO; R-050 added 2026-08-14 from P07 testing |
| Approved | 2026-09-15: Chief Operating Officer (Moderate and below), Chief Executive Officer (High and Very High); presented to the board audit committee the same day |

## 1. Scope and risk framing
**Scope.** All business units (office, retail, and mixed-use portfolios; security operations and the SCC; engineering; parking; corporate functions), the Building Automation and Access Control System (BAACS, P02), the corporate SaaS and cloud landing zone (P04), the 41 vendors with system access or data (SYS-15), and the 5 AI use cases (SYS-16). Processes and impact values come from the BIA (P05); vulnerabilities come from the gap analysis (P03) and the control assessment (P07).

**Who can accept risk (tolerance).**
| Risk level | Who may accept | Conditions |
|---|---|---|
| Very Low and Low | The risk owner (director level or above) | Recorded in the register; reviewed annually |
| Moderate | Chief Operating Officer | Treatment plan or documented reason; reviewed every 6 months |
| High | Chief Executive Officer | Temporary only (up to 12 months) with a dated treatment plan; reported to the audit committee each quarter |
| Very High | Not acceptable | The CEO may approve a temporary exception of up to 90 days only after notifying the audit committee chair, while treatment is under way |

### Risk appetite statements
Approved by the Chief Executive Officer and noted by the audit committee on 2026-09-15.

| Area | Appetite | Statement and measure |
|---|---|---|
| Occupant and life safety | **Very low** | No cyber or technology risk that could plausibly harm occupants is accepted above Low, and no change may connect the BAACS to a life-safety system. Measure: safety-linked risks above Low (5 today: R-001, R-011, R-025, R-032, R-047; target 0 by 2027-12-31) |
| Building operations availability | **Low** | Recovery capabilities must meet the BIA RTOs for every High-criticality process (P05). Measure: every High process has a passed recovery test or drill in the last 12 months (0 of 4 today) |
| Personal information of tenants, visitors, and employees | **Low** | The company will not accept a risk of a breach affecting 500 or more Florida residents above Moderate. Measure: R-005 and R-016 at Moderate or lower by 2027-06-30 |
| Regulatory and contractual commitments | **Low** | Florida notice duties, lease notice clauses, PCI DSS validation, and the JV SOC 2 commitment are met on time. Measure: no missed notice or reporting deadline; SAQ P2PE signed without open eligibility gaps |
| Third parties | **Moderate**, with conditions | Integrators and platform vendors are essential, but no vendor gets standing remote access to OT, and every Tier 1 vendor is reviewed each year (P09) |
| Innovation and AI | **Moderate** | The company wants the benefits of analytics and automation, but only through the AI review process (P10). No AI feature that affects entry to a building or writes to building systems runs without review |
| Financial loss from cyber events | **Moderate** | Single-event losses up to the $250,000 insurance retention are tolerable. Scenarios above $2 million need a treatment that reduces likelihood, not only insurance |

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the Commercial Facilities overlay and the CPG 2.0 "risk addressed" statements, SP 800-82 Rev. 3 OT threat guidance, the BIA, interviews with every process owner and all 14 chief engineers, the gap analysis (P03), the control assessment (P07), and the MSSP external scan of 2026-07-21.
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood of adverse impact were each rated, then combined with **Table G-5**.
3. **Rate impact.** Impact used **Table H-3**, anchored to the BIA impact categories (cost, operations, regulatory and contractual, occupant safety, reputation).
4. **Determine risk.** Risk level came from **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the two tables, not assigned by hand.
5. **Semi-quantitative view.** `semi_quant_score` gives each risk level its SP 800-30 Appendix I semi-quantitative value (Very High 10, High 8, Moderate 5, Low 2, Very Low 0). `exposure_estimate_usd` gives an order-of-magnitude single-event loss range from the BIA values, used for the enterprise risk roll-up (NIST IR 8286 Rev. 1). The ranges are estimates for prioritizing, not actuarial figures.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 9 |
| Moderate | 31 |
| Low | 9 |
| Very Low | 0 |
| **Total** | **50** |

Treatments: 46 Mitigate, 3 Accept (R-033, R-035, R-043), 1 Avoid (R-012). Status: 29 Open, 17 In progress, 3 Accepted, 1 Closed (R-048, closed by the POL-03 ransom decision rule approved 2026-09-15).

Cyber insurance ($10 million limit, $250,000 retention) transfers part of the financial exposure for R-001, R-005, and R-016. It is not recorded as the treatment for any risk, because it does not lower the likelihood of harm to occupants or operations.

### Top risks (Very High and High)
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware on BAS servers spreads across flat property networks | Very High | Integrator B to the gateway; OT zones at 10 properties; Platform B backups; restore tests; OT tabletop | IT Director | 2027-06-30 |
| R-002 | Compromise of BAS Integrator B or its always-on tool | High | Remove the tool; gateway access with MFA and approval; security addendum | Building Technology Manager | 2026-11-30 |
| R-004 | Platform B server lost with no backup | High | Nightly images; controller program exports; restore tests | IT Director | 2027-03-31 |
| R-005 | Cloud access control platform compromise exposes 14,500 credential holders | High | Vendor review; platform audit events to the SIEM; access platform runbook | Director of Security Operations | 2027-03-31 |
| R-008 | Internet-exposed NVRs and Park 2 BAS web interface | High | Remove remaining forwarding; monthly external scans | IT Director | 2026-10-15 |
| R-012 | Face verification pilot keeps templates without notice or limits | High | **Avoid:** suspend and delete unless P10 conditions are met | Vice President of Property Management | 2026-10-31 |
| R-016 | Breach of the visitor ID archive (about 610,000 records) | High | Purge to 30 days; keep minimal fields; breach notice terms | Director of Security Operations | 2026-12-31 |
| R-029 | Attacks on OT or the platform go undetected | High | OT and platform logs to the SIEM; passive OT monitoring | Security Manager | 2027-03-31 |
| R-047 | Integrator links a life-safety system to the BAS network | High | Contract design rule; annual walkdown; change review | Vice President of Engineering | 2027-03-31 |
| R-050 | Tower 1 any-any rule to the Platform A server (found in P07) | High | Remove the rule; quarterly rule review | IT Director | 2026-09-30 |

**Themes.**
- **Two portfolios, two security levels (R-001, R-002, R-004, R-008, R-009, R-010, R-050).** The 2025 tower project gave Towers 1-4 OT zones, a remote access gateway, and backups. The 8 Platform B properties have none of these, and they are reachable from the same SD-WAN.
- **Seeing and proving (R-028, R-029, R-041).** The company cannot see 45% of its OT devices or any OT activity, and it cannot prove whether tenant data was accessed. That raises both the chance of a long intrusion and the cost of notice.
- **Personal information held longer than needed (R-016, R-012, R-014).** The largest breach exposure is not the BAS. It is 610,000 visitor ID scans and a face template store that nobody decided to keep.
- **Vendors with deep access (R-002, R-005, R-011, R-023, R-024, R-037).** Integrators, the platform vendor, the energy optimization vendor, and the MSSP all have privileged paths into building systems.

## 4. Treatment summary
**Funded in the FY2027 security plan (approved by the CEO 2026-09-15, $1.32 million one-time and $465,000 a year):**
- OT segmentation at Mixed-Use 1-2, Parks 1-2, and Retail 1-6, and passive OT discovery ($420,000 one-time)
- Platform B server and software upgrade ($380,000, 2027 capital plan)
- Integrator B gateway onboarding and default credential cleanup ($45,000)
- OT log collection and monitoring service through the MSSP ($150,000 a year)
- Backup expansion and quarterly restore testing ($60,000 one-time, $25,000 a year)
- Vendor risk program and Tier 1 reviews, with part of the GRC Analyst's time ($90,000 a year)
- SOC 2 readiness and Type 2 examination for the JV ($240,000 across 2027)
- Phishing-resistant MFA for finance and property management staff ($55,000 one-time, $20,000 a year)
- Cellular backup at the 8 single-ISP properties and SCC failover drills ($120,000 one-time, $30,000 a year)
- OT security training for engineering and SCC staff ($150,000 a year including backfill)

Smaller items (contract addenda, retention changes, inspection checklists) are funded from the operating budget. Each funded item maps to a P07 POA&M entry.

**Accepted (3):** R-033 (Low, IT Director; guardrails prevent public storage), R-035 (Low, IT Director; backups are isolated and write-once), R-043 (Low, IT Director; vendor DDoS protection). **Avoided (1):** R-012, by suspending the face verification pilot unless the P10 conditions are met.

**Contract actions:** security addenda for Integrator B, the guard contractor, the parking operator, and the visitor management vendor (R-002, R-014, R-016, R-022, R-023), due 2027-03-31; recovery and 24-hour notice terms with the access control and video platform vendor at its 2027 renewal (R-005, R-006).

## 5. Enterprise and system-level registers
This file is the **enterprise register**. Following NIST IR 8286 Rev. 1, it rolls up to the company's enterprise risk register as one line, "Cybersecurity and building technology resilience", owned by the COO and reported to the audit committee each quarter with the counts above and the top risks.

System-level registers are filtered views of this file, kept by each system owner, rather than separate spreadsheets. That keeps one set of ratings.

| System-level register | Owner | Risks in scope |
|---|---|---|
| BAACS (SSP in P02) | Chief Operating Officer, maintained by the GRC Analyst | 28 risks whose affected assets include SYS-01 to SYS-04 or the SCC (filter the `affected_asset_or_process` column) |
| Platform B properties (Parks 1-2, Retail 1-6) | Vice President of Engineering | R-001, R-002, R-004, R-008, R-009, R-010, R-026, R-046 |
| Personal information and notice | General Counsel | R-005, R-012, R-014, R-016, R-023, R-031, R-041 |
| AI portfolio (P10) | vCISO (AI review group chair) | R-011, R-012, R-013, R-014, R-015 |

When a system-level review changes a rating, the owner updates this file, and the change flows to the enterprise roll-up.

## 6. Approval
- Chief Operating Officer: approved Moderate and Low treatments and the acceptance of R-033, R-035, and R-043 (Low risks, accepted by the risk owner and noted by the COO), 2026-09-15.
- Chief Executive Officer: approved the High and Very High treatment plans, the risk appetite statements, and the FY2027 security budget, 2026-09-15.
- Board audit committee: received the results on 2026-09-15. Next report: 2026-12 quarterly meeting.
- Next full risk assessment: July 2027, or sooner after a major change (for example the 2027 acquisitions, R-045) or a significant incident.
