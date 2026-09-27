# Regulatory Gap Analysis: Cris Santos Company | Finance and Insurance | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded bank holding company); Cris Santos Bank, N.A. (OCC-supervised national bank); Cris Santos Investment Services, LLC (SEC-registered broker-dealer and investment adviser) |
| Tier / Vertical | Enterprise / Finance and Insurance |
| Primary regulation | Interagency Guidelines Establishing Information Security Standards as issued by the OCC: 12 CFR Part 30, Appendix B, with Supplement A (N52-R02). Text read from eCFR, current through 2026-09-23 |
| Other regulations analyzed | OCC heightened standards (12 CFR Part 30, Appendix D); incident notification (12 CFR Part 53; 12 CFR 225 Subpart N); Federal Reserve risk committee rule (12 CFR 252.22); SEC Form 8-K Item 1.05 and Regulation S-K Item 106 (N52-R08); SEC Regulation S-P, 17 CFR 248.30 (N52-R05); SEC Regulation S-ID, 17 CFR 248.201 (N52-R06); OCC identity theft red flags (12 CFR 41.90); SAR rule (12 CFR 21.11); ECOA and Regulation B, and FCRA adverse action (for credit models); state breach notification laws (Florida worked example) |
| Assessment dates | 2026-05-04 to 2026-07-10 (evidence sampling completed 2026-07-31) |
| Assessors | GRC team with the Chief Compliance Officer and the Director of Technology and Operational Risk (second line); sampling for 8 rows reperformed by Internal Audit |
| Approved | Chief Compliance Officer, Chief Risk Officer, and CISO, 2026-08-21; roadmap reviewed by the board risk committee, 2026-09-15 |

## 1. Applicability
Every rule was checked for whether it binds this company at this size before it was analyzed. Citations were read in the eCFR (versions current through 2026-09-23), the Federal Register, or the issuing agency's website.

| Regulation | Applies? | Basis |
|---|---|---|
| Interagency Guidelines, 12 CFR 30 App. B (N52-R02) | **Yes** | The Guidelines apply to customer information maintained by or on behalf of national banks (App. B I.A). No size exemption: the program must be appropriate to the bank's size and complexity (II.A). The parent's Federal Reserve version (12 CFR 225 App. F) is met through the same enterprise program |
| OCC heightened standards, 12 CFR 30 App. D | **Yes** | They apply to a bank with average total consolidated assets of $50 billion or more (App. D I.A; I.E.5). The bank's four-quarter average is $84.9 billion. Because the bank's assets are 98.3% of the parent's (95% or more), the bank uses the parent's risk governance framework and documents that assessment every year (I.3, I.4). The Guidelines ask for a formal risk governance framework designed by independent risk management (II.A), defined roles for front line units, independent risk management, and internal audit (II.C), a risk appetite statement with qualitative and quantitative limits (II.E), risk data aggregation (II.J), and board standards including at least two independent directors (III.D) |
| 12 CFR Part 53 | **Yes** | Applies to national banks (53.1(c)). Notice to the OCC no later than 36 hours after the bank determines a notification incident has occurred (53.3); bank service providers must notify the bank (53.4) |
| 12 CFR 225 Subpart N | **Yes, for the parent** | Applies to U.S. bank holding companies (225.300(c)); the same 36-hour notice goes to the Federal Reserve (225.302) |
| 12 CFR 252.22 (Regulation YY, subpart C) | **Yes, for the parent** | A bank holding company with average total consolidated assets of $50 billion or more must keep a risk committee and a chief risk officer (252.21(a)); the parent's $86.4 billion is below the $100 billion level where subpart D replaces subpart C |
| SEC Form 8-K Item 1.05 and Reg S-K Item 106 (N52-R08) | **Yes, for the parent** | Exchange Act reporting company; a large accelerated filer, not a smaller reporting company. No exemption by size |
| SEC Regulation S-P, 17 CFR 248.30 (N52-R05) | **Yes, for the broker-dealer** | Brokers, dealers, and registered investment advisers are covered institutions (248.30(d)(3)). The 2024 amendments are in force for the broker-dealer (larger-entity compliance date 2025-12-03) |
| SEC Regulation S-ID, 17 CFR 248.201 (N52-R06) | **Yes, for the broker-dealer** | Registered broker-dealers and investment advisers that maintain covered accounts (248.201(a)) |
| OCC identity theft red flags, 12 CFR 41.90 | **Yes, for the bank** | National banks that offer covered accounts (41.90(a)) |
| SAR rule, 12 CFR 21.11 | **Yes, for the bank** | National banks; cyber-enabled fraud is a common SAR trigger |
| ECOA and Regulation B; FCRA 15 U.S.C. 1681m(a) | **Yes, for credit models** | The bank is a creditor and uses consumer reports in underwriting; AI-001 is analyzed in P10. The CFPB supervises the bank for federal consumer financial law because it has more than $10 billion in assets (12 U.S.C. 5515) |
| State breach notification laws | **Yes** | The law of each state where affected individuals reside; Florida (Fla. Stat. 501.171) is the worked example |
| NYDFS 23 NYCRR Part 500 (N52-R04) | **No** | No group entity holds a license, registration, or charter under the New York Banking, Insurance, or Financial Services Law, and the bank has no New York office. Rechecked at each new license, product, or acquisition |
| FTC Safeguards Rule, 16 CFR Part 314 (N52-R03) | **No** | The bank is OCC-supervised; the broker-dealer and adviser are SEC-regulated |
| NAIC Model #668 (N52-R07) | **No** | No insurance licensee |
| 12 CFR 304.23 (FDIC); 12 CFR 748.1 (NCUA) | **No** | The OCC is the bank's primary federal regulator; not a credit union |
| CIRCIA | **Not in force** | Final rule not published as of 2026-09-25; reporting to CISA is voluntary |
| Regulation B subpart B (small business lending data) | **Not yet required** | Compliance date 2028-01-01 (91 FR 23530); handled by the fair lending program |
| SOX section 404 | Separate program | IT general controls over financial reporting are tested by the SOX program and not repeated here |

**How the bank is examined.** OCC examiners assess the Guidelines using the FFIEC Information Technology Examination Handbook. The FFIEC Cybersecurity Assessment Tool was retired on 2025-08-31, and the FFIEC pointed institutions to NIST CSF 2.0, the CISA Cybersecurity Performance Goals, the Cyber Risk Institute profile, and the CIS Critical Security Controls. That is why every row maps to CSF 2.0 and SP 800-53.

## 2. Method
1. **Decompose.** Each paragraph of App. B sections II and III is one row; III.C.1.a is split into four rows (workforce access, consumer authentication, commercial authentication and payment controls, and fraudulent means) because the bank's exposures differ by channel. Supplement A's response-program and customer-notice paragraphs are included because III.C.1.g requires a response program and Supplement A is the OCC's interpretation of what it contains. App. D rows follow its section structure, grouping paragraphs that share evidence. Other rules were broken into citation-level duties.
2. **Type each row.** App. B "shall" provisions are **Required**; the eight III.C.1 measures are **Consider; adopt if appropriate**, and for a bank of this size and complexity every one is appropriate and assessed as if required. Supplement A rows are **Guidance** ("should"). App. D rows are **Guidelines** ("should"; Part 30 safety and soundness guidelines under 12 U.S.C. 1831p-1). Rule text with "must" is **Rule**.
3. **Crosswalk.** Each row maps to CSF 2.0 and SP 800-53 Rev. 5. These are **author mappings**: no official NIST mapping of these rules was found.
4. **Evidence sampling.** Where a requirement operates on a population, the team tested a sample and recorded the population, sample size, and exceptions in the CSV. Key controls with large populations used 60 items (95% confidence, 5% tolerable deviation, zero expected deviations); lower-risk controls used 25 to 40 items; configuration, contract, and account data were checked in full with analytics. Selections were random. **29 rows were tested by sampling or full-population analytics; 17 found exceptions.**
5. **Rate.** Met, Partially met, Not met, or Not applicable. Each gap is rated with the P01 scale and carries an owner and date. High gaps are in the P01 register and the P07 POA&M.

## 3. Results summary
| Regulation / section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| Interagency Guidelines, App. B (II and III) | 17 | 13 | 0 | 1 | 31 |
| Interagency Guidelines, Supplement A | 8 | 1 | 0 | 0 | 9 |
| OCC heightened standards, App. D | 13 | 6 | 0 | 0 | 19 |
| Incident notification (Part 53; 225 Subpart N) | 2 | 2 | 0 | 0 | 4 |
| Federal Reserve risk committee rule (252.22) | 3 | 1 | 0 | 0 | 4 |
| SEC Form 8-K Item 1.05 | 3 | 1 | 0 | 0 | 4 |
| SEC Regulation S-K Item 106 | 4 | 0 | 0 | 0 | 4 |
| SEC Regulation S-P | 5 | 2 | 0 | 0 | 7 |
| SEC Regulation S-ID | 2 | 0 | 0 | 0 | 2 |
| OCC identity theft red flags (41.90) | 1 | 1 | 0 | 0 | 2 |
| SAR rule (21.11) | 3 | 0 | 0 | 0 | 3 |
| ECOA and Regulation B; FCRA | 3 | 2 | 0 | 0 | 5 |
| State breach notification laws | 3 | 1 | 0 | 0 | 4 |
| Not in scope (applicability checks) | 0 | 0 | 0 | 6 | 6 |
| **Total** | **67** | **30** | **0** | **7** | **104** |

Of the 30 partially met rows: 10 are **Rule** provisions, 8 are **III.C.1 measures**, 6 are **App. D guidelines**, 5 are **Required** App. B provisions, and 1 is **Supplement A guidance**. No requirement is wholly Not met; the gaps concentrate in payment fraud controls, the mainframe's place outside identity governance and PAM, third-party contracts and reviews, the independence of second-line cyber oversight, and AI-001's fair lending work.

**Gap risk levels:** High 7, Moderate 21, Low 2.

## 4. Priority gaps (High)
| Row | Citation | Gap | Action | Owner | Target |
|---|---|---|---|---|---|
| G-012 | App. B III.C.1.a (workforce) | 3 of 60 sampled terminations removed from the mainframe 4 to 9 business days late; 41 mainframe IDs with standing privileges outside PAM; dormant integration service account | Identity governance connector, PAM, service credential review (POAM-001, POAM-002, POAM-013) | Director of Identity and Access Management | 2027-03-31 |
| G-014 | App. B III.C.1.a (commercial) | New beneficiaries paid under $100,000 without out-of-band confirmation or alert (11 of 60 sampled); legacy platform has no confirmation | Confirm every new beneficiary; alert rule; legacy migration (POAM-004, POAM-006, POAM-007) | Head of Treasury Management | 2027-03-31 |
| G-015 | App. B III.C.1.a (fraudulent means) | 4 of 60 branch-originated email or phone wire requests without callback evidence; no role-based BEC training for client service staff | Route to the callback team; required field; training (POAM-007, POAM-015) | Head of Payments Operations | 2026-12-31 |
| G-020 | App. B III.C.1.f | Core maintenance events not collected or reviewed; no beneficiary-plus-wire alert under $100,000 | SIEM onboarding and fraud rules (POAM-003, POAM-006) | Director of Cyber Defense | 2026-12-31 |
| G-022 | App. B III.C.1.h | No logically isolated immutable copy of core data; treasury platform contract RTO exceeds BIA RTO | Cyber vault (POAM-020); vendor terms and fallback test (POAM-018) | Director of Data Center and Mainframe Operations | 2027-06-30 |
| G-045 | App. D II.C.2 | Second-line cyber challenge depends on a team located in the front line | Move the cyber risk oversight team to the CRO (POAM-014) | Chief Risk Officer | 2027-01-31 |
| G-046 | App. D I.E.7(d) | The cyber risk oversight team reports through the CISO to the CIO, a front line unit executive | As G-045; update the Item 106 description (POAM-014) | Chief Risk Officer | 2027-01-31 |

## 5. Compliance roadmap
| Quarter | Milestones | Regulations served | Evidence produced |
|---|---|---|---|
| 2026 Q4 | Disable dormant service account (POAM-013); send 53.4 contacts to 9 critical third parties (POAM-019); mandatory determination field (POAM-011); reason code rewrite and corrected statements (POAM-022); card segment fair lending testing (POAM-022); core maintenance events to the SIEM (POAM-003); beneficiary-plus-wire alert (POAM-006); callback routing and role-based BEC training (POAM-007, POAM-015); SOC review backlog (POAM-012); related-occurrence step in the materiality playbook (POAM-017); 2026 independent assessment of the risk governance framework including technology risk (POAM-024) | App. B III.C.1.a, III.C.1.f, III.C.2, III.D.3; Part 53; Item 1.05; Regulation B; App. D II.C.3.(d) | Account removal record; contact letters; case management configuration; fair lending test report; SIEM source list; training records |
| 2027 Q1 | Cyber risk oversight team moves to the CRO (POAM-014); mainframe identity governance connector (POAM-001) and PAM (POAM-002); SMS migration and step-up (POAM-005); out-of-band confirmation of every new beneficiary (POAM-007); Regulation S-P contract amendments (POAM-021); cyber KRI automation (POAM-016); middleware drift and OS upgrade (POAM-008) | App. D I.E.7(d), II.C.2, II.J; 252.22(a)(2)(ii)(C); App. B III.C.1.a, III.C.1.d; 248.30(a)(5) | Organization chart and charter; PAM onboarding report; authenticator mix report; amended contracts |
| 2027 Q1 (February) | Legacy commercial platform retired after client migration (POAM-004) | App. B III.C.1.a, III.C.1.f | Migration closure report |
| 2027 Q2 | Cyber vault live (POAM-020); treasury platform contract renewal with a 2-hour RTO and full-day fallback test (POAM-018) | App. B III.C.1.h; App. D II.F, II.I | Vault restore test; contract; test report |
| 2027 Q3 | Annual risk assessment and gap reassessment; review the status of the App. D threshold proposal | All | Updated P01 and P03 |

## 6. Pending regulatory changes
- **OCC heightened standards threshold.** On 2025-12-30 the OCC proposed to raise the App. D threshold from $50 billion to $700 billion in average total consolidated assets (90 FR 61084; comments closed 2026-03-02). No final rule was found in the Federal Register as of 2026-09-25, and the eCFR text current through 2026-09-23 still says $50 billion, so App. D applies today. If the proposal is finalized as proposed, the bank would no longer be a covered bank. Management's position, recorded by the board risk committee on 2026-09-15: keep the three-lines framework, the risk appetite statement, and the independence fixes either way, because 12 CFR 252.22 still requires the parent's risk committee and chief risk officer, and the Interagency Guidelines still require board oversight and independent testing.
- **Third-party guidance.** The OCC, Federal Reserve, FDIC, and NCUA proposed replacement third-party risk management guidance on 2026-09-15 (91 FR 58536; comments due 2026-11-16). It is guidance, not a rule; the App. B III.D duties are regulation text and do not change. Rows G-026 to G-028 and G-037 carry a watch note.
- **Regulation B.** A final rule effective 2026-07-21 (91 FR 21620) amended 12 CFR 1002.6(a) to state that the Act does not provide for the "effects test". The disparate treatment and adverse action duties analyzed here are unchanged, and the bank still measures outcome disparities as a warning sign of proxy variables (P10). The small business lending data rule has a compliance date of 2028-01-01 (91 FR 23530).
- **Model risk guidance.** On 2026-04-17 the Federal Reserve, OCC, and FDIC issued revised model risk management guidance (SR 26-2), which superseded SR 11-7 and says it is most relevant to banking organizations with more than $30 billion in total assets. It excludes generative and agentic AI models from its scope. This is guidance and is applied in P10, not rated here.
- **CIRCIA:** no final rule as of 2026-09-25. **SEC:** no proposal to amend or rescind Item 1.05 or Item 106 was found in the Federal Register as of 2026-09-25.

## 7. Regulator-ready package
The GRC team keeps an evidence binder in the GRC platform, indexed by `req_id`, so the bank can respond quickly to an OCC examination request, a Federal Reserve inspection, a CFPB supervisory request on AI-001, an SEC or FINRA examination of the broker-dealer, or an SEC comment letter:
- this report, `gap-analysis.csv`, and the sample selections with exceptions for every sampled row;
- the P01 risk register, P02 SSP, P05 BIA, P06 policy set, P07 assessment and POA&M, and P08 runbook;
- the risk governance framework, the risk appetite statement, and the annual assessment that the bank may use the parent's framework (App. D I.3);
- the board risk committee charter and minutes (252.22);
- notification incident determinations and notices sent (Part 53; 225.302);
- AI-001 validation, fair lending test results, and reason code library (from P10);
- documents kept for at least 7 years under the records schedule.

## 8. Approval
Approved by the Chief Compliance Officer, the Chief Risk Officer, and the CISO on 2026-08-21. The roadmap was reviewed by the board risk committee on 2026-09-15. Next reassessment: 2027-05 to 2027-07.
