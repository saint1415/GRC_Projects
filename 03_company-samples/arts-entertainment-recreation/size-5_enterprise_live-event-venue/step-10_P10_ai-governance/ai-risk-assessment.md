# AI Governance Risk Assessment: Enterprise AI Portfolio, Dynamic Ticket Pricing, and Bot Detection

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded live entertainment company; 36 venues in 8 states; in-house ticketing platform) |
| Tier / Vertical | Enterprise / Arts, Entertainment, and Recreation |
| Scope | Enterprise AI portfolio (13 use cases in `ai-use-case-inventory.csv`), with full assessments of AI-001 dynamic ticket pricing (section 7) and AI-002 bot detection and virtual queue (section 8) |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the AI RMF Playbook; the Generative AI Profile (NIST AI 600-1) for AI-007, AI-009, AI-011, and AI-012; repository risk tier rubric |
| Assessor / date | AI governance committee (chaired by the Vice President, Data and AI), meeting of 2026-08-25; GRC team prepared the portfolio review; fieldwork 2026-08-17 to 2026-08-28 |
| Decision | Executive risk committee, 2026-09-10 (section 10) |
| Related | P01 R-009, R-016, R-041 to R-045; P03 G-082, G-084, G-088, G-090; P06 POL-01 4.15, POL-04 4.7 to 4.10, POL-05 4.6; P07 POAM-020 |

## 1. Portfolio summary
| Measure | Result |
|---|---|
| Use cases in the inventory | 13 |
| Risk tier | High 3, Medium 6, Low 4 |
| Status | In production 10, Pilot 1, Paused 1, Suspended 1 |
| Committee review complete | 8 of 13 |
| Not yet reviewed | 5: AI-005, AI-006, AI-010, AI-012, AI-013 (all due 2026-11-30, POAM-020) |
| High-tier use cases without committee review | 3 (AI-005 paused, AI-006 pilot, AI-010 suspended) |
| Use cases that set prices or decide purchase access for patrons | 2 (AI-001, AI-002), both assessed in full below |

**Main findings:** all three High-tier use cases entered through vendor pilots or vendor feature releases before the intake control existed, and none has been reviewed; two are now stopped and one is limited to a 3-arena pilot. The two patron-facing ticketing models work as designed for most buyers but failed two specific tests: accessible seating price parity (AI-001) and accessibility of the bot challenge (AI-002).

## 2. GOVERN: AI governance committee operating model
**Charter.** The AI governance committee was formed in 2025 under POL-01 and reports to the executive risk committee. Its risks roll up to enterprise risk ER-08 (P01), which the board risk committee reviews quarterly.

**Members:** Vice President, Data and AI (chair); Chief Privacy Officer; CISO; Chief Compliance Officer; General Counsel's delegate; Director of Accessibility Compliance; Chief Human Resources Officer (for workforce tools); Vice President, Pricing and Revenue Management; Director of Fraud and Bot Defense; Vice President, Venue Security and Safety (for safety tools). Internal Audit observes. A member does not vote on a use case they own.

**Decision rights by tier:**
| Tier | Who approves | Required before production |
|---|---|---|
| High | Committee vote, then the executive risk committee | Local validation and bias testing on the company's data; impact assessment; legal review for each state of use; human review design; notice to affected people; monitoring plan |
| Medium | Committee vote | Human oversight design; output quality monitoring; AI disclosure where people interact with it; accessibility review for patron-facing tools; privacy and security review |
| Low | Committee chair (fast track) | Approved-tool listing; data handling rules (POL-04) |

**Intake and inventory.** Any new AI use, including AI features switched on inside existing vendor products and modules offered to SL-1 clients, must be registered before use (POL-05 4.6; POL-04 4.7). Since 2026-07, procurement and the change process block AI features without an inventory ID. The GRC team owns the inventory.

**Policies:** POL-01 4.15 (total price display; change control for pricing and bot rules); POL-04 4.7 (privacy and AI review for new uses of patron data), 4.9 (no Restricted data in AI tools), and 4.10 (biometric data only with approval and opt-in consent); POL-05 4.6 (approved tools only); STD-05.3 (approved AI tools list).

**Cadence:** monthly committee meetings; quarterly monitoring review for every High and Medium patron-facing tool; annual re-review of every use case.

## 3. MAP: context and applicable rules
| Rule | Applies? | Why |
|---|---|---|
| FTC Rule on Unfair or Deceptive Fees, 16 CFR Part 464 (N71-R05) | **Yes, AI-001, AI-007, AI-009** | Live-event tickets are a covered good (464.1). Every price offered, displayed, or advertised must include the total price (464.2(a)), shown more prominently than other pricing information (464.2(b)), and fees must not be misrepresented (464.3). The rule does not forbid demand-based pricing, but every dynamic price, every "from" price in AI-written copy, and every fee answer from the support assistant must follow it |
| FTC Act Section 5, 15 U.S.C. 45(a), (n) (N71-R05) | **Yes, all patron-facing tools** | Statements about pricing, posted ticket limits, and AI assistant answers must be accurate; unfair practices include blocking or overcharging patrons in ways they cannot avoid |
| ADA Title III ticketing rules, 28 CFR 36.302(f) | **Yes, AI-001 and AI-002** | Accessible seating may not be priced higher than other tickets in the same section and must be available at all price levels (36.302(f)(3)); patrons with disabilities must have an equal opportunity to buy during the same stages of sale and through the same methods (36.302(f)(1)(ii)); purchase limits must match (36.302(f)(4)); no proof of disability may be required (36.302(f)(8)) |
| BOTS Act, 15 U.S.C. 45c | **Protects the company (AI-002)** | Circumventing a ticket issuer's security measures or posted purchase limits, and selling tickets obtained that way, is unlawful (45c(a)). The FTC enforces it (45c(b)) and state attorneys general may sue (45c(c)). AI-002 records are the evidence for referrals, so retention matters |
| State consumer privacy laws | **Yes, AI-002, AI-005, AI-008** | Profiling and targeted advertising opt-outs and data protection assessments in states where thresholds are met (counsel's list); applied generically, with Florida as the worked example (the Florida Digital Bill of Rights does not apply; P03 G-098) |
| State biometric privacy laws and Fla. Stat. 501.171 | **Yes, AI-005** | Laws differ by state. Florida's breach statute treats biometric data, as defined in Fla. Stat. 501.702, as personal information; 501.702 excludes photographs and data generated from video. Whether face templates computed from gate camera video are biometric data under Florida law is unsettled (counsel to confirm), so the company treats them as biometric data |
| Federal equal employment opportunity law; state AI employment laws | **Yes, AI-010** | Title VII disparate impact liability exists by statute; state AI employment notice and anti-discrimination rules apply in some hiring states (counsel to confirm). An adverse impact analysis is required before any re-enable |
| State AI laws on consequential decisions | **No, today** | Ticket pricing and ticket purchase access are not consequential-decision categories under the repository rubric or the state laws summarized in the cross-sector file. AI-010 (employment) would be, and stays suspended |
| PCI DSS v4.0.1 (N71-R04) | Indirectly | AI-003 uses processor scores, and AI-012 touches payment code, which stays under secure development (Requirement 6.2) and code review |

## 4. Risk tiering
Rubric: `00_universal-framework/projects/step-10_P10_ai-governance/README.md` (repository-defined). High = a substantial factor in a consequential decision about a person (here, employment) or able to affect physical safety.

| ID | Use case | Tier | Status | Committee review |
|---|---|---|---|---|
| AI-001 | Dynamic ticket pricing (11 own venues; 52 SL-1 clients opted in) | Medium | In production | Reviewed 2025-11-18; re-reviewed 2026-08-25 |
| AI-002 | Bot detection and virtual queue for high-demand on-sales | Medium | In production | Reviewed 2025-11-18; re-reviewed 2026-08-25 |
| AI-003 | Payment fraud scoring at checkout | Medium | In production | Reviewed 2026-01-20 |
| AI-004 | Demand forecasting for routing and capacity | Low | In production | Reviewed 2025-12-09 |
| AI-005 | Facial recognition express entry pilot | High | Paused (2 venues) | Not reviewed (due 2026-11-30) |
| AI-006 | Crowd density video analytics on CCTV | High | Pilot (3 arenas) | Not reviewed (due 2026-11-30) |
| AI-007 | Patron support assistant (generative) | Medium | In production | Reviewed 2026-03-17 |
| AI-008 | Marketing audience segmentation | Medium | In production | Reviewed 2026-02-24 |
| AI-009 | Generative marketing copy and images | Low | In production | Reviewed 2026-02-24 |
| AI-010 | Seasonal staff applicant screening and ranking | High | Suspended (ranking disabled) | Not reviewed (due 2026-11-30) |
| AI-011 | Enterprise generative AI assistant | Medium | In production | Reviewed 2026-02-10 |
| AI-012 | Code assistant for engineers | Low | In production | Not reviewed (due 2026-11-30) |
| AI-013 | SOC alert triage assistant | Low | In production | Not reviewed (due 2026-11-30) |

**Tiering notes:** AI-006 is High because a missed crowding alert can affect physical safety, even though staff decide every action. AI-005 is High because it processes biometric data at the gate, where a false non-match delays entry and a breach exposes data that cannot be changed. AI-001 and AI-002 stay Medium because a price per price level and a session decision for one sale are not consequential decisions about a person; the escalation triggers in sections 7.3 and 8.3 would re-tier them.

## 5. Portfolio findings that need action
1. **Unreviewed High-tier tools.** AI-005, AI-006, and AI-010 started through vendor pilots or releases. AI-005 was paused on 2026-07-31 and AI-010's ranking was disabled on 2026-06-30 (P01 R-042 avoided; R-045). AI-006 may continue only in its 3-arena pilot until review.
2. **Client modules.** AI-001 is offered to SL-1 clients as an opt-in module. Clients set their own floors and ceilings, but the company runs the model, so the accessible seating parity control and the total-price display must be enforced by the platform for every client (POL-01 4.15).
3. **Generative tools.** AI-007 must never invent fee or refund terms (AI 600-1 confabulation risk); answers are grounded in approved policy pages, and weekly sampling found 3 incorrect answers in 200 (1.5%), all about transfer deadlines.

## 6. MEASURE: portfolio bias testing plan
| Tool | Metric | Groups compared | Threshold for action |
|---|---|---|---|
| AI-001 dynamic pricing | Accessible seating price minus the lowest current price of other seats in the same section; price paid by channel | Accessible versus other seats; online, app, box office, phone | Any accessible seat priced above the section (zero tolerance); any channel more than 2% above online for the same seat type at the same time |
| AI-002 bot detection | Block and challenge-failure rates | Access type: mobile carrier network, home broadband, VPN or privacy relay, assistive technology (screen reader test) | A group's rate more than 2 times the baseline and more than 1 percentage point above it; any failed screen-reader test |
| AI-003 fraud scoring | Decline and false-positive rates | Billing region; card type | False-positive rate more than 1.5 times the overall rate |
| AI-005 face matching (before any restart) | False non-match and false match rates | Self-reported age band and sex of opt-in volunteers; skin tone scale in controlled tests | Any group's false non-match rate more than 2 times the lowest group |
| AI-010 applicant ranking (before any re-enable) | Selection rate ratios | Sex, race and ethnicity, age 40 and over, where self-reported | Any ratio below 0.8 investigated before use |

**Data limits:** the company does not collect protected characteristics from patrons, so AI-002 uses access type as the measurable proxy and AI-001 uses seat type and channel. For AI-005 and AI-010, testing uses voluntary self-reported data and controlled test sets.

## 7. Full assessment: AI-001 dynamic ticket pricing
### 7.1 MAP
| Item | Description |
|---|---|
| Purpose and intended use | Raise or lower the price of each price level for reserved-seat events as demand changes, within floors and ceilings set per event, to reduce underpriced tickets going to resellers and to fill slow events |
| Where used | Reserved-seat events at 11 own venues (arenas and amphitheaters), about 1,900 events in 2026 H1, and 52 SL-1 clients that opted in. General admission events use fixed prices |
| Users / operators | Pricing analysts set floors and ceilings (artist caps as ceilings); the model applies changes automatically within them |
| Affected people | Every buyer of a reserved seat at those events, including buyers of accessible seating; artists and promoters with price caps; clients using the module |
| Data | Inputs: sales velocity, seats remaining by section, days to event, page views, queue size, floor and ceiling settings. Outputs: a new price per price level and a reason code. **No patron-level data is an input** (confirmed by test in 7.4) |
| Build or buy | Build: in-house model on Cloud provider B, served through the platform pricing service |
| Not intended | Individual prices for different buyers, prices based on a buyer's history or location, and any change to fees. Any of these requires re-assessment |

### 7.2 Risk tier
Medium (section 4). **Escalation triggers (re-tier to High and re-assess):** any patron-level input (history, location, device); extension to fees; accessible price levels returned to automation without the parity control; use for any event type where price affects access to an essential service.

### 7.3 MEASURE (sample of 40 events, 2026 H1, with the price-change log)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Every price stays within the event's floor and ceiling, including artist caps | 1 of 40 events exceeded an artist cap by 6% because the cap was entered after on-sale | **No** |
| Safe | Accessible seating never priced above other seats in the same section; accessible seating at every price level (28 CFR 36.302(f)(3)) | 2 of 40 events had accessible seats priced above the section for 1 and 3 days (P03 G-090). Accessible seating existed at all price levels | **No** |
| Secure and resilient | Pricing rules changed only by named users with MFA through change control; model artifacts signed | Named analyst roles with MFA; rule changes logged; 2 emergency rule changes lacked post-approval | Partial |
| Accountable and transparent | Patrons told prices may change with demand; every displayed price is a total price (16 CFR 464.2) | Own-brand event pages carry the statement; 9 of 52 client templates using AI-001 do not. Checkout totals correct on all templates; base-price displays on 41 client templates (P03 G-084) | **No** |
| Explainable and interpretable | Each price change has a reason code analysts can read | Reason codes for all sampled changes; log kept 13 months | Yes |
| Privacy-enhanced | No patron-level inputs; same price for every buyer at the same time | Test accounts with different purchase histories and locations saw identical prices on 6 events; box office and online prices matched on 30 spot checks | Yes |
| Fair, with harmful bias managed | Section 6 metrics | Channel parity met; accessible seating parity failed (as above) | **No** |

### 7.4 MANAGE
- **Human in the loop:** bounded automation. Changes over 25% within 24 hours go to an analyst approval queue; artist caps must be entered before on-sale and are locked as ceilings; the owner can pause the model for any event.
- **Accessible seating:** accessible price levels come out of automation by 2026-10-15 and are then set daily to no more than the lowest current price of other seats in the same section, with an automated parity check that blocks publication of a breach. Buyers affected by the two breaches receive refunds of the difference (POAM-020).
- **Disclosure:** "prices may change with demand" on every event page that uses AI-001, including client templates (platform-enforced); total prices everywhere (POAM-021).
- **Monitoring:** daily parity check; weekly price-change review per on-sale week; quarterly fairness report to the committee; updates to P01 R-016 and R-017.
- **Incidents:** an unauthorized change to pricing rules is a security incident under POL-03 and the P08 runbook. A pricing error is fixed by pausing the model; accessible seating breaches are always refunded.
- **Decommissioning:** switched off for an event type if a parity or cap breach recurs after these controls are live, if the price-change log cannot be kept for 13 months, or if any patron-level input is added without re-assessment.

## 8. Full assessment: AI-002 bot detection and virtual queue
### 8.1 MAP
| Item | Description |
|---|---|
| Purpose and intended use | Keep automated buying tools out of high-demand on-sales, randomize queue position at on-sale time, and enforce posted ticket limits |
| Where used | About 140 high-demand on-sales a year, for own events and SL-1 clients |
| Users / operators | The edge provider's bot engine and in-house risk models run automatically; the Director of Fraud and Bot Defense sets protection levels per on-sale; guest services can release a blocked patron |
| Affected people | Every patron who joins a protected on-sale (about 2.4 million queue entrants across the 12 on-sales reviewed) |
| Data | Inputs: device and browser signals, network address and type, request timing, account age, and linked-account signals (shared cards and addresses). Outputs: allow, challenge, or block per session, with a reason code. Session records kept 30 days today |
| Build or buy | Configure and build: vendor bot management plus in-house models |
| Not intended | Automatic cancellation of completed orders or permanent account bans; both require human review |

### 8.2 Risk tier
Medium (section 4). **Escalation triggers:** automatic order cancellation or permanent bans; biometric or identity document checks; use outside ticketing.

### 8.3 MEASURE (12 high-demand on-sales, 2026 H1)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Post-sale audit of orders above posted limits across linked accounts | 4 of 12 on-sales had linked-account clusters above the posted limits (about 3,900 tickets in total); the model blocked about 610,000 sessions and challenged about 380,000 | **No** (linked-account checks run after the sale; P03 G-082) |
| Safe | Protected on-sales never stop phone and box office sales | Phone and box office sales ran during all 12 | Yes |
| Secure and resilient | Protection settings changed only by named users with MFA through change control | Met for workforce users; client users of opted-in clients can lower protection on their own events without MFA (POAM-004) | Partial |
| Accountable and transparent | Blocked patrons see a reason and an appeal route; evidence kept long enough for BOTS Act referrals | Own-brand block page has an appeal link; client templates do not. Session records kept 30 days | **No** |
| Explainable and interpretable | Reason codes visible to guest services | Available in the console since 2026-05 | Yes |
| Privacy-enhanced | Signals limited to bot detection; privacy notice describes them | No sale of signals; the privacy notice does not describe bot detection signals (P03 G-081) | Partial |
| Fair, with harmful bias managed | Section 6 metrics; screen-reader test | Challenge failure on mobile carrier networks 3.4% versus 1.0% on home broadband (flagged). VPN or privacy relay 19% (expected bot signal; appeal route needed). Visual-only challenge at 5 of 12 on-sales (audio alternative not enabled for those protection levels); screen-reader test failed on those 5 (P03 G-088) | **No** |

**Bias findings.** Patrons on mobile carrier networks fail the challenge about 3.4 times as often as home broadband users, probably because many phones share one network address; younger patrons and patrons without home internet are most affected. Blind patrons using screen readers could not pass the visual-only challenge at 5 on-sales, which also denies the same stage of sale that 28 CFR 36.302(f)(1)(ii) protects for accessible seating buyers.

### 8.4 MANAGE
- **Human in the loop:** session decisions stay automated because no one can review sessions in real time. Humans handle outcomes: a published appeal route on every template, logged releases by guest services, and human review with documented reasons before any order cancellation for limit breaches.
- **Accessibility:** the audio and accessible challenge alternatives are enabled for every protection level, and the phone line stays open during every protected on-sale (POAM-020, due 2026-12-31).
- **Linked accounts:** real-time linked-account checks at checkout (P01 R-009), with the posted limit wording matched to how limits are enforced (P03 G-082).
- **Evidence retention:** keep records of blocked sessions, flagged linked-account orders, and cancellation decisions for 12 months to support FTC or state attorney general referrals under 15 U.S.C. 45c; keep other session records no longer than 30 days (POL-04 4.5).
- **Monitoring:** a one-page report after each protected on-sale with block, challenge, and failure rates by access type, appeals, releases, and the linked-account audit; quarterly fairness report to the committee; updates to P01 R-009 and R-043.
- **Decommissioning or fallback:** fall back to queue-only mode (no automated blocking) for any template where the mobile network or accessibility flag is still open after 2 re-measured on-sales.

## 9. MANAGE: portfolio controls
- **Monitoring:** every High and Medium patron-facing tool has quarterly performance and fairness metrics (inventory column `monitoring`) reported to the committee; threshold breaches trigger re-review.
- **Incident handling:** AI incidents (unsafe output, bias finding, data misuse, unauthorized change to model settings) are logged as SOC cases and follow P08 where security or patron data is involved.
- **Third parties:** AI vendors are tier-1 in the vendor program; contracts require notice of material model changes and no training on company data.
- **Decommissioning:** tools are retired if they fail monitoring thresholds twice, change data-use terms, or lose committee approval; the inventory records retirement.

## 10. Decisions
The executive risk committee approved these decisions on 2026-09-10, on the committee's recommendation of 2026-08-25:
1. **AI-001:** approved to continue with conditions: accessible price levels out of automation with the automated parity check by 2026-10-15 and refunds by 2026-10-31; caps locked before on-sale; demand-pricing statement and total prices on every template by 2026-11-30 (POAM-020; POAM-021).
2. **AI-002:** approved to continue with conditions: accessible challenge on every protection level and an appeal route on every template by 2026-12-31; real-time linked-account checks and 12-month evidence retention by 2027-03-31; mobile network tuning re-measured at the next 2 high-demand on-sales.
3. **AI-005:** stays paused. Restart requires committee and executive risk committee approval, counsel's review for each venue state, opt-in consent, and the section 6 accuracy tests.
4. **AI-006:** may continue only in the 3-arena pilot, alerts only, until committee review by 2026-11-30 and false-negative testing at gates.
5. **AI-010:** ranking stays disabled until committee review, an adverse impact analysis, and counsel's review for each hiring state.
6. **AI-012 and AI-013:** may continue in current scope until fast-track review by 2026-11-30.
7. **Next full re-assessment** of AI-001 and AI-002: by 2027-08-31, or sooner if an escalation trigger is met.
