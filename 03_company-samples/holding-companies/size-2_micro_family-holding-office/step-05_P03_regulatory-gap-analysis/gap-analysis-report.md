# Regulatory Gap Analysis: Cris Santos Company | Management of Companies and Enterprises | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (family holding company and single-family office) |
| Tier / Vertical | Micro / Management of Companies and Enterprises |
| Primary benchmark | NIST Cybersecurity Framework (CSF) 2.0 Organizational Profile (voluntary), NIST CSWP 29 (Feb. 26, 2024), Govern function emphasis |
| Profile method | NIST SP 1301, *NIST Cybersecurity Framework 2.0: Quick-Start Guide for Creating and Using Organizational Profiles* (Feb. 2024), https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1301.pdf |
| Binding regulation | FTC Standards for Safeguarding Customer Information (Safeguards Rule), 16 CFR Part 314, as narrowed by the small-institution exception in 314.6. Text checked on eCFR as of 2026-09-23 (last amended 88 FR 77508, Nov. 13, 2023) |
| Applicability gate | Advisers Act family office exclusion, 17 CFR 275.202(a)(11)(G)-1 (eCFR as of 2026-09-23; last amended 81 FR 60457, Sept. 1, 2016) |
| Assessment dates | 2026-08-03 to 2026-08-14 |
| Assessor | Family Office Director (Qualified Individual) with the MSP lead technician; applicability conclusions reviewed by outside counsel on 2026-08-12 |
| Approved | 2026-09-18 by the Principal |
| File | `gap-analysis.csv` (82 rows) |

## 1. Applicability
A holding company's cyber obligations come mostly from what it is and from what it does. This office is two things at once: the parent of three operating companies, and the family's investment and administrative office. Each candidate requirement was checked against its primary text.

| Requirement | Applies? | Basis |
|---|---|---|
| **N55-R01** SEC Regulation S-K Item 106 (17 CFR 229.106) | **No** | Regulation S-K sets the content of registration statements and Exchange Act reports (17 CFR 229.10(a)). The office has registered no securities, files no reports, and has 2 holders of record, so section 12(g) registration is not required (17 CFR 240.12g-1). |
| **N55-R02** Form 8-K Item 1.05 | **No** | Applies to SEC registrants. Same reason. |
| **N55-R03** SOX section 404 (15 U.S.C. 7262) | **No** | Applies to issuers filing Exchange Act reports. |
| **N55-R04** Federal Reserve incident notification (12 CFR 225.300-225.303) | **No** | The office controls no bank or savings association, so it is not a bank holding company or savings and loan holding company (12 CFR 225.2). |
| **N55-R05** 12 CFR Part 225, Appendix F | **No** | Same reason. The Safeguards Rule covers the office instead. |
| **N55-R06** HIPAA (group health plan) | **Limited** | The insured plan for 7 employees is a group health plan because the insurer administers it (45 CFR 160.103), but the office receives only enrollment information, so 164.530(k) relief applies and the 164.314(b) plan-document security terms are not triggered. No gap rows. |
| **N55-R07** CIRCIA (proposed 6 CFR Part 226) | **Not yet** | Proposed only; no final rule as of 2026-09-25. |
| **Advisers Act family office exclusion** (17 CFR 275.202(a)(11)(G)-1) | **Relied on** | See below. Three exclusion conditions are tracked as rows G-001 to G-003. |
| **FTC Safeguards Rule** (16 CFR Part 314) | **Yes, narrowed by 314.6** | See below. |
| Florida Information Protection Act (Fla. Stat. 501.171) | **Yes** | The office is a covered entity (501.171(1)(b)). 501.171(2) requires "reasonable measures to protect and secure data in electronic form containing personal information", and 501.171(8) requires disposal of customer records when no longer retained. Two rows; breach notice duties are in P08. |
| Florida Digital Bill of Rights (Fla. Stat. 501.702) | **No** | A controller must exceed $1 billion in global gross annual revenue and meet one of three further tests (50% or more of revenue from online advertising, a smart speaker service, or an app store with at least 250,000 applications). The office meets none. |

**The family office exclusion (why the office is not an SEC-registered adviser).** The office gives investment advice, so without an exclusion it would be an investment adviser under the Advisers Act. Rule 202(a)(11)(G)-1 excludes a "family office", a company that (b)(1) has no clients other than family clients, (b)(2) is wholly owned by family clients and exclusively controlled by family members or family entities, and (b)(3) does not hold itself out to the public as an investment adviser. The office meets all three today (rows G-001 to G-003). The exclusion matters for security in two ways:
- Losing it would bring registration and new compliance duties, so the conditions are tracked like any other requirement. The one partial finding is (b)(3): a staff profile that described the office as offering advisory services (corrected 2026-08-13).
- Being outside the Advisers Act does not take the office outside every privacy rule. That leads to the Safeguards Rule.

**How the Safeguards Rule reaches the office (conservative position).**
1. **Financial institution.** 16 CFR 314.2(h)(1) covers any institution significantly engaged in an activity that is financial in nature under section 4(k) of the Bank Holding Company Act. Providing investment advisory services is such an activity (314.2(h)(2)(xii)), and 314.1(b) lists "investment advisors that are not required to register with the Securities and Exchange Commission" and "other financial advisors" among covered entities. Advising the family is the office's core business, not an occasional activity.
2. **Customers.** Family members obtain advisory services for a fee under written service agreements, which is a customer relationship (314.2(e)(2)(i)(G)). The family entities are not consumers (a consumer is an individual, 314.2(b)(1)), but customer information is protected wherever it sits.
3. **Counsel's view.** No FTC statement specific to single-family offices was found. Counsel agreed on 2026-08-12 that treating the office as covered is the safer reading, and that the cost is small because of the exception below.
4. **The 314.6 exception applies.** The office maintains customer information on 11 individuals, far fewer than 5,000 consumers. So **314.4(b)(1)** (written risk assessment content), **(d)(2)** (penetration testing and vulnerability assessments), **(h)** (written incident response plan), and **(i)** (annual report to the board) do not apply. The office adopts (h) and (i) voluntarily, and its risk assessment meets (b)(1) anyway. Every other element applies.
5. **FTC notice is practically unreachable.** 314.4(j) requires FTC notice only for a notification event involving at least 500 consumers. The obligation stays in the P08 matrix in case the office grows.
6. **No required and addressable split.** The rule's elements are mandatory, with two built-in alternatives the Qualified Individual may approve: compensating controls where encryption is infeasible (314.4(c)(3)) and reasonably equivalent controls in place of MFA (314.4(c)(5), approved in writing). Neither has been approved.

**Why CSF 2.0 is still the primary benchmark.** The vertical's parent-level drivers (SEC and Federal Reserve) do not apply to a private office that owns no bank. The Safeguards Rule sets a floor for family customer information. Neither says how the office should govern risk across its three roles: subsidiary parent, investment office, and family administrator. CSF 2.0's Govern function covers that question, including the office's oversight of the subsidiaries and of its vendors.

**Why there are no subsidiary profiles.** The Small sample builds a profile for each subsidiary because it runs a shared platform for them. At this size each subsidiary runs its own IT through its own provider; the office's part is oversight (GV.RM-05, GV.SC-05) and the guest access and payment approvals it shares with them.

## 2. Method
The profile follows the five steps in CSF 2.0 section 3.1 and NIST SP 1301.
1. **Scope.** One Organizational Profile for the office and the Family Office Shared Services Platform, covering all threat types and the office's oversight of the subsidiaries. The Family Office Director owns it; the Principal sets expectations for the target.
2. **Gather information.** P01 risk register, P05 BIA, the SSP (P02), contracts, configuration exports from SYS-02, SYS-03, SYS-07, and SYS-11, the March 2026 fraud attempt, and interviews with all 7 staff, two Subsidiary Presidents (by phone), and the MSP lead technician.
3. **Create the profile.** SP 1301 step 3b allows including the outcomes that apply to the use case with a rationale. **This first cycle includes 41 subcategories:** 18 from Govern (organizational context, risk strategy, roles, policy, oversight, and supplier risk) and 23 from the other five Functions that bear on the P01 risks. Each row records current practices (`current_state`, `evidence`), a **rating** on a 1-5 scale, a **priority** (High or Medium), and the target (`remediation_action`).

   Rating scale (author-defined, as SP 1301 allows): 1 = not performed; 2 = informal or partial; 3 = defined and performed; 4 = consistent and evidenced; 5 = measured and improving. Status maps from the rating: 1 = Not met, 2-3 = Partially met, 4-5 = Met.

   **CSF Tiers.** Current practices are **Tier 1 (Partial)**. The target is **Tier 2 (Risk Informed)** by 2027-09-30, with a rating of 3 or better on every High-priority outcome.
4. **Analyze gaps and plan.** Each gap has an owner, date, and risk level on the P01 scale. High and Moderate gaps feed the risk register (P01) and the POA&M (P07).
5. **Implement and update.** The profile is refreshed each August with the risk assessment.

**Status date.** Every status reflects the end of fieldwork (2026-08-14). Actions completed since then (for example, policies approved 2026-09-18) appear in the remediation column but do not change the status.

**Crosswalk.** CSF rows list NIST's official CSF 2.0 to SP 800-53 Rev. 5.2.0 informative references in `nist_official_sp800_53r5` and the key controls in `sp800_53_controls`. Safeguards Rule, Advisers Act, and Florida rows use an **author mapping** to CSF 2.0 and SP 800-53; NIST has published no official mapping for those texts.

**Traceability note.** The vertical requirements list (`02_industry-rules/holding-companies/requirements.csv`) has rows only for the parent-level drivers (N55-R01 to N55-R07), all not applicable here. The binding rows therefore cite the regulation directly in the `regulatory_driver` column (for example, "16 CFR 314.4(c)(5)" or "Fla. Stat. 501.171(8)").

## 3. Results summary
### 3.1 CSF 2.0 Organizational Profile (41 outcomes)
| Function | Met | Partially met | Not met |
|---|---|---|---|
| Govern (GV) | 0 | 11 | 7 |
| Identify (ID) | 1 | 1 | 4 |
| Protect (PR) | 1 | 7 | 2 |
| Detect (DE) | 0 | 0 | 3 |
| Respond (RS) | 0 | 0 | 2 |
| Recover (RC) | 0 | 0 | 2 |
| **Total (41)** | **2** | **19** | **20** |

**Govern is partial everywhere and met nowhere.** The office has capable people and long-standing vendors, but before August 2026 it had no policy, no designated security lead, no Board reporting, and no security terms in any contract. The two met outcomes are ID.RA-05 (the 2026 risk assessment) and PR.DS-02 (encryption in transit, supplied by the vendors). Detect, Respond, and Recover score lowest: nothing watches for a mailbox takeover, and nothing says what to do if one happens. Of the 41 outcomes, 24 are High priority and 17 Medium.

### 3.2 FTC Safeguards Rule (29 requirements)
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| 314.3(a) Written program | 0 | 0 | 1 | 0 |
| 314.4(a) Qualified Individual | 1 | 0 | 0 | 1 |
| 314.4(b) Risk assessment | 1 | 1 | 0 | 1 |
| 314.4(c) Safeguards | 0 | 5 | 5 | 0 |
| 314.4(d) Testing and monitoring | 0 | 1 | 0 | 1 |
| 314.4(e) Personnel | 0 | 2 | 2 | 0 |
| 314.4(f) Service providers | 0 | 2 | 1 | 0 |
| 314.4(g)-(j) Adjust, incident plan, board report, FTC notice | 0 | 2 | 0 | 2 |
| **Total (29)** | **2** | **13** | **9** | **5** |

The 5 not-applicable rows are the four elements excepted by 314.6 and 314.4(a)(1)-(3), which applies only when the Qualified Individual works for a service provider or affiliate.

### 3.3 Other rows (12)
| Group | Met | Partially met | Not applicable |
|---|---|---|---|
| Advisers Act family office exclusion (3) | 2 | 1 | 0 |
| Florida Information Protection Act (2) | 0 | 2 | 0 |
| Vertical requirements N55-R01 to N55-R07 (7) | 0 | 0 | 7 |

### 3.4 All rows
| Status | Rows |
|---|---|
| Met | 6 |
| Partially met | 35 |
| Not met | 29 |
| Not applicable | 12 |
| **Total** | **82** |

Of the 64 unmet or partially met rows, 6 are rated High risk, 39 Moderate, and 19 Low.

## 4. Priority gaps and roadmap
| Gap | Reference | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| MFA can be phished; SYS-11 admin password-only | PR.AA-03; 314.4(c)(5) | High | Security keys for staff and admins; SYS-11 behind the MSP's MFA gateway | Family Office Director | 2026-12-31 |
| Every staff member can open every family folder | PR.AA-05; 314.4(c)(1)(ii) | High | Need-to-know groups; tax and ID documents only in the vault; bill pay dual approval | Office Manager | 2026-10-31 |
| No idea where family personal information is | ID.AM-07 | High | Data inventory by system and folder | Family Office Director | 2026-11-30 |
| Payment staff untrained on email fraud | PR.AT-02 | High | Verification training; callback procedure and log (P01 R-002) | Controller | 2026-10-31 |
| No written program or policies | 314.3(a); GV.PO-01 | Moderate | POL-02, POL-03, POL-04 and the SSP (approved 2026-09-18) | Family Office Director | 2026-09-18 |
| No monitoring of user activity | 314.4(c)(8); DE.CM-03 | Moderate | SYS-02 alerts to the MSP and the Family Office Director; monthly review; one-year logs | Family Office Director | 2026-12-31 |
| No contractual safeguards or assessments of providers | 314.4(f)(2)-(3); GV.SC-05; GV.SC-07 | Moderate | MSP amendment; service provider list; annual SOC 2 reviews | Family Office Director | 2026-12-31 |
| Records kept since 2009 | 314.4(c)(6)(i); Fla. Stat. 501.171(8) | Moderate | Retention schedule and disposal log | Controller | 2027-03-31 |
| Backups missing or untested | PR.DS-11; RC.RP-03 | Moderate | Independent SaaS backup; separate-account snapshots; restore tests | Office Manager | 2026-11-30 |
| No lines of communication with subsidiaries | GV.RM-05 | Moderate | 24-hour notice terms in management agreements; monthly security item | Family Office Director | 2027-03-31 |

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07).

## 5. Remediation plan
The plan fits a 7-person office: most actions are short procedures, settings in existing SaaS tools, or MSP work. Costs are in the P01 treatment summary.

| Phase | Due | Actions | Main rows closed |
|---|---|---|---|
| 1. Governance and payments | 2026-10-31 | Adopt policies and the SSP (done 2026-09-18); callback procedure and payment log; payment-fraud training; need-to-know folders; bill pay dual approval; offboarding checklist; family-client eligibility and communications rules | 314.3(a); GV.PO-01; PR.AT-02; PR.AA-05; 314.4(c)(1)(ii); GV.RR-04; G-001; G-003 |
| 2. Identity and visibility | 2026-12-31 | Security keys; named MSP admin accounts; SYS-11 behind the MFA gateway and upgraded; SYS-02 alerts and one-year logs; monthly scans; data inventory; independent backup and restore tests | PR.AA-01; PR.AA-03; 314.4(c)(5); DE.CM-03; 314.4(c)(8); ID.RA-01; ID.AM-07; PR.DS-11 |
| 3. Third parties | 2026-12-31 to 2027-03-31 | MSP contract amendment; service provider list; SOC 2 reviews; security terms in management agreements and the CPA engagement letter | GV.SC-04; GV.SC-05; GV.SC-07; 314.4(f)(1)-(3); GV.RM-05 |
| 4. Records | 2027-03-31 | Retention schedule; disposal of records past it | 314.4(c)(6)(i); Fla. Stat. 501.171(8); ID.AM-08 |
| 5. Annual cycle | 2027-08-31 to 2027-09-30 | Risk and profile update (August); independent assessment; written report to the Board of Managers (September) | 314.4(b)(2); GV.OV-01; GV.RR-01 |

**Progress check.** The Family Office Director reports progress to the Principal at a monthly 30-minute meeting, using the P07 POA&M as the tracker.

## 6. Pending regulatory changes and watch items
- **CIRCIA** (N55-R07) is proposed only. If finalized, recheck the sector and size criteria; do not treat it as a current obligation.
- **Safeguards Rule:** no pending amendments found. The FTC notice requirement (314.4(j)) has been in effect since May 13, 2024 (314.5).
- **Family office rule:** no pending amendments found.
- **Structural triggers that would change this analysis:**
  - accepting a non-family client or co-investor, or holding out to the public (the office would lose the exclusion and could become an SEC- or state-registered adviser with new duties);
  - customer information reaching 5,000 or more consumers (the four excepted Safeguards elements would apply), which is not realistic for a single-family office;
  - acquiring an interest in a bank (N55-R04, N55-R05);
  - registering or publicly offering securities (N55-R01 to N55-R03);
  - self-insuring the health plan or receiving claims data (N55-R06).
