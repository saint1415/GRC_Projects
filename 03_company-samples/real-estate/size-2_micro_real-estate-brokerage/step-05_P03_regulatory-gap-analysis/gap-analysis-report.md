# Regulatory Gap Analysis: Cris Santos Company | Real Estate and Rental and Leasing | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (residential real estate brokerage with property management) |
| Tier / Vertical | Micro / Real Estate and Rental and Leasing |
| Regulation analyzed | FTC Standards for Safeguarding Customer Information (Safeguards Rule), 16 CFR Part 314 (N53-R01), **as a benchmark**: it does not bind this brokerage (section 1.1). Text read from eCFR as of 2026-09-23 |
| Binding rules analyzed | Fla. Stat. 501.171; Florida broker escrow and records (Fla. Stat. 475.25(1)(d)1. and (1)(k), 475.5015; Fla. Admin. Code ch. 61J2-14 and r. 61J2-10.032); FCRA (15 U.S.C. 1681m(a); 16 CFR 682.3); FTC Act Section 5 (N53-R02) |
| Assessment dates | 2026-07-27 to 2026-08-07; FinCEN and HUD status rechecked 2026-10-06 |
| Assessor | Office Manager (security and compliance lead) with the MSP lead technician |
| Approved | Broker-owner, 2026-09-14 |

## 1. Applicability
### 1.1 Is the brokerage a "financial institution" under the Safeguards Rule?
The rule applies to financial institutions under FTC jurisdiction: entities whose business is engaging in an activity that is financial in nature under section 4(k) of the Bank Holding Company Act, and that are **significantly engaged** in it (16 CFR 314.1(b); 314.2(h)(1), (h)(3)(iv)). Each activity was tested:

| Activity | Financial activity? | Basis |
|---|---|---|
| Residential sales brokerage | **No** | Brokerage is not listed in 12 CFR 225.28. The nearest listed activity, acting as a **finder** (314.2(h)(2)(xiii); 12 CFR 225.86(d)(1)), excludes it: a finder "may not engage in any activity that would require the company to register or obtain a license as a real estate agent or broker under applicable law" (12 CFR 225.86(d)(1)(iii)(D)) |
| Property management and leasing | **No** | Leasing real property is a listed financial activity only on a nonoperating basis (12 CFR 225.28(b)(3)). The brokerage manages and maintains the homes for their owners, which is an operating arrangement |
| Holding and moving escrow funds | **No (judgment)** | The rule's example of "a business that regularly wires money to and from consumers" (314.2(h)(2)(vi)) was considered. The brokerage's escrow deposits and transfers happen only because Florida license law requires a broker to hold entrusted funds (Fla. Stat. 475.25(1)(k)); they are part of the brokerage and management services, not a money transfer service offered to the public. No FTC statement on broker trust accounts was found, so this is recorded as a reasoned judgment, to be revisited if the business changes |
| Settlement or closing services | **No** | Title companies or closing attorneys close every sale; "an entity that provides real estate settlement services" would be covered (314.2(h)(2)(x)) |
| Mortgage referrals | **No** | The brokerage takes no loan applications and arranges no loans (a mortgage broker would be covered, 314.2(h)(2)(xi)); agents give buyers a list of unaffiliated lenders |

**Decision: the Safeguards Rule does not apply.** It is used as the **benchmark** for this gap analysis because its elements give a concrete checklist for the "reasonable measures" that Fla. Stat. 501.171(2) does require, and because the FTC Act's unfairness standard (N53-R02) applies to the brokerage anyway. Benchmark rows are marked `Benchmark (not binding; P03 1.1)` in the CSV.

**Size exception, for the record.** If the brokerage ever became covered (for example by adding a closing desk, as the Small sample in this vertical has), it would hold information on about 2,300 consumers, fewer than 5,000, so 314.6 would except it from the written risk assessment (314.4(b)(1)), penetration testing and vulnerability assessments (314.4(d)(2)), the written incident response plan (314.4(h)), and the annual report (314.4(i)). The brokerage **chose to adopt all four in a reduced form anyway**, because each costs little and the incident response plan addresses its biggest risk.

### 1.2 Binding rules
| Rule | Why it applies | Rows |
|---|---|---|
| Fla. Stat. 501.171 | The brokerage is a "covered entity" (501.171(1)(b)) that holds personal information such as names with driver license numbers (501.171(1)(g)). Duties: reasonable measures (2), notice (3)-(5), third-party agents (6), disposal of customer records (8) | G-031 to G-034 |
| Broker escrow and records | A broker must place entrusted funds in escrow by the end of the third business day and keep them "until disbursement thereof is properly authorized" (Fla. Stat. 475.25(1)(k); r. 61J2-14.008(3)); sales associates deliver deposits by the next business day (r. 61J2-14.009); the broker reconciles monthly (r. 61J2-14.012); escrow disputes go to the Commission within 15 business days (r. 61J2-10.032(1)); records are kept 5 years (Fla. Stat. 475.5015). These rules are where a diverted deposit becomes a licensing problem | G-035 to G-043 |
| FCRA | The brokerage obtains consumer reports to screen rental applicants. Adverse action notices (15 U.S.C. 1681m(a)) and the disposal rule (16 CFR 682.3, which covers "any person" that possesses consumer information for a business purpose, 682.2(b)) apply | G-044, G-045 |
| FTC Act Section 5 (N53-R02) | No size threshold; covers unreasonable security and untrue security statements | G-046 |

**Florida rule text.** Rule chapters 61J2-14 and 61J2-10 were read from the Legal Information Institute's reproduction of the Florida Administrative Code (the official site returned a browser challenge to this environment). Statutes were read on the Florida Legislature's site (2026 text).

### 1.3 Other rules considered
| Rule | Applies? | Where handled |
|---|---|---|
| FinCEN residential real estate rule (31 CFR 1031.320) | No. Vacated by the U.S. District Court for the Eastern District of Texas on 2026-03-19; FinCEN, with the Department of Justice, has appealed, and states that reporting persons need not file while the order stands (FinCEN page rechecked 2026-10-06). The reporting cascade starts with the closing or settlement agent; brokers are not in it | G-047 (watch) |
| Fair Housing Act (42 U.S.C. 3604) and Fla. Stat. 760.23 | Yes, for tenant screening | P10 |
| CCPA/CPRA (N53-R03) | No: no California business; receipts far below $26,625,000 | None |
| PCI DSS (N53-R04) | Contractual only; rent card payments run on the property management platform's hosted page and no card data touches company systems | Noted in P04 |
| SEC disclosure (N53-R05) | No: privately held | None |

## 2. Method
1. **Requirements.** Each paragraph of 16 CFR 314.3, 314.4, and 314.6 became a row, split where one paragraph holds separable duties (for example, encryption in transit and at rest). Some sub-paragraphs were combined where the brokerage would meet them with one action: 314.4(e)(2)-(4) and 314.4(h)(1)-(7). The binding rows cover the parts of Fla. Stat. 501.171, the escrow rules, and the FCRA that bear on protecting client information and money; non-security parts (for example interest-bearing escrow accounts) were left out.
2. **Crosswalk.** Each row is mapped to CSF 2.0 and SP 800-53 Rev. 5. **This is an author mapping.** No official NIST mapping of 16 CFR 314, the Florida rules, or the FCRA was found.
3. **Documentary evidence.** Each status rests on a named record: user and MFA exports from SYS-01 and SYS-02, the SYS-01 visibility setting, the MSP device, encryption, and backup reports, the MSP contract, the agent agreement template, 15 sales escrow deposits, 20 transaction files for deposit verification, 12 months of reconciliations for both escrow accounts, the SYS-05 screening decision report and 10 applicant files, the website privacy page, and a walkthrough of the office on 2026-07-29. Interviews covered all 7 employees, three contractor agents, and the MSP lead technician.
4. **Status.** Each row was rated Met, Partially met, Not met, or Not applicable **as of the end of fieldwork (2026-08-07)**. Actions taken since (for example the designation letter, the policies, and the runbook) are in the remediation column and do not change the status. Gaps were rated with the P01 risk scale.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| 314.3 Program | 0 | 1 | 1 | 0 | 2 |
| 314.4(a) Qualified individual | 1 | 0 | 0 | 0 | 1 |
| 314.4(b) Risk assessment | 1 | 1 | 1 | 0 | 3 |
| 314.4(c) Safeguards | 0 | 6 | 5 | 1 | 12 |
| 314.4(d) Testing and monitoring | 0 | 0 | 2 | 0 | 2 |
| 314.4(e) Personnel and training | 0 | 2 | 0 | 0 | 2 |
| 314.4(f) Service providers | 0 | 0 | 3 | 0 | 3 |
| 314.4(g) Evaluate and adjust | 0 | 0 | 1 | 0 | 1 |
| 314.4(h) Incident response plan | 0 | 0 | 1 | 0 | 1 |
| 314.4(i) Annual report | 0 | 0 | 1 | 0 | 1 |
| 314.4(j) FTC notification | 0 | 0 | 0 | 1 | 1 |
| 314.6 Exception | 0 | 0 | 0 | 1 | 1 |
| **Safeguards Rule benchmark subtotal** | **2** | **10** | **15** | **3** | **30** |
| Fla. Stat. 501.171 | 0 | 2 | 2 | 0 | 4 |
| Florida broker escrow and records | 5 | 4 | 0 | 0 | 9 |
| FCRA | 0 | 2 | 0 | 0 | 2 |
| FTC Act Section 5 | 0 | 1 | 0 | 0 | 1 |
| FinCEN 31 CFR 1031.320 | 0 | 0 | 0 | 1 | 1 |
| **Total** | **7** | **19** | **17** | **4** | **47** |

Of the 36 rows with gaps, 4 are rated High, 19 Moderate, and 13 Low. The benchmark rows hold 25 of the gaps (3 High); the binding rows hold 11 (1 High: Fla. Stat. 501.171(2)).

**What the numbers say.** The money rules score best: deposits are placed on time, the Broker-owner signs every reconciliation, and online banking enforces dual control. The information rules score worst: almost nothing was written down, agent mailboxes have no MFA, and nobody watches for a takeover. The brokerage protects the bank account well and the email channel that tells people where to send money poorly.

## 4. Priority gaps
| Gap | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|
| Agent mailboxes, the shared administrator, and the backup console lack MFA | 314.4(c)(5) (G-014) | High | MFA for every account; block legacy protocols; named administrator accounts | Office Manager | 2026-10-31 |
| No monitoring of mailbox sign-ins or forwarding rules | 314.4(c)(8) (G-018) | High | Turn on alerts; block external forwarding; weekly review | Office Manager | 2026-10-31 |
| Reasonable measures not met on the email channel | 501.171(2) (G-031) | High | Close G-014 and G-018; verification rule (P01 R-002) | Office Manager | 2026-10-31 |
| Program not designed around the main threat | 314.3(b) (G-002) | High | The three High-risk treatments in P01 | Office Manager | 2026-10-31 |
| No incident response plan or notice deadlines known | 314.4(h); 501.171(3)-(5) (G-027, G-032) | Moderate | P08 runbook and matrix (approved 2026-09-14); tabletop | Office Manager | 2026-11-30 |
| Deposit verification requests missed in 4 of 20 files | r. 61J2-14.008(2)(b) (G-037) | Moderate | Deadline task in SYS-01; same-day escalation | Transaction Coordinator (senior) | 2026-10-31 |
| No adverse action notice for conditional approvals | 15 U.S.C. 1681m(a) (G-044) | Moderate | Notice for every conditional approval | Property Manager | 2026-10-31 |
| Every agent can open every file | 314.4(c)(1)(ii) (G-008) | Moderate | Limit agents to their own files | Office Manager | 2026-10-31 |
| No vendor due diligence, contract terms, or reviews | 314.4(f)(1)-(3) (G-023 to G-025) | Moderate | Vendor list; MSP amendment; annual reviews | Office Manager; Broker-owner | 2027-03-31 |
| No disposal of electronic records or screening reports | 314.4(c)(6)(i); 501.171(8); 682.3 (G-015, G-034, G-045) | Moderate | Retention schedule and January purge | Office Manager; Property Manager | 2027-01-31 |

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and, where the control was assessed, the POA&M (P07).

## 5. Remediation plan
The plan fits a 7-person office: most actions are settings in services the brokerage already pays for, or one-page procedures. The MSP performs the technical work under the Office Manager's direction. Costs are in the P01 treatment summary.

| Phase | Due | Actions | Gaps closed |
|---|---|---|---|
| 1. Stop the bleeding | 2026-09-30 | Named administrator accounts with MFA; payment instruction verification rule; offboarding checklist; first restore test (including the escrow ledger); escrow dispute step in the runbook | G-007, G-039, G-042, part of G-014 |
| 2. Close the email channel | 2026-10-31 | MFA for all agents; legacy protocols blocked; alerts and forwarding block; agents limited to their own files; instructions only through client document sharing; desktop encryption; inventory; new-tool approval; adverse action notices; deposit verification tasks; website statement corrected | G-002, G-004, G-008, G-009, G-010, G-011, G-013, G-014, G-018, G-026, G-031, G-037, G-044, G-046 |
| 3. Prepare and train | 2026-12-31 | Runbook tabletop with the MSP; training with a wire fraud module and phishing simulations; external scan; SaaS change log; vendor list with third-party agent contacts; MSP contract amendment | G-017, G-020, G-021, G-023, G-024, G-027, G-032, G-033, G-036 |
| 4. Records and vendors | 2027-03-31 | Retention schedule and first purge; screening report disposal; vendor reviews; security course for the Office Manager | G-015, G-022, G-025, G-034, G-045 |
| 5. Annual cycle | 2027-07-31 to 2027-09-30 | Risk assessment update (July); independent assessment and policy and retention review (August); written report to the Broker-owner (September) | G-001, G-006, G-016, G-019, G-028 |

**Progress check.** The Office Manager and the Broker-owner review the P07 POA&M for 30 minutes each month.

## 6. Pending regulatory changes
- **Safeguards Rule.** No proposed amendment to 16 CFR Part 314 was found in a Federal Register search through 2026-09-26. Because the rule does not bind the brokerage, the larger change to watch is in the business itself: adding closing or settlement services, or arranging loans, would make the rule apply.
- **FinCEN residential real estate rule.** Vacated, with the government's appeal pending (section 1.3). Even if reinstated, it would not make the brokerage a reporting person unless it acted as the closing or settlement agent.
- **HUD disparate impact rule.** HUD proposed on 2026-01-14 (91 FR 1475) and in a supplemental proposal on 2026-08-10 (91 FR 51416) to remove its discriminatory effects regulation (24 CFR 100.500). The regulation is still in eCFR as of 2026-09-23, and no final rule was found on 2026-10-06. This affects tenant screening (P10), not this table.
