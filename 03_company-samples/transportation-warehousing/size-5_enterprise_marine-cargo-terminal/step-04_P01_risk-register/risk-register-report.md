# Enterprise Risk Register Report: Cris Santos Company | Transportation and Warehousing | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded multi-port marine cargo terminal operator: 8 terminals at 6 ports in FL, GA, SC and TX; two service lines sold to outside customers) |
| Size tier | Enterprise (12,000 employees) |
| Vertical | Transportation and Warehousing |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) for each risk; NIST IR 8286 Rev. 1 for integration into enterprise risk management (ERM) |
| Also satisfies | Input to the Cybersecurity Assessment that must analyze all networks and the risk posed by each digital asset (33 CFR 101.650(e)(1)(i)); input to the Reg S-K Item 106 description of risk management processes |
| Prepared | 2026-06-01 to 2026-07-31 by the GRC team for the CISO and the CySO; updated 2026-08-28 with Internal Audit findings (P07) |
| Approved | Executive risk committee (chaired by the Chief Risk Officer), 2026-09-08; reviewed by the risk committee of the board, 2026-09-10 |

## 1. Scope and risk framing
**Scope.** All IT and OT systems at the 8 terminals, the enterprise planning center and headquarters; the two cloud estates and two colocation data centers; the SL-1 and SL-2 service lines; the acquired terminal T-08; and the roughly 1,300 vendors (210 tier 1 or 2) and the port partners. Business processes and impact values come from the enterprise BIA (P05). ETOP is also covered at system level in the SSP (P02).

**Three lines.** Risk owners in operations, IT and OT (first line) own and treat risks. The GRC team, the Chief Risk Officer and the CySO's team (second line) run this method and roll risks up into the enterprise risk register. Internal Audit (third line) tests controls independently (P07).

**Risk appetite (board-approved, 2026-02).** Qualitative statements set by the board:
- **Safety:** very low appetite for technology-related harm to workers, crews, truck drivers or emergency responders, including hazardous cargo events.
- **Maritime security, regulatory and disclosure:** very low appetite for noncompliance with Subpart F, the FSPs, customs release rules or SEC disclosure rules.
- **Terminal continuity:** low appetite for disruption of vessel and gate operations at more than one terminal.
- **Data:** low appetite for unauthorized disclosure of personal information, SSI or customers' cargo data.
- **Growth and innovation (acquisitions, automation, AI, service lines):** moderate appetite, provided risks are identified and funded at the time of the decision.

**Risk tolerance (measurable, per enterprise risk).** The highest residual risk level each enterprise risk may carry without a board-reported treatment plan. A risk above its threshold is **Outside tolerance** in the register.

| Enterprise risk | Tolerance threshold |
|---|---|
| ER-01 Terminal operations disruption from cyber and technology events | Moderate |
| ER-02 OT, equipment and cargo safety | Low |
| ER-03 Maritime security, regulatory and disclosure compliance | Low |
| ER-04 Third-party, port partner and concentration risk | Moderate |
| ER-05 Integration of acquired terminals (T-08 and future deals) | Moderate |
| ER-06 Service line commitments to outside customers (SL-1, SL-2) | Moderate |
| ER-07 Compromise of personal information, SSI and commercial cargo data | Moderate |
| ER-08 Financial reporting integrity, fraud and risk transfer | Low |
| ER-09 Responsible use of AI | Moderate |

**Who can accept risk:**
| Residual level | Acceptance authority |
|---|---|
| Very Low, Low | Risk owner (vice president or director) with GRC concurrence |
| Moderate | CISO with the accountable executive (and the CySO for risks to critical IT or OT) |
| High | Executive risk committee (Chief Risk Officer, CIO, COO, CISO, General Counsel), reported to the board risk committee |
| Very High | CEO and CFO jointly, reported to the board risk committee at its next meeting |

Safety risks (ER-02) at High or above cannot be accepted without a dated treatment plan. Any acceptance expires after 12 months. A risk accepted for a Subpart F measure must also be recorded as an unresolved vulnerability in Section 12 of the Cybersecurity Plan (101.630(c)(12)).

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E; the maritime threat picture (ransomware against terminal operators, OEM and supply chain access to cranes, nation-state interest in port OT, which led to MARSEC Directives 105-4 and 105-5); the BIA (P05); the gap analysis (P03); and the Internal Audit assessment (P07).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial), and likelihood of adverse impact, combined with **Table G-5**.
3. **Rate impact.** **Table H-3**, calibrated to the BIA impact values (P05 section 3).
4. **Determine risk.** **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the tables, not assigned by hand.
5. **Integrate with ERM (NIST IR 8286 Rev. 1).**
   - Each system-level cybersecurity risk is a row in this register, with an owner, a treatment and a key risk indicator (KRI).
   - Each row is normalized into one of **9 enterprise risks (ER-01 to ER-09)** in the Chief Risk Officer's enterprise risk register, with an ERM category (operational, safety, compliance, strategic, contractual, financial).
   - **Aggregation rule:** an enterprise risk's exposure equals its highest constituent risk level, and the profile also reports how many constituent risks sit outside tolerance. This keeps one severe risk from being averaged away.
   - The enterprise risk profile (section 4) is what the board risk committee sees each quarter.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 12 |
| Moderate | 33 |
| Low | 19 |
| **Total** | **65** |

By threat source type: Adversarial 33, Structural 25, Accidental 6, Environmental 1.
By treatment: Mitigate 56, Accept 6, Share/Transfer 2, Avoid 1.
By status: In progress 49, Open 8, Closed (accepted) 6, Closed (transferred) 1, Closed (avoided) 1.
**25 risks are outside tolerance** and each has a dated treatment plan.

## 4. Enterprise risk profile (roll-up for the board)
| ID | Enterprise risk | ERM category | Risks | Very High | High | Moderate | Low | Exposure (highest) | Tolerance | Outside tolerance |
|---|---|---|---|---|---|---|---|---|---|---|
| ER-01 | Terminal operations disruption from cyber and technology events | Operational | 12 | 1 | 2 | 7 | 2 | **Very High** | Moderate | 3 |
| ER-02 | OT, equipment and cargo safety | Safety | 10 | 0 | 4 | 4 | 2 | **High** | Low | 8 |
| ER-03 | Maritime security, regulatory and disclosure compliance | Compliance | 11 | 0 | 1 | 5 | 5 | **High** | Low | 6 |
| ER-04 | Third-party, port partner and concentration risk | Operational | 7 | 0 | 2 | 4 | 1 | **High** | Moderate | 2 |
| ER-05 | Integration of acquired terminals (T-08 and future deals) | Strategic | 6 | 0 | 2 | 3 | 1 | **High** | Moderate | 2 |
| ER-06 | Service line commitments to outside customers (SL-1, SL-2) | Strategic and contractual | 5 | 0 | 1 | 2 | 2 | **High** | Moderate | 1 |
| ER-07 | Compromise of personal information, SSI and commercial cargo data | Compliance and reputational | 6 | 0 | 0 | 2 | 4 | **Moderate** | Moderate | 0 |
| ER-08 | Financial reporting integrity, fraud and risk transfer | Financial | 4 | 0 | 0 | 3 | 1 | **Moderate** | Low | 3 |
| ER-09 | Responsible use of AI | Strategic and operational | 4 | 0 | 0 | 3 | 1 | **Moderate** | Moderate | 0 |

**Reading the profile:**
- **ER-01 (terminal disruption)** carries the only Very High risk: ransomware on ETOP across several terminals and the SL-2 clients (R-001). Its likelihood stays high because one platform serves 11 terminals and the platform cannot yet be restored within its RTO (R-008).
- **ER-02 (OT and safety)** has the lowest tolerance and the most risks outside it: 4 High risks (IT-to-OT spread at T-07 and T-08, OEM tunnels, nation-state pre-positioning in PRC-manufactured cranes, OT KEVs) and 4 Moderate risks.
- **ER-03 (compliance)** is outside tolerance mainly because the materiality and multi-COTP reporting process has not been exercised with the current disclosure committee (R-012), and because the Cybersecurity Plans and Assessment are still in progress (R-040).
- **ER-05 (T-08)** shows what an unfunded integration costs: no MFA, no SIEM, partial EDR and untested backups at an acquired terminal (R-003, R-031).
- **ER-07 and ER-09** are within tolerance today. ER-09 depends on the AI reviews and fairness tests due by 2027-01-31 (R-029, R-030).

## 5. Top risks (Very High and High)
| Risk ID | Risk | Level | Enterprise risk | Treatment | Owner | Due |
|---|---|---|---|---|---|---|
| R-001 | Ransomware encrypts the ETOP TOS platform and gate systems at several terminals and the SL-2 client environments at once | Very High | ER-01 | Prove the 4 h RTO for all 11 environments (POAM-005); close T-08 gaps (POAM-001, POAM-012, POAM-020); materiality and multi-COTP exercise (POAM-010); SL-2 notice terms (POAM-011) | CISO | 2027-03-31 |
| R-002 | Ransomware or a wiper spreads from IT to crane and automation OT, or OT is shut down as a precaution | High | ER-02 | OT zone at T-07 (POAM-003); OT monitoring at T-06 to T-08 (POAM-009); T-08 segmentation with the migration | Director of OT Engineering | 2027-06-30 |
| R-003 | Attacker enters through T-08's legacy directory and flat network and reaches enterprise systems | High | ER-05 | Federate T-08 identities with MFA (POAM-001); EDR to 100% (POAM-012); T-08 logs to SIEM (POAM-008); migration by 2027-06-30 | Vice President, Integration Management Office | 2027-03-31 |
| R-004 | Attacker uses an OEM persistent remote tunnel to reach crane PLCs or the T-01 automated yard | High | ER-02 | Move both OEMs to the gateway; remove the T-08 modem (POAM-002) | Director of OT Engineering | 2026-12-15 |
| R-005 | Nation-state pre-positioning in port OT and PRC-manufactured STS cranes | High | ER-02 | Complete MARSEC Directive actions and verify them in the Assessment; OT monitoring at T-07 (POAM-009); KEV compensating controls (POAM-006) | Director of Maritime Cybersecurity (CySO) | 2027-03-31 |
| R-006 | Exploitation of an OT KEV (37 open beyond 30 days without documented compensating controls) | High | ER-02 | Compensating control records within 10 days of listing; OEM patch plan (POAM-006) | Director of OT Engineering | 2026-12-31 |
| R-008 | TOS platform recovery exceeds the 4-hour RTO in a multi-terminal event | High | ER-01 | Parallel restore; failover test of all 11 environments (POAM-005) | Vice President, Terminal Technology | 2027-02-28 |
| R-010 | Customs data exchange outage or compromise stops release status at all terminals | High | ER-04 | Security and notice terms; second channel; fallback test (POAM-022) | Director of Third-Party Risk Management | 2027-03-31 |
| R-012 | Late or inaccurate disclosure, or Coast Guard reports in several COTP zones inconsistent with the disclosure | High | ER-03 | Update the playbook; tabletop on 2026-11-18 (POAM-010) | General Counsel | 2026-11-30 |
| R-013 | SL-2 clients cannot make their own immediate 6.16-1 reports because the company's notice is late | High | ER-06 | Amend agreements; responsibility matrix; joint drills (POAM-011) | Vice President, Terminal Technology | 2027-01-31 |
| R-015 | Malicious code in a TOS update or OEM controller firmware | High | ER-04 | Firmware hash verification; SBOM requests for tier-1 software | CISO | 2027-06-30 |
| R-031 | T-08 legacy TOS loses up to 24 hours of data; restore never tested | High | ER-05 | Interim immutable copy and restore test (POAM-020); migration by 2027-06-30 | Vice President, Integration Management Office | 2026-12-31 |
| R-044 | Zero-day in an internet-facing edge device is exploited | High | ER-01 | Retire the T-08 legacy firewall; zero-trust access for staff | Director of Network Engineering | 2027-06-30 |

## 6. Themes from the 2026 analysis
1. **Platform concentration (ER-01).** ETOP gives every terminal the same strong identity, logging and backup controls, but it also means one ransomware event or one region outage reaches 11 terminals in 6 COTP zones and 4 outside clients. The recovery test is the single most important open item (R-001, R-008, R-025).
2. **The OT edge (ER-02).** Cloud and IT controls are mature; the gaps are where IT meets cranes and automation: a shared VLAN at T-07, a flat network at T-08, two OEM tunnels outside the gateway, OT KEVs, devices without password controls, and OT monitoring only at T-01 to T-05 (R-002, R-004, R-006, R-007, R-042). Testing found default passwords on 3 OT devices (R-007, POAM-004).
3. **T-08 integration (ER-05).** The acquisition closed in 2025-11 before integration funding was approved. T-08 has its own directory without MFA, partial EDR, no SIEM feed, an always-on OEM modem and untested backups (R-003, R-031, R-033). Going forward, deal approvals must include security due diligence and integration funding (R-057).
4. **Port partners and concentration (ER-04).** The customs data exchange service delivers every hold status and has no security or notice terms; the 6 port community systems are the same (R-010, R-011).
5. **Reporting under several regimes at once (ER-03).** A multi-terminal incident triggers immediate 6.16-1 reports in each affected COTP zone, SL-2 clients' own reports, state breach notices and possibly a Form 8-K. The playbook has not been exercised for that combination (R-012, R-013).
6. **AI (ER-09).** AI-001 runs in production at 3 terminals with the independent constraint check at only one, and appointment fairness has not been tested (R-028, R-029).

## 7. Treatment summary
- **Funded (2026 Q4 to 2027 Q2), about $5.4 million:** T-08 identity federation ($1.2M), T-07 OT zone ($620K), OCR server replacement ($410K), standby capacity and restore automation ($310K a year plus internal effort), CySO program and co-sourced OT assessors ($280K), OT monitoring sensors ($260K), OEM services for HMIs and KEVs ($300K), OEM gateway onboarding ($230K), second hold-status channel ($150K), T-08 endpoints and EDR ($131K), SIEM ingestion ($85K a year), training content and labor arrangements ($60K), outside counsel and exercise support ($95K), and other items in the POA&M. Items map to the POA&M in P07.
- **Accepted (6):** R-046, R-047, R-049, R-050, R-051, R-061. Each is Low or Moderate residual with strong existing controls, accepted at the right level (section 1) and reviewed within 12 months.
- **Transferred (2):** R-052 (card data stays with the payment service provider) and R-055 (cyber insurance, with higher limits and OT business interruption coverage sought at renewal; still outside the Low tolerance of ER-08 until renewal).
- **Avoided (1):** R-043. Unapproved generative AI domains are blocked and the reviewed enterprise assistant (AI-008) is the approved route.
- **Very High risk R-001:** not accepted as is. The CEO and CFO approved the treatment plan and the residual target of High on 2026-09-08; the board risk committee reviewed it on 2026-09-10.

## 8. Board reporting
**Risk committee of the board (quarterly):** the enterprise risk profile (section 4), every Very High and High risk with its treatment status and KRI trend, risks outside tolerance, new risks since the last meeting, risk acceptances made, and the status of the Cybersecurity Plans against the 2027-07-16 deadline. The 2026-09-10 meeting received this report, the Internal Audit results (P07) and the regulatory roadmap (P03).
**Audit committee (quarterly):** Internal Audit results, SOX IT general control status (R-032), and the disclosure controls topics (R-012). The audit committee also reviews the annual Item 106 disclosure draft, which describes this process.
**Management:** the executive risk committee meets monthly and reviews KRIs for all risks outside tolerance. The CySO reports Subpart F status to it each month.

## 9. Approval
- Executive risk committee: approved the register, treatments and acceptances, 2026-09-08.
- CEO and CFO: approved the treatment plan and residual target for Very High risk R-001, 2026-09-08.
- Risk committee of the board: reviewed the enterprise risk profile, 2026-09-10.
- Next full review: June to July 2027, or sooner after a major change, incident or acquisition. This register will be refreshed for the Cybersecurity Assessment due by 2027-07-16. KRIs are refreshed quarterly.
