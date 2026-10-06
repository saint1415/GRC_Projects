# AI Use Assessment: Automated Tenant Screening Recommendation (one page)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (residential real estate brokerage) |
| Tier / Vertical | Sole Proprietorship / Real Estate and Rental and Leasing |
| AI use case | AI-001: the online tenant screening service's automated score and recommendation (SYS-10). About 35 applications in the last 12 months: 22 approved, 3 approved with a higher deposit, 10 declined |
| Registry use case | "Automated tenant and buyer screening". **Adapted:** the owner does no automated buyer screening; buyers' pre-approval letters are read by the owner. AI-002 (the writing assistant) is screened briefly in section 7 |
| Framework | NIST AI RMF 1.0 (Govern, Map, Measure, Manage), short form. AI 600-1 applies only to AI-002 |
| Assessor and decision | Broker-owner, 2026-09-10; decision 2026-09-15 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases) |

## 1. What it does (Map)
The applicant enters their own identity data and Social Security number in the screening service and pays the fee. The service pulls a consumer report, eviction records, and criminal records, applies the **vendor's default criteria** (income at least 3 times rent, a minimum score band, 7-year lookbacks), and returns a score with **approve, approve with a higher deposit, or decline** and reason codes. The owner forwards the result to the landlord client, who in every case in the last 12 months followed it. The vendor has given no documentation of how the score is built or tested. **In practice the recommendation is the decision.**

## 2. Rules that apply
| Rule | Applies? | Why |
|---|---|---|
| Fair Housing Act, 42 U.S.C. 3604(a)-(b), (f) | **Yes** | Rental decisions and their terms may not discriminate because of a protected class. A small landlord's exemption in 3603(b)(1) applies only if the house is rented "without the use in any manner of the sales or rental facilities or the sales or rental services of any real estate broker" (3603(b)(1)(A)). **Using this brokerage therefore brings every landlord client fully under 3604**; the broker is covered in any case |
| HUD discriminatory effects rule, 24 CFR 100.500 | **Yes, for now** | In force. HUD has **proposed** removing it (91 FR 1475, 2026-01-14; supplemental 91 FR 51416, 2026-08-10); no final rule as of 2026-10-06. Removal would not remove disparate impact claims under the statute itself |
| FCRA, 15 U.S.C. 1681m(a); 16 CFR 682.3 | **Yes** | A decline **or a higher deposit** based in whole or in part on the report is adverse action and needs the notice. Reports must be disposed of securely |
| FTC Act Section 5 (N53-R02) | **Yes** | Governs what the owner tells applicants and landlords about the screening |
| HUD tenant screening guidance (No. 24-098, May 2, 2024) | **Not current** | Archived; FHEO removed tenant screening algorithm materials on 2025-09-16. Background only |
| Colorado SB26-189; California ADMT regulations | No | Florida-only business; not a California business |

## 3. Risk screen (repository rubric)
**Tier: High.** The tool is a substantial factor in a consequential housing decision, and its inputs (eviction filings and criminal records) are known to produce disparities by race and national origin. The High tier requires human review before action, bias review, notice to affected people, and monitoring.

## 4. Measure (sized for 35 applications a year)
| Check | Result | Pass? |
|---|---|---|
| Accuracy: 10 recent reports compared with what applicants provided | 1 counted a dismissed eviction filing as an eviction; 1 matched a criminal record on name only | **No** |
| Human review before action | None; recommendation forwarded as is | **No** |
| Adverse action notices | Sent for declines through the service; 0 of 3 conditional approvals got one | **No** |
| Vendor documentation and security | None requested; click-through terms only | **No** |
| Fairness | **Statistical testing is not meaningful at 35 applications a year** and the owner collects no race or ethnicity data. Instead the owner reviewed the criteria themselves: the default 3-times-rent income test counts housing vouchers inconsistently, and the lookbacks count eviction filings, not judgments | **No** (criteria change needed) |

## 5. Data-sharing rules (Govern)
1. Applicants enter their own Social Security numbers and identity data in the screening service; the owner never collects them by email or text (POL-01 8.5).
2. The owner keeps one copy of each report in the transaction or lease file for the 5-year brokerage record period and deletes every other copy within 30 days of the decision (POL-01 8.7; 16 CFR 682.3).
3. Screening data never goes into the AI writing assistant or any other AI tool (POL-01 9.5).
4. Landlords receive the recommendation and reason codes, not the full report, unless they need it for the decision.

## 6. Human review and decision (Manage): approve with conditions (2026-09-15)
From 2026-10-31 (P01 R-011):
1. **Written screening criteria**, agreed with each landlord and given to applicants before they apply: eviction **judgments** only, not filings; criminal records limited to a short list of recent offenses that bear on the tenancy, with a match on at least two identifiers; housing vouchers counted as income.
2. **The owner reviews every decline and conditional approval** against the written criteria before anything goes to the landlord, and writes the reason for any change. The applicant can explain or correct a record before the decision.
3. **Adverse action notice** for every decline and every conditional approval (by 2026-11-30); counsel confirms whether the owner or the landlord sends it.
4. **Vendor review** by 2026-12-31: security summary, data retention, data sources, and model documentation (POAM-006).
5. **Monitoring:** each August, review all decisions for the year, overrides, disputes, and complaints. **Stop using the recommendation** and screen manually against the written criteria if the vendor will not let the owner set the criteria above or will not provide documentation.

## 7. AI-002: generative AI writing assistant (short screen)
**Tier: Low** as now restricted: internal drafting, no decisions about people. Between March and August 2026 the owner pasted parts of about 6 client emails into the consumer tool (P01 R-012). From 2026-09-15: no client personal information or Confidential data in any AI tool, the vendor's training opt-out turned on, and every AI-drafted listing description or ad checked before publishing for any statement of preference based on a protected class (42 U.S.C. 3604(c)). Re-tier to Medium if it is ever used to answer clients directly.
