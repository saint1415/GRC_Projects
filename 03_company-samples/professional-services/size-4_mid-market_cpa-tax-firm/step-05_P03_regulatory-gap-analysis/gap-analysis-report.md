# Regulatory Gap Analysis: Cris Santos Company | Professional, Scientific, and Technical Services | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed CPA, tax, and advisory firm, with its attest affiliate) |
| Tier / Vertical | Mid-Market / Professional, Scientific, and Technical Services |
| Primary regulation | FTC Standards for Safeguarding Customer Information (Safeguards Rule), 16 CFR Part 314 (N54-R01). Text read from eCFR, current through 2026-09-23 |
| Other regulations for the primary business line | IRC 7216 and 26 CFR 301.7216-1 to -3 (N54-R02); IRS e-file and PTIN program requirements (N54-R03); Fla. Stat. 501.171(2) and (8) |
| Secondary business line | HIPAA Security Rule (standard level) and 45 CFR 164.410, for the business associate work of the Attest Firm, advisory, and CAS (N54-R06) |
| Assessment dates | 2026-07-06 to 2026-07-31; evidence refreshed with P07 results through 2026-08-21 |
| Assessor | GRC Manager and the Privacy Officer, with the Director of Information Security (Qualified Individual); reviewed by the co-sourced internal audit firm |
| Approved | Chief Operating Officer, 2026-09-22 |

## 1. Applicability
**Primary business line:** individual and business tax preparation, which is about 55% of receipts and the activity that makes the Company a financial institution. CAS and advisory share the same systems and customer information.

| Regulation | Applies? | Basis |
|---|---|---|
| FTC Safeguards Rule, 16 CFR Part 314 | **Yes, in full** | 16 CFR 314.2(h)(2)(viii): "An accountant or other tax preparation service that is in the business of completing income tax returns is a financial institution." Individual tax clients have a customer relationship (314.2(e)(2)(i)(H)). The rule covers all customer information the Company holds (314.1(b)) |
| 314.6 exception | **No** | It removes 314.4(b)(1), (d)(2), (h), and (i) only for institutions with customer information on fewer than 5,000 consumers. The Company holds it on about 205,000 |
| 314.4(j) FTC notification | **Yes** | In force since 2024-05-13 (314.5). Applies to notification events involving at least 500 consumers |
| IRC 7216 and 26 CFR 301.7216-1 to -3 | **Yes** | The Company and every employee who assists in preparing returns are tax return preparers (301.7216-1(b)(2)). The regulations and GLBA apply side by side (301.7216-1(c)). The offshore program brings in the rules on preparers outside the United States (301.7216-2(c)(2), 301.7216-3(a)(3)(i)(D), and 301.7216-3(b)(4)) |
| IRS e-file and PTIN requirements | **Yes** | Authorized IRS e-file Provider (ERO) with 6 EFINs; about 300 PTIN holders. Pub. 1345 (Rev. 12-2025) requires next-business-day reporting of security incidents. Pubs. 4557 and 5708 are guidance; the legal duty comes from 16 CFR 314 |
| Fla. Stat. 501.171(2) and (8) | **Yes** | Reasonable security and disposal duties for personal information of Florida residents. Breach notification is in P08. Other states' security and disposal laws are handled generically, with Florida as the worked example |
| HIPAA Security Rule, as business associate | **Yes, for the ePHI of 44 health care clients** | 45 CFR 164.302 applies the Security Rule to business associates. This line is secondary, so it was analyzed at the **standard level**, with implementation specifications rolled into each standard. A specification-level analysis follows the move of PHI to the restricted enclave (2027 Q2) |
| 45 CFR 164.410 | **Yes** | Business associate notice to the covered entity |

**Considered and excluded:**
- FAR 52.204-21, DFARS 252.204-7012, and CMMC (N54-R04, N54-R05): no federal contracts or subcontracts.
- ABA Model Rules (N54-R07): not a law firm.
- AICPA Code of Professional Conduct (N54-R08), including independence for the alternative practice structure: professional standard, not verified from its source for this analysis.
- PCAOB and SEC: the Attest Firm audits no issuers; the Company is private.
- Florida Digital Bill of Rights: a "controller" must exceed $1 billion in global gross annual revenue and meet one of three business tests (online advertising revenue, a smart speaker service, or an app store). The Company's revenue is $100 million, so it is not a controller.
- 314.4(a)(1)-(3) (Qualified Individual provided by a service provider): the Qualified Individual is a Company employee.
- 164.314(b) (group health plans): the Company acts here only as a business associate.

## 2. Method
1. **Requirements.**
   - Each paragraph of 314.3 and 314.4 is one row, split to the lowest lettered or numbered level that states its own duty. 314.4(h)(1)-(7) got one row each because the plan must address all seven areas. The 314.6 exception is a row, to record the applicability decision.
   - For IRC 7216, each permission or condition that governs how the Company shares data became a row: inside the firm, with other U.S. preparers, with contractors, by consent, and with preparers outside the United States.
   - IRS program duties are typed separately from regulations, and Pub. 4557 guidance is typed "not binding."
   - HIPAA standards use the NIST SP 800-66 Rev. 2 requirement text from the Health Care crosswalk; 164.308(b)(2) and 164.410 were decomposed from the eCFR text.
2. **Crosswalk.** Each row is mapped to CSF 2.0 and SP 800-53 Rev. 5. These are **author mappings**: no official NIST mapping of 16 CFR 314, 26 CFR 301.7216, IRS publications, or the Florida statute was found, and the HIPAA rows use the repository's Health Care crosswalk, itself an author mapping.
3. **Evidence.** Interviews with every process owner, document and contract review, system exports, and walkthroughs at 3 of 6 offices (Office 1 with the document processing center, Office 4, and Office 6).
4. **Evidence sampling.** Where a requirement operates many times, a sample was tested rather than the whole population. Samples were chosen at random from system-generated populations, using the co-sourced internal audit firm's attribute sampling table (25 items for a control that operates many times a year; 10 to 20 for less frequent ones):
   - seasonal accounts: 25 of 131;
   - terminations: 25 of 96;
   - transfers: 25 of 58;
   - offshore returns (consent and masking): 25 of about 5,500;
   - lender and adviser releases (consent timing): 25 of about 1,900;
   - outbound emails with tax attachments: 60 from one March 2026 week;
   - service provider contracts: 20 of 85;
   - BAAs: 15 of 44;
   - e-signed Forms 8879: 25;
   - incidents: 10 of 31;
   - seasonal training records: 25;
   - destruction certificates: 10.
   Each `evidence` cell names the sample and its result.
5. **Status.** Each row was rated Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| 314.3 Program and objectives | 0 | 2 | 0 | 0 | 2 |
| 314.4(a) Qualified Individual | 1 | 0 | 0 | 1 | 2 |
| 314.4(b) Risk assessment | 4 | 1 | 0 | 0 | 5 |
| 314.4(c) Safeguards | 0 | 9 | 1 | 0 | 10 |
| 314.4(d) Testing and monitoring | 1 | 3 | 0 | 0 | 4 |
| 314.4(e) Personnel and training | 2 | 2 | 0 | 0 | 4 |
| 314.4(f) Service providers | 0 | 2 | 1 | 0 | 3 |
| 314.4(g) Evaluate and adjust | 0 | 1 | 0 | 0 | 1 |
| 314.4(h) Incident response plan | 6 | 2 | 0 | 0 | 8 |
| 314.4(i) Report to the board | 0 | 1 | 0 | 0 | 1 |
| 314.4(j) FTC notification | 0 | 1 | 0 | 0 | 1 |
| 314.6 Exception | 0 | 0 | 0 | 1 | 1 |
| **Safeguards Rule subtotal** | **14** | **24** | **2** | **2** | **42** |
| 26 CFR 301.7216 | 2 | 6 | 2 | 0 | 10 |
| IRS e-file and PTIN requirements | 4 | 1 | 0 | 0 | 5 |
| Fla. Stat. 501.171(2) and (8) | 0 | 2 | 0 | 0 | 2 |
| **Primary business line subtotal** | **20** | **33** | **4** | **2** | **59** |
| HIPAA 164.308 Administrative safeguards | 3 | 6 | 0 | 0 | 9 |
| HIPAA 164.310 Physical safeguards | 2 | 2 | 0 | 0 | 4 |
| HIPAA 164.312 Technical safeguards | 2 | 3 | 0 | 0 | 5 |
| HIPAA 164.314 Organizational requirements | 1 | 1 | 0 | 1 | 3 |
| HIPAA 164.316 Policies and documentation | 1 | 1 | 0 | 0 | 2 |
| HIPAA 164.410 Business associate notice | 2 | 1 | 0 | 0 | 3 |
| **HIPAA subtotal** | **11** | **14** | **0** | **1** | **26** |
| **Total** | **31** | **47** | **4** | **3** | **85** |

**Gap risk ratings (51 rows Partially met or Not met):** 9 High, 32 Moderate, 10 Low.

**Reading the results.** The program is defined and the paperwork elements are largely Met: the Qualified Individual, the written risk assessment and its criteria, the incident response plan, and training of security staff. The gaps sit where scale outgrew the program:
- identity and access across a large, seasonal, and partly offshore workforce (314.4(c)(1), (c)(5));
- monitoring inside SaaS applications (314.4(c)(8));
- service providers, with 31 contracts lacking security terms (314.4(f));
- the offshore program and AI features under IRC 7216 (301.7216-3(a)(1), (a)(3)(i)(D), (b)(4));
- disposal of records past retention (314.4(c)(6)).

The four Not met rows are disposal (G-016), periodic service provider assessment (G-030), the contractor notice under 301.7216-2(d)(2) (G-046), and SSN masking for offshore preparers under 301.7216-3(b)(4) (G-050).

## 4. Priority gaps
| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| SSNs visible to offshore preparers in scanned documents (G-050) | 26 CFR 301.7216-3(b)(4) | High | Offshore-only DMS view of masked images; counsel review of the IRS safeguard guidance | Director of Tax Operations | 2026-12-15 |
| Returns routed offshore before consent (G-048) | 301.7216-3(a)(3)(i)(D) | High | Portal workflow gate | Director of Tax Operations | 2026-12-15 |
| AI drafting used without a 7216 basis (G-047) | 301.7216-3(a)(1) | High | Counsel determination before re-enabling (P10) | National Tax Practice Leader | 2026-10-31 |
| Client portal MFA optional; CAS local accounts (G-015) | 314.4(c)(5) | High | Mandatory client MFA; federate CAS services | Director of Information Security | 2027-01-15 |
| No monitoring of SaaS application activity (G-019) | 314.4(c)(8) | High | SIEM onboarding with bulk-download and inbox-rule alerts | Director of Information Security | 2027-01-15 |
| Need-to-know and privileged access (G-011) | 314.4(c)(1)(ii) | High | Team-based DMS permissions; privileged access management | Director of Information Security | 2027-01-15 |
| Late seasonal disables; accounts outside SSO (G-010) | 314.4(c)(1)(i) | High | Automated disable; CAS federation | Chief Information Officer | 2026-12-31 |
| 31 provider contracts without security terms (G-029) | 314.4(f)(2) | High | Contract amendments, Tier 1 first | General Counsel | 2027-03-31 |
| Risk treatment backlog (G-002) | 314.3(b) | High | FY2027 security plan (P01) | Director of Information Security | 2027-03-31 |
| No disposal of records past retention (G-016) | 314.4(c)(6)(i); Fla. Stat. 501.171(8) | Moderate | First disposal run | General Counsel | 2027-06-30 |
| Contractor notice not given (G-046) | 301.7216-2(d)(2) | Moderate | Written 6713 and 7216 notices | General Counsel | 2026-11-30 |
| No periodic vendor assessment (G-030) | 314.4(f)(3) | Moderate | Tiered reviews (P09) | GRC Manager | 2027-03-31 |
| Incomplete 2025 board report (G-040) | 314.4(i) | Moderate | 2026-10-27 report | Director of Information Security | 2026-10-27 |
| PHI not segregated; no ePHI risk analysis (G-060, G-063) | 45 CFR 164.308(a)(1), (a)(4) | Moderate | Move PHI to the enclave; HIPAA risk analysis | Attest Firm Quality and Independence Partner | 2027-03-31 |

High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07). The full list, with evidence, is in `gap-analysis.csv`.

## 5. Program roadmap
| Phase | Window | Outcomes | Gaps closed (examples) |
|---|---|---|---|
| **1. Stabilize** | 2026 Q4 (to 2026-12-15) | Offshore masking and consent gate; AI drafting decision; contractor notices; board report; BEC tabletop with counsel and the Stakeholder Liaison call; privileged accounts separated | G-046, G-047, G-048, G-050, G-040, G-041, G-053 |
| **2. Ready for filing season** | to 2027-01-15 | Mandatory client MFA; security keys for high-risk users; SaaS logs in the SIEM; automated seasonal disables; training gate; CAS federation | G-010, G-011, G-015, G-019, G-024 |
| **3. Third parties and standards** | 2027 Q1 | Vendor tiering, contract amendments, Tier 1 reviews; standards issued; SaaS change control; PHI moved to the enclave; HIPAA risk analysis | G-001, G-012, G-018, G-028, G-029, G-030, G-060, G-063 |
| **4. Reduce what is kept** | 2027 Q2 | First disposal run; retention schedule review; printer replacements; specification-level HIPAA analysis | G-016, G-017, G-059, G-071 |
| **5. Sustain** | 2027 Q3 and after | Annual risk assessment (July 2027); penetration test with the expanded scope; second board report; SOC 2 Type 2 period for CAS (P09) | G-005, G-022, G-040 |

Progress is reported quarterly to the audit committee as the count of rows moving from Partially met or Not met to Met.

**Timing.** The filing season starts in January, when the workforce grows by about 130 seasonal staff and interns and client document traffic peaks. Every High gap except the vendor contracts (G-029) and the treatment backlog (G-002) is due by 2027-01-15.

## 6. Pending regulatory changes
- **FTC Safeguards Rule.** The Federal Register shows no pending proposal to amend 16 CFR Part 314 as of 2026-09-25. The last change was the notification amendment (88 FR 77508, effective 2024-05-13).
- **IRC 7216 regulations.** No pending Treasury proposal was found. There is no AI-specific IRS guidance under section 7216; the IRS Section 7216 Information Center, checked 2026-09-25, lists guidance only through Rev. Proc. 2013-14 and 2013-19. The AI rows apply the regulation text directly, and counsel will confirm them (P10).
- **HIPAA Security Rule NPRM** (90 FR 898, 2025-01-06) is **still proposed**, with a final rule projected for July 2027. If finalized as proposed, it would remove the required and addressable distinction, require encryption of ePHI at rest and in transit with limited exceptions, MFA, a written technology asset inventory and network map, penetration testing at least every 12 months, restoration of certain systems within 72 hours, an annual compliance audit, and business associate notice within 24 hours of activating a contingency plan. None of these is treated as a current obligation. The HIPAA rows note this in `pending_rule_change`.
- **CIRCIA (N54-R09).** Proposed only (89 FR 23644). Unlike the Small sample, the Company **exceeds** its SBA size standard. If the final rule keeps the proposed size-based criterion (226.2(a)) and the Company is treated as part of a critical infrastructure sector, it could be covered. Counsel will assess that when a final rule is published. It is not treated as an obligation.
