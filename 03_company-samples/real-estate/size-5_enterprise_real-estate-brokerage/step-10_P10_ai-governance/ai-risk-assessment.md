# AI Governance Risk Assessment: Enterprise AI Portfolio and Automated Tenant and Buyer Screening

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded residential real estate brokerage with title and settlement, property management, and relocation lines; 9 states) |
| Tier / Vertical | Enterprise / Real Estate and Rental and Leasing |
| Scope | Enterprise AI portfolio (12 use cases in `ai-use-case-inventory.csv`), with full assessments of AI-001 automated tenant screening (section 7) and AI-002 buyer lead scoring and pre-qualification (section 8) |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (NIST AI 600-1) for AI-002, AI-004, AI-005, AI-008, and AI-010; repository risk tier rubric (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`) |
| Assessor / date | AI governance committee (chaired by the Chief Data Officer), meeting of 2026-08-26; GRC team prepared the portfolio review |
| Decision | Executive risk committee, 2026-09-08 (section 10) |

## 1. Portfolio summary
| Measure | Result |
|---|---|
| Use cases in the inventory | 12 |
| Risk tier | High 2, Medium 7, Low 3 |
| Status | In production 10, Pilot 2 |
| Committee review complete | 7 of 12 |
| Not yet reviewed | 5: AI-003, AI-006, AI-008, AI-011, AI-012 (all due 2026-11-30, POAM-019) |
| Use cases in scope of state ADMT laws from 2027-01-01 | AI-001 (California and Colorado); AI-003 possible (California, independent contractor compensation; under review) |
| Use cases with a fairness disparity flagged in 2026 | 2: AI-001 (approval ratio) and AI-002 (response time by language) |

**Main findings:** one of the two High-tier use cases, agent recruiting and retention scoring (AI-003), has run for a year without committee review and may make significant decisions about independent contractors' compensation under the California rules. Tenant screening (AI-001) is in practice the decision, shows an approval-rate disparity on the first local test, and needs notices, an appeal path, and records in California and Colorado before 2027-01-01. Buyer lead scoring (AI-002) slows first contact for Spanish-language inquiries.

## 2. GOVERN: AI governance committee operating model
**Charter.** The AI governance committee was formed in 2025 under POL-01 and reports to the executive risk committee. Its risks roll up to enterprise risk ER-08 (P01), which the board risk committee reviews quarterly.

**Members:** Chief Data Officer (chair); Chief Privacy Officer; CISO; Chief Compliance Officer (fair housing, RESPA, and FCRA); General Counsel's delegate; President, Property Management; Executive Vice President, Brokerage Operations; Vice President, Consumer Digital; Chief Human Resources Officer (for workforce and agent tools); the data science lead. Internal Audit observes.

**Decision rights by tier:**
| Tier | Who approves | Required before production |
|---|---|---|
| High | Committee vote, then the executive risk committee | Local validation and disparate outcome testing on the company's data; fair housing and FCRA review by the Chief Compliance Officer; CPPA-format risk assessment where California applies; human review design; consumer notices; monitoring plan |
| Medium | Committee vote | Human oversight design; output quality monitoring; AI disclosure where people interact with it; privacy and security review |
| Low | Committee chair (fast track) | Approved-tool listing; data handling rules (POL-04) |

**Intake and inventory.** Any new AI use, including AI features switched on inside existing vendor products, must be registered before use (POL-05 4.5; STD-05.3). Since 2026-06, procurement and IT change management block AI features without an inventory ID. The GRC team owns the inventory.

**Policies:** POL-05 4.5 (customer and client information only in approved AI tools); POL-04 4.1 (Restricted data); POL-01 4.8 (vendor tiering and contract terms, including no training on company data); STD-05.3 (approved AI tools list).

**Cadence:** monthly committee meetings; quarterly monitoring review for every High-tier tool; annual re-review of every use case.

**Why 5 use cases lack review.** Three entered through vendor feature releases before the intake block existed (AI-006, AI-011, AI-012), one started as an analytics project (AI-003), and one is a pilot (AI-008). The committee set review dates for all five (section 10).

## 3. MAP: context and applicable rules
| Rule | Applies? | Why |
|---|---|---|
| Fair Housing Act (42 U.S.C. 3604; 3605) | **Yes** | Rental decisions and their terms (AI-001), brokerage services and statements (AI-002, AI-004, AI-005), and valuations used in brokering (AI-006) may not discriminate because of race, color, religion, sex, familial status, national origin, or disability. Disparate impact claims are cognizable under the Act (*Texas Dept. of Housing and Community Affairs v. Inclusive Communities Project*, 576 U.S. 519 (2015)) |
| HUD discriminatory effects rule (24 CFR 100.500) | **Yes, for now** | In force. HUD proposed changing its implementation of the disparate impact standard on 2026-01-14 (91 FR 1475) and in a supplemental proposal on 2026-08-10 (91 FR 51416). Both are proposals; neither removes disparate impact liability under the statute |
| State fair housing laws | Yes | Each state where the company manages homes or brokers sales; Florida worked example: Fla. Stat. 760.23 |
| FCRA (15 U.S.C. 1681m(a); 16 CFR 682.3) | **Yes, for AI-001** | Adverse action notices for declines and for conditional approvals based on a consumer report; secure disposal of reports |
| CCPA ADMT and risk assessment rules (Cal. Code Regs. tit. 11, 7150-7157; 7200-7222) | **Yes, for AI-001 in California; under review for AI-003** | Housing and independent contracting compensation are significant decisions. Compliance for existing uses by 2027-01-01 (7200(b)); risk assessments for existing processing by 2027-12-31 (7155(b)). The FCRA exemption (Civ. Code 1798.145(d)) covers the consumer report itself but not the screening model's use of application data (P03 section 1.3) |
| Colorado SB26-189 (C.R.S. 6-1-1701 to 6-1-1709 as enacted) | **Yes, for AI-001 in Colorado** | Lease of residential real estate in Colorado is a covered domain; applies to consequential decisions made on or after 2027-01-01. Advertising, marketing, product recommendations, fraud, and cybersecurity tools are excluded, so AI-002, AI-009, and AI-012 are outside it |
| HUD guidance on tenant screening (No. 24-098, May 2, 2024) | **Not current** | Moved to HUD's archive site; a 2025-09-16 FHEO memo removed tenant screening algorithm materials from the guidance repository. Used only as background on good practice |
| FTC Act Section 5 (N53-R02) | Yes | Accuracy of AI claims to consumers (AI-002, AI-005, AI-006) and of vendor claims the company relies on |
| FTC Safeguards Rule (N53-R01) | Yes, for AI-008, AI-009, and AI-010 | They process Title and Escrow customer information; vendors are service providers under 314.4(f) |

## 4. Risk tiering
Rubric: repository-defined. High = a substantial factor in a consequential decision (here, housing or independent contractor compensation) or able to cause direct financial harm without human review.

| ID | Use case | Tier | Status | Committee review |
|---|---|---|---|---|
| AI-001 | Automated tenant screening | High | In production (about 64,000 applications a year) | Reviewed 2025-11-12; re-reviewed 2026-08-26 |
| AI-002 | Buyer lead scoring and pre-qualification assistant | Medium | In production | Reviewed 2026-02-18; re-reviewed 2026-08-26 |
| AI-003 | Agent recruiting and retention scoring | High | In production | Not reviewed (due 2026-11-30) |
| AI-004 | Generative listing description drafting | Medium | In production | Reviewed 2026-03-11 |
| AI-005 | Consumer website property search chatbot | Medium | In production | Reviewed 2026-04-15 |
| AI-006 | Automated home value estimates | Medium | In production | Not reviewed (due 2026-11-30) |
| AI-007 | Transaction document review in SYS-01 | Low | In production | Reviewed 2026-01-21 |
| AI-008 | Title examination assistant | Medium | Pilot (2 closing offices) | Not reviewed (due before expansion, 2026-11-30) |
| AI-009 | Payment anomaly detection for disbursements | Medium | In production | Reviewed 2026-05-20 |
| AI-010 | Enterprise generative AI assistant | Medium | In production | Reviewed 2025-12-03 |
| AI-011 | Relocation expense audit | Low | Pilot (3 clients) | Not reviewed (due 2026-11-30) |
| AI-012 | SOC alert triage assistant | Low | In production | Not reviewed (fast track, due 2026-11-30) |

**Tiering notes:** AI-002 stays Medium because every lead is routed and the score sets only follow-up order; using it to decline representation or limit the listings a buyer sees would re-tier it to High. AI-009 is Medium, not High, because it only raises alerts; it never blocks or releases a payment. AI-003 is High until the committee confirms whether its outputs drive commission split offers.

## 5. State ADMT duties for tenant screening (California and Colorado)
| Duty | What the company will do | Status | P03 row |
|---|---|---|---|
| California Pre-use Notice (7220) | Notice in the rental application for California homes, before screening data is processed | Not met; due 2026-12-15 | G-078 |
| California opt-out or human appeal (7221) | Appeal to a trained leasing manager with authority to overturn | Not met; due 2026-12-15 | G-079 |
| California ADMT access requests (7222) | New request type in the privacy portal with response templates | Not met; due 2026-12-15 | G-080 |
| California risk assessment (7150(b)(3); 7155(b)) | CPPA-format assessment built from section 7 | Partially met; due 2027-06-30 | G-076 |
| Colorado notice (6-1-1704(1)-(2)) | Point-of-interaction notice in Colorado applications | Not met; due 2026-12-15 | G-081 |
| Colorado post-adverse outcome disclosure (6-1-1704(3)) | Disclosure within 30 days of each adverse outcome, with the ADMT's role and how to get more information | Not met; due 2026-12-15 | G-082 |
| Colorado correction and human review (6-1-1705(1)) | Same appeal path as California | Not met; due 2026-12-15 | G-083 |
| Colorado records (6-1-1703) | Keep decision records with the vendor model version for at least 3 years | Partially met; due 2026-12-15 | G-084 |

These rows are tracked as POAM-021. The company chose to provide notices and an appeal path even where human review might take a use outside the California definition of ADMT, because Colorado's "materially influence" test still applies and one process is simpler to run.

## 6. MEASURE: disparate outcome testing across the portfolio
**Gap.** Until 2026-08 the only fairness evidence for AI-001 was the vendor's own data; AI-003 and AI-006 have never been tested.

**Method.** The company does not collect race or ethnicity from applicants or buyers. For aggregate testing only, race and ethnicity are estimated with Bayesian Improved Surname Geocoding (BISG) from surname and address; estimates are never written to a person's record. National origin is partly visible through application or inquiry language. Familial status and disability cannot be estimated reliably, so the **criteria themselves** are reviewed (for example, how income multiples treat housing vouchers and disability benefits). An outcome ratio below 0.80 for any group, against the group with the best outcome, is a **screening flag**, not a legal conclusion. Any flag triggers a driver analysis and counsel's review of whether the practice is necessary to a substantial, legitimate, nondiscriminatory interest and whether a less discriminatory alternative would serve it (24 CFR 100.500(b)-(c)).

| Use case | Metric | Groups compared | Threshold for action | Due |
|---|---|---|---|---|
| AI-001 tenant screening | Approval, conditional approval, and decline rates; reason-code frequency | Estimated race and ethnicity; application language; state | Ratio below 0.80 | Quarterly; full local test 2027-03-31 (POAM-019) |
| AI-002 lead scoring | Median time to first contact; share of leads scored lowest | Inquiry language; areas grouped by majority population | Any group's median above twice the overall median | Monthly |
| AI-003 agent scoring | Share of agents flagged for recruiting or retention offers | Estimated race and ethnicity; age band; office | Ratio below 0.80 | Before re-approval |
| AI-006 home value estimates | Estimate error against sale price | Areas grouped by majority population | Mean error gap above 3 percentage points | Before re-approval |

## 7. Full assessment: AI-001 automated tenant screening
### 7.1 MAP
| Item | Description |
|---|---|
| Purpose and intended use | Help leasing teams decide on about 64,000 rental applications a year for about 21,000 homes in Florida, Georgia, Texas, Arizona, Colorado, and California. The screening provider pulls a consumer report, eviction and criminal records, and income data, applies its model and the company's thresholds, and returns accept, accept with conditions (higher deposit), or decline with reason codes |
| Users / operators | About 420 leasing staff; regional leasing managers |
| Affected people | Rental applicants and household members; property owners (vacancy time) |
| Data | Inputs: identity data, Social Security number, credit history, eviction filings and judgments, criminal records, stated and verified income. Outputs: recommendation, score band, reason codes |
| Build or buy | Configure: vendor model inside SYS-10. The company sets thresholds (income at least 3 times rent, minimum score band, 7-year eviction and 10-year criminal lookbacks). The vendor provided model and data-source documentation in 2026-05 |
| How it is used today | **The recommendation is the decision in practice.** Leasing staff changed 3.1% of recommendations in the last 12 months, mostly upgrades |
| Not intended | Setting rent, choosing which homes to show, or screening buyers |

### 7.2 Risk tier
**High.** It is a substantial factor in a consequential housing decision, and it relies on record types known to produce disparities by race and national origin.

### 7.3 MEASURE (applications screened 2025-07-01 to 2026-06-30)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | 60 reports checked against applicant documents: records must belong to the applicant and be current | 2 reports included another person's records (name-only match); 3 counted dismissed eviction filings as evictions | **No** |
| Safe | No applicant is declined or charged a higher deposit without human review against written criteria | Recommendation followed in about 97% of cases | **No** |
| Secure and resilient | Screening provider security review; SSO with MFA for leasing staff | SSO with MFA in place; provider review overdue (POAM-012) | Partial |
| Accountable and transparent | Adverse action notice for every decline and conditional approval | 1 of 40 sampled conditional approvals had no notice (P03 G-063) | Partial |
| Explainable and interpretable | Reason codes shown to staff and usable in notices; vendor documentation | Reason codes shown; vendor documentation received 2026-05 | Yes |
| Privacy-enhanced | Reports kept only as long as needed and disposed of securely | Kept indefinitely in SYS-10 (POAM-013) | **No** |
| Fair, with harmful bias managed | Approval-rate ratio by estimated group (section 6) | Applicants estimated Black: **0.76**; Hispanic 0.88; Asian and other 0.95. 54% of declines among applicants estimated Black were driven by eviction filings (including dismissed filings) and criminal records more than 7 years old | **No.** Disparity flagged |

### 7.4 MANAGE
**Human-in-the-loop design (from 2026-11-30):**
- Written screening criteria, reviewed by counsel for fair housing risk, are published to applicants before they apply.
- A trained leasing manager reviews **every** decline and conditional approval against the written criteria, and can override with a written reason; regional managers review overrides monthly.
- Criminal and eviction records get an **individualized review**: nature and age of the record, what happened since, and whether it bears on the tenancy. Dismissed filings and records that do not match the applicant are disregarded, and the applicant can explain or correct a record before a decision.
- Every decline and conditional approval gets an FCRA adverse action notice; California and Colorado applicants also get the notices and appeal path in section 5.

**Configuration changes (by 2026-11-30):** count eviction judgments only, not filings; limit criminal records to a counsel-approved list of offenses and lookback; require a second identifier (date of birth or Social Security number) for record matches; record the vendor model version with each decision.

**Monitoring:** quarterly disparate outcome testing (section 6); monthly 20-report accuracy sample; applicant disputes and complaints tracked by the Chief Compliance Officer; override rate reported quarterly (too low suggests rubber-stamping; too high suggests the criteria are wrong).

**Incident handling:** a breach at the screening provider follows P08 and the state third-party agent notice duties (Florida worked example: Fla. Stat. 501.171(6)). A fair housing complaint or a wrongful denial pattern is escalated to the Chief Compliance Officer and counsel and logged in the risk register (R-058).

**Decommissioning:** turn off automated recommendations and screen manually against the written criteria if (a) the ratio for any estimated group stays below 0.80 for two quarters after the configuration changes and counsel cannot document a justification, (b) the vendor will not provide notice of material model changes, or (c) the vendor changes its data sources without notice.

## 8. Full assessment: AI-002 buyer lead scoring and pre-qualification assistant
### 8.1 MAP
| Item | Description |
|---|---|
| Purpose | Rank about 1,900 inbound buyer inquiries a day so the 1,040 employed inside sales agents call the most promising first, and answer general financing questions through a chat assistant on the website and app |
| Inputs | ZIP code of the inquirer, inquiry language, price range, pre-approval status, web activity, chat text |
| Outputs | Score (A, B, C); suggested price range; hand-off to an agent or, at the buyer's request, to a lender (the mortgage joint venture or another lender) with the RESPA affiliated business disclosure (12 CFR 1024.15(b)(1)) |
| Affected people | Prospective buyers |
| Not intended | Deciding whether to represent a buyer, which listings a buyer sees, or whether a buyer qualifies for a loan |

### 8.2 Risk tier
**Medium.** The score does not decide whether anyone can buy, but it decides who gets prompt service. Housing-related services may not be provided on different terms because of a protected class (42 U.S.C. 3604(b)), and a buyer may not be told a home is unavailable when it is (3604(d)). ZIP code and inquiry language can act as proxies for race and national origin.

### 8.3 MEASURE (inquiries 2026-07-01 to 2026-08-31)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Conversion rate by score band | A-band leads convert at 3.4 times C-band leads | Yes |
| Fair, with harmful bias managed | Median time to first contact by language and area group | Spanish-language inquiries 9 hours against 2 hours for English; leads from areas with mostly Black residents scored C 48% of the time against 27% overall | **No** |
| Accountable and transparent | AI disclosure in the chat assistant; notice at collection | Both in place | Yes |
| Valid and reliable (assistant) | 200 sampled financing answers reviewed by a licensed loan officer | 6 answers overstated what a buyer could afford; all included the hand-off message | Partial |
| Privacy-enhanced | Chat transcripts kept 12 months; no use for model training without notice | In place | Yes |

### 8.4 MANAGE
- Remove ZIP code and inquiry language as scoring inputs by 2026-11-30 (R-060).
- Route Spanish-language leads to Spanish-speaking agents; same-day first contact for every lead regardless of score.
- The assistant gives only general information and a range; it may not state that a buyer qualifies for a loan. Prompt and answer templates are reviewed quarterly by a licensed loan officer (R-063).
- Monthly parity check, with a flag when any group's median first-contact time exceeds twice the overall median.
- **Decision:** continue with these conditions; re-tier to High if the score is ever used to decline representation or limit listings shown.

## 9. MANAGE: portfolio controls
- **Monitoring:** each High-tier tool has quarterly performance and fairness metrics (inventory column `monitoring`) reported to the committee; drift or threshold breaches trigger re-review.
- **Incident handling:** AI incidents (harmful output, bias finding, data misuse) are logged as SOC or compliance events and follow P08 where security or customer information is involved.
- **Third parties:** AI vendors are tier-1 in the vendor program; contracts require notice of material model changes and no training on company data (POL-01 4.8).
- **Generative AI (AI 600-1):** blocked-term filters and human approval for published text (AI-004); steering test suites for the chatbot (AI-005); no customer information in AI-010 outside the approved tenant (POL-05 4.5).
- **Decommissioning:** tools are retired if they fail monitoring thresholds twice or change data-use terms; the inventory records retirement.

## 10. Decisions
The executive risk committee approved these decisions on 2026-09-08, on the AI governance committee's recommendation of 2026-08-26:
1. **AI-001:** approved to continue with conditions: human review design, individualized record review, and configuration changes by 2026-11-30; California and Colorado notices, appeal path, and records by 2026-12-15 (POAM-021); full local disparate outcome testing by 2027-03-31 (POAM-019). Residual risk target: Low (P01 R-058, R-059).
2. **AI-002:** approved to continue with the conditions in section 8.4.
3. **AI-003:** commission split offers based on the model are paused until committee review (due 2026-11-30); outreach lists may continue, with a managing broker deciding every contact.
4. **AI-006, AI-011, AI-012:** may continue in current scope until review by 2026-11-30; no expansion.
5. **AI-008:** stays in its 2-office pilot until committee review and a Safeguards Rule vendor review.
6. **AI-009:** approved for real-time alerts to the SOC and escrow accounting (SI-4(12), due 2027-01-31), with monthly precision and recall reporting.
