# Enterprise Risk Register Report: Cris Santos Company | Wholesale Trade | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded IT hardware and software distributor; 6 distribution centers; commercial resellers and DoD customers) |
| Size tier | Enterprise (12,000 employees) |
| Vertical | Wholesale Trade |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) for each risk; NIST IR 8286 Rev. 1 for integration into enterprise risk management (ERM); supply chain threats per NIST SP 800-161 Rev. 1 |
| Also satisfies | SP 800-171 Rev. 2 requirement 3.11.1 for the FSCE (periodic risk assessment); input to the Reg S-K Item 106 description of risk management processes; C-SCRM plan (SR-2) |
| Prepared | 2026-06-01 to 2026-07-31 by the GRC team for the CISO; updated 2026-08-28 with Internal Audit findings (P07) and AI risks (P10) |
| Approved | Executive risk committee (chaired by the Chief Risk Officer), 2026-09-08; reviewed by the risk committee of the board, 2026-09-10 |

## 1. Scope and risk framing
**Scope.** All systems and processes in the enterprise BIA (P05): the OCFP (P02), the commercial cloud estates and colocation data centers (P04), the FSCE, distribution-center OT, the AQ-1 legacy environment, and about 3,600 suppliers and 1,100 IT and service vendors. The register covers three kinds of harm:
- harm to the company's own operations and data (ransomware, fraud, data theft);
- harm to customers from the **products** the company distributes (counterfeit, tampered, or covered equipment);
- loss of federal business or disclosure failures (CMMC, DFARS, FAR, SEC).

**Three lines.** Risk owners in the business and IT (first line) own and treat risks. The GRC team and the Chief Risk Officer (second line) run this method and roll risks up into the enterprise risk register. Internal Audit (third line) tests controls independently (P07).

**Risk appetite (board-approved, 2026-02).**
- **Product integrity:** very low appetite for counterfeit, tampered, or covered products reaching customers, and none for federal customers.
- **Regulatory and disclosure:** very low appetite for noncompliance with federal contract clauses, CMMC affirmations, or SEC disclosure rules.
- **Distribution continuity:** low appetite for disruption of order capture and fulfillment beyond one shipping day.
- **Workforce safety:** very low appetite for technology-related safety events in automated distribution centers.
- **Growth and innovation (acquisitions, AI, automation):** moderate appetite, provided risks are identified and funded at the time of the decision.

**Risk tolerance (measurable, per enterprise risk).** The highest residual risk level each enterprise risk may carry without a board-reported treatment plan. A risk above its threshold is **Outside tolerance** in the register.

| Enterprise risk | Tolerance threshold |
|---|---|
| ER-01 Distribution and order-to-cash disruption from cyber and technology events | Moderate |
| ER-02 Product integrity and supply chain (counterfeit, tampered, or covered products) | Low |
| ER-03 Federal contract and disclosure compliance (CMMC, DFARS, FAR, SEC) | Low |
| ER-04 Third-party and concentration risk | Moderate |
| ER-05 Confidentiality of CUI, customer, and personal data | Moderate |
| ER-06 Payment and order fraud, and financial reporting integrity | Low |
| ER-07 Integration of acquisitions | Moderate |
| ER-08 Distribution-center OT and workforce safety | Low |
| ER-09 Responsible use of AI | Moderate |

**Who can accept risk:**
| Residual level | Acceptance authority |
|---|---|
| Very Low, Low | Risk owner (vice president or director) with GRC concurrence |
| Moderate | CISO with the accountable executive |
| High | Executive risk committee (Chief Risk Officer, CIO, COO, CISO, General Counsel), reported to the board risk committee |
| Very High | CEO and CFO jointly, reported to the board risk committee at its next meeting |

Product-integrity risks that could put counterfeit, tampered, or covered equipment into a federal delivery (ER-02, ER-03) cannot be accepted at High or above without a dated treatment plan. Any acceptance expires after 12 months.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the supply chain threat examples in SP 800-161 Rev. 1, the BIA (P05), the gap analysis (P03), the Internal Audit assessment (P07), fraud and incident history (14 fraudulent reseller orders in 2026 H1; the 2026 CUI spill), and interviews with distribution, supply chain, Federal Solutions, finance, and e-commerce leaders.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial), and likelihood of adverse impact, combined with **Table G-5**.
3. **Rate impact.** **Table H-3**, calibrated to the BIA impact values (P05 section 3). Harm to DoD missions from distributed products counts as Very High.
4. **Determine risk.** **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the tables, not assigned by hand.
5. **Integrate with ERM (NIST IR 8286 Rev. 1).**
   - Each cybersecurity and supply chain risk is a row in this register, with an owner, a treatment, and a key risk indicator (KRI).
   - Each row is normalized into one of **9 enterprise risks (ER-01 to ER-09)** in the Chief Risk Officer's enterprise risk register, with an ERM category.
   - **Aggregation rule:** an enterprise risk's exposure equals its highest constituent risk level, and the profile also reports how many constituent risks sit outside tolerance. This keeps one severe risk from being averaged away.
   - The enterprise risk profile (section 4) is what the board risk committee sees each quarter.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 13 |
| Moderate | 33 |
| Low | 18 |
| Very Low | 0 |
| **Total** | **65** |

By threat source type: Adversarial 30, Structural 22, Accidental 11, Environmental 2.
By treatment: Mitigate 55, Accept 8, Avoid 2.
By status: In progress 53, Open 2, Closed (accepted) 8, Closed (avoided) 2.
**26 risks are outside tolerance** and each has a dated treatment plan.

## 4. Enterprise risk profile (roll-up for the board)
| ID | Enterprise risk | ERM category | Risks | Very High | High | Moderate | Low | Exposure (highest) | Tolerance | Outside tolerance |
|---|---|---|---|---|---|---|---|---|---|---|
| ER-01 | Distribution and order-to-cash disruption from cyber and technology events | Operational | 10 | 1 | 0 | 6 | 3 | **Very High** | Moderate | 1 |
| ER-02 | Product integrity and supply chain | Operational and compliance | 7 | 0 | 3 | 4 | 0 | **High** | Low | 7 |
| ER-03 | Federal contract and disclosure compliance | Compliance | 11 | 0 | 4 | 2 | 5 | **High** | Low | 6 |
| ER-04 | Third-party and concentration risk | Operational | 9 | 0 | 1 | 5 | 3 | **High** | Moderate | 1 |
| ER-05 | Confidentiality of CUI, customer, and personal data | Compliance and reputational | 8 | 0 | 1 | 3 | 4 | **High** | Moderate | 1 |
| ER-06 | Payment and order fraud, and financial reporting integrity | Financial | 7 | 0 | 1 | 6 | 0 | **High** | Low | 7 |
| ER-07 | Integration of acquisitions | Strategic | 6 | 0 | 1 | 4 | 1 | **High** | Moderate | 1 |
| ER-08 | Distribution-center OT and workforce safety | Operational | 2 | 0 | 2 | 0 | 0 | **High** | Low | 2 |
| ER-09 | Responsible use of AI | Strategic | 5 | 0 | 0 | 3 | 2 | **Moderate** | Moderate | 0 |

**Reading the profile:**
- **ER-01 (distribution disruption)** carries the only Very High risk, enterprise ransomware (R-001). The AQ-1 pathway (R-007) and the ERP recovery time (R-012) are the main reasons it is not lower.
- **ER-02 (product integrity)** has the lowest tolerance and every constituent risk is outside it. Three are High: open-market counterfeits (R-003), a compromised supplier injecting substitutes (R-004, the P08 scenario), and undetected firmware tampering (R-040).
- **ER-03 (federal and disclosure compliance)** has four High risks: drop-ship Section 889 exposure (R-005), the CUI spill path (R-006), the FSCE closeout deadline (R-009), and a materiality process with no supplier scenario (R-017).
- **ER-06 (fraud)** is outside tolerance on all 7 risks, led by reseller account takeover (R-011).
- **ER-09 (AI)** is within tolerance, but depends on drift monitoring for automated reordering (R-030) and the CCPA ADMT work (R-029) due before 2027-01-01.

## 5. Top risks (Very High and High)
| Risk ID | Risk | Level | Enterprise risk | Treatment | Owner | Due |
|---|---|---|---|---|---|---|
| R-001 | Ransomware encrypts ERP, WMS, edge servers, and distribution-center systems across multiple sites | Very High | ER-01 | Close AQ-1 gaps (POAM-002); ERP RTO fix (POAM-010); OH-1 OT segmentation (POAM-009); annual ransomware exercise with the disclosure committee | CISO | 2027-03-31 |
| R-002 | Exfiltration of customer pricing, quotes, and personal information with extortion | High | ER-05 | Egress anomaly models for cloud storage and APIs; data minimization (R-062) | Director of Security Operations | 2027-03-31 |
| R-003 | Counterfeit or tampered network equipment from the open-market desk ships to commercial customers | High | ER-02 | 100% inspection for network and security products from brokers; serial APIs; firmware hash library (POAM-005) | Chief Supply Chain Officer | 2027-03-31 |
| R-004 | A compromised supplier account injects substitute products or fraudulent ship instructions | High | ER-02 | P08 runbook; substitution re-verification (POAM-006); supply chain tabletop (POAM-014) | Chief Supply Chain Officer | 2027-01-31 |
| R-005 | Covered (Section 889) equipment delivered on a federal order through a drop-ship substitution | High | ER-03 | Structured substitutions screened before acceptance; weekly retro-screen (POAM-006) | Director, Government Contracts | 2026-12-31 |
| R-006 | CUI uploaded again to the reseller platform and synchronized into the ERP | High | ER-03 | Block attachments for federal-flagged accounts; CUI marking detection (POAM-007) | Vice President, E-commerce | 2026-10-15 |
| R-007 | Attacker moves from AQ-1 over the site-to-site VPN into the EDI translator and ERP integration layer | High | ER-07 | Named-flow VPN rules; EDR to 100%; federation; cutover (POAM-002) | Vice President, Integration Management Office | 2027-03-31 |
| R-009 | FSCE Conditional Level 2 (C3PAO) status expires at the 2026-11-10 closeout deadline | High | ER-03 | Close 4 items by 2026-09-30; pre-assessment; closeout 2026-10-20 (POAM-020), kept as a voluntary choice while CMMC Phase 2 is suspended | President, Federal Solutions | 2026-11-10 |
| R-011 | Reseller account takeover leads to fraudulent orders shipped to freight forwarders | High | ER-06 | Ship-to risk scoring and holds; fraud model with analyst review (POAM-012) | Vice President, E-commerce | 2026-12-31 |
| R-014 | Malware on an unsupported HMI stops sortation or causes unsafe conveyor behavior | High | ER-08 | Segment OH-1; refresh or isolate HMIs (POAM-009) | Director, OT Engineering | 2027-06-30 |
| R-015 | An OT vendor's always-on remote tool is compromised | High | ER-08 | Move OT vendor access to PAM (POAM-008) | Director, OT Engineering | 2026-12-31 |
| R-017 | A material incident is disclosed late or inaccurately (no supplier-compromise scenario) | High | ER-03 | Supply chain scenario and decision tree; tabletop 2026-11-18 (POAM-014) | General Counsel | 2026-12-15 |
| R-020 | Malicious code arrives in a trusted software update | High | ER-04 | Staged handheld firmware rollout; SBOM requests for tier-1 vendors | CISO | 2027-06-30 |
| R-040 | Tampered firmware in network equipment is not detected before shipment | High | ER-02 | Firmware hash library and automated checks (POAM-005) | Director, Product Authentication Lab | 2027-03-31 |

## 6. Themes from the 2026 analysis
1. **Product integrity is the distributor's signature risk (ER-02).** Brokers supply only 1.9% of product spend, but that is about $85 million a year of equipment whose history the company cannot fully trace. Commercial receipts are sampled, firmware checks are manual, and returns are restocked after a visual check (R-003, R-039, R-040). A compromised supplier account (R-004) would bypass even authorized-source rules, which is why P08 is built on that scenario.
2. **Federal compliance depends on scope discipline (ER-03).** The FSCE is in good shape, but CUI leaked into commercial systems through customer uploads (R-006), drop-ship substitutions bypass the Section 889 screen (R-005), and shared kiosk accounts undercut the Level 1 affirmation (R-018, R-058). The closeout deadline (R-009) is the nearest hard date.
3. **AQ-1 (ER-07).** The acquired network, directory, backups, and logging are the weakest part of the estate and raise the likelihood of enterprise ransomware (R-001, R-007, R-043, R-050). Treatment completes with the 2027-03-31 cutover. Future deals must fund security diligence and integration (R-061).
4. **Fraud through the reseller channel (ER-06).** Account takeover and static API keys (R-011, R-013) cost $1.3 million in 2026 H1.
5. **Concentration (ER-04).** One VAN carries 72% of EDI (R-010), the TMS contract RTO is 8 hours (R-033), and staffing agencies and 3PLs sit outside third-party tiering (R-031).
6. **OT safety (ER-08).** Unsupported HMIs and always-on vendor tools (R-014, R-015) put both throughput and worker safety at risk; hardware safety interlocks are independent of the HMIs, which keeps impact from being worse.

**New risk from testing.** P07 found 3 shared dock kiosk accounts in the WMS at OH-1, through which DoD ship-to data (FCI) is accessed (R-058, POAM-003). It also raised R-018 for the Level 1 affirmation.

## 7. Treatment summary
- **Funded (2026 Q4 to 2027 Q2), $7.55 million, approved by the executive risk committee on 2026-09-08:** AQ-1 integration security ($1.6M; R-007, R-043, R-044, R-050), OT segmentation at OH-1 and HMI refresh ($2.2M; R-014), reseller API credential modernization and fraud analytics ($1.1M; R-011, R-013), Product Authentication Lab automation ($0.9M; R-003, R-040), drop-ship screening integration ($0.6M; R-005), CUI upload controls and FSCE closeout ($0.45M; R-006, R-009), EDI VAN failover ($0.35M; R-010), AI governance tooling and bias testing ($0.3M; R-029, R-030, R-055), and outside counsel for the supply chain tabletop ($0.05M; R-017). Items map to the POA&M in P07.
- **Accepted (8):** R-034, R-036, R-046, R-047, R-052, R-054, R-056, R-060. Each is Low or Moderate residual with existing controls, accepted at the right level (section 1) and reviewed within 12 months.
- **Avoided (2):** R-032 (unapproved generative AI domains blocked) and R-063 (customer-facing AI pricing chat not enabled).
- **Very High risk R-001:** not accepted as is. The CEO and CFO approved the treatment plan and a residual target of High on 2026-09-08; the board risk committee reviewed it on 2026-09-10.

## 8. Board reporting
**Risk committee of the board (quarterly):** the enterprise risk profile (section 4), every Very High and High risk with its treatment status and KRI trend, risks outside tolerance, new risks since the last meeting, and acceptances made. The 2026-09-10 meeting received this report, the Internal Audit results (P07), and the regulatory roadmap (P03).
**Audit committee (quarterly):** Internal Audit results, SOX IT general control status (R-025, R-048), and disclosure control topics (R-017, R-059). The audit committee also reviews the annual Item 106 disclosure draft, which describes this process.
**Management:** the executive risk committee meets monthly and reviews KRIs for all risks outside tolerance.

## 9. Approval
- Executive risk committee: approved the register, treatments, and acceptances, 2026-09-08.
- CEO and CFO: approved the treatment plan and residual target for Very High risk R-001, 2026-09-08.
- Risk committee of the board: reviewed the enterprise risk profile, 2026-09-10.
- Next full review: June to July 2027, or sooner after a major change, incident, or acquisition (including the AQ-1 cutover). KRIs are refreshed quarterly.
