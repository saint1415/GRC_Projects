# Risk Register Report: Cris Santos Company | Information Technology | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (cloud hosting and managed infrastructure provider) |
| Size tier | Mid-Market (600 employees) |
| Vertical | Information Technology |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2, I-3 values); enterprise roll-up per NIST IR 8286 Rev. 1 |
| Also satisfies | RA-3 and RA-3(1) in the FedRAMP Rev5 Class C control list (P02); input to the 2026 rules transition (P03) |
| Prepared | 2026-07-31 by the GRC Manager with the Director of Security, the process owners, and the data center operations managers; R-026 added 2026-08-14 from P07 testing |
| Approved | 2026-09-22: Chief Technology Officer (Moderate and below), Chief Executive Officer (High and Very High); presented to the board audit committee the same day |

## 1. Scope and risk framing
**Scope.** All business units and the 16 processes in the BIA (P05); the Hosting Control Plane and Customer Portal (HCP) in both partitions (P02); the RMM tool, backup platform, and corporate systems (SYS-08, SYS-10, SYS-12, SYS-13); about 260 vendors (SYS-15); and the AI tools in P10. Impact values come from the BIA; vulnerabilities come from the FedRAMP transition and regulatory gap analysis (P03), the cloud control map (P04), and the control assessment (P07).

**Who can accept risk (tolerance).**
| Risk level | Who may accept | Conditions |
|---|---|---|
| Very Low and Low | The risk owner (director level or above) | Recorded in the register; reviewed yearly |
| Moderate | Chief Technology Officer | Treatment plan or documented reason; reviewed every 6 months |
| High | Chief Executive Officer | Temporary only (up to 12 months) with a dated treatment plan; reported to the audit committee each quarter |
| Very High | Not acceptable | The CEO may approve a temporary exception of up to 90 days only after notifying the audit committee chair, while treatment is under way |

### Risk appetite statements
Approved by the Chief Executive Officer and noted by the audit committee on 2026-09-22.

| Area | Appetite | Statement and measure |
|---|---|---|
| Customer trust and tenant isolation | **Very low** | No risk that could let one attack reach many customers at once (tooling, control plane, templates) is accepted above Moderate. Measure: R-001, R-002, R-011 at Moderate or lower by 2027-03-31 |
| Federal certification | **Very low** | The Government Cloud must keep its FedRAMP certification without corrective action. Every 2026 ruleset must be met by its "maintaining" date, not its grace date. Measure: P03 roadmap milestones met each quarter (R-023) |
| Availability | **Low** | Recovery must meet the BIA RTOs for all High-criticality processes (P05), and no outage may reach the 4-hour bank notice threshold because recovery failed. Measure: every High process has a passed recovery test in the last 12 months (R-005, R-018) |
| Regulatory and contract notices | **Very low** | Every notice clock (FedRAMP, DFARS, bank rule, state law, MSA) is met. Measure: both P08 tabletops pass their notice steps; bank contacts verified for 38 of 38 banks |
| Third parties | **Moderate**, with conditions | Vendors are used widely, but every Tier 1 vendor is reviewed each year, and any vendor with access to customer data or production has incident notice terms. Measure: 14 of 14 Tier 1 reviews current (R-025) |
| Innovation and AI | **Moderate** | AI is welcome in operations and engineering, but only through the P10 process, and never with authority to close security alerts on privileged access or tooling without human review |
| Financial loss from cyber events | **Moderate** | Single-event losses up to the $500,000 insurance retention are tolerable. Scenarios above $3 million need a treatment that lowers likelihood, not only insurance |

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the Information Technology overlay (cloud control planes, identity providers, software supply chain, MSP RMM tools, DNS), CISA advisories on attacks against managed service providers, the BIA, interviews with process owners, the gap analysis (P03), and the control assessment (P07).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood of adverse impact were each rated, then combined with **Table G-5**.
3. **Rate impact.** Impact used **Table H-3**, anchored to the BIA impact categories (cost, operations, regulatory and contractual, reputation). Risks that reach many customers at once through shared tooling were rated Very High impact.
4. **Determine risk.** Risk level came from **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the two tables, not assigned by hand.
5. **Semi-quantitative view.** `semi_quant_score` gives each risk level its SP 800-30 Appendix I value (Very High 10, High 8, Moderate 5, Low 2, Very Low 0). `exposure_estimate_usd` gives an order-of-magnitude single-event loss range built from the BIA values (for example the SLA credit tiers and the DC-1 scenario), used for the enterprise roll-up (NIST IR 8286 Rev. 1). The ranges are estimates for prioritizing, not actuarial figures.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 13 |
| Moderate | 18 |
| Low | 20 |
| Very Low | 0 |
| **Total** | **52** |

Treatments: 48 Mitigate, 4 Accept (R-014, R-019, R-021, R-032, all Low). Status: 25 Open, 23 In progress, 4 Accepted.

Cyber insurance ($15 million limit, $500,000 retention) transfers part of the financial exposure for R-001, R-002, R-011, and R-025. It is not recorded as the treatment for any risk, because it does not lower the likelihood of harm to customers.

### Top risks (Very High and High)
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | RMM tool used to push a malicious script to 11,200 managed customer servers | Very High | Retire shared super-administrator accounts; two-person approval for multi-customer scripts; RMM logs to the SIEM | Director of Managed Services | 2026-12-31 |
| R-002 | Commercial control plane credentials act on every commercial VM | High | Scoped short-lived credentials per job and cluster | VP Software Engineering | 2027-03-31 |
| R-003 | Takeover of DC-1 clusters A and B through local accounts and the NOC network path | High | Federate through PAM; deny by default; retire the legacy VPN | VP Platform Engineering | 2026-12-31 |
| R-004 | Destructive attack on the control plane | High | Quarterly restore tests; ransomware tabletop | Director of Cloud Operations | 2027-03-31 |
| R-005 | Commercial control plane misses its 4-hour RTO | High | Government runbook for the commercial partition; quarterly tests | VP Software Engineering | 2027-03-31 |
| R-006 | Unpatched hypervisor, storage controller, or BMC exploited | High | Monthly scans everywhere; KEV automation; BMC firmware cycle | VP Platform Engineering | 2027-03-07 |
| R-011 | Malicious code in a commercial VM template | High | HSM signing and verification in both partitions; SBOM | VP Software Engineering | 2026-12-31 |
| R-015 | Intrusion missed because DC-1 and RMM logs are not collected | High | Onboard sources; 1-year online retention | Security Operations Manager | 2027-01-31 |
| R-016 | AI triage closes a true-positive alert | High | Stop auto-close for privileged and tooling alerts; weekly sampling | Security Operations Manager | 2026-11-30 |
| R-018 | Hurricane takes DC-1 offline for days | High | Contingency plan and DC-1 site-loss runbook; failover exercise; protection by default for bank customers | VP Platform Engineering | 2027-06-30 |
| R-023 | FedRAMP corrective action or loss of certification in the 2026 rules transition | High | P03 transition roadmap with quarterly audit committee status | GRC Manager | 2027-04-02 |
| R-025 | Breach at a Tier 1 vendor reaches customers | High | Complete Tier 1 reviews; incident notice terms | GRC Manager | 2026-12-31 |
| R-026 | Unowned machine credential changes the government partition (found in P07) | High | Machine credential inventory; 90-day lifetime; quarterly review | Security Engineering Lead | 2026-12-31 |
| R-030 | FedRAMP 1-hour Initial Incident Report missed | High | Reportability and PAIN steps; JSON templates; tabletop | Security Operations Manager | 2026-12-15 |

**Themes.**
- **Two-speed security (R-002, R-003, R-006, R-009, R-011, R-015).** The government partition is well controlled. The commercial partition and DC-1 lag, and attackers would go there first because one compromise reaches thousands of VMs.
- **Tools that reach many customers (R-001, R-002, R-011, R-016, R-026).** The RMM tool, the control plane, the template pipeline, and the SIEM triage all have reach across customers. These carry the highest impact ratings.
- **The FedRAMP transition (R-023, R-030, R-031, R-035, R-036, R-039).** The certification is in place, but the 2026 rules change how it is maintained. The first deadlines (VDR and VER, 2026-12-07) are close.
- **Recovery at scale (R-004, R-005, R-018).** Backups are isolated and immutable. What is missing is proof of commercial recovery within the RTO and a plan for losing DC-1.
- **AI adopted without governance (R-016, R-040 to R-043).** Five tools went live or into pilot without review. P10 addresses them.

## 4. Treatment summary
**Funded in the FY2027 security plan (approved by the CEO 2026-09-22, $2.6 million one-time and $1.05 million a year):**
- PAM and just-in-time elevation for DC-1 and the commercial accounts; federation of DC-1 clusters A and B ($420,000 one-time, $120,000 a year)
- RMM hardening, RMM log integration, and per-customer engineer scoping ($90,000 one-time, $40,000 a year)
- SIEM onboarding of DC-1 and RMM sources and 1-year commercial retention ($260,000 a year)
- Commercial signing key in the HSM, signature verification at deployment, SBOM and build provenance ($180,000)
- Vulnerability management at scale: monthly commercial scanning, KEV automation, BMC firmware program, replacement of 9 end-of-support storage controllers ($640,000 one-time, $90,000 a year)
- Recovery: commercial restore testing, DC-1 failover exercise, added capacity at DC-2 and DC-3 ($780,000 one-time)
- FedRAMP 2026 rules transition: machine-readable package, trust center, PAIN-based vulnerability and incident tooling, FedRAMP advisor ($310,000 one-time, $150,000 a year)
- Two GRC analysts and one vendor risk analyst ($390,000 a year)
- Expanded SOC 2 Type 2 examination ($180,000 one-time, as part of the 2027 audit budget)

Each funded item maps to a P07 POA&M entry or a P03 roadmap milestone.

**Accepted (4):** R-014 (Low; hardware keys), R-019 (Low; inherited facility controls), R-021 (Low; two carriers per site), R-032 (Low; encrypted laptops).

**Contract actions:** incident notice terms for 4 Tier 1 vendors, including the RMM vendor (R-025), due 2027-03-31; a 28 CFR Part 202 question in vendor onboarding (R-046).

## 5. Enterprise and system-level registers
This file is the **enterprise register**. Following NIST IR 8286 Rev. 1, it rolls up to the company's enterprise risk register as one line, "Cybersecurity, tenant trust, and platform resilience", owned by the CTO and reported to the audit committee each quarter with the counts above and the top risks.

System-level registers are filtered views of this file, kept by each system or program owner, rather than separate spreadsheets. That keeps one set of ratings.

| System-level register | Owner | Risks in scope |
|---|---|---|
| HCP (SSP in P02) | Chief Technology Officer, maintained by the GRC Manager | 29 risks whose affected assets include SYS-01 to SYS-04, SYS-06, SYS-07, SYS-09, or SYS-11 (filter the `affected_asset_or_process` column) |
| Government Cloud and FedRAMP certification | Federal Program Director | R-004, R-023, R-026, R-030, R-031, R-033, R-034, R-035, R-036, R-039, R-046 |
| Data centers DC-1, DC-2, DC-3 | VP Platform Engineering | 18 risks whose affected assets include DC-1 or SYS-05 |
| Managed services and the RMM tool | Director of Managed Services | R-001, R-015, R-022, R-025, R-033, R-050 |
| AI portfolio (P10) | Chief Technology Officer | R-016, R-040, R-041, R-042, R-043 |

When a system-level review changes a rating, the owner updates this file, and the change flows to the enterprise roll-up.

## 6. Approval
- Chief Technology Officer: approved the Moderate and Low treatments and the acceptance of R-014, R-019, R-021, and R-032, 2026-09-22.
- Chief Executive Officer: approved the High and Very High treatment plans, the risk appetite statements, and the FY2027 security budget, 2026-09-22. R-001 is accepted only until its first milestone (shared RMM accounts retired by 2026-10-31).
- Board audit committee: received the results on 2026-09-22. Next report: the 2026-12 quarterly meeting.
- Next full risk assessment: July 2027, or sooner after a major change (for example a new data center or an acquisition) or a significant incident.
