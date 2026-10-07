# Risk Register Report: Cris Santos Company | Defense Industrial Base | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed aircraft parts manufacturer, DoD subcontractor) |
| Size tier | Mid-Market (850 employees) |
| Vertical | Defense Industrial Base |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2, and the Appendix I semi-quantitative values); enterprise roll-up per NIST IR 8286 Rev. 1 |
| Also satisfies | SP 800-171 Rev. 2 requirement 3.11.1 (periodic risk assessment), CMMC RA.L2-3.11.1 |
| Prepared | 2026-07-31 by the Security Manager and the GRC analyst with the vCISO; R-050 added 2026-08-14 from P07 testing |
| Approved | 2026-09-17: Chief Operating Officer (Moderate and below), Chief Executive Officer (High and Very High, risk appetite, budget); presented to the board audit committee the same day |

## 1. Scope and risk framing
**Scope.** Both plants, the services line, and enterprise functions; the CUI Engineering Enclave (CEE, SSP in P02); the systems outside the enclave that could affect it or the company's defense contracts (corporate network, ERP, payroll and HR, the MSSP, suppliers that receive CUI); and the AI portfolio (P10). Processes and impact values come from the BIA (P05); vulnerabilities come from the gap analysis (P03) and the control assessment (P07). See `../00_company-facts.md` sections 3 and 4.

**Who can accept risk (tolerance).**
| Risk level | Who may accept | Conditions |
|---|---|---|
| Very Low and Low | The risk owner (director level or above) | Recorded in the register; reviewed annually |
| Moderate | Chief Operating Officer | Treatment plan or documented reason; reviewed every 6 months |
| High | Chief Executive Officer | Temporary only (up to 12 months) with a dated treatment plan; reported to the audit committee each quarter |
| Very High | Not acceptable | The CEO may approve a temporary exception of up to 90 days only after notifying the audit committee chair, while treatment is under way |
| Never acceptable | Not acceptable at any level | A known failure to meet a DFARS 252.204-7012 duty (adequate security, reporting, preservation, flowdown), an unauthorized ITAR release, or an SPRS affirmation not supported by evidence. These are treated, not accepted |

### Risk appetite statements
Approved by the Chief Executive Officer and noted by the audit committee on 2026-09-17.

| Area | Appetite | Statement and measure |
|---|---|---|
| Defense contract eligibility | **Very low** | The company will hold CMMC Level 2 (C3PAO) status before the first prime award that requires it. All 110 requirements are to be Met before the C3PAO assessment; a CMMC POA&M is a fallback for 1-point items only. Measure: recalculated score (today -44; target 110 by 2027-02-26) and R-001 and R-047 |
| Product and flight safety | **Very low** | No cyber or AI risk that could let a nonconforming flight part leave the plant is accepted above Low. Measure: safety-linked risks above Low (3 today: R-022, R-029, R-045; target 0 by 2027-06-30) |
| Confidentiality of CUI and export control | **Low** | No risk of CUI loss or unauthorized release above Moderate after 2027-03-31. Measure: R-002, R-006, and R-010 at Moderate or lower by then |
| Availability of production | **Low** | Recovery must meet the BIA RTOs for every High process (P05). Measure: each High process has a passed restore or recovery test in the last 12 months (none today) |
| Third parties and suppliers | **Moderate**, with conditions | Suppliers and service providers are used widely, but no supplier receives CUI without DFARS flowdown and a verified SPRS status, and every Tier 1 vendor is reviewed each year (P09) |
| Innovation and AI | **Moderate** | The company wants AI benefits in engineering, quality, and maintenance, but only through the P10 process. No AI tool touches CUI unless it is inside the assessed boundary |
| Financial loss from cyber events | **Moderate** | Single-event losses up to the $500,000 insurance retention are tolerable. Scenarios above $2 million need a treatment that reduces likelihood, not only insurance |

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA, interviews with every process owner and both plant managers, the plant walkthroughs, the gap analysis (P03), and the control assessment (P07). Threats from foreign intelligence services and contracted actors were included because the company holds controlled technical information for military aircraft.
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood that the event causes adverse impact were each rated, then combined with **Table G-5**.
3. **Rate impact.** Impact used **Table H-3**, anchored to the BIA impact categories (cost, operations, regulatory and contract, product safety, reputation).
4. **Determine risk.** Risk level came from **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the two tables, not assigned by hand.
5. **Semi-quantitative view.** `semi_quant_score` gives each risk level its SP 800-30 Appendix I semi-quantitative value (Very High 10, High 8, Moderate 5, Low 2, Very Low 0). `exposure_estimate_usd` gives an order-of-magnitude single-event loss range from the BIA values, used for the enterprise roll-up (NIST IR 8286 Rev. 1). The ranges are estimates for prioritizing, not actuarial figures.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 2 |
| High | 10 |
| Moderate | 27 |
| Low | 11 |
| Very Low | 0 |
| **Total** | **50** |

By threat source type: 19 Adversarial, 14 Accidental, 13 Structural, 4 Environmental. Treatments: 44 Mitigate, 3 Accept (R-024, R-035, R-041), 2 Avoid (R-031, R-032), 1 Transfer (R-038). Status: 25 Open, 22 In progress, 3 Accepted.

Cyber insurance ($15 million limit, $500,000 retention) transfers part of the financial exposure for R-002, R-004, and R-010. It is not recorded as the treatment for any of them, because it does not lower the likelihood of losing CUI, contract eligibility, or production.

### Top risks (Very High and High)
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | No CMMC Level 2 (C3PAO) status when primes flow down DFARS 252.204-7021 | Very High | P03 roadmap; readiness re-check; C3PAO assessment 2027-03 | Chief Operating Officer | 2027-03-19 |
| R-004 | Ransomware spreads across the flat Plant 2 network to MES, DNC, and backups | Very High | Plant 2 enclave firewall; close remote desktop; cloud backups; server replacement | IT Director | 2027-01-31 |
| R-002 | Session theft and exfiltration of PLM exports through the virtual desktop pool | High | Phishing-resistant authenticators; export and download alerts | Security Manager | 2027-01-31 |
| R-003 | SPRS score of 74 overstates implementation (recalculated -44) | High | Corrected score and date-to-110 | Director of Trade Compliance and Contracts | 2026-09-30 |
| R-005 | Shop-floor intrusion undetected for weeks | High | SIEM onboarding of shop-floor sources; passive OT monitoring | Security Manager | 2027-01-31 |
| R-006 | Visitor views ITAR drawings on the Plant 2 floor | High | Electronic visitor system and escort; covered racks | Facilities and Security Manager | 2026-10-31 |
| R-010 | Supplier without DFARS flowdown is breached | High | Re-paper 9 suppliers; verify all 22 | Director of Supply Chain | 2026-10-31 |
| R-011 | Plant 2 MES, DNC, and local backup destroyed together | High | Nightly encrypted cloud backups; restore test | IT Director | 2026-11-30 |
| R-013 | Unsupported or unpatched MES server exploited | High | Replace Plant 2 servers; MES patch windows; scanning | Manufacturing Systems Manager | 2027-01-31 |
| R-029 | Machine-vision model passes a defective flight assembly | High | Version lock; 10% re-inspection of passes; escape review | Director of Quality | 2026-12-31 |
| R-047 | A requirement that cannot be on a CMMC POA&M is still open at the assessment | High | Close 3.1.20, 3.10.3, 3.10.4, 3.12.4 first | Security Manager | 2026-10-31 |
| R-050 | Prior owner's contractor account active on the Plant 2 MES server (found in P07) | High | Disabled on discovery; full account review; close remote desktop | Manufacturing Systems Manager | 2026-10-31 |

**Themes.**
- **The acquisition (R-004 to R-007, R-011, R-013 to R-016, R-019, R-040, R-046, R-050).** Plant 2 came with a flat network, shared logins, unsupported servers, and a forgotten contractor account. It costs 84 points of the CMMC score on its own (P03) and drives both Very High risks. R-048 makes sure the next acquisition does not repeat it.
- **Contract eligibility (R-001, R-003, R-043, R-047).** About 62% of revenue depends on defense primes. The company's cloud enclave is mature, but it cannot yet prove the plants meet the same standard.
- **CUI leaving the company (R-002, R-006, R-010, R-017, R-026, R-027, R-030).** The most likely paths are session theft, visitors at Plant 2, suppliers without flowdown, and AI tools that sit outside the boundary.
- **AI adopted without review (R-026 to R-032).** Five tools went live or were enabled without a security review. P10 addresses them; R-029 is a flight safety risk, not only a security risk.

## 4. Treatment summary
**Funded in the FY2027 security plan (approved by the CEO 2026-09-17: $1.62 million one-time and $540,000 a year):**
- Plant 2 enclave firewall, shop-floor VLANs, scanner wireless, and cellular backup ($260,000) (R-004, R-025, R-040)
- Plant 2 MES and DNC replacement with named sign-in through SYS-01 ($420,000) (R-013, R-014)
- DNC serial gateway for 8 legacy CNC machines ($90,000) (R-015)
- SIEM onboarding of shop-floor sources and passive OT monitoring ($150,000 one-time, $180,000 a year) (R-005, R-045)
- MDR coverage extension to Plant 2 ($90,000 a year) (R-004)
- Phishing-resistant authenticators for 290 enclave users ($45,000) (R-002)
- Vulnerability scanning of MES and Plant 2 ($40,000 a year) (R-013)
- OT DMZ for the predictive maintenance gateway and access broker extension for vendors ($70,000 one-time, $50,000 a year) (R-016, R-026)
- Contingency plan and restore testing program ($150,000) (R-011, R-012)
- Visitor management system and shred bins at Plant 2 ($30,000) (R-006, R-019)
- Supplier flowdown and verification, including legal review ($35,000) (R-010, R-043)
- C3PAO assessment and readiness re-check ($160,000) (R-001)
- SOC 2 readiness and Type 2 examination ($210,000 across 2027) (R-036)
- Second GRC analyst ($120,000 a year), forensic OT imaging retainer ($20,000 a year), and AI program monitoring ($40,000 a year) (R-009, R-027 to R-029)

Each funded item maps to a P07 POA&M entry.

**Accepted (3, all Low):** R-024 (cloud regional outage; backups in a second region), R-035 (services outage; service credits capped), R-041 (lost laptop; encrypted). Risk owners accepted them and the COO confirmed on 2026-09-17.

**Avoided (2):** R-031 (applicant ranking feature disabled on 2026-09-17) and R-032 (public chatbots prohibited). **Transferred (1):** R-038 (hurricane: insurance plus preparation steps).

**Contract actions:** DFARS 252.204-7012 and 252.204-7020 flowdown to 9 suppliers (R-010) by 2026-10-31; DFARS 252.204-7021 in purchase order templates before 2026-11-10 (R-043); vendor security terms for the additive printer and predictive maintenance vendors (R-016, R-026).

## 5. Enterprise and system-level registers
This file is the **enterprise register**. Following NIST IR 8286 Rev. 1, it rolls up to the company's enterprise risk register as two lines owned by the COO and reported to the audit committee each quarter: "Defense contract eligibility (CMMC and DFARS)" and "Cybersecurity and production resilience", with the counts above and the top risks.

System-level registers are filtered views of this file, kept by each owner, rather than separate spreadsheets. That keeps one set of ratings.

| System-level register | Owner | Risks in scope |
|---|---|---|
| CUI Engineering Enclave (SSP in P02) | Security Manager | 28 risks whose affected assets include SYS-01 to SYS-08, SYS-12, or SYS-13 (filter the `affected_asset_or_process` column) |
| Plant 2 integration | IT Director with the Plant 2 Manager | 15 risks: R-004, R-005, R-006, R-007, R-011, R-013, R-014, R-015, R-016, R-019, R-025, R-039, R-040, R-046, R-050 |
| AI portfolio (P10) | Director of Engineering with the vCISO | R-026 to R-032 |
| Additive and engineering services (SOC 2 scope, P09) | Director of Additive and Engineering Services | R-034, R-035, R-036 |

When a system-level review changes a rating, the owner updates this file, and the change flows to the enterprise roll-up.

## 6. Approval
- Chief Operating Officer: approved Moderate and Low treatments and confirmed the 3 Low acceptances, 2026-09-17.
- Chief Executive Officer (CMMC Affirming Official): approved the Very High and High treatment plans, the risk appetite statements, and the FY2027 security budget, 2026-09-17. No High or Very High risk was accepted.
- Board audit committee: received the results on 2026-09-17. Next report: 2026-12 quarterly meeting.
- Next full risk assessment: July 2027, or sooner after a major change (an acquisition, R-048), a significant incident, or the C3PAO assessment.
