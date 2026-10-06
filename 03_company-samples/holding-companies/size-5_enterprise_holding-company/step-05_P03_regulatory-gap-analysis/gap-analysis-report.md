# Regulatory Gap Analysis: Cris Santos Company | Management of Companies and Enterprises | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded holding company with four operating subsidiaries; six states) |
| Tier / Vertical | Enterprise / Management of Companies and Enterprises |
| Regulations analyzed | SEC Regulation S-K Item 106 and Form 8-K Item 1.05; Exchange Act Rule 13a-15 and SOX section 404; FTC Safeguards Rule (Finance, reaching the holding company as service provider); HIPAA plan sponsor duties for the self-insured group health plan; state breach and data security laws (Florida worked example); and the vertical's voluntary benchmark, a **NIST CSF 2.0 group profile** (Govern function) with subsidiary profiles |
| Applicability checks | Federal Reserve Regulation Y Subpart N; 12 CFR Part 225 Appendix F; CIRCIA (proposed); Florida Digital Bill of Rights |
| Assessment dates | 2026-05-04 to 2026-07-17 (evidence sampling completed 2026-07-31) |
| Assessors | GRC team (second line) with the Chief Compliance Officer and the Finance Information Security Officer; SEC and SOX rows reviewed with the Chief Accounting Officer and outside securities counsel; sampling reperformed by Internal Audit for 6 rows |
| Approved | Chief Compliance Officer and CISO, 2026-08-21; roadmap reviewed by the joint audit and risk committee session, 2026-09-17 |
| Files | `gap-analysis.csv` (99 rows); `subsidiary-profiles.csv` (22 CSF categories for the group and 4 subsidiaries) |

## 1. Applicability
A holding company's cyber obligations come from what it is (public or private, bank holding company or not) and from what its subsidiaries do. Each candidate requirement was checked against its primary text (eCFR, version of 2026-09-23; Federal Register text of SEC Release 33-11216).

| Requirement | Applies? | Basis |
|---|---|---|
| **N55-R01** Reg S-K Item 106 (17 CFR 229.106) | **Yes** | SEC registrant filing Form 10-K. Item 106 is disclosed in 10-K Item 1C. No size relief applies to Item 106 |
| **N55-R02** Form 8-K Item 1.05 | **Yes** | SEC registrant; not a smaller reporting company. Filing is due within four business days after the materiality determination (General Instruction B.1 as amended) |
| **N55-R03** SOX section 404 (15 U.S.C. 7262) and Rule 13a-15 | **Yes, including 404(b)** | Large accelerated filer, so the auditor attestation in 7262(b) applies. Rule 13a-15(a)-(d) sets the quarterly disclosure controls evaluation and the annual ICFR evaluation |
| **N55-R04** Federal Reserve incident notification (12 CFR 225.300-225.303) | **No** | Scope is bank holding companies, savings and loan holding companies, and the other entities in 225.300(c). No subsidiary is a bank or savings association; Finance takes no deposits |
| **N55-R05** 12 CFR Part 225, Appendix F | **No** | Same reason. Finance is covered by the FTC Safeguards Rule instead |
| **N55-R06** HIPAA (group health plan) | **Yes, as plan sponsor** | The self-insured plan (about 21,000 covered lives) is a covered entity. The holding company receives PHI for plan administration (appeals, stop-loss), so the plan-document restrictions in 164.504(f) and the security provisions in 164.314(b) apply. The 164.314(b) exception for summary and enrollment information does not cover this use. The plan's own Security Rule program (risk analysis, TPA oversight) is run by the benefits program and is outside this analysis |
| **N55-R07** CIRCIA (proposed 6 CFR Part 226) | **Not in force** | Proposed only; no final rule as of 2026-09-25. If finalized as proposed, the group would likely meet the size-based criterion; recheck when final |
| **FTC Safeguards Rule** (16 CFR Part 314) | **Yes, for Finance; reaches the holding company** | Finance is a financial institution (314.1(b); 314.2(h)) with customer information on about 520,000 consumers, so the 314.6 exception does not apply. GBS receives, maintains, and processes Finance customer information through shared identity, email, files, ACH, and bank connectivity, so it is Finance's service provider (314.2(r); 314.4(f)). Finance employs its own Qualified Individual, so the affiliate provisions in 314.4(a)(1)-(3) do not apply |
| State breach and data security laws | **Yes** | Each state where affected individuals reside. Florida (Fla. Stat. 501.171) is the worked example: every group company must take reasonable measures (501.171(2)) and dispose of records it no longer keeps (501.171(8)); GBS is a third-party agent for each subsidiary (501.171(6)) |
| Florida Digital Bill of Rights (Fla. Stat. 501.702) | **No** | A controller must exceed $1 billion in global gross annual revenue **and** earn 50% or more of revenue from online advertising, operate a consumer smart speaker and voice command service, or operate an app store with at least 250,000 applications. The group passes the revenue test but meets none of the three others |
| PCI DSS | Contractual | Assessed each year by the separate PCI program; not repeated here |
| FAR reporting clauses | **No** | No federal contracts or subcontracts |

**Why the CSF 2.0 group profile is still included.** The vertical's benchmark for holding companies is a CSF 2.0 group profile with a Govern emphasis. At this size it does a second job: Item 106 requires the 10-K to describe the group's risk management processes, board oversight, and management's role, and the Govern outcomes are the evidence behind those statements. Rows G-001 to G-010 test the disclosure; rows G-066 to G-096 test the practices it describes.

## 2. Method
1. **Decompose.** Item 106 and Rule 13a-15 were broken into paragraph-level duties from the eCFR text. Form 8-K Item 1.05, its instructions, and General Instruction B.1 come from the Federal Register text of Release 33-11216 (88 FR 51896). Safeguards Rule rows follow 16 CFR 314.3 and 314.4 paragraph by paragraph. HIPAA rows follow 164.504(f) and 164.314(b). The Govern function has all 31 subcategories.
2. **Crosswalk.** CSF rows use NIST's official CSF 2.0 to SP 800-53 Rev. 5.2.0 informative references (`nist_official_sp800_53r5`; key controls in `sp800_53_controls`). All other rows are **author mappings** to CSF 2.0 and SP 800-53 (NIST publishes no official mapping for these rules) and are labeled that way in `crosswalk_source`.
3. **Evidence sampling.** Where a requirement operates on a population, the team tested a sample and recorded the population, sample size, and exceptions in the CSV. Large populations of manual activity used 60 items (95% confidence, 5% tolerable deviation, zero expected deviations); smaller or lower-risk populations used 25 items; account and configuration data were tested in full with analytics. Selections were random. **21 rows were tested by sampling or full-population analytics; 12 found exceptions.**
4. **Rate.** Met, Partially met, Not met, or Not applicable. CSF rows also carry a 1-5 rating (1 not performed; 2 informal; 3 defined but not consistent across the group; 4 consistent across the group; 5 measured and improving) and map to status as 4-5 Met, 2-3 Partially met, 1 Not met. Each gap is rated with the P01 scale and carries an owner and date. High gaps are in the P01 register and the P07 POA&M.

**CSF tiers and targets.** The group operates at **CSF Tier 3 (Repeatable)** at the group level. The target is a rating of 4 in every category for the group and every subsidiary by 2027-12-31 (`subsidiary-profiles.csv`).

## 3. Results summary
| Regulation / section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| SEC Regulation S-K Item 106 (N55-R01) | 7 | 3 | 0 | 0 | 10 |
| SEC Form 8-K Item 1.05 (N55-R02) | 4 | 3 | 0 | 0 | 7 |
| Exchange Act Rule 13a-15 and SOX section 404 (N55-R03) | 4 | 2 | 0 | 0 | 6 |
| FTC Safeguards Rule (Finance) | 19 | 9 | 0 | 1 | 29 |
| HIPAA plan sponsor (N55-R06) | 3 | 5 | 0 | 0 | 8 |
| State breach and data security laws | 2 | 2 | 0 | 1 | 5 |
| NIST CSF 2.0 group profile, Govern | 18 | 13 | 0 | 0 | 31 |
| Applicability checks (N55-R04, N55-R05, N55-R07) | 0 | 0 | 0 | 3 | 3 |
| **Total** | **57** | **37** | **0** | **5** | **99** |

**Gap risk levels (37 partially met rows):** High 9, Moderate 22, Low 6.

**What the results say.** No requirement is wholly unmet; this is a mature program with targeted gaps. The gaps cluster in four places:
1. **The outsourced service desk** shows up in five regimes at once: Item 106 (third-party oversight, G-004), the Safeguards Rule (MFA, provider selection and contracts, G-035, G-046, G-047), and the Govern profile (G-070, G-090, G-091).
2. **Materiality and escalation across subsidiaries** (G-008, G-011, G-013, G-015, G-019, G-075).
3. **Data minimization at Finance** (G-031, G-036, G-062).
4. **The plan sponsor firewall** for the self-insured health plan (G-055 to G-058).

**Subsidiary profiles.** The group profile is rated 4 in 12 of 22 categories and 3 in 10. Building Products and Home Services sit close to the group because they inherit almost everything from GBS; Home Services is rated 2 in PR.AA (branch payables conflicts). Manufacturing has the most gaps (4 categories rated 2: ID.AM, PR.PS, PR.IR, DE.CM), all in plant OT. Finance is rated 4 in 18 categories, reflecting its Safeguards Rule program.

## 4. Priority gaps (High)
| Row | Citation | Gap | Action | Owner | Target |
|---|---|---|---|---|---|
| G-004 | 17 CFR 229.106(b)(1)(iii) | 18 of 64 tier-1 vendor reassessments overdue; disclosed annual cycle not fully operating | Clear backlog; re-tier the service desk; align Item 1C wording (POAM-012; POAM-013) | Director of Third-Party Risk Management | 2027-02-15 |
| G-011 | Form 8-K Item 1.05, Instruction 1 | Playbook does not cover subsidiary, OT, or vendor-originated incidents or aggregation; not exercised since 2025-03 | Playbook update; correlation review; tabletop 2026-11-19 (POAM-011) | General Counsel | 2026-11-30 |
| G-031 | 16 CFR 314.4(c)(1)(ii) | Full SSNs in the warehouse; 2 Finance sites shared group-wide and reachable by the AI assistant | Tokenize SSNs (POAM-022); restrict and label sites (POAM-024) | Finance Information Security Officer | 2026-12-31 |
| G-035 | 16 CFR 314.4(c)(5) | MFA can be reset by the service desk after knowledge-based checks | Verified identity proofing (POAM-001); phishing-resistant MFA for administrators (POAM-002) | Director of Identity and Access Management | 2026-12-15 |
| G-046 | 16 CFR 314.4(f)(1) | Service desk mis-tiered and selected without a verification requirement | Re-tier and reassess (POAM-012) | Director of Third-Party Risk Management | 2026-12-31 |
| G-047 | 16 CFR 314.4(f)(2) | Service desk contract lacks verification standard and audit rights | Contract amendment (POAM-012) | Director of Third-Party Risk Management | 2026-12-31 |
| G-070 | CSF GV.OC-05 | Service desk not recognized as a critical dependency | Tier-1 contingency planning (POAM-012) | Director of Third-Party Risk Management | 2026-12-31 |
| G-090 | CSF GV.SC-04 | Tiering criteria ignore identity and payment functions | Revise criteria; re-tier (POAM-012) | Director of Third-Party Risk Management | 2026-12-31 |
| G-091 | CSF GV.SC-05 | Older contracts lack security and notice terms | Amend at renewal; service desk now (POAM-012) | Director of Third-Party Risk Management | 2026-12-31 |

The full list, with evidence and samples, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07): POAM-021 to POAM-024 were opened from this analysis.

## 5. Compliance roadmap
| Quarter | Milestones | Regulations served | Evidence produced |
|---|---|---|---|
| 2026 Q4 | Disclosure committee tabletop and playbook update (POAM-011); service desk identity proofing and contract amendment (POAM-001; POAM-012); restricted plan site and plan document amendment (POAM-023); AI site labeling (POAM-024); Q3 change memo on AQ uploads (G-021); state law matrix refresh (G-064) | Item 1.05; Rule 13a-15(b), (d); 16 CFR 314.4(c)(1)(ii), (c)(5), (f); 45 CFR 164.314(b), 164.504(f) | Tabletop report; amended contract; plan amendment; label coverage report |
| 2027 Q1 | Tier-1 vendor backlog cleared (POAM-013); warehouse SSN tokenization and purge (POAM-022); dealer account inactivity control (G-030); Internal Audit review of the FY2026 Item 1C draft (G-001); phishing-resistant MFA for all privileged accounts (POAM-002); integration platform logging and warehouse egress analytics (POAM-009, due 2027-01-31) | Item 106(b)(1), (b)(1)(iii); 16 CFR 314.4(c)(1)(i), (c)(5), (c)(6), (c)(8), (f)(3) | Vendor reviews; purge reports; Item 1C evidence map; log source list |
| 2027 Q2 | AQ-02 migration to the group ERP (2027-04); added IT audit capacity and a three-year rotation (G-080, due 2027-06-30) | Rule 13a-15(d); CSF GV.RR-03, GV.OV-02 | Migration sign-off; Internal Audit plan |
| 2027 Q3 | Annual gap reassessment; refresh subsidiary profiles; recheck CIRCIA status | All | Updated P03 |

## 6. Pending regulatory changes and watch items
- **CIRCIA** (N55-R07) is proposed only. The final rule had not been published as of 2026-09-25. Reporting to CISA stays voluntary until it takes effect; do not treat it as a current obligation.
- **SEC:** a 2025 petition asks the SEC to rescind Item 1.05. No SEC proposal to amend or rescind was found as of 2026-09-25, so Item 1.05 and Item 106 remain in force.
- **Safeguards Rule:** no pending amendments found; the FTC notification requirement (314.4(j)) has applied since May 13, 2024.
- **Structural triggers that would change this analysis:** acquiring a bank or savings association (N55-R04 and N55-R05 would apply); Finance becoming subject to a banking regulator; moving the health plan to fully insured with summary-only information (164.314(b) would narrow); entering a new state (state law matrix).

## 7. Regulator-ready package
The GRC team keeps an evidence binder in the GRC platform, indexed by `req_id`, so the group can respond quickly to an SEC comment letter, an FTC inquiry about Finance, an HHS inquiry about the plan, or a state attorney general:
- this report, `gap-analysis.csv`, `subsidiary-profiles.csv`, and the sample selections with exceptions for every sampled row;
- the P01 register, P02 SSP, P05 BIA, P06 policy set, P07 assessment and POA&M, and P08 runbook and notification matrix;
- disclosure committee minutes, sub-certifications, and the Item 1C evidence map;
- Finance's WISP, risk assessment, and Qualified Individual reports;
- the plan documents, sponsor certification, and the benefits access reviews;
- records kept at least 7 years (POL-01 4.11).

## 8. Approval
Approved by the Chief Compliance Officer and the CISO on 2026-08-21. The roadmap was reviewed by the joint session of the audit committee and the risk committee on 2026-09-17. Next reassessment: 2027-05 to 2027-07.
