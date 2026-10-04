# Regulatory Gap Analysis: Cris Santos Company | Educational Services | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded postsecondary education company operating one private, for-profit college; 23 campuses in six states; online students in all 50 states and DC) |
| Tier / Vertical | Enterprise / Educational Services |
| Primary regulation | FTC Standards for Safeguarding Customer Information (Safeguards Rule), 16 CFR Part 314, as applied to Title IV institutions and enforced by Federal Student Aid (FSA). Text checked on eCFR as of 2026-09-23 |
| Regulations analyzed | Safeguards Rule (all 47 rows: 314.3(a), every 314.4 paragraph, 314.6); FERPA (8 rows); Title IV requirements tied to security, fraud, refunds, and campus emergency notification (7 rows); SEC Form 8-K Item 1.05 and Reg S-K Item 106 (8 rows); state breach and data security laws (Florida worked example, 4 rows); applicability rows for COPPA, CIPA, HIPAA, CIRCIA, Colorado SB26-189, and the California ADMT rules (6 rows) |
| Assessment dates | 2026-06-01 to 2026-07-31 (evidence sampling completed 2026-08-14) |
| Assessors | GRC team (second line) with the Chief Compliance Officer and the Chief Privacy Officer; Internal Audit reperformed the samples for 8 rows (G-012, G-017, G-020, G-031, G-050, G-058, G-059, G-061) |
| Approved | Chief Compliance Officer and CISO (Qualified Individual), 2026-08-21; roadmap reviewed by the board risk committee, 2026-09-10 |

## 1. Applicability
| Regulation | Applies? | Basis |
|---|---|---|
| FTC Safeguards Rule (N61-R02) | **Yes, every element** | Each Title IV institution agrees in its PPA to comply with 16 CFR Part 314. FSA enforces it through the annual compliance audit and treats information security safeguards as part of administrative capability under 34 CFR 668.16(c) (FSA Electronic Announcement GENERAL-23-09, Feb. 9, 2023). For GLBA purposes FSA defines customer information as information obtained as a result of providing a financial service to a student, past or present, such as administering Title IV aid or making institutional loans |
| 16 CFR 314.6 exception | **No** | The exception applies only below 5,000 consumers. The company maintains customer information on about **2.3 million consumers** |
| FERPA (N61-R01) | **Yes** | The College receives funds under Department of Education programs. FERPA has no breach notification clock, but it requires a record of each disclosure (34 CFR 99.32(a)), which includes unauthorized ones |
| Title IV program requirements | **Yes** | SAIG Enrollment Agreement (breach report to FSA); administrative capability and separation of duties (34 CFR 668.16(c)); referral of applicant fraud to the Office of Inspector General (668.16(g)(1)); credit balance timing (668.164(h)(2)); campus emergency notification (668.46(g)); HEA section 483 limits on FAFSA data |
| SEC Item 1.05 and Item 106 | **Yes** | Publicly traded SEC registrant, not a smaller reporting company |
| State breach and data security laws | **Yes** | The law of each state where affected individuals reside; Florida (Fla. Stat. 501.171) is the worked example |
| COPPA (N61-R03) | **No** | No services directed to children under 13 and no users under 13 (minimum enrollment age 17). The company is for-profit, so it would be an "operator" if that changed |
| CIPA (N61-R04) | **No** | Not an E-Rate recipient |
| HIPAA Security Rule (N61-R05) | **No** | Not a covered entity. PHI excludes health information in education records covered by FERPA (45 CFR 160.103) |
| CIRCIA (N61-R06) | **Not in force** | Final rule not published as of 2026-09-25. The proposed rule would cover every Title IV institution; tracked in `pending_rule_change` |
| Colorado SB26-189 and California CPPA ADMT rules | **Not yet** | Both reach automated decisions about education. Colorado's act applies to consequential decisions made on or after 2027-01-01; the California ADMT compliance date is 2027-01-01. Readiness is assessed in P10 |
| SOX Section 404 | Separate program | IT general controls over ERP, payroll, and student billing are tested by the SOX program and not repeated here |
| PCI DSS | Separate program (contractual) | Card payments run on the payment processor's hosted pages |

**Not applicable within the Safeguards Rule:** 314.4(a)(1) to (a)(3), because the Qualified Individual is a company employee, not a service provider or affiliate.

## 2. Method
1. **Decompose.** Each row is a paragraph of 16 CFR 314.3 or 314.4, or of 34 CFR Part 99 or Part 668, at the most granular level the regulation uses (for example, 314.4(h)(1) to (h)(7)). Summaries paraphrase public-domain regulatory text. SEC rows follow 17 CFR 229.106 and Form 8-K Item 1.05; state rows follow the Florida statute text.
2. **Requirement type.** The Safeguards Rule has no required and addressable split. Its elements are mandatory, with two built-in alternatives: compensating controls for encryption reviewed and approved by the Qualified Individual (314.4(c)(3)), and equivalent controls for MFA approved in writing by the Qualified Individual (314.4(c)(5)). No alternative has been approved; student accounts therefore remain a gap under (c)(5).
3. **Crosswalk.** Each row maps to CSF 2.0 and SP 800-53 Rev. 5. These are **author mappings**; no official NIST mapping for 16 CFR Part 314 exists.
4. **Evidence sampling.** Where a requirement operates on a population, the team tested a sample and recorded the population, sample size, and exceptions in the CSV. Key controls with populations over 250 used 60 items (95% confidence, 5% tolerable deviation, zero expected deviations); populations of 50 to 250 used 40 items; lower-risk controls used 25 items; configuration and account data were checked in full with analytics. Selections were random. **30 rows were tested by sampling or full-population analytics; 17 found exceptions.**
5. **Status.** Met, Partially met, Not met, or Not applicable, as of the end of fieldwork. Each gap is rated with the P01 scale and carries an owner and date. High gaps are in the P01 register and the P07 POA&M.

## 3. Results summary
| Regulation / section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| 314.3(a) Written program | 1 | 0 | 0 | 0 | 1 |
| 314.4(a) Qualified Individual | 1 | 0 | 0 | 3 | 4 |
| 314.4(b) Risk assessment | 4 | 1 | 0 | 0 | 5 |
| 314.4(c) Safeguards | 1 | 9 | 1 | 0 | 11 |
| 314.4(d) Testing and monitoring | 4 | 0 | 0 | 0 | 4 |
| 314.4(e) Personnel | 4 | 0 | 0 | 0 | 4 |
| 314.4(f) Service providers | 1 | 2 | 0 | 0 | 3 |
| 314.4(g) Evaluate and adjust | 1 | 0 | 0 | 0 | 1 |
| 314.4(h) Incident response plan | 5 | 3 | 0 | 0 | 8 |
| 314.4(i) Report to the board | 3 | 0 | 0 | 0 | 3 |
| 314.4(j) FTC notification | 1 | 1 | 0 | 0 | 2 |
| 314.6 Exception | 0 | 0 | 0 | 1 | 1 |
| **Safeguards Rule subtotal** | **26** | **16** | **1** | **4** | **47** |
| FERPA (N61-R01) | 3 | 5 | 0 | 0 | 8 |
| Title IV program requirements | 2 | 4 | 1 | 0 | 7 |
| SEC Form 8-K Item 1.05 | 1 | 2 | 0 | 0 | 3 |
| SEC Regulation S-K Item 106 | 5 | 0 | 0 | 0 | 5 |
| State breach and data security laws | 2 | 2 | 0 | 0 | 4 |
| COPPA, CIPA, HIPAA, CIRCIA, Colorado SB26-189, California ADMT | 0 | 0 | 0 | 6 | 6 |
| **Total** | **39** | **29** | **2** | **10** | **80** |

**Gap risk levels across all regulations (31 gaps):** High 9, Moderate 18, Low 4.

**What is working:** a mature written program with a Qualified Individual who reports to the board in writing every year; a risk assessment that meets 314.4(b)(1); encryption of customer information at rest and in transit (60 of 60 sampled storage locations); annual independent penetration testing and quarterly scanning; security training; an incident response plan that addresses all seven 314.4(h) elements; separation of awarding and disbursing (60 of 60 sampled disbursements); credit balances paid on time (60 of 60 sampled refunds); and the Item 106 disclosures.

**The 2 Not met rows** are 314.4(c)(6)(i) (no disposal of customer information has ever run, G-018) and HEA section 483 (FAFSA-derived data used outside aid administration, G-059).

## 4. Priority gaps (High)
| Row | Citation | Gap | Action | Owner | Target |
|---|---|---|---|---|---|
| G-012 | 16 CFR 314.4(c)(1)(i) | 9 of 60 sampled adjunct separations disabled 8 to 43 days late; help desk resets MFA on knowledge-based questions | Adjunct automation (POAM-001); verified MFA resets (POAM-013) | Director of Identity and Access Management | 2026-12-31 |
| G-017 | 16 CFR 314.4(c)(5) | Student accounts can reach customer information without MFA; no written Qualified Individual approval of equivalent controls | Required student MFA and step-up MFA for bank changes (POAM-002) | Vice President, Student Finance | 2026-12-15 |
| G-031 | 16 CFR 314.4(f)(2) | 19 legacy contracts lack Safeguards Rule terms; the Title IV third-party servicer may take 10 days to report incidents | Amend legacy contracts (POAM-005) and the servicer contract (POAM-020) | Director of Third-Party Risk Management | 2027-03-31 |
| G-038 | 16 CFR 314.4(h)(4) | Materiality playbook omits Title IV consequences; external communications not exercised with current decision makers | Update playbook; tabletop 2026-11-12 (POAM-011) | General Counsel | 2026-11-30 |
| G-057 | 34 CFR 668.16(c)(1) | Open High gaps could be cited in the compliance audit as an internal control weakness | Close High gaps before fiscal 2026 audit fieldwork | Chief Compliance Officer | 2027-01-31 |
| G-059 | HEA section 483 | ISIR-derived fields in 5 of 17 data platform data sets, used in AI-003 and marketing analytics | Remove, purge, and register approved uses (POAM-004) | Chief Data and Analytics Officer | 2026-11-30 |
| G-060 | 34 CFR 668.16(g)(1) | 6 of 40 sampled flagged online applications were never assessed for referral | Shared fraud signals; written referral criteria; identity verification before first disbursement (POAM-023) | Vice President, Financial Aid | 2027-03-31 |
| G-063 | Form 8-K Item 1.05 | Process untested with current members; education-specific impacts missing | POAM-011 | General Counsel | 2026-11-30 |
| G-064 | Form 8-K Item 1.05 (materiality determination) | Escalation timelines never tested end to end | POAM-011 | General Counsel | 2026-11-30 |

## 5. Compliance roadmap
| Quarter | Milestones | Regulations served | Evidence produced |
|---|---|---|---|
| 2026 Q4 | Scanner credentials and inventory (POAM-012); remove ISIR-derived fields (POAM-004); disclosure committee tabletop with the FSA and FTC steps (POAM-011); required student MFA and bank-change controls (POAM-002); verified MFA resets and adjunct automation (POAM-013, POAM-001); servicer contract amendment (POAM-020); FERPA notice and SL-1 consent cleanup (POAM-021); SAIG isolation (POAM-016); AI committee reviews and AI-002 fairness test (POAM-019) | 314.4(c)(1), (c)(2), (c)(5), (f)(2), (h)(4); HEA section 483; 99.7(a), 99.30(a); Item 1.05 | Configuration exports; purge certificates; tabletop report; signed amendments; updated notice |
| 2027 Q1 | Enrollment advisor role redesign (POAM-003); SIS DR retest (POAM-006); legacy vendor reviews and amendments (POAM-005); identity verification for first-time online students (POAM-023); emergency notification IT outage scenario (POAM-024); detection content for bulk exports (POAM-015); Internal Audit test of Item 106 statements | 314.4(c)(1)(ii), (c)(8), (f)(3), (h); 99.31(a)(1)(ii); 668.16(g); 668.46(g) | Role reports; DR test report; vendor review files; referral log; test records |
| 2027 Q2 | Imaging system retired (POAM-008); first disposal run under the approved records schedule (POAM-010); LMS contract RTO amendment and observed failover (POAM-007) | 314.4(c)(1), (c)(6); Fla. Stat. 501.171(8) | Decommission record; disposal certificates; amended contract |
| 2027 Q3 | Annual risk assessment and gap reassessment; Qualified Individual's 2027 report; review CIRCIA, Colorado, and California status | All | Updated P01 and P03; board report |

## 6. Pending regulatory changes
- **16 CFR Part 314:** no pending FTC amendment was identified. The most recent change added the 314.4(j) FTC notice.
- **CIRCIA (N61-R06)** is **still proposed**. The proposed rule (89 FR 23644, Apr. 4, 2024) would cover every institution of higher education that participates in Title IV and would require reports to CISA within 72 hours of a covered cyber incident and within 24 hours of a ransom payment. It is flagged in the `pending_rule_change` column and is **not** treated as a current obligation.
- **Colorado SB26-189** (signed 2026-05-14) applies to consequential decisions made on or after 2027-01-01, including education; attorney general rules are due by that date. **California CPPA ADMT rules** require compliance by 2027-01-01 for businesses using ADMT for significant decisions, including education; counsel is confirming how the CCPA's exemptions apply to the College's GLBA and FERPA data. Readiness for both is in P10 and POAM-019.
- **FSA and NIST SP 800-171:** FSA has encouraged institutions to incorporate SP 800-171 controls (Electronic Announcements of Dec. 18, 2020 and GENERAL-23-09) but states that the current requirement is the Safeguards Rule. Tracked as guidance.
- **SEC:** a 2025 petition asks the SEC to rescind Item 1.05. No SEC proposal to amend or rescind was found as of 2026-09-25, so Item 1.05 and Item 106 remain in force.

## 7. Regulator-ready package
FSA resolves GLBA findings as part of its administrative capability determination; where no breach has occurred, an institution found out of compliance must provide a corrective action plan with timeframes, and repeated noncompliance may lead to administrative action (GENERAL-23-09). The GRC team therefore keeps an evidence binder in the GRC platform, indexed by `req_id`, so the company can respond quickly to the compliance auditor, an FSA program review, an FTC inquiry, a state attorney general, or an SEC comment letter:
- this report, `gap-analysis.csv`, and the sample selections with exceptions for every sampled row;
- the Qualified Individual's written reports to the board (2024, 2025, 2026);
- the P01 risk assessment, P02 SSP, P05 BIA, P06 policy set, P07 assessment and POA&M, and P08 runbook;
- vendor contracts and SOC report reviews for the 260 vendors with student data;
- the FERPA annual notice, disclosure records, and consent records;
- the OIG referral log and fraud procedures;
- records retained at least as long as the Title IV retention periods (34 CFR 668.24(e)) and the company's 7-year security record standard (POL-01 4.11).

## 8. Approval
Approved by the Chief Compliance Officer and the CISO on 2026-08-21. The roadmap was reviewed by the board risk committee on 2026-09-10 and is part of the Qualified Individual's annual written report. Next reassessment: 2027-06 to 2027-07.
