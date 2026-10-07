# Enterprise Risk Register Report: Cris Santos Company | Nuclear Reactors, Materials, and Waste | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded nuclear generation company: four stations, seven units; FL, GA, SC, AL) |
| Size tier | Enterprise (12,000 employees) |
| Vertical | Nuclear Reactors, Materials, and Waste |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) for each risk; NIST IR 8286 Rev. 1 for integration into enterprise risk management (ERM) |
| Also satisfies | Evaluation and management of cyber risk for business systems that border the CDA program (10 CFR 73.54(d)(2)); input to the Reg S-K Item 106 description of risk management processes |
| Prepared | 2026-06-01 to 2026-07-31 by the GRC team for the CISO, with the Director, Nuclear Cyber Security; updated 2026-08-28 with Internal Audit findings (P07) |
| Approved | Executive risk committee (chaired by the Chief Risk Officer), 2026-09-08; reviewed by the risk committee of the board and the nuclear safety oversight committee, 2026-09-10 |

## 1. Scope and risk framing
**Scope.** All business systems that support the seven units, the four plant business networks, the fleet work management system (WMS), the two cloud estates and two data centers, the Generation Dispatch Center, the two service lines (SL-1, SL-2), Station 4's legacy systems, and the roughly 2,900 suppliers (410 with network or data access). Business processes and impact values come from the enterprise BIA (P05). WMS-PBN is also covered at system level in the SSP (P02).

**Relationship to the CSP.** Each station's cyber security plan has its own process to evaluate and manage cyber risk to CDAs (73.54(d)(2)), and its results stay in the station programs. This register records CDA-related risks only at enterprise level (for example, R-002, R-058, R-061) so the board sees them; it does not replace the station analyses.

**Three lines.** Risk owners in the business, the stations, and IT (first line) own and treat risks. The GRC team and the Chief Risk Officer (second line) run this method and roll risks up into the enterprise risk register. Internal Audit (third line) tests controls independently (P07). Nuclear Oversight, which is independent of station line management, separately reviews the security program, including cyber, at least every 24 months (73.55(m)).

**Risk appetite (board-approved, 2026-02).** Qualitative statements set by the board:
- **Nuclear safety and security:** very low appetite for any cyber-related effect on safety, security, or emergency preparedness functions.
- **Regulatory and disclosure:** very low appetite for noncompliance with NRC, NERC, or SEC rules.
- **Generation and outage performance:** low appetite for lost generation or outage extensions from technology events.
- **Sensitive information:** low appetite for disclosure of SGI, security-related information, export-controlled technology, or personal information.
- **Growth and innovation (acquisitions, AI, service lines):** moderate appetite, provided risks are identified and funded before or at the time of the decision.

**Risk tolerance (measurable, per enterprise risk).** The highest residual risk level each enterprise risk may carry without a board-reported treatment plan. A risk above its threshold is **Outside tolerance** in the register.

| Enterprise risk | Tolerance threshold |
|---|---|
| ER-01 Generation and outage disruption from cyber and technology events | Moderate |
| ER-02 Compromise of sensitive nuclear and security information | Moderate |
| ER-03 Third-party, supply chain, and concentration risk | Moderate |
| ER-04 Integration of Station 4 | Moderate |
| ER-05 Nuclear safety, security, and NRC and NERC compliance | Low |
| ER-06 Disclosure and financial reporting | Low |
| ER-07 Personal information and service line commitments | Moderate |
| ER-08 Responsible use of AI | Moderate |

**Who can accept risk:**
| Residual level | Acceptance authority |
|---|---|
| Very Low, Low | Risk owner (vice president or director) with GRC concurrence |
| Moderate | CISO with the accountable executive (for station risks, the Site Vice President) |
| High | Executive risk committee (Chief Risk Officer, Chief Nuclear Officer, CIO, CISO, General Counsel), reported to the board risk committee |
| Very High | CEO and CFO jointly, reported to the board risk committee at its next meeting |

ER-05 risks at High or above cannot be accepted without a dated treatment plan, and no risk acceptance may waive a regulatory requirement. Any acceptance expires after 12 months.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the nuclear sector threat picture (nation-state pre-operational planning, ransomware against energy companies, outage-time insider and contractor risk), the BIA (P05), the gap analysis (P03), and the Internal Audit assessment (P07).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial), and likelihood of adverse impact, combined with **Table G-5**.
3. **Rate impact.** **Table H-3**, calibrated to the BIA impact values (P05 section 3).
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
| High | 8 |
| Moderate | 37 |
| Low | 18 |
| **Total** | **64** |

By threat source type: Adversarial 25, Structural 25, Accidental 13, Environmental 1.
By treatment: Mitigate 53, Accept 9, Avoid 2.
By status: In progress 44, Open 9, Closed (accepted) 9, Closed (avoided) 2.
**20 risks are outside tolerance** and each has a dated treatment plan. 13 of them sit in ER-05, whose tolerance is Low.

## 4. Enterprise risk profile (roll-up for the board)
| ID | Enterprise risk | ERM category | Risks | Very High | High | Moderate | Low | Exposure (highest) | Tolerance | Outside tolerance |
|---|---|---|---|---|---|---|---|---|---|---|
| ER-01 | Generation and outage disruption from cyber and technology events | Operational | 10 | 1 | 1 | 8 | 0 | **Very High** | Moderate | 2 |
| ER-02 | Compromise of sensitive nuclear and security information | Security and compliance | 5 | 0 | 1 | 1 | 3 | **High** | Moderate | 1 |
| ER-03 | Third-party, supply chain, and concentration risk | Operational | 7 | 0 | 1 | 4 | 2 | **High** | Moderate | 1 |
| ER-04 | Integration of Station 4 | Strategic | 6 | 0 | 1 | 4 | 1 | **High** | Moderate | 1 |
| ER-05 | Nuclear safety, security, and NRC and NERC compliance | Nuclear safety and compliance | 17 | 0 | 3 | 10 | 4 | **High** | Low | 13 |
| ER-06 | Disclosure and financial reporting | Financial and compliance | 4 | 0 | 1 | 1 | 2 | **High** | Low | 2 |
| ER-07 | Personal information and service line commitments | Compliance and reputational | 8 | 0 | 0 | 5 | 3 | **Moderate** | Moderate | 0 |
| ER-08 | Responsible use of AI | Strategic and operational | 7 | 0 | 0 | 4 | 3 | **Moderate** | Moderate | 0 |

**Reading the profile:**
- **ER-01 (generation and outage disruption)** carries the only Very High risk: fleet-wide ransomware during a refueling outage (R-001), when a day of delay costs about $3.2 million (P05 BP-07).
- **ER-05 (nuclear safety, security, and compliance)** has the lowest tolerance and the most risks outside it. Its three High risks are the business-network pivot toward CDAs (R-002), the unanalyzed sensor gateways at Station 4 (R-005), and WMS clearance and surveillance integrity (R-006). Most of its Moderate risks are process gaps with clear fixes: notification coordination (R-014, R-015, R-055), clearance role conflicts (R-007, R-008), and untested scheduling changes (R-009).
- **ER-06 (disclosure)** is outside tolerance mainly because the SEC materiality process has not been exercised on a plant scenario that also triggers NRC notifications (R-013).
- **ER-08 (AI)** is within tolerance today, but 4 of 12 use cases lack committee review (R-046), so the rating depends on the reviews due 2026-11-30.

## 5. Top risks (Very High and High)
| Risk ID | Risk | Level | Enterprise risk | Treatment | Owner | Due |
|---|---|---|---|---|---|---|
| R-001 | Ransomware encrypts business systems across the fleet during a refueling outage, extending the outage | Very High | ER-01 | Station 4 EDR and SIEM (POAM-004); WMS outage-mode RTO (POAM-010); contractor segment enforcement; enterprise ransomware exercise with the disclosure committee (POAM-013) | CISO | 2027-03-31 |
| R-002 | Attacker on the plant business network pivots toward CDAs through portable media, maintenance equipment, or a misconfigured boundary device | High | ER-05 | Close the kiosk bypass (POAM-015); pivot scenario in station tabletops; monthly boundary device checks | Director, Nuclear Cyber Security | 2026-12-31 |
| R-003 | Attacker enters through Station 4's flat network or the prior owner's vendor VPN and reaches fleet systems | High | ER-04 | Segment the network and retire the VPN (POAM-009); federate identities (POAM-003); EDR and SIEM (POAM-004) | Vice President, Integration Management | 2027-03-31 |
| R-005 | Wireless sensor gateways with cellular links create an unanalyzed path next to plant equipment at Station 4 | High | ER-05 | Disconnect, analyze under 73.54(b)(1), design change review, CAP entry (POAM-011; POAM-018) | Director, Nuclear Cyber Security | 2026-12-31 |
| R-006 | Compromise of the WMS changes clearance records or surveillance schedules | High | ER-05 | Automated integrity response (SI-7(2), SI-7(5)); alerts on off-hours clearance edits | Vice President, Fleet Work Management | 2027-01-31 |
| R-012 | Cyber security plan details, CDA inventories, or network diagrams are stolen from business file shares | High | ER-02 | Sweep for security-related information outside restricted folders; DLP rules | Director, Nuclear Cyber Security | 2027-03-31 |
| R-013 | A material incident is disclosed late or inaccurately because the materiality process has not been exercised on a plant scenario | High | ER-06 | Disclosure committee tabletop on 2026-11-19 using the P08 scenario (POAM-013) | General Counsel | 2026-11-30 |
| R-019 | The WMS software vendor is compromised or ships a malicious update | High | ER-03 | Software bills of materials and signed packages in the 2027 renewal | Director of Third-Party Risk Management | 2027-06-30 |
| R-036 | Default passwords on business network devices are used to gain a foothold (found on sensor gateways) | High | ER-01 | Change passwords; default credential scan in every walkdown (POAM-011) | Director, Nuclear Cyber Security | 2026-10-31 |

## 6. Themes from the 2026 analysis
1. **The boundary between business IT and plant systems (ER-05).** The defensive architecture works as designed: no path from the business network or the cloud reaches a CDA network. The risk sits in what crosses the boundary by hand (portable media, contractor equipment) and in devices installed near plant equipment without the 73.54(b)(1) analysis, such as the Station 4 sensor gateways (R-002, R-005, R-036, R-037).
2. **Station 4 integration (ER-04).** Fifteen months after the acquisition, Station 4 still runs the prior owner's directory, flat network, vendor VPN, and work management system. These conditions raise the likelihood of fleet-wide ransomware (R-001) and slow detection (R-040). Treatment: segmentation, federation, EDR and SIEM, and the WMS migration, all due by 2027-05-31.
3. **Outages concentrate risk (ER-01).** During a refueling outage the fleet adds up to 1,500 contractors, freezes patching, and depends most on the WMS. Contractor account removal (R-004), contractor devices (R-018), and WMS recovery time (R-010) all peak then.
4. **Integrity of work control records (ER-05).** Clearance role conflicts (R-007), shared kiosk approvals (R-008), and untested scheduling changes (R-009) do not cause harm by themselves because field verification and surveillance look-aheads catch errors, but each removes a layer.
5. **Notification and disclosure (ER-05, ER-06).** NRC clocks can start from events in the business network (73.77(a)(2)(iii) and (a)(3)), and NRC event notification reports are public. The SOC, the stations, and the disclosure committee have not yet practiced this together (R-013, R-014, R-055).
6. **AI (ER-08).** 12 use cases, 8 reviewed. AI-001 predictive maintenance touches equipment in Maintenance Rule scope and is validated only fleet-wide (R-042, R-043).

## 7. Treatment summary
- **Funded (2026 Q4 to 2027 Q2), about $7.2 million:** Station 4 network segmentation and VPN retirement ($1.9M), Station 4 identity federation ($0.9M), Station 4 EDR, SIEM collectors, and network detection ($1.1M), WMS migration for Station 4 ($1.6M), WMS standby automation and integrity controls ($0.6M), sensor gateway analysis and replacement ($0.3M), second carrier at Station 4 ($0.2M per year), portable media kiosks at warehouses ($0.4M), dosimetry restore testing and portal hardening ($0.2M), and outside counsel for the disclosure tabletop ($0.04M). Items map to the POA&M in P07.
- **Accepted (9):** R-021, R-029, R-031, R-047, R-048, R-051, R-052, R-059, R-064. Each is Low or Moderate residual with strong existing controls, accepted at the right level (section 1) and reviewed within 12 months.
- **Avoided (2):** R-041 and R-045. Unapproved generative AI domains are blocked, and AI resume ranking is disabled until review.
- **Very High risk R-001:** not accepted as is. The CEO and CFO approved the treatment plan and the residual target of High on 2026-09-08; the board risk committee reviewed it on 2026-09-10.

## 8. Board reporting
**Risk committee of the board (quarterly):** the enterprise risk profile (section 4), every Very High and High risk with its treatment status and KRI trend, risks outside tolerance, new risks since the last meeting, and risk acceptances made. The 2026-09-10 meeting received this report, the Internal Audit results (P07), and the regulatory roadmap (P03).
**Nuclear safety oversight committee (quarterly):** ER-05 risks, NRC inspection results, Nuclear Oversight 73.55(m) review results, and the CDA boundary themes in section 6.
**Audit committee (quarterly):** Internal Audit results, SOX IT general control status (R-048), and the disclosure topics (R-013, R-049). The audit committee also reviews the annual Item 106 disclosure draft, which describes this process.
**Management:** the executive risk committee meets monthly and reviews KRIs for all risks outside tolerance.

## 9. Approval
- Executive risk committee: approved the register, treatments, and acceptances, 2026-09-08.
- CEO and CFO: approved the treatment plan and residual target for Very High risk R-001, 2026-09-08.
- Risk committee of the board and nuclear safety oversight committee: reviewed the enterprise risk profile, 2026-09-10.
- Next full review: June to July 2027, or sooner after a major change, incident, acquisition, or final NRC rule. KRIs are refreshed quarterly.
