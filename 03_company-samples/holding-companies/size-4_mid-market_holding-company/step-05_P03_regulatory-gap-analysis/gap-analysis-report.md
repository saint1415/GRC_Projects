# Regulatory Gap Analysis: Cris Santos Company | Management of Companies and Enterprises | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed holding company with four operating subsidiaries) |
| Tier / Vertical | Mid-Market / Management of Companies and Enterprises |
| Primary benchmark | NIST Cybersecurity Framework (CSF) 2.0 group profile (voluntary), NIST CSWP 29 (Feb. 26, 2024), Govern function emphasis; all 106 subcategories |
| Profile method | NIST SP 1301, *NIST Cybersecurity Framework 2.0: Quick-Start Guide for Creating and Using Organizational Profiles* (Feb. 2024), https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1301.pdf |
| Binding rules analyzed at requirement level | FTC Standards for Safeguarding Customer Information (Safeguards Rule), 16 CFR Part 314, for CSC Consumer Finance ("Finance") and the holding company as its affiliate and service provider (text checked on eCFR as of 2026-09-23; last amended 88 FR 77508, Nov. 13, 2023). HIPAA Security Rule (45 CFR Part 164, Subpart C), plan sponsor terms (164.504(f), 164.314(b)), and Breach Notification Rule for the self-funded group health plan (N55-R06). Florida Information Protection Act, Fla. Stat. 501.171(2) and (8) |
| Assessment dates | 2026-07-13 to 2026-08-07; evidence refreshed with P07 results through 2026-09-04 |
| Assessor | Security Manager (Qualified Individual for Finance) and the GRC analyst, with the vCISO; applicability conclusions reviewed by the General Counsel and outside counsel; method reviewed by the co-sourced internal audit firm |
| Approved | CEO, 2026-09-22; Finance and plan sections also received by Finance's Board of Managers and the Benefits Committee the same day |
| Files | `gap-analysis.csv` (221 rows), `subsidiary-profiles.csv` (22 CSF categories x 6 profiles) |

## 1. Applicability
A holding company's cyber obligations come mostly from what it is (public or private, bank holding company or not) and from what its subsidiaries and benefit plans do. Each candidate requirement was checked against its primary text. **The mid-market answer differs from the small-company answer in one place: the group health plan.** At 600 employees the plan is self-funded, so HIPAA reaches the holding company as plan sponsor.

**Primary business line.** The holding company's business is shared services for its subsidiaries (NAICS 551112). The rules that bind those services are the ones that follow the data the shared platform holds: Finance customer information (Safeguards Rule) and plan PHI (HIPAA). Both are analyzed requirement by requirement.

| Requirement | Applies? | Basis |
|---|---|---|
| **N55-R01** SEC Regulation S-K Item 106 (17 CFR 229.106) | **No** | Regulation S-K sets the content of registration statements and Exchange Act reports (17 CFR 229.10(a)); Item 106 speaks to "the registrant." The company has registered no securities, files no reports, and has 24 holders of record, so section 12(g) registration is not required (17 CFR 240.12g-1) |
| **N55-R02** Form 8-K Item 1.05 | **No** | Applies to SEC registrants. Same reason |
| **N55-R03** SOX section 404 (15 U.S.C. 7262) | **No** | Applies to issuers filing Exchange Act reports. The audited statements required by the lenders and the sponsor are contractual |
| **N55-R04** Federal Reserve incident notification (12 CFR 225.300-225.303) | **No** | Scope is bank holding companies and the others listed in 225.300(c). A bank holding company controls a bank (225.2(c)(1)). Finance takes no deposits and is not a bank (225.2(b)). Selling loan participations to the bank partner does not change that |
| **N55-R05** 12 CFR Part 225, Appendix F | **No** | Same reason. The Safeguards Rule covers Finance instead; the bank partner's expectations arrive by contract (P09) |
| **N55-R06** HIPAA (group health plan) | **Yes** | The plan has about 470 participants, so it is a group health plan (45 CFR 160.103, 50 or more participants) and a covered entity. It is self-funded, and the sponsor's Benefits team receives PHI for plan administration (appeals, stop-loss files, high-cost claimant reports). The 164.530(k) relief requires benefits provided solely through an insurance contract, so it does not apply. The 164.314(b)(1) exception covers only summary health and enrollment information, so the plan documents must carry the security terms. Analyzed: all 69 Security Rule rows in the vertical crosswalk, 164.504(f)(2)(iii), and 5 Breach Notification rows |
| **N55-R07** CIRCIA (proposed 6 CFR Part 226) | **Not yet** | Proposed only; no final rule as of 2026-09-25. The group exceeds the SBA size standard, so the proposed size-based criterion must be rechecked when the rule is final |
| **FTC Safeguards Rule** (16 CFR Part 314) | **Yes, for Finance; reaches the holding company** | See below. All 31 elements analyzed |
| **Florida Information Protection Act** (Fla. Stat. 501.171) | **Yes, all group companies** | Each holds personal information of Florida residents. 501.171(2) requires reasonable measures to protect it, and 501.171(8) requires disposal of customer records no longer retained. Breach notice duties are in P08 |
| **Florida Digital Bill of Rights** (Fla. Stat. 501.702) | **No** | A controller must exceed $1 billion in global gross annual revenue and meet one of three activity tests (online advertising revenue, a smart speaker service, or an app store with at least 250,000 applications). The group has about $100 million and meets none |

**How the Safeguards Rule reaches the group.**
1. **Finance is a financial institution.** 16 CFR 314.2(h)(1) covers institutions significantly engaged in activities that are financial in nature, and 314.1(b) names "finance companies." Finance makes consumer installment loans and is under FTC jurisdiction.
2. **The small-institution exception does not apply.** 314.6 exempts institutions with customer information on fewer than 5,000 consumers from 314.4(b)(1), (d)(2), (h), and (i). Finance holds customer information on about 34,000 consumers, including declined applicants.
3. **The holding company is reached in two ways.** It employs Finance's Qualified Individual (314.4(a)(1)-(3)), and it is Finance's service provider because it receives, maintains, and processes customer information through shared services (314.2(r); 314.4(f)). Customer information includes records handled or maintained by or on behalf of Finance or its affiliates (314.2(d)).
4. **Supply, Home Services, and Fabrication are not financial institutions.** Supply extends trade credit only to businesses. Home Services passes along Finance's application link but does not take, evaluate, or broker applications. Counsel confirmed this treatment on 2026-08-05.
5. **No required and addressable split.** Safeguards elements are mandatory, with two alternatives the Qualified Individual may approve: compensating controls where encryption is infeasible (314.4(c)(3)) and equivalent controls in place of MFA, approved in writing (314.4(c)(5)). Neither has been approved.

**Why CSF 2.0 stays the primary benchmark.** No binding rule sets cyber governance for the group as a whole. The parent-level drivers (SEC and the Federal Reserve) do not apply to a private group that owns no bank. The group's real exposure is governance at scale: one shared platform, five companies, an acquisition program, and subsidiaries buying technology on their own. CSF 2.0's Govern function is built for that, and its Organizational Profiles let the group set one target and track each subsidiary against it. The Safeguards Rule and HIPAA are the binding floors for the regulated data the platform holds.

## 2. Method
**CSF 2.0 group profile (CSF section 3.1 and SP 1301 steps):**
1. **Scope the profiles.** A **Group Organizational Profile** covers the holding company and the SCSP, where most outcomes are delivered once for everyone. Five subsidiary profiles at category level (Supply, Home Services South and Central, Home Services North, Fabrication, Finance) inherit group outcomes and add what each does on its own systems. Home Services North has its own profile until it is integrated. The CFO owns the profiles; the CEO set the target.
2. **Gather information.** P01, P05, P02, the Finance WISP (2025), plan documents, contracts, configuration exports, and interviews and walkthroughs at 6 of 9 sites (HQ, the distribution center, Branch 2, the Central shop, the North shop, and the plant).
3. **Create the profiles.** All **106 subcategories** are in scope this cycle (the group's first full profile). Each row records current practice (`current_state`, `evidence`), a **rating** on a 1-5 scale, a **priority**, and the target (`remediation_action`). Rating scale (author-defined, as SP 1301 allows): 1 = not performed; 2 = informal or only at some entities; 3 = defined and performed for the shared platform; 4 = consistent across the group; 5 = measured and improving. Status maps from the rating: 1 = Not met, 2-3 = Partially met, 4-5 = Met.
4. **CSF Tiers.** Current practice is **Tier 2 (Risk Informed)** at the group and Tier 1 (Partial) at Home Services North and Fabrication. The target is **Tier 3 (Repeatable)** for the group by 2027-12-31.
5. **Analyze gaps and plan.** Each gap has an owner, a date, and a risk level on the P01 scale. High and Moderate gaps feed P01 and the P07 POA&M.

**Regulation rows.** Safeguards Rule elements were decomposed from the eCFR text. HIPAA Security Rule rows and their Required, Addressable, or Standard designations come from NIST SP 800-66 Rev. 2 through the vertical crosswalk (`02_industry-rules/health-care/hipaa-security-rule-crosswalk.csv`, 69 rows). The plan sponsor and Breach Notification rows were decomposed from the eCFR text (164.504(f), 164.402-164.410, verified 2026-09-23).

**Crosswalk.** CSF rows use NIST's official CSF 2.0 to SP 800-53 Rev. 5.2.0 informative references (`nist_official_sp800_53r5`) plus key controls selected by the author. Safeguards, plan sponsor, Breach Notification, and Florida rows use an **author mapping**; NIST has published no official mapping for them. HIPAA Security Rule rows use the vertical crosswalk, which is also an **author mapping** (with NIST's official OLIR SP 800-53 references where they exist).

**Traceability.** The vertical requirements list has no row for the Safeguards Rule, so Safeguards rows cite the regulation directly ("16 CFR 314.4(c)(5) (Finance)"). HIPAA rows cite N55-R06 with the section. N55-R06 names Subpart E; because the self-funded plan is a covered entity, Subparts C and D apply to it as well, and those rows are traced to N55-R06 too.

**Evidence sampling.** Where a requirement operates many times, a sample was tested rather than the whole population, chosen at random from system-generated populations with sizes from the co-sourced internal audit firm's attribute sampling table (25 for controls that operate many times a year; all items for small populations). Samples shared with P07 were tested once and used in both:
- terminations: 25 of 142 (12 months to 2026-06-30);
- transfers between subsidiaries or roles: 25 of 58;
- changes to Tier 1 systems: 25 of 214;
- vendor bank-detail changes: 25 of 310;
- declined Finance applications: 20 (retention test);
- critical vendor contracts: 22 of 22; Finance service provider contracts: 9 of 9; plan business associates: 3 of 3;
- collaboration site permissions: 96 of 96 (automated report);
- backup job days: 31 of 31 (July 2026);
- security incidents: 10 of 41;
- staff interviews on incident reporting: 15 across 6 sites.
Each `evidence` cell names the sample and its result where one was used.

## 3. Results summary
### 3.1 CSF 2.0 Group Organizational Profile (106 outcomes)
| Function | Met | Partially met | Not met | Total |
|---|---|---|---|---|
| Govern (GV) | 2 | 27 | 2 | 31 |
| Identify (ID) | 6 | 13 | 2 | 21 |
| Protect (PR) | 3 | 19 | 0 | 22 |
| Detect (DE) | 1 | 10 | 0 | 11 |
| Respond (RS) | 0 | 13 | 0 | 13 |
| Recover (RC) | 0 | 8 | 0 | 8 |
| **Total** | **12** | **90** | **4** | **106** |

**Govern is where scale shows.** The four Not met outcomes are GV.RM-05 (no lines of communication with subsidiaries), GV.SC-06 (no due diligence before suppliers or acquisitions), ID.AM-07 (no data map), and ID.RA-10 (critical suppliers not assessed before purchase). All four are about growth outrunning governance. The 12 Met outcomes are the risk method and risk records (GV.RM-06, ID.RA-03 to ID.RA-06), the strategy link (GV.OC-01), asset prioritization (ID.AM-05), independent assessment (ID.IM-01), federation tokens (PR.AA-04), encryption in transit (PR.DS-02), capacity (PR.IR-04), and MSSP escalation (DE.AE-06). Priorities: 46 High, 46 Medium, 14 Low.

### 3.2 Subsidiary profiles (category level, `subsidiary-profiles.csv`)
| Profile | Categories rated 1 | Rated 2 | Rated 3 | Main difference from the group |
|---|---|---|---|---|
| Group (holding company and SCSP) | 0 | 6 | 16 | Baseline |
| Supply | 4 | 14 | 4 | Shared counter accounts; unencrypted legacy shares on HQ servers |
| Home Services (South and Central) | 5 | 10 | 7 | Bought the AI voice agent without review |
| Home Services North | 22 | 0 | 0 | Outside group controls until integration (gap 2) |
| Fabrication | 12 | 10 | 0 | Flat plant network, unsupported controllers, weekly backup drive |
| Finance | 0 | 8 | 14 | Has a Qualified Individual and WISP; customer information raises its target to 4 in 7 categories |

The target for every profile is 3 in every category by 2027-12-31, and 4 for Finance in ID.AM, ID.RA, PR.AA, PR.AT, PR.DS, DE.CM, and RS.CO.

### 3.3 FTC Safeguards Rule (31 requirements)
| Section | Met | Partially met | Not met |
|---|---|---|---|
| 314.3(a) Written program | 0 | 1 | 0 |
| 314.4(a) Qualified Individual | 4 | 0 | 0 |
| 314.4(b) Risk assessment | 2 | 1 | 0 |
| 314.4(c) Safeguards | 0 | 8 | 2 |
| 314.4(d) Testing and monitoring | 2 | 0 | 0 |
| 314.4(e) Personnel | 1 | 3 | 0 |
| 314.4(f) Service providers | 0 | 3 | 0 |
| 314.4(g)-(j) Adjust, incident plan, board report, FTC notice | 0 | 4 | 0 |
| **Total (31)** | **9** | **20** | **2** |

Finance's program is mature at the top (Qualified Individual, oversight, risk assessment, testing) and weak in the safeguards themselves. The two Not met rows are disposal (314.4(c)(6)(i)) and the retention policy review (314.4(c)(6)(ii)).

### 3.4 HIPAA for the group health plan
| Section | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| 164.308 Administrative safeguards | 10 | 18 | 1 | 1 | 30 |
| 164.310 Physical safeguards | 8 | 4 | 0 | 0 | 12 |
| 164.312 Technical safeguards | 9 | 3 | 0 | 0 | 12 |
| 164.314 Organizational requirements | 0 | 3 | 5 | 2 | 10 |
| 164.316 Policies, procedures, documentation | 1 | 4 | 0 | 0 | 5 |
| **Security Rule subtotal** | **28** | **32** | **6** | **3** | **69** |
| 164.504(f)(2)(iii) and Breach Notification (164.402-164.410) | 0 | 6 | 0 | 0 | 6 |
| **Total** | **28** | **38** | **6** | **3** | **75** |

Of the 38 Security Rule rows that are Partially met or Not met, 14 are standards, 17 are **Required** implementation specifications, and 7 are **Addressable**. The 6 Not met rows are 164.308(a)(1)(ii)(D) (no review of activity on plan ePHI) and the 164.314(b) standard and its four implementation specifications (the plan documents have no security terms). The technical safeguards are largely Met because the plan's ePHI lives on the group's SaaS platforms with MFA, encryption, and EDR. What is missing is **plan-specific**: who may see plan PHI, the plan document promises, and activity review.

**Addressable is not optional.** For each addressable gap, the plan will implement the specification; none is being documented as unreasonable (164.306(d)(3)).

### 3.5 Florida and not applicable rows
- Fla. Stat. 501.171(2) and (8): 2 rows, both Partially met.
- Not applicable: 7 applicability rows (N55-R01 to N55-R05, N55-R07, and the Florida Digital Bill of Rights), plus 3 HIPAA rows (164.308(a)(4)(ii)(A), 164.314(a)(2)(ii), 164.314(a)(2)(iii)).

### 3.6 All rows
| Status | Rows |
|---|---|
| Met | 49 |
| Partially met | 150 |
| Not met | 12 |
| Not applicable | 10 |
| **Total** | **221** |

Of the 162 rows that are Partially met or Not met, 5 are rated High risk, 93 Moderate, and 64 Low.

## 4. Priority gaps
| Gap | Reference | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| No due diligence before suppliers or acquisitions; Home Services North outside controls | G-027 GV.SC-06 | High | M&A cyber checklist; day-1 control set; purchasing gate; North integration | VP of Corporate Development | 2026-12-31 |
| Phishable MFA for high-risk users; no MFA for directory administration | G-055 PR.AA-03; G-123 314.4(c)(5) | High | FIDO2 keys for about 70 users; MFA for directory administration through the broker | Security Manager | 2027-03-31 |
| Over-privilege across the group (14 Domain Admins members, 6 global administrators, HR site) | G-057 PR.AA-05 | High | Directory tiering; 2 standing global administrators; quarterly reviews | Security Manager | 2027-03-31 |
| On-premises backups exposed and untested | G-064 PR.DS-11 | High | Off-site immutable backups for HQ and plant; forest recovery test | VP of Information Technology | 2027-01-31 |
| Excess access to Finance customer information (export rights, site sharing) | G-116 314.4(c)(1)(ii) | High | Export rights to 4 roles; Restricted labels | Finance President | 2026-12-31 |
| Plan documents lack the 164.314(b) security terms | G-197 to G-201 | Moderate | Amend the plan documents; Benefits Committee approval | General Counsel | 2026-12-31 |
| Plan PHI reachable by 11 HR staff; no activity review | G-149 164.308(a)(3); G-145 164.308(a)(1)(ii)(D); G-207 164.504(f)(2)(iii) | Moderate | Restricted benefits site; monthly access review | VP of Human Resources | 2026-12-31 |
| Benefits consultant receives plan PHI without a BAA | G-166 164.308(b)(1) | Moderate | BAA or de-identified reports | General Counsel | 2026-11-30 |
| No disposal of Finance customer information | G-122 314.4(c)(6)(i); G-214 501.171(8) | Moderate | Retention schedule and purge | Finance President | 2026-12-31 |
| No lines of communication with subsidiaries | G-010 GV.RM-05; G-014 GV.RR-02 | Moderate | Monthly cyber risk forum; written duties for Presidents | CFO | 2026-11-30 |
| No data map for regulated data | G-037 ID.AM-07; G-118 314.4(c)(2) | Moderate | Data map | GRC Analyst | 2026-12-31 |
| Customer information activity not monitored | G-125 314.4(c)(8); G-089 DE.CM-03 | Moderate | Servicing and warehouse logs to the SIEM; export alerts | Security Manager | 2027-03-31 |

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07).

## 5. Program roadmap
| Phase | Window | Outcomes | Gaps closed (examples) |
|---|---|---|---|
| **1. Stabilize** | 2026 Q4 | Day-1 controls at Home Services North (EDR, end the seller's access); ACH service account vaulted; restricted benefits site; consultant BAA; plan document amendment; monthly cyber risk forum; group tabletop with FTC and plan breach walkthroughs (2026-11-18); retention schedule | GV.RM-05; GV.RR-02; 164.308(a)(3); 164.308(b)(1); 164.314(b); 314.4(c)(6); 314.4(h); 314.4(j) |
| **2. Harden identity and recovery** | 2027 Q1 | Directory tiering and privileged access management; FIDO2 keys; off-site backups and forest recovery test; SIEM sources for servicing, ERP, HRIS, file servers; data map; plant segmentation; North integration complete | PR.AA-03; PR.AA-05; PR.DS-11; RC.RP-03; DE.CM-03; ID.AM-07; PR.IR-01; 314.4(c)(5), (c)(8) |
| **3. Prove** | 2027 Q2 | Quarterly access reviews running; restore tests passing; all 22 critical vendors reviewed; SOC 2 Type 1 for the bank partner (2027-06-30, P09); credit scorecard validated (P10) | GV.SC-07; 314.4(f)(3); 164.308(a)(7)(ii)(D) |
| **4. Sustain** | 2027 Q3-Q4 | SOC 2 Type 2 observation period (from 2027-07-01); second full profile and risk assessment (July 2027); group at CSF Tier 3 | GV.OV-03; ID.IM-02 |

Progress is reported quarterly to the audit committee as rows moving to Met, with the Finance rows in the Qualified Individual's annual report and the plan rows to the Benefits Committee.

## 6. Pending regulatory changes and watch items
- **CIRCIA** (N55-R07) is proposed only. If finalized, recheck the sector criteria and the size-based criterion against the group; do not treat it as a current obligation.
- **HIPAA Security Rule NPRM** (90 FR 898, 2025-01-06) is **proposed only**; the regulatory agenda projects a final rule in July 2027. If finalized as proposed it would affect the plan: the Required and Addressable distinction would be removed (7 addressable gaps become mandatory), all ePHI would need encryption at rest and in transit with limited exceptions, MFA would be required, a written technology asset inventory and network map would be required, certain systems would need restoring within 72 hours, a compliance audit would be needed at least every 12 months, and business associates would have to notify within 24 hours of activating their contingency plan. The `pending_rule_change` column flags each affected row.
- **Safeguards Rule:** no pending amendments found; the FTC notification requirement (314.4(j)) has been in effect since May 13, 2024 (314.5).
- **Structural triggers that would change this analysis:** registering or publicly offering securities (N55-R01 to N55-R03 would apply); acquiring a bank or savings association (N55-R04, N55-R05); moving the plan back to fully insured with summary information only (N55-R06 would narrow); Home Services starting to take or broker credit applications (it could become a financial institution); each acquisition (new data, new rules). The profile is refreshed after any of these.
