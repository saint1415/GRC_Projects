# Regulatory Gap Analysis: Cris Santos Company | Professional, Scientific, and Technical Services | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (CPA and tax preparation firm) |
| Tier / Vertical | Small / Professional, Scientific, and Technical Services |
| Regulation analyzed | FTC Standards for Safeguarding Customer Information (Safeguards Rule), 16 CFR Part 314 (N54-R01). Text read from eCFR, current through 2026-09-23 |
| Secondary regulation | IRC 7216 and 26 CFR 301.7216-1 to -3 (N54-R02), with the IRS e-file provider and PTIN requirements that apply to the firm (N54-R03) |
| Assessment dates | 2026-07-13 to 2026-07-24 |
| Assessor | IT Manager (Qualified Individual) with the Risk and Quality Partner and the Tax Partner |

## 1. Applicability

### 1.1 FTC Safeguards Rule: applies in full
- **The firm is a financial institution under the rule.** 16 CFR 314.2(h)(2)(viii) gives this example: "An accountant or other tax preparation service that is in the business of completing income tax returns is a financial institution because tax preparation services is a financial activity listed in 12 CFR 225.28(b)(6)(vi)." 314.1(b) also lists "tax preparation firms" among the entities the rule covers.
- **Its individual tax clients are customers.** Under 314.2(e)(2)(i)(H), a consumer has a continuing customer relationship when he or she "becomes your client for the purpose of obtaining tax preparation" services. Customer information is any record of nonpublic personal information about a customer, in any form (314.2(d)). The rule applies to all customer information in the firm's possession (314.1(b)).
- **Business clients are outside the definition, but their owners are not.** Corporations, partnerships, and trusts are not "consumers" (314.2(b)(1) covers individuals obtaining services for personal, family, or household purposes). Business return files still hold owners' and employees' personal data, so the firm protects them under the same program and under IRC 7216.
- **The small-institution exception does not apply.** Section 314.6 says that 314.4(b)(1) (written risk assessment), (d)(2) (continuous monitoring or annual penetration testing and six-month vulnerability assessments), (h) (written incident response plan), and (i) (annual written report to the board) "do not apply to financial institutions that maintain customer information concerning fewer than five thousand consumers." The firm prepares returns for about 7,400 individual consumers a year. Because it has never disposed of old files, it maintains customer information on about 21,000 consumers. **No element is exempt.** Even if a future disposal program (314.4(c)(6)) cut the count, current clients alone exceed 5,000.
- **The FTC notification duty is in force.** 314.4(j) took effect on 2024-05-13 (314.5). It applies to notification events involving at least 500 consumers.

### 1.2 IRC 7216: applies (secondary regulation)
Under 301.7216-1(b)(2), the firm is a tax return preparer, and so is every employee who helps prepare returns, including the scanning and data entry staff. Contractors that receive tax return information to service the firm's software or equipment also become tax return preparers (301.7216-2(d)(2)). Tax return information includes everything furnished "in connection with" preparing a return, and it includes information the preparer derives from it (301.7216-1(b)(3)). The regulations and GLBA apply side by side; neither overrides the other (301.7216-1(c)).

The IRS has not issued guidance specific to artificial intelligence under section 7216. The IRS Section 7216 Information Center, checked 2026-09-25, lists guidance only through Rev. Proc. 2013-14 and 2013-19. The AI rows below therefore apply the regulation text directly, and counsel will confirm them (see P10).

### 1.3 IRS program requirements that apply
- **Pub. 1345 (Rev. 12-2025).** The firm is an Authorized IRS e-file Provider acting as an ERO. Of the six security, privacy, and business standards, five apply only to Online Providers. The sixth, "Reporting of Security Incidents," now applies to all Providers: report security incidents to the IRS "as soon as possible but not later than the next business day after confirmation," and EROs do so through their local Stakeholder Liaison.
- **Form W-12 (Rev. 10-2025), line 11.** Every PTIN applicant or renewer must answer whether they are aware that paid preparers "are required by law to create and maintain a written information security plan." **Form 8879** (Rev. January 2021) has no data security attestation; its duties are signature and retention.
- **Pubs. 4557 (Rev. 6-2024) and 5708 (Rev. 8-2024)** are guidance. They explain the Safeguards Rule for tax professionals and give a WISP template. The legal duty comes from 16 CFR 314. Pub. 4557's recommendations are rated only where the firm adopted them.

### 1.4 Considered and excluded
- HIPAA as a business associate (N54-R06), FAR and DFARS with CMMC (N54-R04, N54-R05), and ABA Model Rules (N54-R07): not applicable (scenario facts section 1).
- 314.4(a)(1)-(3) (Qualified Individual provided by a service provider): not applicable, because the Qualified Individual is a firm employee.
- The AICPA confidentiality rule (N54-R08): a professional standard, not verified from its source for this analysis.

## 2. Method
1. **Requirements.** Each paragraph of 314.3 and 314.4 became one row, split to the lowest lettered or numbered level that states its own duty. 314.4(h)(1)-(7) got one row each because the plan must address all seven areas. The 314.6 exception is a row, to record the applicability decision. For IRC 7216, each permission or condition that governs how the firm shares data (inside the firm, with other preparers, with contractors, and by consent) became a row. IRS program duties are typed separately from regulations, and Pub. 4557 guidance is typed "not binding."
2. **Crosswalk.** Each row was mapped to CSF 2.0 subcategories and SP 800-53 Rev. 5 controls. This is an **author mapping**: no official NIST mapping of 16 CFR 314 or 26 CFR 301.7216 was found.
3. **Evidence.** Current state came from interviews (Managing Partner, Firm Administrator, Tax Partner, Risk and Quality Partner, IT Manager, Client Services Supervisor, the MSP account lead, and 10 staff chosen at random), policy and contract review, system exports, a sample of 25 lender releases for consent timing, and a walkthrough of both offices on 2026-08-05.
4. **Status.** Each row was rated Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| 314.3 Program and objectives | 0 | 2 | 0 | 0 |
| 314.4(a) Qualified Individual | 1 | 0 | 0 | 1 |
| 314.4(b) Risk assessment | 3 | 2 | 0 | 0 |
| 314.4(c) Safeguards | 0 | 7 | 3 | 0 |
| 314.4(d) Testing and monitoring | 0 | 1 | 3 | 0 |
| 314.4(e) Personnel and training | 1 | 3 | 0 | 0 |
| 314.4(f) Service providers | 0 | 2 | 1 | 0 |
| 314.4(g) Evaluate and adjust | 0 | 1 | 0 | 0 |
| 314.4(h) Incident response plan | 4 | 4 | 0 | 0 |
| 314.4(i) Report to governing body | 0 | 0 | 1 | 0 |
| 314.4(j) FTC notification | 0 | 1 | 0 | 0 |
| 314.6 Exception | 0 | 0 | 0 | 1 |
| **Safeguards Rule subtotal (42)** | **9** | **23** | **8** | **2** |
| 26 CFR 301.7216 (9) | 2 | 6 | 1 | 0 |
| IRS e-file and PTIN requirements (5) | 2 | 3 | 0 | 0 |
| **Total (56)** | **13** | **32** | **9** | **2** |

Of the 41 unmet or partially met rows, 7 are rated High, 23 Moderate, and 11 Low.

The Met rows in 314.4(b)(1) and 314.4(h) reflect documents approved on 2026-08-31 as a result of this work. Before this assessment the firm had no written risk assessment and no incident response plan.

## 4. Priority gaps and roadmap
| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| No penetration test; no vulnerability scan in 16 months; no continuous monitoring | 314.4(d)(2), (d)(2)(i), (d)(2)(ii) | High | Monthly scans from 2026-11; annual penetration test starting 2026-11 | IT Manager | 2026-11-30 |
| MFA gaps: legacy authentication, optional client MFA, push fatigue | 314.4(c)(5) | High | Block legacy authentication; number matching; mandatory client MFA | IT Manager | 2026-11-30 (client MFA 2027-01-15) |
| No monitoring of authorized user activity | 314.4(c)(8) | High | Log workspace with alerts; monthly review | IT Manager | 2026-12-31 |
| Need-to-know access and standing admin rights | 314.4(c)(1)(ii) | High | Team-based DMS permissions; separate admin accounts | IT Manager | 2026-12-31 |
| Five High risks open | 314.3(b) | High | Execute funded Q4 treatments (P01) | IT Manager | 2027-01-15 |
| No report to the Partner Group | 314.4(i) | Moderate | First written report | IT Manager | 2026-10-20 |
| No disposal schedule; files since 2009 | 314.4(c)(6) | Moderate | Retention schedule and first purge | Risk and Quality Partner | 2027-06-30 |
| Contractor access without the 7216 written notice | 301.7216-2(d)(2) | Moderate | Written 6713/7216 notice; limit MSP access | Firm Administrator | 2026-10-31 |
| AI features without a 7216 basis or U.S.-processing assurance | 301.7216-2(d)(1), -3(a)(1), -3(b)(4) | Moderate | Contract terms and consent decisions (P10) | Tax Partner | 2026-10-31 |
| Next-business-day IRS report unknown to the Responsible Official | Pub. 1345 | Moderate | Tabletop covering the Stakeholder Liaison call | Tax Partner | 2026-12-15 |

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07).

**Timing.** The filing season starts in mid-January and is when phishing against tax firms peaks (IRS Pub. 4557). Every High gap is due by 2027-01-15.

## 5. Pending regulatory changes
- **FTC Safeguards Rule.** The Federal Register shows no pending proposal to amend 16 CFR Part 314 as of 2026-09-25. The last change was the 2023 notification amendment (88 FR 77508, effective 2024-05-13).
- **IRC 7216 regulations.** No pending Treasury proposal was found. The last amendment was published 2012-12-28. There is no AI-specific IRS guidance (section 1.2).
- **CIRCIA (N54-R09).** Proposed only (89 FR 23644). The firm would likely fall outside the proposed size criterion, because it is below its SBA size standard. It is not treated as an obligation.

The `pending_rule_change` column records "None known" for each row on this basis.
