# Enterprise Risk Register Report: Cris Santos Company | Mining, Quarrying, and Oil and Gas Extraction | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded independent crude oil producer; Permian, Mid-Continent, and Florida operating areas) |
| Size tier | Enterprise (12,000 employees) |
| Vertical | Mining, Quarrying, and Oil and Gas Extraction (NAICS 211120) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) for each risk; NIST IR 8286 Rev. 1 for integration into enterprise risk management (ERM) |
| Benchmark | NIST CSF 2.0 with NIST SP 800-82 Rev. 3 (`N21-BM`, see P03). The register is also the input to the Reg S-K Item 106 description of risk management processes |
| Prepared | 2026-06-01 to 2026-07-31 by the GRC team for the CISO, with field site walkthroughs at the IOC, the BCC, the Florida regional control room, and AQ-MC; updated 2026-08-28 with Internal Audit findings (P07) |
| Approved | Executive risk committee (chaired by the Chief Risk Officer), 2026-09-08; reviewed by the risk committee of the board, 2026-09-10 |
| Register | `risk-register.csv` (64 risks) |

## 1. Scope and risk framing
**Scope.** All three operating areas (Permian, Mid-Continent including the acquired AQ-MC assets, Florida), the IOC, the BCC, and the Florida regional control room, the field device estate (about 11,000 controllers and 6,500 cellular modems), the two cloud estates and two colocation data centers, the 13 enterprise systems in `../00_company-facts.md` section 3, and the roughly 1,600 vendors (210 with remote access). Business processes and impact values come from the enterprise BIA (P05). The Field SCADA and Production Accounting System (FSPA) is also covered at system level in the SSP (P02).

**Three lines.** Risk owners in operations, technology, and finance (first line) own and treat risks. The GRC team, the Chief Compliance Officer, and the Chief Risk Officer (second line) run this method and roll risks up into the enterprise risk register. Internal Audit (third line) tests controls independently (P07).

**Risk appetite (board-approved, 2026-02).** Qualitative statements set by the board:
- **Process safety and the environment:** very low appetite for technology-related harm to people, loss of containment, or reportable releases.
- **Regulatory and disclosure:** very low appetite for noncompliance with PHMSA, EPA, state, or SEC disclosure rules.
- **Production continuity:** low appetite for loss of remote control of an operating area; moderate appetite for short, local production deferral that manual operations can cover.
- **Personal and confidential data:** low appetite for unauthorized disclosure of royalty owner, partner, or employee personal information, or of seismic and reservoir trade secrets.
- **Financial integrity:** low appetite for misstated volumes, revenue, royalties, or taxes.
- **Growth and innovation (acquisitions, AI):** moderate appetite, provided risks are identified and funded at the time of the decision.

**Risk tolerance (measurable, per enterprise risk).** The highest residual risk level each enterprise risk may carry without a board-reported treatment plan. A risk above its threshold is **Outside tolerance** in the register.

| Enterprise risk | Tolerance threshold |
|---|---|
| ER-01 Production disruption from cyber and technology events | Moderate |
| ER-02 Process safety and environmental harm from OT compromise | Low |
| ER-03 Third-party, vendor access, and concentration risk | Moderate |
| ER-04 Integration of acquired assets | Moderate |
| ER-05 Compromise of personal and confidential data | Moderate |
| ER-06 Regulatory, disclosure, and reporting compliance | Low |
| ER-07 Financial reporting, revenue, and royalty integrity and fraud | Low |
| ER-08 Responsible use of AI | Moderate |

**Who can accept risk:**
| Residual level | Acceptance authority |
|---|---|
| Very Low, Low | Risk owner (vice president or director) with GRC concurrence |
| Moderate | CISO with the accountable executive |
| High | Executive risk committee (Chief Risk Officer, COO, CIO, CISO, General Counsel), reported to the board risk committee |
| Very High | CEO and CFO jointly, reported to the board risk committee at its next meeting |

Process safety and environmental risks (ER-02) at High or above cannot be accepted without a dated treatment plan. Any acceptance expires after 12 months.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E; the oil and gas threat picture (ransomware that crosses from IT into OT, compromised suppliers and remote access paths, attacks on internet-exposed field devices); SP 800-82 Rev. 3 OT threats and vulnerabilities; the BIA (P05); the gap analysis (P03); and the Internal Audit assessment (P07).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial), and likelihood of adverse impact, combined with **Table G-5**. Hardwired and separate safety shutdowns lower the likelihood that an OT compromise turns into physical harm, and that is reflected in the likelihood of adverse impact, not in impact.
3. **Rate impact.** **Table H-3**, calibrated to the BIA impact values (P05 section 3): Very High means harm to people or a reportable release, loss of remote control of an operating area, or an incident likely to be material for SEC purposes.
4. **Determine risk.** **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the tables, not assigned by hand.
5. **Integrate with ERM (NIST IR 8286 Rev. 1).**
   - Each system-level cybersecurity risk is a row in this cybersecurity risk register, with an owner, a treatment, and a key risk indicator (KRI).
   - Each row is normalized into one of **8 enterprise risks (ER-01 to ER-08)** in the Chief Risk Officer's enterprise risk register, with an ERM category (strategic, operational, health safety and environment, compliance, financial).
   - **Aggregation rule:** an enterprise risk's exposure equals its highest constituent risk level, and the profile also reports how many constituent risks sit outside tolerance. This keeps one severe risk from being averaged away.
   - The enterprise risk profile (section 4) is what the board risk committee sees each quarter.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 11 |
| Moderate | 29 |
| Low | 23 |
| Very Low | 0 |
| **Total** | **64** |

By threat source type: Adversarial 31, Structural 20, Accidental 12, Environmental 1.
By treatment: Mitigate 54, Accept 8, Avoid 2.
By status: In progress 55, Open 1, Closed (accepted) 8.
**20 risks are outside tolerance** and each has a dated treatment plan. **20 risks are reported to the board** (every Very High and High risk, plus every risk outside tolerance).

## 4. Enterprise risk profile (roll-up for the board)
| ID | Enterprise risk | ERM category | Risks | Very High | High | Moderate | Low | Very Low | Exposure (highest) | Tolerance | Outside tolerance |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ER-01 | Production disruption from cyber and technology events | Operational | 17 | 1 | 2 | 10 | 4 | 0 | **Very High** | Moderate | 3 |
| ER-02 | Process safety and environmental harm from OT compromise | Health, safety, and environment | 7 | 0 | 3 | 3 | 1 | 0 | **High** | Low | 6 |
| ER-03 | Third-party, vendor access, and concentration risk | Operational | 6 | 0 | 3 | 2 | 1 | 0 | **High** | Moderate | 3 |
| ER-04 | Integration of acquired assets | Strategic | 4 | 0 | 1 | 3 | 0 | 0 | **High** | Moderate | 1 |
| ER-05 | Compromise of personal and confidential data | Compliance and reputational | 8 | 0 | 1 | 3 | 4 | 0 | **High** | Moderate | 1 |
| ER-06 | Regulatory, disclosure, and reporting compliance | Compliance | 7 | 0 | 1 | 0 | 6 | 0 | **High** | Low | 1 |
| ER-07 | Financial reporting, revenue, and royalty integrity and fraud | Financial | 9 | 0 | 0 | 5 | 4 | 0 | **Moderate** | Low | 5 |
| ER-08 | Responsible use of AI | Strategic and operational | 6 | 0 | 0 | 3 | 3 | 0 | **Moderate** | Moderate | 0 |

**Reading the profile:**
- **ER-01 (production disruption)** carries the only Very High risk: ransomware that starts in business IT and reaches OT (R-001). The Florida control room without an OT DMZ and the AQ-MC network that reaches the enterprise WAN are the main reasons its likelihood is not lower, and the 9-hour failover (R-005) is why its impact stays Very High.
- **ER-02 (process safety and environment)** has the lowest tolerance. Its High risks are about the integrity of control: manipulated logic or setpoints (R-004), unvalidated logic changes (R-010), and field devices found with default credentials during testing (R-061). Hardwired safety shutdowns keep the likelihood of physical harm down, which is why none of these is Very High.
- **ER-03 (third parties and concentration)** combines the ESP vendor's cloud path with setpoint write (R-003), cellular carrier concentration (R-009), and software supply chain risk (R-021).
- **ER-06 (regulatory and disclosure)** is outside tolerance mainly because the SEC materiality playbook has never been exercised for an OT incident and has no quick way to quantify deferred production (R-008).
- **ER-08 (AI)** is within tolerance today, but 4 of 11 use cases lack council review (R-042), and the predictive maintenance model was expanded before its well group review was repeated (R-041).

## 5. Top risks (Very High and High)
| Risk ID | Risk | Level | Enterprise risk | Treatment | Owner | Due |
|---|---|---|---|---|---|---|
| R-001 | Ransomware that starts in business IT spreads toward OT and halts remote operations across an operating area | Very High | ER-01 | Florida OT DMZ and AQ-MC VPN restriction (POAM-003); prove 4-hour failover (POAM-004); OT tabletop with the disclosure committee (POAM-012); OT monitoring at Florida and AQ-MC (POAM-010) | CISO | 2027-03-31 |
| R-002 | Attacker enters through the AQ-MC flat network and VPN and reaches enterprise systems or the AQ-MC legacy SCADA | High | ER-04 | Restrict the VPN to the historian link now; remove the integrator tool; migrate AQ-MC to the enterprise platform (POAM-003; POAM-002; POAM-014) | Vice President, Integration Management Office | 2027-06-30 |
| R-003 | Attacker or rogue insider at the ESP vendor uses the vendor cloud path to change drive setpoints on many wells at once | High | ER-03 | Disable remote write by 2026-10-31; bring the vendor path under the gateway; supplier assessment and contract schedule (POAM-002; POAM-016) | Director of OT Security | 2026-12-31 |
| R-004 | Manipulated controller logic or setpoints cause a loss of containment (tank overflow or gathering line overpressure) before hardwired protection acts | High | ER-02 | Remote programming mode off unless ticketed; automated change enforcement; program compare for all regions (POAM-006) | Vice President, Operations Technology and Automation | 2027-03-31 |
| R-005 | Failover from the IOC to the BCC takes longer than the 4-hour RTO, leaving a region without remote visibility | High | ER-01 | Automate re-pointing; repeat failover test by 2027-02-28 (POAM-004) | Vice President, Operations Technology and Automation | 2027-02-28 |
| R-007 | Royalty owner and employee personal information is stolen during a ransomware attack (double extortion) | High | ER-05 | Egress anomaly models for cloud storage; remove owner exports from file shares; tokenize bank details in reports | Director of Security Operations | 2027-03-31 |
| R-008 | A material incident is disclosed late or inaccurately because the OT and production impact cannot be quantified quickly | High | ER-06 | Add the OT scenario and production-loss worksheet; full tabletop 2026-11-19 (POAM-012) | General Counsel | 2026-11-30 |
| R-009 | Outage at the primary cellular carrier blinds most cellular field sites for hours | High | ER-03 | Second carrier at alarm-critical sites; priority restoration term; patrol staffing plan (POAM-019) | Vice President, Operations Technology and Automation | 2027-06-30 |
| R-010 | An unauthorized or unvalidated controller logic change goes undetected and causes unsafe or wrong operation | High | ER-02 | Program repository and compare for all regions; automated download block (POAM-006) | Vice President, Operations Technology and Automation | 2027-03-31 |
| R-021 | Malicious code arrives in a trusted OT or IT vendor software update | High | ER-03 | Software bill of materials requests for tier-1 vendors; hash verification of OT packages | CISO | 2027-06-30 |
| R-022 | A zero-day in an internet-facing VPN or firewall is exploited | High | ER-01 | Retire AQ-MC edge devices with migration; 72-hour emergency patch SLA | Director of Network Engineering | 2027-06-30 |
| R-061 | Internet-exposed AQ-MC modems with default admin credentials, and LACT flow computers with vendor default passwords, are taken over | High | ER-02 | Move modems to the private APN; replace legacy modems; credential audit of all LACT flow computers (POAM-008) | Director of OT Security | 2026-10-31 |

## 6. Themes from the 2026 analysis
1. **Acquisition integration (ER-04).** The AQ-MC assets still run the seller's legacy SCADA on a flat network that reaches the enterprise WAN over a site-to-site VPN, with shared operator logins and an always-on integrator tool. These conditions raise the likelihood of enterprise ransomware (R-001), lateral movement (R-002), slow incident response (R-060), and default-credential takeover of field modems (R-061). Treatment: restrict the VPN to the historian link now and migrate AQ-MC to the enterprise platform by 2027-06-30. Future deals must include an OT assessment and integration funding (R-062).
2. **Integrity of control (ER-02).** Change control gaps at AQ-MC and Florida (6 of 40 sampled changes had no approval record), no program compare outside the Permian, and devices left in remote programming mode (R-004, R-010). Treatment: one program repository with automated compare and download blocking for all regions (POAM-006).
3. **Vendor-operated paths into the field (ER-03).** The ESP vendor's cloud service can write setpoints on 260 drives outside the remote access gateway (R-003); 38 of 210 vendors with remote access lack a current assessment (R-031).
4. **Recovery of OT (ER-01).** The IOC-to-BCC failover took 9 hours against a 4-hour RTO (R-005); Florida has no standby and same-room backups (R-019); one cellular carrier carries 88% of field modems (R-009).
5. **Disclosure readiness (ER-06).** The materiality playbook lacks an OT scenario and a method to estimate deferred production quickly (R-008). A full tabletop with the disclosure committee is set for 2026-11-19.
6. **AI (ER-08).** The predictive maintenance model (AI-001) was expanded across the Permian before its fairness review by well group was repeated (R-041), and a proposal to let an optimization model write setpoints was refused for now (R-040, treatment Avoid).

## 7. Treatment summary
- **Funded (2026 Q4 to 2027 Q2), about $14.6 million:** AQ-MC migration acceleration and VPN restriction ($6.2M), Florida OT DMZ and SCADA server and HMI replacement ($2.4M), OT monitoring sensors and SIEM onboarding for Florida and AQ-MC ($1.3M), second cellular carrier at alarm-critical sites ($1.9M), failover automation between the IOC and the BCC ($850K), program repository and compare for all regions ($720K), private APN migration and legacy modem replacement ($640K), OT identity governance integration ($410K), and outside counsel and facilitation for the disclosure tabletop ($60K). Items map to the POA&M in P07.
- **Accepted (8):** R-033, R-044, R-047, R-048, R-050, R-051, R-054, R-063. Each is Low or Moderate residual with strong existing controls, accepted at the right level (section 1) and reviewed within 12 months.
- **Avoided (2):** R-040, R-043. Closed-loop setpoint writes by an optimization model are not approved (advisory mode only), and the telematics driver ranking feature stays disabled until council and HR review.
- **Very High risk R-001:** not accepted as is. The CEO and CFO approved the treatment plan and the residual target of High on 2026-09-08; the board risk committee reviewed it on 2026-09-10.

## 8. Board reporting
**Risk committee of the board (quarterly):** the enterprise risk profile (section 4), every Very High and High risk with its treatment status and KRI trend, risks outside tolerance, new risks since the last meeting, and risk acceptances made. The 2026-09-10 meeting received this report, the Internal Audit results (P07), and the compliance roadmap (P03).
**Audit committee (quarterly):** Internal Audit results, SOX IT general control status over hydrocarbon accounting (R-012, R-032), and the disclosure controls topics (R-008, R-058). The audit committee also reviews the annual Item 106 disclosure draft, which describes this process.
**Management:** the executive risk committee meets monthly and reviews KRIs for all risks outside tolerance. The COO's operations leadership meeting reviews the OT risks (ER-01 and ER-02) monthly with the Director of OT Security.

## 9. Approval
- Executive risk committee: approved the register, treatments, and acceptances, 2026-09-08.
- CEO and CFO: approved the treatment plan and residual target for Very High risk R-001, 2026-09-08.
- Risk committee of the board: reviewed the enterprise risk profile, 2026-09-10.
- Next full review: June to July 2027, or sooner after a major change (including the AQ-MC migration), an incident, or an acquisition. KRIs are refreshed quarterly.
