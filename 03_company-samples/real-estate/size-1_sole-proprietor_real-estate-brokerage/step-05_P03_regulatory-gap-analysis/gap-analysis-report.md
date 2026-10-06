# Regulatory Gap Analysis: Cris Santos Company | Real Estate and Rental and Leasing | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (residential real estate brokerage) |
| Tier / Vertical | Sole Proprietorship / Real Estate and Rental and Leasing |
| Regulations analyzed (binding) | **Florida broker escrow duties**, Fla. Stat. 475.25(1)(d)1. and (1)(k), Fla. Admin. Code ch. 61J2-14 and r. 61J2-10.032, and record retention in Fla. Stat. 475.5015; **Fla. Stat. 501.171** (reasonable measures, breach notice, disposal). Statute text read from the 2026 Florida Statutes on 2026-10-06; rule text from the Legal Information Institute's reproduction of the Florida Administrative Code |
| Also binding | FTC Act Section 5, 15 U.S.C. 45(a) (N53-R02); FCRA adverse action, 15 U.S.C. 1681m(a), and the disposal rule, 16 CFR 682.3 (tenant screening) |
| Yardstick | **16 CFR 314.3-314.4** (FTC Safeguards Rule elements, N53-R01), used as a **benchmark only** to judge "reasonable measures" under 501.171(2). Text read from eCFR (point in time 2026-09-23) |
| Regulation named in the scenario brief | FTC Safeguards Rule. **Does not apply**: the brokerage is not a financial institution (section 1.1) |
| Assessment dates | 2026-08-17 to 2026-08-21 (self-assessment); FinCEN status rechecked 2026-10-06 |
| Assessor | Broker-owner, with the on-call IT technician (confidentiality agreement since 2026-08-14). Evidence is self-attested, checked on screen where possible |
| Adopted | 2026-09-15 |

## 1. Applicability
### 1.1 Is a one-broker residential brokerage a "financial institution" under the Safeguards Rule?
The rule covers financial institutions under FTC jurisdiction, meaning businesses "significantly engaged" in an activity that is financial in nature under section 4(k) of the Bank Holding Company Act (16 CFR 314.1(b), 314.2(h)(1)). Each activity was tested:

| Activity | Financial activity? | Basis |
|---|---|---|
| Buyer and seller representation | **No** | Not listed in 12 CFR 225.28. The nearest example, a **finder** that brings buyers and sellers together (314.2(h)(2)(xiii)), is defined in 12 CFR 225.86(d)(1), and a finder "may not engage in any activity that would require the company to register or obtain a license as a real estate agent or broker under applicable law" (225.86(d)(1)(iii)(D)). Everything the owner does for buyers and sellers requires the broker license |
| Tenant placement | **No** | Finding tenants and negotiating leases for landlords is brokerage. The owner leases nothing as principal, so the nonoperating leasing activity does not arise |
| Holding deposits in the sales escrow account | **No (author's analysis)** | 314.2(h)(2)(vi) treats a business that "regularly wires money to and from consumers" as a financial institution. The owner's escrow handling is a duty of the broker license (Fla. Stat. 475.25(1)(k)), not a service sold to consumers, and amounts to about 16 outgoing payments a year, mostly to title companies and landlords. The owner is not "significantly engaged" in transferring money. Counsel is asked to confirm this in the annual review |
| Settlement or closing services | **No** | Title companies and closing attorneys close every sale. If the owner ever acted as closing agent, 314.2(h)(2)(x) would make the business a financial institution, as in the Small sample in this vertical |
| Mortgage brokering | **No** | The owner takes no loan applications and gives buyers a list of unaffiliated lenders |

**Result: the Safeguards Rule does not apply.** Its elements are still the clearest federal description of a reasonable security program for a business that handles financial details, so they are used as the yardstick for Florida's "reasonable measures" duty (rows G-020 to G-044). Had the rule applied, the 314.6 exception (fewer than 5,000 consumers) would have removed four of its elements; the owner keeps a written risk assessment and incident plan anyway.

### 1.2 What does bind the owner
- **Florida broker escrow duties (primary).** These anchor the highest risks in P01. A broker must "immediately place, upon receipt" entrusted funds in a Florida escrow account, "wherein the funds shall be kept until disbursement thereof is properly authorized" (475.25(1)(k)); "immediately" means by the end of the third business day (r. 61J2-14.008(3)). The broker must be a signatory (r. 61J2-14.010(1)), keep records (r. 61J2-14.012(1)), and reconcile monthly (r. 61J2-14.012(2)-(3)). When a title company or attorney holds the deposit, the broker must request written verification within 10 business days (r. 61J2-14.008(2)(b)). Conflicting demands require Commission notice within 15 business days (r. 61J2-10.032(1)). Brokerage records are kept at least 5 years (475.5015).
- **Fla. Stat. 501.171 (primary).** A "covered entity" includes "a sole proprietorship ... that acquires, maintains, stores, or uses personal information" (501.171(1)(b)), with no size threshold. Client files hold names with driver license numbers, and screening reports hold Social Security numbers. A bank account number alone is personal information only "in combination with any required security code, access code, or password" (501.171(1)(g)1.a.(III)), so most wire instructions are not personal information under 501.171. They are still the most valuable data the business holds, which is why the escrow rows matter more. Encrypted information is excluded (501.171(1)(g)2.). The brokerage has no federal functional regulator, so the deemed-compliance path in 501.171(4)(g) is not available.
- **FTC Act Section 5 (N53-R02).** No size threshold; reaches inaccurate security statements (G-017).
- **FCRA.** Tenant screening makes the owner a user of consumer reports: adverse action notices (15 U.S.C. 1681m(a)) and disposal (16 CFR 682.3).
- **Other states' breach laws** apply after a breach to affected people who live elsewhere (about 30% of buyers). Florida is the worked example in P08.

### 1.3 Considered and not applicable
| Requirement | Decision |
|---|---|
| FinCEN residential real estate rule, 31 CFR 1031.320 | Vacated by the U.S. District Court for the Eastern District of Texas on 2026-03-19; FinCEN and the Department of Justice have appealed, and FinCEN states that no reports are required while the order stands (checked 2026-10-06). Brokers are not in its reporting cascade, which starts with the closing or settlement agent (G-045) |
| CCPA/CPRA (N53-R03) | No California business; receipts far below $26,625,000 |
| PCI DSS (N53-R04) | No payment cards accepted; applicants pay screening fees to the screening service directly |
| SEC disclosure (N53-R05) | Not a public company |
| Fair Housing Act, 42 U.S.C. 3604 | Applies to tenant screening and advertising; handled in P10, not as gap rows |

**Excluded rows, with reasons (6):** G-005 (fewer than 1,000 individuals in all records), G-035 (pen testing and scanning: benchmark row, no owner-run internet-facing systems), G-042 (no board), G-043 (FTC notice: not a financial institution), G-044 (314.6 recorded for reference), and G-045 (FinCEN rule vacated).

## 2. Method
1. **Requirements.** 501.171 was decomposed by subsection. The Florida escrow rows cover the provisions that bear on how funds are received, held, verified, and disbursed; non-cyber parts of ch. 61J2-14 (such as interest-bearing accounts) were left out. Each paragraph of 16 CFR 314.3(a), 314.4, and 314.6 became one benchmark row, using the rule's own numbering, with closely linked paragraphs combined where a one-person business answers them together (for example 314.4(e)(2)-(4)). **45 rows in total.**
2. **Requirement type.** Florida and federal duties are "shall" duties. The 16 CFR 314 rows are labeled "Benchmark (not binding)".
3. **Crosswalk.** CSF 2.0 and SP 800-53 columns are an **author mapping**; no official NIST mapping of these sources exists.
4. **Evidence.** Self-attested by the owner and checked on screen with the IT technician: account security pages and sign-in tests (2026-08-20), the escrow ledger and 12 months of reconciliations, a sample of 10 buyer files for deposit verification, 8 outgoing escrow payments, the contracts folder, the website, and a home office walkthrough (2026-08-19).
5. **Status.** Met, Partially met, Not met, or Not applicable as of the end of fieldwork (2026-08-21). Fixes since (POL-01 adopted 2026-09-15) appear in the remediation columns, not as a changed status. Gap risk uses the P01 scale.

## 3. Results summary
| Source | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| Fla. Stat. 501.171 | 0 | 3 | 3 | 1 | 7 |
| Florida broker escrow (475.25; ch. 61J2-14; r. 61J2-10.032) | 5 | 2 | 1 | 0 | 8 |
| Florida brokerage records (475.5015) | 1 | 0 | 0 | 0 | 1 |
| FTC Act Section 5 | 0 | 0 | 1 | 0 | 1 |
| FCRA (1681m(a); 16 CFR 682.3) | 0 | 1 | 1 | 0 | 2 |
| 16 CFR 314 benchmark | 1 | 12 | 8 | 4 | 25 |
| FinCEN 31 CFR 1031.320 | 0 | 0 | 0 | 1 | 1 |
| **Total** | **7** | **18** | **14** | **6** | **45** |

Of the 32 rows with gaps, 5 are rated **High**, 15 **Moderate**, and 12 **Low**.

**The main finding.** The escrow account itself is in good order: deposits are placed on time, the broker is the signatory, and reconciliations are signed every month (5 of 8 escrow rows Met). What is missing is the step **before** money moves. The owner pays out escrowed funds on emailed instructions with no callback (G-015, High), and the mailbox those instructions arrive in is shared with the coordinator under one password and a forwarded text code (G-024, G-029), with no alerting (G-033). A taken-over mailbox would therefore defeat the escrow rules that otherwise work.

## 4. Action list (half page)
In order. The first five cost nothing.

| # | Action | Rows | Gap risk | Target |
|---|---|---|---|---|
| 1 | Callback rule before every outgoing escrow payment, recorded on the ledger | G-015 | High | 2026-09-15 (done) |
| 2 | Separate coordinator login; security key or authenticator app on email, platform, and banking; password manager | G-024, G-029, G-025 | High | 2026-09-30 |
| 3 | Adopt POL-01 (written program, designation, retention schedule, rules of use) | G-001, G-020, G-021, G-026 | High | 2026-09-15 (done) |
| 4 | Replace the "bank-level security" website statement with an accurate one | G-017 | Moderate | 2026-09-30 |
| 5 | Block external auto-forwarding; alerts for new rules and unusual sign-ins; weekly review | G-033 | High | 2026-10-31 |
| 6 | Adopt the P08 runbook, confirm the bank fraud desk and counsel contacts, add the escrow dispute step | G-003, G-004, G-014, G-041 | Moderate | 2026-10-31 |
| 7 | Written terms with the coordinator and bookkeeper (safeguards, 10-day breach notice, return of data) | G-006, G-038 | Moderate | 2026-10-31 |
| 8 | Secure document sharing for identity documents and wire instructions; deposit verification sent to independently found addresses | G-027, G-010 | Moderate | 2026-10-31 |
| 9 | Adverse action notice for every decline and conditional approval | G-018 | Moderate | 2026-11-30 |
| 10 | Retention schedule and first purge; delete extra screening reports and identity copies | G-007, G-019, G-030 | Moderate | 2026-12-31 |

High and Moderate gaps are in the risk register (P01) and the POA&M (P07).

## 5. Pending changes to watch
- **FinCEN residential real estate rule.** Vacated, appeal pending (section 1.3). It would matter to this business only if the owner began acting as closing agent.
- **16 CFR Part 314.** No Federal Register document affecting Part 314 has been published since 2024-01-01 (search on 2026-10-06). Its status here changes only if the owner's activities change (section 1.1).
- **HUD disparate impact rule (24 CFR 100.500).** Proposed for removal (91 FR 1475, 2026-01-14; supplemental proposal 91 FR 51416, 2026-08-10); no final rule as of 2026-10-06. Affects P10, not these rows.
- **Fla. Stat. 501.171.** The 2026 text lists biometric data and geolocation as personal information; recheck the definitions each year.
