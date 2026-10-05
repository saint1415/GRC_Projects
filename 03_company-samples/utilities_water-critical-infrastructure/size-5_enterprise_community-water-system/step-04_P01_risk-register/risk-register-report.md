# Enterprise Risk Register Report: Cris Santos Company | Water and Wastewater Systems | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded parent of four state-regulated water utilities: 126 community water systems, about 9.6 million people served; FL, GA, NC, TN) |
| Size tier | Enterprise (12,000 employees) |
| Vertical | Water and Wastewater Systems |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) for each risk; NIST IR 8286 Rev. 1 for integration into enterprise risk management (ERM); NIST SP 800-82 Rev. 3 for OT threat events |
| Also satisfies | Cyber element evidence for the SDWA section 1433 risk and resilience assessments ("electronic, computer, or other automated systems (including the security of such systems)", 42 U.S.C. 300i-2(a)(1)(A)(ii)); input to the Reg S-K Item 106 description of risk management processes (17 CFR 229.106(b)) |
| Prepared | 2026-06-01 to 2026-07-31 by the GRC team for the CISO; updated 2026-08-28 with the independent assessment findings (P07) |
| Approved | Executive risk committee (chaired by the Chief Risk Officer), 2026-09-08; reviewed by the safety, environmental, and risk committee of the board, 2026-09-10 |

## 1. Scope and risk framing
**Scope.** All 126 community water systems and their OT (SCADA, PLCs, RTUs, telemetry, remote access), the enterprise IT estate (two clouds, two colocation data centers, about 640 sites), customer systems (CIS, AMI, portal), the two service lines (SL-1 and SL-2), the six acquired systems, and about 1,600 vendors (about 140 OT vendors and 11 bulk chemical suppliers). Business processes and impact values come from the enterprise BIA (P05). The GCR-WTSS is also covered at system level in the SSP (P02).

**Three lines.** Risk owners in operations, IT, and OT (first line) own and treat risks. The GRC team and the Chief Risk Officer (second line) run this method and roll risks up into the enterprise risk register. Internal Audit, with a co-sourced OT assessment firm (third line), tests controls independently (P07).

**Risk appetite (board-approved, 2026-02).** Qualitative statements set by the board:
- **Public health and safety:** very low appetite for technology-related events that could make water unsafe, cause a chemical release, or cut fire flow.
- **Regulatory and disclosure:** very low appetite for noncompliance with SDWA section 1433, the public notification rule, release reporting, or SEC disclosure rules.
- **Service continuity:** low appetite for disruption of treatment and distribution; moderate for business systems that have manual workarounds.
- **Customer information:** low appetite for unauthorized disclosure.
- **Growth and innovation (acquisitions, AI):** moderate appetite, provided risks are identified and funded before or at the time of the decision.

**Risk tolerance (measurable, per enterprise risk).** The highest residual risk level each enterprise risk may carry without a board-reported treatment plan. A risk above its threshold is **Outside tolerance** in the register.

| Enterprise risk | Tolerance threshold |
|---|---|
| ER-01 Public health and safety from OT compromise or failure | Low |
| ER-02 Disruption of water service and business operations | Moderate |
| ER-03 Compromise of customer and sensitive information | Moderate |
| ER-04 Third-party, supplier, and concentration risk | Moderate |
| ER-05 Integration of acquired systems | Moderate |
| ER-06 Regulatory and disclosure compliance | Low |
| ER-07 Financial reporting integrity and fraud | Low |
| ER-08 Responsible use of AI and data | Moderate |

**Who can accept risk:**
| Residual level | Acceptance authority |
|---|---|
| Very Low, Low | Risk owner (vice president or director) with GRC concurrence |
| Moderate | CISO with the accountable executive |
| High | Executive risk committee (Chief Risk Officer, COO, CIO, CISO, General Counsel), reported to the board's safety, environmental, and risk committee |
| Very High | CEO and CFO jointly, reported to the board committee at its next meeting |

Public health and safety risks (ER-01) at High or above cannot be accepted without a dated treatment plan. Any acceptance expires after 12 months.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, EPA's baseline information on malevolent acts for community water systems, CISA and water-sector information sharing center advisories (remote access and HMI attacks, internet-exposed OT devices), the BIA (P05), the gap analysis (P03), and the independent assessment (P07).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial), and likelihood of adverse impact, combined with **Table G-5**. Hardwired chemical feed limits and analyzer alarms lower the likelihood of adverse impact for OT events that target dosing.
3. **Rate impact.** **Table H-3**, calibrated to the BIA impact values (P05 section 3): public health, service, regulatory, and financial consequences.
4. **Determine risk.** **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the tables, not assigned by hand.
5. **Integrate with ERM (NIST IR 8286 Rev. 1).**
   - Each system-level cybersecurity risk is a row in this register, with an owner, a treatment, and a key risk indicator (KRI).
   - Each row is normalized into one of **8 enterprise risks (ER-01 to ER-08)** in the Chief Risk Officer's enterprise risk register, with an ERM category.
   - **Aggregation rule:** an enterprise risk's exposure equals its highest constituent risk level, and the profile also reports how many constituent risks sit outside tolerance. This keeps one severe risk from being averaged away.
   - The enterprise risk profile (section 4) is what the board committee sees each quarter.
6. **Feed the RRAs.** Rows that apply to a covered system are exported into that system's RRA cyber element, so the 86 RRAs use one consistent risk method.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 13 |
| Moderate | 32 |
| Low | 19 |
| **Total** | **65** |

By threat source type: Adversarial 33, Structural 24, Accidental 5, Environmental 3.
By treatment: Mitigate 58, Accept 6, Avoid 1.
By status: In progress 51, Open 8, Closed (accepted) 6.
**24 risks are outside tolerance** and each has a dated treatment plan. All 24 are reported to the board committee (`board_reported` = Yes).

## 4. Enterprise risk profile (roll-up for the board)
| ID | Enterprise risk | ERM category | Risks | Very High | High | Moderate | Low | Exposure (highest) | Tolerance | Outside tolerance |
|---|---|---|---|---|---|---|---|---|---|---|
| ER-01 | Public health and safety from OT compromise or failure | Operational and public safety | 15 | 0 | 5 | 7 | 3 | **High** | Low | 12 |
| ER-02 | Disruption of water service and business operations | Operational | 19 | 1 | 2 | 9 | 7 | **Very High** | Moderate | 3 |
| ER-03 | Compromise of customer and sensitive information | Compliance and reputational | 7 | 0 | 1 | 3 | 3 | **High** | Moderate | 1 |
| ER-04 | Third-party, supplier, and concentration risk | Operational | 6 | 0 | 2 | 4 | 0 | **High** | Moderate | 2 |
| ER-05 | Integration of acquired systems | Strategic | 3 | 0 | 1 | 2 | 0 | **High** | Moderate | 1 |
| ER-06 | Regulatory and disclosure compliance | Compliance | 6 | 0 | 2 | 2 | 2 | **High** | Low | 4 |
| ER-07 | Financial reporting integrity and fraud | Financial | 2 | 0 | 0 | 1 | 1 | **Moderate** | Low | 1 |
| ER-08 | Responsible use of AI and data | Strategic and operational | 7 | 0 | 0 | 4 | 3 | **Moderate** | Moderate | 0 |

**Reading the profile:**
- **ER-01 (public health and safety)** has the lowest tolerance and the most risks outside it (12). Its High risks are HMI takeover through vendor remote access at AQ-05 (R-001), undetected PLC logic changes (R-004), internet-exposed telemetry gateways (R-006), unsupported controllers and hosts (R-008), and state-sponsored pre-positioning (R-014). Hardwired chemical feed limits are the reason none of them is Very High.
- **ER-02 (service disruption)** carries the only Very High risk, enterprise ransomware that forces precautionary IT/OT disconnection in every region (R-002).
- **ER-06 (regulatory and disclosure)** is outside tolerance because 24 ERP review certifications are still due by 2026-12-26 (R-009) and the disclosure committee has never exercised an OT or public health scenario (R-007).
- **ER-05 (acquired systems)** has only 3 rows, but the acquisition gap also drives R-001, R-022, and R-031 in other enterprise risks.
- **ER-08 (AI)** is within tolerance today, but 4 of 11 use cases lack committee review and AI-001 has no drift monitoring (R-044, R-045).

## 5. Top risks (Very High and High)
| Risk ID | Risk | Level | Enterprise risk | Treatment | Owner | Due |
|---|---|---|---|---|---|---|
| R-002 | Ransomware encrypts enterprise IT and forces precautionary IT/OT disconnection in every region | Very High | ER-02 | EDR at AQ sites; IT/OT disconnect playbook tested in every region; annual enterprise ransomware exercise including the disclosure committee (POAM-014) | CISO | 2027-01-31 |
| R-001 | Attacker uses the always-on vendor remote desktop agent at AQ-05 to take over an HMI and change a chemical feed setpoint | High | ER-01 | Remove the agent; gateway; named HMI accounts (POAM-001) | Vice President, Integration Management Office | 2026-12-15 |
| R-003 | Attacker moves from an acquired system's flat network over the site VPN into regional networks | High | ER-05 | Restrict VPNs; SD-WAN and OT DMZ at AQ-04 to AQ-06 (POAM-001) | Vice President, Integration Management Office | 2027-01-31 |
| R-004 | A malicious or unauthorized PLC logic change at GCR goes undetected | High | ER-01 | Automated logic comparison; post-change verification (POAM-003) | Director of OT Engineering | 2027-03-31 |
| R-005 | A compromised integrator uses its access or delivers a malicious project file | High | ER-04 | Contract terms; attestation; hash verification (POAM-012) | Director of Third-Party Risk Management | 2027-03-31 |
| R-006 | Attacker signs in to an internet-reachable telemetry gateway with default credentials | High | ER-01 | 9 gateways fixed 2026-08-20; fleet-wide audit (POAM-009) | Director of Network Engineering | 2026-10-31 |
| R-007 | A material OT incident is disclosed late or inaccurately | High | ER-06 | OT scenario; COO on the committee; tabletop 2026-11-12 (POAM-014) | General Counsel | 2026-11-30 |
| R-008 | Attacker exploits an unsupported controller, HMI, or server | High | ER-01 | Replace GCR hosts (POAM-008); controller lifecycle 2027-2030 | Director of OT Engineering | 2027-06-30 |
| R-009 | ERP review certifications for 24 systems missed or made without current cyber findings | High | ER-06 | ERP sprint; cyber addenda (POAM-019) | Vice President, Resilience and Emergency Management | 2026-12-26 |
| R-010 | A wiper destroys a ROCC's SCADA servers and recovery outlasts manual operation | High | ER-02 | Automate the transfer runbook (POAM-010); rebuild media for each ROCC | Vice President, Gulf Coast Regional Operations | 2027-02-28 |
| R-014 | A state-sponsored actor pre-positions in ROCC networks | High | ER-01 | Quarterly OT threat hunts; monitoring extension (POAM-020) | Director of OT Security | 2027-06-30 |
| R-026 | A CIS breach exposes customer personal information for millions of accounts | High | ER-03 | Tokenize bank account numbers; egress anomaly detection | Chief Privacy Officer | 2027-03-31 |
| R-030 | Malicious code arrives in a trusted IT vendor software update | High | ER-04 | Staged rollout; SBOM requests for tier-1 vendors | CISO | 2027-06-30 |
| R-031 | A zero-day in an internet-facing edge device is exploited | High | ER-02 | Retire legacy AQ VPN appliances (POAM-001); 72-hour emergency patch SLA | Director of Network Engineering | 2027-01-31 |

## 6. Themes from the 2026 analysis
1. **Acquisition integration (ER-05 and ER-01).** AQ-04 to AQ-06 (about 139,300 people) still run legacy SCADA with vendor remote desktop tools, shared HMI accounts, flat networks, and site VPNs. These conditions drive R-001, R-003, R-022, and R-031. Going forward, deal approvals must include an OT site assessment before signing and integration funding in the deal model (R-060).
2. **Remote and third-party OT access (ER-01, ER-04).** 29 of 126 systems are not behind the OT remote access gateway, 6 of 23 integrators use their own tools at 11 legacy systems, and 31 of about 140 OT vendor contracts lack security terms (R-005, R-017).
3. **Legacy OT (ER-01).** About 1,150 of 6,800 controllers are past vendor support, and 38 OT servers and workstations run an unsupported operating system (R-008). A controller lifecycle program runs from 2027 to 2030; until then, exceptions carry documented compensating controls.
4. **Detection coverage (ER-01).** OT monitoring covers 31 systems serving about 84% of the population; the other 55 covered systems are unmonitored (R-013, R-014, R-037).
5. **Regulatory calendar (ER-06).** 24 ERP review certifications are due by 2026-12-26; 12 RRA reviews used EPA's small-system checklist for the cyber element, and AQ-05 and AQ-06 used their former owners' approaches (R-009).
6. **Disclosure readiness (ER-06).** The materiality playbook was built for data breaches and has no operations member (R-007). Item 106 statements are not yet tested before filing (R-050).
7. **AI (ER-08).** 11 use cases, 7 reviewed. AI-001 runs without drift monitoring (R-044), and a vendor collections feature (AI-006) was enabled without review (R-045).

## 7. Treatment summary
- **Funded (2026 Q4 to 2027 Q2), about $9.4 million:** AQ-04 to AQ-06 integration, including gateway enrollment, OT DMZs, and SD-WAN ($3.2M); OT monitoring extension, first wave of 20 systems ($2.1M); replacement of the 4 unsupported GCR hosts and the first 140 unsupported controllers ($1.9M); automated PLC logic comparison at the 5 ROCCs ($0.8M); backup control center transfer automation ($0.4M); fleet-wide telemetry gateway audit ($0.3M); integrator contract remediation and attestation program ($0.25M); AI drift monitoring ($0.2M); outside counsel for the disclosure tabletop ($0.05M); ERP sprint contractor support ($0.2M). Items map to the POA&M in P07.
- **Accepted (6):** R-033, R-034, R-038, R-048, R-061, R-063. Each is Low residual with strong existing controls, accepted at the right level (section 1) and reviewed within 12 months.
- **Avoided (1):** R-041. Unapproved generative AI domains are blocked at the proxy; staff use the approved enterprise tenant.
- **Very High risk R-002:** not accepted as is. The CEO and CFO approved the treatment plan and the residual target of High on 2026-09-08; the board committee reviewed it on 2026-09-10.

## 8. Board reporting
**Safety, environmental, and risk committee (quarterly):** the enterprise risk profile (section 4), every Very High and High risk with its treatment status and KRI trend, risks outside tolerance, new risks since the last meeting, risk acceptances, and the EPA certification calendar. The 2026-09-10 meeting received this report, the independent assessment results (P07), and the regulatory roadmap (P03).
**Audit committee (quarterly):** Internal Audit results, SOX IT general control status (R-049), and disclosure controls topics (R-007, R-050). The audit committee also reviews the annual Item 106 disclosure draft, which describes this process.
**Management:** the executive risk committee meets monthly and reviews KRIs for all risks outside tolerance.

## 9. Approval
- Executive risk committee: approved the register, treatments, and acceptances, 2026-09-08.
- CEO and CFO: approved the treatment plan and residual target for Very High risk R-002, 2026-09-08.
- Safety, environmental, and risk committee of the board: reviewed the enterprise risk profile, 2026-09-10.
- Next full review: June to July 2027, or sooner after a major change, incident, or acquisition. KRIs are refreshed quarterly.
