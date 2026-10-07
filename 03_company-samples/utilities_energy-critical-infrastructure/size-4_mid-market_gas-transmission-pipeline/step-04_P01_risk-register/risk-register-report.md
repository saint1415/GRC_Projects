# Risk Register Report: Cris Santos Company | Energy | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed interstate natural gas transmission pipeline operator) |
| Size tier | Mid-Market (600 employees) |
| Vertical | Energy (CISA critical infrastructure sector) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2, I-3 values), with OT threat sources and predisposing conditions from NIST SP 800-82 Rev. 3 Appendix C; enterprise roll-up per NIST IR 8286 Rev. 1 |
| Also satisfies | The annual risk view behind the TSA Cybersecurity Implementation Plan and Cybersecurity Assessment Plan (SD Pipeline-2021-02G Sections II.B and III.G); input to the SD 01G Section II.D vulnerability assessment remediation tracking |
| Prepared | 2026-07-31 by the GRC lead and the vCISO with the Director of Gas Control and the SCADA and OT Engineering Manager; R-003 and R-040 added 2026-08-14 from P07 testing |
| Approved | 2026-09-17: Chief Operating Officer (Moderate and below), Chief Executive Officer (High and Very High, and the risk appetite); presented to the board audit committee the same day |

## 1. Scope and risk framing
**Scope.** All business units, the Pipeline SCADA and Gas Control System (PSGCS, SYS-01 to SYS-07, the SSP system in P02), business IT, the 5-account cloud landing zone (P04), the SaaS services, the two laterals operated under OSAs, and the 85 third parties with access (`../00_company-facts.md` section 3). Processes and impact values come from the BIA (P05); vulnerabilities come from the gap analysis (P03) and the control assessment (P07).

**What makes this register different from an office business.** The worst outcomes are physical: overpressure, an undetected release, or loss of gas supply to about 1.3 million homes and businesses and 7 power plants. Cyber risks are rated on those consequences, and a precautionary shutdown is treated as a harm in its own right, not as a safe default (P05 section 4).

**Who can accept risk (tolerance).**
| Risk level | Who may accept | Conditions |
|---|---|---|
| Very Low and Low | The risk owner (director level or above) | Recorded in the register; reviewed annually |
| Moderate | Chief Operating Officer | Treatment plan or documented reason; reviewed every 6 months |
| High | Chief Executive Officer | Temporary only (up to 12 months) with a dated treatment plan; reported to the audit committee each quarter |
| Very High | Not acceptable | The CEO may approve a temporary exception of up to 90 days only after notifying the audit committee chair, while treatment is under way |

A risk that could cause loss of pipeline control or public harm may not be accepted above Moderate.

### Risk appetite statements
Approved by the Chief Executive Officer and noted by the audit committee on 2026-09-17.

| Area | Appetite | Statement and measure |
|---|---|---|
| Public safety and pipeline control | **Very low** | No cyber risk that could plausibly cause loss of pipeline control or public harm is accepted above Moderate. Each such risk rated High or Very High must have a funded treatment plan within 90 days. Measure: number of High or Very High risks with a safety or control consequence (7 today: R-001 to R-005, R-010, R-011; target 0 by 2027-12-31) |
| Reliability of firm service | **Low** | Recovery capabilities must meet the BIA RTOs for all High-criticality processes (P05). No precautionary shutdown without the P08 criteria. Measure: every High process has a passed recovery or failover test in the last 12 months (BCC failover yes; full SCADA rebuild no) |
| Regulatory compliance (TSA, PHMSA, FERC) | **Low** | Every measure in the TSA-approved Cybersecurity Implementation Plan is implemented on its schedule or covered by a mitigation TSA has been told about. Permanent changes are filed as amendments within 50 days. No repeat PHMSA finding under 192.631 |
| Confidentiality of SSI and CEII | **Low** | SSI is stored and shared only as 49 CFR Part 1520 requires. Measure: zero unmarked SSI copies in quarterly scans |
| Third parties | **Moderate**, with conditions | Vendors are used widely, but no vendor gets OT access except through the remote access gateway, and every Tier 1 vendor is reassessed each year (P09) |
| Innovation and AI | **Moderate** | The company wants the benefits of AI in leak detection, maintenance, and patrols, but only through the AI governance process in P10. No AI may act on OT without a new assessment |
| Financial loss from cyber events | **Moderate** | Single-event losses up to the $500,000 insurance retention are tolerable. Scenarios above $3 million need a treatment that reduces likelihood, not only insurance |

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, SP 800-82 Rev. 3 Appendix C (OT threats and vulnerabilities), CISA and TSA advisories, the BIA, interviews with every process owner, the gap analysis (P03), and the control assessment (P07).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood of adverse impact were each rated, then combined with **Table G-5**.
3. **Rate impact.** Impact used **Table H-3**, anchored to the BIA impact categories (cost, operations, regulatory, public safety, reputation). Safety and supply impacts set the rating when they are the worst case.
4. **Determine risk.** Risk level came from **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the two tables, not assigned by hand.
5. **Semi-quantitative view.** `semi_quant_score` gives each risk level its SP 800-30 Appendix I semi-quantitative value (Very High 10, High 8, Moderate 5, Low 2, Very Low 0). `exposure_estimate_usd` gives an order-of-magnitude single-event loss range from the BIA values, used for the enterprise roll-up (NIST IR 8286 Rev. 1). The ranges are estimates for prioritizing, not actuarial figures.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 6 |
| Moderate | 28 |
| Low | 16 |
| Very Low | 0 |
| **Total** | **51** |

Treatments: 46 Mitigate, 4 Accept (R-024, R-042, R-044, R-045), 1 Avoid (R-050). Status: 19 Open, 28 In progress, 4 Accepted.

Cyber insurance ($20 million limit, $500,000 retention) transfers part of the financial exposure for R-001, R-004, and R-037. It is not recorded as the treatment for any risk, because it does not lower the likelihood of harm to the public or to firm service.

### Top risks (Very High and High)
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-003 | Attacker reaches a compressor unit control panel through the OEM's undocumented cellular modem (found in P07) | Very High | Modem disconnected 2026-08-13 (temporary); survey all units; route OEM data through the DMZ; OEM contract terms | SCADA and OT Engineering Manager | 2026-10-31 |
| R-001 | Ransomware on business IT leads to a precautionary pipeline shutdown | High | P08 operate-or-shut-down criteria in the TSA incident response plan; live isolation drill; OT monitoring at all stations | Security Manager | 2027-03-31 |
| R-002 | Stolen staff or vendor credentials used on the remote access gateway | High | Fewer OT administrators; phishing-resistant authenticators for all gateway users | SCADA and OT Engineering Manager | 2027-01-31 |
| R-004 | SCADA at both control centers lost; full rebuild untested | High | Annual bare-metal rebuild test; separate BCC administrative credentials | SCADA and OT Engineering Manager | 2026-12-31 |
| R-005 | Nation-state pre-positioning at unmonitored stations or field sites | High | Sensors at the 3 remaining stations; telecom baseline; 12-month OT log retention | Security Manager | 2027-03-31 |
| R-010 | Wrong or late shutdown decision | High | P08 decision tree; executive tabletop with the board chair | Chief Operating Officer | 2026-12-31 |
| R-011 | False data or commands mislead controllers | High | Command anomaly detection at all stations; microwave encryption; field verification step | Security Manager | 2027-09-30 |

**Themes.**
- **The control centers are strong; the edges are not (R-003, R-005 to R-009, R-031, R-038).** Segmentation, the remote access gateway, the hot-standby BCC, and monitoring at the core are in place. The gaps sit at 3 of 5 compressor stations, in the field, and with the OEM.
- **The shutdown decision is the biggest business risk (R-001, R-010).** The BIA shows the company can run the pipeline without business IT. The risk is that leaders shut it down anyway, as happened elsewhere in the industry, because they cannot prove OT is clean.
- **TSA compliance hygiene (R-029, R-030, R-046).** The plans exist and are approved, but amendments, the assessment schedule, and SSI handling have slipped.
- **Third parties (R-012, R-013, R-019, R-020, R-023, R-048).** The SCADA vendor, the customer activities website vendor, and the OEM are critical and largely unassessed.
- **AI is advisory today (R-025 to R-028).** The controls in P10 keep it that way.

## 4. Treatment summary
**Funded in the FY2027 security plan (approved by the CEO 2026-09-17, $1.6 million one-time and $380,000 a year):**
- OT monitoring sensors at Compressor Stations 2, 4, and 5 and a field telecommunications baseline ($240,000 one-time, $60,000 a year through the MSSP)
- Replacement of the 14 unsupported station HMIs with individual logins and allowlisting ($520,000)
- Spare SCADA servers for rebuild tests and offline media at the BCC ($90,000)
- Phishing-resistant authenticators for all gateway users ($40,000)
- Microwave backbone encryption at the 2027 refresh ($380,000)
- Second-carrier cellular service at the 15 largest delivery points ($35,000 a year)
- Third OT security engineer ($165,000 a year)
- OT log archive and SSI data loss rule ($30,000 a year)
- SOC 2 readiness and Type 2 examination for the contract operations services ($180,000 across 2027)
- Vendor risk reviews and contract amendments ($150,000 one-time, $90,000 a year for the GRC analyst time and tooling)

Smaller items (tamper alarms, change tool configuration, training modules) come from the operating budget. Each funded item maps to a P07 POA&M entry.

**Accepted (4):** R-024 (Low, SCADA and OT Engineering Manager), R-042 (Low, IT Director), R-044 (Low, SCADA and OT Engineering Manager), R-045 (Low, IT Director). **Avoided (1):** R-050, by the POL-03 rule that no ransom is paid without an OFAC check and the required approvals.

**Contract actions:** OEM security terms and data path (R-003), SCADA vendor assessment (R-012, R-048), customer activities website vendor SOC 2 and breach notice (R-019, R-020), and the security addendum for the remaining vendors (R-023), due by 2027-06-30.

**TSA actions:** file the 2 Cybersecurity Implementation Plan amendment requests by 2026-10-31 and the annual Cybersecurity Assessment Plan update and report by 2026-11-20 (R-030).

## 5. Enterprise and system-level registers
This file is the **enterprise register**. Following NIST IR 8286 Rev. 1, it rolls up to the company's enterprise risk register as one line, "Cybersecurity and OT resilience", owned by the COO and reported to the audit committee each quarter with the counts above and the top risks.

System-level registers are filtered views of this file, kept by each owner, rather than separate spreadsheets. That keeps one set of ratings.

| System-level register | Owner | Risks in scope |
|---|---|---|
| PSGCS (SSP in P02) | SCADA and OT Engineering Manager | 28 risks whose affected assets include SYS-01 to SYS-07 (filter the `affected_asset_or_process` column) |
| Contract operations (OSA laterals, P09 scope) | Director of Gas Control | R-001, R-004, R-010, R-041 |
| TSA plan view (Critical Cyber Systems) | Security Manager | Every risk whose `regulatory_driver` cites C-ENERGY-R02 or C-ENERGY-R03 |
| AI portfolio (P10) | Director of Gas Control | R-025, R-026, R-027, R-028 |

When a system-level review changes a rating, the owner updates this file, and the change flows to the enterprise roll-up.

## 6. Approval
- Chief Operating Officer: approved Moderate and Low treatments and the 4 acceptances, 2026-09-17.
- Chief Executive Officer: approved the High and Very High treatment plans, the risk appetite statements, and the FY2027 security budget, 2026-09-17.
- Board audit committee: received the results on 2026-09-17. Next report: the December 2026 quarterly meeting.
- Next full risk assessment: July 2027, or sooner after a major change (new compressor station, SCADA upgrade, acquisition), a TSA directive revision, or a significant incident.
