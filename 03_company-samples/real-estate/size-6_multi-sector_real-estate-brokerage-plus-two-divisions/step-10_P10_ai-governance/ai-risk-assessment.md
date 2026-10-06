# AI Governance Risk Assessment: Group AI Program | Cris Santos Company Holdings

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (Residential Brokerage, Mortgage and Title, Homebuilding, corporate) |
| Tier / Vertical | Multi-Sector / Real Estate and Rental and Leasing |
| Scope | The group AI governance program: group standards, the division use-case inventory, and the regulator-specific rules for the priority use cases built around automated tenant and buyer screening: tenant screening (AI-001, brokerage), the mortgage pre-qualification model (AI-004), and the automated valuation model (AI-005), with shorter assessments of the other six |
| Framework | NIST AI RMF 1.0 (AI 100-1), the Generative AI Profile (AI 600-1) for AI-003 and AI-009, and the AI RMF Playbook |
| Assessors / date | Group AI council (chaired by the Group Chief Risk Officer), 2026-08-27; presented to the board risk committee 2026-09-17 |
| Inventory | `ai-use-case-inventory.csv` (9 use cases: 3 High, 4 Medium, 2 Low) |

**Why the registry default was adapted.** The registry default for this vertical is "automated tenant and buyer screening." At this size the group screens tenants (brokerage property management) and also screens buyers for credit (Home Loans' pre-qualification model and AVM). The assessment therefore covers both kinds of screening, because both are consequential decisions about housing and credit and share the same group governance gap (scenario gap 6).

## 1. GOVERN (group program)
### 1.1 Structure
| Body or role | Responsibility |
|---|---|
| Board risk committee | Oversees AI risk as part of enterprise risk; receives the High-tier list quarterly |
| Group AI council | Group Chief Risk Officer (chair), Group CISO, Group Chief Privacy Officer, Group General Counsel, Home Loans chief credit officer, Residential Brokerage president of property management, Title compliance officer, Homebuilding chief operating officer. Approves High-tier use cases and the approved-tools list |
| Division AI owners | Named business owner for each use case (inventory column); run monitoring and report monthly |
| Group CISO | AI security standard (prompt injection, model supply chain, data leakage) |
| Group Chief Privacy Officer | Use of customer information and consumer reports; biometric handling |
| Group internal audit | Includes High-tier AI controls in the annual assessment from 2027 |

### 1.2 Group AI Standard (adopted 2026-04, under POL-01 4.14)
1. **Register before use.** Every AI use case that uses customer information, consumer reports, or client data, or that supports decisions about applicants, borrowers, buyers, tenants, or homeowners, is registered in the inventory before deployment or material change.
2. **Tier with the repository rubric** (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`). High tier: council approval, a pre-deployment impact assessment, bias testing, notice to affected people, and quarterly monitoring reports.
3. **Vendor terms.** AI vendors that handle Restricted information sign contracts with no-training and retention terms and provide model documentation (POL-01 4.8; POL-04 4.9).
4. **Regulator overlays in each division supplement:** Fair Housing Act and FCRA for property management; ECOA, Fair Housing Act section 3605, and Reg Z AVM quality control for Home Loans; fair housing advertising rules for every division's marketing.
5. **Change gate.** A new model, new data source, new vendor, or a new decision role triggers re-assessment before release.
6. **Approved tools only** for workforce generative AI (POL-05 4.8). Generative AI is prohibited for credit, housing, screening, or valuation decisions.

**Where the program fell short in 2026.** The standard was adopted after all three priority use cases were in production. The AVM quality control policy (2025) required testing that never happened, tenant screening was never tested for disparities, and the pre-qualification model was last reviewed in 2024. All three are now under conditions (section 6).

## 2. MAP (division use cases and applicable rules)
| ID | Use case | Division | Tier | Status |
|---|---|---|---|---|
| AI-001 | Tenant screening recommendations | Residential Brokerage | High | In production; approved with conditions |
| AI-002 | Buyer lead scoring | Residential Brokerage | Medium | In production; inputs to be changed |
| AI-003 | Generative listing descriptions | Residential Brokerage | Low | In production with fair housing check |
| AI-004 | Mortgage pre-qualification model | Mortgage and Title (Home Loans) | High | In production; continue with conditions |
| AI-005 | AVM in credit decisions | Mortgage and Title (Home Loans) | High | In production; continue with conditions |
| AI-006 | Identity verification for closings | Mortgage and Title (Title) | Medium | In production |
| AI-007 | Wire anomaly scoring | Group (SYS-G5) | Medium | In production |
| AI-008 | Construction schedule optimization | Homebuilding | Low | In production |
| AI-009 | Enterprise generative AI assistant | Group | Medium | Pilot (3,000 employees) |

### 2.1 Tenant screening (AI-001): housing and consumer report rules
| Rule | What it requires | What it means for AI-001 |
|---|---|---|
| Fair Housing Act, 42 U.S.C. 3604(a)-(b) and (f) | No refusal to rent, and no different terms or conditions, because of race, color, religion, sex, familial status, national origin, or disability | Disparate impact claims are cognizable under the Act (*Texas Dept. of Housing and Community Affairs v. Inclusive Communities Project*, 576 U.S. 519 (2015)). A higher deposit is a term or condition |
| HUD discriminatory effects rule, 24 CFR 100.500 | Burden-shifting standard for discriminatory effects | In force as of 2026-10-06. HUD proposals of 2026-01-14 (91 FR 1475) and 2026-08-10 (91 FR 51416) are not final. A change to the rule would not remove liability under the statute |
| State fair housing laws (Fla. Stat. 760.23 worked example) | Parallel prohibitions | Apply in all 5 property management states |
| FCRA, 15 U.S.C. 1681b and 1681m(a); disposal rule 16 CFR 682.3 | Permissible purpose; adverse action notice for any adverse action based in whole or in part on a consumer report; secure disposal | Every decline **and** conditional approval needs a notice; reports must be disposed of securely |
| FTC Act Section 5 (N53-R02) | No unfair or deceptive practices | Covers the vendor's accuracy claims and the brokerage's representations to applicants |
| HUD tenant screening guidance (No. 24-098, 2024) | Not current federal guidance | Moved to HUD's archive; a 2025-09-16 memo removed tenant screening algorithm materials from the guidance repository. Used here only as background on good practice |

### 2.2 Pre-qualification model (AI-004) and AVM (AI-005): credit and valuation rules
| Rule | What it requires | What it means |
|---|---|---|
| ECOA, 15 U.S.C. 1691; Reg B 12 CFR 1002.9 | No credit discrimination on a prohibited basis; notice of action taken within 30 days of a completed application, with specific reasons for adverse action or the right to them | Applies to applications. Whether some pre-qualification requests are applications under Reg B depends on how Home Loans evaluates them; counsel decides by 2026-12-31. CFPB Circulars 2022-03 and 2023-03 on complex algorithms were withdrawn (90 FR 20084); the Reg B duty itself remains |
| Fair Housing Act, 42 U.S.C. 3605 | No discrimination in residential real estate-related transactions, including making loans and appraising residential property | Covers both the pre-qualification model and the AVM |
| Reg Z, 12 CFR 1026.42(i)(3) | Mortgage originators using AVMs in credit decisions must adopt policies, practices, procedures, and control systems so that AVMs meet quality control standards designed to (i) ensure a high level of confidence in the estimates, (ii) protect against data manipulation, (iii) seek to avoid conflicts of interest, (iv) require random sample testing and reviews, and (v) comply with nondiscrimination laws | Effective 2025-10-01 (89 FR 64538). Applies to Home Loans because it is a mortgage originator and not a financial institution as defined in 12 U.S.C. 3350(7) (1026.42(i)(1)). Using the AVM to set a maximum loan amount or to change loan terms is a credit decision under 1026.42(i)(2)(iv). **Gap:** factors (iv) and (v) not done; (i) not validated |
| FCRA, 15 U.S.C. 1681b | Permissible purpose for the soft credit inquiry | Consumer authorization captured in SYS-M1 |

### 2.3 Other use cases
| Use case | Rules | Implication |
|---|---|---|
| AI-002 lead scoring | 42 U.S.C. 3604(b) and (d) | Services may not be provided on different terms because of a protected class; ZIP code and language act as proxies. Re-tier to High if the score is used to decline representation or to choose which listings a buyer sees |
| AI-003 listing descriptions | 42 U.S.C. 3604(c) | AI drafts may contain discriminatory statements; human fair housing check before publication (POL-05 4.9) |
| AI-006 identity verification | Safeguards Rule 314.3(b); FTC Act Section 5; Florida law on biometric data | Whether face templates computed from a selfie or video are "biometric data" under Florida law is unsettled: Fla. Stat. 501.702 excludes photographs and data generated from video. Counsel to confirm; the group treats them as biometric data by policy (vendor deletes within 30 days) |
| AI-007 wire anomaly scoring | Safeguards Rule 314.4(c)(8) | A monitoring control; a human releases every held wire |
| AI-008 schedule optimization | None specific | Superintendents approve every schedule |
| AI-009 enterprise assistant | Safeguards Rule 314.4(c)(1)(ii), (f); AI 600-1 | Contract terms and data loss prevention; prohibited for consequential decisions |

**State AI laws.** Colorado SB26-189 (effective 2027-01-01) and California's ADMT regulations do not apply: the group has no operations in either state (P03 section 1.4). The Group General Counsel rechecks each year as the footprint changes.

## 3. Risk tiers (repository rubric)
- **High:** AI-001 (a substantial factor in housing decisions; in practice it is the decision), AI-004 and AI-005 (substantial factors in credit decisions: who is encouraged to apply, for how much, and on what terms).
- **Medium:** AI-002, AI-006, AI-007, AI-009. Humans make the final decision, but outputs shape who gets service, access, or payment timing.
- **Low:** AI-003, AI-008.

**Re-tier triggers:** using AI-002 to decline representation or steer listings; letting AI-006 reject consumers without human review; any use of AI-009 in a credit, housing, or valuation decision (prohibited); using AI-005 to deny credit without appraisal review.

## 4. MEASURE
Results are from monitoring and retrospective analyses between 2026-05 and 2026-08.

### 4.1 Tenant screening (AI-001)
Review of 64,800 applications screened from 2025-08-01 to 2026-07-31.

| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Sample of 60 reports checked against applicant documents | 4 reports included another person's records (name-only match); 3 counted dismissed eviction filings | **No** |
| Safe (automation bias) | Override rate; target between 3% and 15% (too low suggests rubber-stamping) | 1.9% | **No** |
| Accountable and transparent | Adverse action notice for every decline and conditional approval | Declines only; 0 of 20 sampled conditional approvals got a notice | **No** (15 U.S.C. 1681m(a)) |
| Explainable | Reason codes usable in notices; vendor model documentation | Reason codes shown; no model documentation | Partial |
| Privacy-enhanced | Reports disposed of when no longer needed | Kept indefinitely (POAM-010) | **No** |
| Fair, harmful bias managed | Approval-rate ratio against the highest group; flag below 0.80 | Applicants estimated Black 0.72; Hispanic 0.86; Asian and other 0.94 | **Flagged** |

**Bias testing plan (AI-001).** Race and ethnicity are estimated with Bayesian Improved Surname Geocoding and used only in aggregate, never on an applicant's file. Familial status and disability cannot be estimated reliably, so the criteria themselves are reviewed (for example, how income multiples treat housing vouchers and disability benefits). Metrics: approval, conditional approval, and decline rates by group; the approval-rate ratio against the highest group; reason-code frequency by group. A ratio below 0.80 is a **screening flag**, borrowed from the four-fifths rule of thumb, not a legal conclusion. Any flag triggers a driver analysis and a counsel review under the burden-shifting standard in 24 CFR 100.500(c). Quarterly, on all applications. **Current drivers:** 61% of declines among applicants estimated Black were driven by eviction filings (including dismissed filings) and criminal records more than 7 years old.

### 4.2 Pre-qualification model (AI-004)
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Pre-qualified amount within 10% of the later approved amount | 84% of 9,400 requests that became funded loans | Yes |
| Fair, harmful bias managed | Share of applicants pre-qualified at less than 80% of the amount later approved, by government monitoring information collected at application; flag a gap of more than 3 points | Overall 9%; applicants who identified as Black 15%; Hispanic 12% | **Flagged.** Driver: a ZIP-level home value trend feature |
| Explainable | Consumers told why a pre-qualified amount is lower | No reasons shown | **No** |
| Accountable | Model review cycle | Last validated 2024 | **No** |

### 4.3 AVM (AI-005), against 12 CFR 1026.42(i)(3)
| Factor | Test / metric | Result | Pass? |
|---|---|---|---|
| (i) High level of confidence | Confidence threshold validated against appraisals | Threshold set in 2025, never validated | **No** |
| (ii) Data manipulation | Loan officers cannot edit property data after the AVM call; changes logged | In place (P03 MT-G-019) | Yes |
| (iii) Conflicts of interest | Vendor chosen and overseen by credit risk, not production | In place | Yes |
| (iv) Random sample testing | Quarterly sample of AVM values against appraisals | Never done; a one-time council analysis of 400 loans with both values found a median absolute error of 6.1% | **No** |
| (v) Nondiscrimination | Error and use by census tract demographics | In the same 400 loans: median absolute error 9.8% in majority-minority tracts against 5.4% elsewhere; AVM more than 10% below the appraisal in 14% of majority-minority tract loans against 7% elsewhere | **Flagged** |

### 4.4 Other use cases
| Use case | Metric | Result | Pass? |
|---|---|---|---|
| AI-002 lead scoring | Median first-contact time by inquiry language; flag above twice the overall median | Spanish-language inquiries 19 hours; English 2 hours | **Flagged** |
| AI-006 identity verification | Failed-check rate by age band (vendor gives no demographic data) | Overall 3.2%; consumers 75 and older 6.9%; all failures reviewed the same day | Flagged; manual path works |
| AI-007 wire anomaly scoring | Detection in a red-team test of 4 simulated diversions; hold rate | 3 of 4 held; hold rate 1.1% | Yes, tune for payoff changes |
| AI-009 assistant (AI 600-1 data privacy) | Sampled prompts containing customer information | 2.4% of 500 sampled prompts | Within terms; data loss prevention rules added |

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** written screening criteria published to applicants; a leasing coordinator reviews every decline and conditional approval before any notice; individualized review of criminal and eviction records; the applicant can explain or correct a record; monthly review of overrides by the president of property management.
- **AI-004:** loan officers review every pre-qualification; consumers are told they may apply regardless; reasons for a lower amount are shown from 2027-01.
- **AI-005:** an AVM value more than 10% below the contract price triggers appraisal review, never an automatic term change; underwriters decide.
- **AI-006:** every failed check goes to a Title closer the same day.
- **AI-007:** Treasury analysts release or reject every held wire.

**Monitoring:** monthly metrics to division owners; quarterly High-tier report to the council and the board risk committee; P01 risks GR-07, BR-016, BR-017, BR-019, BR-021, MT-004, MT-005, MT-016, and GR-17.

**Incident handling:** an AI failure that wrongly denies housing or credit, discloses customer information, or exposes biometric data follows POL-03 and P08; vendor incidents follow the third-party notice path in the matrix.

**Decommissioning:** each use case has an off switch and a fallback the BIA already covers (P05): manual screening against written criteria (BP-BR07), loan officer pre-qualification and appraisals (BP-MT03), manual identity verification by phone (BP-BR02), and manual wire review (BP-G03).

## 6. Decisions
| Use case | Decision | Conditions and dates |
|---|---|---|
| AI-001 tenant screening | **Approve with conditions** (council 2026-08-27; board risk committee informed 2026-09-17) | Adverse action notices for conditional approvals by 2026-11-30; coordinator review and individualized record review by 2026-11-30; count eviction judgments only and limit criminal lookback to a counsel-approved list by 2026-12-31; second identifier for record matches; vendor model documentation by 2026-12-31; first quarterly disparity test on post-change data by 2027-01-31 (POAM-020). Turn off automated recommendations if the ratio stays below 0.80 for two quarters without a documented justification |
| AI-004 pre-qualification | **Continue with conditions** | Remove the ZIP-level trend feature and revalidate by 2026-12-31; counsel decision on when a request is a Reg B application by 2026-12-31; reason statements by 2027-01-31; annual validation |
| AI-005 AVM | **Continue with conditions** | No use of AVM values to lower pre-qualified amounts until testing is in place; quarterly random sample testing from 2026-11-30; threshold validation by 2026-12-31; nondiscrimination review by 2027-01-31; if the tract error gap persists, require appraisals in affected tracts (POAM-019) |
| AI-002 lead scoring | **Approve with conditions** | Remove ZIP code and language inputs by 2026-12-31; route Spanish-language leads to Spanish-speaking agents; monthly response-time parity check |
| AI-006 identity verification | **Continue** | Vendor demographic error data by 2027-03-31; keep the same-day manual path; counsel confirms the biometric classification |
| AI-007 wire anomaly scoring | **Approved** | Tune for payoff changes; quarterly red-team tests |
| AI-003, AI-008 | **Approved** | Standard monitoring; fair housing check for AI-003 |
| AI-009 enterprise assistant | **Pilot continues** | Data loss prevention rules; contractor agents excluded until the agent MFA program is complete (POAM-001); prohibited for consequential decisions |
