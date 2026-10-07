# Enterprise Risk Register Report: Cris Santos Company | Government Services and Facilities | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded facilities support contractor operating about 2,134 government buildings in 8 states and DC) |
| Size tier | Enterprise (12,000 employees) |
| Vertical | Government Services and Facilities |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) for each risk, with OT threats informed by NIST SP 800-82 Rev. 3; NIST IR 8286 Rev. 1 for integration into enterprise risk management (ERM) |
| Also satisfies | Risk assessment under the state cybersecurity exhibits (SP 800-53 RA-3); input to the Reg S-K Item 106 description of risk management processes (17 CFR 229.106(b)) |
| Prepared | 2026-06-01 to 2026-07-31 by the GRC team for the CISO; updated 2026-08-28 with Internal Audit findings (P07) |
| Approved | Executive risk committee (chaired by the Chief Risk Officer), 2026-09-08; reviewed by the risk committee of the board, 2026-09-10 |

## 1. Scope and risk framing
**Scope.** All systems that hold customer or personal data or support tier-1 processes: the IBOP and its OT edge at about 1,420 buildings, the Facility Services Portal, the two cloud estates and two colocation data centers, corporate systems, the three ROCs, the two acquired businesses (AQ-1 and AQ-2), and the roughly 2,600 subcontractors and suppliers (about 340 with remote or data access). Business processes and impact values come from the enterprise BIA (P05). The IBOP is also covered at system level in the SSP (P02).

**What is out of scope.** GSA's own building systems on the GSA Building Systems Network. GSA owns, authorizes, and monitors them. The register covers only the company's part at federal buildings: its people, PIV cards, procedures, and the data it holds.

**What makes this company different.** It does not own the buildings or the field equipment. Its largest risks come from operating other people's building systems at scale: one platform reaches 1,420 government buildings, so a single intrusion can open doors or change HVAC in many places at once. A failure can harm people, not only leak data, and it can trigger customer notice clocks, state reporting by the customers, and an SEC materiality decision in the same week.

**Three lines.** Risk owners in the segments, operations, and IT (first line) own and treat risks. The GRC team and the Chief Risk Officer (second line) run this method and roll risks up into the enterprise risk register. Internal Audit (third line) tests controls independently (P07).

**Risk appetite (board-approved, 2026-02).** Qualitative statements set by the board:
- **Physical safety and security of customer buildings:** very low appetite for technology events that could unlock doors, disable life-safety supervision, or create unsafe building conditions.
- **Government contract and regulatory compliance:** very low appetite for breaching FAR clauses, customer security terms, CJIS or FERPA obligations, or SEC disclosure rules. Federal and state eligibility is the company's license to operate.
- **Service continuity:** low appetite for loss of ROC monitoring or access administration.
- **Customer and personal data:** low appetite for unauthorized disclosure of cardholder, biometric, student, employee, or CUI data.
- **Growth and innovation (acquisitions, AI, analytics):** moderate appetite, provided risks are identified and funded before or at the time of the decision.

**Risk tolerance (measurable, per enterprise risk).** The highest residual risk level each enterprise risk may carry without a board-reported treatment plan. A risk above its threshold is **Outside tolerance** in the register.

| Enterprise risk | Tolerance threshold |
|---|---|
| ER-01 Physical safety and security of customer buildings from cyber and OT events | Low |
| ER-02 Service delivery disruption (ROCs, IBOP, FSP) | Moderate |
| ER-03 Compromise of customer and personal data | Moderate |
| ER-04 Third-party, subcontractor, and supply chain risk | Moderate |
| ER-05 Integration of acquired businesses | Moderate |
| ER-06 Government contract and regulatory compliance | Low |
| ER-07 Financial reporting, disclosure, and fraud | Low |
| ER-08 Responsible use of AI and biometrics | Moderate |

**Who can accept risk:**
| Residual level | Acceptance authority |
|---|---|
| Very Low, Low | Risk owner (vice president or director) with GRC concurrence |
| Moderate | CISO with the accountable executive |
| High | Executive risk committee (Chief Risk Officer, Chief Operating Officer, CIO, CISO, General Counsel), reported to the board risk committee |
| Very High | CEO and CFO jointly, reported to the board risk committee at its next meeting |

Risks in ER-01 (physical safety) at High or above cannot be accepted without a dated treatment plan. Any acceptance expires after 12 months.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the OT threat discussion in SP 800-82 Rev. 3, CISA advisories for PACS and BAS products, the BIA (P05), the gap analysis (P03), interviews with segment and operations leaders, site sampling visits (2026-06-15 to 2026-07-17), and the Internal Audit assessment (P07).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial), and likelihood of adverse impact, combined with **Table G-5**.
3. **Rate impact.** **Table H-3**, calibrated to the BIA impact categories (P05 section 3), including safety and physical security.
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
| High | 11 |
| Moderate | 35 |
| Low | 17 |
| **Total** | **64** |

By threat source type: Adversarial 29, Structural 24, Accidental 8, Environmental 3.
By treatment: Mitigate 56, Accept 6, Avoid 2.
By status: In progress 43, Open 13, Closed (accepted) 6, Closed (avoided) 2.
**29 risks are outside tolerance** and each has a dated treatment plan.

## 4. Enterprise risk profile (roll-up for the board)
| ID | Enterprise risk | ERM category | Risks | Very High | High | Moderate | Low | Exposure (highest) | Tolerance | Outside tolerance |
|---|---|---|---|---|---|---|---|---|---|---|
| ER-01 | Physical safety and security of customer buildings from cyber and OT events | Operational and safety | 14 | 1 | 3 | 10 | 0 | **Very High** | Low | 14 |
| ER-02 | Service delivery disruption (ROCs, IBOP, FSP) | Operational | 9 | 0 | 2 | 5 | 2 | **High** | Moderate | 2 |
| ER-03 | Compromise of customer and personal data | Compliance and reputational | 8 | 0 | 0 | 4 | 4 | **Moderate** | Moderate | 0 |
| ER-04 | Third-party, subcontractor, and supply chain risk | Operational | 4 | 0 | 2 | 1 | 1 | **High** | Moderate | 2 |
| ER-05 | Integration of acquired businesses | Strategic | 6 | 0 | 2 | 4 | 0 | **High** | Moderate | 2 |
| ER-06 | Government contract and regulatory compliance | Compliance | 11 | 0 | 1 | 6 | 4 | **High** | Low | 7 |
| ER-07 | Financial reporting, disclosure, and fraud | Financial | 6 | 0 | 1 | 1 | 4 | **High** | Low | 2 |
| ER-08 | Responsible use of AI and biometrics | Strategic and compliance | 6 | 0 | 0 | 4 | 2 | **Moderate** | Moderate | 0 |

**Reading the profile:**
- **ER-01 (physical safety)** carries the only Very High risk, a multi-building intrusion through the IBOP (R-001). Its tolerance is Low, so every one of its 14 risks is outside tolerance until treated; this is deliberate, because the board does not accept Moderate risk of doors opening at courthouses or public safety buildings.
- **ER-05 (acquisitions)** holds the risk most likely to start an incident: AQ-1's legacy remote-support tool (R-002), which is also the P08 scenario. Testing added R-058 (vendor default credentials at AQ sites).
- **ER-06 (government contracts)** is outside tolerance mainly because of supply chain screening (R-017, R-018), CUI handling (R-023), customer notice clocks (R-024), and CJIS training lapses (R-031). Loss of federal eligibility would affect the $1.73 billion Federal Facilities segment.
- **ER-07 (disclosure)** is outside tolerance because the materiality playbook has never been run for an OT incident with physical safety effects (R-025).
- **ER-08 (AI)** is within tolerance today because the 1:N face identification request was declined (R-045) and resume ranking is off (R-049), but local bias testing for the face verification pilots is still due (R-044).

## 5. Top risks (Very High and High)
| Risk ID | Risk | Level | Enterprise risk | Treatment | Owner | Due |
|---|---|---|---|---|---|---|
| R-001 | Intruder gains remote access to the IBOP and unlocks doors or changes HVAC at many customer buildings at once | Very High | ER-01 | Retire the AQ-1 tool (POAM-001); OT monitoring to 95% (POAM-005); credential sweep (POAM-003); OT tabletop with the disclosure committee (POAM-013) | CISO | 2027-06-30 |
| R-002 | Attacker uses AQ-1's legacy always-on remote-support tool to reach access control and video at AQ-1 sites | High | ER-05 | Migrate 142 sites to the OT gateway and uninstall the tool; weekly agent inventory meanwhile (POAM-001) | Vice President, Integration Management Office | 2027-01-31 |
| R-004 | Default or shared credentials on field devices let an attacker change programs or video | High | ER-01 | Credential sweep, AQ sites first; commissioning gate (POAM-003; POAM-004) | Director of OT Security | 2026-12-31 |
| R-006 | Ransomware encrypts IBOP servers and corporate systems across the ROCs | High | ER-02 | PACS failover automation (POAM-007); EDR on AQ-2 endpoints; annual ransomware exercise | CISO | 2027-01-31 |
| R-011 | OT intrusion goes undetected at the 550 buildings without OT sensors | High | ER-01 | Deploy sensors, AQ sites first (POAM-005) | Director of OT Security | 2027-06-30 |
| R-017 | Covered telecommunications or video equipment in company use (AQ-1 offices or spares) | High | ER-06 | Finish AQ-1 screening; report within 1 business day if covered; replace (POAM-010) | Vice President, Government Contracts Compliance | 2026-11-30 |
| R-019 | A subcontractor with remote access is compromised and used to reach customer OT | High | ER-04 | Security reviews and subcontract addendum (POAM-012) | Director of Third-Party Risk Management | 2027-03-31 |
| R-021 | A malicious or vulnerable PACS or BAS software update spreads to all tenants | High | ER-04 | 7-day staging for major releases; vendor attestation at renewal | Chief Technology Officer | 2027-03-31 |
| R-025 | A material incident is disclosed late or inaccurately because the playbook lacks OT and physical-safety factors | High | ER-07 | Update playbook; tabletop 2026-11-19 (POAM-013) | General Counsel | 2026-12-15 |
| R-027 | An edge gateway or VPN zero-day is exploited at scale | High | ER-01 | 72-hour emergency patch SLA; firmware compliance at AQ-1 sites (POAM-016) | Director of OT Security | 2027-06-30 |
| R-040 | A privileged cloud administrator account is compromised | High | ER-02 | Session anomaly detection for PAM | Director of Identity and Access Management | 2027-03-31 |
| R-058 | Vendor default credentials found during testing are used to change programs or delete video | High | ER-05 | Enterprise credential sweep (POAM-003) | Director of OT Security | 2026-12-31 |

## 6. Themes from the 2026 analysis
1. **Remote access into government OT is the weak point (ER-01, ER-05).** The AQ-1 legacy tool (R-002), default credentials (R-004, R-058), flat customer networks (R-005), and blind spots in OT monitoring (R-011) are what turn a single foothold into the Very High multi-building scenario (R-001). Closing POAM-001, POAM-003, and POAM-005 is the main treatment for the whole enterprise risk.
2. **Integrity of door and setpoint changes.** The company plans first for someone changing what buildings do, not for data theft. That is why the IBOP adds High-baseline integrity controls (P02 section 6) and why the controller program repository matters (R-010).
3. **Supply chain eligibility (ER-06).** The FAR clauses prohibit the company's own use of covered equipment (52.204-25(b)(2)) and set 1- and 3-business-day reporting clocks. AQ-1's offices and spares are the open exposure (R-017, R-055).
4. **Disclosure readiness (ER-07).** An OT incident that unlocks doors at public buildings could be material even with little financial loss, because of customer contracts and reputation. The playbook does not yet say so (R-025).
5. **AI and biometrics (ER-08).** Face verification pilots began on customer orders before committee review; local bias testing is due (R-044). The 1:N request was declined (R-045).
6. **Acquired businesses (ER-05).** ER-05 holds 6 risks (R-002, R-003, R-054, R-058, R-060, R-061), two of them High, and AQ legacy conditions also raise the likelihood of R-001, R-004, R-011, and R-027. Deal approvals now require security due diligence and integration funding (R-061; POL-01 4.10).

## 7. Treatment summary
- **Funded (2026 Q4 to 2027 Q2), about $9.6 million:** OT network sensors at 550 buildings ($3.4M), AQ-1 site migration to the OT gateway ($2.1M), AQ-2 campus migration to the IBOP ($1.2M), cellular backup for life-safety sites ($0.9M), GovRAMP verification for the FSP ($0.8M), field device credential sweep ($0.6M), PACS failover automation ($0.45M), FIDO2 keys for all ROC roles ($0.15M), and outside counsel for the disclosure tabletop ($0.04M). Items map to the POA&M in P07.
- **Accepted (6):** R-014, R-037, R-038, R-043, R-052, R-063. Each is Low or Very Low residual with existing controls, accepted at the right level (section 1) and reviewed within 12 months.
- **Avoided (2):** R-045 and R-049. The company declined to configure 1:N face identification of the public, and AI resume ranking is disabled until review.
- **Very High risk R-001:** not accepted. The CEO and CFO approved the treatment plan and a residual target of Moderate on 2026-09-08; the board risk committee reviewed it on 2026-09-10. Interim measure: the SOC checks weekly that AQ-1 agents are disabled outside approved service windows.

## 8. Board reporting
**Risk committee of the board (quarterly):** the enterprise risk profile (section 4), every Very High and High risk with its treatment status and KRI trend, risks outside tolerance (29 at this report), new risks since the last meeting, and risk acceptances. The 2026-09-10 meeting received this report, the Internal Audit results (P07), and the compliance roadmap (P03).
**Audit committee (quarterly):** Internal Audit results, SOX IT general control status (R-043), and disclosure controls topics (R-025, R-062). The audit committee also reviews the annual Item 106 disclosure draft, which describes this process.
**Management:** the executive risk committee meets monthly and reviews KRIs for all risks outside tolerance.

## 9. Approval
- Executive risk committee: approved the register, treatments, and acceptances, 2026-09-08.
- CEO and CFO: approved the treatment plan and residual target for Very High risk R-001, 2026-09-08.
- Risk committee of the board: reviewed the enterprise risk profile, 2026-09-10.
- Next full review: June to July 2027, or sooner after a major change, incident, acquisition, or new contract type. KRIs are refreshed quarterly.
