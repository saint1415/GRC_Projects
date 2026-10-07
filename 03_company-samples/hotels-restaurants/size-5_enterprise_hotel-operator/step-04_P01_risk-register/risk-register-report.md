# Enterprise Risk Register Report: Cris Santos Company | Accommodation and Food Services | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded hotel franchisor, manager, and owner: 750 hotels, 110 company-operated, in 33 states and DC) |
| Size tier | Enterprise (12,000 employees) |
| Vertical | Accommodation and Food Services |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) for each risk; NIST IR 8286 Rev. 1 for integration into enterprise risk management (ERM) |
| Also satisfies | PCI DSS 12.3 risk analysis input (targeted risk analyses are kept separately); input to the Reg S-K Item 106(b) description of risk management processes |
| Prepared | 2026-06-01 to 2026-07-31 by the GRC team for the CISO; updated 2026-08-28 with Internal Audit findings (P07) |
| Approved | Executive risk committee (chaired by the Chief Risk Officer), 2026-09-08; reviewed by the risk committee of the board, 2026-09-10 |

## 1. Scope and risk framing
**Scope.** All systems that store, process, or transmit card data or guest personal information, or that support tier-1 processes: the CRS and guest profile hub, the Property and Payment Platform (P02), the managed property network that also serves 410 franchised hotels, digital channels and loyalty, the two cloud estates and two colocation hubs, the 9 resorts still on the seller's systems, and about 1,100 vendors. It also covers the risks the company carries for franchised hotels: systems it designs, connects, or manages for them, and the brand harm from franchisee breaches. Business processes and impact values come from the enterprise BIA (P05).

**Three lines.** Risk owners in hotel operations, commercial, and IT (first line) own and treat risks. The GRC team, the Director of Payments and PCI Compliance, and the Chief Risk Officer (second line) run this method and roll risks up into the enterprise risk register. Internal Audit (third line) tests controls independently (P07); the external QSA validates PCI DSS.

**Risk appetite (board-approved, 2026-02).** Qualitative statements set by the board:
- **Payment card data:** very low appetite for compromise of card data held or processed by the company or by systems it manages for franchisees.
- **Regulatory, contractual, and disclosure:** very low appetite for failed PCI DSS validation, unlawful pricing displays, or late or inaccurate SEC disclosure.
- **Guest safety and hotel operations:** low appetite for disruption of check-in, payments, or room access.
- **Guest and loyalty data:** low appetite for unauthorized disclosure.
- **Growth and innovation (acquisitions, franchise services, AI pricing):** moderate appetite, provided risks are identified and funded at the time of the decision.

**Risk tolerance (measurable, per enterprise risk).** The highest residual risk level each enterprise risk may carry without a board-reported treatment plan. A risk above its threshold is **Outside tolerance** in the register.

| Enterprise risk | Tolerance threshold |
|---|---|
| ER-01 Hotel operations and guest safety disruption from cyber and technology events | Moderate |
| ER-02 Compromise of payment card data | Moderate |
| ER-03 Compromise of guest and loyalty personal data | Moderate |
| ER-04 Third-party, franchisee, and concentration risk | Moderate |
| ER-05 Integration of acquired resorts | Moderate |
| ER-06 Regulatory, contractual, and disclosure compliance | Low |
| ER-07 Financial reporting integrity and fraud | Low |
| ER-08 Responsible use of AI and pricing practices | Moderate |

**Who can accept risk:**
| Residual level | Acceptance authority |
|---|---|
| Very Low, Low | Risk owner (vice president or director) with GRC concurrence |
| Moderate | CISO with the accountable executive |
| High | Executive risk committee (Chief Risk Officer, CIO, COO, CISO, General Counsel), reported to the board risk committee |
| Very High | CEO and CFO jointly, reported to the board risk committee at its next meeting |

Card data risks (ER-02) at High or above, and guest safety risks at High or above, cannot be accepted without a dated treatment plan. Any acceptance expires after 12 months.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the hospitality threat picture (POS memory scraping, e-skimming, credential stuffing against loyalty programs, ransomware, vendor remote access), the *FTC v. Wyndham* allegations, the BIA (P05), the gap analysis (P03), and the Internal Audit assessment (P07).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial), and likelihood of adverse impact, combined with **Table G-5**.
3. **Rate impact.** **Table H-3**, calibrated to the BIA impact values (P05 section 3).
4. **Determine risk.** **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the tables, not assigned by hand.
5. **Integrate with ERM (NIST IR 8286 Rev. 1).**
   - Each system-level cybersecurity risk is a row in this register, with an owner, a treatment, and a key risk indicator (KRI).
   - Each row is normalized into one of **8 enterprise risks (ER-01 to ER-08)** in the Chief Risk Officer's enterprise risk register, with an ERM category.
   - **Aggregation rule:** an enterprise risk's exposure equals its highest constituent risk level, and the profile also reports how many constituent risks sit outside tolerance. One severe risk is never averaged away.
   - The enterprise risk profile (section 4) is what the board risk committee sees each quarter.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 14 |
| Moderate | 38 |
| Low | 11 |
| **Total** | **64** |

By threat source type: Adversarial 36, Structural 19, Accidental 6, Environmental 3.
By treatment: Mitigate 53, Accept 8, Avoid 2, Share/Transfer 1.
By status: In progress 54, Open 2, Closed (accepted) 8.
**22 risks are outside tolerance** and each has a dated treatment plan.

## 4. Enterprise risk profile (roll-up for the board)
| ID | Enterprise risk | ERM category | Risks | Very High | High | Moderate | Low | Exposure (highest) | Tolerance | Outside tolerance |
|---|---|---|---|---|---|---|---|---|---|---|
| ER-01 | Hotel operations and guest safety disruption from cyber and technology events | Operational | 9 | 0 | 2 | 4 | 3 | **High** | Moderate | 2 |
| ER-02 | Compromise of payment card data | Compliance and financial | 18 | 1 | 3 | 11 | 3 | **Very High** | Moderate | 4 |
| ER-03 | Compromise of guest and loyalty personal data | Compliance and reputational | 9 | 0 | 2 | 6 | 1 | **High** | Moderate | 2 |
| ER-04 | Third-party, franchisee, and concentration risk | Operational | 9 | 0 | 4 | 3 | 2 | **High** | Moderate | 4 |
| ER-05 | Integration of acquired resorts | Strategic | 3 | 0 | 1 | 2 | 0 | **High** | Moderate | 1 |
| ER-06 | Regulatory, contractual, and disclosure compliance | Compliance | 7 | 0 | 1 | 5 | 1 | **High** | Low | 6 |
| ER-07 | Financial reporting integrity and fraud | Financial | 3 | 0 | 0 | 2 | 1 | **Moderate** | Low | 2 |
| ER-08 | Responsible use of AI and pricing practices | Strategic and legal | 6 | 0 | 1 | 5 | 0 | **High** | Moderate | 1 |

**Reading the profile:**
- **ER-02 (card data)** carries the only Very High risk, a POS and reservation system compromise through a vendor remote tool (R-001). It is the scenario rehearsed in the P08 runbook. Three conditions drive its likelihood: vendor tools outside PAM (R-003), the legacy POS (R-005), and the hub rule that let franchised segments reach the CRS integration tier (R-007).
- **ER-04 (third parties and franchisees)** has the most High risks. The franchise model means a breach at a franchised hotel, the PMS vendor, or a vendor update can reach many hotels at once (R-006, R-025, R-030).
- **ER-06 (regulatory and disclosure)** is outside tolerance mainly because the SEC materiality process has not been exercised with the current disclosure committee (R-015), and because of fee display errors (R-013) and the missed service provider segmentation test (R-051).
- **ER-08 (AI and pricing)** has one High risk: the revenue-management system pools non-public data from independently owned competing hotels (R-012), the fact pattern in *Cornish-Adebiyi v. Caesars Entertainment, Inc.* (3d Cir. 2026) (see P10).

## 5. Top risks (Very High and High)
| Risk ID | Risk | Level | Enterprise risk | Treatment | Owner | Due |
|---|---|---|---|---|---|---|
| R-001 | Organized criminal group compromises the POS and reservation systems through a vendor remote tool and steals card data at scale | Very High | ER-02 | Vendors into PAM (POAM-005); legacy POS replacement (POAM-001); hub rule and six-month segmentation tests (POAM-004); runbook exercise with the disclosure committee (POAM-014) | CISO | 2027-06-30 |
| R-002 | Ransomware encrypts CRS integrations, PMS interfaces, and hotel systems across many hotels | High | ER-01 | EDR on POS replacements; vendor tools removed; resort migration; enterprise ransomware exercise | CISO | 2027-03-31 |
| R-003 | Attacker uses a vendor-managed remote tool outside PAM at 37 hotels | High | ER-04 | All vendor access through PAM; tools blocked at hotel firewalls (POAM-005) | Vice President, Hotel Technology | 2026-12-31 |
| R-004 | The 9 resorts on the seller's systems suffer a long outage or a compromise through the unfederated directory | High | ER-05 | Migration and identity federation (POAM-002; POAM-003) | Vice President, Integration Management Office | 2027-03-31 |
| R-005 | Memory-scraping malware on legacy POS workstations captures card data | High | ER-02 | Cloud POS with validated P2PE (POAM-001); interim allow-listing | POS Operations Manager | 2027-06-30 |
| R-006 | A compromise at a franchised hotel is used to reach CRS and PMS data for many hotels | High | ER-04 | Technical minimums and AOC enforcement (POAM-012); inactive franchisee accounts (POAM-008) | Director of Franchise Technology Compliance | 2027-03-31 |
| R-007 | Attacker moves from a franchised hotel network through the hub to the CRS integration tier | High | ER-02 | Verify rule removal; six-month segmentation tests (POAM-004) | Director of Network Engineering | 2026-10-31 |
| R-009 | A door lock server is compromised or fails | High | ER-01 | Replace 31 unsupported lock servers; isolate them (POAM-009) | Vice President, Hotel Technology | 2027-03-31 |
| R-010 | Credential stuffing takes over loyalty accounts | High | ER-03 | MFA or passkeys for redemptions and profile changes (POAM-017) | Vice President, Digital and Loyalty | 2027-01-31 |
| R-012 | Revenue-management system pools non-public data from competing hotels | High | ER-08 | Opt out of pooling; separate franchisee data; counsel review (POAM-020) | Chief Commercial Officer | 2026-12-31 |
| R-015 | A material incident is disclosed late or inaccurately | High | ER-06 | Playbook update; tabletop 2026-11-12 (POAM-014) | General Counsel | 2026-11-30 |
| R-016 | Guest profile hub data (61 million profiles) is exfiltrated | High | ER-03 | Retention schedule and purge (POAM-018); export anomaly detection | Chief Privacy Officer | 2027-03-31 |
| R-025 | The brand PMS vendor suffers a breach or extended outage affecting 741 hotels | High | ER-04 | Quarterly vendor reviews; 24-hour notice term; joint exercise | Director of Third-Party Risk Management | 2027-03-31 |
| R-030 | Malicious code arrives in a trusted POS or PMS vendor update | High | ER-04 | Staged rollouts; software bill of materials requests | CISO | 2027-06-30 |
| R-038 | Vendor default credentials on legacy POS back-office servers are used to take control of POS | High | ER-02 | Credential sweep at all 41 legacy hotels (POAM-010) | POS Operations Manager | 2026-09-30 |

## 6. Themes from the 2026 analysis
1. **Legacy property systems (ER-02, ER-01).** The legacy POS at 41 hotels, 31 unsupported lock servers, and vendor remote tools at 37 hotels are where card data and guest safety are most exposed (R-003, R-005, R-009, R-038, R-048, R-049, R-059). Internal Audit's new finding, vendor default credentials on legacy POS servers at 3 hotels (R-038), came from this group.
2. **Franchisor duties (ER-04).** *FTC v. Wyndham* is the reference point: the FTC alleged that a franchisor failed to secure the hotel systems it managed. The company manages the PMS tenant and the network for 410 franchised hotels and holds card data for all 640. The hub rule (R-007), franchisee credentials (R-006), and missing franchisee AOCs (R-018) are the franchise-specific risks.
3. **Resort integration (ER-05).** 9 of 14 acquired resorts remain on seller systems with weaker recovery, identity, and logging (R-004, R-052, R-062). The deal did not budget integration, which led to the new due diligence rule (R-061).
4. **Guest data volume (ER-03).** 61 million guest profiles kept indefinitely, 14.2 million loyalty accounts with optional MFA, and copies in the warehouse (R-010, R-016, R-046, R-053).
5. **Pricing and AI (ER-08).** Pooled benchmarking (R-012), emergency pricing (R-057), fee display errors (R-013, in ER-06), and AI use cases without review (R-014, R-043) are tracked with the AI governance committee (P10).
6. **Disclosure and independence (ER-06).** The materiality playbook has not been exercised since 3 members changed (R-015), and independence safeguards for assessors are not written down (R-055).

## 7. Treatment summary
- **Funded (2026 Q4 to 2027 Q2), about $14.8 million:** legacy POS replacement with cloud POS and P2PE ($8.9M), resort migration and identity federation ($2.6M), lock server replacement ($1.4M), PAM onboarding for the 5 vendors and hotel firewall rules ($420K), loyalty MFA and risk-based sign-in ($780K), SIEM collectors for legacy and resort sources ($260K), user behavior analytics ($310K), and outside counsel for the disclosure tabletop and the pricing review ($110K). Items map to the POA&M in P07.
- **Accepted (8):** R-021, R-022, R-029, R-034, R-035, R-047, R-050, R-063. Each is Low or Moderate residual with strong existing controls, accepted at the right level (section 1) and reviewed within 12 months.
- **Avoided (2):** R-041, R-043. Unapproved generative AI domains are blocked, and AI resume ranking is disabled until review.
- **Shared (1):** R-026, gateway breach, through contract indemnity and cyber insurance.
- **Very High risk R-001:** not accepted as is. The CEO and CFO approved the treatment plan and the residual target of Moderate on 2026-09-08; the board risk committee reviewed it on 2026-09-10.

## 8. Board reporting
**Risk committee of the board (quarterly):** the enterprise risk profile (section 4), every Very High and High risk with its treatment status and KRI trend, risks outside tolerance, new risks since the last meeting, risk acceptances made, and the PCI DSS validation status for both ROCs. The 2026-09-10 meeting received this report, the Internal Audit results (P07), and the regulatory roadmap (P03).
**Audit committee (quarterly):** Internal Audit results, SOX IT general control status (R-032), the disclosure controls topics (R-015), and assessor independence (R-055). The audit committee also reviews the annual Item 106 disclosure draft, which describes this process.
**Management:** the executive risk committee meets monthly and reviews KRIs for all risks outside tolerance.

## 9. Approval
- Executive risk committee: approved the register, treatments, and acceptances, 2026-09-08.
- CEO and CFO: approved the treatment plan and residual target for Very High risk R-001, 2026-09-08.
- Risk committee of the board: reviewed the enterprise risk profile, 2026-09-10.
- Next full review: June to July 2027, or sooner after a major change, incident, or acquisition. KRIs are refreshed quarterly.
