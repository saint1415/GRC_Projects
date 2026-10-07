# Enterprise Risk Register Report: Cris Santos Company | Financial Services | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded merchant payment processor; about 410,000 merchants; three sponsor banks; NYDFS-licensed payouts subsidiary) |
| Size tier | Enterprise (12,000 employees) |
| Vertical | Financial Services (CISA critical infrastructure sector) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) for each risk; NIST IR 8286 Rev. 1 for integration into enterprise risk management (ERM) |
| Also satisfies | FTC Safeguards Rule written risk assessment (16 CFR 314.4(b)); PCI DSS risk analysis inputs (12.3.1); the payouts subsidiary's annual risk assessment (23 NYCRR 500.9); input to the Reg S-K Item 106 description of risk management processes (17 CFR 229.106(b)) |
| Prepared | 2026-06-01 to 2026-07-31 by the GRC team for the CISO; updated 2026-08-28 with Internal Audit findings (P07) |
| Approved | Executive risk committee (chaired by the Chief Risk Officer), 2026-09-08; reviewed by the board risk and technology committee, 2026-09-10 |

## 1. Scope and risk framing
**Scope.** All systems that store, process, or transmit cardholder data, merchant data, or funding instructions, or that support tier-1 processes: the Cloud A and Cloud B estates, DC-1 and DC-2, SaaS, the payouts subsidiary, and about 1,400 vendors (96 of them PCI DSS service providers). Business processes and impact values come from the enterprise BIA (P05). The Core Payment Processing Platform is also covered at system level in the SSP (P02).

**Three lines.** Risk owners in the business and technology (first line) own and treat risks. The GRC team and the Chief Risk Officer (second line) run this method and roll risks up into the enterprise risk register. Internal Audit (third line) tests controls independently (P07).

**Risk appetite (board-approved, 2026-02).** Qualitative statements set by the board:
- **Payment processing continuity:** low appetite for disruption of authorization or merchant funding.
- **Cardholder and customer data:** low appetite for unauthorized disclosure.
- **Sponsor bank, card network, and regulatory obligations:** very low appetite for breaching sponsor agreements, network rules, notice duties, or SEC disclosure rules.
- **Fraud and financial integrity:** low to moderate appetite; fraud losses are inherent in card acceptance and are managed within budgeted loss rates.
- **Technology change and AI:** moderate appetite, provided risks are identified and funded at the time of the decision.

**Risk tolerance (measurable, per enterprise risk).** The highest residual risk level each enterprise risk may carry without a board-reported treatment plan. A risk above its threshold is **Outside tolerance** in the register.

| Enterprise risk | Tolerance threshold |
|---|---|
| ER-01 Payment processing disruption (authorization, settlement, funding) | Moderate |
| ER-02 Compromise of cardholder and customer data | Moderate |
| ER-03 Third-party and concentration risk | Moderate |
| ER-04 Sponsor bank and card network obligations | Low |
| ER-05 Financial integrity and fraud | Moderate |
| ER-06 Regulatory and disclosure compliance | Low |
| ER-07 Legacy technology and skills | Moderate |
| ER-08 Responsible use of AI and models | Moderate |

**Who can accept risk:**
| Residual level | Acceptance authority |
|---|---|
| Very Low, Low | Risk owner (vice president or director) with GRC concurrence |
| Moderate | CISO with the accountable executive |
| High | Executive risk committee (Chief Risk Officer, CTO, CIO, COO, CISO, General Counsel), reported to the board risk and technology committee |
| Very High | CEO and CFO jointly, reported to the board risk and technology committee at its next meeting |

Risks under ER-04 and ER-06 at Moderate or above cannot be accepted without a dated treatment plan. Any acceptance expires after 12 months.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the financial sector threat picture (payment card theft, ransomware, file transfer product exploitation, third-party compromise, fraud), the BIA (P05), the gap analysis (P03), and the Internal Audit assessment (P07).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial), and likelihood of adverse impact, combined with **Table G-5**.
3. **Rate impact.** **Table H-3**, calibrated to the BIA impact values (P05 section 3).
4. **Determine risk.** **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the tables, not assigned by hand.
5. **Integrate with ERM (NIST IR 8286 Rev. 1).**
   - Each cybersecurity risk is a row in this register, with an owner, a treatment, and a key risk indicator (KRI).
   - Each row is normalized into one of **8 enterprise risks (ER-01 to ER-08)** in the Chief Risk Officer's enterprise risk register, with an ERM category (operational, compliance, financial, strategic).
   - **Aggregation rule:** an enterprise risk's exposure equals its highest constituent risk level, and the profile also reports how many constituent risks sit outside tolerance. This keeps one severe risk from being averaged away.
   - The enterprise risk profile (section 4) is what the board risk and technology committee sees each quarter.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 2 |
| High | 12 |
| Moderate | 33 |
| Low | 18 |
| **Total** | **65** |

By threat source type: Adversarial 33, Structural 17, Accidental 10, Environmental 5.
By treatment: Mitigate 54, Accept 10, Avoid 1.
By status: In progress 47, Open 8, Closed (accepted) 10.
**21 risks are outside tolerance**, and each has a dated treatment plan. 21 risks are board-reported (every Very High and High risk, plus the Moderate risks outside tolerance).

## 4. Enterprise risk profile (roll-up for the board)
| ID | Enterprise risk | ERM category | Risks | Very High | High | Moderate | Low | Exposure (highest) | Tolerance | Outside tolerance |
|---|---|---|---|---|---|---|---|---|---|---|
| ER-01 | Payment processing disruption | Operational | 7 | 1 | 1 | 2 | 3 | **Very High** | Moderate | 2 |
| ER-02 | Compromise of cardholder and customer data | Compliance and reputational | 19 | 1 | 6 | 7 | 5 | **Very High** | Moderate | 7 |
| ER-03 | Third-party and concentration risk | Operational | 9 | 0 | 3 | 4 | 2 | **High** | Moderate | 3 |
| ER-04 | Sponsor bank and card network obligations | Compliance | 5 | 0 | 0 | 5 | 0 | **Moderate** | Low | 5 |
| ER-05 | Financial integrity and fraud | Financial | 8 | 0 | 0 | 7 | 1 | **Moderate** | Moderate | 0 |
| ER-06 | Regulatory and disclosure compliance | Compliance | 8 | 0 | 1 | 2 | 5 | **High** | Low | 3 |
| ER-07 | Legacy technology and skills | Strategic | 3 | 0 | 1 | 2 | 0 | **High** | Moderate | 1 |
| ER-08 | Responsible use of AI and models | Strategic | 6 | 0 | 0 | 4 | 2 | **Moderate** | Moderate | 0 |

**Reading the profile:**
- **ER-02 (data compromise)** carries the most risks and one of the two Very High risks: theft of card data at scale (R-001). The open conditions that keep its likelihood up are the MFT monitoring gap (R-003), the segmentation path after the interconnect change (R-025), partner-hosted payment fields (R-010), push-based MFA in Cloud B (R-006), and the plain-text scheduler credentials found by Internal Audit (R-058).
- **ER-01 (processing disruption)** carries the other Very High risk: ransomware on the settlement platform that delays funding past bank cutoffs (R-002). The 9.5-hour settlement recovery in the last test (R-004) is why its impact cannot be reduced yet.
- **ER-04 (sponsor bank and card network obligations)** has no High risk but all five of its risks are outside its Low tolerance: Bank C notice contacts (R-013), no joint recovery procedure with the banks (R-014), a possible ROC finding (R-038), Bank C scope documentation (R-060), and SOC 2 readiness for the settlement service line (R-064).
- **ER-06 (regulatory and disclosure)** is outside tolerance mainly because the SEC materiality process has not been exercised with the current disclosure committee (R-012) and the NYDFS 72-hour notice is not in the playbook (R-015).
- **ER-08 (AI)** is within tolerance today, but 5 of 12 use cases lack committee review (R-056), so the rating depends on the reviews due 2026-11-30.

## 5. Top risks (Very High and High)
| Risk ID | Risk | Level | Enterprise risk | Treatment | Owner | Due |
|---|---|---|---|---|---|---|
| R-001 | Attacker compromises the CDE and steals card data at scale | Very High | ER-02 | MFT monitoring (POAM-009); segmentation fix (POAM-003); partner payment fields (POAM-021); disclosure tabletop (POAM-005) | CISO | 2027-03-31 |
| R-002 | Ransomware on the settlement platform delays funding past bank cutoffs | Very High | ER-01 | Replace unsupported servers (POAM-001); vault credentials (POAM-002); operator MFA (POAM-004); recovery automation and retest (POAM-006) | Senior Vice President, Core Payment Platforms | 2027-06-30 |
| R-003 | Zero-day exploitation of the MFT appliances | High | ER-03 | File-level logging and egress allow-listing (POAM-009); 72-hour emergency patching; second product evaluation | Director of Settlement Systems | 2026-12-31 |
| R-004 | Settlement recovery exceeds the 6-hour RTO | High | ER-01 | Scheduler automation; retest with Bank A (POAM-006; POAM-016) | Senior Vice President, Settlement and Treasury Operations | 2027-03-31 |
| R-005 | Exploitation of unsupported settlement servers | High | ER-07 | Compensating controls documented; replacement (POAM-001) | Director of Settlement Systems | 2027-06-30 |
| R-006 | Phishing defeats push MFA for Cloud B administrators | High | ER-02 | Phishing-resistant keys and full PAM coverage (POAM-019) | Director of Identity and Access Management | 2027-01-31 |
| R-007 | Over-privileged Cloud B pipeline service account abused | High | ER-02 | Short-lived workload identity (POAM-020) | Executive Vice President, Integrated Payments | 2026-12-15 |
| R-008 | Provider-wide Cloud A outage stops authorization | High | ER-03 | Provider-wide outage playbook; minimum authorization capability study | Chief Technology Officer | 2027-06-30 |
| R-010 | Skimming script in partner-hosted payment fields | High | ER-02 | Full tamper-detection coverage; partner attestations (POAM-021) | Executive Vice President, Integrated Payments | 2027-01-31 |
| R-012 | Material incident disclosed late or inaccurately | High | ER-06 | Playbook update; new member briefings; tabletop 2026-11-12 (POAM-005) | General Counsel | 2026-11-30 |
| R-016 | PAN in call recordings and data lake tables exposed | High | ER-02 | Automatic pause-and-resume; recording purge; wider PAN discovery (POAM-014) | Chief Data and Analytics Officer | 2027-01-31 |
| R-025 | Attacker uses the unintended path into the Cloud A CDE | High | ER-02 | Route fix; guardrail code; retest (POAM-003) | Director of Data Center and Network Engineering | 2026-10-15 |
| R-035 | Malicious code in a tier-1 vendor update | High | ER-03 | Hash verification; SBOM requests | Director of Third-Party Risk Management | 2027-06-30 |
| R-058 | Reuse of batch scheduler credentials found in plain text | High | ER-02 | Script scanning and secret blocking (POAM-002) | Director of Settlement Systems | 2026-12-15 |

## 6. Themes from the 2026 analysis
1. **The settlement platform is where old and new risk meet (ER-01, ER-02, ER-07).** It runs on a mainframe and 46 midrange servers, 12 of them unsupported. Internal Audit found plain-text batch credentials, password-only operator sign-in since 2026-02, emergency changes without timely approval, and daily (not near real-time) log forwarding. Recovery took 9.5 hours against a 6-hour RTO. Together these drive R-002, R-004, R-005, R-026, R-029, R-030, and R-058. Treatment is funded through 2027-06-30; full modernization is planned for 2028.
2. **File transfer is the soft edge of settlement (ER-03).** Every clearing and funding file passes through one MFT product that cannot run EDR. Mass exploitation of file transfer products is a recurring pattern across industries, so this is the initial access path rehearsed in P08 (R-003).
3. **The banks are part of recovery, not just recipients of notices (ER-04).** Three sponsor banks depend on the company's funding files, but none has joined a recovery test, and Bank C's designated contacts are not loaded (R-013, R-014). A 4-hour disruption of covered services requires notice to all three banks under three different rules with identical text (12 CFR 53.4, 304.24, 225.303).
4. **Cloud B lags Cloud A on identity (ER-02).** Push-based MFA, partial PAM coverage, and a standing pipeline administrator (R-006, R-007).
5. **Disclosure readiness (ER-06).** The SEC materiality process has not been exercised with the current committee, and the NYDFS 72-hour notice is not built into the same timeline (R-012, R-015). A full tabletop is set for 2026-11-12.
6. **AI (ER-08).** 12 use cases; 7 reviewed; the vendor underwriting model has no independent validation or fairness testing (R-020, R-056).

## 7. Treatment summary
- **Funded (2026 Q4 to 2027 Q2), about $14.8 million:** midrange server replacement ($5.6M), settlement recovery automation and DC-2 replication upgrade ($2.9M), phishing-resistant keys and PAM expansion for Cloud B ($1.7M), MFT monitoring and a second-product evaluation ($1.2M), partner payment field tamper-detection ($1.1M), mainframe MFA gateway ($0.9M), contact center pause-and-resume automation ($0.8M), PAN discovery expansion ($0.4M), and outside counsel and facilitation for the disclosure tabletop ($0.2M). Items map to the POA&M in P07.
- **Accepted (10):** R-009, R-044, R-045, R-046, R-047, R-050, R-051, R-061, R-062, R-063. Each is Low or Moderate residual with strong existing controls, accepted at the right level (section 1) and reviewed within 12 months.
- **Avoided (1):** R-021. Public generative AI domains are blocked at the proxy; staff use the approved enterprise assistant.
- **Very High risks R-001 and R-002:** not accepted as is. The CEO and CFO approved the treatment plans and the residual target of High for both on 2026-09-08; the board risk and technology committee reviewed them on 2026-09-10.

## 8. Board reporting
**Risk and technology committee of the board (quarterly):** the enterprise risk profile (section 4), every Very High and High risk with its treatment status and KRI trend, risks outside tolerance, new risks since the last meeting, and acceptances made. The CISO's written annual report under 16 CFR 314.4(i), which also serves as the CISO's annual report for the payouts subsidiary under 23 NYCRR 500.4(b) when it covers that rule's content (POAM-023), goes to this committee. The 2026-09-10 meeting received this report, the Internal Audit results (P07), and the compliance roadmap (P03).
**Audit committee (quarterly):** Internal Audit results, SOX IT general control status, and the disclosure controls topics (R-012, R-057). The audit committee also reviews the annual Item 106 disclosure draft, which describes this process.
**Management:** the executive risk committee meets monthly and reviews KRIs for all risks outside tolerance.

## 9. Approval
- Executive risk committee: approved the register, treatments, and acceptances, 2026-09-08.
- CEO and CFO: approved the treatment plans and residual targets for Very High risks R-001 and R-002, 2026-09-08.
- Board risk and technology committee: reviewed the enterprise risk profile, 2026-09-10.
- Next full review: June to July 2027, or sooner after a major change, incident, acquisition, or new sponsor bank. KRIs are refreshed quarterly.
