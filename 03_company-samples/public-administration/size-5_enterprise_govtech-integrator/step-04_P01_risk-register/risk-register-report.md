# Enterprise Risk Register Report: Cris Santos Company | Public Administration | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded GovTech systems integrator; about 145 agency customers in 16 states) |
| Size tier | Enterprise (12,000 employees) |
| Vertical | Public Administration |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) for each risk; NIST IR 8286 Rev. 1 for integration into enterprise risk management (ERM) |
| Also satisfies | SP 800-53 RA-3 (every agency contract); the risk assessment agencies expect under CJISSECPOL RA-3 and Pub. 1075; the HIPAA risk analysis for the AG-04 business associate scope (45 CFR 164.308(a)(1)(ii)(A)); input to the Reg S-K Item 106 description of risk management processes |
| Prepared | 2026-06-01 to 2026-07-31 by the GRC team for the CISO; updated 2026-08-28 with Internal Audit findings (P07) |
| Approved | Executive risk committee (chaired by the Chief Risk Officer), 2026-09-08; reviewed by the risk committee of the board, 2026-09-10 |

## 1. Scope and risk framing
**Scope.** Every system that holds or reaches agency data or supports a tier-1 process: ACMC and the integration hub, the four IES environments, legacy hosting in DC-1 and DC-2, the AQ-1 platform, the CUI enclave, the enterprise platform services, and about 1,450 vendors (214 with agency data or system access). Processes and impact values come from the enterprise BIA (P05). ACMC is also covered at system level in the SSP (P02).

**Whose harm counts.** For a GovTech integrator, the worst impacts usually land on agencies and the people they serve: a wrongful arrest, a family without food assistance, a taxpayer's return disclosed. Impact ratings (Table H-3) include harm to agencies and individuals, not only to the company, and a contract termination right or a CJIS or IRS sanction is treated as a severe impact.

**Three lines.** Risk owners in the segments and IT (first line) own and treat risks. The GRC team, the Director of Regulated Data Compliance, and the Chief Risk Officer (second line) run this method and roll risks up into the enterprise risk register. Internal Audit (third line) tests controls independently (P07).

**Risk appetite (board-approved, 2026-02).**
- **Public safety and welfare:** very low appetite for technology failures that harm the people agencies serve.
- **Regulated data and contract compliance:** very low appetite for breaching a CJIS Security Addendum, Pub. 1075 Exhibit 7, business associate agreement, DPPA, or federal clause.
- **Service continuity:** low appetite for disruption of tier-1 agency services.
- **Disclosure and financial reporting:** very low appetite for SEC disclosure or SOX failures.
- **Growth and innovation (acquisitions, AI):** moderate appetite, provided risks are identified and funded at the time of the decision.

**Risk tolerance (measurable, per enterprise risk).** The highest residual risk level each enterprise risk may carry without a board-reported treatment plan. A risk above its threshold is **Outside tolerance** in the register.

| Enterprise risk | Tolerance threshold |
|---|---|
| ER-01 Disruption of agency services | Moderate |
| ER-02 Compromise of regulated agency data | Moderate |
| ER-03 Third-party and subcontractor risk | Moderate |
| ER-04 Integration of acquired businesses | Moderate |
| ER-05 Regulatory and contract compliance (CJIS, Pub. 1075, HIPAA, DPPA, federal clauses) | Low |
| ER-06 SEC disclosure and financial reporting integrity | Low |
| ER-07 Legacy technology | Moderate |
| ER-08 Responsible use of AI in public services | Moderate |

**Who can accept risk:**
| Residual level | Acceptance authority |
|---|---|
| Very Low, Low | Risk owner (vice president or director) with GRC concurrence |
| Moderate | CISO with the accountable executive (segment president) |
| High | Executive risk committee (Chief Risk Officer, CIO, CTO, CISO, General Counsel, segment presidents), reported to the board risk committee |
| Very High | CEO and CFO jointly, reported to the board risk committee at its next meeting |

A risk that would breach a CJIS Security Addendum, Pub. 1075 Exhibit 7, or business associate agreement term may not be accepted at any level; it must be treated or the regulated data removed. Any acceptance expires after 12 months.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the threat picture for state and local government suppliers (ransomware against integrators, supply chain compromise, insider misuse of CJI and FTI), the BIA (P05), the gap analysis (P03), the AI review (P10), and the Internal Audit assessment (P07).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial), and likelihood of adverse impact, combined with **Table G-5**.
3. **Rate impact.** **Table H-3**, calibrated to the BIA impact values (P05 section 3).
4. **Determine risk.** **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the tables, not assigned by hand.
5. **Integrate with ERM (NIST IR 8286 Rev. 1).**
   - Each system-level cybersecurity risk is a row in this register, with an owner, a treatment, and a key risk indicator (KRI).
   - Each row is normalized into one of **8 enterprise risks (ER-01 to ER-08)** in the Chief Risk Officer's enterprise risk register, with an ERM category.
   - **Aggregation rule:** an enterprise risk's exposure equals its highest constituent risk level, and the profile also reports how many constituent risks sit outside tolerance, so one severe risk is never averaged away.
   - The enterprise risk profile (section 4) is what the board risk committee sees each quarter.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 13 |
| Moderate | 36 |
| Low | 16 |
| **Total** | **66** |

By threat source type: Structural 29, Adversarial 22, Accidental 11, Environmental 4.
By treatment: Mitigate 58, Accept 6, Avoid 2.
By status: In progress 53, Open 5, Closed (accepted) 6, Closed (avoided) 2.
**21 risks are outside tolerance**, and each has a dated treatment plan.

## 4. Enterprise risk profile (roll-up for the board)
| ID | Enterprise risk | ERM category | Risks | Very High | High | Moderate | Low | Exposure (highest) | Tolerance | Outside tolerance |
|---|---|---|---|---|---|---|---|---|---|---|
| ER-01 | Disruption of agency services | Operational | 13 | 1 | 1 | 6 | 5 | **Very High** | Moderate | 2 |
| ER-02 | Compromise of regulated agency data | Compliance and reputational | 13 | 0 | 1 | 10 | 2 | **High** | Moderate | 1 |
| ER-03 | Third-party and subcontractor risk | Operational | 6 | 0 | 3 | 3 | 0 | **High** | Moderate | 3 |
| ER-04 | Integration of acquired businesses | Strategic | 5 | 0 | 1 | 4 | 0 | **High** | Moderate | 1 |
| ER-05 | Regulatory and contract compliance | Compliance | 12 | 0 | 2 | 6 | 4 | **High** | Low | 8 |
| ER-06 | SEC disclosure and financial reporting integrity | Financial and compliance | 4 | 0 | 1 | 1 | 2 | **High** | Low | 2 |
| ER-07 | Legacy technology | Operational | 6 | 0 | 2 | 3 | 1 | **High** | Moderate | 2 |
| ER-08 | Responsible use of AI in public services | Strategic and public trust | 7 | 0 | 2 | 3 | 2 | **High** | Moderate | 2 |

**Reading the profile:**
- **ER-01 (service disruption)** carries the only Very High risk: ransomware spreading across ACMC, the integration hub, and legacy hosting (R-001). The AQ-1 peering (R-003, ER-04) and the legacy estate (R-005, R-015, ER-07) are the main reasons its likelihood is not lower.
- **ER-05 (regulatory and contract compliance)** has the lowest tolerance and the most risks outside it (8). Two are High: unscreened AQ-1 staff with court CJI access (R-004) and FIPS 140-2 modules on CJI paths after the CJIS cutoff (R-006). The others are process gaps in agency notice, subcontractor flowdown, DPPA exports, the AG-04 business associate scope, and CMMC readiness.
- **ER-03 (third parties)** is outside tolerance because the help desk subcontractor exposed FTI to an overnight tier outside the United States (R-007), alongside vendor breach (R-013) and software supply chain (R-014) risks.
- **ER-06 (disclosure)** is outside tolerance mainly because the materiality process has not been exercised with the current disclosure committee and does not weigh harm to agency customers (R-010).
- **ER-08 (AI)** has two High risks from the AI eligibility assistant pilot: automation bias (R-011) and unequal accuracy across language and age groups (R-012). The AI governance committee set suggestions to be switched off from 2026-09-11 until the P10 conditions are met.

## 5. Top risks (Very High and High)
| Risk ID | Risk | Level | Enterprise risk | Treatment | Owner | Due |
|---|---|---|---|---|---|---|
| R-001 | Ransomware encrypts ACMC, the integration hub, and legacy hosting across many agencies | Very High | ER-01 | Restrict and federate AQ-1 (POAM-004, POAM-001); immutable legacy backups (POAM-008); replace unsupported servers (POAM-005); tabletop with the disclosure committee and agencies (POAM-013) | CISO | 2027-01-31 |
| R-002 | Theft of FTI and CJI during an intrusion, followed by extortion | High | ER-02 | 24-hour purge of staged files; egress anomaly models; AQ-1 peering restriction | Director of Security Operations | 2027-03-31 |
| R-003 | Attacker enters through AQ-1 and reaches the integration hub over the peering | High | ER-04 | Peering restriction (POAM-004); SIEM onboarding (POAM-003); federation (POAM-001) | Vice President, Integration Management Office | 2027-01-31 |
| R-004 | Audit finds AQ-1 staff with court CJI access unscreened | High | ER-05 | Access suspended; checks, certifications, and training before restoring (POAM-002) | Chief Human Resources Officer | 2026-10-31 |
| R-005 | Exploit of an unsupported legacy server | High | ER-07 | Replatform or isolate the 64 servers (POAM-005); segment management network (POAM-024) | Director of Network and Data Center Operations | 2027-06-30 |
| R-006 | FIPS 140-2 modules on CJI paths after 2026-09-21 | High | ER-05 | Replace 7 appliances by 2026-09-18 or shut the tunnels (POAM-006) | Director of Network and Data Center Operations | 2026-09-18 |
| R-007 | FTI in ticket screenshots viewed by the help desk overnight tier outside the United States | High | ER-03 | U.S.-only routing; block attachments; disclose to the revenue agencies (POAM-009) | Director of Third-Party Risk Management | 2026-09-30 |
| R-009 | IES outage exceeds the 8-hour RTO | High | ER-01 | Parallel restore; retest (POAM-015) | President, Eligibility and Enrollment Operations | 2027-02-28 |
| R-010 | Material incident disclosed late or inaccurately | High | ER-06 | Playbook update; tabletop 2026-11-12 (POAM-013) | General Counsel | 2026-11-30 |
| R-011 | Caseworkers accept wrong AI eligibility suggestions | High | ER-08 | Suggestions off; review-first design; deterministic calculations (POAM-022) | Chief Data and AI Officer | 2026-12-31 |
| R-012 | AI-001 less accurate for some language and age groups | High | ER-08 | Stratified bias test before re-enablement (POAM-022) | Chief Data and AI Officer | 2026-12-31 |
| R-013 | A third party with agency data is breached | High | ER-03 | Clear overdue reviews; continuous monitoring (POAM-011) | Director of Third-Party Risk Management | 2027-03-31 |
| R-014 | Malicious code in a vendor update or dependency | High | ER-03 | Staged rollout; provenance checks | Chief Technology Officer | 2027-06-30 |
| R-015 | Legacy backups deleted or encrypted | High | ER-07 | Immutable backup appliance (POAM-008) | Director of Network and Data Center Operations | 2026-12-31 |

## 6. Themes from the 2026 analysis
1. **The acquisition is the easiest way in (ER-04).** AQ-1 runs its own directory with 31 standing administrators, keeps logs 90 days outside the SIEM, and has peering into the integration hub that Internal Audit used to reach hub management ports (R-003, R-036 to R-038). It also brought 39 unscreened staff with court CJI access (R-004). Treatment: restrict, monitor, then federate, all by 2027-01-31. New deals now need a funded security integration plan (R-061).
2. **Legacy hosting carries old risk (ER-07).** 64 unsupported servers, a flat management network, non-immutable backups, a shared vendor VPN profile, and a single site for 6 customers (R-005, R-015, R-034, R-039). Treatment: immutable backups by 2026-12-31 and replatforming by 2027-06-30.
3. **Dated regulatory deadlines (ER-05).** The CJIS FIPS 140-2 cutoff of 2026-09-21 falls 11 days after this report (R-006). The CMMC Phase 2 date (2026-11-10, 32 CFR 170.3(e)) matters for the DoD subcontract's 2027 option (R-028).
4. **Regulated data in the wrong places (ER-02, ER-03, ER-05).** FTI in support tickets seen outside the United States (R-007), subcontractors outside the IRS notifications (R-008), unmasked ePHI in an IES test environment (R-026), and FTI in free-text notes (R-054).
5. **AI in benefits decisions (ER-08).** The AI eligibility assistant pilot showed high caseworker acceptance of wrong suggestions and lower accuracy for Spanish and Haitian Creole documents and older households (R-011, R-012). A proposed fraud-risk score was declined (R-044, Avoid).
6. **Disclosure readiness (ER-06).** The materiality playbook must weigh harm that falls mainly on agencies, and the committee must practice with its new members (R-010). Item 106 statements will be tested by Internal Audit before the next 10-K (R-064).

## 7. Treatment summary
- **Funded (2026 Q4 to 2027 Q2), about $11.8 million:** legacy replatforming and isolation ($4.6M), AQ-1 integration security workstream ($2.1M), immutable backup appliance for legacy hosting ($0.9M), VPN appliance replacement and a second edge in DC-2 ($1.3M), third-party continuous monitoring and review backlog ($0.7M), IES recovery redesign ($0.8M), AI-001 remediation and bias testing ($0.6M), CMMC Level 2 readiness and C3PAO assessment ($0.4M), three Internal Audit positions ($0.3M per year), and outside counsel for the disclosure tabletop ($0.1M). Items map to the POA&M in P07.
- **Accepted (6):** R-033, R-047, R-050, R-055, R-056, R-063. Each is Low or Moderate residual with strong existing controls, accepted at the right level (section 1) and reviewed within 12 months. None involves a CJIS, Pub. 1075, or business associate term.
- **Avoided (2):** R-041 (unapproved generative AI domains blocked) and R-044 (fraud-risk scoring proposal declined).
- **Very High risk R-001:** not accepted as is. The CEO and CFO approved the treatment plan and a residual target of High on 2026-09-08; the board risk committee reviewed it on 2026-09-10.

## 8. Board reporting
**Risk committee of the board (quarterly):** the enterprise risk profile (section 4), every Very High and High risk with its treatment status and KRI trend, risks outside tolerance, new risks since the last meeting, and acceptances made. The 2026-09-10 meeting received this report, the Internal Audit results (P07), and the regulatory roadmap (P03).
**Audit committee (quarterly):** Internal Audit results, SOX IT general control status (R-032), and disclosure controls (R-010, R-064). The audit committee also reviews the annual Item 106 disclosure draft, which describes this process.
**Management:** the executive risk committee meets monthly and reviews KRIs for all risks outside tolerance.
**Agencies:** on request under their contracts, agencies receive the risks that affect their data (for example, R-004 for criminal justice agencies, R-007 and R-008 for revenue agencies), without other customers' details.

## 9. Approval
- Executive risk committee: approved the register, treatments, and acceptances, 2026-09-08.
- CEO and CFO: approved the treatment plan and residual target for Very High risk R-001, 2026-09-08.
- Risk committee of the board: reviewed the enterprise risk profile, 2026-09-10.
- Next full review: June to July 2027, or sooner after a major change, incident, acquisition, or new CJISSECPOL version. KRIs are refreshed quarterly.
