# Regulatory Gap Analysis: Cris Santos Company | Professional, Scientific, and Technical Services | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (CPA and tax preparation firm) |
| Tier / Vertical | Micro / Professional, Scientific, and Technical Services |
| Regulation analyzed | FTC Standards for Safeguarding Customer Information (Safeguards Rule), 16 CFR Part 314 (N54-R01). Text read from eCFR, current through 2026-09-23 |
| Secondary regulation | IRC 7216 and 26 CFR 301.7216-1 to -3 (N54-R02), with the IRS e-file provider and PTIN requirements that apply to the firm (N54-R03) |
| Assessment dates | 2026-07-06 to 2026-07-17 |
| Assessor | Office Manager (Qualified Individual) with the MSP lead technician; the Owner CPA answered for the tax practice |
| Approved | 2026-08-31 by the Owner CPA |

## 1. Applicability

### 1.1 FTC Safeguards Rule: applies, with the small-institution exception
- **The firm is a financial institution under the rule.** 16 CFR 314.2(h)(2)(viii): "An accountant or other tax preparation service that is in the business of completing income tax returns is a financial institution because tax preparation services is a financial activity listed in 12 CFR 225.28(b)(6)(vi)." 314.1(b) also lists "tax preparation firms" among the covered entities. There is no size threshold for coverage.
- **Its individual tax clients are customers.** A consumer has a continuing customer relationship when he or she "becomes your client for the purpose of obtaining tax preparation" services (314.2(e)(2)(i)(H)). Business clients are not consumers (314.2(b)(1) covers individuals obtaining services for personal, family, or household purposes), and neither are the employees of payroll clients. The firm still protects their data under the same program, IRC 7216, and Florida law.
- **The 314.6 exception applies.** Section 314.6: "Section 314.4(b)(1), (d)(2), (h), and (i) do not apply to financial institutions that maintain customer information concerning fewer than five thousand consumers." On 2026-07-08 the Office Manager counted about 3,300 consumers: about 1,400 current individual clients and about 1,900 former clients whose folders are still kept. Even if the 420 employees of payroll clients were added, the total (about 3,700) stays under 5,000. Four elements are therefore exempt: the **written** risk assessment criteria (314.4(b)(1)), continuous monitoring or annual penetration testing with six-month vulnerability assessments (314.4(d)(2)), the written incident response plan (314.4(h)), and the Qualified Individual's annual written report (314.4(i)).
- **What the exception does not remove.** The written information security program itself (314.3(a)), the Qualified Individual (314.4(a)), a risk assessment that the program is based on (314.4(b)) and periodic reassessment ((b)(2)), every safeguard in 314.4(c), regular testing or monitoring of key controls (314.4(d)(1)), training, service provider oversight, program adjustment, and **FTC notification of events involving 500 or more consumers (314.4(j))** all apply in full.
- **The firm chose to do some exempt work anyway.** The P01 risk assessment uses written criteria, and the P08 runbook is a written incident response plan, because IRS Pub. 1345 requires next-business-day incident reporting and BEC is the firm's top risk. The exempt rows are marked Not applicable in `gap-analysis.csv`, with the voluntary work noted.
- **Watch the count.** About 1,900 former clients make up more than half of the count. A disposal schedule (314.4(c)(6)) would lower it, but buying a retiring preparer's client list would raise it. Row G-042 adds a yearly recount.

### 1.2 IRC 7216: applies (secondary regulation)
Under 301.7216-1(b)(2), the firm is a tax return preparer, and so is every employee who helps prepare returns, including the Client Services Coordinator and the seasonal assistant. Contractors that receive tax return information to service the firm's equipment or software also become tax return preparers (301.7216-2(d)(2)). As an accountancy firm, it may use a client's return information to prepare that client's books and payroll records (301.7216-2(h)(1)), which covers the Bookkeeper's work.

The IRS has issued no AI-specific guidance under section 7216 (checked on the IRS Section 7216 Information Center, 2026-09-25). The AI rows below therefore apply the regulation text directly, and counsel will confirm them (P10).

### 1.3 IRS program requirements that apply
- **Pub. 1345 (Rev. 12-2025).** The firm is an Authorized IRS e-file Provider acting as an ERO. The "Reporting of Security Incidents" standard applies to all Providers: report security incidents to the IRS "as soon as possible but not later than the next business day after confirmation of the incident"; EROs contact their local Stakeholder Liaison. Pub. 1345 also sets the Form 8879 retention period and the e-signature identity check.
- **Form W-12 (Rev. 10-2025), line 11.** PTIN applicants and renewers acknowledge that paid preparers are required by law to create and maintain a written information security plan.
- **Pubs. 4557 and 5708** are guidance. They explain the Safeguards Rule for tax professionals and give the WISP template the firm used in 2024. Pub. 4557 recommendations are rated only where the firm adopted them.

### 1.4 Considered and excluded
- HIPAA as a business associate (N54-R06), FAR and DFARS with CMMC (N54-R04, N54-R05), and the ABA Model Rules (N54-R07): not applicable (scenario facts section 1).
- 314.4(a)(1)-(3) (Qualified Individual provided by a service provider): not applicable, because the Qualified Individual is a firm employee.
- The AICPA confidentiality rule (N54-R08): a professional standard, not verified from its source for this analysis.

## 2. Method
1. **Requirements.** Each paragraph of 314.3 and 314.4 became one row, split to the lowest lettered or numbered level that states its own duty, so that the 314.6 exemptions show up row by row. The 314.6 exception is a row, to record the count and the monitoring duty. For IRC 7216, each permission or condition that governs how the firm shares data (inside the firm, with other preparers, with contractors, for bookkeeping, and by consent) became a row. IRS program duties are typed separately, and Pub. 4557 guidance is typed "not binding."
2. **Crosswalk.** Each row was mapped to CSF 2.0 subcategories and SP 800-53 Rev. 5 controls. This is an **author mapping**: no official NIST mapping of 16 CFR 314 or 26 CFR 301.7216 was found.
3. **Documentary evidence.** Each status rests on a named document or record: the 2024 WISP, the designation memo, the tax software and suite user lists and settings, the portal settings, the MSP device list, patch report, and contract, the cloud storage folder listing, the consumer count, 15 sent emails with returns, the 12 lender-release consent files from 2026, PTIN renewal records, and a walkthrough on 2026-07-09. Interviews covered all 7 employees and the MSP lead technician.
4. **Status.** Each row was rated Met, Partially met, Not met, or Not applicable **as of the end of fieldwork (2026-07-17)**. Actions completed since then (for example, blocking external forwarding on 2026-07-20 and approving the policies on 2026-08-31) are noted but do not change the status. Gap risk uses the P01 scale.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| 314.3 Program and objectives | 0 | 2 | 0 | 0 |
| 314.4(a) Qualified Individual | 1 | 0 | 0 | 1 |
| 314.4(b) Risk assessment | 0 | 1 | 1 | 3 |
| 314.4(c) Safeguards | 0 | 4 | 6 | 0 |
| 314.4(d) Testing and monitoring | 0 | 0 | 1 | 3 |
| 314.4(e) Personnel and training | 0 | 2 | 2 | 0 |
| 314.4(f) Service providers | 0 | 1 | 2 | 0 |
| 314.4(g) Evaluate and adjust | 0 | 0 | 1 | 0 |
| 314.4(h) Incident response plan | 0 | 0 | 0 | 8 |
| 314.4(i) Report to governing body | 0 | 0 | 0 | 1 |
| 314.4(j) FTC notification | 0 | 0 | 1 | 0 |
| 314.6 Exception | 0 | 1 | 0 | 0 |
| **Safeguards Rule subtotal (42)** | **1** | **11** | **14** | **16** |
| 26 CFR 301.7216 (9) | 3 | 5 | 1 | 0 |
| IRS e-file and PTIN requirements (5) | 2 | 1 | 2 | 0 |
| **Total (56)** | **6** | **17** | **17** | **16** |

Of the 34 unmet or partially met rows, 4 are rated High, 19 Moderate, and 11 Low. Fifteen of the 16 Not applicable rows come from the 314.6 exception; the sixteenth is 314.4(a)(1)-(3).

**What the numbers say.** The firm met only one Safeguards Rule element at the end of fieldwork, the Qualified Individual designation made at the start of this work. The firm had a WISP on paper, but no element of it was operating. The SaaS vendors carry the strongest controls (encryption at rest, MFA on the tax software). The weak spots are on the firm's side: email, access removal, monitoring, disposal, and vendor oversight. The 314.6 exception removes the four most expensive elements; it does not remove the safeguards that stop a BEC attack.

## 4. Priority gaps
| Gap | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|
| No monitoring or alerting on user activity | 314.4(c)(8) | High | Suite alert policies; one year of logs; monthly review | Office Manager | 2026-10-31 |
| MFA weaknesses (push approval, MSP-held logins, optional client MFA) | 314.4(c)(5) | High | Number matching; MFA on MSP-held logins; mandatory client MFA | Office Manager | 2027-01-15 |
| Plain email attachments; unencrypted desktops and MFP drive | 314.4(c)(3) | High | Portal-only delivery; desktop encryption; MFP image overwrite | Office Manager | 2026-12-31 |
| Three High risks open | 314.3(b) | High | Execute the funded Q4 treatments (P01) | Office Manager | 2027-01-15 |
| FTC notice and IRS next-business-day report unknown | 314.4(j); Pub. 1345 | Moderate | P08 notification matrix; tabletop | Office Manager; Owner CPA | 2026-12-15 |
| AI uploads without an IRC 7216 basis | 301.7216-1(a); -3(a)(1); -3(b)(4) | Moderate | No client-identifying content in AI tools; deletion request; counsel review (P10) | Senior Tax Accountant | 2026-09-30 |
| MSP access without the 7216 written notice; no MSP security terms | 301.7216-2(d)(2); 314.4(f)(2) | Moderate | Written notice; contract amendment | Office Manager; Owner CPA | 2026-10-31; 2026-12-31 |
| No disposal schedule; files since 2016 | 314.4(c)(6) | Moderate | Retention schedule and first purge | Owner CPA | 2027-06-30 |
| No current training | 314.4(e)(1) | Moderate | Training before the season; phishing simulations | Office Manager | 2026-12-15 |
| No inventory; no change procedure | 314.4(c)(2), (c)(7) | Moderate | One-page inventory; change log with approval | Office Manager | 2026-10-31 |

The full list, with evidence, is in `gap-analysis.csv`. Every High and Moderate gap is carried into the risk register (P01) and, where the control was assessed, the POA&M (P07).

## 5. Remediation plan
The plan fits a 7-person firm: most actions are one-page procedures or MSP settings, not new systems. The MSP performs the technical work under the Office Manager's direction. Costs are in the P01 treatment summary. Everything that protects the 2027 filing season is due by 2027-01-15, because phishing against tax professionals peaks in the season (IRS Pub. 4557).

| Phase | Due | Actions | Rows closed |
|---|---|---|---|
| 1. Program, contracts, and AI | 2026-09-30 | Publish the written program (P06 policies and index); approved-tools rule and AI deletion request; termination checklist; MFA on MSP-held logins; first full restore test | G-001, G-043, G-048, G-051 |
| 2. Visibility and hardening | 2026-10-31 | Inventory; change log; separate administrator accounts and folder limits; suite alerts and one year of logs; pre-adoption checklist; written 7216 notice to contractors | G-005, G-010, G-011, G-012, G-014, G-018, G-019, G-046 |
| 3. Before the season | 2026-12-31 | Training and phishing simulations; tabletop covering the IRS and FTC steps; desktop encryption and portal-only delivery; vendor inventory, MSP contract amendment, and first vendor reviews; EDR; PTIN briefing | G-013, G-020, G-024, G-025, G-026, G-028, G-029, G-030, G-031, G-041, G-045, G-049, G-052, G-055 |
| 4. Filing season start | 2027-01-15 | Mandatory client portal MFA; number matching confirmed; weekly EFIN and PTIN checks | G-002, G-015, G-056 |
| 5. Annual cycle | 2027-03-31 to 2027-07-31 | Personnel knowledge check; retention schedule and first purge; consumer recount and risk reassessment (July) | G-009, G-016, G-017, G-027, G-042 |

**Progress check.** The Office Manager reports progress to the Owner CPA at a monthly 30-minute meeting, using the P07 POA&M as the tracker. That meeting is also the light, voluntary version of the 314.4(i) report.

## 6. Pending regulatory changes
- **FTC Safeguards Rule.** The Federal Register shows no pending proposal to amend 16 CFR Part 314 as of 2026-09-25. The last change was the 2023 notification amendment (88 FR 77508), effective 2024-05-13 (314.5). The 314.6 threshold of 5,000 consumers is unchanged since the 2021 amendments (86 FR 70308).
- **IRC 7216 regulations.** No pending Treasury proposal was found. There is no AI-specific IRS guidance (section 1.2).
- **CIRCIA (N54-R09).** Proposed only (89 FR 23644). The firm is below its SBA size standard, the proposed size criterion, so it would likely fall outside the rule. It is not treated as an obligation.

The `pending_rule_change` column records "None known" for each row on this basis.
