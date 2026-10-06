# Regulatory Gap Analysis: Cris Santos Company | Financial Services | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded merchant payment processor; three sponsor banks; NYDFS-licensed payouts subsidiary) |
| Tier / Vertical | Enterprise / Financial Services |
| Primary standard | PCI DSS v4.0.1 (PCI SSC, June 2024), assessed as a **service provider** |
| Other rules analyzed | FTC Safeguards Rule (16 CFR Part 314); bank service provider notice (12 CFR 53.4, 304.24, 225.303; C-FINANCIAL-R01); NYDFS Cybersecurity Regulation for the payouts subsidiary (23 NYCRR Part 500; C-FINANCIAL-R05); SEC Form 8-K Item 1.05 and Regulation S-K Item 106; state breach and data security laws (Florida worked example); applicability checks for C-FINANCIAL-R02, R03, R04, and R06 |
| Assessment dates | 2026-06-01 to 2026-07-31 (evidence sampling completed 2026-08-14; P07 findings through 2026-08-21 reflected) |
| Assessors | GRC team (second line) with the Chief Compliance Officer and the PCI program office; Internal Audit reperformed the sampling for 8 rows |
| Approved | Chief Compliance Officer and CISO, 2026-08-21; roadmap reviewed by the board risk and technology committee, 2026-09-10 |

## 1. Applicability
Applicability was decided first, one rule at a time, before any gap was rated. Regulatory text comes from the eCFR (point-in-time versions for 2026-09-23), the NYDFS-published text of the Second Amendment to Part 500, the U.S. Code, the Florida statute, and the SEC's compliance guide; card brand rules come from Visa's public site.

| Rule | Applies? | Basis |
|---|---|---|
| PCI DSS v4.0.1 (primary) | **Yes, as a service provider** | Binds the company by contract through the three sponsor agreements and the card brands' rules, because it stores, processes, and transmits account data for brand members. Level 1 under Visa's service provider levels (more than 300,000 transactions a year; levels are set by the brands, not PCI SSC). No size exemption |
| FTC Safeguards Rule, 16 CFR Part 314 | **Yes** | A non-bank financial institution: data processing of financial data is listed in 12 CFR 225.28(b)(14) and financial in nature under 12 U.S.C. 1843(k) (314.2(h)(1)). It holds other institutions' customers' information (314.1(b)). The 314.6 exception is unavailable. With a board, the Qualified Individual reports to the board (314.4(i)) |
| Bank service provider notice (C-FINANCIAL-R01) | **Yes, under all three rules** | Each sponsor agreement names authorization, clearing, settlement, reconciliation, and funding file services as services subject to the Bank Service Company Act (12 U.S.C. 1867(c)), so they are "covered services" (53.2(b)(5); 304.22(b)(5); 225.301(b)(5)). The company is a bank service provider to Bank A under 12 CFR 53.4, to Bank B under 304.24, and to Bank C (a state member bank, in scope under 225.300(c)) under 225.303. The three sections have the same text |
| NYDFS 23 NYCRR Part 500 (C-FINANCIAL-R05) | **Yes, for Cris Santos Payouts, LLC** | The subsidiary operates under a New York money transmitter license, so it is a covered entity (500.1(e)). It is a **Class A company** (500.1(d)): over $20 million in gross annual revenue in each of the last two fiscal years and over 2,000 employees counting affiliates that share its information systems. The 500.19(a) limited exemption is unavailable. It adopted the parent's program under 500.2(d), so this analysis tests the shared program against Part 500 for the subsidiary. The parent company itself holds no New York license |
| SEC Form 8-K Item 1.05; Reg S-K Item 106 | **Yes** | Publicly traded SEC registrant (large accelerated filer) |
| State breach and data security laws | **Yes** | The law of each state where affected individuals reside. Florida (Fla. Stat. 501.171) is the worked example. For cardholder data the company is usually a third-party agent of its merchants (501.171(6)); for merchant owner and workforce data it is the covered entity |
| Interagency Guidelines (C-FINANCIAL-R02) | **No (reach by contract)** | Apply to Banks A, B, and C. They reach the company through the sponsor agreements' service provider oversight terms, which the banks test in annual due diligence |
| NCUA 12 CFR 748.1(c) (C-FINANCIAL-R03) | **No** | Not a federally insured credit union |
| SEC Regulation SCI (C-FINANCIAL-R04) | **No** | Not an SCI entity |
| CIRCIA (C-FINANCIAL-R06) | **Not in force** | Proposed rule only (89 FR 23644); no final rule as of 2026-09-25. Tracked in section 6 |
| SOX Section 404 | Separate program | IT general controls over the ERP and settlement accounting are tested by the SOX program and not repeated here |
| PCI PIN Security Requirements | Separate assessment | PIN debit acquiring is validated in a separate PCI PIN assessment and is outside this analysis |

**PCI DSS service provider rows.** The service-provider-only requirements are assessed as their own rows: 3.6.1.1, 3.7.9, 8.3.10.1, 11.4.6, 11.5.1.1, 12.4.1, 12.4.2 (with 12.4.2.1), 12.5.2.1, 12.5.3, 12.9.1, and 12.9.2. 3.7.9 applies because the company shares terminal key exchange guidance with 41 enterprise merchants that manage their own keys. Not applicable, with reasons in the CSV: 2.3 (no wireless in the CDE), 3.3.3 (not an issuer), 9.5 (no company-operated POI devices), 11.4.7 and Appendix A1 (not a multi-tenant hosting provider), 12.3.2 (no customized approach), A2 (no SSL or early TLS), A3 (not designated).

## 2. Method
1. **Decompose.**
   - PCI DSS was decomposed below the requirement level where the enterprise has distinct controls or gaps (for example, 3.2.1, 3.3.1, 6.3.3, 6.4.3, 8.2.5, 8.4.2, 8.6.2, 11.6.1, 12.10.7), with every service-provider-only sub-requirement as its own row. PCI DSS is copyrighted, so rows give the requirement number and a short topic label in our own words; read the full text in the PCI SSC document library.
   - The Safeguards Rule was decomposed to the paragraph level of 16 CFR 314.4; Part 500 to its sections and the paragraphs that carry distinct duties (including the Class A duties in 500.2(c), 500.7(c), and 500.14(b)); the bank notice rules to their paragraphs; Item 1.05 to its three duties; Item 106 to its paragraphs; Florida to 501.171(2), (6), and (8).
2. **Crosswalk.** Each row maps to CSF 2.0 subcategories and SP 800-53 Rev. 5 controls. These are **author mappings**: no official NIST mapping from PCI DSS v4.0.1, 16 CFR 314, Part 500, or the SEC rules to CSF 2.0 or SP 800-53 was used.
3. **Evidence sampling.** Where a requirement operates on a population, the team tested a sample and recorded the population, sample size, and exceptions. Key controls with large populations used 60 items (95% confidence, 5% tolerable deviation, zero expected deviations); populations under 250 used 25 to 40 items; configuration and account data were checked in full with analytics. Selections were random or stratified (contractors were oversampled for terminations). **30 rows were tested by sampling or full-population analytics; 12 found exceptions.**
4. **Rate.** Met, Partially met, Not met, or Not applicable. Each gap is rated with the P01 scale and carries an owner and date. High gaps are in the P01 register and the P07 POA&M.

This is a gap analysis, not a PCI DSS assessment. Only the QSA's ROC can conclude on PCI DSS compliance.

## 3. Results summary
| Regulation / section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| PCI DSS Req. 1 Network security controls | 5 | 2 | 0 | 0 | 7 |
| PCI DSS Req. 2 Secure configurations | 2 | 1 | 0 | 1 | 4 |
| PCI DSS Req. 3 Protect stored account data | 8 | 3 | 0 | 1 | 12 |
| PCI DSS Req. 4 Protect data in transmission | 4 | 0 | 0 | 0 | 4 |
| PCI DSS Req. 5 Anti-malware | 5 | 0 | 0 | 0 | 5 |
| PCI DSS Req. 6 Secure systems and software | 5 | 3 | 0 | 0 | 8 |
| PCI DSS Req. 7 Restrict access by need to know | 5 | 1 | 0 | 0 | 6 |
| PCI DSS Req. 8 Identify and authenticate | 11 | 5 | 0 | 0 | 16 |
| PCI DSS Req. 9 Physical access | 4 | 0 | 0 | 1 | 5 |
| PCI DSS Req. 10 Logging and monitoring | 7 | 0 | 0 | 0 | 7 |
| PCI DSS Req. 11 Security testing | 8 | 3 | 0 | 1 | 12 |
| PCI DSS Req. 12 Policies and programs | 18 | 7 | 0 | 1 | 26 |
| PCI DSS Appendices A1 to A3 | 0 | 0 | 0 | 3 | 3 |
| FTC Safeguards Rule 16 CFR 314 | 8 | 9 | 0 | 1 | 18 |
| Bank service provider notice (12 CFR 53.4, 304.24, 225.303) | 3 | 2 | 0 | 0 | 5 |
| Other vertical requirements (C-FINANCIAL-R02, R03, R04, R06) | 0 | 0 | 0 | 4 | 4 |
| SEC Form 8-K Item 1.05 | 1 | 2 | 0 | 0 | 3 |
| SEC Regulation S-K Item 106 | 5 | 0 | 0 | 0 | 5 |
| NYDFS 23 NYCRR Part 500 (payouts subsidiary) | 18 | 14 | 0 | 1 | 33 |
| State breach and data security laws | 2 | 2 | 0 | 0 | 4 |
| **Total** | **119** | **54** | **0** | **14** | **187** |

**Gap risk levels (54 gaps):** High 20, Moderate 30, Low 4. PCI DSS accounts for 25 gaps (13 High, 12 Moderate); Part 500 for 14 (4 High, 9 Moderate, 1 Low).

**What the pattern says:**
- **A mature base with no outright failures.** No requirement is wholly Not met. Encryption, transmission security, anti-malware, logging, physical security, service provider acknowledgments, and governance (12.4.1, 12.4.2) are Met across the estate.
- **The gaps sit at the edges of the program:** the legacy settlement platform (unsupported servers, patch timing, embedded secrets, operator MFA), the DC-1 to Cloud A interconnect change, partner-hosted payment fields, PAN in places outside the CDE, and third parties without current assurance.
- **One weakness, several rules.** Password-only mainframe operator sign-in appears under PCI DSS 8.4.2, 16 CFR 314.4(c)(5), and 23 NYCRR 500.12; the same fix closes all three. The same is true of the disclosure exercise (PCI DSS 12.10.2, Item 1.05, 500.16(d), 500.17(a)).

## 4. Priority gaps (High)
| Row | Citation | Gap | Action | Owner | Target |
|---|---|---|---|---|---|
| G-005 | PCI 1.3 | Unintended path into the Cloud A CDE after the interconnect change | Route fix; guardrail code; retest (POAM-003) | Director of Data Center and Network Engineering | 2026-10-15 |
| G-081 | PCI 11.4.5-11.4.6 | Segmentation not confirmed effective | Retest before ROC fieldwork (POAM-003) | Director of Data Center and Network Engineering | 2026-10-15 |
| G-009 | PCI 2.2 | 12 unsupported midrange settlement servers | Compensating controls documented; replacement (POAM-001) | Director of Settlement Systems | 2027-06-30 |
| G-037 | PCI 6.3.3 | Critical patches exceed one month on DC-1 midrange servers | Weekly windows; automation (POAM-010) | Director of Infrastructure Engineering | 2027-03-31 |
| G-013 | PCI 3.2.1 | PAN outside the CDE not caught by the quarterly process | Wider PAN discovery (POAM-014) | Chief Data and Analytics Officer | 2027-01-31 |
| G-014 | PCI 3.3.1 | Spoken card verification codes in call recordings | Automatic pause-and-resume; redaction (POAM-014) | Senior Vice President, Merchant Services | 2026-12-31 |
| G-018 | PCI 3.5.1 | Unencrypted PAN reached a data lake table | Ingestion blocking (POAM-014) | Chief Data and Analytics Officer | 2026-11-30 |
| G-039 | PCI 6.4.3 | Script controls missing for 36% of ISV integrations | Extend controls; attestations (POAM-021) | Executive Vice President, Integrated Payments | 2027-01-31 |
| G-086 | PCI 11.6.1 | Tamper-detection missing for 36% of ISV integrations | Extend coverage (POAM-021) | Executive Vice President, Integrated Payments | 2027-01-31 |
| G-044 | PCI 7.2.5 | Standing administrator rights for the Cloud B pipeline account | Short-lived workload identity (POAM-020) | Executive Vice President, Integrated Payments | 2026-12-15 |
| G-057 | PCI 8.4.2 | Password-only mainframe operator sign-in | MFA gateway (POAM-004) | Director of Identity and Access Management | 2026-12-31 |
| G-122 | 314.4(c)(5) | Same, without written Qualified Individual approval | POAM-004 | Director of Identity and Access Management | 2026-12-31 |
| G-169 | 500.12 | Same, without written CISO approval | Interim written approval now; MFA gateway (POAM-004) | CISO | 2026-12-31 |
| G-061 | PCI 8.6.2 | Embedded secrets in 31 settlement scripts | Remove; secret scanning (POAM-002) | Director of Settlement Systems | 2026-12-15 |
| G-107 | PCI 12.10.2 | Executive and disclosure exercise more than 12 months old | Tabletop 2026-11-12 (POAM-005) | General Counsel | 2026-11-30 |
| G-143 | Form 8-K Item 1.05 | Process untested with the current committee | Playbook update; tabletop (POAM-005) | General Counsel | 2026-11-30 |
| G-144 | Item 1.05 (materiality determination) | SEC, NYDFS, and bank clocks never run together | POAM-005 | General Counsel | 2026-11-30 |
| G-180 | 500.17(a) | 72-hour NYDFS notice not in the playbook or tooling | POAM-005 | Chief Compliance Officer | 2026-11-30 |
| G-164 | 500.7(c) | PAM covers 62% of Cloud B administrative roles, where the payouts platform runs | POAM-019 | Director of Identity and Access Management | 2027-01-31 |
| G-176 | 500.16(a)(2) | Settlement recovery not proven within the RTO; no joint procedure with the banks | POAM-006; POAM-016 | Senior Vice President, Settlement and Treasury Operations | 2027-03-31 |

## 5. Compliance roadmap
| Quarter | Milestones | Rules served | Evidence produced |
|---|---|---|---|
| 2026 Q4 (before ROC fieldwork on 2026-10-19) | Segmentation fix and retest (POAM-003); Bank C contacts and determination step (POAM-007); scope confirmation with Bank C flows (G-097; POAM-024); interim written CISO approval for operator sign-in (POAM-004) | PCI 1.3, 11.4.6, 12.5.2.1; 225.303; 500.12 | Retest report; contact register; scope document; signed approval |
| 2026 Q4 (rest of quarter) | Service provider AOCs and matrices (POAM-008); disclosure tabletop with NYDFS and bank clocks (POAM-005); embedded secrets removed (POAM-002); Cloud B pipeline identity (POAM-020); contractor disablement automation (POAM-011); emergency change control (POAM-013); call recording pause-and-resume (POAM-014); 2026 CISO report with a Part 500 section (POAM-023) | PCI 12.8.4-12.8.5, 8.6.2, 7.2.5, 8.2.5, 6.5, 3.3.1, 12.10.2; 314.4(c)(1), (f), (h); 500.4(b), 500.7(a), 500.11, 500.16(d), 500.17(a); Item 1.05 | AOC register; tabletop after-action report; scan results; access reports |
| 2027 Q1 | Mainframe operator MFA live (POAM-004, 2026-12-31); partner payment field controls (POAM-021); Cloud B phishing-resistant MFA and PAM (POAM-019); settlement recovery retest with Bank A (POAM-006; POAM-016); patch automation (POAM-010); near real-time mainframe logging (POAM-012); asset record completion (POAM-018); decision on the 2026 NYDFS filing (POAM-023, 2027-03-15) | PCI 8.4.2, 6.4.3, 11.6.1, 6.3.3; 314.4(c)(5), (c)(8); 500.5(c), 500.7(c), 500.12, 500.13(a), 500.16(a)(2), 500.17(b) | DR retest report; coverage reports; NYDFS filing by 2027-04-15 |
| 2027 Q2 | Unsupported server replacement (POAM-001); joint tests with Banks B and C (POAM-016) | PCI 2.2, 6.3.3, 12.3.4; 500.13(a)(1)(iv) | Decommission records; exercise reports |
| 2027 Q3 | Annual gap reassessment; CIRCIA status check | All | Updated P01 and P03 |

**The 2026 NYDFS annual filing.** Part 500.17(b) asks for either a certification that the covered entity materially complied during the prior calendar year or an acknowledgment that names the sections not complied with and gives a remediation timeline. The 500.12 gap (since 2026-02-09) and the 500.13(a) data gaps existed during 2026, so the Chief Compliance Officer and counsel will decide by 2027-03-15 which filing is accurate, based on the gap evidence file. The filing must be signed by the highest-ranking executive and the CISO and submitted by 2027-04-15; supporting records are kept for five years (500.17(b)(3)).

## 6. Pending regulatory changes
- **PCI DSS.** v4.0.1 is the current version in the PCI SSC document library. Every future-dated v4.0 requirement took effect on 2025-03-31 and is assessed here as a current requirement. No newer version is assumed.
- **CIRCIA** (6 U.S.C. 681b; proposed 6 CFR Part 226, 89 FR 23644, 2024-04-04). No final rule had been published as of 2026-09-25, and CISA held further town halls in 2026. If finalized as proposed, covered entities would report covered cyber incidents to CISA within 72 hours and ransom payments within 24 hours. **Not a current obligation.** At this size and sector the company would likely meet the proposed criteria, so the incident tooling already records the data a report would need.
- **SEC.** A search of the Federal Register (2024-01-01 to 2026-10-06) found no proposed or final rule amending Form 8-K Item 1.05 or Regulation S-K Item 106, so both are treated as in force.
- **NYDFS Part 500.** All Second Amendment provisions are in force, including universal MFA (500.12) and the asset inventory (500.13(a)) since 2025-11-01.

The `pending_rule_change` column is "None" for every row except the CIRCIA row.

## 7. Regulator-ready package
The GRC team keeps an evidence binder in the GRC platform, indexed by `req_id`, so the company can respond quickly to a sponsor bank's due diligence or examination request, an NYDFS examination of the payouts subsidiary, a QSA request, an FTC inquiry, or an SEC comment letter:
- this report, `gap-analysis.csv`, and the sample selections with exceptions for every sampled row;
- the P01 risk register, P02 SSP, P04 control map, P05 BIA, P06 policy set, P07 assessment and POA&M, and P08 runbook and notification matrix;
- the 2025 ROC and AOC, the SOC 1 and SOC 2 reports, and the service provider AOC register;
- Part 500 records: the 500.2(d) adoption resolution, CISO designation and oversight letters, the annual CISO report, the 2025 certification with its sub-certifications, and the 2026 gap evidence file (kept five years under 500.17(b)(3));
- the bank designated contact register and records of every 4-hour determination;
- Item 106 working papers.

## 8. Approval
Approved by the Chief Compliance Officer and the CISO on 2026-08-21. The roadmap was reviewed by the board risk and technology committee on 2026-09-10. Next reassessment: 2027-06 to 2027-07.
