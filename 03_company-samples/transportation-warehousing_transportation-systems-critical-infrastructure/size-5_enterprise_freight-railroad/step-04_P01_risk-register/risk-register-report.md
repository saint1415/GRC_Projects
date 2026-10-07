# Enterprise Risk Register Report: Cris Santos Company | Transportation Systems | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded holding company of 64 short line and regional freight railroads in 27 states, plus a rail services segment) |
| Size tier | Enterprise (12,000 employees) |
| Vertical | Transportation Systems |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) for each risk; NIST IR 8286 Rev. 1 for integration into enterprise risk management (ERM) |
| Also satisfies | Risk input to the Cybersecurity Implementation Plan and the remediation plan from the TSA cybersecurity vulnerability assessment (SD 1580-21-01E Sec. II.E); input to the Reg S-K Item 106 description of risk management processes |
| Prepared | 2026-06-01 to 2026-07-31 by the GRC team for the CISO; updated 2026-08-28 with Internal Audit findings (P07) |
| Approved | Executive risk committee (chaired by the Chief Risk Officer), 2026-09-08; reviewed by the board safety, security, and risk committee, 2026-09-10 |

## 1. Scope and risk framing
**Scope.** All IT and OT systems that support the 17 business processes in the enterprise BIA (P05) across the 64 railroads, about 290 field sites, DC-1 and DC-2, the two cloud estates, the six acquired railroads, and about 1,100 vendors (140 tier-1). The Train Dispatching and PTC Back Office Platform is also covered at system level in the SSP (P02).

**Three lines.** Risk owners in operations, engineering, and technology (first line) own and treat risks. The GRC team and the Chief Risk Officer (second line) run this method and roll risks up into the enterprise risk register. Internal Audit (third line) tests controls independently (P07).

**Risk appetite (board-approved, 2026-02).** Qualitative statements set by the board:
- **Rail safety:** very low appetite for technology-related harm to employees, the public, or trains carrying hazardous materials.
- **Regulatory and disclosure:** very low appetite for noncompliance with TSA directives and regulations, FRA rules, or SEC disclosure rules.
- **Operations continuity:** low appetite for disruption of train movement on more than one region.
- **Sensitive information:** low appetite for disclosure of SSI or personal information.
- **Growth and innovation (acquisitions, technology services, AI):** moderate appetite, provided risks are identified and funded before or at the time of the decision.

**Risk tolerance (measurable, per enterprise risk).** The highest residual risk level each enterprise risk may carry without a board-reported treatment plan. A risk above its threshold is **Outside tolerance** in the register.

| Enterprise risk | Tolerance threshold |
|---|---|
| ER-01 Rail operations disruption from cyber and technology events | Moderate |
| ER-02 Rail safety from technology (dispatch integrity, PTC, signals, crossings, detectors) | Low |
| ER-03 Third-party and concentration risk | Moderate |
| ER-04 Integration of acquired railroads | Moderate |
| ER-05 Regulatory and disclosure compliance (TSA, FRA, SEC, state) | Low |
| ER-06 Compromise of sensitive information (SSI, personal information, customer data) | Moderate |
| ER-07 Technology service line commitments (SL-1, SL-2) | Moderate |
| ER-08 Responsible use of AI | Moderate |
| ER-09 Financial reporting integrity and fraud | Low |

**Who can accept risk:**
| Residual level | Acceptance authority |
|---|---|
| Very Low, Low | Risk owner (vice president or director) with GRC concurrence |
| Moderate | CISO with the accountable executive |
| High | Executive risk committee (Chief Risk Officer, Chief Operating Officer, CIO, CISO, Chief Safety Officer, General Counsel), reported to the board safety, security, and risk committee |
| Very High | CEO and CFO jointly, reported to the board safety, security, and risk committee at its next meeting |

Rail safety risks (ER-02) at Moderate or above cannot be accepted without a dated treatment plan. Any acceptance expires after 12 months.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the rail sector threat picture (ransomware on dispatch and back-office systems, state actors pre-positioning in transportation OT, third-party concentration), the BIA (P05), the gap analysis (P03), and the Internal Audit assessment (P07).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial), and likelihood of adverse impact, combined with **Table G-5**.
3. **Rate impact.** **Table H-3**, calibrated to the BIA impact values (P05 section 3). Any plausible conflicting movement authority, unprotected crossing, or PIH release is rated Very High.
4. **Determine risk.** **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the tables, not assigned by hand.
5. **Integrate with ERM (NIST IR 8286 Rev. 1).**
   - Each cybersecurity risk is a row in this register, with an owner, a treatment, and a key risk indicator (KRI).
   - Each row is normalized into one of **9 enterprise risks (ER-01 to ER-09)** in the Chief Risk Officer's enterprise risk register, with an ERM category (operational, safety, strategic, compliance, financial).
   - **Aggregation rule:** an enterprise risk's exposure equals its highest constituent risk level, and the profile also reports how many constituent risks sit outside tolerance. This keeps one severe risk from being averaged away.
   - The enterprise risk profile (section 4) is what the board safety, security, and risk committee sees each quarter.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 11 |
| Moderate | 33 |
| Low | 18 |
| **Total** | **63** |

By threat source type: Structural 28, Adversarial 26, Accidental 7, Environmental 2.
By treatment: Mitigate 55, Accept 7, Avoid 1.
By status: In progress 39, Open 16, Closed (accepted) 7, Closed (avoided) 1.
**21 risks are outside tolerance** and each has a dated treatment plan; all 21 are board reported.

## 4. Enterprise risk profile (roll-up for the board)
| ID | Enterprise risk | ERM category | Risks | Very High | High | Moderate | Low | Exposure (highest) | Tolerance | Outside tolerance |
|---|---|---|---|---|---|---|---|---|---|---|
| ER-01 | Rail operations disruption from cyber and technology events | Operational | 16 | 1 | 4 | 8 | 3 | **Very High** | Moderate | 5 |
| ER-02 | Rail safety from technology | Safety | 9 | 0 | 3 | 4 | 2 | **High** | Low | 7 |
| ER-03 | Third-party and concentration risk | Operational | 9 | 0 | 2 | 5 | 2 | **High** | Moderate | 2 |
| ER-04 | Integration of acquired railroads | Strategic | 4 | 0 | 1 | 3 | 0 | **High** | Moderate | 1 |
| ER-05 | Regulatory and disclosure compliance | Compliance | 9 | 0 | 1 | 4 | 4 | **High** | Low | 5 |
| ER-06 | Compromise of sensitive information | Compliance and reputational | 6 | 0 | 0 | 2 | 4 | **Moderate** | Moderate | 0 |
| ER-07 | Technology service line commitments | Strategic | 4 | 0 | 0 | 2 | 2 | **Moderate** | Moderate | 0 |
| ER-08 | Responsible use of AI | Strategic and safety | 4 | 0 | 0 | 4 | 0 | **Moderate** | Moderate | 0 |
| ER-09 | Financial reporting integrity and fraud | Financial | 2 | 0 | 0 | 1 | 1 | **Moderate** | Low | 1 |

**Reading the profile:**
- **ER-01 (operations disruption)** carries the only Very High risk, enterprise ransomware on dispatch and back-office systems (R-001). PTC back office recovery (R-004) and the untested manual dispatch fallback for CTC territory (R-013) are the reasons a successful attack would last longer than the BIA allows.
- **ER-02 (rail safety)** has the lowest tolerance and three High risks, all about unauthorized control of OT: the corporate-to-OT directory trust (R-002), unpatched PTC back office servers (R-005), and shared CTC administrator accounts (R-006). Vital field logic and PTC enforcement limit the worst outcomes, which is why none is Very High.
- **ER-05 (regulatory and disclosure)** is outside tolerance because the materiality process has not been exercised with the current disclosure committee (R-017), the CR-10 CIP amendment was filed late (R-016), and the TSA 30-minute RSSM answer has no tested fallback (R-014).
- **ER-08 (AI)** is within tolerance, but only because the two safety inspection models are advisory and FRA-required human inspections continue (R-043, R-044).

## 5. Top risks (Very High and High)
| Risk ID | Risk | Level | Enterprise risk | Treatment | Owner | Due |
|---|---|---|---|---|---|---|
| R-001 | Ransomware encrypts dispatch, PTC back office, and business systems across the enterprise | Very High | ER-01 | Close acquisition gaps (POAM-018; POAM-001); PTC failover automation (POAM-006); OT logging (POAM-007); ransomware tabletop with the disclosure committee on 2026-11-18 (POAM-010) | CISO | 2027-03-31 |
| R-002 | Attacker pivots from corporate IT to the NOC operations zone through the legacy directory trust | High | ER-02 | Remove the trust (POAM-005) | Director of OT Security | 2026-12-31 |
| R-003 | Attacker enters through an acquired railroad's flat network and reaches enterprise systems | High | ER-04 | Restrict VPNs; EDR; SD-WAN and federation with each CAD migration (POAM-018; POAM-001) | Vice President, Integration Management Office | 2027-05-31 |
| R-004 | PTC back office cannot be recovered within the 4-hour RTO | High | ER-01 | Automated failover; third key custodian; retest (POAM-006) | Director of Train Control Systems | 2027-03-31 |
| R-005 | Known vulnerability exploited on unpatched PTC back office servers | High | ER-02 | Documented compensating measures in the CIP; vendor SLA (POAM-003) | PTC Back Office Manager | 2026-12-31 |
| R-006 | Shared CTC code server administrator accounts used to send unauthorized controls | High | ER-02 | Named PAM-vaulted accounts (POAM-004) | Director of OT Security | 2026-11-30 |
| R-010 | Crossing monitor vendor's modems used to reach a CTC field network | High | ER-03 | Disconnect 2 modems; vendor access through PAM (POAM-008) | Director of OT Security | 2027-01-31 |
| R-013 | Manual dispatch fallback for CTC territory fails | High | ER-01 | Exercise at the other 9 signaled railroads (POAM-020) | Vice President, Network Operations | 2027-06-30 |
| R-017 | A material incident is disclosed late or inaccurately | High | ER-05 | Merged playbook; tabletop 2026-11-18 (POAM-010) | General Counsel | 2026-11-30 |
| R-025 | Malicious code in a trusted CAD or PTC vendor release | High | ER-03 | SBOM terms; out-of-band hash checks | CISO | 2027-06-30 |
| R-048 | Zero-day in an internet-facing VPN or firewall | High | ER-01 | Retire legacy AQ edge devices (POAM-018); 72-hour emergency patch SLA | Director of Network Engineering | 2027-05-31 |
| R-062 | Takeover of an identity provider administrator account | High | ER-01 | Two-person administrative actions; identity threat detection | Director of Identity and Access Management | 2027-03-31 |

## 6. Themes from the 2026 analysis
1. **Acquisition integration (ER-04).** AQ-04 to AQ-06 run legacy dispatch on single servers, local directories, flat networks, and no EDR. These conditions raise the likelihood of enterprise ransomware (R-001, R-003), late terminations (R-063), and a day-long dispatch outage (R-015). The CR-10 CIP amendment was filed 118 days after closing against the 50-day limit (R-016). Treatment follows the CAD migration dates (2026-12-15, 2027-02-28, 2027-05-31). Future deals must pass a security and TSA filing gate (R-060).
2. **OT access hygiene (ER-02).** The corporate-to-OT directory trust (R-002), shared CTC accounts (R-006), default credentials on field devices (R-007), and the crossing monitor vendor's modems (R-010) are each a direct path to Critical Cyber Systems. All four are SD 1580/82-2022-01E Sec. III.C measures.
3. **Recovery and manual operations (ER-01).** The CAD meets its 2-hour RTO, but the PTC back office does not (R-004), manual CTC operations are untested on 9 of 11 signaled railroads (R-013), and the TSA RSSM answer has no tested fallback (R-014).
4. **Visibility in OT (ER-01).** 61% of OT log sources reach the SIEM (R-008), 88% of the OT inventory is complete (R-009), and 22% of field segments are outside passive detection (R-037).
5. **Disclosure (ER-05).** The disclosure committee has not exercised the materiality playbook since 3 members joined, and the CISA/TSA and SEC steps live in separate playbooks (R-017, R-054).
6. **AI (ER-08).** 13 use cases; 8 reviewed. The two safety inspection models were validated on Class I data, not short line track and equipment (R-043, R-044). The applicant screening tool faces Colorado and Illinois rules (R-045, R-059).

## 7. Treatment summary
- **Funded (2026 Q4 to 2027 Q2), about $7.4 million, approved by the executive risk committee on 2026-09-08:** acquired railroad network and identity integration ahead of the CAD migrations ($2.6M), OT passive detection and log forwarding ($1.3M), PTC back office failover automation and vendor services ($1.1M), CTC code line encrypting gateways on 3 Class II railroads ($780K), crossing monitor vendor access rebuild ($420K), backhaul diversity at 14 tower sites ($510K), manual operations exercises ($240K), SL-2 SOC 2 readiness ($310K), and AI local validation ($140K). Items map to the POA&M in P07.
- **Accepted (7):** R-023, R-029, R-030, R-031, R-049, R-050, R-061. Each is Low or Moderate residual with strong existing controls, accepted at the right level (section 1) and reviewed within 12 months.
- **Avoided (1):** R-047. Unapproved generative AI domains are blocked.
- **Very High risk R-001:** not accepted as is. The CEO and CFO approved the treatment plan and the residual target of High on 2026-09-08; the board safety, security, and risk committee reviewed it on 2026-09-10.

## 8. Board reporting
**Board safety, security, and risk committee (quarterly):** the enterprise risk profile (section 4), every Very High and High risk with its treatment status and KRI trend, risks outside tolerance, new risks since the last meeting, and risk acceptances made. The 2026-09-10 meeting received this report, the Internal Audit results (P07), and the regulatory roadmap (P03).
**Audit committee (quarterly):** Internal Audit results, SOX IT general control status (R-032), and the disclosure controls topics (R-017, R-054). The audit committee also reviews the annual Item 106 disclosure draft, which describes this process.
**Management:** the executive risk committee meets monthly and reviews KRIs for all risks outside tolerance.

## 9. Approval
- Executive risk committee: approved the register, treatments, and acceptances, 2026-09-08.
- CEO and CFO: approved the treatment plan and residual target for Very High risk R-001, 2026-09-08.
- Board safety, security, and risk committee: reviewed the enterprise risk profile, 2026-09-10.
- Next full review: June to July 2027, or sooner after a major change, incident, or acquisition. KRIs are refreshed quarterly.
