# Enterprise Risk Register Report: Cris Santos Company | Dams | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded hydroelectric generation company: 46 developments, 63 dams, 8,640 MW in GA, AL, NC, SC, TN, and VA; headquarters in Florida) |
| Size tier | Enterprise (12,000 employees) |
| Vertical | Dams |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) for each risk; NIST IR 8286 Rev. 1 for integration into enterprise risk management (ERM) |
| Also satisfies | FERC Security Program Form 3 Questions 23, 29, and 30 (threat assessment, enterprise all-hazards risk strategy, periodic risk assessments); CIP-013-2 R1.1 supply chain risk identification; input to the Reg S-K Item 106 description of risk management processes |
| Prepared | 2026-06-01 to 2026-07-31 by the GRC team for the CISO; updated 2026-08-28 with Internal Audit findings (P07) |
| Approved | Executive risk committee (chaired by the Chief Risk Officer), 2026-09-08; reviewed by the safety, risk, and reliability committee of the board, 2026-09-10 |

## 1. Scope and risk framing
**Scope.** All systems and processes in the enterprise BIA (P05): the HFCDMS at HOC-A, HOC-B, and the 35 HOC-operated developments (also covered at system level in the P02 SSP); the 9 Piedmont developments; the two service lines (SL-1 contract operations and SL-2 dam safety monitoring); the two clouds, two colocation data centers, and SaaS (P04); and about 1,100 vendors (240 with system or data access, 58 with remote paths into OT).

**What is different about a dam operator's register.** Most cyber risk registers measure money and data. Here the worst outcomes are physical: an uncontrolled release toward a downstream community, or loss of gate control during a flood. Impact ratings use the P05 safety column first. A risk that can plausibly cause harm downstream is rated Very High impact even when its dollar cost is modest.

**Three lines.** Risk owners in operations, dam safety, IT, and the service lines (first line) own and treat risks. The GRC team, the NERC compliance team, and the Chief Risk Officer (second line) run this method and roll risks up into the enterprise risk register. Internal Audit, with a co-sourced OT specialist firm (third line), tests controls independently (P07).

**Risk appetite (board-approved, 2026-02).**
- **Public safety:** very low appetite for any technology-related risk to people downstream or on project lands.
- **Regulatory:** very low appetite for NERC CIP violations, FERC dam safety or security findings, or SEC disclosure failures.
- **Generation and grid reliability:** low appetite for loss of HOC control or failure of grid obligations (blackstart, real-time data).
- **Sensitive information:** low appetite for disclosure of CEII, BCSI, or security documents.
- **Growth (acquisitions, service lines, AI):** moderate appetite, provided risks are identified and funded at the time of the decision.

**Risk tolerance (measurable, per enterprise risk).** The highest residual risk level each enterprise risk may carry without a board-reported treatment plan. A risk above its threshold is **Outside tolerance** in the register.

| Enterprise risk | Tolerance threshold |
|---|---|
| ER-01 Public safety from loss of control of water-retaining features | Low |
| ER-02 Generation and grid reliability disruption | Moderate |
| ER-03 Regulatory compliance (NERC CIP, FERC dam safety and security) | Low |
| ER-04 Third-party and supply chain concentration | Moderate |
| ER-05 Integration of acquired assets (Piedmont) | Moderate |
| ER-06 Protection of sensitive information (CEII, BCSI, personal data) | Moderate |
| ER-07 Service line client commitments (SL-1, SL-2) | Moderate |
| ER-08 Financial reporting and disclosure integrity | Low |
| ER-09 Responsible use of AI | Moderate |

**Who can accept risk:**
| Residual level | Acceptance authority |
|---|---|
| Very Low, Low | Risk owner (vice president or director) with GRC concurrence |
| Moderate | CISO with the accountable executive |
| High | Executive risk committee (Chief Risk Officer, COO, CIO, CISO, General Counsel, Chief Compliance Officer), reported to the safety, risk, and reliability committee |
| Very High | CEO and CFO jointly, reported to the safety, risk, and reliability committee at its next meeting |

Public safety risks (ER-01) at High or above cannot be accepted without a dated treatment plan. Any acceptance expires after 12 months. NERC CIP noncompliance cannot be accepted as a risk; it must be mitigated and, where required, self-reported.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E; the energy and dams sector threat picture (state actors pre-positioning in OT, ransomware in IT, vendor remote access); the BIA (P05); the gap analysis (P03); the Internal Audit assessment (P07); the Section 9 determinations; and the Group 1 Vulnerability Assessments.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial), and likelihood of adverse impact, combined with **Table G-5**.
3. **Rate impact.** **Table H-3**, calibrated to the BIA impact values (P05 section 3). Downstream safety consequences are rated Very High.
4. **Determine risk.** **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the tables, not assigned by hand.
5. **Integrate with ERM (NIST IR 8286 Rev. 1).**
   - Each system-level risk is a row in this cybersecurity risk register, with an owner, a treatment, and a key risk indicator (KRI).
   - Each row is normalized into one of **9 enterprise risks (ER-01 to ER-09)** in the Chief Risk Officer's enterprise risk register, with an ERM category.
   - **Aggregation rule:** an enterprise risk's exposure equals its highest constituent risk level, and the profile also reports how many constituent risks sit outside tolerance. One severe risk is never averaged away.
   - The enterprise risk profile (section 4) is what the board committee sees each quarter.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 17 |
| Moderate | 34 |
| Low | 13 |
| Very Low | 0 |
| **Total** | **65** |

By threat source type: Adversarial 25, Structural 25, Accidental 13, Environmental 2.
By treatment: Mitigate 55, Accept 8, Avoid 2.
By status: In progress 35, Open 21, Closed (accepted) 8, Closed (avoided) 1.
**30 risks are outside tolerance** and each has a dated treatment plan.

## 4. Enterprise risk profile (roll-up for the board)
| ID | Enterprise risk | ERM category | Risks | Very High | High | Moderate | Low | Very Low | Exposure (highest) | Tolerance | Outside tolerance |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ER-01 | Public safety from loss of control of water-retaining features | Safety | 14 | 0 | 5 | 8 | 1 | 0 | **High** | Low | 13 |
| ER-02 | Generation and grid reliability disruption | Operational | 13 | 0 | 4 | 7 | 2 | 0 | **High** | Moderate | 4 |
| ER-03 | Regulatory compliance (NERC CIP, FERC dam safety and security) | Compliance | 6 | 0 | 1 | 3 | 2 | 0 | **High** | Low | 4 |
| ER-04 | Third-party and supply chain concentration | Operational | 7 | 0 | 1 | 4 | 2 | 0 | **High** | Moderate | 1 |
| ER-05 | Integration of acquired assets (Piedmont) | Strategic | 5 | 1 | 2 | 2 | 0 | 0 | **Very High** | Moderate | 3 |
| ER-06 | Protection of sensitive information (CEII, BCSI, personal data) | Compliance and reputational | 5 | 0 | 1 | 2 | 2 | 0 | **High** | Moderate | 1 |
| ER-07 | Service line client commitments (SL-1, SL-2) | Strategic | 6 | 0 | 2 | 4 | 0 | 0 | **High** | Moderate | 2 |
| ER-08 | Financial reporting and disclosure integrity | Financial | 4 | 0 | 1 | 1 | 2 | 0 | **High** | Low | 2 |
| ER-09 | Responsible use of AI | Strategic and safety | 5 | 0 | 0 | 3 | 2 | 0 | **Moderate** | Moderate | 0 |

**Reading the profile:**
- **ER-05 (Piedmont integration)** carries the only Very High risk: an attacker using the legacy VPN or an always-on vendor connection to operate gates at PD-04 or PD-06 (R-003). It is the scenario in the P08 runbook.
- **ER-01 (public safety)** has the lowest tolerance and the most risks outside it. Its High risks come from three places: monitoring coverage below the HOC (R-002, R-008), legacy equipment (R-006), and undocumented vendor paths (R-054), plus the compound flood-and-cyber event (R-018).
- **ER-03 (regulatory)** is outside tolerance because of three potential CIP noncompliance issues self-reported to SERC (R-051, with the late access removal also tracked as R-056) and the late Group 1 security documents (R-052).
- **ER-07 (service lines)** has two High risks that affect clients' dams, not the company's: DSMS threshold changes without change control (R-042) and shared COC credentials at 6 client endpoints (R-043).
- **ER-08 (disclosure)** is outside tolerance mainly until the disclosure committee exercises an OT and dam safety scenario on 2026-11-18 (R-047); business email compromise of settlement payments (R-050) is the other risk above its Low threshold.

## 5. Top risks (Very High and High)
| Risk ID | Risk | Level | Enterprise risk | Treatment | Owner | Due |
|---|---|---|---|---|---|---|
| R-001 | Ransomware encrypts corporate IT (ERP, email, scheduling platform) and the attackers try to reach the OT DMZs | High | ER-02 | Annual enterprise ransomware exercise including the HOC and the disclosure committee (POAM-013); scheduling platform fallback drill; egress controls on the OT DMZ file transfer | CISO | 2027-03-31 |
| R-002 | State-sponsored actor pre-positions inside OT networks to enable a disruptive attack on gates and units during a crisis | High | ER-01 | OT sensor rollout to all Group 1 and 2 gated plants first (POAM-003); annual threat hunt across OT with the retainer firm | Director, OT Security | 2027-06-30 |
| R-003 | Attacker uses an always-on vendor connection or the password-only legacy VPN at the Piedmont plants to operate spillway gates or units at PD-04 or PD-06 | Very High | ER-05 | Replace the legacy VPN with the HOC Intermediate Systems, named accounts, and MFA; remove always-on vendor tools; OT sensors at all 9 PD plants (POAM-001, POAM-002) | Vice President, Integration Management Office | 2026-12-31 |
| R-006 | Attacker exploits an unsupported gate control workstation after lateral movement and issues gate commands | High | ER-01 | Replace the 9 gate workstations first, then the 64 HMIs (POAM-005) | Director, Hydro Control Systems Engineering | 2027-12-31 |
| R-008 | An intrusion at one of the 24 HOC-operated plants without OT network monitoring goes undetected long enough to cause harm | High | ER-01 | OT sensors at all plants, Group 1 and 2 gated plants first (POAM-003) | Director of Security Operations | 2027-06-30 |
| R-012 | HOC failover exceeds the 2-hour RTO during a flood or a loss of HOC-A, leaving gates on local control with stretched crews | High | ER-02 | Standing night-shift crew at HOC-B; automated database resynchronization; retest by 2027-01-31 (POAM-010) | Director, Hydro Operations Center | 2027-01-31 |
| R-013 | PLC and gate logic copies older than 12 months at 14 plants prevent a clean, verified restore after compromise or failure | High | ER-02 | Collect and verify copies at the 14 plants; quarterly copy schedule (POAM-008) | Director, Hydro Control Systems Engineering | 2026-12-31 |
| R-018 | A major flood coincides with a cyber incident or HOC outage (compound event) | High | ER-01 | Joint flood and cyber exercise with county emergency management in 2027; pre-staged crews when major floods are forecast | Senior Vice President, Hydro Operations | 2027-06-30 |
| R-021 | A telecom carrier outage at the 19 single-carrier plants puts them on local control during high water | High | ER-02 | Diverse paths (second carrier or microwave) for the 19 plants, Group 1 and 2 first (POAM-011) | Director, OT Network Engineering | 2027-06-30 |
| R-024 | Compromise or failure of the governor and exciter OEM affects 91 of 151 units | High | ER-04 | Contract amendment with CIP-013-2 terms; test the on-site fallback; second qualified service provider for 30% of units (POAM-014) | Director of Third-Party Risk Management | 2027-03-31 |
| R-032 | An intrusion at a Piedmont plant goes undetected because there is no OT monitoring | High | ER-05 | OT sensors and log forwarding at all 9 PD plants (POAM-001) | Director of Security Operations | 2026-12-31 |
| R-033 | Shared operator accounts at Piedmont plants prevent attribution and fast revocation | High | ER-05 | Named accounts managed by OT PAM (POAM-002) | Vice President, Integration Management Office | 2027-01-31 |
| R-036 | BCSI for the HOCs is exposed through a contractor-shared project folder | High | ER-06 | Remove the folder, review access history, assess as a potential CIP-011 noncompliance, and add BCSI DLP rules (POAM-006) | Director, NERC Compliance | 2026-11-30 |
| R-042 | An uncontrolled change to DSMS alert thresholds or models suppresses alerts for client dams | High | ER-07 | Threshold and model change control with dual approval and audit trail (POAM-019) | Vice President, Dam Safety Monitoring Services | 2026-12-31 |
| R-043 | Shared COC credentials at 6 SL-1 client endpoints allow untraceable or unauthorized operation of client plants | High | ER-07 | Named credentials with MFA at all 27 endpoints, coordinated with the 11 clients (POAM-021) | Vice President, Hydro Services | 2026-12-31 |
| R-047 | A material OT incident is disclosed late or inaccurately because the disclosure committee has not exercised an OT or dam safety scenario | High | ER-08 | Tabletop 2026-11-18 with an OT and dam safety scenario; playbook update (POAM-013) | General Counsel | 2026-11-30 |
| R-051 | Potential NERC CIP violations (Piedmont Sections 3 and 6, late access removal, BCSI exposure) lead to penalties and mitigation plans | High | ER-03 | Complete mitigation plans (POAM-001, POAM-006, POAM-016); extend internal controls monitoring to newly acquired assets | Director, NERC Compliance | 2027-03-31 |
| R-054 | Undocumented vendor paths (cellular modems at dataloggers) bypass the Intermediate Systems | High | ER-01 | Remove the paths; vendor access only through the Intermediate Systems (POAM-012) | Vice President, Dam Safety | 2026-11-30 |

## 6. Themes from the 2026 analysis
1. **Piedmont (ER-05).** Nine acquired plants still run on the prior owner's password-only VPN, shared accounts, and always-on vendor connections, with no OT monitoring (R-003, R-031 to R-034). Two of them hold Group 2 gated dams. Interim measures have been in place since 2026-09-18; the full fix is due 2026-12-31, ahead of integration on 2027-03-31.
2. **Seeing below the HOC (ER-01).** The HOCs are well monitored, but 24 of 35 plants have no OT network sensors (R-008) and 13 have had no OT vulnerability assessment in 12 months. A patient attacker at a plant would have a long window (R-002).
3. **Legacy equipment (ER-01, ER-02).** 64 plant HMIs and 9 gate workstations are unsupported (R-006, R-022), and logic copies are stale at 14 plants (R-013).
4. **Recovery (ER-02).** HOC failover missed its RTO (R-012), and 19 plants depend on one carrier (R-021). Both matter most in a flood, when local control needs the most people (R-018).
5. **Vendors (ER-04).** One OEM services 60% of units without CIP-013-2 terms (R-024).
6. **Service lines (ER-07).** SL-2 change control for alert thresholds and models (R-042) and SL-1 shared credentials (R-043) are the main gaps before the SOC 2 work in P09.
7. **Disclosure (ER-08).** The committee has never exercised an OT or dam safety scenario (R-047).

## 7. Treatment summary
- **Funded (2026 Q4 to 2027 Q4), about $14.6 million:** Piedmont remote access and monitoring ($2.1M), OT sensors at 24 plants ($3.4M), HMI and gate workstation replacement ($5.2M), diverse telecom paths for 19 plants ($2.3M), HOC-B staffing and database automation ($0.9M a year), OEM second source and fallback test ($0.4M), DSMS change control and ingestion automation ($0.3M). Items map to the POA&M in P07.
- **Accepted (8):** R-019, R-027, R-029, R-038, R-046, R-049, R-057, R-063. Each is Low or Moderate residual with strong existing controls, accepted at the right level (section 1) and reviewed within 12 months.
- **Avoided (2):** R-039, R-062. Public generative AI tools stay blocked for CEII and BCSI, and inflow forecast output cannot be used directly for gate settings.
- **Very High risk R-003:** not accepted as is. The CEO and CFO approved the treatment plan and the residual target of Moderate on 2026-09-08; the board committee reviewed it on 2026-09-10.

## 8. Board reporting
**Safety, risk, and reliability committee of the board (quarterly):** the enterprise risk profile (section 4), every Very High and High risk with treatment status and KRI trend, risks outside tolerance, new risks, risk acceptances, NERC self-reports, and FERC inspection results. The 2026-09-10 meeting received this report, the Internal Audit results (P07), and the regulatory roadmap (P03).
**Audit committee (quarterly):** Internal Audit results, SOX IT general control status (R-049), and disclosure controls topics (R-047, R-048). It also reviews the annual Item 106 disclosure draft, which describes this process.
**Management:** the executive risk committee meets monthly and reviews KRIs for every risk outside tolerance.

## 9. Approval
- Executive risk committee: approved the register, treatments, and acceptances, 2026-09-08.
- CEO and CFO: approved the treatment plan and residual target for Very High risk R-003, 2026-09-08.
- Safety, risk, and reliability committee of the board: reviewed the enterprise risk profile, 2026-09-10.
- Next full review: June to July 2027, or sooner after a major change (the Piedmont integration), an incident, or an acquisition. KRIs are refreshed quarterly.
