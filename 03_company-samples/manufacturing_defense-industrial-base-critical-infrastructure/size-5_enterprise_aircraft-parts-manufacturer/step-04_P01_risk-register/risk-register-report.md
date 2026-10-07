# Enterprise Risk Register Report: Cris Santos Company | Defense Industrial Base | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded tier-1 aerostructures and aircraft components manufacturer; 8 sites in 6 states) |
| Size tier | Enterprise (12,000 employees) |
| Vertical | Defense Industrial Base |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) for each risk; NIST IR 8286 Rev. 1 for integration into enterprise risk management (ERM) |
| Also satisfies | SP 800-171 Rev. 2 requirement 3.11.1 (CMMC RA.L2-3.11.1); threat-informed risk assessment for CMMC Level 3 (RA.L3-3.11.1e); input to the Regulation S-K Item 106 description of risk management processes |
| Prepared | 2026-06-01 to 2026-07-31 by the GRC team for the CISO; updated 2026-08-28 with Internal Audit findings (P07) |
| Approved | Executive risk committee (chaired by the Chief Risk Officer), 2026-09-08; reviewed by the risk and technology committee of the board, 2026-09-10 |

## 1. Scope and risk framing
**Scope.** The CUI Engineering Enclave (P02) and the Manufacturing Operations Zone, the 8 sites and 2 data centers, the commercial cloud service lines, the KS-1 legacy environment, the classified program at FL-1 (reporting duties only), and the supply chain of about 1,400 suppliers (380 with CUI). Business processes and impact values come from the enterprise BIA (P05).

**Three lines.** Risk owners in the business and IT (first line) own and treat risks. The GRC team, the CMMC Program Office, and the Chief Risk Officer (second line) run this method and roll risks up into the enterprise risk register. Internal Audit (third line) tests controls independently (P07).

**Risk appetite (board-approved, 2026-02).**
- **CUI and export-controlled data:** very low appetite for unauthorized disclosure or release.
- **Defense contract eligibility:** very low appetite for any lapse in CMMC status, SPRS accuracy, or DFARS compliance.
- **Product integrity and flight safety:** very low appetite for technology-related nonconformance.
- **Regulatory and disclosure:** very low appetite for noncompliance with ITAR, EAR, NISPOM, or SEC disclosure rules.
- **Production continuity:** low appetite for disruption of plants and deliveries.
- **Growth and innovation (acquisitions, new sites, AI):** moderate appetite, provided risks are identified and funded before or at the time of the decision.

**Risk tolerance (measurable, per enterprise risk).** The highest residual risk level each enterprise risk may carry without a board-reported treatment plan. A risk above its threshold is **Outside tolerance** in the register.

| Enterprise risk | Tolerance threshold |
|---|---|
| ER-01 CUI and export-controlled data compromise | Low |
| ER-02 Defense contract eligibility (CMMC, SPRS, DFARS) | Low |
| ER-03 Production and delivery disruption from cyber and technology events | Moderate |
| ER-04 Supply chain and third-party cyber risk | Moderate |
| ER-05 Product integrity and flight safety from technology | Low |
| ER-06 Integration of acquired and new sites | Moderate |
| ER-07 Regulatory, export, security clearance, and disclosure compliance | Low |
| ER-08 Responsible use of AI | Moderate |

**Who can accept risk:**
| Residual level | Acceptance authority |
|---|---|
| Very Low, Low | Risk owner (vice president or director) with GRC concurrence |
| Moderate | CISO with the accountable executive |
| High | Executive risk committee (Chief Risk Officer, COO, CIO, CISO, General Counsel), reported to the risk and technology committee |
| Very High | CEO and CFO jointly, reported to the risk and technology committee at its next meeting |

**Never accepted, at any level:** a known failure to meet a DFARS 252.204-7012 duty (adequate security, reporting, flowdown), processing CUI for a contract that requires a CMMC status on a system without that status, an affirmation the company cannot support, or an unauthorized export. These are treated, not accepted. Any acceptance expires after 12 months.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, threat intelligence on campaigns against aerospace suppliers (DoD, prime, and commercial sources), the BIA (P05), the gap analysis (P03), and the Internal Audit assessment (P07).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial), and likelihood of adverse impact, combined with **Table G-5**.
3. **Rate impact.** **Table H-3**, calibrated to the BIA impact values (P05 section 3), including flight safety, export control, and contract eligibility harm.
4. **Determine risk.** **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the tables, not assigned by hand.
5. **Integrate with ERM (NIST IR 8286 Rev. 1).**
   - Each cybersecurity risk is a row in this register, with an owner, a treatment, and a key risk indicator (KRI).
   - Each row is normalized into one of **8 enterprise risks (ER-01 to ER-08)** in the Chief Risk Officer's enterprise risk register, with an ERM category.
   - **Aggregation rule:** an enterprise risk's exposure equals its highest constituent risk level, and the profile also reports how many constituent risks sit outside tolerance, so one severe risk is never averaged away.
   - The enterprise risk profile (section 4) is what the board committee sees each quarter.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 12 |
| Moderate | 31 |
| Low | 20 |
| Very Low | 0 |
| **Total** | **64** |

By threat source type: Adversarial 17, Structural 30, Accidental 15, Environmental 2.
By treatment: Mitigate 50, Accept 12, Avoid 1, Share/Transfer 1.
By status: In progress 47, Open 4, Closed (accepted) 12, Closed (avoided) 1.
**27 risks are outside tolerance** and each has a dated treatment plan.

## 4. Enterprise risk profile (roll-up for the board)
| ID | Enterprise risk | ERM category | Risks | Very High | High | Moderate | Low | Exposure (highest) | Tolerance | Outside tolerance |
|---|---|---|---|---|---|---|---|---|---|---|
| ER-01 | CUI and export-controlled data compromise | Compliance and national security | 12 | 1 | 2 | 7 | 2 | **Very High** | Low | 10 |
| ER-02 | Defense contract eligibility (CMMC, SPRS, DFARS) | Strategic | 8 | 0 | 3 | 4 | 1 | **High** | Low | 7 |
| ER-03 | Production and delivery disruption from cyber and technology events | Operational | 7 | 0 | 1 | 2 | 4 | **High** | Moderate | 1 |
| ER-04 | Supply chain and third-party cyber risk | Operational | 10 | 0 | 2 | 5 | 3 | **High** | Moderate | 2 |
| ER-05 | Product integrity and flight safety from technology | Safety | 4 | 0 | 1 | 2 | 1 | **High** | Low | 3 |
| ER-06 | Integration of acquired and new sites | Strategic | 6 | 0 | 2 | 4 | 0 | **High** | Moderate | 2 |
| ER-07 | Regulatory, export, security clearance, and disclosure compliance | Compliance | 10 | 0 | 1 | 1 | 8 | **High** | Low | 2 |
| ER-08 | Responsible use of AI | Strategic | 7 | 0 | 0 | 6 | 1 | **Moderate** | Moderate | 0 |

**Reading the profile:**
- **ER-01 (CUI compromise)** carries the only Very High risk: exploitation of the internet-facing managed file transfer service by a state-sponsored actor (R-001). It is also the P08 scenario. The insider (R-003) and export attribute (R-004) risks keep the exposure High even after R-001 is treated.
- **ER-02 (contract eligibility)** is the board's main concern this year. The annual affirmation (R-013) and the Program H Level 3 requirement (R-014) depend on the same remediation work, and one work order for a contract with DFARS 252.204-7021 was routed to KS-1 (R-015).
- **ER-06 (integration)** is where the technical debt sits: KS-1 (R-022, R-046) and AZ-1 (R-047).
- **ER-08 (AI)** is within tolerance today because the AI-001 assistant is in a controlled pilot; expansion depends on the conditions in P10.

## 5. Top risks (Very High and High)
| Risk ID | Risk | Level | Enterprise risk | Treatment | Owner | Due |
|---|---|---|---|---|---|---|
| R-001 | A state-sponsored actor exploits a zero-day in the managed file transfer software and exfiltrates CUI program data from the CEE gateway (and corporate files from the separate instance) | Very High | ER-01 | Purge staging after 72 hours; virtual patching rules at the web application firewall; vendor notification clause; P08 runbook tabletop with the disclosure committee (POAM-019); egress anomaly model for the gateway | CISO | 2027-01-31 |
| R-003 | A departing engineer copies CUI to personal storage or offers it to a competitor or foreign buyer | High | ER-01 | Insider risk program for all CEE users with HR triggers (POAM-022); departure watch lists | Corporate Facility Security Officer | 2027-03-31 |
| R-004 | An EAR-licensed foreign-person engineer views ITAR technical data because PLM folders lack export attributes | High | ER-01 | Attribute check on every migration; weekly attribute analytics; recertify all foreign-person access; voluntary disclosure handled by the Senior Empowered Official (POAM-002) | Vice President, Trade Compliance | 2026-11-30 |
| R-013 | The annual CMMC affirmation (due 2027-03-20) cannot truthfully be made because requirements are no longer MET in the certified sites | High | ER-02 | Close all certified-site gaps by 2027-02-28; readiness re-check before the affirmation | Chief Operating Officer | 2027-02-28 |
| R-014 | The company cannot reach Level 3 (DIBCAC) status in time for the Program H solicitation | High | ER-02 | Scope decision 2026-12-15; readiness program (POAM-021); Level 2 assessment of the expanded scope 2027-05; DIBCAC request 2027-06 | Director, CMMC Program Office | 2027-08-13 |
| R-015 | Work on a contract that includes DFARS 252.204-7021 is performed on KS-1 systems that have no CMMC status | High | ER-02 | Hard block in ERP and MES routing; contract review with the Vice President, Contracts; accelerate KS-1 migration (POAM-020) | Vice President, Contracts | 2026-10-31 |
| R-021 | Ransomware spreads from corporate IT into the MOZ and stops MES and DNC at several plants | High | ER-03 | Close AZ-1 and KS-1 segmentation gaps (POAM-005; POAM-020); annual OT recovery exercise | Director of OT Engineering | 2027-03-31 |
| R-022 | Ransomware encrypts the KS-1 legacy file server, MES, and their local backups | High | ER-06 | Daily offsite backups for KS-1 now; migration into CEE and MOZ by 2027-03-31 (POAM-020) | Vice President, Integration Management Office | 2027-03-31 |
| R-029 | A CUI supplier without the CMMC status its subcontract needs receives CUI | High | ER-04 | Verify all 380 in SPRS; block CUI release in the gateway to suppliers without verified status (POAM-018) | Vice President, Supply Chain | 2027-01-31 |
| R-032 | Malicious code arrives in a trusted CAD, PLM, or file transfer software update | High | ER-04 | Signature verification for server software; supply chain plan for system components (POAM-023) | CISO | 2027-03-31 |
| R-039 | An altered NC program or additive build file produces a nonconforming flight part | High | ER-05 | Checksum verification at DNC and printer load (POAM-021) | Vice President, Quality | 2027-03-31 |
| R-046 | CUI on the KS-1 legacy file server is exfiltrated | High | ER-06 | Migrate CUI by 2027-03-31; interim MFA and SIEM forwarding (POAM-020) | Vice President, Integration Management Office | 2027-03-31 |
| R-050 | A material incident is disclosed late or inaccurately, or the 8-K draft discloses CUI or classified details | High | ER-07 | Add data-theft scenario, content review, and delay path; tabletop 2026-11-19 (POAM-019) | General Counsel | 2026-11-30 |

## 6. Themes from the 2026 analysis
1. **Drift after certification (ER-02).** Final Level 2 (C3PAO) status was earned in 2026-03, but sampling found operating exceptions in the six certified sites that would score 80 today (P03). The COO cannot make the 2027-03-20 affirmation until they close (R-013, R-017, R-020).
2. **New and acquired sites (ER-06).** AZ-1 joined after the assessment and KS-1 remains outside the scope. Both carry segmentation, baseline, logging, and backup gaps (R-022, R-023, R-043, R-046, R-047, R-049), and a contract routing error put 7021 work on KS-1 (R-015).
3. **Export control inside the enclave (ER-01).** A data migration dropped ITAR attributes on 14 PLM folders, and an EAR-licensed foreign-person engineer opened ITAR files (R-004). The Senior Empowered Official filed an initial voluntary disclosure notification on 2026-08-19 (R-051).
4. **Supply chain (ER-04).** Only 46% of CUI suppliers have a verified CMMC status, and 4 of 60 sampled purchase orders lacked the DFARS clauses (R-029, R-031). Phase 2 begins 2026-11-10.
5. **Level 3 (ER-02).** 10 of 24 requirements are met. Penetration testing, threat hunting records, supply chain planning, and specialized asset segregation are the main gaps (R-014).
6. **Disclosure readiness (ER-07).** The materiality playbook was tested only with ransomware. A data theft with no outage, and an 8-K draft that must not reveal CUI or classified details, are not covered (R-050).

## 7. Treatment summary
- **Funded (2026 Q4 to 2027 Q3), about $7.4 million:** KS-1 migration and decommissioning ($2.9M), AZ-1 segmentation, transfer service, and baselines ($850K), Level 3 readiness including penetration testing and the DIBCAC preparation ($1.2M), supplier CMMC verification program ($420K), 802.1X and discovery at FL-3 and AZ-1 ($610K), insider risk program for all CEE users ($540K), managed file transfer hardening and virtual patching ($180K), PLM export attribute analytics ($260K), outside counsel for the disclosure tabletop and export matters ($440K). Items map to the POA&M in P07.
- **Accepted (12):** R-007, R-011, R-019, R-024, R-026, R-028, R-034, R-042, R-044, R-053, R-057, R-058. Each is Low residual with strong existing controls, accepted at the right level (section 1) and reviewed within 12 months.
- **Avoided (1):** R-063. The resume ranking feature is off until review.
- **Shared (1):** R-025. Property and business interruption insurance for hurricanes, plus pre-storm failover.
- **Very High risk R-001:** not accepted as is. The CEO and CFO approved the treatment plan and the residual target of High on 2026-09-08; the risk and technology committee reviewed it on 2026-09-10.

## 8. Board reporting
**Risk and technology committee (quarterly):** the enterprise risk profile (section 4), every Very High and High risk with its treatment status and KRI trend, risks outside tolerance, CMMC status and affirmation readiness, Level 3 progress, new risks, and risk acceptances. The 2026-09-10 meeting received this report, the Internal Audit results (P07), and the compliance roadmap (P03).
**Audit committee (quarterly):** Internal Audit results, SOX IT general control status (R-058), and disclosure controls (R-050, R-056). The audit committee reviews the annual Item 106 disclosure draft, which describes this process.
**Management:** the executive risk committee meets monthly and reviews KRIs for all risks outside tolerance.

## 9. Approval
- Executive risk committee: approved the register, treatments, and acceptances, 2026-09-08.
- CEO and CFO: approved the treatment plan and residual target for Very High risk R-001, 2026-09-08.
- Risk and technology committee of the board: reviewed the enterprise risk profile, 2026-09-10.
- Next full review: June to July 2027, or sooner after a major change, an incident, an acquisition, or a CMMC assessment. KRIs are refreshed quarterly.
