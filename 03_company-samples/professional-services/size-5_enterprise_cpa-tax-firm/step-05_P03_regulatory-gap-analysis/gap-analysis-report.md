# Regulatory Gap Analysis: Cris Santos Company | Professional, Scientific, and Technical Services | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLP (national CPA and tax firm; 64 offices in 14 states; privately owned by its partners) |
| Tier / Vertical | Enterprise / Professional, Scientific, and Technical Services |
| Primary regulation | FTC Standards for Safeguarding Customer Information (Safeguards Rule), 16 CFR Part 314 (N54-R01), all 42 rows. Text read from eCFR, current through 2026-09-23 |
| Also analyzed | IRC 7216 and 26 CFR 301.7216-1 to -3 (N54-R02); IRS e-file and PTIN program requirements (N54-R03); HIPAA Security Rule and breach duties as a business associate (N54-R06); FAR 52.204-21 (N54-R04); state breach and data security laws (Florida worked example) |
| Assessment dates | 2026-06-01 to 2026-07-31 (evidence sampling completed 2026-08-14) |
| Assessors | GRC team (second line) with the Office of General Counsel; sampling reperformed by Internal Audit for 8 rows |
| Approved | CISO (Qualified Individual) and General Counsel, 2026-08-21; roadmap reviewed by the Audit and Risk Committee, 2026-09-15 |

## 1. Applicability
| Regulation | Applies? | Basis |
|---|---|---|
| FTC Safeguards Rule (N54-R01) | **Yes, in full** | 16 CFR 314.2(h)(2)(viii): "An accountant or other tax preparation service that is in the business of completing income tax returns is a financial institution." Individual tax clients have a customer relationship (314.2(e)(2)(i)(H)). The 314.6 exception covers institutions with customer information on fewer than 5,000 consumers; the firm holds about 2.9 million, so no element is exempt |
| IRC 7216 and 26 CFR 301.7216 (N54-R02) | **Yes** | The firm and every employee who helps prepare returns are tax return preparers (301.7216-1(b)(2)). Tax return information includes everything furnished for, or derived from, return preparation (301.7216-1(b)(3)). The regulations and the Safeguards Rule apply side by side (301.7216-1(c)) |
| IRS e-file and PTIN requirements (N54-R03) | **Yes** | Authorized IRS e-file Provider (ERO) with 30 EFINs: Pub. 1345 (Rev. 12-2025) incident reporting, signature, and retention duties; Form W-12 line 11 acknowledgment for about 5,200 PTIN holders. Pub. 4557 (Rev. 6-2024) and Pub. 5708 (Rev. 8-2024) are guidance; the legal WISP duty comes from 16 CFR 314 |
| HIPAA as business associate (N54-R06) | **Yes, for PHI held for about 240 health care clients** | The firm creates, receives, or maintains PHI for covered entities in audit and consulting engagements, so it is a business associate (45 CFR 160.103) subject to the Security Rule directly (164.302), the breach notice to covered entities (164.410), and the use limits in its agreements (164.502(a)(3)). 16 key rows are analyzed; the full Security Rule crosswalk is covered by the enterprise controls in P02 and P07 |
| FAR 52.204-21 (N54-R04) | **Yes, for the government services practice** | About 30 federal civilian contracts include the clause; all 15 basic safeguarding requirements and the subcontract flow-down are analyzed |
| DFARS 252.204-7012 and CMMC (N54-R05) | **No** | No DoD contracts or CUI; engagement acceptance declines such work |
| State breach and data security laws | **Yes** | The law of each state where affected individuals reside; Florida (Fla. Stat. 501.171) is the worked example |
| Florida Digital Bill of Rights (Fla. Stat. 501.702 and following) | **No** | A "controller" must exceed $1 billion in global gross annual revenue **and** meet one of three tests: 50% or more of revenue from selling online advertisements, operating a consumer smart speaker and voice command service, or operating an app store offering at least 250,000 applications. The firm passes the revenue test but meets none of the three, so it is not a controller |
| SEC Form 8-K Item 1.05 and Reg S-K Item 106 | **No, for the firm itself** | The firm is a private partnership, not an SEC registrant. Its SEC-registrant clients must assess incidents on third-party systems they use (SEC Release 33-11216), which drives the client-notice step in P08 and the contract terms tracked under POAM-023 |
| ABA Model Rules (N54-R07) | **No** | The firm does not practice law |
| AICPA Code, confidential client information (N54-R08) | **Noted, not assessed** | Professional standard adopted through state licensing; its text was not verified from the source for this analysis |
| CIRCIA (N54-R09) | **Not in force** | Proposed rule only (89 FR 23644); no final rule as of 2026-09-25. Reporting to CISA is voluntary |
| PCAOB and professional quality standards | Separate program | Audit quality and independence are governed by the firm's quality management system and are outside this security analysis |

**Considered and excluded within the analyzed rules:** 314.4(a)(1)-(3) (the Qualified Individual is a firm employee) and 314.6 (consumer count far above 5,000) are rated Not applicable.

**FAR overhaul numbering.** The requirements analyzed here as FAR 52.204-21 appear as FAR 52.240-93 in awards made under an agency's FAR Part 40 class deviation. The 15 requirements are the same, so these results apply to both. See `00_company-facts.md`.

## 2. Method
1. **Decompose.** Each paragraph of 16 CFR 314.3 and 314.4 became one row, split to the lowest level that states its own duty; 314.4(h)(1)-(7) got one row each. For IRC 7216, each permission or condition that governs how the firm shares data became a row. HIPAA rows use the requirement text and types from the Health Care crosswalk (NIST SP 800-66 Rev. 2 wording) plus the eCFR text of 164.308(b), 164.410, and 164.502(a)(3) (retrieved for 2026-09-23). FAR rows follow the clause text of 52.204-21(b)(1)(i)-(xv) and (c). Florida rows follow the statute text.
2. **Crosswalk.** Each row maps to CSF 2.0 and SP 800-53 Rev. 5. These are **author mappings**: no official NIST mapping of 16 CFR 314, 26 CFR 301.7216, IRS publications, FAR 52.204-21, or Fla. Stat. 501.171 was found. HIPAA rows use the repository's Health Care crosswalk (also an author mapping).
3. **Evidence sampling.** Where a requirement operates on a population, the team tested a sample and recorded the population, sample size, and exceptions in the CSV. Key manual controls with populations over 250 used 60 items (95% confidence, 5% tolerable deviation, zero expected deviations); lower-risk controls and smaller populations used 25 to 40 items; configuration and account data were checked in full with analytics. Selections were random. **21 rows were tested by sampling or full-population analytics; 17 found exceptions.**
4. **Rate.** Met, Partially met, Not met, or Not applicable. Each gap is rated with the P01 scale and carries an owner and date. High gaps are in the P01 register and the P07 POA&M.

## 3. Results summary
| Regulation / section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| 314.3 Program and objectives | 1 | 1 | 0 | 0 | 2 |
| 314.4(a) Qualified Individual | 1 | 0 | 0 | 1 | 2 |
| 314.4(b) Risk assessment | 4 | 1 | 0 | 0 | 5 |
| 314.4(c) Safeguards | 1 | 8 | 1 | 0 | 10 |
| 314.4(d) Testing and monitoring | 3 | 1 | 0 | 0 | 4 |
| 314.4(e) Personnel and training | 3 | 1 | 0 | 0 | 4 |
| 314.4(f) Service providers | 1 | 2 | 0 | 0 | 3 |
| 314.4(g) Evaluate and adjust | 1 | 0 | 0 | 0 | 1 |
| 314.4(h) Incident response plan | 5 | 3 | 0 | 0 | 8 |
| 314.4(i) Report to governing body | 1 | 0 | 0 | 0 | 1 |
| 314.4(j) FTC notification | 0 | 1 | 0 | 0 | 1 |
| 314.6 Exception | 0 | 0 | 0 | 1 | 1 |
| **Safeguards Rule subtotal** | **21** | **18** | **1** | **2** | **42** |
| IRC 7216 regulations (N54-R02) | 4 | 6 | 0 | 0 | 10 |
| IRS e-file and PTIN program (N54-R03) | 3 | 2 | 0 | 0 | 5 |
| HIPAA as business associate (N54-R06) | 10 | 6 | 0 | 0 | 16 |
| FAR 52.204-21 (N54-R04) | 13 | 3 | 0 | 0 | 16 |
| State breach and data security laws | 1 | 4 | 0 | 0 | 5 |
| **Total** | **52** | **39** | **1** | **2** | **94** |

**Gap risk levels across all regulations (40 unmet or partially met rows):** High 9, Moderate 25, Low 6.

**Reading the results.** The firm has the program elements a large firm should have: a Qualified Individual reporting to the Partnership Board, a written risk assessment, annual penetration testing, and a written incident response plan. The gaps sit where scale makes controls hard to apply evenly: identity for 760,000 client accounts and thousands of seasonal staff, need-to-know across 516,000 engagement repositories, consent at offshore volumes, and two acquired firms not yet integrated. The single Not met row is disposal (314.4(c)(6)(i)): no electronic disposal has ever been run.

## 4. Priority gaps (High)
| Row | Citation | Gap | Action | Owner | Target |
|---|---|---|---|---|---|
| G-002 | 314.3(b) | Identity-driven risks not yet within tolerance | Execute funded treatments before the 2027 season | CISO | 2027-01-15 |
| G-010 | 314.4(c)(1)(i) | Late seasonal terminations; about 41,000 dormant client accounts; AF users outside identity governance | POAM-006; POAM-002; POAM-005 | Director of Identity and Access Management | 2027-01-15 |
| G-011 | 314.4(c)(1)(ii) | 31% of DMS tax repositories open to whole office teams | Engagement-based permissions (POAM-003) | National Tax Leader | 2027-03-31 |
| G-015 | 314.4(c)(5) | Client MFA optional; legacy authentication exceptions not approved in writing by the Qualified Individual; push MFA bypassable | POAM-001; POAM-002 | Director of Identity and Access Management | 2027-01-15 |
| G-019 | 314.4(c)(8) | No token replay detection; review evidence gaps; AF-05 tenant unmonitored | POAM-004; POAM-005 | Director of Security Operations | 2026-12-31 |
| G-032 | 314.4(h) | Business email compromise runbook never exercised | Tabletop 2026-11-19 (POAM-010) | General Counsel | 2026-12-15 |
| G-048 | 301.7216-3(a)(1) | 3 of 60 offshore packages released before consent | Automated consent gate (POAM-008) | National Tax Leader | 2026-12-31 |
| G-050 | 301.7216-3(b)(1) | Same exceptions: consent after disclosure | POAM-008 | National Tax Leader | 2026-12-31 |
| G-051 | 301.7216-3(b)(4) | 4 of 60 offshore packages held unmasked partner SSNs on Schedules K-1 | Masking and SSN pattern block (POAM-008) | National Tax Leader | 2026-12-31 |

## 5. Compliance roadmap
| Quarter | Milestones | Regulations served | Evidence produced |
|---|---|---|---|
| 2026 Q4 | Incident Disclosure Committee tabletop and runbook update (POAM-010); state law matrix and client notice register (POAM-023); offshore consent gate and K-1 masking (POAM-008); AF-05 migration and IRC 7216 notice to AF providers (POAM-005; POAM-024); token replay detections (POAM-004); dormant client accounts disabled (POAM-002); change test evidence enforced (POAM-009); HIPAA subcontractor agreements (POAM-021) | 314.4(c)(1), (c)(7), (c)(8), (h), (j); 301.7216-2(d)(2), -3(a)(1), -3(b)(4); Pub. 1345; Fla. Stat. 501.171(3)-(5); 164.308(b)(2) | Tabletop report; matrix; consent gate logs; masking reports; notice acknowledgments; detection test results |
| 2027 Q1 | Phishing-resistant MFA for all tax staff and mandatory client MFA before peak (POAM-001; POAM-002); seasonal training before access (POAM-006); DR retest (POAM-011); vendor reviews (POAM-015); AI 7216 memos (POAM-020); DMS permissions (POAM-003); AF-06 migration (POAM-005); HIPAA business associate risk analysis (POAM-021); FAR flow-down (POAM-022) | 314.4(c)(1), (c)(5), (e)(1), (f)(3), (h); 301.7216-2(d)(1); 164.308(a)(1)(ii)(A); 52.204-21(c) | Authenticator reports; training records; DR report; vendor reviews; memos; risk analysis |
| 2027 Q2 and Q3 | First electronic disposal run after the season (POAM-007); transmitter contract and second path (POAM-019); legacy agreement re-papering (POAM-021); annual reassessment | 314.4(c)(6); Fla. Stat. 501.171(8); 164.502(a)(3) | Disposal log; contract amendment; updated P01 and P03 |

## 6. Pending regulatory changes
- **FTC Safeguards Rule.** No pending proposal to amend 16 CFR Part 314 was found in the Federal Register as of 2026-09-25. The last change was the notification amendment (88 FR 77508), effective 2024-05-13.
- **IRC 7216 regulations.** No pending Treasury proposal was found. The IRS has issued no AI-specific guidance under section 7216, so the AI rows apply the regulation text and are confirmed by counsel (P10).
- **HIPAA Security Rule NPRM** (90 FR 898, 2025-01-06) is **still proposed** and is not treated as an obligation for the business associate rows.
- **FAR.** The FAR CUI rule and the FAR cyber incident reporting rule remain proposed, and a FAR Overhaul proposed rule was published 2026-06-23. None changes the 52.204-21 rows today.
- **CIRCIA:** no final rule as of 2026-09-25.

## 7. Regulator-ready package
The GRC team keeps an evidence binder in the GRC platform, indexed by `req_id`, so the firm can respond quickly to an FTC inquiry, an IRS e-file program review, a health care client's business associate audit, a federal contracting officer's request, or a state attorney general inquiry:
- this report, `gap-analysis.csv`, and the sample selections with exceptions for every sampled row;
- the P01 risk assessment (the 314.4(b)(1) written assessment), P02 SSP, P05 BIA, P06 policy set (the WISP parts), P07 assessment and POA&M, and P08 runbook (the 314.4(h) plan);
- the Qualified Individual's annual reports to the Partnership Board (314.4(i));
- penetration test and vulnerability assessment reports (314.4(d)(2));
- IRC 7216 consent templates, consent samples, and contractor notice acknowledgments;
- business associate agreements and the business associate risk analysis;
- retention of 7 years for program documents (exceeds the 6 years in 164.316(b)(2)(i)).

## 8. Approval
Approved by the CISO (Qualified Individual) and the General Counsel on 2026-08-21. The roadmap was reviewed by the Audit and Risk Committee on 2026-09-15. Next reassessment: 2027-06 to 2027-07.
