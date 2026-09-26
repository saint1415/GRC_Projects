# AI Risk Assessment: Automated Tenant and Buyer Screening

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (residential real estate brokerage with property management) |
| Tier / Vertical | Small / Real Estate and Rental and Leasing |
| AI use cases | **AI-001:** tenant screening recommendations in the property management platform (main assessment). **AI-002:** buyer lead scoring in the CRM (short assessment in section 7) |
| Framework | NIST AI RMF 1.0 (AI 100-1). AI 600-1 is not needed: neither use case is generative |
| Assessor / date | Director of Property Management and Inside Sales Manager with the IT Manager, 2026-09-10 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases) |

## 1. GOVERN
- **Accountable owners:** Director of Property Management (AI-001); Inside Sales Manager (AI-002); COO (AI-003, generative AI for marketing).
- **Decision authority:** the COO approves AI use cases. High-tier use cases are also reported to the majority owner and Broker of Record, who accepts any High risk they carry (POL-01 4.4).
- **Policies that apply:**
  - POL-05 4.8: approved AI tools only; scoring or ranking features used only as approved here
  - POL-04 4.10: consumer reports used only for the rental decision and disposed of securely
  - POL-01 4.8: service provider due diligence, which the screening provider has never had (P03 G-029)
- **Scale for a Small company:** there is no AI committee. The COO, IT Manager, Director of Property Management, and Inside Sales Manager review the inventory and the fairness results quarterly.
- **Approved-tools list:** kept by the IT Manager. Today it lists AI-001 and AI-002 with the conditions in section 6; the enterprise generative AI tool (AI-003) is under evaluation.

## 2. MAP (AI-001)
| Item | Description |
|---|---|
| Purpose and intended use | Help leasing coordinators decide on about 1,700 rental applications a year for about 430 managed homes. The screening provider pulls a consumer report, eviction and criminal records, and income data, applies a scoring model and the company's configured thresholds, and returns **accept, accept with conditions (higher deposit), or decline** with reason codes |
| Users / operators | 4 leasing coordinators; the Director of Property Management |
| Affected people | Rental applicants and their household members; property owners (vacancy time) |
| Data | Inputs: identity data, Social Security number, credit history, eviction filings and judgments, criminal records, stated income. Outputs: recommendation, score band, reason codes |
| Build or buy | Configure: vendor model inside the property management platform. The company sets the thresholds (income at least 3 times rent, minimum score band, 7-year eviction and 10-year criminal lookbacks). The vendor has provided no validation or fairness documentation |
| How it is used today | **The recommendation is the decision in practice.** Coordinators changed only 41 of 1,680 recommendations in the last 12 months (2.4%), mostly upgrades. Adverse action notices go out only when the decline button is used, not for conditional approvals (P01 R-025) |
| Not intended | Setting rent, choosing which units to show, or screening buyers. Buyer lead scoring is a separate tool (AI-002) |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| Fair Housing Act, 42 U.S.C. 3604(a)-(b) and (f) | **Yes** | Rental decisions and their terms may not discriminate because of race, color, religion, sex, familial status, national origin, or disability. The Supreme Court held that disparate impact claims are cognizable under the Act (*Texas Dept. of Housing and Community Affairs v. Inclusive Communities Project*, 576 U.S. 519 (2015)) |
| HUD discriminatory effects rule, 24 CFR 100.500 | **Yes, for now** | In force as of 2026-09-23. HUD has **proposed** removing it (91 FR 1475, 2026-01-14; supplemental proposal 91 FR 51416, 2026-08-10, comments close 2026-10-09). Removal would leave the standard to the courts; it would not remove disparate impact liability under the statute. Not final as of 2026-09-26 |
| Florida Fair Housing Act, Fla. Stat. 760.23 | **Yes** | Parallel state prohibitions for the same protected classes |
| FCRA, 15 U.S.C. 1681b and 1681m(a); disposal rule 16 CFR 682.3 | **Yes** | Reports are obtained for a permissible purpose; any adverse action based in whole or part on a consumer report (a decline or a higher deposit) requires the notice in 1681m(a); reports must be disposed of securely |
| FTC Act Section 5 (N53-R02) | **Yes** | Governs the vendor's accuracy and fairness claims and the company's own representations to applicants |
| FTC Safeguards Rule (N53-R01) | Not directly | Tenant data is not customer information under 314.2(d), but the company applies the same program to it by choice (P03 section 1.1) |
| HUD guidance on tenant screening (No. 24-098, May 2, 2024) | **Not current** | Moved to HUD's archive site; a Sept. 16, 2025 FHEO memo removed tenant screening algorithm materials from its guidance repository. Used here only as background on good practice, not as a requirement |
| State AI laws (Colorado SB26-189, California ADMT regulations) | No | The company operates only in Florida and is not a California business (P03 section 1.4) |

## 3. Risk tier
**AI-001: High** (repository rubric, `00_universal/projects/P10_ai-governance/README.md`).
- It is a **substantial factor in a consequential housing decision**; in practice it is the decision.
- It uses consumer report data and record types (eviction filings and criminal records) that are known to produce disparities by race and national origin.

**AI-002: Medium** (section 7). **AI-003: Low**, rising to High if client data is entered (blocked by POL-05 4.8).

## 4. MEASURE (AI-001)
Results are from a retrospective review of 1,680 applications screened from 2025-09-01 to 2026-08-31.

| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Sample of 40 reports checked against applicant documents: records must belong to the applicant and be current | 3 reports included another person's records (name-only match); 2 counted dismissed eviction filings as evictions | **No** |
| Safe | No applicant is declined or charged a higher deposit without human review against written criteria | Recommendation used as the decision; 2.4% override rate | **No** |
| Secure and resilient | Screening provider security review (SOC 2 report or questionnaire); SSO with MFA for coordinators | Coordinators use SSO with MFA; provider never reviewed (P03 G-029) | Partial |
| Accountable and transparent | Adverse action notice for every decline **and** conditional approval, naming the reporting agency and the applicant's rights | Sent for declines only; 0 of 12 sampled conditional approvals got a notice | **No** |
| Explainable and interpretable | Reason codes shown to the coordinator and usable in the notice | Reason codes shown; vendor gives no documentation of how the score is built | Partial |
| Privacy-enhanced | Reports kept only as long as needed and disposed of securely | Kept indefinitely in the platform (no retention schedule, POAM-024) | **No** |
| Fair, with harmful bias managed | See the bias testing plan below. Threshold: an approval-rate ratio below 0.80 for any group, compared with the group with the highest rate | Applicants estimated Black: approval ratio **0.69**. Hispanic 0.85; Asian and other 0.93 | **No.** Disparity flagged |

### Bias testing plan
- **Groups compared.** The company does not collect race or ethnicity on applications. Race and ethnicity are estimated with the Bayesian Improved Surname Geocoding (BISG) method from surname and address, and results are treated as estimates, never recorded on an applicant's file. National origin is partly visible through application language. Sex is estimated from first name only for aggregate testing. Familial status and disability cannot be estimated reliably, so the **criteria themselves** are reviewed instead (for example, how the income multiple treats disability benefits and housing vouchers, and occupancy limits).
- **Metrics.** For each group: outright approval rate, conditional approval rate, decline rate, and the approval-rate ratio against the highest group. Reason-code frequency by group, to find which criterion drives any gap.
- **Threshold.** A ratio below 0.80 is a **screening flag**, not a legal conclusion. It borrows the four-fifths rule of thumb used in employment testing. Any flag triggers a driver analysis and a counsel review of whether the criterion is necessary to a substantial, legitimate, nondiscriminatory interest and whether a less discriminatory alternative would serve that interest (the burden-shifting test in 24 CFR 100.500(c), which courts also apply).
- **Frequency and sample.** Quarterly, on all applications in the quarter; annually on the full year. Results go to the quarterly review in section 1.
- **Current result and drivers.** Estimated approval rates: White 71% (640 applicants), Black 49% (410), Hispanic 60% (470), Asian and other 66% (160). **58% of declines among applicants estimated Black were driven by eviction filings (including dismissed filings) and criminal records more than 7 years old.** Those two criteria are the first to change.

## 5. MANAGE (AI-001)
**Human-in-the-loop design (from 2026-10-31):**
- Written screening criteria, reviewed by counsel for Fair Housing Act risk, are published to applicants before they apply.
- A leasing coordinator reviews **every** decline and conditional approval against the written criteria before any notice goes out. The coordinator can override the recommendation with a written reason; the Director of Property Management reviews all overrides monthly.
- Criminal and eviction records get an **individualized review**: the nature and age of the record, what happened since, and whether it bears on the tenancy. Dismissed filings and records that do not match the applicant are disregarded, and the applicant can explain or correct a record before a decision.
- Every decline and conditional approval gets an FCRA adverse action notice.

**Configuration changes (by 2026-11-30):** count eviction judgments only, not filings; limit criminal records to a counsel-approved list of offenses and lookback; require a second identifier (date of birth or Social Security number) for record matches.

**Monitoring:** quarterly bias testing (section 4); monthly sample of 10 reports for accuracy; applicant disputes and complaints routed to the Director of Property Management and tracked; override rate reported quarterly (too low suggests rubber-stamping; too high suggests the criteria are wrong).

**Incident handling:** a data breach at the screening provider follows P08 and the Florida third-party agent notice duty (Fla. Stat. 501.171(6)). A Fair Housing complaint or a wrongful denial pattern is escalated to the COO and counsel and logged in the risk register (R-023).

**Decommissioning:** turn off automated recommendations and screen manually against the written criteria if (a) the Black-estimated approval ratio stays below 0.80 for two quarters after the configuration changes and counsel cannot document a justification, (b) the vendor will not provide model and data-source documentation by 2026-12-31, or (c) the vendor changes its data sources without notice.

## 6. Decision
**AI-001: approve with conditions.** COO, 2026-09-21; reported to the majority owner the same day. Continued use requires:
1. Written criteria, coordinator review of every decline and conditional approval, and individualized record review in use by 2026-10-31.
2. Adverse action notices for conditional approvals by 2026-11-30 (P01 R-025).
3. The configuration changes in section 5 by 2026-11-30.
4. Vendor due diligence (security report, model documentation, data sources) and a contract addendum by 2026-12-31 (POAM-013).
5. First quarterly bias test on post-change data by 2027-01-31.

Residual risk after these conditions: Low (target in P01 R-023).

## 7. AI-002: buyer lead scoring (short assessment)
- **Purpose:** rank inbound buyer inquiries (A, B, C) so the 6 inside sales agents call the most promising first. About 560 leads a month.
- **Inputs:** ZIP code of the inquirer, inquiry language, price range, pre-approval status, and web activity.
- **Tier: Medium.** The score does not decide whether anyone can buy or rent, but it decides who gets prompt service. Housing-related services may not be provided on different terms because of a protected class (42 U.S.C. 3604(b)), and a buyer may not be told a home is unavailable when it is (3604(d)). ZIP code and inquiry language can act as proxies for race and national origin. **Re-tier to High** if the score is used to decline to represent a buyer or to decide which listings a buyer is shown.
- **Measure:** in July and August 2026 (1,120 leads), Spanish-language inquiries waited a median of 26 hours for first contact, compared with 3 hours for English; leads from three ZIP codes with mostly Black residents were scored C 64% of the time, against 30% overall. **Disparity flagged.**
- **Manage and decision: approve with conditions** (COO, 2026-09-21): remove ZIP code and inquiry language as inputs by 2026-11-30 (P01 R-024); route Spanish-language leads to a Spanish-speaking agent; enforce same-day first contact for every lead regardless of score; monthly response-time parity check by language and ZIP code group, with a flag when any group's median first-contact time exceeds twice the overall median.

**AI-003 (generative AI for listing copy):** public tools are prohibited for client data (POL-05 4.8). Every AI-drafted listing description or advertisement must be checked for discriminatory statements before publication (42 U.S.C. 3604(c)). The enterprise tool decision is due 2026-12-31 (P01 R-026).
