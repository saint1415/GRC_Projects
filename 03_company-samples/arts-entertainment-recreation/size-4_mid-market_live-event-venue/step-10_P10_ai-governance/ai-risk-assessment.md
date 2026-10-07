# AI Governance Risk Assessment: AI Use-Case Portfolio

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (live event venue operator with ticketing; private equity-backed; three Florida venues) |
| Tier / Vertical | Mid-Market / Arts, Entertainment, and Recreation |
| Scope | Portfolio of 5 AI use cases (AI-001 to AI-005), inventory in `ai-use-case-inventory.csv`. The registry use case (dynamic ticket pricing and bot detection) is the core: AI-001 and AI-002 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the AI RMF Playbook, with the Generative AI Profile (NIST AI 600-1) for AI-003 and AI-005 |
| Assessors / date | vCISO (lead) and Security Manager (security), General Counsel (privacy and legal), Vice President of Ticketing and Vice President of Marketing and Digital (business), Director of Safety and Security (AI-004), 2026-08-24 to 2026-09-04 |
| Decision | Chief Operating Officer, 2026-09-15; the High-tier decision (AI-004) noted by the CEO |
| Related | P01 R-014 to R-017, R-029 to R-033; P03 G-075, G-076, G-077, G-081, G-083, G-084; P06 POL-01 4.9, 4.11, 4.14, POL-04 4.6, 4.9, POL-05 4.8, STD-05; P07 POAM-026, POAM-027; P08 runbooks; P09 VEN-09 |

## 1. Summary
All five AI uses were switched on by departments without a security, privacy, or legal review (gap 12). None is out of control, but four need conditions before they grow:
- **AI-001, dynamic pricing:** priced accessible seating above parity on 2 of 14 shows reviewed and went above artist price caps on 3 shows.
- **AI-002, bot detection:** blocks screen reader users at the challenge and does not enforce the posted limit across linked accounts.
- **AI-003, the chatbot:** told patrons that accessible seating requires proof of disability, which the ADA ticketing rules forbid, and revealed order details on an order number alone.
- **AI-004, crowd analytics:** undercounts the Amphitheater lawn at night, and its server still had the integrator's default password (found in P07).

| ID | Use case | Risk tier | Decision |
|---|---|---|---|
| AI-001 | Dynamic ticket pricing | Medium | Approve with conditions |
| AI-002 | Bot detection and virtual queue | Medium | Approve with conditions |
| AI-003 | Guest service chatbot (generative) | Medium | Approve with conditions; accessibility answers handed to staff at once |
| AI-004 | CCTV crowd analytics | High | Approve with conditions; advisory only until validated |
| AI-005 | Marketing propensity scoring and generative copy | Low | Approve with conditions |

Tiers: 1 High, 3 Medium, 1 Low.

## 2. GOVERN
- **Accountable owner for the AI program:** the vCISO, with the General Counsel. Each use case has a business owner (inventory).
- **Policies:**
  - POL-01 4.9 (purchasing gate) and 4.14 (AI approval through this process);
  - POL-01 4.11: every price shown or advertised is the total price, and the privacy notice matches practice;
  - POL-04 4.6 (new uses of patron data reviewed first) and 4.9 (retention of bot mitigation records and crowd analytics outputs);
  - POL-05 4.8: approved AI tools only; no Restricted data in AI tools; a person reviews AI content before patrons see it;
  - STD-05 AI use standard (draft, due 2026-12-31).
- **Approved AI tools list:** kept by the Security Manager. It lists AI-001 to AI-005 with their conditions. No general-purpose AI assistant is approved for Confidential data.

### 2.1 Lightweight AI governance process
A mid-market venue company does not need a standing AI committee. It needs a short gate and a monthly rhythm, reusing existing roles.

| Step | What happens | Who | Time |
|---|---|---|---|
| 1. Intake | Any department wanting an AI tool, or an AI feature switched on in an existing tool, submits a one-page intake: purpose, users, people affected, data, vendor, decisions affected | Business owner | 15 minutes |
| 2. Triage | Provisional tier with the P10 rubric; purchasing gate check (POL-01 4.9) | Security Manager | 2 business days |
| 3. Review | **Low:** security and data checklist. **Medium:** plus privacy, consumer protection (fee rule, FTC Act), and accessibility (ADA ticketing rules) review. **High:** full MAP and MEASURE assessment like this one, with a validation and bias plan | Security Manager; General Counsel; business reviewer | Low 1 week; Medium 2 weeks; High 4 weeks |
| 4. Decide | Low: Security Manager. Medium: the **AI review group** (vCISO, General Counsel, Vice President of Ticketing, Vice President of Marketing and Digital, Director of Safety and Security), monthly for 30 minutes. High: the group recommends; the COO decides and informs the CEO | As listed | Monthly |
| 5. Monitor | Owner reports the agreed metrics monthly; incidents go to P08 | Business owner | Ongoing |
| 6. Re-review | Annually, or on a trigger: new feature, model change, new data type, new venue (including the County PAC), or a safety or accessibility event | AI review group | Annual |

**Tier rubric:** the repository rubric in `00_universal-framework/projects/step-10_P10_ai-governance/README.md`. Re-tier triggers are listed per use case in section 4.

## 3. MAP
| Item | AI-001 Pricing | AI-002 Bot detection | AI-003 Chatbot | AI-004 Crowd analytics | AI-005 Marketing |
|---|---|---|---|---|---|
| Purpose | Move price levels with demand within set limits | Keep bots out of high-demand on-sales; enforce limits; randomize the queue | Answer patron questions; look up orders; hand off to staff | Estimate crowd density by zone; alert the command post | Score purchase likelihood; draft campaign copy |
| Where used | Reserved-seat Amphitheater and Music Hall shows (61 since 2025-11) | High-demand on-sales (22 in 12 months) | Website, all venues | Amphitheater and Music Hall since 2026-04 | All email and SMS campaigns |
| Users / operators | Vice President of Ticketing and 3 ticketing supervisors set rules; the module applies prices automatically | Vendor scoring runs automatically; guest services can release blocked patrons | Patrons; guest services takes handoffs | Command post and security supervisors | 6 marketing staff |
| People affected | Every reserved-seat buyer, including accessible seating buyers; artists with price caps | Every patron in a protected on-sale (about 140,000 queue entrants in the 4 on-sales reviewed) | About 9,000 chat sessions a month | Every attendee in covered zones | About 640,000 subscribers |
| Data | Aggregate demand signals; **no patron-level data** (tested) | Device, browser, network, timing, account age | Names, emails, order data, free text including accessibility needs | Live video processed on premises; outputs are counts | Purchase history, engagement, preferences, ZIP code |
| Build or buy | Buy (vendor module) | Buy (vendor module) | Buy (SaaS) | Buy (VMS module) | Buy (platform feature) |
| Generative AI? | No | No | Yes | No | Yes (copy) |

### 3.1 Applicable laws and rules
| Rule | Use cases | Why |
|---|---|---|
| FTC Rule on Unfair or Deceptive Fees, 16 CFR Part 464 (90 FR 2166, effective 2025-05-12) | AI-001, AI-005 | Live-event tickets are covered (464.1). Any price offered, displayed, or advertised must include the total price (464.2(a)), shown more prominently than other pricing information (464.2(b)); fees must not be misrepresented (464.3). The rule does not forbid demand-based pricing, but every dynamic price shown, and every price in generated copy, must be a total price (P03 G-077) |
| FTC Act Section 5, 15 U.S.C. 45(a), (n) (N71-R05) | All | Deception: posted limits that are not enforced as stated (G-076), privacy statements that omit bot detection, the chatbot, and scoring (G-075), wrong chatbot answers. Unfairness: harm patrons cannot avoid |
| ADA Title III ticketing rules, 28 CFR 36.302(f) | AI-001, AI-002, AI-003 | Price parity for accessible seating ((f)(3); G-083); equal opportunity during the same stages of sale and through the same methods ((f)(1)(ii); G-081); multiple tickets up to the posted limit ((f)(4); G-084); accurate identification of accessible seating ((f)(2)); no proof of disability ((f)(8)), which the chatbot contradicted |
| BOTS Act, 15 U.S.C. 45c | AI-002 | Protects the company as a ticket issuer: it is unlawful to circumvent a security measure or access control system a ticket issuer uses to enforce posted purchase limits or order rules, and to sell tickets obtained that way (45c(a)(1)). The FTC and state attorneys general enforce it. AI-002 records are the evidence for a referral |
| Fla. Stat. 817.36(5) | AI-002 | A person who intentionally uses or sells software to circumvent a ticket seller's security measure or access control system is liable to the state for a civil penalty. The resale limits elsewhere in 817.36 apply to resellers, not to the company as original seller |
| Fla. Stat. 501.171 and 501.702 | AI-004 (only if face matching were enabled) | Florida's breach law covers biometric data as defined in 501.702, and 501.702 excludes photographs, video or audio recordings, and data generated from them. Whether face templates computed from CCTV video are biometric data is unsettled; counsel would have to confirm, and the company would treat them as biometric data. Face matching is switched off |
| State AI and surveillance-pricing laws | None today | Ticket prices, on-sale access, guest service, crowd density, and marketing offers are not consequential-decision categories under the repository rubric or Colorado SB26-189, and the company operates only in Florida. Texas TRAIGA (effective 2026-01-01) sets intent-based prohibitions and disclosure duties for government agencies and health care providers only. Some states limit prices set from personal data (for example Connecticut PA 26-64 from 2026-10-01); AI-001 uses no personal data. This assessment did not identify a Florida AI-specific statute for these uses |

## 4. Risk tiers and re-tier triggers
| Use case | Tier | Why this tier | Re-tier triggers |
|---|---|---|---|
| AI-001 | Medium | Not a consequential decision about a person, and the same price for every buyer at a moment; not Low because it sets prices patrons pay, is regulated by the fee rule and the ADA ticketing rules, and acts with no human review today | Any patron-level input; fees in scope; accessible levels back in auto-apply |
| AI-002 | Medium | Blocking a session from one on-sale is not a consequential decision; the patron can still buy at the box office or by phone. Not Low because it makes automated decisions about individual patrons | Automatic order cancellation or permanent bans; biometric or identity document checks |
| AI-003 | Medium | Interacts directly with patrons; staff make refund and accessibility decisions | Chatbot allowed to issue refunds, change seats, or decide accessibility requests |
| AI-004 | **High** | Can affect physical safety (crowd management), which the rubric treats as High even though a person decides every action | Face matching switched on; alerts used to trigger automatic actions (gate closures) |
| AI-005 | Low | Internal marketing use with a person approving every message; no consequential decisions and no sensitive data | Use of sensitive data; automated sending without approval; price personalization |

## 5. MEASURE (by use case)
Fieldwork 2026-08-24 to 2026-09-04. AI-001: price-change logs for 14 reserved-seat shows (March to July 2026; 388 price changes). AI-002: vendor reports for the 4 protected on-sales since 2026-06-01 (including the on-sale observed on 2026-07-15) and a post-sale order audit. AI-003: 40 scripted questions, 10 order-lookup attempts, and 200 sampled transcripts. AI-004: alert logs and supervisor counts at 6 shows. AI-005: 12 campaigns.

| Use case | Trustworthy characteristic | Test or metric | Threshold | Result | Pass? |
|---|---|---|---|---|---|
| AI-001 | Valid and reliable | Prices within each show's floor and ceiling, including artist caps | 100% | Caps never entered; 3 of 14 shows above the artist cap by up to 15% | **No** |
| AI-001 | Safe; fair with harmful bias managed | Accessible seating never priced above other seats in the same section (28 CFR 36.302(f)(3)) | 0 breaches | 2 of 14 shows: accessible seats $9 and $14 above the section for 2 and 4 days | **No** |
| AI-001 | Privacy-enhanced | Same price for every buyer at the same time; no patron-level inputs | Identical prices | Two test accounts (new and long-time, different states) saw identical prices on 5 shows; online and box office matched on 20 checks | Yes |
| AI-001 | Accountable and transparent | Patrons told prices may change; every displayed price is a total price | Both | Event pages show total prices but no statement that prices change; emails show base prices (G-077) | **No** |
| AI-001 | Explainable and interpretable | Reason code for each change visible to the owner | 100% | Reason codes for all 388 changes; vendor log kept 90 days | Yes |
| AI-002 | Valid and reliable | Orders above the posted limit of 8 across linked accounts (shared card or address) | 0 clusters | 41 linked-account clusters bought 1,610 tickets above the limit across 4 on-sales; many were listed for resale within an hour | **No** |
| AI-002 | Fair with harmful bias managed | Challenge-failure rate by access type (mobile carrier, home broadband, VPN or relay, assistive technology); flag a group above 2 times the baseline and more than 1 point above it; screen reader test | No flags; screen reader passes | Mobile carrier 4.1% vs home broadband 1.2% (flagged); screen reader test failed (visual puzzle only; audio alternative switched off) | **No** |
| AI-002 | Accountable and transparent | Blocked patrons see a reason and an appeal route; evidence kept for a BOTS Act referral | Both | "Unusual activity" page with no contact route; 52 complaints, 19 released by hand with no record; records kept 30 days | **No** |
| AI-002 | Safe | Box office and phone sales keep working during protected on-sales | Yes | Worked in all 4 on-sales | Yes |
| AI-003 | Valid and reliable | Correct answers on 40 scripted refund, venue, and accessibility questions | 38 of 40 | 33 of 40 correct: 4 wrong refund answers; 3 accessibility answers wrong, including "proof of disability is required for accessible seating" (contrary to 28 CFR 36.302(f)(8)) | **No** |
| AI-003 | Secure and resilient; privacy-enhanced | Order details shown only after matching the email on file | 0 of 10 disclosures | 2 of 10 attempts revealed order details with an order number alone after a crafted prompt | **No** |
| AI-003 | Accountable and transparent | Patrons told they are talking to an AI; easy handoff to staff | Both | Disclosure banner present; handoff works | Yes |
| AI-003 | Privacy-enhanced | Transcripts kept only as needed; no vendor training on company data | 90 days; contract clause | Vendor default 1 year; contract allows "service improvement" use | **No** |
| AI-004 | Valid and reliable; safe | Zone counts within 10% of supervisor counts; alerts before supervisors call density | Within 10% | Gates and concourses within 7%; Amphitheater lawn undercounted by 18% to 25% after dark | **No** (lawn at night) |
| AI-004 | Secure and resilient | Analytics servers hardened; access only from the security office | All true | Default administrator password found by P07 (changed 2026-08-14); reachable from the corporate segment | **No** |
| AI-004 | Privacy-enhanced | Outputs are counts only; face matching off; video retention 30 days | All true | All true (configuration checked 2026-08-27) | Yes |
| AI-005 | Accountable and transparent | Every generated message shows total prices and is approved before sending | 100% | 12 of 12 approved; 5 of 12 used base prices from the event feed (G-077) | **No** |
| AI-005 | Privacy-enhanced | Inputs limited to purchase and engagement data; privacy notice describes scoring | Both | Inputs limited; notice silent on scoring (G-075) | Partial |

**Bias findings.**
- **Mobile networks (AI-002).** Patrons on mobile carrier networks fail the challenge about 3.4 times as often as home broadband users, probably because many phones share one network address. Younger patrons and patrons without home internet are the most affected. The vendor will tune the network-address signal, and the company will re-measure at the next 2 protected on-sales.
- **Assistive technology (AI-002, AI-003).** A screen reader user cannot pass the visual challenge, which also denies the same stage of sale that 28 CFR 36.302(f)(1)(ii) protects. The chatbot's wrong answer about proof of disability could deter buyers of accessible seating. Both are fixed before the next protected on-sale (section 7).
- **Accessible seating prices (AI-001).** Automatic changes to accessible price levels breached parity within days. Accessible price levels come out of auto-apply.
- **Lighting conditions (AI-004).** Undercounting on the dark lawn is a coverage and lighting problem, not a demographic one, but it hits the zone with the highest density. Until fixed, lawn alerts are not relied on.

## 6. MANAGE
**Human-in-the-loop design:**
- **AI-001:** bounded automation. Prices move only between a floor and a ceiling the Vice President of Ticketing sets for each show, with the artist cap as the ceiling. Changes of more than 25% within 24 hours go to an approval queue. Accessible seating levels are set daily at no more than the lowest current price of other seats in the same section. The module can be paused per show.
- **AI-002:** decisions per session stay automated, because a person cannot review sessions in real time. Humans handle outcomes: a published appeal route, logged releases, and a human review of linked-account evidence before any order cancellation.
- **AI-003:** the chatbot answers general questions only. Order details require a matched email and order number; refunds, exchanges, and every accessibility question go to staff.
- **AI-004:** alerts are advisory. The event commander and the safety lead decide every action; supervisors' counts remain the primary control (P08 event-day runbook).
- **AI-005:** a marketing manager approves every segment and message; prices come from the total-price feed only.

**Monitoring:** owners report the section 5 metrics monthly to the AI review group; AI-004 also gets a quarterly deep dive with the Director of Safety and Security. Results feed P01 R-015, R-016, R-017, R-030, R-032, and R-033.

**Evidence retention:** keep AI-002 records of blocked sessions, flagged linked-account orders, and cancellation decisions for 12 months, long enough to support an FTC or state referral under 15 U.S.C. 45c or Fla. Stat. 817.36(5) (POL-04 4.9). Other session records follow the vendor's 30 days.

**Incident handling:**
- An unauthorized change to pricing, bot, or chatbot settings is a security incident under POL-03 and the P08 runbook.
- A pricing error (cap or parity breach) is handled by the Vice President of Ticketing: pause the module, fix the price, and decide with the Controller and counsel on refunds. A parity breach is always refunded.
- A chatbot disclosure of order data is a privacy incident for the General Counsel to assess.
- An AI-004 failure during a show is handled under the event-day runbook; crowd decisions never wait for the system.

**Decommissioning criteria:**
- AI-001: switched off if a cap or parity breach happens after the conditions are live, or if the vendor adds patron-level inputs without notice.
- AI-002: falls back to queue-only mode if the mobile network or assistive technology flag remains after 2 re-measured on-sales.
- AI-003: switched off if the identity check and the accessibility handoff are not live by 2026-10-31.
- AI-004: removed from the lawn zone if night accuracy is not within 10% after the camera and lighting changes.
- Any tool: stopped if the vendor changes data-use terms or the model without notice.

## 7. Decisions
| Use case | Decision | Conditions and due dates | Decided by |
|---|---|---|---|
| AI-001 | **Approve with conditions** | Floors, ceilings, and artist caps entered for every show on sale; accessible levels out of auto-apply with daily parity checks; refunds to affected buyers; approval queue for large changes (all by 2026-09-30); "prices may change with demand" statement and total prices in all displays (2026-09-30, with POAM-026) | COO, 2026-09-15 |
| AI-002 | **Approve with conditions** | Audio challenge alternative on and the phone line open during protected on-sales (2026-09-30); appeal route and release log (2026-10-31); access-type measurement after every protected on-sale and vendor tuning (2026-11-30); posted limit wording or linked-account checks, and 12-month evidence retention (2026-12-31); wheelchair-space orders up to the posted limit (2026-10-31, G-084) | COO, 2026-09-15 |
| AI-003 | **Approve with conditions** | Accessibility questions handed to staff and the wrong answers corrected in the knowledge base (done 2026-09-08); identity check before order details (2026-10-31); 90-day transcript retention and a no-training clause (2026-12-31); monthly answer testing | COO, 2026-09-15 |
| AI-004 | **Approve with conditions** | Advisory use only; server hardening and access only from the security office (2026-10-31, with POAM-004 and POAM-022); camera and lighting changes and re-validation on the lawn (2026-12-31); face matching stays off, and enabling it would need a new High-tier assessment and counsel review | COO, 2026-09-15; noted by the CEO |
| AI-005 | **Approve with conditions** | Prices only from the total-price feed (2026-09-30); privacy notice describes scoring (2026-10-31) | Security Manager, 2026-09-15 |

The conditions are tracked as POAM-027 (AI governance) and POAM-026 (fee display and accessible seating rules) in P07, and in the risk register. The AI review group holds its first monthly meeting on 2026-10-06. Full re-assessment is due by 2027-09-15, or sooner on any re-tier trigger, and before any use case is extended to the County PAC.
