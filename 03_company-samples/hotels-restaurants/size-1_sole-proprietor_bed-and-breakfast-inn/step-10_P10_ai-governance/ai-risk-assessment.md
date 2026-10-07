# AI Use Assessment: Innkeeping Software AI Add-on (one page)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (six-room bed-and-breakfast inn) |
| Tier / Vertical | Sole Proprietorship / Accommodation and Food Services |
| AI tool | One third-party tool: the innkeeping software's AI add-on (SYS-11), turned on 2026-05-01, with two features: **AI-001** rate suggestions and **AI-002** website guest chat assistant |
| Why this tool | The registry default for this vertical is revenue-management pricing and a guest chatbot. A six-room inn does not buy an enterprise revenue-management system; its innkeeping vendor bundles both features in one add-on, so the tier's "one third-party AI tool" is this add-on |
| Framework | NIST AI RMF 1.0 (Govern, Map, Measure, Manage), short form; AI 600-1 for the generative chat feature |
| Assessor and decision | Owner-innkeeper, 2026-08-24 to 2026-08-25; decision 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases, one tool) |

## 1. What it does (Map)
**AI-001 rate suggestions** forecast demand from the inn's own booking history and public OTA rates, then change nightly rates in the calendar, booking engine, and both OTA channels. **Auto-apply is on, with no floor, ceiling, or daily limit.** The vendor's terms (read 2026-08-24) say suggestions use only the inn's own data plus public rates, and that the inn's non-public data is not shared with other inns. Rates are the same for every guest; the add-on has no personalized pricing feature.

**AI-002 chat assistant** answers questions on the website (parking, pets, breakfast, check-in) and quotes rates and availability, then links to the booking engine. Transcripts, including guests' names and emails, are kept by the vendor with no deletion period. The owner switched it on without reading the terms.

## 2. Rules that apply
| Rule | Applies? | Why |
|---|---|---|
| 16 CFR 464.2 and 464.3 | **Yes, both** | An inn's short-term lodging is a covered service (464.1). Every price offered or displayed must show the total price, including the mandatory $15 housekeeping fee, more prominently than other pricing. The chat quotes nightly rates only (**fails**). AI-001 changes nightly rates; the fee must be part of what every channel shows |
| FTC Act Section 5, 15 U.S.C. 45(a) | **Yes, both** | Chat answers about prices and policies are the inn's own representations |
| Fla. Stat. 501.160 | **Yes, AI-001** | During a Governor-declared state of emergency it is unlawful to rent or offer at an unconscionable price essential services or a dwelling unit needed as a direct result of the emergency. A gross disparity from the average price in the 30 days before the declaration is prima facie evidence, unless explained by added costs or market trends. The statute does not name hotels or inns; the inn treats rooms sought by evacuees as covered, which is the cautious reading. An add-on that raises rates on sudden demand is the exact risk |
| PCI DSS v4.0.1 (Req 3.2, 4.2) and Fla. Stat. 501.171 | **Yes, AI-002** | Guests have typed card numbers into chat (4 transcripts); transcripts hold personal information, and the vendor is a third-party agent that must report breaches within 10 days (501.171(6)(a)) |

## 3. Risk screen (repository rubric)
**AI-001: Medium.** It sets the price every guest pays and acts with no human today, but prices are not individualized and a room rate is not a consequential decision under the rubric. **Re-tier to High** for the duration of any declared state of emergency covering the county, or if a personalized pricing feature is ever offered. **AI-002: Medium.** It talks to guests and makes price statements, but makes no decisions about them and hands bookings to the booking engine.

## 4. Data-sharing rules (Govern)
1. No card numbers, ID numbers, or passwords go into the add-on or any AI tool (POL-01 9.5). The chat window must say "Please do not type card details here; book securely through our booking page."
2. The vendor must mask card numbers typed into chat and keep transcripts no longer than 90 days; the 4 transcripts with card numbers must be deleted.
3. Any new feature (personalized prices, payments or reservation changes in chat) needs a new assessment first.

## 5. Human review of outputs (Measure and Manage)
**Checks run on 2026-08-24:**
- AI-001: the change log for May to August 2026 showed 214 automatic rate changes. The highest applied rate was $289 on a festival weekend, 86% above the $155 average daily rate. No declared emergency occurred in the period, but the add-on has no emergency setting at all.
- AI-002: 20 test questions. 18 answered correctly (the pet fee and the cancellation window were wrong); 0 of the 8 rate answers included the $15 fee.

**Ongoing:** each Monday the owner reviews the week's automatic rate changes and reads 10 chat transcripts. A wrong price published at scale or a chat that collects card data is logged as an incident (POL-01 10.2).

## 6. Decision: approve with conditions (2026-08-31)
**AI-001** may keep applying rates automatically **only if**, by 2026-10-15: a floor ($119), a ceiling ($249), and a 15% daily change limit are set, with owner approval for anything outside them; and, whenever the Governor declares a state of emergency covering the county, auto-apply is turned off and rates stay at or below the 30-day pre-declaration average unless the owner documents a cost reason. Otherwise switch to "suggest only."

**AI-002** may keep running **only if**: every rate answer states the total price including the fee by 2026-09-30 (or the fee is folded into the nightly rate, P03 G-070); questions about accessibility, safety, or booking changes hand off to the owner by 2026-09-30; and card masking, deletion of the 4 transcripts, and 90-day retention are in place by 2026-10-31. If any condition is missed, turn the chat off and keep the FAQ page. Tracked as P01 R-013.
