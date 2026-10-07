# AI Governance Risk Assessment: Group AI Program | Cris Santos Company Holdings

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (Banking, Financial Software and Data Services, Commercial Real Estate, corporate) |
| Tier / Vertical | Multi-Sector / Finance and Insurance |
| Scope | The group AI governance program: group standards, the division use-case inventory, and the regulator-specific rules for three priority use cases: the bank's AI credit underwriting model (AI-001), the Financial Software cash-flow data service (AI-005), and the bank's payment fraud model (AI-002) |
| Framework | NIST AI RMF 1.0 (AI 100-1), the Generative AI Profile (AI 600-1) for generative use cases, and the AI RMF Playbook |
| Assessors / date | Group AI council (chaired by the Group Chief Risk Officer), with independent validation evidence from model risk management, 2026-08-28; presented to both board risk committees 2026-09-10 |
| Inventory | `ai-use-case-inventory.csv` (10 use cases: 2 High, 6 Medium, 2 Low) |

## 1. GOVERN (group program)
### 1.1 Structure
| Body or role | Responsibility |
|---|---|
| Holding company and bank board risk committees | Oversee AI risk as part of model, compliance, and operational risk; receive the High-tier list quarterly |
| Group AI council | Group Chief Risk Officer (chair), Group CISO, Group Chief Compliance Officer, Group Chief Privacy Officer, Group General Counsel, Head of Model Risk Management, and one executive from each division. Approves High-tier use cases and the approved-tools list |
| Head of Model Risk Management (second line) | Independent validation of every model used in credit, fraud, and AML decisions, including AI models; effective challenge |
| Group Chief Compliance Officer | Fair lending testing and adverse action notice review |
| Division AI owners | Named business owner for each use case (inventory column); run monitoring |
| Group CISO | AI security standard (prompt injection, model supply chain, data leakage) |
| Group internal audit | Includes High-tier AI controls in the annual assessment from 2027 |

### 1.2 Group AI Standard (adopted 2026, under POL-01 4.13)
1. **Register before use.** Every AI use case that uses customer information or client data, or that supports decisions about people, is registered before deployment or material change.
2. **Tier with the repository rubric** (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`). High tier: council approval, pre-deployment fairness testing, an impact assessment, notice to affected people, and quarterly monitoring reports.
3. **Model risk management applies to AI.** Models used in credit, fraud, or AML decisions are validated before production and after any material change, including new input attributes. The group applies independent validation, conceptual soundness review, and outcomes analysis as a program requirement; the current status of the agencies' model risk management guidance was not verified for this sample.
4. **Client data is the client's.** Client institutions' data may train or feed a product only as the client agreement allows (POL-04 4.3).
5. **Change gate.** A new model, new attributes, a new data source, or a new decision role triggers re-assessment before release, including SOC description impact for products sold to clients.
6. **Developer documentation for products.** Any AI product sold to client institutions ships with documentation of intended uses, limitations, testing results, and human-review guidance.
7. **Approved tools only** for workforce generative AI (POL-05 4.7).

**Where the program fell short in 2026.** The standard was adopted after the cash-flow attributes were added to AI-001 (2026-03) and after AI-005 was sold to client banks. The attribute change went through performance validation but not through adverse action reason mapping, and AI-005 shipped without developer documentation (scenario gap 4). Both are now under conditions (section 6).

## 2. MAP (division use cases and applicable rules)
| ID | Use case | Division | Tier | Status |
|---|---|---|---|---|
| AI-001 | AI credit underwriting model (consumer and small business) | Banking | High | In production with conditions |
| AI-002 | Wire and ACH payment fraud scoring | Banking | Medium | In production |
| AI-003 | AML alert prioritization | Banking | Medium | In production |
| AI-004 | Contact center generative assistant | Banking | Medium | In production; expansion paused |
| AI-005 | Cash-flow data service for 64 client banks | Financial Software | High | In production; new sales paused |
| AI-006 | Platform fraud scoring for client tenants | Financial Software | Medium | In production |
| AI-007 | Engineering coding assistant | Financial Software | Low | Approved |
| AI-008 | CRE underwriting assistant | Commercial Real Estate | Medium | Pilot |
| AI-009 | Building energy analytics | Commercial Real Estate | Low | Approved |
| AI-010 | Enterprise generative AI assistant | Group | Medium | Pilot (8,000 users) |

### 2.1 Bank AI credit underwriting model (AI-001): ECOA, Regulation B, and model risk
| Item | Description |
|---|---|
| Purpose and use | Score consumer installment loan applications (up to $50,000, since 2025-10) and small business credit line applications (up to $250,000, since 2026-03). Returns a score, a recommendation, and the top 4 reason codes |
| Decision role | Consumer: about 70% of applications are decided automatically inside credit policy cutoffs; the rest go to underwriters. Small business: underwriters decide every application. The model is a **substantial factor** in both |
| Volume (2026-03 to 2026-08) | About 148,000 consumer and 6,900 small business applications; about 30,100 adverse action notices |
| Data | Credit bureau attributes, application data, and, since 2026-03, **cash-flow attributes** from the Financial Software data service (AI-005) derived from the applicant's deposit transactions at the bank |

| Rule | What it requires | What it means for the model |
|---|---|---|
| 12 CFR 1002.9(b)(2) | The statement of reasons for adverse action must be specific and give the principal reasons; saying the applicant failed to reach a qualifying score on the creditor's scoring system is insufficient | Reason codes must reflect the model's actual main drivers, including cash-flow attributes. **Gap:** validation sampled 400 adverse action notices from 2026-03 to 2026-08; in 92 (23%) the stated reasons omitted the main cash-flow driver |
| 12 CFR 1002.9(a)(3) | Modified notice rules for business credit applicants (different for businesses with gross revenues of $1 million or less and above) | Small business notices follow the right path by revenue; checked in the 400-notice sample with no errors |
| 12 CFR 1002.4(a); 1002.6(b)(1) | No discrimination on a prohibited basis in any aspect of a credit transaction; no prohibited basis in any system of evaluating creditworthiness | Attributes that act as close proxies for a prohibited basis must be found and removed |
| 12 CFR 1002.6(a) (amended by 91 FR 21620, effective 2026-07-21) | States that the Act does not provide for the "effects test" | Outcome disparities are not by themselves a Regulation B violation. The group still measures them, as a warning that an input may act as a proxy for a prohibited basis |
| 12 CFR 1002.6(b)(2) | Age may be used only in an empirically derived, demonstrably and statistically sound system, and an elderly applicant's age must not be assigned a negative value | The model does not use age; confirmed at each release |
| Regulation B subpart B (12 CFR 1002.105, 1002.114) | Small business data collection applies from 2028-01-01 for institutions with at least 1,000 covered originations in each of 2026 and 2027; voluntary collection of principal owners' demographic data is permitted from 12 months before | The bank will be covered. Counsel will advise whether and how data collected under subpart B can support fairness testing, given the firewall rule in 1002.108 |
| CFPB Circulars 2022-03 and 2023-03 | Withdrawn on 2025-05-12 (90 FR 20084), per the vertical research | The 1002.9 duty itself is unchanged |
| 12 CFR 30 App. B; GLBA | Customer information used in the model and its serving environment is protected under the bank's program | Covered by the CDBP and SYS-B3 controls (P02, P04) |
| Colorado SB26-189 | Deployer duties for covered decisions from 2027-01-01 | Not applicable today: the bank's lending footprint does not include Colorado. Re-check if the footprint changes |

### 2.2 Financial Software cash-flow data service (AI-005): developer duties and client commitments
| Rule or commitment | Implication |
|---|---|
| Client banks' ECOA and Regulation B duties (1002.9(b)(2)) | Client banks must give specific reasons when the score contributes to a decline. They can only do that if the division tells them what drives the score. **Gap:** no attribute-level reason guidance or documentation exists |
| Client banks' third-party and model risk oversight (12 CFR 30 App. B III.D and their own model governance) | Client banks need testing results, limitations, and change notices to validate the score. **Gap:** the service is not in the SOC reports (P09) and changes are not announced (P07 CM-3) |
| Bank Service Company Act (12 U.S.C. 1867(c)) | The service is performed for examined client banks, so their agencies can examine it |
| Colorado SB26-189 (effective 2027-01-01) | Developers of covered technology that materially influences lending decisions must give deployers documentation of intended uses, training-data categories, limitations, and human-review instructions. 3 client banks in Colorado use the score. The law's enforcement posture is unsettled (litigation and federal preemption efforts; see `00_universal-framework/cross-sector/us-cross-sector-obligations.md`), so counsel is reviewing. The documentation is needed for every client anyway |
| FTC Act Section 5 (N51-R01) | Accuracy and fairness claims in sales materials must be substantiated |
| Client contracts and SOC 2 commitments | Client data used only for the contracted service; the score is part of the service and must be described (P09 CC2.3) |

### 2.3 Other use cases
| Use case | Rules and commitments |
|---|---|
| AI-002 payment fraud scoring | App. B III.C.1.f (monitoring); model risk policy. In the P08 scenario the model flagged the $14.2 million funding wire (new beneficiary, high amount), and the hold was released after the callback to the customer's designated contact. The model worked; the callback path was the weak link |
| AI-003 AML alert prioritization | 12 CFR 21.11: SAR decisions stay with investigators; below-threshold alerts are sampled |
| AI-004 contact center assistant (generative) | Caller verification before the assistant sees account data; AI 600-1 risks (confabulation, information security) |
| AI-006 platform fraud scoring for client tenants | Client contracts; 18 client banks asked for documentation |
| AI-008 CRE underwriting assistant (generative) | ECOA and Regulation B apply to business credit; underwriters verify every figure; the credit committee decides |
| AI-010 enterprise generative assistant | POL-05 4.7 and POL-04 4.9; prohibited for credit, fraud, AML, and customer decisions |

## 3. Risk tiers (repository rubric)
- **High:** AI-001 (a substantial factor in consequential credit decisions, and automatic for about 70% of consumer applications) and AI-005 (a substantial factor in 64 client banks' credit decisions, even though the division decides nothing itself).
- **Medium:** AI-002, AI-003, AI-004, AI-006, AI-008, AI-010. A human makes the final decision affecting individuals, or the output influences a business decision.
- **Low:** AI-007, AI-009.

**Re-tier triggers:** letting AI-002 decline payments without review (to High); using AI-004 to act on accounts (to High); extending AI-008 to decide loans or to consumer credit (to High); AI-010 use in any customer decision (prohibited).

## 4. MEASURE
Results are from validation, monitoring, and compliance testing between 2026-03 and 2026-08.

### 4.1 Bank AI credit underwriting model (AI-001)
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Independent validation on bank data (discrimination and calibration) for both segments | Consumer validated 2025-09 and re-validated for the 2026-03 attributes; small business validated 2026-02. Performance within tolerance | Yes |
| Explainable and interpretable | Share of adverse action notices whose stated reasons include the model's main driver (target 100%) | 308 of 400 (77%); 92 omitted the main cash-flow driver | **No** (1002.9(b)(2)) |
| Fair, with harmful bias managed | Approval-rate ratio, consumer, by estimated race and ethnicity (surname and geography proxy); flag below 0.80 | Lowest group ratio 0.83 | Yes (monitor) |
| Fair, with harmful bias managed | Approval-rate ratio, small business, majority-minority census tracts versus others; flag below 0.80 | 0.76; the attribute "payments to non-bank lenders" was a top-2 reason in 41% of flagged declines | **Flagged.** Proxy review of the attribute |
| Safe | Automatic declines only inside credit policy cutoffs; loan amount caps enforced | Limits held in all sampled decisions | Yes |
| Accountable and transparent | Named owner; inventory; override tracking | In place; small business overrides tracked since 2026-06 only | Partial |
| Secure and resilient | Version pinned and hashed; scoring log; private access only | In place (P04) | Yes |
| Privacy-enhanced | Cash-flow data used only for the applicant's own application | Confirmed; no client data from other institutions used | Yes |

### 4.2 Financial Software cash-flow data service (AI-005)
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Accuracy testing before each release | Done for 6 of 6 releases | Yes |
| Valid and reliable (stability) | Score stability across client portfolios and over time | Not tested | **No** |
| Fair, with harmful bias managed | Proxy review of attributes before release | Not done; the same "payments to non-bank lenders" attribute is in the library | **No** |
| Accountable and transparent | Developer documentation for clients; change notices | None; 4 releases in 2026 without client notice | **No** |
| Explainable and interpretable | Attribute-level reason guidance for client adverse action notices | None | **No** |
| Privacy-enhanced | Each client's score uses only that client's customer data | Confirmed by access tests (P04 SYS-S2 AC-3) | Yes |

### 4.3 Bank payment fraud scoring (AI-002)
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Detection rate on confirmed fraud (target at least 85%) | 88% | Yes |
| Safe | Holds reviewed within 30 minutes during business hours | 96% | Yes |
| Accountable and transparent | Hold reasons shown to analysts | In place | Yes |
| Resilient to drift | Challenger model comparison | Quarterly only; new BEC patterns missed for weeks | Partial (monthly challenger from 2026-11) |

### 4.4 Bias and fairness testing plan (AI-001 and AI-005)
| Item | Plan |
|---|---|
| Data | All scored applications each quarter; before any new attribute, a back-test on 2024 to 2025 applications with and without the attribute |
| Groups compared | Race and ethnicity estimated with a surname and geography proxy method (Regulation B generally bars asking for these for non-mortgage credit; 1002.5); sex estimated by first-name proxy; census tract minority share; age 62 or older versus younger |
| Metrics and thresholds | Approval-rate ratio: flag below 0.80. Score difference after controlling for credit factors: flag if statistically significant at the 5% level. Reason code frequency: flag if a code is twice as frequent in one group. Override rates: flag a difference over 10 percentage points |
| Proxy review | For each flag, test whether each attribute predicts group membership; remove or replace attributes that act as close proxies and are not needed for accuracy |
| Less discriminatory alternative | Compare versions with and without flagged attributes; prefer the version with smaller disparities where accuracy is comparable; the model owner documents the trade-off |
| Who | Model risk management and the Group Chief Compliance Officer's fair lending team; results to the AI council and both board risk committees quarterly. For AI-005, results go to client banks in the documentation package |

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001 consumer:** automatic decisions only inside credit policy cutoffs; applicants near cutoffs go to underwriters; underwriters can override with a written reason.
- **AI-001 small business:** the underwriter decides; from 2026-10-15 a second officer reviews every model-recommended decline before notice.
- **AI-005:** client banks decide; the documentation package tells them what the score is for, what it must not be used for (for example, as the sole basis for a decline), and how to explain it.
- **AI-002:** analysts review every hold; the model never returns a payment on its own.

**Monitoring:** monthly metrics to use-case owners; quarterly High-tier report to the council and both board risk committees; P01 risks GR-05, GR-14, BR-010, BR-011, BR-014, BR-015, BR-016, FS-008, FS-009, RR-013.

**Incident handling:** an AI failure that harms customers, exposes customer or client data, or breaks client commitments follows P08 and POL-03. A fair lending issue goes to the Group Chief Compliance Officer and counsel.

**Decommissioning:** each use case has an off switch and a fallback the BIA covers (P05: manual underwriting for BP-B07; clients underwrite without attributes for BP-S03; analyst rules for fraud holds).

## 6. Decisions
| Use case | Decision | Conditions and dates |
|---|---|---|
| AI-001 credit model | **Continue with conditions** (council, 2026-08-28; both board risk committees informed 2026-09-10) | Remap reason codes to include cash-flow drivers by 2026-10-15; send corrected statements of specific reasons to affected applicants (about 6,900, estimated from the 23% sample rate) by 2026-10-31; suspend the "payments to non-bank lenders" attribute for small business pending proxy review; second-officer review of small business declines from 2026-10-15; re-validation by 2026-11-30; no small business expansion until all are met (POAM-021) |
| AI-005 data service | **Continue for the 64 existing clients; pause new sales** | Stability and fairness testing method approved by model risk management by 2026-11-15; developer documentation package, including reason guidance, sent to all 64 clients by 2026-12-31; service added to the SOC 2 description or excluded with a statement; change gate live by 2026-11-30 (POAM-014, POAM-015) |
| AI-002 payment fraud | **Approved** | Monthly challenger model from 2026-11 |
| AI-004 contact center assistant | **Continue; expansion paused** | Monthly output sampling (confabulation and disclosure errors) before expansion beyond 600 agents |
| AI-008 CRE underwriting assistant | **Continue pilot** | Monthly accuracy sampling; no use for consumer credit |
| AI-003, AI-006, AI-007, AI-009, AI-010 | **Approved** | Standard monitoring; AI-006 client documentation by 2027-03-31; AI-010 prohibited for customer decisions |
