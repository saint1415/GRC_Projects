# AI Risk Assessment: Dynamic Pricing Tool (with the Proposed Guest Messaging Assistant)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent 38-unit roadside motel) |
| Tier / Vertical | Micro / Accommodation and Food Services |
| AI use case assessed | AI-001: dynamic pricing tool (SYS-10), publishing rates automatically since 2025-03 |
| Also recorded | AI-002: the PMS vendor's AI guest messaging assistant (proposed, not enabled); AI-003: staff use of public AI chatbots |
| Why not a chatbot | The registry default for this vertical is "revenue-management pricing and guest chatbot." The motel has no guest chatbot. Its AI exposure is the pricing tool, so that is the tier's one use case; the chatbot the PMS vendor offers is recorded with conditions for any future switch-on |
| Framework | NIST AI RMF 1.0 (AI 100-1); the Generative AI Profile (AI 600-1) applies to AI-002 if it is ever enabled |
| Assessor / date | Assistant Manager (Security and Privacy Lead) with the Owner-Manager, 2026-08-20 to 2026-08-21 |
| Decision | Owner-Manager, 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases) |

## 1. GOVERN
- **Accountable owner and decision authority:** the Owner-Manager, who subscribed to the tool and sets rates. A conflict exists: the person who benefits from higher rates also approves the pricing rules. It is compensated by written rules (section 5), the Assistant Manager's monthly review of the change log, and the yearly independent assessment.
- **Policies that apply:**
  - POL-04 4.7: approved AI tools only; the guest messaging add-on must not be switched on without an assessment; no Restricted or Internal data in public AI tools.
  - POL-02 A.5: written terms before any vendor gets motel data or access.
  - POL-02 A.2: a new AI feature is a major change that triggers a risk assessment update.
- **Approved-tools list:** kept by the Assistant Manager in POL-04 4.7. Today it has one entry, the dynamic pricing tool.
- **Scale for a Micro motel:** there is no AI committee. The Owner-Manager and Assistant Manager review AI use at the monthly security meeting.

## 2. MAP
### AI-001 Dynamic pricing tool
| Item | Description |
|---|---|
| Purpose and intended use | Forecast demand by date and room type and set the daily rate, to fill rooms on slow nights and earn more on busy ones |
| Users / operators | Owner-Manager; front desk staff see the resulting rates in the PMS |
| Affected people | Every guest who books (about 5,900 stays a year), including evacuees during hurricanes. Crew accounts are on negotiated rates and are not affected |
| Data | Occupancy, pickup, and rate history from the PMS through an interface; public competitor rates from OTA listings; a local events calendar. **No guest names or contact details** (interface field list checked 2026-08-20) |
| Build or buy | Buy: third-party SaaS for small properties, configured by the Owner-Manager |
| Automation | **Rates publish automatically** to the PMS, which pushes them to the booking engine and 3 OTAs, with no human approval, no ceiling, no floor, and no rule for a declared state of emergency |
| Not intended | Different prices for different guests based on their profile, location, or device (the tool has no such feature) |
| Contract | Subscription terms: the vendor uses only the motel's own data and public listed rates for the motel's recommendations; no pooling of the motel's non-public data with other customers (terms read 2026-08-20) |

### AI-002 AI guest messaging assistant (proposed)
The PMS vendor offers an add-on that answers guest texts and OTA messages with a generative AI model, quotes availability and rates, and drafts replies. The Owner-Manager was offered a free trial in July 2026 and did not start it. It is not enabled.

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| Fla. Stat. 501.160 (unconscionable prices during a declared state of emergency) | **Yes, AI-001** | After the Governor declares a state of emergency, it is unlawful to rent or offer to rent, within the declared area, an essential commodity (which includes services necessary as a direct result of the emergency) or a dwelling unit necessary for habitation as a direct result of the emergency at an unconscionable price (501.160(2)). A gross disparity from the average price in the 30 days before the declaration is prima facie evidence, unless explained by added costs or market trends (501.160(1)(b)). The prohibition lasts up to 60 days under the initial declaration and may be extended by executive order. It is enforced by the state attorney or the Department of Legal Affairs as a violation of s. 501.204 (501.160(7)); there is no private right of action under this section (501.160(6)). The statute does not name motels; Chapter 509 calls the occupancy of a motel unit occupancy of a "dwelling unit" (509.013(12)), so the motel treats its room rates as covered (the cautious reading; counsel to confirm) |
| FTC Rule on Unfair or Deceptive Fees, 16 CFR 464.2 | **Yes, AI-001; AI-002 if enabled** | Every offer or display of a room price must show the total price including the mandatory $6 fee, more prominently than other pricing (464.2(a)-(b)). The tool publishes base rates; the fee must reach every channel as a mandatory fee so the total can be shown. A chat assistant quoting rates would be making price offers |
| FTC Act Section 5, 15 U.S.C. 45(a) and (n) | **Yes, both** | Price displays and chat answers are the motel's representations; pricing practices that cause substantial, unavoidable injury could be unfair |
| Federal antitrust (Sherman Act Section 1, 15 U.S.C. 1) | Watch only, AI-001 | Algorithmic pricing claims against hotels have turned on whether competitors' non-public data are pooled in a shared tool. This tool uses only the motel's own data and public listed rates, so this is a watch item, not a gap. Recheck if the vendor adds a "market benchmark" feature |
| PCI DSS v4.0.1 and Fla. Stat. 501.171 | **AI-002 only** | Guests type card numbers into chats; transcripts would hold card data and personal information, and the vendor would be a third-party agent (501.171(6)(a)) |
| State AI laws (for example Colorado SB26-189) | No | Room pricing is not among the consequential-decision categories, and the motel operates only in Florida |

## 3. Risk tier
**AI-001: Medium** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`). It sets the price every guest pays and acts with no human today, but prices are not individualized and a room rate is not one of the rubric's consequential decisions.

**Escalation (re-tier to High and require human approval for every rate change):**
- a declared state of emergency covering the motel's county, for its full duration;
- any feature that sets different prices for different guests;
- any feature that shares the motel's non-public data with other properties.

**AI-002: Medium if enabled** (interacts directly with guests and makes price statements; no decisions about individuals). **AI-003: Low** when used only with public information; prohibited for anything else.

## 4. MEASURE
The Assistant Manager back-tested the tool's change log from 2025-03-01 to 2026-07-31 and ran rate checks on 2026-08-20.

| Trustworthy characteristic | Test or metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | 14-day occupancy forecast error under 12% | 10.4% average error | Yes |
| Valid and reliable | Published rates stay within a floor and ceiling the Owner-Manager sets | No floor or ceiling existed; 9 nights below the motel's $62 break-even rate | **No** |
| Safe (emergency pricing) | During a declared state of emergency, no rate above the 30-day pre-declaration average without approval | 2025 hurricane evacuation: rates rose 61% above the 30-day average for 2 nights while the county was in a declared emergency | **No.** Flagged |
| Secure and resilient | Vendor security evidence; MFA on the tool account; managed interface credential | Vendor answered a short security questionnaire (no SOC 2 report); MFA available but off; PMS interface credential never changed | Partial |
| Accountable and transparent | Every automatic change logged with its drivers and reviewed | Vendor log exists; nobody reviews it | Partial |
| Explainable and interpretable | Owner-Manager can see why a rate was set | Driver breakdown (demand, competitor rates, events) shown per date | Yes |
| Privacy-enhanced | Only occupancy and rate data leave the PMS | Interface field list: no guest names or contacts | Yes |
| Fee rule (16 CFR 464.2) | Total price including the $6 fee shown on every channel the tool's rates reach | Booking engine shows the total; one of the 3 OTAs showed the base rate in search results because the fee is not mapped as mandatory in its channel feed | **No** |
| Fair, with harmful bias managed | Same room and dates quoted from the booking engine on desktop and phone, logged in and anonymous, English and Spanish pages, and by phone: prices identical | 24 quotes; no unexplained differences | Yes |

**Harm and fairness plan.** The tool cannot single out individual guests, so the main fairness risk is **who bears emergency surges**: evacuees from coastal counties, who often include older travelers and families with few other options. The control is the emergency mode in section 5, tested before each hurricane season. The quote test above is repeated each quarter and after any vendor model update; any unexplained price difference between channels, devices, or languages is a stop-and-investigate event.

## 5. MANAGE
**Human-in-the-loop design (AI-001):**
- Automatic publishing continues only within a floor ($62), a ceiling set each season by the Owner-Manager, and a 15% daily change limit. Anything outside needs the Owner-Manager's approval in the tool, logged with a reason.
- **Emergency mode.** When the Governor declares a state of emergency covering the motel's county, the Assistant Manager switches the tool to manual on the day of the declaration and caps rates at or below the 30-day pre-declaration average for the declared period (up to 60 days, or longer if extended). Any increase needs the Owner-Manager's written cost reason (Fla. Stat. 501.160(1)(b)). The switch is on the hurricane checklist (P01 R-013, R-022).
- The Owner-Manager can override any rate in the PMS at any time.

**Price display (16 CFR Part 464):** map the $6 fee as a mandatory fee in all 3 OTA channel feeds; check the total price on every channel monthly; the roadside sign, website banner, and phone script lead with the total price (P03 G-070, G-071).

**Data protection and security:** MFA on the tool account; rotate the PMS interface credential and add it to the yearly rotation (P03 G-036); no guest identities in the interface, rechecked after any vendor change.

**Monitoring:** the Assistant Manager reviews the tool's change log monthly (floor and ceiling breaches, approvals, emergency-mode periods) and reports at the monthly security meeting. Tracked as P01 R-013 and R-014.

**Incident handling:** a wrong price published at scale, a missed emergency switch, or a fee display failure is logged under POL-03 and corrected the same day; guests overcharged during a declared emergency are refunded the difference.

**Decommissioning:** switch to manual rates (P05 BP-02 tolerates manual pricing indefinitely) if the floor, ceiling, and emergency controls are not working by 2026-10-15, or if the vendor changes its data terms to pool non-public data.

**Conditions for AI-002 before any switch-on:** a new assessment; every rate answer states the total price including the $6 fee; card numbers detected and masked, with a reply that sends a pay-by-link; transcripts kept no more than 90 days; written terms on data use and breach notice (POL-02 A.5); the assistant says it is AI and hands off to staff for bookings changes, complaints, accessibility, and emergencies; English and Spanish answers tested against the same question set before launch.

## 6. Decision
**Approve AI-001 with conditions.** Owner-Manager, 2026-08-31.

The tool may keep publishing automatically **only if**, by 2026-10-15:
1. The floor, ceiling, and 15% daily change limit are set, with approval for anything outside them.
2. Emergency mode is written into the hurricane checklist and tested once with the Assistant Manager.
3. The $6 fee is mapped as mandatory in all 3 OTA feeds and the total price is confirmed on each channel.
4. MFA is on the tool account and the interface credential is rotated.

If any condition is missed, rates go to manual until it is met. **AI-002 is not approved** and stays off until it is assessed against the conditions in section 5. **AI-003** remains prohibited for anything but public information.
