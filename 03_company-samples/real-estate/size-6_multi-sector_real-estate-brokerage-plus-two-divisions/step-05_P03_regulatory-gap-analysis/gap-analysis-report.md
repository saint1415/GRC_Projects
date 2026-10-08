# Regulatory Gap Analysis: Cris Santos Company Holdings | Real Estate | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (three divisions plus corporate shared services) |
| Tier / Vertical | Multi-Sector / Real Estate and Rental and Leasing (focus division: Residential Brokerage) |
| Primary regulation | FTC Standards for Safeguarding Customer Information (Safeguards Rule), 16 CFR Part 314 (N53-R01; the same rule is N52-R03 for the Finance and Insurance division). Text read from eCFR as of 2026-09-23 (last amended 88 FR 77508, Nov. 13, 2023; 314.4(j) effective May 13, 2024 under 314.5) |
| Division regulations | Mortgage and Title: Safeguards Rule entity duties, state title trust fund law, state insurance data security laws where enacted, Reg Z AVM quality control, ECOA, RESPA, and the Bank Secrecy Act. Homebuilding: FTC Act Section 5, state breach and deposit escrow law, RESPA, and group policy (its construction-sector federal contract rules do not apply) |
| Gap tables | `gap-analysis.csv` (group Safeguards program as applied to the TMCC and the Residential Brokerage, plus brokerage-specific rules; 55 rows); `gap-analysis-mortgage-title.csv` (27 rows); `gap-analysis-homebuilding.csv` (18 rows) |
| Assessment dates | 2026-05-04 to 2026-07-24, with evidence updated from the P07 assessment (to 2026-08-28); FinCEN and HUD status rechecked 2026-10-06 |
| Assessors | Division security and compliance leads and the Title and Home Loans compliance officers, coordinated by the Group Chief Privacy Officer; reviewed by group internal audit |
| Approved | Group CISO (Qualified Individual) and Group General Counsel, 2026-09-17 |

## 1. Applicability
### 1.1 Which legal entities are "financial institutions" under the Safeguards Rule?
The rule applies to financial institutions under FTC jurisdiction whose business is engaging in an activity that is financial in nature under section 4(k) of the Bank Holding Company Act, and an institution "significantly engaged" in such activities is a financial institution (16 CFR 314.1(b), 314.2(h)(1)). The rule attaches to each **legal entity**, so each subsidiary was tested separately.

| Entity | Financial institution? | Basis |
|---|---|---|
| Cris Santos Title, LLC ("Title") | **Yes** | "An entity that provides real estate settlement services is a financial institution" (314.2(h)(2)(x), citing 12 CFR 225.28(b)(2)(viii)). Title is settlement agent in about 128,000 closings a year. The conclusion rests on settlement and disbursement work, not on the title insurance agency license |
| Cris Santos Home Loans, LLC ("Home Loans") | **Yes** | 314.1(b) names "mortgage lenders"; making loans is a financial activity under 12 CFR 225.28(b)(1). Home Loans funds about 58,000 loans a year. It is a nonbank lender, so the FTC, not a banking agency, is its Safeguards authority |
| Cris Santos Realty, LLC (brokerage) | **No, in its own right** | Real estate brokerage is not listed in 12 CFR 225.28. The nearest listed activity, acting as a finder (314.2(h)(2)(xiii)), excludes any activity that requires a real estate broker license (12 CFR 225.86(d)(1)(iii)(D)). Property management leases are operating leases, not the nonoperating leases listed in 12 CFR 225.28(b)(3). This reasoning is reused from the Small sample and still applies at this size: size does not change the activity test |
| Cris Santos Homes, Inc. (Homebuilding) | **No** | It extends no credit, and its referrals to Home Loans are incidental to home sales. Counsel concluded it is not significantly engaged in a financial activity (memo 2026-06). Revisit if Homebuilding offers its own financing |
| Cris Santos Company Holdings, Inc. (parent) | **Affiliate and service provider** | The parent employs the Qualified Individual and runs IT, security, and treasury for both institutions. The rule allows an affiliate's Qualified Individual if the institution retains responsibility, designates a senior overseer, and requires the affiliate to maintain a compliant program (314.4(a)(1)-(3)). The parent also "receives, maintains, processes, or otherwise is permitted access to customer information" for them, so it is their service provider (314.2(r); 314.4(f)) |

**Why the brokerage's systems are still in scope.** Three parts of the rule pull brokerage systems into the program even though the brokerage is not itself a financial institution:
1. "Customer information" includes records "handled or maintained by or on behalf of you or your affiliates" (314.2(d)). Title's settlement statements and wire instructions sit in the brokerage-run TMCC.
2. An "information system" includes one "connected to a system containing customer information" (314.2(j)). SYS-B1 and SYS-B2 connect directly to SYS-M2.
3. The rule applies to all customer information in the institution's possession, including information about other institutions' customers, such as lenders' borrower data in closing packages (314.1(b)).

**Decision:** the group runs **one** Safeguards program (POL-01) that serves both institutions and extends by policy to the brokerage and Homebuilding. Program-level requirements are assessed once in `gap-analysis.csv`, using the TMCC and the brokerage as the evidence base, because that is where the rule and the group's top risk meet. Duties that belong to each institution as a legal entity (the Qualified Individual arrangement, the board report, FTC notification, and their own vendors and records) are assessed in `gap-analysis-mortgage-title.csv`.

**Size exception.** 314.6 exempts institutions holding customer information on fewer than 5,000 consumers from 314.4(b)(1), (d)(2), (h), and (i). Home Loans holds about 1.3 million and Title about 2.4 million, so **the full rule applies to both**. FTC notice under 314.4(j) applies to each institution's notification events involving at least 500 consumers. Because the threshold is per institution, a mixed incident must be counted separately for Home Loans and for Title.

### 1.2 Wire fraud anchors in state law
The group's top risk is diverted closing funds (P01 GR-01). State escrow and trust fund law puts the duties squarely on the divisions. Florida is the worked example; each state of operation has its own rules, tracked by each Broker of Record and the Title compliance officer.
- **Title trust funds** "shall be used only in accordance with the terms of the individual, escrow, settlement, or closing instructions under which the funds were accepted" (Fla. Stat. 626.8473(4)).
- **Brokerage deposits** must be placed in escrow immediately, meaning by the end of the third business day (Fla. Stat. 475.25(1)(k); Fla. Admin. Code r. 61J2-14.008(3)). When a title company holds the deposit, the broker must request written verification of receipt within 10 business days (r. 61J2-14.008(2)(b)), a built-in check that catches diverted deposits.
- **Builder deposits** on Florida new homes (up to 10 percent of the price) go to escrow unless the buyer waives in writing, and withdrawals need both the builder's and the buyer's signatures (Fla. Stat. 501.1375(2)-(3)).

### 1.3 FinCEN residential real estate reporting rule (31 CFR 1031.320)
- **Status as of 2026-10-06: not in effect.** On 2026-03-19 the U.S. District Court for the Eastern District of Texas vacated the rule. FinCEN, with the Department of Justice, appealed. FinCEN's website states that while the order remains in force, reporting persons are not required to file and are not liable for failing to do so (checked 2026-10-06).
- **Who would report.** The cascade starts with the closing or settlement agent named on the settlement statement (1031.320(c)(1)(i)). If the rule is restored, it would reach **Title**, not the brokerage. Title keeps a ready procedure (watch row MT-G-026).

### 1.4 Other rules considered
| Rule | Applies? | Where handled |
|---|---|---|
| FTC Act Section 5 (N53-R02) | Yes, all divisions; no size threshold | P01, P10, Homebuilding table |
| SEC Reg S-K Item 106 and Form 8-K Item 1.05 (N53-R05) | Yes, the parent is an SEC registrant | P08, P01 GR-04 |
| State breach notification laws | Yes, in each state where affected individuals reside (Fla. Stat. 501.171 worked example) | P08; rows in all three tables |
| FCRA adverse action and disposal (15 U.S.C. 1681m(a); 16 CFR 682.3) | Yes, tenant screening and Home Loans credit reports | P10; focus and Mortgage and Title tables |
| Fair Housing Act (42 U.S.C. 3604, 3605); ECOA (12 CFR 1002.9) | Yes, brokerage, property management, and lending | P10 |
| CCPA/CPRA (N53-R03) | No: no California operations; GLBA data is exempt at the data level in any case (Cal. Civ. Code 1798.145(e)) | Reviewed yearly by the Group General Counsel |
| PCI DSS (N53-R04) | Contractual only: rent and design studio card payments use processors' hosted pages | P04; Homebuilding table |
| NYDFS Part 500 (N52-R04) | No: no New York licenses | None |
| FAR 52.204-21, DFARS 252.204-7012, CMMC (N23-R01 to N23-R04) | No: Homebuilding holds no federal contracts | Homebuilding table (recorded as not applicable) |
| CIRCIA | No: final rule not published as of 2026-09-25 | P08 watch item |

**FAR overhaul numbering.** The requirements analyzed here as FAR 52.204-21 appear as FAR 52.240-93 in awards made under an agency's FAR Part 40 class deviation. The 15 requirements are the same, so these results apply to both. See `00_company-facts.md`.

## 2. Regulation-by-division matrix
| Requirement | Residential Brokerage | Mortgage and Title | Homebuilding | Group (corporate) |
|---|---|---|---|---|
| N53-R01 / N52-R03 FTC Safeguards Rule | **Primary for this analysis.** Not a financial institution itself; its TMCC holds and connects to Title customer information, so the program applies (314.2(d), (j)) | **Applies to Home Loans and Title** as financial institutions (entity duties in their table) | Not a financial institution; program applied by group policy | Affiliate employing the Qualified Individual and service provider to both institutions (314.4(a), (f)) |
| N53-R02 FTC Act Section 5 | Applies | Applies (with Safeguards Rule) | **Applies** (buyer data, smart-home devices, marketing claims) | Applies |
| State breach notification and data security laws | Applies (client data) | Applies (each institution is a covered entity for its customers) | Applies (buyer and homeowner data) | Third-party agent duties to each division (Fla. Stat. 501.171(6) worked example) |
| State escrow and trust fund law | Broker escrow (475.25; ch. 61J2-14 worked example) | Title trust funds (626.8473 worked example) | Builder deposits (501.1375 worked example) | SYS-G5 moves all of these funds |
| N52-R07 State insurance data security laws (NAIC Model #668 where enacted) | Not applicable | **Title, where enacted** (not Florida) | Not applicable | Supports Title |
| Reg Z AVM quality control (12 CFR 1026.42(i)) | Not applicable | **Home Loans** | Not applicable | Group AI Standard (P10) |
| ECOA (Reg B) and Fair Housing Act 3605 | Fair Housing Act 3604 (sales, rentals, advertising) | **Home Loans** (credit decisions, AVM, pre-qualification) | Fair Housing Act 3604 (sales and advertising) | Group AI Standard (P10) |
| FCRA | **Tenant screening** (1681m(a); 682.3) | Credit reports (682.3) | Not applicable | None |
| RESPA affiliated business arrangements (12 CFR 1024.15) | Refers to Home Loans and Title | Receives and makes referrals | Refers to Home Loans and Title | Group General Counsel oversees |
| Bank Secrecy Act SAR (31 CFR 1029.320) | Not applicable | **Home Loans** (residential mortgage lender) | Not applicable | SOC routes fraud cases |
| FinCEN residential real estate rule (31 CFR 1031.320) | Not applicable (not in the cascade) | Title, if restored (vacated; appeal pending) | Not applicable | Tracked by the Group General Counsel |
| N53-R05 SEC Reg S-K Item 106; Form 8-K Item 1.05 | Via group | Via group | Via group | **Applies** (SEC registrant) |
| N23-R01 to N23-R04 federal contract cyber rules | Not applicable | Not applicable | Not applicable (no federal contracts) | Not applicable |
| PCI DSS (contractual) | Rent payments through processor | Not applicable | Design studio deposits through processor | None |

## 3. Method
1. **Requirements.** Each paragraph of 16 CFR 314.3, 314.4, and 314.6 became a row, split where one paragraph holds two separable duties (for example, encryption in transit and at rest in 314.4(c)(3)). Program-level rows are in the focus table; entity rows for Home Loans and Title are in their table. Reg Z, Reg B, RESPA, FCRA, and BSA rows were read from eCFR (current through 2026-09-23). State rows use Florida as the worked example (Fla. Stat. 501.171, 501.1375, and 626.8473 read from the Florida statutes site; Fla. Admin. Code ch. 61J2-14 and r. 61J2-10.032 as verified for the Small sample). State insurance rows are generic, based on NAIC Model #668, whose text varies by state.
2. **Requirement type.** The Safeguards Rule has no required or addressable split. Its elements are mandatory ("shall"), with three built-in alternatives: compensating controls for encryption approved by the Qualified Individual (314.4(c)(3)); written approval of equivalent controls instead of MFA (314.4(c)(5)); and continuous monitoring instead of annual penetration testing and semiannual vulnerability assessments (314.4(d)(2)). The group uses the first alternative for email in transit (approved in writing in 2025) and no other.
3. **Crosswalk.** Each row was mapped to CSF 2.0 and SP 800-53 Rev. 5. **This is an author mapping.** No official NIST mapping of 16 CFR 314, Reg Z, or the state rules was found.
4. **Evidence.** Interviews with each division's leadership, the Brokers of Record, and the Title and Home Loans compliance officers; document review; configuration exports; samples (40 brokerage deposits, 40 transaction files, 50 brokerage and 50 Home Loans referrals, 60 Title disbursement wires, 30 rental applications, 25 Homebuilding contracts); and P07 test results.
5. **Status.** Met, Partially met, Not met, or Not applicable. Gaps were rated with the P01 risk scale.

## 4. Results
### 4.1 Group Safeguards program, TMCC, and Residential Brokerage (`gap-analysis.csv`)
| Section | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| 314.3 Program and objectives | 1 | 1 | 0 | 0 | 2 |
| 314.4(a) Qualified Individual | 1 | 0 | 0 | 0 | 1 |
| 314.4(b) Risk assessment | 5 | 0 | 0 | 0 | 5 |
| 314.4(c) Safeguards | 4 | 7 | 1 | 0 | 12 |
| 314.4(d) Testing and monitoring | 3 | 0 | 0 | 0 | 3 |
| 314.4(e) Personnel and training | 3 | 1 | 0 | 0 | 4 |
| 314.4(f) Service providers | 1 | 2 | 0 | 0 | 3 |
| 314.4(g) Evaluate and adjust | 1 | 0 | 0 | 0 | 1 |
| 314.4(h) Incident response plan | 5 | 3 | 0 | 0 | 8 |
| 314.6 Exception | 0 | 0 | 0 | 1 | 1 |
| **Safeguards Rule subtotal** | **24** | **14** | **1** | **1** | **40** |
| State broker escrow rules (Florida worked example) | 5 | 3 | 0 | 0 | 8 |
| State breach and disposal law (Fla. Stat. 501.171 worked example) | 0 | 2 | 1 | 0 | 3 |
| FCRA (adverse action; disposal rule) | 0 | 2 | 0 | 0 | 2 |
| RESPA 12 CFR 1024.15(b)(1) | 0 | 1 | 0 | 0 | 1 |
| FinCEN 31 CFR 1031.320 | 0 | 0 | 0 | 1 | 1 |
| **Total** | **29** | **22** | **2** | **2** | **55** |

Of the 24 rows with gaps, 4 are rated High, 15 Moderate, and 5 Low. The program is defined and mostly operating: risk assessment, testing, change management, and secure development are all met. The **High** gaps are the ones that let business email compromise succeed: the program is not yet designed evenly against the main threat (G-002, 314.3(b)), about 9,900 contractor agents still have no MFA (G-016, 314.4(c)(5); and the matching state duty, G-049), and payee or document tampering in SYS-B1 and SYS-M2 goes unlogged (G-020, 314.4(c)(8)). The two **Not met** rows are both about disposal: nothing is disposed of, in SYS-B1 or elsewhere (G-017, 314.4(c)(6)(i); G-051, Fla. Stat. 501.171(8)).

### 4.2 Mortgage and Title (`gap-analysis-mortgage-title.csv`)
| Regulation | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| Safeguards Rule entity duties (Home Loans and Title) | 4 | 6 | 2 | 0 | 12 |
| Title trust funds (Fla. Stat. 626.8473 worked example) | 2 | 1 | 0 | 0 | 3 |
| State insurance data security laws (Model #668 where enacted) | 0 | 2 | 0 | 0 | 2 |
| Reg Z AVM quality control (12 CFR 1026.42(i)) | 2 | 1 | 2 | 0 | 5 |
| ECOA Reg B; RESPA; BSA SAR; FCRA disposal | 0 | 4 | 0 | 0 | 4 |
| FinCEN 31 CFR 1031.320 | 0 | 0 | 0 | 1 | 1 |
| **Total** | **8** | **14** | **4** | **1** | **27** |

Of the 18 rows with gaps, 3 are High, 11 Moderate, and 4 Low.

**Not met:**
- **314.4(a)(3)** (MT-G-004): the parent employs the Qualified Individual and runs both institutions' IT and security, but the 2021 intercompany services agreement does not require it to maintain a compliant program.
- **314.4(c)(6)(i)** (MT-G-011): Title's scanned closing files from 2006 to 2015 and Home Loans' withdrawn applications since 2019 are kept with no documented reason.
- **12 CFR 1026.42(i)(3)(iv) and (v)** (MT-G-021, MT-G-022): the AVM quality control policy adopted in 2025 requires random sample testing and nondiscrimination review, and neither has been done (scenario gap 6). The AVM rule took effect on 2025-10-01 (89 FR 64538). It applies to Home Loans because it is a mortgage originator and not a financial institution as defined in 12 U.S.C. 3350(7) (1026.42(i)(1)).

**Title's wire controls are strong but not perfect.** In 60 sampled disbursement wires, 59 had a callback record. One payoff was paid on an emailed payoff letter without lender portal verification (MT-G-014, High, because a single miss can mean a six-figure loss of trust funds).

### 4.3 Homebuilding (`gap-analysis-homebuilding.csv`)
| Obligation group | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| Federal contract cyber rules (N23-R01 to N23-R04) and the Safeguards Rule | 0 | 0 | 0 | 5 | 5 |
| FTC Act Section 5 (data, devices, claims) | 0 | 2 | 1 | 0 | 3 |
| State breach and disposal law (Fla. Stat. 501.171 worked example) | 0 | 3 | 0 | 0 | 3 |
| Builder deposit escrow (Fla. Stat. 501.1375 worked example) | 2 | 0 | 0 | 0 | 2 |
| RESPA; PCI DSS (contractual) | 1 | 1 | 0 | 0 | 2 |
| Group policy (supplement, inheritance, payee verification) | 0 | 0 | 3 | 0 | 3 |
| **Total** | **3** | **6** | **4** | **5** | **18** |

Of the 10 rows with gaps, 2 are High, 7 Moderate, and 1 Low. Homebuilding's construction-sector primary regulation (FAR 52.204-21 and CMMC) does not apply because it has no federal contracts, so its binding duties are general consumer protection law. **Not met:** smart-home device security (HB-G-007, scenario gap 8), and three group policy requirements it has never implemented: a division supplement, documented inheritance (gap 5), and payee verification for trade partner bank changes (HB-G-018, gap 2).

## 5. Group roadmap
| # | Gap (scenario gap) | Divisions | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|---|---|
| 1 | Contractor agents without MFA (1) | Brokerage; group | 314.4(c)(5); Fla. Stat. 501.171(2) | High | Enforce MFA; disable non-compliant accounts (POAM-001) | Group identity director | 2026-12-31 |
| 2 | Payee verification uneven (2) | All | 314.3(b); Fla. Stat. 626.8473(4); POL-01 4.9 | High | Every payment type through SYS-G5 payee verification; lender portal payoff checks (POAM-003) | Group Treasurer | 2027-01-31 |
| 3 | Application logs and payee changes unmonitored (3) | Brokerage; Title; Homebuilding | 314.4(c)(8) | High | SIEM onboarding and alerts (POAM-004) | Group SOC director | 2027-01-31 |
| 4 | AVM quality control and model disparities (6) | Mortgage and Title; Brokerage | 1026.42(i)(3)(iv)-(v); 1681m(a) | High | AVM sample testing and nondiscrimination review; tenant screening notices and testing (POAM-019, POAM-020) | President, Mortgage; president of property management | 2027-01-31 |
| 5 | Smart-home access (8) | Homebuilding | 15 U.S.C. 45(a) | High | Remove builder roles; unique passcodes (POAM-016) | Homebuilding chief operating officer | 2026-12-31 |
| 6 | Notification matrix not exercised (7) | All | 314.4(h)(3)-(4), (h)(6), (j); Model #668 sec. 6; Form 8-K Item 1.05 | Moderate | Per-institution counting; commissioner rows; tabletop (POAM-007) | Group General Counsel | 2026-12-15 |
| 7 | Affiliate oversight of the parent | Mortgage and Title | 314.4(a)(2)-(3); 314.4(f)(2)-(3) | Moderate | Amend the intercompany agreement; oversight minutes (POAM-013) | Group General Counsel | 2026-12-31 |
| 8 | Affiliate data flows and referral disclosures (4) | All | 314.4(c)(1)(ii), (c)(2); 12 CFR 1024.15(b)(1) | Moderate | Data sharing register; required disclosure and consent flags on lead APIs (POAM-006) | Group Chief Privacy Officer | 2027-03-31 |
| 9 | Homebuilding outside common controls (5) | Homebuilding | POL-01 4.5, 4.6; 15 U.S.C. 45(a) | Moderate | Supplement, inheritance matrix, legacy tenant migration (POAM-014, POAM-015) | Homebuilding security and compliance lead | 2027-03-31 |
| 10 | Retention and disposal (9) | All | 314.4(c)(6); Fla. Stat. 501.171(8); 16 CFR 682.3 | Moderate | Group retention schedule and purge (POAM-010) | Group Chief Privacy Officer | 2027-06-30 |
| 11 | SAR routing for loan-related fraud | Mortgage and Title | 31 CFR 1029.320 | Moderate | Route cases to the BSA officer (POAM-021) | President, Mortgage | 2026-12-31 |
| 12 | Deposit verification skipped | Brokerage | r. 61J2-14.008(2)(b) | Moderate | Blocking task and automatic Title receipt confirmation (POAM-022) | Florida Broker of Record | 2027-01-31 |

High and Moderate gaps are carried into the registers (P01) and the POA&M (P07). POAM-013, POAM-015, and POAM-019 to POAM-022 trace directly to this analysis.

## 6. Pending regulatory changes
- **Safeguards Rule.** No proposed amendment to 16 CFR Part 314 was found in the Federal Register through 2026-10-06. The last change was the notification amendment (88 FR 77499, Nov. 13, 2023).
- **FinCEN residential real estate rule.** Vacated, with the government's appeal pending (section 1.3). If the vacatur is reversed, Title would need a reporting procedure for non-financed transfers to entities and trusts.
- **HUD disparate impact rule.** HUD proposed on 2026-01-14 (91 FR 1475) and in a supplemental proposal on 2026-08-10 (91 FR 51416), with comments closing 2026-10-09, to change its discriminatory effects regulation (24 CFR 100.500). Both are still proposals as of 2026-10-06. This affects P10 (tenant screening, AVM, and pre-qualification), not the Safeguards Rule, and does not change the Fair Housing Act itself.
- **CIRCIA** reporting is not in effect (final rule not published as of 2026-09-25). None of these is treated as a current obligation.
