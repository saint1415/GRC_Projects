# Review of the Multi-Sector division pairings, October 2026

**Date:** 2026-10-08
**Scope:** all 36 pairings in `02_industry-rules/multi-sector-divisions.csv` (the focus division plus two other divisions for each industry's size-6 sample). 33 were proposed during Phase 5 and marked "pairing open for review" (`PLAN.md`, open item 3).
**Method:** each pairing was read against its size-6 facts file (`00_company-facts.md`). Three questions were asked:
1. Is it realistic? Would a real group own these three businesses?
2. Does it teach? Do the divisions bring different regulators or assurance needs?
3. Is the ownership lawful? Size 6 is always a publicly traded holding company, so the check is whether anything blocks public ownership or common control, and whether the sample says how it handles that.

Legal claims were checked against primary sources: eCFR (point-in-time 2026-10-01), Florida Statutes on leg.state.fl.us, and the Florida Administrative Code text on LII.

## Verdict

All 36 pairings are kept. 33 need no change. 3 needed a missing fact, and these were added in the same change as this review. No sample was rebuilt.

| Verdict | Pairings |
|---|---|
| Keep as is (33) | Agriculture; Food and Agriculture; Mining; Energy; Dams; Nuclear; Water; Construction; Manufacturing; Chemical; Defense Industrial Base; Wholesale; Transportation; Transportation Systems; Information; Communications; Information Technology; Finance and Insurance; Financial Services; Real Estate; Commercial Facilities; Professional Services; Management of Companies; Administrative and Support; Educational Services; Health Care; Healthcare and Public Health; Arts and Entertainment; Accommodation and Food Services; Other Services; Public Administration; Government Facilities; Emergency Services |
| Keep, add a missing fact (3) | Utilities; Critical Manufacturing; Retail Trade |
| Replace | None |

## What works well

The best pairings teach a conflict that comes from owning the businesses together, and the samples already handle it:
- **Real Estate (brokerage, mortgage and title, homebuilding).** Referrals between divisions are RESPA affiliated business arrangements (12 CFR 1024.15), with the disclosure given at referral.
- **Professional Services (CPA firm, wealth management, practice software).** A public company cannot own an attest practice in the usual way. The sample uses an alternative practice structure: a separate CPA partnership that the group does not own. The partnership also takes no part in the group's own control assessment, to protect its independence.
- **Retail Trade (grocer, wholesale, store card).** The store card is not a payment brand card, so PCI DSS does not reach it. It is covered by the FTC Safeguards Rule instead.
- **Health Care (care delivery, health plan, health SaaS).** Two separate HIPAA covered entities share one data platform.

Ownership was checked where a public holding company might not fit the industry. The college is a private, for-profit institution. The nursing school owned by the hospital group is also for-profit. The CPA group carves out its attest firm.

## The three fixes

| Pairing | Gap | Fix (fact row in `00_company-facts.md`, plus a context note in the P03 gap analysis report) |
|---|---|---|
| **Utilities**: electric utility, gas production, engineering services | The facts did not say which holding company and affiliate rules govern the utility's purchases from its sister divisions. Engineering Services does about $400 million a year of work for the utility. | FERC holding company notice and books-and-records access (18 CFR 366.4(a), 366.2). Single-state waiver of the accounting rules only (366.3(c)(1)). No purchases of non-power goods or services from a non-utility affiliate above market price (35.44(b)(2)). Florida PSC affiliate pricing, cost allocation manual and annual reporting (Fla. Admin. Code R. 25-6.1351(3)(c), (5), (6)). |
| **Critical Manufacturing**: transformer maker, electric utility, grid engineering | This is the least realistic pairing, because a manufacturer rarely owns a large regulated utility. The facts also did not say what rules govern the utility buying transformers and engineering from its sister divisions. | Same rules as the Utilities row. The facts now say the pairing is unusual and is kept on purpose to show affiliate conflicts. |
| **Retail Trade**: grocer, grocery wholesale, store card and consumer loans | Financial Services issues revolving credit and personal loans without being a bank, but the facts did not name the license that allows it. | Florida retail installment seller license, because it grants revolving credit for purchases at the group's stores (Fla. Stat. 520.31(16), 520.32(1)). Consumer finance license for loans of $25,000 or less above 18 percent a year (Fla. Stat. 516.02(1), (2)(a)). Other states are handled generically. |

These are background facts. They are not scored in P03, because they are not security requirements, so no risk, gap or assessment count changed.

## Observation, not a defect

The second and third divisions lean toward a few sectors. Professional, scientific and technical services (NAICS 54, mostly engineering and consulting) accounts for 15 of the 72. Information (51) and finance (52) account for 8 each, and wholesale (42) for 7. Two groups stay close to one industry: Financial Services (processor, payments software, merchant consulting) and Public Administration (GovTech, IT consulting, government software). Both are realistic. They teach less about handling different regulators across divisions, but replacing them would mean rebuilding whole samples, so they are kept.

## Not verified

- The official Florida Administrative Code site (flrules.org) did not respond. Rule 25-6.1351 was read from LII's reproduction of the official text.
- Lending licenses in states other than Florida are handled generically and were not checked state by state.
