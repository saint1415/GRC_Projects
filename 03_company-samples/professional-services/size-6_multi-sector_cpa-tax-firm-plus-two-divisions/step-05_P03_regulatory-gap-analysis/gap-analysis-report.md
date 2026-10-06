# Regulatory Gap Analysis: Cris Santos Company Holdings | Professional Services | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (three divisions plus corporate shared services; CPA Partners included under the administrative services agreement) |
| Tier / Vertical | Multi-Sector / Professional, Scientific, and Technical Services (focus division: CPA and Tax Services) |
| Primary regulation | FTC Safeguards Rule, 16 CFR Part 314 (N54-R01), for Tax and Advisory. Text read from eCFR, current through 2026-09-23 |
| Division regulations | Tax and Advisory: IRC 7216 and 26 CFR 301.7216-1 to -3 (N54-R02) and IRS e-file duties (N54-R03). CPA Partners: HIPAA business associate duties (N54-R06). Wealth: SEC Regulation S-P (N52-R05), Regulation S-ID (N52-R06), and Advisers Act compliance and records rules. Practice Cloud: Safeguards Rule duties flowed down by customer contracts, IRC 7216 as an auxiliary-services preparer, SOC 2 and contract commitments, FTC Act Section 5 (N51-R01) |
| Gap tables | `gap-analysis.csv` (CPA and Tax Services, 65 rows); `gap-analysis-wealth.csv` (26 rows); `gap-analysis-practice-cloud.csv` (21 rows) |
| Assessment dates | 2026-05-04 to 2026-07-31, with evidence updated from the P07 assessment (to 2026-08-28) |
| Assessors | Division security and compliance leads, the Wealth Chief Compliance Officer, and the Practice Cloud trust and assurance director, coordinated by the Group Chief Privacy Officer; reviewed by group internal audit |

## 1. Applicability
### 1.1 Who is what
| Entity | Role under the rules | Basis |
|---|---|---|
| Tax and Advisory | **Financial institution** under the FTC Safeguards Rule. 16 CFR 314.2(h)(2)(viii) gives this example: "An accountant or other tax preparation service that is in the business of completing income tax returns is a financial institution." Individuals who become clients "for the purpose of obtaining tax preparation" services are customers (314.2(e)(2)(i)(H)) | 16 CFR 314.1(b), 314.2 |
| Tax and Advisory | **Tax return preparer** for IRC 7216, together with every employee who assists in preparation, including seasonal staff and scanning staff | 26 CFR 301.7216-1(b)(2)(i)(A), (D) |
| Tax and Advisory | **Authorized IRS e-file Provider** acting as an ERO | IRS Pub. 1345 |
| Tax and Advisory | **Service provider to Wealth** for integrated planning data it receives and holds for Wealth | 17 CFR 248.30(d)(10) |
| CPA Partners | **HIPAA business associate** of about 85 health care audit clients under engagement BAAs | 45 CFR 164.504(e); N54-R06 |
| Wealth | **Covered institution** under Regulation S-P: "any investment adviser ... registered with the Commission" | 17 CFR 248.30(d)(3) |
| Wealth | Within **Regulation S-ID**, which applies to a registered adviser that is a financial institution or creditor under the FCRA (counsel's 2024 determination) | 17 CFR 248.201(a)(3) |
| Wealth | **Registered adviser** with a compliance program and records duties | 17 CFR 275.206(4)-7; 275.204-2 |
| Practice Cloud | **Service provider** to its customer firms (which are themselves Safeguards Rule financial institutions), a **third-party agent** under state breach laws, and, in group legal's position, a **tax return preparer providing auxiliary services** | 16 CFR 314.4(f); Fla. Stat. 501.171(6) (worked example); 26 CFR 301.7216-1(b)(2)(i)(B) |
| Holding company | **SEC registrant** | Reg S-K Item 106; Form 8-K Item 1.05 |

### 1.2 The Safeguards Rule applies to Tax and Advisory in full
- **No size exception.** Section 314.6 exempts 314.4(b)(1), (d)(2), (h), and (i) only for institutions that maintain customer information on fewer than 5,000 consumers. Tax and Advisory holds it on about 24 million. Every element applies.
- **The Qualified Individual is an affiliate's employee.** 314.4(a) allows the Qualified Individual to be "employed by you, an affiliate, or a service provider." Because the Group CISO is employed by the holding company, Tax and Advisory must also (1) retain responsibility for compliance, (2) designate a senior member to direct and oversee the Qualified Individual, and (3) require the affiliate to maintain a program that protects it under Part 314. Rows G-004 to G-006 assess each.
- **The governing body is the subsidiary's board of managers.** 314.4(i) requires a written report "to your board of directors or equivalent governing body." For Tax and Advisory that is its board of managers, not the holding company board, although the board risk committee receives the same content.
- **Customer information of other institutions is in scope.** 314.1(b) applies the rule to all customer information in Tax and Advisory's possession, "regardless of whether such information pertains to individuals with whom you have a customer relationship." Integrated planning data received from Wealth is therefore protected under both Part 314 and Wealth's Regulation S-P program.

### 1.3 Why Wealth is under Regulation S-P, not the FTC rule
314.1(b) limits the FTC rule to financial institutions "not otherwise subject to the enforcement authority of another regulator under section 505" of the Gramm-Leach-Bliley Act. GLBA section 505(a)(5) (15 U.S.C. 6805(a)(5)) assigns investment advisers registered with the SEC to the SEC, as the Finance Sole Proprietor sample verified. Wealth is a "larger entity" (assets under management of $1.5 billion or more), so its Regulation S-P compliance date was 2025-12-03; the amended rule is in force for it.

### 1.4 Practice Cloud is not treated as a financial institution
Group legal recorded on 2026-06-10 that Practice Cloud provides software and document services to accounting firms rather than financial products to consumers, so it is analyzed as a service provider whose duties come from customer contracts (which carry 314.4(f)(2) terms), state third-party agent laws, IRC 7216, its SOC 2 commitments, and FTC Act Section 5. Counsel revisits this if Practice Cloud begins to move client funds itself.

### 1.5 IRC 7216 at group scale
Section 7216 binds the **preparer**, and each legal entity is a separate person. 301.7216-2(c)(2) lets information move without consent only within "the same tax return preparer." Wealth is a separate company, so every disclosure of tax return information from Tax and Advisory to Wealth needs a permission or a consent that meets 301.7216-3:
- the consent must identify the recipient and, for solicitations, "each specific type of product or service" (301.7216-3(a)(3)(i)(B); the regulation's own examples include mutual funds, individual retirement accounts, and life insurance);
- it must be signed **before** the disclosure (301.7216-3(b)(1));
- consent to solicitation of business unrelated to tax preparation may not be requested after the completed return is provided for signature, nor requested again after a refusal (301.7216-3(b)(2), (3));
- statistical compilations of tax return information are themselves tax return information (301.7216-1(b)(3)(i)(B)), and 301.7216-2(o) permits them only for the preparer's own tax preparation business or bona fide tax research, disclosed only anonymously from 10 or more returns.

The IRS Section 7216 Information Center lists no guidance on artificial intelligence (checked 2026-09-25 for the Small sample of this industry), so the AI rows apply the regulation text and counsel confirms them.

### 1.6 Considered and excluded
- **FAR 52.204-21, DFARS 252.204-7012, and CMMC (N54-R04, N54-R05):** no federal contracts or subcontracts in any division.
- **ABA Model Rules (N54-R07):** no law practice.
- **AICPA confidentiality rule (N54-R08):** a professional standard binding CPA Partners' CPAs through state boards; its text was not verified from the source for this sample, so it is noted, not assessed.
- **PCAOB:** CPA Partners audits no issuers and is not registered.
- **NYDFS Part 500 (N52-R04):** no group entity is licensed by the New York Department of Financial Services.
- **314.6 exception:** recorded as a row (G-044) to document the decision.

## 2. Regulation-by-division matrix
| Requirement | Tax and Advisory | CPA Partners | Wealth | Practice Cloud | Group (corporate) |
|---|---|---|---|---|---|
| N54-R01 FTC Safeguards Rule, 16 CFR 314 | **Primary.** Applies in full | Not a financial institution for its attest work | Not applicable (SEC jurisdiction, 314.1(b)) | Flowed down by customer contracts (314.4(f)) | Affiliate providing the Qualified Individual and shared services (314.4(a)(3)) |
| N54-R02 IRC 7216 | **Applies** (preparer) | Applies only if it prepares returns (it does not; tax work is in Tax and Advisory) | Recipient: may receive only what a valid consent covers | Applies as auxiliary-services preparer (group legal position) | Not a preparer; operates systems under contractor terms (301.7216-2(d)(2)) |
| N54-R03 IRS e-file, Pubs. 1345, 4557, 5708 | **Applies** (ERO) | Not applicable | Not applicable | Supports customers' Form 8879 e-signature duties | Not applicable |
| N54-R06 HIPAA as business associate | Not applicable (no PHI) | **Applies** (about 85 health care audit clients) | Not applicable | Not applicable (no BAAs offered) | Subcontractor to CPA Partners for PHI (not yet papered) |
| N52-R05 Regulation S-P, 17 CFR 248.30 | Service provider to Wealth (248.30(a)(5)) | Not applicable | **Applies** (covered institution) | Not applicable | Service provider to Wealth (amended agreement 2025-11) |
| N52-R06 Regulation S-ID, 17 CFR 248.201 | Not applicable | Not applicable | **Applies** | Not applicable | Not applicable |
| Advisers Act rules, 17 CFR 275.206(4)-7 and 275.204-2 | Not applicable | Not applicable | **Applies** | Not applicable | Not applicable |
| N51-R01 FTC Act Section 5 | Applies (general) | Applies (general) | Limited (SEC-regulated activity) | **Applies** (security and AI claims) | Applies |
| N51-R03 CCPA and CPPA regulations | GLBA-covered data exempt at the data level (1798.145(e)); other data in scope where it does business in California | Same | Same | As a service provider for customer firms that are CCPA businesses | Group privacy program |
| N51-R04 DOJ Data Security Program, 28 CFR 202 | Applies (bulk financial data) | Applies | Applies | Applies | Group vendor screening |
| N52-R04 NYDFS Part 500 | Not applicable | Not applicable | Not applicable (no DFS license) | Not applicable | Not applicable |
| N51-R02 COPPA; N51-R07 FedRAMP | Not applicable | Not applicable | Not applicable | Not applicable (no child-directed service; no federal agency customers) | Not applicable |
| N52-R08 / N51-R08 SEC Reg S-K Item 106; Form 8-K Item 1.05 | Via group | Via group (not part of the registrant) | Via group | Via group | **Applies** (SEC registrant) |
| Circular 230, 31 CFR 10.22 | Applies to CPAs and enrolled agents who practice before the IRS | Applies to its CPAs | Not applicable | Not applicable | Not applicable |
| State breach notification laws | Each state where affected individuals reside (Florida worked example: Fla. Stat. 501.171) | Same | Same | Third-party agent duties to customer firms (501.171(6)(a) worked example) | Coordinates |
| SOC 2 (contractual) | Client accounting services readiness (P09) | Issues SOC reports for outside clients only | Not in scope (P09) | **Annual Type 2** (P09) | Group services carved in |
| N54-R09 CIRCIA | Proposed only; not an obligation | Same | Same | Same | Same |

## 3. Method
1. **Requirements.** Each paragraph of 16 CFR 314.3 and 314.4 became one row, split to the lowest level that states its own duty, including 314.4(a)(1) to (3) because the Qualified Individual is an affiliate's employee. IRC 7216 rows follow each permission or condition that governs how Tax and Advisory shares tax return information. Regulation S-P rows follow 248.30(a) and (b) paragraph by paragraph; S-ID and Advisers Act rows cover the program elements. Practice Cloud rows follow its legal duties and the SOC 2 and contract commitments it has made. Text was read from the eCFR (current through 2026-09-23).
2. **Crosswalk.** Each row was mapped to CSF 2.0 subcategories and SP 800-53 Rev. 5 controls. These are **author mappings**: no official NIST mapping of 16 CFR 314, 26 CFR 301.7216, or 17 CFR 248 and 275 was found. SOC 2 criteria are listed by ID only, with short topic labels.
3. **Evidence.** Interviews with each division's leadership, privacy and compliance staff, and counsel; document and contract review; configuration exports; a sample of 80 integrated planning referrals (consent content, timing, and fields sent); and P07 test results.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale.

## 4. Results
### 4.1 CPA and Tax Services (`gap-analysis.csv`)
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| 314.3 Program and objectives | 1 | 1 | 0 | 0 |
| 314.4(a) Qualified Individual (affiliate-employed) | 3 | 1 | 0 | 0 |
| 314.4(b) Risk assessment | 5 | 0 | 0 | 0 |
| 314.4(c) Safeguards | 3 | 7 | 0 | 0 |
| 314.4(d) Testing and monitoring | 4 | 0 | 0 | 0 |
| 314.4(e) Personnel and training | 3 | 1 | 0 | 0 |
| 314.4(f) Service providers | 2 | 1 | 0 | 0 |
| 314.4(g) Evaluate and adjust | 1 | 0 | 0 | 0 |
| 314.4(h) Incident response plan | 5 | 3 | 0 | 0 |
| 314.4(i) Report to governing body | 1 | 0 | 0 | 0 |
| 314.4(j) FTC notification | 0 | 1 | 0 | 0 |
| 314.6 Exception | 0 | 0 | 0 | 1 |
| **Safeguards Rule subtotal (44)** | **28** | **15** | **0** | **1** |
| 26 CFR 301.7216 (12) | 3 | 6 | 3 | 0 |
| IRS e-file and PTIN requirements (5) | 4 | 1 | 0 | 0 |
| HIPAA business associate, CPA Partners (4) | 0 | 3 | 1 | 0 |
| **Total (65)** | **35** | **25** | **4** | **1** |

Of the 29 unmet or partially met rows, 9 are rated High, 16 Moderate, and 4 Low.

**The Safeguards Rule program is mature where the group built it once.** Risk assessment, testing (annual penetration tests and continuous scanning), training, the written plan, and the annual report to the board of managers are all Met. The gaps are in safeguards that touch seasonal staff and office email (314.4(c)(1), (c)(5), (c)(8)) and in exercising the cross-division plan (314.4(h), (j)).

**IRC 7216 is where the division is weakest.** All three Not met rows are about Wealth: statistical compilations used by another company (G-046), a consent template that does not name each product or service (G-052), and consents requested at the signing appointment, after the completed return is provided (G-055).

### 4.2 Wealth (`gap-analysis-wealth.csv`)
| Obligation group | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| Regulation S-P, 248.30 (14) | 8 | 5 | 0 | 1 |
| Advisers Act rules, 275.204-2 and 275.206(4)-7 (6) | 4 | 2 | 0 | 0 |
| Regulation S-ID, 248.201 (4) | 2 | 2 | 0 | 0 |
| Applicability rows: FTC rule, NYDFS (2) | 0 | 0 | 0 | 2 |
| **Total (26)** | **14** | **9** | **0** | **3** |

Of the 9 partially met rows, 7 are Moderate and 2 Low. Wealth adopted its amended Regulation S-P program on time. Its gaps come from **affiliates**: Tax and Advisory holds integrated planning data for Wealth but is not in Wealth's service provider oversight and is not bound to the 72-hour notice in 248.30(a)(5)(i)(B), and the notice procedure does not say when Wealth "becomes aware" of an incident at an affiliate (248.30(a)(4)(iii)). The AI meeting notes pilot also creates advice records outside the archive (275.204-2(a)(7)).

### 4.3 Practice Cloud (`gap-analysis-practice-cloud.csv`)
| Obligation group | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| Safeguards Rule duties flowed down to Practice Cloud (3) | 2 | 1 | 0 | 0 |
| IRC 7216 as auxiliary-services preparer (4) | 1 | 2 | 1 | 0 |
| SOC 2 commitments (6) | 1 | 3 | 2 | 0 |
| Customer contracts (3) | 0 | 2 | 1 | 0 |
| State, FTC Act, DOJ, CCPA, COPPA and FedRAMP (5) | 3 | 1 | 0 | 1 |
| **Total (21)** | **7** | **9** | **4** | **1** |

Of the 13 unmet or partially met rows, 5 are High, 5 Moderate, and 3 Low. **All four Not met rows trace to the AI document intake feature** (scenario gap 5): no recorded IRC 7216 basis for sending customers' client documents to the model provider, no system description or customer communication of the change for the SOC 2 period, and no sub-processor notice.

## 5. Group roadmap
| # | Gap (scenario gap) | Units | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|---|---|
| 1 | Tax-to-wealth sharing without compliant consent (1) | Tax, Wealth | 301.7216-3(a)(3)(i)(B), (b)(1)-(3); 301.7216-1(b)(3)(i)(B); 301.7216-2(o) | High | Consent register enforced by the interface; new consent at engagement start; stop compilations; re-consent | Chief Tax Officer; Group Chief Privacy Officer | 2026-12-31 (interface); 2027-03-31 (consents) |
| 2 | Legacy authentication and monitoring gaps in tax office email (3) | Tax, group | 314.4(c)(5), (c)(8) | High | Block legacy authentication; tax office inbox-rule alerts; portal upload | Group collaboration services director; Group SOC director | 2027-01-04 |
| 3 | Practice Cloud AI feature commitments (5) | Practice Cloud | 301.7216-2(d)(1); SOC 2 description, CC2.3, CC8.1; contracts | High | Description update; sub-processor notice; customer 7216 information pack; contract term for U.S. processing | Practice Cloud division president | 2026-12-31 |
| 4 | Tax AI governance (4) | Tax | 314.4(c)(4), (c)(7); 301.7216-2(d)(1); 31 CFR 10.22 | Moderate | Accuracy and bias monitoring for AI-001; AI-002 restricted until reviewed | Chief Tax Officer | 2027-01-04 |
| 5 | Seasonal identity (2) | Tax, group | 314.4(c)(1)(i), (e)(1) | Moderate | Activation gated on screening and training; same-day expiry | Group identity director; seasonal workforce director | 2027-01-04 |
| 6 | Cross-division notification not exercised (6) | All | 314.4(h)(4), (j); Pub. 1345; 248.30(a)(4)(iii); 164.410; Form 8-K Item 1.05 | Moderate | Combined matrix; tabletop | Group General Counsel | 2026-12-15 |
| 7 | Affiliate agreements and oversight (6, 7) | Wealth, CPA Partners | 248.30(a)(5)(i); 164.308(b)(2); 164.314(a); 314.4(a)(3) | Moderate | Amend the integrated planning and administrative services agreements; add affiliates to Wealth oversight | Group General Counsel | 2026-12-31 |
| 8 | CPA Partners inheritance and supplement (7) | CPA Partners | 164.308(a)(1)(ii)(A); 164.316(b)(2)(iii) | Moderate | Inheritance matrix; re-issued supplement | CPA Partners risk and quality partner | 2027-03-31 |
| 9 | Disposal past the retention schedule | Tax | 314.4(c)(6)(i) | Moderate | Purge about 3.1 million former clients' files | Chief Tax Officer | 2027-06-30 |

High and Moderate gaps are carried into the registers (P01) and the POA&M (P07). POAM-022 to POAM-024 trace directly to this analysis; the others came from P07 testing of the same weaknesses.

**Timing.** The filing season starts in mid-January, when phishing against tax professionals peaks (IRS Pub. 4557). Roadmap items 2, 4, and 5 are due before 2027-01-15.

## 6. Pending regulatory changes
- **FTC Safeguards Rule.** No pending proposal to amend 16 CFR Part 314 was found in the Federal Register as of 2026-09-25. The last change was the notification amendment (88 FR 77508, effective 2024-05-13).
- **IRC 7216 regulations.** No pending Treasury proposal was found; no AI-specific IRS guidance exists.
- **Regulation S-P.** The 2024 amendments are in force for Wealth (compliance date 2025-12-03 for larger entities). The SEC's 2022 proposed cybersecurity risk management rule for investment advisers (File No. S7-04-22) was **withdrawn** on 2025-06-17 (90 FR 25531), together with the 2023 predictive data analytics proposal (S7-12-23). Neither is treated as a pending obligation.
- **HIPAA Security Rule NPRM** (90 FR 898, 2025-01-06) is still **proposed**. If finalized as proposed it would remove the required and addressable distinction and require, among other things, encryption of ePHI, MFA, a written asset inventory and network map, and notice by business associates to covered entities within 24 hours of activating a contingency plan. That would affect CPA Partners' business associate duties. It is tracked only.
- **CIRCIA** (N54-R09) remains proposed (89 FR 23644); no final rule was published as of 2026-09-25. The group is above its SBA size standard, so it would likely be in the proposed scope if it falls in a critical infrastructure sector; counsel will assess when a final rule issues.

The `pending_rule_change` column records this for each row.
