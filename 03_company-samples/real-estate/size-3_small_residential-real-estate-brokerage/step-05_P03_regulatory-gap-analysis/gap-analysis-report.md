# Regulatory Gap Analysis: Cris Santos Company | Real Estate and Rental and Leasing | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (residential real estate brokerage with property management and an in-house Closing Services division) |
| Tier / Vertical | Small / Real Estate and Rental and Leasing |
| Primary regulation | FTC Standards for Safeguarding Customer Information (Safeguards Rule), 16 CFR Part 314 (N53-R01). Text read from eCFR as of 2026-09-23 (last amended 88 FR 77508, Nov. 13, 2023; 314.4(j) effective May 13, 2024 under 314.5) |
| Secondary rules | Florida escrow duties that anchor the wire fraud controls: Fla. Stat. 475.25(1)(d)1. and (1)(k) with Fla. Admin. Code ch. 61J2-14 (broker deposits), and Fla. Stat. 626.8473 (title agency trust funds) |
| Assessment dates | 2026-08-03 to 2026-08-14; evidence refreshed with P07 results through 2026-08-28; FinCEN and HUD status rechecked 2026-09-26 |
| Assessor | IT Manager (Qualified Individual) with the Controller and the Closing Services Manager |
| Approved | COO, 2026-09-21 |

## 1. Applicability
### 1.1 Is the company a "financial institution" under the Safeguards Rule?
The rule applies to financial institutions under FTC jurisdiction: entities whose business is engaging in an activity that is financial in nature under section 4(k) of the Bank Holding Company Act, including the activities the Federal Reserve lists in 12 CFR 225.28 and 225.86 (314.1(b), 314.2(h)(1)). An entity must be **significantly engaged** in the activity (314.2(h)(1), (h)(3)(iv)). Each business line was tested separately:

| Business line | Financial activity? | Basis |
|---|---|---|
| Residential sales brokerage | **No** | Real estate brokerage is not listed in 12 CFR 225.28. The nearest listed activity, acting as a **finder** (314.2(h)(2)(xiii); 12 CFR 225.86(d)(1)), expressly excludes it: a finder "may not engage in any activity that would require the company to register or obtain a license as a real estate agent or broker under applicable law" (12 CFR 225.86(d)(1)(iii)(D)). Holding earnest money in the broker's escrow account was not treated as a separate financial activity |
| Property management and leasing | **No** | Leasing real property is financial only on a **nonoperating** basis (12 CFR 225.28(b)(3)(i)). The company manages, maintains, and repairs the homes it leases, which is an operating basis |
| Closing Services division | **Yes** | "An entity that provides real estate settlement services is a financial institution" (314.2(h)(2)(x), citing 12 CFR 225.28(b)(2)(viii)). The division acts as settlement agent in about 620 closings a year, prepares settlement statements, and disburses funds from its trust account. Footnote 5 to 225.28(b)(2)(viii) excludes "providing title insurance as principal, agent, or broker" from settlement services, so the conclusion rests on the settlement and disbursement work, not on the title insurance agency license |
| Mortgage referrals | **No** | The company does not take loan applications or arrange loans (it would otherwise be a mortgage broker under 314.2(h)(2)(xi)). Agents give buyers a list of unaffiliated lenders |

**Significantly engaged.** The Closing Services division is a separately staffed, regular line of business (7 staff, about 17% of receipts), not an occasional accommodation. The company is therefore a financial institution. The rule attaches to the **legal entity**, Cris Santos Company, LLC.

**Which information is covered.** "Customer information" is nonpublic personal information about a customer (314.2(d)). A consumer who "obtains real estate settlement services from you" has a customer relationship (314.2(e)(2)(i)(K)). The rule covers all customer information in the company's possession, including information about other financial institutions' customers, such as lenders' borrower data in closing packages (314.1(b)). Brokerage-only client data and tenant data are not customer information in the rule's sense. **Decision:** the company applies the program to every system in the TMCC boundary (P02), because the same email, transaction platform, and devices carry both kinds of data, and the rule's definition of an information system includes systems "connected to" one that contains customer information (314.2(j)). Tenant screening data is protected under the same program as a business choice and under the FCRA disposal rule (16 CFR 682.3).

**Size exception.** 314.6 exempts institutions that maintain customer information on fewer than 5,000 consumers from 314.4(b)(1), (d)(2), (h), and (i). Closing Services holds customer information on about 7,900 consumers, so **the full rule applies**. FTC notice under 314.4(j) applies only to notification events involving at least 500 consumers.

**Had the answer been no.** If the company had no settlement activity, the Safeguards Rule would not apply and this analysis would have used NIST CSF 2.0 as a voluntary benchmark, with FTC Act Section 5 (N53-R02) as the binding security standard. Section 5 applies anyway and is handled in P01 and P10.

### 1.2 Secondary rules: the wire fraud anchor
The company's highest risks are diverted closing funds (P01 R-001, R-002). Florida law puts the escrow duties squarely on the company:
- **Broker deposits.** A broker must "immediately place, upon receipt" entrusted deposits in escrow with a Florida title company or depository, where "the funds shall be kept until disbursement thereof is properly authorized" (Fla. Stat. 475.25(1)(k)). "Immediately" means by the end of the third business day (r. 61J2-14.008(3)). Sales associates must deliver deposits to the broker by the end of the next business day (r. 61J2-14.009). The broker must reconcile monthly and explain differences (r. 61J2-14.012). If there are conflicting demands for escrowed property, the broker must promptly notify the Florida Real Estate Commission and use one of the listed settlement procedures (475.25(1)(d)1.).
- **Deposit verification.** When a title company or attorney holds the deposit, the buyer's broker must request written verification of receipt within 10 business days (r. 61J2-14.008(2)(b)). This is a built-in fraud detection step: a diverted deposit shows up as an unverified deposit.
- **Closing funds.** Funds the title agency receives are trust funds that "shall be used only in accordance with the terms of the individual, escrow, settlement, or closing instructions under which the funds were accepted" (Fla. Stat. 626.8473(4)).

Rule 61J2-14 text was read from the Legal Information Institute's reproduction of the Florida Administrative Code, because the official site (flrules.org) returned a browser challenge to this environment. Rule history shows the last amendments in 2004 to 2010.

### 1.3 FinCEN residential real estate reporting rule (31 CFR 1031.320)
- **Status as of 2026-09-26: not in effect.** FinCEN issued the rule in August 2024 (89 FR 70258) with an effective date of December 1, 2025. On September 30, 2025 FinCEN postponed reporting to March 1, 2026 by exemptive order. On March 19, 2026 the U.S. District Court for the Eastern District of Texas vacated the rule (*Flowers Title Companies, LLC v. Bessent*). FinCEN states that reporting persons are not required to file and are not liable while the order remains in force. FinCEN, through the Department of Justice, appealed to the Fifth Circuit (filed May 11, 2026, per secondary sources). The text remains in eCFR.
- **Who would report.** The reporting person is determined by a cascade that starts with "the person listed as the closing or settlement agent on the closing or settlement statement" (1031.320(c)(1)(i)). An employee's duty is deemed the employer's (1031.320(c)(2)).
- **Does it reach a brokerage?** Not as a brokerage. Real estate agents and brokers are not in the cascade. It would reach **this company through its Closing Services division** when the division is the settlement agent on a non-financed transfer to an entity or trust. The division should keep a ready procedure in case the appeal restores the rule. Geographic Targeting Orders apply to title insurance companies; the last one found ran from 2025-10-10 to 2026-02-28, and whether a later order issued was not confirmed.

### 1.4 Other rules considered
| Rule | Applies? | Where handled |
|---|---|---|
| FTC Act Section 5 (N53-R02) | Yes, no size threshold | P01, P10 |
| Fla. Stat. 501.171 (breach notice) | Yes | P08 |
| FCRA adverse action and disposal (15 U.S.C. 1681m(a); 16 CFR 682.3) | Yes, for tenant screening | P10, POL-04 |
| Fair Housing Act (42 U.S.C. 3604) | Yes | P10 |
| CCPA/CPRA (N53-R03) | No: no California business; receipts below $26,625,000 | None |
| PCI DSS (N53-R04) | Contractual only; the hosted payment page keeps card data out of company systems | Noted in P04 |
| SEC disclosure (N53-R05) | No: privately held | None |

## 2. Method
1. **Requirements.** Each paragraph of 16 CFR 314.3, 314.4, and 314.6 became a row, split where one paragraph holds two separable duties (for example, encryption in transit and at rest in 314.4(c)(3)). The Florida rows cover the escrow provisions that bear on how funds are received, held, verified, and disbursed; the non-cyber parts of ch. 61J2-14 (such as interest-bearing account rules) were left out. One FinCEN row records the applicability decision.
2. **Requirement type.** The Safeguards Rule has no required/addressable split. Its elements are mandatory ("shall"), with three built-in alternatives: compensating controls for encryption approved by the Qualified Individual (314.4(c)(3)), written approval of equivalent controls instead of MFA (314.4(c)(5)), and continuous monitoring instead of annual penetration testing and semiannual vulnerability assessments (314.4(d)(2)). No alternative has been approved today.
3. **Crosswalk.** Each row was mapped to CSF 2.0 and SP 800-53 Rev. 5. **This is an author mapping.** No official NIST mapping of 16 CFR 314 or of the Florida rules was found.
4. **Evidence.** Interviews (majority owner and Broker of Record, COO, IT Manager, Controller, Closing Services Manager, Transaction Coordination Manager, Director of Property Management, both Sales Managers), document review, configuration exports, samples (25 sales escrow deposits, 20 transaction files for deposit verification, 30 disbursement wires, 12 departing contractors), 12 months of escrow reconciliations, and walkthroughs of both offices on 2026-08-06.
5. **Status.** Each row was rated Met, Partially met, Not met, or Not applicable. Gaps were rated with the P01 risk scale.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| 314.3 Program and objectives | 0 | 2 | 0 | 0 | 2 |
| 314.4(a) Qualified Individual | 0 | 1 | 0 | 1 | 2 |
| 314.4(b) Risk assessment | 3 | 2 | 0 | 0 | 5 |
| 314.4(c) Safeguards | 0 | 5 | 7 | 0 | 12 |
| 314.4(d) Testing and monitoring | 0 | 1 | 2 | 0 | 3 |
| 314.4(e) Personnel and training | 0 | 3 | 1 | 0 | 4 |
| 314.4(f) Service providers | 0 | 2 | 1 | 0 | 3 |
| 314.4(g) Evaluate and adjust | 0 | 1 | 0 | 0 | 1 |
| 314.4(h) Incident response plan | 3 | 5 | 0 | 0 | 8 |
| 314.4(i) Annual report | 0 | 0 | 3 | 0 | 3 |
| 314.4(j) FTC notification | 0 | 3 | 0 | 0 | 3 |
| 314.6 Exception | 0 | 0 | 0 | 1 | 1 |
| **Safeguards Rule subtotal** | **6** | **25** | **14** | **2** | **47** |
| Florida broker escrow (475.25; ch. 61J2-14) | 3 | 5 | 0 | 0 | 8 |
| Florida title agency trust funds (626.8473) | 2 | 1 | 0 | 0 | 3 |
| FinCEN 31 CFR 1031.320 | 0 | 0 | 0 | 1 | 1 |
| **Total** | **11** | **31** | **14** | **3** | **59** |

Of the 45 rows with gaps, 5 are rated High, 26 Moderate, and 14 Low.

## 4. Priority gaps and roadmap
| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Disbursements can follow spoofed payoff letters or changed instructions (11 of 30 sampled wires had no verification record) | 626.8473(4) | High | Written disbursement verification procedure with independent callback | Closing Services Manager | 2026-10-31 |
| Contractor agents (about 70% of users) have no MFA; legacy protocols on | 314.4(c)(5) | High | MFA for all accounts; block legacy protocols | IT Manager | 2026-11-30 |
| Deposit wire instructions sent to buyers by ordinary email | r. 61J2-14.009; 475.25(1)(k) | High | Instructions only from the portal, with a callback script | Controller | 2026-11-30 |
| No monitoring of user activity; five external forwarding rules found | 314.4(c)(8) | High | MSP alerting and weekly review | IT Manager | 2026-12-31 |
| Program not yet designed around the main threat | 314.3(b) | High | Complete the two High treatments above | IT Manager | 2026-11-30 |
| Single approver on sales and property management escrow wires | r. 61J2-14.010(1) | Moderate | Dual approval (bank setting) | Controller | 2026-10-15 |
| No penetration test or vulnerability assessment | 314.4(d)(2) | Moderate | Pen test by 2026-11-15; monthly scans | IT Manager | 2026-11-30 |
| No secure development or testing for the Closing Communications Portal | 314.4(c)(4) | Moderate | Standard in the developer contract; pen test | IT Manager | 2026-12-31 |
| No annual report to the majority owner | 314.4(i) | Moderate | First written report | IT Manager | 2026-12-15 |
| Service providers unmanaged | 314.4(f) | Moderate | Inventory, contract terms, annual reviews | COO | 2027-03-31 |
| No retention or disposal schedule | 314.4(c)(6) | Moderate | Retention schedule and annual purge | Controller | 2027-03-31 |

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07).

## 5. Pending changes to watch
- **Safeguards Rule.** No proposed amendment to 16 CFR Part 314 was found in a Federal Register search from 2023-01-01 to 2026-09-26. The last change was the notification amendment (88 FR 77499, Nov. 13, 2023).
- **FinCEN residential real estate rule.** Vacated, with the government's appeal pending (section 1.3). If the vacatur is reversed, the Closing Services division would need a reporting procedure for non-financed transfers to entities and trusts. The FinCEN row carries a watch note.
- **HUD disparate impact rule.** HUD proposed on 2026-01-14 (91 FR 1475) and in a supplemental proposal on 2026-08-10 (91 FR 51416) to remove its discriminatory effects regulation (24 CFR 100.500) and leave the question to the courts. The regulation is still in eCFR as of 2026-09-23. This affects P10, not the Safeguards Rule.
