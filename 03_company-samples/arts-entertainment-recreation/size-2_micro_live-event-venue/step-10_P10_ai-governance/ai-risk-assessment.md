# AI Risk Assessment: Ticket Price Recommendations and Bot Screening

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (live event venue operator with ticketing; one music club) |
| Tier / Vertical | Micro / Arts, Entertainment, and Recreation |
| AI use case | AI-001: the ticketing platform's "demand tools" module (SYS-01), switched on 2026-04-06. It has two functions with one settings page and one owner: price recommendations for ticket tiers, and bot screening with an on-sale queue |
| Why one use case | The registry default for this industry is "dynamic ticket pricing and bot detection". At this size the company does not let software set prices: the module only recommends, and a person accepts or rejects each change. Both functions are one vendor module, configured by one person, so they are assessed together (`../00_company-facts.md` section 5) |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the AI RMF Playbook. The Generative AI Profile (AI 600-1) is not used because the module is not generative AI |
| Assessor / date | Box Office and Ticketing Manager (business owner) with the Venue Manager (Security and Privacy Lead), 2026-08-17 to 2026-08-21 |
| Decision | Owner and General Manager, 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases; AI-002 is listed for completeness), built from the ticketing platform settings, the card statements and a question to the 7 employees (EV-009, EV-032, EV-041). The question did not reach the contractor workers, and what the Marketing Coordinator enters into public chatbots rests on that person's own answer; neither was established further |
| Related | P01 R-016, R-017, R-018, R-014; P03 G-071 to G-076; P06 POL-02 A.8, A.10, POL-04 4.7; P07 POAM-001 and POAM-003 |

## 1. GOVERN
- **Accountable owner:** the Box Office and Ticketing Manager. **Decision authority:** the Owner and General Manager.
- **Policies that apply:**
  - POL-04 4.7: only approved AI tools may use Restricted data, and any new AI feature or new use of patron data needs a P10 review before it goes live
  - POL-02 A.8: every ticket price shown or advertised must be the total price, with accurate fee names
  - POL-02 A.10: changes to price tiers and demand tools settings go through change control
  - POL-02 C.3: no patron data in public AI tools (AI-002)
- **Approved-tools list:** kept by the Venue Manager in POL-04 4.7. It has one entry, AI-001, under the conditions in section 6.
- **Scale for a Micro company:** there is no AI committee. The Owner, the Box Office and Ticketing Manager, and the Venue Manager review AI-001 at the monthly security meeting.

**How it started.** The Box Office and Ticketing Manager switched the module on after a vendor webinar, because it came at no extra cost with the platform. Nobody reviewed total-price display, price-change disclosure, artist price caps, or accessible ticket prices first (EV-009; EV-038). This assessment is the review that should have happened first.

## 2. MAP
### 2.1 Price recommendations
| Item | Description |
|---|---|
| Purpose and intended use | Suggest when to move a general admission show to its next price tier, or change a tier's price, so that underpriced tickets do not go to resellers and slow shows fill |
| Where used | 9 shows since April 2026: 31 recommendations, 27 accepted, 4 rejected. Each recommendation arrives as a notification; the Box Office and Ticketing Manager accepts or rejects it, usually on her phone within minutes |
| Affected people | Every ticket buyer for those shows, including buyers of accessible tickets; artists and promoters, whose agreements may cap prices |
| Data | Inputs: sales pace, tickets remaining by tier, days to show, event page views, queue size, and aggregate results for similar shows on the platform. Outputs: a suggested tier move or price with a short reason. **No patron-level data is an input** (vendor documentation, confirmed by test in section 4) |
| Build or buy | Buy: vendor machine-learning demand forecast inside SYS-01. The company configures it and cannot see or change the model |
| Not intended | Different prices for different buyers, prices based on a buyer's history or location, and any change to fees. Any of these requires a new assessment |

### 2.2 Bot screening and on-sale queue
| Item | Description |
|---|---|
| Purpose and intended use | Keep automated buying tools out of high-demand on-sales, randomize queue position at on-sale time, and enforce the posted limit of 4 tickets |
| Where used | Every on-sale marked high demand: 6 in the last 12 months, including the on-sale observed on 2026-07-21 |
| Affected people | Every patron who joins a protected on-sale (about 9,000 queue entrants across the 2 most recent protected on-sales) |
| Data | Inputs: device and browser signals, network address and network type, request timing, and account age. Outputs: allow, challenge, or block per session, with a reason code. The vendor keeps session records for 30 days |
| Build or buy | Buy: vendor machine-learning risk scoring inside SYS-01 |
| Not intended | Cancelling completed orders automatically. Cancelling orders that break the limit is a human decision (section 5) |

### 2.3 Applicable laws and rules
| Rule | Applies? | Why |
|---|---|---|
| FTC Rule on Unfair or Deceptive Fees, 16 CFR Part 464 (effective 2025-05-12) | **Yes** | Live-event tickets are a covered good (464.1). Any price offered, displayed, or advertised must include the total price (464.2(a)), shown more prominently than other pricing information (464.2(b)), and fees must not be misrepresented (464.3). The rule does not forbid demand-based prices, but every price the company shows, including "prices go up Friday" emails, must be a total price (P03 G-072; P01 R-014) |
| FTC Act Section 5, 15 U.S.C. 45(a), (n) (N71-R05) | **Yes** | Deception: the posted "limit 4 per customer" is enforced per account only (P03 G-071), and the privacy notice does not mention bot screening signals. Unfairness: blocking or overcharging patrons in ways they cannot avoid |
| ADA Title III ticketing rules, 28 CFR 36.302(f) | **Yes** | Accessible seating may not be priced higher than other tickets in the same seating section and must be available at all price levels (36.302(f)(3)). Individuals with disabilities must be able to buy accessible seating during the same stages of sale and through the same methods of distribution as other patrons (36.302(f)(1)(ii)). With a limit of 4 tickets, a buyer of a wheelchair space must be offered up to 3 additional seats next to it where available (36.302(f)(4)(i)). Proof of disability may not be required (36.302(f)(8)). The company treats the accessible viewing platform as part of the general admission section for pricing |
| BOTS Act, 15 U.S.C. 45c | **Protects the company** (no compliance duty) | It is unlawful to circumvent a security measure or access control system a ticket issuer uses to enforce posted purchase limits or online purchasing order rules, and to sell tickets obtained that way (45c(a)(1)). The room's 650 capacity exceeds the 200-person threshold in the "event" definition. The FTC enforces it (45c(b)) and state attorneys general may sue (45c(c)). Bot screening records are the evidence for a referral |
| Fla. Stat. 817.36 | **Protects the company** | 817.36(5) makes a person who intentionally uses or sells software to circumvent a ticket seller's website security measure, access control system, or other measure used to ensure an equitable ticket-buying process liable to the state for a civil penalty of treble the ticket price. The resale limits in 817.36(1) apply to resellers, not to the company as the original seller |
| PCI DSS v4.0.1 (N71-R04) | Indirectly | The module never touches card data. Its settings are changed only by venue users, so MFA and change control (POAM-003; POL-02 A.10) protect it |
| State AI and personal-data pricing laws | **No, today** | Ticket prices and access to one on-sale are not consequential-decision categories under the repository rubric, and the company operates only in Florida. The module uses no personal data to set prices (tested). Counsel must review before any personalized pricing feature is switched on |

## 3. Risk tier
**Tier: Medium** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`).
- **Why not High:** a tier price is the same for every buyer at a given moment and is not a consequential decision about a person; a person accepts every price change; a blocked session can still buy through a later sale or the door.
- **Why not Low:** the module sets prices patrons pay and decides which patrons reach a sold-out on-sale, it interacts directly with customers, and both functions are regulated (fee rule, ADA ticketing rules, FTC Act).

**Re-tier to High and reassess if:** price recommendations use any patron-level data; prices are applied automatically without a person accepting them; the module is extended to fees or to accessible tickets without the parity control in section 5; or bot screening is used to cancel completed orders or ban accounts automatically.

## 4. MEASURE
Fieldwork 2026-08-17 to 2026-08-21. Price recommendations: all 31 recommendations on the 9 shows, with the vendor's price-change log (EV-064). Bot screening: vendor reports for the 2 most recent protected on-sales (including 2026-07-21), a post-sale order check, and box office mailbox complaints (EV-065).

| Trustworthy characteristic | Test or metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Every accepted price stays within the artist's agreed cap; post-sale check finds no buyers above the posted limit across linked accounts | 2 of 9 shows went above the artist-agreed cap (by up to 15%) after accepted recommendations. 7 groups of linked accounts (same card or address) bought 61 tickets above the limit across the 2 on-sales | **No** |
| Safe | Accessible tickets never cost more than general admission for the same show (36.302(f)(3)); protected on-sales do not stop door sales | One show: the platform tier rose $6 above general admission for 2 days after an accepted recommendation applied to all tiers. Door sales ran normally during both on-sales | **No** |
| Secure and resilient | Settings changed only by named users with MFA, through change control | 3 administrators and the shared door login can see the module; no MFA (POAM-003); no change log | **No** |
| Accountable and transparent | Patrons told prices may change with demand; every advertised price a total price; blocked patrons see a reason and a way to appeal | No statement that prices change; "prices go up Friday" emails show base prices only; the block page says "unusual activity" with no contact route | **No** |
| Explainable and interpretable | Each recommendation and each block has a reason the business owner can read | Reasons available for all 31 recommendations; block reason codes visible in the vendor console; log kept 90 days | Yes |
| Privacy-enhanced | No patron-level data used to price; the same price for every buyer at the same time | Two test accounts (new, and a 4-year buyer in another city) saw identical prices at the same time on 3 shows; door and online prices matched on 10 spot checks. The 2023 privacy notice does not mention bot screening signals | Partial |
| Fair, with harmful bias managed | Bot screening challenge-failure rates by access type (mobile carrier network, home broadband, VPN or privacy relay, assistive technology). The company collects no protected characteristics, so access type is the measurable proxy. Flag a group whose rate is more than 2 times the baseline and more than 1 percentage point above it. Screen-reader test of the challenge | Mobile carrier networks 4.1% vs home broadband 1.3% (flagged). VPN or privacy relay 19% (an expected bot signal; appeal route needed). Screen-reader test failed: the challenge is a visual puzzle only, because the vendor's audio alternative is switched off in the venue settings | **No** |

**Bias findings.**
- **Mobile networks.** Patrons on mobile carrier networks fail the challenge about 3 times as often as home broadband users, probably because many phones share one network address. Younger patrons and patrons without home internet are the most likely to be affected. The vendor will tune the signal and the company will re-measure at the next 2 protected on-sales.
- **Assistive technology.** A blind patron using a screen reader cannot pass the challenge. That also denies the same stage of sale that 28 CFR 36.302(f)(1)(ii) protects for buyers of accessible seating.
- **Accessible ticket channel.** Accessible tickets are sold only by phone today (P03 section 1.2), so they are not sold "through the same methods of distribution" as other tickets. This must be fixed before phone card sales stop.

## 5. MANAGE
**Human-in-the-loop design:**
- **Price recommendations:** before each on-sale, the Box Office and Ticketing Manager enters a floor and a ceiling for every tier, with the artist's cap as the ceiling. The module may only recommend inside those limits. Accessible tiers are removed from the module and set daily to the general admission price. Any accepted change of more than 20% within 24 hours needs the Owner's approval, recorded in the change log. Recommendations are reviewed at a desk, not accepted on a phone at the door.
- **Bot screening:** allow, challenge, and block decisions stay automated, because a person cannot review sessions in real time. People handle the outcomes: a published appeal route by email, a release log kept by the Box Office and Ticketing Manager, and a human decision, with the linked-account evidence, before any completed order that breaks the limit is cancelled under the purchase terms on the event page.

**Disclosure:**
- Event pages for shows that use recommendations say that prices may change with demand and that the price shown at checkout is the total price.
- Email, website, and social price displays show the total price at the time of sending or posting (POL-02 A.8; P03 G-072, G-073).
- The limit wording becomes "4 per account", or the vendor's linked-account check is switched on (P03 G-071).
- The privacy notice rewrite (P03 G-070) describes the bot screening signals and their 30-day retention.

**Data protection:**
- No patron-level data may be added as a pricing input without a new P10 review and counsel's advice (POL-04 4.7).
- Only the Box Office and Ticketing Manager and one backup administrator can change module settings, with MFA (POAM-001, POAM-003).
- Block and release records for flagged sessions and any cancellation decisions are exported after each protected on-sale and kept 12 months in a restricted suite folder, long enough to support an FTC or state referral under 15 U.S.C. 45c or Fla. Stat. 817.36(5). Other session records stay with the vendor for its 30 days.

**Monitoring:**
- After each show that used recommendations: a one-line check of cap, floor, and accessible tier parity in the change log.
- After each protected on-sale: blocks, challenges, and challenge-failure rates by access type; appeals and releases; and the linked-account check.
- Monthly summary at the security meeting, updating P01 R-016, R-017, and R-018.

**Incident handling:** an unauthorized change to price tiers or module settings is a security incident under POL-03 and the P08 runbook (section 4, item 3 checks for changed price tiers and demand tools settings). A pricing error (a cap or parity breach) is handled by the Box Office and Ticketing Manager: pause the module, fix the price, and refund the difference with the Owner's approval. An accessible tier parity breach is always refunded.

**Decommissioning:** switch price recommendations off if a cap or parity breach happens after the section 5 controls are live, or if the vendor adds patron-level inputs without notice. Switch bot screening to queue-only mode if the mobile network or assistive technology flag is still open after 2 re-measured on-sales and the vendor cannot fix it.

## 6. Decision
**Approve with conditions.** Owner and General Manager, 2026-08-31.

**Before the next on-sale that uses recommendations, and no later than 2026-09-15:**
1. Floors and ceilings entered for every show on sale, with artist caps as ceilings.
2. Accessible tiers removed from the module and set to the general admission price. The Owner approved refunding the $6 difference to the 3 buyers affected in August.
3. Owner approval recorded for any change of more than 20% within 24 hours.

**By 2026-09-30:**
4. "Prices may change with demand" statement on affected event pages; total prices in all email, website, and social displays (with P01 R-014).
5. Audio challenge alternative switched on; appeal route published; release log started.
6. Accessible tickets on sale online through the same checkout as other tickets (36.302(f)(1)(ii)), before phone card sales stop under P03 Option B.
7. MFA for all venue users (POAM-003).

**By 2026-11-30:** access-type measurement after the next 2 protected on-sales, vendor tuning for mobile networks, and corrected limit wording or the linked-account check (P01 R-016).

The Box Office and Ticketing Manager reports progress at the monthly security meeting. The next full reassessment is due by 2027-08-31, or sooner if a re-tier trigger in section 3 is met.
