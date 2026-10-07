# AI Use Assessment: Ticketing Platform Smart Pricing and Bot Protection (one page)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent event promoter with one leased room) |
| Tier / Vertical | Sole Proprietorship / Arts, Entertainment, and Recreation |
| AI use case | AI-001: the ticketing platform's smart pricing and bot protection features (SYS-01). Smart pricing ran in auto-apply mode on 8 shows from 2026-05-01 to 2026-07-31 (37 price changes); bot protection runs on every on-sale |
| Framework | NIST AI RMF 1.0 (Govern, Map, Measure, Manage), short form. AI 600-1 is not used for AI-001, which is not generative AI |
| Assessor and decision | Owner, 2026-08-12, with the IT consultant; decision 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases; AI-002 is a consumer chatbot for drafting posts, Low tier) |

## 1. What it does (Map)
**Smart pricing** watches sales speed, tickets left, days to the show, and page views, and suggests or (in auto-apply mode) makes price changes per price level. The vendor states that no patron-level data is used, so every buyer sees the same price at the same moment; the owner cannot see or change the model. **Bot protection** scores each session at an on-sale using device, browser, network, and timing signals, then allows, challenges, or blocks it. On the 2 sold-out on-sales of 2026 it blocked 610 sessions; 3 fans emailed that they were blocked, and they had no route to appeal except emailing the owner. The owner turned smart pricing on after a vendor webinar, without any review (`../00_company-facts.md` section 4, gap 12).

## 2. Rules that apply
| Rule | Applies? | Why |
|---|---|---|
| FTC Rule on Unfair or Deceptive Fees, 16 CFR 464.2 | **Yes** | Every ticket price the owner offers, displays, or advertises must be the total price. A post or flyer showing an old face price "plus fees" breaks the rule twice once smart pricing has moved the price (P03 G-072) |
| FTC Act Section 5, 15 U.S.C. 45(a)(1) | **Yes** | Statements such as "prices never go up" or a posted ticket limit must match what the features do (P03 G-070) |
| ADA Title III, 28 CFR 36.302(f) | **Yes, seated shows** | Accessible seating may not be priced higher than other tickets in the same seating section and must be available at all price levels (36.302(f)(3)); people with disabilities must be able to buy during the same stages of sale and through the same methods (36.302(f)(1)(ii)), which a challenge they cannot pass would deny |
| BOTS Act, 15 U.S.C. 45c, and Fla. Stat. 817.36(5) | **Protect the owner** | Circumventing a ticket issuer's security measures or purchase limits is unlawful (45c(a)(1)); Florida imposes a civil penalty of treble the ticket price on anyone who uses or sells software to get around a ticket seller's website security measures (817.36(5)). Bot protection records are the evidence for a referral |
| Fla. Stat. 817.36(1) resale limits | No | They bind resellers, not the original seller |

## 3. Risk screen (repository rubric)
**Tier: Medium.** Ticket prices and access to an on-sale are not consequential decisions in the rubric's categories, and smart pricing sets the same price for every buyer. It is not Low because both features act directly on the public, prices are regulated by the fee rule and the ADA ticketing rules, and in auto-apply mode no human looks before a price changes. **Re-tier to High** if pricing ever uses patron-level data (history, location, device), if fees are priced by the model, or if bot protection is used to cancel orders or ban accounts automatically.

## 4. Data-sharing rules (Govern)
1. No patron data, card data, or credentials go into any AI tool, including AI-002 (POL-01 9.5). The 2026-06 paste of a complaint email was deleted from the chatbot history on 2026-08-12, and the assistant was briefed.
2. Smart pricing may use only event-level data. The owner keeps the vendor's statement on file and re-checks it with each SOC 2 review (P09).
3. Bot protection session data stays with the vendor; the owner exports only the records of sessions blocked at an on-sale and keeps them 12 months for a possible BOTS Act or Fla. Stat. 817.36(5) referral, then deletes them (POL-01 8.6).

## 5. Human review of outputs and testing (Measure and Manage)
| Check | Result in the review (8 shows, 2 on-sales) | Rule from 2026-09-01 |
|---|---|---|
| Prices within artist caps | 1 show went 12% above the artist's agreed cap for 4 days | Suggest-only mode: the owner approves each change; the artist cap is entered as the ceiling |
| Accessible seating parity (seated shows) | Parity held on all 5 seated shows, but no setting enforces it | Accessible price level excluded from changes; checked against the same section before each on-sale and weekly |
| Advertised prices | 17 of 20 posts and all 6 flyers showed "$X plus fees" | Posts link to the live event page and show the current total price |
| Blocked fans | 3 complaints, no appeal route | Appeal address on the event page; the owner reviews each appeal within 1 business day and releases genuine fans |
| Bot protection fairness | Block rates by access type cannot be measured at this size (vendor report shows totals only) | After each sold-out on-sale, count appeals and confirm the vendor's accessible challenge option (audio) is on; ask the vendor for block rates by network type at the annual review |

## 6. Decision: approve with conditions (2026-08-31)
Keep both features, under the rules in section 5, with smart pricing in **suggest-only mode** from 2026-09-01 (P01 R-012, due 2026-09-30). Refund the difference to buyers of the show that exceeded the artist's cap if the artist agreement requires it. Turn smart pricing off for any show where a cap or accessible seating breach happens again. Re-assess by 2027-08-31, or sooner if a re-tier trigger in section 3 occurs. AI-002 is approved for public information only.
