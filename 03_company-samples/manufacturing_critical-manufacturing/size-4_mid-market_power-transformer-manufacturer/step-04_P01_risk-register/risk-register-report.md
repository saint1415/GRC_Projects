# Risk Register Report: Cris Santos Company | Critical Manufacturing | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed power and distribution transformer manufacturer, Florida) |
| Size tier | Mid-Market (850 employees; not SBA-small under the 800-employee standard for NAICS 335311) |
| Vertical | Critical Manufacturing |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2, and the Appendix I semi-quantitative values), with OT threat sources and predisposing conditions from NIST SP 800-82 Rev. 3 Appendix C; enterprise roll-up per NIST IR 8286 Rev. 1 |
| Benchmark | NIST CSF 2.0 with SP 800-82 Rev. 3 (voluntary; see P03 section 1) |
| Prepared | 2026-07-31 by the Security Manager and the vCISO with the OT Security Engineer; R-051 added 2026-08-21 from P07 testing |
| Approved | 2026-09-15: Chief Operating Officer (Moderate and below), Chief Executive Officer (High and Very High, risk appetite); presented to the board audit committee the same day |

## 1. Scope and risk framing
**Scope.** The whole company:
- both plants and their control systems, test systems, and historians;
- the ERP and Production Scheduling Platform (EPSP, P02) and the landing zone (P04);
- the products and services supplied to utilities: TMU configuration software, supplied firmware, field service access, and the Fleet Monitoring Service (FMS);
- the PLM vault, SaaS services, and the AI portfolio (P10);
- the suppliers with access to company systems or data (about 190, including the MSSP, cloud provider, OEMs, and the TMU electronics supplier);
- the obligations the company owes customers: the 31 utility Supplier Cyber Security Addenda, the FMS subscription terms, and the federal contract clauses.

Processes and impact values come from the BIA (P05); vulnerabilities come from the gap analysis (P03) and the control assessment (P07).

**What matters most.** The company builds equipment that utilities need to keep the grid running and to restore it after storms. Leadership ranks three outcomes above the rest:
- nobody gets hurt at a drying oven, oil processing station, or test bay, and nothing unsafe reaches a utility substation;
- both plants keep producing, especially in hurricane season;
- the 31 addendum utilities and the 14 FMS subscribers keep trusting the company, which now depends on meeting the cyber terms in their contracts.

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
| Worker safety and product integrity | **Very low** | No cyber risk that could plausibly injure a worker or put an unsafe product, firmware, software, or advisory in a utility substation is accepted above Low. Any such risk rated Moderate or higher must have a funded treatment plan within 90 days. Measure: safety and product-integrity risks above Low (7 today: R-001, R-003, R-006, R-007, R-011, R-012, R-028; target 0 by 2027-12-31) |
| Customer cyber obligations | **Low** | No utility addendum notice or FAR reporting clock may be missed. Measure: missed or late notices (3 in 2026; target 0 from 2026-11-01) |
| Availability of production | **Low** | Recovery capabilities must meet the BIA RTOs for all High-criticality processes (P05). Measure: every High process has a passed recovery test in the last 12 months (0 of 9 today) |
| Confidentiality of designs and customer data | **Moderate** | Designs are shared with suppliers and customers under NDA as the business requires, but no Restricted data goes to an unapproved service. Measure: R-013 and R-032 at Low by 2027-12-31 |
| Third parties | **Moderate**, with conditions | Suppliers and OEMs are used widely, but every Tier 1 supplier is reassessed each year (P09) and every OEM with plant access goes through the remote access gateway |
| Innovation and AI | **Moderate** | The company wants AI in planning, maintenance, and the FMS, but only through the AI governance process in P10. No AI may make or substantially inform a decision about a person, or an alert to a utility, without human review |
| Financial loss from cyber events | **Moderate** | Single-event losses up to the $500,000 insurance retention are tolerable. Scenarios above $2 million need a treatment that reduces likelihood, not only insurance |

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, SP 800-82 Rev. 3 Appendix C, the vertical scenario (ransomware disrupting production of grid equipment), the BIA, interviews with every process owner and both Plant Managers, the gap analysis (P03), and the control assessment (P07).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood of adverse impact were each rated, then combined with **Table G-5**.
3. **Rate impact.** Impact used **Table H-3**, anchored to the BIA impact categories (cost, operations, safety, regulatory and contractual, reputation).
4. **Determine risk.** Risk level came from **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the two tables, not assigned by hand.
5. **Semi-quantitative view.** `semi_quant_score` gives each risk level its SP 800-30 Appendix I semi-quantitative value (Very High 10, High 8, Moderate 5, Low 2, Very Low 0). `exposure_estimate_usd` gives an order-of-magnitude single-event loss range from the BIA values, used for the enterprise risk roll-up (NIST IR 8286 Rev. 1). The ranges are estimates for prioritizing, not actuarial figures.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 10 |
| Moderate | 24 |
| Low | 17 |
| Very Low | 0 |
| **Total** | **52** |

Treatments: 49 Mitigate, 3 Accept (R-017, R-023, R-030). Status: 25 Open, 24 In progress, 3 Accepted.

Cyber insurance ($15 million limit, $500,000 retention) transfers part of the financial exposure for R-001, R-002, and R-051. It is not recorded as the treatment for any risk, because it does not lower the likelihood of harm to workers, plants, or customers.

### Top risks (Very High and High)
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware spreads through Plant 2's flat network, dual-homed MES, and domain trust and stops both plants | Very High | Plant 2 OT DMZ; remove dual-homing and the trust; allowlisting; Plant 2 OT monitoring | OT Security Engineer | 2027-06-30 |
| R-002 | ERP encrypted and recovery takes far longer than the 24-hour RTO | High | Contingency plan; quarterly restore tests; annual rebuild exercise | IT Director | 2027-03-31 |
| R-003 | Always-on Plant 2 OEM router used to change oven or oil processing setpoints | High | Routers off between sessions; move OEMs to the remote access gateway | OT Security Engineer | 2026-12-31 |
| R-006 | Plant 2 controller programs cannot be restored | High | Automated OT backups at Plant 2; OT restore tests at both plants | Director of Manufacturing Engineering | 2027-03-31 |
| R-007 | Tampered firmware or configuration software shipped to utility substations | High | Hash re-check at final test; SBOM; secure development standard | VP Engineering | 2027-03-31 |
| R-008 | Missed utility addendum notice costs a supply agreement | High | Notice procedures; automated access notices; monthly register check | General Counsel | 2026-12-31 |
| R-012 | Code signing key stolen and used to sign malicious software | High | Hardware-backed signing with 2-person approval | VP Engineering | 2026-12-15 |
| R-015 | MSSP or SIEM platform compromise pushes malicious actions | High | Platform SOC 2; 2-person approval for mass actions | Security Manager | 2027-03-31 |
| R-028 | AI-003 misses an incipient fault on a utility transformer | High | Subgroup monitoring; quarterly validation; model change control | Director of Digital Services | 2027-03-31 |
| R-038 | Takeover of a privileged account that uses push MFA | High | FIDO2 keys for all 41 privileged accounts | Security Manager | 2026-12-31 |
| R-051 | Plant 2 MES service account with corporate Domain Admins rights (found in P07) | High | Rights removed 2026-08-19; one-way trust; retire the Plant 2 domain | Security Manager | 2027-03-31 |

**Themes.**
- **Plant 2 is the soft spot (R-001, R-003, R-006, R-009, R-010, R-033, R-051).** Plant 1 got an OT DMZ, a remote access gateway, OT monitoring, and automated OT backups in 2025. Plant 2 was acquired in 2024 and has none of them. Fixing Plant 2 lowers 15 of the 52 risks.
- **Products and services supplied to utilities (R-007, R-008, R-012, R-028, R-039, R-045).** The company is now a software and data supplier as well as a transformer maker. Its customers' CIP-013 programs and the FMS make those risks contractual, and three notices were already late in 2026.
- **Recovery is designed but unproven (R-002, R-006, R-024, R-047).** Backups are isolated and immutable, but no High-criticality process has a passed recovery test.
- **Third parties with privileged reach (R-015, R-018, R-019).** The MSSP, OEMs, and the ERP vendor all hold paths into company systems.
- **AI adopted ahead of governance (R-028 to R-031).** P10 addresses them.

## 4. Treatment summary
**Funded in the FY2027 security plan (approved by the CEO 2026-09-15; about $1.29 million one-time and capital, and $245,000 a year):**
- Plant 2 OT DMZ, zoning, and extension of the remote access gateway ($420,000)
- Passive OT monitoring at Plant 2 with MSSP monitoring ($60,000 one-time, $45,000 a year)
- SIEM onboarding of both MES instances, the historians, the integration platform, and the FMS ($85,000 a year)
- Retirement of the Plant 2 legacy domain ($90,000)
- Extension of the OT backup tool to Plant 2 and a recovery testing program ($70,000)
- FIDO2 keys for all privileged accounts and privileged access management for OT engineering workstations ($110,000 one-time, $30,000 a year)
- Hardware-backed code signing, SBOM tooling, and secure development training ($75,000 one-time, $20,000 a year)
- FMS recovery, continuous backup, and logging ($60,000 one-time, $25,000 a year)
- SOC 2 readiness and Type 2 examination for the FMS ($240,000 across 2027)
- Replacement of 8 unsupported HMIs a year with OEM support ($160,000 a year of capital, first tranche in FY2027)
- Vendor risk program tooling ($40,000 a year)

Smaller items (Plant 2 server room badge reader, access point removal, call-back verification, exercise facilitation, contract changes) are funded from the operating budget. Each funded item maps to a P07 POA&M entry.

**Accepted (3):** R-017 (Low; workarounds adequate), R-023 (Low; the AI-002 replica is already isolated in the OT DMZ), and R-030 (Low; preventive maintenance continues unchanged). The COO recorded all three on 2026-09-15.

**Contract and procedure actions (no capital):** notice procedures and an automated access-notice step for the 31 addendum utilities (R-008, R-039); OEM security terms at renewal (R-018); an incident notice term in the HR SaaS contract (R-037); the quarterly SAM.gov FASCSA check (R-035).

## 5. Enterprise and system-level registers
This file is the **enterprise register**. Following NIST IR 8286 Rev. 1, it rolls up to the company's enterprise risk register as one line, "Cybersecurity and operational technology resilience", owned by the COO and reported to the audit committee each quarter with the counts above and the top risks.

System-level registers are filtered views of this file, kept by each system owner, rather than separate spreadsheets. That keeps one set of ratings.

| System-level register | Owner | Risks in scope |
|---|---|---|
| ERP and Production Scheduling Platform (EPSP; SSP in P02) | Chief Operating Officer, maintained by the Security Manager | 17 risks whose affected assets include SYS-01, SYS-02, SYS-03, SYS-05, or SYS-09 (filter the `affected_asset_or_process` column) |
| Plant 2 OT and integration | Director of Manufacturing Engineering with the OT Security Engineer | 15 risks that name Plant 2: R-001, R-003, R-006, R-009, R-010, R-011, R-021, R-022, R-033, R-034, R-041, R-048, R-049, R-050, R-051 |
| Fleet Monitoring Service (SOC 2 scope, P09) | Director of Digital Services | R-024, R-025, R-026, R-027, R-028, R-052 |
| Products supplied to utilities | VP Engineering | R-007, R-012, R-028, R-039, R-045 |
| AI portfolio (P10) | vCISO for the AI review group | R-014, R-023, R-028, R-029, R-030, R-031 |

When a system-level review changes a rating, the owner updates this file, and the change flows to the enterprise roll-up.

## 6. Approval
- Chief Operating Officer: approved Moderate and Low treatments and the 3 acceptances, 2026-09-15.
- Chief Executive Officer: approved the Very High and High treatment plans, the risk appetite statements, and the FY2027 security budget, 2026-09-15. The CEO accepted none of the High risks; all are being mitigated.
- Board audit committee: received the results on 2026-09-15. Next report: 2026-12 quarterly meeting.
- Next full risk assessment: July 2027, or sooner after a major change (the Plant 2 OT DMZ cutover, the Plant 2 MES migration, an acquisition), a significant incident, or publication of the CIRCIA final rule.
