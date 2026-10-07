# Regulatory Gap Analysis: Cris Santos Company | Management of Companies and Enterprises | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (holding company with three operating subsidiaries) |
| Tier / Vertical | Small / Management of Companies and Enterprises |
| Primary benchmark | NIST Cybersecurity Framework (CSF) 2.0 group profile (voluntary), NIST CSWP 29 (Feb. 26, 2024), Govern function emphasis |
| Profile method | NIST SP 1301, *NIST Cybersecurity Framework 2.0: Quick-Start Guide for Creating and Using Organizational Profiles* (Feb. 2024), https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1301.pdf |
| Secondary regulation | FTC Standards for Safeguarding Customer Information (Safeguards Rule), 16 CFR Part 314, as it applies to CSC Consumer Finance ("Finance") and reaches the holding company. Text checked on eCFR as of 2026-09-23 (last amended 88 FR 77508, Nov. 13, 2023) |
| Assessment dates | 2026-08-17 to 2026-08-28 |
| Assessor | IT Manager (Qualified Individual for Finance) with the CFO; applicability conclusions reviewed by outside counsel |
| Files | `gap-analysis.csv` (108 rows), `subsidiary-profiles.csv` (22 CSF categories x 4 profiles) |

## 1. Applicability
A holding company's cyber obligations mostly come from what it is (public or private, bank holding company or not) and from what its subsidiaries do. Each candidate requirement was checked against its primary text.

| Requirement | Applies? | Basis |
|---|---|---|
| **N55-R01** SEC Regulation S-K Item 106 (17 CFR 229.106) | **No** | Regulation S-K sets the content of registration statements and of annual and other reports under Exchange Act sections 13 and 15(d) (17 CFR 229.10(a)). Item 106 speaks to "the registrant." The company has registered no securities, files no reports, and has 5 holders of record, so it is not required to register a class under section 12(g) (17 CFR 240.12g-1(b)(1): fewer than 2,000 holders of record, fewer than 500 of them non-accredited). |
| **N55-R02** Form 8-K Item 1.05 | **No** | Applies to SEC registrants. Same reason. |
| **N55-R03** SOX section 404 (15 U.S.C. 7262) | **No** | Applies to issuers filing Exchange Act reports. The lender's audited-statement requirement is contractual. |
| **N55-R04** Federal Reserve incident notification (12 CFR 225.300-225.303) | **No** | Scope is bank holding companies, savings and loan holding companies, and others listed in 225.300(c). A bank holding company is a company that controls a bank (225.2(c)(1)). Finance takes no deposits and is not a bank (225.2(b)). |
| **N55-R05** 12 CFR Part 225, Appendix F | **No** | Same reason. The Safeguards Rule covers Finance instead. |
| **N55-R06** HIPAA (group health plan) | **Limited** | The plan has about 52 participants, so it is a group health plan (45 CFR 160.103). It is fully insured, and the sponsor receives only enrollment and summary health information, so 164.530(k) relief applies and the 164.314(b) plan-document security terms are not triggered. No gap rows. |
| **N55-R07** CIRCIA (proposed 6 CFR Part 226) | **Not yet** | Proposed only; no final rule as of 2026-09-25. |
| **FTC Safeguards Rule** (16 CFR Part 314) | **Yes, for Finance; reaches the holding company** | See below. Selected as the secondary regulation. |
| Florida Information Protection Act (Fla. Stat. 501.171) | **Yes, all four entities** | Each entity holds personal information (employee SSNs and bank accounts; Finance customer data). 501.171(2) requires "reasonable measures to protect and secure data in electronic form containing personal information," and 501.171(8) requires disposal of customer records when no longer retained. Breach notice duties are in P08. Not decomposed here: the statute sets no control elements beyond those two duties. |

**How the Safeguards Rule reaches the group.**
1. **Finance is a financial institution.** 16 CFR 314.2(h)(1) covers any institution significantly engaged in an activity that is financial in nature under section 4(k) of the Bank Holding Company Act, and 314.1(b) lists "finance companies" among covered entities. Finance makes consumer installment loans and is under FTC jurisdiction (it is not supervised by a banking agency).
2. **The small-institution exception does not apply.** 314.6 exempts institutions with customer information on fewer than 5,000 consumers from 314.4(b)(1), (d)(2), (h), and (i). Finance holds customer information on about 8,600 consumers (active and paid-off borrowers, and declined applicants, who are consumers under 314.2(b)(2)(i)).
3. **The holding company is reached in two ways.**
   - It employs Finance's **Qualified Individual** (the IT Manager). 314.4(a) allows that, but Finance must retain responsibility, designate a senior member of its own staff to oversee the Qualified Individual, and **require the affiliate to maintain an information security program that protects Finance** (314.4(a)(1)-(3)).
   - It is Finance's **service provider**: it "receives, maintains, processes, or otherwise is permitted access to customer information" through shared services (314.2(r)). Finance must select, contract with, and periodically assess it (314.4(f)).
   - The rule applies to "all customer information in your possession" (314.1(b)), and customer information includes records "handled or maintained by or on behalf of you or your affiliates" (314.2(d)). Finance customer information in the shared email, file, backup, and bank-file systems is in scope.
4. **Supply and Home Services are not financial institutions.** Supply extends trade credit only to businesses. Home Services gives customers Finance's application link but does not take, evaluate, or broker applications. Counsel confirmed this treatment on 2026-08-27.
5. **The Safeguards Rule has no required and addressable split.** Its elements are mandatory, with two built-in alternatives the Qualified Individual may approve: compensating controls where encryption is infeasible (314.4(c)(3)) and reasonably equivalent controls in place of MFA (314.4(c)(5), approved in writing). Neither has been approved.

**Why CSF 2.0 is the primary benchmark.** The vertical's parent-level drivers (SEC and Federal Reserve) do not apply to a private group that owns no bank. No binding rule sets cyber governance for the group as a whole, but the group's real exposure is governance: one shared platform, four entities, and no one deciding risk for all of them. CSF 2.0's Govern function is built for that question, and its Organizational Profiles let the group set one target and track each subsidiary against it. The Safeguards Rule is the binding floor for the part of the group that holds consumer financial data.

## 2. Method
The group profile follows the five steps in CSF 2.0 section 3.1 and NIST SP 1301.

1. **Scope the profiles.** CSF 2.0 allows "as many Organizational Profiles as desired, each with a different scope." The group uses four:
   - a **Group Organizational Profile** for the holding company and the Shared Corporate Services Platform, where most outcomes are delivered once for everyone;
   - three **subsidiary profiles** (Supply, Home Services, Finance) that inherit group outcomes and add what each subsidiary does on its own systems.

   Scope includes all threat types and all four entities. The CFO owns the profiles and the CEO sets expectations for the target.
2. **Gather information.** P01 risk register, P05 BIA, the SSP (P02), Finance's 2023 WISP, contracts, configuration exports, and interviews at all three sites.
3. **Create the profiles.** For each selected outcome, `gap-analysis.csv` records current practices (`current_state`, `evidence`), a **rating** on a 1-5 scale, a **priority** (High, Medium, Low), and the target goal (`remediation_action`). SP 1301 step 3b allows including the outcomes that apply to the use case with a rationale. **This first cycle includes all 31 Govern subcategories and 39 subcategories from the other five Functions** that bear on the shared platform and the P01 risks. The other 36 subcategories are covered at control level in the SSP (P02) and will be added in the 2027 cycle.

   Rating scale (author-defined, as SP 1301 allows): 1 = not performed; 2 = informal or only at some entities; 3 = defined and performed for the shared platform; 4 = consistent across the group; 5 = measured and improving. Status maps from the rating: 1 = Not met, 2-3 = Partially met, 4-5 = Met.

   **CSF Tiers.** The group's current practices are **Tier 1 (Partial)**. The target is **Tier 2 (Risk Informed)** for the group by 2027-09-30. Finance's customer-information outcomes target a rating of 4.
4. **Analyze gaps and create the action plan.** Each gap has an owner, date, and risk level on the P01 scale. High and Moderate gaps feed the risk register (P01) and POA&M (P07).
5. **Implement and update.** The profile is refreshed each August with the risk assessment.

**Crosswalk.** CSF rows use NIST's official CSF 2.0 to SP 800-53 Rev. 5.2.0 informative references (full list in `nist_official_sp800_53r5`; key controls in `sp800_53_controls`). Safeguards Rule rows use an **author mapping** to CSF 2.0 and SP 800-53; NIST has published no official mapping for 16 CFR Part 314.

**Traceability note.** The vertical requirements list (`02_industry-rules/holding-companies/requirements.csv`) has no row for the Safeguards Rule, so Safeguards rows cite the regulation directly (for example, "16 CFR 314.4(c)(5) (Finance)") in the `regulatory_driver` column.

## 3. Results summary
### 3.1 CSF 2.0 Group Organizational Profile (70 outcomes)
| Function | Met | Partially met | Not met |
|---|---|---|---|
| Govern (GV) | 0 | 21 | 10 |
| Identify (ID) | 2 | 6 | 4 |
| Protect (PR) | 1 | 11 | 1 |
| Detect (DE) | 0 | 4 | 2 |
| Respond (RS) | 0 | 3 | 2 |
| Recover (RC) | 0 | 0 | 3 |
| **Total (70)** | **3** | **45** | **22** |

**Govern is the weakest Function.** No Govern outcome is met. The three met outcomes are ID.RA-05 and ID.RA-06 (the 2026 risk assessment and treatment tracking) and PR.DS-02 (encryption in transit). Of the 70 outcomes, 39 are High priority, 22 Medium, and 9 Low.

### 3.2 Subsidiary profiles (category level, `subsidiary-profiles.csv`)
| Profile | Categories rated 1 | Rated 2 | Rated 3 | Main difference from the group |
|---|---|---|---|---|
| Group (holding company and SCSP) | 5 | 11 | 6 | Baseline |
| Supply | 15 | 7 | 0 | Shared counter account; single circuit and flat warehouse network |
| Home Services | 17 | 5 | 0 | SYS-11 outside single sign-on; firewall firmware behind |
| Finance | 9 | 11 | 2 | Has a Qualified Individual and WISP; customer information raises its target to 4 in 7 categories |

The subsidiaries score lower than the group because they rely on it: where the shared platform has not delivered an outcome, no subsidiary has a local substitute. The target for every profile is 3 in every category by 2027-09-30, and 4 for Finance in ID.AM, ID.RA, PR.AA, PR.AT, PR.DS, DE.CM, and RS.CO.

### 3.3 FTC Safeguards Rule (31 requirements)
| Section | Met | Partially met | Not met |
|---|---|---|---|
| 314.3(a) Written program | 0 | 1 | 0 |
| 314.4(a) Qualified Individual | 2 | 1 | 1 |
| 314.4(b) Risk assessment | 2 | 1 | 0 |
| 314.4(c) Safeguards | 0 | 5 | 5 |
| 314.4(d) Testing and monitoring | 0 | 1 | 1 |
| 314.4(e) Personnel | 0 | 3 | 1 |
| 314.4(f) Service providers | 0 | 3 | 0 |
| 314.4(g)-(j) Adjust, incident plan, board report, FTC notice | 0 | 4 | 0 |
| **Total (31)** | **4** | **19** | **8** |

### 3.4 Not applicable (7 rows)
N55-R01 to N55-R07, with reasons in section 1.

Of the 94 unmet or partially met rows, 4 are rated High risk, 65 Moderate, and 25 Low.

## 4. Priority gaps and roadmap
| Gap | Reference | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| MFA can be phished; admins and payment staff exposed | PR.AA-03; 314.4(c)(5) | High | Hardware security keys for 22 high-risk users; device-based conditional access | IT Manager | 2026-12-31 |
| Seven global admins; all-employee sites exposed Finance data | PR.AA-05; 314.4(c)(1)(ii) | High | 2 standing admins plus break-glass; quarterly access and site reviews | IT Manager | 2026-11-30 |
| Payables and treasury untrained on payment fraud | PR.AT-02 | High | Fraud training; callback procedure (P01 R-002) | CFO | 2026-10-31 |
| Backups exposed and untested | PR.DS-11; RC.RP-03 | High | Immutable separate-account backups; first restore test 2026-10-30 | IT Manager | 2027-01-31 |
| No written requirement on the holding company as Finance's affiliate and service provider | 314.4(a)(3); 314.4(f)(2); GV.OC-05 | Moderate | Security schedule in the intercompany services agreement | CFO | 2026-12-31 |
| No penetration testing or vulnerability assessments | 314.4(d)(2); ID.RA-01 | Moderate | Monthly scans; annual penetration test | IT Manager | 2026-12-31 |
| No user activity monitoring; 30-day logs | 314.4(c)(8); DE.CM-03 | Moderate | Log workspace with 1-year retention; weekly review | IT Manager | 2026-12-31 |
| Customer information kept indefinitely | 314.4(c)(6); Fla. Stat. 501.171(8) | Moderate | Retention schedule; 90-day ACH file deletion | Finance President | 2026-11-30 |
| No lines of communication with subsidiaries on cyber risk | GV.RM-05; GV.RR-01 | Moderate | Monthly cyber item with subsidiary Presidents; cyber duties in their roles | CFO | 2026-10-31 |
| No supplier due diligence or reviews | GV.SC-06; GV.SC-07; 314.4(f)(1), (f)(3) | Moderate | Security questionnaire in purchasing; annual SOC 2 reviews (P09) | CFO; IT Manager | 2026-12-31 |

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07).

## 5. Pending regulatory changes and watch items
- **CIRCIA** (N55-R07) is proposed only. If finalized, recheck the sector criteria and the size-based criterion against the group; do not treat it as a current obligation.
- **Safeguards Rule:** no pending amendments found; the FTC notification requirement (314.4(j)) has been effective since May 13, 2024 (314.5).
- **Structural triggers that would change this analysis:** registering or publicly offering securities (N55-R01 to N55-R03 would apply); acquiring a bank or savings association (N55-R04, N55-R05); self-insuring the health plan (N55-R06); Home Services starting to take or broker credit applications (it could become a financial institution); Finance falling below 5,000 consumers (314.6 exception). The group profile is refreshed after any of these.
