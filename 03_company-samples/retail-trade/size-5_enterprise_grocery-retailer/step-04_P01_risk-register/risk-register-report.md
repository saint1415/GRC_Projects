# Enterprise Risk Register Report: Cris Santos Company | Retail Trade | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded regional supermarket chain: 112 stores in FL, GA, AL, SC, TN; online ordering; 2 distribution centers) |
| Size tier | Enterprise (12,000 employees) |
| Vertical | Retail Trade |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) for each risk; NIST IR 8286 Rev. 1 for integration into enterprise risk management (ERM) |
| Also satisfies | PCI DSS v4.0.1 Requirement 12.3.1 enterprise risk input (targeted risk analyses are kept separately by the PCI Program Manager); input to the Reg S-K Item 106 description of risk management processes |
| Prepared | 2026-06-01 to 2026-07-31 by the GRC team for the CISO; updated 2026-08-28 with Internal Audit findings (P07) |
| Approved | Executive risk committee (chaired by the Chief Risk Officer), 2026-09-08; reviewed by the risk and technology committee of the board, 2026-09-10 |

## 1. Scope and risk framing
**Scope.** All systems that store, process, or transmit card data or customer personal information, or that support tier-1 processes, across the 112 stores, the 2 distribution centers, the two cloud estates and two colocation sites, the 14 acquired-banner (AB) stores, and the roughly 1,100 vendors (71 TPSPs). Business processes and impact values come from the enterprise BIA (P05). The Omnichannel Commerce and Payments Platform (OCPP) is also covered at system level in the SSP (P02).

**Three lines.** Risk owners in the business and technology (first line) own and treat risks. The GRC team and the Chief Risk Officer (second line) run this method and roll risks up into the enterprise risk register. Internal Audit (third line) tests controls independently (P07); the QSA validates PCI DSS separately.

**Risk appetite (board-approved, 2026-02).** Qualitative statements set by the board:
- **Food safety:** very low appetite for technology-related failures that could let unsafe food reach customers.
- **Regulatory, card brand, and disclosure:** very low appetite for noncompliance with SEC disclosure rules, SNAP retailer obligations, consumer protection law, or the merchant agreement.
- **Store and checkout continuity:** low appetite for disruption of checkout and online ordering.
- **Payment card and customer data:** low appetite for compromise.
- **Growth and innovation (acquisitions, AI, retail media):** moderate appetite, provided risks are identified and funded before or at the time of the decision.

**Risk tolerance (measurable, per enterprise risk).** The highest residual risk level each enterprise risk may carry without a board-reported treatment plan. A risk above its threshold is **Outside tolerance** in the register.

| Enterprise risk | Tolerance threshold |
|---|---|
| ER-01 Store and checkout disruption from cyber and technology events | Moderate |
| ER-02 Compromise of payment card data | Moderate |
| ER-03 Compromise of customer personal information | Moderate |
| ER-04 Third-party and concentration risk | Moderate |
| ER-05 Integration of the acquired banner | Moderate |
| ER-06 Food safety and store operational technology | Low |
| ER-07 Regulatory, card brand, and disclosure compliance | Low |
| ER-08 Responsible use of AI and customer data | Moderate |
| ER-09 Financial reporting integrity and fraud | Low |

**Who can accept risk:**
| Residual level | Acceptance authority |
|---|---|
| Very Low, Low | Risk owner (vice president or director) with GRC concurrence |
| Moderate | CISO with the accountable executive |
| High | Executive risk committee (Chief Risk Officer, CIO, COO, CFO, CISO, General Counsel), reported to the board risk and technology committee |
| Very High | CEO and CFO jointly, reported to the board risk and technology committee at its next meeting |

Food safety risks (ER-06) at High or above cannot be accepted without a dated treatment plan. A risk outside tolerance cannot be accepted; it must be treated. Any acceptance expires after 12 months.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the retail threat picture (e-commerce skimming, POS malware, ransomware, account takeover, third-party concentration), the BIA (P05), the gap analysis (P03), and the Internal Audit assessment (P07).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial), and likelihood of adverse impact, combined with **Table G-5**.
3. **Rate impact.** **Table H-3**, calibrated to the BIA impact values (P05 section 3).
4. **Determine risk.** **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the tables, not assigned by hand.
5. **Integrate with ERM (NIST IR 8286 Rev. 1).**
   - Each system-level cybersecurity risk is a row in this register, with an owner, a treatment, and a key risk indicator (KRI).
   - Each row is normalized into one of **9 enterprise risks (ER-01 to ER-09)** in the Chief Risk Officer's enterprise risk register, with an ERM category.
   - **Aggregation rule:** an enterprise risk's exposure equals its highest constituent risk level, and the profile also reports how many constituent risks sit outside tolerance. One severe risk is never averaged away.
   - The enterprise risk profile (section 4) is what the board risk and technology committee sees each quarter.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 8 |
| Moderate | 43 |
| Low | 12 |
| **Total** | **64** |

By threat source type: Adversarial 34, Structural 23, Accidental 6, Environmental 1.
By treatment: Mitigate 49, Accept 12, Avoid 2, Share/Transfer 1.
By status: In progress 45, Open 5, Closed (accepted) 12, Closed (avoided) 2.
**20 risks are outside tolerance** and each has a dated treatment plan.

## 4. Enterprise risk profile (roll-up for the board)
| ID | Enterprise risk | ERM category | Risks | Very High | High | Moderate | Low | Exposure (highest) | Tolerance | Outside tolerance |
|---|---|---|---|---|---|---|---|---|---|---|
| ER-01 | Store and checkout disruption from cyber and technology events | Operational | 12 | 1 | 1 | 10 | 0 | **Very High** | Moderate | 2 |
| ER-02 | Compromise of payment card data | Compliance and financial | 7 | 0 | 1 | 5 | 1 | **High** | Moderate | 1 |
| ER-03 | Compromise of customer personal information | Compliance and reputational | 8 | 0 | 0 | 4 | 4 | **Moderate** | Moderate | 0 |
| ER-04 | Third-party and concentration risk | Operational | 7 | 0 | 3 | 4 | 0 | **High** | Moderate | 3 |
| ER-05 | Integration of the acquired banner | Strategic | 5 | 0 | 1 | 4 | 0 | **High** | Moderate | 1 |
| ER-06 | Food safety and store operational technology | Operational and safety | 4 | 0 | 1 | 2 | 1 | **High** | Low | 3 |
| ER-07 | Regulatory, card brand, and disclosure compliance | Compliance | 8 | 0 | 1 | 6 | 1 | **High** | Low | 7 |
| ER-08 | Responsible use of AI and customer data | Strategic | 7 | 0 | 0 | 5 | 2 | **Moderate** | Moderate | 0 |
| ER-09 | Financial reporting integrity and fraud | Financial | 6 | 0 | 0 | 3 | 3 | **Moderate** | Low | 3 |

**Reading the profile:**
- **ER-01 (store and checkout disruption)** carries the only Very High risk, chain-wide ransomware (R-001). The acquired banner (R-003, ER-05) and store OT (R-007, ER-06) are the main reasons its likelihood is not lower.
- **ER-02 (payment card data)** is driven by e-commerce skimming (R-002). Encryption at the PIN pad keeps in-store POS malware at Moderate (R-004), so the card data exposure has moved to the browser.
- **ER-04 (third parties)** has three High risks: processor concentration (R-005), TPSP compliance (R-006), and software supply chain (R-025).
- **ER-06 (food safety and store OT)** has the lowest tolerance; refrigeration tampering (R-007) and the new ESL credential finding (R-062) put it outside tolerance.
- **ER-07 (regulatory and disclosure)** is outside tolerance mainly because the materiality process has never been exercised for a card compromise (R-010), and because Tennessee Act assessments (R-014) and PCI DSS targeted risk analyses (R-053) are incomplete.
- **ER-08 (AI and customer data)** is within tolerance today, but 5 of 12 use cases lack committee review (R-013), so the rating depends on the reviews due 2026-11-30.

## 5. Top risks (Very High and High)
| Risk ID | Risk | Level | Enterprise risk | Treatment | Owner | Due |
|---|---|---|---|---|---|---|
| R-001 | Ransomware encrypts store, payment, supply chain, and e-commerce systems across regions | Very High | ER-01 | AB conversion and interim segmentation (POAM-001); OT segmentation (POAM-005); annual ransomware exercise including the disclosure committee (POAM-010) | CISO | 2027-03-31 |
| R-002 | Malicious script on payment pages (e-commerce skimming) captures card data that customers type at checkout | High | ER-02 | Extend inventory, integrity values, and tamper detection to express checkout and cart pages; remove the tag manager from payment pages; targeted penetration test (POAM-002) | Director of E-commerce Engineering | 2026-10-16 |
| R-003 | Attacker on an AB store network captures clear-text card data between legacy PIN pads and store servers | High | ER-05 | Conversion wave 1 (5 Alabama stores) by 2026-12-15 and wave 2 (9 Tennessee stores) by 2027-03-31 (POAM-001); interim SIEM collectors and daily review (POAM-009) | Vice President, Integration Management Office | 2027-03-31 |
| R-005 | Primary processor outage lasts beyond the 4-hour store-and-forward window | High | ER-04 | Write and test the extended outage procedure (POAM-016); evaluate a secondary processor for card-present volume | Vice President, Payments | 2027-03-31 |
| R-006 | A third-party service provider with PCI DSS responsibilities is breached or falls out of compliance | High | ER-04 | Collect AOCs, complete responsibility matrices, and add AOC delivery terms at renewal (POAM-003) | Director of Third-Party Risk Management | 2026-11-30 |
| R-007 | Refrigeration or building controls are tampered with through a vendor remote tool or the shared store VLAN, and spoilage goes undetected | High | ER-06 | Move vendor access to PAM (POAM-004); segment OT (POAM-005); exercise the manual fallback | Director of Facilities Engineering | 2027-01-31 |
| R-010 | A material card data incident is disclosed late or inaccurately because the materiality process fails under pressure | High | ER-07 | Update the playbook; full tabletop with the disclosure committee on 2026-11-12 (POAM-010) | General Counsel | 2026-11-30 |
| R-020 | Zero-day in an internet-facing edge device (VPN or firewall) is exploited | High | ER-01 | Retire the AB legacy VPN at conversion; replace remaining remote access VPN with the zero-trust service | Director of Network Engineering | 2027-03-31 |
| R-025 | Malicious code arrives in a POS or payment switch software update | High | ER-04 | Require software bills of materials and signed packages from POS and switch vendors; 72-hour pilot-store soak | CISO | 2027-06-30 |

## 6. Themes from the 2026 analysis
1. **The card data exposure moved to the browser (ER-02).** In-store card data is encrypted at the PIN pad, but online card data passes through the customer's browser on pages the company controls. 47 scripts load on payment pages, and the express checkout and cart pages are outside the script controls (R-002, R-036). This is also the P08 scenario.
2. **Acquired banner (ER-05).** The 14 AB stores send clear-text card data across flat networks to a legacy processor link, with a shared administrator account and no SIEM feed (R-003, R-018, R-019, R-052). Conversion is due in two waves by 2027-03-31; going forward, deal approvals must include security due diligence and integration funding (R-061).
3. **Third-party concentration (ER-04).** One processor carries 98% of card volume (R-005, R-064), one delivery provider carries 62% of home deliveries (R-016), and 9 TPSPs lack a current AOC (R-006).
4. **Store OT and food safety (ER-06).** Refrigeration vendors use always-on remote tools, OT shares the back-office VLAN at 37 stores, and testing found default credentials on ESL base stations (R-007, R-055, R-062).
5. **Materiality and disclosure (ER-07).** The disclosure committee has not exercised a card compromise, and the card brand and forensic steps are not tied to the materiality timeline (R-010). A full tabletop is set for 2026-11-12.
6. **AI and customer data (ER-08).** Pricing fairness is tested only by store cluster (R-011), emergency price freezes cover only Florida (R-012), Tennessee assessments are incomplete (R-014), and clean room thresholds are not enforced everywhere (R-015).

## 7. Treatment summary
- **Funded (2026 Q4 to 2027 Q2), about $7.4 million:** AB POS conversion and encrypting PIN pads ($3.6M), NAC and OT segmentation at the remaining stores ($1.3M), payment page script protection for all checkout paths ($420K), identity federation for AB staff ($380K), PAM onboarding for refrigeration vendors ($260K), delivery surge contracts and volume test ($240K), switch EBT failover test and voucher drills ($180K), TPSP assurance and contract work ($150K), fairness testing tooling for pricing and offers ($310K), outside counsel for the disclosure tabletop ($40K), and Tennessee data protection assessments with outside privacy counsel ($110K), with the remainder in staff time. Items map to the POA&M in P07.
- **Accepted (12):** R-004, R-021, R-026, R-030, R-032, R-043, R-044, R-045, R-048, R-049, R-058, R-059. Each is Low or Moderate residual, within tolerance, with strong existing controls, accepted at the right level (section 1) and reviewed within 12 months.
- **Avoided (2):** R-040, R-041. Facial recognition is prohibited by the board, and AI resume ranking stays disabled until review.
- **Shared (1):** R-060, through a higher payment card sublimit in the 2027 cyber insurance renewal.
- **Very High risk R-001:** not accepted as is. The CEO and CFO approved the treatment plan and the residual target of High on 2026-09-08; the board risk and technology committee reviewed it on 2026-09-10.

## 8. Board reporting
**Risk and technology committee of the board (quarterly):** the enterprise risk profile (section 4), every Very High and High risk with its treatment status and KRI trend, risks outside tolerance, new risks since the last meeting, risk acceptances made, and PCI DSS validation status. The 2026-09-10 meeting received this report, the Internal Audit results (P07), and the regulatory roadmap (P03).
**Audit committee (quarterly):** Internal Audit results, SOX IT general control status (R-026), and the disclosure controls topics (R-010). The audit committee also reviews the annual Item 106 disclosure draft, which describes this process.
**Management:** the executive risk committee meets monthly and reviews KRIs for all risks outside tolerance; the payments security council (Vice President, Payments, chair) meets monthly on ER-02 risks and the ROC.

## 9. Approval
- Executive risk committee: approved the register, treatments, and acceptances, 2026-09-08.
- CEO and CFO: approved the treatment plan and residual target for Very High risk R-001, 2026-09-08.
- Risk and technology committee of the board: reviewed the enterprise risk profile, 2026-09-10.
- Next full review: June to July 2027, or sooner after a major change, incident, acquisition, or the AB conversion waves. KRIs are refreshed quarterly.
