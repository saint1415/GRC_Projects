# Regulatory Gap Analysis: Cris Santos Company | Communications | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded regional broadband and wired telecommunications carrier; FL, GA, SC, NC) |
| Tier / Vertical | Enterprise / Communications |
| Primary regulation | FCC CPNI rules, 47 CFR 64.2001-64.2011 (47 U.S.C. 222), text in force on 2026-09-23 (C-COMMUNICATIONS-R01) |
| Other regulations analyzed | CALEA SSI rules, 47 CFR Part 1, Subpart Z (C-COMMUNICATIONS-R03); FCC outage reporting, 47 CFR Part 4 (C-COMMUNICATIONS-R02); SEC Form 8-K Item 1.05 and Reg S-K Item 106 (C-COMMUNICATIONS-R06); state breach and data security laws (Florida worked example); FAR reporting clauses 52.204-23, 52.204-25, 52.204-30 |
| Voluntary benchmark | NIST CSF 2.0, prioritized with the CISA Cross-Sector Cybersecurity Performance Goals |
| Assessment dates | 2026-06-01 to 2026-07-31 (evidence sampling completed 2026-08-14) |
| Assessors | GRC team (second line) with the Chief Compliance Officer and the Vice President, Regulatory Affairs; outside telecommunications counsel reviewed section 1; sampling reperformed by Internal Audit for 8 rows |
| Sources checked | eCFR full text (point in time 2026-09-23) for 47 CFR 64.2011, 4.9, 1.20003-1.20006, and 17 CFR 229.106; Federal Register API (searched through 2026-10-05); govinfo text of SEC Release 33-11216 (88 FR 51896) for Form 8-K Item 1.05; Florida Statutes 501.171 (2026) from the Legislature's site |
| Approved | Chief Compliance Officer and CISO, 2026-08-21; roadmap reviewed by the risk and technology committee of the board, 2026-09-10 |

## 1. Applicability
### 1.1 Regulations that apply
| Regulation | Applies? | Basis |
|---|---|---|
| **FCC CPNI rules** (C-COMMUNICATIONS-R01) | **Yes** | The rules bind "telecommunications carriers," defined by reference to 47 U.S.C. 153, and "shall include an entity that provides interconnected VoIP service" (47 CFR 64.2003(o)). The company provides local exchange, interexchange, and wholesale common carrier services, and 630,000 interconnected VoIP lines. Each operating carrier subsidiary (main company, AQ-01, AQ-02, AQ-03) is covered. No size threshold exists in 64.2001-64.2011. Only 64.2010(h) (CMRS) does not apply |
| **CALEA SSI rules** (C-COMMUNICATIONS-R03) | **Yes** | Each subsidiary is engaged in "the transmission or switching of wire or electronic communications as a common carrier for hire" (47 U.S.C. 1001(8)(A)). The FCC's January 2025 declaratory ruling reading CALEA section 105 as a general cybersecurity duty was rescinded on 2025-11-20 (FCC 25-81, 90 FR 58006); the analysis covers the codified SSI rules only |
| **Outage reporting** (C-COMMUNICATIONS-R02) | **Yes** | Wireline (4.9(f)), interconnected VoIP (4.9(g)), SS7 provider for 14 rural carriers (4.9(d)), and LEC tandem facilities (4.9(b)); PSAP and 988 notices (4.9(h), (i)); DIRS (4.18). Thresholds are outage-based, not size-based |
| **SEC Form 8-K Item 1.05 and Reg S-K Item 106** (C-COMMUNICATIONS-R06) | **Yes** | Exchange Act registrant, not a smaller reporting company. **Item 1.05(d)** applies because the company is subject to 47 CFR 64.2011 |
| **State breach and data security laws** | **Yes** | The law of each state where affected individuals reside; Florida (Fla. Stat. 501.171) is the worked example, including its data security (501.171(2)) and disposal (501.171(8)) duties |
| **FAR reporting clauses** | **Yes, for federal contracts** | About 140 federal agency contracts include 52.204-23, 52.204-25, and 52.204-30 |
| CIRCIA (C-COMMUNICATIONS-R05) | **Not in force** | No final rule published as of 2026-10-05. The proposed rule's sector criteria would reach communications providers; reporting to CISA is voluntary until then |
| Submarine cable rules (C-COMMUNICATIONS-R04) | No | No cable landing license or SLTE |
| Covered 911 service provider rules (47 CFR 9.19) and the 2026 NG911 reliability order (91 FR 42794) | Not analyzed here | 911 routing to PSAPs is provided by state and regional NG911 system service providers, not the company. Regulatory Affairs is reviewing with counsel whether any originating-provider duties in the NG911 orders reach the company; that review is outside this gap analysis |
| EAS rules | No | No video or broadcast service |
| SOX Section 404 | Separate program | IT general controls over billing and ERP are tested by the SOX program and not repeated here |

### 1.2 Broadband is outside the CPNI rules today
CPNI is information about "a telecommunications service subscribed to by any customer of a telecommunications carrier" plus information in bills for telephone exchange or toll service (47 U.S.C. 222(h)(1)). In *Ohio Telecom Ass'n v. FCC* (6th Cir., decided 2025-01-02, No. 24-7000) the court held that broadband providers offer only an information service and set aside the FCC's 2024 reclassification order; the FCC conformed the CFR on 2025-08-08 (90 FR 38406). No later reclassification was found through 2026-10-05. **Result:** broadband usage data is not CPNI, but broadband counts as a communications-related service for marketing (64.2003(e), (i)), so using voice CPNI to sell broadband needs approval (64.2007(b)). **By policy (POL-04), the company protects the whole customer account record to the CPNI standard.**

### 1.3 Status of the 2023 breach amendments to 64.2011
The FCC's 2023 Data Breach Reporting Order (FCC 23-111, 89 FR 9968) took effect 2024-03-13 except the amendments to 64.2011, which are delayed indefinitely pending an FCC effective-date notice. The Sixth Circuit denied the petitions for review on 2025-08-13 (*Ohio Telecom Ass'n v. FCC*, Nos. 24-3133/3206/3252), upholding the rules under 47 U.S.C. 201(b). No effective-date notice was found in the Federal Register through 2026-10-05, and the eCFR text current through 2026-09-23 still shows the original 64.2011. **This analysis uses the current 64.2011**; the amended text is in the `pending_rule_change` column only.

### 1.4 Where the CPNI rule and the SEC rule meet
A CPNI breach can also be a material cybersecurity incident. Section 64.2011(a) bars a carrier from disclosing a breach publicly until the law enforcement notice process is complete, and 64.2011(b)(1) adds a hold of 7 full business days after the USSS and FBI notice. The SEC identified this as the one federal rule that conflicts with Item 1.05 and added **Item 1.05(d)**: a registrant subject to 64.2011 that must delay disclosing a data breach may delay the Item 1.05 disclosure for the 64.2011(b)(1) period, no more than seven business days after the law enforcement notice, if it notifies the SEC by EDGAR correspondence no later than the date the 8-K was otherwise due (SEC Release 33-11216, 88 FR 51896). The SEC release notes that the exception does not extend to further delays an agency directs under 64.2011(b)(3); those go through the Attorney General path in Item 1.05(c). The company's materiality playbook does not yet reflect any of this (G-054).

## 2. Method
1. **Decompose.** Each paragraph of 47 CFR 64.2005-64.2011 that imposes, permits, or limits conduct became one row, cited to the paragraph (public-domain text; short quotes only), with 47 U.S.C. 222(a) as the statutory duty (G-001). CALEA, Part 4, SEC, Florida, and FAR rows follow the same method from the retrieved text. The benchmark rows use the CSF 2.0 outcomes most relevant to the P08 intrusion scenario.
2. **Crosswalk.** Regulatory rows are mapped to CSF 2.0 and SP 800-53 Rev. 5 as **author mappings**; NIST has published no official mapping for 47 CFR Parts 1, 4, or 64, the SEC rules, the FAR clauses, or state statutes. Benchmark rows use NIST's official CSF 2.0 to SP 800-53 reference mapping (a selection of the listed controls).
3. **Evidence sampling.** Where a requirement operates on a population, the team tested a sample and recorded the population, sample size, and exceptions in the CSV. Key controls with large populations used 60 items per stratum (95% confidence, 5% tolerable deviation, zero expected deviations); lower-risk controls used 25 to 40 items; contact records, entitlements, and element data were checked in full with analytics. Selections were random. **26 rows were tested by sampling or full-population analytics; 10 found exceptions.**
4. **Rate.** Met, Partially met, Not met, or Not applicable. Each gap is rated with the P01 scale and carries an owner and date. High gaps are in the P01 register and the P07 POA&M.

## 3. Results summary
| Regulation | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| FCC CPNI rules (47 U.S.C. 222(a); 64.2005-64.2011) | 34 | 18 | 15 | 0 | 1 |
| CALEA SSI rules (47 CFR 1.20000-1.20006) | 8 | 3 | 4 | 1 | 0 |
| Outage reporting (47 CFR Part 4) | 7 | 6 | 1 | 0 | 0 |
| SEC Form 8-K Item 1.05 and Reg S-K Item 106 | 10 | 8 | 1 | 1 | 0 |
| State breach and data security laws | 7 | 4 | 3 | 0 | 0 |
| FAR reporting clauses | 3 | 3 | 0 | 0 | 0 |
| NIST CSF 2.0 benchmark (voluntary) | 16 | 4 | 12 | 0 | 0 |
| **Total** | **85** | **46** | **36** | **2** | **1** |

**Gap risk levels (38 gaps):** High 10, Moderate 21, Low 7.

**Where the gaps are.** Most CPNI gaps sit in the acquired carriers (AQ-02 and AQ-03: notices, approvals, portal authentication, change notices) and in one care vendor. The main company's in-house care, retail, portal, breach procedure, and approval mechanics are Met. The two Not met rows are the AQ-03 CALEA filing (G-041) and the Item 1.05(d) path (G-054).

## 4. Priority gaps (High)
| Row | Citation | Gap | Action | Owner | Target |
|---|---|---|---|---|---|
| G-021 | 64.2010(a) | Reasonable measures not yet in place for the network management plane, which leads to the CDR store | POAM-002; POAM-004; POAM-016 | CISO | 2027-03-31 |
| G-022 | 64.2010(b) | 4 of 60 sampled CV-2 calls discussed call detail after SSN4 or biographical checks | Vendor role change, retraining, monthly sampling (POAM-005) | Chief Customer Officer | 2026-12-31 |
| G-023 | 64.2010(c) | AQ-02 online access reachable with biographical information | Rebuild AQ-02 reset (POAM-006) | Chief Customer Officer | 2026-11-30 |
| G-025 | 64.2010(e) | AQ-02 backup authentication uses date of birth and SSN4 | POAM-006 | Chief Customer Officer | 2026-11-30 |
| G-051 | Form 8-K Item 1.05, Instruction 1 | Determination steps never tested with the current committee | Tabletop 2026-11-12 (POAM-013) | General Counsel | 2026-11-30 |
| G-054 | Form 8-K Item 1.05(d) | Playbook lacks the CPNI delay path and EDGAR correspondence | Playbook update and template (POAM-013) | General Counsel | 2026-11-30 |
| G-074 | CSF PR.PS-02 | 9 of 60 sampled critical network findings past SLA | POAM-008; POAM-009 | Director of Network Security Engineering | 2027-01-31 |
| G-075 | CSF PR.AA-01 | About 7,400 elements on shared local accounts | POAM-002 | Director of Network Security Engineering | 2027-03-31 |
| G-077 | CSF PR.IR-01 | AQ management networks not isolated | POAM-003 | Vice President, Integration Management Office | 2027-01-31 |
| G-081 | CSF DE.CM-01 | 42% of network elements send no logs to the SIEM | POAM-004 | Director of Security Operations | 2027-03-31 |

## 5. Compliance roadmap
| Quarter | Milestones | Regulations served | Evidence produced |
|---|---|---|---|
| 2026 Q4 | AQ-03 CALEA SSI filing through CEFS (POAM-020); disclosure tabletop and Item 1.05(d) playbook update (POAM-013); AQ-02 portal reset rebuild (POAM-006); care vendor authentication fix and training gate (POAM-005, POAM-018); PSAP contact confirmation (POAM-021); AQ CPNI notices and campaign pause (POAM-022); AQ change notices (POAM-024); default credential cleanup (POAM-012) | 47 CFR 1.20003, 1.20005; Form 8-K Item 1.05; 64.2008, 64.2009(b), 64.2010(b), (c), (e), (f); 4.9(h) | CEFS receipt; tabletop report; portal test results; call samples; mailing records; contact confirmations |
| 2027 Q1 | AQ VPN restriction and jump-host routing (POAM-003); BSS DR retest (POAM-011); evidence-based CPNI certifications for four carriers by 2027-03-01 (POAM-019); management plane named accounts and MFA (POAM-002); network log coverage to 95% (POAM-004); CPNI read analytics (POAM-016); vendor contract amendments (POAM-014) | 64.2009(e); 64.2010(a); Fla. Stat. 501.171(2), (6); CSF PR.AA-01, PR.IR-01, DE.CM-01 | Certification packages; coverage reports; DR report; amended contracts |
| 2027 Q2 | AQ-02 SBC replacement complete (POAM-008); CDR transfer encryption (POAM-017); Internal Audit test of Item 106 statements | 64.2010(a); Item 106 | Replacement records; protocol inventory |
| 2027 Q3 | AQ-03 BSS migration (2027-09-30); annual risk and gap reassessment; recheck 64.2011 amendment status and CIRCIA | All | Updated P01 and P03 |
| 2028 | TDM switch retirement (POAM-009) | CSF PR.PS-02 | Retirement records |

## 6. Pending regulatory changes
- **64.2011 amendments (delayed indefinitely).** If the FCC announces an effective date: the FCC would be notified along with the USSS and FBI within 7 business days; "breach" would cover customer PII as well as CPNI and inadvertent access; customer notice would be due without unreasonable delay and within 30 days, with no 7-day hold; breaches under 500 customers with no reasonably likely harm would go into an annual summary. Removing the hold would also remove the Item 1.05(d) delay basis (the SEC release noted the FCC proposal could eliminate the conflict). The P08 matrix carries both versions.
- **CIRCIA.** Covered cyber incident reports within 72 hours and ransom payment reports within 24 hours are expected once a final rule is published and effective. None is in effect as of 2026-10-05.
- **SEC.** No SEC proposal to amend or rescind Item 1.05 or Item 106 was found in the Federal Register as of 2026-10-05.
- **Broadband classification.** If broadband were reclassified, broadband usage data would become CPNI; the whole-account policy already covers it.

## 7. Regulator-ready package
The GRC team keeps an evidence binder in the GRC platform, indexed by `req_id`, so the company can respond quickly to an FCC Enforcement Bureau letter of inquiry, a state attorney general request, an SEC comment letter, or a contracting officer:
- this report, `gap-analysis.csv`, and the sample selections with exceptions for every sampled row;
- the P01 register, P02 SSP, P05 BIA, P06 policy set, P07 assessment and POA&M, and P08 runbook and matrix;
- CPNI certifications with their evidence packages (from CY2026), breach register and reporting facility receipts, approval and notice records (at least 1 year), and the campaign register;
- CALEA SSI filings and CEFS receipts for every subsidiary, and intercept certification records (held by the Director, Lawful Intercept Compliance, under restricted access);
- NORS, DIRS, and PSAP notification records;
- security documentation retained at least 6 years (POL-01 4.11).

## 8. Approval
Approved by the Chief Compliance Officer and the CISO on 2026-08-21. The roadmap was reviewed by the risk and technology committee of the board on 2026-09-10. Next reassessment: 2027-06 to 2027-07.
