# Risk Register Report: Cris Santos Company | Utilities | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (investor-owned electric distribution utility, NERC-registered Distribution Provider, with a Utility Services line for 4 client utilities) |
| Size tier | Mid-Market (850 employees) |
| Vertical | Utilities |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2, and Appendix I semi-quantitative values); enterprise roll-up per NIST IR 8286 Rev. 1 |
| Also supports | NERC CIP-003-9 low impact cyber security plan (risk basis for Attachment 1 choices); the FTC Identity Theft Red Flags Rule periodic risk assessment of covered accounts (16 CFR 681.1(c)); the SOC 2 risk assessment criteria CC3.1 to CC3.4 (P09) |
| Prepared | 2026-07-31 by the Information Security Manager, the GRC analyst, and the vCISO; R-005 and R-041 updated and R-052 added on 2026-08-21 from P07 testing |
| Approved | 2026-09-17: Chief Operating Officer (Moderate and below), President and CEO (High, and the 90-day exception for the Very High risk); presented to the board audit committee the same day |

## 1. Scope and risk framing
**Scope.** All business units (System Operations, Engineering and Protection, OT Engineering, Field Operations, Customer Operations, Utility Services, Power Supply and Rates, and enterprise functions); the Distribution Operations Platform (DOP, the SSP system in P02); the cloud landing zone (P04); the customer and Utility Services SaaS systems; about 85 vendors with system or data access; and the AI and model portfolio (P10). Processes and impact values come from the BIA (P05); vulnerabilities come from the 15 gaps in `../00_company-facts.md`, the gap analysis (P03), and the control assessment (P07).

**Who can accept risk (tolerance).**
| Risk level | Who may accept | Conditions |
|---|---|---|
| Very Low and Low | The risk owner (director level or above) | Recorded in the register; reviewed each year |
| Moderate | Chief Operating Officer | Treatment plan or documented reason; reviewed every 6 months |
| High | President and CEO | Temporary only (up to 12 months) with a dated treatment plan; reported to the audit committee each quarter |
| Very High | Not acceptable | The CEO may approve a temporary exception of up to 90 days only after notifying the audit committee chair, while treatment is under way |

A known noncompliance with a NERC Reliability Standard is never accepted as a risk. It is remediated and self-reported (R-010).

### Risk appetite statements
Approved by the President and CEO and noted by the audit committee on 2026-09-17.

| Area | Appetite | Statement and measure |
|---|---|---|
| Public and crew safety | **Very low** | No cyber or technology risk that could plausibly energize a line under clearance, cause a protection misoperation, or remove remote control of the grid is accepted above Low. Measure: safety-linked risks above Low (6 today: R-001, R-004, R-005, R-007, R-014, R-016; target 0 by 2027-12-31) |
| Reliability standards compliance | **Very low** | Every potential noncompliance with a NERC Reliability Standard is self-reported within 60 days of discovery and mitigated on a dated plan. No OT project may go live without a CIP-002 review. Measure: open potential noncompliances (2 today, gaps 2 and 3) and OT project gates without a CIP-002 check (0 since 2026-09-17) |
| Availability of grid operations | **Low** | Recovery must meet the BIA RTOs for all High-criticality processes (P05). Measure: each High process has a passed recovery test in the last 12 months (1 of 4 today) |
| Confidentiality of customer data | **Low** | The company will not hold customer identity data it does not need. No risk of a breach of more than 10,000 customers' SSNs or driver license numbers is accepted above Moderate. Measure: R-003 and R-024 at Moderate or lower by 2027-03-31 |
| Utility Services clients | **Low** | Client data and service levels are protected as the company's own; a SOC 2 Type 2 report is available before the 2027 renewals. Measure: R-021, R-022, R-049 at Low by 2027-09-30 |
| Third parties | **Moderate**, with conditions | Vendors are used widely, but every vendor with OT remote access or customer data has security terms, and Tier 1 vendors are reviewed each year (P09) |
| Innovation and AI | **Moderate** | The company wants AI benefits in forecasting, revenue protection, and customer service, but only through the P10 governance process. No AI tool receives customer data or CEII without review |
| Financial loss from cyber events | **Moderate** | Single-event losses up to the $500,000 insurance retention are tolerable. Scenarios above $5 million need a treatment that lowers likelihood, not only insurance |

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the Utilities overlay, SP 800-82 Rev. 3 threat themes (vendor remote access, IT/OT pivot, field network attacks, supply chain), public advisories on campaigns against U.S. utilities, the BIA, interviews with every process owner, substation walkthroughs (2026-07-21 to 2026-07-23), the gap analysis (P03), and the control assessment (P07).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood of adverse impact were each rated, then combined with **Table G-5**.
3. **Rate impact.** Impact used **Table H-3**, anchored to the BIA impact categories (cost, operations, regulatory, public and crew safety, reputation).
4. **Determine risk.** Risk level came from **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the two tables, not assigned by hand.
5. **Semi-quantitative view.** `semi_quant_score` gives each risk level its SP 800-30 Appendix I semi-quantitative value (Very High 10, High 8, Moderate 5, Low 2, Very Low 0). `exposure_estimate_usd` gives an order-of-magnitude single-event loss range from the BIA values and client fees, used for the enterprise risk roll-up (NIST IR 8286 Rev. 1). The ranges are estimates for prioritizing, not actuarial figures. Safety consequences are described, not priced.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 7 |
| Moderate | 32 |
| Low | 12 |
| Very Low | 0 |
| **Total** | **52** |

Treatments: 46 Mitigate, 5 Accept (R-031, R-034, R-039, R-045, R-050), 1 Avoid (R-006). Status: 22 Open, 25 In progress, 5 Accepted.

Cyber insurance ($25 million aggregate limit, $500,000 retention) transfers part of the financial exposure for R-001, R-002, R-003, and R-014. It is not recorded as the treatment for any risk, because it does not lower the likelihood of harm to crews, customers, or the grid.

### Top risks (Very High and High)
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Unauthorized SCADA commands through the vendor support path and the 3 shared SCADA administrator accounts | Very High | Named, vaulted OT accounts with PAM extended to OT; session recording; SCADA command anomaly alerts. Running under a 90-day CEO exception (2026-09-17 to 2026-12-16) | OT Engineering Manager | 2026-12-31 |
| R-002 | Ransomware on corporate IT and cloud workloads halts dispatch, contact center integration, and Utility Services | High | Remove legacy IT/OT rules; restore tests; phishing for field and DCC staff; ransomware tabletop | Director of Information Technology | 2027-03-31 |
| R-003 | Theft of the CIS export (about 410,000 customer records with SSNs) | High | Minimize and expire the extract; named access; bulk-read alerts | Vice President of Customer Operations | 2026-12-31 |
| R-004 | Pivot from the corporate network to the historian and engineering workstations through 6 legacy rules | High | Remove the rules; engineering access only through jump hosts | Information Security Manager | 2026-11-30 |
| R-005 | Routable access to BES relays outside gateway and jump host controls (Substation H modem) | High | Survey all 74 substations; contract ban on contractor remote equipment; offline settings copy; SERC self-report | Director of Engineering and Protection | 2026-11-30 |
| R-006 | ADMS load-shedding module goes live as a medium impact BES Cyber System without a medium impact program | High | Avoid: board decision 2026-12-10 between a redesign and a funded medium impact program; CIP-002 check at every OT project gate | Chief Operating Officer | 2026-12-10 |
| R-007 | SCADA cannot be restored within 2 hours after a destructive attack | High | Spare server and gold images; quarterly restore drills; yearly failover; cross-training | OT Engineering Manager | 2027-03-31 |
| R-014 | Mass remote disconnect through the AMI head-end | High | Bulk limits and two-person approval; bulk rights cut from 22 to 4 users; DCC alert | Vice President of Customer Operations | 2026-11-30 |

**Themes.**
- **Vendor and privileged paths into OT (R-001, R-004, R-005, R-008, R-041, R-052).** The company met the new CIP-003-9 vendor remote access requirements on time, but privileged access on the SCADA servers, legacy firewall rules, and contractor equipment at substations still create paths around those controls. The P07 testing found two of them (the Substation H modem and default passwords on private LTE routers).
- **Recovery and visibility (R-007, R-011, R-016, R-017).** Detection is strong at the DCC and weak in the field; recovery targets are set but not yet demonstrated.
- **CIP scope change (R-006).** The largest compliance exposure is not a current gap but a design decision that would create a medium impact BES Cyber System in 2027.
- **Customer data concentration (R-003, R-019, R-020, R-023, R-024).** The company holds more identity data than it needs, in more places than it needs, and its Identity Theft Prevention Program is 7 years old.
- **Utility Services (R-014, R-021, R-022, R-049).** Client trust and about $14 million a year in fees depend on SOC 2 readiness and on controls the company runs inside vendor SaaS.

## 4. Treatment summary
**Funded in the FY2027 security plan (approved by the President and CEO 2026-09-17, about $2.06 million one-time and $310,000 a year):**
- PAM extended to OT, vaulting of SCADA administrator and router credentials ($260,000 one-time, $60,000 a year)
- Passive OT monitoring at the 20 largest substations and gateway log collection through the MSSP ($650,000 one-time, $140,000 a year)
- SCADA recovery: spare server, gold images, restore drills ($180,000)
- IT/OT firewall redesign ($90,000)
- SOC 2 readiness, Type 1, and the first Type 2 examination for Utility Services ($260,000 across 2027)
- CIS export redesign, data minimization, and purge jobs ($120,000)
- Cameras at the 20 most critical substations ($400,000, capital)
- FIDO2 security keys for administrators and vendor jump host users ($40,000)
- Identity Theft Prevention Program update with outside counsel ($60,000)
- Vendor risk tooling ($80,000 a year) and phishing simulations for all staff ($30,000 a year)

The SCADA upgrade that replaces the 2 unsupported HMIs and the historian (R-012) is in the 2027 capital plan ($1.4 million) and is not counted above. Smaller items (key rekeying, shred bins, scanning kiosks, procedure changes) are funded from operating budgets. Each funded item maps to a P07 POA&M entry or a P03 roadmap item.

**Avoided (1):** R-006. The risk is removed by a design or program decision before go-live rather than reduced afterwards.

**Accepted (5):** R-031 (Low, Director of Customer Service; field verification precedes any action), R-034 (Moderate, Chief Operating Officer; within appetite because the backup DCC, generators, and second-region backups exist), R-039 (Low), R-045 (Low), R-050 (Low).

**Contract actions:** security terms for Tier 1 and Tier 2 vendors at renewal (R-026), a ban on contractor remote equipment at substations (R-005), software integrity terms with the SCADA and ADMS vendor (R-015), an 8-hour RTO with the CIS vendor (R-021), and AI data-use terms with the contact center platform vendor (R-029).

## 5. Enterprise and system-level registers
This file is the **enterprise register**. Following NIST IR 8286 Rev. 1, it rolls up to the company's enterprise risk register as one line, "Cybersecurity, OT, and technology resilience", owned by the Chief Operating Officer and reported to the audit committee each quarter with the counts above and the top risks.

System-level registers are filtered views of this file, kept by each owner, rather than separate spreadsheets. That keeps one set of ratings.

| System-level register | Owner | Risks in scope |
|---|---|---|
| Distribution Operations Platform (DOP; SSP in P02) | Chief Operating Officer (system owner), maintained by the OT Engineering Manager | 25 risks whose affected assets include SYS-01, SYS-02, SYS-03, SYS-04, SYS-11, SYS-12, or SYS-14 (filter the `affected_asset_or_process` column) |
| Low impact BES Cyber Systems and CIP program | NERC Compliance Manager | R-001, R-005, R-006, R-008, R-009, R-010, R-011, R-042, R-046, R-048, R-051 |
| Utility Services system (SOC 2 scope, P09) | Director of Utility Services | R-003, R-014, R-021, R-022, R-026, R-043, R-049 |
| Customer data and identity theft (Red Flags Program) | Vice President of Customer Operations | R-003, R-019, R-020, R-023, R-024, R-025, R-032 |
| AI and model portfolio (P10) | Director of Power Supply and Rates (chair of the AI review group) | R-028, R-029, R-030, R-031, R-032 |

When a system-level review changes a rating, the owner updates this file, and the change flows to the enterprise roll-up.

## 6. Approval
- Chief Operating Officer: approved Moderate and Low treatments and the acceptance of R-034, 2026-09-17.
- President and CEO: approved the High treatment plans, the 90-day exception for R-001 after notifying the audit committee chair, the risk appetite statements, and the FY2027 security budget, 2026-09-17.
- Board audit committee: received the results on 2026-09-17. Next report: 2026-12 quarterly meeting, together with the ADMS design decision (R-006) on 2026-12-10.
- Next full risk assessment: July 2027, or sooner after a major change (for example the ADMS go-live decision or a new client utility) or a significant incident.
