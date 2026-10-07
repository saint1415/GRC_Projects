# AI Risk Assessment: AI Credit Underwriting Model (LOS Scoring Add-on)

| Field | Value |
|---|---|
| Organization | Cris Santos Community Federal Credit Union (member-owned federal credit union) |
| Tier / Vertical | Micro / Finance and Insurance |
| AI use case | AI-001: the LOS vendor's AI credit scoring add-on for online consumer auto and personal loan applications up to $25,000, in a pilot since 2026-04-06 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the AI RMF Playbook |
| Assessor / date | Lending Manager and the ISO, with the Accounting and Compliance Officer (fair lending), 2026-08-21 |
| Decision | President and CEO, 2026-08-31, after the board was briefed on 2026-08-25 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases; AI-001 assessed here in full) |

## 1. GOVERN
- **Accountable owner:** Lending Manager. **Fair lending review:** Accounting and Compliance Officer. **Security and vendor terms:** ISO. **Decision authority:** President and CEO; the board is briefed because the tier is High.
- **Policies that apply:**
  - POL-04 4.5: the ISO approves any new vendor feature that touches member information before it is switched on. **The add-on was switched on by the LOS vendor at the Lending Manager's request in April 2026, before that rule existed and with no review** (gap 11 in the scenario facts; P03 G-028).
  - POL-02 A.5: vendor due diligence and contract terms apply to the model vendor.
  - POL-04 4.6: the add-on is the only AI tool approved for member information, and only under the conditions in section 6.
- **Inventory:** the ISO keeps the AI inventory. AI-001 was added on 2026-08-21, with AI-002 and AI-003.
- **Scale for a Micro credit union:** there is no AI committee. The Lending Manager, the ISO, and the Accounting and Compliance Officer review AI use each quarter and report to the President and CEO, who briefs the board.

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Score online applications for consumer auto and personal loans up to $25,000, recommend approve, refer, or decline, and give up to 4 reason codes. The goal is faster decisions for members who apply online after hours |
| Users / operators | Lending Manager; the LOS applies auto-approvals without a person |
| Affected people | Applicants (members and people joining to borrow). Pilot from 2026-04-06 to 2026-08-14: **212 scored applications.** 97 were approved automatically. 115 were referred to the Lending Manager (the model recommended decline on 52 and refer on 63); of those, 61 were approved, 45 declined, and 9 withdrawn or incomplete |
| Data | Inputs: credit report attributes, stated income and debts, employment length, membership tenure, share balances and 6 months of deposit cash flow from the core, vehicle value for auto loans, and vendor "digital identity" signals (age of the email address, phone line type, and whether the phone and email match other records). Outputs: a score, a recommendation, and reason codes stored in the LOS |
| Build or buy | Configure: a vendor-built machine learning model inside the vendor's SaaS LOS. The credit union sets the approve and decline cutoffs and the loan types |
| Human role | The model makes approvals by itself above the cutoff. For declines, the Lending Manager followed the model's decline recommendation in 43 of 49 decided cases (88%), so the model is a **substantial factor** in declines |
| Not intended | Automatic declines, pricing, loans above $25,000, in-branch applications, mortgages. Any of these requires re-assessment |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| ECOA and Regulation B, 12 CFR 1002.9 (notice of action taken and adverse action) | **Yes** | A decline is adverse action. The notice must be in writing within 30 days of a completed application and state specific principal reasons (or the right to them). Statements that the applicant failed to achieve a qualifying score on the creditor's scoring system are **insufficient** (1002.9(b)(2)). For a federal credit union, NCUA enforces ECOA compliance (15 U.S.C. 1691c(a)(2)) |
| Regulation B, 12 CFR 1002.4(a) and 1002.6(b)(1) (discrimination) | **Yes** | The credit union must not discriminate on a prohibited basis in any aspect of a credit transaction or take a prohibited basis into account in any system of evaluating creditworthiness. A model input that works as a close proxy for national origin or race raises this risk |
| Regulation B, 12 CFR 1002.6(a) ("effects test") | **Yes, shapes the test** | 1002.6(a) now states that the Act does not provide that the effects test applies. Outcome disparities are therefore not by themselves a Regulation B violation. The credit union still measures them, as a warning that an input may be acting as a proxy for a prohibited basis |
| Regulation B, 12 CFR 1002.6(b)(2) (age) | **Yes** | Age may be used only in an empirically derived, demonstrably and statistically sound scoring system, and an elderly applicant's age must not receive a negative value. The vendor's documentation says the model does not use applicant age; it uses the age of the oldest credit account |
| FCRA adverse action notice, 15 U.S.C. 1681m(a) | **Yes** | Declines rely in part on consumer reports, so the notice must include the credit score used, the consumer reporting agency's contact details, and the consumer's rights. The LOS notice template includes these |
| CFPB Circulars 2022-03 and 2023-03 (complex algorithms and adverse action) | **No longer in effect** | Withdrawn on 2025-05-12 (90 FR 20084), per the vertical research. The 1002.9 duty itself is unchanged |
| GLBA and NCUA Part 748 Appendix A III.D (N52-R01) | **Yes** | The LOS vendor is a service provider that processes member information; due diligence, contract terms, and monitoring apply |
| State AI laws (for example Colorado SB26-189, effective 2027-01-01) | No | The field of membership is one Florida county and loans are made to Florida residents. State AI laws outside Florida are out of scope by decision; recheck if the credit union lends to residents of other states |
| Model risk management guidance | Program choice | The credit union applies validation, outcomes analysis, and vendor documentation review as a policy choice. Whether any agency model risk guidance applies to a credit union of this size was not verified for this assessment |

## 3. Risk tier
**Tier: High** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`).

**Why High:** the model makes credit approvals on its own and is a substantial factor in declines (88% agreement), and its reason codes flow directly into adverse action notices. Credit is a consequential decision category.

**Minimum controls for High:** human review before action, pre-deployment bias testing, an impact assessment (this document), notice to affected people (the adverse action notice), and ongoing monitoring. Bias testing and a review of reason codes were **not done** before the pilot. Auto-approval has no human review; section 5 explains why that is kept, with monitoring, for favorable outcomes only.

## 4. MEASURE
| Trustworthy characteristic | Test / metric | Result (pilot, 2026-04-06 to 2026-08-14) | Pass? |
|---|---|---|---|
| Valid and reliable | Validation on the credit union's own members; agreement with the Lending Manager | The vendor's validation covers only its pooled development sample; no validation on credit union data. Agreement on declines 88%. Too early to measure defaults | **No** |
| Safe | Limits held: loans up to $25,000, online only, no automatic declines | Limits held on all 212 applications | Yes |
| Secure and resilient | Vendor SOC 2 report; MFA on LOS staff accounts; model version change notice | MFA on for both LOS users; SOC 2 report requested, not yet received; no change notice term | Partial |
| Accountable and transparent | Named owner; inventory entry; overrides recorded | Owner and inventory in place since 2026-08-21; override reasons not recorded before August | Partial |
| Explainable and interpretable | Reason codes specific enough for 1002.9(b)(2) | **9 of 45 decline notices** gave "insufficient model score" as a principal reason, which is insufficient | **No** |
| Privacy-enhanced | Contract bars secondary use; data minimization | The add-on terms let the vendor use "de-identified application data" to improve its models; digital identity signals come from a third-party data source the credit union has not reviewed | **No** |
| Fair, with harmful bias managed | Approval-rate ratio by estimated ethnicity and by age 62 and over; auto-approval rate by group; proxy review of inputs | Of 203 decided applications, 158 were approved. Hispanic-estimated applicants: 38 of 58 approved (65.5%); non-Hispanic white-estimated: 102 of 121 (84.3%); ratio **0.78**, below the 0.80 flag. Auto-approval: 17 of 58 (29%) versus 68 of 121 (56%). Digital identity signals were among the top 4 reasons in 13 of the 20 declines of Hispanic-estimated applicants. Age 62 and over: 25 of 31 approved (80.6%) versus 133 of 172 under 62 (77.3%); no flag | **No.** Flag raised; sample is small |

**Bias finding.** The sample is too small for statistical conclusions, but the flag, the gap in auto-approvals, and the reason-code pattern point to the digital identity signals as a possible proxy for national origin (for example, prepaid phone lines and recently created email addresses). The credit union will have the vendor turn those signals off for its members and re-test on the pilot applications before any expansion.

### Bias and fairness testing plan
| Item | Plan |
|---|---|
| Data | (1) Now: the 212 pilot applications, re-scored with and without the digital identity signals. (2) Ongoing: all scored applications, every quarter |
| Groups compared | Race and ethnicity estimated with a surname and geography proxy method (Regulation B generally bars asking for these on non-mortgage consumer credit, 1002.5(b)); sex estimated by first name; age 62 and over versus younger (age is on the application) |
| Metrics and thresholds | Approval-rate ratio: flag below 0.80. Auto-approval-rate ratio: flag below 0.80. Frequency of each reason code by group: flag if one code is twice as frequent in a group's declines. Override rates by group: flag a difference of more than 10 percentage points |
| Proxy review | For every flag, test whether each input (especially the digital identity signals, membership tenure, and deposit cash flow) predicts group membership; remove or neutralize inputs that act as close proxies and are not needed for accuracy |
| Less discriminatory alternative | Compare the model with and without flagged inputs; prefer the version with smaller disparities where accuracy is comparable, and record the trade-off |
| Who and when | Independent reviewer of the vendor's validation and the fairness tests (about $6,000, funded in P01) before any expansion, due 2026-12-31; the Accounting and Compliance Officer quarterly after that; results to the President and CEO and the board |

## 5. MANAGE
**Human-in-the-loop design:**
- **Declines:** the model recommends; the Lending Manager decides and records their own reasons in the LOS. From 2026-09-15 the Accounting and Compliance Officer reviews every model-recommended decline before the notice is sent. The model can never decline by itself.
- **Approvals:** auto-approval above the cutoff continues, because an approval is a favorable outcome and removing it would slow members who apply after hours. It is kept only with monitoring: the Lending Manager reviews a monthly sample of 10 auto-approvals, and auto-approval rates are part of the fairness tests. If the auto-approval ratio stays below 0.80 after the digital identity signals are turned off, auto-approval is paused.
- Overrides in either direction need a written reason in the LOS.

**Adverse action notices:**
- The Accounting and Compliance Officer maps each reason code to specific, plain-language principal reasons; score-only codes are removed from the notice template by 2026-10-15.
- The 9 applicants who received insufficient reasons are sent a corrected statement of specific reasons by 2026-10-15.

**Data protection and vendor terms (POL-02 A.5):** amend the add-on terms by 2026-11-30 to bar any use of member data beyond providing the service (including de-identified use), give the credit union the model documentation and validation summary, require 30 days' notice before model changes, and name the source of the digital identity data. Counsel confirms whether that data is a consumer report under the FCRA.

**Monitoring:** quarterly fairness tests (above); a monthly drift check on the approval and auto-approval rates, flagging a change of more than 10 percentage points; risk register entry R-011 (P01) tracks the residual risk.

**Incident handling:** a security incident at the LOS vendor follows POL-03 and the P08 escalation path, including the 72-hour NCUA decision for third-party incidents (748.1(c)(1)(i)(C)). A fair lending issue goes to the Accounting and Compliance Officer and counsel.

**Decommissioning:** turn the add-on off and return to manual underwriting if the independent review finds the model unsound for the credit union's members, if a fairness flag cannot be explained or fixed within one quarter, or if the vendor will not accept the contract terms.

## 6. Decision
**Approve continued pilot with conditions.** President and CEO, 2026-08-31. The pilot may continue **only if** these conditions are met by 2026-10-15:
1. The vendor turns off the digital identity signals for the credit union's applications and confirms it in writing.
2. The second review of every model-recommended decline is in place (from 2026-09-15).
3. Reason codes are mapped to specific reasons, and corrected statements are sent to the 9 affected applicants.
4. Override reasons are recorded for every referred application.

**Expansion** to loans above $25,000, to in-branch applications, or to other loan types requires: the independent review of validation and fairness, a re-test with no unexplained flag, the amended vendor terms, and a board briefing. Target: 2026-12-31 (P01 R-011).

**Related actions.** AI-002 (online banking fraud scoring): ask the digital banking provider for a description of its fraud model in the SOC review due 2026-11-30 (P09). AI-003 (public chatbots): prohibited for member information (POL-04 4.6); covered in annual training.
