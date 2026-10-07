# Enterprise Cyber Risk Register Report: Cris Santos Company | Finance and Insurance | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded bank holding company: Cris Santos Bank, N.A., 610 branches in FL, GA, AL, SC, NC, TN; Cris Santos Investment Services, LLC) |
| Size tier | Enterprise (12,000 employees; $86.4 billion in average total consolidated assets) |
| Vertical | Finance and Insurance |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) for each risk; NIST IR 8286 Rev. 1 for integration into enterprise risk management (ERM) |
| Also satisfies | The risk assessment in the Interagency Guidelines (12 CFR 30 App. B III.B.1 to III.B.3); independent risk management's ongoing assessment of material aggregate risks (App. D II.C.2.(b)); input to the Reg S-K Item 106 description of risk management processes |
| Prepared | 2026-05-04 to 2026-07-10 by the GRC team with Technology and Operational Risk; updated 2026-08-14 with Internal Audit findings (P07) |
| Approved | Executive risk committee (chaired by the Chief Risk Officer), 2026-09-18; the risk profile was reviewed by the board risk committee on 2026-09-15 |

## 1. Scope and risk framing
**Scope.** All systems that hold customer information or support tier-1 processes across the bank, the broker-dealer, and the parent: the core and payments hub in DC-1 and DC-2, both cloud estates, 610 branches and about 1,480 ATMs, the treasury management platform, the acquired bank's remaining legacy platform, the AI portfolio, and about 2,400 third parties (41 critical). Business processes and impact values come from the enterprise BIA (P05). The CBDC platform is also covered at system level in the SSP (P02).

**Three lines.** Risk owners in the business and technology (first line) own and treat risks. The Chief Risk Officer's independent risk management (second line), including Technology and Operational Risk, Model Risk Management, and Third-Party Risk Management, sets this method, challenges the ratings, and rolls risks up into the enterprise risk register, as App. D II.C.2 expects. Internal Audit (third line) tests controls independently (P07). **Known structural weakness:** the cyber risk oversight team that performs second-line challenge of cybersecurity still reports through the CISO to the CIO (R-006; P03 G-046).

**Risk appetite (board-approved risk appetite statement, 2026-01-27).** The statement has qualitative components and quantitative limits (App. D II.E). The cyber and technology parts:
- **Customer money and payments:** very low appetite for losses from payment fraud caused by bank control failures; quantitative limit: net fraud losses from bank-side control failures under $15 million a year.
- **Critical services:** low appetite for disruption; limit: no tier-1 service down longer than its BIA RTO more than twice a year.
- **Customer information:** low appetite for unauthorized disclosure; limit: zero incidents requiring notice to more than 10,000 customers.
- **Regulatory and disclosure:** very low appetite for missed notifications, filings, or violations of consumer financial law (including Regulation B).
- **Innovation (AI, digital channels, acquisitions):** moderate appetite, provided risks are identified, validated, and funded before or at the time of the decision.

**Risk tolerance (measurable, per enterprise risk).** The highest residual risk level each enterprise risk may carry without a board-reported treatment plan. A risk above its threshold is **Outside tolerance** in the register, which is a risk limit breach under the breach protocol (App. D II.H).

| Enterprise risk | Tolerance threshold |
|---|---|
| ER-01 Disruption of critical banking services from cyber and technology events | Moderate |
| ER-02 Compromise of customer information | Moderate |
| ER-03 Payments fraud and account takeover | Moderate |
| ER-04 Third-party and concentration risk | Moderate |
| ER-05 Legacy technology and acquisition integration | Moderate |
| ER-06 Regulatory, supervisory, and disclosure compliance | Low |
| ER-07 Model and AI risk, including fair lending | Moderate |
| ER-08 Insider risk and financial reporting integrity | Low |

**Who can accept risk:**
| Residual level | Acceptance authority |
|---|---|
| Very Low, Low | Risk owner (executive or director) with second-line concurrence |
| Moderate | CISO with the accountable executive, with the Director of Technology and Operational Risk concurring |
| High | Executive risk committee (Chief Risk Officer, CIO, COO, CISO, General Counsel), reported to the board risk committee |
| Very High | CEO and CFO jointly, reported to the board risk committee at its next meeting |

Risks in ER-06 (regulatory and disclosure) above Low cannot be accepted without a dated treatment plan. Any acceptance expires after 12 months.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the financial sector threat picture (business email compromise, account takeover, ransomware and destructive attacks, third-party concentration), the BIA (P05), the gap analysis (P03), and the Internal Audit assessment (P07).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial), and likelihood of adverse impact, combined with **Table G-5**.
3. **Rate impact.** **Table H-3**, calibrated to the BIA impact values (P05 section 3).
4. **Determine risk.** **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the tables, not assigned by hand.
5. **Integrate with ERM (NIST IR 8286 Rev. 1).**
   - Each system-level cybersecurity risk is a row in this register, with an owner, a treatment, and a key risk indicator (KRI).
   - Each row is normalized into one of **8 enterprise risks (ER-01 to ER-08)** in the Chief Risk Officer's enterprise risk register, with an ERM category.
   - **Aggregation rule:** an enterprise risk's exposure equals its highest constituent risk level, and the profile also reports how many constituent risks sit outside tolerance. This keeps one severe risk from being averaged away.
   - The enterprise risk profile (section 4) is what the board risk committee sees each quarter (12 CFR 252.22(a)(3)(iv); App. D II.G.3).

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 10 |
| Moderate | 36 |
| Low | 19 |
| **Total** | **66** |

By threat source type: Adversarial 31, Structural 28, Accidental 5, Environmental 2.
By treatment: Mitigate 55, Accept 8, Avoid 2, Share/Transfer 1.
By status: In progress 53, Open 3, Closed (accepted) 8, Closed (avoided) 2.
**16 risks are outside tolerance** and each has a dated treatment plan.

## 4. Enterprise risk profile (roll-up for the board)
| ID | Enterprise risk | ERM category | Risks | Very High | High | Moderate | Low | Exposure (highest) | Tolerance | Outside tolerance |
|---|---|---|---|---|---|---|---|---|---|---|
| ER-01 | Disruption of critical banking services from cyber and technology events | Operational | 10 | 1 | 0 | 6 | 3 | **Very High** | Moderate | 1 |
| ER-02 | Compromise of customer information | Compliance and reputational | 9 | 0 | 2 | 4 | 3 | **High** | Moderate | 2 |
| ER-03 | Payments fraud and account takeover | Operational (fraud) | 14 | 0 | 3 | 8 | 3 | **High** | Moderate | 3 |
| ER-04 | Third-party and concentration risk | Operational | 6 | 0 | 3 | 3 | 0 | **High** | Moderate | 3 |
| ER-05 | Legacy technology and acquisition integration | Strategic | 6 | 0 | 1 | 3 | 2 | **High** | Moderate | 1 |
| ER-06 | Regulatory, supervisory, and disclosure compliance | Compliance | 10 | 0 | 0 | 5 | 5 | **Moderate** | Low | 5 |
| ER-07 | Model and AI risk, including fair lending | Compliance and strategic | 9 | 0 | 0 | 7 | 2 | **Moderate** | Moderate | 0 |
| ER-08 | Insider risk and financial reporting integrity | Financial | 2 | 0 | 1 | 0 | 1 | **High** | Low | 1 |

**Reading the profile:**
- **ER-01 (service disruption)** carries the only Very High risk: a destructive attack that reaches the core and its replica, because there is no isolated immutable copy of core data (R-002).
- **ER-03 (payments fraud)** has the most risks. Business email compromise (R-001), a compromised bank mailbox in client services (R-005), and wire splitting under the $100,000 confirmation threshold (R-017) are all High. This is why the P08 runbook covers BEC.
- **ER-04 (third parties)** is outside tolerance on three High risks: a critical vendor breach (R-009), a card processor outage (R-010), and a treasury platform outage beyond the BIA RTO (R-022).
- **ER-06 (regulatory and disclosure)** has no High risk but five risks above its Low tolerance, led by the independence gap in second-line cyber oversight (R-006) and by notification timing (R-014, R-015).
- **ER-07 (AI and models)** is within tolerance, but AI-001's fair lending testing for credit cards and its reason codes (R-011, R-012) must close by 2026-12-15 to keep it there.

## 5. Top risks (Very High and High)
| Risk ID | Risk | Level | Enterprise risk | Treatment | Owner | Due |
|---|---|---|---|---|---|---|
| R-002 | Destructive attack encrypts or destroys data center systems, including the core and its replica | Very High | ER-01 | Cyber vault (POAM-020); mainframe privileged access into PAM (POAM-002); annual destructive-attack exercise | CISO | 2027-06-30 |
| R-001 | Business email compromise of commercial clients | High | ER-03 | Out-of-band confirmation of every new beneficiary (POAM-007); new alert rule (POAM-006); BEC training (POAM-015) | Head of Treasury Management | 2027-03-31 |
| R-004 | Fraudulent wires through the acquired bank's legacy commercial platform | High | ER-05 | Accelerate migration; interim callback for every new beneficiary (POAM-004) | Vice President, Integration Management Office | 2027-02-26 |
| R-005 | Compromised bank mailbox in commercial client services used to send or alter payment instructions | High | ER-03 | Phishing-resistant MFA and token protection; inbox rule alerting; training (POAM-015) | CISO | 2026-12-31 |
| R-007 | Privileged mainframe misuse alters core data or audit settings undetected | High | ER-08 | Mainframe privileged IDs into PAM (POAM-002) | Director of Data Center and Mainframe Operations | 2027-03-31 |
| R-008 | Exfiltration of customer NPI from the data platform or digital stores | High | ER-02 | Egress anomaly models; data minimization | Director of Cyber Defense | 2027-03-31 |
| R-009 | Breach at a critical third party with customer information | High | ER-04 | SOC review backlog (POAM-012); notice terms (POAM-019) | Director of Third-Party Risk Management | 2027-03-31 |
| R-010 | Card processor outage stops all authorizations | High | ER-04 | Processor-side stand-in and failover; secondary processor review at renewal | Head of Consumer and Small Business Banking | 2027-09-30 |
| R-017 | Wire splitting under $100,000 to new beneficiaries | High | ER-03 | New alert rule (POAM-006); confirmation of every new beneficiary (POAM-007) | Director of Fraud Strategy | 2026-12-31 |
| R-022 | Treasury platform outage beyond the 2-hour BIA RTO | High | ER-04 | Renegotiate RTO; full-day fallback test (POAM-018) | Head of Treasury Management | 2027-06-30 |
| R-027 | Dormant integration service account used to query the customer information file | High | ER-02 | Disable; review non-expiring credentials (POAM-013) | Head of Digital Banking Technology | 2026-10-31 |

## 6. Themes from the 2026 analysis
1. **Payments fraud is the most frequent loss event (ER-03).** BEC and account takeover produce losses every month. The controls that matter are out of band: callbacks to the number on file, confirmation of new beneficiaries, and alerts on a new beneficiary followed quickly by a payment. The $100,000 threshold for confirmation and the missing alert below it (R-017) are the gaps attackers exploit.
2. **Legacy and integration (ER-05).** The acquired bank's commercial platform (R-004, R-054) and the mainframe's position outside PAM and identity governance (R-007, R-025) are the main legacy exposures.
3. **Resilience against destructive attack (ER-01).** The core is well protected against a site loss (R-030, R-029) but not against an attacker with administrator access to both data centers (R-002).
4. **Third-party concentration (ER-04).** One treasury platform, one card processor, and one clearing firm; contracts and SOC reviews lag (R-022, R-010, R-023, R-024, R-041).
5. **Governance under the heightened standards (ER-06).** The independence of second-line cyber oversight (R-006), manual cyber KRIs (R-046), and the scope of the independent assessment of the risk governance framework (R-047) are App. D issues rather than control failures.
6. **New finding from testing.** Internal Audit found a dormant integration service account with a non-expiring password and query rights to the customer information file (R-027). It was added to this register on 2026-08-14.

## 7. Treatment summary
- **Funded (2026 Q4 to 2027 Q3), about $11.8 million:** cyber vault for core data ($4.6M), mainframe PAM and identity governance connector ($1.9M), acceleration of the legacy platform migration ($1.2M), SIEM onboarding of core maintenance events and fraud use cases ($0.9M), customer authenticator migration away from SMS ($1.4M), treasury fraud rules and out-of-band beneficiary confirmation ($0.7M), third-party review backlog and contract amendments ($0.6M), cyber KRI automation ($0.3M), and AI-001 fair lending testing and reason code work ($0.2M). Items map to the POA&M in P07.
- **Accepted (8):** R-029, R-040, R-044, R-048, R-049, R-057, R-063, R-064. Each is Low residual with strong existing controls, accepted at the right level (section 1) and reviewed within 12 months.
- **Avoided (2):** R-065 (AI resume screening stays disabled) and R-066 (public generative AI tools stay blocked).
- **Shared (1):** R-039 (card-not-present fraud losses are shared through card network rules).
- **Very High risk R-002:** not accepted as is. The CEO and CFO approved the treatment plan and a residual target of High on 2026-09-18; the board risk committee reviewed the plan on 2026-09-15.

## 8. Board reporting
**Board risk committee (quarterly, as 12 CFR 252.22 requires):** the enterprise risk profile (section 4), every Very High and High risk with its treatment status and KRI trend, risks outside tolerance and the breach protocol status (App. D II.H), new risks since the last meeting, and risk acceptances made. The 2026-09-15 meeting received this report, the Internal Audit results (P07), and the regulatory roadmap (P03).
**Audit committee (quarterly):** Internal Audit results, SOX IT general control status, and the disclosure control topics (R-014, R-045). The audit committee also reviews the annual Item 106 disclosure draft, which describes this process.
**Management:** the executive risk committee meets monthly and reviews KRIs for all risks outside tolerance.

## 9. Approval
- Executive risk committee: approved the register, treatments, and acceptances, 2026-09-18.
- CEO and CFO: approved the treatment plan and residual target for Very High risk R-002, 2026-09-18.
- Board risk committee: reviewed the enterprise risk profile, 2026-09-15.
- Next full review: May to July 2027, or sooner after a major change, incident, or acquisition. KRIs are refreshed quarterly.
