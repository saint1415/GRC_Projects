# AI Risk Assessment: Dynamic Ticket Pricing and Bot Detection

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (live event venue operator with ticketing) |
| Tier / Vertical | Small / Arts, Entertainment, and Recreation |
| AI use cases | AI-001: dynamic ticket pricing module (in production since March 2026). AI-002: bot detection and virtual queue (in production since 2024). Both are modules of the ticketing platform (SYS-01) |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the AI RMF Playbook. The Generative AI Profile (AI 600-1) is not used because neither module is generative AI |
| Assessor / date | Director of Ticketing (business owner) with the IT Manager (Information Security Lead), fieldwork 2026-08-17 to 2026-08-21 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases), built from the ticketing platform's module settings and change history, the vendor's SOC 2 system description, and the fieldwork tests in section 4 (EV-032, EV-026, EV-062). Whether staff use public AI tools with company data was not established (intake open request) |
| Related | P01 R-013, R-014, R-015, R-016; P03 G-071 to G-076; P06 POL-01 4.11 and 4.12, POL-04 4.6, POL-05 4.8; P07 POAM-003 and POAM-010; P08 runbook; P09 vendor report review |

## 1. GOVERN
- **Accountable owner:** Director of Ticketing, for both use cases. **Decision authority:** General Manager (Medium tier). The majority owner decides if a use case is re-tiered High, and already owns the High fee-display risk (P01 R-015).
- **Policies that apply:**
  - POL-01 4.11: every ticket price shown or advertised must be the total price, and fee names must be accurate
  - POL-01 4.12: changes to pricing rules and bot mitigation settings go through change control with owner approval
  - POL-04 4.6: new uses of patron data, including new AI features, require a P10 review before go-live
  - POL-05 4.8: only AI tools on the approved tools list may be used with company data
- **Approved tools list:** kept by the IT Manager. Today it lists AI-001 and AI-002 only, both as vendor modules inside SYS-01. No general-purpose AI tool is approved for company data. Public AI tools may be used only with Public data (POL-04).
- **What went wrong in March 2026:** the dynamic pricing module was switched on by a ticketing administrator after a vendor webinar. Nobody reviewed total-price display, price-change disclosures, artist price caps, or accessible seating prices (EV-032 settings history; EV-035 document request; P09 CC3.4). This assessment is the review that should have happened first.
- **Scale for a Small company:** there is no AI committee. The Director of Ticketing, the Marketing Director, the IT Manager, and the Controller review both use cases quarterly and before any new module or setting that changes how prices or purchase access are decided.

## 2. MAP

### 2.1 AI-001 Dynamic ticket pricing
| Item | Description |
|---|---|
| Purpose and intended use | Raise or lower the price of each price level for reserved-seat Hall shows as demand changes, within limits the company sets, to reduce underpriced tickets going to resellers and to fill slow shows |
| Where used | Hall shows in the seated configuration only. General admission Lounge shows and all standing shows use fixed prices. 46 Hall shows have used the module since March 2026 |
| Users / operators | Director of Ticketing and 2 box office supervisors set rules. The module applies price changes automatically ("auto-apply" mode, the vendor default) |
| Affected people | Every buyer of a Hall reserved seat (online, box office, and phone), including buyers of accessible seating. Also artists and promoters, whose agreements may set price caps |
| Data | Inputs: sales velocity, seats remaining by section, days to show, event page views, virtual queue size, and the company's floor and ceiling settings. Outputs: a new price per price level and a reason code. **No patron-level data is an input** (vendor documentation, confirmed by test in section 4) |
| Build or buy | Buy: vendor machine-learning demand forecast inside SYS-01. The company configures it and cannot see or change the model |
| Not intended | Individual prices for different buyers, prices based on a buyer's history or location, and any change to fees. Any of these requires re-assessment |

### 2.2 AI-002 Bot detection and virtual queue
| Item | Description |
|---|---|
| Purpose and intended use | Keep automated buying tools out of high-demand on-sales, randomize queue position at on-sale time, and enforce the posted limit of 6 tickets |
| Where used | Every on-sale the Director of Ticketing marks as high demand (14 on-sales in the last 12 months) |
| Users / operators | The vendor's risk scoring runs automatically. The Director of Ticketing sets the protection level per on-sale. Guest services can release a blocked patron by hand |
| Affected people | Every patron who joins a protected on-sale; about 61,000 queue entrants across the 3 on-sales reviewed |
| Data | Inputs: device and browser signals, network address and network type, request timing, and account age. Outputs: allow, challenge, or block per session, with a reason code. The vendor keeps session records for 30 days |
| Build or buy | Buy: vendor machine-learning risk scoring and queue inside SYS-01 |
| Not intended | Automatic cancellation of completed orders. Cancelling orders that break the ticket limit is a human decision (section 5) |

### 2.3 Applicable laws and rules
| Rule | Applies? | Why |
|---|---|---|
| FTC Rule on Unfair or Deceptive Fees, 16 CFR Part 464 (90 FR 2066, effective 2025-05-12) | **Yes, both** | "Covered good or service" includes live-event tickets (464.1). Any price offered, displayed, or advertised must include the total price (464.2(a)), shown more prominently than other pricing information (464.2(b)), and fees must not be misrepresented (464.3). The rule does not forbid demand-based pricing, but every dynamic price the company shows, including "from" prices in emails, must be a total price. Open gaps: P03 G-072, G-073, G-075; P01 R-015 (High) |
| FTC Act Section 5, 15 U.S.C. 45(a), (n) (N71-R05) | **Yes, both** | Deception: the posted "limit 6 per customer" is enforced per account only (P03 G-071), and the privacy notice does not mention bot detection signals. Pricing statements (for example "prices never change after on-sale") must match what AI-001 does. Unfairness: blocking or overcharging patrons in ways they cannot avoid |
| BOTS Act, 15 U.S.C. 45c | **Protects the company** (no compliance duty) | It is unlawful to circumvent a security measure or access control system a ticket issuer uses to enforce posted purchase limits or online purchasing order rules, and to sell tickets obtained that way (45c(a)(1)). "Ticket issuer" may include the venue operator, and an "event" is held in a venue with capacity over 200 (Pub. L. 114-274, sec. 3). Both rooms qualify (3,200 and 350). The FTC enforces it as a trade regulation rule violation (45c(b)) and state attorneys general may sue (45c(c)). AI-002 logs and queue records are the evidence for a referral, which is why retention matters (P01 R-013; P03 G-076) |
| Fla. Stat. 817.36 | **Protects the company** for AI-002; resale caps do not bind the company | 817.36(5) makes a person who intentionally uses or sells software to circumvent a ticket seller's website security measure, access control system, or other measure used to ensure an equitable ticket-buying process liable to the state for a civil penalty of treble the ticket price. The resale limits in 817.36(1) apply to resellers, not to the company as the original seller |
| ADA Title III ticketing rules, 28 CFR 36.302(f) | **Yes, AI-001; also relevant to AI-002** | A concert hall is a place of public accommodation (28 CFR 36.104). Accessible seating may not be priced higher than other tickets in the same seating section, and must be available at all price levels (36.302(f)(3)). Patrons with disabilities must have an equal opportunity to buy during the same stages of sale and through the same methods (36.302(f)(1)(ii)). Because the posted limit exceeds 4, patrons buying a wheelchair space may buy up to the same number of tickets (36.302(f)(4)(iv)). Proof of disability may not be required (36.302(f)(8)) |
| PCI DSS v4.0.1 (N71-R04) | Indirectly | Neither module touches card data. Changes to checkout settings follow 6.4.3 and 6.5 through POL-01 4.12 |
| State AI and surveillance-pricing laws | **No, today** | Ticket pricing and ticket purchase access are not consequential-decision categories under the repository rubric or Colorado SB26-189, and the company operates only in Florida. Some states are adding limits on prices set from personal data (for example Connecticut PA 26-64, effective 2026-10-01). AI-001 does not use personal data (tested), so these laws are not expected to apply. Counsel must review before any personalized pricing feature is enabled |

## 3. Risk tier
**Both use cases: Medium** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`).

**AI-001, why not High:** a price per price level is not a consequential decision about a person, and it is the same for every buyer at a given moment. **Why not Low:** it sets prices that patrons pay directly, it is regulated by the fee rule and the ADA ticketing rules, and it acts with no human review today.

**AI-002, why not High:** blocking a session from one on-sale is not a consequential decision in the rubric's categories, and the patron can still buy through the box office, the phone line, or a later sale. **Why not Low:** it makes automated allow or block decisions about individual patrons, with no appeal path today.

**Escalation triggers (re-tier to High and re-assess):**
- AI-001 uses any patron-level data (purchase history, location, device) to set a price
- AI-001 is extended to fees, or to accessible seating price levels without the parity control in section 5
- AI-002 is used to cancel completed orders automatically or to ban accounts permanently
- AI-002 adds biometric or identity-document checks

## 4. MEASURE
Fieldwork 2026-08-17 to 2026-08-21. AI-001: a sample of 12 Hall shows from March to August 2026, with the vendor's price-change log (214 price changes). AI-002: vendor reports for the 3 high-demand on-sales held since 2026-06-01 (including the on-sale observed on 2026-07-17), a post-sale order audit, and guest services emails.

### 4.1 AI-001 Dynamic ticket pricing
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Every price stays inside the show's floor and ceiling, including caps in the artist agreement | Caps were never entered in the module. 3 of 12 shows went above the artist-agreed cap, by up to 18% | **No** |
| Safe | Prices for accessible seating are never higher than other seats in the same section (28 CFR 36.302(f)(3)); accessible seating exists at every price level | 1 of 12 shows: accessible seats in one section were $12 above the rest of the section for 3 days, because the module moved the accessible price level on its own. All price levels had accessible seating | **No** |
| Secure and resilient | Pricing rules changed only by named users with MFA, through change control | 11 administrators can change pricing rules; MFA not enforced (POAM-003); no change log (POAM-010) | **No** |
| Accountable and transparent | Patrons are told prices may change with demand; every advertised price is a total price (16 CFR 464.2) | Vendor event and checkout pages show total prices. No statement anywhere that prices change with demand. Emails still use "from $39" base prices set at announcement (P03 G-072) | **No** |
| Explainable and interpretable | Each price change has a reason code the Director of Ticketing can read | Reason codes available for all 214 changes (for example "sell-through above forecast"); log kept 90 days | Yes |
| Privacy-enhanced | No patron-level data used; same price for every buyer at the same time | Two test accounts (new and 5-year buyer, different cities) saw identical prices at the same time on 4 shows; box office and online prices matched on 20 spot checks | Yes |
| Fair, with harmful bias managed | Compare prices paid by channel (online, box office, phone) and by accessible versus other seats in the same section. Flag any channel or accessible seat priced above the matching online price for the same seat type at the same time | Channels matched. Accessible seating breach as in "Safe" above. 27 patron complaints about price changes, mostly about a show where prices fell 30% two days before the show | **No** (accessible seating) |

### 4.2 AI-002 Bot detection and virtual queue
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Post-sale audit: orders over the posted limit of 6 across accounts that share a card or billing address | 34 linked-account clusters bought 1,020 tickets above the limit across the 3 on-sales, and many of those seats were listed for resale within an hour. The module blocked 7,400 sessions and challenged 5,900 | **No** (linked accounts not checked; P03 G-071) |
| Safe | Protected on-sales do not stop box office and phone sales | Box office and phone sales ran normally during all 3 on-sales | Yes |
| Secure and resilient | Protection level changed only by named users with MFA, through change control | Same 11 administrators and no MFA as AI-001 | **No** |
| Accountable and transparent | Blocked patrons see a reason and a way to appeal; evidence kept long enough for a BOTS Act referral | Block page says "unusual activity" with no contact route. 38 patrons complained; guest services released 14 by hand and kept no record. Session records kept 30 days | **No** |
| Explainable and interpretable | Reason code per block or challenge visible to guest services | Reason codes exist in the vendor console but guest services has no access | Partial |
| Privacy-enhanced | Signals limited to what bot detection needs; privacy notice describes them | Device and network signals only, no sale to third parties. The 2021 privacy notice does not mention bot detection | Partial |
| Fair, with harmful bias managed | Block and challenge-failure rates by access type (mobile carrier network, home broadband, VPN or privacy relay, assistive technology). The company does not collect protected characteristics, so access type is the measurable proxy. Flag a group whose rate is more than 2 times the baseline and more than 1 percentage point above it. Screen-reader test of the challenge | Challenge failure: mobile carrier networks 3.8% vs 1.1% on home broadband (flagged). VPN or privacy relay 22% (expected bot signal; appeal path needed). Screen-reader test failed: visual puzzle only, because the vendor's audio alternative is switched off in the venue settings | **No** |

**Bias findings.**
- **Mobile networks.** Patrons on mobile carrier networks fail the challenge about 3.5 times as often as home broadband users, probably because many phones share one network address. Younger patrons and patrons without home internet are the most likely to be affected. The vendor will tune the network-address signal, and the company will re-measure at the next 2 high-demand on-sales.
- **Assistive technology.** A blind patron using a screen reader cannot pass the challenge. That also denies the same stage of sale that 28 CFR 36.302(f)(1)(ii) protects for buyers of accessible seating. The audio alternative must be switched on before the next protected on-sale, and the box office phone line must stay open during every protected on-sale.
- **Accessible seating prices.** Automatic changes to accessible price levels can breach 28 CFR 36.302(f)(3) within hours. Accessible price levels are removed from auto-apply (section 5).

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** switch from "auto-apply" to bounded automation. The module may change prices only between a floor and a ceiling that the Director of Ticketing enters for each show before on-sale, with any artist cap as the ceiling. A change of more than 25% within 24 hours goes to the vendor's approval queue for the Director of Ticketing or a box office supervisor. Accessible seating price levels are removed from the module and set daily to no more than the lowest current price of other seats in the same section. The Director of Ticketing can pause the module for any show at any time.
- **AI-002:** automated allow, challenge, and block decisions stay automated, because a person cannot review sessions in real time. Humans handle the outcomes: guest services can release a blocked patron through a published appeal route, and every release is logged. Cancelling completed orders that break the ticket limit requires the Director of Ticketing's review of the linked-account evidence and a documented reason, under the purchase terms posted on the event page.

**Disclosure:**
- Event pages for Hall shows that use AI-001 say that prices may change with demand before and after on-sale, and that the price shown at checkout is the total price.
- Email and website price displays show the total price at the time of sending or publishing (POL-01 4.11; P03 G-072, G-073).
- The posted limit wording is changed to match enforcement, or linked-account checks are switched on (P03 G-071).
- The privacy notice rewrite (P01 R-030) describes the bot detection signals and their retention.

**Monitoring:**
- AI-001: weekly pricing review during each on-sale week (price changes, cap and floor hits, accessible seating parity check, complaints), recorded in the change log.
- AI-002: after each protected on-sale, a one-page report with block, challenge, and challenge-failure rates by access type; appeals and releases; and the post-sale linked-account audit.
- Quarterly summary to the General Manager and updates to P01 R-013, R-014, and R-016.

**Evidence retention:** keep AI-002 records of blocked sessions, flagged linked-account orders, and any cancellation decisions for 12 months, which is long enough to support an FTC or state attorney general referral under 15 U.S.C. 45c or Fla. Stat. 817.36(5). Keep other session records no longer than the vendor's 30 days (POL-04 4.7).

**Incident handling:**
- An unauthorized change to pricing or bot settings is a security incident under POL-03 and the P08 runbook (the P08 scenario includes checking for changed prices and bot settings).
- A pricing error (a wrong price, a cap or parity breach) is handled by the Director of Ticketing: pause the module, fix the price, and decide with the Controller and counsel whether to refund the difference. An accessible seating parity breach is always refunded.

**Decommissioning criteria:**
- AI-001 is switched off for all shows if a cap or accessible seating breach happens after the controls in this section are live, if the vendor cannot keep a 12-month price-change log, or if the vendor adds patron-level inputs without notice.
- AI-002 falls back to queue-only mode (no automated blocking) if the mobile network or assistive technology flag is still open after 2 re-measured on-sales and the vendor cannot fix it.

## 6. Decision
**Approve with conditions, both use cases.** General Manager, 2026-08-31. The majority owner approved the related High risk (R-015) treatment the same day.

**AI-001 conditions (items 1 to 3 due before the next Hall on-sale and no later than 2026-09-15):**
1. Floors and ceilings entered for every show on sale, with artist caps as ceilings.
2. Accessible seating price levels removed from auto-apply and checked daily for parity (28 CFR 36.302(f)(3)). The Controller refunds the difference to the buyers affected by the August breach.
3. Approval queue on for changes of more than 25% within 24 hours.
4. "Prices may change with demand" statement on Hall event pages, and total prices in all email and website displays (due 2026-09-30 with P01 R-015).

**AI-002 conditions:**
1. Audio challenge alternative on, and the phone line open during every protected on-sale. Due before the next protected on-sale and no later than 2026-09-30.
2. Published appeal route and a release log for guest services. Due 2026-09-30.
3. Access-type measurement after every protected on-sale, and vendor tuning for mobile networks. Due 2026-11-30 (P01 R-014).
4. Corrected limit wording or linked-account checks by 2026-10-31 (P03 G-071), and linked-account checks plus 12-month retention of block and cancellation evidence by 2026-12-31 (P01 R-013).

**Both use cases:** MFA for all venue users (POAM-003, due 2026-09-30) and change control for pricing and bot settings (POL-01 4.12; POAM-010, due 2026-10-31). The Director of Ticketing reports progress at the quarterly review. The next full re-assessment is due by 2027-08-31, or sooner if an escalation trigger in section 3 is met.
