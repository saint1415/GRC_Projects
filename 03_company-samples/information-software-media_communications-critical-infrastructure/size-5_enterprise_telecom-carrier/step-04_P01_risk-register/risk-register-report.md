# Enterprise Risk Register Report: Cris Santos Company | Communications | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded regional broadband and wired telecommunications carrier; FL, GA, SC, NC) |
| Size tier | Enterprise (12,000 employees) |
| Vertical | Communications |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) for each risk; NIST IR 8286 Rev. 1 for integration into enterprise risk management (ERM) |
| Also supports | The "reasonable measures" duty for CPNI (47 CFR 64.2010(a)); the Reg S-K Item 106 description of risk management processes (17 CFR 229.106(b)) |
| Prepared | 2026-06-01 to 2026-07-31 by the GRC team for the CISO; updated 2026-08-28 with Internal Audit findings (P07) |
| Approved | Executive risk committee (chaired by the Chief Risk Officer), 2026-09-08; reviewed by the risk and technology committee of the board, 2026-09-10 |

## 1. Scope and risk framing
**Scope.** All systems that hold CPNI or customer personal information, or that support tier-1 processes, across the four states: the carrier network (voice core, IP and access network, management plane), the lawful-intercept platform, the two cloud estates and two data centers, the acquired carriers AQ-01 to AQ-03, and about 1,400 vendors (230 with CPNI or customer personal information). Business processes and impact values come from the enterprise BIA (P05). The OSS/BSS is also covered at system level in the SSP (P02).

**Three lines.** Risk owners in the business, network, and IT (first line) own and treat risks. The GRC team and the Chief Risk Officer (second line) run this method and roll risks up into the enterprise risk register. Internal Audit (third line) tests controls independently (P07).

**Risk appetite (board-approved, 2026-02).** Qualitative statements set by the board:
- **Public safety:** very low appetite for events that stop 911 calling or compromise lawful intercept.
- **Regulatory and disclosure:** very low appetite for noncompliance with FCC rules (CPNI, CALEA, outage reporting) or SEC disclosure rules.
- **Network service continuity:** low appetite for disruption of voice, broadband, and business transport.
- **Customer information:** low appetite for unauthorized disclosure of CPNI or customer personal information.
- **Growth and innovation (acquisitions, AI):** moderate appetite, provided risks are identified and funded before or at the time of the decision.

**Risk tolerance (measurable, per enterprise risk).** The highest residual risk level each enterprise risk may carry without a board-reported treatment plan. A risk above its threshold is **Outside tolerance** in the register.

| Enterprise risk | Tolerance threshold |
|---|---|
| ER-01 Network service disruption from cyber and technology events | Moderate |
| ER-02 Compromise of CPNI and customer personal information | Moderate |
| ER-03 Third-party and supply chain risk | Moderate |
| ER-04 Integration of acquired carriers | Moderate |
| ER-05 Public safety communications and lawful intercept | Low |
| ER-06 Regulatory and disclosure compliance | Low |
| ER-07 Financial reporting integrity and fraud | Low |
| ER-08 Responsible use of AI | Moderate |

**Who can accept risk:**
| Residual level | Acceptance authority |
|---|---|
| Very Low, Low | Risk owner (vice president or director) with GRC concurrence |
| Moderate | CISO with the accountable executive |
| High | Executive risk committee (Chief Risk Officer, CIO, Chief Network Officer, CISO, General Counsel), reported to the board risk and technology committee |
| Very High | CEO and CFO jointly, reported to the board risk and technology committee at its next meeting |

Public safety risks (ER-05) at High or above cannot be accepted without a dated treatment plan. Any acceptance expires after 12 months.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the Communications sector threat picture (state-sponsored intrusion into carrier networks, pretexting for call detail, SIM and account takeover, DDoS, hurricanes), the BIA (P05), the gap analysis (P03), and the Internal Audit assessment (P07). The FCC's 2025 order on reconsideration records that a state-sponsored group infiltrated at least eight U.S. communications companies using publicly known vulnerabilities and avoidable weaknesses (90 FR 58006); that pattern drives R-001, R-007, R-008, and R-048.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial), and likelihood of adverse impact, combined with **Table G-5**.
3. **Rate impact.** **Table H-3**, calibrated to the BIA impact values (P05 section 3).
4. **Determine risk.** **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the tables, not assigned by hand.
5. **Integrate with ERM (NIST IR 8286 Rev. 1).**
   - Each system-level cybersecurity risk is a row in this cybersecurity risk register, with an owner, a treatment, and a key risk indicator (KRI).
   - Each row is normalized into one of **8 enterprise risks (ER-01 to ER-08)** in the Chief Risk Officer's enterprise risk register, with an ERM category (operational, compliance, strategic, public safety, financial).
   - **Aggregation rule:** an enterprise risk's exposure equals its highest constituent risk level, and the profile also reports how many constituent risks sit outside tolerance. This keeps one severe risk from being averaged away.
   - The enterprise risk profile (section 4) is what the board risk and technology committee sees each quarter.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 11 |
| Moderate | 37 |
| Low | 15 |
| **Total** | **64** |

By threat source type: Adversarial 32, Structural 20, Accidental 11, Environmental 1.
By treatment: Mitigate 55, Accept 8, Avoid 1.
By status: In progress 41, Open 15, Closed (accepted) 8.
**21 risks are outside tolerance** and each has a dated treatment plan.

## 4. Enterprise risk profile (roll-up for the board)
| ID | Enterprise risk | ERM category | Risks | Very High | High | Moderate | Low | Exposure (highest) | Tolerance | Outside tolerance |
|---|---|---|---|---|---|---|---|---|---|---|
| ER-01 | Network service disruption from cyber and technology events | Operational | 13 | 0 | 4 | 7 | 2 | **High** | Moderate | 4 |
| ER-02 | Compromise of CPNI and customer personal information | Compliance and reputational | 15 | 1 | 2 | 9 | 3 | **Very High** | Moderate | 3 |
| ER-03 | Third-party and supply chain risk | Operational | 6 | 0 | 1 | 3 | 2 | **High** | Moderate | 1 |
| ER-04 | Integration of acquired carriers | Strategic | 6 | 0 | 1 | 5 | 0 | **High** | Moderate | 1 |
| ER-05 | Public safety communications and lawful intercept | Public safety | 6 | 0 | 2 | 2 | 2 | **High** | Low | 4 |
| ER-06 | Regulatory and disclosure compliance | Compliance | 8 | 0 | 1 | 4 | 3 | **High** | Low | 5 |
| ER-07 | Financial reporting integrity and fraud | Financial | 5 | 0 | 0 | 3 | 2 | **Moderate** | Low | 3 |
| ER-08 | Responsible use of AI | Strategic and customer | 5 | 0 | 0 | 4 | 1 | **Moderate** | Moderate | 0 |

**Reading the profile:**
- **ER-02 (CPNI)** carries the only Very High risk: a state-sponsored intrusion through the management plane that reaches the CDR store and lawful-intercept systems (R-001). The shared accounts on legacy elements (R-008) and the AQ networks (R-003, ER-04) are the main reasons its likelihood is not lower.
- **ER-05 (public safety)** has the lowest tolerance and two High risks: containment that takes 911 down without timely PSAP notice (R-011) and compromise of lawful intercept (R-012).
- **ER-06 (regulatory and disclosure)** is outside tolerance mainly because the materiality playbook does not build in the 64.2011 law enforcement hold and the Item 1.05(d) EDGAR correspondence (R-014), and because AQ-03's CALEA filing is late (R-013).
- **ER-08 (AI)** is within tolerance today, but 4 of 12 use cases lack council review (R-030), so the rating depends on the reviews due 2026-11-30.

## 5. Top risks (Very High and High)
| Risk ID | Risk | Level | Enterprise risk | Treatment | Owner | Due |
|---|---|---|---|---|---|---|
| R-001 | State-sponsored actor exploits a network edge device, persists in the management plane, steals call detail records, and reaches lawful-intercept systems | Very High | ER-02 | Named accounts and MFA on all elements (POAM-002); network log and flow coverage to 95% (POAM-004); AQ segmentation (POAM-003); edge patch SLA (POAM-008); quarterly threat hunts | CISO | 2027-03-31 |
| R-002 | Ransomware encrypts OSS/BSS servers, management plane tools, and corporate systems | High | ER-01 | AQ segmentation (POAM-003); EDR on AQ-03 servers (R-060); BSS RTO fix (POAM-011); ransomware exercise with the disclosure committee (POAM-013) | Director of Security Operations | 2027-01-31 |
| R-003 | Attacker enters through an acquired carrier's flat management network over the site VPN | High | ER-04 | Restrict VPNs to named hosts; route AQ management through enterprise jump hosts (POAM-003) | Vice President, Integration Management Office | 2027-01-31 |
| R-005 | Pretexter obtains call detail from an outsourced care agent who skips CPNI authentication | High | ER-02 | Remove call detail screens from vendor roles without password capture; retrain; monthly sampling (POAM-005; POAM-018) | Chief Customer Officer | 2026-12-31 |
| R-006 | Account takeover through the AQ-02 portal reset that asks for date of birth and SSN4 | High | ER-02 | One-time code reset; change notices (POAM-006; POAM-024) | Chief Customer Officer | 2026-11-30 |
| R-007 | Exploitation of an unpatched edge router or an unsupported SBC | High | ER-01 | Replace AQ-02 SBCs; 72-hour emergency patch path for known exploited vulnerabilities (POAM-008) | Director of Network Security Engineering | 2027-01-31 |
| R-008 | Reuse of a shared local administrator password across legacy access elements | High | ER-01 | TACACS+ with named accounts and MFA, or jump-host-only access (POAM-002) | Director of Network Security Engineering | 2027-03-31 |
| R-011 | A cyber event or its containment takes 911 delivery down and PSAP notices are late | High | ER-05 | 911 impact check in every SOC containment playbook; annual joint NOC-SOC exercise | Vice President, Network Operations Center | 2026-12-31 |
| R-012 | Lawful-intercept platform or intercept records are compromised | High | ER-05 | Move AQ intercepts to the enterprise platform; quarterly enclave access review | Director, Lawful Intercept Compliance | 2027-06-30 |
| R-014 | A material CPNI incident is disclosed late, early, or inaccurately | High | ER-06 | Update playbook; brief new members; full tabletop 2026-11-12 (POAM-013) | General Counsel | 2026-11-30 |
| R-024 | Malicious code arrives in a network equipment software update | High | ER-03 | Automated image hash verification; staged rollouts; SBOM requests to tier-1 vendors | Chief Network Officer | 2027-06-30 |
| R-048 | Zero-day in an internet-facing VPN or firewall is exploited | High | ER-01 | Retire AQ edge devices (POAM-003); 72-hour emergency patch path (POAM-008) | Director of Network Security Engineering | 2027-01-31 |

## 6. Themes from the 2026 analysis
1. **The management plane is the crown jewel (ER-01, ER-02).** About 7,400 legacy access elements still use shared local accounts outside TACACS+ and MFA, and only 58% of element logs reach the SIEM (R-001, R-008, R-009). A state-sponsored campaign against carriers succeeded with exactly these kinds of avoidable weaknesses. Treatment: named accounts and MFA everywhere, or jump-host-only reach where firmware cannot support it, by 2027-03-31.
2. **Acquisition integration (ER-04).** AQ-02 and AQ-03 run legacy billing, identity, and flat management networks that reach the enterprise over site VPNs (R-003, R-004, R-051, R-058, R-060). AQ-03's CALEA SSI policies were not refiled within 90 days of closing (R-013). Going forward, deal approval requires security due diligence and a CALEA filing plan (R-061).
3. **Authentication at the edges of care (ER-02).** In-house care and the main portal meet 64.2010, but sampled calls at one care vendor (R-005) and the AQ-02 portal reset (R-006) do not. These are the most likely routes for a pretexter to obtain call detail.
4. **Disclosure readiness (ER-06).** A CPNI breach that is also material puts two clocks against each other: the 64.2011 bar on public disclosure for 7 full business days after the law enforcement notice, and the 4-business-day Form 8-K clock. Item 1.05(d) allows the 8-K to be delayed for that period, but only with EDGAR correspondence filed by the original due date. The playbook does not yet say this (R-014).
5. **AI (ER-08).** 12 use cases; 8 reviewed. The customer-service chatbot with account access shows a higher error rate in Spanish (R-027), and the red-team found actions outside the allow-list (R-026). Unapproved public AI tools are blocked (R-029, treatment Avoid).
6. **Legacy voice (ER-03).** 61 TDM switches past vendor support (R-025) and clear-text CDR collection from 41 of them (R-017) are retired with the switches by 2028.

## 7. Treatment summary
- **Funded (2026 Q4 to 2027 Q2), about $9.8 million:** management plane remediation and jump hosts ($3.1M), network log and flow onboarding ($1.6M), AQ identity federation and segmentation ($1.9M), AQ-02 SBC replacement ($1.2M), BSS automated failover ($0.6M), care vendor authentication controls and sampling ($0.4M), CPNI read analytics ($0.5M), portal reset rebuild for AQ-02 ($0.3M), and outside counsel for the disclosure tabletop ($0.2M). Items map to the POA&M in P07.
- **Accepted (8):** R-021, R-032, R-041, R-047, R-050, R-052, R-057, R-062. Each is Low residual with strong existing controls, accepted at the right level (section 1) and reviewed within 12 months.
- **Avoided (1):** R-029. Unapproved generative AI domains are blocked at the web gateway.
- **Very High risk R-001:** not accepted as is. The CEO and CFO approved the treatment plan and the residual target of High on 2026-09-08; the board risk and technology committee reviewed it on 2026-09-10.

## 8. Board reporting
**Risk and technology committee of the board (quarterly):** the enterprise risk profile (section 4), every Very High and High risk with its treatment status and KRI trend, risks outside tolerance, new risks since the last meeting, and risk acceptances made. The 2026-09-10 meeting received this report, the Internal Audit results (P07), and the regulatory roadmap (P03).
**Audit committee (quarterly):** Internal Audit results, SOX IT general control status (R-032), and disclosure controls (R-014). The audit committee also reviews the annual Item 106 disclosure draft, which describes this process.
**Management:** the executive risk committee meets monthly and reviews KRIs for all risks outside tolerance.

## 9. Approval
- Executive risk committee: approved the register, treatments, and acceptances, 2026-09-08.
- CEO and CFO: approved the treatment plan and residual target for Very High risk R-001, 2026-09-08.
- Risk and technology committee of the board: reviewed the enterprise risk profile, 2026-09-10.
- Next full review: June to July 2027, or sooner after a major change, incident, or acquisition. KRIs are refreshed quarterly.
