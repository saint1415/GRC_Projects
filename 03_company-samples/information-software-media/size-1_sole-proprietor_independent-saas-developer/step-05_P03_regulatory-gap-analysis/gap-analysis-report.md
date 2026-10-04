# Regulatory Gap Analysis: Cris Santos Company | Information | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent B2B SaaS software publisher; online booking and reminders for small appointment-based businesses) |
| Tier / Vertical | Sole Proprietorship / Information |
| Primary analysis | FTC Act Section 5 data security expectations (15 U.S.C. 45(a)), measured against the FTC's own business guidance, plus the security and data-use statements the company makes on its website, in its Terms of Service and DPA, and in questionnaire answers. Rows also carry SOC 2 criterion IDs so the same work prepares for a future SOC 2 examination (P09) |
| Applicability checks only | CCPA/CPRA (N51-R03); COPPA (N51-R02); DOJ Data Security Program (N51-R04); PADFA, FCC CPNI, FedRAMP, SEC (N51-R05 to N51-R08) |
| Assessment dates | 2026-08-24 to 2026-08-28 (self-assessment; tests on 2026-08-27 with the contract security consultant) |
| Assessor | Owner-developer. Evidence is self-attested, checked on screen with the consultant where possible |
| Adopted | 2026-09-25 |

## 1. Applicability

### 1.1 FTC Act Section 5 applies
Section 5(a) declares "unfair or deceptive acts or practices in or affecting commerce" unlawful (15 U.S.C. 45(a)(1)). The company is a for-profit software business selling to subscribers in 11 states. It is not in any statutory carve-out (banks, savings and loans, federal credit unions, common carriers, air carriers), and **there is no size threshold** (N51-R01). A one-person business is covered the same way a large one is. Both FTC theories matter here:
- **Unfairness:** a practice is unfair if it "causes or is likely to cause substantial injury to consumers which is not reasonably avoidable by consumers themselves and not outweighed by countervailing benefits to consumers or to competition" (15 U.S.C. 45(n)). The 88,000 end clients whose names, phone numbers, and service notes sit in the platform cannot protect that data themselves.
- **Deception:** a material representation, omission, or practice likely to mislead a consumer acting reasonably. The website security page, the Smart Replies release note, the DPA, and questionnaire answers are representations to subscribers.

Section 5 lists no specific controls. The requirement set is the FTC's own business guidance (the same sources the Information Small sample uses, checked there on 2026-09-26):

| Source | URL | Rows |
|---|---|---|
| Start with Security: A Guide for Business (10 lessons, 28 practices) | https://www.ftc.gov/business-guidance/resources/start-security-guide-business | G-001 to G-028 |
| Protecting Personal Information: A Guide for Business | https://www.ftc.gov/business-guidance/resources/protecting-personal-information-guide-business | G-029, G-030 |
| Data Breach Response: A Guide for Business | https://www.ftc.gov/business-guidance/resources/data-breach-response-guide-business | G-031 |
| The company's own statements and contract promises | Website, release note, Terms of Service, DPA, questionnaire answers | G-032 to G-040 |

### 1.2 SOC 2 applies only by customer request
SOC 2 is not a law. The company has no SOC 2 report, and a sole proprietor rarely needs one. Two larger subscribers have asked for one, and the owner has called it "planned" in questionnaire answers (G-040). This analysis therefore tags each row with related Trust Services Criteria IDs (author mapping; criteria cited by ID only) and leaves criterion-by-criterion readiness to P09.

### 1.3 CCPA applicability check (no gap table)
| Test (N51-R03) | Threshold | Company | Result |
|---|---|---|---|
| "Business" (Cal. Civ. Code 1798.140(d)) | Annual gross revenue over $26,625,000 (CPI-adjusted, effective 2025-01-01); or buys, sells, or shares personal information of 100,000 or more consumers or households; or 50% or more of revenue from selling or sharing personal information | About $180,000 revenue; sells no personal information; revenue comes from subscriptions | **Not a business.** The CCPA's direct duties, cybersecurity audit, and risk assessment rules do not apply |
| Service provider terms | Apply by contract if a subscriber is itself a CCPA business | Subscribers are small local businesses; none is known to meet a threshold | No action now. If a subscriber asks for CCPA service-provider terms, the existing DPA use limits already match (G-034, G-036) |

### 1.4 Other checks
- **COPPA (N51-R02): not applicable.** The booking pages are general-audience pages used by adults to book services. When a child gets a haircut, the parent books with the parent's own details. The service is not directed to children under 13 and the owner has no actual knowledge of collecting their information. Recheck if a subscriber offers children's classes with child profiles.
- **DOJ Data Security Program (N51-R04): not applicable.** The rule restricts covered data transactions that give countries of concern or covered persons access to bulk U.S. sensitive personal data. The company has no such transactions: no offshore contractors or hosting, and every sub-processor is U.S.-based. Its data is mostly contact data, and "demographic or contact data that is linked only to other demographic or contact data" is excluded from covered personal identifiers (28 CFR 202.212(b)(1)); the 88,000 records are also below the 100,000-person bulk threshold (28 CFR 202.205(f)). Verified against eCFR on 2026-10-04.
- **PADFA, FCC CPNI, FedRAMP, SEC (N51-R05 to N51-R08): not applicable.** The company is not a data broker, not a carrier, has no federal customers, and is not a public company.
- **State breach laws** apply to the company as a service provider ("third-party agent" in Florida, Fla. Stat. 501.171(6)) and are handled in P08, not here.

## 2. Method
1. **Requirements.** Each practice in the three FTC guides became one row, cited by guide, lesson, and practice heading (FTC guidance is a U.S. government work, so headings are quoted). Each public statement or contract promise became one deception row.
2. **Crosswalk.** Each row maps to CSF 2.0, SP 800-53 Rev. 5, and related SOC 2 criterion IDs. This is an **author mapping**; no official NIST or FTC mapping of this guidance exists.
3. **Evidence.** Self-attested by the owner and checked on screen where possible: account and role lists, the secret scan and configuration review on 2026-08-27, the website captured on 2026-08-25, the uptime monitor report, vendor terms, and the Terms of Service and DPA.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale.

## 3. Results summary
| Requirement set | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| FTC Start with Security (reasonable security) | 28 | 6 | 13 | 8 | 1 |
| FTC Protecting Personal Information | 2 | 0 | 2 | 0 | 0 |
| FTC Data Breach Response | 1 | 0 | 1 | 0 | 0 |
| Deception: public statements and contract promises | 9 | 1 | 3 | 5 | 0 |
| **Total** | **40** | **7** | **19** | **13** | **1** |

Of the 32 rows that are not met or partially met, 4 are rated High, 24 Moderate, and 4 Low. The one N/A row is G-025 (paper and removable media), because the company keeps none.

**The main finding.** The owner's technical habits are sound where the FTC guidance starts (encryption, standard methods, framework security defaults, brute-force limits). The gaps are where a one-person business cuts corners: plaintext production secrets (G-007), real data on the laptop and in AI prompts (G-003), no monitoring (G-014), and **public statements that are not true** (G-034, G-035, G-040). The deception rows are the cheapest to fix and the easiest for a regulator or subscriber to prove, so they come first.

## 4. Action list (half page)
In order. The first four cost nothing and take under a day.

| # | Action | Rows | Gap risk | Target |
|---|---|---|---|---|
| 1 | Correct the website security page ("never share", "99.9%", "bank-level") and the questionnaire answers | G-034, G-035, G-032, G-040 | High | 2026-10-15 |
| 2 | Move secrets out of the `.env` file, rotate all of them, turn on secret scanning with push protection | G-007 | High | 2026-10-31 |
| 3 | Delete the laptop data copy; send the model only the fields a reply needs | G-003 | High | 2026-10-31 |
| 4 | Add the model provider to the sub-processor list with 14 days' notice; sign its DPA | G-037, G-036, G-021 | Moderate | 2026-10-31 |
| 5 | Subscriber security contact list, notice templates, and a runbook walkthrough | G-031, G-039, G-030 | Moderate | 2026-10-31 |
| 6 | Fix the 2 high-severity library alerts; monthly triage | G-023 | Moderate | 2026-10-31 |
| 7 | Hosting log review, sign-in alerts, admin action log, 12-month log retention | G-014 | High | 2026-11-30 |
| 8 | Owner-only super-admin with MFA; named support role for the contractor | G-005, G-004, G-016 | Moderate | 2026-11-30 |
| 9 | Delete the 31 closed accounts and their photos; automated deletion | G-038, G-002, G-019 | Moderate | 2026-11-30 |
| 10 | Tenant isolation tests and a second isolation layer | G-009, G-013 | Moderate | 2027-03-31 |

High and Moderate gaps are in the risk register (P01) and the POA&M (P07). The full list is in `gap-analysis.csv`.

## 5. Pending and watch items
- **FTC staff views on AI and data use** (Office of Technology blog posts, 2024-01-09 and 2024-02-13, as cited in the Information Small sample): companies that promise not to use customer data for other purposes, such as model training, must keep that promise, and quietly changing terms to allow AI use may be unfair or deceptive. These are staff views, not rules, but they explain why G-036 and G-037 matter.
- **CCPA thresholds:** recheck each January. The company is very far from the revenue threshold, so this changes only if it starts selling or sharing personal information.
- **Colorado SB26-189 and the CPPA ADMT rules** (effective or compliance dates 2027-01-01) concern automated decisions with significant or consequential effects. Smart Replies makes no such decisions (P10), so neither applies today. Recheck before any feature that ranks, prices, or screens end clients.
