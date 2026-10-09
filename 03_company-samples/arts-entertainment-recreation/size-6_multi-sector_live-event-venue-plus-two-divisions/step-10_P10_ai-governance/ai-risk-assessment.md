# AI Governance Risk Assessment: Group AI Program | Cris Santos Company Holdings

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (Live Venues, Hotels and Restaurants, Ticketing and Streaming, corporate) |
| Tier / Vertical | Multi-Sector / Arts, Entertainment, and Recreation |
| Scope | The group AI governance program: group standard, the division use-case inventory, and the rules that apply to three priority use cases: dynamic ticket pricing (AI-001), bot detection and virtual queue (AI-002), and the face-based express entry pilot (AI-006) |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the AI RMF Playbook; the Generative AI Profile (AI 600-1) for AI-007 and AI-009 only |
| Assessors / date | Group AI council (chaired by the Group Chief Risk Officer), fieldwork 2026-08-17 to 2026-08-28; presented to the board risk committee 2026-09-15 |
| Inventory | `ai-use-case-inventory.csv` (9 use cases: 1 High, 7 Medium, 1 Low), built from AI tool discovery across procurement, SaaS discovery, the SYS-G1 application list and the TVOP module register (EV-035), module and platform configuration records (EV-038, EV-059, EV-072, EV-074), the face entry pilot records (EV-084), and the P10 fieldwork tests (EV-101 to EV-104). Not established: workforce use of public generative AI tools outside the approved tools (intake open request) |
| Related | P01 GR-04, GR-10, GR-11, GR-17, LV-003, LV-010, LV-011, TS-003, TS-011, TS-013, HO-008; P03 G-071, G-072, G-076, G-077, TS-G37; P06 POL-01 4.12 and 4.14, POL-04 4.6 and 4.7, POL-05 4.7; P07 POAM-020, POAM-022, POAM-026 |

## 1. GOVERN (group program)
### 1.1 Structure
| Body or role | Responsibility |
|---|---|
| Board risk committee | Oversees AI risk as part of cyber and enterprise risk; receives the High-tier list quarterly |
| Group AI council | Group Chief Risk Officer (chair), Group CISO, Group Chief Privacy Officer, Group General Counsel, VP Product, Pricing and Access, VP Ticketing and Box Office, VP Revenue Management, and an accessibility lead. Approves High-tier use cases, re-tiers, and the approved-tools list |
| Division AI owners | Named business owner for each use case (inventory column); run monitoring |
| Group CISO | AI security standard (prompt injection, model supply chain, data leakage) |
| Group Chief Privacy Officer | Personal and biometric data, purposes, notices, client data terms |
| Group General Counsel | Price display standard (16 CFR Part 464), ADA ticketing, client contract terms |
| Group internal audit | Includes High-tier AI controls in the annual assessment from 2027 |

### 1.2 Group AI Standard (adopted 2026-06, under POL-01 4.14; EV-100)
1. **Register before use.** Every AI use case that sets or changes prices, controls access to purchases or venues, uses patron, guest, or subscriber data, or interacts with customers is registered before deployment or material change.
2. **Tier with the repository rubric** (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`), **plus a group rule:** any use case that processes biometric data is High, whatever the rubric says. High tier: council approval, a pre-deployment impact assessment, bias testing, notice to affected people, and quarterly monitoring.
3. **Price rules are product rules.** Any AI that sets a price must keep accessible seating at or below the price of other seats in the same section (28 CFR 36.302(f)(3)), respect contractual caps, and feed only total prices to displays (16 CFR 464.2).
4. **Access rules are product rules.** Any AI that gates a purchase must leave an accessible path during the same stages of sale (28 CFR 36.302(f)(1)(ii)) and a human appeal route.
5. **Client data stays with the client** (POL-04 4.4). No model is trained on a client's patron data unless the client agreement permits it.
6. **Change gate.** A material change (new model, new input type, new decision role, new client offering) triggers re-assessment before release.
7. **Approved tools only** for workforce generative AI (POL-05 4.7).

**Where the program fell short in 2026.** The standard was adopted after AI-001, AI-002, and AI-006 were live. Dynamic pricing was offered to clients without the parity safeguard, the bot challenge's accessible alternative was off by default for new on-sales, and the face entry pilot started without a privacy review (group gap 4). All three are now under conditions (section 6).

## 2. MAP (division use cases and applicable rules)
| ID | Use case | Division | Tier | Status |
|---|---|---|---|---|
| AI-001 | Dynamic ticket pricing (group venues and 310 opt-in clients) | Ticketing and Streaming; Live Venues | Medium | In production with conditions |
| AI-002 | Bot detection and virtual queue | Ticketing and Streaming; Live Venues | Medium | In production with conditions |
| AI-003 | Hotel revenue management | Hotels and Restaurants | Medium | In production; register and review |
| AI-004 | Patron propensity and segmentation | Group | Medium | In production with conditions |
| AI-005 | Streaming recommendations | Ticketing and Streaming | Medium | Approved |
| AI-006 | Face-based express entry pilot | Live Venues | High | Pilot; new enrollments paused |
| AI-007 | Generative customer support assistant | Ticketing and Streaming | Medium | In production |
| AI-008 | Payment fraud and card-testing scoring | Ticketing and Streaming | Medium | Approved |
| AI-009 | Enterprise generative AI assistant pilot | Group | Low | Approved (Internal and Public data) |

### 2.1 AI-001 Dynamic pricing and AI-002 bot detection: rules that apply
| Rule | AI-001 | AI-002 | What it means |
|---|---|---|---|
| 16 CFR Part 464 (N71-R05; effective 2025-05-12) | **Yes** | No | Live-event tickets are a covered good (464.1). Every dynamic price shown, including "from" prices in emails, must be a total price (464.2(a)), more prominent than other pricing (464.2(b)), with fees described accurately (464.3). Demand-based pricing itself is not prohibited |
| FTC Act Section 5, 15 U.S.C. 45(a) (N71-R05) | **Yes** | **Yes** | Statements such as "prices never change after on-sale" or "limit 8 per customer" must match what the modules do (P03 G-071). The privacy notice must describe bot detection signals (POL-04 4.6) |
| ADA Title III, 28 CFR 36.302(f) | **Yes** (f)(3) price parity | **Yes** (f)(1)(ii) same stages and methods | Accessible seats may not be priced above other tickets in the same section and must exist at all price levels. A bot challenge that a screen-reader user cannot pass denies the same stage of sale |
| BOTS Act, 15 U.S.C. 45c | No | **Protects** | Circumventing a ticket issuer's purchase limits or access controls is unlawful (45c(a)(1)). "Ticket issuer" may include the venue operator, the promoter, and an agent for either, so the TVOP's records serve Live Venues and clients as evidence |
| Fla. Stat. 817.36(5) (worked example) | No | **Protects** | Civil penalty for intentionally using or selling software to circumvent a ticket seller's security measures |
| State surveillance-pricing laws (for example Connecticut PA 26-64, from 2026-10-01, per the cross-sector file) | **Not expected** | No | AI-001 uses no personal data (tested in section 4). Counsel reviews before any personalized feature, and for client deployments in states with such laws |
| Colorado SB26-189 and CPPA ADMT rules | No | No | Ticket pricing and on-sale access are not consequential or significant decision categories |
| Client agreements | **Yes** | **Yes** | The product must let clients meet their own ADA and fee duties; the 2024 agreement promises "accessibility-ready" features |

### 2.2 AI-006 Face-based express entry: rules that apply
| Rule | Implication |
|---|---|
| Fla. Stat. 501.171(1)(g)1.a.(VI) and 501.702 (worked example) | A name with biometric data, as defined in 501.702, is personal information for breach notice. 501.702 defines biometric data as automatic measurements of biological characteristics used to identify a person, and excludes physical or digital photographs and video or audio recordings or data generated from them. **Whether face templates computed from gate camera images fall inside or outside that exclusion is unsettled; counsel is to confirm. Until then the group treats them as biometric data** for security, breach notice, and retention |
| Florida Digital Bill of Rights (Fla. Stat. ch. 501, part V; "controller" defined in 501.702) | **Does not apply.** A "controller" must exceed $1 billion in global gross annual revenue **and** (a) earn 50% or more of that revenue from selling online advertisements, (b) operate a consumer smart speaker and voice command service, or (c) operate an app store or digital distribution platform with at least 250,000 applications. The group exceeds $1 billion but meets none of (a) to (c) |
| FTC Act Section 5 (N51-R01) | Notice, consent, and retention statements must match practice; unfairness if templates are kept or shared in ways patrons cannot avoid. The vendor keeps templates 12 months, against the group's 24-hour rule (POL-04 4.7) |
| Other states' biometric laws | The pilot runs only in Florida. Counsel must check each state's law before any expansion (POL-01 4.14) |

### 2.3 Other use cases
- **AI-003 hotel revenue management:** short-term lodging is a covered good under Part 464 (464.1). Rates go to channels that must show the total price, including the $32 resort fee (P03 HO-G25).
- **AI-004 propensity models:** use only registered purposes and group customers' data (POL-04 4.3, 4.4); no identity document numbers (POAM-024); honor opt-outs where state law gives them (N51-R03).
- **AI-007 support assistant:** AI 600-1 risks (confabulation, information security, data privacy). The assistant discloses that it is AI and hands off to people for refunds and account changes.
- **AI-008 fraud scoring:** runs in the CDE under PCI DSS; declines can be appealed through client support.

## 3. Risk tiers
- **High:** AI-006 (group rule: biometric data).
- **Medium:** AI-001, AI-002, AI-003, AI-004, AI-005, AI-007, AI-008. They set prices or gate purchases for customers, or interact directly with customers, but none is a consequential decision in the rubric's categories.
- **Low:** AI-009.

**Re-tier triggers (re-assess as High):** AI-001 uses any patron-level data (purchase history, location, device) to set a price, or sets fees; AI-002 cancels completed orders automatically or bans accounts permanently, or adds identity-document checks; AI-004 is used to decide eligibility for any offer that carries a financial term; AI-007 is allowed to issue refunds.

## 4. MEASURE
Fieldwork 2026-08-17 to 2026-08-28. AI-001: 40 sampled group events from March to August 2026 (about 3,100 price changes) and product telemetry for the 310 opt-in clients. AI-002: vendor-neutral platform reports for 5 group on-sales (about 410,000 queue entrants) and a screen-reader test at each. AI-006: enrollment and gate logs for 61 events.

### 4.1 AI-001 Dynamic pricing
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Every price stays inside the event's floor and ceiling, including caps in artist agreements | Caps were not entered for 2 of 40 events; prices went above the cap by up to 12% | **No** |
| Safe | Accessible seats never priced above other seats in the same section (28 CFR 36.302(f)(3)); accessible seating at every price level | 3 of 40 events had accessible seats above the rest of their section for up to 2 days. 22 of 310 opt-in clients have accessible price levels in auto-apply | **No** |
| Secure and resilient | Pricing rules changed only by named users with MFA, through change control | Workforce users on SYS-G1 with MFA; client users without enforced MFA (POAM-010) | Partial |
| Accountable and transparent | Patrons told prices may change; every advertised price is a total price | TVOP checkout shows total prices. "Prices may change with demand" is missing on event pages at 14 of 27 venues. Emails show base "from" prices (P03 G-072) | **No** |
| Explainable and interpretable | Each price change has a readable reason code | Reason codes for all sampled changes; kept 13 months | Yes |
| Privacy-enhanced | No patron-level inputs; same price for every buyer at the same time | Paired test accounts (new and long-time buyers, different states) saw identical prices on 6 events; box office and online matched on 30 spot checks | Yes |
| Fair, with harmful bias managed | Compare prices paid by channel and by accessible versus other seats in the same section; flag any accessible or channel price above the matching online price for the same seat type at the same time | Channels matched; accessible seating breaches as above | **No** (accessible seating) |

### 4.2 AI-002 Bot detection and virtual queue
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Post-sale audit: orders over the posted limit of 8 across accounts sharing a card or address | 61 linked-account clusters bought about 2,600 tickets over the limit across the 5 on-sales; about 31,000 sessions blocked and 22,000 challenged | **No** (linked accounts not checked; P03 G-071) |
| Safe | Box office and phone sales unaffected during protected on-sales | Unaffected at all 5 | Yes |
| Secure and resilient | Protection level changed only by named users through change control | Workforce changes controlled; client changes self-service | Partial |
| Accountable and transparent | Blocked patrons see a reason and an appeal route; evidence kept long enough for referral | Block page says "unusual activity" with no route; records kept 30 days (BOTS Act and 817.36 referrals need longer) | **No** |
| Explainable and interpretable | Reason code per decision visible to support staff | Visible to client support since 2026-05 | Yes |
| Privacy-enhanced | Signals limited to bot detection; described in the privacy notice | Device and network signals only; notice silent on them | Partial |
| Fair, with harmful bias managed | Challenge failure by access type (mobile carrier network, home broadband, VPN or privacy relay, assistive technology), because no protected characteristics are collected. Flag a group whose rate is more than 2 times the baseline and more than 1 percentage point above it. Screen-reader test of the challenge | Mobile carrier networks 3.4% vs home broadband 1.0% (**flagged**); VPN or privacy relay 19% (expected bot signal; appeal route needed); screen-reader test **failed at 2 of 5** on-sales because the audio alternative is off by default for new on-sales | **No** |

### 4.3 AI-006 Face-based express entry
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | False non-match rate at the gate (target under 2%); false match rate (target 0 in sampled admissions) | 1.9% false non-match; no false matches found in 500 sampled admissions | Yes |
| Fair, with harmful bias managed | False non-match by age band from account birth year (the only demographic held); flag a band more than 2 times the rate of others. Vendor demographic test results requested | 65 and older: 4.8% vs 1.6% for others (**flagged**). Vendor has not provided demographic test results | **No** |
| Privacy-enhanced | Templates deleted within 24 hours of the event (POL-04 4.7); notice describes the feature; consent recorded | Vendor keeps templates 12 months; in-app consent recorded but the privacy notice does not mention face matching | **No** |
| Safe | Opting out or failing a match never blocks entry | Ticket scan always available at the same gate | Yes |
| Secure and resilient | Vendor security assessment and breach notice terms | No assessment; contract has no breach notice clause | **No** |

### 4.4 Other use cases (summary)
| Use case | Metric | Result | Pass? |
|---|---|---|---|
| AI-003 | Rates sent to channels carry the total price | Metasearch and 2 partner channels show rates without the resort fee | **No** (P03 HO-G25) |
| AI-004 | Inputs match registered purposes | Identity document numbers present in the source table (not used by models) | Partial (POAM-024) |
| AI-007 | Wrong policy answers in 400 sampled conversations (target under 2%); prompt injection test (30 attempts) | 2.5% wrong refund answers; no cross-account disclosure | Partial |
| AI-008 | Appeals upheld as share of declines | 0.4% of declines overturned on appeal | Yes |

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** bounded automation. The module changes prices only between a floor and a ceiling entered before on-sale, with any artist cap as the ceiling. A change of more than 25% within 24 hours goes to an approval queue. Accessible seating price levels are removed from auto-apply and set daily at or below the lowest current price of other seats in the same section; for clients this becomes the **product default**, which a client can change only with a written acknowledgment of its ADA duty.
- **AI-002:** per-session decisions stay automated, because no person can review sessions in real time. People handle outcomes: a published appeal route, logged releases, and human review of linked-account evidence before any order is cancelled under the posted purchase terms. The accessible challenge alternative is on by default for every protected on-sale, and box office and phone sales stay open.
- **AI-006:** gate staff can always admit by ticket scan; enrollment is opt-in and withdrawal deletes the template.

**Disclosure:** "prices may change with demand" on every event page that uses AI-001; total prices in all displays (POL-01 4.12); the privacy notice updated for bot detection signals and face matching (POL-04 4.6); AI-007 identifies itself as AI.

**Monitoring:** after each protected on-sale, a one-page AI-002 report (block, challenge, and failure rates by access type; appeals; linked-account audit); weekly AI-001 parity and cap checks for group venues and a monthly client telemetry report; AI-006 false non-match by age band each event. Quarterly High-tier and flagged-metric report to the council and the board risk committee; updates to P01 GR-04, GR-17, LV-003, LV-010, LV-011, TS-003, TS-011.

**Evidence retention:** keep AI-002 records of blocked sessions, linked-account evidence, and cancellation decisions for 12 months to support BOTS Act or Fla. Stat. 817.36(5) referrals; other session records no longer than 30 days (POL-04 4.7).

**Incident handling:** an unauthorized change to pricing or bot settings, or a vendor breach of face templates, is a security incident under POL-03 and P08. A pricing error (cap or parity breach) is handled by the business owner: pause the module for the event, fix the price, and refund the difference to affected buyers; an accessible seating parity breach is always refunded.

**Decommissioning:** AI-001 off for any event where a parity or cap breach recurs after the controls are live; AI-002 falls back to queue-only mode if the accessibility or mobile-network flag stays open after 3 re-measured on-sales; AI-006 ends if the vendor will not accept 24-hour deletion and breach notice terms by 2026-12-31, and all templates are then deleted.

## 6. Decisions
| Use case | Decision | Conditions and dates |
|---|---|---|
| AI-001 dynamic pricing | **Continue with conditions** (council, 2026-08-28; board risk committee informed 2026-09-15) | Accessible levels out of auto-apply at group venues and refunds for the 3 events by 2026-10-15; caps entered as ceilings for every event on sale by 2026-10-15; "prices may change" statement and total prices by 2026-10-31 (POAM-023); product parity safeguard as the client default and release tests by 2026-11-30 (POAM-020, POAM-022) |
| AI-002 bot detection | **Continue with conditions** | Accessible challenge on by default and an appeal route by 2026-11-30; linked-account checks and 12-month evidence retention by 2026-12-31; mobile-network tuning re-measured at the next 3 on-sales (P01 TS-011, LV-010) |
| AI-006 face entry pilot | **Continue for enrolled patrons only; new enrollments paused** | Privacy review, notice update, vendor 24-hour deletion and breach notice terms, and vendor demographic test results by 2026-12-31 (POAM-026); age-band disparity mitigation before any expansion; no new venue or state without council approval |
| AI-003 hotel revenue management | **Continue** | Register in the inventory (done); weekly rate review; total price in channel feeds by 2026-10-31 (POAM-023) |
| AI-004 propensity models | **Continue with conditions** | No identity numbers in sources (POAM-024); no client data (POAM-012); purpose register entries by 2026-12-31 |
| AI-007 support assistant | **Continue** | Monthly sampling; refund answers link to the written policy; target under 2% wrong answers by 2027-01-31 |
| AI-005, AI-008, AI-009 | **Approved** | Standard monitoring; AI-009 prohibited for pricing decisions and Restricted data |

The next full re-assessment of the program is due by 2027-08-31, or sooner if an escalation trigger in section 3 is met.
