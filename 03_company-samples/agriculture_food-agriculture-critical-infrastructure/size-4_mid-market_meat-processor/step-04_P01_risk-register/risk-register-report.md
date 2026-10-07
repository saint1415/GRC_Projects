# Risk Register Report: Cris Santos Company | Food and Agriculture | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed meat processor with two USDA-inspected plants) |
| Size tier | Mid-Market (850 employees) |
| Vertical | Food and Agriculture |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2, I-3 values); enterprise roll-up per NIST IR 8286 Rev. 1 |
| Also supports | HACCP reassessment inputs (9 CFR 417.4(a)(3)); the voluntary food defense vulnerability assessments; PSM process hazard analysis revalidation (29 CFR 1910.119(e)) |
| Prepared | 2026-07-24 by the Security Manager and the vCISO with the Controls Engineering Manager and the VP FSQA; updated 2026-08-21 with P07 results (R-052 added 2026-08-10 from P07 testing) and 2026-09-04 with P10 results |
| Approved | 2026-09-15: Chief Operating Officer (Moderate and below), Chief Executive Officer (High and Very High); presented to the board audit committee the same day |

## 1. Scope and risk framing
**Scope.** Both plants and the corporate functions, the Plant Production and Cold-Chain Monitoring System (PPCM, SSP in P02), the cloud landing zone (P04), the business SaaS systems, the Customer Traceability and EDI Services (P09), the 26 vendors with OT, cloud, or data access, and the AI portfolio (P10). Processes and impact values come from the BIA (P05); vulnerabilities come from the gap analysis (P03) and the control assessment (P07).

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
| Food safety | **Very low** | No cyber or technology risk that could plausibly let adulterated or misbranded product reach consumers is accepted above Low. Any such risk at Moderate or higher must have a funded treatment plan within 90 days. Measure: food-safety-linked risks above Moderate (8 today: R-001, R-003, R-006, R-012, R-015, R-026, R-031, R-052; target 0 by 2027-12-31) |
| Worker and community safety (ammonia) | **Very low** | No cyber risk to refrigeration control or ammonia alarms is accepted above Low. Measure: R-005 and R-014 at Low by 2026-12-31 |
| Availability of production and cold chain | **Low** | Recovery capabilities must meet the BIA RTOs for every High-criticality process (P05). Measure: every High process has a passed recovery test in the last 12 months |
| Regulatory compliance | **Low** | No FSIS HACCP, Sanitation SOP, or recall requirement and no PSM or RMP requirement analyzed in P03 may stay Not met beyond 2027-03-31 |
| Third parties | **Moderate**, with conditions | Vendors are essential (integrators, refrigeration contractors, SaaS), but no vendor gets standing OT access, and every Tier 1 vendor is reassessed each year (P09) |
| Acquisitions | **Moderate**, with conditions | The PE strategy includes further acquisitions. No acquired site connects to company networks until it passes the integration standard (R-022) |
| Innovation and AI | **Moderate** | The company wants AI benefits in inspection, planning, and maintenance, but only through the P10 governance process. No AI system may replace a CCP or a food safety decision |
| Financial loss from cyber events | **Moderate** | Single-event losses up to the $500,000 insurance retention are tolerable. Scenarios above $3 million need a treatment that reduces likelihood, not only insurance |

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the Food and Agriculture overlay, CISA and FBI advisories on ransomware in food processing, the BIA, interviews with every process owner, walkthroughs of both plants (2026-07-08 and 2026-07-14), the gap analysis (P03), and the control assessment (P07).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood of adverse impact were each rated, then combined with **Table G-5**.
3. **Rate impact.** Impact used **Table H-3**, anchored to the BIA impact categories (cost, operations, regulatory, food and worker safety, reputation).
4. **Determine risk.** Risk level came from **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the two tables, not assigned by hand.
5. **Semi-quantitative view.** `semi_quant_score` gives each risk level its SP 800-30 Appendix I semi-quantitative value (Very High 10, High 8, Moderate 5, Low 2, Very Low 0). `exposure_estimate_usd` gives an order-of-magnitude single-event loss range from the BIA values, used for the enterprise roll-up (NIST IR 8286 Rev. 1). The ranges are estimates for prioritizing, not actuarial figures.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 2 |
| High | 13 |
| Moderate | 29 |
| Low | 8 |
| Very Low | 0 |
| **Total** | **52** |

Treatments: 48 Mitigate, 4 Accept (R-030, R-040, R-049, R-050). Status: 23 Open, 25 In progress, 4 Accepted.

Cyber insurance ($15 million limit, $500,000 retention) transfers part of the financial exposure for R-001, R-002, and R-034. It is not recorded as the treatment for any risk, because it does not lower the likelihood of harm to consumers, workers, or operations.

### Top risks (Very High and High)
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware spreads into OT and halts lines and cold-chain monitoring | Very High | Plant 2 segmentation; vendors onto the gateway; immutable OT backups; OT alerts to the MSSP | IT Director | 2027-03-31 |
| R-002 | Plant 2 integrator's shared VPN account used to reach SCADA and blenders | Very High | Gateway with named accounts and MFA; retire the VPN | Security Manager | 2026-10-31 |
| R-003 | Malicious or unauthorized change to dosing, cook, or chill setpoints through shared logins | High | Named accounts; two-person approval; range limits; change alerts | Controls Engineering Manager | 2027-03-31 |
| R-005 | Plant 2 refrigeration controller manipulated through the cellular modem | High | Disconnect the modem; gateway; PSM management of change | Director of Engineering and Maintenance | 2026-10-31 |
| R-006 | Electronic CCP and Sanitation SOP records cannot be shown to be trustworthy | High | Audit trail; named sign-off; record locking; STD-05 | VP FSQA | 2026-12-31 |
| R-007 | Plant 1 SCADA and MES not restorable within RTO | High | Immutable OT backups; repository; quarterly restore tests | Controls Engineering Manager | 2026-12-31 |
| R-012 | Plant 2 cold-chain monitoring fails silently | High | Escalation; dedicated gateway network; manual log procedure | Director of Supply Chain and Logistics | 2026-10-31 |
| R-014 | Refrigeration run blind during a cyber incident leads to an ammonia release | High | Cyber scenarios in PSM and RMP emergency plans; manual operation drill | Director of Engineering and Maintenance | 2026-12-31 |
| R-015 | Product ships during a control-system incident because response is not tied to product hold and FSIS notice | High | P08 runbooks; tabletop | VP FSQA | 2026-11-30 |
| R-019 | Privileged SaaS or OT engineering account takeover | High | Privileged access management; MFA on engineering workstations | Security Manager | 2027-03-31 |
| R-023 | Plant 1 integrator compromise reaches SCADA or the MES | High | Per-session vendor enablement; contract terms | Security Manager | 2026-12-31 |
| R-026 | Over-reliance on AI vision inspection lets foreign material pass | High | P10 conditions; subgroup monitoring | VP FSQA | 2026-12-31 |
| R-031 | Insider routes CIP chemicals into the Injector 2 brine system | High | Hardwired interlock; valve alarms | Director of Engineering and Maintenance | 2026-12-31 |
| R-038 | SOC 2 Type 2 not ready; largest customer reduces volume | High | P09 remediation; observation period from 2027-04-01 | Chief Financial Officer | 2027-12-31 |
| R-052 | Default password on the Line 6 x-ray unit used to weaken the foreign material CCP (found in P07) | High | Credential sweep of inspection devices; disable web services | OT security engineer | 2026-10-31 |

**Themes.**
- **Plant 2 carries the acquisition's debt (R-001, R-002, R-004, R-005, R-008, R-012, R-021, R-047).** The company bought a plant with a flat network, shared remote access, and no OT inventory. Most Very High and High risks start there.
- **Shared OT logins break both security and food safety records (R-003, R-006, R-020, R-052).** The same fix (named accounts with fast sign-in) closes an attack path and makes CCP records attributable as 9 CFR 417.5(b) expects.
- **Recovery is proven in the cloud, not in OT (R-007, R-008, R-016).** Cloud backups are isolated and tested; OT backups are neither.
- **Safety-critical decisions are not yet linked to cyber response (R-014, R-015, R-051).** P08 adds product hold, FSIS notice, and PSM emergency steps to the runbooks.

## 4. Treatment summary
**Funded in the FY2027 security plan (approved by the CEO 2026-09-15: $1.44 million one-time and $260,000 a year, plus $240,000 for SOC 2 across 2027):**
- Plant 2 segmentation, OT DMZ, and remote access migration ($420,000)
- OT monitoring: Plant 2 sensor and MSSP OT onboarding ($90,000 one-time, $140,000 a year)
- Named HMI and MES accounts with two-person approval, by both integrators ($260,000)
- OT backup and recovery: immutable storage, Plant 2 repository, restore testing ($150,000)
- Privileged access management for SaaS and OT administrators ($120,000 one-time, $80,000 a year)
- Replacement of 9 unsupported HMIs and 2 engineering workstations (2027 capital plan, $310,000)
- Records application and historian integrity changes ($90,000)
- Security awareness for production, sanitation, and maintenance workers ($40,000 a year)
- SOC 2 readiness and Type 2 examination for the Customer Traceability and EDI Services ($240,000 across 2027)

Smaller items (badge locks at Plant 2, cellular failover, exercise facilitation, contract changes) are funded from the operating budget. Each funded item maps to a P07 POA&M entry.

**Accepted (4):** R-030 (Low, Director of Engineering and Maintenance), R-040 (Moderate, COO; within appetite because backups are isolated and write-once), R-049 (Low, edge protection), R-050 (Low, encrypted devices).

**Contract actions:** security, change notice, and incident notice terms for both controls integrators, both refrigeration contractors, the cold-chain vendor, and the AI vision vendor (R-023, R-024, R-025), due 2026-12-31.

## 5. Enterprise and system-level registers
This file is the **enterprise register**. Following NIST IR 8286 Rev. 1, it rolls up to the company's enterprise risk register as one line, "Cybersecurity and technology resilience", owned by the COO and reported to the audit committee each quarter with the counts above and the top risks.

System-level registers are filtered views of this file, kept by each system owner, rather than separate spreadsheets. That keeps one set of ratings.

| System-level register | Owner | Risks in scope |
|---|---|---|
| PPCM (SSP in P02) | Controls Engineering Manager with the Security Manager | 34 risks whose affected assets include SYS-01 to SYS-07 or SYS-14 (filter the `affected_asset_or_process` column) |
| Plant 2 integration | Plant Manager, Plant 2 with the IT Director | R-001, R-002, R-004, R-005, R-008, R-012, R-021, R-044, R-047 |
| Ammonia refrigeration (feeds the PSM process hazard analyses) | Director of Engineering and Maintenance | R-005, R-014, R-030, R-043 |
| AI portfolio (P10) | VP FSQA (AI-001) and Chief Operating Officer (others) | R-025, R-026, R-027, R-028, R-029, R-030 |

When a system-level review changes a rating, the owner updates this file, and the change flows to the enterprise roll-up.

## 6. Approval
- Chief Operating Officer: approved Moderate and Low treatments and the acceptance of R-040, 2026-09-15.
- Chief Executive Officer: approved the High and Very High treatment plans, the risk appetite statements, and the FY2027 security budget, 2026-09-15.
- Board audit committee: received the results on 2026-09-15. Next report: 2026-12 quarterly meeting.
- Next full risk assessment: July 2027, or sooner after a major change (for example another acquisition, R-022) or a significant incident.
