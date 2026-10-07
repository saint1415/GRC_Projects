# Regulatory Gap Analysis: Cris Santos Company | Professional, Scientific, and Technical Services | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (CPA and tax preparation practice) |
| Tier / Vertical | Sole Proprietorship / Professional, Scientific, and Technical Services |
| Regulation analyzed | **FTC Safeguards Rule, 16 CFR Part 314** (N54-R01). Text read from eCFR, current through 2026-09-23 (last amended 88 FR 77508, 2023-11-13) |
| Also checked | IRC 7216 and 26 CFR 301.7216-1 to -3 (N54-R02); IRS e-file and PTIN duties and Pub. 4557 guidance (N54-R03); Fla. Stat. 501.171(2), (3), (4), (8) |
| Assessment dates | 2026-07-27 to 2026-07-31 (self-assessment; gap analysis 2026-07-30) |
| Assessor | CPA-owner, with the on-call IT consultant (services agreement and IRC 7216 notice since 2026-07-23). Evidence is self-attested, checked on screen where possible |
| Adopted | 2026-08-31 |

## 1. Applicability
**The Safeguards Rule applies, with four paragraphs exempt.**
- **The practice is a financial institution.** 16 CFR 314.2(h)(2)(viii): "An accountant or other tax preparation service that is in the business of completing income tax returns is a financial institution because tax preparation services is a financial activity listed in 12 CFR 225.28(b)(6)(vi)." 314.1(b) also names "tax preparation firms". Being a one-person sole proprietorship changes nothing here.
- **Its individual clients are customers.** A consumer who "becomes your client for the purpose of obtaining tax preparation" services has a continuing customer relationship (314.2(e)(2)(i)(H)). Business clients are not consumers (314.2(b)(1)), but their owners usually are individual clients too, and their files hold employees' data, so the owner protects all client files the same way.
- **The 314.6 exception applies.** Section 314.6 says that 314.4(b)(1), (d)(2), (h), and (i) "do not apply to financial institutions that maintain customer information concerning fewer than five thousand consumers." The practice holds customer information on about 1,450 consumers (current and former clients since 2014). So the written risk assessment, the penetration testing and vulnerability assessments, the written incident response plan, and the annual written report are **not required**. Every other element of 314.3 and 314.4 applies, and 314.3(a) still requires a written program "appropriate to your size and complexity".
- **The FTC notice duty applies.** 314.4(j) is not in the 314.6 list. It applies to notification events involving at least 500 consumers; the owner's mailbox alone holds documents on more than 500.
- **The owner keeps two exempt items anyway.** The written risk assessment (P01) and the incident runbook (P08) are kept because the FTC 30-day notice, the IRS next-business-day report, and Florida's 30-day notice cannot be met without them.

**IRC 7216 applies (rows G-036 to G-042).** The owner is a tax return preparer (301.7216-1(b)(2)(i)(A)). Tax return information is anything furnished in connection with preparing a return, including what the preparer derives from it (301.7216-1(b)(3)). The regulations and GLBA apply side by side; neither overrides the other (301.7216-1(c)). The IRS has issued no AI-specific guidance under section 7216 (the IRS Section 7216 Information Center, checked 2026-09-26, lists guidance only through Rev. Procs. 2013-14 and 2013-19 and does not mention AI), so the AI rows apply the regulation text, and counsel will confirm them (P10).

**IRS program duties (rows G-043 to G-047).** As an ERO the owner must report security incidents to the IRS "as soon as possible but not later than the next business day after confirmation" through the local Stakeholder Liaison (Pub. 1345, Rev. 12-2025). Form W-12 (Rev. 10-2025) line 11 asks each PTIN renewer to confirm awareness that paid preparers "are required by law to create and maintain a written information security plan". Pubs. 4557 and 5708 are guidance; the legal duty comes from 16 CFR 314.

**Florida (rows G-048 to G-050).** A sole proprietorship that holds personal information is a covered entity under Fla. Stat. 501.171(1)(b), so the data security, notice, and disposal duties apply.

**Excluded, with reasons (7 rows):** 314.4(a)(1) to (a)(3) apply only when the Qualified Individual works for a service provider or affiliate (the owner is the Qualified Individual); 314.4(b)(1), (d)(2), (h), and (i) are exempt under 314.6. HIPAA, FAR and DFARS, ABA rules, and CIRCIA are out of scope (`../00_company-facts.md` section 1).

## 2. Method
1. **Requirements.** Each paragraph of 16 CFR 314.3 and 314.4 is one row, using the rule's own numbering, with 314.4(c)(1) and (c)(6) split into their numbered parts (35 rows). Seven IRC 7216 rows cover the permissions and conditions that govern how the owner shares client data. Five IRS rows and three Florida rows follow. 50 rows in total.
2. **Crosswalk.** CSF 2.0 and SP 800-53 columns are an **author mapping**; no official NIST mapping of these rules was found.
3. **Evidence.** Self-attested by the owner and checked on screen with the IT consultant: account security pages and sign-in tests (2026-07-29), the tax software user list, the client folders and paper boxes, the contracts folder, portal consent records, and the PTIN renewal records.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale. Rows that depend on documents adopted on 2026-08-31 (POL-01, P08) are rated Partially met until those documents are used or tested.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| 314.3 Program and objectives | 0 | 4 | 0 | 0 |
| 314.4(a)-(b) Qualified Individual and risk assessment | 1 | 1 | 1 | 4 |
| 314.4(c) Safeguards | 1 | 5 | 4 | 0 |
| 314.4(d)-(j) Testing, people, providers, adjustment, response, reporting, FTC notice | 0 | 8 | 3 | 3 |
| **Safeguards Rule subtotal (35)** | **2** | **18** | **8** | **7** |
| 26 CFR 301.7216 (7) | 3 | 4 | 0 | 0 |
| IRS e-file, PTIN, and Pub. 4557 (5) | 2 | 2 | 1 | 0 |
| Fla. Stat. 501.171 (3) | 0 | 3 | 0 | 0 |
| **Total (50)** | **7** | **27** | **9** | **7** |

Of the 36 unmet or partially met rows, 2 are rated High, 18 Moderate, and 16 Low. The two High rows are 314.3(b)(3) (protection against access that could cause customers substantial harm, which is where refund diversion sits) and 314.4(c)(5) (MFA).

## 4. Action list (half page)
In order. The first four cost nothing and take under a day.

| # | Action | Citation | Gap risk | Target |
|---|---|---|---|---|
| 1 | Scan-to-folder; then MFA on the mailbox and practice management; password manager | 314.4(c)(5); 314.4(c)(1)(i) | High | 2026-09-15 |
| 2 | Adopt POL-01 as the WISP; designate the Qualified Individual | 314.3(a); 314.4(a); Form W-12 line 11 | Moderate | 2026-08-31 (done) |
| 3 | Call-back rule for any bank account, address, or email change; tell clients before filing season | 314.3(b)(3) | High | 2026-12-15 |
| 4 | No client data in the AI assistant; counsel reviews past uploads | 301.7216-1(a); 301.7216-3(a)(1) | Moderate | 2026-10-31 |
| 5 | Monthly review of mailbox sign-ins and rules and the tax software activity log; quarterly user review | 314.4(c)(8); 314.4(c)(1)(i) | Moderate | 2026-10-31 |
| 6 | Vendor list, pre-adoption checklist, practice management terms review | 314.4(c)(4); 314.4(f) | Moderate | 2026-10-31 |
| 7 | Record the IRS Stakeholder Liaison number; walk through the P08 runbook | Pub. 1345; 314.4(j); Fla. Stat. 501.171(3)-(4) | Moderate | 2026-11-30 |
| 8 | Security course with phishing and business email compromise modules | 314.4(e)(1) | Moderate | 2026-11-30 |
| 9 | Portal-only exchange of returns and documents; required client portal MFA; phone photo cleanup | 314.4(c)(3); 314.4(c)(2) | Moderate | 2027-01-15 |
| 10 | Retention schedule (Forms 8879 at least 3 years); first purge; withdraw old IRS authorizations | 314.4(c)(6); Fla. Stat. 501.171(8); Pub. 4557 | Moderate | 2027-06-30 |

High and Moderate gaps are in the risk register (P01) and the POA&M (P07).

## 5. Pending changes and triggers to watch
- **No proposed amendment to 16 CFR Part 314** was found in the Federal Register as of 2026-09-25. The last change was the FTC notification requirement (314.4(j), effective 2024-05-13 under 314.5).
- **No pending Treasury proposal on 26 CFR 301.7216** was found as of 2026-09-25, and no AI-specific IRS guidance.
- **Consumer count trigger.** If customer information reaches 5,000 consumers, rows G-010, G-023, G-032, and G-033 become mandatory. Disposing of old files (action 10) keeps the count well below the line; growth in clients would not reach it soon.
- **CIRCIA (N54-R09)** is proposed only (89 FR 23644). The practice is far below its SBA size standard, the proposed size criterion. It is not treated as an obligation.
