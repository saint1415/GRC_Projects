# Enterprise Risk Register Report: Cris Santos Company | Commercial Facilities | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded office and retail REIT: 140 properties in FL, TX, GA, NC, AZ, and CA; 112 owned, 28 managed) |
| Size tier | Enterprise (12,000 employees) |
| Vertical | Commercial Facilities |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) for each risk; NIST IR 8286 Rev. 1 for integration into enterprise risk management (ERM) |
| Also supports | CPG 2.0 goals 1.B and 2.B (C-COMMERCIAL-FACILITIES-R05); the Reg S-K Item 106 description of risk management processes (C-COMMERCIAL-FACILITIES-R04); the CCPA reasonable security duty and the 2027 CPPA cybersecurity audit (C-COMMERCIAL-FACILITIES-R03) |
| Prepared | 2026-06-01 to 2026-07-31 by the GRC team for the CISO; updated 2026-08-28 with Internal Audit findings (P07) |
| Approved | Executive risk committee (chaired by the Chief Risk Officer), 2026-09-08; reviewed by the risk committee of the board, 2026-09-10 |

## 1. Scope and risk framing
**Scope.** All systems that support building operations or hold personal information across the 140 properties, the three RSOCs, the two clouds and two colocation data centers, the 19 acquired properties, the TRS service lines (SL-1 and SL-2), and the roughly 3,100 vendors (420 with system access or data). Business processes and impact values come from the enterprise BIA (P05). The Building Automation and Access Control System (BAACS) is also covered at system level in the SSP (P02).

**Three lines.** Risk owners in the business, engineering, security operations, and IT (first line) own and treat risks. The GRC team and the Chief Risk Officer (second line) run this method and roll risks up into the enterprise risk register. Internal Audit (third line) tests controls independently (P07).

**Risk appetite (board-approved, 2026-02).** Qualitative statements set by the board:
- **Occupant safety and physical security:** very low appetite for technology-related harm to occupants or unsecured buildings.
- **Regulatory, contractual, and disclosure:** very low appetite for noncompliance with SEC disclosure rules, privacy laws, PCI DSS, or JV, lender, and SOC 2 client commitments.
- **Building operations continuity:** low appetite for disruption of building systems at more than one property at a time.
- **Personal information:** low appetite for unauthorized disclosure of tenant employee, visitor, or employee data.
- **Growth and innovation (acquisitions, AI, proptech):** moderate appetite, provided risks are identified and funded before or at the time of the decision.

**Risk tolerance (measurable, per enterprise risk).** The highest residual risk level each enterprise risk may carry without a board-reported treatment plan. A risk above its threshold is **Outside tolerance** in the register.

| Enterprise risk | Tolerance threshold |
|---|---|
| ER-01 Building operations disruption from cyber and technology events | Moderate |
| ER-02 Compromise of personal information (tenant employees, visitors, employees) | Moderate |
| ER-03 Third-party and concentration risk | Moderate |
| ER-04 Integration of acquired properties | Moderate |
| ER-05 Occupant safety and physical security from technology | Low |
| ER-06 Regulatory, contractual, and disclosure compliance | Low |
| ER-07 Financial reporting integrity and fraud | Low |
| ER-08 Responsible use of AI and surveillance technology | Moderate |

**Who can accept risk:**
| Residual level | Acceptance authority |
|---|---|
| Very Low, Low | Risk owner (vice president or director) with GRC concurrence |
| Moderate | CISO with the accountable executive |
| High | Executive risk committee (Chief Risk Officer, CIO, COO, CISO, General Counsel), reported to the board risk committee |
| Very High | CEO and CFO jointly, reported to the board risk committee at its next meeting |

Occupant-safety risks (ER-05) at High or above cannot be accepted without a dated treatment plan. Any acceptance expires after 12 months.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the Commercial Facilities threat picture (ransomware against building systems through integrators, access control tampering, third-party concentration), the BIA (P05), the gap analysis (P03), and the Internal Audit assessment (P07).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial), and likelihood of adverse impact, combined with **Table G-5**.
3. **Rate impact.** **Table H-3**, calibrated to the BIA impact values (P05 section 3).
4. **Determine risk.** **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the tables, not assigned by hand.
5. **Integrate with ERM (NIST IR 8286 Rev. 1).**
   - Each system-level cybersecurity risk is a row in this register, with an owner, a treatment, and a key risk indicator (KRI).
   - Each row is normalized into one of **8 enterprise risks (ER-01 to ER-08)** in the Chief Risk Officer's enterprise risk register, with an ERM category (operational, compliance, strategic, safety, financial).
   - **Aggregation rule:** an enterprise risk's exposure equals its highest constituent risk level, and the profile also reports how many constituent risks sit outside tolerance. This keeps one severe risk from being averaged away.
   - The enterprise risk profile (section 4) is what the board risk committee sees each quarter.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 9 |
| Moderate | 40 |
| Low | 15 |
| **Total** | **65** |

By threat source type: Adversarial 33, Accidental 17, Structural 13, Environmental 2.
By treatment: Mitigate 56, Accept 7, Avoid 2.
By status: In progress 54, Open 4, Closed (accepted) 7.
**25 risks are outside tolerance** and each has a dated treatment plan.

## 4. Enterprise risk profile (roll-up for the board)
| ID | Enterprise risk | ERM category | Risks | Very High | High | Moderate | Low | Exposure (highest) | Tolerance | Outside tolerance |
|---|---|---|---|---|---|---|---|---|---|---|
| ER-01 | Building operations disruption from cyber and technology events | Operational | 16 | 1 | 3 | 7 | 5 | **Very High** | Moderate | 4 |
| ER-02 | Compromise of personal information | Compliance and reputational | 9 | 0 | 1 | 6 | 2 | **High** | Moderate | 1 |
| ER-03 | Third-party and concentration risk | Operational | 5 | 0 | 3 | 2 | 0 | **High** | Moderate | 3 |
| ER-04 | Integration of acquired properties | Strategic | 5 | 0 | 1 | 4 | 0 | **High** | Moderate | 1 |
| ER-05 | Occupant safety and physical security from technology | Safety | 10 | 0 | 0 | 8 | 2 | **Moderate** | Low | 8 |
| ER-06 | Regulatory, contractual, and disclosure compliance | Compliance | 10 | 0 | 1 | 6 | 3 | **High** | Low | 7 |
| ER-07 | Financial reporting integrity and fraud | Financial | 2 | 0 | 0 | 1 | 1 | **Moderate** | Low | 1 |
| ER-08 | Responsible use of AI and surveillance technology | Strategic and compliance | 8 | 0 | 0 | 6 | 2 | **Moderate** | Moderate | 0 |

**Reading the profile:**
- **ER-01 (building operations disruption)** carries the only Very High risk, portfolio-wide ransomware on the BAS (R-001). The acquired properties (R-003, ER-04) and the Platform B and C recovery gap (R-011) are the main reasons its likelihood and impact are not lower.
- **ER-05 (occupant safety)** has no High risk but the lowest tolerance, so 8 Moderate risks sit outside it: door schedule tampering (R-010), unapproved BAS program changes (R-009), stale tenant credentials (R-016), excess platform administrators (R-045), RSOC failover (R-012), and occupant notification (R-051), among others.
- **ER-06 (regulatory and disclosure)** is outside tolerance mainly because the SEC materiality process has not been exercised for a building-outage scenario (R-017) and the first CPPA cybersecurity audit period starts on 2027-01-01 (R-018).
- **ER-03 (third parties)** carries three High risks: platform vendor concentration (R-005), malicious vendor updates (R-030), and a breach at a vendor holding company data (R-037).
- **ER-08 (AI and surveillance)** is within tolerance today, but 5 of 12 use cases lack committee review and one may be ADMT for a significant decision under the CPPA rules (R-021), so the rating depends on the reviews due 2026-12-31.

## 5. Top risks (Very High and High)
| Risk ID | Risk | Level | Enterprise risk | Treatment | Owner | Due |
|---|---|---|---|---|---|---|
| R-001 | Ransomware encrypts BAS supervisory servers and engineering workstations across several regions | Very High | ER-01 | Remove Integrator C tool (POAM-003); segment acquired properties (POAM-004); OT logging (POAM-005); Platform C backups and Platform B restore fix (POAM-008); building-outage tabletop with the disclosure committee (POAM-012) | CISO | 2027-03-31 |
| R-002 | Exfiltration of credential records, visitor ID scans, and employee data during a ransomware attack | High | ER-02 | Purge visitor records beyond standard (POAM-019); egress rules for the data platform and PACS exports; CPPA audit readiness (POAM-020) | Chief Privacy Officer | 2027-03-31 |
| R-003 | Attacker enters through Integrator C's always-on tool and moves over the seller site VPN | High | ER-04 | Move Integrator C to the OT gateway (POAM-003); interim access lists, then OT zones and SD-WAN (POAM-004) | Vice President, Integration Management Office | 2026-11-30 |
| R-005 | Platform vendor outage or compromise stops credential administration and video at 121 properties | High | ER-03 | 2-hour administration recovery commitment, 24-hour incident notice, degraded-mode procedure, exit plan (POAM-011) | Director of Third-Party Risk Management | 2027-03-31 |
| R-006 | Exploit of unsupported OS on Platform C servers or Platform B workstations | High | ER-01 | Replace in the migration and refresh; exceptions with compensating controls (POAM-007) | Senior Vice President, Engineering | 2027-06-30 |
| R-011 | Platform B and C supervisory servers cannot be rebuilt within RTO | High | ER-01 | Platform C backups and program escrow; Platform B restore automation; quarterly tests (POAM-008) | Senior Vice President, Engineering | 2027-03-31 |
| R-017 | A material incident is disclosed late or inaccurately because the materiality process fails for a building outage | High | ER-06 | Update the worksheet; brief new members; tabletop 2026-11-17 (POAM-012) | General Counsel | 2026-11-30 |
| R-030 | Malicious code in a trusted vendor update (BAS software, PACS firmware, tenant app libraries) | High | ER-03 | Firmware hash verification; SBOM requests for tier-1 OT vendors | CISO | 2027-06-30 |
| R-037 | A vendor holding company data (visitor management, payroll, property management) suffers a breach | High | ER-03 | Clear overdue reassessments; 72-hour notice terms at renewal (POAM-011) | Director of Third-Party Risk Management | 2027-03-31 |
| R-040 | Zero-day in an internet-facing edge device is exploited | High | ER-01 | Retire seller VPN concentrators with the SD-WAN migration (POAM-004); 72-hour emergency patch standard | Director of Network Engineering | 2027-03-31 |

## 6. Themes from the 2026 analysis
1. **Acquisition integration (ER-04).** The 19 properties acquired in November 2025 run Platform C on an unsupported OS with no backups, a legacy PACS, flat networks, and Integrator C's always-on remote tool, and send no logs to the SIEM. These conditions raise the likelihood of portfolio-wide ransomware (R-001, R-003), unrecoverable servers (R-011), and undetected activity (R-008, R-065). Treatment runs to 2027-06-30. Going forward, deal approvals must include OT due diligence and integration funding (R-058).
2. **OT visibility at scale (ER-01).** The OT inventory is about 82% complete, passive monitoring covers 54 of 140 properties, and Platform B and C logs do not reach the SIEM (R-007, R-008). Testing found default passwords on 7 of 60 sampled OT devices (R-014, new from P07).
3. **Third-party concentration (ER-03).** One platform vendor runs PACS and video at 121 properties with a recovery commitment that does not meet the BIA (R-005). 9 integrators hold privileged OT access (R-015), and 11 of 48 tier-1 vendor reassessments are overdue (R-037).
4. **Disclosure and privacy compliance (ER-06).** The materiality playbook has not been exercised for a building outage (R-017). The CPPA cybersecurity audit period starts 2027-01-01 and Internal Audit's independence for the OT standard is limited (R-018). No CPPA risk assessment has been completed yet (R-020).
5. **AI and surveillance (ER-08).** 12 use cases; 7 reviewed. The face verification pilot (R-022, R-023), tailgating alerts that fall unevenly on accessible lanes (R-024), vendor training on company video (R-025), the officer scheduling tool (R-021), and patrol analytics (R-060) need decisions. The resume screening feature stays off (R-061, treatment Avoid).
6. **Credential lifecycle (ER-05).** About 14,200 active badges have not been used in more than 90 days (R-016), and the access control platform has 61 full administrators (R-045).

## 7. Treatment summary
- **Funded (2026 Q4 to 2027 Q2), about $11.8 million:** Platform C replacement and migration ($4.6M), OT zones and SD-WAN at the acquired properties ($1.9M), legacy PACS migration ($1.4M), passive OT monitoring at 86 more properties and OT log onboarding ($1.7M), Platform B workstation refresh and restore automation ($1.1M), access control administrator role redesign and credential auto-suspend ($0.3M), co-sourced OT assessment and CPPA audit readiness ($0.5M), and outside counsel for the disclosure tabletop ($0.05M) and CPPA risk assessments ($0.25M). Items map to the POA&M in P07.
- **Accepted (7):** R-013, R-046, R-048, R-050, R-052, R-063, R-064. Each is Low or Moderate residual with existing controls, accepted at the right level (section 1) and reviewed within 12 months.
- **Avoided (2):** R-028, R-061. Unapproved generative AI domains are blocked, and AI resume screening stays disabled until review.
- **Very High risk R-001:** not accepted as is. The CEO and CFO approved the treatment plan and the residual target of High on 2026-09-08; the board risk committee reviewed it on 2026-09-10.

## 8. Board reporting
**Risk committee of the board (quarterly):** the enterprise risk profile (section 4), every Very High and High risk with its treatment status and KRI trend, risks outside tolerance, new risks since the last meeting, and risk acceptances made. The 2026-09-10 meeting received this report, the Internal Audit results (P07), and the regulatory roadmap (P03).
**Audit committee (quarterly):** Internal Audit results, SOX IT general control status (R-033), disclosure controls topics (R-017, R-019), and the CPPA cybersecurity audit plan (R-018). The audit committee also reviews the annual Item 106 disclosure draft, which describes this process.
**Management:** the executive risk committee meets monthly and reviews KRIs for all risks outside tolerance and the integration status of the acquired properties (R-059).

## 9. Approval
- Executive risk committee: approved the register, treatments, and acceptances, 2026-09-08.
- CEO and CFO: approved the treatment plan and residual target for Very High risk R-001, 2026-09-08.
- Risk committee of the board: reviewed the enterprise risk profile, 2026-09-10.
- Next full review: June to July 2027, or sooner after a major change, incident, or acquisition. KRIs are refreshed quarterly.
