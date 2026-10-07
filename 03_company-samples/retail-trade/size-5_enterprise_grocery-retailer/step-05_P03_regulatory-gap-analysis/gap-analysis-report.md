# Regulatory Gap Analysis: Cris Santos Company | Retail Trade | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded regional supermarket chain; 112 stores in FL, GA, AL, SC, TN; online ordering) |
| Tier / Vertical | Enterprise / Retail Trade |
| Primary standard | PCI DSS v4.0.1 (PCI Security Standards Council, June 2024), at Report on Compliance depth. A contractual standard enforced through the merchant agreement, **not law** (N44-45-R01) |
| Other requirements analyzed | FTC Act Section 5 (N44-45-R02); FACTA receipt truncation (N44-45-R05); Visa Core Rules (contractual); SNAP EBT retailer and third party processor rules (7 CFR 274.3, 274.8, 278.1); SEC Form 8-K Item 1.05 and Regulation S-K Item 106; Tennessee Information Protection Act; state breach, data security, and price gouging laws (Florida worked example) |
| Assessment dates | 2026-06-01 to 2026-07-31 (evidence sampling completed 2026-08-14) |
| Assessors | GRC team (second line) with the PCI Program Manager and the Chief Compliance Officer; sampling reperformed by Internal Audit for 10 rows |
| Approved | Chief Compliance Officer and CISO, 2026-08-21; roadmap reviewed by the risk and technology committee of the board, 2026-09-10 |

## 1. Applicability
| Requirement | Applies? | Basis |
|---|---|---|
| PCI DSS v4.0.1 (N44-45-R01) | **Yes, by contract** | The merchant agreement requires compliance. The acquirer designated the company a Level 1 merchant and requires an annual ROC by a QSA (letter dated 2026-02-10, fictional). PCI SSC sets no size tiers; merchant levels come from the card brands. Visa's rules state that each merchant's level criteria are set out in its Account Information Security Program Guide; this analysis does not restate the thresholds |
| FTC Act Section 5 (N44-45-R02) | **Yes** | No size threshold. Deception (45(a)(1)) covers privacy, security, and pricing statements; unfairness (45(n)) requires substantial injury that consumers cannot reasonably avoid and that is not outweighed by benefits |
| FACTA (N44-45-R05) | **Yes** | Any person that accepts cards and prints receipts electronically |
| Visa Core Rules (contractual) | **Yes, through the acquirer** | Verified on the Visa Core Rules and Visa Product and Service Rules, April 2026 edition (sections 1.9.4.1, 1.9.4.2, 10.3.1.1, 10.3.1.2). These rules bind Visa members (the acquirer), which pass them to merchants by contract. Other brands' rules were not reviewed |
| SNAP EBT (7 CFR Parts 274 and 278) | **Yes** | Every store is FNS-authorized (278.1). The payment switch drives core-store terminals, which makes the company a **third party processor** under 274.3(d) in each state's EBT system. Several 274.3 and 274.8 duties are written as State agency duties; they reach the company through retailer agreements and third party processor certification |
| SEC Item 1.05 and Item 106 | **Yes** | Publicly traded SEC registrant, not a smaller reporting company |
| Tennessee Information Protection Act | **Yes** | 2023 Tenn. Pub. Acts ch. 408 (HB1181 as amended by House Amendment HA0348), effective 2025-07-01. Applies to businesses with revenue over $25,000,000 that control or process personal information of at least 175,000 Tennessee consumers in a calendar year (or 25,000 with more than 50% of revenue from sales of personal information). The company has about 240,000 Tennessee loyalty members. Section numbers follow the enacted bill text; Legal confirms against the codified text |
| State breach and data security laws | **Yes** | The law of each state where affected individuals reside; Florida (Fla. Stat. 501.171) is the worked example. Price gouging during declared emergencies: Fla. Stat. 501.160 as the worked example |
| FTC Safeguards Rule (N44-45-R03) and Red Flags Rule (N44-45-R04) | **No** | The co-brand credit card is issued, underwritten, and serviced by a partner bank. The company extends no credit, cashes no checks, and offers no money transmission, so it is not a financial institution under 16 CFR Part 314 and holds no covered accounts. Legal rechecks yearly and before any new financial product |
| CCPA and CPPA regulations (N44-45-R06) | **No** | No stores, delivery, or targeted marketing in California. Recheck if online sales reach California |
| Florida Digital Bill of Rights | **No** | Revenue exceeds $1 billion, but the company meets none of the other controller criteria in Fla. Stat. 501.702 (online advertising revenue, smart speaker service, or app store) |
| COPPA (N44-45-R07) | **No** | Sites and apps are not directed to children; accounts require age 18 (risk R-044 covers accidental collection) |
| INFORM Consumers Act (N44-45-R08) | **No** | No third-party marketplace sellers |
| HIPAA | **No** | No pharmacy (Phase 3 decision, confirmed by the board) |
| SOX Section 404 | Separate program | IT general controls over the ERP are tested by the SOX program and not repeated here |
| CIRCIA | **Not in force** | Final rule not published as of 2026-09-25; reporting is voluntary |

**PCI DSS scope at enterprise depth.** The in-store encryption is the processor's end-to-end solution, **not a PCI-listed P2PE solution**, so the acquirer has not approved scope reduction: lanes, store controllers, store payment VLANs, and the payment switch stay in scope at the 98 core stores. Online, the hosted payment fields keep card data off company servers, but the checkout pages that host them are in scope for 6.4.3 and 11.6.1. The **14 AB stores enter the company's ROC for the first time in 2026**, with clear-text card data inside the stores; most partially met PCI rows below are partially met because of them.

**Rows marked Not applicable** (8) are stored-data requirements with nothing to protect (3.5 to 3.7; no full card numbers are stored after authorization) and requirements for service providers or special cases only (12.4, 12.9, Appendices A1 to A3).

## 2. Method
1. **Decompose.** PCI DSS was broken into its 12 principal requirements and their requirement groups. The payment page requirements were taken to the defined-requirement level (6.4.1 to 6.4.3, 11.6.1), and 12.8 was split into 12.8.1 to 12.8.5 because third-party oversight is a priority gap. Labels are short topics written for this analysis, not PCI SSC text, because PCI DSS is copyrighted; read the requirement text in the company's licensed copy. Other requirements were broken into citation-level duties from primary text: eCFR (7 CFR Parts 274 and 278, retrieved 2026-09-23 version), the Visa rules PDF (April 2026 edition), the Tennessee General Assembly bill and amendment text, the Florida Statutes, 17 CFR 229.106, and the SEC Item 1.05 release.
2. **Crosswalk.** Each row maps to CSF 2.0 and SP 800-53 Rev. 5. **These are author mappings.** No official NIST mapping from PCI DSS v4.0.1, card brand rules, or these statutes was used.
3. **Evidence sampling.** Where a requirement operates on a population, the team tested a sample and recorded the population, sample size, and exceptions in the CSV. Key controls with large populations used 60 items (95% confidence, 5% tolerable deviation, zero expected deviations); lower-risk controls used 25 to 40 items; configuration, account, and third-party data were checked in full with analytics. Selections were random and stratified where the AB stores were a separate population. **54 rows were tested by sampling or full-population analytics; 27 found exceptions.** Population and sample sizes match the QSA's testing procedures where possible so the ROC can reuse them.
4. **Rate.** Met, Partially met, Not met, or Not applicable. Each gap is rated with the P01 scale and carries an owner and date. High gaps are in the P01 register and the P07 POA&M.

## 3. Results summary
| Area | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| PCI Req 1 Network security controls | 3 | 2 | 0 | 0 | 5 |
| PCI Req 2 Secure configurations | 2 | 1 | 0 | 0 | 3 |
| PCI Req 3 Stored account data | 4 | 0 | 0 | 3 | 7 |
| PCI Req 4 Transmission | 1 | 1 | 0 | 0 | 2 |
| PCI Req 5 Malware and phishing | 4 | 0 | 0 | 0 | 4 |
| PCI Req 6 Secure systems and software | 4 | 3 | 0 | 0 | 7 |
| PCI Req 7 Restrict access | 2 | 1 | 0 | 0 | 3 |
| PCI Req 8 Identify and authenticate | 5 | 1 | 0 | 0 | 6 |
| PCI Req 9 Physical access and POI devices | 4 | 1 | 0 | 0 | 5 |
| PCI Req 10 Logging and monitoring | 5 | 2 | 0 | 0 | 7 |
| PCI Req 11 Security testing | 1 | 5 | 0 | 0 | 6 |
| PCI Req 12 Policies and programs | 5 | 7 | 0 | 2 | 14 |
| PCI DSS Appendices A1-A3 | 0 | 0 | 0 | 3 | 3 |
| **PCI DSS subtotal** | **40** | **24** | **0** | **8** | **72** |
| FTC Act Section 5 (N44-45-R02) | 2 | 4 | 0 | 0 | 6 |
| FACTA receipt truncation (N44-45-R05) | 1 | 0 | 0 | 0 | 1 |
| Visa Core Rules (contractual) | 1 | 2 | 0 | 0 | 3 |
| SNAP EBT retailer rules | 4 | 2 | 0 | 0 | 6 |
| SEC Form 8-K Item 1.05 | 1 | 2 | 0 | 0 | 3 |
| SEC Regulation S-K Item 106 | 5 | 0 | 0 | 0 | 5 |
| Tennessee Information Protection Act | 2 | 6 | 1 | 0 | 9 |
| State breach and data security laws | 2 | 2 | 0 | 0 | 4 |
| State price gouging laws | 0 | 1 | 0 | 0 | 1 |
| **Total** | **58** | **43** | **1** | **8** | **110** |

**PCI DSS:** 40 Met, 24 Partially met, 0 Not met, 8 Not applicable (72 rows). No PCI requirement is wholly Not met; the gaps concentrate in the acquired banner, payment page coverage, third-party oversight, and evidence for PIN pad inspections.

**Gap risk levels across all requirements:** High 11, Moderate 25, Low 8.

## 4. Priority gaps (High)
| Row | Citation | Gap | Action | Owner | Target |
|---|---|---|---|---|---|
| G-002 | 1.2 | AB stores have no network security controls separating card data; no AB data flow diagrams | Interim AB card data VLANs and firewall rules; convert AB stores (POAM-001) | Vice President, Integration Management Office | 2027-03-31 |
| G-003 | 1.3 | AB card data not isolated | POAM-001 | Vice President, Integration Management Office | 2027-03-31 |
| G-017 | 4.2 | AB legacy link accepts outdated TLS; clear-text card data inside AB stores | Disable outdated protocols on the AB link now (POAM-017); conversion (POAM-001) | Director of Network Engineering | 2026-12-15 |
| G-027 | 6.4.3 | Script controls do not cover all payment pages | Extend inventory and integrity values to all payment pages; remove the tag manager from them (POAM-002) | Director of E-commerce Engineering | 2026-10-16 |
| G-033 | 8.2 | Shared AB account; late AB terminations; inactive POS IDs | POAM-008; POAM-007; POAM-015 | Director of Identity and Access Management | 2026-12-31 |
| G-046 | 10.4 | Review coverage gaps | POAM-009; POAM-002 | Director of Security Operations | 2026-11-30 |
| G-055 | 11.6.1 | Monitoring coverage gap | Extend monitoring to all payment pages; daily checks during peak (POAM-002) | Director of E-commerce Engineering | 2026-10-16 |
| G-066 | 12.8.4 | Compliance status not confirmed for 9 TPSPs | Collect AOCs or alternative evidence; escalation for non-responders (POAM-003) | Director of Third-Party Risk Management | 2026-11-30 |
| G-069 | 12.10 | Plan not tested for card compromise; business recovery gap | Card compromise tabletop with the disclosure committee (POAM-010); processor outage procedure (POAM-016) | Director of Security Operations | 2026-11-30 |
| G-089 | Form 8-K Item 1.05; SEC Release 33-11216 | Process untested for the most likely material incident type | Tabletop 2026-11-12; playbook update (POAM-010) | General Counsel | 2026-11-30 |
| G-090 | Form 8-K Item 1.05 (materiality determination) | Inputs and timing not defined for card incidents | POAM-010 | General Counsel | 2026-11-30 |

**Before the QSA fieldwork (2026-10-19):** close G-027 and G-055 (all payment pages), complete the missing targeted risk analyses (G-058), and agree with the acquirer and the QSA how the AB stores will be reported while conversion is under way (G-002, G-003, G-017). The company should not represent the AB stores as compliant in the 2026 AOC until conversion is complete; the acquirer decides whether a remediation plan with milestones is acceptable.

## 5. Compliance roadmap
| Quarter | Milestones | Requirements served | Evidence produced |
|---|---|---|---|
| 2026 Q4 | Payment page coverage and express checkout test (POAM-002); targeted risk analyses (POAM-018); TPSP AOCs and matrices (POAM-003); AB link protocols and SIEM collectors (POAM-017, POAM-009); AB shared account removed (POAM-008); disclosure tabletop (POAM-010); Tennessee assessments and app consent (POAM-019); clean room data contract (POAM-020); AB wave 1 (5 stores) | PCI 6.4.3, 11.6.1, 11.4, 12.3, 12.8, 4.2, 10.2, 10.4, 8.2, 12.10; SEC Item 1.05; Tennessee Act 47-18-3204, 3206; Visa 1.9.4.2 | Script inventory; monitoring reports; AOC tracker; tabletop report; assessments |
| 2027 Q1 | AB wave 2 (9 Tennessee stores) and segmentation tests (POAM-001); EBT failover test and voucher drills (POAM-011, POAM-024); processor outage procedure (POAM-016); delivery surge test (POAM-022); pricing fairness tests (POAM-021); privacy notice (POAM-023) | PCI 1.2, 1.3, 9.5, 11.2, 11.5; 7 CFR 274.3(c)(4), (d)(2); FTC 45(a)(1), 45(n) | Conversion records; test reports; fairness results; new notice |
| 2027 Q2 | NAC and OT segmentation at remaining stores (POAM-005); price freeze for all states tested before hurricane season | PCI 1.2, 11.5; Fla. Stat. 501.160 | NAC coverage report; freeze test |
| 2027 Q3 | Annual gap reassessment; next ROC planning | All | Updated P01 and P03 |

## 6. Pending changes and watch items
- **PCI DSS.** v4.0.1 remains current. PCI SSC ran a request for comments (June to July 2026) toward the next version. The analysis will be updated when a new version is published.
- **SEC.** A 2025 petition asks the SEC to rescind Item 1.05. No SEC proposal to amend or rescind was found as of 2026-09-25, so Item 1.05 and Item 106 remain in force.
- **State privacy laws.** More states may pass comprehensive privacy laws that reach the company's footprint; the Privacy Office checks each legislative session for Florida, Georgia, Alabama, South Carolina, and Tennessee.
- **CIRCIA.** No final rule as of 2026-09-25; reporting to CISA is voluntary.
- **FTC.** The FTC's surveillance pricing 6(b) study is a study, not a rule; it signals interest in prices or offers set from personal data (P10).
- None of these is treated as a current obligation.

## 7. Regulator-ready package
The GRC team keeps an evidence binder in the GRC platform, indexed by `req_id`, so the company can respond quickly to the QSA, the acquirer, a card brand, the FTC, a state attorney general (including Tennessee's civil investigative demands under the Act), FNS or a state EBT agency, or an SEC comment letter:
- this report, `gap-analysis.csv`, and the sample selections with exceptions for every sampled row;
- the P01 risk register, P02 SSP, P05 BIA, P06 policy set, P07 assessment and POA&M, and P08 runbook;
- the PCI DSS scope document, data flow diagrams, targeted risk analyses, TPSP list and AOCs, and prior ROCs;
- state EBT certification letters and retailer agreements;
- Tennessee data protection assessments (confidential under the Act when provided to the attorney general);
- document retention of at least 3 years for PCI DSS evidence and 5 years for breach determinations (POL-01).

## 8. Approval
Approved by the Chief Compliance Officer and the CISO on 2026-08-21. The roadmap was reviewed by the risk and technology committee of the board on 2026-09-10. Next reassessment: 2027-06 to 2027-07, and after each AB conversion wave.
