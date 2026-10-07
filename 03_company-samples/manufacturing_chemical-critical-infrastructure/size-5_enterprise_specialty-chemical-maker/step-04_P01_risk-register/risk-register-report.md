# Enterprise Risk Register Report: Cris Santos Company | Chemical | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded specialty chemical formulator and packager: 14 plants, 9 distribution centers, 2 R&D centers in eight states) |
| Size tier | Enterprise (12,000 employees) |
| Vertical | Chemical (NAICS 325998) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) for each risk; NIST IR 8286 Rev. 1 for integration into enterprise risk management (ERM) |
| Also satisfies | Input to the PLT-01 MTSA Cybersecurity Assessment (33 CFR 101.650(e)(1)); input to the RMP and PSM hazard analyses where a cyber event can initiate or worsen a release (40 CFR 68.67; 29 CFR 1910.119(e)); input to the DOT hazmat security plan risk assessment (49 CFR 172.802(a)); input to the Reg S-K Item 106 description of risk management processes |
| Prepared | 2026-06-01 to 2026-07-31 by the GRC team for the CISO and the Chief Risk Officer; updated 2026-08-28 with Internal Audit findings (P07) |
| Approved | Executive risk committee (chaired by the Chief Risk Officer), 2026-09-08; reviewed by the risk committee of the board, 2026-09-10 |

## 1. Scope and risk framing
**Scope.** All 14 plants (OT and IT), the 9 distribution centers and 2 R&D centers, the two cloud estates and two colocation data centers, the SL-1 and SL-2 service lines, the three plants acquired in 2025, and about 2,600 vendors (about 180 with OT or remote access). Business processes and impact values come from the enterprise BIA (P05). The PLT-01 Gulf Coast Complex Process Control and Batch Management System (GC-PCBMS) is also covered at system level in the SSP (P02).

**Three lines.** Risk owners in operations, process safety, and IT (first line) own and treat risks. The GRC team and the Chief Risk Officer (second line) run this method and roll risks up into the enterprise risk register. Internal Audit (third line) tests controls independently (P07).

**Risk appetite (board-approved, 2026-02).**
- **Process safety:** very low appetite for any cyber event that could cause or worsen a release of a toxic or flammable chemical, harm workers, or reach the public.
- **Regulatory and disclosure:** very low appetite for noncompliance with the MTSA cybersecurity rule, RMP, PSM, DOT hazmat security, release reporting, or SEC disclosure rules.
- **Production and supply continuity:** low appetite for disruption of supply to municipal water utilities; moderate appetite for disruption of other product lines that other plants can cover.
- **Confidential information:** low appetite for loss of formulations, toll customer recipes, and SSI.
- **Growth and innovation (acquisitions, AI):** moderate appetite, provided risks are identified and funded before or at the time of the decision.

**Risk tolerance (measurable, per enterprise risk).** The highest residual risk level each enterprise risk may carry without a board-reported treatment plan. A risk above its threshold is **Outside tolerance** in the register.

| Enterprise risk | Tolerance threshold |
|---|---|
| ER-01 Process safety: toxic or flammable release caused or worsened by a cyber event | Low |
| ER-02 Production and supply disruption from cyber and technology events | Moderate |
| ER-03 Third-party, OT vendor, and concentration risk | Moderate |
| ER-04 Integration of acquired plants | Moderate |
| ER-05 Regulatory and disclosure compliance | Low |
| ER-06 Confidential information: formulations, toll customer recipes, SSI, and personal information | Moderate |
| ER-07 Financial reporting integrity and fraud | Low |
| ER-08 Responsible use of AI | Moderate |

**Who can accept risk:**
| Residual level | Acceptance authority |
|---|---|
| Very Low, Low | Risk owner (vice president or director) with GRC concurrence |
| Moderate | CISO with the accountable executive |
| High | Executive risk committee (Chief Risk Officer, COO, CIO, CISO, General Counsel, Vice President, Process Safety and EHS), reported to the board risk committee |
| Very High | CEO and CFO jointly, reported to the board risk committee at its next meeting |

Process safety risks (ER-01) at Moderate or above cannot be accepted without a dated treatment plan and the concurrence of the Vice President, Process Safety and EHS. Any acceptance expires after 12 months.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the chemical sector threat picture (OT-capable state actors, ransomware that spreads from IT to OT, compromised integrators, insiders, theft and diversion of chemicals of interest), the BIA (P05), the gap analysis (P03), and the Internal Audit assessment (P07).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial), and likelihood of adverse impact, combined with **Table G-5**. Independent safety layers (SIS, mechanical relief, manual emergency shutdown) lower the likelihood of adverse impact; they do not lower the likelihood of initiation.
3. **Rate impact.** **Table H-3**, calibrated to the BIA impact values (P05 section 3). Very High impact is reserved for events that could plausibly cause a release reaching the public or stop several plants for days.
4. **Determine risk.** **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the tables, not assigned by hand.
5. **Integrate with ERM (NIST IR 8286 Rev. 1).**
   - Each cybersecurity risk is a row in this register with an owner, a treatment, and a key risk indicator (KRI).
   - Each row is normalized into one of **8 enterprise risks (ER-01 to ER-08)** in the Chief Risk Officer's enterprise risk register, with an ERM category.
   - **Aggregation rule:** an enterprise risk's exposure equals its highest constituent risk level, and the profile also reports how many constituent risks sit outside tolerance. This keeps one severe risk from being averaged away.
   - The enterprise risk profile (section 4) is what the board risk committee sees each quarter.
6. **Link to process safety.** Every ER-01 risk at High or above is sent to the Vice President, Process Safety and EHS for the next PHA revalidation of the affected process, so the cyber scenario is analyzed with the process safeguards.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 14 |
| Moderate | 30 |
| Low | 19 |
| **Total** | **64** |

By threat source type: Adversarial 30, Structural 23, Accidental 9, Environmental 2.
By treatment: Mitigate 50, Accept 10, Avoid 2, Share/Transfer 2.
By status: In progress 43, Open 9, Closed (accepted) 10, Closed (avoided) 2.
**23 risks are outside tolerance** and each has a dated treatment plan. This count includes R-026 (closed-loop AI pilot), which is rated on the design as proposed; the avoidance decision removes the exposure as long as the pilot stays unapproved.

## 4. Enterprise risk profile (roll-up for the board)
| ID | Enterprise risk | ERM category | Risks | Very High | High | Moderate | Low | Exposure (highest) | Tolerance | Outside tolerance |
|---|---|---|---|---|---|---|---|---|---|---|
| ER-01 | Process safety: toxic or flammable release caused or worsened by a cyber event | Operational (process safety) | 13 | 0 | 6 | 4 | 3 | **High** | Low | 10 |
| ER-02 | Production and supply disruption from cyber and technology events | Operational | 15 | 1 | 2 | 9 | 3 | **Very High** | Moderate | 3 |
| ER-03 | Third-party, OT vendor, and concentration risk | Operational | 5 | 0 | 1 | 3 | 1 | **High** | Moderate | 1 |
| ER-04 | Integration of acquired plants | Strategic | 5 | 0 | 2 | 3 | 0 | **High** | Moderate | 2 |
| ER-05 | Regulatory and disclosure compliance | Compliance | 13 | 0 | 2 | 3 | 8 | **High** | Low | 5 |
| ER-06 | Confidential information: formulations, toll customer recipes, SSI, and personal information | Compliance and reputational | 7 | 0 | 0 | 4 | 3 | **Moderate** | Moderate | 0 |
| ER-07 | Financial reporting integrity and fraud | Financial | 2 | 0 | 0 | 1 | 1 | **Moderate** | Low | 1 |
| ER-08 | Responsible use of AI | Strategic and operational | 4 | 0 | 1 | 3 | 0 | **High** | Moderate | 1 |

**Reading the profile:**
- **ER-02 (production and supply)** carries the only Very High risk, ransomware that spreads from enterprise IT through the shared OT services to several plants at once (R-002). Centralizing OT remote access and backups improved control at each plant but created a shared point of failure that must be protected more strongly than any single plant.
- **ER-01 (process safety)** has the lowest tolerance and six High risks, led by the integrator-account intrusion scenario at PLT-01 (R-001), SIS program integrity (R-003), OT changes outside MOC (R-004), and emergency notification that depends on the business network (R-021). The independent SIS layers keep none of these at Very High.
- **ER-05 (regulatory and disclosure)** is outside tolerance because of the KEV backlog under the MTSA rule (R-005) and a materiality process built for data breaches (R-012).
- **ER-04 (acquired plants)** has two High risks (R-010, R-011). These plants are outside the common OT services, so their risk is close to what the Small sample shows for an unmanaged plant.

## 5. Top risks (Very High and High)
| Risk ID | Risk | Level | Enterprise risk | Treatment | Owner | Due |
|---|---|---|---|---|---|---|
| R-002 | Ransomware spreads from enterprise IT through shared OT services to several plants | Very High | ER-02 | Separate admin tiers for gateway and vault; second offline vault copy; OT restore tests (POAM-003); enterprise OT exercise with the disclosure committee (POAM-004) | CISO | 2027-03-31 |
| R-001 | Compromised integrator account on the gateway used to change PLT-01 ammonia unit alarm limits and setpoints | High | ER-01 | Named integrator accounts (POAM-005); OT detections (POAM-022); PHA revalidation | Director of OT Security | 2026-11-30 |
| R-003 | SIS program altered or different from the approved copy | High | ER-01 | Monthly comparison now, automated by 2027-01-31 (POAM-009) | PLT-01 Controls Engineering Manager | 2027-01-31 |
| R-004 | Control changes outside MOC create an unsafe condition | High | ER-01 | Change log reconciliation; automated comparison (POAM-001) | Vice President, Process Safety and EHS | 2027-03-31 |
| R-005 | KEV exploited on a PLT-01 OT host | High | ER-05 | Compensating controls for all open KEVs by 2026-10-31 (POAM-002) | PLT-01 CySO | 2026-10-31 |
| R-006 | Attack on PLT-01 OT goes undetected | High | ER-01 | OT use cases (POAM-022); terminal and rack monitoring (POAM-011) | Director of Security Operations | 2026-11-30 |
| R-007 | OT recovery far exceeds the 12-hour RTO | High | ER-02 | Restore tests for the remaining DCS areas (POAM-003) | PLT-01 Controls Engineering Manager | 2027-02-28 |
| R-008 | Ransomware forces a PLT-01 safe-state shutdown | High | ER-02 | Replace unsupported stations (POAM-020); media control (POAM-021) | PLT-01 Plant Manager | 2027-06-30 |
| R-010 | Intrusion through an acquired plant's flat network | High | ER-04 | OT DMZ, named accounts, vault onboarding (POAM-015) | Vice President, Integration Management Office | 2027-06-30 |
| R-011 | Integrator remote tool at an acquired plant used to take control | High | ER-04 | Disable tools except supervised call-in; extend the gateway (POAM-014) | Director of OT Security | 2026-12-31 |
| R-012 | Material OT incident disclosed late or inaccurately | High | ER-05 | OT materiality factors; operations members; tabletop 2026-11-12 (POAM-004) | General Counsel | 2026-11-30 |
| R-016 | Insider with engineering rights sabotages recipes or logic | High | ER-01 | Quarterly review of engineering actions; insider indicators | Vice President, Corporate Security | 2027-03-31 |
| R-021 | Emergency notification fails during a release | High | ER-01 | Notification kits at 11 more plants (POAM-017) | Vice President, Process Safety and EHS | 2026-12-31 |
| R-026 | Closed-loop AI pilot creates a cloud write path into the DCS | High | ER-08 | Avoided: pilot not approved (P10) | Chief Operating Officer | 2026-08-26 |
| R-030 | Malicious code in a DCS vendor update | High | ER-03 | Hash verification for all OT vendors; staged rollout | Director of OT Security | 2027-06-30 |

## 6. Themes from the 2026 analysis
1. **Shared OT services cut both ways (ER-02).** The central gateway and vault brought 11 plants under named access, MFA, recording, and offline backups. They are also the one place an attacker could reach many plants (R-002). Treatment hardens the services themselves rather than undoing the centralization.
2. **Safety layers hold, but the cyber layer around them is thin (ER-01).** The SIS are independent and proof-tested on schedule. The weak points are the people and processes around them: shared integrator accounts (R-001), manual SIS comparison (R-003), changes outside MOC (R-004), and missing OT detections (R-006).
3. **The MTSA rule sets the clock at PLT-01 (ER-05).** The KEV backlog (R-005) is a current obligation, while the Cybersecurity Assessment and Plan (R-009) are due 2027-07-16. Both are tracked in the P03 roadmap.
4. **Acquired plants (ER-04).** PLT-12 to PLT-14 are outside the common services (R-010, R-011, R-060). Going forward, deal approvals must include OT due diligence and integration funding (R-059).
5. **Disclosure of OT incidents (ER-05).** The materiality process has never been tested on an event where the harm is lost production and safety exposure rather than stolen data (R-012).
6. **New finding from P07 (closing the loop).** Internal Audit found default vendor passwords on the PLT-01 tank gauging server and two truck rack PLC web interfaces on 2026-08-12. This was added as **R-014** and POAM-013 on 2026-08-28. It also raised the likelihood of R-051 and R-052.

## 7. Treatment summary
- **Funded (2026 Q4 to 2027 Q2), about $7.3 million:** OT security at the acquired plants, including OT DMZs, gateway and vault onboarding, and named accounts ($3.1M); Blend Hall 1 console upgrade ($1.6M); OT monitoring extension to 5 plants and the PLT-01 terminal network ($0.9M); notification kits for 11 plants ($0.25M); automated configuration and SIS comparison tooling ($0.6M); MTSA Cybersecurity Assessment support and OT penetration test ($0.45M); restore test outages and vendor services ($0.35M); outside counsel for the disclosure tabletop ($0.04M); and contract amendments for OT suppliers (internal effort). Items map to the POA&M in P07.
- **Accepted (10):** R-023, R-033, R-039, R-041, R-042, R-049, R-056, R-058, R-062, R-064. Each is Low or Moderate with strong existing controls, accepted at the right level (section 1), and reviewed within 12 months.
- **Avoided (2):** R-026 (closed-loop AI pilot not approved) and R-027 (unapproved generative AI services blocked).
- **Shared or transferred (2):** R-029 (hurricane, through property and business interruption insurance) and R-044 (HR and payroll vendor breach, through cyber insurance and contract terms).
- **Very High risk R-002:** not accepted as is. The CEO and CFO approved the treatment plan and a residual target of High on 2026-09-08; the board risk committee reviewed it on 2026-09-10.

## 8. Board reporting
**Risk committee of the board (quarterly):** the enterprise risk profile (section 4), every Very High and High risk with its treatment status and KRI trend, risks outside tolerance, new risks since the last meeting, and risk acceptances made. The 2026-09-10 meeting received this report, the Internal Audit results (P07), and the regulatory roadmap (P03). The risk committee oversees cybersecurity and process safety together, so ER-01 is presented jointly by the CISO and the Vice President, Process Safety and EHS.
**Audit committee (quarterly):** Internal Audit results, SOX IT general control status (R-045, R-046), and the disclosure controls topics (R-012). The audit committee also reviews the annual Item 106 disclosure draft, which describes this process.
**Management:** the executive risk committee meets monthly and reviews KRIs for all risks outside tolerance.

## 9. Approval
- Executive risk committee: approved the register, treatments, and acceptances, 2026-09-08.
- CEO and CFO: approved the treatment plan and residual target for Very High risk R-002, 2026-09-08.
- Risk committee of the board: reviewed the enterprise risk profile, 2026-09-10.
- Next full review: June to July 2027, or sooner after a major change, incident, or acquisition. KRIs are refreshed quarterly. The 2027 review will be timed so it feeds the PLT-01 Cybersecurity Assessment.
