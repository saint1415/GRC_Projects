# Regulatory Gap Analysis: Cris Santos Company | Information | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (B2B SaaS software publisher, workforce scheduling and timekeeping platform) |
| Tier / Vertical | Small / Information |
| Primary analysis | FTC Act Section 5 data security expectations (15 U.S.C. 45(a)), measured against the FTC's own business guidance, plus the security and data-use commitments the company makes in its website, MSA, DPA, and SOC 2 system description |
| Applicability checks only | CCPA/CPRA (N51-R03); DOJ Data Security Program (N51-R04) |
| Assessment dates | 2026-08-10 to 2026-08-21 |
| Assessor | IT Manager (security and compliance lead) with the COO (privacy lead); outside privacy counsel reviewed sections 1 and 5 |

## 1. Applicability

### 1.1 FTC Act Section 5 applies
Section 5(a) declares "unfair or deceptive acts or practices in or affecting commerce" unlawful (15 U.S.C. 45(a)(1)). The company is a for-profit software publisher selling across state lines. It is not in any of the statutory carve-outs (banks, savings and loans, federal credit unions, common carriers, air carriers), and there is no size threshold (N51-R01). The FTC uses two theories in data security cases, and both are relevant here:
- **Unfairness:** a practice is unfair if it "causes or is likely to cause substantial injury to consumers which is not reasonably avoidable by consumers themselves and not outweighed by countervailing benefits to consumers or to competition" (15 U.S.C. 45(n)). Workers whose schedules, contact details, and pay rates sit in the platform cannot protect that data themselves; only the company can.
- **Deception:** a material representation, omission, or practice likely to mislead a consumer acting reasonably (FTC Policy Statement on Deception, as summarized on the FTC's enforcement authority page). The company's security page, DPA, and questionnaire answers are representations.

Section 5 does not list specific controls. The FTC explains what it expects through business guidance drawn from its cases. This analysis uses three FTC guidance documents as the requirement set (all URLs checked on 2026-09-26):

| Source | URL | Used for |
|---|---|---|
| Start with Security: A Guide for Business (10 lessons, 28 practices) | https://www.ftc.gov/business-guidance/resources/start-security-guide-business | G-001 to G-028 |
| Protecting Personal Information: A Guide for Business (5 principles) | https://www.ftc.gov/business-guidance/resources/protecting-personal-information-guide-business | G-029, G-030 |
| Data Breach Response: A Guide for Business | https://www.ftc.gov/business-guidance/resources/data-breach-response-guide-business | G-031 |
| FTC enforcement authority page (Section 5 tests) | https://www.ftc.gov/about-ftc/mission/enforcement-authority | Deception and unfairness tests |
| FTC data security guidance hub | https://www.ftc.gov/business-guidance/privacy-security/data-security | Index of guidance and cases |

### 1.2 SOC 2 commitments apply by contract
SOC 2 is not a law. It applies because customers require it and the MSA promises a current SOC 2 report. What makes the SOC 2 work a Section 5 matter is the overlap: statements in the SOC 2 system description, DPA, and website are representations, so a control that does not operate as described is both a SOC 2 exception and a deception risk. Rows G-032 to G-042 test those commitments. Criterion-by-criterion readiness for the Type 2 is **not** repeated here; it is in P09, which reuses the `related_tsc_criteria` column of this analysis.

### 1.3 CCPA applicability check (no gap table)
| Test | Threshold (N51-R03; cross-sector file) | Company | Result |
|---|---|---|---|
| "Business" (Cal. Civ. Code 1798.140(d)) | Annual gross revenue over $26,625,000 (CPI-adjusted, effective 2025-01-01), or other tests | $28.2 million; does business in California | **Is a business** for personal information it collects for its own purposes (its employees, customer contacts, prospects) |
| Service provider (Cal. Civ. Code 1798.140) | Processes personal information on behalf of a business under a written contract | Processes about 9,500 California workers' data for customers under DPAs with service-provider terms | **Acts as a service provider** for customer worker data; the use limits are tested in G-038 |
| Cybersecurity audit (Cal. Code Regs. tit. 11, 7120) | Revenue test met and, in the prior year, personal information of 250,000 or more consumers or households, or sensitive personal information of 50,000 or more consumers | About 9,500 California workers plus a small number of its own California contacts | **Not triggered** at current volumes. Counsel noted it is unsettled whether service-provider processing counts; even if it does, the count is far below the threshold. Recheck each January |
| Risk assessments and ADMT rules | Apply to listed processing and to ADMT used for significant decisions | Customers may use the AI shift-swap feature in employment decisions | Handled in P10 as a customer-driven requirement |

By decision (vertical profile, 2026-09-26), the CCPA stays an applicability check and is not decomposed into a gap table.

### 1.4 DOJ Data Security Program check
28 CFR Part 202 restricts covered data transactions (data brokerage, vendor, employment, and investment agreements) that give countries of concern or covered persons access to bulk U.S. sensitive personal data. The platform's roughly 140,000 worker profiles could exceed the 100,000-person bulk threshold for covered personal identifiers, depending on which data elements qualify. The company has **no** covered data transactions today: no offshore staff or hosting, and all 6 sub-processors are U.S.-based. Action: add a Data Security Program question to sub-processor reviews (P01 R-034, P09).

### 1.5 Not applicable
COPPA (N51-R02), FCC CPNI (N51-R06), FedRAMP (N51-R07), SEC disclosure (N51-R08), and PADFA (N51-R05) do not apply; reasons are in `../scenario-facts.md` section 1. The FTC Health Breach Notification Rule does not apply because the platform holds no health records. State breach laws are handled in P08.

## 2. Method
1. **Requirements.** Each practice in the three FTC guides became one row, cited by guide, lesson, and practice heading (FTC guidance is a U.S. government work, so headings are quoted). Each commitment the company makes publicly or by contract became one deception row.
2. **Crosswalk.** Each row was mapped to CSF 2.0, SP 800-53 Rev. 5, and related SOC 2 criterion IDs. This is an **author mapping**: no official NIST or FTC mapping of this guidance exists. SOC 2 criteria are listed by ID only (the AICPA text is copyrighted).
3. **Evidence.** Interviews (CTO, Platform Engineering Lead, Engineering Manager, Customer Support Manager, COO, Director of Product), configuration exports, the SOC 2 Type 1 report, contracts, the website security page captured on 2026-08-12, and an office walkthrough on 2026-08-13.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale.

## 3. Results summary
| Requirement set | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| FTC Start with Security (reasonable security) | 28 | 8 | 15 | 5 | 0 |
| FTC Protecting Personal Information | 2 | 0 | 2 | 0 | 0 |
| FTC Data Breach Response | 1 | 0 | 1 | 0 | 0 |
| Deception: security and data-use representations and commitments | 11 | 1 | 6 | 4 | 0 |
| **Total** | **42** | **9** | **24** | **9** | **0** |

Of the 33 rows that are not met or partially met, 6 are rated High, 24 Moderate, and 3 Low.

**The main finding.** The company's controls are reasonable in most places the FTC's guidance looks first (encryption, endpoints, authentication for its own staff). The gaps are where the guidance draws on cases most like this company: a shared, fully privileged cloud credential; real personal data used for development; one client's users able to reach another client's data; and no monitoring of data leaving the network. Of the six High gaps, three (G-003, G-005, G-007) are the same weaknesses as SOC 2 Type 1 exceptions 1 and 2 and the P08 incident scenario. Two (G-013, G-014) are the tenant isolation and monitoring gaps. The sixth (G-032) is a deception gap: the security page says every access is logged, which is not true for the shared role.

## 4. Priority gaps and roadmap
| Gap | Row | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Shared break-glass role and broad CI keys | G-005 | High | Named just-in-time access with session recording; scoped short-lived CI credentials | CTO | 2026-10-23 |
| Static cloud keys never rotated; no secret scanning | G-007 | High | Federated short-lived CI credentials; push protection | Platform Engineering Lead | 2026-10-16 |
| Security page claims every access is logged | G-032 | High | Correct the page now; restore only after session recording is live | COO | 2026-10-15 |
| Real worker data in staging and in AI prompts | G-003 | High | Purge staging copies; masked or synthetic data; remove names from prompts | Engineering Manager | 2026-10-30 |
| No monitoring of data leaving the platform | G-014 | High | Threat detection; bulk-read and snapshot alerts; 1-year log archive | Platform Engineering Lead | 2026-11-30 |
| Tenant isolation only in application code | G-013 | High | Database-level second layer; isolation merge gate | Engineering Manager | 2027-01-31 |
| Model provider added with 12 days' notice and no DPA | G-036, G-021 | Moderate | Re-notice with 30-day objection window; signed DPA | COO | 2026-10-31 |
| No sub-processor verification | G-022 | Moderate | Tiered review program (P09) | COO | 2026-10-30 |
| Terminated customers' data kept past 90 days | G-037, G-002 | Moderate | Delete 14 tenants; automated deletion | Engineering Manager | 2026-11-30 |
| Unsubstantiated "fair and unbiased" AI claim | G-042 | Moderate | Withdraw the claim; P10 testing | Director of Product | 2026-10-15 |

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07). Readiness gates for the SOC 2 Type 2 are in P09.

## 5. Pending and watch items
- **FTC proposed AI-accuracy policy statement** (Docket FTC-2026-0727; press release 2026-07-01; comments closed 2026-07-31): **not final** as of 2026-09-25. It would treat steering of AI outputs away from accuracy as potential deception. Flagged on G-033 and G-042; not treated as a current obligation.
- **FTC staff views on AI and data use** (Office of Technology blog, 2024-01-09 and 2024-02-13): staff state that companies that promised not to use customer data for other purposes, such as model training, must keep that promise, and that changing terms quietly to allow AI use may be unfair or deceptive. These are staff views, not rules, but they explain why G-033 and G-036 matter.
- **CCPA cybersecurity audits:** not triggered today (section 1.3). If they become triggered, the first report for a business under $50 million revenue would be due 2030-04-01 (based on 2028 revenue).
- **CPPA ADMT rules:** compliance for existing ADMT uses by 2027-01-01. This falls on customers that are CCPA businesses using the shift-swap feature for significant decisions; the company's supporting duties are in P10.
