# AI Risk Assessment: Automated Tenant Screening

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (residential real estate brokerage with property management) |
| Tier / Vertical | Micro / Real Estate and Rental and Leasing |
| AI use cases | **AI-001:** tenant screening recommendations in the property management platform (main assessment). **AI-002:** generative AI writing assistant (short screen in section 7) |
| Adaptation | The registry use case is "automated tenant and buyer screening". The brokerage does no automated buyer screening: agents read buyers' pre-approval letters themselves, and there is no lead scoring tool. Only the tenant side is assessed |
| Framework | NIST AI RMF 1.0 (AI 100-1). NIST AI 600-1 is used only for the short screen of AI-002, which is generative |
| Assessor / date | Property Manager and Office Manager, 2026-08-26; reviewed by the Broker-owner |
| Inventory | `ai-use-case-inventory.csv` (2 use cases) |

## 1. GOVERN
- **Accountable owners:** Property Manager (AI-001); Office Manager (AI-002).
- **Decision authority:** the Broker-owner approves every AI use case and accepts any Moderate residual risk it carries (POL-02 A.3). There is no AI committee at this size; the Broker-owner, Property Manager, and Office Manager review the screening results once a year and after any complaint.
- **Policies that apply:**
  - POL-04 4.6: no Restricted information (which includes screening reports) in any AI tool; approved list for Internal information
  - POL-04 4.8: screening reports kept 2 years after the decision, then deleted
  - POL-02 A.5: vendor approval and security check, which the screening provider has never had (P03 G-023)
- **Approved-tools list:** kept by the Office Manager. Today it lists AI-001 with the conditions in section 6. No generative AI tool is approved for Internal information yet.

## 2. MAP (AI-001)
| Item | Description |
|---|---|
| Purpose and intended use | Help the Property Manager decide on about 280 rental applications a year for about 85 managed homes. The screening provider pulls a consumer report, eviction and criminal records, and stated income, applies a scoring model and the brokerage's configured thresholds, and returns **accept, accept with conditions (higher deposit), or decline** with reason codes |
| Users | Property Manager; Leasing Assistant (sends invitations and reads results) |
| Affected people | Rental applicants and their households; owners (vacancy time) |
| Data | Inputs: identity data, Social Security number, credit history, eviction filings and judgments, criminal records, stated income. Outputs: recommendation, score band, reason codes |
| Build or buy | Configure. The vendor's model runs inside the property management platform. The brokerage set the thresholds in 2023 (income at least 3 times rent, a minimum score band, any eviction filing in 7 years, any criminal record in 10 years). The vendor has provided no validation or fairness documentation |
| Who decides | The brokerage acts as the owners' agent. The Property Manager tells the owner the result and the owner signs the lease. In practice the **recommendation is the decision**: in the 12 months to 2026-07-31 the Property Manager changed 4 of 276 recommendations |
| Not intended | Setting rent, choosing which homes to show, or screening buyers |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| Fair Housing Act, 42 U.S.C. 3604(a)-(b) and (f) | **Yes** | Rental decisions and their terms may not discriminate because of race, color, religion, sex, familial status, national origin, or disability. Disparate impact claims are cognizable under the Act (*Texas Dept. of Housing and Community Affairs v. Inclusive Communities Project*, 576 U.S. 519 (2015)) |
| HUD discriminatory effects rule, 24 CFR 100.500 | **Yes, for now** | In eCFR as of 2026-09-23. HUD has **proposed** removing it (91 FR 1475, 2026-01-14; supplemental 91 FR 51416, 2026-08-10); no final rule found on 2026-10-06. Removal would not remove disparate impact liability under the statute |
| Florida Fair Housing Act, Fla. Stat. 760.23 | **Yes** | Parallel state prohibitions |
| FCRA, 15 U.S.C. 1681b and 1681m(a); disposal rule 16 CFR 682.3 | **Yes** | Reports are pulled for a permissible purpose with the applicant's application. An action "adverse to the interests of the consumer" in connection with the application (15 U.S.C. 1681a(k)(1)(B)(iv)), such as a decline or a higher deposit, based in whole or part on a report requires the 1681m(a) notice. Reports must be disposed of securely |
| FTC Act Section 5 (N53-R02) | **Yes** | Covers the brokerage's statements to applicants and how it handles their data |
| FTC Safeguards Rule (N53-R01) | No | The brokerage is not a financial institution (P03 1.1); its benchmark elements are applied to the screening data anyway |
| HUD tenant screening guidance (No. 24-098, May 2, 2024) | **Not current** | Moved to HUD's archive site; a Sept. 16, 2025 FHEO memo removed tenant screening algorithm materials from its guidance repository. Used only as background on good practice |
| State AI laws (Colorado SB26-189; California ADMT regulations) | No | The brokerage operates only in Florida and is not a California business |

## 3. Risk tier
**AI-001: High** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`).
- It is a **substantial factor in a consequential housing decision**; today it is the decision.
- It relies on record types (eviction filings and criminal records) that are known to fall more heavily on some racial and national origin groups.

The size of the brokerage does not lower the tier. A Micro business screens fewer people, but each decision matters as much to the applicant.

**AI-002: Low**, rising to High if client information is entered (section 7).

## 4. MEASURE (AI-001)
Results are from a review of the 276 applications screened from 2025-08-01 to 2026-07-31 and 20 sampled files.

| Trustworthy characteristic | Test or check | Result | Pass? |
|---|---|---|---|
| Valid and reliable | 20 sampled reports checked against applicants' documents: each record must belong to the applicant and be current | 2 reports included another person's records (name-only match); 3 counted dismissed eviction filings | **No** |
| Safe | No applicant is declined or charged a higher deposit without human review against written criteria | Criteria not written; recommendation used as the decision | **No** |
| Secure and resilient | Platform access with MFA; screening reports not copied outside the platform | Text-message MFA for the 4 platform users; reports emailed to owners as PDFs | Partial |
| Accountable and transparent | Adverse action notice for every decline **and** conditional approval | Sent for 47 declines; none for 58 conditional approvals | **No** |
| Explainable and interpretable | Reason codes usable in notices and reviews | Reason codes shown; no vendor documentation of the score | Partial |
| Privacy-enhanced | Reports kept only as long as needed, then disposed of | Kept indefinitely in the platform and in owners' email | **No** |
| Fair, with harmful bias managed | Criteria and decline-driver review (plan below) | Eviction filings and old criminal records drive 28 of 47 declines | **No.** Flagged for counsel review |

### Bias and fairness testing plan (scaled to about 280 applications a year)
- **Why not a group approval-rate test now.** The brokerage does not collect race, ethnicity, or other protected characteristics on applications. Estimating them (for example with surname and address methods) on about 280 applications a year would give group sizes too small for reliable rate comparisons. The plan therefore tests the **criteria** that drive outcomes, which is where disparate impact usually enters, and asks the vendor for its own group-level testing across its customer base.
- **Driver analysis (annual, and after any criteria change).** Count which reason codes drive declines and conditional approvals. **Threshold:** any single criterion that drives more than 25% of declines, or any criterion based on eviction filings or criminal records, goes to counsel for the legally sufficient justification test: whether it is necessary to a substantial, legitimate, nondiscriminatory interest and whether a less discriminatory alternative would serve that interest (24 CFR 100.500(b), with the burdens of proof in 100.500(c)).
- **Current result.** Of 47 declines, 19 were driven by eviction filings (7 of them dismissed filings) and 9 by criminal records more than 7 years old: together 28, or 60%. Credit score drove 14 and income 5. Both record-based criteria are flagged.
- **Accuracy check (quarterly).** 5 random reports checked against the applicant's documents; any mismatch is corrected before a decision.
- **Disability and familial status.** These cannot be measured from outcomes, so the criteria are read for them: how the income test treats disability benefits and housing assistance, and whether any rule limits households with children. Requests for reasonable accommodation are logged and answered by the Property Manager.
- **Vendor evidence.** Request the screening provider's model documentation, data sources, and any disparate impact testing by 2026-12-31.

## 5. MANAGE (AI-001)
**Human-in-the-loop design (from 2026-10-31):**
- Written screening criteria, reviewed by counsel for Fair Housing Act risk, are given to applicants before they apply and to owners when they sign the management agreement.
- The Property Manager reviews **every** decline and conditional approval against the written criteria before any notice goes out or any result goes to an owner. The Property Manager can override the recommendation with a written reason; the Broker-owner reviews every override and every decline each quarter.
- **Individualized review** of criminal and eviction records: the nature and age of the record, what happened since, and whether it bears on the tenancy. Dismissed filings and records that do not match the applicant on a second identifier are disregarded. The applicant may explain or correct a record before the decision.
- Every decline and conditional approval gets an FCRA adverse action notice (P01 R-017).
- Owners receive the decision and the reasons, **not** the consumer report.

**Configuration changes (by 2026-11-30):** count eviction judgments only, not filings; limit criminal records to a counsel-approved list of offenses and lookback period; require a second identifier (date of birth or Social Security number) for record matches.

**Data protection:** reports stay in the platform (no PDFs by email); access limited to the Property Manager and Leasing Assistant with MFA; reports deleted 2 years after the decision (POL-04 4.8; 16 CFR 682.3); vendor security review under POL-02 A.5.

**Monitoring:** annual driver analysis and quarterly accuracy check (section 4); applicant disputes and complaints logged by the Property Manager; override rate reported to the Broker-owner each quarter (near zero suggests rubber-stamping; very high suggests the criteria are wrong).

**Incident handling:** a breach at the screening provider follows P08 and the third-party agent notice duty (Fla. Stat. 501.171(6)(a)). A Fair Housing complaint or a pattern of wrongful denials goes to the Broker-owner and counsel and is logged in the risk register (R-016).

**Decommissioning:** turn off automated recommendations and screen manually against the written criteria if (a) counsel cannot document a justification for a flagged criterion and the vendor cannot remove it, (b) the vendor will not provide model and data-source documentation by 2026-12-31, or (c) the vendor changes its data sources without notice.

## 6. Decision
**AI-001: approve with conditions.** Broker-owner, 2026-09-14. Continued use requires:
1. Written criteria reviewed by counsel, human review of every decline and conditional approval, and individualized record review in use by 2026-10-31.
2. Adverse action notices for conditional approvals by 2026-10-31 (P01 R-017).
3. The configuration changes in section 5 by 2026-11-30.
4. Vendor documentation and a security review by 2026-12-31 (POAM-009).
5. First annual driver analysis on post-change data by 2027-08-31.

Residual risk after these conditions: Low (target in P01 R-016).

## 7. AI-002: generative AI writing assistant (short screen)
- **Use:** staff and agents use consumer plans of a general-purpose assistant to draft listing descriptions, social posts, and client emails.
- **What went wrong:** between March and August 2026, client names, budgets, and one buyer's pre-approval amount were pasted into the tool in about 9 email drafts (P01 R-018). Consumer terms may allow the provider to use inputs for training.
- **Tier: Low** for listing copy with no client data; **High** if client information is entered, which POL-04 4.6 now prohibits.
- **NIST AI 600-1 risks that apply:** data privacy (client details in prompts), information integrity (invented property features), and harmful bias (discriminatory wording in listings). A listing or ad that indicates a preference based on a protected characteristic is prohibited (42 U.S.C. 3604(c)).
- **Decision: allowed with conditions** (Broker-owner, 2026-09-14): no client information of any kind in consumer tools; every draft checked for facts and wording before use; the Office Manager decides by 2026-12-31 whether to buy a business plan with no-training terms, which would let Internal information be used under POL-04 4.6.
