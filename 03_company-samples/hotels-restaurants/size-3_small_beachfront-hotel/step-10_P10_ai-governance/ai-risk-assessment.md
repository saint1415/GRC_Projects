# AI Risk Assessment: Revenue-Management Pricing and Guest Chatbot

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent 140-room beachfront hotel) |
| Tier / Vertical | Small / Accommodation and Food Services |
| AI use cases | AI-001: revenue-management pricing (SYS-12, live since 2024). AI-002: guest chatbot (SYS-13, live since March 2026) |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (AI 600-1) for AI-002 |
| Assessor / date | IT Manager with the Revenue Manager and the Director of Sales and Marketing, 2026-08-17 to 2026-08-21 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases) |

## 1. GOVERN
- **Accountable owners:** Revenue Manager (AI-001); Director of Sales and Marketing (AI-002). **Decision authority:** General Manager (Medium tier). Majority owner for any use case re-tiered High.
- **Policies that apply:**
  - POL-01 4.12: privacy, fee, and rate statements reviewed for accuracy
  - POL-04 4.9: no Restricted data in AI tools without approval and contract terms
  - POL-05 4.10: approved tools only; only named owners change pricing or chatbot settings
  - POL-01 4.10: service provider agreements and annual review
- **Approved-tools list:** kept by the IT Manager. Today: AI-001, AI-002, and the enterprise assistant in AI-003.
- **Scale for a Small hotel:** no AI committee. The General Manager, IT Manager, Revenue Manager, and Director of Sales and Marketing review AI use cases quarterly, and before any new feature is switched on.

## 2. MAP
### AI-001 Revenue-management pricing
| Item | Description |
|---|---|
| Purpose and intended use | Forecast demand by room type and date and recommend daily rates, to raise revenue per available room |
| Users / operators | Revenue Manager; front office reads the resulting rates |
| Affected people | Every guest who books (about 15,700 stays a year) |
| Data | Aggregated bookings and stay history, public competitor rates, events calendar. **The nightly extract also carries guest names, which the model does not need** |
| Build or buy | Buy: vendor SaaS configured by the Revenue Manager |
| Automation | **Recommendations publish automatically** to the PMS, booking engine, and channel manager with no human approval and no floor, ceiling, or emergency rule |
| Not intended | Personalized prices for individual guests based on their profiles, location, or device. This feature exists in the vendor product and is **off**. Enabling it requires re-assessment |
| Contract | Allows the vendor to pool the hotel's non-public rate and occupancy data into a market benchmark shared with other client hotels |

### AI-002 Guest chatbot
| Item | Description |
|---|---|
| Purpose and intended use | Answer common questions (parking, pets, check-in times, amenities), quote availability and rates, and link to the booking engine |
| Users / operators | Guests and prospective guests; marketing staff maintain its answer sources |
| Affected people | About 2,400 conversations a month |
| Data | Guest questions and contact details; transcripts kept by the vendor indefinitely; **23 transcripts found with card numbers typed by guests** |
| Build or buy | Buy (vendor generative model) plus a hotel-built integration in the cloud tenant that reads PMS availability and rates |
| Not intended | Taking payments, changing reservations, answering legal or medical questions, or giving evacuation instructions (hand off to staff) |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| FTC Rule on Unfair or Deceptive Fees, 16 CFR 464.2 and 464.3 (effective 2025-05-12) | **Yes, both** | Short-term lodging is a covered service (464.1). Any offer or display of a price must show the total price, including the mandatory $35 amenity fee, more prominently than other pricing (464.2(a)-(b)). The chatbot quotes the base rate only (**fails**). AI-001 publishes base rates; the hotel must send the amenity fee as a mandatory fee in its feeds so that each channel can show a total price, and its own displays must show it. Fees must not be misrepresented (464.3) |
| FTC Act Section 5, 15 U.S.C. 45(a) and (n) | **Yes, both** | Chatbot answers about policies and prices are representations by the hotel. Pricing practices that cause substantial, unavoidable injury could be unfair |
| Fla. Stat. 501.160 (unconscionable prices during a declared state of emergency) | **Yes, AI-001** | During a Governor-declared state of emergency, renting or offering at an unconscionable price is unlawful in the declared area. A gross disparity from the average price in the 30 days before the declaration is prima facie evidence, unless explained by added costs or market trends. The statute names dwelling units and essential services rather than hotels expressly; the hotel treats its room rates as covered, which is the cautious reading. An automated system that raises rates on evacuation demand is the exact risk |
| Sherman Act Section 1, 15 U.S.C. 1 (algorithmic pricing) | **Litigation risk, AI-001** | In *Cornish-Adebiyi v. Caesars Entertainment, Inc.*, No. 24-3006 (3d Cir. July 29, 2026), the court revived claims that casino-hotels fed non-public pricing and occupancy data into a shared pricing algorithm. In *Gibson v. Cendyn Group, LLC*, No. 24-3576 (9th Cir. Aug. 15, 2025), the court affirmed dismissal where hotels only licensed the same software. Neither binds Florida federal courts (Eleventh Circuit), but the **pooled benchmarking clause** is the fact pattern the Third Circuit found plausible. The hotel will opt out |
| PCI DSS v4.0.1 (3.2.1; 4.2.2) | **Yes, AI-002** | Card numbers typed into chat are stored and sent through end-user messaging outside the approved payment services |
| Fla. Stat. 501.171 | **Yes, AI-002** | Transcripts hold personal information; the chatbot vendor is a third-party agent that must report breaches within 10 days (501.171(6)(a)) |
| State AI laws (e.g., Colorado SB26-189) | No | Room pricing and hotel information are not among the consequential-decision categories, and the hotel operates only in Florida. Other state chatbot or AI disclosure laws were not analyzed (Florida-only scope by decision) |
| FTC proposed AI accuracy policy statement (July 2026) | Watch only | Proposed, not final |

## 3. Risk tier
**AI-001: Medium.** It influences the prices every guest pays and acts without a human today, but prices are not individualized and a room rate is not one of the rubric's consequential decisions. **Escalation triggers (re-tier to High):**
- a declared state of emergency covering the hotel's area (treated as High for its duration: every rate change needs human approval);
- enabling personalized prices based on guest profile, location, device, or browsing;
- connecting any feature that shares non-public hotel data with competitors.

**AI-002: Medium.** It interacts directly with guests and makes price representations, but it makes no decisions about individuals and hands bookings to the booking engine. **Escalation triggers:** taking payments or reservation changes in chat, answering accessibility or emergency questions without handoff, or using transcripts for marketing profiles.

**AI-003: Low.** Internal drafting with no guest data.

## 4. MEASURE
### AI-001 Revenue-management pricing
| Trustworthy characteristic | Test / metric | Result (back-test June 2025 to July 2026) | Pass? |
|---|---|---|---|
| Valid and reliable | 14-day occupancy forecast error under 10% | 8.5% average error | Yes |
| Valid and reliable | Published rates outside a floor and ceiling set by the Revenue Manager | No floor or ceiling existed; 11 days below the Revenue Manager's break-even rate | **No** |
| Safe (emergency pricing) | During a declared state of emergency, no increase above the 30-day pre-declaration average without approval | Back-test of one 2025 declared emergency period: auto-published rates rose 38% above the 30-day average for 3 nights | **No.** Flagged |
| Secure and resilient | Vendor assurance; single sign-on; change log of settings | SOC 2 Type 1 only; local vendor accounts without MFA | Partial |
| Accountable and transparent | Every auto-published change logged with its drivers | Vendor log exists; nobody reviews it | Partial |
| Explainable and interpretable | Revenue Manager can see why a rate was recommended | Driver breakdown available in the vendor dashboard | Yes |
| Privacy-enhanced | Only aggregated data sent to the vendor | Guest names in the nightly extract | **No** |
| Fair, with harmful bias managed | Same room type and dates quoted from 5 locations (Florida, 2 other states, 2 foreign), 3 device types, logged-in and anonymous, English and Spanish site: prices must be identical apart from the disclosed member discount | 60 quotes; no unexplained differences | Yes |
| Competition safeguards | No sharing of non-public hotel data with a pooled benchmark | Contract permits pooling; feature active by default | **No** |

### AI-002 Guest chatbot
| Trustworthy characteristic | Test / metric | Result (August 2026) | Pass? |
|---|---|---|---|
| Valid and reliable | Monthly 50-question test set (policies, amenities, hours); 95% correct | 88% correct (pet fee and cancellation window wrong) | **No** |
| Valid and reliable (fee rule) | Every rate answer states the total price including the amenity fee, before other pricing | 0 of 20 rate answers included the fee | **No** (16 CFR 464.2) |
| Safe | Accessibility, medical, and hurricane questions handed to staff | 7 of 10 handed off; 3 answered from general knowledge | **No** |
| Secure and resilient | Prompt-injection attempts to reveal other guests' data or system instructions | No guest data exposed (the integration reads availability and rates only); system instructions partly revealed | Partial |
| Accountable and transparent | Chatbot says it is an AI assistant at the start and offers a human | Yes, both | Yes |
| Explainable and interpretable | Answers link to the hotel page they come from | 44 of 50 answers linked a source | Yes |
| Privacy-enhanced | Card numbers masked on entry; transcripts kept 90 days | No masking; indefinite retention; 23 transcripts with card numbers | **No** |
| Fair, with harmful bias managed | Same 50 questions in English and Spanish (large share of Florida and Latin American guests). Flag if Spanish accuracy trails English by more than 5 percentage points | English 90%, Spanish 78% | **No.** Disparity flagged |

**Bias and fairness plan (ongoing):**
- AI-001: repeat the 60-quote location, device, and language test each quarter and after any vendor model update. Any unexplained price difference between groups is a stop-and-investigate event.
- AI-002: repeat the English and Spanish test sets monthly. Spanish answers show a handoff offer on every reply until the gap is 5 points or less for two months in a row.

## 5. MANAGE
**Human-in-the-loop design:**
- AI-001: automatic publishing continues only within a floor and ceiling and a 10% daily change limit. Anything outside needs Revenue Manager approval in the vendor tool. **Emergency mode:** when the Governor declares a state of emergency covering the hotel's county, the Revenue Manager freezes rates at or below the 30-day pre-declaration average for the declared period; increases need General Manager approval with a written cost reason (Fla. Stat. 501.160).
- AI-002: staff take over any booking change, complaint, accessibility, medical, or emergency question. Staff review 50 transcripts a week.

**Price display (16 CFR Part 464):**
- The chatbot integration adds the amenity fee to every nightly rate and states the total first; taxes and the final amount are shown by the booking engine before payment.
- Rate feeds from AI-001 carry the amenity fee as a mandatory fee so channels can show total price.
- The Director of Sales and Marketing checks 20 chatbot rate answers and all website rate displays monthly.

**Data protection:**
- Card-number detection and masking in chat, with a reply that directs guests to the booking engine; purge the 23 transcripts; 90-day transcript retention in the contract (POAM-022, POAM-023).
- Remove guest names from the AI-001 extract.
- Opt out of pooled benchmarking and confirm in writing that past pooled data will not be used further.

**Monitoring:** monthly AI report to the General Manager: AI-001 exceptions, floor and ceiling breaches, emergency-mode events; AI-002 accuracy, fee compliance, language gap, handoffs. Tracked as P01 R-011, R-012, R-013, R-029, R-030.

**Incident handling:** a wrong price published at scale, a fee-rule failure, or a chatbot data exposure is logged under POL-03; card numbers exposed through the chatbot follow P08.

**Decommissioning:**
- AI-001: switch to manual rates (P05 BP-09 tolerates 72 hours) if emergency controls fail, or if the vendor will not remove the pooling clause by 2026-10-31.
- AI-002: turn off rate quoting (keep FAQ answers) if total price is not live by 2026-09-30; turn the chatbot off if card masking is not live by 2026-10-31.

## 6. Decision
**Approve both with conditions.** General Manager, 2026-08-31.

AI-001 may keep publishing automatically **only if**, by 2026-10-15:
1. Floor, ceiling, and 10% daily change limits are set, with approval for anything outside them.
2. Emergency mode is documented and tested with the Revenue Manager and General Manager.
3. Pooled benchmarking is switched off, and counsel has reviewed the contract.
4. Guest names are removed from the nightly extract.

AI-002 may keep running **only if**:
1. Every rate answer states the total price including the amenity fee by 2026-09-30 (16 CFR 464.2), and the fee description is corrected (464.3).
2. Card-number masking, purge of existing transcripts, and 90-day retention are in place by 2026-10-31.
3. Accessibility, medical, and hurricane questions always hand off to staff by 2026-09-30.
4. Spanish answers carry a handoff offer until the language gap closes.

Any new AI feature (personalized pricing, payments in chat, reservation changes) requires a new assessment before it is switched on.
