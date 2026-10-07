# Enterprise Risk Register Report: Cris Santos Company | Emergency Services | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded private ambulance provider with a managed transportation division and EMS billing services; FL, GA, AL, SC, TN) |
| Size tier | Enterprise (12,000 employees) |
| Vertical | Emergency Services |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) for each risk; NIST IR 8286 Rev. 1 for integration into enterprise risk management (ERM) |
| Also satisfies | HIPAA risk analysis and risk management (45 CFR 164.308(a)(1)(ii)(A)-(B)); input to the Reg S-K Item 106 description of risk management processes |
| Prepared | 2026-06-01 to 2026-07-31 by the GRC team for the CISO; updated 2026-08-28 with Internal Audit findings (P07) |
| Approved | Executive risk committee (chaired by the Chief Risk Officer), 2026-09-08; reviewed by the risk committee of the board, 2026-09-10 |

## 1. Scope and risk framing
**Scope.** All systems that create, receive, maintain, or transmit ePHI or support tier-1 processes across the 231 sites, the four communications centers, the fleet of about 1,450 ambulances, the two cloud estates and the colocation data center, the two acquired operations (AQ-01 and AQ-02), the two service lines (SL-1 and SL-2), and the roughly 650 vendors (190 with PHI) and 1,400 managed transportation network providers. Business processes and impact values come from the enterprise BIA (P05). The Enterprise Dispatch and Patient Care Platform is also covered at system level in the SSP (P02).

**Three lines.** Risk owners in the business and IT (first line) own and treat risks. The GRC team and the Chief Risk Officer (second line) run this method and roll risks up into the enterprise risk register. Internal Audit (third line) tests controls independently (P07).

**Risk appetite (board-approved, 2026-02).** Qualitative statements set by the board:
- **Public and patient safety:** very low appetite for technology-related delays in emergency response or harm to patients.
- **Regulatory, contract, and disclosure:** very low appetite for noncompliance with HIPAA, state EMS rules, Medicare documentation rules, county agreements, Section 1557, or SEC disclosure rules.
- **Service continuity:** low appetite for disruption of dispatch and transport services.
- **Protected health information:** low appetite for unauthorized disclosure.
- **Growth and innovation (acquisitions, AI):** moderate appetite, provided risks are identified and funded before or at the time of the decision.

**Risk tolerance (measurable, per enterprise risk).** The highest residual risk level each enterprise risk may carry without a board-reported treatment plan. A risk above its threshold is **Outside tolerance** in the register.

| Enterprise risk | Tolerance threshold |
|---|---|
| ER-01 Disruption of emergency response and transport services | Moderate |
| ER-02 Compromise of protected health information and personal information | Moderate |
| ER-03 Third-party and concentration risk | Moderate |
| ER-04 Integration of acquired operations | Moderate |
| ER-05 Patient and public safety from dispatch and clinical technology | Low |
| ER-06 Regulatory, contract, and disclosure compliance | Low |
| ER-07 Financial reporting integrity and fraud | Low |
| ER-08 Responsible use of AI | Moderate |

**Who can accept risk:**
| Residual level | Acceptance authority |
|---|---|
| Very Low, Low | Risk owner (vice president or director) with GRC concurrence |
| Moderate | CISO with the accountable executive |
| High | Executive risk committee (Chief Risk Officer, CIO, COO, CISO, General Counsel, Chief Medical Officer), reported to the board risk committee |
| Very High | CEO and CFO jointly, reported to the board risk committee at its next meeting |

Safety risks (ER-05) at High or above cannot be accepted without a dated treatment plan. Any acceptance expires after 12 months.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the Emergency Services threat picture (ransomware against dispatch, edge devices, third-party concentration), the BIA (P05), the gap analysis (P03), and the Internal Audit assessment (P07).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial), and likelihood of adverse impact, combined with **Table G-5**.
3. **Rate impact.** **Table H-3**, calibrated to the BIA impact values (P05 section 3). Any plausible delay in emergency response is rated at least High.
4. **Determine risk.** **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the tables, not assigned by hand.
5. **Integrate with ERM (NIST IR 8286 Rev. 1).**
   - Each system-level cybersecurity risk is a row in this cybersecurity risk register, with an owner, a treatment, and a key risk indicator (KRI).
   - Each row is normalized into one of **8 enterprise risks (ER-01 to ER-08)** in the Chief Risk Officer's enterprise risk register, with an ERM category (operational, compliance, strategic, clinical and public safety, financial).
   - **Aggregation rule:** an enterprise risk's exposure equals its highest constituent risk level, and the profile also reports how many constituent risks sit outside tolerance. This keeps one severe risk from being averaged away.
   - The enterprise risk profile (section 4) is what the board risk committee sees each quarter.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 11 |
| Moderate | 37 |
| Low | 17 |
| **Total** | **66** |

By threat source type: Adversarial 30, Structural 28, Accidental 7, Environmental 1.
By treatment: Mitigate 54, Accept 9, Avoid 3.
By status: In progress 49, Open 5, Closed 12 (9 accepted, 3 avoided).
**22 risks are outside tolerance** and each has a dated treatment plan. 22 risks are board-reported (every Very High and High risk plus every risk outside tolerance).

## 4. Enterprise risk profile (roll-up for the board)
| ID | Enterprise risk | ERM category | Risks | Very High | High | Moderate | Low | Exposure (highest) | Tolerance | Outside tolerance |
|---|---|---|---|---|---|---|---|---|---|---|
| ER-01 | Disruption of emergency response and transport services | Operational | 13 | 1 | 2 | 6 | 4 | **Very High** | Moderate | 3 |
| ER-02 | Compromise of protected health information and personal information | Compliance and reputational | 16 | 0 | 1 | 11 | 4 | **High** | Moderate | 1 |
| ER-03 | Third-party and concentration risk | Operational | 6 | 0 | 3 | 2 | 1 | **High** | Moderate | 3 |
| ER-04 | Integration of acquired operations | Strategic | 5 | 0 | 1 | 4 | 0 | **High** | Moderate | 1 |
| ER-05 | Patient and public safety from dispatch and clinical technology | Clinical and public safety | 5 | 0 | 3 | 2 | 0 | **High** | Low | 5 |
| ER-06 | Regulatory, contract, and disclosure compliance | Compliance | 12 | 0 | 1 | 6 | 5 | **High** | Low | 7 |
| ER-07 | Financial reporting integrity and fraud | Financial | 4 | 0 | 0 | 2 | 2 | **Moderate** | Low | 2 |
| ER-08 | Responsible use of AI | Strategic and clinical | 5 | 0 | 0 | 4 | 1 | **Moderate** | Moderate | 0 |

**Reading the profile:**
- **ER-01 (service disruption)** carries the only Very High risk, ransomware against the enterprise CAD (R-001). The slow regional failover (R-005) and the AQ-01 pathway (R-003, ER-04) are the main reasons its likelihood is not lower.
- **ER-05 (public and patient safety)** has the lowest tolerance, so all 5 of its risks are outside it, including three High risks: end-of-support vehicle routers (R-006), untested CAD response plan changes (R-008), and default passwords on radio console gateways (R-009, fixed 2026-08-14 and awaiting verification).
- **ER-06 (regulatory and disclosure)** is outside tolerance mainly because the SEC materiality process has never been exercised for a dispatch outage (R-017).
- **ER-08 (AI)** is within tolerance today because AI call triage runs only in shadow mode. The safety side of that tool sits in ER-05 (R-011) and is outside tolerance until the go-live gate in P10 is met.

## 5. Top risks (Very High and High)
| Risk ID | Risk | Level | Enterprise risk | Treatment | Owner | Due |
|---|---|---|---|---|---|---|
| R-001 | Ransomware encrypts the enterprise CAD application tier and dispatch consoles at more than one communications center | Very High | ER-01 | Close AQ-01 gaps (R-003); automate regional failover (POAM-011); exercise a dispatch-outage scenario with the disclosure committee (POAM-014) | CISO | 2027-01-31 |
| R-002 | Exfiltration of CAD data, call recordings, and ePCR extracts during ransomware | High | ER-02 | Egress anomaly detection for object storage; shorten recording retention (R-053) | Director of Security Operations | 2027-03-31 |
| R-003 | Attacker enters through AQ-01's flat network and reaches the integration hub over the site VPN | High | ER-04 | Restrict the VPN; SD-WAN migration; identity federation (POAM-016; POAM-001) | Vice President, Integration Management Office | 2027-01-31 |
| R-005 | Enterprise CAD regional failover takes longer than the 1-hour RTO | High | ER-01 | Automate interface and DNS cutover; retest; test RCC-3 failover (POAM-011) | Director of CAD and Dispatch Systems | 2027-01-31 |
| R-006 | Attacker exploits end-of-support firmware on vehicle routers | High | ER-05 | Replace routers; enroll AQ-01 routers (POAM-009) | Director of Endpoint and Mobile Engineering | 2027-03-31 |
| R-008 | An untested CAD response plan or unit recommendation change sends the wrong unit or level of care | High | ER-05 | Dispatch change board with a test record; automated block (POAM-006) | Medical Director for Communications | 2026-12-15 |
| R-009 | Default vendor passwords on radio console gateways let an attacker disrupt dispatch radio | High | ER-05 | Passwords changed; vault and scan gateways (POAM-012) | Vice President, Communications Centers | 2026-10-31 |
| R-014 | Network provider portal account takeover exposes member PHI or redirects trips | High | ER-03 | MFA for all provider accounts; attestation before trips are assigned (POAM-013) | President, Managed Transportation | 2026-12-31 |
| R-017 | A material incident is disclosed late or inaccurately because the materiality process was built for data breaches | High | ER-06 | Operational-outage factors in the worksheet; full tabletop on 2026-11-18 (POAM-014) | General Counsel | 2026-11-30 |
| R-025 | A third party with PHI suffers a breach | High | ER-03 | Continuous monitoring of tier-1 and tier-2 vendors; AQ-02 contract review (POAM-022) | Director of Third-Party Risk Management | 2027-03-31 |
| R-030 | Malicious code arrives in a trusted CAD, router firmware, or monitor software update | High | ER-03 | Staged firmware rollout; SBOM requests for tier-1 vendors | CISO | 2027-06-30 |
| R-048 | Zero-day in an internet-facing edge device is exploited | High | ER-01 | Retire AQ-01 legacy firewalls with SD-WAN migration (POAM-016); 72 h emergency patch SLA | Director of Network Engineering | 2027-01-31 |

## 6. Themes from the 2026 analysis
1. **Dispatch continuity (ER-01).** The enterprise CAD has a warm standby, but the last regional failover took 1 hour 25 minutes against a 1-hour RTO, and RCC-3 has never failed over to another center (R-005). Manual dispatch is drilled quarterly and is what keeps R-001 from being worse.
2. **Acquisition integration (ER-04).** AQ-01 still runs a legacy CAD on an unsupported operating system with shared console logins, a legacy directory, a flat network, and no SIEM feed. These conditions raise the likelihood of enterprise ransomware (R-001, R-003), late terminations (R-004), data loss (R-007), undetected misuse (R-016), and late escalation (R-060). Treatment: identity federation, SD-WAN, and migration to the enterprise CAD, all due by 2027-03-31. Going forward, deal approvals must include security due diligence and integration funding (R-061).
3. **Fleet edge (ER-05).** About 160 vehicle routers run end-of-support firmware, AQ-01 routers are unmanaged, and some MDCs still use shared vehicle logins (R-006, R-058). Testing found default passwords on radio console gateways (R-009).
4. **Managed transportation network (ER-03).** About 1,400 small transportation providers reach member PHI through the broker portal, with MFA on 62% of accounts and security attestations missing for 38% of providers (R-014).
5. **Materiality and disclosure (ER-06).** The playbook was written for data breaches. A dispatch outage harms the business through county penalties, contract risk, and public safety rather than through records counts, and the worksheet does not yet capture that (R-017).
6. **AI (ER-05 and ER-08).** 9 use cases; 5 reviewed; AI call triage under-triages Spanish-language calls in shadow mode (R-011, R-012, R-013). Free-text screening in the recruiting chatbot was switched off pending review (R-043, treatment Avoid).

## 7. Treatment summary
- **Funded (2026 Q4 to 2027 Q2), about $7.0 million:** AQ-01 CAD migration and integration ($3.2M), vehicle router replacement ($1.9M), AQ-01 identity federation ($600K), AQ-01 SD-WAN migration ($520K), automated CAD failover engineering ($420K), network provider portal MFA ($180K), dispatch change board tooling ($150K), and outside counsel for the disclosure tabletop ($40K). Items map to the POA&M in P07.
- **Accepted (9):** R-021, R-029, R-033, R-044, R-047, R-050, R-051, R-052, R-063. Each is Low or Moderate residual with strong existing controls, within its enterprise risk's tolerance, accepted at the right level (section 1), and reviewed within 12 months.
- **Avoided (3):** R-039, R-041, R-043. The company declines criminal justice information in CAD, blocks unapproved generative AI domains, and has disabled free-text screening in the recruiting chatbot.
- **Very High risk R-001:** not accepted as is. The CEO and CFO approved the treatment plan and the residual target of High on 2026-09-08; the board risk committee reviewed it on 2026-09-10.

## 8. Board reporting
**Risk committee of the board (quarterly):** the enterprise risk profile (section 4), every Very High and High risk with its treatment status and KRI trend, risks outside tolerance, new risks since the last meeting, and risk acceptances made. The 2026-09-10 meeting received this report, the Internal Audit results (P07), and the regulatory roadmap (P03).
**Audit committee (quarterly):** Internal Audit results, SOX IT general control status (R-032), and the disclosure controls topics (R-017, R-019). The audit committee also reviews the annual Item 106 disclosure draft, which describes this process.
**Management:** the executive risk committee meets monthly and reviews KRIs for all risks outside tolerance.

## 9. Approval
- Executive risk committee: approved the register, treatments, and acceptances, 2026-09-08.
- CEO and CFO: approved the treatment plan and residual target for Very High risk R-001, 2026-09-08.
- Risk committee of the board: reviewed the enterprise risk profile, 2026-09-10.
- Next full review: June to July 2027, or sooner after a major change, incident, or acquisition. KRIs are refreshed quarterly.
