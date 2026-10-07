# Risk Register Report: Cris Santos Company | Public Administration | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed GovTech systems integrator serving state and local agencies) |
| Size tier | Mid-Market (600 employees) |
| Vertical | Public Administration |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2, I-3 values); enterprise roll-up per NIST IR 8286 Rev. 1 |
| Also satisfies | SP 800-53 RA-3 (contract requirement); the risk assessment inputs agencies expect under Pub. 1075 and CJISSECPOL RA-3; GovRAMP and SOC 2 (CC3) risk assessment evidence |
| Prepared | 2026-07-31 by the GRC Manager with the vCISO and the Director of Information Security; R-050 added 2026-08-19 from P07 testing |
| Approved | 2026-09-17: Chief Operating Officer (Moderate and below), Chief Executive Officer (High and Very High); presented to the board audit committee the same day |

## 1. Scope and risk framing
**Scope.** All business units (ACMC hosted services, managed services, delivery, engineering, security, and corporate functions), the ACMC as bounded in the SSP (P02), the managed services remote management platform (SYS-10) and the agency-hosted systems it reaches, the 22 vendors with agency data or system access, and the AI use cases in P10. Processes and impact values come from the BIA (P05); vulnerabilities come from the gap analysis (P03) and the control assessment (P07).

**Whose harm counts.** Impact includes harm to agencies and to the people in their records, not only harm to the company. A failed CJIS or IRS review can end a contract as surely as an outage can, so contract and audit risks are rated alongside technical ones.

**Who can accept risk (tolerance).**
| Risk level | Who may accept | Conditions |
|---|---|---|
| Very Low and Low | The risk owner (director level or above) | Recorded in the register; reviewed annually |
| Moderate | Chief Operating Officer | Treatment plan or documented reason; reviewed every 6 months |
| High | Chief Executive Officer | Temporary only (up to 12 months) with a dated treatment plan; reported to the audit committee each quarter |
| Very High | Not acceptable | The CEO may approve a temporary exception of up to 90 days only after notifying the audit committee chair, while treatment is under way |
| Any risk that would breach a CJIS Security Addendum, Pub. 1075 Exhibit 7, or DPPA term | Not acceptable at any level | Treat it, or remove the regulated data or access |

### Risk appetite statements
Approved by the Chief Executive Officer and noted by the audit committee on 2026-09-17.

| Area | Appetite | Statement and measure |
|---|---|---|
| Regulated agency data (FTI, CJI, benefits, motor vehicle) | **Very low** | No risk of unauthorized access to regulated data is accepted above Low, and no breach of a Security Addendum, Exhibit 7, or DPPA term is accepted at all. Measure: risks above Low that involve unauthorized access to regulated data (8 today: R-001, R-003, R-004, R-005, R-029, R-035, R-047, R-050); target 0 above Moderate by 2027-06-30 |
| Agency operations and recovery | **Low** | Recovery must meet the contract RTO of 8 hours for every regulated tenant. Measure: every High-criticality process (P05) has a passed timed recovery test in the last 12 months (0 of 8 today) |
| Access to agency-hosted systems (managed services) | **Low** | The company will not hold standing administrator access to agency systems without vaulting, phishing-resistant MFA, and session recording. Measure: R-001 and R-050 at Moderate or lower by 2027-01-31 |
| Regulatory and contract compliance | **Low** | No High gap in P03 stays open past its POA&M date; no CJIS or IRS review finding goes uncorrected beyond the agency's deadline |
| Third parties | **Moderate**, with conditions | Vendors are used widely, but no vendor receives agency data or system access without a review scaled to its tier and contract terms, and every Tier 1 vendor is reassessed each year (P09) |
| Innovation and AI | **Moderate** | The company builds AI features for agencies, but only through the AI governance process in P10, and never so that an AI output replaces a decision that law gives to government staff |
| Financial loss from cyber events | **Moderate** | Single-event losses up to the $500,000 insurance retention are tolerable. Scenarios above $3 million need a treatment that reduces likelihood, not only insurance |

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the Public Administration overlay, CISA advisories on ransomware through remote management tools, the BIA, interviews with every process owner, the gap analysis (P03), and the control assessment (P07).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood of adverse impact were each rated, then combined with **Table G-5**.
3. **Rate impact.** Impact used **Table H-3**, anchored to the BIA impact categories (cost, operations, regulatory, safety, reputation), including impact on agencies and individuals.
4. **Determine risk.** Risk level came from **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the two tables, not assigned by hand.
5. **Semi-quantitative view.** `semi_quant_score` gives each risk level its SP 800-30 Appendix I semi-quantitative value (Very High 10, High 8, Moderate 5, Low 2, Very Low 0). `exposure_estimate_usd` gives an order-of-magnitude single-event loss range from the BIA values and contract values, used for the enterprise risk roll-up (NIST IR 8286 Rev. 1). The ranges are estimates for prioritizing, not actuarial figures.
6. **Registers.** `register_scope` tags each risk to the enterprise level and to one or more system-level registers (section 5).

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 2 |
| High | 6 |
| Moderate | 29 |
| Low | 15 |
| Very Low | 0 |
| **Total** | **52** |

Treatments: 49 Mitigate, 3 Accept (R-023, R-024, R-025). Status: 34 Open, 15 In progress, 3 Accepted.

Cyber insurance ($15 million limit, $500,000 retention) transfers part of the financial exposure for R-001, R-002, R-003, and R-050. It is not recorded as the treatment for any risk, because it does not lower the likelihood of harm to agencies or the people in their records.

### Top risks (Very High and High)
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware pushed through the remote management platform to agency-hosted servers (including AG-02 CJI systems) and into the company | Very High | Vault and rotate agency credentials; phishing-resistant keys; session recording and SIEM onboarding for SYS-10; remove the jump path into the landing zone | Director of Managed Services | 2027-01-31 |
| R-050 | SYS-10 automation API token in a wiki readable by 212 staff (found in P07) | Very High | Token revoked 2026-08-19; scoped tokens in the secrets manager; wiki secrets scan; log review for prior use | Director of Managed Services | 2026-10-31 |
| R-002 | Ransomware or destruction in ACMC production | High | Contingency plan rewrite; document storage in the vault; timed restores; region B failover | Director of Cloud Operations | 2027-06-30 |
| R-003 | Theft of regulated data for extortion | High | Egress allow-list; export alerts; application audit events to the SIEM | Security Operations Manager | 2027-01-31 |
| R-004 | CJIS or IRS review finds unscreened staff with access | High | Remove access for the 18 staff until screened; screening gate | HR Director | 2026-10-31 |
| R-006 | Recovery exceeds the 8-hour contract RTO | High | Parallel restore design; timed restores; rebuild runbook | Director of Cloud Operations | 2027-03-31 |
| R-008 | Managed services engineer account takeover through MFA fatigue | High | Phishing-resistant keys for all staff with access to agency systems or regulated data | Director of Information Security | 2027-01-31 |
| R-013 | Remote management platform vendor compromise | High | Vendor review; restrict agent rights; central kill switch | Director of Managed Services | 2027-03-31 |

**Themes.**
- **The managed services line is the largest exposure (R-001, R-008, R-013, R-028, R-038, R-050).** The ACMC landing zone is well separated, but the remote management platform holds the keys to 9 agencies' servers with weaker controls than the cloud. It also bridges into the landing zone. P07 confirmed the theme with the exposed automation token.
- **Regulated data access has outgrown its checks (R-004, R-005, R-029, R-035, R-042, R-047).** Screening, access reviews, and misuse detection were built for a smaller company and have not kept up with hiring and new customers.
- **Recovery is isolated but slow (R-002, R-006, R-014).** The write-once vault means data survives an attack, but the contract recovery times are not met.
- **AI and new states (R-009 to R-011, R-051).** The eligibility assistant is in production without monitoring, and the Colorado contract adds a state AI law from 2027.

## 4. Treatment summary
**Funded in the FY2027 security plan (approved by the CEO 2026-09-17, $955,000 one-time and $455,000 a year):**
- Managed services privileged access: credential vault and session recording for SYS-10, phishing-resistant keys for about 250 staff ($210,000 one-time, $85,000 a year)
- Application audit analytics and MDR scope expansion to SYS-10 and the regulated tenants ($160,000 a year)
- Recovery program: scripted region B build, document storage in the vault, timed restore tests ($240,000 one-time, $60,000 a year)
- FIPS 140-3 certified modules on the message-switch connectors ($45,000)
- Vendor risk tooling and one GRC analyst position ($150,000 a year)
- SOC 2 Type 2 examination and GovRAMP Authorized assessment ($310,000 across 2027)
- AI governance: bias testing, monitoring, and Colorado developer documentation ($120,000)
- Screening fees and Personnel Security Coordinator time ($30,000)

Each funded item maps to a P07 POA&M entry.

**Accepted (3):** R-023 (Low, laptop encryption), R-024 (Low, remote work covers loss of an office), and R-025 (Low, provider DDoS protection). All were accepted by the Chief Operating Officer on 2026-09-17, which is above the minimum authority for Low risks, and will be reviewed by 2027-09-17.

**Agency disclosures:** the FTI copied to the analytics service (R-035; P03 PB-09) goes to the AG-01 disclosure officer by 2026-09-30, so AG-01 can decide on its own reporting under Pub. 1075 section 1.8.

## 5. Enterprise and system-level registers
This file is the **enterprise register**. Following NIST IR 8286 Rev. 1, it rolls up to the company's enterprise risk register as one line, "Cybersecurity, regulated data, and service resilience", owned by the Chief Operating Officer and reported to the audit committee each quarter with the counts above and the top risks.

System-level registers are filtered views of this file (column `register_scope`), kept by each system owner, rather than separate spreadsheets. That keeps one set of ratings. A risk can sit in more than one view.

| Register | Owner | Risks in scope |
|---|---|---|
| Enterprise (cross-cutting risks) | Chief Operating Officer | 18 risks tagged Enterprise, including R-001 to R-005, R-012, R-018, R-020, and R-021 |
| Agency Case Management Cloud (ACMC; SSP in P02) | Chief Technology Officer | 25 risks tagged ACMC |
| Managed services (SYS-10 and agency-hosted systems) | Director of Managed Services | 7 risks: R-001, R-008, R-013, R-028, R-038, R-050, R-051 |
| AI portfolio (P10) | Director of Data and AI | 7 risks: R-009, R-010, R-011, R-031, R-032, R-033, R-034 |

When a system-level review changes a rating, the owner updates this file, and the change flows to the enterprise roll-up.

## 6. Approval
- Chief Operating Officer: approved Moderate and Low treatments and the acceptance of R-023, R-024, and R-025, 2026-09-17.
- Chief Executive Officer: approved the Very High and High treatment plans, the risk appetite statements, and the FY2027 security budget, 2026-09-17.
- Board audit committee: received the results on 2026-09-17. Next report: 2026-12 quarterly meeting.
- Next full risk assessment: July 2027, or sooner after a major change (for example the planned acquisition, R-043), a significant incident, or a new CJISSECPOL version.
