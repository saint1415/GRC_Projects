# Risk Register Report: Cris Santos Company | Agriculture, Forestry, Fishing and Hunting | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed diversified precision-agriculture crop farm with a central packinghouse and a Grower Services unit) |
| Size tier | Mid-Market (600 employees at peak) |
| Vertical | Agriculture, Forestry, Fishing and Hunting |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2, I-3 values); enterprise roll-up per NIST IR 8286 Rev. 1; OT threat sources and conditions from SP 800-82 Rev. 3 Appendix C |
| Also supports | CSF 2.0 ID.RA and GV.RM outcomes (benchmark, P03); the risk analysis retail customers expect behind the food defense plan |
| Prepared | 2026-07-31 by the Security Manager and the vCISO; R-050 added 2026-08-14 from P07 testing |
| Approved | 2026-09-15: Chief Operating Officer (Moderate and below), Chief Executive Officer (High and Very High); presented to the board audit committee the same day |

## 1. Scope and risk framing
**Scope.** All business units (three farms, irrigation and water resources, the packinghouse, food safety, sales, Grower Services, HR, finance, and corporate IT), the Farm Management and Irrigation Control Platform (FMICP; P02), the systems around it (SYS-08 to SYS-13), about 110 vendors, and the AI portfolio (P10), as listed in the intake [asset inventory](../step-00_P00_intake/asset-inventory.csv) and [vendor register](../step-00_P00_intake/vendor-register.csv). Processes and impact values come from the BIA (P05); vulnerabilities come from the intake evidence, the gap analysis (P03) and the control assessment (P07).

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
| Food safety and worker safety | **Very low** | No cyber or technology risk that could plausibly send unsafe produce to customers or expose workers to chemicals is accepted above Low. Any such risk rated Moderate or higher must have a funded treatment plan within 90 days. Measure: safety-linked risks above Low (4 today: R-002, R-006, R-022, R-050; target 0 by 2027-12-31) |
| Crop protection and availability of irrigation and packing | **Low** | Recovery capabilities must meet the BIA RTOs for all High-criticality processes (P05), and freeze protection must have a tested manual fallback before each freeze season. Measure: every High process has a passed recovery or manual-operation test in the last 12 months |
| Integrity of grower settlements | **Very low** | No settlement may be paid from logic or data that was not independently reviewed. Measure: settlement errors over $1,000 per grower per week (target 0); 100% of settlement code changes approved by the company |
| Confidentiality of worker and grower data | **Low** | The company will not accept a risk of a breach of workers' government identifiers, bank accounts, or biometric data above Moderate. Measure: R-003 and R-035 at Moderate or lower by 2027-06-30 |
| Regulatory records | **Low** | Produce Safety, pesticide application, and H-2A records must be producible within 24 hours from a company-held copy. Measure: quarterly retrieval drill passed |
| Third parties | **Moderate**, with conditions | Vendors are essential (FMIS, pivots, integrator, developers), but no vendor gets standing access to OT, and every Tier 1 vendor is reassessed each year (P09) |
| Innovation and AI | **Moderate** | The company wants the benefits of precision agriculture and AI, but only through the AI governance process in P10. No AI may act on irrigation, spraying, or settlements without the controls P10 sets |
| Financial loss from cyber events | **Moderate** | Single-event losses up to the $250,000 insurance retention are tolerable. Scenarios above $2 million need a treatment that reduces likelihood, not only insurance |

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, SP 800-82 Rev. 3 Appendix C (OT threat sources, vulnerabilities, and incidents), the BIA, the intake evidence, and risk interviews and a threat workshop with the process owners, the IT Director, the Security Manager and the MSSP service lead (EV-067). The gap analysis (P03) ran in the same fieldwork window, and the two shared findings. The control assessment (P07) added one risk in a second pass.
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood of adverse impact were each rated, then combined with **Table G-5**. Each rating rests on evidence named in the `likelihood_basis` column: the incident queue (EV-028), scan results (EV-017), phishing results (EV-037), configuration exports, the walk-throughs and interviews. A rating with no evidence behind it would be a guess, so none was made.
3. **Rate impact.** Impact used **Table H-3**, anchored to the BIA impact categories (cost, operations, regulatory, safety, reputation).
4. **Determine risk.** Risk level came from **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the two tables, not assigned by hand.
5. **Semi-quantitative view.** `semi_quant_score` gives each risk level its SP 800-30 Appendix I semi-quantitative value (Very High 10, High 8, Moderate 5, Low 2, Very Low 0). `exposure_estimate_usd` gives an order-of-magnitude single-event loss range from the BIA values, used for the enterprise risk roll-up (NIST IR 8286 Rev. 1). The ranges are estimates for prioritizing, not actuarial figures.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 9 |
| Moderate | 29 |
| Low | 11 |
| Very Low | 0 |
| **Total** | **50** |

Treatments: 46 Mitigate, 4 Accept (R-036, R-043, R-046, R-047). Status: 29 Open, 17 In progress, 4 Accepted.

Cyber insurance ($10 million limit, $250,000 retention) transfers part of the financial exposure for R-001 and R-003. It is not recorded as the treatment for any risk, because it does not lower the likelihood of harm to crops, food safety, or workers.

### Top risks (Very High and High)
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware halts irrigation automation, packing, shipping, and settlements at harvest | Very High | Broker vendor access; offline SCADA and PLC backups; OT segmentation; restore tests; tabletop | Security Manager | 2027-03-31 |
| R-002 | SCADA integrator's shared remote account used to change pump or fertigation settings | High | Remove the remote tool; brokered, recorded vendor sessions with MFA; contract terms | Director of Irrigation and Water Resources | 2026-12-31 |
| R-003 | Theft of worker and grower data for extortion | High | Restrict the personnel share; purge exports; egress alerts; data inventory | HR Director | 2027-01-31 |
| R-004 | Freeze protection fails to start on a freeze night | High | Standalone alarm; written and tested manual start; roster | Farm Manager (Farm 2) | 2026-11-30 |
| R-007 | SCADA and PLC programs cannot be rebuilt in time | High | Offline versioned backups; rebuild procedure tested with the integrator | Director of Irrigation and Water Resources | 2026-12-31 |
| R-009 | Privileged account takeover outside the cloud | High | Privileged access management for directory, SYS-01, ERP, SCADA; phishing-resistant MFA | Security Manager | 2027-03-31 |
| R-015 | Shared crew logins make tally and harvest records unattributable | High | Named crew accounts with tablet PINs; weekly tally edit review | Farm Managers (3) | 2026-11-15 |
| R-021 | OT intrusions and setpoint changes go undetected | High | Passive OT monitoring into the SIEM; change alerts | Security Manager | 2027-03-31 |
| R-023 | Hurricane causes multi-day loss of power and connectivity | High | Hurricane plan with cyber recovery steps; backup links; alternate SCADA operation | Chief Operating Officer | 2027-05-31 |
| R-050 | Default credentials on packinghouse ripening and refrigeration controllers (found in P07) | High | Change credentials; remove the broad firewall rule; contractor jump host | Packinghouse Manager | 2026-10-15 |

**Two passes.** Pass 1 was completed on 2026-07-31 from intake and fieldwork evidence. Pass 2 followed the control assessment (P07): R-050 was added on 2026-08-14 after testing found default administrator credentials on the ripening room and cold storage refrigeration controllers, reachable from the packinghouse office VLAN (EV-IA-5, EV-SC-7). The `assessment_pass` column shows which pass produced each risk.

**Themes.**
- **OT access and recovery (R-001, R-002, R-005, R-007, R-018, R-019, R-021, R-050).** IT is reasonably protected and monitored. OT is reachable by vendors with shared accounts, partly flat, unmonitored, and not recoverable from company-held copies.
- **Weather sets the clock (R-004, R-022, R-023, R-042).** The shortest MTDs are biological (frost, heat, cold chain), so manual fallbacks matter as much as cyber controls.
- **Grower Services integrity (R-010, R-011, R-012, R-031, R-045).** The company is now a service provider. Its own code, graders, and payment process carry processing-integrity risk that growers and lenders will test through SOC 2 (P09).
- **Records and workers (R-015, R-024, R-025, R-035).** Regulated records depend on one SaaS copy and on shared crew logins.
- **AI adopted without governance (R-028 to R-033).** Five tools went live without review. P10 addresses them.

## 4. Treatment summary
**Funded in the FY2027 security plan (approved by the CEO 2026-09-15, $1.25 million one-time and $460,000 a year):**
- OT segmentation at Farms 1 and 2 and passive OT discovery and monitoring at headquarters, the packinghouse, and Farms 1 and 2 ($420,000 one-time; $85,000 a year)
- Privileged and vendor access brokering for directory, SYS-01, ERP, and SCADA, with phishing-resistant MFA for administrators ($170,000 one-time; $80,000 a year)
- Offline OT backup appliance, PLC program management, and recovery testing with the integrator ($110,000 one-time; $40,000 a year)
- Freeze alarm second path, cellular backup links, and IOC alternate operation ($90,000)
- Secure development pipeline and settlement regression testing for the grower portal ($120,000 one-time; $60,000 a year)
- Vendor risk program tooling and one GRC analyst position ($135,000 a year)
- SOC 2 readiness and Type 2 examination for Grower Services ($240,000 across 2027)
- Replacement of the 2 unsupported HMIs (2027 capital plan, $100,000)

Smaller items (pump-station locks, crew tablet PINs, alarm tests, exercise facilitation, contract changes) are funded from the operating budget. Each funded item maps to a P07 POA&M entry.

**Accepted (4):** R-036 (Low, Director of Sales; P2PE keeps card data off company systems), R-043 (Low, Director of Irrigation and Water Resources; spares on hand), R-046 (Low, Precision Agriculture Manager; dealer support), R-047 (Low, Precision Agriculture Manager; with P10 conditions).

**Contract actions:** security terms for the SCADA integrator, pivot manufacturer, refrigeration contractor, and development firm (R-002, R-014, R-045, R-050), due 2026-12-31; data-use terms with the agronomy analytics vendor (R-028); FMIS recovery terms at the 2027 renewal (R-013).

## 5. Enterprise and system-level registers
This file is the **enterprise register**. Following NIST IR 8286 Rev. 1, it rolls up to the company's enterprise risk register as one line, "Cybersecurity, OT, and technology resilience", owned by the COO and reported to the audit committee each quarter with the counts above and the top risks.

System-level registers are filtered views of this file, kept by each system owner, rather than separate spreadsheets. That keeps one set of ratings.

| System-level register | Owner | Risks in scope |
|---|---|---|
| FMICP (SSP in P02) | Chief Operating Officer, with the Security Manager | Risks whose affected assets include SYS-01, SYS-04 to SYS-07, SYS-12, or SYS-14 (filter the `affected_asset_or_process` column) |
| Irrigation and freeze protection OT | Director of Irrigation and Water Resources | R-002, R-004, R-005, R-006, R-007, R-014, R-018, R-019, R-020, R-021, R-030, R-042, R-043, R-048 |
| Packinghouse OT | Packinghouse Manager | R-006, R-022, R-031, R-050 |
| Grower Services (SOC 2 scope, P09) | Vice President of Grower Services | R-008, R-010, R-011, R-012, R-031, R-045 |
| AI portfolio (P10) | Precision Agriculture Manager with the vCISO | R-028, R-029, R-030, R-031, R-032, R-033 |

When a system-level review changes a rating, the owner updates this file, and the change flows to the enterprise roll-up.

## 6. Approval
- Chief Operating Officer: approved Moderate and Low treatments, 2026-09-15.
- Chief Executive Officer: approved the High and Very High treatment plans, the risk appetite statements, and the FY2027 security budget, 2026-09-15.
- Board audit committee: received the results on 2026-09-15. Next report: 2026-12 quarterly meeting.
- Next full risk assessment: July 2027, or sooner after a major change (for example an acquisition, R-049) or a significant incident.
