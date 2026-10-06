# Regulatory Gap Analysis: Cris Santos Company | Other Services | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded national electronics and device repair chain, NAICS 811210; 1,120 stores in 44 states and DC) |
| Tier / Vertical | Enterprise / Other Services (except Public Administration) |
| Primary benchmark | NIST Cybersecurity Framework (CSF) 2.0 (NIST CSWP 29, 2024-02-26), all 106 subcategories. **Voluntary benchmark: no sector cybersecurity rule applies** (section 1). Label `N81-BM` in the other deliverables |
| Binding by contract | PCI DSS v4.0.1 at ROC depth (N81-R03); Manufacturer A, B, and C program agreements (fictional terms); SL-1 and SL-2 client agreements (P09) |
| Binding law and regulation | FTC Act Section 5 (N81-R01); FACTA receipt truncation (15 U.S.C. 1681c(g)); FTC Disposal Rule (N81-R04); state breach notification and data security laws (N81-R02), Florida worked example Fla. Stat. 501.171; California CCPA cybersecurity audit, risk assessment, and ADMT regulations (11 CCR 7120-7124, 7150-7157, 7200 and following); other state comprehensive privacy laws; SEC Form 8-K Item 1.05 and Regulation S-K Item 106; HIPAA Security Rule standards and business associate breach notice for SL-2 only (N81-R06) |
| Sanitization reference | NIST SP 800-88 Rev. 2, *Guidelines for Media Sanitization* (final, September 2025) |
| Assessment dates | 2026-06-01 to 2026-07-31 (evidence sampling completed 2026-08-14; DLP scan of the STPP on 2026-07-21) |
| Assessors | GRC team (second line) with the Chief Compliance Officer and the PCI Program Manager; applicability reviewed with outside counsel; sampling reperformed by Internal Audit for 8 rows |
| Workbook | `gap-analysis.csv` (230 rows) |
| Approved | Chief Compliance Officer and CISO, 2026-08-21; roadmap reviewed by the risk and technology committee of the board, 2026-09-10 |

## 1. Applicability
**No sector cybersecurity regulation applies.** No federal agency issues cybersecurity rules for repair businesses, so the vertical research (`02_industry-rules/repair-personal-services/`) names NIST CSF 2.0 as the benchmark. At this size the company is bound by more general law, by contract, and by its status as a public company. Each candidate was checked against its source:

| Requirement | Test (source text) | Decision |
|---|---|---|
| **FTC Act Section 5** (N81-R01) | 45(a)(1) declares "unfair or deceptive acts or practices in or affecting commerce" unlawful. 45(n): a practice is unfair only if it "causes or is likely to cause substantial injury to consumers which is not reasonably avoidable by consumers themselves and not outweighed by countervailing benefits to consumers or to competition." No size threshold | **Applies.** For-profit business in commerce. Deception covers intake notices and AI claims; unfairness covers the handling of devices, passcodes, and sanitization (4 rows) |
| **PCI DSS v4.0.1** (N81-R03) | Contractual, through the merchant agreement. Level 1 as designated by the acquirer (letter 2026-02-17, fictional); validation by ROC with a QSA; AC stores in 2026 scope | **Applies by contract.** All 12 requirements at requirement or sub-requirement level, plus the three appendices (68 rows). The PCI SSC standards page (checked 2026-09-26) shows no newer version |
| **FACTA receipt truncation** | 15 U.S.C. 1681c(g)(1): no person that accepts credit or debit cards "shall print more than the last 5 digits of the card number or the expiration date upon any receipt provided to the cardholder at the point of the sale or transaction"; applies to electronically printed receipts ((g)(2)) | **Applies** (1 row) |
| **FTC Disposal Rule** (N81-R04) | Applies to "consumer information", meaning consumer reports and information derived from them (16 CFR 682.1(b), 682.3(a)) | **Applies narrowly** to background check reports on about 38,000 applicants a year. **It does not govern customer device wiping** (1 row) |
| **State breach and data security laws** (N81-R02) | Each state where affected individuals reside. Florida worked example: a covered entity is a "commercial entity that acquires, maintains, stores, or uses personal information" (501.171(1)(b)); personal information includes an email or user name with a password, and a name with geolocation, medical, or biometric information ((1)(g)) | **Applies.** 1 generic row and 6 Florida rows ((2), (3), (4), (5), (6), (8)). The company is also a third-party agent for SL-1 and SL-2 clients under (6) |
| **California CCPA and CPPA regulations** | A CCPA business includes one with annual gross revenue over $26,625,000 (Cal. Civ. Code 1798.140(d), as adjusted). The cybersecurity audit applies to a business that meets the revenue test and processed personal information of 250,000 or more consumers in the prior year (11 CCR 7120). Regulations effective 2026-01-01 | **Applies.** About 3.6 million California customer records. First audit period 2027-01-01 to 2028-01-01, report due 2028-04-01 (2026 revenue over $100 million). ADMT duties apply from 2027-01-01 to applicant screening (AI-004). Risk assessments for existing processing due 2027-12-31 (3 rows) |
| **Other state comprehensive privacy laws** | Thresholds vary; the cross-sector reference lists 23 enacted laws as of 2026-09-25 | **Applies in several states.** The Chief Privacy Officer keeps a state-by-state register; 1 summary row here |
| **SEC Item 1.05 and Item 106** | Publicly traded SEC registrant, not a smaller reporting company. Form 8-K Item 1.05; 17 CFR 229.106(b)-(d) (eCFR text read 2026-09-23 version) | **Applies** (8 rows) |
| **HIPAA, SL-2 only** (N81-R06) | Not a covered entity (45 CFR 160.103). Under 38 BAAs with health care clients the company is a business associate, and "a covered entity or business associate must comply with the applicable standards" of the Security Rule (164.302). A business associate must notify the covered entity of a breach of unsecured PHI no later than 60 calendar days after discovery (164.410(b)) | **Applies to SL-2 only.** 22 Security Rule standards plus two required implementation specifications that matter most here (risk analysis and disposal), and 164.410 (25 rows). 164.314(b) is not applicable |
| **Manufacturer program agreements** | Contract (fictional terms, scenario facts section 1) | **Applies by contract** (1 summary row) |
| FTC Safeguards Rule, COPPA, HIPAA covered entity, Florida Digital Bill of Rights, CIRCIA | 16 CFR 314.1(b); 16 CFR Part 312; 45 CFR 160.103; Fla. Stat. 501.702; 6 U.S.C. 681-681g | **Not applicable** (5 screen rows). The Florida Digital Bill of Rights needs revenue over $1 billion **and** one of: 50% or more of revenue from online advertising, a smart speaker and voice command service, or an app store with at least 250,000 applications. The company passes only the revenue test |

**Why the Disposal Rule is not the wiping rule.** Repair businesses often assume the FTC Disposal Rule governs wiping customer devices. It covers consumer reports only. The duty to dispose of customer data properly comes from state law, with Fla. Stat. 501.171(8) as the worked example ("all reasonable measures to dispose ... of customer records containing personal information ... by shredding, erasing, or otherwise modifying the personal information ... to make it unreadable or undecipherable"), from FTC Act Section 5, from the SL-2 BAAs (45 CFR 164.310(d)(2)(i) for ePHI), and from client contracts. **Author interpretation, for counsel to confirm:** devices left for recycling and data recovery copies are "customer records" under 501.171(1)(c). The company treats them that way and uses SP 800-88 Rev. 2 as the method.

**When technician access becomes a breach.** Fla. Stat. 501.171(1)(a) excludes "good faith access of personal information by an employee or agent ... provided that the information is not used for a purpose unrelated to the business." Opening the photo app to test the camera is good-faith access. Browsing or copying a customer's photos is not. This line is the basis of the customer data access standard (POL-04 4.4) and of the P08 runbook.

**FTC precedent.** A search of ftc.gov found no FTC action against a repair business for technician snooping. The closest precedent is *In re DesignerWare, LLC* and seven rent-to-own operators (complaints announced 2012-09-25, final orders 2013-04-15), where covert collection of data from consumers' rented computers was treated as unfair. The duty does not depend on authorized status: the company must make its own practices reasonable and its statements true.

## 2. Method
1. **Decompose.** CSF 2.0: every subcategory (106 rows) quoted from `00_universal-framework/frameworks/csf2_core.csv`. PCI DSS v4.0.1: requirement groups 1.1 to 12.10 at the second level, with 6.4 and 11.6 split to their numbered requirements because of the payment page gap, plus Appendices A1 to A3. **PCI DSS is copyrighted; the rows give requirement numbers with short topic labels written for this analysis. Read the official standard for the text.** Statutes and regulations were broken into citation-level duties from the source text (FTC Act, FACTA, 16 CFR 682, Fla. Stat. 501.171, 17 CFR 229.106 from the eCFR, 11 CCR as summarized in the cross-sector reference). HIPAA rows use the requirement text from NIST SP 800-66 Rev. 2 as listed in the Health Care crosswalk.
2. **Crosswalk.** CSF rows carry NIST's official CSF 2.0 informative references to SP 800-53 Rev. 5.2.0 in full (`nist_official_sp800_53r5`), with a key-control selection by the author. HIPAA rows use the Health Care crosswalk (an author mapping). All other rows are author mappings and are labeled that way; no official mapping exists for PCI DSS v4.0.1, the FTC Act, or state law.
3. **Evidence sampling.** Where a requirement operates on a population, the team tested a sample and recorded the population, sample size, and exceptions. Key controls with large populations used 60 items (95% confidence, 5% tolerable deviation, zero expected deviations); populations under 250 or lower-risk controls used 25 to 40; AC store conditions used 10 stores selected at random across the six AC states; configuration and data analytics covered 100% of the population. **42 rows were tested by sampling or full-population analytics; 34 found exceptions.**
4. **Rate.** Met, Partially met, Not met, or Not applicable. Each gap is rated with the P01 scale and carries an owner and date. High gaps are in the P01 register and the P07 POA&M.

## 3. Results summary
| Regulation / section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| CSF 2.0 GOVERN (GV) | 23 | 8 | 0 | 0 | 31 |
| CSF 2.0 IDENTIFY (ID) | 15 | 6 | 0 | 0 | 21 |
| CSF 2.0 PROTECT (PR) | 11 | 11 | 0 | 0 | 22 |
| CSF 2.0 DETECT (DE) | 7 | 4 | 0 | 0 | 11 |
| CSF 2.0 RESPOND (RS) | 10 | 3 | 0 | 0 | 13 |
| CSF 2.0 RECOVER (RC) | 7 | 1 | 0 | 0 | 8 |
| **CSF 2.0 subtotal** | **73** | **33** | **0** | **0** | **106** |
| PCI DSS v4.0.1 (N81-R03) | 33 | 28 | 0 | 7 | 68 |
| FTC Act Section 5 (N81-R01) | 0 | 4 | 0 | 0 | 4 |
| FACTA receipt truncation | 0 | 1 | 0 | 0 | 1 |
| FTC Disposal Rule (N81-R04) | 1 | 0 | 0 | 0 | 1 |
| State breach and data security laws (N81-R02) | 4 | 3 | 0 | 0 | 7 |
| California CCPA regulations | 0 | 2 | 1 | 0 | 3 |
| Other state comprehensive privacy laws | 0 | 1 | 0 | 0 | 1 |
| SEC Form 8-K Item 1.05 | 1 | 2 | 0 | 0 | 3 |
| SEC Regulation S-K Item 106 | 5 | 0 | 0 | 0 | 5 |
| HIPAA Security Rule, SL-2 business associate (N81-R06) | 15 | 8 | 0 | 1 | 24 |
| HIPAA 164.410, SL-2 business associate (N81-R06) | 0 | 1 | 0 | 0 | 1 |
| Manufacturer program agreements | 0 | 1 | 0 | 0 | 1 |
| Applicability screens | 0 | 0 | 0 | 5 | 5 |
| **Total** | **132** | **84** | **1** | **13** | **230** |

**Gap risk levels (85 unmet or partially met rows):** High 40, Moderate 40, Low 5.

**Reading the pattern.** The core estate meets most requirements; the program is mature. Two things drive almost every gap:
1. **The acquired chain.** 26 of the 40 High rows are wholly or partly about the 160 AC stores: card data in clear text (PCI DSS 1.2, 1.3, 4.2, 5.2, 6.3), shared logins and no MFA (7.2, 8.2, 8.4), no logs or detection (10.2, 10.4, 11.5), and passcodes in the legacy ticketing service. Conversion is the fix, with interim controls before QSA fieldwork.
2. **What makes a repair business different.** Passcodes in free-text notes (G-037, G-116), technician access to devices (G-057), and sanitization that is not yet verified per device everywhere (G-038, G-187, G-213, G-214).

The one Not met row is the California ADMT duty for applicant screening (G-190), which starts 2027-01-01.

## 4. Priority gaps (High)
| Rows | Gap | Action | Owner | Target |
|---|---|---|---|---|
| G-062, G-063, G-108, G-109, G-113, G-123, G-125, G-130, G-148 | AC card data in clear text on flat networks; hardening, patching, malware, and PIN pad inspection gaps at AC stores | Interim card data VLANs, EDR, unique admin passwords, inspections; conversion to P2PE in two waves (POAM-001; POAM-002) | Vice President, Integration Management Office | 2027-03-31 (wave 1 2026-12-15) |
| G-055, G-061, G-136, G-139, G-141 | AC shared logins, no MFA, passcodes and passwords in the AC legacy ticketing service | Purge; named accounts with MFA; federation; migration (POAM-004; POAM-011) | Vice President, Integration Management Office | 2026-12-15 |
| G-068, G-075, G-150, G-152, G-158, G-160 | No logs, detection, or internal scan follow-up at AC stores | SIEM collectors and EDR (POAM-012); patching (POAM-019) | Director of Security Operations | 2026-12-31 |
| G-037, G-116, G-117 | Passcode and card-number strings in STPP notes; spoken card numbers in recordings | Purge and block (POAM-003); DTMF masking and recording pause (POAM-013) | Chief Digital Officer; Vice President, Contact Center | 2026-11-30; 2027-03-31 |
| G-057, G-079 | Notes visible to all location roles; bench sessions reviewed only on alert; 9% of bench workstations without EDR | POAM-003; POAM-005 | Chief Digital Officer; Senior Vice President, Store Operations | 2027-01-31 |
| G-038, G-187, G-213, G-214 | Sanitization not verified per device at Depot West; 2026-05 resale exposure; 180 TB of old recovered data | POAM-006; POAM-016 | Director of Sanitization and Asset Recovery | 2026-12-31 |
| G-133, G-161 | Mobile web deposit page outside script inventory and change detection | POAM-007 | Director of Digital Engineering | 2026-11-15 |
| G-071 | AC flat networks; NAC missing at 320 core stores | POAM-002; POAM-018 | Director of Network Engineering | 2027-06-30 |
| G-052, G-089, G-192, G-193 | Materiality process and escalation not exercised for a card compromise with customer data exposure | Tabletop 2026-11-12 and playbook update (POAM-008) | General Counsel | 2026-11-30 |
| G-175, G-177, G-182 | FTC Act and Florida reasonable security: AC intake form promises no data access; the core exceptions above | Replace AC intake forms now; close POAM-003 to POAM-006 | Chief Privacy Officer; CISO | 2026-10-31 to 2027-03-31 |
| G-190 | California ADMT duties for applicant screening from 2027-01-01 | Notice, opt-out, and access process, or disable ranking for California roles (POAM-009) | Chief Human Resources Officer | 2026-12-31 |

The full list, with evidence and samples, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07).

**Before QSA fieldwork (2026-10-19):** AC interim controls in place at all 160 stores (unique admin passwords, browsing blocked on POS PCs, EDR on POS PCs, inspection logs), the AC scope document (G-166), and the purge of card numbers from STPP notes started with evidence. The Vice President, Payments agreed with the acquirer on 2026-09-02 that AC stores not converted by fieldwork are assessed against the conversion plan and interim controls (P01 R-013).

## 5. Compliance roadmap
| Quarter | Milestones | Requirements served | Evidence produced |
|---|---|---|---|
| 2026 Q4 | AC interim controls and wave 1 (70 stores) (POAM-001, POAM-002); notes purge (POAM-003); AC legacy ticketing purge and migration (POAM-004); Depot West verification (POAM-006); mobile deposit page script controls (POAM-007); disclosure tabletop (POAM-008); SL-1 API fix (POAM-010); SIEM at AC stores (POAM-012); TPSP AOCs (POAM-014); BAA inventory (POAM-022); California audit scoping (POAM-021); ADMT readiness (POAM-009) | PCI DSS 1 to 12; FTC Act; Fla. Stat. 501.171(2), (8); Item 1.05; 164.310(d), 164.410; 11 CCR 7120, 7200 | ROC evidence; purge records; sanitization records; tabletop report; scope and auditor selection |
| 2027 Q1 | AC wave 2 (90 stores) and federation (POAM-001, POAM-011); bench image and analytics (POAM-005); DTMF masking to 100% (POAM-013); downstream recycler terms and subcontractor BAAs (POAM-015); processor fallback test (POAM-020) | PCI DSS 3.3, 7, 8, 12.8; 164.308(b)(1); FTC Act | Conversion records; masking coverage report; amended contracts |
| 2027 Q2 | NAC at the remaining core stores (POAM-018); first quarterly California audit evidence review | PCI DSS 1.2, 11.2; 11 CCR 7120 | NAC coverage report |
| 2027 Q3 | Annual gap reassessment; CCPA risk assessments for existing processing (due 2027-12-31) | All | Updated P01 and P03 |

## 6. Pending regulatory changes
- **PCI DSS.** v4.0.1 remains current per the PCI SSC standards page (checked 2026-09-26). Recheck before each ROC.
- **California.** The CPPA regulations took effect 2026-01-01. ADMT compliance for existing uses is due 2027-01-01; the first cybersecurity audit report is due 2028-04-01; risk assessments for existing processing are due 2027-12-31 and submissions 2028-04-01.
- **State AI hiring laws.** Colorado SB26-189 applies to consequential decisions from 2027-01-01. Illinois Public Act 103-0804 and NYC Local Law 144 apply now (P10).
- **HIPAA Security Rule NPRM** (90 FR 898, 2025-01-06) is still proposed. The 24 SL-2 Security Rule rows note it in `pending_rule_change`. It is not treated as a current obligation.
- **CIRCIA:** the final rule had not been published as of 2026-09-25. Reporting to CISA is voluntary until it takes effect.
- **SEC:** a 2025 petition asks the SEC to rescind Item 1.05. No SEC proposal to amend or rescind was found as of 2026-09-25, so Item 1.05 and Item 106 remain in force.
- **FTC AI accuracy policy statement** (proposed 2026-07) is not final; it is relevant to AI claims (P10).

## 7. Regulator-ready package
The GRC team keeps an evidence binder in the GRC platform, indexed by `req_id`, so the company can respond quickly to a state attorney general inquiry, an FTC civil investigative demand, the acquirer or card brands, a client or manufacturer audit, an SEC comment letter, or the California cybersecurity auditor:
- this report, `gap-analysis.csv`, and the sample selections with exceptions for every sampled row;
- the P01 risk register, P02 SSP, P05 BIA, P06 policy set, P07 assessment and POA&M, and P08 runbook and notification matrix;
- the 2025 ROC and AOC, and the 2026 ROC once issued;
- sanitization records and certificates by client and lot;
- the state breach law matrix from outside counsel and the state privacy applicability register;
- BAAs with abstracts for SL-2 health care clients;
- document retention of at least 6 years (POL-01 4.11).

## 8. Approval
Approved by the Chief Compliance Officer and the CISO on 2026-08-21. The roadmap was reviewed by the risk and technology committee of the board on 2026-09-10. Next reassessment: 2027-06 to 2027-07.
