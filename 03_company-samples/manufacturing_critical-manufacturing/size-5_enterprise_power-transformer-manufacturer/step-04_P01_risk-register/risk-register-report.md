# Enterprise Risk Register Report: Cris Santos Company | Critical Manufacturing | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded power and distribution transformer manufacturer: 7 plants in FL, GA, TN, TX, NC, and OH; 9 service centers; 3 spare yards; 2 colocation data centers) |
| Size tier | Enterprise (12,000 employees) |
| Vertical | Critical Manufacturing |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) for each risk, with OT threat sources and predisposing conditions from NIST SP 800-82 Rev. 3 Appendix C; NIST IR 8286 Rev. 1 for integration into enterprise risk management (ERM) |
| Also satisfies | Input to the Reg S-K Item 106 description of risk management processes (17 CFR 229.106(b)); the risk analysis step of the CSF 2.0 profile (P03 G-042, G-043) |
| Prepared | 2026-06-01 to 2026-07-31 by the GRC team for the CISO; updated 2026-08-28 with Internal Audit findings (P07) |
| Approved | Executive risk committee (chaired by the Chief Risk Officer), 2026-09-08; reviewed by the risk committee of the board, 2026-09-10 |

## 1. Scope and risk framing
**Scope.** All systems that support tier-1 processes across the 7 plants, the 9 service centers, the 3 spare yards, the two cloud estates and two colocation data centers, the acquired Ohio plant (AQ-01), the products and services supplied to utilities (TMU firmware, FMS, STRS), and the roughly 2,400 suppliers (410 with system access or data). Business processes and impact values come from the enterprise BIA (P05). The EPSP is also covered at system level in the SSP (P02).

**Three lines.** Risk owners in the business, IT, and manufacturing (first line) own and treat risks. The GRC team and the Chief Risk Officer (second line) run this method and roll risks up into the enterprise risk register. Internal Audit (third line) tests controls independently (P07).

**Risk appetite (board-approved, 2026-02).** Qualitative statements set by the board:
- **Worker safety and product integrity:** very low appetite for technology-related harm to workers or for shipping a transformer whose design, build, or test data cannot be trusted.
- **Regulatory, contractual, and disclosure obligations:** very low appetite for missing an SEC, federal contract, export, DOE, or utility addendum obligation.
- **Security of products and services supplied to utilities:** low appetite, because the company's customers operate the grid.
- **Production and delivery continuity:** low appetite for disruption of grid equipment production, especially storm-restoration units.
- **Intellectual property:** low appetite for loss of designs and customer drawings.
- **Growth and innovation (acquisitions, AI, new services):** moderate appetite, provided risks are identified and funded at the time of the decision.

**Risk tolerance (measurable, per enterprise risk).** The highest residual risk level each enterprise risk may carry without a board-reported treatment plan. A risk above its threshold is **Outside tolerance** in the register.

| Enterprise risk | Tolerance threshold |
|---|---|
| ER-01 Production and delivery disruption from cyber and technology events | Moderate |
| ER-02 Compromise of intellectual property and sensitive data | Moderate |
| ER-03 Third-party and supply chain concentration | Moderate |
| ER-04 Integration of acquired operations | Moderate |
| ER-05 Security of products and services supplied to utilities (TMU, FMS, STRS) | Low |
| ER-06 Regulatory, contractual, financial reporting, and disclosure compliance | Low |
| ER-07 OT process safety and product integrity | Low |
| ER-08 Responsible use of AI | Moderate |

**Who can accept risk:**
| Residual level | Acceptance authority |
|---|---|
| Very Low, Low | Risk owner (vice president or director) with GRC concurrence |
| Moderate | CISO with the accountable executive |
| High | Executive risk committee (Chief Risk Officer, CIO, COO, CISO, General Counsel), reported to the board risk committee |
| Very High | CEO and CFO jointly, reported to the board risk committee at its next meeting |

Process safety risks (ER-07) at High or above cannot be accepted without a dated treatment plan. Any acceptance expires after 12 months.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E and SP 800-82 Rev. 3 Appendix C, the critical manufacturing threat picture (ransomware that reaches plant floors, supplier compromise, theft of designs), the BIA (P05), the gap analysis (P03), and the Internal Audit assessment (P07).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial), and likelihood of adverse impact, combined with **Table G-5**.
3. **Rate impact.** **Table H-3**, calibrated to the BIA impact values (P05 section 3).
4. **Determine risk.** **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the tables, not assigned by hand.
5. **Integrate with ERM (NIST IR 8286 Rev. 1).**
   - Each cybersecurity risk is a row in this register, with an owner, a treatment, and a key risk indicator (KRI).
   - Each row is normalized into one of **8 enterprise risks (ER-01 to ER-08)** in the Chief Risk Officer's enterprise risk register, with an ERM category.
   - **Aggregation rule:** an enterprise risk's exposure equals its highest constituent risk level, and the profile also reports how many constituent risks sit outside tolerance. This keeps one severe risk from being averaged away.
   - The enterprise risk profile (section 4) is what the board risk committee sees each quarter.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 12 |
| Moderate | 34 |
| Low | 19 |
| **Total** | **66** |

By threat source type: Adversarial 35, Accidental 17, Structural 13, Environmental 1.
By treatment: Mitigate 54, Accept 10, Avoid 2.
By status: In progress 50, Open 4, Closed (accepted) 10, Closed (avoided) 2.
**25 risks are outside tolerance** and each has a dated treatment plan. Five risks were added or re-rated after the Internal Audit fieldwork (R-008, R-009, R-027, R-028, R-032; last reviewed 2026-08-28).

## 4. Enterprise risk profile (roll-up for the board)
| ID | Enterprise risk | ERM category | Risks | Very High | High | Moderate | Low | Exposure (highest) | Tolerance | Outside tolerance |
|---|---|---|---|---|---|---|---|---|---|---|
| ER-01 | Production and delivery disruption from cyber and technology events | Operational | 16 | 1 | 4 | 9 | 2 | **Very High** | Moderate | 5 |
| ER-02 | Compromise of intellectual property and sensitive data | Strategic and compliance | 8 | 0 | 0 | 5 | 3 | **Moderate** | Moderate | 0 |
| ER-03 | Third-party and supply chain concentration | Operational | 5 | 0 | 1 | 3 | 1 | **High** | Moderate | 1 |
| ER-04 | Integration of acquired operations | Strategic | 4 | 0 | 1 | 2 | 1 | **High** | Moderate | 1 |
| ER-05 | Security of products and services supplied to utilities (TMU, FMS, STRS) | Strategic | 8 | 0 | 1 | 5 | 2 | **High** | Low | 6 |
| ER-06 | Regulatory, contractual, financial reporting, and disclosure compliance | Compliance | 13 | 0 | 2 | 4 | 7 | **High** | Low | 6 |
| ER-07 | OT process safety and product integrity | Operational (safety) | 7 | 0 | 2 | 3 | 2 | **High** | Low | 5 |
| ER-08 | Responsible use of AI | Strategic | 5 | 0 | 1 | 3 | 1 | **High** | Moderate | 1 |

**Reading the profile:**
- **ER-01 (production disruption)** carries the only Very High risk: ransomware that reaches plant OT at several plants (R-001). Unproven recovery (R-005, R-031) and the AQ-01 pathway (R-003, ER-04) are the main reasons its likelihood and impact are not lower.
- **ER-05 (products and services for utilities)** has the lowest tolerance and the most risks outside it: tampered TMU firmware (R-010), misuse of the code signing key (R-013), FMS compromise and analytics misses (R-014, R-046), STRS dispatch failure (R-015), and sabotage of spare units (R-041).
- **ER-06 (compliance)** is outside tolerance mainly because utility addendum deadlines have been missed (R-011, R-012) and the SEC materiality process cannot yet quantify a production outage (R-016).
- **ER-07 (process safety)** carries two High risks found or confirmed in testing: the AQ-01 cellular routers (R-007) and OEM default passwords on drying oven HMIs (R-009).
- **ER-08 (AI)** has one High risk: extending drying oven maintenance intervals on AI-002 advice (R-043). The committee refused the change until the model is validated as a High-tier use case (P10).

## 5. Top risks (Very High and High)
| Risk ID | Risk | Level | Enterprise risk | Treatment | Owner | Due |
|---|---|---|---|---|---|---|
| R-001 | Ransomware encrypts IT systems and spreads into plant OT at several plants, stopping production of grid equipment | Very High | ER-01 | Close AQ-01 paths (POAM-004); prove ERP RTO (POAM-006); controller restores at every plant (POAM-007); 24x7 OT alert routing (POAM-005); ransomware exercise with the disclosure committee (POAM-011) | CISO | 2027-03-31 |
| R-002 | Ransomware operator with stolen cloud administrator rights encrypts the ERP and APS and tries to delete backups | High | ER-01 | Automate failover and restore (POAM-006); quarterly restore test from the offline copy | Vice President, Enterprise Applications | 2027-01-31 |
| R-003 | Attacker enters through AQ-01 and reaches the corporate domain and P1 to P6 | High | ER-04 | Remove the trust and federate identities (POAM-001); OT DMZ and gateway (POAM-004; POAM-008); OT sensor (POAM-015) | Vice President, Integration Management Office | 2027-03-31 |
| R-006 | Unsupported HMI, engineering workstation, or MES kiosk operating system exploited | High | ER-01 | Compensating controls for every unsupported asset; funded refresh; P3 kiosks (POAM-009) | Vice President, Manufacturing Engineering | 2027-06-30 |
| R-007 | AQ-01 OEM cellular router used to change drying oven or impregnation parameters | High | ER-07 | Remove routers; extend the OT gateway (POAM-008) | Director of OT Security | 2027-03-31 |
| R-009 | OEM default password on drying oven HMI web pages used to change setpoints (P07 finding) | High | ER-07 | Change passwords with the OEM; commissioning check (POAM-012) | Vice President, Manufacturing Engineering | 2026-10-31 |
| R-010 | Tampered TMU firmware ships to utilities | High | ER-05 | Assess the contract manufacturer (POAM-018); verify boot images; SBOM for every release (POAM-019) | Chief Technology Officer | 2027-03-31 |
| R-011 | A utility addendum deadline is missed | High | ER-06 | Per-utility clocks and templates (POAM-016); disclosure tracker (POAM-019) | Chief Compliance Officer | 2026-12-31 |
| R-016 | A material incident is disclosed late or inaccurately | High | ER-06 | Production-loss method; OT ransomware tabletop 2026-11-18 (POAM-011) | General Counsel | 2026-11-30 |
| R-025 | Malicious code in a trusted IT software vendor update | High | ER-03 | Staged rollout for all tier-1 software; SBOM requests | CIO | 2027-06-30 |
| R-031 | Controller programs cannot be restored at a plant that never tested an OT restore | High | ER-01 | Restore tests at every plant; automated AQ-01 backups (POAM-007) | Vice President, Manufacturing Engineering | 2027-06-30 |
| R-043 | Drying oven maintenance intervals extended on AI-002 advice | High | ER-08 | Change refused until validated as High tier (P10) | Maintenance Director (corporate) | 2027-03-31 |
| R-048 | Zero-day in an internet-facing edge device | High | ER-01 | Retire the AQ-01 legacy VPN; reduce exposed services | Director of Network Engineering | 2027-03-31 |

## 6. Themes from the 2026 analysis
1. **The plant floor is where impact concentrates (ER-01, ER-07).** P1 to P6 have OT DMZs, monitoring, and a gateway, but recovery is unproven at most plants (R-031), 148 HMIs and engineering workstations are unsupported (R-006), OT alerts wait for business hours (R-030), and testing found default passwords and an unapproved OEM remote tool (R-008, R-009).
2. **AQ-01 is the soft entry point (ER-04).** The acquired plant combines a flat OT network, a dual-homed MES, a two-way domain trust, cellular routers, and no monitoring (R-003, R-004, R-007). Integration milestones run to 2027-06-30. Future deals must fund integration up front (R-061).
3. **Customers' grid risk is the company's risk (ER-05, ER-06).** The 88 addenda make the company answerable for incident notices, access revocation, vulnerability disclosure, and firmware integrity. Three access notices and one disclosure were late in 2026 (R-011, R-012), and the contract manufacturer has never been assessed (R-010, R-023).
4. **Recovery time, not backups, is the ERP gap (ER-01).** Backups are immutable and met the RPO, but the failover took 11 hours (R-005).
5. **Disclosure readiness for an OT event (ER-06).** The materiality process has never been run on a production outage; the 2026-11-18 tabletop will use the P05 values (R-016).
6. **AI is being adopted faster than it is reviewed (ER-08).** 5 of 14 use cases lack review; one vendor feature was switched on without review and has been disabled (R-044, treatment Avoid).

## 7. Treatment summary
- **Funded (2026 Q4 to 2027 Q2), about $6.3 million:** AQ-01 OT DMZ ($1.6M) and identity federation ($0.9M), OT refresh wave 1 ($2.4M), ERP standby capacity ($240K a year, plus staff time for automation), SIEM licensing for new sources ($180K), ERP vendor services for change workflow ($120K), contract manufacturer and Tier 2 assessments ($150K), P3 kiosk replacement ($150K), spare yard monitoring ($210K), AQ-01 OT sensor ($85K), OT training ($60K), AQ-01 OT backup server ($60K), bias testing for AI use cases ($50K), gateway licenses ($45K), outside counsel for the disclosure tabletop ($40K), and OEM visits for HMI passwords ($18K). Items map to the POA&M in P07.
- **Accepted (10):** R-021, R-035, R-050, R-051, R-052, R-057, R-058, R-059, R-063, R-065. Each is Low or Moderate residual with strong existing controls, accepted at the right level (section 1), and reviewed within 12 months.
- **Avoided (2):** R-020 and R-044. Unapproved generative AI tools are blocked, and the applicant screening feature is disabled until review.
- **Very High risk R-001:** not accepted as is. The CEO and CFO approved the treatment plan and the residual target of High on 2026-09-08; the board risk committee reviewed it on 2026-09-10.

## 8. Board reporting
**Risk committee of the board (quarterly):** the enterprise risk profile (section 4), every Very High and High risk with its treatment status and KRI trend, risks outside tolerance, new risks since the last meeting, and risk acceptances made. The 2026-09-10 meeting received this report, the Internal Audit results (P07), and the regulatory roadmap (P03).
**Audit committee (quarterly):** Internal Audit results, SOX IT general control status for the ERP (R-027), and disclosure controls topics (R-016, R-064). The audit committee also reviews the annual Item 106 disclosure draft, which describes this process.
**Management:** the executive risk committee meets monthly and reviews KRIs for all risks outside tolerance.

## 9. Approval
- Executive risk committee: approved the register, treatments, and acceptances, 2026-09-08.
- CEO and CFO: approved the treatment plan and residual target for Very High risk R-001, 2026-09-08.
- Risk committee of the board: reviewed the enterprise risk profile, 2026-09-10.
- Next full review: June to July 2027, or sooner after a major change, incident, or acquisition. KRIs are refreshed quarterly.
